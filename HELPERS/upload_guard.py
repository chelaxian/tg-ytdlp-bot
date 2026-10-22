import os
import threading
import concurrent.futures
import time
import atexit
from CONFIG.limits import LimitsConfig
from HELPERS.logger import logger


class UploadAlreadyInProgressError(TimeoutError):
    pass


class UploadSlotsBusyError(TimeoutError):
    pass


_SERVER_RES = LimitsConfig.detect_system_resources()
LimitsConfig._resolve_dynamic_limits()
_MAX_CONCURRENT_UPLOADS = _SERVER_RES['max_uploads']
_UPLOAD_SEMAPHORE = threading.Semaphore(_MAX_CONCURRENT_UPLOADS)
_UPLOAD_EXECUTOR = concurrent.futures.ThreadPoolExecutor(
    max_workers=_MAX_CONCURRENT_UPLOADS * 4,
    thread_name_prefix="tg_upload"
)

_ACTIVE_UPLOAD_KEYS = set()
_ACTIVE_UPLOAD_LOCK = threading.Lock()

_ZOMBIE_FUTURES = []
_ZOMBIE_FUTURES_LOCK = threading.Lock()


# How long an upload waits for the Pyrogram client to become connected
# (startup race) before giving up with a clear error.
_APP_READY_WAIT_SECONDS = 30


class ClientNotReadyError(ConnectionError):
    """Pyrogram client is not connected (still starting or shutting down)."""


def _ensure_app_started():
    """Make sure the Pyrogram client is connected before an upload runs.

    'Client has not been started yet' is raised by Pyrogram whenever the client
    is not connected. The previous fix (60129f6) called app.start() from the
    upload worker thread - unsafe when the client is being stopped by a
    SIGTERM (service restart), because it raced with app.stop() in the main
    thread. Now we never start/restart the client from a worker (issue #326):
    * shutdown in progress -> fail fast with ClientNotReadyError;
    * startup race -> wait up to _APP_READY_WAIT_SECONDS for the main thread.
    """
    from HELPERS.app_instance import get_app, is_app_stopping
    app = get_app()
    if app is None:
        return
    if is_app_stopping():
        raise ClientNotReadyError("Bot is shutting down, upload cancelled")

    def _connected():
        connected = getattr(app, 'is_connected', None)
        if connected is None:
            connected = getattr(app, 'is_started', True)
        return bool(connected)

    if _connected():
        return
    logger.warning(
        f"[Upload] Pyrogram client is not connected, waiting up to {_APP_READY_WAIT_SECONDS}s"
    )
    deadline = time.monotonic() + _APP_READY_WAIT_SECONDS
    while time.monotonic() < deadline:
        if is_app_stopping():
            raise ClientNotReadyError("Bot is shutting down, upload cancelled")
        time.sleep(0.5)
        if _connected():
            logger.info("[Upload] Pyrogram client connected, continuing upload")
            return
    raise ClientNotReadyError(
        f"Pyrogram client not connected after {_APP_READY_WAIT_SECONDS}s"
    )


# Upload timeout scaling (issue #372): a fixed 1200s budget means a 2 GB
# file needs >1.7 MB/s sustained - not achievable over the degraded WG tunnel
# on DE. Big files get time proportional to their size, bounded by a cap.
_UPLOAD_MIN_RATE_BPS = getattr(LimitsConfig, 'UPLOAD_MIN_RATE_BYTES_PER_SEC', 512 * 1024)
_UPLOAD_TIMEOUT_GRACE = 120


def _upload_timeout_cap(base_timeout):
    return getattr(LimitsConfig, 'UPLOAD_TIMEOUT_MAX_SECONDS', base_timeout * 4)


def _infer_file_size(file_path, dedup_key):
    """Size of the uploaded file: explicit file_path, or the path carried in a
    (user_id, abs_path) dedup_key as used by DOWN_AND_UP/sender.py."""
    candidates = []
    if file_path:
        candidates.append(file_path)
    if isinstance(dedup_key, tuple):
        candidates.extend(x for x in dedup_key if isinstance(x, str))
    for path in candidates:
        try:
            return os.path.getsize(path)
        except OSError:
            continue
    return None


def compute_upload_timeout(file_size, base_timeout=None):
    """Timeout for uploading file_size bytes: never below the base timeout,
    scaled at _UPLOAD_MIN_RATE_BPS for large files, capped."""
    if base_timeout is None:
        base_timeout = LimitsConfig.UPLOAD_TIMEOUT_SECONDS
    if not file_size or file_size <= 0:
        return base_timeout
    scaled = int(file_size / _UPLOAD_MIN_RATE_BPS) + _UPLOAD_TIMEOUT_GRACE
    return max(base_timeout, min(scaled, _upload_timeout_cap(base_timeout)))


def _log_late_completion(future, dedup_key, timeout):
    """Report what a timed-out upload eventually did. The caller has already
    received TimeoutError and moved on, so the result is only logged
    (issue #372: make the 'background thread may still run' outcome visible)."""
    if future.cancelled():
        logger.info(f"[Upload] Timed-out upload was cancelled before start (key={dedup_key})")
        return
    exc = future.exception()
    if exc is not None:
        logger.warning(
            f"[Upload] Timed-out upload (>{timeout}s) finished later with error, key={dedup_key}: "
            f"{type(exc).__name__}: {exc}"
        )
    else:
        logger.warning(
            f"[Upload] Timed-out upload (>{timeout}s) completed late, key={dedup_key}; "
            f"result ignored (the message may still have been delivered)"
        )


