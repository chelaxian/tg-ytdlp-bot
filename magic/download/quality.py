"""Quality management functions"""
import logging

logger = logging.getLogger(__name__)

# --- receiving formats and metadata via yt-dlp ---
def get_video_formats(url, user_id=None, playlist_start_index=1):
    ytdl_opts = {
        'quiet': True,
        'skip_download': True,
        'forcejson': True,
        'no_warnings': True,
        'extract_flat': False,
        'simulate': True,
        'playlist_items': str(playlist_start_index),
    }
    if user_id is not None:
        user_dir = os.path.join("users", str(user_id))
        cookie_file = os.path.join(user_dir, os.path.basename(Config.COOKIE_FILE_PATH))
        if os.path.exists(cookie_file):
            ytdl_opts['cookiefile'] = cookie_file
    try:
        with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        if 'entries' in info and info.get('entries'):
            return info['entries'][0]
        return info
    except yt_dlp.utils.DownloadError as e:
        error_text = str(e)
        return {'error': error_text}
    except Exception as e:
        return {'error': str(e)}


# --- Always ask processing ---
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

def ask_quality_menu(app, message, url, tags, playlist_start_index=1):
    user_id = message.chat.id
    proc_msg = None
    try:
        proc_msg = app.send_message(user_id, "Processing... ♻️", reply_to_message_id=message.id, reply_markup=get_main_reply_keyboard())
        original_text = message.text or message.caption or ""
        is_playlist = is_playlist_with_range(original_text)
        playlist_range = None
        if is_playlist:
            _, video_start_with, video_end_with, _, _, _, _ = extract_url_range_tags(original_text)
            playlist_range = (video_start_with, video_end_with)
            cached_qualities = get_cached_playlist_qualities(get_clean_playlist_url(url))
        else:
            cached_qualities = get_cached_qualities(url)
        info = get_video_formats(url, user_id, playlist_start_index)
        title = info.get('title', 'Video')
        video_id = info.get('id')
        tags_text = generate_final_tags(url, tags, info)
        thumb_path = None
        user_dir = os.path.join("users", str(user_id))
        create_directory(user_dir)
        if ("youtube.com" in url or "youtu.be" in url) and video_id:
            thumb_path = os.path.join(user_dir, f"yt_thumb_{video_id}.jpg")
            try:
                download_thumbnail(video_id, thumb_path)
            except Exception:
                thumb_path = None
        # --- Table with qualities and sizes ---
        popular = [144, 240, 360, 480, 540, 576, 720, 1080, 1440, 2160, 4320]
        # popular_sizes = [[256,144],[426,240],[640,360],[854,480],[960,540],[1024,576],[1280,720],[1920,1080],[2560,1440],[3840,2160],[7680,4320]]
        minside_size_dim_map = {}
        for f in info.get('formats', []):
            if f.get('vcodec', 'none') != 'none' and f.get('height') and f.get('width'):
                w = f['width']
                h = f['height']
                # Use the get_quality_by_min_side function to determine the quality
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
        table_lines = []
        found_quality_keys = set()
        # Sort by quality from lowest to highest
        for (quality_key, w, h), size_val in sorted(minside_size_dim_map.items(), key=lambda x: sort_quality_key(x[0][0])):
            found_quality_keys.add(quality_key)
            size_str = f"{round(size_val/1024, 1)}GB" if size_val >= 1024 else f"{size_val}MB"
            dim_str = f" ({w}×{h})"
            scissors = ""
            if get_user_split_size(user_id):
                video_bytes = size_val * 1024 * 1024
                if video_bytes > get_user_split_size(user_id):
                    n_parts = (video_bytes + get_user_split_size(user_id) - 1) // get_user_split_size(user_id)
                    scissors = f" ✂️{n_parts}"
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
        # --- Forming caption ---
        cap = f"<b>{title}</b>\n"
        if tags_text:
            cap += f"{tags_text}\n"
        # Block with qualities
        if table_block:
            cap += f"\n<blockquote>{table_block}</blockquote>\n"
        # Hint as a separate code block at the very bottom
        hint = "<pre language=\"info\">📹 — Choose quality for new download.\n🚀 — Instant repost. Video is already saved.</pre>"
        cap += f"\n{hint}\n"
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
        if not buttons and popular:
            for height in popular:
                quality_key = f"{height}p"
                # Find the file size for this quality
                size_val = None
                for (qk, w, h), size in minside_size_dim_map.items():
                    if qk == quality_key:
                        size_val = size
                        break
                
                if size_val is None:
                    continue
                    
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
        if not buttons:
            quality_key = "best"
            if is_playlist and playlist_range:
                indices = list(range(playlist_range[0], playlist_range[1]+1))
                n_cached = get_cached_playlist_count(get_clean_playlist_url(url), quality_key, indices)
                total = len(indices)
                icon = "🚀" if n_cached > 0 else "📹"
                postfix = f" ({n_cached}/{total})" if total > 1 else ""
                button_text = f"{icon} Best Quality{postfix}"
            else:
                icon = "🚀" if quality_key in cached_qualities else "📹"
                button_text = f"{icon} Best Quality"
            buttons.append(InlineKeyboardButton(button_text, callback_data=f"askq|{quality_key}"))
        # --- Form rows of 3 buttons ---
        keyboard_rows = []
        for i in range(0, len(buttons), 3):
            keyboard_rows.append(buttons[i:i+3])
        # --- button mp3 ---
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
        # cap already contains a hint and a table
        app.delete_messages(user_id, proc_msg.id)
        proc_msg = None
        if thumb_path and os.path.exists(thumb_path):
            app.send_photo(user_id, thumb_path, caption=cap, parse_mode=enums.ParseMode.HTML, reply_markup=keyboard, reply_to_message_id=message.id)
        else:
            app.send_message(user_id, cap, parse_mode=enums.ParseMode.HTML, reply_markup=keyboard, reply_to_message_id=message.id)
        send_to_logger(message, f"Always Ask menu sent for {url}")
    except FloodWait as e:
        wait_time = e.value
        user_dir = os.path.join("users", str(user_id))
        create_directory(user_dir)
        flood_time_file = os.path.join(user_dir, "flood_wait.txt")
        with open(flood_time_file, 'w') as f:
            f.write(str(wait_time))
        hours = wait_time // 3600
        minutes = (wait_time % 3600) // 60
        seconds = wait_time % 60
        time_str = f"{hours}h {minutes}m {seconds}s"
        flood_msg = f"⚠️ Telegram has limited message sending.\n\n⏳ Please wait: {time_str}\n\nTo update timer send URL again 2 times."
        if proc_msg:
            try:
                app.edit_message_text(chat_id=user_id, message_id=proc_msg.id, text=flood_msg)
            except Exception as e:
                if 'MESSAGE_ID_INVALID' not in str(e):
                    logger.warning(f"Failed to edit message: {e}")
            proc_msg = None
        else:
            app.send_message(user_id, flood_msg, reply_to_message_id=message.id)
        return
    except Exception as e:
        error_text = f"❌ Error retrieving video information:\n{e}\n> Try the /clean command and try again. If the error persists, YouTube requires authorization. Update cookies.txt via /download_cookie or /cookies_from_browser and try again."
        try:
            if proc_msg:
                result = app.edit_message_text(chat_id=user_id, message_id=proc_msg.id, text=error_text)
                if result is None:
                    app.send_message(user_id, error_text, reply_to_message_id=message.id)
            else:
                app.send_message(user_id, error_text, reply_to_message_id=message.id)
        except Exception as e2:
            logger.error(f"Error sending error message: {e2}")
            app.send_message(user_id, error_text, reply_to_message_id=message.id)
        send_to_logger(message, f"Always Ask menu error for {url}: {e}")
        return


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
            # If the smaller
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


# round height to popular quality for cache only
# --- Round height to nearest higher popular quality ---
def ceil_to_popular(h):
    popular = [144, 240, 360, 480, 540, 576, 720, 1080, 1440, 2160, 4320]
    for p in popular:
        if h <= p:
            return p
    return popular[-1]
