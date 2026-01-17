import yt_dlp
import logging
import os
from urllib.parse import quote
from COMMANDS.proxy_cmd import get_proxy_config
from CONFIG.messages import Messages, safe_get_messages
from HELPERS.pot_helper import add_pot_to_ytdl_opts
from URL_PARSERS.youtube import is_youtube_url

logger = logging.getLogger(__name__)

def get_direct_link_with_proxy(url: str, format_spec: str = "bv+ba/best", user_id: int = None) -> dict:
    """
    Get direct stream link using proxy
    
    Args:
        url (str): Video URL
        format_spec (str): Format specification for yt-dlp
        
    Returns:
        dict: Dictionary with direct links for different players
    """
    try:
        # Get proxy configuration
        proxy_config = get_proxy_config()
        
        # Configure yt-dlp options with proxy
        ydl_opts = {
            'format': format_spec,
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'nocheckcertificate': True,
            'ignoreerrors': False,
        }
        
        # Add proxy configuration
        if proxy_config and 'type' in proxy_config and 'ip' in proxy_config and 'port' in proxy_config:
            if proxy_config['type'] == 'http':
                if proxy_config.get('user') and proxy_config.get('password'):
                    proxy_url = f"http://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
                else:
                    proxy_url = f"http://{proxy_config['ip']}:{proxy_config['port']}"
            elif proxy_config['type'] == 'https':
                if proxy_config.get('user') and proxy_config.get('password'):
                    proxy_url = f"https://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
                else:
                    proxy_url = f"https://{proxy_config['ip']}:{proxy_config['port']}"
            elif proxy_config['type'] in ['socks4', 'socks5', 'socks5h']:
                if proxy_config.get('user') and proxy_config.get('password'):
                    proxy_url = f"{proxy_config['type']}://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
                else:
                    proxy_url = f"{proxy_config['type']}://{proxy_config['ip']}:{proxy_config['port']}"
            else:
                if proxy_config.get('user') and proxy_config.get('password'):
                    proxy_url = f"http://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
                else:
                    proxy_url = f"http://{proxy_config['ip']}:{proxy_config['port']}"
            
            ydl_opts['proxy'] = proxy_url
            logger.info(f"Using proxy for yt-dlp: {proxy_url}")
        else:
            messages = safe_get_messages(user_id)
            logger.warning(messages.HELPER_PROXY_CONFIG_INCOMPLETE_MSG)
        
        # Add cookie file for YouTube if user_id is provided
        #if user_id and 'youtube.com' in url or 'youtu.be' in url:
        if user_id:
            messages = safe_get_messages(user_id)
            cookie_path = messages.HELPER_PROXY_COOKIE_PATH_MSG.format(user_id=user_id)
            if os.path.exists(cookie_path):
                ydl_opts['cookiefile'] = cookie_path
        
        # Extract video info
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
        if not info:
            raise Exception("Failed to extract video information")
            
        # Get the best format URL
        if 'url' in info:
            direct_url = info['url']
        elif 'formats' in info and info['formats']:
            # Get the best format
            best_format = None
            for fmt in info['formats']:
                if fmt.get('vcodec') != 'none' and fmt.get('acodec') != 'none':
                    best_format = fmt
                    break
            if not best_format:
                best_format = info['formats'][0]
            direct_url = best_format['url']
        else:
            raise Exception("No direct URL found")
            
        # Create player-specific URLs
        encoded_url = quote(direct_url, safe='')
        
        # Parse URL to get host and path for Android intent
        from urllib.parse import urlparse
        parsed_url = urlparse(direct_url)
        scheme = parsed_url.scheme
        host_path = f"{parsed_url.netloc}{parsed_url.path}"
        if parsed_url.query:
            host_path += f"?{parsed_url.query}"
        if parsed_url.fragment:
            host_path += f"#{parsed_url.fragment}"
        
        player_urls = {
            'direct': direct_url,
            'vlc_ios': f"vlc-x-callback://x-callback-url/stream?url={encoded_url}",
            'vlc_android': f"intent://{host_path}#Intent;scheme={scheme};package=org.videolan.vlc;type=video/*;end"
        }
        
        return {
            'success': True,
            'title': info.get('title', 'Unknown'),
            'duration': info.get('duration', 0),
            'player_urls': player_urls
        }
        
    except Exception as e:
        logger.error(f"Error getting direct link with proxy: {e}")
        return {
            'success': False,
            'error': str(e)
        }

