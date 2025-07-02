"""
URL parsing and processing functions
"""
import re
import logging
import hashlib
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse, unquote
from typing import Optional
from config import Config

logger = logging.getLogger(__name__)


def extract_real_url_if_google(url: str) -> str:
    """
    If the link is a redirect via Google, returns the target link.
    Otherwise, returns the original link.
    """
    parsed = urlparse(url)
    if parsed.netloc.endswith('google.com') and parsed.path.startswith('/url'):
        qs = parse_qs(parsed.query)
        # Google may use either ?q= or ?url=
        real_url = qs.get('q') or qs.get('url')
        if real_url:
            # Take the first variant, decode if needed
            return unquote(real_url[0])
    return url



def is_youtube_url(url: str) -> bool:
    parsed = urlparse(url)
    return 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc



def youtube_to_short_url(url: str) -> str:
    """Converts youtube.com/watch?v=... to youtu.be/... while preserving query parameters."""
    parsed = urlparse(url)
    if 'youtube.com' in parsed.netloc and parsed.path == '/watch':
        qs = parse_qs(parsed.query)
        v = qs.get('v', [None])[0]
        if v:
            # Collect query without v
            query = {k: v for k, v in qs.items() if k != 'v'}
            query_str = urlencode(query, doseq=True)
            base = f'https://youtu.be/{v}'
            if query_str:
                return f'{base}?{query_str}'
            return base
    elif 'youtube.com' in parsed.netloc and parsed.path.startswith('/shorts/'):
        # For YouTube Shorts, convert to youtu.be format
        video_id = parsed.path.split('/')[2]  # /shorts/VIDEO_ID
        if video_id:
            return f'https://youtu.be/{video_id}'
    return url


def youtube_to_long_url(url: str) -> str:
    """Converts youtu.be/... to youtube.com/watch?v=... while preserving query parameters."""
    parsed = urlparse(url)
    if 'youtu.be' in parsed.netloc:
        video_id = parsed.path.lstrip('/')
        if video_id:
            qs = parsed.query
            base = f'https://www.youtube.com/watch?v={video_id}'
            if qs:
                return f'{base}&{qs}'
            return base
    elif 'youtube.com' in parsed.netloc and parsed.path.startswith('/shorts/'):
        # For YouTube Shorts, convert to watch format
        video_id = parsed.path.split('/')[2]  # /shorts/VIDEO_ID
        if video_id:
            return f'https://www.youtube.com/watch?v={video_id}'
    return url


def is_tiktok_url(url: str) -> bool:
    """
    Checks if URL is a TikTok link
    """
    try:
        clean_url = get_clean_url_for_tagging(url)
        parsed_url = urlparse(clean_url)
        return any(domain in parsed_url.netloc for domain in Config.TIKTOK_DOMAINS)
    except:
        return False


def extract_tiktok_profile(url: str) -> str:
    """
    Extract TikTok profile username from URL
    """
    # Looking for @username after the domain
    clean_url = get_clean_url_for_tagging(url)
    m = re.search(r'/@([\w\.\-_]+)', clean_url)
    if m:
        return m.group(1)
    return ''


def strip_range_from_url(url: str) -> str:
    """Strip range parameters from URL for cache normalization"""
    # Remove common range parameters
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)
    
    # Remove playlist range parameters
    range_params = ['index', 'start_radio', 'playnext']
    for param in range_params:
        if param in query_params:
            del query_params[param]
    
    # Rebuild URL
    new_query = urlencode(query_params, doseq=True)
    result = urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, ''))
    return result


def get_clean_playlist_url(url: str) -> str:
    """Returns the clean playlist URL for YouTube (https://www.youtube.com/playlist?list=...) or the original URL for other sites."""
    original_url = url
    m = re.search(r'list=([A-Za-z0-9_-]+)', url)
    if m:
        result = f"https://www.youtube.com/playlist?list={m.group(1)}"
        logger.info(f"get_clean_playlist_url: '{original_url}' -> '{result}'")
        return result
    logger.info(f"get_clean_playlist_url: '{original_url}' -> '{original_url}' (no list parameter)")
    return url


