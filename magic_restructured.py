#!/usr/bin/env python3
"""
TG-YTDLP Bot - Restructured Main File
"""

import os
import sys
import signal
import threading
import time
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait

# Add magic package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'magic'))

# Import configuration
from config import Config

# Import all modules
from magic.utils.formatters import humanbytes, TimeFormatter, truncate_caption, sanitize_filename
from magic.utils.filesystem import (
    create_directory, cleanup_temp_files, cleanup_user_temp_files,
    get_active_download, set_active_download
)
from magic.utils.communication import (
    send_to_all, send_to_logger, send_to_user, progress_bar,
    safe_send_message, safe_forward_messages, safe_edit_message_text,
    start_hourglass_animation, start_cycle_progress
)
from magic.database.firebase import AuthedDB, logger, write_logs, check_user, is_user_blocked
from magic.processing.tags import (
    extract_url_range_tags, generate_final_tags, get_auto_tags,
    clean_telegram_tag, save_user_tags, is_playlist_with_range
)
from magic.processing.url_parser import (
    extract_real_url_if_google, youtube_to_short_url, youtube_to_long_url,
    is_youtube_url, is_tiktok_url, get_clean_url_for_tagging
)
from magic.processing.video import (
    split_video_2, get_duration_thumb, create_default_thumbnail, send_videos
)
from magic.download.cache import (
    save_to_video_cache, get_cached_message_ids, get_cached_qualities,
    save_to_playlist_cache, get_cached_playlist_videos, get_cached_playlist_qualities,
    get_clean_playlist_url, get_cached_playlist_count
)
from magic.download.quality import (
    get_video_formats, sort_quality_key, ask_quality_menu,
    get_quality_by_min_side, get_real_height_for_quality, ceil_to_popular
)
from magic.download.downloader import down_and_audio, down_and_up
from magic.user.settings import (
    get_user_split_size, set_user_split_size, is_mediainfo_enabled,
    toggle_mediainfo, get_user_quality_preference
)
from magic.handlers.commands import register_command_handlers, get_main_reply_keyboard

# Initialize Pyrogram client
app = Client(
    "tg_ytdlp_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    workers=4
)

