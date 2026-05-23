# #############################################################################################################################
import re
import time
import logging
import threading
import asyncio
import concurrent.futures
import inspect
from types import SimpleNamespace
from HELPERS.app_instance import get_app
from CONFIG.messages import Messages, safe_get_messages
from pyrogram.errors import FloodWait
import os
from pyrogram.types import ReplyParameters
from pyrogram import enums

# Configure local logger
logger = logging.getLogger(__name__)

# Global message sending throttle to prevent msg_seqno issues
# Per-chat throttling: each chat has its own timing, no cross-chat blocking
_last_message_sent = {}
_message_send_locks = {}  # {chat_id: threading.Lock()}
_message_send_locks_lock = threading.Lock()

# Periodic cleanup for _last_message_sent to prevent unbounded growth
_last_msg_ts_cleanup = 0
_MSG_TS_CLEANUP_INTERVAL = 300  # Every 5 minutes

# Module-level storage for last edit timestamps per chat (throttle edits in groups)
_last_edit_ts_per_chat = {}
_last_edit_cleanup_ts = 0

# Get app instance dynamically to avoid None issues
def get_app_safe():
    app = get_app()
    if app is None:
        raise RuntimeError(safe_get_messages(None).HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG)
    return app


def run_pyrogram_client_coroutine(app, coro, timeout=30):
    """Выполнить async-метод Pyrogram Client из sync-кода (обработчики в executor)."""
    # В некоторых окружениях используется sync-Client (методы возвращают Message/результат сразу),
    # а не coroutine. В таком случае не трогаем asyncio вовсе.
    try:
        if not inspect.isawaitable(coro):
            return coro
    except Exception:
        # Если не смогли определить awaitable — лучше не падать.
        return coro

    # asyncio.run_coroutine_threadsafe принимает только coroutine object.
    # Pyrogram может возвращать awaitable-объект (имеет __await__), который НЕ является coroutine.
    try:
        if not inspect.iscoroutine(coro):
            async def _wrap(awaitable):
                return await awaitable
            coro = _wrap(coro)
    except Exception:
        pass

    loop = getattr(app, "loop", None)
    if loop is None:
        # Если это awaitable, но loop почему-то недоступен — попробуем выполнить в отдельном loop,
        # чтобы не блокировать основную логику.
        try:
            return asyncio.run(coro)
        except RuntimeError:
            # Уже внутри event loop (не наш случай для sync-хендлеров) — просто пробросим.
            raise RuntimeError("Pyrogram client event loop is not available")

    # If we're already executing inside the same event loop, waiting on
    # run_coroutine_threadsafe().result() would deadlock. In that case, schedule
    # the coroutine and return the Task (best-effort fire-and-forget).
    try:
        running = asyncio.get_running_loop()
    except RuntimeError:
        running = None
    if running is loop:
        try:
            return asyncio.create_task(coro)
        except Exception:
            return None

    fut = asyncio.run_coroutine_threadsafe(coro, loop)
    try:
        return fut.result(timeout=timeout)
    except concurrent.futures.TimeoutError:
        logger.error(f"Pyrogram client call timed out after {timeout}s")
        raise

