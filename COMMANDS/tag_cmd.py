from HELPERS.app_instance import get_app
from pyrogram import filters
import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyParameters
from HELPERS.safe_messeger import safe_send_message
from HELPERS.decorators import background_handler
from CONFIG.config import Config
from HELPERS.logger import send_to_logger
from HELPERS.limitter import is_user_in_channel
from CONFIG.messages import Messages, safe_get_messages

# Get app instance for decorators
app = get_app()

@app.on_message(filters.command("tags") & filters.private)
# @reply_with_keyboard
@background_handler(label="tags_command")
def tags_command(app, message):
    messages = safe_get_messages(message.chat.id)
    user_id = message.chat.id
    is_admin = int(user_id) in Config.ADMIN
    
    # Check if user is ignored (even admins can be ignored, but ignore/unignore commands are always allowed) - highest priority
    text = getattr(message, 'text', '').strip() if hasattr(message, 'text') else ''
    is_ignore_command = text.startswith(Config.IGNORE_USER_COMMAND) or text.startswith(Config.UNIGNORE_USER_COMMAND)
    
    if not is_ignore_command:
        from DATABASE.firebase_init import is_user_ignored
        if is_user_ignored(message):
            return  # User is ignored, no response at all (even for admins)
    
    # Check if user is blocked (except for admins)
    if not is_admin:
        from DATABASE.firebase_init import is_user_blocked
        if is_user_blocked(message):
            return  # User is blocked, message already sent by is_user_blocked
    
    # Subscription check for non-admins
    if not is_admin and not is_user_in_channel(app, message):
        return
    user_dir = os.path.join("users", str(user_id))
    tags_file = os.path.join(user_dir, "tags.txt")
    if not os.path.exists(tags_file):
        reply_text = safe_get_messages(user_id).TAGS_NO_TAGS_MSG
        safe_send_message(user_id, reply_text, reply_parameters=ReplyParameters(message_id=message.id))
        send_to_logger(message, reply_text)
        return
    with open(tags_file, "r", encoding="utf-8") as f:
        tags = [line.strip() for line in f if line.strip()]
    if not tags:
        reply_text = safe_get_messages(user_id).TAGS_NO_TAGS_MSG
        safe_send_message(user_id, reply_text, reply_parameters=ReplyParameters(message_id=message.id))
        send_to_logger(message, reply_text)
        return
    # We form posts by 4096 characters
    msg = ''
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(safe_get_messages(user_id).TAG_CLOSE_BUTTON_MSG, callback_data="tags_close|close")]
    ])
    for tag in tags:
        if len(msg) + len(tag) + 1 > 4096:
            safe_send_message(user_id, msg, reply_parameters=ReplyParameters(message_id=message.id), reply_markup=keyboard)
            send_to_logger(message, msg)
            msg = ''
        msg += tag + '\n'
    if msg:
        safe_send_message(user_id, msg, reply_parameters=ReplyParameters(message_id=message.id), reply_markup=keyboard)
        send_to_logger(message, msg)

@app.on_callback_query(filters.regex(r"^tags_close\|"))
def tags_close_callback(app, callback_query):
    messages = safe_get_messages(None)
    data = callback_query.data.split("|")[1]
    if data == "close":
        try:
            callback_query.message.delete()
        except Exception:
            callback_query.edit_message_reply_markup(reply_markup=None)
        callback_query.answer(safe_get_messages(user_id).TAGS_MESSAGE_CLOSED_MSG)
        send_to_logger(callback_query.message, safe_get_messages(user_id).TAGS_MESSAGE_CLOSED_MSG)
        return

    data = callback_query.data.split("|")[1]
    if data == "close":
        try:
            callback_query.message.delete()
        except Exception:
            callback_query.edit_message_reply_markup(reply_markup=None)
        callback_query.answer(safe_get_messages(user_id).TAGS_MESSAGE_CLOSED_MSG)
        send_to_logger(callback_query.message, safe_get_messages(user_id).TAGS_MESSAGE_CLOSED_MSG)
        return