def build_proxy_url(proxy_config):
    """Build proxy URL from configuration"""
    if not proxy_config or 'type' not in proxy_config or 'ip' not in proxy_config or 'port' not in proxy_config:
        return None
    
    if proxy_config['type'] == 'http':
        if proxy_config.get('user') and proxy_config.get('password'):
            return f"http://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
        else:
            return f"http://{proxy_config['ip']}:{proxy_config['port']}"
    elif proxy_config['type'] == 'https':
        if proxy_config.get('user') and proxy_config.get('password'):
            return f"https://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
        else:
            return f"https://{proxy_config['ip']}:{proxy_config['port']}"
    elif proxy_config['type'] in ['socks4', 'socks5', 'socks5h']:
        if proxy_config.get('user') and proxy_config.get('password'):
            return f"{proxy_config['type']}://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
        else:
            return f"{proxy_config['type']}://{proxy_config['ip']}:{proxy_config['port']}"
    else:
        if proxy_config.get('user') and proxy_config.get('password'):
            return f"http://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
        else:
            return f"http://{proxy_config['ip']}:{proxy_config['port']}"

def add_proxy_to_ytdl_opts(ytdl_opts: dict, url: str, user_id: int = None) -> dict:
    """Add proxy to yt-dlp options if proxy is enabled for user or domain requires it"""
    logger.info(f"add_proxy_to_ytdl_opts called: user_id={user_id}, url={url}")
    
    # ГЛОБАЛЬНАЯ ЗАЩИТА: Инициализируем messages
    messages = safe_get_messages(user_id)
    
    # Priority 1: Check if user has selected a country from proxy file
    if user_id:
        try:
            from COMMANDS.proxy_cmd import get_proxy_url_for_user_country
            country_proxy_url, selected_country = get_proxy_url_for_user_country(user_id)
            if country_proxy_url:
                ytdl_opts['proxy'] = country_proxy_url
                logger.info(f"Using proxy from file for country {selected_country}: {country_proxy_url}")
                return ytdl_opts
        except Exception as e:
            logger.warning(f"Error checking country proxy for user {user_id}: {e}")
            pass
    
    # Priority 2: Check if user has proxy enabled (ALL AUTO mode) - uses first available proxy
    # (Config first, then file) - full rotation happens in try_with_proxy_fallback
    if user_id:
        try:
            from COMMANDS.proxy_cmd import is_proxy_enabled
            proxy_enabled = is_proxy_enabled(user_id)
            logger.info(f"User {user_id} proxy enabled: {proxy_enabled}")
            if proxy_enabled:
                # Try Config proxies first
                proxy_config = select_proxy_for_user()
                if proxy_config:
                    proxy_url = build_proxy_url(proxy_config)
                    if proxy_url:
                        ytdl_opts['proxy'] = proxy_url
                        logger.info(f"Added user proxy from Config for {user_id} (ALL AUTO mode): {proxy_url}")
                        return ytdl_opts
                
                # If no Config proxies, try first proxy from file
                try:
                    from HELPERS.proxy_file_helper import get_all_proxies_from_file
                    file_proxies = get_all_proxies_from_file("TXT/proxy.txt")
                    if file_proxies:
                        proxy_url = file_proxies[0]['proxy_url']
                        ytdl_opts['proxy'] = proxy_url
                        logger.info(f"Added user proxy from file for {user_id} (ALL AUTO mode): {proxy_url}")
                        return ytdl_opts
                except Exception as e:
                    logger.warning(f"Error loading proxies from file: {e}")
        except Exception as e:
            logger.warning(f"Error checking proxy for user {user_id}: {e}")
            pass
    
    # Priority 3: Check if domain requires specific proxy (only if user proxy is OFF)
    logger.info(f"Checking domain-specific proxy for {url}")
    proxy_config = select_proxy_for_domain(url)
    if proxy_config:
        proxy_url = build_proxy_url(proxy_config)
        if proxy_url:
            ytdl_opts['proxy'] = proxy_url
            logger.info(f"Added domain-specific proxy for {url}: {proxy_url}")
        else:
            logger.warning(f"Failed to build proxy URL from config: {proxy_config}")
    else:
        logger.info(f"No domain-specific proxy found for {url}")
    
    return ytdl_opts

