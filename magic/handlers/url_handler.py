"""
URL and Message Handler - CRITICAL COMPONENT
"""
import os
from pyrogram import enums
from config import Config
from ..database.firebase import logger, is_user_blocked, is_user_in_channel
from ..utils.communication import send_to_all
from ..utils.filesystem import remove_media, create_directory
from ..handlers.commands import (
    save_as_cookie_file, download_cookie, checking_cookie_file, 
    cookies_from_browser, audio_command_handler, set_format,
    mediainfo_command, settings_command, split_command
)
from ..handlers.admin import (
    get_user_log, tags_command, uncache_command, send_promo_message,
    block_user, unblock_user, check_runtime, get_user_details
)


def reply_with_keyboard(func):
    """Decorator to add main keyboard to responses"""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@reply_with_keyboard
def url_distractor(app, message):
    """CRITICAL FUNCTION - Main URL and command dispatcher"""
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

            # Delete all files in the user folder
            for file in allfiles:
                file_path = os.path.join(user_dir, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        removed_files.append(file)
                        logger.info(f"Removed file: {file_path}")
                except Exception as e:
                    logger.error(f"Failed to remove file {file_path}: {e}")

            if removed_files:
                files_list = "\n".join([f"• {file}" for file in removed_files])
                send_to_all(message, f"🗑 All files removed successfully!\n\nRemoved files:\n{files_list}")
            else:
                send_to_all(message, "🗑 No files to remove.")
            return
        else:
            # Regular command /clean - delete only media files with filtering
            remove_media(message)
            send_to_all(message, "🗑 All media files are removed.")
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


def video_url_extractor(app, message):
    """Extract and process video URLs - PLACEHOLDER"""
    # This function needs to be implemented
    from ..processing.tags import extract_url_range_tags
    from ..download.downloader import down_and_up
    
    text = message.text or message.caption or ""
    url, video_start_with, video_end_with, video_count, playlist_name, tags_text, format_override = extract_url_range_tags(text)
    
    if url:
        down_and_up(app, message, url, playlist_name, video_count, video_start_with, tags_text, format_override=format_override)


def caption_editor(app, message):
    """Edit video captions - PLACEHOLDER"""
    send_to_all(message, "Caption editor functionality placeholder")


def save_my_cookie(app, message):
    """Save cookie from document upload"""
    if not message.document:
        send_to_all(message, "Please send a valid cookie file.")
        return
        
    user_id = message.chat.id
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    
    file_path = os.path.join(user_dir, "cookie.txt")
    app.download_media(message.document, file_path)
    
    send_to_all(message, "✅ Cookie file saved successfully!") 