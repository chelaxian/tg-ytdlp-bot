#!/usr/bin/env python3
"""
Universal thumbnail downloader for various video services
"""

import os
import re
import requests
import shutil
import tempfile
import ipaddress
from urllib.parse import urlparse
from typing import Optional, Tuple
from CONFIG.config import Config
from CONFIG.messages import Messages, safe_get_messages
from CONFIG.logger_msg import LoggerMsg
from HELPERS.logger import logger
import yt_dlp


def _validate_url_for_ssrf(url: str) -> tuple[bool, str]:
    """
    Валидирует URL для предотвращения SSRF атак.
    Возвращает (is_valid, error_message).
    """
    if not url:
        return False, "URL is empty"
    
    try:
        parsed = urlparse(url)
        
        # Разрешаем только HTTP и HTTPS
        if parsed.scheme not in ('http', 'https'):
            return False, f"Invalid scheme: {parsed.scheme}. Only http and https are allowed"
        
        # Проверяем хост
        host = parsed.hostname
        if not host:
            return False, "URL must have a hostname"
        
        host_lower = host.lower()
        
        # Блокируем localhost и его варианты
        blocked_hosts = {
            'localhost',
            '127.0.0.1',
            '0.0.0.0',
            '::1',
            '[::1]',
        }
        if host_lower in blocked_hosts:
            return False, f"Blocked hostname: {host}"
        
        # Блокируем внутренние IP адреса
        try:
            ip = ipaddress.ip_address(host)
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
                return False, f"Blocked private/reserved IP: {host}"
            # Блокируем метаданные облачных сервисов (169.254.169.254)
            if str(ip) == '169.254.169.254':
                return False, f"Blocked metadata service IP: {host}"
        except ValueError:
            # Не IP адрес, проверяем домен
            # Блокируем домены, которые могут указывать на внутренние ресурсы
            if host_lower.endswith('.local') or host_lower.endswith('.internal'):
                return False, f"Blocked internal domain: {host}"
            # Блокируем домены, содержащие localhost
            if 'localhost' in host_lower:
                return False, f"Blocked hostname containing localhost: {host}"
        
        return True, ""
    except Exception as e:
        return False, f"URL validation error: {str(e)}"


def _is_domain_match(hostname: str, domain: str) -> bool:
    """
    Безопасно проверяет, соответствует ли hostname указанному домену.
    Учитывает поддомены (например, www.twitter.com соответствует twitter.com).
    Защищено от обхода через поддомены злоумышленников (например, evil.com?twitter.com).
    """
    if not hostname or not domain:
        return False
    
    # Нормализуем входные данные
    hostname_lower = hostname.lower().strip()
    domain_lower = domain.lower().strip()
    
    # Убираем порт если есть
    if ':' in hostname_lower:
        hostname_lower = hostname_lower.split(':')[0]
    
    # Точное совпадение
    if hostname_lower == domain_lower:
        return True
    
    # Проверяем, что домен является суффиксом hostname (для поддоменов)
    # Используем точную проверку с точкой, чтобы избежать обхода через поддомены злоумышленников
    if hostname_lower.endswith('.' + domain_lower):
        # Дополнительная проверка: убеждаемся, что перед точкой нет других точек
        prefix = hostname_lower[:-len(domain_lower) - 1]
        # Если в префиксе есть точка, это может быть попытка обхода
        if '.' in prefix:
            # Разрешаем только если это валидный поддомен (например, www, api, mobile)
            parts = prefix.split('.')
            # Если последняя часть префикса не является валидным поддоменом, блокируем
            if len(parts) > 0 and parts[-1]:
                # Разрешаем только если это простой поддомен без специальных символов
                last_part = parts[-1]
                if not last_part.replace('-', '').replace('_', '').isalnum():
                    return False
        return True
    
    return False


