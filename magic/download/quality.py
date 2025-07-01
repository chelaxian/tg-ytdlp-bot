"""
Video quality management and format selection
"""
import os
import yt_dlp
from pyrogram import enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
from ..database.firebase import logger
from ..utils.communication import send_to_all, send_to_logger
from ..utils.formatters import humanbytes
from ..utils.filesystem import create_directory
from ..processing.tags import generate_final_tags
from .cache import get_cached_playlist_count, get_cached_qualities, get_clean_playlist_url
from ..user.settings import get_user_split_size


def sort_quality_key(quality_key):
    """Sort qualities by increasing resolution from lower to higher"""
    if quality_key == "best":
        return 999999  # best is always at the end
    elif quality_key == "mp3":
        return -1  # mp3 at the very beginning
    else:
        # Extract a number from a string (e.g. "720p" -> 720)
        try:
            return int(quality_key.replace('p', ''))
        except ValueError:
            return 0  # for unknown formats


def get_video_formats(url, user_id=None, playlist_start_index=1):
    """Get available video formats for a URL"""
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
        }
        
        if Config.COOKIES_FILE_PATH and os.path.exists(Config.COOKIES_FILE_PATH):
            ydl_opts['cookiefile'] = Config.COOKIES_FILE_PATH
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            return info_dict
            
    except Exception as e:
        logger.error(f"Error getting video formats: {e}")
        return None


def get_quality_by_min_side(width: int, height: int) -> str:
    """
    Determines the quality by the smaller side of the video.
    Works for both horizontal and vertical videos.
    For example, for 1280×720 returns '720p', for 720×1280 also '720p'.
    """
    min_side = min(width, height)
    quality_map = {
        144: "144p", 256: "144p",
        240: "240p", 426: "240p",
        480: "480p", 854: "480p",
        540: "540p", 960: "540p",
        576: "576p", 1024: "576p",
        720: "720p", 1280: "720p",
        1080: "1080p", 1920: "1080p",
        1440: "1440p", 2560: "1440p",
        2160: "2160p", 3840: "2160p",
        4320: "4320p", 7680: "4320p"
    }
    return quality_map.get(min_side, "best")


def get_real_height_for_quality(quality: str, width: int, height: int) -> int:
    """
    Returns the real height for the given quality, considering the video orientation.
    For example, for quality '720p' and video 1280×720 returns 720, for 720×1280 returns 1280.
    """
    if quality == "best":
        return height  # For best, we use the real height

    try:
        quality_val = int(quality.replace('p', ''))
        # Determine which side corresponds to the selected quality
        if min(width, height) == quality_val:
            # If the smaller side matches
            return height
        else:
            # Otherwise, find the corresponding height
            quality_map = {
                144: [144, 256],
                240: [240, 426],
                480: [480, 854],
                540: [540, 960],
                576: [576, 1024],
                720: [720, 1280],
                1080: [1080, 1920],
                1440: [1440, 2560],
                2160: [2160, 3840],
                4320: [4320, 7680]
            }
            heights = quality_map.get(quality_val, [quality_val])
            # Select the height that is closest to the real height of the video
            return min(heights, key=lambda h: abs(h - height))
    except ValueError:
        return height


def ceil_to_popular(h):
    """Round height to nearest higher popular quality for cache only"""
    popular = [144, 240, 360, 480, 540, 576, 720, 1080, 1440, 2160, 4320]
    for p in popular:
        if h <= p:
            return p
    return popular[-1]


