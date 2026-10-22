from HELPERS.cookie_file import validated_cookie_options
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
from HELPERS.fallback_helper import should_fallback_to_gallery_dl, gallery_dl_has_extractor


# Retryability classification lives in HELPERS/ytdlp_errors.py (single source
# of truth); the former local _RATE_LIMIT/_PERMANENT_UNAVAILABLE/_TRANSIENT
# indicator copies were removed.
from HELPERS.ytdlp_errors import (
    classify_retryability,
    is_auth_required,
    is_transient_network_error,
    should_abort_retries,
    RATE_LIMITED,
)

# Terminal get_video_formats() results are remembered for a short time per
# (user, URL, playlist range). The download path calls get_video_formats once
# per format attempt, and users re-send the same dead link; without this cache
# one deleted / members-only / age-gated video produced 9+ identical
# extractions, each logging an ERROR (issues #352, #360, #386, #479).
# A new cookie.txt (different mtime) invalidates the entry so /cookie works
# immediately.
_TERMINAL_RESULT_TTL = 120
_terminal_results = {}


def _cookie_mtime(user_id):
    if user_id is None:
        return None
    try:
        return os.path.getmtime(os.path.join("users", str(user_id), "cookie.txt"))
    except OSError:
        return None


def _get_cached_terminal_result(key, user_id):
    import time
    entry = _terminal_results.get(key)
    if not entry:
        return None
    ts, cookie_mtime, result = entry
    if time.monotonic() - ts > _TERMINAL_RESULT_TTL or cookie_mtime != _cookie_mtime(user_id):
        _terminal_results.pop(key, None)
        return None
    return dict(result)


def _remember_terminal_result(key, user_id, result):
    import time
    now = time.monotonic()
    for k in [k for k, v in list(_terminal_results.items()) if now - v[0] > _TERMINAL_RESULT_TTL]:
        _terminal_results.pop(k, None)
    _terminal_results[key] = (now, _cookie_mtime(user_id), dict(result))


def _terminal_error_result(error_text, cookie_pass_done=True):
    """Map a terminal yt-dlp error to the structured dict callers already handle.

    Returns None when the error is not terminal (another attempt may help).
    Every caller of get_video_formats understands 'RATE_LIMITED' and
    'PERMANENT_UNAVAILABLE' (with 'original_error' for classify_yt_dlp_error);
    auth-required (after the cookie pass), client HTTP 4xx and local file
    errors are reported as PERMANENT_UNAVAILABLE for the same reason.
    """
    if not should_abort_retries(error_text):
        return None
    # Auth-required errors get exactly one cookie pass before becoming terminal.
    if not cookie_pass_done and is_auth_required(error_text):
        return None
    if classify_retryability(error_text) == RATE_LIMITED:
        return {'error': 'RATE_LIMITED', 'original_error': error_text}
    return {'error': 'PERMANENT_UNAVAILABLE', 'original_error': error_text}


_CACHEABLE_TERMINAL_ERRORS = ('PERMANENT_UNAVAILABLE', 'RATE_LIMITED', 'UNSUPPORTED_URL')


def get_video_formats(url, user_id=None, playlist_start_index=1, cookies_already_checked=False, use_proxy=False, playlist_end_index=None):
    """Extract yt-dlp info (formats + metadata) for url.

    Returns the info dict on success, or a dict with an 'error' key
    (LIVE_STREAM_DETECTED, RATE_LIMITED, PERMANENT_UNAVAILABLE, UNSUPPORTED_URL,
    FALLBACK_TO_GALLERY_DL, TIKTOK_PRIVATE_ACCOUNT, EXTRACTION_ERROR; most carry
    'original_error'). Unclassified yt-dlp failures re-raise the DownloadError.
    """
    cache_key = (user_id, url, playlist_start_index, playlist_end_index)
    cached = _get_cached_terminal_result(cache_key, user_id)
    if cached is not None:
        logger.info(f"get_video_formats: reusing terminal result {cached.get('error')} for {url} (no new extraction)")
        return cached
    result = _get_video_formats_uncached(
        url, user_id, playlist_start_index, cookies_already_checked, use_proxy, playlist_end_index)
    if isinstance(result, dict) and result.get('error') in _CACHEABLE_TERMINAL_ERRORS:
        _remember_terminal_result(cache_key, user_id, result)
    return result


