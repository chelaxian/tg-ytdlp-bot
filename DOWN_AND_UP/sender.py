# @reply_with_keyboard
from pyrogram import enums
from pyrogram.errors import FloodWait, UserIsBlocked
from pyrogram.types import ReplyParameters, InputPaidMediaVideo
from HELPERS.app_instance import get_app
from HELPERS.logger import logger
from HELPERS.logger import get_log_channel
from HELPERS.download_status import progress_bar
from HELPERS.limitter import TimeFormatter, humanbytes
from HELPERS.caption import truncate_caption
from DOWN_AND_UP.ffmpeg import get_video_info_ffprobe
import os
import subprocess
import json
from HELPERS.safe_messeger import safe_forward_messages, safe_send_message, safe_edit_message_text
from URL_PARSERS.thumbnail_downloader import download_thumbnail
from CONFIG.config import Config
from CONFIG.messages import Messages, safe_get_messages
from CONFIG.limits import LimitsConfig
import time
import threading

# Get app instance for decorators
app = get_app()

# Dictionary to track active uploads for logging
_active_uploads = {}
_active_uploads_lock = threading.Lock()

_user_blocked_flag = set()

def _start_upload_logging(user_id, msg_id):
    """Start logging upload activity to prevent watchdog false positives"""
    stop_event = threading.Event()
    key = (user_id, msg_id)
    
    with _active_uploads_lock:
        _active_uploads[key] = stop_event
    
    def upload_logger():
        while not stop_event.is_set():
            logger.info("[Upload] Uploading video to Telegram")
            # Wait 10 seconds or until stop event
            stop_event.wait(10.0)
    
    thread = threading.Thread(target=upload_logger, daemon=True)
    thread.start()
    return stop_event

def _stop_upload_logging(user_id, msg_id):
    """Stop logging upload activity"""
    key = (user_id, msg_id)
    with _active_uploads_lock:
        if key in _active_uploads:
            stop_event = _active_uploads[key]
            stop_event.set()
            del _active_uploads[key]

def mark_user_blocked(user_id):
    _user_blocked_flag.add(user_id)

def is_user_blocked_flagged(user_id):
    return user_id in _user_blocked_flag

def clear_user_blocked_flag(user_id):
    _user_blocked_flag.discard(user_id)