def fake_message(text, user_id, command=None, original_chat_id=None, message_thread_id=None, original_message=None):
    _messages = safe_get_messages(user_id)
    m = SimpleNamespace()
    m.chat = SimpleNamespace()
    # Ensure user_id is int (convert from string if needed)
    if isinstance(user_id, str):
        try:
            user_id = int(user_id)
        except (ValueError, TypeError):
            user_id = 0
    # Ensure original_chat_id is int if provided
    if original_chat_id is not None and isinstance(original_chat_id, str):
        try:
            original_chat_id = int(original_chat_id)
        except (ValueError, TypeError):
            original_chat_id = None
    # Use original_chat_id if provided, otherwise use user_id
    # Ensure we have a valid chat_id (fallback to -1 if both are None)
    chat_id = original_chat_id if original_chat_id is not None else user_id
    if chat_id is None:
        chat_id = -1  # Fallback for gallery-dl operations
    m.chat.id = chat_id
    m.chat.first_name = safe_get_messages(user_id).HELPER_USER_NAME_MSG
    # Set chat type based on chat_id (negative = group, positive = private)
    # Ensure we compare numbers, not strings
    comparison_id = int(original_chat_id) if original_chat_id is not None else int(user_id)
    m.chat.type = enums.ChatType.PRIVATE if comparison_id > 0 else enums.ChatType.SUPERGROUP
    m.text = text
    m.first_name = m.chat.first_name
    m.reply_to_message = None
    m.id = 0
    m.from_user = SimpleNamespace()
    m.from_user.id = user_id
    m.from_user.first_name = m.chat.first_name
    # ЖЕСТКО: Помечаем как fake message для правильной обработки платных медиа
    m._is_fake_message = True
    # ЖЕСТКО: Сохраняем оригинальный chat_id для правильного определения is_private_chat
    m._original_chat_id = original_chat_id if original_chat_id is not None else user_id
    # ЖЕСТКО: Сохраняем message_thread_id для правильной работы с топиками в группах
    m.message_thread_id = message_thread_id
    # ЖЕСТКО: Сохраняем оригинальное сообщение для реплаев
    m._original_message = original_message
    if command is not None:
        m.command = command
    else:
        # Emulate pyrogram's Message.command behavior when text starts with '/'
        try:
            if isinstance(text, str) and text.startswith('/'):
                parts = text.strip().split()
                if parts:
                    cmd = parts[0][1:] if len(parts[0]) > 1 else ''
                    args = parts[1:]
                    m.command = [cmd] + args
        except Exception:
            pass
    return m

def fake_message_with_context(text, user_id, context_message=None, command=None):
    """
    Создает fake_message с автоматическим извлечением message_thread_id из контекста.
    
    Args:
        text: Текст сообщения
        user_id: ID пользователя
        context_message: Сообщение для извлечения контекста (message_thread_id, chat_id)
        command: Команда (опционально)
    
    Returns:
        fake_message с правильным message_thread_id
    """
    if context_message:
        original_chat_id = getattr(getattr(context_message, 'chat', None), 'id', user_id)
        message_thread_id = getattr(context_message, 'message_thread_id', None)
        return fake_message(text, user_id, command=command, original_chat_id=original_chat_id, 
                          message_thread_id=message_thread_id, original_message=context_message)
    else:
        return fake_message(text, user_id, command=command)

def _handle_flood_wait(error_obj, user_id, retry_delay=5):
    """Extract flood wait seconds, sleep, and return True if we should retry."""
    err_str = str(error_obj)
    wait_match = re.search(r'A wait of (\d+) seconds is required', err_str)
    _messages = safe_get_messages(user_id)
    if wait_match:
        wait_seconds = int(wait_match.group(1))
        logger.warning(_messages.HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG.format(wait_seconds=wait_seconds))
        time.sleep(min(wait_seconds + 1, 30))
    else:
        logger.warning(_messages.HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG.format(retry_delay=retry_delay))
        time.sleep(retry_delay)


def _should_retry(error, user_id, retry_delay=5):
    """Check if an error is retryable (flood/seqno/random_id) and handle delay. Returns True if retryable."""
    err_str = str(error)
    _messages = safe_get_messages(user_id)
    if "FLOOD_WAIT" in err_str:
        _handle_flood_wait(error, user_id, retry_delay)
        return True
    if "msg_seqno is too high" in err_str:
        logger.warning(_messages.HELPER_MSG_SEQNO_ERROR_DETECTED_MSG.format(retry_delay=retry_delay))
        time.sleep(retry_delay)
        return True
    if "RANDOM_ID_DUPLICATE" in err_str:
        logger.warning("RANDOM_ID_DUPLICATE detected, backing off briefly and retrying")
        time.sleep(0.5)
        return True
    return False


def _write_flood_wait_file(chat_id, value):
    """Persist FloodWait seconds to user's flood_wait.txt file."""
    try:
        user_dir = os.path.join("users", str(chat_id))
        os.makedirs(user_dir, exist_ok=True)
        with open(os.path.join(user_dir, "flood_wait.txt"), 'w') as f:
            f.write(str(value))
    except Exception:
        pass


