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
# One keyboard refresh per user at a time: concurrent commands used to race on
# reply_keyboard_msg_ids and leave several empty "⁣" messages in the chat.
_reply_kb_locks = {}  # user_id: Lock
_reply_kb_locks_guard = threading.Lock()
_reply_kb_last = {}  # user_id: (mode, monotonic time of the last refresh)
_REPLY_KB_MIN_INTERVAL = 20  # seconds; a burst of commands refreshes the keyboard once

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
    import time
    with _reply_kb_locks_guard:
        lock = _reply_kb_locks.setdefault(user_id, threading.Lock())
    with lock:
        last = _reply_kb_last.get(user_id)
        if (last and last[0] == mode and reply_keyboard_msg_ids.get(user_id)
                and time.monotonic() - last[1] < _REPLY_KB_MIN_INTERVAL):
            return
        _send_reply_keyboard_locked(user_id, mode)
        if reply_keyboard_msg_ids.get(user_id):
            _reply_kb_last[user_id] = (mode, time.monotonic())


def _send_reply_keyboard_locked(user_id, mode):
    global reply_keyboard_msg_ids, _reply_kb_cleanup_counter
    try:
        # Periodic cleanup: limit dict size to prevent unbounded growth
        _reply_kb_cleanup_counter += 1
        if _reply_kb_cleanup_counter >= _REPLY_KB_CLEANUP_INTERVAL:
            _reply_kb_cleanup_counter = 0
            # Keep only last 2000 users
            if len(reply_keyboard_msg_ids) > 2000:
                reply_keyboard_msg_ids = dict(list(reply_keyboard_msg_ids.items())[-2000:])
                with _reply_kb_locks_guard:
                    for uid in list(_reply_kb_locks):
                        if uid not in reply_keyboard_msg_ids and not _reply_kb_locks[uid].locked():
                            _reply_kb_locks.pop(uid, None)
                            _reply_kb_last.pop(uid, None)
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


# Two pools keep handler work off Pyrogram's dispatcher threads (Client.executor,
# 8 threads by default): once every one of them was busy with a download, the
# bot accepted no updates at all while systemd still reported it alive.
#   * heavy: handlers explicitly marked @background_handler (downloads, uploads);
#     bounded by an inflight semaphore so overload is reported to the user;
#   * light: every other sync message/callback handler (menus, settings), routed
#     here by install_handler_offload(); never starved by downloads.
# The heavy pool is a priority queue ordered by (class, estimated size in MB):
# a single link starts first, several links in one message and playlists go to
# the back and may hold at most 3/4 of the workers and half of the queue, so they
# never lock single links out; inside a class the lighter job (lower quality,
# shorter, already cached) goes first, which empties the queue fastest.
PRIORITY_SINGLE, PRIORITY_NORMAL, PRIORITY_BULK = 0, 1, 2
UNKNOWN_COST_MB = 300.0
_BG_EXECUTOR = None
_BG_INFLIGHT_SEM = None
_BG_BULK_SEM = None
_LIGHT_EXECUTOR = None
_POOL_INIT_LOCK = threading.Lock()
_BG_QUEUED = [0]  # heavy tasks accepted but not yet started
_BG_QUEUED_LOCK = threading.Lock()
_OFFLOAD_WRAPPERS = set()  # ids of wrappers that already offload themselves


class _PriorityExecutor:
    """Fixed worker threads taking the lowest (priority, arrival) task first;
    bulk tasks run on at most `bulk_max` workers at once."""

    def __init__(self, workers, bulk_max, name):
        import heapq
        import itertools
        self._heapq = heapq
        self._seq = itertools.count()
        self._queue = []
        self._cv = threading.Condition()
        self._bulk_max = max(1, bulk_max)
        self._bulk_running = 0
        for i in range(workers):
            threading.Thread(target=self._work, name=f"{name}_{i}", daemon=True).start()

    def submit(self, fn, *args, priority=(PRIORITY_NORMAL, UNKNOWN_COST_MB)):
        if not isinstance(priority, tuple):
            priority = (priority, UNKNOWN_COST_MB)
        with self._cv:
            self._heapq.heappush(self._queue, (priority, next(self._seq), fn, args))
            self._cv.notify()

    def _take(self):
        with self._cv:
            while True:
                if self._queue and (self._queue[0][0][0] != PRIORITY_BULK or self._bulk_running < self._bulk_max):
                    priority, _, fn, args = self._heapq.heappop(self._queue)
                    if priority[0] == PRIORITY_BULK:
                        self._bulk_running += 1
                    return priority[0], fn, args
                self._cv.wait()

    def _work(self):
        while True:
            priority, fn, args = self._take()
            try:
                fn(*args)
            except Exception:
                logger.exception("[WORKERS] heavy task crashed")
            finally:
                if priority == PRIORITY_BULK:
                    with self._cv:
                        self._bulk_running -= 1
                        self._cv.notify_all()


