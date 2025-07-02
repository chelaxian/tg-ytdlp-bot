"""Command handlers"""
import logging
import os
import subprocess
import re
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import enums
from config import Config

# Import required functions and objects
from magic.utils.helpers import reply_with_keyboard, get_active_download
from magic.utils.communication import send_to_user, send_to_logger, send_to_all
from magic.utils.filesystem import create_directory
from magic.database.firebase import check_user, is_user_in_channel
from magic.processing.url_parser import extract_url_range_tags
from magic.processing.tags import save_user_tags
from magic.download.downloader import down_and_audio

# Pyrogram App Initialization
app = Client(
    "magic",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

logger = logging.getLogger(__name__)

@app.on_message(filters.command("start") & filters.private)
@reply_with_keyboard
def command1(app, message):
    if int(message.chat.id) in Config.ADMIN:
        send_to_user(message, "Welcome Master 🥷")
    else:
        check_user(message)
        app.send_message(
            message.chat.id,
            f"Hello {message.chat.first_name},\n \n__This bot🤖 can download any videos into telegram directly.😊 For more information press **/help**__ 👈\n \n {Config.CREDITS_MSG}")
        send_to_logger(message, f"{message.chat.id} - user started the bot")

@app.on_message(filters.command("help"))
@reply_with_keyboard
def command2(app, message):
    app.send_message(message.chat.id, (Config.HELP_MSG),
                     parse_mode=enums.ParseMode.HTML)
    send_to_logger(message, f"Send help txt to user")

# Command to Set Browser Cooks
@app.on_message(filters.command("cookies_from_browser") & filters.private)
@reply_with_keyboard
def cookies_from_browser(app, message):
    user_id = message.chat.id
    # For non-admins, we check the subscription
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return

    # Logging a request for cookies from browser
    send_to_logger(message, "User requested cookies from browser.")

    # Path to the User's Directory, E.G. "./users/1234567"
    user_dir = os.path.join(".", "users", str(user_id))
    create_directory(user_dir)  # Ensure The User's Folder Exists

    # Dictionary with Browsers and Their Paths
    browsers = {
        "brave": "~/.config/BraveSoftware/Brave-Browser/",
        "chrome": "~/.config/google-chrome/",
        "chromium": "~/.config/chromium/",
        "edge": "~/.config/microsoft-edge/",
        "firefox": "~/.mozilla/firefox/",
        "opera": "~/.config/opera/",
        "safari": "~/Library/Safari/",
        "vivaldi": "~/.config/vivaldi/",
        "whale": ["~/.config/Whale/", "~/.config/naver-whale/"]
    }

    # Create a list of only installed browsers
    installed_browsers = []
    for browser, path in browsers.items():
        if browser == "safari":
            exists = False
        elif isinstance(path, list):
            exists = any(os.path.exists(os.path.expanduser(p)) for p in path)
        else:
            exists = os.path.exists(os.path.expanduser(path))
        if exists:
            installed_browsers.append(browser)

    # If there are no installed browsers, send a message about it
    if not installed_browsers:
        app.send_message(
            user_id,
            "❌ No supported browsers found on the server. Please install one of the supported browsers or use manual cookie upload."
        )
        send_to_logger(message, "No installed browsers found.")
        return

    # Create buttons only for installed browsers
    buttons = []
    for browser in installed_browsers:
        display_name = browser.capitalize()
        button = InlineKeyboardButton(f"✅ {display_name}", callback_data=f"browser_choice|{browser}")
        buttons.append([button])

    # Add a cancel button
    buttons.append([InlineKeyboardButton("🔙 Cancel", callback_data="browser_choice|cancel")])
    keyboard = InlineKeyboardMarkup(buttons)

    app.send_message(
        user_id,
        "Select a browser to download cookies from:",
        reply_markup=keyboard
    )
    send_to_logger(message, "Browser selection keyboard sent with installed browsers only.")


# Callback Handler for Browser Selection
@app.on_callback_query(filters.regex(r"^browser_choice\|"))
@reply_with_keyboard
def browser_choice_callback(app, callback_query):
    logger.info(f"[BROWSER] callback: {callback_query.data}")

    user_id = callback_query.from_user.id
    data = callback_query.data.split("|")[1]  # E.G. "Chromium", "Firefox", or "Cancel"
    # Path to the User's Directory, E.G. "./users/1234567"
    user_dir = os.path.join(".", "users", str(user_id))
    create_directory(user_dir)
    cookie_file = os.path.join(user_dir, "cookie.txt")

    if data == "cancel":
        callback_query.edit_message_text("🔚 Browser selection canceled.")
        callback_query.answer("✅ Browser choice updated.")
        send_to_logger(callback_query.message, "Browser selection canceled.")
        return

    browser_option = data

    # Dictionary with Browsers and Their Paths (Same as ABOVE)
    browsers = {
        "brave": "~/.config/BraveSoftware/Brave-Browser/",
        "chrome": "~/.config/google-chrome/",
        "chromium": "~/.config/chromium/",
        "edge": "~/.config/microsoft-edge/",
        "firefox": "~/.mozilla/firefox/",
        "opera": "~/.config/opera/",
        "safari": "~/Library/Safari/",
        "vivaldi": "~/.config/vivaldi/",
        "whale": ["~/.config/Whale/", "~/.config/naver-whale/"]
    }
    path = browsers.get(browser_option)
    # If the browser is not installed, we inform the user and do not execute the command
    if (browser_option == "safari") or (
            isinstance(path, list) and not any(os.path.exists(os.path.expanduser(p)) for p in path)
    ) or (isinstance(path, str) and not os.path.exists(os.path.expanduser(path))):
        callback_query.edit_message_text(f"⚠️ {browser_option.capitalize()} browser not installed.")
        callback_query.answer("⚠️ Browser not installed.")
        send_to_logger(callback_query.message, f"Browser {browser_option} not installed.")
        return

    # Build the command for cookie extraction: yt-dlp --cookies "cookie.txt" --cookies-from-browser <browser_option>
    cmd = f'yt-dlp --cookies "{cookie_file}" --cookies-from-browser {browser_option}'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        if "You must provide at least one URL" in result.stderr:
            callback_query.edit_message_text(f"✅ Cookies saved using browser: {browser_option}")
            send_to_logger(callback_query.message, f"Cookies saved using browser: {browser_option}")
        else:
            callback_query.edit_message_text(f"❌ Failed to save cookies: {result.stderr}")
            send_to_logger(callback_query.message,
                           f"Failed to save cookies using browser {browser_option}: {result.stderr}")
    else:
        callback_query.edit_message_text(f"✅ Cookies saved using browser: {browser_option}")
        send_to_logger(callback_query.message, f"Cookies saved using browser: {browser_option}")

    callback_query.answer("✅ Browser choice updated.")

# Command to Download Audio from a Video url
@app.on_message(filters.command("audio") & filters.private)
@reply_with_keyboard
def audio_command_handler(app, message):
    user_id = message.chat.id
    if get_active_download(user_id):
        app.send_message(user_id, "⏰ WAIT UNTIL YOUR PREVIOUS DOWNLOAD IS FINISHED", reply_to_message_id=message.id)
        return
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    text = message.text
    url, _, _, _, tags, tags_text, tag_error = extract_url_range_tags(text)
    if tag_error:
        wrong, example = tag_error
        app.send_message(user_id, f"❌ Tag #{wrong} contains forbidden characters. Only letters, digits and _ are allowed.\nPlease use: {example}", reply_to_message_id=message.id)
        return
    if not url:
        send_to_user(message, "Please, send valid URL.")
        return
    save_user_tags(user_id, tags)
    
    # Extract playlist parameters from the message
    full_string = message.text or message.caption or ""
    _, video_start_with, video_end_with, playlist_name, _, _, tag_error = extract_url_range_tags(full_string)
    video_count = video_end_with - video_start_with + 1
    
    down_and_audio(app, message, url, tags, quality_key="mp3", playlist_name=playlist_name, video_count=video_count, video_start_with=video_start_with)

# /Playlist Command
@app.on_message(filters.command("playlist") & filters.private)
@reply_with_keyboard
def playlist_command(app, message):
    user_id = message.chat.id
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return

    app.send_message(user_id, Config.PLAYLIST_HELP_MSG, parse_mode=enums.ParseMode.HTML)
    send_to_logger(message, "User requested playlist help.")

# Command /Format Handler
@app.on_message(filters.command("format") & filters.private)
@reply_with_keyboard
def set_format(app, message):
    user_id = message.chat.id
    # For non-admins, we check the subscription
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return

    send_to_logger(message, "User requested format change.")
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)  # Ensure The User's Folder Exists

    # If the additional text is transmitted, we save it as Custom Format
    if len(message.command) > 1:
        custom_format = message.text.split(" ", 1)[1].strip()
        with open(os.path.join(user_dir, "format.txt"), "w", encoding="utf-8") as f:
            f.write(custom_format)
        app.send_message(user_id, f"✅ Format updated to:\n{custom_format}")
        send_to_logger(message, f"Format updated to: {custom_format}")
    else:
        # Main Menu with A Few Popular Options, Plus The Others Button
        main_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("❓ Always Ask (menu + buttons)", callback_data="format_option|alwaysask")],
            [InlineKeyboardButton("🎛 Others (144p - 4320p)", callback_data="format_option|others")],
            [InlineKeyboardButton("💻4k (best for PC/Mac Telegram)", callback_data="format_option|bv2160")],
            [InlineKeyboardButton("📱FullHD (best for mobile Telegram)", callback_data="format_option|bv1080")],
            [InlineKeyboardButton("📈Bestvideo+Bestaudio (MAX quality)", callback_data="format_option|bestvideo")],
            # [InlineKeyboardButton("📉best (no ffmpeg) (bad)", callback_data="format_option|best")],
            [InlineKeyboardButton("🎚 Custom (enter your own)", callback_data="format_option|custom")],
            [InlineKeyboardButton("🔙 Cancel", callback_data="format_option|cancel")]
        ])
        app.send_message(
            user_id,
            "Select a format option or send a custom one using `/format <format_string>`:",
            reply_markup=main_keyboard
        )
        send_to_logger(message, "Format menu sent.")

