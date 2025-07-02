"""
URL parsing and validation functions
"""
import re
import logging
from urllib.parse import urlparse, parse_qs, urlunparse, unquote, urlencode
from config import Config

logger = logging.getLogger(__name__)


def extract_real_url_if_google(url: str) -> str:
    """
    If this is a Google link (google.com/url?q=...), then we extract the real URL.
    Otherwise return as is.
    """
    if 'google.com/url' in url and 'q=' in url:
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)
        if 'q' in query_params:
            real_url = query_params['q'][0]
            return unquote(real_url)
    return url


def is_youtube_url(url: str) -> bool:
    """Checks if URL is a YouTube link"""
    clean_url = get_clean_url_for_tagging(url)
    return 'youtube.com' in clean_url or 'youtu.be' in clean_url


def youtube_to_short_url(url: str) -> str:
    """
    Converts a long YouTube URL to youtu.be format
    """
    if not is_youtube_url(url):
        return url
    
    try:
        parsed = urlparse(url)
        
        # From youtube.com/watch?v=ID
        if parsed.path == '/watch':
            params = parse_qs(parsed.query)
            if 'v' in params:
                video_id = params['v'][0]
                return f"https://youtu.be/{video_id}"
        
        # From youtube.com/shorts/ID
        elif parsed.path.startswith('/shorts/'):
            video_id = parsed.path.split('/shorts/')[-1]
            return f"https://youtu.be/{video_id}"
        
        # Already short URL
        elif 'youtu.be' in parsed.netloc:
            return url
    
    except Exception:
        pass
    
    return url


def youtube_to_long_url(url: str) -> str:
    """
    Converts a youtu.be URL to full youtube.com format
    """
    if not is_youtube_url(url):
        return url
    
    try:
        parsed = urlparse(url)
        
        # From youtu.be/ID
        if 'youtu.be' in parsed.netloc:
            video_id = parsed.path.lstrip('/')
            return f"https://www.youtube.com/watch?v={video_id}"
        
        # Already long URL
        else:
            return url
    
    except Exception:
        pass
    
    return url


def is_tiktok_url(url: str) -> bool:
    """Checks if URL is a TikTok link"""
    try:
        clean_url = get_clean_url_for_tagging(url)
        parsed = urlparse(clean_url)
        domain = parsed.netloc.lower()
        return 'tiktok.com' in domain
    except Exception:
        return False


def extract_tiktok_profile(url: str) -> str:
    # Looking for @username after the domain
    if not is_tiktok_url(url):
        return ""
    try:
        clean_url = get_clean_url_for_tagging(url)
        match = re.search(r'@([a-zA-Z0-9_.]+)', clean_url)
        return match.group(1) if match else ""
    except Exception:
        return ""


def strip_range_from_url(url: str) -> str:
    """Remove range specifications from URL"""
    # Remove patterns like *1*10, 5*15, etc.
    clean_url = re.sub(r'\*\d+\*\d+|\d+\*\d+|\*', '', url)
    return clean_url.strip()


def get_clean_playlist_url(url: str) -> str:
    """Extract clean playlist URL without range specifications"""
    return strip_range_from_url(url)


def is_playlist_with_range(text: str) -> bool:
    """
    Check if text contains playlist range patterns like *1*10, 5*15, etc.
    """
    # Look for patterns like *1*3, 1*1000, *5*10, or just * for full playlist
    range_pattern = r'\*[0-9]+\*[0-9]+|[0-9]+\*[0-9]+|\*'
    return bool(re.search(range_pattern, text))








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

    # For all other URLs, strip everything and leave only basic structure
    result = urlunparse((parsed.scheme, domain, path, '', '', ''))
    logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (default)")
    return result








