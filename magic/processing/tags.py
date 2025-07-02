"""Tags processing functions"""
import logging
import re
import os
import requests
import tldextract
from urllib.parse import urlparse
from config import Config

logger = logging.getLogger(__name__)

# --- global lists of domains and keywords ---
PORN_DOMAINS = set()
SUPPORTED_SITES = set()
PORN_KEYWORDS = set()

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

# --- Function for cleaning tags for Telegram ---
def clean_telegram_tag(tag: str) -> str:
    return '#' + re.sub(r'[^\w]', '', tag.lstrip('#'))

# --- a function for extracting the URL, the range and tags from the text ---
def extract_url_range_tags(text: str):
    # This function now always returns the full original download link
    if not isinstance(text, str):
        return None, 1, 1, None, [], '', None
    url_match = re.search(r'https?://[^\s\*#]+', text)
    if not url_match:
        return None, 1, 1, None, [], '', None
    url = url_match.group(0)

    after_url = text[url_match.end():]
    # Range
    range_match = re.match(r'\*([0-9]+)\*([0-9]+)', after_url)
    if range_match:
        video_start_with = int(range_match.group(1))
        video_end_with = int(range_match.group(2))
        after_range = after_url[range_match.end():]
    else:
        video_start_with = 1
        video_end_with = 1
        after_range = after_url
    playlist_name = None
    playlist_match = re.match(r'\*([^\s\*#]+)', after_range)
    if playlist_match:
        playlist_name = playlist_match.group(1)
        after_playlist = after_range[playlist_match.end():]
    else:
        after_playlist = after_range
    tags = []
    tags_text = ''
    error_tag = None
    error_tag_example = None
    tag_part = after_playlist.strip()
    if tag_part:
        for raw in re.finditer(r'#([^#\s]+)', tag_part):
            tag = raw.group(1)
            # We check that the tag consists only of the permitted characters
            if not re.fullmatch(r'[\w\d_]+', tag, re.UNICODE):
                error_tag = tag
                # For example, show the user how the corrected tag would look like
                example = re.sub(r'[^\w\d_]', '_', tag, flags=re.UNICODE)
                error_tag_example = f'#{example}'
                break  # Interrupt the check after the first error
            tags.append(f'#{tag}')
        # We form Tags_text with spaces between tags
        tags_text = ' '.join(tags)
    # Return the motorcade with an error if it was found
    return url, video_start_with, video_end_with, playlist_name, tags, tags_text, (error_tag, error_tag_example) if error_tag else None

def save_user_tags(user_id, tags):
    if not tags:
        return
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    tags_file = os.path.join(user_dir, "tags.txt")
    # We read already saved tags
    existing = set()
    if os.path.exists(tags_file):
        with open(tags_file, "r", encoding="utf-8") as f:
            for line in f:
                tag = line.strip()
                if tag:
                    existing.add(tag.lower())
    # Add new tags (without registering and without repetitions)
    new_tags = [t for t in tags if t and t.lower() not in existing]
    if new_tags:
        with open(tags_file, "a", encoding="utf-8") as f:
            for tag in new_tags:
                f.write(tag + "\n")

def extract_youtube_id(url: str) -> str:
    """
    It extracts YouTube Video ID from different link formats.
    """
    patterns = [
        r"youtu\.be/([^?&/]+)",
        r"v=([^?&/]+)",
        r"embed/([^?&/]+)",
        r"youtube\.com/watch\?[^ ]*v=([^?&/]+)"
    ]
    for pat in patterns:
        m = re.search(pat, url)
        if m:
            return m.group(1)
    raise ValueError("Failed to extract YouTube ID")

def download_thumbnail(video_id: str, dest: str) -> None:
    """
    Trying to download maxressdefault.jpg, then hqdefault.jpg.
    """
    base = f"https://img.youtube.com/vi/{video_id}"
    for name in ("maxresdefault.jpg", "hqdefault.jpg"):
        r = requests.get(f"{base}/{name}", timeout=10)
        if r.status_code == 200 and len(r.content) <= 200 * 1024:
            with open(dest, "wb") as f:
                f.write(r.content)
            return
    raise RuntimeError("Failed to download thumbnail or it is too big")

# --- global lists of domains and keywords ---
PORN_DOMAINS = set()
SUPPORTED_SITES = set()
PORN_KEYWORDS = set()