# Helper function for safe message sending with flood wait handling
def safe_send_message(chat_id, text, **kwargs):
    _messages = safe_get_messages(None)
    user_id = chat_id
    # Normalize reply parameters and preserve topic/thread info
    original_message = kwargs.get('message')
    # Peek callback_query (will be popped later) to inherit thread context in topics
    cb_peek = kwargs.get('_callback_query', None)
    
    # DEBUG: Log all parameters
    logger.info(f"[SAFE_SEND_DEBUG] chat_id={chat_id}, text_length={len(text) if text else 0}")
    logger.info(f"[SAFE_SEND_DEBUG] original_message={original_message}")
    logger.info(f"[SAFE_SEND_DEBUG] original_message.message_thread_id={getattr(original_message, 'message_thread_id', None) if original_message else None}")
    logger.info(f"[SAFE_SEND_DEBUG] cb_peek={cb_peek}")
    logger.info(f"[SAFE_SEND_DEBUG] kwargs keys: {list(kwargs.keys())}")
    if 'reply_parameters' not in kwargs:
        if 'reply_to_message_id' in kwargs and kwargs['reply_to_message_id'] is not None:
            kwargs['reply_parameters'] = ReplyParameters(message_id=kwargs['reply_to_message_id'])
            del kwargs['reply_to_message_id']
        elif original_message is not None and getattr(original_message, 'id', None) is not None:
            # Check if this is a fake message with original message reference
            if hasattr(original_message, '_is_fake_message') and hasattr(original_message, '_original_message'):
                if original_message._original_message is not None and getattr(original_message._original_message, 'id', None) is not None:
                    logger.info(f"[SAFE_SEND] Using original message for reply: {original_message._original_message.id}")
                    kwargs['reply_parameters'] = ReplyParameters(message_id=original_message._original_message.id)
                else:
                    logger.info(f"[SAFE_SEND] Fake message but no original message available, using fake message id: {original_message.id}")
                    kwargs['reply_parameters'] = ReplyParameters(message_id=original_message.id)
            else:
                kwargs['reply_parameters'] = ReplyParameters(message_id=original_message.id)
        elif cb_peek is not None and getattr(getattr(cb_peek, 'message', None), 'id', None) is not None:
            kwargs['reply_parameters'] = ReplyParameters(message_id=cb_peek.message.id)
    # Ensure topic/thread routing for supergroups with topics (only for groups, not private chats)
    try:
        # Only apply topic routing for groups (negative chat_id)
        if chat_id and chat_id < 0:
            # Check if message is provided in kwargs (for fake messages)
            if original_message is not None:
                # For fake messages, use the original message's thread_id
                if hasattr(original_message, '_is_fake_message') and hasattr(original_message, '_original_message') and original_message._original_message is not None:
                    message_thread_id = getattr(original_message._original_message, 'message_thread_id', None)
                    logger.info(f"[SAFE_SEND] fake_message._original_message.message_thread_id={message_thread_id}, chat_id={chat_id}")
                else:
                    message_thread_id = getattr(original_message, 'message_thread_id', None)
                    logger.info(f"[SAFE_SEND] original_message.message_thread_id={message_thread_id}, chat_id={chat_id}")
                
                if message_thread_id:
                    kwargs.setdefault('message_thread_id', message_thread_id)
                    logger.info(f"[SAFE_SEND] Set message_thread_id={message_thread_id} for chat_id={chat_id}")
            # Inherit thread_id from callback context when message is not provided
            elif cb_peek is not None and getattr(getattr(cb_peek, 'message', None), 'message_thread_id', None):
                kwargs.setdefault('message_thread_id', cb_peek.message.message_thread_id)
        else:
            logger.info(f"[SAFE_SEND] Skipping topic routing for private chat_id={chat_id}")
    except Exception as e:
        logger.warning(f"[SAFE_SEND] Error in topic routing: {e}")
        pass
    # Remove helper-only key
    if 'message' in kwargs:
        del kwargs['message']
    
    # DEBUG: Log final parameters before sending
    logger.info(f"[SAFE_SEND_FINAL] chat_id={chat_id}, message_thread_id={kwargs.get('message_thread_id', 'NOT_SET')}")
    logger.info(f"[SAFE_SEND_FINAL] Final kwargs: {kwargs}")
    
    max_retries = 3
    retry_delay = 5
    # Extract internal helper kwargs (not supported by pyrogram)
    cb = kwargs.pop('_callback_query', None)
    notice = kwargs.pop('_fallback_notice', None)
    # Drop any other underscored keys just in case
    for k in list(kwargs.keys()):
        if isinstance(k, str) and k.startswith('_'):
            kwargs.pop(k, None)

    # Auto-attach ReplyKeyboard for private chats (if user has keyboard enabled)
    if 'reply_markup' not in kwargs:
        try:
            from HELPERS.decorators import get_reply_keyboard_if_needed
            kb = get_reply_keyboard_if_needed(chat_id)
            if kb is not None:
                kwargs['reply_markup'] = kb
        except Exception:
            pass

    # Throttle message sending per-chat to prevent msg_seqno issues
    # Per-chat lock: different users don't block each other
    with _message_send_locks_lock:
        if chat_id not in _message_send_locks:
            _message_send_locks[chat_id] = threading.Lock()
        chat_lock = _message_send_locks[chat_id]

    with chat_lock:
        last_sent = _last_message_sent.get(chat_id, 0)
        now = time.time()
        # Increase minimum spacing to reduce RANDOM_ID_DUPLICATE in high-throughput chats
        min_spacing = 0.25  # seconds
        if now - last_sent < min_spacing:
            time.sleep(min_spacing - (now - last_sent))
        _last_message_sent[chat_id] = time.time()

        # Periodic cleanup: remove stale entries (older than 10 minutes)
        global _last_msg_ts_cleanup
        if now - _last_msg_ts_cleanup > _MSG_TS_CLEANUP_INTERVAL:
            _last_msg_ts_cleanup = now
            cutoff = now - 600
            # Clean stale timestamps
            stale = [cid for cid, ts in _last_message_sent.items() if ts < cutoff]
            for cid in stale:
                del _last_message_sent[cid]
                _message_send_locks.pop(cid, None)

    for attempt in range(max_retries):
        try:
            app = get_app_safe()
            return run_pyrogram_client_coroutine(app, app.send_message(chat_id, text, **kwargs))
        except FloodWait as e:
            if e.value <= 60 and attempt < max_retries - 1:
                logger.warning(f"FloodWait ({e.value}s) while sending to {chat_id}, retrying ({attempt+1}/{max_retries})")
                time.sleep(e.value + 1)
                continue
            _write_flood_wait_file(chat_id, e.value)
            logger.warning(f"Flood wait detected ({e.value}s) while sending message to {chat_id}")
            try:
                if cb is not None:
                    cb.answer(notice or safe_get_messages(user_id).HELPER_FLOOD_LIMIT_TRY_LATER_MSG, show_alert=False)
            except Exception:
                pass
            return None
        except Exception as e:
            if _should_retry(e, user_id, retry_delay) and attempt < max_retries - 1:
                continue
            logger.error(f"Failed to send message after {max_retries} attempts: {e}")
            return None