@app.on_message(filters.command("tags") & filters.private)
@reply_with_keyboard
def tags_command(app, message):
    user_id = message.chat.id
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return

    if len(message.command) > 1:
        # User is setting tags
        tags_text = message.text.split(" ", 1)[1].strip()
        tags = [tag.strip() for tag in tags_text.split() if tag.strip()]
        save_user_tags(user_id, tags)
        app.send_message(user_id, f"✅ Tags saved: {' '.join(tags)}")
        send_to_logger(message, f"User {user_id} saved tags: {tags_text}")
    else:
        # User is requesting current tags
        try:
            user_dir = os.path.join("users", str(user_id))
            tags_file = os.path.join(user_dir, "tags.txt")
            if os.path.exists(tags_file):
                with open(tags_file, 'r', encoding='utf-8') as f:
                    current_tags = f.read().strip()
                if current_tags:
                    app.send_message(user_id, f"📎 Your current tags: {current_tags}")
                else:
                    app.send_message(user_id, "📎 No tags saved. Use `/tags your tag1 tag2` to set tags.")
            else:
                app.send_message(user_id, "📎 No tags saved. Use `/tags your tag1 tag2` to set tags.")
        except Exception as e:
            logger.error(f"Error reading tags for user {user_id}: {e}")
            app.send_message(user_id, "❌ Error reading tags.")