def try_with_proxy_fallback(ytdl_opts: dict, url: str, user_id: int = None, operation_func=None, *args, **kwargs):
    """
    Try operation with different proxies in case of failure when user proxy is enabled
    
    Args:
        ytdl_opts: yt-dlp options
        url: URL to process
        user_id: User ID
        operation_func: Function to call with ytdl_opts
        *args, **kwargs: Additional arguments for operation_func
    
    Returns:
        Result of operation_func or None if all proxies failed
    """
    messages = safe_get_messages(user_id)
    if not operation_func:
        return None
    
    # Check if user has proxy enabled
    if not user_id:
        # No user ID, try without proxy fallback
        return operation_func(ytdl_opts, *args, **kwargs)
    
    try:
        from COMMANDS.proxy_cmd import is_proxy_enabled
        proxy_enabled = is_proxy_enabled(user_id)
        if not proxy_enabled:
            # User proxy is disabled, try without proxy fallback
            return operation_func(ytdl_opts, *args, **kwargs)
    except Exception as e:
        logger.warning(f"Error checking proxy for user {user_id}: {e}")
        return operation_func(ytdl_opts, *args, **kwargs)
    
    # Check if user has selected a country from proxy file
    try:
        from COMMANDS.proxy_cmd import get_user_selected_country, get_proxies_for_country
        selected_country = get_user_selected_country(user_id)
        if selected_country:
            # User selected country - try proxies from file (HTTP first, then SOCKS5)
            proxies = get_proxies_for_country(selected_country)
            if proxies:
                logger.info(f"User {user_id} selected country {selected_country}, trying {len(proxies)} proxies from file")
                for i, proxy_info in enumerate(proxies):
                    try:
                        current_opts = ytdl_opts.copy()
                        proxy_url = proxy_info['proxy_url']
                        current_opts['proxy'] = proxy_url
                        # Добавляем PO token provider для YouTube (если еще не добавлен)
                        if is_youtube_url(url):
                            current_opts = add_pot_to_ytdl_opts(current_opts, url)
                        
                        # Если это HLS-стрим - добавляем параметры для быстрого прерывания при ошибках 403
                        if "m3u8" in url.lower() or current_opts.get("downloader") == "ffmpeg" or current_opts.get("hls_prefer_native") is False:
                            logger.info("HLS stream with proxy detected in fallback - adding fast-fail options")
                            current_opts["fragment_retries"] = 0
                            current_opts["hls_fragment_retries"] = 0
                            current_opts["abort_on_unavailable_fragment"] = True
                            current_opts["max_fragments"] = 1
                        
                        logger.info(f"Trying {url} with proxy from file {i+1}/{len(proxies)} ({proxy_info['type']}): {proxy_url}")
                        result = operation_func(current_opts, *args, **kwargs)
                        
                        if result is not None:
                            logger.info(f"Success with proxy from file {i+1}/{len(proxies)} ({proxy_info['type']}): {proxy_url}")
                            return result
                        else:
                            logger.warning(f"Operation returned None with proxy from file {i+1}/{len(proxies)} ({proxy_info['type']}): {proxy_url}")
                    except Exception as e:
                        logger.warning(f"Failed with proxy from file {i+1}/{len(proxies)} ({proxy_info['type']}): {e}")
                        continue
                
                # All proxies from file failed for selected country - do NOT fall back to config proxies
                # User explicitly selected a country, so we should only use proxies from that country
                logger.warning(f"All proxies from file for country {selected_country} failed, not trying config proxies (user selected specific country)")
                # Try without proxy as last resort
                try:
                    logger.info(f"Trying {url} without proxy as last resort (selected country proxies failed)")
                    current_opts = ytdl_opts.copy()
                    if 'proxy' in current_opts:
                        del current_opts['proxy']
                    # Добавляем PO token provider для YouTube (если еще не добавлен)
                    if is_youtube_url(url):
                        current_opts = add_pot_to_ytdl_opts(current_opts, url)
                    return operation_func(current_opts, *args, **kwargs)
                except Exception as e:
                    logger.error(f"Failed without proxy for {url}: {e}")
                    return None
            else:
                # Selected country but no proxies found - return None
                logger.warning(f"User selected country {selected_country} but no proxies found for this country")
                return None
        else:
            # No country selected - continue to ALL AUTO mode below
            pass
    except Exception as e:
        logger.warning(f"Error checking user selected country: {e}")
    
    # User proxy is enabled (ALL AUTO mode) - try all proxies: first from Config, then from file
    all_proxies_to_try = []
    
    # Step 1: Add all proxies from Config
    all_configs = get_all_proxy_configs()
    for proxy_config in all_configs:
        proxy_url = build_proxy_url(proxy_config)
        if proxy_url:
            all_proxies_to_try.append({
                'proxy_url': proxy_url,
                'source': 'config',
                'index': len(all_proxies_to_try) + 1
            })
    
    # Step 2: Add all proxies from file (if file exists)
    try:
        from HELPERS.proxy_file_helper import get_all_proxies_from_file
        file_proxies = get_all_proxies_from_file("TXT/proxy.txt")
        for proxy_info in file_proxies:
            all_proxies_to_try.append({
                'proxy_url': proxy_info['proxy_url'],
                'source': 'file',
                'country': proxy_info['country'],
                'type': proxy_info['type'],
                'index': len(all_proxies_to_try) + 1
            })
    except Exception as e:
        logger.warning(f"Error loading proxies from file: {e}")
    
    if not all_proxies_to_try:
        logger.info(f"No proxies available for {url}, trying without proxy")
        # Добавляем PO token provider для YouTube (если еще не добавлен)
        if is_youtube_url(url):
            ytdl_opts = add_pot_to_ytdl_opts(ytdl_opts.copy(), url)
        return operation_func(ytdl_opts, *args, **kwargs)
    
    logger.info(f"Trying {len(all_proxies_to_try)} proxies in ALL AUTO mode: {len(all_configs)} from Config, {len(all_proxies_to_try) - len(all_configs)} from file")
    
    # Try with each proxy
    for proxy_item in all_proxies_to_try:
        try:
            current_opts = ytdl_opts.copy()
            proxy_url = proxy_item['proxy_url']
            current_opts['proxy'] = proxy_url
            # Добавляем PO token provider для YouTube (если еще не добавлен)
            if is_youtube_url(url):
                current_opts = add_pot_to_ytdl_opts(current_opts, url)
            
            # Если это HLS-стрим - добавляем параметры для быстрого прерывания при ошибках 403
            if "m3u8" in url.lower() or current_opts.get("downloader") == "ffmpeg" or current_opts.get("hls_prefer_native") is False:
                logger.info("HLS stream with proxy detected in ALL AUTO fallback - adding fast-fail options")
                current_opts["fragment_retries"] = 0
                current_opts["hls_fragment_retries"] = 0
                current_opts["abort_on_unavailable_fragment"] = True
                current_opts["max_fragments"] = 1
            
            source_info = f"{proxy_item['source']}"
            if proxy_item['source'] == 'file':
                source_info += f" ({proxy_item.get('country', 'unknown')}, {proxy_item.get('type', 'unknown')})"
            
            logger.info(f"Trying {url} with proxy {proxy_item['index']}/{len(all_proxies_to_try)} from {source_info}: {proxy_url}")
            result = operation_func(current_opts, *args, **kwargs)
            
            if result is not None:
                logger.info(f"Success with proxy {proxy_item['index']}/{len(all_proxies_to_try)} from {source_info}: {proxy_url}")
                return result
            else:
                logger.warning(f"Operation returned None with proxy {proxy_item['index']}/{len(all_proxies_to_try)} from {source_info}: {proxy_url}")
        except Exception as e:
            logger.warning(f"Failed with proxy {proxy_item['index']}/{len(all_proxies_to_try)} from {source_info}: {e}")
            continue
    
    # If all proxies failed, try without proxy as last resort
    try:
        logger.warning(f"All {len(all_proxies_to_try)} proxies failed for {url}, trying without proxy")
        current_opts = ytdl_opts.copy()
        if 'proxy' in current_opts:
            del current_opts['proxy']
        return operation_func(current_opts, *args, **kwargs)
    except Exception as e:
        logger.error(f"Failed without proxy for {url}: {e}")
        return None