# Import function to get user args
def get_user_args(user_id: int):
    """Get user's saved args settings"""
    messages = safe_get_messages(user_id)
    import os
    import json
    user_dir = os.path.join("users", str(user_id))
    args_file = os.path.join(user_dir, "args.txt")
    
    if not os.path.exists(args_file):
        return {}
    
    try:
        with open(args_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(safe_get_messages(user_id).SENDER_ERROR_READING_USER_ARGS_MSG.format(user_id=user_id, error=e))
        return {}

def send_videos(
    message,
    video_abs_path: str,
    caption: str,
    duration: int,
    thumb_file_path: str,
    info_text: str,
    msg_id: int,
    full_video_title: str,
    tags_text: str = '',
    skip_size_check: bool = False,
    video_quality_codec: str = '',
    paid_star_count: int = 0,
):
    class PaidMediaSendError(RuntimeError):
        """Paid NSFW media failed to send.

        This must be treated as a hard stop: never fallback to free media.
        """

    import re
    import os
    user_id = message.chat.id
    messages = safe_get_messages(user_id)
    text = message.text or ""
    m = re.search(r'https?://[^\s\*]+', text)
    video_url = m.group(0) if m else ""
    temp_desc_path = os.path.join(os.path.dirname(video_abs_path), "full_description.txt")
    was_truncated = False

    # Validate file exists and is readable before attempting to send
    if not os.path.exists(video_abs_path):
        logger.error(f"File not found before sending: {video_abs_path}")
        from HELPERS.logger import send_error_to_user
        send_error_to_user(message, messages.ERROR_SENDING_VIDEO_MSG.format(error=f"File not found: {os.path.basename(video_abs_path)}"))
        return None
    file_size = os.path.getsize(video_abs_path)
    if file_size == 0:
        logger.error(f"File is empty (0 bytes) before sending: {video_abs_path}")
        from HELPERS.logger import send_error_to_user
        send_error_to_user(message, messages.ERROR_SENDING_VIDEO_MSG.format(error=f"File is empty (0 bytes): {os.path.basename(video_abs_path)}"))
        return None
    logger.info(f"File validated before sending: {video_abs_path} ({humanbytes(file_size)})")
    
    # --- ASCII-safe path rename for Pyrogram compatibility ---
    # Pyrogram's send_video uses os.path.isfile() which may fail for paths
    # containing non-ASCII characters (accents, diacritics) on some Linux systems.
    # If the path contains non-ASCII chars, rename to a safe temp name and
    # rename back in the finally block after sending.
    _original_video_path_for_rename = None  # set only if renamed
    _original_filename_before_rename = os.path.basename(video_abs_path)  # preserve for file_name param
    try:
        video_abs_path.encode('ascii')
    except UnicodeEncodeError:
        _ascii_safe_name = f"_tg_send_{int(time.time() * 1000)}_{os.getpid()}{os.path.splitext(video_abs_path)[1]}"
        _ascii_safe_path = os.path.join(os.path.dirname(video_abs_path), _ascii_safe_name)
        try:
            os.rename(video_abs_path, _ascii_safe_path)
            logger.info(f"Renamed to ASCII-safe path for Pyrogram: {video_abs_path} -> {_ascii_safe_path}")
            _original_video_path_for_rename = video_abs_path
            video_abs_path = _ascii_safe_path
        except Exception as _rename_err:
            logger.warning(f"Failed to rename to ASCII-safe path (will try sending anyway): {_rename_err}")
    
    # Initialize send_as_file flag (may be set to True by remux fallback below)
    send_as_file = False

    # Convert unsupported formats to MP4 before sending.
    # Telegram doesn't support FLV, some TS variants — remux via ffmpeg.
    unsupported_extensions = ('.flv', '.f4v')
    if video_abs_path.lower().endswith(unsupported_extensions):
        try:
            mp4_path = os.path.splitext(video_abs_path)[0] + "_remuxed.mp4"
            if not os.path.exists(mp4_path):
                logger.info(f"Remuxing unsupported format ({os.path.splitext(video_abs_path)[1]}) to MP4: {video_abs_path}")
                import subprocess
                result = subprocess.run(
                    ['ffmpeg', '-y', '-i', video_abs_path, '-c', 'copy', '-movflags', '+faststart', mp4_path],
                    capture_output=True, text=True, timeout=120
                )
                if result.returncode == 0 and os.path.exists(mp4_path):
                    logger.info(f"Remuxed successfully: {mp4_path} ({humanbytes(os.path.getsize(mp4_path))})")
                    video_abs_path = mp4_path
                else:
                    logger.warning(f"Remux failed (code {result.returncode}), will try sending as document: {result.stderr[:200]}")
                    send_as_file = True  # Fallback to document send
            else:
                logger.info(f"Using existing remuxed file: {mp4_path}")
                video_abs_path = mp4_path
        except Exception as remux_err:
            logger.warning(f"Remux error, falling back to document send: {remux_err}")
            send_as_file = True
    
    # Check if user has send_as_file enabled
    user_args = get_user_args(user_id)
    send_as_file = send_as_file or user_args.get("send_as_file", False)
    
    # Check file size before sending (Telegram limit: 2000 MiB)
    # If file is too large, split it into parts
    # Skip check if this is already a split part (to avoid infinite recursion)
    if not skip_size_check:
        TELEGRAM_MAX_SIZE_MIB = 2000
        TELEGRAM_MAX_SIZE_BYTES = TELEGRAM_MAX_SIZE_MIB * 1024 * 1024
        video_to_send = video_abs_path
        original_video_path = video_abs_path
        
        try:
            if os.path.exists(video_abs_path):
                file_size = os.path.getsize(video_abs_path)
                if file_size > TELEGRAM_MAX_SIZE_BYTES:
                    logger.info(f"File too large ({file_size / (1024 * 1024):.2f} MiB), splitting into parts...")
                    # Get video duration for splitting
                    try:
                        _, _, video_duration = get_video_info_ffprobe(video_abs_path)
                        video_duration = int(video_duration) if video_duration else duration
                    except Exception:
                        video_duration = duration if duration else 0
                    
                    # Split video into parts
                    from DOWN_AND_UP.ffmpeg import split_video_2
                    video_dir = os.path.dirname(video_abs_path)
                    video_name = os.path.splitext(os.path.basename(video_abs_path))[0]
                    
                    split_result = split_video_2(
                        video_dir,
                        video_name,
                        video_abs_path,
                        file_size,
                        TELEGRAM_MAX_SIZE_BYTES,
                        video_duration,
                        user_id
                    )
                    
                    part_paths = split_result.get("path", [])
                    part_captions = split_result.get("video", [])
                    
                    if not part_paths:
                        logger.error("Failed to split video into parts")
                        messages = safe_get_messages(user_id)
                        safe_send_message(
                            user_id,
                            messages.SENDER_FILE_SPLIT_FAILED_MSG.format(size_mib=file_size / (1024 * 1024)),
                            reply_parameters=ReplyParameters(message_id=message.id),
                            message=message
                        )
                        return None
                    
                    # Send each part separately
                    logger.info(f"Sending {len(part_paths)} parts of split video")
                    sent_parts = []
                    for i, part_path in enumerate(part_paths):
                        if not os.path.exists(part_path):
                            logger.warning(f"Part {i+1} does not exist: {part_path}")
                            continue
                        
                        part_size = os.path.getsize(part_path)
                        # If part is still too large, split it again recursively
                        if part_size > TELEGRAM_MAX_SIZE_BYTES:
                            logger.warning(f"Part {i+1} is still too large ({part_size / (1024 * 1024):.2f} MiB), splitting again...")
                            try:
                                _, _, part_duration = get_video_info_ffprobe(part_path)
                                part_duration = int(part_duration) if part_duration else 0
                                
                                part_name = os.path.splitext(os.path.basename(part_path))[0]
                                part_split_result = split_video_2(
                                    video_dir,
                                    part_name,
                                    part_path,
                                    part_size,
                                    TELEGRAM_MAX_SIZE_BYTES,
                                    part_duration,
                                    user_id
                                )
                                
                                # Send recursively split parts
                                messages = safe_get_messages(user_id)
                                for sub_part_idx, sub_part_path in enumerate(part_split_result.get("path", [])):
                                    if os.path.exists(sub_part_path):
                                        subpart_num = sub_part_idx + 1
                                        part_text = messages.SENDER_VIDEO_SUBPART_MSG.format(part_num=i+1, subpart_num=subpart_num)
                                        sub_part_caption = f"{caption} ({part_text})"
                                        try:
                                            send_videos(
                                                message,
                                                sub_part_path,
                                                sub_part_caption,
                                                duration,
                                                thumb_file_path,
                                                info_text,
                                                msg_id,
                                                full_video_title,
                                                tags_text,
                                                skip_size_check=True,  # Skip size check for sub-parts
                                                video_quality_codec=video_quality_codec,
                                            )
                                            sent_parts.append(sub_part_path)
                                        except Exception as send_error:
                                            logger.error(f"Error sending sub-part {sub_part_path}: {send_error}")
                                
                                # Clean up intermediate part file
                                try:
                                    if os.path.exists(part_path):
                                        os.remove(part_path)
                                except Exception:
                                    pass
                            except Exception as split_error:
                                logger.error(f"Error splitting part {i+1} again: {split_error}")
                                # Try to send as document if splitting fails
                                try:
                                    messages = safe_get_messages(user_id)
                                    part_text = messages.SENDER_VIDEO_PART_MSG.format(part_num=i+1)
                                    part_caption = f"{caption} ({part_text})"
                                    send_videos(
                                        message,
                                        part_path,
                                        part_caption,
                                        duration,
                                        thumb_file_path,
                                        info_text,
                                        msg_id,
                                        full_video_title,
                                        tags_text,
                                        skip_size_check=True,  # Skip size check for parts
                                        video_quality_codec=video_quality_codec,
                                    )
                                    sent_parts.append(part_path)
                                except Exception:
                                    pass
                        else:
                            # Send part normally
                            messages = safe_get_messages(user_id)
                            part_text = messages.SENDER_VIDEO_PART_OF_MSG.format(part_num=i+1, total_parts=len(part_paths))
                            part_caption = f"{caption} ({part_text})"
                            try:
                                send_videos(
                                    message,
                                    part_path,
                                    part_caption,
                                    duration,
                                    thumb_file_path,
                                    info_text,
                                    msg_id,
                                    full_video_title,
                                    tags_text,
                                    skip_size_check=True,  # Skip size check for parts
                                    video_quality_codec=video_quality_codec,
                                )
                                sent_parts.append(part_path)
                            except Exception as send_error:
                                logger.error(f"Error sending part {i+1}: {send_error}")
                    
                    if sent_parts:
                        logger.info(f"Successfully sent {len(sent_parts)} parts of split video")
                        # Clean up original file if all parts were sent
                        try:
                            if os.path.exists(original_video_path) and len(sent_parts) == len(part_paths):
                                os.remove(original_video_path)
                        except Exception:
                            pass
                        return None  # Parts were sent separately
                    else:
                        logger.error("Failed to send any parts of split video")
                        return None
        except Exception as size_check_error:
                logger.warning(f"Error checking/splitting file size: {size_check_error}")
                # Continue with normal send if splitting fails

    # --- Define the size of the preview/video ---
    width = None
    height = None
    # Безопасная проверка домена через urlparse
    is_youtube = False
    if video_url:
        try:
            from urllib.parse import urlparse
            parsed_url = urlparse(video_url)
            url_hostname = (parsed_url.hostname or '').lower()
            is_youtube = url_hostname in ('youtube.com', 'www.youtube.com', 'youtu.be', 'www.youtu.be') or \
                        url_hostname.endswith('.youtube.com') or url_hostname.endswith('.youtu.be')
        except Exception:
            pass
    
    # Determine actual video dimensions via ffprobe for ALL sources
    # (YouTube videos can be vertical even without /shorts/ in URL)
    try:
        width, height, _ = get_video_info_ffprobe(video_abs_path)
        logger.info(f"Video dimensions from ffprobe: {width}x{height}")
    except Exception as e:
        logger.error(safe_get_messages(user_id).SENDER_FFPROBE_BYPASS_ERROR_MSG.format(video_path=video_abs_path, error=e))
        import traceback
        logger.error(traceback.format_exc())
        width, height = 0, 0
    is_shorts = is_youtube and ('/shorts/' in video_url or 'youtube.com/shorts/' in video_url)

    try:
        # Logic simplified: use tags that were already generated in down_and_up.
        # Use original title for caption, but truncated description
        title_html, pre_block, blockquote_content, tags_block, link_block, was_truncated = truncate_caption(
            title=caption,  # Original title for caption
            description=full_video_title,  # Full description to be truncated
            url=video_url,
            tags_text=tags_text,  # Use final tags for calculation
            max_length=1000,  # Reduced for safety
            user_id=user_id,
            quality_codec_suffix=video_quality_codec,
        )
        # Define spoiler flag for porn-tagged content
        try:
            is_spoiler = bool(re.search(r"(?i)(?:^|\s)#nsfw(?:\s|$)", tags_text or ""))
        except Exception:
            is_spoiler = False
        # Флаг: было ли отправлено как платное медиа
        was_paid = False
        # Form HTML caption: title outside the quote, timecodes outside the quote, description in the quote, tags and link outside the quote
        cap = ''
        if title_html:
            cap += title_html + '\n\n'
        if pre_block:
            cap += pre_block + '\n'
        cap += f'<blockquote expandable>{blockquote_content}</blockquote>\n'
        if tags_block:
            cap += tags_block
        cap += link_block

        def _should_generate_cover(video_path: str, duration_seconds: int) -> bool:
            try:
                size_mb = os.path.getsize(video_path) / (1024 * 1024)
            except Exception:
                size_mb = 0.0
            try:
                dur = float(duration_seconds or 0)
            except Exception:
                dur = 0.0
            # Generate unless both duration<60 and size<10
            return (dur >= 60.0) or (size_mb >= 10.0)

        def _gen_thumb(video_path: str) -> str | None:
            try:
                if not _should_generate_cover(video_path, duration):
                    return None
                base_dir = os.path.dirname(video_path)
                base_name = os.path.splitext(os.path.basename(video_path))[0]
                thumb_path = os.path.join(base_dir, base_name + '.__tgthumb.jpg')
                if os.path.exists(thumb_path) and os.path.getsize(thumb_path) > 0:
                    return thumb_path
                middle_sec = max(1, int(duration) // 2 if isinstance(duration, int) else 1)
                subprocess.run([
                    'ffmpeg','-y','-ss', str(middle_sec), '-i', video_abs_path,
                    '-vframes','1','-vf','scale=320:-1', thumb_path
                ], capture_output=True, text=True, timeout=30)
                return thumb_path if os.path.exists(thumb_path) and os.path.getsize(thumb_path) > 0 else None
            except Exception:
                return None

        def _detect_crop(src_path: str) -> str | None:
            """Run cropdetect to find non-black region, returns crop filter string or None."""
            import subprocess as _sp  # local import — _sp is not visible from _thumb_fit_ar scope
            try:
                r = _sp.run([
                    'ffmpeg', '-i', src_path,
                    '-vf', 'cropdetect=limit=24:round=2:reset=0',
                    '-frames:v', '5', '-f', 'null', '-'
                ], capture_output=True, text=True, timeout=15)
                # Parse last crop= line from stderr
                crops = re.findall(r'crop=(\d+:\d+:\d+:\d+)', r.stderr)
                if crops:
                    return crops[-1]
            except Exception:
                pass
            return None

        def _thumb_fit_ar(src_path: str, dest_path: str, target_w: int, target_h: int) -> bool:
            """Crop black bars from thumbnail, then scale+pad to match target aspect ratio."""
            import subprocess as _sp  # needed due to nested function scope
            try:
                filters = []
                # Step 1 — crop black bars if detected
                crop_str = _detect_crop(src_path)
                if crop_str:
                    filters.append(f'crop={crop_str}')
                # Step 2 — scale so the image fits inside target dims, preserving AR
                filters.append(f'scale={target_w}:{target_h}:force_original_aspect_ratio=decrease')
                # Step 3 — pad to exact target dims with black
                filters.append(f'pad={target_w}:{target_h}:(ow-iw)/2:(oh-ih)/2:color=black')
                vf = ','.join(filters)
                r = _sp.run([
                    'ffmpeg', '-y', '-i', src_path,
                    '-vf', vf, '-vframes', '1', '-q:v', '4', dest_path
                ], capture_output=True, text=True, timeout=30)
                if r.returncode != 0:
                    logger.warning(f"_thumb_fit_ar ffmpeg failed (rc={r.returncode}): {r.stderr[:300]}")
                logger.info(f"_thumb_fit_ar: vf={vf}, exists={os.path.exists(dest_path)}")
                return os.path.exists(dest_path) and os.path.getsize(dest_path) > 0
            except Exception as e:
                logger.warning(f"_thumb_fit_ar error: {e}")
                return False

        def _resize_to_cover(src_path: str, dest_path: str) -> bool:
            """Resize for paid media cover (320×320 square)."""
            try:
                return _thumb_fit_ar(src_path, dest_path, 320, 320)
            except Exception:
                return False

        def _gen_paid_cover(video_path: str) -> str | None:
            try:
                base_dir = os.path.dirname(video_path)
                base_name = os.path.splitext(os.path.basename(video_path))[0]
                cover_path = os.path.join(base_dir, base_name + '.__tgcover_paid.jpg')
                if os.path.exists(cover_path) and os.path.getsize(cover_path) > 0:
                    return cover_path
                # 1) Try downloading external thumbnail
                try:
                    tmp_dl = os.path.join(base_dir, base_name + '.__ext_thumb.jpg')
                    if video_url:
                        if download_thumbnail(video_url, tmp_dl):
                            if _resize_to_cover(tmp_dl, cover_path):
                                try:
                                    if os.path.exists(tmp_dl):
                                        os.remove(tmp_dl)
                                except Exception:
                                    pass
                                return cover_path
                    try:
                        if os.path.exists(tmp_dl):
                            os.remove(tmp_dl)
                    except Exception:
                        pass
                except Exception:
                    pass
                # 2) Fallback: use passed-in thumb_file_path (already downloaded by down_and_up)
                if thumb_file_path and os.path.exists(thumb_file_path) and os.path.getsize(thumb_file_path) > 0:
                    if _resize_to_cover(thumb_file_path, cover_path):
                        logger.info(f"Using passed-in thumbnail for paid cover: {thumb_file_path}")
                        return cover_path
                # 3) Last resort: extract frame from video (only for large/long videos)
                if _should_generate_cover(video_path, duration):
                    try:
                        tmp_frame = os.path.join(base_dir, base_name + '.__frame.jpg')
                        middle_sec = max(1, int(duration) // 2 if isinstance(duration, int) else 1)
                        subprocess.run([
                            'ffmpeg','-y','-ss', str(middle_sec), '-i', video_path,
                            '-vframes','1','-q:v','4', tmp_frame
                        ], capture_output=True, text=True, timeout=30)
                        if os.path.exists(tmp_frame) and os.path.getsize(tmp_frame) > 0:
                            if _resize_to_cover(tmp_frame, cover_path):
                                try:
                                    if os.path.exists(tmp_frame):
                                        os.remove(tmp_frame)
                                except Exception:
                                    pass
                                return cover_path
                        try:
                            if os.path.exists(tmp_frame):
                                os.remove(tmp_frame)
                        except Exception:
                            pass
                    except Exception:
                        pass
                return cover_path if os.path.exists(cover_path) and os.path.getsize(cover_path) > 0 else None
            except Exception:
                return None

        def _thumb_crop_center(src_path: str, dest_path: str, target_w: int, target_h: int) -> bool:
            """Crop thumbnail to fill target dimensions (center crop, no padding)."""
            import subprocess as _sp
            try:
                filters = []
                filters.append(f'scale={target_w}:{target_h}:force_original_aspect_ratio=increase')
                filters.append(f'crop={target_w}:{target_h}')
                vf = ','.join(filters)
                r = _sp.run([
                    'ffmpeg', '-y', '-i', src_path,
                    '-vf', vf, '-vframes', '1', '-q:v', '4', dest_path
                ], capture_output=True, text=True, timeout=30)
                if r.returncode != 0:
                    logger.warning(f'_thumb_crop_center ffmpeg failed (rc={r.returncode}): {r.stderr[:300]}')
                return os.path.exists(dest_path) and os.path.getsize(dest_path) > 0
            except Exception as e:
                logger.warning(f'_thumb_crop_center error: {e}')
                return False

        def _resize_to_thumb_free(src_path: str, dest_path: str) -> bool:
            """Resize for free video thumbnail, matching the video's aspect ratio.

            Telegram thumbnail limits: width <= 320, height <= 320.
            For horizontal videos (landscape): fit width to 320.
            For vertical videos (portrait): fit height to 320.
            Both dimensions always stay within 320x320.
            """
            try:
                tw, th = 320, 180  # default 16:9
                vw, vh, ar = 0, 0, 1.0  # safe defaults in case ffprobe returned 0,0
                try:
                    if width and height and int(width) > 0 and int(height) > 0:
                        vw, vh = int(width), int(height)
                        ar = vw / vh
                        if ar >= 1:
                            # Horizontal / square video: fit width to 320
                            tw = 320
                            th = max(2, round(320 / ar))
                        else:
                            # Vertical video: fit height to 320
                            th = 320
                            tw = max(2, round(320 * ar))
                        # Ensure both dimensions are even (required by some encoders)
                        tw = tw + (tw % 2)
                        th = th + (th % 2)
                except Exception as e:
                    logger.warning(f"_resize_to_thumb_free: AR calc error: {e}")
                logger.info(f"_resize_to_thumb_free: video={vw}x{vh}, ar={ar:.2f}, target={tw}x{th}, shorts={is_shorts}")
                if is_shorts:
                    result = _thumb_crop_center(src_path, dest_path, tw, th)
                else:
                    result = _thumb_fit_ar(src_path, dest_path, tw, th)
                if not result:
                    logger.warning(f"_resize_to_thumb_free: _thumb_fit_ar failed for {src_path} -> {dest_path} ({tw}x{th})")
                return result
            except Exception as e:
                logger.warning(f"_resize_to_thumb_free: unexpected error: {e}")
                return False

        def _gen_free_cover(video_path: str) -> str | None:
            try:
                base_dir = os.path.dirname(video_path)
                base_name = os.path.splitext(os.path.basename(video_path))[0]
                cover_path = os.path.join(base_dir, base_name + '.__tgthumb_ext.jpg')
                if os.path.exists(cover_path) and os.path.getsize(cover_path) > 0:
                    return cover_path
                # 1) Try downloading external thumbnail (scaled to 320px width)
                try:
                    tmp_dl = os.path.join(base_dir, base_name + '.__ext_thumb.jpg')
                    if video_url and download_thumbnail(video_url, tmp_dl):
                        if _resize_to_thumb_free(tmp_dl, cover_path):
                            try:
                                if os.path.exists(tmp_dl):
                                    os.remove(tmp_dl)
                            except Exception:
                                pass
                            return cover_path
                    try:
                        if os.path.exists(tmp_dl):
                            os.remove(tmp_dl)
                    except Exception:
                        pass
                except Exception:
                    pass
                # 2) Fallback: use passed-in thumb_file_path (already downloaded by down_and_up)
                if thumb_file_path and os.path.exists(thumb_file_path) and os.path.getsize(thumb_file_path) > 0:
                    if _resize_to_thumb_free(thumb_file_path, cover_path):
                        logger.info(f"Using passed-in thumbnail for free cover: {thumb_file_path}")
                        return cover_path
                    # If resize failed, return thumb_file_path as-is
                    logger.info(f"Returning passed-in thumbnail directly (resize skipped): {thumb_file_path}")
                    return thumb_file_path
                # 3) Last resort: extract frame from video (only for large/long videos)
                if _should_generate_cover(video_path, duration):
                    return _gen_thumb(video_path)
                return None
            except Exception:
                return _gen_thumb(video_path) if _should_generate_cover(video_path, duration) else None

        def _is_small_video() -> bool:
            """Check if video is small enough for Telegram to auto-generate thumbnails."""
            try:
                size_mb = os.path.getsize(video_abs_path) / (1024 * 1024)
            except Exception:
                size_mb = 0.0
            try:
                dur = float(duration or 0)
            except Exception:
                dur = 0.0
            return (dur < 60.0) and (size_mb < 10.0)

        def _resolve_thumb() -> str | None:
            """Pick the best available thumbnail respecting size rules.
            
            For small videos (<10MB, <60s): only use external/web thumbnails,
            skip ffmpeg-generated frames — Telegram handles those itself.
            For large videos: use any available thumbnail.
            """
            small = _is_small_video()
            # 1) Try generated cover (external download → thumb_file_path → ffmpeg frame)
            try:
                gen = _gen_free_cover(video_abs_path)
                if gen and os.path.exists(gen) and os.path.getsize(gen) > 0:
                    # For small videos: skip ffmpeg-generated frames
                    if small and gen.endswith('.__tgthumb.jpg'):
                        logger.info(f"Skipping ffmpeg frame for small video: {gen}")
                    else:
                        logger.info(f"Using generated cover as thumbnail: {gen}")
                        return gen
            except Exception as thumb_error:
                logger.warning(f"Error generating thumbnail: {thumb_error}")
            # 2) Fallback to thumb_file_path passed from down_and_up
            if thumb_file_path and os.path.exists(thumb_file_path) and os.path.getsize(thumb_file_path) > 0:
                # For small videos: skip if it looks like an ffmpeg-generated thumbnail
                if small and ('__tgthumb' in thumb_file_path or 'default_thumb' in thumb_file_path):
                    logger.info(f"Skipping generated thumbnail for small video: {thumb_file_path}")
                else:
                    logger.info(f"Using passed-in thumbnail (thumb_file_path): {thumb_file_path}")
                    return thumb_file_path
            if not small:
                logger.warning("No thumbnail available for large video (both generated and passed-in are missing/empty)")
            else:
                logger.info("Small video without external thumbnail — Telegram will auto-generate")
            return None

        def _try_send_video(caption_text: str):
            messages = safe_get_messages(user_id)
            nonlocal was_paid
            local_thumb_free = _resolve_thumb()
            # Paid media only in private chats; in groups/channels send regular video
            try:
                chat_type = getattr(message.chat, "type", None)
                is_private_chat = chat_type == enums.ChatType.PRIVATE
            except Exception:
                is_private_chat = True
            # Проверяем, должен ли админ получать платный контент
            from HELPERS.limitter import should_apply_limits_to_admin
            should_send_paid = is_spoiler and is_private_chat and should_apply_limits_to_admin(user_id=user_id, message=message)
            # Also paid if subtitle hard-burn with star cost > 0
            is_sub_paid = (paid_star_count > 0) and is_private_chat and should_apply_limits_to_admin(user_id=user_id, message=message)
            effective_paid = should_send_paid or is_sub_paid
            effective_star_count = paid_star_count if is_sub_paid else (LimitsConfig.NSFW_STAR_COST if should_send_paid else 0)
            if effective_paid:
                try:
                    # Пробиваем метаданные и добавляем корректный cover и параметры
                    try:
                        v_w, v_h, v_dur = get_video_info_ffprobe(video_abs_path)
                    except Exception:
                        v_w, v_h, v_dur = width, height, duration
                    # duration для paid должен быть float и >0
                    try:
                        safe_paid_dur = float(v_dur) if v_dur and float(v_dur) > 0 else float(duration) if duration and float(duration) > 0 else 1.0
                    except Exception:
                        safe_paid_dur = 1.0
                    # ширина/высота обязаны быть заданы (>0)
                    try:
                        safe_w = int(v_w) if v_w and int(v_w) > 0 else 640
                    except Exception:
                        safe_w = 640
                    try:
                        safe_h = int(v_h) if v_h and int(v_h) > 0 else 360
                    except Exception:
                        safe_h = 360
                    # Try to generate paid cover, but handle errors gracefully
                    paid_cover = None
                    try:
                        paid_cover = _gen_paid_cover(video_abs_path)
                        if paid_cover and not os.path.exists(paid_cover):
                            logger.warning(f"Paid cover file does not exist: {paid_cover}")
                            paid_cover = None
                        elif paid_cover and os.path.getsize(paid_cover) == 0:
                            logger.warning(f"Paid cover file is empty: {paid_cover}")
                            paid_cover = None
                    except Exception as cover_error:
                        logger.warning(f"Error generating paid cover, continuing without it: {cover_error}")
                        paid_cover = None
                    
                    paid_media = InputPaidMediaVideo(
                        media=video_abs_path,
                        cover=paid_cover,
                        width=safe_w,
                        height=safe_h,
                        duration=safe_paid_dur,
                        supports_streaming=True
                    )
                except TypeError:
                    paid_media = InputPaidMediaVideo(
                        media=video_abs_path,
                    )
                allow_broadcast = getattr(message.chat, "type", None) != enums.ChatType.PRIVATE
                # Start upload logging to prevent watchdog false positives
                _start_upload_logging(user_id, msg_id)
                try:
                    try:
                        result = app.send_paid_media(
                            chat_id=user_id,
                            media=[paid_media],
                            star_count=effective_star_count,
                            **({"allow_paid_broadcast": True} if allow_broadcast else {}),
                            payload=str(Config.STAR_RECEIVER),
                            reply_parameters=ReplyParameters(message_id=message.id),
                        )
                    except Exception as e:
                        logger.error(f"send_paid_media failed (will NOT fallback to free): {e}")
                        raise PaidMediaSendError(str(e)) from e
                    try:
                        # Some forks return list for albums; wrap to single message for uniformity
                        video_msg = result[0] if isinstance(result, list) and result else result
                        # Paid media will be forwarded to LOGS_PAID_ID in image_cmd.py for caching
                        was_paid = True
                        return video_msg
                    except Exception:
                        was_paid = True
                        return result
                finally:
                    # Stop upload logging after upload completes or fails
                    _stop_upload_logging(user_id, msg_id)
            # Для бесплатных тоже удерживаем правильные метаданные и мини-обложку по правилу
            try:
                v_w2, v_h2, v_dur2 = get_video_info_ffprobe(video_abs_path)
            except Exception:
                v_w2, v_h2, v_dur2 = width, height, duration
            # Final check for thumbnail before sending
            if local_thumb_free and not os.path.exists(local_thumb_free):
                logger.warning(f"Thumbnail file missing before send, removing from request: {local_thumb_free}")
                local_thumb_free = None
            
            # Start upload logging to prevent watchdog false positives
            _start_upload_logging(user_id, msg_id)
            try:
                result = app.send_video(
                    chat_id=user_id,
                    video=video_abs_path,
                    caption=caption_text,
                    duration=int(v_dur2) if v_dur2 else duration,
                    width=int(v_w2) if v_w2 else width,
                    height=int(v_h2) if v_h2 else height,
                    supports_streaming=True,
                    thumb=local_thumb_free,
                    has_spoiler=False,
                    progress=progress_bar,
                    progress_args=(
                        user_id,
                        msg_id,
                        f"{info_text}\n<b>{safe_get_messages(user_id).SENDER_VIDEO_DURATION_MSG}</b> <i>{TimeFormatter(duration*1000)}</i>\n\n<i>{safe_get_messages(user_id).SENDER_UPLOADING_VIDEO_MSG}</i>"
                    ),
                    reply_parameters=ReplyParameters(message_id=message.id),
                    parse_mode=enums.ParseMode.HTML
                )
            finally:
                # Stop upload logging after upload completes or fails
                _stop_upload_logging(user_id, msg_id)
            # Cleanup special thumb (free-only temp files)
            try:
                if local_thumb_free and (
                    local_thumb_free.endswith('.__tgthumb.jpg') or local_thumb_free.endswith('.__tgthumb_ext.jpg')
                ) and os.path.exists(local_thumb_free):
                    os.remove(local_thumb_free)
            except Exception:
                pass
            return result

        def _fallback_send_document(caption_text: str):
            messages = safe_get_messages(user_id)
            nonlocal was_paid
            local_thumb = _resolve_thumb()
            try:
                if not local_thumb or not os.path.exists(local_thumb):
                    local_thumb = os.path.join(os.path.dirname(video_abs_path), os.path.splitext(os.path.basename(video_abs_path))[0] + ".jpg")
                    import subprocess
                    try:
                        middle_sec = max(1, int(duration) // 2 if isinstance(duration, int) else 1)
                        subprocess.run([
                            'ffmpeg','-y','-ss', str(middle_sec), '-i', video_abs_path,
                            '-vframes','1','-vf','scale=320:-1', local_thumb
                        ], capture_output=True, text=True, timeout=30)
                        if not os.path.exists(local_thumb):
                            local_thumb = None
                    except Exception:
                        local_thumb = None
            except Exception:
                local_thumb = thumb_file_path
            try:
                chat_type = getattr(message.chat, "type", None)
                is_private_chat = chat_type == enums.ChatType.PRIVATE
            except Exception:
                is_private_chat = True
            # Проверяем, должен ли админ получать платный контент
            from HELPERS.limitter import should_apply_limits_to_admin
            should_send_paid = is_spoiler and is_private_chat and should_apply_limits_to_admin(user_id=user_id, message=message)
            # Also paid if subtitle hard-burn with star cost > 0
            is_sub_paid = (paid_star_count > 0) and is_private_chat and should_apply_limits_to_admin(user_id=user_id, message=message)
            effective_paid = should_send_paid or is_sub_paid
            effective_star_count = paid_star_count if is_sub_paid else (LimitsConfig.NSFW_STAR_COST if should_send_paid else 0)
            if effective_paid:
                try:
                    try:
                        v_w, v_h, v_dur = get_video_info_ffprobe(video_abs_path)
                    except Exception:
                        v_w, v_h, v_dur = width, height, duration
                    # duration для paid должен быть float и >0
                    try:
                        safe_paid_dur = float(v_dur) if v_dur and float(v_dur) > 0 else float(duration) if duration and float(duration) > 0 else 1.0
                    except Exception:
                        safe_paid_dur = 1.0
                    # ширина/высота обязаны быть заданы (>0)
                    try:
                        safe_w = int(v_w) if v_w and int(v_w) > 0 else 640
                    except Exception:
                        safe_w = 640
                    try:
                        safe_h = int(v_h) if v_h and int(v_h) > 0 else 360
                    except Exception:
                        safe_h = 360
                    # Try to generate paid cover, but handle errors gracefully
                    paid_cover = None
                    try:
                        paid_cover = _gen_paid_cover(video_abs_path)
                        if paid_cover and not os.path.exists(paid_cover):
                            logger.warning(f"Paid cover file does not exist: {paid_cover}")
                            paid_cover = None
                        elif paid_cover and os.path.getsize(paid_cover) == 0:
                            logger.warning(f"Paid cover file is empty: {paid_cover}")
                            paid_cover = None
                    except Exception as cover_error:
                        logger.warning(f"Error generating paid cover, continuing without it: {cover_error}")
                        paid_cover = None
                    
                    paid_media = InputPaidMediaVideo(
                        media=video_abs_path,
                        cover=paid_cover,
                        width=safe_w,
                        height=safe_h,
                        duration=safe_paid_dur,
                        supports_streaming=True
                    )
                except TypeError:
                    paid_media = InputPaidMediaVideo(
                        media=video_abs_path,
                    )
                allow_broadcast = getattr(message.chat, "type", None) != enums.ChatType.PRIVATE
                # Start upload logging to prevent watchdog false positives
                _start_upload_logging(user_id, msg_id)
                try:
                    try:
                        result = app.send_paid_media(
                            chat_id=user_id,
                            media=[paid_media],
                            star_count=effective_star_count,
                            **({"allow_paid_broadcast": True} if allow_broadcast else {}),
                            payload=str(Config.STAR_RECEIVER),
                            reply_parameters=ReplyParameters(message_id=message.id),
                        )
                    except Exception as e:
                        logger.error(f"send_paid_media (document fallback) failed (will NOT fallback to free): {e}")
                        raise PaidMediaSendError(str(e)) from e
                    try:
                        video_msg = result[0] if isinstance(result, list) and result else result
                        # Paid media will be forwarded to LOGS_PAID_ID in image_cmd.py for caching
                        was_paid = True
                        return video_msg
                    except Exception:
                        was_paid = True
                        return result
                finally:
                    # Stop upload logging after upload completes or fails
                    _stop_upload_logging(user_id, msg_id)
            # Get original filename for document (use pre-rename name to preserve Unicode)
            original_filename = _original_filename_before_rename
            # Sanitize filename to avoid Pyrogram decode errors with special characters
            from HELPERS.filesystem_hlp import sanitize_filename
            original_filename = sanitize_filename(original_filename)
            # Start upload logging to prevent watchdog false positives
            _start_upload_logging(user_id, msg_id)
            try:
                result = app.send_document(
                    chat_id=user_id,
                    document=video_abs_path,
                    file_name=original_filename,
                    caption=caption_text,
                    thumb=local_thumb,
                    progress=progress_bar,
                    progress_args=(
                        user_id,
                        msg_id,
                        f"{info_text}\n<b>{safe_get_messages(user_id).SENDER_VIDEO_DURATION_MSG}</b> <i>{TimeFormatter(duration*1000)}</i>\n\n<i>{safe_get_messages(user_id).SENDER_UPLOADING_FILE_MSG}</i>"
                    ),
                    reply_parameters=ReplyParameters(message_id=message.id),
                    parse_mode=enums.ParseMode.HTML
                )
            finally:
                # Stop upload logging after upload completes or fails
                _stop_upload_logging(user_id, msg_id)
            # Cleanup special thumb
            try:
                if local_thumb and (local_thumb.endswith('.__tgthumb.jpg') or local_thumb.endswith('.__tgcover_paid.jpg')) and os.path.exists(local_thumb):
                    os.remove(local_thumb)
            except Exception:
                pass
            return result

        try:
            # Check if user wants to send as file
            if send_as_file:
                logger.info(safe_get_messages(user_id).SENDER_USER_SEND_AS_FILE_ENABLED_MSG.format(user_id=user_id))
                video_msg = _fallback_send_document(cap)
            else:
                attempts_left = 3
                flood_wait_retries = 3
                while True:
                    try:
                        video_msg = _try_send_video(cap)
                        break
                    except PaidMediaSendError as e:
                        from HELPERS.logger import send_error_to_user
                        send_error_to_user(
                            message,
                            safe_get_messages(user_id).ERROR_SENDING_VIDEO_MSG.format(error=str(e)),
                        )
                        raise
                    except Exception as e:
                        error_str = str(e)
                        if isinstance(e, UserIsBlocked) or "USER_IS_BLOCKED" in error_str:
                            logger.warning(f"User {user_id} has blocked the bot, aborting send")
                            mark_user_blocked(user_id)
                            return None

                        if "No such file or directory" in error_str and ("__tgthumb" in error_str or "thumb" in error_str.lower()):
                            logger.warning(f"Thumbnail file error, trying as document: {e}")
                            video_msg = _fallback_send_document(cap)
                            break
                        
                        if "Failed to decode" in error_str:
                            if not os.path.exists(video_abs_path):
                                logger.error(f"Failed to decode: file no longer exists on disk: {video_abs_path}")
                                from HELPERS.logger import send_error_to_user
                                send_error_to_user(message, safe_get_messages(user_id).VIDEO_FILE_NOT_FOUND_MSG.format(filename=os.path.basename(video_abs_path)))
                                return None
                            logger.warning(f"Failed to decode error, trying as document: {e}")
                            video_msg = _fallback_send_document(cap)
                            break

                        if "RPC_CALL_FAIL" in error_str or "500" in error_str or "internal problems" in error_str.lower():
                            attempts_left -= 1
                            if attempts_left <= 0:
                                logger.warning(f"Telegram RPC error persisted after retries, trying as document: {e}")
                                video_msg = _fallback_send_document(cap)
                                break
                            backoff = 3 * (4 - attempts_left)
                            logger.warning(f"Telegram RPC error (500), retrying in {backoff}s... ({attempts_left} left): {e}")
                            time.sleep(backoff)
                            continue

                        if isinstance(e, FloodWait):
                            wait_time = e.value
                            flood_wait_retries -= 1
                            if wait_time <= 120 and flood_wait_retries > 0:
                                wait_time_safe = wait_time + 1
                                logger.warning(f"FloodWait received ({wait_time}s), waiting {wait_time_safe}s... ({flood_wait_retries} retries left)")
                                try:
                                    safe_edit_message_text(user_id, msg_id,
                                        f"⏳ FloodWait {wait_time}s — auto-retrying...")
                                except Exception:
                                    pass
                                time.sleep(wait_time_safe)
                                continue
                            else:
                                hours = wait_time // 3600
                                minutes = (wait_time % 3600) // 60
                                seconds = wait_time % 60
                                time_str = f"{hours}h {minutes}m {seconds}s" if hours > 0 else f"{minutes}m {seconds}s"
                                reason = "too long" if wait_time > 120 else "max retries exceeded"
                                logger.warning(f"FloodWait {reason} ({wait_time}s / {time_str}), saving and notifying user")
                                user_dir = os.path.join("users", str(user_id))
                                try:
                                    os.makedirs(user_dir, exist_ok=True)
                                    with open(os.path.join(user_dir, "flood_wait.txt"), 'w') as fw_f:
                                        fw_f.write(str(wait_time))
                                except Exception:
                                    pass
                                from HELPERS.logger import send_error_to_user
                                send_error_to_user(message,
                                    f"⏳ **Telegram FloodWait**: {time_str}\n\n"
                                    f"Telegram требует подождать перед следующей отправкой. "
                                    f"Бот автоматически продолжит после истечения таймера.")
                                return None

                        if "Request timed out" in error_str or isinstance(e, TimeoutError):
                            attempts_left -= 1
                            if attempts_left <= 0:
                                logger.warning(safe_get_messages(user_id).SENDER_SEND_VIDEO_TIMED_OUT_MSG)
                                video_msg = _fallback_send_document(cap)
                                break
                            time.sleep(2)
                            continue
                        raise
        except Exception as e:
            if isinstance(e, UserIsBlocked) or "USER_IS_BLOCKED" in str(e):
                logger.warning(f"User {user_id} has blocked the bot, aborting send (outer handler)")
                mark_user_blocked(user_id)
                return None
            if "MEDIA_CAPTION_TOO_LONG" in str(e):
                logger.info(safe_get_messages(user_id).SENDER_CAPTION_TOO_LONG_MSG)
                # If the caption is too long, try sending only with the main information
                minimal_cap = ''
                if title_html:
                    minimal_cap += title_html + '\n\n'
                minimal_cap += link_block
                
                try:
                    if send_as_file:
                        # If send_as_file is enabled, always use document
                        video_msg = _fallback_send_document(minimal_cap)
                    else:
                        attempts_left = 2
                        flood_wait_retries = 2
                        while True:
                            try:
                                video_msg = _try_send_video(minimal_cap)
                                break
                            except PaidMediaSendError as e_paid:
                                from HELPERS.logger import send_error_to_user
                                send_error_to_user(
                                    message,
                                    safe_get_messages(user_id).ERROR_SENDING_VIDEO_MSG.format(error=str(e_paid)),
                                )
                                raise
                            except Exception as e2:
                                error_str2 = str(e2)
                                if isinstance(e2, UserIsBlocked) or "USER_IS_BLOCKED" in error_str2:
                                    logger.warning(f"User {user_id} has blocked the bot, aborting send (minimal cap)")
                                    mark_user_blocked(user_id)
                                    return None

                                if "No such file or directory" in error_str2 and ("__tgthumb" in error_str2 or "thumb" in error_str2.lower()):
                                    logger.warning(f"Thumbnail file error with minimal caption, retrying without thumbnail: {e2}")
                                    video_msg = _fallback_send_document(minimal_cap)
                                    break
                                
                                if "Failed to decode" in error_str2:
                                    if not os.path.exists(video_abs_path):
                                        logger.error(f"Failed to decode (minimal cap): file no longer exists on disk: {video_abs_path}")
                                        from HELPERS.logger import send_error_to_user
                                        send_error_to_user(message, safe_get_messages(user_id).VIDEO_FILE_NOT_FOUND_MSG.format(filename=os.path.basename(video_abs_path)))
                                        return None
                                    logger.warning(f"Failed to decode error with minimal caption, trying as document: {e2}")
                                    video_msg = _fallback_send_document(minimal_cap)
                                    break

                                if "RPC_CALL_FAIL" in error_str2 or "500" in error_str2 or "internal problems" in error_str2.lower():
                                    attempts_left -= 1
                                    if attempts_left <= 0:
                                        logger.warning(f"Telegram RPC error persisted after retries (minimal cap), trying as document")
                                        video_msg = _fallback_send_document(minimal_cap)
                                        break
                                    backoff = 3 * (3 - attempts_left)
                                    logger.warning(f"Telegram RPC error (minimal cap), retrying in {backoff}s... ({attempts_left} left)")
                                    time.sleep(backoff)
                                    continue

                                if isinstance(e2, FloodWait):
                                    flood_wait_retries -= 1
                                    if flood_wait_retries > 0:
                                        wait_time = min(e2.value + 1, 30)
                                        logger.warning(f"FloodWait received (minimal cap), waiting {wait_time}s... ({flood_wait_retries} retries left)")
                                        time.sleep(wait_time)
                                        continue
                                    else:
                                        logger.warning(f"FloodWait max retries exceeded (minimal cap), falling back to document")
                                        video_msg = _fallback_send_document(minimal_cap)
                                        break

                                if "Request timed out" in error_str2 or isinstance(e2, TimeoutError):
                                    attempts_left -= 1
                                    if attempts_left <= 0:
                                        logger.warning(safe_get_messages(user_id).SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG)
                                        video_msg = _fallback_send_document(minimal_cap)
                                        break
                                    time.sleep(2)
                                    continue
                                raise
                except Exception as e:
                    logger.error(safe_get_messages(user_id).SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG.format(error=e))
                    # Последний фолбэк — без описания, с документом при таймауте
                    try:
                        if send_as_file:
                            video_msg = _fallback_send_document("")
                        else:
                            video_msg = _try_send_video("")
                    except PaidMediaSendError as e_paid3:
                        from HELPERS.logger import send_error_to_user
                        send_error_to_user(
                            message,
                            safe_get_messages(user_id).ERROR_SENDING_VIDEO_MSG.format(error=str(e_paid3)),
                        )
                        raise
                    except Exception as e3:
                        error_str3 = str(e3)
                        if isinstance(e3, UserIsBlocked) or "USER_IS_BLOCKED" in error_str3:
                            logger.warning(f"User {user_id} has blocked the bot, aborting send (empty cap)")
                            mark_user_blocked(user_id)
                            return None
                        # Handle thumbnail file errors
                        if "No such file or directory" in error_str3 and ("__tgthumb" in error_str3 or "thumb" in error_str3.lower()):
                            logger.warning(f"Thumbnail file error, trying as document: {e3}")
                            video_msg = _fallback_send_document("")
                        # Handle "Failed to decode" errors
                        elif "Failed to decode" in error_str3:
                            if not os.path.exists(video_abs_path):
                                logger.error(f"Failed to decode (empty cap): file no longer exists on disk: {video_abs_path}")
                                return None
                            logger.warning(f"Failed to decode error, trying as document: {e3}")
                            video_msg = _fallback_send_document("")
                        elif "Request timed out" in error_str3 or isinstance(e3, TimeoutError):
                            video_msg = _fallback_send_document("")
                        else:
                            raise
            else:
                error_str = str(e)
                if isinstance(e, UserIsBlocked) or "USER_IS_BLOCKED" in error_str:
                    logger.warning(f"User {user_id} has blocked the bot, aborting send (else branch)")
                    mark_user_blocked(user_id)
                    return None
                # Handle thumbnail file errors
                if "No such file or directory" in error_str and ("__tgthumb" in error_str or "thumb" in error_str.lower()):
                    logger.warning(f"Thumbnail file error in main handler, trying as document: {e}")
                    try:
                        video_msg = _fallback_send_document(cap if 'cap' in locals() else "")
                    except Exception as fallback_error:
                        logger.error(f"Fallback to document also failed: {fallback_error}")
                        from HELPERS.logger import send_error_to_user
                        send_error_to_user(message, safe_get_messages(user_id).ERROR_SENDING_VIDEO_MSG.format(error=str(fallback_error)))
                        raise fallback_error
                # Handle "Failed to decode" errors
                elif "Failed to decode" in error_str:
                    if not os.path.exists(video_abs_path):
                        logger.error(f"Failed to decode (else branch): file no longer exists on disk: {video_abs_path}")
                        return None
                    logger.warning(f"Failed to decode error in main handler, trying as document: {e}")
                    try:
                        video_msg = _fallback_send_document(cap if 'cap' in locals() else "")
                    except Exception as fallback_error:
                        logger.error(f"Fallback to document also failed: {fallback_error}")
                        from HELPERS.logger import send_error_to_user
                        send_error_to_user(message, safe_get_messages(user_id).ERROR_SENDING_VIDEO_MSG.format(error=str(fallback_error)))
                        raise fallback_error
                else:
                    # If the error is not related to the length of the caption, log it and pass it further
                    from HELPERS.logger import send_error_to_user
                    send_error_to_user(message, safe_get_messages(user_id).ERROR_SENDING_VIDEO_MSG.format(error=error_str))
                    raise e
        # Note: Forwarding to log channels is now handled in down_and_up.py
        # to avoid double forwarding and ensure proper channel routing

        if was_truncated and full_video_title:
            try:
                os.makedirs(os.path.dirname(temp_desc_path), exist_ok=True)
                with open(temp_desc_path, "w", encoding="utf-8") as f:
                    f.write(full_video_title)
            except OSError as desc_err:
                logger.warning(f"Could not write description file: {desc_err}")
                was_truncated = False
        if was_truncated and os.path.exists(temp_desc_path):
            try:
                user_doc_msg = app.send_document(
                    chat_id=user_id,
                    document=temp_desc_path,
                    caption=safe_get_messages(user_id).CHANGE_CAPTION_HINT_MSG,
                    reply_parameters=ReplyParameters(message_id=message.id),
                    parse_mode=enums.ParseMode.HTML
                )
                # Note: Description file forwarding is handled in down_and_up.py
            except Exception as e:
                logger.error(safe_get_messages(user_id).SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG.format(error=e))
                from HELPERS.logger import send_error_to_user
                send_error_to_user(message, safe_get_messages(user_id).ERROR_SENDING_DESCRIPTION_FILE_MSG.format(error=str(e)))
        return video_msg
    finally:
        # Rename file back to original path if it was renamed for ASCII compatibility
        if _original_video_path_for_rename and os.path.exists(video_abs_path):
            try:
                os.rename(video_abs_path, _original_video_path_for_rename)
                logger.info(f"Renamed back to original path: {video_abs_path} -> {_original_video_path_for_rename}")
            except Exception as _rename_back_err:
                logger.warning(f"Failed to rename back to original path: {_rename_back_err}")
        if os.path.exists(temp_desc_path):
            try:
                os.remove(temp_desc_path)
            except Exception as e:
                logger.error(safe_get_messages(user_id).SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG.format(error=e))
                # This is not critical enough to log to LOG_EXCEPTION channel

#####################################################################################
