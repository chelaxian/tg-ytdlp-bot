

import threading
import time
import os
import re
from CONFIG.config import Config
from CONFIG.limits import LimitsConfig
from CONFIG.messages import Messages, safe_get_messages
from HELPERS.app_instance import get_app
from HELPERS.logger import logger
from HELPERS.safe_messeger import safe_edit_message_text
from HELPERS.filesystem_hlp import create_directory, cleanup_user_temp_files

# Global dictionary to track active downloads and lock for thread-safe access
# Now stores download count (int) per user instead of bool
active_downloads = {}
active_downloads_lock = threading.Lock()

# Global dictionary to track playlist errors and lock for thread-safe access
playlist_errors = {}
playlist_errors_lock = threading.Lock()

# Add a global dictionary to track download start times
download_start_times = {}
download_start_times_lock = threading.Lock()

# Per-user download cancellation registry.
# Structure: {user_id: [threading.Event, ...]}
# Each active download for a user registers its own Event.
# When /clean is called, all events for that user are set → downloads check and abort.
_user_cancel_events = {}
_user_cancel_events_lock = threading.Lock()


def register_download_cancel_event(user_id):
    """
    Create and register a new threading.Event for a user's download.
    Returns the event so the download loop can check it.

    This is per-download: each download gets its own event.
    Other users are completely unaffected.
    """
    ev = threading.Event()
    with _user_cancel_events_lock:
        if user_id not in _user_cancel_events:
            _user_cancel_events[user_id] = []
        _user_cancel_events[user_id].append(ev)
    return ev


def unregister_download_cancel_event(user_id, ev):
    """
    Remove a specific event from the user's list after download finishes.
    """
    with _user_cancel_events_lock:
        if user_id in _user_cancel_events:
            try:
                _user_cancel_events[user_id].remove(ev)
            except ValueError:
                pass
            if not _user_cancel_events[user_id]:
                del _user_cancel_events[user_id]


def cancel_user_downloads(user_id):
    """
    Signal all active downloads for a specific user to stop.
    Sets all registered events for this user_id only.
    Returns the number of cancelled tasks.
    Other users are NEVER affected.
    """
    count = 0
    with _user_cancel_events_lock:
        events = _user_cancel_events.pop(user_id, [])
        for ev in events:
            ev.set()
            count += 1
    if count:
        logger.info(f"[CANCEL] Cancelled {count} active download(s) for user {user_id}")
    return count


# Get app instance for decorators
app = get_app()

def set_download_start_time(user_id):
    """
    Sets the download start time for a user
    """
    with download_start_times_lock:
        download_start_times[user_id] = time.time()


def clear_download_start_time(user_id):
    """
    Clears the download start time for a user
    """
    with download_start_times_lock:
        if user_id in download_start_times:
            del download_start_times[user_id]


def check_download_timeout(user_id):
    """
    Checks if the download timeout has been exceeded. For admins, timeout does not apply.
    """
    # If the user is an admin, timeout does not apply
    if hasattr(Config, 'ADMIN') and int(user_id) in Config.ADMIN:
        return False
    with download_start_times_lock:
        if user_id in download_start_times:
            start_time = download_start_times[user_id]
            current_time = time.time()
            if current_time - start_time > Config.DOWNLOAD_TIMEOUT:
                return True
    return False

