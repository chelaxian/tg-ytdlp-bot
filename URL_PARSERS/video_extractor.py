# URL Extractor
from HELPERS.app_instance import get_app
from HELPERS.limitter import check_playlist_range_limits
from HELPERS.download_status import get_active_download
from HELPERS.logger import send_to_logger, send_error_to_user, logger
from URL_PARSERS.tags import extract_url_range_tags, save_user_tags, get_auto_tags
from URL_PARSERS.tiktok import is_tiktok_url
from DOWN_AND_UP.always_ask_menu import ask_quality_menu
from DOWN_AND_UP.down_and_up import down_and_up
from HELPERS.download_status import playlist_errors, playlist_errors_lock
from CONFIG.config import Config
from CONFIG.messages import safe_get_messages
from CONFIG.logger_msg import LoggerMsg
from CONFIG.limits import LimitsConfig
import os
from pyrogram.types import ReplyParameters
import hashlib
import re

# Get app instance for decorators
app = get_app()

def extract_multiple_urls(text):
    """
    Extract multiple URLs from text.
    URLs can be on separate lines or separated by spaces.
    Returns list of URLs found in the text.
    """
    if not isinstance(text, str):
        return []
    
    # Pattern to match URLs (http:// or https://)
    url_pattern = r'https?://[^\s\*#]+'
    
    # Find all URLs in the text
    urls = re.findall(url_pattern, text)
    
    # Remove duplicates while preserving order
    seen = set()
    unique_urls = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append(url)
    
    return unique_urls

