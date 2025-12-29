import re
import json
import os
import shutil
from functools import lru_cache
from typing import Dict, Optional, Tuple
from datetime import datetime
from urllib.parse import urlparse

import requests


DEFAULT_TIMEOUT_SECONDS = 6
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept": "text/html,application/json;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


def _load_cookies_for_user(user_id: int) -> Optional[str]:
    """
    Загружает куки для пользователя.
    Возвращает путь к файлу куки или None.
    """
    if not user_id:
        return None
    
    user_dir = os.path.join("users", str(user_id))
    user_cookie_path = os.path.join(user_dir, "cookie.txt")
    
    # Проверяем пользовательские куки
    if os.path.exists(user_cookie_path):
        return user_cookie_path
    
    # Пробуем глобальные куки
    try:
        from CONFIG._config import Config
        global_cookie_path = Config.COOKIE_FILE_PATH
        if os.path.exists(global_cookie_path):
            # Создаем директорию пользователя и копируем глобальные куки
            os.makedirs(user_dir, exist_ok=True)
            shutil.copy2(global_cookie_path, user_cookie_path)
            return user_cookie_path
    except Exception as e:
        print(f"[COOKIES] Error loading global cookies: {e}")
    
    return None


def _create_session_with_cookies(user_id: int = None) -> requests.Session:
    """
    Создает сессию requests с куки пользователя.
    Uses managed session for automatic cleanup.
    """
    from HELPERS.http_manager import get_managed_session
    
    session_name = f"api-info-{user_id}" if user_id else "api-info-global"
    manager = get_managed_session(session_name)
    session = manager.get_session()
    
    # Устанавливаем заголовки
    session.headers.update(DEFAULT_HEADERS)
    
    # Загружаем куки если указан user_id
    if user_id:
        cookie_path = _load_cookies_for_user(user_id)
        if cookie_path:
            try:
                # Загружаем куки из файла
                session.cookies = _load_cookies_from_file(cookie_path)
                print(f"[COOKIES] Loaded cookies for user {user_id} from {cookie_path}")
            except Exception as e:
                print(f"[COOKIES] Error loading cookies for user {user_id}: {e}")
    
    return session


