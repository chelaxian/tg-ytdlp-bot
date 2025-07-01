"""
Video and playlist caching system
"""
import hashlib
import logging
from typing import List, Set, Dict, Optional
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


logger = logging.getLogger(__name__)


def get_url_hash(url: str) -> str:
    """Returns a hash of the URL for use as a cache key."""
    hash_result = hashlib.md5(url.encode()).hexdigest()
    logger.info(f"get_url_hash: '{url}' -> '{hash_result}'")
    return hash_result


def normalize_url_for_cache(url: str) -> str:
    """
    Normalizes URLs for caching based on a set of specific rules,
    removing all non-essential query parameters.
    """
    from magic.processing.tags import get_clean_url_for_tagging
    from magic.processing.url_parser import extract_real_url_if_google
    
    if not isinstance(url, str):
        return ''

    original_url = url
    url = extract_real_url_if_google(url)
    clean_url = get_clean_url_for_tagging(url)
    parsed = urlparse(clean_url)
    domain = parsed.netloc.lower()
    path = parsed.path
    query_params = parse_qs(parsed.query)

    # YouTube/youtu.be: always from www.youtube.com and youtu.be
    if domain in ('youtube.com', 'www.youtube.com'):
        domain = 'www.youtube.com'
    if domain in ('youtu.be', 'www.youtu.be'):
        domain = 'youtu.be'

    # Pornhub: keep full path and query parameters for unique video identification
    if domain.endswith('.pornhub.com'):
        base_domain = 'pornhub.com'
        result = urlunparse((parsed.scheme, base_domain, path, parsed.params, parsed.query, parsed.fragment))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (pornhub)")
        return result

    # TikTok: always strip all params, keep only path
    if 'tiktok.com' in domain:
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (tiktok)")
        return result

    # YouTube shorts and youtu.be: always strip all params
    if ("youtube.com" in domain and path.startswith('/shorts/')):
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (shorts)")
        return result
    if domain == 'youtu.be':
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (youtu.be)")
        return result

    # /watch: only v parameter
    if 'youtube.com' in domain and path == '/watch':
        v = None
        if 'v' in query_params:
            v = query_params['v'][0]
            v = v.split('?')[0].split('&')[0]
        if v:
            new_query = urlencode({'v': v}, doseq=True)
            result = urlunparse((parsed.scheme, domain, path, '', new_query, ''))
            logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (watch)")
            return result

    # Default fallback
    result = urlunparse((parsed.scheme, domain, path, '', '', ''))
    logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (fallback)")
    return result


def save_to_video_cache(url: str, quality_key: str, message_ids: List[int], 
                       clear: bool = False, original_text: str = None, db=None):
    """Saves message IDs to cache for video URLs."""
    from magic.processing.url_parser import is_youtube_url, youtube_to_short_url, youtube_to_long_url
    from magic.processing.tags import extract_url_range_tags
    from config import Config
    
    logger.info(f"save_to_video_cache called: url={url}, quality_key={quality_key}, "
               f"message_ids={message_ids}, clear={clear}")
    
    if not quality_key:
        logger.warning(f"save_to_video_cache: quality_key is empty, skipping cache save for URL: {url}")
        return
    
    # Check if this is a playlist with range - if so, skip cache
    if original_text:
        _, start_idx, end_idx, _, _, _, _ = extract_url_range_tags(original_text)
        if start_idx is not None and end_idx is not None:
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
            
            # Simplified logic for caching
            if len(message_ids) == 1:
                # Single video - save as is
                cache_ref.child(quality_key).set(str(message_ids[0]))
                logger.info(f"Saved single video to cache for URL hash {url_hash}, quality {quality_key}, msg_id {message_ids[0]}")
            else:
                # Split video (multiple parts) - save all IDs through comma
                ids_string = ",".join(map(str, message_ids))
                cache_ref.child(quality_key).set(ids_string)
                logger.info(f"Saved split video to cache for URL hash {url_hash}, quality {quality_key}, "
                           f"msg_ids {ids_string} ({len(message_ids)} parts)")
                
    except Exception as e:
        logger.error(f"Failed to save to cache: {e}")


