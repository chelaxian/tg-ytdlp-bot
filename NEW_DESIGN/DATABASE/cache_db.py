import os
import json
import time
import threading
from datetime import datetime, timedelta
from CONFIG.config import Config
from HELPERS.app_instance import get_app_lazy
from HELPERS.logger import logger, send_to_user, send_to_logger
from HELPERS.safe_messeger import fake_message
from DATABASE.firebase_init import db
from URL_PARSERS.normalizer import normalize_url_for_cache
from URL_PARSERS.youtube import is_youtube_url, youtube_to_short_url, youtube_to_long_url
from URL_PARSERS.playlist_utils import is_playlist_with_range
from COMMANDS.subtitles_cmd import check_subs_availability, is_subs_enabled, get_user_subs_auto_mode

# Get app instance
app = get_app_lazy()

# Global variable for local cache Firebase
firebase_cache = {}

# Global variable to monitor the state of automatic loading cache
auto_cache_enabled = getattr(Config, 'AUTO_CACHE_RELOAD_ENABLED', True)
auto_cache_thread = None

###################################################

def load_firebase_cache():
    """Load local Firebase cache from JSON file."""
    global firebase_cache
    try:
        cache_file = getattr(Config, 'FIREBASE_CACHE_FILE', 'firebase_cache.json')
        if os.path.exists(cache_file):
            with open(cache_file, "r", encoding="utf-8") as f:
                firebase_cache = json.load(f)
            print(f"✅ Firebase cache loaded: {len(firebase_cache)} root nodes")
        else:
            print(f"⚠️ Firebase cache file not found, starting with empty cache: {cache_file}")
            firebase_cache = {}
    except Exception as e:
        print(f"❌ Failed to load firebase cache: {e}")
        firebase_cache = {}

def reload_firebase_cache():
    """Reloading the local Firebase cache from JSON file"""
    global firebase_cache
    try:
        cache_file = getattr(Config, 'FIREBASE_CACHE_FILE', 'firebase_cache.json')
        if os.path.exists(cache_file):
            with open(cache_file, "r", encoding="utf-8") as f:
                firebase_cache = json.load(f)
            print(f"✅ Firebase cache reloaded: {len(firebase_cache)} root nodes")
            return True
        else:
            print(f"⚠️ Firebase cache file not found: {cache_file}")
            return False
    except Exception as e:
        print(f"❌ Failed to reload firebase cache: {e}")
        return False