# Helper function for safe message forwarding with flood wait handling
def safe_forward_messages(chat_id, from_chat_id, message_ids, **kwargs):
    _messages = safe_get_messages(None)
    user_id = chat_id
    max_retries = 3
    retry_delay = 5

    for attempt in range(max_retries):
        try:
            app = get_app_safe()
            return run_pyrogram_client_coroutine(app, app.forward_messages(chat_id, from_chat_id, message_ids, **kwargs))
        except Exception as e:
            if _should_retry(e, user_id, retry_delay) and attempt < max_retries - 1:
                continue
            logger.error(f"Failed to forward messages after {max_retries} attempts: {e}")
            return None

# Helper function for safely editing message text with flood wait handling
def safe_edit_message_text(chat_id, message_id, text, **kwargs):
    _messages = safe_get_messages(None)
    user_id = chat_id
    max_retries = 3

    # Throttle edits in groups to no more than once per 5 seconds per chat
    try:
        is_group = isinstance(chat_id, int) and chat_id < 0
    except Exception:
        is_group = False

    if is_group:
        now = time.time()
        last_ts = _last_edit_ts_per_chat.get(chat_id, 0.0)
        elapsed = now - last_ts
        if 0 < elapsed < 5.0:
            try:
                time.sleep(5.0 - elapsed)
            except Exception:
                pass
        _last_edit_ts_per_chat[chat_id] = time.time()

        # Periodic cleanup
        global _last_edit_cleanup_ts
        if now - _last_edit_cleanup_ts > 300:
            _last_edit_cleanup_ts = now
            cutoff = now - 600
            stale = [cid for cid, ts in _last_edit_ts_per_chat.items() if ts < cutoff]
            for cid in stale:
                del _last_edit_ts_per_chat[cid]

    for attempt in range(max_retries):
        try:
            app = get_app_safe()
            return run_pyrogram_client_coroutine(app, app.edit_message_text(chat_id, message_id, text, **kwargs))
        except FloodWait as e:
            if e.value <= 60 and attempt < max_retries - 1:
                logger.warning(f"FloodWait ({e.value}s) while editing message for {chat_id}, retrying ({attempt+1}/{max_retries})")
                time.sleep(e.value + 1)
                continue
            _write_flood_wait_file(chat_id, e.value)
            logger.warning(f"Flood wait detected ({e.value}s) while editing message for {chat_id}")
            return None
        except Exception as e:
            if _messages.HELPER_MESSAGE_ID_INVALID_MSG in str(e):
                if attempt == 0:
                    logger.debug(f"Tried to edit message that was already deleted: {message_id}")
                return None