def process_multiple_urls_queue(app, message, urls, saved_format, is_admin, is_group):
    """
    Process multiple URLs in queue with status display (similar to playlist downloads).
    """
    from HELPERS.safe_messeger import safe_send_message, safe_edit_message_text
    from pyrogram.types import ReplyParameters
    
    user_id = message.chat.id
    messages = safe_get_messages(user_id)
    
    # Calculate limit
    if is_admin:
        url_limit = 0  # 0 means unlimited
    elif is_group:
        url_limit = LimitsConfig.MAX_MULTI_URL_LIMIT * LimitsConfig.GROUP_MULTIPLIER
    else:
        url_limit = LimitsConfig.MAX_MULTI_URL_LIMIT
    
    # Check limit
    if url_limit > 0 and len(urls) > url_limit:
        error_msg = messages.MULTI_URL_LIMIT_EXCEEDED_MSG.format(
            count=len(urls),
            limit=url_limit
        ) if hasattr(messages, 'MULTI_URL_LIMIT_EXCEEDED_MSG') else f"❌ Превышен лимит ссылок: {len(urls)}/{url_limit}"
        safe_send_message(user_id, error_msg, reply_parameters=ReplyParameters(message_id=message.id))
        return
    
    # Send initial status message
    total_urls = len(urls)
    status_msg_text = f"""
<b>📶 {messages.TOTAL_PROGRESS_MSG}</b>
<blockquote>{messages.URL_PROGRESS_MSG.format(current=0, total=total_urls)}</blockquote>
"""
    status_msg = safe_send_message(user_id, status_msg_text, reply_parameters=ReplyParameters(message_id=message.id))
    status_msg_id = status_msg.id if status_msg else None
    
    # Process each URL in queue
    for idx, url in enumerate(urls, 1):
        try:
            # Update status message
            if status_msg_id:
                try:
                    status_msg_text = f"""
<b>📶 {messages.TOTAL_PROGRESS_MSG}</b>
<blockquote>{messages.URL_PROGRESS_MSG.format(current=idx, total=total_urls)}</blockquote>
"""
                    safe_edit_message_text(user_id, status_msg_id, status_msg_text)
                except Exception as e:
                    logger.debug(f"Failed to update status message: {e}")
            
            # Extract URL, range, tags from the URL string
            # For multiple URLs, we treat each URL as a separate message
            url_text = url
            url_parsed, video_start_with, video_end_with, playlist_name, tags, tags_text, tag_error = extract_url_range_tags(url_text)
            
            if tag_error:
                if isinstance(tag_error, tuple) and len(tag_error) == 2:
                    wrong, example = tag_error
                    error_msg = messages.TAG_FORBIDDEN_CHARS_MSG.format(tag=wrong, example=example)
                    safe_send_message(user_id, error_msg, reply_parameters=ReplyParameters(message_id=message.id))
                continue
            
            if not url_parsed:
                continue
            
            # Check blacklist
            for black_item in Config.BLACK_LIST:
                if black_item in url_text:
                    send_error_to_user(message, messages.PORN_CONTENT_CANNOT_DOWNLOAD_MSG)
                    continue
            
            # Check range limits
            if not check_playlist_range_limits(url_parsed, video_start_with, video_end_with, app, message):
                continue
            
            # Wait if there's an active download
            while get_active_download(user_id):
                import time
                time.sleep(1)
            
            # Process tags
            is_tiktok = is_tiktok_url(url_parsed)
            auto_tags = get_auto_tags(url_parsed, tags)
            all_tags = tags + auto_tags
            tags_text_full = ' '.join(all_tags)
            
            # Calculate video_count
            if video_start_with < 0 and video_end_with < 0:
                video_count = abs(video_end_with) - abs(video_start_with) + 1
            elif video_start_with > video_end_with:
                video_count = abs(video_start_with - video_end_with) + 1
            else:
                video_count = video_end_with - video_start_with + 1
            
            if playlist_name:
                with playlist_errors_lock:
                    error_key = f"{user_id}_{playlist_name}"
                    if error_key in playlist_errors:
                        del playlist_errors[error_key]
            
            save_user_tags(user_id, all_tags)
            
            # Create quality_key based on saved format
            quality_key = None
            if saved_format:
                if "height=144" in saved_format or "height<=144" in saved_format:
                    quality_key = "144p"
                elif "height=240" in saved_format or "height<=240" in saved_format:
                    quality_key = "240p"
                elif "height=360" in saved_format or "height<=360" in saved_format:
                    quality_key = "360p"
                elif "height=480" in saved_format or "height<=480" in saved_format:
                    quality_key = "480p"
                elif "height=720" in saved_format or "height<=720" in saved_format:
                    quality_key = "720p"
                elif "height=1080" in saved_format or "height<=1080" in saved_format:
                    quality_key = "1080p"
                elif "height=1440" in saved_format or "height<=1440" in saved_format:
                    quality_key = "1440p"
                elif "height=2160" in saved_format or "height<=2160" in saved_format:
                    quality_key = "2160p"
                elif "height=4320" in saved_format or "height<=4320" in saved_format:
                    quality_key = "4320p"
                elif "bestvideo+bestaudio" in saved_format or "bv*[vcodec*=avc1]+ba" in saved_format or "bv*[vcodec*=av01]+ba" in saved_format:
                    quality_key = "bestvideo"
                elif saved_format == "best":
                    quality_key = "best"
                else:
                    quality_key = f"custom_{hashlib.md5(saved_format.encode()).hexdigest()[:8]}"
            
            # Create a fake message for this URL
            from HELPERS.safe_messeger import fake_message
            fake_msg = fake_message(url_text, user_id, original_chat_id=message.chat.id, 
                                   message_thread_id=getattr(message, 'message_thread_id', None),
                                   original_message=message)
            
            # Download the URL
            if is_tiktok:
                down_and_up(app, fake_msg, url_parsed, playlist_name, video_count, video_start_with, 
                           tags_text_full, force_no_title=True, format_override=saved_format, 
                           quality_key=quality_key, cached_video_info=None)
            else:
                down_and_up(app, fake_msg, url_parsed, playlist_name, video_count, video_start_with, 
                           tags_text_full, format_override=saved_format, quality_key=quality_key, 
                           cached_video_info=None)
            
        except Exception as e:
            logger.error(f"Error processing URL {idx}/{total_urls} ({url}): {e}")
            continue
    
    # Update final status
    if status_msg_id:
        try:
            final_status = f"""
<b>📶 {messages.TOTAL_PROGRESS_MSG}</b>
<blockquote>{messages.URL_PROGRESS_MSG.format(current=total_urls, total=total_urls)}</blockquote>
✅ {messages.MULTI_URL_COMPLETED_MSG if hasattr(messages, 'MULTI_URL_COMPLETED_MSG') else 'Обработка завершена'}
"""
            safe_edit_message_text(user_id, status_msg_id, final_status)
        except Exception as e:
            logger.debug(f"Failed to update final status: {e}")