# --- loading lists at start ---
def load_domain_lists():
    global PORN_DOMAINS, SUPPORTED_SITES, PORN_KEYWORDS
    try:
        with open(Config.PORN_DOMAINS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            PORN_DOMAINS = set(line.strip().lower() for line in f if line.strip())
        logger.info(f"Loaded {len(PORN_DOMAINS)} domains from {Config.PORN_DOMAINS_FILE}. Example: {list(PORN_DOMAINS)[:5]}")
    except Exception as e:
        logger.error(f"Failed to load {Config.PORN_DOMAINS_FILE}: {e}")
        PORN_DOMAINS = set()
    try:
        with open(Config.PORN_KEYWORDS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            PORN_KEYWORDS = set(line.strip().lower() for line in f if line.strip())
        logger.info(f"Loaded {len(PORN_KEYWORDS)} keywords from {Config.PORN_KEYWORDS_FILE}. Example: {list(PORN_KEYWORDS)[:5]}")
    except Exception as e:
        logger.error(f"Failed to load {Config.PORN_KEYWORDS_FILE}: {e}")
        PORN_KEYWORDS = set()
    try:
        with open(Config.SUPPORTED_SITES_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            SUPPORTED_SITES = set(line.strip().lower() for line in f if line.strip())
        logger.info(f"Loaded {len(SUPPORTED_SITES)} supported sites from {Config.SUPPORTED_SITES_FILE}. Example: {list(SUPPORTED_SITES)[:5]}")
    except Exception as e:
        logger.error(f"Failed to load {Config.SUPPORTED_SITES_FILE}: {e}")
        SUPPORTED_SITES = set()

load_domain_lists()

# --- an auxiliary function for extracting a domain ---
def extract_domain_parts(url):
    try:
        ext = tldextract.extract(url)
        # We collect the domain: Domain.suffix (for example, xvideos.com)
        if ext.domain and ext.suffix:
            full_domain = f"{ext.domain}.{ext.suffix}".lower()
            subdomain = ext.subdomain.lower() if ext.subdomain else ''
            # We get all the suffixes: xvideos.com, b.xvideos.com, a.b.xvideos.com
            parts = [full_domain]
            if subdomain:
                sub_parts = subdomain.split('.')
                for i in range(len(sub_parts)):
                    parts.append('.'.join(sub_parts[i:] + [full_domain]))
            return parts, ext.domain.lower()
        elif ext.domain:
            return [ext.domain.lower()], ext.domain.lower()
        else:
            return [url.lower()], url.lower()
    except Exception:
        # Fallback for URLs without a clear domain, e.g., "localhost"
        parsed = urlparse(url)
        if parsed.netloc:
             return [parsed.netloc.lower()], parsed.netloc.lower()
        return [url.lower()], url.lower()


    auto_tags = [t for t in auto_tags if t.lower() not in user_tags_lower]
    return auto_tags

# --- White list of domains that are not considered porn ---
# Now we take from config.py

def is_porn_domain(domain_parts):
    # If any suffix domain on a white list is not porn
    for dom in domain_parts:
        if dom in Config.WHITELIST:
            return False
    # If any suffix domain in the list of porn is porn
    for dom in domain_parts:
        if dom in PORN_DOMAINS:
            return True
    return False

# --- a new function for checking for porn ---
def is_porn(url, title, description, caption=None):
    """
    Checks content for pornography by domain and keywords (substring search) in title, description and caption.
    If the domain or subdomain is found in WHITELIST, it immediately returns False.
    """
    clean_url = get_clean_url_for_tagging(url)
    domain_parts, _ = extract_domain_parts(clean_url)
    #First, check WHITELIST
    for dom in domain_parts:
        if dom in Config.WHITELIST:
            logger.info(f"is_porn: domain in WHITELIST: {dom}")
            return False
    if is_porn_domain(domain_parts):
        logger.info(f"is_porn: domain match: {domain_parts}")
        return True
    title_lower = title.lower() if title else ""
    description_lower = description.lower() if description else ""
    caption_lower = caption.lower() if caption else ""
    logger.debug(f"is_porn check for url: {url}")
    logger.debug(f"is_porn title: '{title_lower}'")
    logger.debug(f"is_porn description: '{description_lower}'")
    logger.debug(f"is_porn caption: '{caption_lower}'")
    logger.debug(f"is_porn keywords being checked: {PORN_KEYWORDS}")
    if not title_lower and not description_lower and not caption_lower:
        logger.info("is_porn: all fields empty")
        return False
    for keyword in PORN_KEYWORDS:
        if not keyword:
            continue
        # Split text into words and check for exact word matches
        title_words = title_lower.split()
        description_words = description_lower.split()
        caption_words = caption_lower.split()
        
        if (keyword in title_words or keyword in description_words or keyword in caption_words):
            logger.info(f"is_porn: found match: {keyword}")
            return True
    logger.info("is_porn: no matches found")
    return False

def sanitize_autotag(tag: str) -> str:
    # Leave only letters (any language), numbers and _
    return '#' + re.sub(r'[^\w\d_]', '_', tag.lstrip('#'), flags=re.UNICODE)

def generate_final_tags(url, user_tags, info_dict):
    """Tags now include #porn if found by title, description or caption."""
    final_tags = []
    seen = set()
    # 1. Custom tags
    for tag in user_tags:
        tag_l = tag.lower()
        if tag_l not in seen:
            final_tags.append(tag)
            seen.add(tag_l)
    # 2. Auto-tags (no duplicates)
    auto_tags = get_auto_tags(url, final_tags)
    for tag in auto_tags:
        tag_l = tag.lower()
        if tag_l not in seen:
            final_tags.append(tag)
            seen.add(tag_l)
    # 3. Profile/channel tags (tiktok/youtube)
    if is_tiktok_url(url):
        tiktok_profile = extract_tiktok_profile(url)
        if tiktok_profile:
            tiktok_tag = sanitize_autotag(tiktok_profile)
            if tiktok_tag.lower() not in seen:
                final_tags.append(tiktok_tag)
                seen.add(tiktok_tag.lower())
        if '#tiktok' not in seen:
            final_tags.append('#tiktok')
            seen.add('#tiktok')
    clean_url_for_check = get_clean_url_for_tagging(url)
    if ("youtube.com" in clean_url_for_check or "youtu.be" in clean_url_for_check) and info_dict:
        channel_name = info_dict.get("channel") or info_dict.get("uploader")
        if channel_name:
            channel_tag = sanitize_autotag(channel_name)
            if channel_tag.lower() not in seen:
                final_tags.append(channel_tag)
                seen.add(channel_tag.lower())
    # 4. #porn if defined by title, description or caption
    video_title = info_dict.get("title")
    video_description = info_dict.get("description")
    video_caption = info_dict.get("caption") if info_dict else None
    if is_porn(url, video_title, video_description, video_caption):
        if '#porn' not in seen:
            final_tags.append('#porn')
            seen.add('#porn')
    result = ' '.join(final_tags)
    logger.info(f"Generated final tags for '{info_dict.get('title', 'N/A')}': \"{result}\"")
    return result


