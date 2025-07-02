"""
Filesystem utilities and operations
"""
import os
import shutil
import time
import threading
import logging
from config import Config

logger = logging.getLogger(__name__)

# Global dictionary to track active downloads and lock for thread-safe access
active_downloads = {}
active_downloads_lock = threading.Lock()

# Add a global dictionary to track download start times
download_start_times = {}
download_start_times_lock = threading.Lock()


def create_directory(path):
    # Create The Directory (And All Intermediate Directories) IF Its Not Exist.
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def set_download_start_time(user_id):
    """
    Sets the download start time for a user
    """
    with download_start_times_lock:
        download_start_times[user_id] = time.time()


def clear_download_start_time(user_id):
    """
    Clears the download start time for a user
    """
    with download_start_times_lock:
        if user_id in download_start_times:
            del download_start_times[user_id]


def check_download_timeout(user_id):
    """
    Checks if the download timeout has been exceeded. For admins, timeout does not apply.
    """
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
        from ..utils.formatters import humanbytes
        total, used, free = shutil.disk_usage(path)
        if free < required_bytes:
            logger.warning(
                f"Not enough disk space. Required: {humanbytes(required_bytes)}, Available: {humanbytes(free)}")
            return False
        return True
    except Exception as e:
        logger.error(f"Error checking disk space: {e}")
        # If we can't check, assume there's enough space
        return True


def get_active_download(user_id):
    """
    Get active download status for user
    """
    with active_downloads_lock:
        return active_downloads.get(user_id, None)


def set_active_download(user_id, status):
    """
    Set active download status for user
    """
    with active_downloads_lock:
        if status is None:
            active_downloads.pop(user_id, None)
        else:
            active_downloads[user_id] = status


def cleanup_temp_files():
    """
    Clean up temporary files
    """
    try:
        # Clean up temporary files in downloads directory
        downloads_dir = "downloads"
        if os.path.exists(downloads_dir):
            for filename in os.listdir(downloads_dir):
                if filename.startswith("temp_") or filename.endswith(".tmp"):
                    file_path = os.path.join(downloads_dir, filename)
                    try:
                        os.remove(file_path)
                        logger.info(f"Removed temp file: {file_path}")
                    except Exception as e:
                        logger.warning(f"Failed to remove temp file {file_path}: {e}")
    except Exception as e:
        logger.error(f"Error during cleanup: {e}")


def cleanup_user_temp_files(user_id):
    """
    Clean up temporary files for specific user
    """
    try:
        user_dir = os.path.join("users", str(user_id))
        if os.path.exists(user_dir):
            for filename in os.listdir(user_dir):
                if filename.startswith("temp_") or filename.endswith(".tmp"):
                    file_path = os.path.join(user_dir, filename)
                    try:
                        os.remove(file_path)
                        logger.info(f"Removed user temp file: {file_path}")
                    except Exception as e:
                        logger.warning(f"Failed to remove user temp file {file_path}: {e}")
    except Exception as e:
        logger.error(f"Error during user cleanup: {e}")


def sanitize_filename(filename, max_length=150):
    """
    Sanitize filename to remove invalid characters
    """
    if not filename:
        return "untitled"
        
    # Remove or replace invalid characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Remove multiple consecutive underscores
    while '__' in filename:
        filename = filename.replace('__', '_')
    
    # Remove leading/trailing dots and spaces
    filename = filename.strip('. ')
    
    # Truncate if too long
    if len(filename) > max_length:
        name, ext = os.path.splitext(filename)
        filename = name[:max_length-len(ext)] + ext
    
    return filename if filename else "untitled"

# Global dictionary to track playlist errors and lock for thread-safe access
playlist_errors = {}
playlist_errors_lock = threading.Lock()

# Global starting point list (do not modify)
starting_point = []
