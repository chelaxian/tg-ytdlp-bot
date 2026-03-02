import re
import os
import tldextract
from urllib.parse import urlparse
# from CONFIG.config import Config  # Unused import
from URL_PARSERS.tiktok import is_tiktok_url, extract_tiktok_profile, get_clean_url_for_tagging
from HELPERS.filesystem_hlp import create_directory
from HELPERS.porn import is_porn_domain, extract_domain_parts, SUPPORTED_SITES, unwrap_redirect_url
from HELPERS.logger import logger

def sanitize_autotag(tag: str) -> str:
    # Leave only letters (any language), numbers and _
    return '#' + re.sub(r'[^\w\d_]', '_', tag.lstrip('#'), flags=re.UNICODE)

def sanitize_uid_for_telegram(uid: str) -> str:
    """Очищает UID для использования в Telegram тегах"""
    if not uid:
        return uid
    
    # Убираем символы @
    uid = uid.replace('@', '')
    
    # Заменяем пробелы на подчеркивания
    uid = uid.replace(' ', '_')
    
    # Заменяем точки на подчеркивания
    uid = uid.replace('.', '_')
    
    # Заменяем недопустимые символы на подчеркивания
    # В Telegram тегах разрешены: буквы, цифры, подчеркивания
    uid = re.sub(r'[^\w\d_]', '_', uid, flags=re.UNICODE)
    
    # Убираем множественные подчеркивания
    uid = re.sub(r'_+', '_', uid)
    
    # Убираем подчеркивания в начале и конце
    uid = uid.strip('_')
    
    return uid

def _extract_uids_from_info(info_dict):
    """Внутренняя функция для извлечения всех UID из метаданных"""
    if not info_dict:
        return []
    
    # Пробуем различные поля для UID в порядке приоритета
    # Для Instagram и TikTok приоритет uploader_id и uploader
    uid_fields = [
        'uploader_id',  # Instagram, TikTok - постоянный для автора
        'uploader',     # TikTok, общий - постоянный для автора
        #'id',           # YouTube, общий - уникальный для каждого поста
        #'display_id',   # YouTube - уникальный для каждого поста
        #'video_id',     # TikTok, общий - уникальный для каждого поста
        #'media_id',     # Instagram - уникальный для каждого поста
        #'post_id',      # Gallery-dl - уникальный для каждого поста
        #'item_id',      # Gallery-dl - уникальный для каждого поста
        #'uid'           # Общий - может быть уникальным для каждого поста
    ]
    
    # Собираем все найденные UID, избегая дублей
    found_uids = []
    seen_uids = set()
    
    for field in uid_fields:
        uid = info_dict.get(field)
        if uid and str(uid).strip():
            uid_str = str(uid).strip()
            # Очищаем UID для Telegram тегов
            cleaned_uid = sanitize_uid_for_telegram(uid_str)
            if cleaned_uid and cleaned_uid not in seen_uids:
                found_uids.append(cleaned_uid)
                seen_uids.add(cleaned_uid)
    
    # YouTube ID из URL не добавляем, так как он уникален для каждого видео, а не для автора
    
    return found_uids

def extract_uid_from_info(info_dict):
    """Извлекает первый UID из метаданных yt-dlp или gallery-dl (для обратной совместимости)"""
    uids = _extract_uids_from_info(info_dict)
    return uids[0] if uids else None

def extract_all_uids_from_info(info_dict):
    """Извлекает ВСЕ UID из метаданных yt-dlp или gallery-dl"""
    return _extract_uids_from_info(info_dict)