# --- New function to check if URL contains playlist range ---
def is_playlist_with_range(text: str) -> bool:
    """
    Checks if the text contains a playlist range pattern like *1*3, 1*1000, *5*10, or just * for full playlist.
    Returns True if a range is detected, False otherwise.
    """
    if not isinstance(text, str):
        return False

    # Look for patterns like *1*3, 1*1000, *5*10, or just * for full playlist
    range_pattern = r'\*[0-9]+\*[0-9]+|[0-9]+\*[0-9]+|\*'
    return bool(re.search(range_pattern, text))


def get_domain_from_url(url: str) -> str:
    """
    Extract domain from URL
    """
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        
        # Remove www. prefix
        if domain.startswith('www.'):
            domain = domain[4:]
        
        return domain
    except Exception:
        return ""


def extract_youtube_id(url: str) -> str:
    """
    Extract YouTube video ID from various URL formats
    """
    if not is_youtube_url(url):
        return ""
    
    try:
        parsed = urlparse(url)
        
        # From youtube.com/watch?v=ID
        if parsed.path == '/watch':
            params = parse_qs(parsed.query)
            if 'v' in params:
                return params['v'][0]
        
        # From youtu.be/ID
        elif 'youtu.be' in parsed.netloc:
            return parsed.path.lstrip('/')
        
        # From youtube.com/shorts/ID
        elif parsed.path.startswith('/shorts/'):
            return parsed.path.split('/shorts/')[-1]
        
        # From youtube.com/embed/ID
        elif parsed.path.startswith('/embed/'):
            return parsed.path.split('/embed/')[-1]
    
    except Exception:
        pass
    
    return ""


def normalize_playlist_url(url: str) -> str:
    """
    Normalize playlist URL for consistent processing
    """
    clean_url = get_clean_playlist_url(url)
    
    # Convert to canonical form if YouTube
    if is_youtube_url(clean_url):
        return youtube_to_long_url(clean_url)
    
    return clean_url


def is_supported_url(url: str) -> bool:
    """
    Check if URL is from a supported platform
    """
    supported_domains = [
        'youtube.com', 'youtu.be', 'tiktok.com', 'instagram.com',
        'twitter.com', 'x.com', 'vk.com', 'vkvideo.ru',
        'pornhub.com', 'twitch.tv', 'vimeo.com'
    ]
    
    domain = get_domain_from_url(url)
    
    return any(supported in domain for supported in supported_domains)


def get_platform_from_url(url: str) -> str:
    """
    Determine platform from URL
    """
    domain = get_domain_from_url(url)
    
    if 'youtube.com' in domain or 'youtu.be' in domain:
        return 'youtube'
    elif 'tiktok.com' in domain:
        return 'tiktok'
    elif 'instagram.com' in domain:
        return 'instagram'
    elif 'twitter.com' in domain or 'x.com' in domain:
        return 'twitter'
    elif 'vk.com' in domain or 'vkvideo.ru' in domain:
        return 'vk'
    elif 'pornhub.com' in domain:
        return 'pornhub'
    elif 'twitch.tv' in domain:
        return 'twitch'
    elif 'vimeo.com' in domain:
        return 'vimeo'
    else:
        return 'unknown'


# --- New function for cleaning URL only for tags ---
def get_clean_url_for_tagging(url: str) -> str:
    """
    Extracts the last (deepest nested) link from URL-wrappers.
    Used ONLY for generating tags.
    """
    if not isinstance(url, str):
        return ''
    last_http_pos = url.rfind('http://')
    last_https_pos = url.rfind('https://')

    start_of_real_url_pos = max(last_http_pos, last_https_pos)

    # If another http/https is found (not at the very beginning), this is the real link
    if start_of_real_url_pos > 0:
        return url[start_of_real_url_pos:]
    return url