# Initialize Firebase
import pyrebase
firebase_config = {
    "apiKey": Config.FIREBASE_API_KEY,
    "authDomain": Config.FIREBASE_AUTH_DOMAIN,
    "databaseURL": Config.FIREBASE_DATABASE_URL,
    "storageBucket": Config.FIREBASE_STORAGE_BUCKET,
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(Config.FIREBASE_EMAIL, Config.FIREBASE_PASSWORD)
db = AuthedDB(firebase.database(), user['idToken'])

# Token refresh thread
def token_refresher():
    """Refresh Firebase token periodically"""
    while True:
        try:
            time.sleep(3500)  # Refresh every hour
            global user, db
            user = auth.refresh(user['refreshToken'])
            db = AuthedDB(firebase.database(), user['idToken'])
            logger.info("Firebase token refreshed")
        except Exception as e:
            logger.error(f"Token refresh error: {e}")

refresh_thread = threading.Thread(target=token_refresher)
refresh_thread.daemon = True
refresh_thread.start()

# Register command handlers
register_command_handlers(app)

# Decorator for adding reply keyboard
def reply_with_keyboard(func):
    """Decorator to add main keyboard to responses"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

# URL processing handler
@app.on_message(filters.text & filters.private)
@reply_with_keyboard
def url_processor(app, message):
    """Process URLs sent by users"""
    try:
        # Check if user is blocked
        if is_user_blocked(message):
            return
            
        # Check if user exists in database
        if not check_user(message):
            return
            
        text = message.text.strip()
        
        # Skip if it's a command
        if text.startswith('/'):
            return
            
        # Check if it looks like a URL
        if not any(domain in text.lower() for domain in [
            'youtube.com', 'youtu.be', 'tiktok.com', 'instagram.com',
            'twitter.com', 'facebook.com', 'vimeo.com', 'twitch.tv'
        ]):
            return
            
        # Extract URL, range, and tags
        url, video_start_with, video_end_with, video_count, playlist_name, tags_text, format_override = extract_url_range_tags(text)
        
        if not url:
            send_to_all(message, "❌ No valid URL found in your message.")
            return
            
        # Process Google redirects
        url = extract_real_url_if_google(url)
        
        # Generate auto tags
        auto_tags = get_auto_tags(url, tags_text)
        final_tags = f"{tags_text} {auto_tags}".strip()
        
        # Check if this is an audio request
        is_audio_request = any(keyword in text.lower() for keyword in ['audio', 'mp3', 'музыка', 'аудио'])
        
        if is_audio_request:
            # Download audio
            down_and_audio(app, message, url, final_tags, quality_key="mp3", 
                         playlist_name=playlist_name, video_count=video_count, 
                         video_start_with=video_start_with)
        else:
            # Check if we should ask for quality
            user_quality = get_user_quality_preference(message.chat.id)
            
            if user_quality == "ask" and not format_override:
                # Show quality selection menu
                ask_quality_menu(app, message, url, final_tags, video_start_with)
            else:
                # Download with default/specified quality
                quality_key = user_quality if user_quality != "ask" else "best"
                down_and_up(app, message, url, playlist_name, video_count, 
                          video_start_with, final_tags, 
                          format_override=format_override, quality_key=quality_key)
                          
    except FloodWait as e:
        logger.warning(f"FloodWait: {e.value} seconds")
        time.sleep(e.value)
    except Exception as e:
        logger.error(f"URL processing error: {e}")
        send_to_all(message, f"❌ Error processing URL: {e}")

# Quality selection callback
@app.on_callback_query(filters.regex(r"^askq\|"))
@reply_with_keyboard
def quality_callback(app, callback_query):
    """Handle quality selection callbacks"""
    try:
        data = callback_query.data.split("|")
        if len(data) != 2:
            return
            
        quality_key = data[1]
        
        if quality_key == "cancel":
            app.delete_messages(callback_query.message.chat.id, callback_query.message.id)
            return
            
        # Get original URL and tags from the callback query message
        original_message = callback_query.message.reply_to_message
        if not original_message:
            callback_query.answer("❌ Original message not found")
            return
            
        text = original_message.text or original_message.caption or ""
        url, video_start_with, video_end_with, video_count, playlist_name, tags_text, format_override = extract_url_range_tags(text)
        
        if not url:
            callback_query.answer("❌ URL not found")
            return
            
        # Process the download
        url = extract_real_url_if_google(url)
        auto_tags = get_auto_tags(url, tags_text)
        final_tags = f"{tags_text} {auto_tags}".strip()
        
        # Delete the quality selection message
        app.delete_messages(callback_query.message.chat.id, callback_query.message.id)
        
        if quality_key == "mp3":
            down_and_audio(app, original_message, url, final_tags, quality_key="mp3",
                         playlist_name=playlist_name, video_count=video_count,
                         video_start_with=video_start_with)
        else:
            down_and_up(app, original_message, url, playlist_name, video_count,
                      video_start_with, final_tags, quality_key=quality_key)
                      
    except Exception as e:
        logger.error(f"Quality callback error: {e}")
        callback_query.answer(f"❌ Error: {e}")

# Document handler for cookies
@app.on_message(filters.document & filters.private)
@reply_with_keyboard
def document_handler(app, message):
    """Handle document uploads (cookies, etc.)"""
    try:
        if not check_user(message):
            return
            
        document = message.document
        if document.file_name and 'cookie' in document.file_name.lower():
            # Download cookies file
            user_dir = os.path.join("users", str(message.chat.id))
            create_directory(user_dir)
            
            file_path = os.path.join(user_dir, "cookies.txt")
            app.download_media(document, file_path)
            
            # Copy to main cookies location if needed
            if hasattr(Config, 'COOKIES_FILE_PATH'):
                import shutil
                shutil.copy2(file_path, Config.COOKIES_FILE_PATH)
                
            send_to_all(message, "✅ Cookies file saved successfully!")
        else:
            send_to_all(message, "📄 Please send a cookies.txt file for YouTube access.")
            
    except Exception as e:
        logger.error(f"Document handler error: {e}")
        send_to_all(message, f"❌ Error processing document: {e}")

# Signal handlers
def signal_handler(sig, frame):
    """Handle shutdown signals"""
    logger.info("Shutting down bot...")
    cleanup_temp_files()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Cleanup function
def periodic_cleanup():
    """Periodic cleanup of temporary files"""
    while True:
        try:
            time.sleep(3600)  # Every hour
            cleanup_temp_files()
            logger.info("Periodic cleanup completed")
        except Exception as e:
            logger.error(f"Periodic cleanup error: {e}")

cleanup_thread = threading.Thread(target=periodic_cleanup)
cleanup_thread.daemon = True
cleanup_thread.start()

# Add missing utility functions that weren't moved to modules yet
def fake_message(text, user_id, command=None):
    """Create a fake message object for internal use"""
    class FakeMessage:
        def __init__(self, text, user_id):
            self.text = text
            self.chat = type('obj', (object,), {'id': user_id, 'first_name': 'User'})()
            self.id = 0
            self._client = app
    
    return FakeMessage(text, user_id)

def remove_media(message, only=None):
    """Remove media files for a user"""
    try:
        user_id = message.chat.id
        cleanup_user_temp_files(user_id)
        send_to_all(message, "🧹 Media files cleaned up!")
    except Exception as e:
        logger.error(f"Remove media error: {e}")

# Admin functions (simplified)
def send_promo_message(app, message):
    """Send promotional message to all users"""
    try:
        # This would need to iterate through all users in the database
        send_to_logger(message, "Promo message feature needs implementation")
    except Exception as e:
        logger.error(f"Promo message error: {e}")

if __name__ == "__main__":
    logger.info("Starting TG-YTDLP Bot (Restructured Version)")
    logger.info(f"Bot version: Restructured")
    
    # Create necessary directories
    create_directory("users")
    create_directory("temp")
    
    # Start the bot
    try:
        app.run()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot error: {e}")
    finally:
        cleanup_temp_files()
        logger.info("Bot shutdown complete") 