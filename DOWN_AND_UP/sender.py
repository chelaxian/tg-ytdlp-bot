# @reply_with_keyboard
from pyrogram import enums
from pyrogram.types import ReplyParameters, InputPaidMediaVideo
from HELPERS.app_instance import get_app
from HELPERS.logger import logger
from HELPERS.logger import get_log_channel
from HELPERS.download_status import progress_bar
from HELPERS.limitter import TimeFormatter
from HELPERS.caption import truncate_caption
from DOWN_AND_UP.ffmpeg import get_video_info_ffprobe
import os
import subprocess
import json
from HELPERS.safe_messeger import safe_forward_messages, safe_send_message
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
):
    import re
    import os
    user_id = message.chat.id
    messages = safe_get_messages(user_id)
    text = message.text or ""
    m = re.search(r'https?://[^\s\*]+', text)
    video_url = m.group(0) if m else ""
    temp_desc_path = os.path.join(os.path.dirname(video_abs_path), "full_description.txt")
    was_truncated = False
    
    # Check if user has send_as_file enabled
    user_args = get_user_args(user_id)
    send_as_file = user_args.get("send_as_file", False)
    
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
                                                skip_size_check=True  # Skip size check for sub-parts
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
                                        skip_size_check=True  # Skip size check for parts
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
                                    skip_size_check=True  # Skip size check for parts
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
    
    if is_youtube:
        if "youtube.com/shorts/" in video_url or "/shorts/" in video_url:
            width, height = 360, 640
        else:
            width, height = 640, 360
    else:
        # For the rest - define the size of the video dynamically
        try:
            width, height, _ = get_video_info_ffprobe(video_abs_path)
        except Exception as e:
            logger.error(safe_get_messages(user_id).SENDER_FFPROBE_BYPASS_ERROR_MSG.format(video_path=video_abs_path, error=e))
            import traceback
            logger.error(traceback.format_exc())
            width, height = 0, 0

    try:
        # Logic simplified: use tags that were already generated in down_and_up.
        # Use original title for caption, but truncated description
        title_html, pre_block, blockquote_content, tags_block, link_block, was_truncated = truncate_caption(
            title=caption,  # Original title for caption
            description=full_video_title,  # Full description to be truncated
            url=video_url,
            tags_text=tags_text, # Use final tags for calculation
            max_length=1000,  # Reduced for safety
            user_id=user_id
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

        def _resize_to_cover(src_path: str, dest_path: str) -> bool:
            try:
                subprocess.run([
                    'ffmpeg','-y','-i', src_path,
                    '-vf','scale=if(gte(a,1),320,-2):if(gte(a,1),-2,320),pad=320:320:(320-iw)/2:(320-ih)/2:color=black',
                    '-vframes','1','-q:v','4', dest_path
                ], capture_output=True, text=True, timeout=30)
                return os.path.exists(dest_path) and os.path.getsize(dest_path) > 0
            except Exception:
                return False

        def _gen_paid_cover(video_path: str) -> str | None:
            try:
                if not _should_generate_cover(video_path, duration):
                    return None
                base_dir = os.path.dirname(video_path)
                base_name = os.path.splitext(os.path.basename(video_path))[0]
                cover_path = os.path.join(base_dir, base_name + '.__tgcover_paid.jpg')
                if os.path.exists(cover_path) and os.path.getsize(cover_path) > 0:
                    return cover_path
                # 1) Попробовать скачать внешнюю миниатюру (приоритетно)
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
                    # удалить временный, если остался
                    try:
                        if os.path.exists(tmp_dl):
                            os.remove(tmp_dl)
                    except Exception:
                        pass
                except Exception:
                    pass
                # 2) Фолбэк: кадр из видео, затем привести к нужному размеру без паддинга (с сохранением пропорций)
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

        def _resize_to_thumb_free(src_path: str, dest_path: str) -> bool:
            try:
                subprocess.run([
                    'ffmpeg','-y','-i', src_path,
                    '-vf','scale=320:-1',
                    '-vframes','1','-q:v','4', dest_path
                ], capture_output=True, text=True, timeout=30)
                return os.path.exists(dest_path) and os.path.getsize(dest_path) > 0
            except Exception:
                return False

        def _gen_free_cover(video_path: str) -> str | None:
            try:
                # Встраиваем миниатюру только если файл >10MB или длительность >=60 сек
                if not _should_generate_cover(video_path, duration):
                    return None
                base_dir = os.path.dirname(video_path)
                base_name = os.path.splitext(os.path.basename(video_path))[0]
                cover_path = os.path.join(base_dir, base_name + '.__tgthumb_ext.jpg')
                if os.path.exists(cover_path) and os.path.getsize(cover_path) > 0:
                    return cover_path
                # 1) Попробовать скачать внешнюю миниатюру (без паддинга, только масштаб до 640 по ширине)
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
                # 2) Фолбэк: кадр из видео (как и раньше)
                return _gen_thumb(video_path)
            except Exception:
                return _gen_thumb(video_path)

        def _try_send_video(caption_text: str):
            messages = safe_get_messages(user_id)
            nonlocal was_paid
            # Для бесплатных сообщений — внешний превью без паддинга; для платных — обложка 320x320
            local_thumb_free = None
            try:
                local_thumb_free = _gen_free_cover(video_abs_path)
                # Ensure thumbnail exists and is readable before using it
                if local_thumb_free:
                    if not os.path.exists(local_thumb_free):
                        logger.warning(f"Thumbnail file does not exist: {local_thumb_free}")
                        local_thumb_free = None
                    elif os.path.getsize(local_thumb_free) == 0:
                        logger.warning(f"Thumbnail file is empty: {local_thumb_free}")
                        local_thumb_free = None
            except Exception as thumb_error:
                logger.warning(f"Error generating thumbnail, continuing without it: {thumb_error}")
                local_thumb_free = None
            # Paid media only in private chats; in groups/channels send regular video
            try:
                chat_type = getattr(message.chat, "type", None)
                is_private_chat = chat_type == enums.ChatType.PRIVATE
            except Exception:
                is_private_chat = True
            # Проверяем, должен ли админ получать платный контент
            from HELPERS.limitter import should_apply_limits_to_admin
            should_send_paid = is_spoiler and is_private_chat and should_apply_limits_to_admin(user_id=user_id, message=message)
            if should_send_paid:
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
                was_paid = True
                allow_broadcast = getattr(message.chat, "type", None) != enums.ChatType.PRIVATE
                # Start upload logging to prevent watchdog false positives
                _start_upload_logging(user_id, msg_id)
                try:
                    result = app.send_paid_media(
                        chat_id=user_id,
                        media=[paid_media],
                        star_count=LimitsConfig.NSFW_STAR_COST,
                        **({"allow_paid_broadcast": True} if allow_broadcast else {}),
                        payload=str(Config.STAR_RECEIVER),
                        reply_parameters=ReplyParameters(message_id=message.id),
                    )
                    try:
                        # Some forks return list for albums; wrap to single message for uniformity
                        video_msg = result[0] if isinstance(result, list) and result else result
                        # Paid media will be forwarded to LOGS_PAID_ID in image_cmd.py for caching
                        return video_msg
                    except Exception:
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
            # Для бесплатных документов — внешний превью без паддинга
            local_thumb = _gen_free_cover(video_abs_path) or thumb_file_path
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
            if should_send_paid:
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
                was_paid = True
                allow_broadcast = getattr(message.chat, "type", None) != enums.ChatType.PRIVATE
                # Start upload logging to prevent watchdog false positives
                _start_upload_logging(user_id, msg_id)
                try:
                    result = app.send_paid_media(
                        chat_id=user_id,
                        media=[paid_media],
                        star_count=LimitsConfig.NSFW_STAR_COST,
                        **({"allow_paid_broadcast": True} if allow_broadcast else {}),
                        payload=str(Config.STAR_RECEIVER),
                        reply_parameters=ReplyParameters(message_id=message.id),
                    )
                    try:
                        video_msg = result[0] if isinstance(result, list) and result else result
                        # Paid media will be forwarded to LOGS_PAID_ID in image_cmd.py for caching
                        return video_msg
                    except Exception:
                        return result
                finally:
                    # Stop upload logging after upload completes or fails
                    _stop_upload_logging(user_id, msg_id)
            # Get original filename for document
            original_filename = os.path.basename(video_abs_path)
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
                # Первая попытка с полным описанием, с ограничением на количество ретраев по таймауту
                attempts_left = 3
                while True:
                    try:
                        video_msg = _try_send_video(cap)
                        break
                    except Exception as e:
                        error_str = str(e)
                        # Handle thumbnail file errors
                        if "No such file or directory" in error_str and ("__tgthumb" in error_str or "thumb" in error_str.lower()):
                            logger.warning(f"Thumbnail file error, trying as document: {e}")
                            video_msg = _fallback_send_document(cap)
                            break
                        
                        # Handle "Failed to decode" errors
                        if "Failed to decode" in error_str:
                            logger.warning(f"Failed to decode error, trying as document: {e}")
                            video_msg = _fallback_send_document(cap)
                            break
                        
                        if "Request timed out" in error_str or isinstance(e, TimeoutError):
                            attempts_left -= 1
                            if attempts_left and attempts_left <= 0:
                                logger.warning(safe_get_messages(user_id).SENDER_SEND_VIDEO_TIMED_OUT_MSG)
                                video_msg = _fallback_send_document(cap)
                                break
                            time.sleep(2)
                            continue
                        raise
        except Exception as e:
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
                        # Попытка с коротким описанием и ограниченными ретраями по таймауту
                        attempts_left = 2
                        while True:
                            try:
                                video_msg = _try_send_video(minimal_cap)
                                break
                            except Exception as e2:
                                error_str2 = str(e2)
                                # Handle thumbnail file errors
                                if "No such file or directory" in error_str2 and ("__tgthumb" in error_str2 or "thumb" in error_str2.lower()):
                                    logger.warning(f"Thumbnail file error with minimal caption, retrying without thumbnail: {e2}")
                                    video_msg = _fallback_send_document(minimal_cap)
                                    break
                                
                                # Handle "Failed to decode" errors
                                if "Failed to decode" in error_str2:
                                    logger.warning(f"Failed to decode error with minimal caption, trying as document: {e2}")
                                    video_msg = _fallback_send_document(minimal_cap)
                                    break
                                
                                if "Request timed out" in error_str2 or isinstance(e2, TimeoutError):
                                    attempts_left -= 1
                                    if attempts_left and attempts_left <= 0:
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
                    except Exception as e3:
                        error_str3 = str(e3)
                        # Handle thumbnail file errors
                        if "No such file or directory" in error_str3 and ("__tgthumb" in error_str3 or "thumb" in error_str3.lower()):
                            logger.warning(f"Thumbnail file error, trying as document: {e3}")
                            video_msg = _fallback_send_document("")
                        # Handle "Failed to decode" errors
                        elif "Failed to decode" in error_str3:
                            logger.warning(f"Failed to decode error, trying as document: {e3}")
                            video_msg = _fallback_send_document("")
                        elif "Request timed out" in error_str3 or isinstance(e3, TimeoutError):
                            video_msg = _fallback_send_document("")
                        else:
                            raise
            else:
                error_str = str(e)
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
            with open(temp_desc_path, "w", encoding="utf-8") as f:
                f.write(full_video_title)
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
        if os.path.exists(temp_desc_path):
            try:
                os.remove(temp_desc_path)
            except Exception as e:
                logger.error(safe_get_messages(user_id).SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG.format(error=e))
                # This is not critical enough to log to LOG_EXCEPTION channel

#####################################################################################