# Callback for format selection
@app.on_callback_query(filters.regex(r"^format_option\|"))
@reply_with_keyboard
def format_option_callback(app, callback_query):
    logger.info(f"[FORMAT] callback: {callback_query.data}")
    user_id = callback_query.from_user.id
    data = callback_query.data.split("|")[1]

    # If you press the Cancel button
    if data == "cancel":
        callback_query.edit_message_text("🔚 Format selection canceled.")
        callback_query.answer("✅ Format choice updated.")
        send_to_logger(callback_query.message, "Format selection canceled.")
        return

    # If the Custom button is pressed
    if data == "custom":
        callback_query.edit_message_text(
            "To use a custom format, send the command in the following form:\n\n`/format bestvideo+bestaudio/best`\n\nReplace `bestvideo+bestaudio/best` with your desired format string."
        )
        callback_query.answer("Hint sent.")
        send_to_logger(callback_query.message, "Custom format hint sent.")
        return

    # If the Others button is pressed - we display the second set of options
    if data == "others":
        full_res_keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("144p (256×144)", callback_data="format_option|bv144"),
                InlineKeyboardButton("240p (426×240)", callback_data="format_option|bv240"),
                InlineKeyboardButton("360p (640×360)", callback_data="format_option|bv360")
            ],
            [
                InlineKeyboardButton("480p (854×480)", callback_data="format_option|bv480"),
                InlineKeyboardButton("720p (1280×720)", callback_data="format_option|bv720"),
                InlineKeyboardButton("1080p (1920×1080)", callback_data="format_option|bv1080")
            ],
            [
                InlineKeyboardButton("1440p (2560×1440)", callback_data="format_option|bv1440"),
                InlineKeyboardButton("2160p (3840×2160)", callback_data="format_option|bv2160"),
                InlineKeyboardButton("4320p (7680×4320)", callback_data="format_option|bv4320")
            ],
            [InlineKeyboardButton("🔙 Back", callback_data="format_option|back")]
        ])
        callback_query.edit_message_text("Select your desired resolution:", reply_markup=full_res_keyboard)
        callback_query.answer()
        send_to_logger(callback_query.message, "Format resolution menu sent.")
        return

    # If the Back button is pressed - we return to the main menu
    if data == "back":
        main_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("❓ Always Ask (menu + buttons)", callback_data="format_option|alwaysask")],
            [InlineKeyboardButton("🎛 Others (144p - 4320p)", callback_data="format_option|others")],
            [InlineKeyboardButton("💻4k (best for PC/Mac Telegram)", callback_data="format_option|bv2160")],
            [InlineKeyboardButton("📱FullHD (best for mobile Telegram)", callback_data="format_option|bv1080")],
            [InlineKeyboardButton("📈Bestvideo+Bestaudio (MAX quality)", callback_data="format_option|bestvideo")],
            # [InlineKeyboardButton("📉best (no ffmpeg) (bad)", callback_data="format_option|best")],
            [InlineKeyboardButton("🎚 Custom (enter your own)", callback_data="format_option|custom")],
            [InlineKeyboardButton("🔙 Cancel", callback_data="format_option|cancel")]
        ])
        callback_query.edit_message_text("Select a format option or send a custom one using `/format <format_string>`:",
                                         reply_markup=main_keyboard)
        callback_query.answer()
        send_to_logger(callback_query.message, "Returned to main format menu.")
        return

    # Mapping for the Rest of the Options
    if data == "bv144":
        chosen_format = "bv*[vcodec*=avc1][height<=144]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/best"
    elif data == "bv240":
        chosen_format = "bv*[vcodec*=avc1][height<=240]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/best"
    elif data == "bv360":
        chosen_format = "bv*[vcodec*=avc1][height<=360]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/best"
    elif data == "bv480":
        chosen_format = "bv*[vcodec*=avc1][height<=480]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/best"
    elif data == "bv720":
        chosen_format = "bv*[vcodec*=avc1][height<=720]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/best"
    elif data == "bv1080":
        chosen_format = "bv*[vcodec*=avc1][height<=1080]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/best"
    elif data == "bv1440":
        chosen_format = "bv*[vcodec*=avc1][height<=1440]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/best"
    elif data == "bv2160":
        chosen_format = "bv*[vcodec*=avc1][height<=2160]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/best"
    elif data == "bv4320":
        chosen_format = "bv*[vcodec*=avc1][height<=4320]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/best"
    elif data == "bestvideo":
        chosen_format = "bestvideo+bestaudio/best"
    elif data == "best":
        chosen_format = "best"
    else:
        chosen_format = data

    # Save The Selected Format
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    with open(os.path.join(user_dir, "format.txt"), "w", encoding="utf-8") as f:
        f.write(chosen_format)
    callback_query.edit_message_text(f"✅ Format updated to:\n{chosen_format}")
    callback_query.answer("✅ Format saved.")
    send_to_logger(callback_query.message, f"Format updated to: {chosen_format}")

    if data == "alwaysask":
        user_dir = os.path.join("users", str(user_id))
        create_directory(user_dir)
        with open(os.path.join(user_dir, "format.txt"), "w", encoding="utf-8") as f:
            f.write("ALWAYS_ASK")
        callback_query.edit_message_text(
            "✅ Format set to: Always Ask. Now you will be prompted for quality each time you send a URL.")
        send_to_logger(callback_query.message, "Format set to ALWAYS_ASK.")
        return

