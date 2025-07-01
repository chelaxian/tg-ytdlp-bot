"""
Tags processing system
"""
import os
import re
from typing import List, Set, Tuple


def clean_telegram_tag(tag: str) -> str:
    """Clean tag for Telegram compatibility"""
    return re.sub(r'[^\w]', '', tag)


def extract_url_range_tags(text: str):
    """
    Extract URL, range, and tags from user input text
    
    This function now always returns the full original download link
    without modifying playlist ranges, ensuring compatibility with yt-dlp
    """
    if not text:
        return None, None, None, None, None, None, None
    
    text = text.strip()
    
    # Look for range pattern *start*end or *start*end*playlist_name
    range_pattern = r'\*(\d+)\*(\d+)(?:\*([^#\s]+))?'
    range_match = re.search(range_pattern, text)
    
    if range_match:
        start_index = int(range_match.group(1))
        end_index = int(range_match.group(2))
        playlist_name = range_match.group(3) if range_match.group(3) else None
        
        # Extract URL (everything before the range pattern)
        url = text[:range_match.start()].strip()
        
        # Extract tags (everything after the range pattern)
        remaining_text = text[range_match.end():].strip()
        
        # Look for tags starting with #
        tag_pattern = r'#([^#\s]+)'
        tags = re.findall(tag_pattern, remaining_text)
        
        # The original download URL includes the range
        original_download_url = url + range_match.group(0)
        
        return (url, start_index, end_index, playlist_name, tags, original_download_url, range_match.group(0))
    else:
        # No range found, look for tags
        tag_pattern = r'#([^#\s]+)'
        tags = re.findall(tag_pattern, text)
        
        if tags:
            # Remove tags from URL
            url = re.sub(r'#[^#\s]+', '', text).strip()
        else:
            url = text
        
        return (url, None, None, None, tags, url, None)


def get_clean_url_for_tagging(url: str) -> str:
    """
    Clean URL for tagging by removing tracking parameters but keeping essential ones
    """
    from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
    
    if not url:
        return url
    
    try:
        parsed = urlparse(url)
        
        # For YouTube, keep only essential parameters
        if 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc:
            query_params = parse_qs(parsed.query)
            
            # Keep only essential YouTube parameters
            essential_params = {}
            for param in ['v', 'list', 'index', 't', 'start']:
                if param in query_params:
                    essential_params[param] = query_params[param]
            
            new_query = urlencode(essential_params, doseq=True)
            return urlunparse((parsed.scheme, parsed.netloc, parsed.path, 
                             parsed.params, new_query, ''))
        
        # For other sites, return as is
        return url
        
    except Exception:
        return url


def load_domain_lists():
    """Load domain and keyword lists for auto-tagging"""
    porn_domains = set()
    porn_keywords = set()
    
    try:
        # Load porn domains
        if os.path.exists("porn_domains.txt"):
            with open("porn_domains.txt", "r", encoding="utf-8") as f:
                porn_domains = {line.strip().lower() for line in f if line.strip()}
        
        # Load porn keywords  
        if os.path.exists("porn_keywords.txt"):
            with open("porn_keywords.txt", "r", encoding="utf-8") as f:
                porn_keywords = {line.strip().lower() for line in f if line.strip()}
                
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error loading domain/keyword lists: {e}")
    
    return porn_domains, porn_keywords


def extract_domain_parts(url):
    """
    Extract domain parts from URL for classification
    """
    from urllib.parse import urlparse
    
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        
        # Remove www. prefix
        if domain.startswith('www.'):
            domain = domain[4:]
        
        # Split by dots to get parts
        parts = domain.split('.')
        
        return parts, domain
        
    except Exception:
        return [], ""


def is_porn_domain(domain_parts):
    """
    Check if domain parts indicate adult content
    
    Args:
        domain_parts: List of domain parts from URL
        
    Returns:
        bool: True if any suffix domain on a whitelist is not porn
    """
    from config import Config
    
    porn_domains, _ = load_domain_lists()
    
    # Check against whitelist first
    for suffix_len in range(1, min(4, len(domain_parts) + 1)):
        suffix_domain = '.'.join(domain_parts[-suffix_len:])
        if suffix_domain in Config.WHITELIST:
            return False
    
    # Check against porn domains
    for suffix_len in range(1, min(4, len(domain_parts) + 1)):
        suffix_domain = '.'.join(domain_parts[-suffix_len:])
        if suffix_domain in porn_domains:
            return True
    
    return False


def is_porn(url, title, description, caption=None):
    """
    Determine if content is adult/porn based on URL, title, and description
    """
    import logging
    logger = logging.getLogger(__name__)
    
    try:
        domain_parts, domain = extract_domain_parts(url)
        
        # Check domain
        if is_porn_domain(domain_parts):
            logger.info(f"Classified as porn due to domain: {domain}")
            return True
        
        # Check keywords in title, description, and caption
        _, porn_keywords = load_domain_lists()
        
        text_to_check = []
        if title:
            text_to_check.append(title.lower())
        if description:
            text_to_check.append(description.lower())
        if caption:
            text_to_check.append(caption.lower())
        
        combined_text = ' '.join(text_to_check)
        
        for keyword in porn_keywords:
            if keyword in combined_text:
                logger.info(f"Classified as porn due to keyword: {keyword}")
                return True
        
        return False
        
    except Exception as e:
        logger.error(f"Error in porn detection: {e}")
        return False