def ask_quality_menu(app, message, url, tags, playlist_start_index=1):
    """Show quality selection menu to user"""
    user_id = message.chat.id
    proc_msg = None
    
    try:
        proc_msg = app.send_message(
            user_id, 
            "Processing... ♻️", 
            reply_to_message_id=message.id
        )
        
        original_text = message.text or message.caption or ""
        from ..processing.tags import is_playlist_with_range, extract_url_range_tags
        
        is_playlist = is_playlist_with_range(original_text)
        playlist_range = None
        
        if is_playlist:
            _, video_start_with, video_end_with, _, _, _, _ = extract_url_range_tags(original_text)
            playlist_range = (video_start_with, video_end_with)
            cached_qualities = get_cached_playlist_qualities(get_clean_playlist_url(url))
        else:
            cached_qualities = get_cached_qualities(url)
        
        info = get_video_formats(url, user_id, playlist_start_index)
        if not info:
            app.delete_messages(user_id, proc_msg.id)
            send_to_all(message, "❌ Could not get video information")
            return
            
        title = info.get('title', 'Video')
        video_id = info.get('id')
        tags_text = generate_final_tags(url, tags, info)
        
        # Get available qualities and sizes
        popular = [144, 240, 360, 480, 540, 576, 720, 1080, 1440, 2160, 4320]
        minside_size_dim_map = {}
        
        for f in info.get('formats', []):
            if f.get('vcodec', 'none') != 'none' and f.get('height') and f.get('width'):
                w = f['width']
                h = f['height']
                quality_key = get_quality_by_min_side(w, h)
                
                if quality_key != "best":  # Exclude best from display
                    if f.get('filesize'):
                        size_mb = int(f['filesize']) // (1024*1024)
                    elif f.get('filesize_approx'):
                        size_mb = int(f['filesize_approx']) // (1024*1024)
                    else:
                        size_mb = None
                    
                    if size_mb:
                        key = (quality_key, w, h)
                        minside_size_dim_map[key] = size_mb
        
        # Build quality table
        table_lines = []
        found_quality_keys = set()
        
        # Sort by quality from lowest to highest
        for (quality_key, w, h), size_val in sorted(minside_size_dim_map.items(), key=lambda x: sort_quality_key(x[0][0])):
            found_quality_keys.add(quality_key)
            size_str = f"{round(size_val/1024, 1)}GB" if size_val >= 1024 else f"{size_val}MB"
            dim_str = f" ({w}×{h})"
            
            # Check if video will be split
            scissors = ""
            if get_user_split_size(user_id):
                video_bytes = size_val * 1024 * 1024
                if video_bytes > get_user_split_size(user_id):
                    n_parts = (video_bytes + get_user_split_size(user_id) - 1) // get_user_split_size(user_id)
                    scissors = f" ✂️{n_parts}"
            
            # Check cache status
            if is_playlist and playlist_range:
                indices = list(range(playlist_range[0], playlist_range[1]+1))
                n_cached = get_cached_playlist_count(get_clean_playlist_url(url), quality_key, indices)
                total = len(indices)
                postfix = f" ({n_cached}/{total})"
                is_cached = n_cached > 0
            else:
                is_cached = quality_key in cached_qualities
                postfix = ""
            
            emoji = "🚀" if is_cached else "📹"
            table_lines.append(f"{emoji}  {quality_key}:  {size_str}{dim_str}{scissors}{postfix}")
        
        table_block = "\n".join(table_lines)
        
        # Create caption
        cap = f"<b>{title}</b>\n"
        if tags_text:
            cap += f"{tags_text}\n"
        
        # Block with qualities
        if table_block:
            cap += f"\n<blockquote>{table_block}</blockquote>\n"
        
        # Hint
        hint = "<pre language=\"info\">📹 — Choose quality for new download.\n🚀 — Instant repost. Video is already saved.</pre>"
        cap += f"\n{hint}\n"
        
        # Create buttons
        buttons = []
        
        # Sort buttons by quality from lowest to highest
        for quality_key in sorted(found_quality_keys, key=sort_quality_key):
            if is_playlist and playlist_range:
                indices = list(range(playlist_range[0], playlist_range[1]+1))
                n_cached = get_cached_playlist_count(get_clean_playlist_url(url), quality_key, indices)
                total = len(indices)
                icon = "🚀" if n_cached > 0 else "📹"
                postfix = f" ({n_cached}/{total})" if total > 1 else ""
                button_text = f"{icon} {quality_key}{postfix}"
            else:
                icon = "🚀" if quality_key in cached_qualities else "📹"
                button_text = f"{icon} {quality_key}"
            
            buttons.append(InlineKeyboardButton(button_text, callback_data=f"askq|{quality_key}"))
        
        # If no buttons, add fallback qualities
        if not buttons:
            for height in popular:
                quality_key = f"{height}p"
                icon = "🚀" if quality_key in cached_qualities else "📹"
                button_text = f"{icon} {quality_key}"
                buttons.append(InlineKeyboardButton(button_text, callback_data=f"askq|{quality_key}"))
        
        # If still no buttons, add best quality
        if not buttons:
            quality_key = "best"
            icon = "🚀" if quality_key in cached_qualities else "📹"
            button_text = f"{icon} Best Quality"
            buttons.append(InlineKeyboardButton(button_text, callback_data=f"askq|{quality_key}"))
        
        # Form rows of 3 buttons
        keyboard_rows = []
        for i in range(0, len(buttons), 3):
            keyboard_rows.append(buttons[i:i+3])
        
        # Add MP3 button
        quality_key = "mp3"
        if is_playlist and playlist_range:
            indices = list(range(playlist_range[0], playlist_range[1]+1))
            n_cached = get_cached_playlist_count(get_clean_playlist_url(url), quality_key, indices)
            total = len(indices)
            icon = "🚀" if n_cached > 0 else "🎵"
            postfix = f" ({n_cached}/{total})" if total > 1 else ""
            button_text = f"{icon} audio (mp3){postfix}"
        else:
            icon = "🚀" if quality_key in cached_qualities else "🎵"
            button_text = f"{icon} audio (mp3)"
        
        keyboard_rows.append([InlineKeyboardButton(button_text, callback_data=f"askq|{quality_key}")])
        keyboard_rows.append([InlineKeyboardButton("🔙 Cancel", callback_data="askq|cancel")])
        
        keyboard = InlineKeyboardMarkup(keyboard_rows)
        
        # Send quality menu
        app.delete_messages(user_id, proc_msg.id)
        app.send_message(
            user_id, 
            cap, 
            parse_mode=enums.ParseMode.HTML, 
            reply_markup=keyboard, 
            reply_to_message_id=message.id
        )
        
        send_to_logger(message, f"Quality menu sent for {url}")
        
    except Exception as e:
        logger.error(f"Error showing quality menu: {e}")
        if proc_msg:
            try:
                app.edit_message_text(
                    chat_id=user_id, 
                    message_id=proc_msg.id, 
                    text=f"❌ Error: {e}"
                )
            except:
                pass
        else:
            send_to_all(message, f"❌ Error: {e}") 