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
from CONFIG.messages import safe_get_messages
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

def get_main_reply_keyboard(mode="2x3"):
    messages = safe_get_messages(None)
    """Function for persistent reply-keyboard (is_persistent=True)"""
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
        is_persistent=True,
        resize_keyboard=True,
        one_time_keyboard=False
    )

# Удаляем конфликтующую функцию on_message из decorators.py
# Она должна быть только в handler_registry.py 

def _is_ignore_command(message):
    """Check if message text is an ignore/unignore command."""
    text = getattr(message, 'text', '')
    if isinstance(text, str):
        text = text.strip()
        return text.startswith(Config.IGNORE_USER_COMMAND) or text.startswith(Config.UNIGNORE_USER_COMMAND)
    return False


def reply_with_keyboard(func):
    """Wrapper: checks ignored users. Reply keyboard persistence is handled by is_persistent=True."""
    def wrapper(*args, **kwargs):
        message = _extract_message_arg(args, kwargs)

        if message and not _is_ignore_command(message) and is_user_ignored(message):
            return

        return func(*args, **kwargs)

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

    