def _load_cookies_from_file(cookie_path: str) -> requests.cookies.RequestsCookieJar:
    """
    Загружает куки из файла в формате Netscape.
    """
    jar = requests.cookies.RequestsCookieJar()
    
    try:
        with open(cookie_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#') or not line:
                    continue
                
                parts = line.split('\t')
                if len(parts) >= 7:
                    domain = parts[0]
                    domain_flag = parts[1] == 'TRUE'
                    path = parts[2]
                    secure = parts[3] == 'TRUE'
                    expiration = parts[4]
                    name = parts[5]
                    value = parts[6]
                    
                    # Пропускаем куки с истекшим сроком (если expiration > 0)
                    if expiration != '0':
                        try:
                            exp_time = int(expiration)
                            if exp_time and exp_time > 0 and exp_time < int(datetime.now().timestamp()):
                                continue
                        except ValueError:
                            pass
                    
                    jar.set(name, value, domain=domain, path=path)
    except Exception as e:
        print(f"[COOKIES] Error parsing cookie file {cookie_path}: {e}")
    
    return jar


def _http_get(url: str, timeout: int = DEFAULT_TIMEOUT_SECONDS, user_id: int = None) -> Optional[str]:
    try:
        session = _create_session_with_cookies(user_id)
        resp = session.get(url, timeout=timeout, allow_redirects=True)
        if resp.ok:
            return resp.text
    except Exception as e:
        print(f"[HTTP_GET] Request error for {url}: {e}")
        return None
    return None


def _http_get_json(url: str, timeout: int = DEFAULT_TIMEOUT_SECONDS, user_id: int = None) -> Optional[Dict]:
    try:
        session = _create_session_with_cookies(user_id)
        resp = session.get(url, timeout=timeout, allow_redirects=True)
        if resp.ok:
            return resp.json()
        else:
            # Логируем HTTP ошибки для отладки, но не прерываем процесс
            if resp.status_code == 401:
                print(f"[HTTP_GET_JSON] Authentication required for {url} (401 Unauthorized)")
            elif resp.status_code == 403:
                print(f"[HTTP_GET_JSON] Access forbidden for {url} (403 Forbidden)")
            else:
                print(f"[HTTP_GET_JSON] HTTP error {resp.status_code} for {url}")
    except Exception as e:
        print(f"[HTTP_GET_JSON] Request error for {url}: {e}")
        return None
    return None


META_TAG_RE = re.compile(
    r"<meta[^>]+(?:property|name)=\"([^\"]+)\"[^>]+content=\"([^\"]*)\"[^>]*>",
    re.IGNORECASE,
)


def _extract_meta(html: str) -> Dict[str, str]:
    metas: Dict[str, str] = {}
    if not html:
        return metas
    for match in META_TAG_RE.finditer(html):
        key = match.group(1).strip().lower()
        val = match.group(2).strip()
        metas[key] = val
    return metas


def _extract_via_oembed(url: str, endpoints: Tuple[str, ...], user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    """
    Пробует стандартные oEmbed endpoints, возвращает (author_name/provider_name, site_label)
    """
    for ep in endpoints:
        try:
            full = ep.format(url=url)
            data = _http_get_json(full, user_id=user_id)
            if not data:
                continue
            author = data.get("author_name") or data.get("author_url") or data.get("title")
            provider = data.get("provider_name") or data.get("provider_url")
            # Очистим author если это URL
            if isinstance(author, str) and author.startswith("http"):
                # вытащим хвост пути
                try:
                    from urllib.parse import urlparse
                    p = urlparse(author)
                    segment = p.path.strip("/").split("/")
                    if segment and segment[0]:
                        author = segment[-1]
                except Exception:
                    pass
            return (author if isinstance(author, str) else None, provider if isinstance(provider, str) else None)
        except Exception as e:
            print(f"[OEMBED] Endpoint {ep} error: {e}")
            continue
    return (None, None)


def _normalize_slug(text: str) -> str:
    if not text:
        return ""
    # Remove emojis and non-word except spaces/underscore/dash
    text = re.sub(r"[\u2600-\u27BF\U0001F300-\U0001FAD6]+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = text.lower()
    text = re.sub(r"[^a-z0-9а-яё\s_-]", "", text)
    text = text.replace(" ", "_")
    return text


def _is_valid_username(token: str) -> bool:
    """Проверяет, что токен похож на ник: >=3 символов, содержит буквы, не только цифры."""
    if not token:
        return False
    token = token.strip()
    if len(token) < 3:
        return False
    if token.isdigit():
        return False
    if not re.search(r"[A-Za-zА-Яа-яЁё]", token):
        return False
    return True


def _parse_date_string(date_str: str) -> Optional[str]:
    """
    Универсальная функция парсинга даты из строки.
    Возвращает дату в формате DD.MM.YYYY или None.
    """
    if not date_str:
        return None
    
    # Список форматов дат для парсинга
    date_formats = [
        "%Y-%m-%d",                    # 2024-10-04
        "%Y-%m-%dT%H:%M:%S",          # 2024-10-04T15:30:00
        "%Y-%m-%dT%H:%M:%SZ",         # 2024-10-04T15:30:00Z
        "%Y-%m-%dT%H:%M:%S.%f",       # 2024-10-04T15:30:00.123456
        "%Y-%m-%dT%H:%M:%S.%fZ",      # 2024-10-04T15:30:00.123456Z
        "%Y-%m-%d %H:%M:%S",          # 2024-10-04 15:30:00
        "%Y-%m-%d %H:%M:%S.%f",       # 2024-10-04 15:30:00.123456
        "%d.%m.%Y",                   # 04.10.2024
        "%d/%m/%Y",                   # 04/10/2024
        "%m/%d/%Y",                   # 10/04/2024
        "%B %d, %Y",                  # October 4, 2024
        "%d %B %Y",                   # 4 October 2024
    ]
    
    # Сначала пробуем стандартные форматы
    for fmt in date_formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%d.%m.%Y")
        except ValueError:
            continue
    
    # Если не удалось распарсить, попробуем извлечь год-месяц-день регулярным выражением
    date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)
    if date_match:
        year, month, day = date_match.groups()
        try:
            dt = datetime(int(year), int(month), int(day))
            return dt.strftime("%d.%m.%Y")
        except ValueError:
            pass
    
    # Попробуем ISO формат с временной зоной
    try:
        # Убираем временную зону если есть
        date_clean = re.sub(r'[+-]\d{2}:\d{2}$', '', date_str)
        dt = datetime.fromisoformat(date_clean)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        pass
    
    return None


def _guess_username_from_url(url: str, service: Optional[str]) -> Optional[str]:
    try:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        path_parts = [p for p in (parsed.path or '').split('/') if p]
        if not path_parts:
            return None
        u = (url or '').lower()
        # Service-specific heuristics
        if service == 'tiktok':
            # https://www.tiktok.com/@username/... -> take after '@'
            for part in path_parts:
                if part.startswith('@') and _is_valid_username(part[1:]):
                    return part[1:]
        if service == 'instagram':
            blocked = {'p', 'reel', 'reels', 'stories', 'explore', 'tv', 's'}
            cand = path_parts[0]
            if cand not in blocked and _is_valid_username(cand):
                return cand
        if service in {'x', 'twitter'}:
            blocked = {'i', 'status', 'home', 'explore', 'notifications', 'share'}
            cand = path_parts[0]
            if cand not in blocked and _is_valid_username(cand):
                return cand
        if service == 'vk':
            # Prefer readable slugs like /somegroup; skip wall-, video, photo
            blocked_prefixes = ('wall', 'video', 'photo')
            cand = path_parts[0]
            if not any(cand.startswith(p) for p in blocked_prefixes) and _is_valid_username(cand):
                return cand
        if service in {'youtube'}:
            # /@channel, /channel/UC..., /c/name, /user/name
            if path_parts[0].startswith('@') and _is_valid_username(path_parts[0][1:]):
                return path_parts[0][1:]
            if len(path_parts) >= 2 and path_parts[0] in {'c', 'user'} and _is_valid_username(path_parts[1]):
                return path_parts[1]
        # Generic fallback: first segment that looks like username and not a known content marker
        generic_blocked = {'status', 'watch', 'post', 'p', 'reel', 'photo', 'video', 'wall'}
        for part in path_parts:
            if part in generic_blocked:
                continue
            # strip common file extensions
            part_clean = re.sub(r"\.(jpg|jpeg|png|gif|webp|mp4|mov|avi|mkv)$", "", part, flags=re.IGNORECASE)
            if _is_valid_username(part_clean):
                return part_clean
    except Exception:
        return None
    return None


def _is_domain_match(hostname: str, domain: str) -> bool:
    """
    Безопасно проверяет, соответствует ли hostname указанному домену.
    Учитывает поддомены (например, www.twitter.com соответствует twitter.com).
    """
    if not hostname or not domain:
        return False
    hostname_lower = hostname.lower()
    domain_lower = domain.lower()
    # Точное совпадение или домен является суффиксом hostname
    return hostname_lower == domain_lower or hostname_lower.endswith('.' + domain_lower)


def _detect_service(url: str) -> Optional[str]:
    if not url:
        return None
    
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname
        if not hostname:
            # Если не удалось распарсить hostname, используем старый метод как fallback
            u = url.lower()
            if "instagram.com" in u or "instagr.am" in u:
                return "instagram"
            if "tiktok.com" in u or "vm.tiktok.com" in u or "vt.tiktok.com" in u:
                return "tiktok"
            if "twitter.com" in u or "x.com" in u:
                return "x"
            if "vk.com" in u or "vkontakte.ru" in u or "vkvideo.ru" in u:
                return "vk"
            if "youtube.com" in u or "youtu.be" in u or "music.youtube.com" in u:
                return "youtube"
            if "reddit.com" in u or "redd.it" in u:
                return "reddit"
            if "pinterest.com" in u or "pin.it" in u:
                return "pinterest"
            if "flickr.com" in u:
                return "flickr"
            if "deviantart.com" in u:
                return "deviantart"
            if "imgur.com" in u:
                return "imgur"
            if "tumblr.com" in u:
                return "tumblr"
            if "pixiv.net" in u:
                return "pixiv"
            if "artstation.com" in u:
                return "artstation"
            if "danbooru.donmai.us" in u or "danbooru" in u:
                return "danbooru"
            if "gelbooru.com" in u:
                return "gelbooru"
            if "yande.re" in u or "yande" in u:
                return "yandere"
            if "sankakucomplex.com" in u or "c.sankakucomplex.com" in u or "chan.sankaku" in u:
                return "sankaku"
            if "e621.net" in u:
                return "e621"
            if "rule34.xxx" in u or "rule34.paheal.net" in u:
                return "rule34"
            if "behance.net" in u or "behance.com" in u:
                return "behance"
            return None
        
        hostname_lower = hostname.lower()
        
        # Безопасная проверка доменов через hostname
        if _is_domain_match(hostname_lower, "instagram.com") or _is_domain_match(hostname_lower, "instagr.am"):
            return "instagram"
        if _is_domain_match(hostname_lower, "tiktok.com") or _is_domain_match(hostname_lower, "vm.tiktok.com") or _is_domain_match(hostname_lower, "vt.tiktok.com"):
            return "tiktok"
        if _is_domain_match(hostname_lower, "twitter.com") or _is_domain_match(hostname_lower, "x.com"):
            return "x"
        if _is_domain_match(hostname_lower, "vk.com") or _is_domain_match(hostname_lower, "vkontakte.ru") or _is_domain_match(hostname_lower, "vkvideo.ru"):
            return "vk"
        if _is_domain_match(hostname_lower, "youtube.com") or _is_domain_match(hostname_lower, "youtu.be") or _is_domain_match(hostname_lower, "music.youtube.com"):
            return "youtube"
        if _is_domain_match(hostname_lower, "reddit.com") or _is_domain_match(hostname_lower, "redd.it"):
            return "reddit"
        if _is_domain_match(hostname_lower, "pinterest.com") or _is_domain_match(hostname_lower, "pin.it"):
            return "pinterest"
        if _is_domain_match(hostname_lower, "flickr.com"):
            return "flickr"
        if _is_domain_match(hostname_lower, "deviantart.com"):
            return "deviantart"
        if _is_domain_match(hostname_lower, "imgur.com"):
            return "imgur"
        if _is_domain_match(hostname_lower, "tumblr.com"):
            return "tumblr"
        if _is_domain_match(hostname_lower, "pixiv.net"):
            return "pixiv"
        if _is_domain_match(hostname_lower, "artstation.com"):
            return "artstation"
        if _is_domain_match(hostname_lower, "danbooru.donmai.us"):
            return "danbooru"
        if _is_domain_match(hostname_lower, "gelbooru.com"):
            return "gelbooru"
        if _is_domain_match(hostname_lower, "yande.re"):
            return "yandere"
        if _is_domain_match(hostname_lower, "sankakucomplex.com") or _is_domain_match(hostname_lower, "c.sankakucomplex.com") or _is_domain_match(hostname_lower, "chan.sankakucomplex.com"):
            return "sankaku"
        if _is_domain_match(hostname_lower, "e621.net"):
            return "e621"
        if _is_domain_match(hostname_lower, "rule34.xxx") or _is_domain_match(hostname_lower, "rule34.paheal.net"):
            return "rule34"
        if _is_domain_match(hostname_lower, "behance.net") or _is_domain_match(hostname_lower, "behance.com"):
            return "behance"
        # Video platforms
        if _is_domain_match(hostname_lower, "vimeo.com"):
            return "vimeo"
        if _is_domain_match(hostname_lower, "dailymotion.com") or _is_domain_match(hostname_lower, "dai.ly"):
            return "dailymotion"
        if _is_domain_match(hostname_lower, "rutube.ru"):
            return "rutube"
        if _is_domain_match(hostname_lower, "twitch.tv"):
            return "twitch"
        if _is_domain_match(hostname_lower, "facebook.com"):
            return "facebook"
        if _is_domain_match(hostname_lower, "pornhub.com") or _is_domain_match(hostname_lower, "pornhub.org"):
            return "pornhub"
        if _is_domain_match(hostname_lower, "bilibili.com") or _is_domain_match(hostname_lower, "bilibili.tv") or _is_domain_match(hostname_lower, "bili.im"):
            return "bilibili"
        if _is_domain_match(hostname_lower, "nicovideo.jp"):
            return "niconico"
        if _is_domain_match(hostname_lower, "soundcloud.com") or _is_domain_match(hostname_lower, "on.soundcloud.com"):
            return "soundcloud"
        if _is_domain_match(hostname_lower, "bandcamp.com"):
            return "bandcamp"
        if _is_domain_match(hostname_lower, "mixcloud.com"):
            return "mixcloud"
        if _is_domain_match(hostname_lower, "spotify.com"):
            return "spotify"
        if _is_domain_match(hostname_lower, "music.apple.com"):
            return "apple_music"
        if _is_domain_match(hostname_lower, "deezer.com"):
            return "deezer"
        if _is_domain_match(hostname_lower, "tidal.com"):
            return "tidal"
        if _is_domain_match(hostname_lower, "kick.com"):
            return "kick"
        if _is_domain_match(hostname_lower, "redgifs.com"):
            return "redgifs"
        if _is_domain_match(hostname_lower, "snapchat.com"):
            return "snapchat"
        if _is_domain_match(hostname_lower, "tnaflix.com") or _is_domain_match(hostname_lower, "m.tnaflix.com"):
            return "tnaflix"
        if _is_domain_match(hostname_lower, "eporner.com"):
            return "eporner"
        if _is_domain_match(hostname_lower, "pornzog.com"):
            return "pornzog"
        if _is_domain_match(hostname_lower, "porntrex.com"):
            return "porntrex"
        if _is_domain_match(hostname_lower, "curiositystream.com"):
            return "curiositystream"
        if _is_domain_match(hostname_lower, "xvideos.com") or _is_domain_match(hostname_lower, "xvideos3.com"):
            return "xvideos"
        if _is_domain_match(hostname_lower, "xnxx.com") or _is_domain_match(hostname_lower, "xnxx.tv"):
            return "xnxx"
        if _is_domain_match(hostname_lower, "xhamster.com") or _is_domain_match(hostname_lower, "fra.xhamster2.com") or _is_domain_match(hostname_lower, "xhamster1.desi") or _is_domain_match(hostname_lower, "xhchannel.com"):
            return "xhamster"
        if _is_domain_match(hostname_lower, "youporn.com"):
            return "youporn"
        if _is_domain_match(hostname_lower, "redtube.com"):
            return "redtube"
        if _is_domain_match(hostname_lower, "spankbang.com"):
            return "spankbang"
        if _is_domain_match(hostname_lower, "porntube.com"):
            return "porntube"
        if _is_domain_match(hostname_lower, "onlyfans.com"):
            return "onlyfans"
        if _is_domain_match(hostname_lower, "patreon.com"):
            return "patreon"
        if _is_domain_match(hostname_lower, "boosty.to"):
            return "boosty"
        if _is_domain_match(hostname_lower, "ok.ru"):
            return "okru"
        if _is_domain_match(hostname_lower, "pikabu.ru"):
            return "pikabu"
        if _is_domain_match(hostname_lower, "zen.yandex.ru"):
            return "yandex_zen"
        if _is_domain_match(hostname_lower, "drive.google.com") or _is_domain_match(hostname_lower, "docs.google.com") or _is_domain_match(hostname_lower, "share.google.com"):
            return "google_drive"
    except Exception:
        # В случае ошибки парсинга URL используем старый метод как fallback
        pass
    
    # Fallback: если парсинг не удался, используем старый метод (менее безопасный, но работает)
    u = url.lower()
    if "vimeo.com" in u:
        return "vimeo"
    if "dailymotion.com" in u or "dai.ly" in u:
        return "dailymotion"
    if "rutube.ru" in u:
        return "rutube"
    if "twitch.tv" in u:
        return "twitch"
    if "facebook.com" in u:
        return "facebook"
    if "pornhub.com" in u or "pornhub.org" in u:
        return "pornhub"
    if "bilibili.com" in u or "bilibili.tv" in u or "bili.im" in u:
        return "bilibili"
    if "nicovideo.jp" in u:
        return "niconico"
    if "soundcloud.com" in u or "on.soundcloud.com" in u:
        return "soundcloud"
    if "bandcamp.com" in u:
        return "bandcamp"
    if "mixcloud.com" in u:
        return "mixcloud"
    if "spotify.com" in u:
        return "spotify"
    if "music.apple.com" in u:
        return "apple_music"
    if "deezer.com" in u:
        return "deezer"
    if "tidal.com" in u:
        return "tidal"
    if "kick.com" in u:
        return "kick"
    if "redgifs.com" in u:
        return "redgifs"
    if "snapchat.com" in u:
        return "snapchat"
    if "tnaflix.com" in u or "m.tnaflix.com" in u:
        return "tnaflix"
    if "eporner.com" in u:
        return "eporner"
    if "pornzog.com" in u:
        return "pornzog"
    if "porntrex.com" in u:
        return "porntrex"
    if "curiositystream.com" in u:
        return "curiositystream"
    if "xvideos.com" in u or "xvideos3.com" in u:
        return "xvideos"
    if "xnxx.com" in u or "xnxx.tv" in u:
        return "xnxx"
    if "xhamster.com" in u or "fra.xhamster2.com" in u or "xhamster1.desi" in u or "xhchannel.com" in u:
        return "xhamster"
    if "youporn.com" in u:
        return "youporn"
    if "redtube.com" in u:
        return "redtube"
    if "spankbang.com" in u:
        return "spankbang"
    if "porntube.com" in u:
        return "porntube"
    if "onlyfans.com" in u:
        return "onlyfans"
    if "patreon.com" in u:
        return "patreon"
    if "boosty.to" in u:
        return "boosty"
    if "ok.ru" in u:
        return "okru"
    if "pikabu.ru" in u:
        return "pikabu"
    if "zen.yandex.ru" in u:
        return "yandex_zen"
    if "drive.google.com" in u or "docs.google.com" in u or "share.google" in u:
        return "google_drive"
    return None


# -------- Instagram --------


def _extract_instagram_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed first with cookies
    try:
        data = _http_get_json(f"https://www.instagram.com/oembed/?url={url}", user_id=user_id)
        if data and isinstance(data, dict):
            author = data.get("author_name")
            provider = data.get("provider_name") or "Instagram"
            if author:
                return (author, provider)
    except Exception as e:
        print(f"[INSTAGRAM_INFO] oEmbed error: {e}")
        pass
    # Fallback to OpenGraph
    html = _http_get(url, user_id=user_id)
    metas = _extract_meta(html or "")
    title = metas.get("og:title") or metas.get("twitter:title")
    site = metas.get("og:site_name") or "Instagram"
    name: Optional[str] = None
    if title:
        # Patterns commonly seen
        patterns = [
            r"^(.*?) on Instagram",
            r"^(.*?) • Instagram",
            r"^Instagram post by (.*?)(?:\s+•|$)",
            r"^(.+?) \(@[^)]+\) • Instagram",
        ]
        for p in patterns:
            m = re.search(p, title, re.IGNORECASE)
            if m and m.group(1):
                name = m.group(1).strip()
                break
    return (name, site)


def _extract_instagram_date(url: str, user_id: int = None) -> Optional[str]:
    """
    Извлекает дату загрузки из Instagram API (oEmbed).
    Возвращает дату в формате DD.MM.YYYY или None.
    """
    try:
        data = _http_get_json(f"https://www.instagram.com/oembed/?url={url}", user_id=user_id)
        if data and isinstance(data, dict):
            # oEmbed может содержать дату в разных полях
            date_str = data.get("upload_date") or data.get("created_at") or data.get("date")
            if date_str:
                return _parse_date_string(date_str)
    except Exception as e:
        # Логируем ошибку, но не прерываем процесс
        print(f"[INSTAGRAM_DATE] API error: {e}")
        pass
    
    # Fallback: попробуем извлечь из OpenGraph мета-тегов
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        
        # Ищем дату в различных мета-тегах
        date_fields = [
            "article:published_time",
            "article:modified_time", 
            "og:updated_time",
            "twitter:data1",
            "date",
            "pubdate"
        ]
        
        for field in date_fields:
            date_str = metas.get(field)
            if date_str:
                result = _parse_date_string(date_str)
                if result:
                    return result
    except Exception as e:
        print(f"[INSTAGRAM_DATE] OpenGraph error: {e}")
        pass
    
    return None


# -------- TikTok --------


def _extract_tiktok_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed with cookies first
    try:
        oembed_url = f"https://www.tiktok.com/oembed?url={url}"
        data = _http_get_json(oembed_url, user_id=user_id)
        if data and isinstance(data, dict):
            author = data.get("author_name")
            if author:
                return (author, "TikTok")
    except Exception as e:
        print(f"[TIKTOK_INFO] oEmbed with cookies error: {e}")
        pass
    
    # Fallback to oEmbed without cookies
    try:
        oembed_url = f"https://www.tiktok.com/oembed?url={url}"
        data = _http_get_json(oembed_url)
        if data and isinstance(data, dict):
            author = data.get("author_name")
            if author:
                return (author, "TikTok")
    except Exception as e:
        print(f"[TIKTOK_INFO] oEmbed without cookies error: {e}")
        pass
    
    # Final fallback to OpenGraph
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        if title:
            m = re.search(r"^(.*?) on TikTok|^(.*?) \| TikTok", title, re.IGNORECASE)
            if m:
                candidate = m.group(1) or m.group(2)
                if candidate:
                    return (candidate.strip(), "TikTok")
    except Exception as e:
        print(f"[TIKTOK_INFO] OpenGraph error: {e}")
        pass
    
    return (None, "TikTok")


def _extract_tiktok_date(url: str, user_id: int = None) -> Optional[str]:
    """Извлекает дату загрузки из TikTok API."""
    # Try with cookies first
    try:
        data = _http_get_json(f"https://www.tiktok.com/oembed?url={url}", user_id=user_id)
        if data and isinstance(data, dict):
            date_str = data.get("upload_date") or data.get("created_at") or data.get("date")
            if date_str:
                return _parse_date_string(date_str)
    except Exception as e:
        print(f"[TIKTOK_DATE] API with cookies error: {e}")
        pass
    
    # Fallback without cookies
    try:
        data = _http_get_json(f"https://www.tiktok.com/oembed?url={url}")
        if data and isinstance(data, dict):
            date_str = data.get("upload_date") or data.get("created_at") or data.get("date")
            if date_str:
                return _parse_date_string(date_str)
    except Exception as e:
        print(f"[TIKTOK_DATE] API without cookies error: {e}")
        pass
    
    # Final fallback to OpenGraph
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        date_str = metas.get("article:published_time") or metas.get("og:updated_time")
        if date_str:
            return _parse_date_string(date_str)
    except Exception as e:
        print(f"[TIKTOK_DATE] OpenGraph error: {e}")
        pass
    
    return None


# -------- X (Twitter) --------


def _extract_x_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed with cookies first
    try:
        oembed_url = f"https://publish.twitter.com/oembed?url={url}"
        data = _http_get_json(oembed_url, user_id=user_id)
        if data and isinstance(data, dict):
            author = data.get("author_name")
            if author:
                return (author, "X")
    except Exception as e:
        print(f"[X_INFO] oEmbed with cookies error: {e}")
        pass
    
    # Fallback to oEmbed without cookies
    try:
        oembed_url = f"https://publish.twitter.com/oembed?url={url}"
        data = _http_get_json(oembed_url)
        if data and isinstance(data, dict):
            author = data.get("author_name")
            if author:
                return (author, "X")
    except Exception as e:
        print(f"[X_INFO] oEmbed without cookies error: {e}")
        pass
    
    # Final fallback: meta twitter:site or title
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        handle = metas.get("twitter:site")
        if handle:
            handle = handle.strip()
            if handle.startswith("@"):
                return (handle, "X")
        title = metas.get("og:title") or metas.get("twitter:title")
        if title:
            m = re.search(r"^(.*?) on X|^(.*?) / X", title, re.IGNORECASE)
            if m:
                candidate = m.group(1) or m.group(2)
                if candidate:
                    return (candidate.strip(), "X")
    except Exception as e:
        print(f"[X_INFO] OpenGraph error: {e}")
        pass
    
    return (None, "X")


def _extract_x_date(url: str, user_id: int = None) -> Optional[str]:
    """Извлекает дату публикации из X (Twitter) API."""
    # Try with cookies first
    try:
        data = _http_get_json(f"https://publish.twitter.com/oembed?url={url}", user_id=user_id)
        if data and isinstance(data, dict):
            date_str = data.get("upload_date") or data.get("created_at") or data.get("date")
            if date_str:
                return _parse_date_string(date_str)
    except Exception as e:
        print(f"[X_DATE] API with cookies error: {e}")
        pass
    
    # Fallback without cookies
    try:
        data = _http_get_json(f"https://publish.twitter.com/oembed?url={url}")
        if data and isinstance(data, dict):
            date_str = data.get("upload_date") or data.get("created_at") or data.get("date")
            if date_str:
                return _parse_date_string(date_str)
    except Exception as e:
        print(f"[X_DATE] API without cookies error: {e}")
        pass
    
    # Final fallback to OpenGraph
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        date_str = metas.get("article:published_time") or metas.get("og:updated_time")
        if date_str:
            return _parse_date_string(date_str)
    except Exception as e:
        print(f"[X_DATE] OpenGraph error: {e}")
        pass
    
    return None


# -------- VK --------


def _extract_vk_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try to resolve owner from wall-<owner>_<post>
    site = "VK"
    try:
        m = re.search(r"vk\.com/(?:wall)(-?\d+)_\d+", url, re.IGNORECASE)
        if m:
            owner_id = int(m.group(1))
            probe_urls = []
            if owner_id and owner_id < 0:
                gid = abs(owner_id)
                probe_urls = [
                    f"https://vk.com/public{gid}",
                    f"https://vk.com/club{gid}",
                ]
            else:
                probe_urls = [
                    f"https://vk.com/id{owner_id}",
                ]
            for pu in probe_urls:
                try:
                    html_p = _http_get(pu, user_id=user_id)
                    metas_p = _extract_meta(html_p or "")
                    t = metas_p.get("og:title") or metas_p.get("twitter:title")
                    s = metas_p.get("og:site_name") or site
                    if t:
                        mm = re.search(r"^(.+?)\s*\|\s*VK$", t, re.IGNORECASE)
                        name = (mm.group(1).strip() if mm and mm.group(1) else t.strip())
                        name = re.sub(r"^Сообщество\s+«?", "", name).strip()
                        name = re.sub(r"»$", "", name).strip()
                        name = re.sub(r"^Запись сообщества\s+", "", name).strip()
                        if name:
                            return (name, s)
                except Exception as e:
                    print(f"[VK_INFO] Probe URL {pu} error: {e}")
                    continue
    except Exception as e:
        print(f"[VK_INFO] Wall parsing error: {e}")
        pass
    
    # Fallback: use current page OG/title heuristics with cookies
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        site = metas.get("og:site_name") or site
        if title:
            mm = re.search(r"^(.+?)\s*\|\s*VK$", title, re.IGNORECASE)
            if mm and mm.group(1):
                cleaned = re.sub(r"^Сообщество\s+«?", "", mm.group(1)).strip()
                cleaned = re.sub(r"»$", "", cleaned).strip()
                cleaned = re.sub(r"^Запись сообщества\s+", "", cleaned).strip()
                if cleaned:
                    return (cleaned, site)
    except Exception as e:
        print(f"[VK_INFO] OpenGraph error: {e}")
        pass
    
    return (None, site)


# -------- YouTube --------


def _extract_youtube_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed with cookies first
    try:
        name, provider = _extract_via_oembed(url, (
            "https://www.youtube.com/oembed?url={url}",
        ), user_id=user_id)
        if name:
            return (name, provider or "YouTube")
    except Exception as e:
        print(f"[YOUTUBE_INFO] oEmbed with cookies error: {e}")
        pass
    
    # Fallback to oEmbed without cookies
    try:
        name, provider = _extract_via_oembed(url, (
            "https://www.youtube.com/oembed?url={url}",
        ))
        if name:
            return (name, provider or "YouTube")
    except Exception as e:
        print(f"[YOUTUBE_INFO] oEmbed without cookies error: {e}")
        pass
    
    # Final fallback to OpenGraph
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        channel = metas.get("og:site_name") or metas.get("twitter:title")
        return (channel, "YouTube")
    except Exception as e:
        print(f"[YOUTUBE_INFO] OpenGraph error: {e}")
        return (None, "YouTube")


def _extract_youtube_date(url: str, user_id: int = None) -> Optional[str]:
    """Извлекает дату загрузки из YouTube API."""
    # Try with cookies first
    try:
        data = _http_get_json(f"https://www.youtube.com/oembed?url={url}", user_id=user_id)
        if data and isinstance(data, dict):
            date_str = data.get("upload_date") or data.get("created_at") or data.get("date")
            if date_str:
                return _parse_date_string(date_str)
    except Exception as e:
        print(f"[YOUTUBE_DATE] API with cookies error: {e}")
        pass
    
    # Fallback without cookies
    try:
        data = _http_get_json(f"https://www.youtube.com/oembed?url={url}")
        if data and isinstance(data, dict):
            date_str = data.get("upload_date") or data.get("created_at") or data.get("date")
            if date_str:
                return _parse_date_string(date_str)
    except Exception as e:
        print(f"[YOUTUBE_DATE] API without cookies error: {e}")
        pass
    
    # Final fallback to OpenGraph
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        date_str = metas.get("article:published_time") or metas.get("og:updated_time")
        if date_str:
            return _parse_date_string(date_str)
    except Exception as e:
        print(f"[YOUTUBE_DATE] OpenGraph error: {e}")
        pass
    
    return None


# -------- Reddit --------


def _extract_reddit_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed with cookies first
    try:
        name, provider = _extract_via_oembed(url, (
            "https://www.reddit.com/oembed?url={url}",
        ), user_id=user_id)
        if name:
            return (name, provider or "Reddit")
    except Exception as e:
        print(f"[REDDIT_INFO] oEmbed with cookies error: {e}")
        pass
    
    # Fallback to oEmbed without cookies
    try:
        name, provider = _extract_via_oembed(url, (
            "https://www.reddit.com/oembed?url={url}",
        ))
        if name:
            return (name, provider or "Reddit")
    except Exception as e:
        print(f"[REDDIT_INFO] oEmbed without cookies error: {e}")
        pass
    
    # Final fallback to OpenGraph
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        return (title, "Reddit")
    except Exception as e:
        print(f"[REDDIT_INFO] OpenGraph error: {e}")
        return (None, "Reddit")


# -------- Pinterest --------


def _extract_pinterest_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Нет официального публичного oEmbed, используем только OpenGraph
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        site = metas.get("og:site_name") or "Pinterest"
        return (title, site)
    except Exception as e:
        print(f"[PINTEREST_INFO] OpenGraph error: {e}")
        return (None, "Pinterest")


# -------- Flickr --------


def _extract_flickr_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed with cookies first
    try:
        name, provider = _extract_via_oembed(url, (
            "https://www.flickr.com/services/oembed?format=json&url={url}",
        ), user_id=user_id)
        if name:
            return (name, provider or "Flickr")
    except Exception as e:
        print(f"[FLICKR_INFO] oEmbed with cookies error: {e}")
        pass
    
    # Fallback to oEmbed without cookies
    try:
        name, provider = _extract_via_oembed(url, (
            "https://www.flickr.com/services/oembed?format=json&url={url}",
        ))
        if name:
            return (name, provider or "Flickr")
    except Exception as e:
        print(f"[FLICKR_INFO] oEmbed without cookies error: {e}")
        pass
    
    # Final fallback to OpenGraph
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title")
        return (title, "Flickr")
    except Exception as e:
        print(f"[FLICKR_INFO] OpenGraph error: {e}")
        return (None, "Flickr")


# -------- DeviantArt --------


def _extract_deviantart_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed with cookies first
    try:
        name, provider = _extract_via_oembed(url, (
            "https://backend.deviantart.com/oembed?url={url}",
        ), user_id=user_id)
        if name:
            return (name, provider or "DeviantArt")
    except Exception as e:
        print(f"[DEVIANTART_INFO] oEmbed with cookies error: {e}")
        pass
    
    # Fallback to oEmbed without cookies
    try:
        name, provider = _extract_via_oembed(url, (
            "https://backend.deviantart.com/oembed?url={url}",
        ))
        if name:
            return (name, provider or "DeviantArt")
    except Exception as e:
        print(f"[DEVIANTART_INFO] oEmbed without cookies error: {e}")
        pass
    
    # Final fallback to OpenGraph
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        author = metas.get("twitter:creator") or metas.get("og:site_name")
        return (author, "DeviantArt")
    except Exception as e:
        print(f"[DEVIANTART_INFO] OpenGraph error: {e}")
        return (None, "DeviantArt")


# -------- Imgur --------


def _extract_imgur_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed with cookies first
    try:
        name, provider = _extract_via_oembed(url, (
            "https://api.imgur.com/oembed?url={url}",
        ), user_id=user_id)
        if name:
            return (name, provider or "Imgur")
    except Exception as e:
        print(f"[IMGUR_INFO] oEmbed with cookies error: {e}")
        pass
    
    # Fallback to oEmbed without cookies
    try:
        name, provider = _extract_via_oembed(url, (
            "https://api.imgur.com/oembed?url={url}",
        ))
        if name:
            return (name, provider or "Imgur")
    except Exception as e:
        print(f"[IMGUR_INFO] oEmbed without cookies error: {e}")
        pass
    
    # Final fallback to OpenGraph
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        return (title, "Imgur")
    except Exception as e:
        print(f"[IMGUR_INFO] OpenGraph error: {e}")
        return (None, "Imgur")


# -------- Tumblr --------


def _extract_tumblr_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed with cookies first
    try:
        name, provider = _extract_via_oembed(url, (
            "https://www.tumblr.com/oembed/1.0?url={url}",
        ), user_id=user_id)
        if name:
            return (name, provider or "Tumblr")
    except Exception as e:
        print(f"[TUMBLR_INFO] oEmbed with cookies error: {e}")
        pass
    
    # Fallback to oEmbed without cookies
    try:
        name, provider = _extract_via_oembed(url, (
            "https://www.tumblr.com/oembed/1.0?url={url}",
        ))
        if name:
            return (name, provider or "Tumblr")
    except Exception as e:
        print(f"[TUMBLR_INFO] oEmbed without cookies error: {e}")
        pass
    
    # Final fallback to OpenGraph
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        site = metas.get("og:site_name") or "Tumblr"
        return (title, site)
    except Exception as e:
        print(f"[TUMBLR_INFO] OpenGraph error: {e}")
        return (None, "Tumblr")


# -------- Pixiv --------


def _extract_pixiv_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try OpenGraph with cookies first
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        site = metas.get("og:site_name") or "Pixiv"
        if title:
            return (title, site)
    except Exception as e:
        print(f"[PIXIV_INFO] OpenGraph with cookies error: {e}")
        pass
    
    # Fallback to OpenGraph without cookies
    try:
        html = _http_get(url)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        site = metas.get("og:site_name") or "Pixiv"
        if title:
            return (title, site)
    except Exception as e:
        print(f"[PIXIV_INFO] OpenGraph without cookies error: {e}")
        pass
    
    # Final fallback: try to parse user from URL
    try:
        from urllib.parse import urlparse
        p = urlparse(url)
        parts = [s for s in p.path.split('/') if s]
        if len(parts) >= 2 and parts[0] in {"users", "member"}:
            return (parts[1], "Pixiv")
    except Exception as e:
        print(f"[PIXIV_INFO] URL parsing error: {e}")
        pass
    
    return (None, "Pixiv")


# -------- ArtStation --------


def _extract_artstation_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # ArtStation has OG meta with title/site
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        site = metas.get("og:site_name") or "ArtStation"
        return (title, site)
    except Exception as e:
        print(f"[ARTSTATION_INFO] OpenGraph error: {e}")
        return (None, "ArtStation")


# -------- Danbooru --------


def _extract_danbooru_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        return (title, "Danbooru")
    except Exception as e:
        print(f"[DANBOORU_INFO] OpenGraph error: {e}")
        return (None, "Danbooru")


# -------- Gelbooru --------


def _extract_gelbooru_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        return (title, "Gelbooru")
    except Exception as e:
        print(f"[GELBOORU_INFO] OpenGraph error: {e}")
        return (None, "Gelbooru")


# -------- Yande.re --------


def _extract_yandere_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        return (title, "Yande.re")
    except Exception as e:
        print(f"[YANDERE_INFO] OpenGraph error: {e}")
        return (None, "Yande.re")


# -------- Sankaku --------


def _extract_sankaku_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        site = metas.get("og:site_name") or "Sankaku"
        return (title, site)
    except Exception as e:
        print(f"[SANKAKU_INFO] OpenGraph error: {e}")
        return (None, "Sankaku")


# -------- e621 --------


def _extract_e621_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        return (title, "e621")
    except Exception as e:
        print(f"[E621_INFO] OpenGraph error: {e}")
        return (None, "e621")


# -------- Rule34 --------


def _extract_rule34_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        return (title, "Rule34")
    except Exception as e:
        print(f"[RULE34_INFO] OpenGraph error: {e}")
        return (None, "Rule34")


# -------- Behance --------


def _extract_behance_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Behance has OG meta; sometimes author is in og:title or profile path
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        site = metas.get("og:site_name") or "Behance"
        if title:
            return (title, site)
    except Exception as e:
        print(f"[BEHANCE_INFO] OpenGraph error: {e}")
        pass
    
    # Fallback: try to parse author from URL path
    try:
        from urllib.parse import urlparse
        p = urlparse(url)
        seg = [s for s in p.path.split('/') if s]
        if seg:
            return (seg[0], "Behance")
    except Exception as e:
        print(f"[BEHANCE_INFO] URL parsing error: {e}")
        pass
    
    return (None, "Behance")


# -------- Universal OpenGraph extractor for services without specific APIs --------


def _extract_via_opengraph(url: str, service_name: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    """
    Универсальная функция для извлечения информации через OpenGraph мета-теги.
    Используется для сервисов без публичных API.
    """
    try:
        html = _http_get(url, user_id=user_id)
        metas = _extract_meta(html or "")
        title = metas.get("og:title") or metas.get("twitter:title")
        site = metas.get("og:site_name") or service_name
        author = metas.get("og:site_name") or metas.get("twitter:site") or metas.get("author")
        
        # Если есть автор, используем его, иначе используем title
        if author:
            # Убираем @ если есть
            author = author.strip().lstrip('@')
            return (author, site)
        elif title:
            return (title, site)
    except Exception as e:
        print(f"[{service_name.upper()}_INFO] OpenGraph error: {e}")
        pass
    
    return (None, service_name)


# -------- Video Platforms --------


def _extract_vimeo_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed first
    try:
        name, provider = _extract_via_oembed(url, (
            "https://vimeo.com/api/oembed.json?url={url}",
        ), user_id=user_id)
        if name:
            return (name, provider or "Vimeo")
    except Exception as e:
        print(f"[VIMEO_INFO] oEmbed error: {e}")
        pass
    
    return _extract_via_opengraph(url, "Vimeo", user_id)


def _extract_dailymotion_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Dailymotion", user_id)


def _extract_rutube_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Rutube", user_id)


def _extract_twitch_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Twitch", user_id)


def _extract_facebook_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Facebook", user_id)


def _extract_pornhub_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Pornhub", user_id)


def _extract_bilibili_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Bilibili", user_id)


def _extract_niconico_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Niconico", user_id)


def _extract_soundcloud_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed first
    try:
        name, provider = _extract_via_oembed(url, (
            "https://soundcloud.com/oembed?url={url}",
        ), user_id=user_id)
        if name:
            return (name, provider or "SoundCloud")
    except Exception as e:
        print(f"[SOUNDCLOUD_INFO] oEmbed error: {e}")
        pass
    
    return _extract_via_opengraph(url, "SoundCloud", user_id)


def _extract_bandcamp_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed first
    try:
        name, provider = _extract_via_oembed(url, (
            "https://bandcamp.com/EmbeddedPlayer/oembed?url={url}",
        ), user_id=user_id)
        if name:
            return (name, provider or "Bandcamp")
    except Exception as e:
        print(f"[BANDCAMP_INFO] oEmbed error: {e}")
        pass
    
    return _extract_via_opengraph(url, "Bandcamp", user_id)


def _extract_mixcloud_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    # Try oEmbed first
    try:
        name, provider = _extract_via_oembed(url, (
            "https://app.mixcloud.com/oembed/?url={url}",
        ), user_id=user_id)
        if name:
            return (name, provider or "Mixcloud")
    except Exception as e:
        print(f"[MIXCLOUD_INFO] oEmbed error: {e}")
        pass
    
    return _extract_via_opengraph(url, "Mixcloud", user_id)


def _extract_spotify_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Spotify", user_id)


def _extract_apple_music_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Apple Music", user_id)


def _extract_deezer_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Deezer", user_id)


def _extract_tidal_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Tidal", user_id)


def _extract_kick_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Kick", user_id)


def _extract_redgifs_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "RedGifs", user_id)


def _extract_snapchat_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Snapchat", user_id)


def _extract_tnaflix_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "TNAFlix", user_id)


def _extract_eporner_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Eporner", user_id)


def _extract_pornzog_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Pornzog", user_id)


def _extract_porntrex_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Porntrex", user_id)


def _extract_curiositystream_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "CuriosityStream", user_id)


