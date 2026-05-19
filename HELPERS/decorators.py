# Decorators for automatic app usage
from functools import wraps
import os
import threading
import concurrent.futures
# ####################################################################################
# Decorators for bot functionality
# ####################################################################################

from HELPERS.app_instance import get_app
from HELPERS.logger import logger
from HELPERS.safe_messeger import safe_send_message
from CONFIG.messages import Messages, safe_get_messages
from CONFIG.config import Config
from DATABASE.firebase_init import is_user_blocked, is_user_ignored

def app_handler(func):
    """Decorator to automatically inject app instance"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # If first argument is not app, inject it
        if args and hasattr(args[0], 'send_message'):
            # First argument is already app
            return func(*args, **kwargs)
        else:
            # Inject app as first argument
            app = get_app()
            return func(app, *args, **kwargs)
    return wrapper
# Get app instance
app = get_app()

# eternal reply-keyboard and reliable work with files
reply_keyboard_msg_ids = {}  # user_id: message_id
_reply_kb_cleanup_counter = 0
_REPLY_KB_CLEANUP_INTERVAL = 500  # Clean every 500 calls

def get_main_reply_keyboard(mode="2x3"):
    messages = safe_get_messages(None)
    """Function for permanent reply-keyboard"""
    from pyrogram.types import ReplyKeyboardMarkup
    
    if mode == "1x3":
        keyboard = [
            ["/clean", "/cookie", "/settings"]
        ]
    elif mode == "FULL":
        keyboard = [
            [messages.CLEAN_EMOJI, messages.COOKIE_EMOJI, messages.SETTINGS_EMOJI, messages.PROXY_EMOJI, messages.IMAGE_EMOJI, messages.SEARCH_EMOJI, messages.ARGS_EMOJI],
            [messages.VIDEO_EMOJI, messages.USAGE_EMOJI, messages.SPLIT_EMOJI, messages.AUDIO_EMOJI, messages.SUBTITLE_EMOJI, messages.LANGUAGE_EMOJI, messages.NSFW_EMOJI],
            [messages.TAG_EMOJI, messages.HELP_EMOJI, messages.LIST_EMOJI, messages.PLAY_EMOJI, messages.KEYBOARD_EMOJI, messages.LINK_EMOJI, "🧾"]
        ]
    else:  # 2x3 mode (default)
        keyboard = [
            ["/clean", "/cookie", "/settings"],
            ["/playlist", "/search", "/help"]
        ]
    
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )

def send_reply_keyboard_always(user_id, mode="2x3"):
    """Send persistent reply keyboard to user"""
    global reply_keyboard_msg_ids, _reply_kb_cleanup_counter
    try:
        # Periodic cleanup: limit dict size to prevent unbounded growth
        _reply_kb_cleanup_counter += 1
        if _reply_kb_cleanup_counter >= _REPLY_KB_CLEANUP_INTERVAL:
            _reply_kb_cleanup_counter = 0
            # Keep only last 2000 users
            if len(reply_keyboard_msg_ids) > 2000:
                reply_keyboard_msg_ids = dict(list(reply_keyboard_msg_ids.items())[-2000:])
                logger.debug(f"[KB-CLEANUP] Trimmed reply_keyboard_msg_ids to 2000 entries")
        msg_id = reply_keyboard_msg_ids.get(user_id)
        if msg_id:
            try:
                app.edit_message_text(user_id, msg_id, "\u2063", reply_markup=get_main_reply_keyboard(mode))
                return
            except Exception as e:
                # Log only if the error is not MESSAGE_ID_INVALID
                if 'MESSAGE_ID_INVALID' not in str(e):
                    logger.warning(f"Failed to edit persistent reply keyboard: {e}")
                # If it didn't work, we delete the id to avoid getting stuck
                reply_keyboard_msg_ids.pop(user_id, None)
        # Always after failure or if there is no id - send a new one
        msg = safe_send_message(user_id, "\u2063", reply_markup=get_main_reply_keyboard(mode))
        # If sending failed (e.g., FloodWait), don't try to access msg.id
        if not msg or not hasattr(msg, "id"):
            return
        # If there was another service msg_id (and it is not equal to the new one), we try to delete the old message
        if msg_id and msg_id != msg.id:
            try:
                app.delete_messages(user_id, [msg_id])
            except Exception as e:
                logger.warning(f"Failed to delete old reply keyboard message: {e}")
        reply_keyboard_msg_ids[user_id] = msg.id
    except Exception as e:
        logger.warning(f"Failed to send persistent reply keyboard: {e}")

# Удаляем конфликтующую функцию on_message из decorators.py
# Она должна быть только в handler_registry.py 

def _extract_user_id(args, kwargs):
    """Extract user_id from handler args/kwargs (Pyrogram message object)."""
    msg = _extract_message_arg(args, kwargs)
    return getattr(getattr(msg, 'chat', None), 'id', None) if msg else None


def _is_ignore_command(message):
    """Check if message text is an ignore/unignore command."""
    text = getattr(message, 'text', '')
    if isinstance(text, str):
        text = text.strip()
        return text.startswith(Config.IGNORE_USER_COMMAND) or text.startswith(Config.UNIGNORE_USER_COMMAND)
    return False


def _get_keyboard_mode(user_id):
    """Read keyboard mode for user from file. Returns (enabled, mode)."""
    keyboard_file = f'./users/{user_id}/keyboard.txt'
    if os.path.exists(keyboard_file):
        try:
            with open(keyboard_file, 'r') as f:
                setting = f.read().strip()
                if setting == "OFF":
                    return False, "2x3"
                if setting in ("1x3", "2x3", "FULL"):
                    return True, setting
        except Exception:
            pass
    return True, "2x3"


def reply_with_keyboard(func):
    """Wrapper for any custom action that adds reply keyboard."""
    def wrapper(*args, **kwargs):
        message = _extract_message_arg(args, kwargs)

        if message and not _is_ignore_command(message) and is_user_ignored(message):
            return

        result = func(*args, **kwargs)

        user_id = _extract_user_id(args, kwargs)
        if not user_id:
            return result

        if message and is_user_ignored(message):
            return result

        keyboard_enabled, keyboard_mode = _get_keyboard_mode(user_id)
        if not keyboard_enabled:
            return result

        is_kb_cmd = getattr(message, 'text', '') == "/keyboard" if message else False
        if not is_kb_cmd:
            send_reply_keyboard_always(user_id, keyboard_mode)

        return result

    return wrapper 


def _extract_message_arg(args, kwargs):
    """Return best-effort message-like object from handler args."""
    for obj in list(args) + list(kwargs.values()):
        if hasattr(obj, "chat"):
            return obj
        if hasattr(obj, "message") and getattr(obj, "message", None):
            return obj.message
    return None


def _format_handler_context(func_name, message_obj):
    chat = getattr(message_obj, "chat", None) if message_obj else None
    from_user = getattr(message_obj, "from_user", None) if message_obj else None
    chat_id = getattr(chat, "id", None)
    chat_type = getattr(chat, "type", None)
    from_id = getattr(from_user, "id", None)
    text = None
    for attr in ("text", "caption", "data"):
        value = getattr(message_obj, attr, None) if message_obj else None
        if value:
            text = value
            break
    if isinstance(text, str) and len(text) > 160:
        text = text[:157] + "..."
    return f"{func_name} chat={chat_id} type={chat_type} from={from_id} text={text!r}"


def background_handler(func=None, *, label=None):
    """
    Decorator that offloads a handler into a background ThreadPoolExecutor
    and logs its lifecycle so long-running jobs don't block Pyrogram updates.
    """
    if func is None:
        return lambda f: background_handler(f, label=label)

    # Global shared executor for background handlers.
    # Keep it here to avoid importing in every call and to share capacity across handlers.
    global _BG_EXECUTOR, _BG_INFLIGHT_SEM
    try:
        _BG_EXECUTOR
    except NameError:
        # Defaults chosen to keep bot responsive while allowing parallel heavy jobs.
        # If needed, expose these via Config/LimitsConfig later.
        _BG_EXECUTOR = concurrent.futures.ThreadPoolExecutor(
            max_workers=int(os.getenv("TG_YTDLP_BG_WORKERS", "32"))
        )
        _BG_INFLIGHT_SEM = threading.Semaphore(
            int(os.getenv("TG_YTDLP_BG_INFLIGHT", "256"))
        )

    @wraps(func)
    def wrapper(*args, **kwargs):
        message_obj = _extract_message_arg(args, kwargs)
        context = _format_handler_context(label or func.__name__, message_obj)
        logger.info(f"[INBOUND] {context}")
        # Try to enqueue into background pool. If overloaded, fail fast to avoid
        # unbounded queue growth and "bot looks alive but doesn't respond".
        acquired = False
        try:
            acquired = _BG_INFLIGHT_SEM.acquire(blocking=False)
            if not acquired:
                # Best-effort notify user when we can.
                try:
                    msg = safe_get_messages(getattr(getattr(message_obj, "chat", None), "id", None))
                    safe_send_message(
                        getattr(getattr(message_obj, "chat", None), "id", None),
                        getattr(msg, "BOT_BUSY_TRY_LATER_MSG", "⏳ Сейчас высокая нагрузка, попробуйте ещё раз через минуту."),
                        message=message_obj,
                    )
                except Exception:
                    pass
                logger.warning(f"[HANDLER-DROP] {context} (background queue full)")
                return None

            logger.info(f"[HANDLER-START] {context}")

            def _run():
                try:
                    result = func(*args, **kwargs)
                    logger.info(f"[HANDLER-DONE] {context}")
                    return result
                except Exception:
                    logger.exception(f"[HANDLER-CRASH] {context}")
                    raise
                finally:
                    try:
                        _BG_INFLIGHT_SEM.release()
                    except Exception:
                        pass

            _BG_EXECUTOR.submit(_run)
            # Important: return immediately so Pyrogram handler threads remain free.
            return None
        except Exception:
            # If we acquired but failed before submit, release to avoid capacity leak.
            if acquired:
                try:
                    _BG_INFLIGHT_SEM.release()
                except Exception:
                    pass
            logger.exception(f"[HANDLER-CRASH] {context}")
            raise

    return wrapper

def check_user_not_blocked(func):
    """Decorator to check if user is blocked before processing command."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        message = _extract_message_arg(args, kwargs)

        if message:
            user_id = message.chat.id
            is_admin = int(user_id) in Config.ADMIN

            if not _is_ignore_command(message) and is_user_ignored(message):
                return

            if not is_admin:
                text = getattr(message, 'text', '').strip() if hasattr(message, 'text') else ''
                is_block_cmd = text.startswith(Config.BLOCK_USER_COMMAND) or text.startswith(Config.UNBLOCK_USER_COMMAND)
                if not is_block_cmd and is_user_blocked(message):
                    return

        return func(*args, **kwargs)
    return wrapper

    