def normalize_url_for_cache(url: str) -> str:
    """
    Normalizes URLs for caching based on a set of specific rules,
    removing all non-essential query parameters.
    For youtube.com (without www) leave as is, for youtu.be always without www and without query.
    """
    if not isinstance(url, str):
        return ''

    original_url = url
    url = extract_real_url_if_google(url)
    clean_url = get_clean_url_for_tagging(url)
    parsed = urlparse(clean_url)
    domain = parsed.netloc.lower()
    path = parsed.path
    query_params = parse_qs(parsed.query)

    # --- YouTube/youtu.be: always from www.youtube.com and youtu.be ---
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

    # Shorts and youtu.be: always strip all params
    if ("youtube.com" in domain and path.startswith('/shorts/')):
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (shorts)")
        return result
    if domain == 'youtu.be':
        # For youtu.be always remove query
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (youtu.be)")
        return result

    # /watch: only v
    if 'youtube.com' in domain and path == '/watch':
        v = None
        if 'v' in query_params:
            v = query_params['v'][0]
            # Fix: If v contains ? or &, only match up to those characters
            v = v.split('?')[0].split('&')[0]
        if v:
            new_query = urlencode({'v': v}, doseq=True)
            result = urlunparse((parsed.scheme, domain, path, '', new_query, ''))
            logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (watch)")
            return result
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (watch no v)")
        return result
    
    # /playlist: list only
    if 'youtube.com' in domain and path == '/playlist':
        if 'list' in query_params:
            new_query = urlencode({'list': query_params['list']}, doseq=True)
            result = urlunparse((parsed.scheme, domain, path, '', new_query, ''))
            logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (playlist)")
            return result
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (playlist no list)")
        return result
    
    # /embed: playlist only
    if 'youtube.com' in domain and path.startswith('/embed/'):
        allowed_params = {k: v for k, v in query_params.items() if k == 'playlist'}
        new_query = urlencode(allowed_params, doseq=True)
        result = urlunparse((parsed.scheme, domain, path, '', new_query, ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (embed)")
        return result
    
    # live: only way
    if 'youtube.com' in domain and (path.startswith('/live/') or path.endswith('/live')):
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (live)")
        return result
    
    # fallback for CLEAN_QUERY domains (suffix match)
    for clean_domain in getattr(Config, 'CLEAN_QUERY', []):
        if domain == clean_domain or domain.endswith('.' + clean_domain):
            result = urlunparse((parsed.scheme, domain, parsed.path, '', '', ''))
            logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (clean domain)")
            return result
    
    # For all other URLs, return them as they are
    result = urlunparse((parsed.scheme, domain, parsed.path, parsed.params, parsed.query, ''))
    logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (fallback)")
    return result


def get_quality_by_min_side(width: int, height: int) -> str:
    """
    Get quality string based on minimum side
    """
    min_side = min(width, height)
    if min_side <= 240:
        return "240p"
    elif min_side <= 360:
        return "360p"  
    elif min_side <= 480:
        return "480p"
    elif min_side <= 720:
        return "720p"
    elif min_side <= 1080:
        return "1080p"
    elif min_side <= 1440:
        return "1440p"
    else:
        return "2160p"


def get_real_height_for_quality(quality: str, width: int, height: int) -> int:
    """
    Get real height for quality based on aspect ratio
    """
    if not quality or not width or not height:
        return height
        
    target_heights = {
        "240p": 240,
        "360p": 360,
        "480p": 480,
        "720p": 720,
        "1080p": 1080,
        "1440p": 1440,
        "2160p": 2160
    }
    
    target_height = target_heights.get(quality)
    if not target_height:
        return height
        
    aspect_ratio = width / height
    return int(target_height * aspect_ratio) if aspect_ratio > 1 else target_height 


def get_url_hash(url: str) -> str:
    """Returns a hash of the URL for use as a cache key."""
    hash_result = hashlib.md5(url.encode()).hexdigest()
    logger.info(f"get_url_hash: '{url}' -> '{hash_result}'")
    return hash_result


def ceil_to_popular(h):
    """Round height to popular resolution"""
    if h <= 240:
        return 240
    elif h <= 360:
        return 360
    elif h <= 480:
        return 480
    elif h <= 720:
        return 720
    elif h <= 1080:
        return 1080
    elif h <= 1440:
        return 1440
    elif h <= 2160:
        return 2160
    else:
        return h


def db_child_by_path(db, path):
    """Navigate to database child by path"""
    try:
        parts = path.strip('/').split('/')
        ref = db
        for part in parts:
            if part:  # Skip empty parts
                ref = ref.child(part)
        return ref
    except Exception as e:
        logger.error(f"Error navigating to database path {path}: {e}")
        return None 