def _init_pools():
    global _BG_EXECUTOR, _BG_INFLIGHT_SEM, _BG_BULK_SEM, _LIGHT_EXECUTOR
    with _POOL_INIT_LOCK:
        if _BG_EXECUTOR is not None:
            return
        from CONFIG.limits import LimitsConfig
        res = LimitsConfig.detect_system_resources()
        bg_workers = int(os.getenv("TG_YTDLP_BG_WORKERS", str(res['bg_workers'])))
        inflight = int(os.getenv("TG_YTDLP_BG_INFLIGHT", str(res['inflight'])))
        light_workers = int(os.getenv("TG_YTDLP_LIGHT_WORKERS", str(res.get('light_workers', 32))))
        _BG_EXECUTOR = _PriorityExecutor(bg_workers, bulk_max=bg_workers * 3 // 4, name="bg")
        _BG_INFLIGHT_SEM = threading.Semaphore(inflight)
        _BG_BULK_SEM = threading.Semaphore(max(1, inflight // 2))
        _LIGHT_EXECUTOR = concurrent.futures.ThreadPoolExecutor(max_workers=light_workers, thread_name_prefix="light")
        logger.info(
            f"[WORKERS] Auto-detected CPU={res['cpu_count']}: "
            f"bg_workers={bg_workers}, inflight={inflight}, light_workers={light_workers}, "
            f"max_uploads={res['max_uploads']}"
        )


_URL_RE = None


def message_has_url(message) -> bool:
    """True when the message text/caption carries a link (work that may download)."""
    global _URL_RE
    if _URL_RE is None:
        import re
        _URL_RE = re.compile(r"(?i)(?:https?://|www\.)\S|\b[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}/\S")
    text = (getattr(message, "text", None) or getattr(message, "caption", None) or "") if message else ""
    if not isinstance(text, str):
        return True
    if getattr(message, "entities", None) or getattr(message, "caption_entities", None):
        for ent in (getattr(message, "entities", None) or getattr(message, "caption_entities", None) or []):
            etype = str(getattr(ent, "type", "")).upper()
            if "URL" in etype or "TEXT_LINK" in etype:
                return True
    return bool(_URL_RE.search(text))


_PLAYLIST_HINTS = ("/playlist", "/sets/", "/album/", "/albums/")


def _request_text(message):
    """Text carrying the user's links: the message itself, or for a menu click the
    user's message the menu answers."""
    for obj in (message, getattr(message, "reply_to_message", None)):
        text = (getattr(obj, "text", None) or getattr(obj, "caption", None) or "") if obj else ""
        if isinstance(text, str) and ("http" in text or "www." in text):
            return text
    return ""


def request_priority(message) -> int:
    """PRIORITY_SINGLE for one link, PRIORITY_BULK for several links or a
    playlist (range syntax url*1*10, list=/playlist/sets/album URLs)."""
    import re
    text = _request_text(message)
    urls = re.findall(r"(?i)(?:https?://|www\.)\S+", text)
    if not urls:
        return PRIORITY_NORMAL
    if len(urls) > 1:
        return PRIORITY_BULK
    url = urls[0].lower()
    if re.search(r"\*-?\d+\*-?\d+", text) or ("list=" in url and "v=" not in url.replace("list=", ""))             or any(h in url for h in _PLAYLIST_HINTS):
        return PRIORITY_BULK
    return PRIORITY_SINGLE


def light_only(message=None) -> bool:
    """heavy_if for menu/settings handlers: they never download, never wait for the heavy pool."""
    return False


def background_queue_depth() -> int:
    """Heavy handler tasks waiting for a free worker (0 when the pool keeps up)."""
    return max(0, _BG_QUEUED[0])


def _extract_update(args, kwargs):
    """The Pyrogram update (Message or CallbackQuery) among handler args."""
    for obj in list(args) + list(kwargs.values()):
        if hasattr(obj, "data") or hasattr(obj, "chat"):
            return obj
    return None


def background_handler(func=None, *, label=None, heavy_if=None, cost_mb=None):
    """
    Decorator that offloads a handler into a background ThreadPoolExecutor
    and logs its lifecycle so long-running jobs don't block Pyrogram updates.

    heavy_if(update) -> bool: when given and False for this update (the Message or
    CallbackQuery), the call runs
    on the light pool instead, so commands and menus never queue behind downloads.
    cost_mb(update) -> float | None: estimated size of the job; lighter jobs start
    first within their priority class.
    """
    if func is None:
        return lambda f: background_handler(f, label=label, heavy_if=heavy_if, cost_mb=cost_mb)

    def _run_light(context, args, kwargs):
        logger.info(f"[HANDLER-START] {context}")
        try:
            from HELPERS.warp_tunnel import task_scope
            with task_scope(context):
                func(*args, **kwargs)
            logger.info(f"[HANDLER-DONE] {context}")
        except Exception:
            logger.exception(f"[HANDLER-CRASH] {context}")

    @wraps(func)
    def wrapper(*args, **kwargs):
        _init_pools()
        message_obj = _extract_message_arg(args, kwargs)
        context = _format_handler_context(label or func.__name__, message_obj)
        if heavy_if is not None:
            try:
                heavy = bool(heavy_if(_extract_update(args, kwargs)))
            except Exception:
                heavy = True
            if not heavy:
                logger.info(f"[INBOUND] {context} (light)")
                _LIGHT_EXECUTOR.submit(_run_light, context, args, kwargs)
                return None
        logger.info(f"[INBOUND] {context}")
        # Try to enqueue into background pool. If overloaded, fail fast to avoid
        # unbounded queue growth and "bot looks alive but doesn't respond".
        acquired = False
        bulk_acquired = False
        try:
            klass = request_priority(message_obj)
            cost = None
            if cost_mb is not None:
                try:
                    cost = cost_mb(_extract_update(args, kwargs))
                except Exception:
                    logger.debug(f"[HANDLER-QUEUED] cost estimate failed for {context}", exc_info=True)
            priority = (klass, round(float(UNKNOWN_COST_MB if cost is None else cost), 1))
            acquired = _BG_INFLIGHT_SEM.acquire(blocking=False)
            if acquired and klass == PRIORITY_BULK:
                bulk_acquired = _BG_BULK_SEM.acquire(blocking=False)
                if not bulk_acquired:
                    _BG_INFLIGHT_SEM.release()
                    acquired = False
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

            with _BG_QUEUED_LOCK:
                _BG_QUEUED[0] += 1
            logger.info(f"[HANDLER-QUEUED] {context} (waiting={background_queue_depth()}, priority={priority})")

            def _run():
                with _BG_QUEUED_LOCK:
                    _BG_QUEUED[0] -= 1
                logger.info(f"[HANDLER-START] {context}")
                try:
                    # one private WARP tunnel per task (WARP_PER_TASK), stopped when it ends
                    from HELPERS.warp_tunnel import task_scope
                    with task_scope(context):
                        result = func(*args, **kwargs)
                    logger.info(f"[HANDLER-DONE] {context}")
                    return result
                except Exception:
                    logger.exception(f"[HANDLER-CRASH] {context}")
                finally:
                    _BG_INFLIGHT_SEM.release()
                    if bulk_acquired:
                        _BG_BULK_SEM.release()

            _BG_EXECUTOR.submit(_run, priority=priority)
            # Important: return immediately so Pyrogram handler threads remain free.
            return None
        except Exception:
            # If we acquired but failed before submit, release to avoid capacity leak.
            if acquired:
                _BG_INFLIGHT_SEM.release()
            if bulk_acquired:
                _BG_BULK_SEM.release()
            logger.exception(f"[HANDLER-CRASH] {context}")
            raise

    _OFFLOAD_WRAPPERS.add(id(wrapper))
    return wrapper


def _light_offload(func):
    """Run a sync handler on the light pool and return to the dispatcher at once."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        _init_pools()

        def _run():
            try:
                from HELPERS.warp_tunnel import task_scope
                with task_scope(f"{func.__name__} chat={getattr(getattr(_extract_message_arg(args, kwargs), 'chat', None), 'id', None)}"):
                    func(*args, **kwargs)
            except Exception:
                message_obj = _extract_message_arg(args, kwargs)
                logger.exception(f"[HANDLER-CRASH] {_format_handler_context(func.__name__, message_obj)}")

        _LIGHT_EXECUTOR.submit(_run)

    return wrapper


def install_handler_offload(client):
    """Make every sync on_message/on_callback_query handler of `client` return to
    the Pyrogram dispatcher immediately.

    Registration still happens through Pyrogram's own decorators; the module-level
    name keeps the original function, so direct calls stay synchronous. Handlers
    already wrapped by @background_handler (the outermost decorator) keep their
    own heavy-pool offload.
    """
    import inspect

    def patch(name):
        original = getattr(client, name)

        def decorator_factory(*args, **kwargs):
            register = original(*args, **kwargs)

            def decorator(func):
                target = func
                if not inspect.iscoroutinefunction(func) and id(func) not in _OFFLOAD_WRAPPERS:
                    target = _light_offload(func)
                register(target)
                return func

            return decorator

        setattr(client, name, decorator_factory)

    for name in ("on_message", "on_callback_query"):
        patch(name)

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

    