def extract_service_info(url: str) -> Tuple[str, str]:
    """
    Extract service type and video ID from URL
    Returns: (service_type, video_id)
    Never raises exceptions - returns ('unknown', '') on error
    """
    try:
        parsed = urlparse(url)
        netloc = parsed.netloc.lower()
        path = parsed.path
        query = parsed.query
        
        # Instagram
        if _is_domain_match(netloc, 'instagram.com') or _is_domain_match(netloc, 'instagr.am'):
            if '/reel/' in path:
                match = re.search(r'/reel/([^/?]+)', path)
                if match:
                    return 'instagram', match.group(1)
            elif '/p/' in path:
                match = re.search(r'/p/([^/?]+)', path)
                if match:
                    return 'instagram', match.group(1)
            elif '/tv/' in path:
                match = re.search(r'/tv/([^/?]+)', path)
                if match:
                    return 'instagram', match.group(1)
        
        # Vimeo
        elif _is_domain_match(netloc, 'vimeo.com'):
            match = re.search(r'/(\d+)', path)
            if match:
                return 'vimeo', match.group(1)
        
        # Dailymotion
        elif _is_domain_match(netloc, 'dailymotion.com') or _is_domain_match(netloc, 'dai.ly'):
            if '/video/' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'dailymotion', match.group(1)
        
        # Rutube
        elif _is_domain_match(netloc, 'rutube.ru'):
            if '/video/' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'rutube', match.group(1)
        
        # Twitch
        elif _is_domain_match(netloc, 'twitch.tv'):
            if '/videos/' in path:
                match = re.search(r'/videos/(\d+)', path)
                if match:
                    return 'twitch', match.group(1)
            elif '/clip/' in path:
                match = re.search(r'/clip/([^/?]+)', path)
                if match:
                    return 'twitch', match.group(1)
        
        # Boosty
        elif _is_domain_match(netloc, 'boosty.to'):
            if '/video/' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'boosty', match.group(1)
        
        # Odnoklassniki (Одноклассники)
        elif _is_domain_match(netloc, 'ok.ru'):
            if '/video/' in path:
                match = re.search(r'/video/(\d+)', path)
                if match:
                    return 'okru', match.group(1)
            elif '/group/' in path and 'video' in query:
                match = re.search(r'video=(\d+)', query)
                if match:
                    return 'okru', match.group(1)
        
        # Reddit
        elif _is_domain_match(netloc, 'reddit.com') or _is_domain_match(netloc, 'redd.it'):
            if '/comments/' in path:
                match = re.search(r'/comments/[^/]+/([^/?]+)', path)
                if match:
                    return 'reddit', match.group(1)
            elif '/r/' in path and '/comments/' in path:
                match = re.search(r'/comments/[^/]+/([^/?]+)', path)
                if match:
                    return 'reddit', match.group(1)
        
        # Pikabu
        elif _is_domain_match(netloc, 'pikabu.ru'):
            if '/story/' in path:
                match = re.search(r'/story/(\d+)', path)
                if match:
                    return 'pikabu', match.group(1)
        
        # Yandex.Dzen (Яндекс.Дзен)
        elif _is_domain_match(netloc, 'zen.yandex.ru'):
            if '/media/' in path:
                match = re.search(r'/media/([^/?]+)', path)
                if match:
                    return 'yandex_zen', match.group(1)
            elif '/video/' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'yandex_zen', match.group(1)
        
        # Google Drive
        elif _is_domain_match(netloc, 'drive.google.com') or _is_domain_match(netloc, 'docs.google.com'):
            if '/file/d/' in path:
                match = re.search(r'/file/d/([^/?]+)', path)
                if match:
                    return 'google_drive', match.group(1)
            elif '/open' in path:
                match = re.search(r'id=([^&]+)', query)
                if match:
                    return 'google_drive', match.group(1)
        
        # Redtube
        elif _is_domain_match(netloc, 'redtube.com'):
            if '/video/' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'redtube', match.group(1)
        
        # YouTube
        elif _is_domain_match(netloc, 'youtube.com') or _is_domain_match(netloc, 'youtu.be') or _is_domain_match(netloc, 'm.youtube.com') or _is_domain_match(netloc, 'music.youtube.com'):
            if _is_domain_match(netloc, 'youtu.be'):
                match = re.search(r'/([^/?]+)', path)
                if match:
                    return 'youtube', match.group(1)
            elif '/watch' in path:
                match = re.search(r'v=([^&]+)', query)
                if match:
                    return 'youtube', match.group(1)
            elif '/embed/' in path:
                match = re.search(r'/embed/([^/?]+)', path)
                if match:
                    return 'youtube', match.group(1)
            elif '/v/' in path:
                match = re.search(r'/v/([^/?]+)', path)
                if match:
                    return 'youtube', match.group(1)
            elif '/shorts/' in path:
                match = re.search(r'/shorts/([^/?]+)', path)
                if match:
                    return 'youtube', match.group(1)
        
        # Bilibili
        elif _is_domain_match(netloc, 'bilibili.com') or _is_domain_match(netloc, 'bilibili.tv') or _is_domain_match(netloc, 'bili.im'):
            if '/video/' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'bilibili', match.group(1)
        
        # Niconico
        elif _is_domain_match(netloc, 'nicovideo.jp'):
            if '/watch/' in path:
                match = re.search(r'/watch/([^/?]+)', path)
                if match:
                    return 'niconico', match.group(1)
        
        # XVideos
        elif _is_domain_match(netloc, 'xvideos.com') or _is_domain_match(netloc, 'xvideos3.com'):
            if '/video' in path:
                match = re.search(r'/video(\d+)', path)
                if match:
                    return 'xvideos', match.group(1)
        
        # XNXX
        elif _is_domain_match(netloc, 'xnxx.com') or _is_domain_match(netloc, 'xnxx.tv'):
            if '/video' in path:
                match = re.search(r'/video([^/?]+)', path)
                if match:
                    return 'xnxx', match.group(1)
        
        # YouPorn
        elif _is_domain_match(netloc, 'youporn.com'):
            if '/watch/' in path:
                match = re.search(r'/watch/(\d+)', path)
                if match:
                    return 'youporn', match.group(1)
        
        # XHamster
        elif _is_domain_match(netloc, 'xhamster.com') or _is_domain_match(netloc, 'fra.xhamster2.com') or _is_domain_match(netloc, 'xhamster1.desi') or _is_domain_match(netloc, 'xhchannel.com'):
            if '/videos/' in path:
                match = re.search(r'/videos/([^/?]+)', path)
                if match:
                    return 'xhamster', match.group(1)
        
        # PornTube
        elif _is_domain_match(netloc, 'porntube.com'):
            if '/videos/' in path:
                match = re.search(r'/videos/([^/?]+)', path)
                if match:
                    return 'porntube', match.group(1)
        
        # SpankBang
        elif _is_domain_match(netloc, 'spankbang.com'):
            if '/video/' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'spankbang', match.group(1)
        
        # OnlyFans
        elif _is_domain_match(netloc, 'onlyfans.com'):
            if '/v/' in path:
                match = re.search(r'/v/(\d+)', path)
                if match:
                    return 'onlyfans', match.group(1)
        
        # Patreon
        elif _is_domain_match(netloc, 'patreon.com'):
            if '/posts/' in path:
                match = re.search(r'/posts/(\d+)', path)
                if match:
                    return 'patreon', match.group(1)
        
        # SoundCloud
        elif _is_domain_match(netloc, 'soundcloud.com') or _is_domain_match(netloc, 'on.soundcloud.com'):
            if '/' in path and not path.startswith('/'):
                match = re.search(r'/([^/?]+)', path)
                if match:
                    return 'soundcloud', match.group(1)
        
        # Bandcamp
        elif _is_domain_match(netloc, 'bandcamp.com'):
            if '/track/' in path:
                match = re.search(r'/track/([^/?]+)', path)
                if match:
                    return 'bandcamp', match.group(1)
        
        # Mixcloud
        elif _is_domain_match(netloc, 'mixcloud.com'):
            if '/' in path and not path.startswith('/'):
                match = re.search(r'/([^/?]+)', path)
                if match:
                    return 'mixcloud', match.group(1)
        
        # Deezer
        elif _is_domain_match(netloc, 'deezer.com'):
            if '/track/' in path:
                match = re.search(r'/track/(\d+)', path)
                if match:
                    return 'deezer', match.group(1)
        
        # Spotify
        elif _is_domain_match(netloc, 'spotify.com'):
            if '/track/' in path:
                match = re.search(r'/track/([^/?]+)', path)
                if match:
                    return 'spotify', match.group(1)
        
        # Apple Music
        elif _is_domain_match(netloc, 'music.apple.com'):
            if '/album/' in path and '/track/' in path:
                match = re.search(r'/track/(\d+)', path)
                if match:
                    return 'apple_music', match.group(1)
        
        # Tidal
        elif _is_domain_match(netloc, 'tidal.com'):
            if '/track/' in path:
                match = re.search(r'/track/(\d+)', path)
                if match:
                    return 'tidal', match.group(1)
        
        # VK
        elif _is_domain_match(netloc, 'vk.com') or _is_domain_match(netloc, 'm.vk.com') or _is_domain_match(netloc, 'vkvideo.ru') or _is_domain_match(netloc, 'm.vkvideo.ru'):
            if '/video' in path:
                match = re.search(r'/video(-?\d+_\d+)', path)
                if match:
                    return 'vk', match.group(1)
        
        # TikTok
        elif _is_domain_match(netloc, 'tiktok.com') or _is_domain_match(netloc, 'vm.tiktok.com') or _is_domain_match(netloc, 'vt.tiktok.com'):
            if '/video/' in path:
                match = re.search(r'/video/(\d+)', path)
                if match:
                    return 'tiktok', match.group(1)
        
        # Twitter/X
        elif _is_domain_match(netloc, 'twitter.com') or _is_domain_match(netloc, 'x.com'):
            if '/status/' in path:
                match = re.search(r'/status/(\d+)', path)
                if match:
                    return 'twitter', match.group(1)
        
        # Facebook
        elif _is_domain_match(netloc, 'facebook.com'):
            if '/reel/' in path:
                match = re.search(r'/reel/(\d+)', path)
                if match:
                    return 'facebook', match.group(1)
            elif '/watch/' in path:
                match = re.search(r'v=(\d+)', query)
                if match:
                    return 'facebook', match.group(1)
        
        # Pornhub
        elif _is_domain_match(netloc, 'pornhub.com') or _is_domain_match(netloc, 'pornhub.org') or _is_domain_match(netloc, 'cn.pornhub.com') or _is_domain_match(netloc, 'de.pornhub.org') or _is_domain_match(netloc, 'es.pornhub.com') or _is_domain_match(netloc, 'fr.pornhub.com') or _is_domain_match(netloc, 'it.pornhub.com') or _is_domain_match(netloc, 'rt.pornhub.com') or _is_domain_match(netloc, 'rt.pornhub.org'):
            if '/view_video.php' in path:
                match = re.search(r'viewkey=([^&]+)', query)
                if match:
                    return 'pornhub', match.group(1)
            elif '/video' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'pornhub', match.group(1)
        
        # Kick.com
        elif _is_domain_match(netloc, 'kick.com'):
            if '/video/' in path:
                match = re.search(r'/video/(\d+)', path)
                if match:
                    return 'kick', match.group(1)
        
        # RedGifs
        elif _is_domain_match(netloc, 'redgifs.com'):
            if '/watch/' in path:
                match = re.search(r'/watch/([^/?]+)', path)
                if match:
                    return 'redgifs', match.group(1)
        
        # Snapchat
        elif _is_domain_match(netloc, 'snapchat.com'):
            if '/story/' in path:
                match = re.search(r'/story/([^/?]+)', path)
                if match:
                    return 'snapchat', match.group(1)
        
        # TNAFlix
        elif _is_domain_match(netloc, 'tnaflix.com') or _is_domain_match(netloc, 'm.tnaflix.com'):
            if '/video/' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'tnaflix', match.group(1)
        
        # Eporner
        elif _is_domain_match(netloc, 'eporner.com'):
            if '/video/' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'eporner', match.group(1)
        
        # Pornzog
        elif _is_domain_match(netloc, 'pornzog.com'):
            if '/video/' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'pornzog', match.group(1)
        
        # Porntrex
        elif _is_domain_match(netloc, 'porntrex.com'):
            if '/video/' in path:
                match = re.search(r'/video/([^/?]+)', path)
                if match:
                    return 'porntrex', match.group(1)
        
        # CuriosityStream
        elif _is_domain_match(netloc, 'curiositystream.com'):
            if '/video/' in path:
                match = re.search(r'/video/(\d+)', path)
                if match:
                    return 'curiositystream', match.group(1)
        
        # Google variants
        elif _is_domain_match(netloc, 'google.com') or _is_domain_match(netloc, 'share.google.com'):
            if '/file/d/' in path:
                match = re.search(r'/file/d/([^/?]+)', path)
                if match:
                    return 'google_drive', match.group(1)
            elif '/open' in path:
                match = re.search(r'id=([^&]+)', query)
                if match:
                    return 'google_drive', match.group(1)
        
        # Pinterest
        elif _is_domain_match(netloc, 'pin.it'):
            return 'pinterest', ''
        
        # Vidyard
        elif _is_domain_match(netloc, 'share.vidyard.com'):
            if '/watch/' in path:
                match = re.search(r'/watch/([^/?]+)', path)
                if match:
                    return 'vidyard', match.group(1)
        
        return 'unknown', ''
    except Exception as e:
        logger.warning(f"Error in extract_service_info: {e}")
        return 'unknown', ''