# Helper function for safely clearing reply markup (inline keyboard)
def safe_edit_reply_markup(chat_id, message_id, reply_markup=None, **kwargs):
    _messages = safe_get_messages(None)
    user_id = chat_id
    max_retries = 3
    retry_delay = 5

    # Inherit thread context from helpers
    original_message = kwargs.get('message')
    cb_peek = kwargs.get('_callback_query', None)
    try:
        if 'message_thread_id' not in kwargs:
            if original_message and getattr(original_message, 'message_thread_id', None):
                kwargs['message_thread_id'] = original_message.message_thread_id
            elif cb_peek and getattr(getattr(cb_peek, 'message', None), 'message_thread_id', None):
                kwargs['message_thread_id'] = cb_peek.message.message_thread_id
    except Exception:
        pass
    kwargs.pop('message', None)
    kwargs.pop('_callback_query', None)

    for attempt in range(max_retries):
        try:
            app = get_app_safe()
            return run_pyrogram_client_coroutine(app, app.edit_message_reply_markup(chat_id, message_id, reply_markup=reply_markup, **kwargs))
        except FloodWait as e:
            _write_flood_wait_file(chat_id, e.value)
            logger.warning(f"Flood wait detected ({e.value}s) while editing reply markup for {chat_id}")
            return None
        except Exception as e:
            if _should_retry(e, user_id, retry_delay) and attempt < max_retries - 1:
                continue
            if attempt == max_retries - 1:
                logger.error(f"Failed to edit reply markup after {max_retries} attempts: {e}")
            return None

# Helper function for safely deleting messages with flood wait handling
def safe_delete_messages(chat_id, message_ids, **kwargs):
    _messages = safe_get_messages(None)
    user_id = chat_id
    max_retries = 3
    retry_delay = 5

    for attempt in range(max_retries):
        try:
            app = get_app_safe()
            return run_pyrogram_client_coroutine(app, app.delete_messages(chat_id=chat_id, message_ids=message_ids, **kwargs))
        except Exception as e:
            err_str = str(e)
            if _messages.HELPER_MESSAGE_ID_INVALID_MSG in err_str or _messages.HELPER_MESSAGE_DELETE_FORBIDDEN_MSG in err_str:
                if attempt == 0:
                    logger.debug(f"Tried to delete non-existent message(s): {message_ids}")
                return None
            if _should_retry(e, user_id, retry_delay) and attempt < max_retries - 1:
                continue
            logger.error(f"Failed to delete messages after {max_retries} attempts: {type(e).__name__}")
            return None

