"""
Helper functions for keyboard management and decorators
"""
import logging
import threading
import time
import shutil
from pyrogram.types import ReplyKeyboardMarkup
from config import Config

logger = logging.getLogger(__name__)

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


# eternal reply-keyboard and reliable work with files
reply_keyboard_msg_ids = {}  # user_id: message_id


def send_reply_keyboard_always(user_id):
    """Send persistent reply keyboard to user"""
    global reply_keyboard_msg_ids
    from magic.handlers.commands import app
    
    try:
        msg_id = reply_keyboard_msg_ids.get(user_id)
        if msg_id:
            try:
                app.edit_message_text(user_id, msg_id, "\u2063", reply_markup=get_main_reply_keyboard())
                return
            except Exception as e:
                # Log only if the error is not MESSAGE_ID_INVALID
                if 'MESSAGE_ID_INVALID' not in str(e):
                    logger.warning(f"Failed to edit persistent reply keyboard: {e}")
                # If it didn't work, we delete the id to avoid getting stuck
                reply_keyboard_msg_ids.pop(user_id, None)
        # Always after failure or if there is no id - send a new one
        msg = app.send_message(user_id, "\u2063", reply_markup=get_main_reply_keyboard())
        # If there was another service msg_id (and it is not equal to the new one), we try to delete the old message
        if msg_id and msg_id != msg.id:
            try:
                app.delete_messages(user_id, [msg_id])
            except Exception as e:
                logger.warning(f"Failed to delete old reply keyboard message: {e}")
        reply_keyboard_msg_ids[user_id] = msg.id
    except Exception as e:
        logger.warning(f"Failed to send persistent reply keyboard: {e}")


# --- Wrapper for any custom action ---
def reply_with_keyboard(func):
    """Decorator to add reply keyboard after function execution"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Determine user_id from arguments (Pyrogram message/chat)
        user_id = None
        if 'message' in kwargs:
            user_id = getattr(kwargs['message'].chat, 'id', None)
        elif len(args) > 0 and hasattr(args[0], 'chat'):
            user_id = getattr(args[0].chat, 'id', None)
        elif len(args) > 1 and hasattr(args[1], 'chat'):
            user_id = getattr(args[1].chat, 'id', None)
        if user_id:
            send_reply_keyboard_always(user_id)
        return result

    return wrapper


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


def set_download_start_time(user_id):
    """Sets the download start time for a user"""
    with download_start_times_lock:
        download_start_times[user_id] = time.time()


def clear_download_start_time(user_id):
    """Clears the download start time for a user"""
    with download_start_times_lock:
        if user_id in download_start_times:
            del download_start_times[user_id]


def check_download_timeout(user_id):
    """Checks if the download timeout has been exceeded. For admins, timeout does not apply."""
    # If the user is an admin, timeout does not apply
    if hasattr(Config, 'ADMIN') and int(user_id) in Config.ADMIN:
        return False
    with download_start_times_lock:
        if user_id in download_start_times:
            start_time = download_start_times[user_id]
            current_time = time.time()
            if current_time - start_time > Config.DOWNLOAD_TIMEOUT:
                return True
    return False


def check_disk_space(path, required_bytes):
    """
    Checks if there's enough disk space available at the specified path.

    Args:
        path (str): Path to check
        required_bytes (int): Required bytes of free space

    Returns:
        bool: True if enough space is available, False otherwise
    """
    try:
        total, used, free = shutil.disk_usage(path)
        if free < required_bytes:
            from magic.utils.formatters import humanbytes
            logger.warning(
                f"Not enough disk space. Required: {humanbytes(required_bytes)}, Available: {humanbytes(free)}")
            return False
        return True
    except Exception as e:
        logger.error(f"Error checking disk space: {e}")
        return False


def get_active_download(user_id):
    """Get active download status for user"""
    with active_downloads_lock:
        return active_downloads.get(user_id, None)


def set_active_download(user_id, status):
    """Set active download status for user"""
    with active_downloads_lock:
        if status is None and user_id in active_downloads:
            del active_downloads[user_id]
        else:
            active_downloads[user_id] = status
