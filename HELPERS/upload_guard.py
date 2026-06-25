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


def _ensure_app_started():
    """Make sure the Pyrogram client is started before an upload runs.

    Guards against the 'Client has not been started yet' race that occurs when
    requests are processed before the client finished starting (issue #326).
    """
    try:
        from HELPERS.app_instance import get_app
        app = get_app()
        if app is None:
            return
        # Pyrogram exposes is_started on Client; guard with getattr for safety
        if getattr(app, 'is_started', True) is False:
            logger.warning("[Upload] Pyrogram client not started, starting now")
            try:
                app.start()
            except Exception as e:
                # If start is rejected because it is starting concurrently,
                # log and let the caller's retry handle the failure.
                logger.warning(f"[Upload] Could not start Pyrogram client on-demand: {e}")
    except Exception as e:
        logger.debug(f"[Upload] _ensure_app_started check failed: {e}")


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
                        # Force-release stale dedup keys after TTL so a zombie upload
                        # no longer blocks the same file for the user (issue #314).
                        ttl = entry.get('ttl')
                        if dk is not None and ttl is not None and (now - entry.get('started', now)) > ttl:
                            with _ACTIVE_UPLOAD_LOCK:
                                _ACTIVE_UPLOAD_KEYS.discard(dk)
                            logger.warning(f"[Upload] Force-releasing stale dedup_key after TTL={ttl}s: {dk}")
                            entry['dedup_key'] = None
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
            if _ZOMBIE_FUTURES:
                logger.error(f"[Upload] Process exiting with {len(_ZOMBIE_FUTURES)} orphan upload threads")
        _UPLOAD_EXECUTOR.shutdown(wait=False, cancel_futures=True)
    except Exception as e:
        logger.debug(f"[Upload] shutdown cleanup error: {e}")


atexit.register(_dump_zombies_on_shutdown)


def timed_upload(upload_fn, timeout=None, dedup_key=None):
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
    """
    if timeout is None:
        timeout = LimitsConfig.UPLOAD_TIMEOUT_SECONDS

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
        logger.error(f"[Upload] Timed out after {timeout}s, releasing slot (background thread may still run)")
        if future is not None:
            with _ZOMBIE_FUTURES_LOCK:
                _ZOMBIE_FUTURES.append({
                    'future': future,
                    'dedup_key': dedup_key,
                    'started': time.time(),
                    # Release dedup key after 2x timeout so a stuck upload stops blocking the file
                    'ttl': timeout * 2,
                })
        raise TimeoutError(f"Upload timed out after {timeout}s")
    except Exception:
        raise
    finally:
        _UPLOAD_SEMAPHORE.release()
        if future is not None and future.done() and dedup_key is not None:
            with _ACTIVE_UPLOAD_LOCK:
                _ACTIVE_UPLOAD_KEYS.discard(dedup_key)
