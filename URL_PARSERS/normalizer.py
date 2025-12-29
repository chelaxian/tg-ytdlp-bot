import re
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode, unquote
from URL_PARSERS.tiktok import get_clean_url_for_tagging
from HELPERS.logger import logger
from CONFIG.config import Config

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

    # Безопасная функция для проверки домена
    def _is_domain_match(hostname: str, domain: str) -> bool:
        if not hostname or not domain:
            return False
        hostname_lower = hostname.lower().strip()
        domain_lower = domain.lower().strip()
        if ':' in hostname_lower:
            hostname_lower = hostname_lower.split(':')[0]
        return hostname_lower == domain_lower or hostname_lower.endswith('.' + domain_lower)
    
    # TikTok: always strip all params, keep only path
    if _is_domain_match(domain, 'tiktok.com'):
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (tiktok)")
        return result

    # Shorts and youtu.be: always strip all params
    if _is_domain_match(domain, 'youtube.com') and path.startswith('/shorts/'):
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (shorts)")
        return result
    if domain == 'youtu.be':
        # For youtu.be always remove query
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (youtu.be)")
        return result

    # /watch: only v
    if _is_domain_match(domain, 'youtube.com') and path == '/watch':
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
    if _is_domain_match(domain, 'youtube.com') and path == '/playlist':
        if 'list' in query_params:
            new_query = urlencode({'list': query_params['list']}, doseq=True)
            result = urlunparse((parsed.scheme, domain, path, '', new_query, ''))
            logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (playlist)")
            return result
        result = urlunparse((parsed.scheme, domain, path, '', '', ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (playlist no list)")
        return result
    # /embed: playlist only
    if _is_domain_match(domain, 'youtube.com') and path.startswith('/embed/'):
        allowed_params = {k: v for k, v in query_params.items() if k == 'playlist'}
        new_query = urlencode(allowed_params, doseq=True)
        result = urlunparse((parsed.scheme, domain, path, '', new_query, ''))
        logger.info(f"normalize_url_for_cache: '{original_url}' -> '{result}' (embed)")
        return result
    # live: only way
    if _is_domain_match(domain, 'youtube.com') and (path.startswith('/live/') or path.endswith('/live')):
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


def extract_real_url_if_google(url: str) -> str:
    """
    If the link is a redirect via Google, returns the target link.
    Otherwise, returns the original link.
    """
    parsed = urlparse(url)
    # Безопасная проверка домена
    netloc_lower = (parsed.netloc or '').lower()
    is_google = netloc_lower in ('google.com', 'www.google.com') or netloc_lower.endswith('.google.com')
    if is_google and parsed.path.startswith('/url'):
        qs = parse_qs(parsed.query)
        # Google may use either ?q= or ?url=
        real_url = qs.get('q') or qs.get('url')
        if real_url:
            # Take the first variant, decode if needed
            return unquote(real_url[0])
    return url



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



def strip_range_from_url(url: str) -> str:
    """Removes a range of the form *1*3 or *1*10000 from the end of the URL."""
    original_url = url
    result = re.sub(r'\*\d+\*\d+$', '', url)
    if original_url != result:
        logger.info(f"strip_range_from_url: '{original_url}' -> '{result}'")
    return result