# Text Message Handler for General Commands
@app.on_message(filters.text & filters.private)
@reply_with_keyboard
def url_distractor(app, message):
    user_id = message.chat.id
    is_admin = int(user_id) in Config.ADMIN
    text = message.text.strip()

    # For non-admin users, if they haven't Joined the Channel, Exit ImmediaTely.
    if not is_admin and not is_user_in_channel(app, message):
        return

    # ----- User Commands -----
    # /Save_as_cookie Command
    if text.startswith(Config.SAVE_AS_COOKIE_COMMAND):
        save_as_cookie_file(app, message)
        return

    # /Download_cookie Command
    if text == Config.DOWNLOAD_COOKIE_COMMAND:
        download_cookie(app, message)
        return

    # /Check_cookie Command
    if text == Config.CHECK_COOKIE_COMMAND:
        checking_cookie_file(app, message)
        return

    # /cookies_from_browser Command
    if text.startswith(Config.COOKIES_FROM_BROWSER_COMMAND):
        cookies_from_browser(app, message)
        return

    # /Audio Command
    if text.startswith(Config.AUDIO_COMMAND):
        audio_command_handler(app, message)
        return

    # /Format Command
    if text.startswith(Config.FORMAT_COMMAND):
        set_format(app, message)
        return

    # /Mediainfo Command
    if text.startswith(Config.MEDIINFO_COMMAND):
        mediainfo_command(app, message)
        return

    # /Settings Command
    if text.startswith(Config.SETTINGS_COMMAND):
        settings_command(app, message)
        return

        # /Playlist Command
    if text.startswith(Config.PLAYLIST_COMMAND):
        settings_command(app, message)
        return

        # /Clean Command
    if text.startswith(Config.CLEAN_COMMAND):
        clean_args = text[len(Config.CLEAN_COMMAND):].strip().lower()
        if clean_args in ["cookie", "cookies"]:
            remove_media(message, only=["cookie.txt"])
            send_to_all(message, "🗑 Cookie file removed.")
            return
        elif clean_args in ["log", "logs"]:
            remove_media(message, only=["logs.txt"])
            send_to_all(message, "🗑 Logs file removed.")
            return
        elif clean_args in ["tag", "tags"]:
            remove_media(message, only=["tags.txt"])
            send_to_all(message, "🗑 Tags file removed.")
            return
        elif clean_args == "format":
            remove_media(message, only=["format.txt"])
            send_to_all(message, "🗑 Format file removed.")
            return
        elif clean_args == "split":
            remove_media(message, only=["split.txt"])
            send_to_all(message, "🗑 Split file removed.")
            return
        elif clean_args == "mediainfo":
            remove_media(message, only=["mediainfo.txt"])
            send_to_all(message, "🗑 Mediainfo file removed.")
            return
        elif clean_args == "all":
            # Delete all files and display the list of deleted ones
            user_dir = f'./users/{str(message.chat.id)}'
            if not os.path.exists(user_dir):
                send_to_all(message, "🗑 No files to remove.")
                return

            removed_files = []
            allfiles = os.listdir(user_dir)

            file_extensions = [
                '.mp4', '.mkv', '.mp3', '.m4a', '.jpg', '.jpeg', '.part', '.ytdl',
                '.txt', '.ts', '.m3u8', '.webm', '.wmv', '.avi', '.mpeg', '.wav'
            ]

            for extension in file_extensions:
                files = [fname for fname in allfiles if fname.endswith(extension)]
                for file in files:
                    if extension == '.txt' and file in ['logs.txt', 'tags.txt']:
                        continue
                    file_path = os.path.join(user_dir, file)
                    try:
                        os.remove(file_path)
                        removed_files.append(file)
                    except Exception as e:
                        logger.error(f"Failed to remove file {file_path}: {e}")

            if removed_files:
                files_list = "\n".join([f"• {file}" for file in removed_files])
                send_to_all(message, f"🗑 Removed files:\n{files_list}")
            else:
                send_to_all(message, "🗑 No files to remove.")
            return

        # If the command Clean did not match anything specific, we delete all media files
        remove_media(message)
        send_to_all(message, "🗑 All media files removed.")
        return

    # /USAGE Command
    if Config.USAGE_COMMAND in text:
        get_user_log(app, message)
        return

    # /tags Command
    if Config.TAGS_COMMAND in text:
        tags_command(app, message)
        return

    # /Split Command
    if text.startswith(Config.SPLIT_COMMAND):
        split_command(app, message)
        return

    # /uncache Command - Clear cache for URL (for admins only)
    if text.startswith(Config.UNCACHE_COMMAND):
        if is_admin:
            uncache_command(app, message)
        else:
            send_to_all(message, "❌ This command is only available for administrators.")
        return

    # If the Message Contains a URL, Launch The Video Download Function.
    if ("https://" in text) or ("http://" in text):
        if not is_user_blocked(message):
            video_url_extractor(app, message)
        return

    # ----- Admin Commands -----
    if is_admin:
        # If the message begins with /BroadCast, we process it as BroadCast, regardless
        if text.startswith(Config.BROADCAST_MESSAGE):
            send_promo_message(app, message)
            return

        # /Block_user Command
        if Config.BLOCK_USER_COMMAND in text:
            block_user(app, message)
            return

        # /unblock_user Command
        if Config.UNBLOCK_USER_COMMAND in text:
            unblock_user(app, message)
            return

        # /Run_Time Command
        if Config.RUN_TIME in text:
            check_runtime(message)
            return

        # /All Command for User Details
        if Config.GET_USER_DETAILS_COMMAND in text:
            get_user_details(app, message)
            return

        # /log Command for User Logs
        if Config.GET_USER_LOGS_COMMAND in text:
            get_user_log(app, message)
            return

        # /uncache Command - Clear cache for URL
        if Config.UNCACHE_COMMAND in text:
            uncache_command(app, message)
            return

    # Reframed processing for all users (admins and ordinary users)
    if message.reply_to_message:
        # If the reference text begins with /broadcast, then:
        if text.startswith(Config.BROADCAST_MESSAGE):
            # Only for admins we call send_promo_message
            if is_admin:
                send_promo_message(app, message)
        else:
            # Otherwise, if the reform contains video, we call Caption_EDITOR
            if not is_user_blocked(message):
                if message.reply_to_message.video:
                    caption_editor(app, message)
        return

    logger.info(f"{user_id} No matching command processed.")

