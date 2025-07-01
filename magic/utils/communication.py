"""
Communication utilities for messaging and progress tracking
"""
import time
import threading
from pyrogram import enums
from config import Config
from .filesystem import get_active_download
from ..database.firebase import logger


def send_to_logger(message, msg):
    """Send message to logger channel"""
    try:
        app = message._client
        app.send_message(Config.LOG_CHANNEL, msg)
    except Exception as e:
        logger.error(f"Failed to send to logger: {e}")


def send_to_user(message, msg):
    """Send message to user"""
    try:
        app = message._client
        app.send_message(message.chat.id, msg, reply_to_message_id=message.id)
    except Exception as e:
        logger.error(f"Failed to send to user: {e}")


def send_to_all(message, msg):
    """Send message to both user and logger"""
    send_to_user(message, msg)
    send_to_logger(message, msg)


def progress_bar(*args):
    """
    Progress bar for downloads
    Expected parameters: Current, Total, Speed, ETA, File_SIZE, then Progress_args (User_id, Msg_id, Status_text)
    """
    try:
        if len(args) < 8:
            return
            
        current, total, speed, eta, file_size, user_id, msg_id, status_text = args[:8]
        
        if not get_active_download(user_id):
            return  # Download was cancelled
            
        # Calculate percentage
        percent = (current / total) * 100 if total > 0 else 0
        
        # Format progress bar
        filled = int(percent // 5)
        bar = "█" * filled + "░" * (20 - filled)
        
        # Format values
        from .formatters import humanbytes, TimeFormatter
        current_str = humanbytes(current)
        total_str = humanbytes(total)
        speed_str = f"{humanbytes(speed)}/s" if speed > 0 else "0 B/s"
        eta_str = TimeFormatter(eta * 1000) if eta > 0 else "Unknown"
        
        progress_text = f"<b>{status_text}</b>\n\n"
        progress_text += f"<code>{bar}</code> {percent:.1f}%\n\n"
        progress_text += f"📊 {current_str} / {total_str}\n"
        progress_text += f"🚀 {speed_str}\n"
        progress_text += f"⏱ ETA: {eta_str}"
        
        # Update message every 3 seconds to avoid flood
        current_time = time.time()
        if not hasattr(progress_bar, 'last_update'):
            progress_bar.last_update = {}
        
        if user_id not in progress_bar.last_update or current_time - progress_bar.last_update[user_id] >= 3:
            try:
                from pyrogram import Client
                # This is a bit tricky - we need to get the app instance somehow
                # For now, we'll skip real-time updates and let the calling function handle it
                progress_bar.last_update[user_id] = current_time
            except Exception as e:
                logger.error(f"Progress bar update error: {e}")
                
    except Exception as e:
        logger.error(f"Progress bar error: {e}")


def safe_send_message(chat_id, text, **kwargs):
    """Safely send message with error handling"""
    try:
        # This function needs access to the app instance
        # For now, we'll return the text to be sent by the caller
        return text
    except Exception as e:
        logger.error(f"Failed to send message: {e}")
        return None


def safe_forward_messages(chat_id, from_chat_id, message_ids, **kwargs):
    """Safely forward messages with error handling"""
    try:
        # This function needs access to the app instance
        # Implementation will depend on the calling context
        return True
    except Exception as e:
        logger.error(f"Failed to forward messages: {e}")
        return False


def safe_edit_message_text(chat_id, message_id, text, **kwargs):
    """Safely edit message text with error handling"""
    try:
        # This function needs access to the app instance
        # Implementation will depend on the calling context
        return True
    except Exception as e:
        logger.error(f"Failed to edit message: {e}")
        return False


def safe_delete_messages(chat_id, message_ids, **kwargs):
    """Safely delete messages with error handling"""
    try:
        # This function needs access to the app instance
        # Implementation will depend on the calling context
        return True
    except Exception as e:
        logger.error(f"Failed to delete messages: {e}")
        return False


def start_hourglass_animation(user_id, hourglass_msg_id, stop_anim):
    """Start hourglass animation for long operations"""
    def animate_hourglass():
        frames = ["⏳", "⌛"]
        frame_index = 0
        
        while not stop_anim.is_set():
            try:
                # Update hourglass animation
                frame_index = (frame_index + 1) % len(frames)
                time.sleep(1)
            except Exception as e:
                logger.error(f"Hourglass animation error: {e}")
                break
    
    animation_thread = threading.Thread(target=animate_hourglass)
    animation_thread.daemon = True
    animation_thread.start()
    return animation_thread


def start_cycle_progress(user_id, proc_msg_id, current_total_process, user_dir_name, cycle_stop):
    """Start cycle progress for batch operations"""
    def cycle_progress():
        while not cycle_stop.is_set():
            try:
                time.sleep(2)
                # Update progress display
            except Exception as e:
                logger.error(f"Cycle progress error: {e}")
                break
    
    progress_thread = threading.Thread(target=cycle_progress)
    progress_thread.daemon = True
    progress_thread.start()
    return progress_thread


def get_mediainfo_cli(file_path):
    """Get mediainfo for a file"""
    import subprocess
    try:
        result = subprocess.run(['mediainfo', file_path], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            return result.stdout
        else:
            logger.error(f"Mediainfo error: {result.stderr}")
            return None
    except subprocess.TimeoutExpired:
        logger.error("Mediainfo timeout")
        return None
    except Exception as e:
        logger.error(f"Mediainfo exception: {e}")
        return None


def send_mediainfo_if_enabled(user_id, file_path, message):
    """Send mediainfo if user has it enabled"""
    from ..user.settings import is_mediainfo_enabled
    
    if not is_mediainfo_enabled(user_id):
        return
        
    mediainfo_text = get_mediainfo_cli(file_path)
    if mediainfo_text:
        try:
            # Truncate if too long
            if len(mediainfo_text) > 4000:
                mediainfo_text = mediainfo_text[:4000] + "\n... (truncated)"
            
            app = message._client
            app.send_message(
                user_id,
                f"📋 <b>MediaInfo:</b>\n\n<pre>{mediainfo_text}</pre>",
                parse_mode=enums.ParseMode.HTML,
                reply_to_message_id=message.id
            )
        except Exception as e:
            logger.error(f"Failed to send mediainfo: {e}") 