def is_proxy_domain(url: str) -> bool:
    """Check if the domain is in PROXY_DOMAINS or PROXY_2_DOMAINS"""
    from CONFIG.domains import DomainsConfig
    
    domain = extract_domain_from_url(url)
    
    # Check PROXY_DOMAINS
    if hasattr(DomainsConfig, 'PROXY_DOMAINS') and DomainsConfig.PROXY_DOMAINS:
        if is_domain_in_list(domain, DomainsConfig.PROXY_DOMAINS):
            return True
    
    # Check PROXY_2_DOMAINS
    if hasattr(DomainsConfig, 'PROXY_2_DOMAINS') and DomainsConfig.PROXY_2_DOMAINS:
        if is_domain_in_list(domain, DomainsConfig.PROXY_2_DOMAINS):
            return True
    
    return False

def get_proxy_config():
    """Get proxy configuration from config"""
    from CONFIG.config import Config
    
    return {
        'type': Config.PROXY_TYPE,
        'ip': Config.PROXY_IP,
        'port': Config.PROXY_PORT,
        'user': Config.PROXY_USER,
        'password': Config.PROXY_PASSWORD
    }

def get_proxy_2_config():
    """Get second proxy configuration from config"""
    from CONFIG.config import Config
    
    return {
        'type': Config.PROXY_2_TYPE,
        'ip': Config.PROXY_2_IP,
        'port': Config.PROXY_2_PORT,
        'user': Config.PROXY_2_USER,
        'password': Config.PROXY_2_PASSWORD
    }

def get_all_proxy_configs():
    """Get all available proxy configurations"""
    from CONFIG.config import Config
    
    configs = []
    
    # First proxy
    if hasattr(Config, 'PROXY_TYPE') and hasattr(Config, 'PROXY_IP') and hasattr(Config, 'PROXY_PORT'):
        if Config.PROXY_IP and Config.PROXY_PORT:
            configs.append({
                'type': Config.PROXY_TYPE,
                'ip': Config.PROXY_IP,
                'port': Config.PROXY_PORT,
                'user': Config.PROXY_USER,
                'password': Config.PROXY_PASSWORD
            })
    
    # Second proxy
    if hasattr(Config, 'PROXY_2_TYPE') and hasattr(Config, 'PROXY_2_IP') and hasattr(Config, 'PROXY_2_PORT'):
        if Config.PROXY_2_IP and Config.PROXY_2_PORT:
            configs.append({
                'type': Config.PROXY_2_TYPE,
                'ip': Config.PROXY_2_IP,
                'port': Config.PROXY_2_PORT,
                'user': Config.PROXY_2_USER,
                'password': Config.PROXY_2_PASSWORD
            })
    
    return configs