# Services with direct thumbnail URLs are handled below
# All other services use yt-dlp fallback automatically


def download_vimeo_thumbnail(video_id: str, dest: str) -> bool:
    """Download Vimeo video thumbnail"""
    try:
        # Vimeo API endpoint for video info
        api_url = f"https://vimeo.com/api/v2/video/{video_id}.json"
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data and len(data) > 0:
                video_info = data[0]
                thumbnail_url = video_info.get('thumbnail_large') or video_info.get('thumbnail_medium')
                if thumbnail_url:
                    # Валидация URL для предотвращения SSRF
                    is_valid, error_msg = _validate_url_for_ssrf(thumbnail_url)
                    if not is_valid:
                        logger.warning(f"Invalid thumbnail URL from Vimeo API: {error_msg}")
                        return False
                    img_response = requests.get(thumbnail_url, timeout=10)
                    if img_response.status_code == 200:
                        with open(dest, 'wb') as f:
                            f.write(img_response.content)
                        return True
        return False
    except Exception as e:
        logger.warning(LoggerMsg.THUMBNAIL_DOWNLOADER_VIMEO_FAILED_LOG_MSG.format(e=e))
        return False


def download_dailymotion_thumbnail(video_id: str, dest: str) -> bool:
    """Download Dailymotion video thumbnail"""
    try:
        # Dailymotion API endpoint
        api_url = f"https://api.dailymotion.com/video/{video_id}?fields=thumbnail_large_url"
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            thumbnail_url = data.get('thumbnail_large_url')
            if thumbnail_url:
                # Валидация URL для предотвращения SSRF
                is_valid, error_msg = _validate_url_for_ssrf(thumbnail_url)
                if not is_valid:
                    logger.warning(f"Invalid thumbnail URL from Dailymotion API: {error_msg}")
                    return False
                img_response = requests.get(thumbnail_url, timeout=10)
                if img_response.status_code == 200:
                    with open(dest, 'wb') as f:
                        f.write(img_response.content)
                    return True
        return False
    except Exception as e:
        logger.warning(LoggerMsg.THUMBNAIL_DOWNLOADER_DAILYMOTION_FAILED_LOG_MSG.format(e=e))
        return False


