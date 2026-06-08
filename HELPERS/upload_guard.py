import threading
import concurrent.futures
import time
from CONFIG.limits import LimitsConfig
from HELPERS.logger import logger


class UploadAlreadyInProgressError(TimeoutError):
    pass


class UploadSlotsBusyError(TimeoutError):
    pass


_SERVER_RES = LimitsConfig.detect_system_resources()
_MAX_CONCURRENT_UPLOADS = min(_SERVER_RES['max_uploads'], 4)
_UPLOAD_SEMAPHORE = threading.Semaphore(_MAX_CONCURRENT_UPLOADS)
_UPLOAD_EXECUTOR = concurrent.futures.ThreadPoolExecutor(
    max_workers=_MAX_CONCURRENT_UPLOADS * 4,
    thread_name_prefix="tg_upload"
)

_ACTIVE_UPLOAD_KEYS = set()
_ACTIVE_UPLOAD_LOCK = threading.Lock()

_ZOMBIE_FUTURES = []
_ZOMBIE_FUTURES_LOCK = threading.Lock()


def _zombie_reaper():
    while True:
        time.sleep(30)
        try:
            with _ZOMBIE_FUTURES_LOCK:
                still_alive = []
                for entry in _ZOMBIE_FUTURES:
                    f = entry['future']
                    if f.done():
                        dk = entry.get('dedup_key')
                        if dk is not None:
                            with _ACTIVE_UPLOAD_LOCK:
                                _ACTIVE_UPLOAD_KEYS.discard(dk)
                        logger.info(f"[Upload] Zombie thread finished, cleaned up key={dk}")
                    else:
                        still_alive.append(entry)
                _ZOMBIE_FUTURES.clear()
                _ZOMBIE_FUTURES.extend(still_alive)
                if still_alive:
                    logger.warning(f"[Upload] Zombie threads still running: {len(still_alive)}")
        except Exception as e:
            logger.error(f"[Upload] Zombie reaper error: {e}")


_reaper_thread = threading.Thread(target=_zombie_reaper, daemon=True, name="tg_upload_reaper")
_reaper_thread.start()


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
                })
        raise TimeoutError(f"Upload timed out after {timeout}s")
    except Exception:
        raise
    finally:
        _UPLOAD_SEMAPHORE.release()
        if future is not None and future.done() and dedup_key is not None:
            with _ACTIVE_UPLOAD_LOCK:
                _ACTIVE_UPLOAD_KEYS.discard(dedup_key)