def generate_final_tags(url, user_tags, info_dict):
    """Tags now include #nsfw if found by title, description or caption."""
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
    # Безопасная функция для проверки домена
    def _is_domain_match(hostname: str, domain: str) -> bool:
        if not hostname or not domain:
            return False
        hostname_lower = hostname.lower().strip()
        domain_lower = domain.lower().strip()
        if ':' in hostname_lower:
            hostname_lower = hostname_lower.split(':')[0]
        return hostname_lower == domain_lower or hostname_lower.endswith('.' + domain_lower)
    
    # Unwrap redirects before any domain-based checks
    clean_url_for_check = get_clean_url_for_tagging(unwrap_redirect_url(url))
    try:
        from urllib.parse import urlparse
        parsed_check = urlparse(clean_url_for_check)
        check_hostname = (parsed_check.hostname or '').lower()
        is_youtube = _is_domain_match(check_hostname, 'youtube.com') or _is_domain_match(check_hostname, 'youtu.be')
    except Exception:
        is_youtube = False
    
    if is_youtube and info_dict:
        channel_name = info_dict.get("channel") or info_dict.get("uploader")
        if channel_name:
            channel_tag = sanitize_autotag(channel_name)
            if channel_tag.lower() not in seen:
                final_tags.append(channel_tag)
                seen.add(channel_tag.lower())
    # 4. UID tags (все найденные UID)
    all_uids = extract_all_uids_from_info(info_dict)
    for uid in all_uids:
        uid_tag = f"#{uid}"
        if uid_tag.lower() not in seen:
            final_tags.append(uid_tag)
            seen.add(uid_tag.lower())
    # 5. #nsfw if defined by title, description, caption, tags or uploader/author (keywords)
    video_title = info_dict.get("title") if info_dict else None
    video_description = info_dict.get("description") if info_dict else None
    video_caption = info_dict.get("caption") if info_dict else None
    video_uploader = None
    if info_dict:
        uploader_parts = [info_dict.get("uploader"), info_dict.get("channel"), info_dict.get("creator"), info_dict.get("artist")]
        video_uploader = " ".join(str(p).strip() for p in uploader_parts if p and str(p).strip()) or None
    # Get tags from info_dict (for tags with underscores)
    video_tags = info_dict.get("tags") if info_dict else None
    # Also check already collected tags (user tags + auto tags)
    existing_tags_text = ' '.join(final_tags) if final_tags else None
    try:
        from HELPERS.porn import is_porn
        # Combine tags from info_dict and already collected tags
        all_tags = None
        if video_tags:
            if isinstance(video_tags, list):
                all_tags = ' '.join(str(t) for t in video_tags)
            else:
                all_tags = str(video_tags)
        if existing_tags_text:
            all_tags = f"{all_tags} {existing_tags_text}" if all_tags else existing_tags_text
        if is_porn(url, video_title, video_description, video_caption, tags=all_tags, uploader=video_uploader):
            if '#nsfw' not in seen:
                final_tags.append('#nsfw')
                seen.add('#nsfw')
    except (ImportError, AttributeError) as e:
        logger.warning("Error checking NSFW content: %s", e)
    result = ' '.join(final_tags)
    # Check if info_dict is None before accessing it
    title = info_dict.get('title', 'N/A') if info_dict else 'N/A'
    logger.info("Generated final tags for '%s': \"%s\"", title, result)
    return result


# --- Function for cleaning tags for Telegram ---
def clean_telegram_tag(tag: str) -> str:
    return '#' + re.sub(r'[^\w]', '', tag.lstrip('#'))