def get_cached_message_ids(url: str, quality_key: str, db=None) -> Optional[List[int]]:
    """Searches cache for video URLs."""
    from magic.processing.url_parser import is_youtube_url, youtube_to_short_url, youtube_to_long_url
    from config import Config
    
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
                logger.info(f"get_cached_message_ids: found cached message_ids {result} for URL: {url}, quality: {quality_key}")
                return result
            else:
                logger.info(f"get_cached_message_ids: no cache found for hash {url_hash}, quality {quality_key}")
        
        logger.info(f"get_cached_message_ids: no cache found for any URL variant, returning None")
        return None
        
    except Exception as e:
        logger.error(f"Failed to get from cache: {e}")
        return None


def get_cached_qualities(url: str, db=None) -> Set[str]:
    """Get all cached qualities for the URL."""
    from config import Config
    
    try:
        url_hash = get_url_hash(normalize_url_for_cache(url))
        data = db.child(Config.VIDEO_CACHE_DB_PATH).child(url_hash).get().val()
        if data:
            return set(data.keys())
        return set()
    except Exception as e:
        logger.error(f"Failed to get cached qualities: {e}")
        return set()


def save_to_playlist_cache(playlist_url: str, quality_key: str, video_indices: List[int], 
                          message_ids: List[int], clear: bool = False, 
                          original_text: str = None, db=None):
    """Save playlist cache data."""
    from magic.processing.url_parser import is_youtube_url, youtube_to_short_url, youtube_to_long_url
    from magic.database.firebase import db_child_by_path
    from config import Config
    
    logger.info(f"save_to_playlist_cache called: playlist_url={playlist_url}, quality_key={quality_key}, "
               f"video_indices={video_indices}, message_ids={message_ids}, clear={clear}")
    
    if not quality_key:
        logger.warning(f"save_to_playlist_cache: quality_key is empty, skipping cache save for playlist: {playlist_url}")
        return
    
    if not hasattr(Config, 'PLAYLIST_CACHE_DB_PATH') or not Config.PLAYLIST_CACHE_DB_PATH:
        logger.error(f"save_to_playlist_cache: PLAYLIST_CACHE_DB_PATH is empty or invalid!")
        return
    
    try:
        from magic.processing.url_parser import strip_range_from_url
        
        urls = [normalize_url_for_cache(strip_range_from_url(playlist_url))]
        if is_youtube_url(playlist_url):
            urls.append(normalize_url_for_cache(strip_range_from_url(youtube_to_short_url(playlist_url))))
            urls.append(normalize_url_for_cache(strip_range_from_url(youtube_to_long_url(playlist_url))))
        
        logger.info(f"save_to_playlist_cache: normalized URLs: {urls}")
        
        for u in set(urls):
            url_hash = get_url_hash(u)
            logger.info(f"save_to_playlist_cache: using URL hash: {url_hash}")
            
            if clear:
                db_child_by_path(db, f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}/{quality_key}").remove()
                logger.info(f"Playlist cache cleared for URL hash {url_hash}, quality {quality_key}")
                continue
            
            if not message_ids or not video_indices:
                logger.warning(f"save_to_playlist_cache: message_ids or video_indices is empty")
                continue
            
            for i, msg_id in zip(video_indices, message_ids):
                cache_path = f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}/{quality_key}/{str(i)}"
                logger.info(f"save_to_playlist_cache: saving to path: {cache_path}, msg_id: {msg_id}")
                db_child_by_path(db, cache_path).set(str(msg_id))
            
            logger.info(f"Saved to playlist cache for URL hash {url_hash}, quality {quality_key}, "
                       f"indices: {video_indices}, msg_ids: {message_ids}")
                       
    except Exception as e:
        logger.error(f"Failed to save to playlist cache: {e}")