def _get_video_formats_uncached(url, user_id=None, playlist_start_index=1, cookies_already_checked=False, use_proxy=False, playlist_end_index=None):
    # ДЕТАЛЬНОЕ ЛОГИРОВАНИЕ ДЛЯ ОТЛАДКИ
    logger.info(f"🔍 [DEBUG] get_video_formats вызвана с параметрами:")
    logger.info(f"   url: {url}")
    logger.info(f"   user_id: {user_id}")
    logger.info(f"   playlist_start_index: {playlist_start_index}")
    logger.info(f"   playlist_end_index: {playlist_end_index}")
    logger.info(f"   cookies_already_checked: {cookies_already_checked}")
    logger.info(f"   use_proxy: {use_proxy}")
    
    # Resolve Facebook share-redirect URLs (/share/v/, /share/r/, fb.watch) to
    # canonical video URLs that yt-dlp can extract (issue #392). Defensive: on
    # any failure the original URL is used unchanged.
    try:
        from URL_PARSERS.normalizer import resolve_facebook_share_url
        _resolved = resolve_facebook_share_url(url)
        if _resolved != url:
            logger.info(f"get_video_formats: resolved Facebook share URL '{url}' -> '{_resolved}'")
            url = _resolved
    except Exception as _fb_err:
        logger.debug(f"get_video_formats: Facebook share resolution skipped: {_fb_err}")
    
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
        'live_from_start': True,
        'socket_timeout': 60,
    }

    # Prevent yt-dlp from routing non-playlist URLs through playlist/tab
    # extractors, which causes "No videos found in playlist" for single
    # videos (issue #389). The download path already sets noplaylist, but
    # this discovery function is called FIRST and must also set it.
    from urllib.parse import urlparse as _urlparse
    try:
        _url_host = (_urlparse(url).hostname or '').lower()
    except ValueError:
        _url_host = ''
    _is_youtube_host = (
        _url_host == 'youtube.com'
        or _url_host.endswith('.youtube.com')
        or _url_host == 'youtu.be'
        or _url_host.endswith('.youtu.be')
    )
    _url_lower = url.lower()
    _is_playlist_url = (
        ('list=' in _url_lower and _is_youtube_host)
        or ('/playlist' in _url_lower)
    )
    if not _is_playlist_url:
        ytdl_opts['noplaylist'] = True
    
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
        
    # Proxy: same logic as /vid /audio /link (country / AUTO / domain)
    from HELPERS.proxy_helper import add_proxy_to_ytdl_opts
    ytdl_opts = add_proxy_to_ytdl_opts(ytdl_opts, url, user_id)
    
    # Add PO token provider for YouTube domains
    ytdl_opts = add_pot_to_ytdl_opts(ytdl_opts, url)
    # Как в down_and_up: явный Node, иначе user_args могут подставить deno/none и format-check даст FORMAT_NOT_AVAILABLE
    ytdl_opts['js_runtimes'] = {'node': {}}

    from HELPERS.proxy_helper import (
        try_with_proxy_fallback, try_with_impersonate_fallback, is_cloudflare_error,
        has_alternative_proxy_route,
    )

    def extract_info_operation(opts):
        """One raw yt-dlp extraction with the given opts.

        Raises on failure: recovery (cookies, proxies, impersonation) is done
        exactly once by _recover_from_download_error(). Fallback helpers call
        this function too, so it must not start fallbacks itself — the old
        nested handler re-entered the cookie/proxy chains from inside every
        fallback attempt and logged one ERROR per attempt (issues #352, #386,
        #479).
        """
        logger.info(f"🔍 [DEBUG] extract_info_operation: начинаем извлечение информации")
        logger.info(f"   url: {url}")
        logger.info(f"   opts keys: {list(opts.keys())}")

        with yt_dlp.YoutubeDL(validated_cookie_options(opts)) as ydl:
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
        if isinstance(info, list):
            info = (info[0] if len(info) > 0 else {})
            logger.info(f"🔍 [DEBUG] info был списком, взяли первый элемент")
        elif isinstance(info, dict) and 'entries' in info:
            entries = info.get('entries')
            if isinstance(entries, list) and len(entries) > 0:
                # Сохраняем все entries для скачивания обложек
                info = entries[0]
                logger.info(f"🔍 [DEBUG] info содержал entries, взяли первый элемент. Всего entries: {len(entries)}")
                # Добавляем entries в info для использования в ask_quality_menu
                info['_playlist_entries'] = entries

        # Check for live stream after extraction (only if detection is enabled)
        if info and info.get('is_live', False) and LimitsConfig.ENABLE_LIVE_STREAM_BLOCKING:
            logger.warning(f"Live stream detected in get_video_formats: {url}")
            return {'error': 'LIVE_STREAM_DETECTED'}

        # Cache successful cookie result for future use
        if info and not is_youtube_url(url) and user_id is not None:
            from COMMANDS.cookies_cmd import set_cookie_cache_result
            cookie_file_path = opts.get('cookiefile')
            if cookie_file_path and os.path.exists(cookie_file_path):
                set_cookie_cache_result(user_id, url, True, cookie_file_path)
                logger.info(f"Cached successful cookie result for format detection {url}")

        logger.info(f"✅ [DEBUG] extract_info_operation: возвращаем info")
        return info

    # --- First (and normally the only) extraction ---
    try:
        result = extract_info_operation(ytdl_opts)
    except yt_dlp.utils.DownloadError as e:
        return _recover_from_download_error(e, url, user_id, ytdl_opts, extract_info_operation)
    except Exception as e:
        # yt-dlp can raise non-DownloadError exceptions during extraction
        # (e.g. an internal TypeError when the GoogleDriveFolder extractor
        # feeds a bool into re.search, issue #380, or the ok.ru extractor's
        # json.loads(dict) TypeError, issues #469/#471). Return a structured
        # error dict instead of re-raising so callers show a clean message.
        error_text = str(e)
        if is_cloudflare_error(error_text):
            logger.info(f"Cloudflare error detected for {url}, trying impersonate fallback")
            try:
                impersonate_result = try_with_impersonate_fallback(
                    ytdl_opts, url, user_id, extract_info_operation, skip_original_attempt=True)
            except Exception as imp_e:
                logger.warning(f"Impersonate fallback failed for {url}: {str(imp_e)[:200]}")
                impersonate_result = None
            if impersonate_result is not None:
                return impersonate_result
        _category = classify_retryability(error_text)
        if _category:
            logger.warning(f"Error extracting info for {url} ({_category}): {e}")
        else:
            logger.error(f"Error extracting info for {url}: {e}")
        return {'error': 'EXTRACTION_ERROR', 'original_error': error_text}

    if result is not None:
        return result

    # yt-dlp returned no info without raising: only a different route can help.
    if has_alternative_proxy_route(url, user_id):
        try:
            result = try_with_proxy_fallback(ytdl_opts, url, user_id, extract_info_operation)
            if result is not None:
                return result
        except Exception as e:
            logger.warning(f"Proxy fallback failed for {url}: {str(e)[:200]}")
    return {'error': 'EXTRACTION_ERROR', 'original_error': 'yt-dlp returned no information'}


