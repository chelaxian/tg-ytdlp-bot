"""
Quality selection handlers - handles video quality selection callbacks
"""
import re
from pyrogram import filters, enums
from pyrogram.types import CallbackQuery
from config import Config
from ..database.firebase import logger
from ..download.cache import get_cached_message_ids, save_to_video_cache, get_cached_playlist_videos, get_clean_playlist_url
from ..processing.url_parser import is_playlist_with_range
from ..processing.tags import extract_url_range_tags
from ..download.downloader import down_and_audio, down_and_up
from ..utils.communication import send_to_logger


def reply_with_keyboard(func):
    """Decorator to add main keyboard to responses"""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@reply_with_keyboard
def askq_callback(app, callback_query):
    """Handle quality selection callbacks - CRITICAL FUNCTION"""
    logger.info(f"[ASKQ] callback: {callback_query.data}")
    user_id = callback_query.from_user.id
    data = callback_query.data.split("|")[1]

    if data == "cancel":
        callback_query.message.delete()
        callback_query.answer("Menu closed.")
        return

    original_message = callback_query.message.reply_to_message
    if not original_message:
        callback_query.answer("❌ Error: Original message not found. It might have been deleted. Please send the link again.", show_alert=True)
        callback_query.message.delete()
        return

    url = None
    if callback_query.message.caption_entities:
        for entity in callback_query.message.caption_entities:
            if entity.type == enums.MessageEntityType.TEXT_LINK and entity.url:
                url = entity.url
                break
    if not url and callback_query.message.reply_to_message:
        url_match = re.search(r'https?://[^\s\*#]+', callback_query.message.reply_to_message.text)
        if url_match:
            url = url_match.group(0)
    if not url:
        callback_query.answer("❌ Error: Original URL not found. Please send the link again.", show_alert=True)
        callback_query.message.delete()
        return

    tags = []
    caption_text = callback_query.message.caption
    if caption_text:
        tag_matches = re.findall(r'#\S+', caption_text)
        if tag_matches:
            tags = tag_matches
    tags_text = ' '.join(tags)

    callback_query.message.delete()

    original_text = original_message.text or original_message.caption or ""
    if is_playlist_with_range(original_text):
        logger.info(f"Playlist with range detected, checking playlist cache for URL: {url}")
        _, video_start_with, video_end_with, playlist_name, _, _, tag_error = extract_url_range_tags(original_text)
        video_count = video_end_with - video_start_with + 1
        requested_indices = list(range(video_start_with, video_start_with + video_count))
        
        # Check cache for selected quality
        cached_videos = get_cached_playlist_videos(get_clean_playlist_url(url), data, requested_indices)
        uncached_indices = [i for i in requested_indices if i not in cached_videos]
        used_quality_key = data
        
        # If there is no cache for the selected quality, try fallback to best
        if not cached_videos and data != "best":
            logger.info(f"askq_callback: no cache for quality_key={data}, trying fallback to best")
            best_cached = get_cached_playlist_videos(get_clean_playlist_url(url), "best", requested_indices)
            if best_cached:
                cached_videos = best_cached
                used_quality_key = "best"
                uncached_indices = [i for i in requested_indices if i not in cached_videos]
                logger.info(f"askq_callback: found cache with best quality, cached: {list(cached_videos.keys())}, uncached: {uncached_indices}")
        
        if cached_videos:
            # Reposting cached videos
            callback_query.answer("🚀 Found in cache! Reposting...", show_alert=False)
            for index in requested_indices:
                if index in cached_videos:
                    try:
                        app.forward_messages(
                            chat_id=user_id,
                            from_chat_id=Config.LOGS_ID,
                            message_ids=[cached_videos[index]]
                        )
                    except Exception as e:
                        logger.warning(f"askq_callback: cached video for index {index} not found: {e}")
            
            # If there are missing videos - download them
            if uncached_indices:
                logger.info(f"askq_callback: we start downloading the missing indexes: {uncached_indices}")
                new_start = uncached_indices[0]
                new_end = uncached_indices[-1]
                new_count = new_end - new_start + 1
                
                if data == "mp3":
                    down_and_audio(app, original_message, url, tags, quality_key=used_quality_key, playlist_name=playlist_name, video_count=new_count, video_start_with=new_start)
                else:
                    # Form the correct format for the missing videos
                    if used_quality_key == "best":
                        format_override = "bestvideo+bestaudio/best"
                    else:
                        try:
                            quality_str = used_quality_key.replace('p', '')
                            quality_val = int(quality_str)
                            format_override = f"bestvideo[height<={quality_val}][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<={quality_val}]+bestaudio/best[height<={quality_val}]/best"
                        except ValueError:
                            format_override = "bestvideo+bestaudio/best"
                    
                    down_and_up(app, original_message, url, playlist_name, new_count, new_start, tags_text, force_no_title=False, format_override=format_override, quality_key=used_quality_key)
            else:
                # All videos were in the cache
                app.send_message(user_id, f"✅ Sent from cache: {len(cached_videos)}/{len(requested_indices)} files.", reply_to_message_id=original_message.id)
                media_type = "Audio" if data == "mp3" else "Video"
                log_msg = f"{media_type} playlist sent from cache to user.\nURL: {url}\nUser: {callback_query.from_user.first_name} ({user_id})"
                send_to_logger(original_message, log_msg)
            return
        else:
            # If there is no cache at all - download everything again
            logger.info(f"askq_callback: no cache found for any quality, starting new download")
            if data == "mp3":
                down_and_audio(app, original_message, url, tags, quality_key=data, playlist_name=playlist_name, video_count=video_count, video_start_with=video_start_with)
            else:
                # Form the correct format for the new download
                if data == "best":
                    format_override = "bestvideo+bestaudio/best"
                else:
                    try:
                        quality_str = data.replace('p', '')
                        quality_val = int(quality_str)
                        format_override = f"bestvideo[height<={quality_val}][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<={quality_val}]+bestaudio/best[height<={quality_val}]/best"
                    except ValueError:
                        format_override = "bestvideo+bestaudio/best"
                
                down_and_up(app, original_message, url, playlist_name, video_count, video_start_with, tags_text, force_no_title=False, format_override=format_override, quality_key=data)
            return
    # --- other logic for single files ---
    message_ids = get_cached_message_ids(url, data)
    if message_ids:
        callback_query.answer("🚀 Found in cache! Forwarding instantly...", show_alert=False)
        try:
            app.forward_messages(
                chat_id=user_id,
                from_chat_id=Config.LOGS_ID,
                message_ids=message_ids
            )
            app.send_message(user_id, "✅ Video successfully sent from cache.", reply_to_message_id=original_message.id)
            media_type = "Audio" if data == "mp3" else "Video"
            log_msg = f"{media_type} sent from cache to user.\nURL: {url}\nUser: {callback_query.from_user.first_name} ({user_id})"
            send_to_logger(original_message, log_msg)
            return
        except Exception as e:
            logger.error(f"Error forwarding from cache: {e}")
            save_to_video_cache(url, data, [], clear=True)
            app.send_message(user_id, "⚠️ Failed to get video from cache, starting a new download...", reply_to_message_id=original_message.id)
            askq_callback_logic(app, callback_query, data, original_message, url, tags_text)
        return
    askq_callback_logic(app, callback_query, data, original_message, url, tags_text)