# --- a function for extracting the URL, the range and tags from the text ---
def extract_url_range_tags(text: str):
    # This function now always returns the full original download link
    logger.info(f"🔍 [DEBUG] extract_url_range_tags вызвана с text='{text}'")
    if not isinstance(text, str):
        return None, 1, 1, None, [], '', None
    
    #  Сначала ищем формат /img start-end URL (поддерживаем отрицательные числа)
    img_range_match = re.search(r'/img\s+(-?\d+)-(-?\d+)\s+(https?://[^\s\*#]+)', text)
    if img_range_match:
        video_start_with = int(img_range_match.group(1))
        video_end_with = int(img_range_match.group(2))
        url = img_range_match.group(3)
        after_url = text[img_range_match.end():]
        after_range = after_url
    else:
        # First, try to find URL with range pattern *start*end at the end (поддерживаем отрицательные числа)
        # Используем более точный regex, который правильно парсит URL с параметрами и диапазоном
        url_with_range_match = re.search(r'(https?://[^\s\*#]+)\*(-?\d+)\*(-?\d+)', text)
        if url_with_range_match:
            url = url_with_range_match.group(1)
            video_start_with = int(url_with_range_match.group(2))
            video_end_with = int(url_with_range_match.group(3))
            after_url = text[url_with_range_match.end():]
            after_range = after_url
            logger.info(f"🔍 [DEBUG] extract_url_range_tags: найдено URL с диапазоном: url='{url}', video_start_with={video_start_with}, video_end_with={video_end_with}")
        else:
            # Fallback to original logic
            url_match = re.search(r'https?://[^\s\*#]+', text)
            if not url_match:
                logger.info(f"🔍 [DEBUG] extract_url_range_tags: URL не найден в тексте: '{text}'")
                return None, 1, 1, None, [], '', None
            url = url_match.group(0)

            after_url = text[url_match.end():]
            # Range (поддерживаем отрицательные числа)
            range_match = re.match(r'\*(-?\d+)\*(-?\d+)', after_url)
            if range_match:
                video_start_with = int(range_match.group(1))
                video_end_with = int(range_match.group(2))
                after_range = after_url[range_match.end():]
                logger.info(f"🔍 [DEBUG] extract_url_range_tags: найдено URL с диапазоном (fallback): url='{url}', video_start_with={video_start_with}, video_end_with={video_end_with}")
            else:
                video_start_with = 1
                video_end_with = 1
                after_range = after_url
                logger.info(f"🔍 [DEBUG] extract_url_range_tags: диапазон не найден, используем значения по умолчанию: video_start_with={video_start_with}, video_end_with={video_end_with}")
    playlist_name = None
    playlist_match = re.match(r'\*([^\s\*#]+)', after_range)
    if playlist_match:
        playlist_name = playlist_match.group(1)
        after_range = after_range[playlist_match.end():]
    # New way: Looking for everything #tags throughout the text (multi -line)
    # But only if they are separated from URLs (by spaces, start/end of line)
    tags = []
    tags_text = ''
    error_tag = None
    error_tag_example = None
    
    # First, extract URL to exclude tags that are part of URL
    url_match = re.search(r'https?://[^\s\*#]+', text)
    url_start = url_match.start() if url_match else -1
    url_end = url_match.end() if url_match else -1
    
    # We collect everything #tags from the whole text (multi -line)
    # But skip tags that are inside URL boundaries
    for raw in re.finditer(r'#([^#\s]+)', text, re.UNICODE):
        tag_start = raw.start()
        tag_end = raw.end()
        
        # Skip if tag is inside URL
        if url_start != -1 and url_end != -1 and url_start <= tag_start < url_end:
            continue
        
        # Check if tag is separated from surrounding text (not part of URL or other text)
        # Tag should be at start of text, end of text, or surrounded by whitespace/newlines
        is_separated = False
        if tag_start == 0:
            # Tag at start of text
            is_separated = True
        elif tag_end == len(text):
            # Tag at end of text
            is_separated = True
        else:
            # Check characters before and after tag
            char_before = text[tag_start - 1] if tag_start > 0 else ' '
            char_after = text[tag_end] if tag_end < len(text) else ' '
            # Tag is separated if surrounded by whitespace or at boundaries
            if char_before.isspace() or char_before in '\n\r\t':
                is_separated = True
            elif char_after.isspace() or char_after in '\n\r\t':
                is_separated = True
            # Also check if before tag is end of URL (space, newline, or end of text)
            # and after tag is not part of URL continuation
            elif tag_start > 0:
                # Check if we're right after URL (after space/newline after URL)
                if url_end != -1 and tag_start > url_end:
                    # Check if there's whitespace between URL end and tag
                    between_text = text[url_end:tag_start]
                    if between_text.strip() == '' or between_text.strip().isspace():
                        is_separated = True
        
        if not is_separated:
            continue
        
        tag = raw.group(1)
        
        # If tag contains '/' character, it's part of URL, not a tag - skip it
        if '/' in tag:
            continue
        
        # If tag contains other forbidden characters, show error
        if not re.fullmatch(r'[\w\d_]+', tag, re.UNICODE):
            error_tag = tag
            sanitized_tag = re.sub(r'[^\w\d_]', '_', tag, flags=re.UNICODE)
            sanitized_tag = re.sub(r'_+', '_', sanitized_tag)
            sanitized_tag = sanitized_tag.strip('_')
            error_tag_example = f'#{sanitized_tag}' if sanitized_tag else '#tag'
            break
        tags.append(f'#{tag}')
    tags_text = ' '.join(tags)
    # Return the error if there is
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


