# --- receiving formats and metadata via yt-dlp ---
import os
import yt_dlp
from CONFIG.config import Config
from CONFIG.messages import Messages, safe_get_messages
from HELPERS.logger import logger, send_error_to_user
from HELPERS.filesystem_hlp import create_directory
from URL_PARSERS.nocookie import is_no_cookie_domain
from URL_PARSERS.youtube import is_youtube_url
from URL_PARSERS.filter_check import is_no_filter_domain
from URL_PARSERS.filter_utils import create_smart_match_filter, create_legacy_match_filter
from HELPERS.pot_helper import add_pot_to_ytdl_opts
from CONFIG.limits import LimitsConfig
from HELPERS.fallback_helper import should_fallback_to_gallery_dl

def get_video_formats(url, user_id=None, playlist_start_index=1, cookies_already_checked=False, use_proxy=False, playlist_end_index=None):
    # ДЕТАЛЬНОЕ ЛОГИРОВАНИЕ ДЛЯ ОТЛАДКИ
    logger.info(f"🔍 [DEBUG] get_video_formats вызвана с параметрами:")
    logger.info(f"   url: {url}")
    logger.info(f"   user_id: {user_id}")
    logger.info(f"   playlist_start_index: {playlist_start_index}")
    logger.info(f"   playlist_end_index: {playlist_end_index}")
    logger.info(f"   cookies_already_checked: {cookies_already_checked}")
    logger.info(f"   use_proxy: {use_proxy}")
    
    # ВНИМАНИЕ ПО ПРОИЗВОДИТЕЛЬНОСТИ:
    # Раньше здесь безусловно сбрасывался кеш проверенных источников YouTube‑куки.
    # Это приводило к тому, что при каждом новом URL бот заново перебирал и проверял
    # все источники куки, даже если у пользователя уже лежит рабочий cookie.txt.
    # Теперь сброс источников выполняется _только_ в тех местах, где реально
    # начинается перебор новых источников (см. ниже), а не при каждом вызове.
    messages = safe_get_messages(user_id)
    
    # Формируем playlist_items с учетом диапазона
    if playlist_end_index is not None and playlist_end_index != playlist_start_index:
        # Для диапазона используем формат START:END или START:END:-1 для обратного порядка
        if playlist_start_index < 0 or playlist_end_index < 0:
            # Для отрицательных индексов определяем обратный порядок
            is_reverse = (playlist_start_index < 0 and playlist_end_index < 0 and abs(playlist_start_index) < abs(playlist_end_index)) or (playlist_start_index > playlist_end_index)
            if is_reverse:
                playlist_items_str = f"{playlist_start_index}:{playlist_end_index}:-1"
            else:
                playlist_items_str = f"{playlist_start_index}:{playlist_end_index}"
        elif playlist_start_index > playlist_end_index:
            # Для обратного порядка с положительными индексами
            playlist_items_str = f"{playlist_start_index}:{playlist_end_index}:-1"
        else:
            # Для прямого порядка
            playlist_items_str = f"{playlist_start_index}:{playlist_end_index}"
    else:
        # Для одного элемента
        playlist_items_str = str(playlist_start_index)
    
    ytdl_opts = {
        'quiet': True,
        'skip_download': True,
        'forcejson': True,
        'no_warnings': True,
        'extract_flat': False,
        'simulate': True,
        'playlist_items': playlist_items_str,    
        'extractor_args': {
            'generic': {
                'impersonate': ['chrome']
            },
            'youtubetab': {
                'skip': ['authcheck']
            }
        },
        'referer': url,
        'geo_bypass': True,
        # check_certificate and no_check_certificates are set from user_args (default: check_certificate=False, no_check_certificates=True)
        'live_from_start': True
    }
    
    # Add match_filter only if domain is not in NO_FILTER_DOMAINS
    if not is_no_filter_domain(url):
        # Use smart filter that allows downloads when duration is unknown
        ytdl_opts['match_filter'] = create_smart_match_filter(user_id=user_id)
    else:
        logger.info(safe_get_messages(user_id).YTDLP_SKIPPING_MATCH_FILTER_MSG.format(url=url))
    
    # Add user's custom yt-dlp arguments (but exclude format to get all available formats)
    # This includes default values for check_certificate and no_check_certificates
    if user_id is not None:
        from COMMANDS.args_cmd import get_user_ytdlp_args, log_ytdlp_options
        user_args = get_user_ytdlp_args(user_id, url)
        if user_args:
            # Remove format parameter to get all available formats
            user_args_copy = user_args.copy()
            user_args_copy.pop('format', None)
            ytdl_opts.update(user_args_copy)
        
        # Log final yt-dlp options for debugging
        log_ytdlp_options(user_id, ytdl_opts, "get_video_formats")
    
    if user_id is not None:
        user_dir = os.path.join("users", str(user_id))
        # Check the availability of cookie.txt in the user folder
        user_cookie_path = os.path.join(user_dir, "cookie.txt")

        # --- YouTube: максимально быстрый путь ---
        # Новая логика:
        #   1) Если у пользователя уже есть cookie.txt, считаем его рабочим
        #      (он появился здесь только после успешной валидации ранее) и
        #      НЕ запускаем повторно test_youtube_cookies_on_url и перебор источников.
        #   2) Только если файла нет или он потом даст cookie‑ошибку, включается
        #      стандартный перебор источников в retry_download_with_different_cookies.
        if is_youtube_url(url) and not cookies_already_checked:
            from COMMANDS.cookies_cmd import get_youtube_cookie_urls, _download_content, reset_checked_cookie_sources

            if os.path.exists(user_cookie_path):
                # Быстрый путь: просто используем уже сохранённые куки без повторной проверки
                cookie_file = user_cookie_path
                logger.info(
                    safe_get_messages(user_id).YTDLP_USING_EXISTING_YOUTUBE_COOKIES_WITHOUT_RECHECK_MSG.format(
                        user_id=user_id
                    )
                )
            else:
                # Файл куки ещё ни разу не получали — здесь действительно нужен перебор
                reset_checked_cookie_sources(user_id)
                logger.info(
                    f"🔄 [DEBUG] Reset checked cookie sources for initial YouTube cookie fetch for user {user_id}"
                )
                cookie_urls = get_youtube_cookie_urls()
                if cookie_urls:
                    from COMMANDS.cookies_cmd import get_unchecked_cookie_sources, mark_cookie_source_checked, test_youtube_cookies_on_url
                    unchecked_indices = get_unchecked_cookie_sources(user_id, cookie_urls)
                    if not unchecked_indices:
                        logger.warning(
                            f"All cookie sources have been checked for user {user_id}, no more sources to try"
                        )
                        cookie_file = None
                    else:
                        success = False
                        for i, idx in enumerate(unchecked_indices, 1):
                            cookie_url = cookie_urls[idx]
                            logger.info(
                                safe_get_messages(user_id).YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG.format(
                                    i=idx + 1, user_id=user_id
                                )
                            )

                            # Отмечаем источник как проверенный
                            mark_cookie_source_checked(user_id, idx)

                            try:
                                ok, status_code, content, error = _download_content(cookie_url, user_id=user_id)
                            except Exception as download_e:
                                logger.error(
                                    f"Error processing cookie source {idx + 1} for user {user_id}: {download_e}"
                                )
                                continue
                            if ok and content and len(content) <= 100 * 1024:
                                with open(user_cookie_path, "wb") as cf:
                                    cf.write(content)
                                if test_youtube_cookies_on_url(user_cookie_path, url, user_id):
                                    cookie_file = user_cookie_path
                                    logger.info(
                                        safe_get_messages(user_id).YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG.format(
                                            i=idx + 1, user_id=user_id
                                        )
                                    )
                                    success = True
                                    break
                                else:
                                    logger.warning(
                                        safe_get_messages(
                                            user_id
                                        ).YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG.format(
                                            i=idx + 1, user_id=user_id
                                        )
                                    )
                                    if os.path.exists(user_cookie_path):
                                        os.remove(user_cookie_path)
                            else:
                                logger.warning(
                                    safe_get_messages(user_id).YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG.format(
                                        i=idx + 1, user_id=user_id
                                    )
                                )

                        if not success:
                            logger.warning(
                                safe_get_messages(user_id).YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG.format(
                                    user_id=user_id
                                )
                            )
                            cookie_file = None
                else:
                    logger.warning(
                        safe_get_messages(user_id).YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG.format(
                            user_id=user_id
                        )
                    )
                    cookie_file = None
        elif is_youtube_url(url) and cookies_already_checked:
            # Cookies already checked in Always Ask menu - use them directly without verification
            if os.path.exists(user_cookie_path):
                cookie_file = user_cookie_path
                logger.info(safe_get_messages(user_id).YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG.format(user_id=user_id))
            else:
                # Cookies were deleted - try to restore them on user's URL
                logger.info(safe_get_messages(user_id).YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG.format(user_id=user_id))
                from COMMANDS.cookies_cmd import get_youtube_cookie_urls, test_youtube_cookies_on_url, _download_content
                cookie_urls = get_youtube_cookie_urls()
                if cookie_urls:
                    success = False
                    for i, cookie_url in enumerate(cookie_urls, 1):
                        logger.info(f"Trying YouTube cookie source {i} for format detection for user {user_id}")
                        try:
                            ok, status_code, content, error = _download_content(cookie_url, user_id=user_id)
                        except Exception as download_e:
                            logger.error(f"Error processing cookie source {i} for user {user_id}: {download_e}")
                            continue
                        if ok and content and len(content) <= 100 * 1024:
                            with open(user_cookie_path, "wb") as cf:
                                cf.write(content)
                            if test_youtube_cookies_on_url(user_cookie_path, url, user_id):
                                cookie_file = user_cookie_path
                                logger.info(f"YouTube cookies from source {i} work on user's URL for format detection for user {user_id} - saved to user folder")
                                success = True
                                break
                            else:
                                logger.warning(f"YouTube cookies from source {i} don't work on user's URL for format detection for user {user_id}")
                                if os.path.exists(user_cookie_path):
                                    os.remove(user_cookie_path)
                        else:
                            logger.warning(f"Failed to download YouTube cookies from source {i} for format detection for user {user_id}")
                    
                    if not success:
                        logger.warning(f"All YouTube cookie sources failed for format detection for user {user_id}, will try without cookies")
                        cookie_file = None
                else:
                    logger.warning(f"No YouTube cookie sources configured for format detection for user {user_id}, will try without cookies")
                    cookie_file = None
        else:
            # For non-YouTube URLs, use new cookie fallback system
            # Для Instagram / Facebook / TikTok / VK действуем по схеме:
            #   1) сначала пробуем БЕЗ куки;
            #   2) если не получилось — пробуем куки пользователя;
            #   3) если и это не помогло — берём куки по URL из конфига.
            # Для остальных доменов остаётся старая логика с кешом.
            from COMMANDS.cookies_cmd import get_cookie_cache_result, try_non_youtube_cookie_fallback, get_service_name_from_url

            service_name = get_service_name_from_url(url)
            special_social = service_name in {"instagram", "facebook", "tiktok", "vk"}

            if special_social:
                # Стартуем максимально быстро: без куки.
                cookie_file = None
                logger.info(f"Using NO cookies for initial format detection on {service_name}: {url}")
            else:
                cache_result = get_cookie_cache_result(user_id, url)
                
                if cache_result and cache_result['result']:
                    # Use cached successful cookies
                    cookie_file = cache_result['cookie_path']
                    logger.info(f"Using cached cookies for non-YouTube format detection: {url}")
                else:
                    # Try user cookies first
                    if os.path.exists(user_cookie_path):
                        cookie_file = user_cookie_path
                        logger.info(f"Using user cookies for non-YouTube format detection: {url}")
                    else:
                        # No user cookies, will try fallback during format detection
                        cookie_file = None
                        logger.info(f"No user cookies found for non-YouTube format detection: {url}, will try fallback")
        
        # We check whether to use —no-Cookies for this domain
        if is_no_cookie_domain(url):
            ytdl_opts['cookiefile'] = None  # Equivalent-No-Cookies
            logger.info(safe_get_messages(user_id).YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG.format(url=url))
        elif cookie_file:
            ytdl_opts['cookiefile'] = cookie_file
            logger.info(f"[YTDLP DEBUG] Using cookies for {url}: {cookie_file}")
        else:
            logger.info(f"[YTDLP DEBUG] No cookies available for {url}")
        
        # Add proxy configuration if needed for this domain 
        if use_proxy:
            # Force proxy for this request
            from COMMANDS.proxy_cmd import get_proxy_config
            proxy_config = get_proxy_config()
            
            if proxy_config and 'type' in proxy_config and 'ip' in proxy_config and 'port' in proxy_config:
                # Build proxy URL
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
                
                ytdl_opts['proxy'] = proxy_url
                logger.info(f"Force using proxy for format detection: {proxy_url}")
            else:
                logger.warning("Proxy requested but proxy configuration is incomplete")
        else:
            # Add proxy configuration if needed for this domain
            from HELPERS.proxy_helper import add_proxy_to_ytdl_opts
            ytdl_opts = add_proxy_to_ytdl_opts(ytdl_opts, url, user_id)
    
    # Add PO token provider for YouTube domains
    ytdl_opts = add_pot_to_ytdl_opts(ytdl_opts, url)
    
    # Try with proxy fallback if user proxy is enabled
    def extract_info_operation(opts):
        try:
            logger.info(f"🔍 [DEBUG] extract_info_operation: начинаем извлечение информации")
            logger.info(f"   url: {url}")
            logger.info(f"   opts keys: {list(opts.keys())}")
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=False)
            
            logger.info(f"✅ [DEBUG] extract_info_operation: извлечение завершено")
            logger.info(f"   info type: {type(info)}")
            if isinstance(info, dict):
                logger.info(f"   info keys: {list(info.keys())}")
                if 'duration' in info:
                    logger.info(f"   duration: {info['duration']} (тип: {type(info['duration'])})")
                if 'is_live' in info:
                    logger.info(f"   is_live: {info['is_live']} (тип: {type(info['is_live'])})")
            
            # Normalize info to a dict
            # Для плейлистов сохраняем все entries для скачивания обложек
            playlist_entries = None
            if isinstance(info, list):
                info = (info[0] if len(info) > 0 else {})
                logger.info(f"🔍 [DEBUG] info был списком, взяли первый элемент")
            elif isinstance(info, dict) and 'entries' in info:
                entries = info.get('entries')
                if isinstance(entries, list) and len(entries) > 0:
                    # Сохраняем все entries для скачивания обложек
                    playlist_entries = entries
                    info = entries[0]
                    logger.info(f"🔍 [DEBUG] info содержал entries, взяли первый элемент. Всего entries: {len(entries)}")
                    # Добавляем entries в info для использования в ask_quality_menu
                    info['_playlist_entries'] = playlist_entries
            
            # Check for live stream after extraction (only if detection is enabled)
            if info and info.get('is_live', False) and LimitsConfig.ENABLE_LIVE_STREAM_BLOCKING:
                logger.warning(f"Live stream detected in get_video_formats: {url}")
                return {'error': 'LIVE_STREAM_DETECTED'}
            
            # Cache successful cookie result for future use
            if not is_youtube_url(url) and user_id is not None:
                from COMMANDS.cookies_cmd import set_cookie_cache_result
                cookie_file_path = opts.get('cookiefile')
                if cookie_file_path and os.path.exists(cookie_file_path):
                    set_cookie_cache_result(user_id, url, True, cookie_file_path)
                    logger.info(f"Cached successful cookie result for format detection {url}")
            
            logger.info(f"✅ [DEBUG] extract_info_operation: возвращаем info")
            return info
        except yt_dlp.utils.DownloadError as e:
            error_text = str(e)
            logger.error(f"DownloadError in get_video_formats: {error_text}")
            
            # Check for live stream detection (only if detection is enabled)
            if "LIVE_STREAM_DETECTED" in error_text and LimitsConfig.ENABLE_LIVE_STREAM_BLOCKING:
                return {'error': 'LIVE_STREAM_DETECTED'}
            
            # Check for YouTube cookie errors and try automatic retry
            if is_youtube_url(url) and user_id is not None:
                from COMMANDS.cookies_cmd import is_youtube_cookie_error, is_youtube_geo_error, retry_download_with_different_cookies, retry_download_with_proxy
                
                if is_youtube_cookie_error(error_text):
                    logger.info(f"YouTube cookie error detected in get_video_formats for user {user_id}, attempting automatic retry")
                    
                    # Try retry with different cookies
                    retry_result = retry_download_with_different_cookies(
                        user_id, url, extract_info_operation, opts
                    )
                    
                    if retry_result is not None:
                        logger.info(f"get_video_formats retry with different cookies successful for user {user_id}")
                        return retry_result
                    else:
                        logger.warning(f"All cookie retry attempts failed in get_video_formats for user {user_id}")
                
                # Note: Geo errors are handled at the outer level (before try_with_proxy_fallback)
                # to ensure proxy from file is tried first
            elif not is_youtube_url(url) and user_id is not None:
                # For non-YouTube sites, try cookie fallback
                logger.info(f"Non-YouTube error detected in get_video_formats for user {user_id}, attempting cookie fallback")
                
                # Check if error is cookie-related
                error_str = error_text.lower()
                if any(keyword in error_str for keyword in ['cookie', 'auth', 'login', 'sign in', '403', '401', 'forbidden', 'unauthorized']):
                    logger.info(f"Error appears to be cookie-related for {url}, trying cookie fallback")
                    
                    # Try cookie fallback with new system
                    from COMMANDS.cookies_cmd import try_non_youtube_cookie_fallback
                    retry_result = try_non_youtube_cookie_fallback(
                        user_id, url, extract_info_operation, opts
                    )
                    
                    if retry_result is not None:
                        logger.info(f"get_video_formats retry with cookie fallback successful for user {user_id}")
                        return retry_result
                    else:
                        logger.warning(f"get_video_formats retry with cookie fallback failed for user {user_id}")
                else:
                    logger.info(f"Error appears to be non-cookie-related for {url}, skipping cookie fallback")
            
            # Check for TikTok private account error
            # Безопасная проверка домена через urlparse
            is_tiktok = False
            try:
                from urllib.parse import urlparse
                parsed_url = urlparse(url)
                tiktok_hostname = (parsed_url.hostname or '').lower()
                is_tiktok = tiktok_hostname in ('tiktok.com', 'www.tiktok.com', 'vm.tiktok.com', 'vt.tiktok.com') or \
                           tiktok_hostname.endswith('.tiktok.com')
            except Exception:
                pass
            
            if is_tiktok and "private" in error_text.lower() and "account" in error_text.lower():
                logger.info(f"TikTok private account detected for {url}, recommending gallery-dl fallback")
                return {'error': 'TIKTOK_PRIVATE_ACCOUNT', 'original_error': error_text}
            
            # Check if we should fallback to gallery-dl
            if should_fallback_to_gallery_dl(error_text, url):
                logger.info(f"Fallback to gallery-dl recommended for {url} due to error: {error_text[:200]}...")
                return {'error': 'FALLBACK_TO_GALLERY_DL', 'original_error': error_text}
            
            # Check for Cloudflare errors and try impersonate fallback
            from HELPERS.proxy_helper import is_cloudflare_error
            if is_cloudflare_error(error_text):
                logger.info(f"Cloudflare error detected for {url}, will try impersonate fallback")
                # Store the error to handle it in the outer scope
                raise e
            
            # Re-raise other DownloadErrors
            raise e
        except Exception as e:
            error_text = str(e)
            # Check if it's a Cloudflare error
            from HELPERS.proxy_helper import is_cloudflare_error, try_with_impersonate_fallback
            if is_cloudflare_error(error_text):
                logger.info(f"Cloudflare error detected for {url}, trying impersonate fallback")
                # Try with different impersonate versions
                impersonate_result = try_with_impersonate_fallback(ytdl_opts, url, user_id, extract_info_operation)
                if impersonate_result is not None:
                    return impersonate_result
                logger.warning(f"All impersonate versions failed for {url}, trying proxy fallback")
            
            logger.error(f"Error extracting info for {url}: {e}")
            raise e
    
    from HELPERS.proxy_helper import try_with_proxy_fallback, try_with_impersonate_fallback, is_cloudflare_error
    
    # First, try to extract info
    try:
        result = extract_info_operation(ytdl_opts)
        if result is not None:
            return result
    except yt_dlp.utils.DownloadError as e:
        error_text = str(e)
        
        # Check for YouTube geo errors BEFORE trying proxy fallback
        if is_youtube_url(url) and user_id is not None:
            from COMMANDS.cookies_cmd import is_youtube_geo_error, retry_download_with_proxy
            
            if is_youtube_geo_error(error_text):
                logger.info(f"YouTube geo-blocked error detected in get_video_formats for user {user_id}, attempting retry with proxy from file")
                
                # Try retry with proxy from file
                # extract_info_operation takes opts as single argument, so we need to wrap it
                # retry_download_with_proxy expects (url, attempt_opts) format, so we create a wrapper
                def extract_with_attempt_opts(url_arg, attempt_opts_dict):
                    # Use attempt_opts_dict (which includes proxy) instead of original opts
                    # Убеждаемся, что geo_bypass включен для обхода геоблокировки
                    if 'geo_bypass' not in attempt_opts_dict:
                        attempt_opts_dict['geo_bypass'] = True
                    logger.info(f"extract_with_attempt_opts: proxy={attempt_opts_dict.get('proxy', 'None')}, geo_bypass={attempt_opts_dict.get('geo_bypass', 'None')}, cookiefile={'set' if attempt_opts_dict.get('cookiefile') else 'None'}")
                    return extract_info_operation(attempt_opts_dict)
                
                retry_result = retry_download_with_proxy(
                    user_id, url, extract_with_attempt_opts, url, ytdl_opts, error_message=error_text
                )
                
                if retry_result is not None:
                    logger.info(f"get_video_formats retry with proxy from file successful for user {user_id}")
                    return retry_result
                else:
                    logger.warning(f"get_video_formats retry with proxy from file failed for user {user_id}")
    
    # If geo retry failed or wasn't applicable, try with proxy fallback from config
    result = try_with_proxy_fallback(ytdl_opts, url, user_id, extract_info_operation)
    if result is None:
        # If proxy fallback failed, check if it was a Cloudflare error and try impersonate fallback
        try:
            # Try once more to capture the error
            extract_info_operation(ytdl_opts)
        except Exception as e:
            error_text = str(e)
            if is_cloudflare_error(error_text):
                logger.info(f"Cloudflare error detected after proxy fallback for {url}, trying impersonate fallback")
                impersonate_result = try_with_impersonate_fallback(ytdl_opts, url, user_id, extract_info_operation)
                if impersonate_result is not None:
                    return impersonate_result
        
        return {'error': 'Failed to extract video information with all available proxies'}
    return result


# YT-DLP HOOK

def ytdlp_hook(d):
    logger.info(d['status'])
