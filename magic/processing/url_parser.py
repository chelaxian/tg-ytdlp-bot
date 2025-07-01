"""
URL parsing and processing utilities
"""
import re
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from typing import Optional


def extract_real_url_if_google(url: str) -> str:
    """
    Extract the real URL from Google redirect URLs
    """
    if "google.com/url" in url:
        try:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            if 'url' in params:
                return params['url'][0]
        except Exception:
            pass
    return url


def is_youtube_url(url: str) -> bool:
    """Check if URL is a YouTube URL"""
    return any(domain in url.lower() for domain in ['youtube.com', 'youtu.be', 'm.youtube.com'])


def youtube_to_short_url(url: str) -> str:
    """
    Convert YouTube URL to short youtu.be format
    """
    if not is_youtube_url(url):
        return url
    
    try:
        parsed = urlparse(url)
        
        # If already youtu.be
        if 'youtu.be' in parsed.netloc:
            return url
        
        # Extract video ID from various YouTube URL formats
        if parsed.path == '/watch':
            params = parse_qs(parsed.query)
            if 'v' in params:
                video_id = params['v'][0]
                return f"https://youtu.be/{video_id}"
        elif parsed.path.startswith('/shorts/'):
            video_id = parsed.path.split('/shorts/')[-1]
            return f"https://youtu.be/{video_id}"
        elif parsed.path.startswith('/embed/'):
            video_id = parsed.path.split('/embed/')[-1]
            return f"https://youtu.be/{video_id}"
    
    except Exception:
        pass
    
    return url


def youtube_to_long_url(url: str) -> str:
    """
    Convert YouTube URL to long youtube.com format
    """
    if not is_youtube_url(url):
        return url
    
    try:
        parsed = urlparse(url)
        
        # If already youtube.com/watch
        if 'youtube.com' in parsed.netloc and parsed.path == '/watch':
            return url
        
        # Convert from youtu.be
        if 'youtu.be' in parsed.netloc:
            video_id = parsed.path.lstrip('/')
            return f"https://www.youtube.com/watch?v={video_id}"
        
        # Convert from shorts
        if parsed.path.startswith('/shorts/'):
            video_id = parsed.path.split('/shorts/')[-1]
            return f"https://www.youtube.com/watch?v={video_id}"
        
        # Convert from embed
        if parsed.path.startswith('/embed/'):
            video_id = parsed.path.split('/embed/')[-1]
            return f"https://www.youtube.com/watch?v={video_id}"
    
    except Exception:
        pass
    
    return url


def is_tiktok_url(url: str) -> bool:
    """Check if URL is a TikTok URL"""
    return 'tiktok.com' in url.lower()


def extract_tiktok_profile(url: str) -> str:
    """
    Extract TikTok profile username from URL
    """
    # Looking for @username after the domain
    match = re.search(r'tiktok\.com/@([^/?#]+)', url)
    if match:
        return f"@{match.group(1)}"
    return ""


def strip_range_from_url(url: str) -> str:
    """
    Remove range parameters (*start*end) from URL
    """
    # Remove patterns like *1*5 or *1*5*name from URL
    pattern = r'\*\d+\*\d+(?:\*[^#\s]*)?'
    return re.sub(pattern, '', url).strip()


def get_clean_playlist_url(url: str) -> str:
    """
    Clean playlist URL by removing range and tags
    """
    # First strip range
    clean_url = strip_range_from_url(url)
    
    # Then remove hashtags
    clean_url = re.sub(r'#[^#\s]*', '', clean_url).strip()
    
    return clean_url


def is_playlist_with_range(text: str) -> bool:
    """
    Check if text contains playlist with range pattern (*start*end)
    """
    # Looking for *number*number pattern
    pattern = r'\*\d+\*\d+'
    return bool(re.search(pattern, text))


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