def _extract_xvideos_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "XVideos", user_id)


def _extract_xnxx_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "XNXX", user_id)


def _extract_xhamster_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "XHamster", user_id)


def _extract_youporn_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "YouPorn", user_id)


def _extract_redtube_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Redtube", user_id)


def _extract_spankbang_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "SpankBang", user_id)


def _extract_porntube_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "PornTube", user_id)


def _extract_onlyfans_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "OnlyFans", user_id)


def _extract_patreon_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Patreon", user_id)


def _extract_boosty_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Boosty", user_id)


def _extract_okru_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Odnoklassniki", user_id)


def _extract_pikabu_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Pikabu", user_id)


def _extract_yandex_zen_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Yandex.Dzen", user_id)


def _extract_google_drive_info(url: str, user_id: int = None) -> Tuple[Optional[str], Optional[str]]:
    return _extract_via_opengraph(url, "Google Drive", user_id)


SERVICE_HANDLERS = {
    "instagram": _extract_instagram_info,
    "tiktok": _extract_tiktok_info,
    "x": _extract_x_info,
    "vk": _extract_vk_info,
    # extended set
    "youtube": _extract_youtube_info,
    "reddit": _extract_reddit_info,
    "pinterest": _extract_pinterest_info,
    "flickr": _extract_flickr_info,
    "deviantart": _extract_deviantart_info,
    "imgur": _extract_imgur_info,
    "tumblr": _extract_tumblr_info,
    # gallery-dl popular
    "pixiv": _extract_pixiv_info,
    "artstation": _extract_artstation_info,
    "danbooru": _extract_danbooru_info,
    "gelbooru": _extract_gelbooru_info,
    "yandere": _extract_yandere_info,
    "sankaku": _extract_sankaku_info,
    "e621": _extract_e621_info,
    "rule34": _extract_rule34_info,
    "behance": _extract_behance_info,
    # Video platforms
    "vimeo": _extract_vimeo_info,
    "dailymotion": _extract_dailymotion_info,
    "rutube": _extract_rutube_info,
    "twitch": _extract_twitch_info,
    "facebook": _extract_facebook_info,
    "pornhub": _extract_pornhub_info,
    "bilibili": _extract_bilibili_info,
    "niconico": _extract_niconico_info,
    "soundcloud": _extract_soundcloud_info,
    "bandcamp": _extract_bandcamp_info,
    "mixcloud": _extract_mixcloud_info,
    "spotify": _extract_spotify_info,
    "apple_music": _extract_apple_music_info,
    "deezer": _extract_deezer_info,
    "tidal": _extract_tidal_info,
    "kick": _extract_kick_info,
    "redgifs": _extract_redgifs_info,
    "snapchat": _extract_snapchat_info,
    "tnaflix": _extract_tnaflix_info,
    "eporner": _extract_eporner_info,
    "pornzog": _extract_pornzog_info,
    "porntrex": _extract_porntrex_info,
    "curiositystream": _extract_curiositystream_info,
    "xvideos": _extract_xvideos_info,
    "xnxx": _extract_xnxx_info,
    "xhamster": _extract_xhamster_info,
    "youporn": _extract_youporn_info,
    "redtube": _extract_redtube_info,
    "spankbang": _extract_spankbang_info,
    "porntube": _extract_porntube_info,
    "onlyfans": _extract_onlyfans_info,
    "patreon": _extract_patreon_info,
    "boosty": _extract_boosty_info,
    "okru": _extract_okru_info,
    "pikabu": _extract_pikabu_info,
    "yandex_zen": _extract_yandex_zen_info,
    "google_drive": _extract_google_drive_info,
}