# Helper function for sending messages with auto-delete functionality
def safe_send_message_with_auto_delete(chat_id, text, delete_after_seconds=60, **kwargs):
    """
    Send a message and automatically delete it after specified seconds
    
    Args:
        chat_id: The chat ID to send to
        text: The message text
        delete_after_seconds: Seconds after which to delete the message (default: 60)
        **kwargs: Additional arguments for send_message
    
    Returns:
        The message object or None if sending failed
    """
    # Send the message first
    message = safe_send_message(chat_id, text, **kwargs)
    
    if message and hasattr(message, 'id'):
        # Schedule deletion in a separate thread with better error handling
        def delete_message_after_delay():
            try:
                logger.info(f"[AUTO-DELETE] Scheduling message {message.id} for deletion in {delete_after_seconds} seconds")
                time.sleep(delete_after_seconds)
                logger.info(f"[AUTO-DELETE] Attempting to delete message {message.id}")
                result = safe_delete_messages(chat_id, [message.id])
                if result:
                    logger.info(f"[AUTO-DELETE] Successfully deleted message {message.id}")
                else:
                    logger.warning(f"[AUTO-DELETE] Failed to delete message {message.id}")
            except Exception as e:
                logger.error(f"[AUTO-DELETE] Error in auto-delete thread for message {message.id}: {e}")
        
        # Start the deletion thread
        delete_thread = threading.Thread(target=delete_message_after_delay, daemon=True)
        delete_thread.start()
        logger.info(f"[AUTO-DELETE] Started auto-delete thread for message {message.id} (thread: {delete_thread.name})")
    else:
        logger.warning(f"[AUTO-DELETE] Failed to send message or message has no ID: {message}")
    
    return message

def schedule_delete_message(chat_id, message_id, delete_after_seconds=60):
    """
    Schedule deletion of an already-sent message after a delay.

    Args:
        chat_id: The chat ID
        message_id: The message ID to delete
        delete_after_seconds: Seconds to wait before deleting
    Returns:
        True if scheduled, False otherwise
    """
    try:
        if not chat_id or not message_id:
            return False

        def _del():
            try:
                logger.info(f"[AUTO-DELETE] Scheduling message {message_id} for deletion in {delete_after_seconds} seconds")
                time.sleep(delete_after_seconds)
                safe_delete_messages(chat_id, [message_id])
            except Exception as e:
                logger.error(f"[AUTO-DELETE] Error while deleting message {message_id}: {e}")

        t = threading.Thread(target=_del, daemon=True)
        t.start()
        return True
    except Exception:
        return False

def schedule_delete_processing_messages(chat_id, delete_after_seconds=5):
    """
    Schedule deletion of all "Processing..." messages for a user after a delay.
    """
    try:
        if not chat_id:
            return False

        def _del_processing_messages():
            try:
                logger.info(f"[AUTO-DELETE] Scheduling deletion of all processing messages for user {chat_id} in {delete_after_seconds} seconds")
                time.sleep(delete_after_seconds)
                
                # Get app instance
                app = get_app_safe()
                if not app:
                    logger.error("[AUTO-DELETE] Cannot get app instance for deleting processing messages")
                    return
                
                # Bots cannot use get_chat_history, so we'll skip this functionality
                # Instead, we'll rely on the individual message deletion that's already scheduled
                logger.info(f"[AUTO-DELETE] Skipping chat history scan for user {chat_id} (bots cannot use get_chat_history)")
                logger.info(f"[AUTO-DELETE] Individual processing messages will be deleted by their own timers")
                    
            except Exception as e:
                logger.error(f"[AUTO-DELETE] Error while deleting processing messages for user {chat_id}: {e}")

        t = threading.Thread(target=_del_processing_messages, daemon=True)
        t.start()
        return True
    except Exception:
        return False