def get_cached_playlist_videos(playlist_url: str, quality_key: str, 
                              requested_indices: List[int], db=None) -> Dict[int, int]:
    """Get cached playlist videos."""
    from magic.processing.url_parser import is_youtube_url, youtube_to_short_url, youtube_to_long_url
    from magic.database.firebase import db_child_by_path  
    from config import Config
    
    logger.info(f"get_cached_playlist_videos called: playlist_url={playlist_url}, "
               f"quality_key={quality_key}, requested_indices={requested_indices}")
    
    if not quality_key:
        logger.warning(f"get_cached_playlist_videos: quality_key is empty for playlist: {playlist_url}")
        return {}
    
    try:
        from magic.processing.url_parser import strip_range_from_url
        from magic.download.quality import ceil_to_popular
        
        quality_keys = [quality_key]
        # Also try rounded quality
        try:
            if quality_key.endswith('p'):
                rounded_quality = f"{ceil_to_popular(int(quality_key[:-1]))}p"
                if rounded_quality != quality_key:
                    quality_keys.append(rounded_quality)
        except Exception:
            pass
        
        urls = [normalize_url_for_cache(strip_range_from_url(playlist_url))]
        if is_youtube_url(playlist_url):
            urls.append(normalize_url_for_cache(strip_range_from_url(youtube_to_short_url(playlist_url))))
            urls.append(normalize_url_for_cache(strip_range_from_url(youtube_to_long_url(playlist_url))))
        
        found = {}
        
        for u in set(urls):
            url_hash = get_url_hash(u)
            logger.info(f"get_cached_playlist_videos: checking URL hash: {url_hash}")
            
            for qk in quality_keys:
                logger.info(f"get_cached_playlist_videos: checking quality: {qk}")
                
                for index in requested_indices:
                    index_str = str(index)
                    try:
                        cache_path = f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}/{qk}/{index_str}"
                        msg_id = db_child_by_path(db, cache_path).get().val()
                        if msg_id is not None:
                            found[index] = int(msg_id)
                            logger.info(f"get_cached_playlist_videos: found cached video for index {index} "
                                       f"(quality={qk}): {msg_id}")
                    except Exception as e:
                        logger.error(f"get_cached_playlist_videos: error reading cache for "
                                   f"url_hash={url_hash}, quality={qk}, index={index}: {e}")
                        continue
                
                if found:
                    logger.info(f"get_cached_playlist_videos: returning cached videos for "
                               f"indices {list(found.keys())}: {found}")
                    return found
        
        logger.info(f"get_cached_playlist_videos: no cache found for any URL/quality variant, returning empty dict")
        return {}
        
    except Exception as e:
        logger.error(f"Failed to get from playlist cache: {e}")
        return {}


def get_cached_playlist_qualities(playlist_url: str, db=None) -> Set[str]:
    """Get all cached qualities for playlist URL."""
    from magic.processing.url_parser import strip_range_from_url
    from config import Config
    
    try:
        clean_url = strip_range_from_url(playlist_url)
        url_hash = get_url_hash(normalize_url_for_cache(clean_url))
        data = db.child(Config.PLAYLIST_CACHE_DB_PATH).child(url_hash).get().val()
        if data:
            return set(data.keys())
        return set()
    except Exception as e:
        logger.error(f"Failed to get cached playlist qualities: {e}")
        return set()


def get_cached_playlist_count(playlist_url: str, quality_key: str, 
                             indices: Optional[List[int]] = None, db=None) -> int:
    """Get count of cached playlist videos."""
    if indices is None:
        return 0
    
    cached_videos = get_cached_playlist_videos(playlist_url, quality_key, indices, db)
    return len(cached_videos)


def is_any_playlist_index_cached(playlist_url: str, quality_key: str, 
                                indices: List[int], db=None) -> bool:
    """Check if any playlist index is cached."""
    cached_count = get_cached_playlist_count(playlist_url, quality_key, indices, db)
    return cached_count > 0 