# Helper function to safely get active download status
def _adaptive_interval(elapsed_seconds):
    """Calculate adaptive update interval based on elapsed time.
    
    0-4 min: 3s, 5-9: 4s, 10-14: 5s, ... 55-59: 14s, 60+: 90s.
    """
    minutes_passed = int(elapsed_seconds // 60)
    if minutes_passed >= 60:
        return 90.0
    return 3.0 + max(0, minutes_passed // 5)


def get_active_download(user_id):
    """
    Thread-safe function to get the active download count for a user

    Args:
        user_id: The user ID

    Returns:
        int: Number of active downloads for this user (0 if none)
    """
    with active_downloads_lock:
        return active_downloads.get(user_id, 0)


def can_start_download(user_id, is_playlist=False, is_multi_url=False):
    """
    Check if a new download can be started for this user.
    
    Rules:
    - Single URL: up to MAX_CONCURRENT_DOWNLOADS per user
    - Playlist: only 1 at a time
    - Multi-URL: only 1 at a time
    
    Returns:
        bool: True if download can start, False if limit reached
    """
    current_count = get_active_download(user_id)
    
    if is_playlist or is_multi_url:
        # Playlists and multi-URLs: only 1 at a time
        return current_count == 0
    
    # Single URLs: up to MAX_CONCURRENT_DOWNLOADS
    return current_count < LimitsConfig.MAX_CONCURRENT_DOWNLOADS


def get_download_limit_msg(user_id, is_playlist=False, is_multi_url=False):
    """Return appropriate wait message based on download type"""
    msgs = safe_get_messages(user_id)
    if is_playlist or is_multi_url:
        return msgs.AUDIO_WAIT_MSG
    return msgs.AUDIO_WAIT_MSG



# Helper function to safely set active download status
def set_active_download(user_id, status):
    """
    Thread-safe function to set the active download status for a user.
    Now manages a reference count instead of bool.
    When status=True, increments the counter.
    When status=False, decrements the counter (removes entry at 0).
    """
    with active_downloads_lock:
        if status:
            active_downloads[user_id] = active_downloads.get(user_id, 0) + 1
        else:
            count = active_downloads.get(user_id, 0)
            if count <= 1:
                active_downloads.pop(user_id, None)
            else:
                active_downloads[user_id] = count - 1

# Helper function to start the hourglass animation
def start_hourglass_animation(user_id, hourglass_msg_id, stop_anim):
    messages = safe_get_messages(user_id)
    """
    Start an hourglass animation in a separate thread

    Args:
        user_id: The user ID
        hourglass_msg_id: The message ID to animate
        stop_anim: An event to signal when to stop the animation

    Returns:
        The animation thread
    """

    def animate_hourglass():
        messages = safe_get_messages(user_id)
        """Animate an hourglass emoji by toggling between two hourglass emojis"""
        counter = 0
        emojis = messages.DOWNLOAD_STATUS_HOURGLASS_EMOJIS
        active = True
        start_time = time.time()
        last_update = 0

        while active and not stop_anim.is_set():
            try:
                current_time = time.time()
                elapsed = current_time - start_time
                
                # HARD LIMIT: Force stop animation after MAX_ANIMATION_DURATION
                if elapsed > LimitsConfig.MAX_ANIMATION_DURATION:
                    logger.warning(f"Hourglass animation force-stopped after {LimitsConfig.MAX_ANIMATION_DURATION}s for user {user_id}")
                    active = False
                    break
                
                minutes_passed = int(elapsed // 60)
                
                interval = _adaptive_interval(elapsed)
                
                if current_time - last_update < interval:
                    time.sleep(1.0)
                    continue
                
                emoji = emojis[counter % len(emojis)]
                # Attempt to edit message but don't keep trying if message is invalid
                result = safe_edit_message_text(user_id, hourglass_msg_id, f"{emoji} {messages.DOWNLOAD_STATUS_PLEASE_WAIT_MSG}")

                # If message edit returns None due to MESSAGE_ID_INVALID, stop animation
                if result is None and counter > 0:  # Allow first attempt to fail
                    active = False
                    break

                counter += 1
                last_update = current_time
                time.sleep(1.0)  # Check more frequently for stop event
            except Exception as e:
                logger.error(f"Error in hourglass animation: {e}")
                # Stop animation on error to prevent log spam
                active = False
                break

        logger.debug(f"Hourglass animation stopped for message {hourglass_msg_id}")

    # Start animation in a daemon thread so it will exit when the main thread exits
    hourglass_thread = threading.Thread(target=animate_hourglass, daemon=True)
    hourglass_thread.start()
    return hourglass_thread

# Cache for throttling upload progress edits per message
# Periodically cleaned to prevent unbounded growth
_last_upload_update_ts = {}
_last_upload_ts_lock = threading.Lock()

# Cache for upload logging to prevent watchdog false positives
_last_upload_log_ts = {}

# Timestamp of last cache cleanup
_last_ts_cleanup = time.time()
_TS_CLEANUP_INTERVAL = 300  # Clean every 5 minutes

# Helper function to start cycle progress animation
def start_cycle_progress(user_id, proc_msg_id, current_total_process, user_dir_name, cycle_stop, progress_data=None):
    messages = safe_get_messages(user_id)
    """
    Start a progress animation for HLS downloads

    Args:
        user_id: The user ID
        proc_msg_id: The message ID to update with progress
        current_total_process: String describing the current process
        user_dir_name: Directory name where fragments are saved
        cycle_stop: Event to signal animation stop
        progress_data: Optional dict with 'downloaded_bytes' and 'total_bytes' for real progress

    Returns:
        The animation thread
    """

    def cycle_progress():
        messages = safe_get_messages(user_id)
        """Show progress animation for HLS downloads"""
        counter = 0
        active = True
        start_time = time.time()
        last_update = 0

        while active and not cycle_stop.is_set():
            try:
                current_time = time.time()
                elapsed = current_time - start_time
                
                # HARD LIMIT: Force stop animation after MAX_ANIMATION_DURATION
                if elapsed > LimitsConfig.MAX_ANIMATION_DURATION:
                    logger.warning(f"Cycle progress animation force-stopped after {LimitsConfig.MAX_ANIMATION_DURATION}s for user {user_id}")
                    active = False
                    break
                
                minutes_passed = int(elapsed // 60)
                
                interval = _adaptive_interval(elapsed)
                
                if current_time - last_update < interval:
                    time.sleep(1.0)
                    continue
                
                counter = (counter + 1) % 11
                
                # Check for fragment files
                frag_files = []
                try:
                    frag_files = [f for f in os.listdir(user_dir_name) if 'Frag' in f]
                except (FileNotFoundError, PermissionError) as e:
                    logger.debug(f"Error checking fragment files: {e}")

                if frag_files:
                    last_frag = sorted(frag_files)[-1]
                    m = re.search(r'Frag(\d+)', last_frag)
                    frag_text = f"Frag{m.group(1)}" if m else "Frag?"
                else:
                    frag_text = messages.DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG

                # Check if we have real progress data (percentages)
                if progress_data and progress_data.get('downloaded_bytes') and progress_data.get('total_bytes'):
                    downloaded = progress_data.get('downloaded_bytes', 0)
                    total = progress_data.get('total_bytes', 0)
                    percent = (downloaded / total * 100) if total else 0
                    blocks = int(percent // 10)
                    bar = "🟩" * blocks + "⬜️" * (10 - blocks)
                    result = safe_edit_message_text(user_id, proc_msg_id,
                        f"{current_total_process}\n{messages.DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG}\n{bar}   {percent:.1f}%")
                else:
                    # Fallback to fragment-based animation
                    bar = "🟩" * counter + "⬜️" * (10 - counter)
                    result = safe_edit_message_text(user_id, proc_msg_id,
                        f"{current_total_process}\n{messages.DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG} {frag_text}\n{bar}")

                # If message was deleted (returns None), stop animation
                if result is None and counter > 2:  # Allow first few attempts to fail
                    active = False
                    break

                last_update = current_time
                time.sleep(1.0)  # Check more frequently for stop event

            except Exception as e:
                logger.warning(f"Cycle progress error: {e}")
                # Stop animation on consistent errors to prevent log spam
                active = False
                break

        logger.debug(f"Cycle progress animation stopped for message {proc_msg_id}")

    cycle_thread = threading.Thread(target=cycle_progress, daemon=True)
    cycle_thread.start()
    return cycle_thread

def _cleanup_upload_ts_cache():
    """Remove stale entries from upload timestamp caches to prevent memory leaks.
    Called periodically from progress_bar (every ~5 minutes)."""
    global _last_ts_cleanup
    now = time.time()
    if now - _last_ts_cleanup < _TS_CLEANUP_INTERVAL:
        return
    _last_ts_cleanup = now
    with _last_upload_ts_lock:
        # Remove entries older than 10 minutes (upload shouldn't be idle that long)
        cutoff = now - 600
        stale_keys = [k for k, ts in _last_upload_update_ts.items() if ts < cutoff]
        for k in stale_keys:
            del _last_upload_update_ts[k]
        stale_log_keys = [k for k, ts in _last_upload_log_ts.items() if ts < cutoff]
        for k in stale_log_keys:
            del _last_upload_log_ts[k]
    if stale_keys or stale_log_keys:
        logger.debug(f"[TS-CLEANUP] Removed {len(stale_keys)} upload + {len(stale_log_keys)} log entries")


def progress_bar(*args):
    # Pyrogram/pyrotgfork pass (current, total, *progress_args).
    # progress_args is (user_id, msg_id, status_text) → 5 args total.
    # Some forks may pass (current, total, speed, eta, file_size, user_id, msg_id, status_text) → 8 args.
    if len(args) < 5:
        return
    current = args[0]
    total = args[1]
    if len(args) >= 8:
        user_id, msg_id, status_text = args[5], args[6], args[7]
    else:
        user_id, msg_id, status_text = args[2], args[3], args[4]
    # Throttle to avoid flood: update at most once per second per message
    now = time.time()
    key = (user_id, msg_id)
    with _last_upload_ts_lock:
        last_ts = _last_upload_update_ts.get(key, 0)
    if now - last_ts < 1.0 and current < total:
        return

    # Log upload activity every 10 seconds to prevent watchdog false positives
    with _last_upload_ts_lock:
        last_log_ts = _last_upload_log_ts.get(key, 0)
        if now - last_log_ts >= 10.0:
            logger.info("[Upload] Uploading video to Telegram")
            _last_upload_log_ts[key] = now

    # Periodically clean stale entries to prevent unbounded memory growth
    _cleanup_upload_ts_cache()

    # Build upload progress bar (same style as download: 🟩/⬜️ cubes)
    try:
        percent = (current / total * 100) if total else 0
        blocks = int(percent // 10)
        bar = "🟩" * blocks + "⬜️" * (10 - blocks)
        text = f"{status_text}\n{bar}   {percent:.1f}%"
        safe_edit_message_text(user_id, msg_id, text)
        with _last_upload_ts_lock:
            _last_upload_update_ts[key] = now
    except Exception as e:
        logger.error(f"Error updating upload progress: {e}")
