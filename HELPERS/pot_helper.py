# PO Token Helper for YouTube
# Adds PO token provider support for YouTube domains

import requests
import time
import re
from CONFIG.config import Config
from CONFIG.messages import Messages, safe_get_messages
from URL_PARSERS.youtube import is_youtube_url
from HELPERS.logger import logger

# Кэш для проверки доступности PO token провайдера
_pot_provider_cache = {
    'available': None,
    'last_check': 0,
    'check_interval': 30  # Проверяем каждые 30 секунд
}

def check_pot_provider_availability(base_url: str) -> bool:
    """
    Проверяет доступность PO token провайдера
    
    Args:
        base_url (str): URL провайдера
        
    Returns:
        bool: True если провайдер доступен, False иначе
    """
    current_time = time.time()
    
    # Проверяем кэш
    if (_pot_provider_cache['available'] is not None and 
        current_time - _pot_provider_cache['last_check'] < _pot_provider_cache['check_interval']):
        return _pot_provider_cache['available']
    
    try:
        # Валидация URL для предотвращения SSRF (но разрешаем localhost для локального сервиса)
        from urllib.parse import urlparse
        import ipaddress
        parsed_url = urlparse(base_url)
        url_host = (parsed_url.hostname or '').lower()
        # Разрешаем localhost для локального PO token провайдера, но блокируем другие внутренние ресурсы
        if url_host not in ('localhost', '127.0.0.1', '::1') and \
           (url_host.endswith('.local') or url_host.endswith('.internal') or 'localhost' in url_host):
            try:
                ip = ipaddress.ip_address(url_host)
                if (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or str(ip) == '169.254.169.254') and \
                   str(ip) not in ('127.0.0.1', '::1'):
                    logger.warning(f"Blocked SSRF attempt: invalid PO token provider URL {base_url}")
                    _pot_provider_cache['available'] = False
                    _pot_provider_cache['last_check'] = current_time
                    return False
            except ValueError:
                pass
        
        # Быстрая проверка доступности провайдера (всегда локально, в обход прокси — сервис на том же сервере/в докере)
        # PO token провайдер может возвращать 404 для корневого пути, но это означает что сервис работает
        response = requests.get(base_url, timeout=5, proxies={'http': None, 'https': None})
        is_available = response.status_code in [200, 404]  # 404 означает что сервис работает, но эндпоинт не найден
        
        # Обновляем кэш
        _pot_provider_cache['available'] = is_available
        _pot_provider_cache['last_check'] = current_time
        
        if is_available:
            logger.info(f"PO token provider is available at {base_url} (status: {response.status_code})")
        else:
            logger.warning(f"PO token provider returned status {response.status_code} at {base_url}")
        
        return is_available
        
    except requests.exceptions.RequestException as e:
        logger.warning(f"PO token provider is not available at {base_url}: {e}")
        
        # Обновляем кэш
        _pot_provider_cache['available'] = False
        _pot_provider_cache['last_check'] = current_time
        
        return False

def add_pot_to_ytdl_opts(ytdl_opts: dict, url: str) -> dict:
    """
    Добавляет PO token аргументы к yt-dlp опциям для YouTube доменов
    
    Args:
        ytdl_opts (dict): Словарь опций yt-dlp
        url (str): URL для проверки
        
    Returns:
        dict: Обновленный словарь опций yt-dlp
    """
    # Проверяем, включен ли PO token провайдер
    if not getattr(Config, 'YOUTUBE_POT_ENABLED', False):
        messages = safe_get_messages()
        logger.info(messages.HELPER_POT_PROVIDER_DISABLED_MSG)
        return ytdl_opts
    
    # Проверяем, является ли URL YouTube доменом
    if not is_youtube_url(url):
        messages = safe_get_messages()
        logger.info(messages.HELPER_POT_URL_NOT_YOUTUBE_MSG.format(url=url))
        return ytdl_opts
    
    # Получаем базовый URL провайдера
    base_url = getattr(Config, 'YOUTUBE_POT_BASE_URL', 'http://127.0.0.1:4416')
    disable_innertube = getattr(Config, 'YOUTUBE_POT_DISABLE_INNERTUBE', False)
    
    # Проверяем доступность PO token провайдера
    if not check_pot_provider_availability(base_url):
        messages = safe_get_messages()
        logger.warning(messages.HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG.format(base_url=base_url))
        return ytdl_opts

    # Добавляем extractor_args к опциям yt-dlp
    if 'extractor_args' not in ytdl_opts:
        ytdl_opts['extractor_args'] = {}
    
    # Добавляем аргументы для YouTube PO token провайдера в правильном формате (nightly ≥ 2025-09-13)
    # Структура:
    # extractor_args: {
    #   'youtubepot': {
    #       'providers': ['bgutilhttp'],
    #       'bgutilhttp': { 'base_url': ['http://...'] },
    #       'disable_innertube': ['1']  # опционально
    #   }
    # }
    pot_args = ytdl_opts['extractor_args'].get('youtubepot', {})
    pot_args['providers'] = list(dict.fromkeys((pot_args.get('providers') or []) + ['bgutilhttp']))
    bg_cfg = pot_args.get('bgutilhttp', {})
    bg_cfg['base_url'] = [base_url]
    pot_args['bgutilhttp'] = bg_cfg
    if disable_innertube:
        pot_args['disable_innertube'] = ["1"]
    ytdl_opts['extractor_args']['youtubepot'] = pot_args
    
    # Добавляем verbose режим для детального логирования PO токенов
    ytdl_opts['verbose'] = True
    
    # Добавляем хук для отладки PO токенов
    ytdl_opts = add_pot_debug_hook(ytdl_opts)
    
    # Явные логи, чтобы видно было активные провайдеры
    active_providers = ytdl_opts['extractor_args'].get('youtubepot', {}).get('providers', [])
    logger.info(f"🔑 PO TOKEN PROVIDER ENABLED for YouTube URL: {url}")
    logger.info(f"🔗 PO Token Base URL: {base_url}")
    logger.info(f"🧩 PO Token Providers: {active_providers}")
    logger.info(f"⚙️  PO Token Config: disable_innertube={disable_innertube}")
    logger.info(f"📋 extractor_args.youtubepot: {ytdl_opts['extractor_args'].get('youtubepot')}")
    
    return ytdl_opts