def askq_callback_logic(app, callback_query, data, original_message, url, tags_text):
    """Logic for handling quality callback when no cache found"""
    from ..download.quality import get_video_formats, get_quality_by_min_side, get_real_height_for_quality
    
    user_id = callback_query.from_user.id
    tags = tags_text.split() if tags_text else []
    if data == "mp3":
        callback_query.answer("Downloading audio...")
        # Extract playlist parameters from the original message
        full_string = original_message.text or original_message.caption or ""
        _, video_start_with, video_end_with, playlist_name, _, _, tag_error = extract_url_range_tags(full_string)
        video_count = video_end_with - video_start_with + 1
        down_and_audio(app, original_message, url, tags, quality_key="mp3", playlist_name=playlist_name, video_count=video_count, video_start_with=video_start_with)
        return
    
    # Logic for forming the format with the real height
    if data == "best":
        callback_query.answer("Downloading best quality...")
        fmt = "bestvideo+bestaudio/best"
        quality_key = "best"
    else:
        try:
            # Get information about the video to determine the sizes
            info = get_video_formats(url, user_id)
            formats = info.get('formats', [])
            
            # Find the format with the highest quality to determine the sizes
            max_width = 0
            max_height = 0
            for f in formats:
                if f.get('width') and f.get('height'):
                    if f['width'] > max_width:
                        max_width = f['width']
                    if f['height'] > max_height:
                        max_height = f['height']
            
            # If the sizes are not found, use the standard logic
            if max_width == 0 or max_height == 0:
                quality_str = data.replace('p', '')
                quality_val = int(quality_str)
                fmt = f"bestvideo[height<={quality_val}][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<={quality_val}]+bestaudio/best[height<={quality_val}]/best"
            else:
                # Determine the quality by the smaller side
                min_side_quality = get_quality_by_min_side(max_width, max_height)
                
                # If the selected quality does not match the smaller side, use the standard logic
                if data != min_side_quality:
                    quality_str = data.replace('p', '')
                    quality_val = int(quality_str)
                    fmt = f"bestvideo[height<={quality_val}][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<={quality_val}]+bestaudio/best[height<={quality_val}]/best"
                else:
                    # Use the real height to form the format
                    real_height = get_real_height_for_quality(data, max_width, max_height)
                    fmt = f"bestvideo[height<={real_height}][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<={real_height}]+bestaudio/best[height<={real_height}]/best"
        except Exception as e:
            logger.error(f"Error in quality processing: {e}")
            quality_str = data.replace('p', '')
            quality_val = int(quality_str)
            fmt = f"bestvideo[height<={quality_val}][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<={quality_val}]+bestaudio/best[height<={quality_val}]/best"
        
        callback_query.answer(f"Downloading {data} quality...")
        quality_key = data
    
    down_and_up_with_format(app, original_message, url, fmt, tags_text, quality_key=quality_key)


def down_and_up_with_format(app, message, url, fmt, tags_text, quality_key=None):
    """Download with specific format - auxiliary function"""
    from ..processing.url_parser import is_tiktok_url
    
    # We extract the range and other parameters from the original user message
    full_string = message.text or message.caption or ""
    _, video_start_with, video_end_with, playlist_name, _, _, tag_error = extract_url_range_tags(full_string)

    # This mistake should have already been caught earlier, but for safety
    if tag_error:
        wrong, example = tag_error
        app.send_message(message.chat.id, f"❌ Tag #{wrong} contains forbidden characters. Only letters, digits and _ are allowed.\nPlease use: {example}", reply_to_message_id=message.id)
        return

    video_count = video_end_with - video_start_with + 1
    
    # Check if there is a link to Tiktok
    is_tiktok = is_tiktok_url(url)

    # We call the main function of loading with the correct parameters of the playlist
    down_and_up(app, message, url, playlist_name, video_count, video_start_with, tags_text, force_no_title=is_tiktok, format_override=fmt, quality_key=quality_key)


def register_quality_handlers(app):
    """Register quality selection handlers"""
    
    @app.on_callback_query(filters.regex(r"^askq\|"))
    def askq_handler(app, callback_query):
        askq_callback(app, callback_query) 