def download_youtube_thumbnail(video_id: str, dest: str) -> bool:
    """Download YouTube video thumbnail"""
    try:
        # YouTube thumbnail URLs
        thumbnail_urls = [
            f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
            f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
            f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg",
            f"https://img.youtube.com/vi/{video_id}/sddefault.jpg",
            f"https://img.youtube.com/vi/{video_id}/default.jpg"
        ]
        
        for url in thumbnail_urls:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200 and len(response.content) > 1000:  # Check if image is valid
                    with open(dest, 'wb') as f:
                        f.write(response.content)
                    return True
            except Exception:
                continue
        
        return False
    except Exception as e:
        logger.warning(LoggerMsg.THUMBNAIL_DOWNLOADER_YOUTUBE_FAILED_LOG_MSG.format(e=e))
        return False


def download_thumbnail_via_ytdlp(url: str, dest: str, user_id: Optional[int] = None) -> bool:
    """
    Download thumbnail using yt-dlp as fallback
    Uses yt-dlp's --write-thumbnail option without downloading the video
    Never raises exceptions - returns False on error
    """
    temp_dir = None
    try:
        logger.info(f"Attempting to download thumbnail via yt-dlp for URL: {url}")
        
        # Create temporary directory for yt-dlp output
        temp_dir = tempfile.mkdtemp(prefix="ytdlp_thumb_")
        
        # Determine output template - yt-dlp will add extension automatically
        base_name = os.path.splitext(os.path.basename(dest))[0]
        outtmpl = os.path.join(temp_dir, base_name)
        
        # yt-dlp options for thumbnail extraction only
        ytdl_opts = {
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,  # Don't download video
            'writethumbnail': True,  # Write thumbnail
            'write_all_thumbnails': False,  # Only write best thumbnail
            'outtmpl': outtmpl,
            'noplaylist': True,
            'extract_flat': False,
        }
        
        # Add cookies if available
        if user_id:
            try:
                user_cookie_path = os.path.join("users", str(user_id), "cookie.txt")
                if os.path.exists(user_cookie_path):
                    ytdl_opts['cookiefile'] = user_cookie_path
            except Exception:
                pass  # Ignore cookie errors
        
        # Add proxy configuration if needed
        try:
            from HELPERS.proxy_helper import add_proxy_to_ytdl_opts
            ytdl_opts = add_proxy_to_ytdl_opts(ytdl_opts, url)
        except Exception:
            pass  # Proxy helper might not be available
        
        # Add PO token for YouTube if available
        try:
            from HELPERS.pot_helper import add_pot_to_ytdl_opts
            ytdl_opts = add_pot_to_ytdl_opts(ytdl_opts, url)
        except Exception:
            pass  # PO token helper might not be available
        
        # Extract thumbnail using yt-dlp
        try:
            with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            logger.warning(f"yt-dlp download failed: {e}")
            return False
        
        # Find downloaded thumbnail file
        # yt-dlp saves thumbnails with various extensions
        thumbnail_extensions = ['.jpg', '.jpeg', '.png', '.webp']
        downloaded_thumb = None
        
        # First, try exact match with extensions
        for ext in thumbnail_extensions:
            possible_path = outtmpl + ext
            if os.path.exists(possible_path):
                downloaded_thumb = possible_path
                break
        
        # If not found, search all files in temp_dir for thumbnail files
        if not downloaded_thumb and temp_dir:
            try:
                for file in os.listdir(temp_dir):
                    file_lower = file.lower()
                    # Check if file has a thumbnail extension
                    if any(file_lower.endswith(ext) for ext in thumbnail_extensions):
                        file_path = os.path.join(temp_dir, file)
                        if os.path.isfile(file_path):
                            downloaded_thumb = file_path
                            break
            except Exception:
                pass
        
        # Last resort: find any file that starts with base_name
        if not downloaded_thumb and temp_dir:
            try:
                for file in os.listdir(temp_dir):
                    if file.startswith(base_name):
                        file_path = os.path.join(temp_dir, file)
                        if os.path.isfile(file_path):
                            downloaded_thumb = file_path
                            break
            except Exception:
                pass
        
        if downloaded_thumb and os.path.exists(downloaded_thumb):
            # Copy thumbnail to destination
            try:
                shutil.copy2(downloaded_thumb, dest)
                logger.info(f"Successfully downloaded thumbnail via yt-dlp: {dest}")
                return True
            except Exception as e:
                logger.warning(f"Failed to copy thumbnail: {e}")
                return False
        
        return False
        
    except Exception as e:
        logger.warning(f"Failed to download thumbnail via yt-dlp: {e}")
        return False
    finally:
        # Cleanup temp directory
        if temp_dir:
            try:
                shutil.rmtree(temp_dir)
            except Exception:
                pass


