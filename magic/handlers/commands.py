"""
Bot command handlers - COMPLETE VERSION with all missing functions
"""
import os
import subprocess
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup
from config import Config
from ..utils.communication import send_to_all, send_to_logger, send_to_user
from ..database.firebase import logger, check_user, is_user_in_channel
from ..user.settings import get_user_split_size, set_user_split_size, is_mediainfo_enabled, toggle_mediainfo
from ..utils.filesystem import cleanup_user_temp_files, get_active_download, create_directory
from ..processing.tags import extract_url_range_tags, save_user_tags
from ..download.downloader import down_and_audio


def reply_with_keyboard(func):
    """Decorator to add main keyboard to responses"""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def get_main_reply_keyboard():
    """Get the main reply keyboard"""
    return ReplyKeyboardMarkup(
        [
            ["/clean", "/download_cookie"],
            ["/playlist", "/settings", "/help"]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )


# Original command1 (start)
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


# Original command2 (help)
@reply_with_keyboard  
def command2(app, message):
    app.send_message(message.chat.id, (Config.HELP_MSG),
                     parse_mode=enums.ParseMode.HTML)
    send_to_logger(message, f"Send help txt to user")


# Cookies from browser command
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


# Browser choice callback
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


# Audio command handler
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


# Playlist command
@reply_with_keyboard
def playlist_command(app, message):
    user_id = message.chat.id
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return

    app.send_message(user_id, Config.PLAYLIST_HELP_MSG, parse_mode=enums.ParseMode.HTML)
    send_to_logger(message, "User requested playlist help.")


# Format command
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
            [InlineKeyboardButton("📺HD (720p)", callback_data="format_option|bv720")],
            [InlineKeyboardButton("📱SD (480p)", callback_data="format_option|bv480")],
            [InlineKeyboardButton("📱Low (360p)", callback_data="format_option|bv360")],
            [InlineKeyboardButton("🎵 Audio Only", callback_data="format_option|bestaudio")],
            [InlineKeyboardButton("🔄 Reset to Default", callback_data="format_option|reset")]
        ])
        app.send_message(user_id, "Choose download format:", reply_markup=main_keyboard)


# Format option callback
@reply_with_keyboard
def format_option_callback(app, callback_query):
    user_id = callback_query.from_user.id
    option = callback_query.data.split("|")[1]
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    format_file = os.path.join(user_dir, "format.txt")

    format_map = {
        "alwaysask": "always_ask",
        "bv2160": "best[height<=2160]",
        "bv1080": "best[height<=1080]", 
        "bv720": "best[height<=720]",
        "bv480": "best[height<=480]",
        "bv360": "best[height<=360]",
        "bestaudio": "bestaudio",
        "reset": ""
    }

    if option == "reset":
        if os.path.exists(format_file):
            os.remove(format_file)
        callback_query.edit_message_text("✅ Format reset to default")
    elif option == "others":
        # Show detailed quality menu
        others_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📱 144p", callback_data="format_option|bv144"),
             InlineKeyboardButton("📱 240p", callback_data="format_option|bv240")],
            [InlineKeyboardButton("📱 360p", callback_data="format_option|bv360"),
             InlineKeyboardButton("📱 480p", callback_data="format_option|bv480")],
            [InlineKeyboardButton("📺 720p", callback_data="format_option|bv720"),
             InlineKeyboardButton("📱 1080p", callback_data="format_option|bv1080")],
            [InlineKeyboardButton("💻 1440p", callback_data="format_option|bv1440"),
             InlineKeyboardButton("💻 2160p", callback_data="format_option|bv2160")],
            [InlineKeyboardButton("💻 4320p", callback_data="format_option|bv4320")],
            [InlineKeyboardButton("🔙 Back", callback_data="format_option|back")]
        ])
        callback_query.edit_message_text("Select quality:", reply_markup=others_keyboard)
        return
    elif option.startswith("bv"):
        height = option[2:]
        format_str = f"best[height<={height}]"
        with open(format_file, "w", encoding="utf-8") as f:
            f.write(format_str)
        callback_query.edit_message_text(f"✅ Format set to {height}p quality")
    else:
        format_str = format_map.get(option, "")
        with open(format_file, "w", encoding="utf-8") as f:
            f.write(format_str)
        callback_query.edit_message_text(f"✅ Format updated")

    callback_query.answer()


def register_command_handlers(app):
    """Register all command handlers with the app"""
    
    @app.on_message(filters.command("start") & filters.private)
    def start_handler(app, message):
        command1(app, message)
        
    @app.on_message(filters.command("help"))
    def help_handler(app, message):
        command2(app, message)
        
    @app.on_message(filters.command("cookies_from_browser") & filters.private)
    def cookies_handler(app, message):
        cookies_from_browser(app, message)
        
    @app.on_message(filters.command("audio") & filters.private)
    def audio_handler(app, message):
        audio_command_handler(app, message)
        
    @app.on_message(filters.command("playlist") & filters.private)
    def playlist_handler(app, message):
        playlist_command(app, message)
        
    @app.on_message(filters.command("format") & filters.private) 
    def format_handler(app, message):
        set_format(app, message)
        
    @app.on_callback_query(filters.regex(r"^browser_choice\|"))
    def browser_callback_handler(app, callback_query):
        browser_choice_callback(app, callback_query)
        
    @app.on_callback_query(filters.regex(r"^format_option\|"))
    def format_callback_handler(app, callback_query):
        format_option_callback(app, callback_query) 