def is_pot_enabled() -> bool:
    """
    Проверяет, включен ли PO token провайдер в конфигурации
    
    Returns:
        bool: True если включен, False иначе
    """
    return getattr(Config, 'YOUTUBE_POT_ENABLED', False)

def get_pot_base_url() -> str:
    """
    Возвращает базовый URL PO token провайдера
    
    Returns:
        str: Базовый URL провайдера
    """
    return getattr(Config, 'YOUTUBE_POT_BASE_URL', 'http://127.0.0.1:4416')

def clear_pot_provider_cache():
    messages = safe_get_messages(None)
    """
    Сбрасывает кэш проверки доступности PO token провайдера
    Полезно для принудительной повторной проверки после восстановления провайдера
    """
    global _pot_provider_cache
    _pot_provider_cache['available'] = None
    _pot_provider_cache['last_check'] = 0
    messages = safe_get_messages()
    logger.info(messages.HELPER_POT_PROVIDER_CACHE_CLEARED_MSG)

def is_pot_provider_available() -> bool:
    """
    Проверяет, доступен ли PO token провайдер (с учетом кэша)
    
    Returns:
        bool: True если провайдер доступен, False иначе
    """
    base_url = getattr(Config, 'YOUTUBE_POT_BASE_URL', 'http://127.0.0.1:4416')
    return check_pot_provider_availability(base_url)

def create_pot_debug_hook():
    messages = safe_get_messages(None)
    """
    Создает хук для yt-dlp, который перехватывает и логирует PO токены
    
    Returns:
        function: Хук функция для yt-dlp
    """
    def pot_debug_hook(d):
        messages = safe_get_messages(None)
        """
        Хук для перехватывания PO токенов в yt-dlp
        
        Args:
            d (dict): Словарь с информацией о загрузке
        """
        if d['status'] == 'downloading':
            # Ищем PO токены в URL или заголовках
            if 'url' in d:
                url = d['url']
                # Проверяем наличие PO токенов в URL
                pot_patterns = [
                    r'po_token=([^&]+)',
                    r'popt=([^&]+)',
                    r'pot=([^&]+)',
                    r'proof_of_origin=([^&]+)'
                ]
                
                for pattern in pot_patterns:
                    match = re.search(pattern, url)
                    if match:
                        token = match.group(1)
                        logger.info(f"🎯 PO TOKEN DETECTED in URL: {token[:20]}...")
                        logger.info(f"🔗 Full URL with PO token: {url}")
                        break
                
                # Проверяем заголовки на наличие PO токенов
                if 'http_headers' in d:
                    headers = d['http_headers']
                    for header_name, header_value in headers.items():
                        if 'po' in header_name.lower() or 'token' in header_name.lower():
                            logger.info(f"🎯 PO TOKEN in header {header_name}: {header_value}")
        
        elif d['status'] == 'finished':
            # Логируем успешное завершение с PO токенами
            messages = safe_get_messages()
            logger.info(messages.HELPER_DOWNLOAD_FINISHED_PO_MSG)
            
    return pot_debug_hook

def add_pot_debug_hook(ytdl_opts: dict) -> dict:
    """
    Добавляет хук для отладки PO токенов к опциям yt-dlp
    
    Args:
        ytdl_opts (dict): Словарь опций yt-dlp
        
    Returns:
        dict: Обновленный словарь опций yt-dlp
    """
    if 'progress_hooks' not in ytdl_opts:
        ytdl_opts['progress_hooks'] = []
    
    # Добавляем наш хук для отладки PO токенов
    ytdl_opts['progress_hooks'].append(create_pot_debug_hook())
    
    return ytdl_opts

def build_cli_extractor_args(url: str) -> list[str]:
    """
    Формирует аргументы CLI для yt-dlp (--extractor-args) с поддержкой PO token.
    Возвращает список вида ["--extractor-args", VALUE], либо пустой список если не нужно добавлять.
    """
    try:
        # Проверяем включение и домен
        if not getattr(Config, 'YOUTUBE_POT_ENABLED', False):
            return []
        if not is_youtube_url(url):
            return []
        base_url = getattr(Config, 'YOUTUBE_POT_BASE_URL', 'http://127.0.0.1:4416')
        disable_innertube = getattr(Config, 'YOUTUBE_POT_DISABLE_INNERTUBE', False)

        # CLI синтаксис для подпровайдера: youtubepot-bgutilhttp:base_url=...;disable_innertube=1
        pot_segment = f"youtubepot-bgutilhttp:base_url={base_url}"
        if disable_innertube:
            pot_segment += ";disable_innertube=1"

        # Дополнительные extractor-args (через запятую между неймспейсами)
        messages = safe_get_messages()
        generic_args = messages.HELPER_POT_GENERIC_ARGS_MSG
        value = ",".join([pot_segment, generic_args])
        logger.info(f"🧱 CLI extractor-args built for POT: {value}")
        return ['--extractor-args', value]
    except Exception as e:
        logger.warning(f"Failed to build CLI extractor-args for POT: {e}")
        return []
