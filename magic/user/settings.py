"""User settings"""
import os
import logging
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from config import Config

logger = logging.getLogger(__name__)

# --- Function for reading split.txt ---
def get_user_split_size(user_id):
    user_dir = os.path.join("users", str(user_id))
    split_file = os.path.join(user_dir, "split.txt")
    if os.path.exists(split_file):
        try:
            with open(split_file, "r", encoding="utf-8") as f:
                size = int(f.read().strip())
                return size
        except Exception:
            pass
    return 1950 * 1024 * 1024  # default 1.95GB

def set_user_split_size(user_id, size):
    """Set user's split size preference"""
    user_dir = os.path.join("users", str(user_id))
    if not os.path.exists(user_dir):
        os.makedirs(user_dir, exist_ok=True)
    split_file = os.path.join(user_dir, "split.txt")
    try:
        with open(split_file, "w", encoding="utf-8") as f:
            f.write(str(size))
        return True
    except Exception as e:
        logger.error(f"Error setting split size for user {user_id}: {e}")
        return False

def is_mediainfo_enabled(user_id):
    user_dir = os.path.join("users", str(user_id))
    mediainfo_file = os.path.join(user_dir, "mediainfo.txt")
    if not os.path.exists(mediainfo_file):
        return False
    try:
        with open(mediainfo_file, "r", encoding="utf-8") as f:
            return f.read().strip().upper() == "ON"
    except Exception:
        return False

def set_user_mediainfo(user_id, enabled):
    """Set user's mediainfo preference"""
    user_dir = os.path.join("users", str(user_id))
    if not os.path.exists(user_dir):
        os.makedirs(user_dir, exist_ok=True)
    mediainfo_file = os.path.join(user_dir, "mediainfo.txt")
    try:
        with open(mediainfo_file, "w", encoding="utf-8") as f:
            f.write("ON" if enabled else "OFF")
        return True
    except Exception as e:
        logger.error(f"Error setting mediainfo for user {user_id}: {e}")
        return False

# Check the USAGE of the BOT
def is_user_in_channel(app, message):
    try:
        cht_member = app.get_chat_member(
            Config.SUBSCRIBE_CHANNEL, message.chat.id)
        if cht_member.status == ChatMemberStatus.MEMBER or cht_member.status == ChatMemberStatus.OWNER or cht_member.status == ChatMemberStatus.ADMINISTRATOR:
            return True

    except:

        text = f"{Config.TO_USE_MSG}\n \n{Config.CREDITS_MSG}"
        button = InlineKeyboardButton(
            "Join Channel", url=Config.SUBSCRIBE_CHANNEL_URL)
        keyboard = InlineKeyboardMarkup([[button]])
        # Use the send_message () Method to send the message with the button
        app.send_message(
            chat_id=message.chat.id,
            text=text,
            reply_markup=keyboard
        )
        return False
