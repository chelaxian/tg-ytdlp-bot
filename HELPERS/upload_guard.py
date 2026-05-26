import threading
import concurrent.futures
from CONFIG.limits import LimitsConfig
from HELPERS.logger import logger

_SERVER_RES = LimitsConfig.detect_system_resources()
_MAX_CONCURRENT_UPLOADS = _SERVER_RES['max_uploads']
_UPLOAD_SEMAPHORE = threading.Semaphore(_MAX_CONCURRENT_UPLOADS)
_UPLOAD_EXECUTOR = concurrent.futures.ThreadPoolExecutor(
    max_workers=_MAX_CONCURRENT_UPLOADS + 2,
    thread_name_prefix="tg_upload"
)

def timed_upload(upload_fn, timeout=None):
    """Run an upload with timeout and concurrency control.

    Prevents a single stuck upload from blocking all bot operations.
    Uploads run in a dedicated thread pool with a hard timeout.
    If timeout fires, the calling thread is freed while the upload
    continues in background (Python threads cannot be killed).
    """
    if timeout is None:
        timeout = LimitsConfig.UPLOAD_TIMEOUT_SECONDS

    acquired = _UPLOAD_SEMAPHORE.acquire(blocking=False)
    if not acquired:
        logger.warning(f"[Upload] All {_MAX_CONCURRENT_UPLOADS} upload slots busy, rejecting")
        raise TimeoutError(
            f"All {_MAX_CONCURRENT_UPLOADS} upload slots are busy. "
            f"Please try again in a few minutes."
        )

    try:
        future = _UPLOAD_EXECUTOR.submit(upload_fn)
        return future.result(timeout=timeout)
    except concurrent.futures.TimeoutError:
        logger.error(f"[Upload] Timed out after {timeout}s, releasing slot (background thread may still run)")
        raise TimeoutError(f"Upload timed out after {timeout}s")
    finally:
        _UPLOAD_SEMAPHORE.release()