def _recover_from_download_error(first_error, url, user_id, ytdl_opts, extract_info_operation):
    """Run each applicable recovery step at most once after a DownloadError.

    Order: terminal check -> one timeout retry -> live_from_start retry ->
    unsupported URL -> single cookie pass -> TikTok private / gallery-dl ->
    YouTube geo proxy -> proxy fallback (only when it uses a different route)
    -> impersonation (Cloudflare). After every failed step the newest error is
    re-classified and a terminal one ends the chain with a structured dict.
    Unclassified failures re-raise the last DownloadError, exactly as before,
    so callers relying on the exception text keep working.
    """
    from HELPERS.proxy_helper import (
        try_with_proxy_fallback, try_with_impersonate_fallback, is_cloudflare_error,
        has_alternative_proxy_route,
    )
    last_error = first_error
    error_text = str(first_error)

    def _terminal(err_text, cookie_pass_done):
        result = _terminal_error_result(err_text, cookie_pass_done=cookie_pass_done)
        if result is not None:
            logger.warning(
                f"Terminal yt-dlp error ({classify_retryability(err_text)}), "
                f"no further retries for {url}: {err_text[:200]}"
            )
        return result

    def _attempt(opts, label):
        """Run one recovery attempt; return (result, DownloadError or None)."""
        try:
            return extract_info_operation(opts), None
        except yt_dlp.utils.DownloadError as retry_e:
            logger.warning(f"{label} failed for {url}: {str(retry_e)[:200]}")
            return None, retry_e

    category = classify_retryability(error_text)
    if category is None:
        logger.error(f"DownloadError in get_video_formats: {error_text}")
    else:
        # Expected, classified condition (deleted / members-only / rate limit /
        # 4xx ...): WARNING instead of ERROR so monitoring is not flooded by
        # user-content problems the bot already reports clearly.
        logger.warning(f"DownloadError in get_video_formats ({category}): {error_text}")

    # Check for live stream detection (only if detection is enabled)
    if "LIVE_STREAM_DETECTED" in error_text and LimitsConfig.ENABLE_LIVE_STREAM_BLOCKING:
        return {'error': 'LIVE_STREAM_DETECTED'}

    # Permanent / rate-limit / client-4xx errors: abort before any retry
    # (issues #323, #329, #330, #352, #360, #394, #436, #475, #477, #479).
    terminal = _terminal(error_text, cookie_pass_done=False)
    if terminal is not None:
        return terminal

    # Transient network timeout (issue #464): retry ONCE with a longer
    # socket_timeout. HTTP 5xx is transient too, but a longer socket timeout
    # does not help it, so only socket-level failures qualify. (The old code
    # retried recursively, doubling the timeout on every new timeout.)
    if is_transient_network_error(error_text) and 'http error' not in error_text.lower():
        retry_opts = ytdl_opts.copy()
        _base_to = ytdl_opts.get('socket_timeout') or 60
        retry_opts['socket_timeout'] = max(120, int(_base_to) * 2)
        logger.warning(
            f"Transient network timeout, retrying once with socket_timeout="
            f"{retry_opts['socket_timeout']}s for {url}: {error_text[:200]}"
        )
        result, retry_e = _attempt(retry_opts, "Retry after network timeout")
        if result is not None:
            logger.info(f"Retry after network timeout successful for {url}")
            return result
        if retry_e is not None:
            last_error, error_text = retry_e, str(retry_e)
            terminal = _terminal(error_text, cookie_pass_done=False)
            if terminal is not None:
                return terminal

    # Auto-retry: --live-from-start fails for non-live streams on VK and
    # other platforms. Retry with live_from_start=False (issue #80/vk).
    if "--live-from-start is passed, but there are no formats that can be downloaded from the start" in error_text:
        logger.info(f"live-from-start not supported for this URL, retrying with --no-live-from-start: {url}")
        ytdl_opts = ytdl_opts.copy()
        ytdl_opts['live_from_start'] = False  # later steps must not hit the same failure
        result, retry_e = _attempt(ytdl_opts, "Retry with --no-live-from-start")
        if result is not None:
            logger.info(f"Retry with --no-live-from-start successful for {url}")
            return result
        if retry_e is not None:
            last_error, error_text = retry_e, str(retry_e)
            terminal = _terminal(error_text, cookie_pass_done=False)
            if terminal is not None:
                return terminal

    _error_lower = error_text.lower()

    # Unsupported URL: only allow gallery-dl fallback (non-YouTube); otherwise bail out
    # without proxy/impersonate retries which cannot help unsupported domains (issue #323).
    if 'unsupported url' in _error_lower:
        if gallery_dl_has_extractor(url) and should_fallback_to_gallery_dl(error_text, url):
            logger.info(f"Unsupported URL — deferring to gallery-dl fallback for {url}")
            return {'error': 'FALLBACK_TO_GALLERY_DL', 'original_error': error_text}
        logger.warning(f"Unsupported URL (no yt-dlp or gallery-dl extractor), no retries for {url}: {error_text[:200]}")
        return {'error': 'UNSUPPORTED_URL', 'original_error': error_text}

    # --- Single cookie pass ---
    if is_youtube_url(url) and user_id is not None:
        from COMMANDS.cookies_cmd import is_youtube_cookie_error, retry_download_with_different_cookies
        if is_youtube_cookie_error(error_text):
            logger.info(f"YouTube cookie error detected in get_video_formats for user {user_id}, attempting automatic retry")
            try:
                retry_result = retry_download_with_different_cookies(
                    user_id, url, extract_info_operation, ytdl_opts.copy()
                )
            except yt_dlp.utils.DownloadError as retry_e:
                last_error, error_text, retry_result = retry_e, str(retry_e), None
            if retry_result is not None:
                logger.info(f"get_video_formats retry with different cookies successful for user {user_id}")
                return retry_result
            logger.warning(f"All cookie retry attempts failed in get_video_formats for user {user_id}")
        # Note: geo errors are handled below, before the proxy fallback.
    elif user_id is not None:
        # For non-YouTube sites, try cookie fallback
        # HTTP 401 from access-restricted hosts (Dailymotion/Vimeo) is a permanent
        # access-denied/API change, NOT a cookie problem — skip cookie fallback to avoid
        # a 4-strategy retry storm that just re-receives 401 (issue #318).
        try:
            from urllib.parse import urlparse
            _host = (urlparse(url).hostname or '').lower()
        except ValueError:
            _host = ''
        _access_denied_host = any(h in _host for h in ('dailymotion.com', 'vimeo.com'))
        if _access_denied_host and ('401' in _error_lower or 'unauthorized' in _error_lower):
            logger.info(f"401/Unauthorized from access-restricted host {_host} for {url} — skipping cookie fallback (permanent access error)")
        elif any(keyword in _error_lower for keyword in ['cookie', 'auth', 'login', 'sign in', '403', '401', 'forbidden', 'unauthorized']):
            logger.info(f"Error appears to be cookie-related for {url}, trying cookie fallback")
            from COMMANDS.cookies_cmd import try_non_youtube_cookie_fallback
            retry_result = try_non_youtube_cookie_fallback(
                user_id, url, extract_info_operation, ytdl_opts.copy()
            )
            if retry_result is not None:
                logger.info(f"get_video_formats retry with cookie fallback successful for user {user_id}")
                return retry_result
            logger.warning(f"get_video_formats retry with cookie fallback failed for user {user_id}")
        else:
            logger.info(f"Error appears to be non-cookie-related for {url}, skipping cookie fallback")

    # The cookie pass is over: auth-required errors are terminal now (Douyin
    # "Fresh cookies ... are needed", issue #386) — proxies cannot add cookies.
    terminal = _terminal(error_text, cookie_pass_done=True)
    if terminal is not None:
        return terminal
    _error_lower = error_text.lower()

    # Generic HTTP 403: после единственного прохода cookies не перебираем
    # браузеры/прокси и форматы на том же отказе сайта (#477).
    if '[generic]' in _error_lower and 'http error 403' in _error_lower:
        return {'error': 'PERMANENT_UNAVAILABLE', 'original_error': error_text}

    # Check for TikTok private account error
    try:
        from urllib.parse import urlparse
        tiktok_hostname = (urlparse(url).hostname or '').lower()
    except ValueError:
        tiktok_hostname = ''
    is_tiktok = tiktok_hostname in ('tiktok.com', 'www.tiktok.com', 'vm.tiktok.com', 'vt.tiktok.com') or \
               tiktok_hostname.endswith('.tiktok.com')
    if is_tiktok and "private" in _error_lower and "account" in _error_lower:
        logger.info(f"TikTok private account detected for {url}, recommending gallery-dl fallback")
        return {'error': 'TIKTOK_PRIVATE_ACCOUNT', 'original_error': error_text}

    # Gallery-dl fallback (e.g. image-only Pinterest pins: "No video formats
    # found", issue #480) — only when gallery-dl has a specific extractor for
    # the URL; for [generic] pages it would just be one more failing attempt
    # (issues #323, #477).
    if should_fallback_to_gallery_dl(error_text, url) and gallery_dl_has_extractor(url):
        logger.info(f"Fallback to gallery-dl recommended for {url} due to error: {error_text[:200]}...")
        return {'error': 'FALLBACK_TO_GALLERY_DL', 'original_error': error_text}

    # YouTube geo error: retry with proxies of the allowed countries
    if is_youtube_url(url) and user_id is not None:
        from COMMANDS.cookies_cmd import is_youtube_geo_error, retry_download_with_proxy
        if is_youtube_geo_error(error_text):
            logger.info(f"YouTube geo-blocked error detected in get_video_formats for user {user_id}, attempting retry with proxy from file")

            # retry_download_with_proxy calls func(url, attempt_opts)
            def extract_with_attempt_opts(url_arg, attempt_opts_dict):
                # Убеждаемся, что geo_bypass включен для обхода геоблокировки
                if 'geo_bypass' not in attempt_opts_dict:
                    attempt_opts_dict['geo_bypass'] = True
                logger.info(f"extract_with_attempt_opts: proxy={'set' if attempt_opts_dict.get('proxy') else 'None'}, geo_bypass={attempt_opts_dict.get('geo_bypass', 'None')}, cookiefile={'set' if attempt_opts_dict.get('cookiefile') else 'None'}")
                return extract_info_operation(attempt_opts_dict)

            try:
                retry_result = retry_download_with_proxy(
                    user_id, url, extract_with_attempt_opts, url, ytdl_opts, error_message=error_text
                )
            except yt_dlp.utils.DownloadError as retry_e:
                last_error, error_text, retry_result = retry_e, str(retry_e), None
            if retry_result is not None:
                logger.info(f"get_video_formats retry with proxy from file successful for user {user_id}")
                return retry_result
            logger.warning(f"get_video_formats retry with proxy from file failed for user {user_id}")
            terminal = _terminal(error_text, cookie_pass_done=True)
            if terminal is not None:
                return terminal

    # Proxy fallback — only when it uses a DIFFERENT route. Without a selected
    # proxy country it just re-ran the identical request (and the old code then
    # ran it a third time "to capture the error"): issues #362, #436, #479.
    if has_alternative_proxy_route(url, user_id):
        try:
            result = try_with_proxy_fallback(ytdl_opts, url, user_id, extract_info_operation)
            if result is not None:
                return result
        except yt_dlp.utils.DownloadError as proxy_e:
            last_error, error_text = proxy_e, str(proxy_e)
            logger.warning(f"Proxy fallback failed for {url}: {error_text[:200]}")
        terminal = _terminal(error_text, cookie_pass_done=True)
        if terminal is not None:
            return terminal
    else:
        logger.info(f"No alternative proxy route for {url} (user {user_id}), skipping proxy fallback")

    # Cloudflare / anti-bot 403: try other impersonation targets once. The
    # original opts were already tried above, so skip that attempt.
    if is_cloudflare_error(error_text):
        logger.info(f"Cloudflare-like error for {url}, trying impersonate fallback")
        try:
            impersonate_result = try_with_impersonate_fallback(
                ytdl_opts, url, user_id, extract_info_operation, skip_original_attempt=True)
        except yt_dlp.utils.DownloadError as imp_e:
            last_error, impersonate_result = imp_e, None
        if impersonate_result is not None:
            return impersonate_result

    # Nothing helped and the error is not terminal: re-raise the last error so
    # callers keep their exception-based handling (Always Ask classifies the
    # text, the download path runs its own error mapping).
    raise last_error


# YT-DLP HOOK

def ytdlp_hook(d):
    logger.info(d['status'])
