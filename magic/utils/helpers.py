"""
Helper utilities for bot operations
"""
import logging
import asyncio
import time
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from typing import Optional, List, Any


logger = logging.getLogger(__name__)


def get_main_reply_keyboard():
    """Get main reply keyboard for the bot"""
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("📺 Download Video")],
        [KeyboardButton("🎵 Audio Only"), KeyboardButton("📋 Playlist")],
        [KeyboardButton("⚙️ Settings"), KeyboardButton("❓ Help")]
    ], resize_keyboard=True)
    return keyboard


def send_reply_keyboard_always(user_id):
    """Always send reply keyboard to user"""
    try:
        from magic import app
        keyboard = get_main_reply_keyboard()
        app.send_message(user_id, "🤖 Choose an option:", reply_markup=keyboard)
    except Exception as e:
        logger.error(f"Error sending reply keyboard: {e}")


def reply_with_keyboard(func):
    """Decorator to add reply keyboard to responses"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # Try to get user_id from message
        try:
            if len(args) >= 2:
                message = args[1]  # Usually second argument is message
                if hasattr(message, 'chat') and hasattr(message.chat, 'id'):
                    user_id = message.chat.id
                    send_reply_keyboard_always(user_id)
        except Exception:
            pass
        
        return result
    return wrapper


def safe_send_message(chat_id, text, **kwargs):
    """Safely send message with error handling"""
    try:
        from magic import app
        
        # Add reply_to_message_id if message is passed
        if 'message' in kwargs:
            message = kwargs.pop('message')
            if hasattr(message, 'id'):
                kwargs['reply_to_message_id'] = message.id
        
        return app.send_message(chat_id, text, **kwargs)
    
    except Exception as e:
        logger.error(f"Error sending message to {chat_id}: {e}")
        return None


def safe_edit_message_text(chat_id, message_id, text, **kwargs):
    """Safely edit message text with error handling"""
    try:
        from magic import app
        return app.edit_message_text(chat_id, message_id, text, **kwargs)
    
    except Exception as e:
        logger.error(f"Error editing message {message_id} in {chat_id}: {e}")
        return None


def safe_delete_messages(chat_id, message_ids, **kwargs):
    """Safely delete messages with error handling"""
    try:
        from magic import app
        
        # Handle single message ID
        if isinstance(message_ids, int):
            message_ids = [message_ids]
        
        return app.delete_messages(chat_id, message_ids, **kwargs)
    
    except Exception as e:
        logger.error(f"Error deleting messages {message_ids} in {chat_id}: {e}")
        return None


def safe_forward_messages(chat_id, from_chat_id, message_ids, **kwargs):
    """Safely forward messages with error handling"""
    try:
        from magic import app
        
        # Handle single message ID
        if isinstance(message_ids, int):
            message_ids = [message_ids]
        
        return app.forward_messages(chat_id, from_chat_id, message_ids, **kwargs)
    
    except Exception as e:
        logger.error(f"Error forwarding messages {message_ids} from {from_chat_id} to {chat_id}: {e}")
        return None


def start_hourglass_animation(user_id, hourglass_msg_id, stop_anim):
    """Start hourglass animation for long operations"""
    import threading
    
    def animate_hourglass():
        hourglass_frames = ["⏳", "⌛"]
        frame_index = 0
        
        while not stop_anim[0]:
            try:
                frame = hourglass_frames[frame_index % len(hourglass_frames)]
                safe_edit_message_text(
                    user_id, 
                    hourglass_msg_id, 
                    f"{frame} Processing..."
                )
                frame_index += 1
                time.sleep(1)
            except Exception as e:
                logger.error(f"Error in hourglass animation: {e}")
                break
    
    # Start animation in separate thread
    thread = threading.Thread(target=animate_hourglass)
    thread.daemon = True
    thread.start()
    
    return thread


def start_cycle_progress(user_id, proc_msg_id, current_total_process, user_dir_name, cycle_stop):
    """Start cycle progress animation"""
    import threading
    import os
    
    def cycle_progress():
        cycle_frames = ["🔄", "🔃", "🔁", "🔄"]
        frame_index = 0
        
        while not cycle_stop[0]:
            try:
                frame = cycle_frames[frame_index % len(cycle_frames)]
                
                # Get current process info
                process_text = ""
                if current_total_process[0] > 0:
                    process_text = f" ({current_total_process[0]} processed)"
                
                # Check if user directory exists
                user_path = os.path.join("users", user_dir_name)
                status = "Active" if os.path.exists(user_path) else "Waiting"
                
                safe_edit_message_text(
                    user_id,
                    proc_msg_id,
                    f"{frame} {status}{process_text}..."
                )
                
                frame_index += 1
                time.sleep(2)
                
            except Exception as e:
                logger.error(f"Error in cycle progress: {e}")
                break
    
    # Start animation in separate thread
    thread = threading.Thread(target=cycle_progress)
    thread.daemon = True
    thread.start()
    
    return thread


def format_progress_bar(current: int, total: int, width: int = 20) -> str:
    """Format progress bar for display"""
    if total == 0:
        return "█" * width
    
    progress = current / total
    filled = int(width * progress)
    bar = "█" * filled + "░" * (width - filled)
    percentage = progress * 100
    
    return f"{bar} {percentage:.1f}%"


def extract_user_command(message) -> Optional[str]:
    """Extract command from message"""
    try:
        if hasattr(message, 'command') and message.command:
            return message.command[0]
        elif hasattr(message, 'text') and message.text:
            if message.text.startswith('/'):
                return message.text.split()[0][1:]  # Remove '/' prefix
        return None
    except Exception:
        return None 