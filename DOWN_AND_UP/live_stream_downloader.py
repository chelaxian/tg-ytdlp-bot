# Live Stream Downloader
# Downloads live streams in chunks by size and sends them immediately

import os
import yt_dlp
import time
from datetime import datetime
from CONFIG.limits import LimitsConfig
from CONFIG.messages import safe_get_messages
from HELPERS.logger import logger, get_log_channel
from HELPERS.safe_messeger import safe_forward_messages
from DOWN_AND_UP.sender import send_videos
from DOWN_AND_UP.ffmpeg import get_duration_thumb, get_video_info_ffprobe, split_video_2
from DOWN_AND_UP.down_and_up import _save_video_cache_with_logging
from COMMANDS.split_sizer import get_user_split_size


def download_live_stream_chunked(
    app, message, url, user_id, user_dir_name, info_dict, 
    proc_msg_id, current_total_process, tags_text="", 
    cookies_already_checked=False, use_proxy=False,
    format_override=None, quality_key=None
):
    """
    Download live stream in chunks by size and send each chunk immediately.
    
    Args:
        app: Pyrogram app instance
        message: Telegram message object
        url: Live stream URL
        user_id: User ID
        user_dir_name: Directory for downloads
        info_dict: Video info dict from yt-dlp
        proc_msg_id: Progress message ID
        current_total_process: Progress text
        tags_text: Tags text
        cookies_already_checked: Whether cookies were already checked
        use_proxy: Whether to use proxy
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        messages = safe_get_messages(user_id)
        
        # Get configuration
        max_duration = LimitsConfig.MAX_LIVE_STREAM_DURATION
        # User‑configured split size (default ~1.95 GiB)
        user_split_size = get_user_split_size(user_id)
        # Hard Telegram limit ~2 GiB, оставим запас ~50 MiB
        telegram_limit_bytes = (2 * 1024 * 1024 * 1024) - (50 * 1024 * 1024)
        # Фактический лимит на размер одного файла/куска
        max_chunk_size = min(user_split_size, telegram_limit_bytes)
        
        logger.info(
            f"Starting live stream download: url={url}, "
            f"user_split_size={user_split_size} bytes, "
            f"telegram_limit={telegram_limit_bytes} bytes, "
            f"effective_max_chunk_size={max_chunk_size} bytes, "
            f"max_duration={max_duration}s"
        )
        # Safe quality key for cache (reuse same semantics as in down_and_up)
        safe_quality_key = quality_key if quality_key is not None else "best"
        
        # Get video title for filename
        video_title = info_dict.get('title', 'live_stream')
        if not video_title or video_title == 'live_stream':
            # Try to get channel name
            channel = info_dict.get('channel', 'live')
            video_title = f"{channel}_live_stream"
        
        # Sanitize title
        from HELPERS.filesystem_hlp import sanitize_filename_strict
        safe_title = sanitize_filename_strict(video_title)
        
        # Get upload date for filename
        upload_date = info_dict.get('upload_date')
        if upload_date:
            try:
                # Parse YYYYMMDD format
                date_obj = datetime.strptime(upload_date, '%Y%m%d')
                date_str = date_obj.strftime('%Y-%m-%d')
            except:
                date_str = datetime.now().strftime('%Y-%m-%d')
        else:
            date_str = datetime.now().strftime('%Y-%m-%d')
        
        # Get channel name
        channel = info_dict.get('channel', 'live')
        safe_channel = sanitize_filename_strict(channel)
        
        # Prepare base yt-dlp options
        # Note: live_from_start will be set per chunk (True for first, False for subsequent)
        base_opts = {
            'concurrent_fragment_downloads': 4,  # -N 4
            'retries': float('inf'),  # -R infinite
            'fragment_retries': float('inf'),  # --fragment-retries infinite
            'retry_sleep': 'fragment:exp=1:30',  # --retry-sleep fragment:exp=1:30
            'continue_dl': True,  # --continue
            'noverwrites': True,  # --no-overwrites
            'hls_prefer_ffmpeg': True,  # --hls-prefer-ffmpeg
            'hls_use_mpegts': True,  # --hls-use-mpegts
            'downloader': 'ffmpeg',  # --downloader ffmpeg
            'quiet': False,
            'no_warnings': False,
        }
        
        # Add user's custom yt-dlp arguments from /args command
        from COMMANDS.args_cmd import get_user_ytdlp_args, log_ytdlp_options
        user_args = get_user_ytdlp_args(user_id, url)
        if user_args:
            # Update base_opts with user args, but preserve live stream specific settings
            # Don't override critical live stream options
            preserved_keys = {
                'live_from_start', 'concurrent_fragment_downloads', 'retries', 
                'fragment_retries', 'retry_sleep', 'continue_dl', 'noverwrites',
                'hls_prefer_ffmpeg', 'hls_use_mpegts', 'downloader', 'downloader_args'
            }
            for key, value in user_args.items():
                if key not in preserved_keys:
                    base_opts[key] = value
                    logger.info(f"Applied user arg for live stream: {key} = {value}")
        
        # Apply format_override if provided (from always_ask_menu or /format)
        if format_override:
            base_opts['format'] = format_override
            logger.info(f"Applied format_override for live stream: {format_override}")
        elif quality_key and quality_key != "best":
            # Convert quality_key to format if no format_override
            try:
                from DOWN_AND_UP.always_ask_menu import get_user_args
                user_args_local = get_user_args(user_id)
                user_codec = user_args_local.get('codec', 'avc1')
                
                # Build format based on quality_key and codec preference
                if quality_key.endswith('p'):
                    quality_val = int(quality_key[:-1])
                    # Determine previous quality
                    if quality_val >= 4320:
                        prev = 2160
                    elif quality_val >= 2160:
                        prev = 1440
                    elif quality_val >= 1440:
                        prev = 1080
                    elif quality_val >= 1080:
                        prev = 720
                    elif quality_val >= 720:
                        prev = 480
                    elif quality_val >= 480:
                        prev = 360
                    elif quality_val >= 360:
                        prev = 240
                    elif quality_val >= 240:
                        prev = 144
                    else:
                        prev = 0
                    
                    if user_codec == "av01":
                        format_str = f"bv*[vcodec*=av01][height<={quality_val}][height>{prev}]+ba[acodec*=mp4a]/bv*[vcodec*=av01][height<={quality_val}]+ba[acodec*=opus]/bv*[vcodec*=av01]+ba/bv+ba/best"
                    elif user_codec == "vp9":
                        format_str = f"bv*[vcodec*=vp9][height<={quality_val}][height>{prev}]+ba[acodec*=mp4a]/bv*[vcodec*=vp9][height<={quality_val}]+ba[acodec*=opus]/bv*[vcodec*=vp9]+ba/bv+ba/best"
                    else:  # avc1
                        format_str = f"bv*[vcodec*=avc1][height<={quality_val}][height>{prev}]+ba[acodec*=mp4a]/bv*[vcodec*=avc1][height<={quality_val}]+ba/bv*[vcodec*=avc1]+ba/bv+ba/best"
                    base_opts['format'] = format_str
                    logger.info(f"Applied quality_key format for live stream: {format_str}")
            except Exception as e:
                logger.warning(f"Error converting quality_key to format: {e}")
        
        # Apply MKV preference from /format command
        try:
            from COMMANDS.format_cmd import get_user_mkv_preference
            mkv_on = get_user_mkv_preference(user_id)
            if mkv_on:
                base_opts['remux_video'] = 'mkv'
                logger.info(f"Applied MKV preference for live stream")
        except Exception as e:
            logger.debug(f"Could not get MKV preference: {e}")
        
        # Log final yt-dlp options for debugging
        log_ytdlp_options(user_id, base_opts, "live_stream_download")
        
        # Add cookies if available
        user_cookie_path = os.path.join("users", str(user_id), "cookie.txt")
        if os.path.exists(user_cookie_path):
            base_opts['cookiefile'] = user_cookie_path
        
        # Add proxy if needed
        if use_proxy:
            from COMMANDS.proxy_cmd import get_proxy_config
            proxy_config = get_proxy_config()
            if proxy_config and 'type' in proxy_config and 'ip' in proxy_config and 'port' in proxy_config:
                if proxy_config['type'] == 'http':
                    if proxy_config.get('user') and proxy_config.get('password'):
                        proxy_url = f"http://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
                    else:
                        proxy_url = f"http://{proxy_config['ip']}:{proxy_config['port']}"
                elif proxy_config['type'] == 'https':
                    if proxy_config.get('user') and proxy_config.get('password'):
                        proxy_url = f"https://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
                    else:
                        proxy_url = f"https://{proxy_config['ip']}:{proxy_config['port']}"
                elif proxy_config['type'] in ['socks4', 'socks5', 'socks5h']:
                    if proxy_config.get('user') and proxy_config.get('password'):
                        proxy_url = f"{proxy_config['type']}://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
                    else:
                        proxy_url = f"{proxy_config['type']}://{proxy_config['ip']}:{proxy_config['port']}"
                else:
                    proxy_url = f"http://{proxy_config['ip']}:{proxy_config['port']}"
                base_opts['proxy'] = proxy_url
        else:
            from HELPERS.proxy_helper import add_proxy_to_ytdl_opts
            base_opts = add_proxy_to_ytdl_opts(base_opts, url, user_id)
        
        # Add PO token provider for YouTube
        from HELPERS.pot_helper import add_pot_to_ytdl_opts
        base_opts = add_pot_to_ytdl_opts(base_opts, url)
        
        # Download chunks sequentially by size
        successful_chunks = 0
        start_time = time.time()
        did_live_from_start_retry = False
        accumulated_duration = 0  # Track total duration downloaded
        chunk_idx = 0
        # Для защиты от дубликатов запоминаем параметры последнего реально отправленного куска
        last_sent_duration = None
        last_sent_size = None
        # Для кэша: список ID сообщений в лог‑канале (все куски/подкуски)
        cache_message_ids = []
        
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= max_duration:
                logger.info(f"Reached max duration limit ({max_duration}s), stopping live stream download")
                break
            
            chunk_idx += 1
            logger.info(f"Downloading live stream chunk {chunk_idx}, max_size={max_chunk_size} bytes, accumulated_duration={accumulated_duration}s")
            
            # Update progress
            try:
                from HELPERS.safe_messeger import safe_edit_message_text
                from HELPERS.limitter import humanbytes
                progress_text = (
                    f"{current_total_process}\n"
                    f"{messages.LIVE_STREAM_DOWNLOAD_PROGRESS_MSG}\n"
                    f"{messages.LIVE_STREAM_CHUNK_NUMBER_MSG.format(chunk=chunk_idx)}\n"
                    f"{messages.LIVE_STREAM_CHUNK_SIZE_MSG.format(size=humanbytes(max_chunk_size))}\n"
                    f"{messages.LIVE_STREAM_ACCUMULATED_DURATION_MSG.format(duration=int(accumulated_duration))}"
                )
                safe_edit_message_text(user_id, proc_msg_id, progress_text)
            except Exception as e:
                logger.error(f"Error updating progress: {e}")
            
            # Create yt-dlp options for this chunk
            chunk_opts = base_opts.copy()
            
            # Use live_from_start only for the first chunk
            # For subsequent chunks, don't use live_from_start to continue from current position
            if chunk_idx == 1:
                chunk_opts['live_from_start'] = True
            else:
                chunk_opts['live_from_start'] = False
            
            # Prepare output filename for this chunk
            chunk_filename = f"{date_str}_{safe_channel}_{safe_title}_{chunk_idx:03d}.ts"
            chunk_file = os.path.join(user_dir_name, chunk_filename)
            chunk_opts['outtmpl'] = chunk_file.replace('.ts', '.%(ext)s')
            
            # Prepare downloader args for ffmpeg to limit size per chunk
            # Use -fs (file size limit) in output args to limit file size
            # Convert max_chunk_size to MB for ffmpeg (ffmpeg uses MB for -fs)
            max_size_mb = max_chunk_size / (1024 * 1024)
            
            # Input: no time limit, let it download until size limit is reached
            ffmpeg_input_args = ""
            
            # Output: use mpegts format for live streams and limit file size
            ffmpeg_output_args = f"-f mpegts -fs {max_size_mb:.0f}M"
            
            chunk_opts['downloader_args'] = {
                'ffmpeg_i': ffmpeg_input_args,
                'ffmpeg_o': ffmpeg_output_args
            }
            
            try:
                # Check if user directory still exists (might have been deleted by /clean)
                if not os.path.exists(user_dir_name):
                    logger.warning(f"User directory was deleted (probably by /clean), stopping live stream download")
                    try:
                        from HELPERS.safe_messeger import safe_edit_message_text
                        final_text = (
                            f"{current_total_process}\n"
                            f"{messages.LIVE_STREAM_DOWNLOAD_STOPPED_MSG}\n"
                            f"{messages.LIVE_STREAM_USER_DIRECTORY_DELETED_MSG}"
                        )
                        safe_edit_message_text(user_id, proc_msg_id, final_text)
                    except Exception as e:
                        logger.error(f"Error updating progress: {e}")
                    break
                
                with yt_dlp.YoutubeDL(chunk_opts) as ydl:
                    ydl.download([url])
                
                # Check if file was created (might have different extension)
                if not os.path.exists(chunk_file):
                    # Try to find file with any extension
                    import glob
                    chunk_pattern = os.path.join(
                        user_dir_name,
                        f"{date_str}_{safe_channel}_{safe_title}_{chunk_idx:03d}.*"
                    )
                    chunk_files = glob.glob(chunk_pattern)
                    if chunk_files:
                        chunk_file = chunk_files[0]
                    else:
                        logger.warning(f"Could not find chunk file for index {chunk_idx}")
                        continue
                
                if not os.path.exists(chunk_file):
                    logger.warning(f"Chunk file not found: {chunk_file}")
                    continue
                
                # Get video info for the chunk
                try:
                    _, _, duration = get_video_info_ffprobe(chunk_file)
                    if duration:
                        duration = float(duration)
                    else:
                        duration = 0
                except Exception as e:
                    logger.error(f"Error getting video info: {e}")
                    duration = 0
                
                # Verify timing continuity: check that this chunk doesn't start from the beginning
                # For chunks after the first, we expect them to continue from where previous ended
                if chunk_idx > 1 and duration > 0:
                    # Check if chunk file size matches expected (should be close to max_chunk_size)
                    chunk_size = os.path.getsize(chunk_file)
                    if chunk_size < max_chunk_size * 0.1:  # If chunk is less than 10% of expected size
                        logger.warning(f"Chunk {chunk_idx} is suspiciously small ({chunk_size} bytes), might be starting from beginning")
                        # This might indicate the chunk started from beginning, but we continue anyway
                
                # Update accumulated duration
                if duration > 0:
                    accumulated_duration += duration
                    logger.info(f"Chunk {chunk_idx} duration: {duration}s, total accumulated: {accumulated_duration}s")
                
                # --- HARD SIZE CHECK & OPTIONAL ADDITIONAL SPLIT ---
                # На всякий случай ещё раз проверяем реальный размер файла.
                from HELPERS.limitter import humanbytes
                chunk_size_bytes = os.path.getsize(chunk_file)
                if chunk_size_bytes > max_chunk_size:
                    logger.warning(
                        f"Chunk {chunk_idx} size {chunk_size_bytes} bytes "
                        f"exceeds effective max_chunk_size {max_chunk_size} bytes, "
                        f"running additional split_video_2"
                    )
                    try:
                        # Используем split_video_2, чтобы порезать файл на части < max_chunk_size.
                        base_name = f"{safe_title}_chunk_{chunk_idx:03d}"
                        split_result = split_video_2(
                            user_dir_name,
                            base_name,
                            chunk_file,
                            chunk_size_bytes,
                            max_chunk_size,
                            int(duration) if duration else int(accumulated_duration) or 0,
                            user_id
                        )
                        part_captions = split_result.get("video") or []
                        part_paths = split_result.get("path") or []
                        
                        # Отправляем каждую часть по очереди и сразу удаляем
                        sent_any = False
                        for i, part_path in enumerate(part_paths):
                            if not os.path.exists(part_path):
                                logger.warning(f"Split part not found: {part_path}")
                                continue
                            
                            # Получаем длительность части
                            try:
                                _, _, part_duration = get_video_info_ffprobe(part_path)
                                part_duration = int(part_duration) if part_duration else 0
                            except Exception as e:
                                logger.error(f"Error getting split part video info: {e}")
                                part_duration = 0
                            
                            part_size_bytes = os.path.getsize(part_path)
                            part_label = f"{chunk_idx}.{i+1}"
                            
                            part_caption = messages.LIVE_STREAM_CHUNK_CAPTION_MSG.format(
                                chunk=part_label,
                                duration=part_duration,
                                size=humanbytes(part_size_bytes)
                            )
                            if tags_text:
                                part_caption += f"\n{tags_text}"
                            
                            # Пытаемся использовать тот же thumb_file, нового уже не делаем
                            logger.info(f"Sending split part {part_label} to user: {part_path}")
                            part_msg = send_videos(
                                message,
                                part_path,
                                part_caption,
                                part_duration,
                                thumb_file or "",
                                messages.LIVE_STREAM_CHUNK_TITLE_MSG.format(chunk=part_label),
                                proc_msg_id,
                                f"{video_title} - {messages.LIVE_STREAM_CHUNK_TITLE_MSG.format(chunk=part_label)}",
                                tags_text
                            )
                            
                            if part_msg:
                                successful_chunks += 1
                                sent_any = True
                                logger.info(f"Successfully sent split part {part_label}")
                                # Пробуем переслать в лог‑канал для кэша
                                try:
                                    log_channel = get_log_channel("video")
                                    if log_channel:
                                        forwarded = safe_forward_messages(log_channel, user_id, [part_msg.id])
                                        if forwarded:
                                            cache_message_ids.extend([m.id for m in forwarded])
                                except Exception as e:
                                    logger.error(f"Error forwarding split part {part_label} to log channel: {e}")
                            else:
                                logger.warning(f"Failed to send split part {part_label}")
                            
                            # Удаляем часть после отправки
                            try:
                                os.remove(part_path)
                                logger.info(f"Cleaned up split part file: {part_path}")
                            except Exception as e:
                                logger.error(f"Error cleaning up split part file: {e}")
                        
                        # Удаляем исходный крупный файл
                        try:
                            if os.path.exists(chunk_file):
                                os.remove(chunk_file)
                                logger.info(f"Cleaned up original oversized chunk file: {chunk_file}")
                        except Exception as e:
                            logger.error(f"Error cleaning up original oversized chunk file: {e}")
                        
                        # Переходим к следующему куску
                        if sent_any:
                            continue
                        else:
                            # Если не удалось отправить ни одной части — считаем это ошибкой и выходим
                            logger.error(f"No split parts were sent successfully for chunk {chunk_idx}, stopping")
                            # Перед выходом пробуем сохранить то, что уже есть, в кэш
                            try:
                                if cache_message_ids and safe_quality_key:
                                    original_text = message.text or message.caption or ""
                                    _save_video_cache_with_logging(
                                        url, safe_quality_key, cache_message_ids,
                                        original_text=original_text, user_id=user_id
                                    )
                            except Exception as e2:
                                logger.error(f"Error saving live stream cache on split failure: {e2}")
                            return successful_chunks > 0
                    except Exception as e:
                        logger.error(f"Error while additional splitting oversized chunk {chunk_idx}: {e}")
                        # Если доп. сплит сломался, продолжаем обычную логику ниже (попробуем отправить как есть)
                
                # --- THUMBNAIL & REGULAR SEND PATH ---
                # Get or create thumbnail
                thumb_file = None
                try:
                    thumb_name = f"{safe_title}_chunk_{chunk_idx:03d}"
                    result = get_duration_thumb(message, user_dir_name, chunk_file, thumb_name)
                    if result:
                        duration_from_thumb, thumb_file = result
                        # Update duration if we got it from thumbnail extraction
                        if duration_from_thumb:
                            duration = duration_from_thumb
                except Exception as e:
                    logger.error(f"Error creating thumbnail: {e}")
                    # Try to use video thumbnail if available
                    thumb_path = os.path.join(user_dir_name, f"{safe_title}.jpg")
                    if os.path.exists(thumb_path):
                        thumb_file = thumb_path
                
                # Prepare caption
                chunk_size_bytes = os.path.getsize(chunk_file)

                # --- SIMPLE DEDUP GUARD ---
                # Если текущий кусок по длительности и размеру практически совпадает
                # с уже отправленным последним куском, считаем, что это дубликат
                # (например, перезапуск того же VOD) и выходим без повторной отправки.
                if last_sent_duration is not None and last_sent_size is not None:
                    dur_diff = abs(int(duration or 0) - int(last_sent_duration))
                    # допустимая погрешность по размеру ~5%
                    size_diff_ratio = abs(chunk_size_bytes - last_sent_size) / max(last_sent_size, 1)
                    if dur_diff <= 5 and size_diff_ratio <= 0.05:
                        logger.info(
                            f"Detected duplicate live chunk (idx={chunk_idx}, "
                            f"duration={duration}s, size={chunk_size_bytes} bytes) "
                            f"similar to last sent (duration={last_sent_duration}s, "
                            f"size={last_sent_size} bytes); stopping to avoid duplicates"
                        )
                        try:
                            from HELPERS.safe_messeger import safe_edit_message_text
                            final_text = (
                                f"{current_total_process}\n"
                                f"{messages.LIVE_STREAM_DOWNLOAD_COMPLETE_MSG}\n"
                                f"{messages.LIVE_STREAM_CHUNKS_DOWNLOADED_MSG.format(chunks=successful_chunks)}\n"
                                f"{messages.LIVE_STREAM_TOTAL_DURATION_MSG.format(duration=int(accumulated_duration))}\n"
                                f"{messages.LIVE_STREAM_ENDED_MSG}"
                            )
                            safe_edit_message_text(user_id, proc_msg_id, final_text)
                        except Exception as e:
                            logger.error(f"Error updating final progress after duplicate detection: {e}")
                        return successful_chunks > 0

                chunk_caption = messages.LIVE_STREAM_CHUNK_CAPTION_MSG.format(
                    chunk=chunk_idx,
                    duration=int(duration) if duration else 0,
                    size=humanbytes(chunk_size_bytes)
                )
                if tags_text:
                    chunk_caption += f"\n{tags_text}"
                
                # Check if file still exists before sending (might have been deleted by /clean)
                if not os.path.exists(chunk_file):
                    logger.warning(f"Chunk file was deleted before sending (probably by /clean), stopping live stream download")
                    try:
                        from HELPERS.safe_messeger import safe_edit_message_text
                        final_text = (
                            f"{current_total_process}\n"
                            f"{messages.LIVE_STREAM_DOWNLOAD_STOPPED_MSG}\n"
                            f"{messages.LIVE_STREAM_FILE_DELETED_MSG}"
                        )
                        safe_edit_message_text(user_id, proc_msg_id, final_text)
                    except Exception as e:
                        logger.error(f"Error updating progress: {e}")
                    break
                
                # Send chunk immediately
                logger.info(f"Sending chunk {chunk_idx} to user: {chunk_file}")
                
                chunk_msg = send_videos(
                    message,
                    chunk_file,
                    chunk_caption,
                    int(duration) if duration else 0,
                    thumb_file or "",
                    messages.LIVE_STREAM_CHUNK_TITLE_MSG.format(chunk=chunk_idx),
                    proc_msg_id,
                    f"{video_title} - {messages.LIVE_STREAM_CHUNK_TITLE_MSG.format(chunk=chunk_idx)}",
                    tags_text
                )
                
                if chunk_msg:
                    successful_chunks += 1
                    # Обновляем сигнатуру последнего реально отправленного куска
                    last_sent_duration = int(duration) if duration else 0
                    last_sent_size = chunk_size_bytes
                    logger.info(f"Successfully sent chunk {chunk_idx}")
                    # Пробуем переслать в лог‑канал для кэша (регулярный канал, без NSFW/PAID)
                    try:
                        log_channel = get_log_channel("video")
                        if log_channel:
                            forwarded = safe_forward_messages(log_channel, user_id, [chunk_msg.id])
                            if forwarded:
                                cache_message_ids.extend([m.id for m in forwarded])
                    except Exception as e:
                        logger.error(f"Error forwarding live chunk {chunk_idx} to log channel: {e}")
                else:
                    logger.warning(f"Failed to send chunk {chunk_idx}")
                
                # Check if chunk reached size limit (if it's smaller, stream might have ended)
                # Also check if file still exists (might have been deleted by /clean)
                if not os.path.exists(chunk_file):
                    logger.warning(f"Chunk file was deleted (probably by /clean), stopping live stream download")
                    try:
                        from HELPERS.safe_messeger import safe_edit_message_text
                        final_text = (
                            f"{current_total_process}\n"
                            f"{messages.LIVE_STREAM_DOWNLOAD_STOPPED_MSG}\n"
                            f"{messages.LIVE_STREAM_FILE_DELETED_MSG}"
                        )
                        safe_edit_message_text(user_id, proc_msg_id, final_text)
                    except Exception as e:
                        logger.error(f"Error updating progress: {e}")
                    break
                
                chunk_size_bytes = os.path.getsize(chunk_file)
                if chunk_size_bytes < max_chunk_size * 0.9:  # If chunk is less than 90% of max size
                    logger.info(f"Chunk {chunk_idx} is smaller than expected ({chunk_size_bytes} < {max_chunk_size * 0.9}), stream might have ended")
                    # Если первый же кусок заметно меньше лимита, скорее всего, это уже полностью завершившийся стрим/VOD,
                    # который целиком поместился в один файл — дополнительных кусков не нужно.
                    if chunk_idx == 1:
                        logger.info("First chunk is significantly smaller than max_chunk_size; assuming full recording fits into a single file")
                        try:
                            from HELPERS.safe_messeger import safe_edit_message_text
                            final_text = (
                                f"{current_total_process}\n"
                                f"{messages.LIVE_STREAM_DOWNLOAD_COMPLETE_MSG}\n"
                                f"{messages.LIVE_STREAM_CHUNKS_DOWNLOADED_MSG.format(chunks=successful_chunks)}\n"
                                f"{messages.LIVE_STREAM_TOTAL_DURATION_MSG.format(duration=int(accumulated_duration))}\n"
                                f"{messages.LIVE_STREAM_ENDED_MSG}"
                            )
                            safe_edit_message_text(user_id, proc_msg_id, final_text)
                        except Exception as e:
                            logger.error(f"Error updating final progress: {e}")
                        # Сохраняем уже отправленные куски в кэш
                        try:
                            if cache_message_ids and safe_quality_key:
                                original_text = message.text or message.caption or ""
                                _save_video_cache_with_logging(
                                    url, safe_quality_key, cache_message_ids,
                                    original_text=original_text, user_id=user_id
                                )
                        except Exception as e2:
                            logger.error(f"Error saving live stream cache on early end (single chunk): {e2}")
                        return successful_chunks > 0
                    # If this is the second consecutive small chunk, assume stream ended
                    if chunk_idx > 1:
                        logger.info(f"Two consecutive small chunks detected, assuming stream has ended")
                        try:
                            from HELPERS.safe_messeger import safe_edit_message_text
                            final_text = (
                                f"{current_total_process}\n"
                                f"{messages.LIVE_STREAM_DOWNLOAD_COMPLETE_MSG}\n"
                                f"{messages.LIVE_STREAM_CHUNKS_DOWNLOADED_MSG.format(chunks=successful_chunks)}\n"
                                f"{messages.LIVE_STREAM_TOTAL_DURATION_MSG.format(duration=int(accumulated_duration))}\n"
                                f"{messages.LIVE_STREAM_ENDED_MSG}"
                            )
                            safe_edit_message_text(user_id, proc_msg_id, final_text)
                        except Exception as e:
                            logger.error(f"Error updating final progress: {e}")
                        # Сохраняем уже отправленные куски в кэш
                        try:
                            if cache_message_ids and safe_quality_key:
                                original_text = message.text or message.caption or ""
                                _save_video_cache_with_logging(
                                    url, safe_quality_key, cache_message_ids,
                                    original_text=original_text, user_id=user_id
                                )
                        except Exception as e2:
                            logger.error(f"Error saving live stream cache on early end (two small chunks): {e2}")
                        return successful_chunks > 0
                
                # Clean up chunk file after sending to save space
                # Check if file still exists before trying to delete (might have been deleted by /clean)
                if os.path.exists(chunk_file):
                    try:
                        os.remove(chunk_file)
                        logger.info(f"Cleaned up chunk file: {chunk_file}")
                    except Exception as e:
                        logger.error(f"Error cleaning up chunk file: {e}")
                else:
                    logger.warning(f"Chunk file was already deleted: {chunk_file}")
                
            except Exception as e:
                error_text = str(e)
                
                # Check if user directory was deleted (probably by /clean)
                if not os.path.exists(user_dir_name):
                    logger.warning(f"User directory was deleted during download (probably by /clean), stopping live stream download")
                    try:
                        from HELPERS.safe_messeger import safe_edit_message_text
                        final_text = (
                            f"{current_total_process}\n"
                            f"{messages.LIVE_STREAM_DOWNLOAD_STOPPED_MSG}\n"
                            f"{messages.LIVE_STREAM_USER_DIRECTORY_DELETED_MSG}"
                        )
                        safe_edit_message_text(user_id, proc_msg_id, final_text)
                    except Exception as e2:
                        logger.error(f"Error updating progress: {e2}")
                    break
                
                # Check for stream ended errors (transmission ended, video unavailable, etc.)
                stream_ended_keywords = [
                    "transmission ended",
                    "video unavailable",
                    "private video",
                    "video is unavailable",
                    "stream ended",
                    "this live stream recording is not available",
                    "live stream recording is not available",
                    "HTTP Error 403",
                    "HTTP Error 404",
                    "unable to download video data",
                    "no video formats found",
                    "requested format is not available"
                ]
                
                is_stream_ended = False
                if isinstance(e, yt_dlp.utils.DownloadError):
                    error_lower = error_text.lower()
                    for keyword in stream_ended_keywords:
                        if keyword.lower() in error_lower:
                            is_stream_ended = True
                            logger.info(f"Stream ended detected (keyword: '{keyword}'): {error_text}")
                            break
                
                if is_stream_ended:
                    logger.info(f"Live stream has ended, stopping download after {successful_chunks} chunks")
                    try:
                        from HELPERS.safe_messeger import safe_edit_message_text
                        final_text = (
                            f"{current_total_process}\n"
                            f"{messages.LIVE_STREAM_DOWNLOAD_COMPLETE_MSG}\n"
                            f"{messages.LIVE_STREAM_CHUNKS_DOWNLOADED_MSG.format(chunks=successful_chunks)}\n"
                            f"{messages.LIVE_STREAM_TOTAL_DURATION_MSG.format(duration=int(accumulated_duration))}\n"
                            f"{messages.LIVE_STREAM_ENDED_MSG}"
                        )
                        safe_edit_message_text(user_id, proc_msg_id, final_text)
                    except Exception as e2:
                        logger.error(f"Error updating final progress: {e2}")
                    # Сохраняем уже отправленные куски в кэш
                    try:
                        if cache_message_ids and safe_quality_key:
                            original_text = message.text or message.caption or ""
                            _save_video_cache_with_logging(
                                url, safe_quality_key, cache_message_ids,
                                original_text=original_text, user_id=user_id
                            )
                    except Exception as e3:
                        logger.error(f"Error saving live stream cache on stream-ended error: {e3}")
                    return successful_chunks > 0
                
                # Check for --live-from-start error and retry with --no-live-from-start
                if isinstance(e, yt_dlp.utils.DownloadError) and "--live-from-start is passed, but there are no formats that can be downloaded from the start" in error_text and not did_live_from_start_retry:
                    logger.info(f"Live-from-start error detected for chunk {chunk_idx}, retrying with --no-live-from-start")
                    did_live_from_start_retry = True
                    # Update base_opts to disable live_from_start for retry
                    base_opts['live_from_start'] = False
                    # Update chunk_opts with the modified base_opts
                    chunk_opts = {**base_opts, **chunk_opts}
                    chunk_opts['live_from_start'] = False
                    # Retry the download for this chunk
                    try:
                        with yt_dlp.YoutubeDL(chunk_opts) as ydl:
                            ydl.download([url])
                        # Continue with the rest of the chunk processing (checking file, sending, etc.)
                        # We'll need to duplicate the logic here or extract it to a function
                        # For now, let's continue normally and let the retry succeed
                        logger.info(f"Chunk {chunk_idx} retry with --no-live-from-start successful")
                        # Re-check file existence and continue processing
                        if os.path.exists(chunk_file):
                            # Continue with chunk processing below
                            pass
                        else:
                            # Try to find file with any extension
                            import glob
                            chunk_pattern = os.path.join(
                                user_dir_name,
                                f"{date_str}_{safe_channel}_{safe_title}_{chunk_idx:03d}.*"
                            )
                            chunk_files = glob.glob(chunk_pattern)
                            if chunk_files:
                                chunk_file = chunk_files[0]
                            else:
                                logger.warning(f"Could not find chunk file for index {chunk_idx} after retry")
                                continue
                        
                        if not os.path.exists(chunk_file):
                            logger.warning(f"Chunk file not found after retry: {chunk_file}")
                            continue
                        
                        # Get video info for the chunk
                        try:
                            _, _, duration = get_video_info_ffprobe(chunk_file)
                            if duration:
                                duration = float(duration)
                            else:
                                duration = 0
                        except Exception as e2:
                            logger.error(f"Error getting video info: {e2}")
                            duration = 0
                        
                        # Update accumulated duration
                        if duration > 0:
                            accumulated_duration += duration
                            logger.info(f"Chunk {chunk_idx} duration after retry: {duration}s, total accumulated: {accumulated_duration}s")
                        
                        # Get or create thumbnail
                        thumb_file = None
                        try:
                            thumb_name = f"{safe_title}_chunk_{chunk_idx:03d}"
                            result = get_duration_thumb(message, user_dir_name, chunk_file, thumb_name)
                            if result:
                                duration_from_thumb, thumb_file = result
                                if duration_from_thumb:
                                    duration = duration_from_thumb
                        except Exception as e2:
                            logger.error(f"Error creating thumbnail: {e2}")
                            thumb_path = os.path.join(user_dir_name, f"{safe_title}.jpg")
                            if os.path.exists(thumb_path):
                                thumb_file = thumb_path
                        
                        # Prepare caption
                        from HELPERS.limitter import humanbytes
                        chunk_size_bytes = os.path.getsize(chunk_file)
                        chunk_caption = messages.LIVE_STREAM_CHUNK_CAPTION_MSG.format(
                            chunk=chunk_idx,
                            duration=int(duration) if duration else 0,
                            size=humanbytes(chunk_size_bytes)
                        )
                        if tags_text:
                            chunk_caption += f"\n{tags_text}"
                        
                        # Send chunk immediately
                        logger.info(f"Sending chunk {chunk_idx} to user: {chunk_file}")
                        
                        chunk_msg = send_videos(
                            message,
                            chunk_file,
                            chunk_caption,
                            int(duration) if duration else 0,
                            thumb_file or "",
                            messages.LIVE_STREAM_CHUNK_TITLE_MSG.format(chunk=chunk_idx),
                            proc_msg_id,
                            f"{video_title} - {messages.LIVE_STREAM_CHUNK_TITLE_MSG.format(chunk=chunk_idx)}",
                            tags_text
                        )
                        
                        if chunk_msg:
                            successful_chunks += 1
                            logger.info(f"Successfully sent chunk {chunk_idx} after retry")
                        else:
                            logger.warning(f"Failed to send chunk {chunk_idx} after retry")
                        
                        # Check if chunk file still exists
                        if not os.path.exists(chunk_file):
                            logger.warning(f"Chunk file was deleted after retry (probably by /clean), stopping")
                            break
                        
                        # Check if chunk reached size limit
                        chunk_size_bytes = os.path.getsize(chunk_file)
                        if chunk_size_bytes < max_chunk_size * 0.9:
                            logger.info(f"Chunk {chunk_idx} is smaller than expected after retry, stream might have ended")
                        
                        # Clean up chunk file after sending
                        if os.path.exists(chunk_file):
                            try:
                                os.remove(chunk_file)
                                logger.info(f"Cleaned up chunk file after retry: {chunk_file}")
                            except Exception as e:
                                logger.error(f"Error cleaning up chunk file after retry: {e}")
                        
                        # Continue to next chunk
                        continue
                    except Exception as retry_e:
                        logger.error(f"Retry with --no-live-from-start also failed for chunk {chunk_idx}: {retry_e}")
                        # Continue with next chunk
                        continue
                
                logger.error(f"Error downloading chunk {chunk_idx}: {e}")
                import traceback
                logger.error(traceback.format_exc())
                # If we've sent at least one chunk successfully, continue
                # Otherwise, stop to avoid infinite loop
                if successful_chunks == 0:
                    logger.error(f"No successful chunks yet, stopping after error")
                    # Перед выходом пробуем сохранить то, что уже есть, в кэш
                    try:
                        if cache_message_ids and safe_quality_key:
                            original_text = message.text or message.caption or ""
                            _save_video_cache_with_logging(
                                url, safe_quality_key, cache_message_ids,
                                original_text=original_text, user_id=user_id
                            )
                    except Exception as e2:
                        logger.error(f"Error saving live stream cache on first-chunk error: {e2}")
                    break
                # Continue with next chunk
                continue
            
            # Check if we've reached max duration
            elapsed_time = time.time() - start_time
            if elapsed_time >= max_duration:
                logger.info(f"Reached max duration limit ({max_duration}s), stopping")
                break
        
        # Final progress update
        try:
            from HELPERS.safe_messeger import safe_edit_message_text
            final_text = (
                f"{current_total_process}\n"
                f"{messages.LIVE_STREAM_DOWNLOAD_COMPLETE_MSG}\n"
                f"{messages.LIVE_STREAM_CHUNKS_DOWNLOADED_MSG.format(chunks=successful_chunks)}\n"
                f"{messages.LIVE_STREAM_TOTAL_DURATION_MSG.format(duration=int(accumulated_duration))}"
            )
            safe_edit_message_text(user_id, proc_msg_id, final_text)
        except Exception as e:
            logger.error(f"Error updating final progress: {e}")
        
        # Сохраняем все присланные куски (и подкуски) в видеокэш,
        # чтобы при повторном присылании того же URL они репостились из лог‑канала.
        try:
            if cache_message_ids and safe_quality_key:
                original_text = message.text or message.caption or ""
                _save_video_cache_with_logging(
                    url, safe_quality_key, cache_message_ids,
                    original_text=original_text, user_id=user_id
                )
        except Exception as e:
            logger.error(f"Error saving live stream cache in finalizer: {e}")
        
        logger.info(f"Live stream download completed: {successful_chunks} chunks downloaded, total duration: {accumulated_duration}s")
        return successful_chunks > 0
        
    except Exception as e:
        logger.error(f"Error in download_live_stream_chunked: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False