def download_thumbnail(url: str, dest: str, user_id: Optional[int] = None, app=None, message=None) -> bool:
    """
    Universal thumbnail downloader for various video services
    Returns True if thumbnail was downloaded successfully, False otherwise
    Never raises exceptions - always returns False on error
    
    Args:
        url: Video URL
        dest: Destination path for thumbnail
        user_id: Optional user ID for cookies and proxy configuration
        app: Optional Pyrogram app instance for Telegram embed extraction
        message: Optional Telegram message object for Telegram embed extraction
    """
    try:
        service, video_id = extract_service_info(url)
        
        logger.info(LoggerMsg.THUMBNAIL_DOWNLOADER_UNIVERSAL_CALLED_LOG_MSG.format(url=url))
        logger.info(LoggerMsg.THUMBNAIL_DOWNLOADER_SERVICE_DETECTED_LOG_MSG.format(service=service, video_id=video_id))
        
        # For some services (like pinterest), video_id might be empty but we can still try yt-dlp
        if not video_id:
            logger.info(f"No video ID extracted, trying yt-dlp fallback directly")
            # Create destination directory if it doesn't exist
            try:
                dest_dir = os.path.dirname(dest)
                if dest_dir:
                    os.makedirs(dest_dir, exist_ok=True)
            except Exception as e:
                logger.warning(f"Failed to create destination directory: {e}")
            
            if download_thumbnail_via_ytdlp(url, dest, user_id):
                return True
            return False
        
        # Create destination directory if it doesn't exist
        try:
            dest_dir = os.path.dirname(dest)
            if dest_dir:
                os.makedirs(dest_dir, exist_ok=True)
        except Exception as e:
            logger.warning(f"Failed to create destination directory: {e}")
        
        # Services with direct thumbnail URLs (no metadata needed)
        services_with_direct_urls = {'youtube', 'vimeo', 'dailymotion'}
        
        # Try service-specific thumbnail download only for services with direct URLs
        success = False
        if service == 'youtube':
            try:
                success = download_youtube_thumbnail(video_id, dest)
            except Exception as e:
                logger.warning(f"YouTube thumbnail download error: {e}")
                success = False
        elif service == 'vimeo':
            try:
                success = download_vimeo_thumbnail(video_id, dest)
            except Exception as e:
                logger.warning(f"Vimeo thumbnail download error: {e}")
                success = False
        elif service == 'dailymotion':
            try:
                success = download_dailymotion_thumbnail(video_id, dest)
            except Exception as e:
                logger.warning(f"Dailymotion thumbnail download error: {e}")
                success = False
        
        if success:
            logger.info(LoggerMsg.THUMBNAIL_DOWNLOADER_SUCCESS_LOG_MSG.format(service=service, dest=dest))
            return True
        
        # Try Telegram embed extraction (before yt-dlp fallback)
        if app and message:
            try:
                if get_thumbnail_from_telegram_embed(app, message, dest):
                    logger.info(f"Successfully downloaded thumbnail from Telegram embed: {dest}")
                    return True
            except Exception as e:
                logger.warning(f"Telegram embed extraction failed: {e}")
        
        # For all other services (or if direct URL method failed), use yt-dlp fallback
        if service not in services_with_direct_urls:
            logger.info(f"Service {service} uses metadata thumbnails, trying yt-dlp fallback")
        else:
            logger.info(LoggerMsg.THUMBNAIL_DOWNLOADER_SERVICE_FAILED_LOG_MSG.format(service=service))
            logger.info(f"Direct URL method failed, trying yt-dlp fallback")
        
        # Try yt-dlp fallback
        if download_thumbnail_via_ytdlp(url, dest, user_id):
            logger.info(f"Successfully downloaded thumbnail via yt-dlp fallback: {dest}")
            return True
        
        return False
        
    except Exception as e:
        logger.error(LoggerMsg.THUMBNAIL_DOWNLOADER_ERROR_LOG_MSG.format(e=e))
        return False