SERVICE_DATE_HANDLERS = {
    "instagram": _extract_instagram_date,
    "tiktok": _extract_tiktok_date,
    "x": _extract_x_date,
    "youtube": _extract_youtube_date,
    # Для остальных сервисов используется fallback через OpenGraph мета-теги
    # в функции get_service_date
}


@lru_cache(maxsize=512)
def get_service_account_info(url: str, user_id: int = None) -> Dict[str, Optional[str]]:
    """
    Возвращает словарь с ключами:
      - service: детектированное имя сервиса
      - account_display: читаемое имя/ник или @handle если получилось
      - site_label: человекочитаемое название площадки (OG)
    Никогда не бросает исключений.
    """
    try:
        service = _detect_service(url)
        if not service:
            return {"service": None, "account_display": None, "site_label": None}
        handler = SERVICE_HANDLERS.get(service)
        if not handler:
            return {"service": service, "account_display": None, "site_label": None}
        
        # Передаем user_id во все handlers для поддержки куки
        if user_id:
            name, site_label = handler(url, user_id)
        else:
            name, site_label = handler(url)
            
        display = name if name else None
        if not display:
            # Fallback to URL-based guess if API/OG didn't provide
            guessed = _guess_username_from_url(url, service)
            if guessed:
                display = guessed
        return {"service": service, "account_display": display, "site_label": site_label}
    except Exception as e:
        print(f"[SERVICE_ACCOUNT_INFO] Error: {e}")
        return {"service": None, "account_display": None, "site_label": None}