def extract_domain_from_url(url):
    """Extract domain from URL, handling subdomains properly"""
    if '://' in url:
        domain = url.split('://')[1].split('/')[0]
    else:
        domain = url.split('/')[0]
    
    # Remove www. prefix if present
    if domain.startswith('www.'):
        domain = domain[4:]
    
    return domain

def is_domain_in_list(domain, domain_list):
    """Check if domain or any of its subdomains match entries in domain_list"""
    if not domain_list:
        return False
    
    # Direct match
    if domain in domain_list:
        return True
    
    # Check if any domain in the list is a subdomain of the current domain
    for listed_domain in domain_list:
        if domain.endswith('.' + listed_domain):
            return True
    
    return False

def select_proxy_for_domain(url):
    """Select appropriate proxy for domain based on PROXY_DOMAINS and PROXY_2_DOMAINS"""
    from CONFIG.domains import DomainsConfig
    
    domain = extract_domain_from_url(url)
    
    logger.info(f"select_proxy_for_domain: URL={url}, extracted_domain={domain}")
    logger.info(f"PROXY_2_DOMAINS: {getattr(DomainsConfig, 'PROXY_2_DOMAINS', 'NOT_FOUND')}")
    logger.info(f"PROXY_DOMAINS: {getattr(DomainsConfig, 'PROXY_DOMAINS', 'NOT_FOUND')}")
    
    # Check PROXY_2_DOMAINS first
    if hasattr(DomainsConfig, 'PROXY_2_DOMAINS') and DomainsConfig.PROXY_2_DOMAINS:
        if is_domain_in_list(domain, DomainsConfig.PROXY_2_DOMAINS):
            logger.info(f"Domain {domain} found in PROXY_2_DOMAINS, using proxy 2")
            return get_proxy_2_config()
    
    # Check PROXY_DOMAINS
    if hasattr(DomainsConfig, 'PROXY_DOMAINS') and DomainsConfig.PROXY_DOMAINS:
        if is_domain_in_list(domain, DomainsConfig.PROXY_DOMAINS):
            logger.info(f"Domain {domain} found in PROXY_DOMAINS, using proxy 1")
            return get_proxy_config()
    
    logger.info(f"Domain {domain} not found in any proxy domain lists")
    return None

def select_proxy_for_user():
    """Select proxy for user based on PROXY_SELECT method"""
    from CONFIG.config import Config
    import random
    
    configs = get_all_proxy_configs()
    if not configs:
        return None
    
    if len(configs) == 1:
        return configs[0]
    
    # Select method based on PROXY_SELECT
    if hasattr(Config, 'PROXY_SELECT') and Config.PROXY_SELECT == "random":
        return random.choice(configs)
    else:  # default to round_robin
        # Simple round-robin using a global counter
        if not hasattr(select_proxy_for_user, 'counter'):
            select_proxy_for_user.counter = 0
        selected = configs[select_proxy_for_user.counter % len(configs)]
        select_proxy_for_user.counter += 1
        return selected

def add_proxy_to_gallery_dl_config(config: dict, url: str, user_id: int = None) -> dict:
    """Add proxy to gallery-dl config if proxy is enabled for user or domain requires it"""
    logger.info(f"add_proxy_to_gallery_dl_config called: user_id={user_id}, url={url}")
    
    # Priority 1: Check if user has proxy enabled (/proxy on)
    if user_id:
        try:
            from COMMANDS.proxy_cmd import is_proxy_enabled
            proxy_enabled = is_proxy_enabled(user_id)
            logger.info(f"User {user_id} proxy enabled: {proxy_enabled}")
            if proxy_enabled:
                # Use round-robin/random selection for user proxy
                proxy_config = select_proxy_for_user()
                if proxy_config:
                    proxy_url = build_proxy_url(proxy_config)
                    if proxy_url:
                        config['extractor']['proxy'] = proxy_url
                        logger.info(f"Added user proxy for {user_id}: {proxy_url}")
                        return config
        except Exception as e:
            logger.warning(f"Error checking proxy for user {user_id}: {e}")
            pass
    
    # Priority 2: Check if domain requires specific proxy (only if user proxy is OFF)
    logger.info(f"Checking domain-specific proxy for {url}")
    proxy_config = select_proxy_for_domain(url)
    if proxy_config:
        proxy_url = build_proxy_url(proxy_config)
        if proxy_url:
            config['extractor']['proxy'] = proxy_url
            logger.info(f"Added domain-specific proxy for {url}: {proxy_url}")
        else:
            logger.warning(f"Failed to build proxy URL from config: {proxy_config}")
    else:
        logger.info(f"No domain-specific proxy found for {url}")
    
    return config