def get_thumbnail_from_telegram_embed(app, message, dest: str) -> bool:
    """
    Attempt to extract thumbnail from Telegram's video embed
    Checks message.web_page.photo and message.reply_to_message.web_page.photo
    Never raises exceptions - returns False on error
    
    Args:
        app: Pyrogram app instance
        message: Telegram message object (can be None)
        dest: Destination path for thumbnail
    """
    try:
        if not app or not message:
            return False
        
        # Create destination directory if it doesn't exist
        try:
            dest_dir = os.path.dirname(dest)
            if dest_dir:
                os.makedirs(dest_dir, exist_ok=True)
        except Exception as e:
            logger.warning(f"Failed to create destination directory for Telegram embed: {e}")
            return False
        
        # Try to get photo from message.web_page (current message embed)
        photo = None
        if hasattr(message, 'web_page') and message.web_page:
            if hasattr(message.web_page, 'photo') and message.web_page.photo:
                photo = message.web_page.photo
                logger.info("Found photo in message.web_page.photo")
        
        # If not found, try reply_to_message (original user message)
        if not photo and hasattr(message, 'reply_to_message') and message.reply_to_message:
            reply_msg = message.reply_to_message
            if hasattr(reply_msg, 'web_page') and reply_msg.web_page:
                if hasattr(reply_msg.web_page, 'photo') and reply_msg.web_page.photo:
                    photo = reply_msg.web_page.photo
                    logger.info("Found photo in reply_to_message.web_page.photo")
            
            # Also check if reply message itself has a photo
            if not photo and hasattr(reply_msg, 'photo') and reply_msg.photo:
                photo = reply_msg.photo
                logger.info("Found photo in reply_to_message.photo")
        
        # Also check current message photo
        if not photo and hasattr(message, 'photo') and message.photo:
            photo = message.photo
            logger.info("Found photo in message.photo")
        
        if photo:
            try:
                # Download photo using Pyrogram
                downloaded_path = app.download_media(photo, file_name=dest)
                if downloaded_path and os.path.exists(downloaded_path):
                    # If downloaded path is different from dest, copy it
                    if downloaded_path != dest:
                        try:
                            shutil.copy2(downloaded_path, dest)
                            # Try to remove temporary file if it's in temp directory
                            if 'temp' in downloaded_path.lower() or 'tmp' in downloaded_path.lower():
                                try:
                                    os.remove(downloaded_path)
                                except Exception:
                                    pass
                        except Exception as e:
                            logger.warning(f"Failed to copy downloaded photo: {e}")
                            # If copy failed but file exists, use downloaded path
                            if os.path.exists(downloaded_path):
                                return True
                    
                    logger.info(f"Successfully downloaded thumbnail from Telegram embed: {dest}")
                    return True
            except Exception as e:
                logger.warning(f"Failed to download photo from Telegram embed: {e}")
                return False
        
        return False
    except Exception as e:
        logger.warning(LoggerMsg.THUMBNAIL_DOWNLOADER_TELEGRAM_EMBED_FAILED_LOG_MSG.format(e=e))
        return False
