"""
Helper functions for keyboard management and decorators
"""
import logging
import threading
import time
import signal
import sys
import os
import shutil
from pyrogram.types import ReplyKeyboardMarkup
from config import Config

logger = logging.getLogger(__name__)

# eternal reply-keyboard and reliable work with files
reply_keyboard_msg_ids = {}  # user_id: message_id

# Global starting point list (do not modify)
starting_point = []

# Global dictionary to track active downloads and lock for thread-safe access
active_downloads = {}
active_downloads_lock = threading.Lock()

# Global dictionary to track playlist errors and lock for thread-safe access
playlist_errors = {}
playlist_errors_lock = threading.Lock()

# Add a global dictionary to track download start times
download_start_times = {}
download_start_times_lock = threading.Lock()

# --- Function for permanent reply-keyboard ---
def get_main_reply_keyboard():
    """Get the main reply keyboard layout"""
    return ReplyKeyboardMarkup(
        [
            ["/clean", "/download_cookie"],
            ["/playlist", "/settings", "/help"]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )

# --- Function to send reply keyboard to user ---
def send_reply_keyboard_always(user_id):
    """Send persistent reply keyboard to user"""
    global reply_keyboard_msg_ids
    from magic.handlers.commands import app
    
    try:
        msg_id = reply_keyboard_msg_ids.get(user_id)
        if msg_id:
            # Try to delete the previous keyboard message
            try:
                app.delete_messages(user_id, msg_id)
            except:
                pass
        
        # Send new keyboard
        keyboard_msg = app.send_message(
            user_id,
            "🎛 Choose an option:",
            reply_markup=get_main_reply_keyboard()
        )
        reply_keyboard_msg_ids[user_id] = keyboard_msg.id
    except Exception as e:
        logger.error(f"Error sending reply keyboard: {e}")

# --- Wrapper for any custom action ---
def reply_with_keyboard(func):
    def wrapper(*args, **kwargs):
        # Execute the original function
        result = func(*args, **kwargs)
        
        # Try to get user_id from the message
        try:
            if len(args) >= 2:
                message = args[1]  # Usually the second argument is the message
                user_id = message.chat.id
                send_reply_keyboard_always(user_id)
        except Exception as e:
            logger.error(f"Error in reply_with_keyboard decorator: {e}")
        
        return result
    return wrapper

def set_download_start_time(user_id):
    """Set download start time for timeout tracking"""
    with download_start_times_lock:
        download_start_times[user_id] = time.time()

def clear_download_start_time(user_id):
    """Clear download start time"""
    with download_start_times_lock:
        if user_id in download_start_times:
            del download_start_times[user_id]

def check_download_timeout(user_id):
    """Check if download has exceeded timeout"""
    with download_start_times_lock:
        start_time = download_start_times.get(user_id)
        if start_time and (time.time() - start_time) > Config.DOWNLOAD_TIMEOUT:
            return True
    return False

def get_active_download(user_id):
    """
    Thread-safe function to get the active download status for a user

    Args:
        user_id: The user ID

    Returns:
        bool: Whether the user has an active download
    """
    with active_downloads_lock:
        return active_downloads.get(user_id, False)

def set_active_download(user_id, status):
    """
    Thread-safe function to set the active download status for a user

    Args:
        user_id: The user ID
        status (bool): Whether the user has an active download
    """
    with active_downloads_lock:
        active_downloads[user_id] = status

def signal_handler(sig, frame):
    """
    Handler for system signals to ensure graceful shutdown

    Args:
        sig: Signal number
        frame: Current stack frame
    """
    logger.info(f"Received signal {sig}, shutting down gracefully...")

    # Stop all active animations and threads
    active_threads = [t for t in threading.enumerate()
                     if t != threading.current_thread() and not t.daemon]

    if active_threads:
        logger.info(f"Waiting for {len(active_threads)} active threads to finish")
        for thread in active_threads:
            logger.info(f"Waiting for thread {thread.name} to finish...")
            thread.join(timeout=2)  # Wait with timeout to avoid hanging

    # Clean up temporary files
    try:
        cleanup_temp_files()
    except Exception as e:
        logger.error(f"Error during cleanup: {e}")

    # Finish the application
    logger.info("Shutting down Pyrogram client...")
    try:
        from magic.handlers.commands import app
        app.stop()
        logger.info("Pyrogram client stopped successfully")
    except Exception as e:
        logger.error(f"Error stopping Pyrogram client: {e}")

    logger.info("Shutdown complete.")
    sys.exit(0)

def cleanup_temp_files():
    """Clean up temporary files across all user directories"""
    if not os.path.exists("users"):
        return

    logger.info("Cleaning up temporary files")
    for user_dir in os.listdir("users"):
        try:
            user_path = os.path.join("users", user_dir)
            if os.path.isdir(user_path):
                for filename in os.listdir(user_path):
                    if filename.endswith(('.part', '.ytdl', '.temp', '.tmp')):
                        try:
                            os.remove(os.path.join(user_path, filename))
                        except Exception as e:
                            logger.error(f"Failed to remove temp file {filename}: {e}")
        except Exception as e:
            logger.error(f"Error cleaning user directory {user_dir}: {e}")

def cleanup_user_temp_files(user_id):
    """Clean up temporary files for a specific user"""
    user_dir = os.path.join("users", str(user_id))
    if not os.path.exists(user_dir):
        return
    
    logger.info(f"Cleaning up temporary files for user {user_id}")
    try:
        for filename in os.listdir(user_dir):
            file_path = os.path.join(user_dir, filename)
            # Remove temporary files
            if (filename.endswith(('.part', '.ytdl', '.temp', '.tmp')) or
                filename.startswith('yt_thumb_') or  # YouTube thumbnails
                filename.endswith('.jpg') or  # Thumbnails
                filename == 'full_title.txt' or  # Full title file
                filename == 'full_description.txt'):  # Tags file
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        logger.debug(f"Removed temp file: {filename}")
                except Exception as e:
                    logger.error(f"Failed to remove temp file {filename}: {e}")
    except Exception as e:
        logger.error(f"Error cleaning user directory {user_id}: {e}")

def sanitize_filename(filename, max_length=150):
    """
    Sanitize filename by removing invalid characters and shortening if needed
    Only allows letters (any language), numbers, and Linux-safe symbols

    Args:
        filename (str): Original filename
        max_length (int): Maximum allowed length for filename (excluding extension)

    Returns:
        str: Sanitized and shortened filename
    """
    # Exit early if None
    if filename is None:
        return "untitled"

    # Extract extension first
    name, ext = os.path.splitext(filename)

    # Remove all emoji and special Unicode characters
    # Keep only letters (any language), numbers, spaces, dots, dashes, underscores
    import unicodedata
    import re
    
    # Normalize Unicode characters
    name = unicodedata.normalize('NFKC', name)
    
    # Keep only letters, numbers, spaces, and safe symbols
    cleaned_name = ''
    for char in name:
        if (char.isalnum() or  # letters and numbers
            char.isspace() or  # spaces
            char in '.-_()'):  # safe symbols
            cleaned_name += char
    
    name = cleaned_name
    
    # Remove invalid filesystem characters (Windows and Linux safe)
    invalid_chars = r'[<>:"/\\|?*\x00-\x1f]'
    name = re.sub(invalid_chars, '', name)
    
    # Remove leading/trailing dots and spaces (not allowed in Linux)
    name = name.strip(' .')
    
    # Replace multiple spaces/dots with single ones
    name = re.sub(r'[\s.]+', ' ', name).strip()
    
    # If name is empty after cleaning, use default
    if not name:
        name = "untitled"
    
    # Shorten if too long
    full_name = name + ext
    max_total = 100
    if len(full_name) > max_total:
       allowed = max_total - len(ext)
       if allowed > 3:
          name = name[:allowed-3] + "..."
       else:
          name = name[:allowed]
       full_name = name + ext
    
    return full_name

# Register handlers for the most common termination signals
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)