def build_tags(info: Dict[str, Optional[str]]) -> Tuple[str, Optional[str]]:
    """
    Формирует пару (service_tag, account_tag) вида ("#instagram", "#some_account").
    Второй элемент может быть None, если аккаунт не распознан.
    Never raises exceptions - returns safe defaults on error
    """
    try:
        if not info:
            return ("", None)
        service = info.get("service") or ""
        account = info.get("account_display") or ""
        if not service:
            return ("", None)
        service_tag = f"#{service}"
        account_tag: Optional[str] = None
        if account:
            try:
                slug = _normalize_slug(account)
                if slug:
                    account_tag = f"#{slug}"
            except Exception:
                pass  # Ignore slug normalization errors
        return (service_tag, account_tag)
    except Exception:
        return ("", None)


def get_account_tag(url: str, user_id: int = None) -> str:
    """
    Удобный интерфейс: возвращает строку хэштегов для сообщения.
    Пример: "#instagram #some_account" или просто "#instagram".
    Never raises exceptions - returns empty string on error
    """
    try:
        info = get_service_account_info(url, user_id)
        service_tag, account_tag = build_tags(info)
        if service_tag and account_tag:
            return f"{service_tag} {account_tag}"
        return service_tag or ""
    except Exception:
        return ""


@lru_cache(maxsize=512)
def get_service_date(url: str, user_id: int = None) -> Optional[str]:
    """
    Извлекает дату загрузки/публикации из API различных сервисов.
    Возвращает дату в формате DD.MM.YYYY или None.
    
    Поддерживаемые сервисы:
    - Instagram (oEmbed API) - с поддержкой куки
    - TikTok (oEmbed API)
    - X/Twitter (oEmbed API)
    - YouTube (oEmbed API)
    - И другие через OpenGraph мета-теги
    
    ВАЖНО: Эта функция НЕ критична для работы бота. 
    Если API недоступен (например, Instagram требует аутентификации),
    функция просто вернет None и процесс продолжится.
    """
    try:
        service = _detect_service(url)
        if not service:
            return None
            
        # Пробуем специализированный обработчик для сервиса
        date_handler = SERVICE_DATE_HANDLERS.get(service)
        if date_handler:
            try:
                # Передаем user_id во все date handlers для поддержки куки
                if user_id:
                    result = date_handler(url, user_id)
                else:
                    result = date_handler(url)
                    
                if result:
                    return result
            except Exception as e:
                # Логируем ошибку, но не прерываем процесс
                print(f"[SERVICE_DATE] {service} API error: {e}")
                pass
        
        # Fallback: попробуем извлечь из OpenGraph мета-тегов
        try:
            html = _http_get(url, user_id=user_id)
            metas = _extract_meta(html or "")
            
            # Ищем дату в различных мета-тегах
            date_fields = [
                "article:published_time",
                "article:modified_time", 
                "og:updated_time",
                "twitter:data1",
                "date",
                "pubdate"
            ]
            
            for field in date_fields:
                date_str = metas.get(field)
                if date_str:
                    result = _parse_date_string(date_str)
                    if result:
                        return result
        except Exception as e:
            print(f"[SERVICE_DATE] OpenGraph error: {e}")
            pass
            
    except Exception as e:
        print(f"[SERVICE_DATE] General error: {e}")
        pass
    
    return None


__all__ = [
    "get_service_account_info",
    "build_tags",
    "get_account_tag",
    "get_service_date",
    "_parse_date_string",
]


