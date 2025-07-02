"""Caching functions"""
import logging
import hashlib

logger = logging.getLogger(__name__)

# --- new functions for caching ---
def get_url_hash(url: str) -> str:
    """Returns a hash of the URL for use as a cache key."""
    import hashlib
    hash_result = hashlib.md5(url.encode()).hexdigest()
    logger.info(f"get_url_hash: '{url}' -> '{hash_result}'")
    return hashlib.md5(url.encode()).hexdigest()

def save_to_video_cache(url: str, quality_key: str, message_ids: list, clear: bool = False, original_text: str = None):
    """Saves message IDs to cache for two YouTube link variants (long/short) at once."""
    logger.info(
        f"save_to_video_cache called: url={url}, quality_key={quality_key}, message_ids={message_ids}, clear={clear}, original_text={original_text}")
    if not quality_key:
        logger.warning(f"save_to_video_cache: quality_key is empty, skipping cache save for URL: {url}")
        return
    # Check if this is a playlist with range - if so, skip cache
    if original_text and is_playlist_with_range(original_text):
        logger.info(f"Playlist with range detected, skipping cache save for URL: {url}")
        return

    try:
        urls = [normalize_url_for_cache(url)]
        # If it's YouTube, add both options
        if is_youtube_url(url):
            urls.append(normalize_url_for_cache(youtube_to_short_url(url)))
            urls.append(normalize_url_for_cache(youtube_to_long_url(url)))
        logger.info(f"save_to_video_cache: normalized URLs: {urls}")
        for u in set(urls):
            url_hash = get_url_hash(u)
            cache_ref = db.child(Config.VIDEO_CACHE_DB_PATH).child(url_hash)
            if clear:
                cache_ref.child(quality_key).remove()
                logger.info(f"Cache cleared for URL hash {url_hash}, quality {quality_key}")
                continue
            if not message_ids:
                logger.warning(f"save_to_video_cache: message_ids is empty for URL: {url}, quality: {quality_key}")
                continue
            
            # Упрощенная логика для кэширования
            if len(message_ids) == 1:
                # Одиночное видео - сохраняем как есть
                cache_ref.child(quality_key).set(str(message_ids[0]))
                logger.info(f"Saved single video to cache for URL hash {url_hash}, quality {quality_key}, msg_id {message_ids[0]}")
            else:
                # Split видео (множественные части) - сохраняем все ID через запятую
                ids_string = ",".join(map(str, message_ids))
                cache_ref.child(quality_key).set(ids_string)
                logger.info(f"Saved split video to cache for URL hash {url_hash}, quality {quality_key}, msg_ids {ids_string} ({len(message_ids)} parts)")
    except Exception as e:
        logger.error(f"Failed to save to cache: {e}")


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
            ids_string = db.child(Config.VIDEO_CACHE_DB_PATH).child(url_hash).child(quality_key).get().val()
            logger.info(f"get_cached_message_ids: raw value from Firebase: {ids_string} (type: {type(ids_string)})")
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



def get_cached_qualities(url: str) -> set:
    """He gets all the castle qualities for the URL."""
    try:
        url_hash = get_url_hash(normalize_url_for_cache(url))
        data = db.child(Config.VIDEO_CACHE_DB_PATH).child(url_hash).get().val()
        if data:
            return set(data.keys())
        return set()
    except Exception as e:
        logger.error(f"Failed to get cached qualities: {e}")
        return set()