def is_cloudflare_error(error_text: str) -> bool:
    """Check if error is related to Cloudflare protection"""
    error_lower = str(error_text).lower()
    cloudflare_indicators = [
        'cloudflare',
        '403',
        'forbidden',
        'anti-bot',
        'challenge',
        'cf-ray',
        'cf-request-id',
        'just a moment',
        'checking your browser'
    ]
    return any(indicator in error_lower for indicator in cloudflare_indicators)

def try_with_impersonate_fallback(ytdl_opts: dict, url: str, user_id: int = None, operation_func=None, *args, **kwargs):
    """
    Try operation with different impersonate versions in case of Cloudflare 403 error
    
    Args:
        ytdl_opts: yt-dlp options
        url: URL to process
        user_id: User ID
        operation_func: Function to call with ytdl_opts
        *args, **kwargs: Additional arguments for operation_func
    
    Returns:
        Result of operation_func or None if all impersonate versions failed
    """
    if not operation_func:
        return None
    
    # List of impersonate versions to try
    # Start with basic versions that work without curl_cffi (available by default)
    # Then try specific versions if curl_cffi is installed
    basic_versions = [
        'chrome',
        'edge',
        'firefox',
        'safari',
    ]
    
    # Specific versions (require curl_cffi to be installed)
    # Only try these if basic versions fail and we detect curl_cffi availability
    specific_versions = [
        'chrome122', 'chrome121', 'chrome120', 'chrome119', 'chrome118', 'chrome117',
        'chrome116', 'chrome115', 'chrome114', 'chrome113', 'chrome112', 'chrome111',
        'chrome110', 'chrome109', 'chrome108', 'chrome107', 'chrome106', 'chrome105',
        'chrome104', 'chrome103', 'chrome102', 'chrome101', 'chrome100',
        'chrome99', 'chrome98', 'chrome97', 'chrome96', 'chrome95', 'chrome94',
        'chrome93', 'chrome92', 'chrome91', 'chrome90', 'chrome89', 'chrome88',
        'chrome87', 'chrome86', 'chrome85', 'chrome84', 'chrome83', 'chrome82',
        'chrome81', 'chrome80',
        'edge110', 'edge109', 'edge108', 'edge107', 'edge106', 'edge105',
        'edge104', 'edge103', 'edge102', 'edge101', 'edge100', 'edge99', 'edge98',
        'edge97', 'edge96', 'edge95', 'edge94', 'edge93', 'edge92', 'edge91',
        'edge90', 'edge89', 'edge88', 'edge87', 'edge86', 'edge85', 'edge84',
        'edge83', 'edge82', 'edge81', 'edge80',
        'firefox120', 'firefox119', 'firefox118', 'firefox117', 'firefox116',
        'firefox115', 'firefox114', 'firefox113', 'firefox112', 'firefox111',
        'firefox110', 'firefox109', 'firefox108', 'firefox107', 'firefox106',
        'firefox105', 'firefox104', 'firefox103', 'firefox102', 'firefox101',
        'firefox100', 'firefox99', 'firefox98', 'firefox97', 'firefox96',
        'firefox95', 'firefox94', 'firefox93', 'firefox92', 'firefox91',
        'firefox90', 'firefox89', 'firefox88', 'firefox87', 'firefox86',
        'firefox85', 'firefox84', 'firefox83', 'firefox82', 'firefox81',
        'firefox80',
        'safari17', 'safari16', 'safari15', 'safari14', 'safari13', 'safari12',
        'safari11', 'safari10',
    ]
    
    # Check if curl_cffi is available (for specific versions)
    curl_cffi_available = False
    curl_cffi_version = None
    curl_cffi_working = False  # Track if curl_cffi actually works (not just installed)
    try:
        import curl_cffi
        curl_cffi_available = True
        try:
            curl_cffi_version = getattr(curl_cffi, '__version__', 'unknown')
        except:
            pass
        
        # Try to check if curl_cffi actually works by checking available browser versions
        try:
            from curl_cffi import Curl
            # Try to create a curl instance to verify it works
            test_curl = Curl()
            curl_cffi_working = True
            test_curl.close()
            
            # Try to check available browser versions (if supported)
            try:
                from curl_cffi import const
                # Check if we can access browser versions
                if hasattr(const, 'BROWSERS') or hasattr(const, 'BrowserType'):
                    logger.debug("curl_cffi browser versions check available")
            except:
                pass
        except Exception as e:
            logger.warning(f"curl_cffi is installed but may not be working properly: {str(e)[:200]}")
            curl_cffi_working = False
        
        if curl_cffi_version:
            if curl_cffi_working:
                logger.info(f"curl_cffi is available (version {curl_cffi_version}), will try specific impersonate versions")
            else:
                logger.warning(f"curl_cffi is installed (version {curl_cffi_version}) but may not be working. Try reinstalling: pip install --upgrade --force-reinstall curl-cffi")
        else:
            if curl_cffi_working:
                logger.info("curl_cffi is available, will try specific impersonate versions")
            else:
                logger.warning("curl_cffi is installed but may not be working. Try reinstalling: pip install --upgrade --force-reinstall curl-cffi")
    except ImportError:
        logger.info("curl_cffi is not available, will only try basic impersonate versions. Install with: pip install curl-cffi")
    
    # Check yt-dlp version for compatibility
    ytdlp_version = None
    try:
        import yt_dlp
        ytdlp_version = getattr(yt_dlp, '__version__', 'unknown')
        if ytdlp_version and ytdlp_version != 'unknown':
            logger.debug(f"yt-dlp version: {ytdlp_version}")
            # Check if version is recent enough (should support curl_cffi)
            try:
                version_parts = ytdlp_version.split('.')
                major = int(version_parts[0]) if version_parts else 0
                minor = int(version_parts[1]) if len(version_parts) > 1 else 0
                if major < 2024 or (major == 2024 and minor < 1):
                    logger.warning(f"yt-dlp version {ytdlp_version} may be too old for proper curl_cffi support. Consider updating: pip install --upgrade --pre yt-dlp")
            except:
                pass
    except:
        pass
    
    # Build list: basic versions first, then specific if curl_cffi is available
    # Note: When curl_cffi is installed, yt-dlp may try to use it for basic versions,
    # but curl_cffi only supports specific versions. We'll try basic versions first,
    # and if they're unavailable, skip to specific versions.
    impersonate_versions = basic_versions.copy()
    if curl_cffi_available:
        impersonate_versions.extend(specific_versions)
        logger.info(f"Will try {len(impersonate_versions)} impersonate versions (including {len(specific_versions)} specific)")
    else:
        logger.info(f"Will try only {len(basic_versions)} basic impersonate versions. Install curl-cffi to enable specific versions: pip install curl-cffi")
    
    # Log first few versions for debugging
    logger.debug(f"First 5 impersonate versions to try: {impersonate_versions[:5]}")
    
    # Try with original options first (skip if we already know it's a Cloudflare error)
    original_error = None
    try:
        logger.info(f"Trying {url} with original impersonate settings")
        result = operation_func(ytdl_opts, *args, **kwargs)
        if result is not None:
            return result
    except Exception as e:
        error_text = str(e)
        original_error = error_text
        if not is_cloudflare_error(error_text):
            # Not a Cloudflare error, re-raise
            raise e
        logger.warning(f"Cloudflare error detected with original settings: {error_text[:200]}")
    
    # Track if we've tried basic versions
    basic_versions_tried = False
    basic_versions_all_failed = True
    basic_versions_unavailable = False  # Track if basic versions are unavailable (when curl_cffi is installed)
    
    # Try with different impersonate versions
    unavailable_specific_count = 0  # Track only specific versions
    max_unavailable_before_skip = 3  # Skip remaining if 3+ consecutive specific versions unavailable
    
    for impersonate_version in impersonate_versions:
        # Check if we're moving from basic to specific versions
        is_basic_version = impersonate_version in basic_versions
        if is_basic_version:
            basic_versions_tried = True
            if unavailable_specific_count > 0:
                logger.debug(f"Resetting unavailable_specific_count when trying basic version {impersonate_version}")
            unavailable_specific_count = 0  # Reset counter when trying basic versions
        elif basic_versions_tried and not curl_cffi_available:
            # If basic versions failed and curl_cffi is not available, skip specific versions
            logger.info("Basic impersonate versions failed and curl_cffi is not installed. Skipping specific versions.")
            logger.info("To enable specific impersonate versions, install: pip install curl-cffi")
            break
        elif basic_versions_unavailable and is_basic_version:
            # Skip basic versions if they're unavailable (when curl_cffi is installed)
            logger.debug(f"Skipping basic version {impersonate_version} (unavailable when curl_cffi is installed)")
            continue
        try:
            # Create a deep copy of options to avoid modifying original
            import copy
            current_opts = copy.deepcopy(ytdl_opts)
            
            # Ensure extractor_args structure exists
            if 'extractor_args' not in current_opts:
                current_opts['extractor_args'] = {}
            if 'generic' not in current_opts['extractor_args']:
                current_opts['extractor_args']['generic'] = {}
            
            # Update impersonate version
            current_opts['extractor_args']['generic']['impersonate'] = [impersonate_version]
            
            # Preserve all other extractor_args (youtubetab, etc.)
            original_extractor_args = ytdl_opts.get('extractor_args', {})
            for key, value in original_extractor_args.items():
                if key != 'generic':
                    current_opts['extractor_args'][key] = copy.deepcopy(value)
            
            logger.info(f"Trying {url} with impersonate={impersonate_version}")
            result = operation_func(current_opts, *args, **kwargs)
            
            if result is not None:
                logger.info(f"Success with impersonate={impersonate_version}")
                return result
            else:
                logger.warning(f"Operation returned None with impersonate={impersonate_version}")
                
        except Exception as e:
            error_text = str(e)
            is_basic = impersonate_version in basic_versions
            
            # Check if error indicates impersonate version is not available
            # Note: yt-dlp outputs "none of these impersonate targets are available" to stderr,
            # which may not be in the exception text. For specific versions (chrome122, etc.),
            # if we get Cloudflare error, it's likely the version is unavailable.
            explicit_unavailable = "none of these impersonate targets are available" in error_text.lower()
            
            # For specific versions: if Cloudflare error and version contains digits (chrome122, etc.),
            # treat as unavailable (since yt-dlp warning goes to stderr, not exception text)
            is_specific_version = not is_basic and any(char.isdigit() for char in impersonate_version)
            likely_unavailable = is_specific_version and is_cloudflare_error(error_text)
            
            if explicit_unavailable or likely_unavailable:
                logger.debug(f"Impersonate version {impersonate_version} is not available, skipping")
                
                # If basic version is unavailable and curl_cffi is installed, mark all basic versions as unavailable
                # This is normal: curl_cffi only supports specific versions (chrome122, chrome121, etc.), not basic ones (chrome, edge, etc.)
                if is_basic and curl_cffi_available and explicit_unavailable:
                    basic_versions_unavailable = True
                    logger.info(f"ℹ️ Basic version {impersonate_version} unavailable (this is normal when curl_cffi is installed).")
                    logger.info(f"   curl_cffi only supports specific versions (chrome122, chrome121, etc.), not basic ones (chrome, edge, etc.).")
                    logger.info(f"   Skipping remaining basic versions and trying specific versions instead...")
                    # Skip remaining basic versions and continue to specific versions
                    continue
                
                # Only track unavailable count for specific versions
                if not is_basic:
                    unavailable_specific_count += 1
                    logger.warning(f"⚠️ Specific version {impersonate_version} unavailable (consecutive failures: {unavailable_specific_count}/{max_unavailable_before_skip})")
                    
                    # If too many consecutive specific versions are unavailable, skip remaining
                    if unavailable_specific_count >= max_unavailable_before_skip:
                        # Calculate remaining specific versions
                        current_idx = impersonate_versions.index(impersonate_version)
                        remaining_specific = [v for v in impersonate_versions[current_idx+1:] if v not in basic_versions]
                        remaining_count = len(remaining_specific)
                        logger.error(f"❌ {unavailable_specific_count} consecutive specific impersonate versions unavailable. STOPPING and skipping remaining {remaining_count} specific versions.")
                        break
                continue
            else:
                # Reset counter if version is available but failed for other reasons
                if impersonate_version not in basic_versions:
                    if unavailable_specific_count > 0:
                        logger.debug(f"Resetting unavailable_specific_count (version {impersonate_version} is available)")
                    unavailable_specific_count = 0
            
            if not is_cloudflare_error(error_text):
                # Not a Cloudflare error, might be a different issue - log but continue
                logger.debug(f"Non-Cloudflare error with impersonate={impersonate_version}: {error_text[:200]}")
            else:
                logger.warning(f"Cloudflare error with impersonate={impersonate_version}: {error_text[:200]}")
            continue
    
    logger.error(f"All impersonate versions failed for {url}")
    if not curl_cffi_available:
        logger.error("❌ curl_cffi is not installed. This is required for impersonate functionality.")
        logger.error("📦 Install with: pip install curl-cffi")
        logger.error("   Or update yt-dlp: pip install --upgrade --pre 'yt-dlp[default,curl-cffi]'")
    elif curl_cffi_available:
        version_info = f" (version {curl_cffi_version})" if curl_cffi_version else ""
        
        # Check if basic versions were unavailable
        if basic_versions_unavailable:
            logger.error(f"❌ curl_cffi{version_info} is installed, but basic browser versions (chrome, edge, firefox, safari) are unavailable.")
            logger.error("   This usually means curl_cffi was installed incorrectly or is incompatible.")
            logger.error("📦 Try reinstalling:")
            logger.error("   1. pip uninstall curl-cffi")
            logger.error("   2. pip install --upgrade --force-reinstall --no-cache-dir curl-cffi")
            logger.error("   3. Or: pip install --upgrade --pre --force-reinstall curl-cffi")
        
        if unavailable_specific_count >= max_unavailable_before_skip:
            logger.error(f"❌ curl_cffi{version_info} is installed, but specific browser versions are unavailable.")
            logger.error("   This usually means curl_cffi needs to be updated or reinstalled.")
            logger.error("📦 Try updating:")
            logger.error("   pip install --upgrade --pre --force-reinstall curl-cffi")
            logger.error("   Or: pip install --upgrade --pre 'yt-dlp[default,curl-cffi]'")
        else:
            logger.warning(f"⚠️ curl_cffi{version_info} is installed, but all impersonate versions failed.")
            logger.warning("   This may indicate that Cloudflare protection is too strong for this site.")
            logger.warning("   Or curl_cffi may need to be reinstalled:")
            logger.warning("   pip install --upgrade --force-reinstall curl-cffi")
    return None