def get_auto_tags(url, user_tags):
    """
    Generate automatic tags based on URL and content
    """
    from urllib.parse import urlparse
    
    auto_tags = []
    
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        
        # Remove www. prefix
        if domain.startswith('www.'):
            domain = domain[4:]
        
        # Platform-specific tags
        if 'youtube.com' in domain or 'youtu.be' in domain:
            auto_tags.append('youtube')
        elif 'tiktok.com' in domain:
            auto_tags.append('tiktok')
        elif 'instagram.com' in domain:
            auto_tags.append('instagram')
        elif 'twitter.com' in domain or 'x.com' in domain:
            auto_tags.append('twitter')
        elif 'pornhub.com' in domain:
            auto_tags.append('adult')
        elif 'vk.com' in domain or 'vkvideo.ru' in domain:
            auto_tags.append('vk')
        elif 'twitch.tv' in domain:
            auto_tags.append('twitch')
        elif 'vimeo.com' in domain:
            auto_tags.append('vimeo')
        
        # Add domain as tag if not already covered
        domain_tag = domain.split('.')[0]
        if domain_tag not in auto_tags and len(domain_tag) > 2:
            auto_tags.append(domain_tag)
        
    except Exception:
        pass
    
    # Combine with user tags
    all_tags = list(user_tags) + auto_tags
    
    # Remove duplicates while preserving order
    seen = set()
    final_tags = []
    for tag in all_tags:
        tag_clean = clean_telegram_tag(tag)
        if tag_clean and tag_clean not in seen:
            seen.add(tag_clean)
            final_tags.append(tag_clean)
    
    return final_tags


def sanitize_autotag(tag: str) -> str:
    """
    Sanitize autotag to contain only safe characters
    Leave only letters (any language), numbers and _
    """
    import re
    return re.sub(r'[^\w_]', '', tag, flags=re.UNICODE)


def generate_final_tags(url, user_tags, info_dict):
    """
    Generate final tags combining user tags, auto tags, and metadata
    
    Args:
        url: Video URL
        user_tags: User-provided tags
        info_dict: Video metadata from yt-dlp
        
    Returns:
        Formatted tags string for caption
    """
    # Get base auto tags
    auto_tags = get_auto_tags(url, user_tags)
    
    # Add metadata-based tags
    metadata_tags = []
    
    try:
        # Add uploader tag if available
        uploader = info_dict.get('uploader') or info_dict.get('channel')
        if uploader:
            uploader_tag = sanitize_autotag(uploader)
            if len(uploader_tag) > 2 and len(uploader_tag) < 20:
                metadata_tags.append(uploader_tag)
        
        # Add duration-based tag
        duration = info_dict.get('duration')
        if duration:
            if duration < 60:
                metadata_tags.append('short')
            elif duration > 3600:
                metadata_tags.append('long')
        
        # Add quality tag
        height = info_dict.get('height')
        if height:
            if height >= 2160:
                metadata_tags.append('4k')
            elif height >= 1080:
                metadata_tags.append('hd')
            elif height >= 720:
                metadata_tags.append('720p')
    
    except Exception:
        pass
    
    # Combine all tags
    all_tags = auto_tags + metadata_tags
    
    # Remove duplicates and format
    final_tags = []
    seen = set()
    
    for tag in all_tags:
        tag_clean = clean_telegram_tag(tag.lower())
        if tag_clean and tag_clean not in seen and len(tag_clean) > 1:
            seen.add(tag_clean)
            final_tags.append(f"#{tag_clean}")
    
    # Limit to reasonable number of tags
    final_tags = final_tags[:10]
    
    return ' '.join(final_tags) if final_tags else ''


def save_user_tags(user_id, tags):
    """
    Save user tags to file
    """
    import os
    from magic.utils.filesystem import create_directory
    
    try:
        user_dir = os.path.join("users", str(user_id))
        create_directory(user_dir)
        
        tags_file = os.path.join(user_dir, "tags.txt")
        
        # Load existing tags
        existing_tags = set()
        if os.path.exists(tags_file):
            with open(tags_file, "r", encoding="utf-8") as f:
                existing_tags = {line.strip() for line in f if line.strip()}
        
        # Add new tags
        for tag in tags:
            if tag and len(tag) > 1:
                existing_tags.add(clean_telegram_tag(tag))
        
        # Save updated tags
        with open(tags_file, "w", encoding="utf-8") as f:
            for tag in sorted(existing_tags):
                f.write(f"{tag}\n")
                
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error saving user tags: {e}")


def get_user_tags(user_id):
    """
    Get user's saved tags
    """
    import os
    
    try:
        user_dir = os.path.join("users", str(user_id))
        tags_file = os.path.join(user_dir, "tags.txt")
        
        if os.path.exists(tags_file):
            with open(tags_file, "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip()]
        
        return []
        
    except Exception:
        return [] 