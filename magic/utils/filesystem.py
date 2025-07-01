"""
Filesystem utilities for the bot
"""
import os
import threading
import tempfile
import time
from typing import Optional


def create_directory(path):
    """
    Create The Directory (And All Intermediate Directories) IF Its Not Exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def check_disk_space(path, required_bytes):
    """
    Check if there's enough disk space for download
    """
    try:
        # Get available disk space
        statvfs = os.statvfs(path)
        available_bytes = statvfs.f_frsize * statvfs.f_available
        
        # Add 10% buffer to required space
        required_with_buffer = required_bytes * 1.1
        
        return available_bytes >= required_with_buffer
    except Exception as e:
        # If we can't check disk space, assume we have enough
        return True


def cleanup_temp_files():
    """Clean up temporary files across all user directories"""
    if not os.path.exists("users"):
        return

    import logging
    logger = logging.getLogger(__name__)
    
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
                            logger.error(f"Error removing temp file {filename}: {e}")
        except Exception as e:
            logger.error(f"Error cleaning up user directory {user_dir}: {e}")


def cleanup_user_temp_files(user_id):
    """Clean up temporary files for a specific user"""
    import logging
    logger = logging.getLogger(__name__)
    
    user_dir = os.path.join("users", str(user_id))
    if not os.path.exists(user_dir):
        return

    try:
        for filename in os.listdir(user_dir):
            file_path = os.path.join(user_dir, filename)
            try:
                # Remove temporary files
                if filename.endswith(('.part', '.ytdl', '.temp', '.tmp')):
                    os.remove(file_path)
                    logger.info(f"Removed temp file: {filename}")
                # Remove old files (older than 1 hour)
                elif os.path.isfile(file_path):
                    file_age = time.time() - os.path.getmtime(file_path)
                    if file_age > 3600:  # 1 hour
                        os.remove(file_path)
                        logger.info(f"Removed old file: {filename}")
            except Exception as e:
                logger.error(f"Error removing file {filename}: {e}")
    except Exception as e:
        logger.error(f"Error cleaning up user {user_id} temp files: {e}")


def remove_media(message, only=None):
    """
    Remove media files for a user
    
    Args:
        message: Telegram message object
        only: Optional filter ('cookies', 'logs', 'tags', 'format', 'split', 'mediainfo')
    """
    from config import Config
    import logging
    logger = logging.getLogger(__name__)
    
    user_id = message.chat.id
    user_dir = os.path.join("users", str(user_id))
    
    if not os.path.exists(user_dir):
        return "No files found to remove."
    
    removed_files = []
    errors = []
    
    try:
        for filename in os.listdir(user_dir):
            file_path = os.path.join(user_dir, filename)
            should_remove = False
            
            if only == "cookies" and filename == Config.COOKIE_FILE_PATH:
                should_remove = True
            elif only == "logs" and filename == "logs.txt":
                should_remove = True
            elif only == "tags" and filename == "tags.txt":
                should_remove = True
            elif only == "format" and filename == "format.txt":
                should_remove = True
            elif only == "split" and filename == "split_size.txt":
                should_remove = True
            elif only == "mediainfo" and filename == "mediainfo.txt":
                should_remove = True
            elif only is None and not filename.endswith(('.txt')):
                # Remove media files only (not settings)
                should_remove = True
            elif only == "all":
                should_remove = True
            
            if should_remove:
                try:
                    os.remove(file_path)
                    removed_files.append(filename)
                except Exception as e:
                    errors.append(f"{filename}: {str(e)}")
    
    except Exception as e:
        logger.error(f"Error listing directory {user_dir}: {e}")
        return f"Error accessing user files: {str(e)}"
    
    result = ""
    if removed_files:
        result += f"✅ Removed {len(removed_files)} files:\n"
        result += "\n".join(f"• {file}" for file in removed_files[:10])  # Show max 10
        if len(removed_files) > 10:
            result += f"\n• ... and {len(removed_files) - 10} more"
    
    if errors:
        result += f"\n\n❌ Failed to remove {len(errors)} files:\n"
        result += "\n".join(f"• {error}" for error in errors[:5])  # Show max 5 errors
        if len(errors) > 5:
            result += f"\n• ... and {len(errors) - 5} more errors"
    
    if not removed_files and not errors:
        if only:
            result = f"No {only} files found to remove."
        else:
            result = "No files found to remove."
    
    return result


def create_default_thumbnail(thumb_path):
    """
    Create a default thumbnail if none exists
    """
    try:
        # Try to create a simple default thumbnail
        # This is a placeholder - in real implementation you might want to
        # create an actual image or copy from a default template
        with open(thumb_path, 'w') as f:
            f.write("default_thumb")
        return thumb_path
    except Exception:
        return None


# Active downloads tracking
_active_downloads = {}
_downloads_lock = threading.Lock()


def get_active_download(user_id):
    """Get active download status for user"""
    with _downloads_lock:
        return _active_downloads.get(user_id, False)


def set_active_download(user_id, status):
    """Set active download status for user"""
    with _downloads_lock:
        if status:
            _active_downloads[user_id] = True
        else:
            _active_downloads.pop(user_id, None)


# Download timing tracking
_download_start_times = {}
_timing_lock = threading.Lock()


def set_download_start_time(user_id):
    """Record when a download started"""
    with _timing_lock:
        _download_start_times[user_id] = time.time()


def clear_download_start_time(user_id):
    """Clear download start time"""
    with _timing_lock:
        _download_start_times.pop(user_id, None)


def check_download_timeout(user_id):
    """Check if download has exceeded timeout"""
    from config import Config
    
    with _timing_lock:
        start_time = _download_start_times.get(user_id)
        if start_time:
            elapsed = time.time() - start_time
            if elapsed > Config.DOWNLOAD_TIMEOUT:
                return True
    return False 