def get_next_reload_time(interval_hours: int) -> datetime:
    """
    Returns Datetime the following reloading point,
    aligned according to the N-hour step from 00:00.
    """
    now = datetime.now()
    # Today's border is “midnight”
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds_since_midnight = (now - midnight).total_seconds()
    interval_seconds = interval_hours * 3600
    # How many full intervals have already passed since midnight
    intervals_passed = int(seconds_since_midnight // interval_seconds)
    # Next = midnight + (intervals_passed + 1) * step
    return midnight + timedelta(seconds=(intervals_passed + 1) * interval_seconds)

def auto_reload_firebase_cache():
    """A stream that every n clock restarts a local cache."""
    global auto_cache_enabled

    interval_hours = getattr(Config, 'RELOAD_CACHE_EVERY', 4)
    while auto_cache_enabled:
        next_exec = get_next_reload_time(interval_hours)
        now = datetime.now()
        wait_seconds = (next_exec - now).total_seconds()
        print(
            f"⏳ Waiting until {next_exec.strftime('%Y-%m-%d %H:%M:%S')} "
            f"to reload Firebase cache ({wait_seconds/3600:.2f} hours)"
        )
        # "Smart" Sleep
        end_time = time.time() + wait_seconds
        while auto_cache_enabled and time.time() < end_time:
            time.sleep(min(1, end_time - time.time()))
        if not auto_cache_enabled:
            print("🛑 Auto Firebase cache reloader stopped by admin")
            return
        # Run the reboot
        try:
            user_id = (
                Config.ADMIN[0]
                if isinstance(Config.ADMIN, (list, tuple))
                else Config.ADMIN
            )
            print(f"🔄 Triggering /reload_cache as admin (user_id={user_id})")
            # Just reload the cache directly
            success = reload_firebase_cache()
            if success:
                print("✅ Firebase cache reloaded successfully!")
            else:
                print("❌ Failed to reload Firebase cache")
        except Exception as e:
            print(f"❌ Error running auto reload_cache: {e}")
            import traceback; traceback.print_exc()

def start_auto_cache_reloader():
    """The flow of auto -outload starts."""
    global auto_cache_thread, auto_cache_enabled
    if auto_cache_enabled and auto_cache_thread is None:
        auto_cache_thread = threading.Thread(
            target=auto_reload_firebase_cache,
            daemon=True
        )
        auto_cache_thread.start()
        print(
            f"🚀 Auto Firebase cache reloader started "
            f"(every {getattr(Config, 'RELOAD_CACHE_EVERY', 4)}h from 00:00)"
        )
    return auto_cache_thread

def stop_auto_cache_reloader():
    """Stops the flow of auto -transshipment."""
    global auto_cache_enabled, auto_cache_thread
    auto_cache_enabled = False
    if auto_cache_thread and auto_cache_thread.is_alive():
        print("🛑 Auto Firebase cache reloader stopped")
    auto_cache_thread = None

def toggle_auto_cache_reloader():
    """Switchs the transload mode."""
    global auto_cache_enabled
    auto_cache_enabled = not auto_cache_enabled
    if auto_cache_enabled:
        start_auto_cache_reloader()
    else:
        stop_auto_cache_reloader()
    return auto_cache_enabled

# We load the cache when importing module
load_firebase_cache()

def get_from_local_cache(path_parts):
    """
    Receives data from a local cache along the way, divided into parts
    For example: get_from_local_cache (['Bot', 'Video_cache', 'Hash123', '720p'])
    """
    global firebase_cache
    current = firebase_cache
    for part in path_parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            log_firebase_access_attempt(path_parts, success=False)
            return None
    
    log_firebase_access_attempt(path_parts, success=True)
    return current

def log_firebase_access_attempt(path_parts, success=True):
    """
    Logs attempts to turn to a local cache (to track the remaining .get () calls)
    """
    # Show the path in JSON format for local cache
    path_str = ' -> '.join(path_parts)  # For example: "bot -> video_cache -> playlists -> url_hash -> quality"
    status = "SUCCESS" if success else "MISS"
    print(f"🔥 Firebase access attempt: {path_str} -> {status}")

###################################################

def auto_cache_command(app, message):
    """Command handler to control the automatic loading of the Firebase cache."""
    if int(message.chat.id) not in Config.ADMIN:
        send_to_user(message, "❌ Access denied. Admin only.")
        return

    new_state = toggle_auto_cache_reloader()
    interval = getattr(Config, 'RELOAD_CACHE_EVERY', 4)

    if new_state:
        next_exec = get_next_reload_time(interval)
        delta_min = int((next_exec - datetime.now()).total_seconds() // 60)
        send_to_user(
            message,
            "🔄 Auto Firebase cache reloading started!\n\n"
            f"📊 Status: ✅ ENABLED\n"
            f"⏰ Schedule: every {interval} hours from 00:00\n"
            f"🕒 Next reload: {next_exec.strftime('%H:%M')} (in {delta_min} minutes)"
        )
        send_to_logger(message, f"Auto reload started; next at {next_exec}")
    else:
        send_to_user(
            message,
            "🛑 Auto Firebase cache reloading stopped!\n\n"
            "📊 Status: ❌ DISABLED\n"
            "💡 Use /auto_cache again to re-enable"
        )
        send_to_logger(message, "Auto reload stopped by admin.")
   

# Added playlist caching - separate functions for saving and retrieving playlist cache
def save_to_playlist_cache(playlist_url: str, quality_key: str, video_indices: list, message_ids: list,
                           clear: bool = False, original_text: str = None):
    logger.info(
        f"save_to_playlist_cache called: playlist_url={playlist_url}, quality_key={quality_key}, video_indices={video_indices}, message_ids={message_ids}, clear={clear}")
    
    if not quality_key:
        logger.warning(f"quality_key is empty, skipping cache save for playlist: {playlist_url}")
        return

    if not hasattr(Config, 'PLAYLIST_CACHE_DB_PATH') or not Config.PLAYLIST_CACHE_DB_PATH or Config.PLAYLIST_CACHE_DB_PATH.strip() in ('', '/', '.'):
        logger.error(f"PLAYLIST_CACHE_DB_PATH is invalid, skipping write for: {playlist_url}")
        return

    try:
        # Normalize the URL (without the range) and form all link options
        urls = [normalize_url_for_cache(strip_range_from_url(playlist_url))]
        if is_youtube_url(playlist_url):
            urls.extend([
                normalize_url_for_cache(strip_range_from_url(youtube_to_short_url(playlist_url))),
                normalize_url_for_cache(strip_range_from_url(youtube_to_long_url(playlist_url))),
            ])
        logger.info(f"Normalized playlist URLs: {urls}")

        for u in set(urls):
            url_hash = get_url_hash(u)
            logger.info(f"Using playlist URL hash: {url_hash}")

            if clear:
                db_child_by_path(db, f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}/{quality_key}").remove()
                logger.info(f"Cleared playlist cache for hash={url_hash}, quality={quality_key}")
                continue

            if not message_ids or not video_indices:
                logger.warning(f"message_ids or video_indices is empty for playlist: {playlist_url}, quality: {quality_key}")
                continue

            for i, msg_id in zip(video_indices, message_ids):
                
                path_parts_local = ["bot", "video_cache", "playlists", url_hash, quality_key, str(i)]
                path_parts = [Config.PLAYLIST_CACHE_DB_PATH, url_hash, quality_key, str(i)]
                already_cached = get_from_local_cache(path_parts_local)

                if already_cached:
                    logger.info(f"Playlist part already cached: {path_parts_local}, skipping")
                    continue

                db_child_by_path(db, "/".join(path_parts)).set(str(msg_id))
                logger.info(f"Saved to playlist cache: path={path_parts}, msg_id={msg_id}")

        logger.info(f"✅ Saved to playlist cache for hash={url_hash}, quality={quality_key}, indices={video_indices}, message_ids={message_ids}")

    except Exception as e:
        logger.error(f"Failed to save to playlist cache: {e}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        

def get_cached_playlist_videos(playlist_url: str, quality_key: str, requested_indices: list) -> dict:
    logger.info(
        f"get_cached_playlist_videos called: playlist_url={playlist_url}, quality_key={quality_key}, requested_indices={requested_indices}")
    if not quality_key:
        logger.warning(f"get_cached_playlist_videos: quality_key is empty for playlist: {playlist_url}")
        return {}
    try:
        urls = [normalize_url_for_cache(strip_range_from_url(playlist_url))]
        if is_youtube_url(playlist_url):
            urls.append(normalize_url_for_cache(strip_range_from_url(youtube_to_short_url(playlist_url))))
            urls.append(normalize_url_for_cache(strip_range_from_url(youtube_to_long_url(playlist_url))))
        quality_keys = [quality_key]
        try:
            if quality_key.endswith('p'):
                h = int(quality_key[:-1])
                rounded = f"{ceil_to_popular(h)}p"
                if rounded != quality_key:
                    quality_keys.append(rounded)
        except Exception:
            pass
        found = {}
        logger.info(f"get_cached_playlist_videos: checking URLs: {urls}")
        logger.info(f"get_cached_playlist_videos: checking quality keys: {quality_keys}")

        for u in set(urls):
            url_hash = get_url_hash(u)
            logger.info(f"get_cached_playlist_videos: checking URL hash: {url_hash}")
            for qk in quality_keys:
                logger.info(f"get_cached_playlist_videos: checking quality: {qk}")

                # A new way for searching in Dump!
                arr = get_from_local_cache(["bot", "video_cache", "playlists", url_hash, qk])
                if isinstance(arr, list):
                    for index in requested_indices:
                        try:
                            if index < len(arr) and arr[index]:
                                found[index] = int(arr[index])
                                logger.info(
                                    f"get_cached_playlist_videos: found cached video for index {index} (quality={qk}): {arr[index]}")
                        except Exception as e:
                            logger.error(
                                f"get_cached_playlist_videos: error reading cache for url_hash={url_hash}, quality={qk}, index={index}: {e}")
                            continue
                    if found:
                        logger.info(
                            f"get_cached_playlist_videos: returning cached videos for indices {list(found.keys())}: {found}")
                        return found

        logger.info(f"get_cached_playlist_videos: no cache found for any URL/quality variant, returning empty dict")
        return {}
    except Exception as e:
        logger.error(f"Failed to get from playlist cache: {e}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return {}


def get_cached_playlist_qualities(playlist_url: str) -> set:
    """Gets all available qualities for a cached playlist."""
    try:
        url_hash = get_url_hash(normalize_url_for_cache(strip_range_from_url(playlist_url)))
        data = get_from_local_cache(["bot", "video_cache", "playlists", url_hash])
        if data and isinstance(data, dict):
            return set(data.keys())
        return set()
    except Exception as e:
        logger.error(f"Failed to get cached playlist qualities: {e}")
        return set()


def is_any_playlist_index_cached(playlist_url, quality_key, indices):
    """Checks if at least one index from the range is in the playlist cache."""
    cached = get_cached_playlist_videos(playlist_url, quality_key, indices)
    return bool(cached)

def get_cached_qualities(url: str) -> set:
    """He gets all the castle qualities for the URL."""
    try:
        url_hash = get_url_hash(normalize_url_for_cache(url))
        
        # We use local cache instead of Firebase
        path_parts = ["bot", "video_cache", url_hash]
        data = get_from_local_cache(path_parts)
        
        if data and isinstance(data, dict):
            return set(data.keys())
        return set()
    except Exception as e:
        logger.error(f"Failed to get cached qualities: {e}")
        return set()

# --- Quickly get the number of cached videos for quality ---
def get_cached_playlist_count(playlist_url: str, quality_key: str, indices: list = None) -> int:
    """
    Returns the number of cached videos for the given quality (based on the number of keys in the database),
    considering and rounded quality_key (ceil_to_popular).
    If a list of indices is passed, it only counts their intersection with the cache.
    For large ranges (>100), it uses a fast count.
    """
    try:
        urls = [normalize_url_for_cache(strip_range_from_url(playlist_url))]
        if is_youtube_url(playlist_url):
            urls.append(normalize_url_for_cache(strip_range_from_url(youtube_to_short_url(playlist_url))))
            urls.append(normalize_url_for_cache(strip_range_from_url(youtube_to_long_url(playlist_url))))
        quality_keys = [quality_key]
        try:
            if quality_key.endswith('p'):
                h = int(quality_key[:-1])
                rounded = f"{ceil_to_popular(h)}p"
                if rounded != quality_key:
                    quality_keys.append(rounded)
        except Exception:
            pass

        cached_count = 0
        for u in set(urls):
            url_hash = get_url_hash(u)
            for qk in quality_keys:
                arr = get_from_local_cache(["bot", "video_cache", "playlists", url_hash, qk])
                if not isinstance(arr, list):
                    continue
                if indices is not None:
                    # For large ranges, we use a fast count
                    if len(indices) > 100:
                        try:
                            cached_count = sum(1 for index in indices if index < len(arr) and arr[index] is not None)
                            logger.info(
                                f"get_cached_playlist_count: fast count for large range: {cached_count} cached videos")
                            return cached_count
                        except Exception as e:
                            logger.error(f"get_cached_playlist_count: error in fast count: {e}")
                            continue
                    else:
                        # For small ranges, check each index separately
                        for index in indices:
                            try:
                                if index < len(arr) and arr[index] is not None:
                                    cached_count += 1
                                    logger.info(
                                        f"get_cached_playlist_count: found cached video for index {index} (quality={qk}): {arr[index]}")
                            except Exception as e:
                                logger.error(
                                    f"get_cached_playlist_count: error reading cache for url_hash={url_hash}, quality={qk}, index={index}: {e}")
                                continue
                else:
                    # Count all non-empty records
                    try:
                        cached_count = sum(1 for item in arr if item is not None)
                    except Exception as e:
                        logger.error(
                            f"get_cached_playlist_count: error reading cache for url_hash={url_hash}, quality={qk}: {e}")
                        continue

                if cached_count > 0:
                    logger.info(f"get_cached_playlist_count: returning {cached_count} cached videos for quality {qk}")
                    return cached_count

        logger.info(f"get_cached_playlist_count: no cached videos found, returning 0")
        return 0
    except Exception as e:
        logger.error(f"get_cached_playlist_count error: {e}")
        return 0

# --- new functions for caching ---
def get_url_hash(url: str) -> str:
    """Returns a hash of the URL for use as a cache key."""
    import hashlib
    hash_result = hashlib.md5(url.encode()).hexdigest()
    logger.info(f"get_url_hash: '{url}' -> '{hash_result}'")
    return hashlib.md5(url.encode()).hexdigest()

def save_to_video_cache(url: str, quality_key: str, message_ids: list, clear: bool = False, original_text: str = None, user_id: int = None):
    """Saves message IDs to Firebase video cache after checking local cache to avoid duplication."""
    found_type = None
    if user_id is not None:
        found_type = check_subs_availability(url, user_id, quality_key, return_type=True)
        subs_enabled = is_subs_enabled(user_id)
        auto_mode = get_user_subs_auto_mode(user_id)
        need_subs = (subs_enabled and ((auto_mode and found_type == "auto") or (not auto_mode and found_type == "normal")))
        if need_subs:
            logger.info("Video with subtitles is not cached!")
            return

    logger.info(f"save_to_video_cache called: url={url}, quality_key={quality_key}, message_ids={message_ids}, clear={clear}, original_text={original_text}")

    if not quality_key:
        logger.warning(f"save_to_video_cache: quality_key is empty, skipping cache save for URL: {url}")
        return

    if original_text and is_playlist_with_range(original_text):
        logger.info(f"Playlist with range detected, skipping cache save for URL: {url}")
        return

    try:
        urls = [normalize_url_for_cache(url)]
        if is_youtube_url(url):
            urls += [
                normalize_url_for_cache(youtube_to_short_url(url)),
                normalize_url_for_cache(youtube_to_long_url(url))
            ]
        
        logger.info(f"save_to_video_cache: normalized URLs: {urls}")

        for u in set(urls):
            url_hash = get_url_hash(u)
            path_parts_local = ["bot", "video_cache", "playlists", url_hash]
            path_parts = [Config.VIDEO_CACHE_DB_PATH, url_hash]
            
            # === CLEAR MODE ===
            if clear:
                logger.info(f"Clearing cache for URL hash {url_hash}, quality {quality_key}")
                db.child(*path_parts).child(quality_key).remove()
                continue

            if not message_ids:
                logger.warning(f"save_to_video_cache: message_ids is empty for URL: {url}, quality: {quality_key}")
                continue

            # === LOCAL CACHE CHECK ===
            existing = get_from_local_cache(path_parts_local + [quality_key])
            if existing is not None:
                logger.info(f"Cache already exists for URL hash {url_hash}, quality {quality_key}, skipping save.")
                continue  # skip writing if already cached locally

            cache_ref = db.child(*path_parts)

            if len(message_ids) == 1:
                cache_ref.child(quality_key).set(str(message_ids[0]))
                logger.info(f"Saved single video to cache: hash={url_hash}, quality={quality_key}, msg_id={message_ids[0]}")
            else:
                ids_string = ",".join(map(str, message_ids))
                cache_ref.child(quality_key).set(ids_string)
                logger.info(f"Saved split video to cache: hash={url_hash}, quality={quality_key}, msg_ids={ids_string}")

    except Exception as e:
        logger.error(f"Failed to save to video cache: {e}")
        

def get_cached_message_ids(url: str, quality_key: str) -> list:
    """Searches cache for both versions of YouTube link (long/short)."""
    logger.info(f"get_cached_message_ids called: url={url}, quality_key={quality_key}")
    if not quality_key:
        logger.warning(f"get_cached_message_ids: quality_key is empty for URL: {url}")
        return None
    try:
        urls = [normalize_url_for_cache(url)]
        if is_youtube_url(url):
            short_url = youtube_to_short_url(url)
            long_url = youtube_to_long_url(url)
            urls.append(normalize_url_for_cache(short_url))
            urls.append(normalize_url_for_cache(long_url))
            logger.info(f"get_cached_message_ids: original={url}, short={short_url}, long={long_url}")
        logger.info(f"get_cached_message_ids: checking URLs: {urls}")
        for u in set(urls):
            url_hash = get_url_hash(u)
            logger.info(f"get_cached_message_ids: checking hash {url_hash} for quality {quality_key}")
            
            # We use local cache instead of Firebase
            path_parts = ["bot", "video_cache", url_hash, quality_key]
            ids_string = get_from_local_cache(path_parts)
            
            logger.info(f"get_cached_message_ids: raw value from local cache: {ids_string} (type: {type(ids_string)})")
            if ids_string:
                result = [int(msg_id) for msg_id in ids_string.split(',')]
                logger.info(
                    f"get_cached_message_ids: found cached message_ids {result} for URL: {url}, quality: {quality_key}")
                return result
            else:
                logger.info(f"get_cached_message_ids: no cache found for hash {url_hash}, quality {quality_key}")
        logger.info(f"get_cached_message_ids: no cache found for any URL variant, returning None")
        return None
    except Exception as e:
        logger.error(f"Failed to get from cache: {e}")
        return None