# Called from url_distractor - no decorator needed
def video_url_extractor(app, message):
    user_id = message.chat.id
    user_dir = os.path.join("users", str(user_id))
    
    # Create user directory (subscription already checked in url_distractor)
    if not os.path.exists(user_dir):
        os.makedirs(user_dir, exist_ok=True)
    format_file = os.path.join(user_dir, "format.txt")

    # By default, ask for quality if a specific format is not selected
    should_ask = True
    saved_format = None
    if os.path.exists(format_file):
        with open(format_file, "r", encoding="utf-8") as f:
            fmt = f.read().strip()
        # Do not ask only if the format is set and it is NOT "ALWAYS_ASK"
        if fmt != "ALWAYS_ASK":
            should_ask = False
            saved_format = fmt

    if should_ask:
        full_string = message.text
        logger.info(f"🔍 [DEBUG] video_extractor: full_string='{full_string}'")
        # In Always Ask mode, process only the first URL
        url, video_start_with, video_end_with, _, tags, _, tag_error = extract_url_range_tags(full_string)
        logger.info(f"🔍 [DEBUG] video_extractor: после extract_url_range_tags: url='{url}', video_start_with={video_start_with}, video_end_with={video_end_with}")
        # Add tag error check
        if tag_error:
            if isinstance(tag_error, tuple) and len(tag_error) == 2:
                wrong, example = tag_error
                error_msg = safe_get_messages(user_id).TAG_FORBIDDEN_CHARS_MSG.format(tag=wrong, example=example)
                app.send_message(user_id, error_msg, reply_parameters=ReplyParameters(message_id=message.id))
                from HELPERS.logger import log_error_to_channel
                log_error_to_channel(message, error_msg)
            return
        # Если есть диапазон, используем video_start_with из парсинга, иначе 1
        # ask_quality_menu сам определит диапазон из original_text и обновит playlist_start_index
        # Для отрицательных индексов проверяем, что хотя бы одно число не равно 1
        has_range = (video_start_with != 1 or video_end_with != 1) or (video_start_with < 0 or video_end_with < 0)
        playlist_start_index = video_start_with if has_range else 1
        logger.info(f"🔍 [DEBUG] video_extractor: video_start_with={video_start_with}, video_end_with={video_end_with}, has_range={has_range}, playlist_start_index={playlist_start_index}")
        ask_quality_menu(app, message, url, tags, playlist_start_index)
        return

    # This code is executed only if the user has selected a specific format
    with playlist_errors_lock:
        keys_to_remove = [k for k in playlist_errors if k.startswith(f"{user_id}_")]
        for key in keys_to_remove:
            del playlist_errors[key]
            
    if get_active_download(user_id):
        app.send_message(user_id, safe_get_messages(user_id).VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG, reply_parameters=ReplyParameters(message_id=message.id))
        return
        
    full_string = message.text
    
    # Check if this is a group chat
    is_group = message.chat.id < 0
    is_admin = int(user_id) in Config.ADMIN
    
    # Extract multiple URLs if in non-Always Ask mode
    all_urls = extract_multiple_urls(full_string)
    
    # If multiple URLs found, process them in queue
    if len(all_urls) > 1:
        logger.info(f"🔍 [DEBUG] video_extractor: Found {len(all_urls)} URLs, processing in queue mode")
        process_multiple_urls_queue(app, message, all_urls, saved_format, is_admin, is_group)
        return
    
    # Single URL processing (original logic)
    # Also add tag error check here
    url, video_start_with, video_end_with, playlist_name, tags, tags_text, tag_error = extract_url_range_tags(full_string)
    if tag_error:
        if isinstance(tag_error, tuple) and len(tag_error) == 2:
            wrong, example = tag_error
            error_msg = safe_get_messages(user_id).TAG_FORBIDDEN_CHARS_MSG.format(tag=wrong, example=example)
            app.send_message(user_id, error_msg, reply_parameters=ReplyParameters(message_id=message.id))
            from HELPERS.logger import log_error_to_channel
            log_error_to_channel(message, error_msg)
        return
    
    # Checking the range limit
    if not check_playlist_range_limits(url, video_start_with, video_end_with, app, message):
        return
    
    if url:
        users_first_name = message.chat.first_name
        send_to_logger(message, safe_get_messages(user_id).URL_PARSER_USER_ENTERED_URL_LOG_MSG.format(user_name=users_first_name, url=full_string))
        for j in range(len(Config.BLACK_LIST)):
            if Config.BLACK_LIST[j] in full_string:
                send_error_to_user(message, safe_get_messages(user_id).PORN_CONTENT_CANNOT_DOWNLOAD_MSG)
                return
        # --- TikTok: auto-tag profile and no title ---
        is_tiktok = is_tiktok_url(url)
        auto_tags = get_auto_tags(url, tags)
        all_tags = tags + auto_tags
        tags_text_full = ' '.join(all_tags)
        # Правильное вычисление video_count для отрицательных индексов
        if video_start_with < 0 and video_end_with < 0:
            # Для отрицательных индексов: -1 до -7 = 7 элементов (от последнего к 7-му с конца)
            video_count = abs(video_end_with) - abs(video_start_with) + 1
        elif video_start_with > video_end_with:
            # Для обратного порядка: считаем абсолютную разницу
            video_count = abs(video_start_with - video_end_with) + 1
        else:
            # Для прямого порядка: обычная формула
            video_count = video_end_with - video_start_with + 1
        if playlist_name:
            with playlist_errors_lock:
                error_key = f"{user_id}_{playlist_name}"
                if error_key in playlist_errors:
                    del playlist_errors[error_key]
        save_user_tags(user_id, all_tags)
        
        # Create quality_key based on saved format for caching
        quality_key = None
        if saved_format:
            # Convert format to quality_key for caching
            # First check for exact height matches, then for <= matches
            if "height=144" in saved_format:
                quality_key = "144p"
            elif "height=240" in saved_format:
                quality_key = "240p"
            elif "height=360" in saved_format:
                quality_key = "360p"
            elif "height=480" in saved_format:
                quality_key = "480p"
            elif "height=720" in saved_format:
                quality_key = "720p"
            elif "height=1080" in saved_format:
                quality_key = "1080p"
            elif "height=1440" in saved_format:
                quality_key = "1440p"
            elif "height=2160" in saved_format:
                quality_key = "2160p"
            elif "height=4320" in saved_format:
                quality_key = "4320p"
            elif "height<=144" in saved_format:
                quality_key = "144p"
            elif "height<=240" in saved_format:
                quality_key = "240p"
            elif "height<=360" in saved_format:
                quality_key = "360p"
            elif "height<=480" in saved_format:
                quality_key = "480p"
            elif "height<=720" in saved_format:
                quality_key = "720p"
            elif "height<=1080" in saved_format:
                quality_key = "1080p"
            elif "height<=1440" in saved_format:
                quality_key = "1440p"
            elif "height<=2160" in saved_format:
                quality_key = "2160p"
            elif "height<=4320" in saved_format:
                quality_key = "4320p"
            elif "bestvideo+bestaudio" in saved_format or "bv*[vcodec*=avc1]+ba" in saved_format or "bv*[vcodec*=av01]+ba" in saved_format:
                quality_key = "bestvideo"
            elif saved_format == "best":
                quality_key = "best"
            else:
                # For custom formats, we use the format hash as quality_key
                quality_key = f"custom_{hashlib.md5(saved_format.encode()).hexdigest()[:8]}"
        
        logger.info(LoggerMsg.VIDEO_EXTRACTOR_SAVED_FORMAT_LOG_MSG.format(saved_format=saved_format, quality_key=quality_key))
        
        # --- Pass title='' for TikTok, otherwise as usual ---
        # Note: cached_video_info=None for direct calls (no optimization available)
        if is_tiktok:
            down_and_up(app, message, url, playlist_name, video_count, video_start_with, tags_text_full, force_no_title=True, format_override=saved_format, quality_key=quality_key, cached_video_info=None)
        else:
            down_and_up(app, message, url, playlist_name, video_count, video_start_with, tags_text_full, format_override=saved_format, quality_key=quality_key, cached_video_info=None)
    else:
        send_error_to_user(message, safe_get_messages(user_id).URL_PARSER_USER_ENTERED_INVALID_MSG.format(input=full_string, error_msg=safe_get_messages(user_id).ERROR1))
