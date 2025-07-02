"""Settings handlers"""
import logging
import os
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import Config
from magic.utils.helpers import reply_with_keyboard
from magic.database.firebase import fake_message
from magic.utils.communication import send_to_logger
from magic.handlers.user_cmd import app, url_distractor, cookies_from_browser, set_format, tags_command, command2, playlist_command
from magic.download.quality import askq_callback_logic

logger = logging.getLogger(__name__)

# ===================== /settings =====================
@app.on_message(filters.command("settings") & filters.private)
@reply_with_keyboard
def settings_command(app, message):
    user_id = message.chat.id
    # Main settings menu
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🧹 CLEAN", callback_data="settings__menu__clean")],
        [InlineKeyboardButton("🍪 COOKIES", callback_data="settings__menu__cookies")],
        [InlineKeyboardButton("🎞 MEDIA", callback_data="settings__menu__media")],
        [InlineKeyboardButton("📖 INFO", callback_data="settings__menu__logs")],
        [InlineKeyboardButton("🔙 Close", callback_data="settings__menu__close")]
    ])
    app.send_message(
        user_id,
        "<b>Bot Settings</b>\n\nChoose a category:",
        reply_markup=keyboard,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=message.id
    )
    send_to_logger(message, "Opened /settings menu")

@app.on_callback_query(filters.regex(r"^settings__menu__"))
@reply_with_keyboard
def settings_menu_callback(app, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data.split("__")[-1]
    if data == "close":
        callback_query.message.delete()
        callback_query.answer("Menu closed.")
        return
    if data == "clean":
        # Show the cleaning menu
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🍪 Cookies", callback_data="clean_option|cookies")],
            [InlineKeyboardButton("📃 Logs ", callback_data="clean_option|logs")],
            [InlineKeyboardButton("#️⃣ Tags", callback_data="clean_option|tags")],
            [InlineKeyboardButton("📼 Format", callback_data="clean_option|format")],
            [InlineKeyboardButton("✂️ Split", callback_data="clean_option|split")],
            [InlineKeyboardButton("📊 Mediainfo", callback_data="clean_option|mediainfo")],
            [InlineKeyboardButton("🗑  All files", callback_data="clean_option|all")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__back")]
        ])
        callback_query.edit_message_text(
            "<b>🧹 Clean Options</b>\n\nChoose what to clean:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return
    if data == "cookies":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📥 /download_cookie - Download my YouTube cookie",
                                  callback_data="settings__cmd__download_cookie")],
            [InlineKeyboardButton("🌐 /cookies_from_browser - Get cookies from browser",
                                  callback_data="settings__cmd__cookies_from_browser")],
            [InlineKeyboardButton("🔎 /check_cookie - Check cookie file in your folder",
                                  callback_data="settings__cmd__check_cookie")],
            [InlineKeyboardButton("🔖 /save_as_cookie - Send text to save as cookie",
                                  callback_data="settings__cmd__save_as_cookie")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__back")]
        ])
        callback_query.edit_message_text(
            "<b>🍪 COOKIES</b>\n\nChoose an action:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return
    if data == "media":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📼 /format - Change quality & format", callback_data="settings__cmd__format")],
            [InlineKeyboardButton("📊 /mediainfo - Turn ON / OFF MediaInfo", callback_data="settings__cmd__mediainfo")],
            [InlineKeyboardButton("✂️ /split - Change split video part size", callback_data="settings__cmd__split")],
            [InlineKeyboardButton("🎧 /audio - Download video as audio", callback_data="settings__cmd__audio")],
            [InlineKeyboardButton("📋 /playlist - How to download playlists", callback_data="settings__cmd__playlist")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__back")]
        ])
        callback_query.edit_message_text(
            "<b>🎞 MEDIA</b>\n\nChoose an action:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return
    if data == "logs":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("#️⃣ /tags - Send your #tags", callback_data="settings__cmd__tags")],
            [InlineKeyboardButton("🆘 /help - Get instructions", callback_data="settings__cmd__help")],
            [InlineKeyboardButton("📃 /usage -Send your logs", callback_data="settings__cmd__usage")],
            [InlineKeyboardButton("📋 /playlist - Playlist's help", callback_data="settings__cmd__playlist")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__back")]
        ])
        callback_query.edit_message_text(
            "<b>📖 INFO</b>\n\nChoose an action:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return
    if data == "back":
        # Return to main menu
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🧹 CLEAN", callback_data="settings__menu__clean")],
            [InlineKeyboardButton("🍪 COOKIES", callback_data="settings__menu__cookies")],
            [InlineKeyboardButton("🎞 MEDIA", callback_data="settings__menu__media")],
            [InlineKeyboardButton("📖 INFO", callback_data="settings__menu__logs")],
            [InlineKeyboardButton("🔙 Close", callback_data="settings__menu__close")]
        ])
        callback_query.edit_message_text(
            "<b>Bot Settings</b>\n\nChoose a category:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return

@app.on_callback_query(filters.regex(r"^settings__cmd__"))
@reply_with_keyboard
def settings_cmd_callback(app, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data.split("__")[2]

    # For commands that are processed only via url_distractor, create a temporary Message
    if data == "clean":
        # Show the cleaning menu instead of direct execution
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🍪 Cookies only", callback_data="clean_option|cookies")],
            [InlineKeyboardButton("📃 Logs ", callback_data="clean_option|logs")],
            [InlineKeyboardButton("#️⃣ Tags", callback_data="clean_option|tags")],
            [InlineKeyboardButton("📼 Format", callback_data="clean_option|format")],
            [InlineKeyboardButton("✂️ Split", callback_data="clean_option|split")],
            [InlineKeyboardButton("📊 Mediainfo", callback_data="clean_option|mediainfo")],
            [InlineKeyboardButton("🗑  All files", callback_data="clean_option|all")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__cookies")]
        ])
        callback_query.edit_message_text(
            "<b>🧹 Clean Options</b>\n\nChoose what to clean:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return
    if data == "download_cookie":
        url_distractor(app, fake_message("/download_cookie", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "cookies_from_browser":
        cookies_from_browser(app, fake_message("/cookies_from_browser", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "check_cookie":
        url_distractor(app, fake_message("/check_cookie", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "save_as_cookie":
        app.send_message(user_id, Config.SAVE_AS_COOKIE_HINT, reply_to_message_id=callback_query.message.id,
                         parse_mode=enums.ParseMode.HTML)
        callback_query.answer("Hint sent.")
        return
    if data == "format":
        # Add the command attribute for set_format to work correctly
        set_format(app, fake_message("/format", user_id, command=["format"]))
        callback_query.answer("Command executed.")
        return
    if data == "mediainfo":
        mediainfo_command(app, fake_message("/mediainfo", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "split":
        split_command(app, fake_message("/split", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "audio":
        # We just send a hint on how to use it
        app.send_message(user_id,
                         "Download only audio from video source.\nUsage: /audio + URL (ex. /audio https://youtu.be/abc123)",
                         reply_to_message_id=callback_query.message.id)
        callback_query.answer("Hint sent.")
        return
    if data == "tags":
        tags_command(app, fake_message("/tags", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "help":
        command2(app, fake_message("/help", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "usage":
        url_distractor(app, fake_message("/usage", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "playlist":
        playlist_command(app, fake_message("/playlist", user_id))
        callback_query.answer("Command executed.")
        return
    callback_query.answer("Unknown command.", show_alert=True)

@app.on_callback_query(filters.regex(r"^clean_option\|"))
@reply_with_keyboard
def clean_option_callback(app, callback_query):
    user_id = callback_query.from_user.id
    data = callback_query.data.split("|")[1]

    if data == "cookies":
        url_distractor(app, fake_message("/clean cookie", user_id))
        callback_query.answer("Cookies cleaned.")
        return
    elif data == "logs":
        url_distractor(app, fake_message("/clean logs", user_id))
        callback_query.answer("logs cleaned.")
        return
    elif data == "tags":
        url_distractor(app, fake_message("/clean tags", user_id))
        callback_query.answer("tags cleaned.")
        return
    elif data == "format":
        url_distractor(app, fake_message("/clean format", user_id))
        callback_query.answer("format cleaned.")
        return
    elif data == "split":
        url_distractor(app, fake_message("/clean split", user_id))
        callback_query.answer("split cleaned.")
        return
    elif data == "mediainfo":
        url_distractor(app, fake_message("/clean mediainfo", user_id))
        callback_query.answer("mediainfo cleaned.")
        return
    elif data == "all":
        url_distractor(app, fake_message("/clean all", user_id))
        callback_query.answer("All files cleaned.")
        return
    elif data == "back":
        # Back to the cookies menu
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📥 /download_cookie - Download my YouTube cookie",
                                  callback_data="settings__cmd__download_cookie")],
            [InlineKeyboardButton("🌐 /cookies_from_browser - Get cookies from browser",
                                  callback_data="settings__cmd__cookies_from_browser")],
            [InlineKeyboardButton("🔎 /check_cookie - Check cookie file in your folder",
                                  callback_data="settings__cmd__check_cookie")],
            [InlineKeyboardButton("🔖 /save_as_cookie - Send text to save as cookie",
                                  callback_data="settings__cmd__save_as_cookie")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__back")]
        ])
        callback_query.edit_message_text(
            "<b>🍪 COOKIES</b>\n\nChoose an action:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return

# /Mediainfo Command
@app.on_message(filters.command("mediainfo") & filters.private)
@reply_with_keyboard
def mediainfo_command(app, message):
    user_id = message.chat.id
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    buttons = [
        [InlineKeyboardButton("✅ ON", callback_data="mediainfo_option|on")],
        [InlineKeyboardButton("❌ OFF", callback_data="mediainfo_option|off")],
        [InlineKeyboardButton("🔙 Cancel", callback_data="mediainfo_option|cancel")]
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    app.send_message(
        user_id,
        "Enable or disable sending MediaInfo for downloaded files?",
        reply_markup=keyboard
    )
    send_to_logger(message, "User opened /mediainfo menu.")

@app.on_callback_query(filters.regex(r"^mediainfo_option\|"))
@reply_with_keyboard
def mediainfo_option_callback(app, callback_query):
    logger.info(f"[MEDIAINFO] callback: {callback_query.data}")
    user_id = callback_query.from_user.id
    data = callback_query.data.split("|")[1]
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    mediainfo_file = os.path.join(user_dir, "mediainfo.txt")
    if callback_query.data == "mediainfo_option|cancel":
        callback_query.edit_message_text("🔚 MediaInfo: cancelled.")
        callback_query.answer("Menu closed.")
        send_to_logger(callback_query.message, "MediaInfo: cancelled.")
        return
    if data == "on":
        with open(mediainfo_file, "w", encoding="utf-8") as f:
            f.write("ON")
        callback_query.edit_message_text("✅ MediaInfo enabled. After downloading, file info will be sent.")
        send_to_logger(callback_query.message, "MediaInfo enabled.")
        callback_query.answer("MediaInfo enabled.")
        return
    if data == "off":
        with open(mediainfo_file, "w", encoding="utf-8") as f:
            f.write("OFF")
        callback_query.edit_message_text("❌ MediaInfo disabled.")
        send_to_logger(callback_query.message, "MediaInfo disabled.")
        callback_query.answer("MediaInfo disabled.")
        return

@app.on_message(filters.command("split") & filters.private)
@reply_with_keyboard
def split_command(app, message):
    user_id = message.chat.id
    # Subscription check for non-admines
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    # 2-3 row buttons
    sizes = [
        ("250 MB", 250 * 1024 * 1024),
        ("500 MB", 500 * 1024 * 1024),
        ("1 GB", 1024 * 1024 * 1024),
        ("1.5 GB", 1536 * 1024 * 1024),
        ("2 GB (default)", 1950 * 1024 * 1024)
    ]
    buttons = []
    # Pass the buttons in 2-3 rows
    for i in range(0, len(sizes), 2):
        row = []
        for j in range(2):
            if i + j < len(sizes):
                text, size = sizes[i + j]
                row.append(InlineKeyboardButton(text, callback_data=f"split_size|{size}"))
        buttons.append(row)
    buttons.append([InlineKeyboardButton("🔙 Cancel", callback_data="split_size|cancel")])
    keyboard = InlineKeyboardMarkup(buttons)
    app.send_message(user_id, "Choose max part size for video splitting:", reply_markup=keyboard)
    send_to_logger(message, "User opened /split menu.")

@app.on_callback_query(filters.regex(r"^split_size\|"))
@reply_with_keyboard
def split_size_callback(app, callback_query):
    logger.info(f"[SPLIT] callback: {callback_query.data}")
    user_id = callback_query.from_user.id
    data = callback_query.data.split("|")[1]
    if data == "cancel":
        callback_query.edit_message_text("🔚 Split size selection canceled.")
        callback_query.answer("✅ Split choice updated.")
        send_to_logger(callback_query.message, "Split selection canceled.")
        return
    try:
        size = int(data)
    except Exception:
        callback_query.answer("Invalid size.")
        return
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    split_file = os.path.join(user_dir, "split.txt")
    with open(split_file, "w", encoding="utf-8") as f:
        f.write(str(size))
    callback_query.edit_message_text(f"✅ Split part size set to: {humanbytes(size)}")
    send_to_logger(callback_query.message, f"Split size set to {size} bytes.")

# --- Callback Processor ---
@app.on_callback_query(filters.regex(r"^askq\|"))
@reply_with_keyboard
def askq_callback(app, callback_query):
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

# --- Function for reading split.txt ---
def get_user_split_size(user_id):
    user_dir = os.path.join("users", str(user_id))
    split_file = os.path.join(user_dir, "split.txt")
    if os.path.exists(split_file):
        try:
            with open(split_file, "r", encoding="utf-8") as f:
                size = int(f.read().strip())
                return size
        except Exception:
            pass
    return 1950 * 1024 * 1024  # default 1.95GB

def set_user_split_size(user_id, size):
    """Set user's split size preference"""
    user_dir = os.path.join("users", str(user_id))
    if not os.path.exists(user_dir):
        os.makedirs(user_dir, exist_ok=True)
    split_file = os.path.join(user_dir, "split.txt")
    try:
        with open(split_file, "w", encoding="utf-8") as f:
            f.write(str(size))
        return True
    except Exception as e:
        logger.error(f"Error setting split size for user {user_id}: {e}")
        return False

def is_mediainfo_enabled(user_id):
    user_dir = os.path.join("users", str(user_id))
    mediainfo_file = os.path.join(user_dir, "mediainfo.txt")
    if not os.path.exists(mediainfo_file):
        return False
    try:
        with open(mediainfo_file, "r", encoding="utf-8") as f:
            return f.read().strip().upper() == "ON"
    except Exception:
        return False

def set_user_mediainfo(user_id, enabled):
    """Set user's mediainfo preference"""
    user_dir = os.path.join("users", str(user_id))
    if not os.path.exists(user_dir):
        os.makedirs(user_dir, exist_ok=True)
    mediainfo_file = os.path.join(user_dir, "mediainfo.txt")
    try:
        with open(mediainfo_file, "w", encoding="utf-8") as f:
            f.write("ON" if enabled else "OFF")
        return True
    except Exception as e:
        logger.error(f"Error setting mediainfo for user {user_id}: {e}")
        return False