# Video URL Extractor
@app.on_message(filters.text & filters.private)
@reply_with_keyboard
def video_url_extractor(app, message):
    check_user(message)
    user_id = message.chat.id
    is_admin = int(user_id) in Config.ADMIN
    
    if not is_admin and not is_user_in_channel(app, message):
        return

    # Check if user has active download
    if get_active_download(user_id):
        app.send_message(user_id, "⏰ WAIT UNTIL YOUR PREVIOUS DOWNLOAD IS FINISHED", reply_to_message_id=message.id)
        return

    text = message.text or message.caption or ""
    
    # URL pattern check
    url_pattern = r'https?://[^\s]+'
    if not re.search(url_pattern, text):
        return

    # Extract URL and process
    url, video_start_with, video_end_with, video_count, playlist_name, tags_text, format_override = extract_url_range_tags(text)
    
    if not url:
        send_to_user(message, "Please, send valid URL.")
        return

    users_first_name = message.chat.first_name
    send_to_logger(message, f"User entered a **url**\n **user's name:** {users_first_name}\nURL: {text}")

    # Check if it's TikTok
    is_tiktok = is_tiktok_url(url)

    # Process the download (implementation would continue here)
    send_to_user(message, "🔄 Processing your request...")

# Updating The Cookie File.
@app.on_message(filters.text & filters.private)
@reply_with_keyboard
def save_as_cookie_file(app, message):
    user_id = str(message.chat.id)
    content = message.text[len(Config.SAVE_AS_COOKIE_COMMAND):].strip()
    new_cookie = ""

    if content.startswith("```"):
        lines = content.splitlines()
        if lines[0].startswith("```"):
            if lines[-1].strip() == "```":
                lines = lines[1:-1]
            else:
                lines = lines[1:]
            new_cookie = "\n".join(lines).strip()
        else:
            new_cookie = content
    else:
        new_cookie = content

    processed_lines = []
    for line in new_cookie.splitlines():
        if "\t" not in line:
            line = re.sub(r' {2,}', '\t', line)
        processed_lines.append(line)
    final_cookie = "\n".join(processed_lines)

    if final_cookie:
        send_to_all(message, "**✅ User provided a new cookie file.**")
        user_dir = os.path.join("users", user_id)
        create_directory(user_dir)
        cookie_filename = os.path.basename(Config.COOKIE_FILE_PATH)
        file_path = os.path.join(user_dir, cookie_filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(final_cookie)
        send_to_user(message, f"**✅ Cookie successfully updated:**\n`{final_cookie}`")
        send_to_logger(message, f"Cookie file updated for user {user_id}.")
    else:
        send_to_user(message, "**❌ Not a valid cookie.**")
        send_to_logger(message, f"Invalid cookie content provided by user {user_id}.")

@app.on_message(filters.document & filters.private)
@reply_with_keyboard
def download_cookie(app, message):
    user_id = str(message.chat.id)
    response = requests.get(Config.COOKIE_URL)
    if response.status_code == 200:
        user_dir = os.path.join("users", user_id)
        create_directory(user_dir)
        cookie_filename = os.path.basename(Config.COOKIE_FILE_PATH)
        file_path = os.path.join(user_dir, cookie_filename)
        with open(file_path, "wb") as cf:
            cf.write(response.content)
        send_to_user(message, "**✅ Cookie file downloaded and saved in your folder.**")
        send_to_logger(message, f"Cookie file downloaded for user {user_id}.")
    else:
        send_to_user(message, "❌ Cookie URL is not available!")
        send_to_logger(message, f"Failed to download cookie file for user {user_id}.")

@app.on_message(filters.text & filters.private)
@reply_with_keyboard
def checking_cookie_file(app, message):
    user_id = str(message.chat.id)
    cookie_filename = os.path.basename(Config.COOKIE_FILE_PATH)
    file_path = os.path.join("users", user_id, cookie_filename)

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as cookie:
            cookie_content = cookie.read()
        if cookie_content.startswith("# Netscape HTTP Cookie File"):
            send_to_user(message, "✅ Cookie file exists and has correct format")
            send_to_logger(message, "Cookie file exists and has correct format.")
        else:
            send_to_user(message, "⚠️ Cookie file exists but has incorrect format")
            send_to_logger(message, "Cookie file exists but has incorrect format.")
    else:
        send_to_user(message, "❌ Cookie file is not found.")
        send_to_logger(message, "Cookie file not found.")

# SEND COOKIE VIA Document
@app.on_message(filters.document & filters.private)
@reply_with_keyboard
def save_my_cookie(app, message):
    user_id = str(message.chat.id)
    # We determine the path to the user folder (for example, "./users/1234567)
    user_folder = f"./users/{user_id}"
    create_directory(user_folder)
    cookie_filename = os.path.basename(Config.COOKIE_FILE_PATH)
    cookie_file_path = os.path.join(user_folder, cookie_filename)
    app.download_media(message, file_name=cookie_file_path)
    send_to_user(message, "✅ Cookie file saved")
    send_to_logger(message, f"Cookie file saved for user {user_id}.")

# Caption Editor for Videos
@app.on_message(filters.text & filters.private)
@reply_with_keyboard
def caption_editor(app, message):
    users_name = message.chat.first_name
    user_id = message.chat.id
    caption = message.text
    video_file_id = message.reply_to_message.video.file_id
    info_of_video = f"\n**Caption:** `{caption}`\n**User id:** `{user_id}`\n**User first name:** `{users_name}`\n**Video file id:** `{video_file_id}`"
    # Sending to logs
    send_to_logger(message, info_of_video)
    app.send_video(user_id, video_file_id, caption=caption)
    app.send_video(Config.LOGS_ID, video_file_id, caption=caption)

# Remove All User Media Files
def remove_media(message, only=None):
    dir = f'./users/{str(message.chat.id)}'
    if not os.path.exists(dir):
        logger.warning(f"Directory {dir} does not exist, nothing to remove")
        return
    if only:
        for fname in only:
            file_path = os.path.join(dir, fname)
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    logger.info(f"Removed file: {file_path}")
                except Exception as e:
                    logger.error(f"Failed to remove file {file_path}: {e}")
        return
    allfiles = os.listdir(dir)
    file_extensions = [
        '.mp4', '.mkv', '.mp3', '.m4a', '.jpg', '.jpeg', '.part', '.ytdl',
        '.txt', '.ts', '.m3u8', '.webm', '.wmv', '.avi', '.mpeg', '.wav'
    ]
    for extension in file_extensions:
        if isinstance(extension, tuple):
            files = [fname for fname in allfiles if any(fname.endswith(ext) for ext in extension)]
        else:
            files = [fname for fname in allfiles if fname.endswith(extension)]
        for file in files:
            if extension == '.txt' and file in ['logs.txt', 'tags.txt']:
                continue
            file_path = os.path.join(dir, file)
            try:
                os.remove(file_path)
                logger.info(f"Removed file: {file_path}")
            except Exception as e:
                logger.error(f"Failed to remove file {file_path}: {e}")
    logger.info(f"Media cleanup completed for user {message.chat.id}")

def get_mediainfo_cli(file_path):
    try:
        result = subprocess.run(
            ["mediainfo", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout
    except Exception as e:
        logger.error(f"mediainfo CLI error: {e}")
        return "MediaInfo CLI error: " + str(e)