def _zombie_reaper():
    while True:
        time.sleep(30)
        try:
            now = time.time()
            with _ZOMBIE_FUTURES_LOCK:
                still_alive = []
                for entry in _ZOMBIE_FUTURES:
                    f = entry['future']
                    dk = entry.get('dedup_key')
                    if f.done():
                        if dk is not None:
                            with _ACTIVE_UPLOAD_LOCK:
                                _ACTIVE_UPLOAD_KEYS.discard(dk)
                        logger.info(f"[Upload] Zombie thread finished, cleaned up key={dk}")
                    else:
                        # Do not expire a live upload's key: the message could
                        # still be delivered, so retries must stay blocked (#372).
                        still_alive.append(entry)
                _ZOMBIE_FUTURES.clear()
                _ZOMBIE_FUTURES.extend(still_alive)
                if still_alive:
                    details = [
                        f"key={e.get('dedup_key')} alive={int(now - e.get('started', now))}s"
                        for e in still_alive
                    ]
                    logger.warning(f"[Upload] Zombie threads still running: {len(still_alive)} | {details}")
        except Exception as e:
            logger.error(f"[Upload] Zombie reaper error: {e}")


_reaper_thread = threading.Thread(target=_zombie_reaper, daemon=True, name="tg_upload_reaper")
_reaper_thread.start()


def _dump_zombies_on_shutdown():
    """Log and clean up orphan upload threads on process exit (issue #314)."""
    try:
        with _ZOMBIE_FUTURES_LOCK:
            live = sum(not entry['future'].done() for entry in _ZOMBIE_FUTURES)
            if live:
                logger.error(f"[Upload] Process exiting with {live} orphan upload threads")
        _UPLOAD_EXECUTOR.shutdown(wait=False, cancel_futures=True)
    except Exception as e:
        logger.debug(f"[Upload] shutdown cleanup error: {e}")


atexit.register(_dump_zombies_on_shutdown)


def timed_upload(upload_fn, timeout=None, dedup_key=None, file_path=None):
    """Run an upload with timeout and concurrency control.

    Prevents a single stuck upload from blocking all bot operations.
    Uploads run in a dedicated thread pool with a hard timeout.
    If timeout fires, the calling thread is freed while the upload
    continues in background (Python threads cannot be killed).

    The dedup_key is kept alive until the background thread finishes,
    preventing duplicate uploads of the same file.

    Args:
        dedup_key: Optional hashable key to prevent duplicate uploads.
                   If another upload with the same key timed out but its
                   background thread is still running, this call will
                   immediately raise TimeoutError without starting a new upload.
        file_path: Optional path of the uploaded file. Its size (or the size of
                   the path inside a (user_id, path) dedup_key) scales the
                   timeout for big files (issue #372).
    """
    base_timeout = LimitsConfig.UPLOAD_TIMEOUT_SECONDS if timeout is None else timeout
    timeout = compute_upload_timeout(_infer_file_size(file_path, dedup_key), base_timeout)
    if timeout > base_timeout:
        logger.info(f"[Upload] Upload timeout scaled to {timeout}s for file size (base {base_timeout}s)")

    if dedup_key is not None:
        with _ACTIVE_UPLOAD_LOCK:
            if dedup_key in _ACTIVE_UPLOAD_KEYS:
                logger.warning(f"[Upload] Duplicate upload blocked for key={dedup_key}, previous upload still in progress")
                raise UploadAlreadyInProgressError(
                    f"Upload already in progress for this file. "
                    f"Please wait for the current upload to complete."
                )
            _ACTIVE_UPLOAD_KEYS.add(dedup_key)

    _queue_wait_timeout = timeout + 300
    acquired = _UPLOAD_SEMAPHORE.acquire(blocking=True, timeout=_queue_wait_timeout)
    if not acquired:
        if dedup_key is not None:
            with _ACTIVE_UPLOAD_LOCK:
                _ACTIVE_UPLOAD_KEYS.discard(dedup_key)
        logger.warning(f"[Upload] Queue wait timed out after {_queue_wait_timeout}s")
        raise UploadSlotsBusyError(
            f"All {_MAX_CONCURRENT_UPLOADS} upload slots are busy. "
            f"Queue wait timed out."
        )

    future = None
    try:
        _ensure_app_started()
        future = _UPLOAD_EXECUTOR.submit(upload_fn)
        result = future.result(timeout=timeout)
        return result
    except concurrent.futures.TimeoutError:
        if future is not None and future.done():
            # The upload function itself raised TimeoutError, not our wait.
            return future.result()
        logger.error(f"[Upload] Timed out after {timeout}s, releasing slot (background thread may still run)")
        if future is not None:
            # Not-yet-started work is dropped; a running upload cannot be killed
            # (Python threads), so its late outcome is only logged.
            future.cancel()
            future.add_done_callback(lambda f: _log_late_completion(f, dedup_key, timeout))
            with _ZOMBIE_FUTURES_LOCK:
                _ZOMBIE_FUTURES.append({
                    'future': future,
                    'dedup_key': dedup_key,
                    'started': time.time(),
                })
        raise TimeoutError(f"Upload timed out after {timeout}s")
    finally:
        _UPLOAD_SEMAPHORE.release()
        # future is None when the upload never started (e.g. ClientNotReadyError):
        # release the dedup key too, otherwise the file stays blocked forever.
        if dedup_key is not None and (future is None or future.done()):
            with _ACTIVE_UPLOAD_LOCK:
                _ACTIVE_UPLOAD_KEYS.discard(dedup_key)
