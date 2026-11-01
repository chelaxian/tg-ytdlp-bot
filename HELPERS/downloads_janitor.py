"""Age-based cleanup of task temp dirs, in the BOT process (#460, #385).

Only users/<uid>/downloads/<task>/ directories are eligible (default 48h
since the newest mtime anywhere inside). Never delete user settings or files
in the user root. Active user counts and A2's download-dir refcounts are
locked through the sweep so starting a new task cannot race with deletion.
Existing do_not_delete_me markers are respected regardless of age.
"""
import logging
import os
import shutil
import threading
import time

logger = logging.getLogger(__name__)
_DEFAULT_MAX_AGE_HOURS = 48
_DEFAULT_INTERVAL_SECONDS = 3600
_FIRST_RUN_DELAY_SECONDS = 600
_janitor_started = False
_janitor_lock = threading.Lock()


def _newest_mtime(path):
    newest = os.lstat(path).st_mtime
    for root, dirs, files in os.walk(path, followlinks=False):
        # Do not follow symlink dirs, even when computing the cutoff.
        dirs[:] = [name for name in dirs if not os.path.islink(os.path.join(root, name))]
        for name in dirs + files:
            try:
                newest = max(newest, os.lstat(os.path.join(root, name)).st_mtime)
            except FileNotFoundError:
                continue
    return newest


def _is_inside(base, path):
    base = os.path.normcase(os.path.realpath(base))
    path = os.path.normcase(os.path.realpath(path))
    return os.path.commonpath([base, path]) == base and path != base


def _overlaps_active(path, active_paths):
    path = os.path.normcase(os.path.abspath(path))
    for active in active_paths:
        active = os.path.normcase(os.path.abspath(active))
        if (active == path or active.startswith(path + os.sep)
                or path.startswith(active + os.sep)):
            return True
    return False


def purge_stale_downloads(users_dir, max_age_seconds, active_user_ids, active_paths=(), now=None):
    """Remove only stale task directories, returning the number removed.

    Caller MUST hold both bot active-task registry locks until this returns.
    Explicit activity arguments avoid accidentally assuming an empty registry
    from a dashboard/other process means no downloads are running.
    """
    if max_age_seconds <= 0:
        return 0
    now = time.time() if now is None else now
    active = {str(uid) for uid in active_user_ids}
    removed = 0
    if os.path.islink(users_dir) or not os.path.isdir(users_dir):
        return 0
    for uid in os.listdir(users_dir):
        user_path = os.path.join(users_dir, uid)
        if uid in active or os.path.islink(user_path) or not os.path.isdir(user_path):
            continue
        base = os.path.join(user_path, 'downloads')
        if os.path.islink(base) or not os.path.isdir(base):
            continue
        for name in os.listdir(base):
            path = os.path.join(base, name)
            try:
                if (os.path.islink(path) or not os.path.isdir(path)
                        or not _is_inside(base, path) or _overlaps_active(path, active_paths)):
                    continue
                # A marker anywhere below the task protects its entire subtree.
                protected = any('do_not_delete_me' in files
                                for _, _, files in os.walk(path, followlinks=False))
                if protected or now - _newest_mtime(path) < max_age_seconds:
                    continue
                shutil.rmtree(path)
                removed += 1
            except FileNotFoundError:
                continue
            except (OSError, ValueError) as e:
                logger.warning(f'[janitor] Could not remove stale download {path}: {e}')
    return removed


def run_janitor_once(users_dir='users', max_age_seconds=None):
    """Run in bot process only. Fail closed if activity registries are absent."""
    from HELPERS.download_status import active_downloads, active_downloads_lock
    from HELPERS.filesystem_hlp import _ACTIVE_DOWNLOAD_DIRS, _ACTIVE_DOWNLOAD_DIRS_LOCK
    if max_age_seconds is None:
        max_age_seconds = _DEFAULT_MAX_AGE_HOURS * 3600
    # Same locks used when tasks register themselves; do not release between
    # snapshot/check and rmtree. Directory registration cannot race the purge.
    with active_downloads_lock, _ACTIVE_DOWNLOAD_DIRS_LOCK:
        active = {str(uid) for uid, count in active_downloads.items() if count}
        paths = tuple(_ACTIVE_DOWNLOAD_DIRS)
        removed = purge_stale_downloads(users_dir, max_age_seconds, active, paths)
    if removed:
        logger.info(f'[janitor] Removed {removed} stale download temp dir(s); active downloads protected')
    return removed


def _janitor_loop(users_dir, max_age_seconds, interval):
    time.sleep(_FIRST_RUN_DELAY_SECONDS)
    while True:
        try:
            run_janitor_once(users_dir, max_age_seconds)
        except (OSError, ValueError, ImportError) as e:
            logger.error(f'[janitor] Pass failed safely: {type(e).__name__}: {e}')
        time.sleep(interval)


def start_downloads_janitor():
    """Start once after app.start() in magic.py. No network operations."""
    global _janitor_started
    from CONFIG.config import Config
    with _janitor_lock:
        if _janitor_started:
            return
        max_age_hours = float(getattr(Config, 'DOWNLOADS_MAX_AGE_HOURS', _DEFAULT_MAX_AGE_HOURS))
        if max_age_hours <= 0:
            logger.info('[janitor] Disabled (DOWNLOADS_MAX_AGE_HOURS <= 0)')
            return
        interval = max(60, int(getattr(Config, 'DOWNLOADS_JANITOR_INTERVAL_SECONDS', _DEFAULT_INTERVAL_SECONDS)))
        users_dir = getattr(Config, 'USERS_DIR', 'users')
        thread = threading.Thread(target=_janitor_loop,
                                  args=(users_dir, max_age_hours * 3600, interval),
                                  daemon=True, name='downloads_janitor')
        thread.start()
        _janitor_started = True
        logger.info(f'[janitor] Started: temp dirs older than {max_age_hours:g}h, interval {interval}s')