# Added playlist caching - separate functions for saving and retrieving playlist cache
def save_to_playlist_cache(playlist_url: str, quality_key: str, video_indices: list, message_ids: list,
                           clear: bool = False, original_text: str = None):
    logger.info(
        f"save_to_playlist_cache called: playlist_url={playlist_url}, quality_key={quality_key}, video_indices={video_indices}, message_ids={message_ids}, clear={clear}")
    if not quality_key:
        logger.warning(
            f"save_to_playlist_cache: quality_key is empty, skipping cache save for playlist: {playlist_url}")
        return
    if not hasattr(Config,
                   'PLAYLIST_CACHE_DB_PATH') or not Config.PLAYLIST_CACHE_DB_PATH or Config.PLAYLIST_CACHE_DB_PATH.strip() in (
            '', '/', '.'):
        logger.error(
            f"save_to_playlist_cache: PLAYLIST_CACHE_DB_PATH is empty or invalid! Skipping cache write for playlist: {playlist_url}")
        return
    try:
        urls = [normalize_url_for_cache(strip_range_from_url(playlist_url))]
        if is_youtube_url(playlist_url):
            urls.append(normalize_url_for_cache(strip_range_from_url(youtube_to_short_url(playlist_url))))
            urls.append(normalize_url_for_cache(strip_range_from_url(youtube_to_long_url(playlist_url))))
        logger.info(f"save_to_playlist_cache: normalized URLs: {urls}")
        for u in set(urls):
            url_hash = get_url_hash(u)
            logger.info(f"save_to_playlist_cache: using URL hash: {url_hash}")
            if clear:
                # Delete the entire quality branch
                db_child_by_path(db, f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}/{quality_key}").remove()
                logger.info(f"Playlist cache cleared for URL hash {url_hash}, quality {quality_key}")
                continue
            if not message_ids or not video_indices:
                logger.warning(
                    f"save_to_playlist_cache: message_ids or video_indices is empty for playlist: {playlist_url}, quality: {quality_key}")
                continue
            for i, msg_id in zip(video_indices, message_ids):
                cache_path = f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}/{quality_key}/{str(i)}"
                logger.info(f"save_to_playlist_cache: saving to path: {cache_path}, msg_id: {msg_id}")
                db_child_by_path(db, cache_path).set(str(msg_id))
            logger.info(
                f"Saved to playlist cache for URL hash {url_hash}, quality {quality_key}, indices: {video_indices}, msg_ids: {message_ids}")
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
    if not hasattr(Config,
                   'PLAYLIST_CACHE_DB_PATH') or not Config.PLAYLIST_CACHE_DB_PATH or Config.PLAYLIST_CACHE_DB_PATH.strip() in (
            '', '/', '.'):
        logger.error(
            f"get_cached_playlist_videos: PLAYLIST_CACHE_DB_PATH is empty or invalid! Skipping cache read for playlist: {playlist_url}")
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

                # Check each requested index separately
                for index in requested_indices:
                    index_str = str(index)
                    try:
                        cache_path = f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}/{qk}/{index_str}"
                        msg_id = db_child_by_path(db, cache_path).get().val()
                        if msg_id is not None:
                            found[index] = int(msg_id)
                            logger.info(
                                f"get_cached_playlist_videos: found cached video for index {index} (quality={qk}): {msg_id}")
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
        # Get all the quality keys inside the url_hash folder
        data = db_child_by_path(db, f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}").get().val()
        if data:
            return set(data.keys())
        return set()
    except Exception as e:
        logger.error(f"Failed to get cached playlist qualities: {e}")
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
                if indices is not None:
                    # For large ranges, we use a fast count
                    if len(indices) > 100:
                        try:
                            data = db_child_by_path(db, f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}/{qk}").get().val()
                            if data and isinstance(data, dict):
                                # Count only indices from the requested range
                                cached_count = sum(
                                    1 for index in indices if str(index) in data and data[str(index)] is not None)
                                logger.info(
                                    f"get_cached_playlist_count: fast count for large range: {cached_count} cached videos")
                                return cached_count
                        except Exception as e:
                            logger.error(f"get_cached_playlist_count: error in fast count: {e}")
                            continue
                    else:
                        # For small ranges, check each index separately
                        for index in indices:
                            index_str = str(index)
                            val = db_child_by_path(db,
                                                   f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}/{qk}/{index_str}").get().val()
                            if val is not None:
                                cached_count += 1
                                logger.info(
                                    f"get_cached_playlist_count: found cached video for index {index} (quality={qk}): {val}")
                else:
                    # Get all quality data and count non-empty records
                    try:
                        data = db_child_by_path(db, f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}/{qk}").get().val()
                        if data:
                            if isinstance(data, dict):
                                cached_count = len(data)
                            elif isinstance(data, list):
                                # If the data is a list, count non-empty elements
                                cached_count = sum(1 for item in data if item is not None)
                            else:
                                logger.warning(
                                    f"get_cached_playlist_count: unexpected data type for url_hash={url_hash}, quality={qk}, type={type(data)}")
                                continue
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


def is_any_playlist_index_cached(playlist_url, quality_key, indices):
    """Checks if at least one index from the range is in the playlist cache."""
    cached = get_cached_playlist_videos(playlist_url, quality_key, indices)
    return bool(cached)