# --- an auxiliary function for searching for car tues ---
def get_auto_tags(url, user_tags):
    auto_tags = set()
    clean_url = get_clean_url_for_tagging(url)
    url_l = clean_url.lower()
    domain_parts, _ = extract_domain_parts(url_l)
    parsed = urlparse(clean_url)
    ext = tldextract.extract(clean_url)
    second_level = ext.domain.lower() if ext.domain else ''
    full_domain = f"{ext.domain}.{ext.suffix}".lower() if ext.domain and ext.suffix else ''
    # 1. Porn Check (domain-based). GREYLIST excluded inside is_porn_domain
    if is_porn_domain(domain_parts):
        auto_tags.add(sanitize_autotag('nsfw'))
    # Безопасная функция для проверки домена
    def _is_domain_match(hostname: str, domain: str) -> bool:
        if not hostname or not domain:
            return False
        hostname_lower = hostname.lower().strip()
        domain_lower = domain.lower().strip()
        if ':' in hostname_lower:
            hostname_lower = hostname_lower.split(':')[0]
        return hostname_lower == domain_lower or hostname_lower.endswith('.' + domain_lower)
    
    # 2. YouTube Check (including YouTu.be)
    check_hostname = parsed.netloc.lower()
    if _is_domain_match(check_hostname, 'youtube.com') or _is_domain_match(check_hostname, 'youtu.be'):
        auto_tags.add("#youtube")
    # 3. VK Check (including VK.com)
    if _is_domain_match(check_hostname, 'vk.com') or _is_domain_match(check_hostname, 'vkontakte.ru') or _is_domain_match(check_hostname, 'vkvideo.ru'):
        auto_tags.add("#vk")
    # 4. Twitter/X check (exact domain match)
    twitter_domains = {"twitter.com", "x.com", "t.co"}
    domain = parsed.netloc.lower()
    if domain in twitter_domains or _is_domain_match(domain, 'twitter.com') or _is_domain_match(domain, 'x.com') or _is_domain_match(domain, 't.co'):
        auto_tags.add("#twitter")
    # 5. Boosty check (boosty.to, boosty.com)
    if _is_domain_match(check_hostname, 'boosty.to') or _is_domain_match(check_hostname, 'boosty.com'):
        auto_tags.add("#boosty")
        auto_tags.add("#nsfw")
    # 6. Service tag for supported sites (by full domain or 2nd level)
    for site in SUPPORTED_SITES:
        site_l = site.lower()
        if second_level == site_l or full_domain == site_l:
            service_tag = '#' + re.sub(r'[^\w\d_]', '', site_l)
            auto_tags.add(service_tag)
            break
    # Do not duplicate user tags
    user_tags_lower = set(t.lower() for t in user_tags)
    auto_tags = [t for t in auto_tags if t.lower() not in user_tags_lower]
    return auto_tags
