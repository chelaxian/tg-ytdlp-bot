# Version: 1.0.1
# ########################################
# Download_and_up function
# ########################################

from HELPERS.logger import send_to_all  # Импорт в самом начале для гарантии видимости
import os
import glob
import threading
import time
import subprocess
import traceback
import yt_dlp
import re
from HELPERS.app_instance import get_app
from HELPERS.logger import logger, send_to_logger, send_to_user, send_to_all, send_error_to_user, get_log_channel, log_error_to_channel
from CONFIG.logger_msg import LoggerMsg
from CONFIG.messages import Messages, safe_get_messages
from HELPERS.limitter import TimeFormatter, humanbytes, check_user, check_file_size_limit, check_subs_limits
from HELPERS.download_status import set_active_download, clear_download_start_time, check_download_timeout, start_hourglass_animation, start_cycle_progress, playlist_errors_lock, playlist_errors
from HELPERS.safe_messeger import safe_delete_messages, safe_edit_message_text, safe_forward_messages
from HELPERS.filesystem_hlp import sanitize_filename, sanitize_filename_strict, cleanup_user_temp_files, cleanup_subtitle_files, create_directory, check_disk_space
from DOWN_AND_UP.ffmpeg import get_duration_thumb, get_video_info_ffprobe, embed_subs_to_video, create_default_thumbnail, split_video_2
from DOWN_AND_UP.sender import send_videos
from DATABASE.firebase_init import write_logs
from URL_PARSERS.tags import generate_final_tags, save_user_tags
from services.stats_events import update_download_progress
from URL_PARSERS.youtube import is_youtube_url, download_thumbnail, extract_youtube_id
from URL_PARSERS.nocookie import is_no_cookie_domain
from URL_PARSERS.filter_check import is_no_filter_domain
from URL_PARSERS.filter_utils import create_smart_match_filter, create_legacy_match_filter
from URL_PARSERS.thumbnail_downloader import download_thumbnail as download_universal_thumbnail
from HELPERS.pot_helper import add_pot_to_ytdl_opts
from CONFIG.config import Config
from CONFIG.limits import LimitsConfig
from COMMANDS.subtitles_cmd import is_subs_enabled, check_subs_availability, get_user_subs_auto_mode, _subs_check_cache, download_subtitles_ytdlp, get_user_subs_language, clear_subs_check_cache, is_subs_always_ask
from COMMANDS.split_sizer import get_user_split_size
from COMMANDS.mediainfo_cmd import send_mediainfo_if_enabled
from URL_PARSERS.playlist_utils import is_playlist_with_range
from URL_PARSERS.normalizer import get_clean_playlist_url
from urllib.parse import urlparse
from DATABASE.cache_db import get_cached_playlist_videos, get_cached_message_ids, save_to_video_cache, save_to_playlist_cache
from HELPERS.qualifier import get_quality_by_min_side
from HELPERS.logger import send_to_all  # Импорт в самом конце для гарантии видимости
from HELPERS.safe_messeger import safe_forward_messages  # Дублирующий импорт для устранения ошибки видимости
from pyrogram import enums
from pyrogram.types import ReplyParameters
from pyrogram.errors import FloodWait
from HELPERS.safe_messeger import safe_send_message
from URL_PARSERS.tags import extract_url_range_tags
from HELPERS.fallback_helper import should_fallback_to_gallery_dl

# Get app instance for decorators
app = get_app()


def is_skippable_video_error(error_message: str) -> bool:
    """
    Определяет, является ли ошибка пропускаемой (частной ошибкой конкретного видео).
    Такие ошибки не должны останавливать скачивание всего плейлиста.
    
    Args:
        error_message: Текст ошибки от yt-dlp
        
    Returns:
        True если ошибку можно пропустить и продолжить со следующим видео, False иначе
    """
    if not error_message:
        return False
    
    error_lower = error_message.lower()
    
    # Пропускаемые ошибки - частные проблемы конкретного видео
    skippable_patterns = [
        # VK ошибки
        "removed at the request of the copyright holder",
        "removed at the request",
        # YouTube ошибки
        "removed for violating youtube's policy",
        "removed for violating",
        "video unavailable. this video is not available",
        "video unavailable",
        "this video has been removed",
        "video is not available",
        # Общие паттерны
        "copyright holder",
        "violating.*policy",
        "video.*removed",
        "video.*unavailable",
    ]
    
    for pattern in skippable_patterns:
        import re
        if re.search(pattern, error_lower, re.IGNORECASE):
            return True
    
    return False


def _handle_quality_key_error(e: Exception, split_msg_ids: list, is_playlist: bool, successful_uploads: int, indices_to_download: list, video_count: int, user_id: int, proc_msg_id: int, message, app, url: str = None, safe_quality_key: str = None):
    messages = safe_get_messages(user_id)
    """Universal handler for quality_key errors that ensures final actions are completed"""
    logger.info(f"quality_key error ignored (non-critical): {e}")
    logger.info(f"Continuing after quality_key error - split_msg_ids={split_msg_ids}, is_playlist={is_playlist}")
    
    # Check if all downloads completed successfully
    # For split videos, check if we have split_msg_ids; for regular videos, check successful_uploads
    logger.info(f"Final check after quality_key error: successful_uploads={successful_uploads}, len(indices_to_download)={len(indices_to_download)}, split_msg_ids={split_msg_ids}, is_playlist={is_playlist}")
    if (successful_uploads == len(indices_to_download)) or (split_msg_ids and not is_playlist):
        logger.info(f"Upload complete condition met after quality_key error, replacing status message")
        success_msg = f"<b>{safe_get_messages(user_id).DOWN_UP_UPLOAD_COMPLETE_MSG}</b> - {video_count} {safe_get_messages(user_id).DOWN_UP_FILES_UPLOADED_MSG}.\n{safe_get_messages(user_id).CREDITS_MSG}"
        safe_edit_message_text(user_id, proc_msg_id, success_msg)
        send_to_logger(message, success_msg)
        try:
            from COMMANDS.subtitles_cmd import clear_subs_cache_for
            from DOWN_AND_UP.always_ask_menu import delete_subs_langs_cache
            delete_subs_langs_cache(user_id, url)
            cleared = clear_subs_cache_for(user_id, url)
            logger.info(f"[SUBS] End of task: cleared {cleared} subtitle cache entries for user={user_id}")
        except Exception as _e:
            logger.debug(f"[SUBS] Failed to clear end cache: {_e}")
        
        # Save to cache if we have the necessary data
        if url and safe_quality_key and split_msg_ids and not is_playlist:
            logger.info(f"down_and_up: saving split video to cache after quality_key error: {split_msg_ids}")
            _save_video_cache_with_logging(url, safe_quality_key, split_msg_ids, original_text=message.text or message.caption or "", user_id=user_id, download_sections=download_sections)
        
        return True
    else:
        logger.warning(f"Upload complete condition NOT met after quality_key error: successful_uploads={successful_uploads}, len(indices_to_download)={len(indices_to_download)}, split_msg_ids={split_msg_ids}, is_playlist={is_playlist}")
        return False

def _save_video_cache_with_logging(url: str, safe_quality_key: str, message_ids: list, original_text: str = None, user_id: int = None, download_sections: str = None, has_subs: bool = False, has_dubs: bool = False):
    """Save video to cache with channel type logging."""
    try:
        # Don't cache trimmed videos
        if download_sections:
            logger.info(f"Skipping cache for trimmed video: url={url}, quality={safe_quality_key}, sections={download_sections}")
            return
        
        # Don't cache videos with subs or dubs (different users may need different languages)
        if has_subs or has_dubs:
            logger.info(f"Skipping cache for video with subs ({has_subs}) or dubs ({has_dubs}): url={url}, quality={safe_quality_key}")
            return
        
        # Check if user has send_as_file enabled
        if user_id is not None:
            from COMMANDS.args_cmd import get_user_args
            user_args = get_user_args(user_id)
            send_as_file = user_args.get("send_as_file", False)
            if send_as_file:
                logger.info(LoggerMsg.DOWN_UP_SKIPPING_CACHE_SEND_AS_FILE_LOG_MSG.format(user_id=user_id, url=url, quality=safe_quality_key))
                return
        
        # Determine channel type for logging
        from HELPERS.porn import is_porn
        is_nsfw = is_porn(url, "", "", None)
        logger.info(LoggerMsg.DOWN_UP_IS_PORN_CHECK_LOG_MSG.format(url=url, is_nsfw=is_nsfw))
        channel_type = "NSFW" if is_nsfw else "regular"
        
        # Don't cache NSFW content
        if is_nsfw:
            logger.info(LoggerMsg.DOWN_UP_SKIPPING_CACHE_NSFW_LOG_MSG.format(url=url, quality=safe_quality_key, channel_type=channel_type))
            return
        
        logger.info(LoggerMsg.DOWN_UP_ABOUT_TO_SAVE_VIDEO_LOG_MSG.format(url=url, quality=safe_quality_key, message_ids=message_ids, channel_type=channel_type))
        save_to_video_cache(url, safe_quality_key, message_ids, original_text=original_text)
        logger.info(LoggerMsg.DOWN_UP_SAVE_REQUESTED_LOG_MSG.format(quality=safe_quality_key, channel_type=channel_type))
    except Exception as e:
        logger.error(LoggerMsg.DOWN_UP_SAVE_FAILED_LOG_MSG.format(quality=safe_quality_key, error=e))


def determine_need_subs(subs_enabled, found_type, user_id):
    """
    Helper function to determine if subtitles are needed based on user settings and found type.
    Returns True if subtitles should be embedded, False otherwise.
    
    Logic:
    1. If Always Ask mode is ON and user has selected a language in subs.txt -> NEED SUBS
    2. If Always Ask mode is OFF but subs are enabled and available -> NEED SUBS  
    3. Otherwise -> NO SUBS
    """
    # Check if we're in Always Ask mode first
    is_always_ask_mode = is_subs_always_ask(user_id)
    
    if is_always_ask_mode:
        # In Always Ask mode, check if user has selected a subtitle language
        subs_lang = get_user_subs_language(user_id)
        if subs_lang and subs_lang not in ["OFF"]:
            logger.info(f"Always Ask mode: user selected language '{subs_lang}' -> NEED SUBS")
            return True  # User has selected a subtitle language in Always Ask mode
        else:
            logger.info(f"Always Ask mode: no language selected -> NO SUBS")
            return False
    
    # For manual mode, check if subtitles are enabled and available
    if not subs_enabled:
        logger.info(f"Manual mode: subtitles disabled -> NO SUBS")
        return False
        
    if found_type is None:
        logger.info(f"Manual mode: no subtitles available -> NO SUBS")
        return False
    
    # In manual mode, respect user's auto_mode setting
    auto_mode = get_user_subs_auto_mode(user_id)
    need_subs = (auto_mode and found_type == "auto") or (not auto_mode and found_type == "normal")
    logger.info(f"Manual mode: auto_mode={auto_mode}, found_type={found_type} -> {'NEED SUBS' if need_subs else 'NO SUBS'}")
    return need_subs

#@reply_with_keyboard
def down_and_up(app, message, url, playlist_name, video_count, video_start_with, tags_text, force_no_title=False, format_override=None, quality_key=None, cookies_already_checked=False, use_proxy=False, cached_video_info=None, clear_subs_cache_on_start=True, download_sections=None):
    # ВАЖНО: не сбрасываем источники YouTube‑куки без необходимости.
    # Если пользователь уже получил рабочие куки и мы пришли из Always Ask меню
    # (cookies_already_checked=True), повторный сброс и перебор источников только
    # замедлит старт скачивания. Сбрасываем источники только для новых задач,
    # когда куки ещё не проверялись.
    user_id = message.chat.id
    if not cookies_already_checked:
        from COMMANDS.cookies_cmd import reset_checked_cookie_sources
        reset_checked_cookie_sources(user_id)
        logger.info(f"🔄 [DEBUG] Reset checked cookie sources for new download task for user {user_id}")
    messages = safe_get_messages(message.chat.id)
    
    # Load trim sections if not provided
    if download_sections is None:
        from DOWN_AND_UP.always_ask_menu import load_trim_sections
        download_sections = load_trim_sections(user_id, url)
        if download_sections:
            logger.info(f"Loaded trim sections for user {user_id}, URL: {url}, sections: {download_sections}")
    """
    Now if part of the playlist range is already cached, we first repost the cached indexes, then download and cache the missing ones, without finishing after reposting part of the range.
    """
    # Import required modules at the beginning
    from URL_PARSERS.youtube import is_youtube_url
    from COMMANDS.cookies_cmd import is_youtube_cookie_error, is_youtube_geo_error, retry_download_with_different_cookies, retry_download_with_proxy
    
    playlist_indices = []
    playlist_msg_ids = []
    playlist_video_urls = {}  # Словарь для хранения уникальных ссылок каждого видео: {index: video_url}    
    found_type = None
    already_forwarded_to_log = False  # Initialize variable to track log forwarding status
    need_subs = False  # Will be determined once at the beginning
    safe_quality_key = quality_key if quality_key is not None else "best"  # Initialize safe_quality_key
    split_msg_ids = []  # Initialize split_msg_ids for split videos
    caption_lst = []  # Initialize caption_lst for split videos
    last_video_msg_id = None  # Initialize last_video_msg_id for caching
    user_id = message.chat.id
    # Ensure fresh subtitle state at the start of a task even for direct calls (bypassing Always Ask)
    if clear_subs_cache_on_start:
        try:
            from COMMANDS.subtitles_cmd import clear_subs_cache_for
            from DOWN_AND_UP.always_ask_menu import delete_subs_langs_cache
            delete_subs_langs_cache(user_id, url)
            cleared = clear_subs_cache_for(user_id, url)
            logger.info(f"[SUBS] Start of task (direct): cleared {cleared} subtitle cache entries for user={user_id}")
        except Exception:
            pass
    successful_uploads = 0  # Initialize successful_uploads counter
    indices_to_download = []  # Initialize indices_to_download list
    proc_msg_id = None  # Initialize proc_msg_id
    logger.info(f"down_and_up called: url={url}, quality_key={quality_key}, format_override={format_override}, video_count={video_count}, video_start_with={video_start_with}")
    
    # ЖЕСТКО: Сохраняем оригинальный текст с диапазоном для фоллбэка
    original_message_text = message.text or message.caption or ""
    logger.info(f"[ORIGINAL TEXT] Saved for fallback: {original_message_text}")
    
    # Initialize retry guards early to avoid UnboundLocalError
    did_proxy_retry = False
    did_cookie_retry = False
    did_live_from_start_retry = False
    is_hls = False
    error_message_sent = False  # Flag to prevent duplicate error messages
    
    # Determine forced NSFW via user tags
    try:
        _u, _s, _e, _p, _tags, _tags_text, _err = extract_url_range_tags(original_message_text)
        user_forced_nsfw = any(t.lower() in ("#nsfw", "#porn") for t in (_tags or []))
    except Exception:
        user_forced_nsfw = False
    
    # Check if format contains /bestaudio (audio-only format)
    if format_override and '/bestaudio' in format_override:
        logger.info(f"Audio-only format detected in down_and_up: {format_override}, redirecting to down_and_audio")
        from DOWN_AND_UP.down_and_audio import down_and_audio
        # Pass cached video info to down_and_audio for optimization
        # Load trim sections if available
        if download_sections is None:
            from DOWN_AND_UP.always_ask_menu import load_trim_sections
            download_sections = load_trim_sections(user_id, url)
        down_and_audio(app, message, url, tags_text, quality_key=quality_key, format_override=format_override, cookies_already_checked=cookies_already_checked, cached_video_info=cached_video_info, download_sections=download_sections)
        return
    
    # Check if LINK mode is enabled - if yes, get direct link instead of downloading
    try:
        from DOWN_AND_UP.always_ask_menu import get_link_mode
        if get_link_mode(user_id):
            logger.info(f"LINK mode enabled for user {user_id}, getting direct link instead of downloading")
            
            # Import link function
            from COMMANDS.link_cmd import get_direct_link
            
            # Convert quality key to quality argument
            quality_arg = None
            if quality_key and quality_key != "best" and quality_key != "mp3":
                quality_arg = quality_key
            
            # Get direct link
            result = get_direct_link(url, user_id, quality_arg, cookies_already_checked=cookies_already_checked, use_proxy=True)
            
            if result.get('success'):
                title = result.get('title', 'Unknown')
                duration = result.get('duration', 0)
                video_url = result.get('video_url')
                audio_url = result.get('audio_url')
                format_spec = result.get('format', 'best')
                
                # Form response
                response = safe_get_messages(user_id).DIRECT_LINK_OBTAINED_MSG
                response += safe_get_messages(user_id).TITLE_FIELD_MSG.format(title=title)
                try:
                    duration_val = float(duration) if duration is not None else 0
                    if duration_val > 0:
                        response += safe_get_messages(user_id).DURATION_FIELD_MSG.format(duration=duration_val)
                except (TypeError, ValueError):
                    pass
                response += safe_get_messages(user_id).FORMAT_FIELD_MSG.format(format_spec=format_spec)
                
                if video_url:
                    response += safe_get_messages(user_id).VIDEO_STREAM_FIELD_MSG.format(video_url=video_url)
                
                if audio_url:
                    response += safe_get_messages(user_id).AUDIO_STREAM_FIELD_MSG.format(audio_url=audio_url)
                
                if not video_url and not audio_url:
                    response += safe_get_messages(user_id).FAILED_STREAM_LINKS_MSG
                
                # Send response
                app.send_message(
                    user_id, 
                    response, 
                    reply_parameters=ReplyParameters(message_id=message.id),
                    parse_mode=enums.ParseMode.HTML
                )
                
                send_to_logger(message, safe_get_messages(user_id).DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG.format(user_id=user_id, url=url))
                
            else:
                error_msg = result.get('error', 'Unknown error')
                app.send_message(
                    user_id,
                    safe_get_messages(user_id).ERROR_GETTING_LINK_MSG.format(error=error_msg),
                    reply_parameters=ReplyParameters(message_id=message.id),
                    parse_mode=enums.ParseMode.HTML
                )
                
                log_error_to_channel(message, safe_get_messages(user_id).DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG.format(user_id=user_id, url=url, error=error_msg), url)
            
            return
    except Exception as e:
        logger.error(f"Error checking LINK mode for user {user_id}: {e}")
        # Continue with normal download if LINK mode check fails
    subs_enabled = is_subs_enabled(user_id)
    need_subs = False
    
    # Check Always Ask mode first - it overrides everything
    is_always_ask_mode = is_subs_always_ask(user_id)
    if is_always_ask_mode and is_youtube_url(url):
        # Check filters state for selected subtitle languages
        try:
            from DOWN_AND_UP.always_ask_menu import get_filters
            filters_state = get_filters(user_id)
            logger.info(f"[DEBUG] Always Ask mode: filters_state keys: {list(filters_state.keys())}")
            logger.info(f"[DEBUG] Always Ask mode: full filters_state: {filters_state}")
            selected_subs_langs = filters_state.get("selected_subs_langs", []) or []
            subs_all_selected = filters_state.get("subs_all_selected", False)
            logger.info(f"[DEBUG] Always Ask mode: selected_subs_langs={selected_subs_langs}, type={type(selected_subs_langs)}, len={len(selected_subs_langs) if selected_subs_langs else 0}")
            logger.info(f"[DEBUG] Always Ask mode: subs_all_selected={subs_all_selected}, type={type(subs_all_selected)}")
            
            if subs_all_selected or (selected_subs_langs and len(selected_subs_langs) > 0):
                need_subs = True
                logger.info(f"Always Ask mode: selected_subs_langs={selected_subs_langs}, subs_all_selected={subs_all_selected} -> FORCE SUBS")
            else:
                # Fallback to old logic (subs.txt) for backward compatibility
                subs_lang = get_user_subs_language(user_id)
                if subs_lang and subs_lang not in ["OFF"]:
                    need_subs = True
                    logger.info(f"Always Ask mode: user selected language '{subs_lang}' (from subs.txt) -> FORCE SUBS")
                else:
                    need_subs = False
                    logger.info(f"Always Ask mode: no language selected -> NO SUBS")
        except Exception as e:
            logger.error(f"Error reading filters state for Always Ask mode: {e}")
            import traceback as tb
            logger.error(tb.format_exc())
            # Fallback to old logic
            subs_lang = get_user_subs_language(user_id)
            if subs_lang and subs_lang not in ["OFF"]:
                need_subs = True
                logger.info(f"Always Ask mode: user selected language '{subs_lang}' (fallback) -> FORCE SUBS")
            else:
                need_subs = False
                logger.info(f"Always Ask mode: no language selected (fallback) -> NO SUBS")
    elif subs_enabled and is_youtube_url(url):
        found_type = check_subs_availability(url, user_id, safe_quality_key, return_type=True)
        # Determine subtitle availability once here
        need_subs = determine_need_subs(subs_enabled, found_type, user_id)
        logger.info(f"Manual mode: subs_enabled={subs_enabled}, found_type={found_type}, need_subs={need_subs}, user_id={user_id}")
    else:
        logger.info(f"Subtitle check skipped: subs_enabled={subs_enabled}, is_youtube={is_youtube_url(url)}, user_id={user_id}")
    
    # Initialize variables for Always Ask mode (needed later in subtitle configuration)
    if not is_always_ask_mode or not is_youtube_url(url):
        selected_subs_langs = []
    
    # Check for dubs (audio tracks) in Always Ask mode
    has_dubs = False
    if is_always_ask_mode and is_youtube_url(url):
        try:
            from DOWN_AND_UP.always_ask_menu import get_filters
            filters_state = get_filters(user_id)
            audio_all_dubs = filters_state.get("audio_all_dubs", False)
            selected_audio_langs = filters_state.get("selected_audio_langs", []) or []
            if audio_all_dubs or selected_audio_langs:
                has_dubs = True
                logger.info(f"Always Ask mode: dubs detected - audio_all_dubs={audio_all_dubs}, selected_audio_langs={selected_audio_langs}")
        except Exception as e:
            logger.warning(f"Error checking for dubs: {e}")
        subs_all_selected = False
    
    # Additional debug info
    if is_youtube_url(url):
        subs_lang = get_user_subs_language(user_id)
        logger.info(f"Final debug: is_always_ask_mode={is_always_ask_mode}, subs_lang='{subs_lang}', need_subs={need_subs}, user_id={user_id}")

    # We define a playlist not only by the number of videos, but also by the presence of a range in the URL
    original_text = message.text or message.caption or ""
    is_playlist = video_count > 1 or is_playlist_with_range(original_text)
    
    # Получаем video_end_with из original_text, если он там есть
    _, parsed_start, parsed_end, _, _, _, _ = extract_url_range_tags(original_text)
    video_end_with = parsed_end if parsed_end != 1 or parsed_start != 1 else (video_start_with + video_count - 1)
    
    # Определяем, нужен ли обратный порядок (когда start > end)
    # Для отрицательных индексов: -1 до -7 означает обратный порядок (7, 6, 5, 4, 3, 2, 1)
    is_reverse_order = False
    has_negative_indices = False
    use_range_download = False  # Объявляем переменную заранее
    if is_playlist and video_start_with is not None and video_end_with is not None:
        # Если оба отрицательные, всегда используем обратный порядок
        if video_start_with < 0 and video_end_with < 0:
            is_reverse_order = True
            has_negative_indices = True
        # Если start > end, это обратный порядок
        elif video_start_with > video_end_with:
            is_reverse_order = True
    
    # Формируем список индексов с учетом обратного порядка
    # Для отрицательных индексов нужно будет преобразовать их в положительные после получения общего количества видео
    if is_playlist:
        if has_negative_indices:
            # Для отрицательных индексов сначала создаем список с отрицательными значениями
            # Позже преобразуем их в положительные после получения общего количества видео
            # -1 до -7 означает: качать в порядке 7, 6, 5, 4, 3, 2, 1 (от последнего к первому)
            # Создаем список от -1 до -7 включительно: [-1, -2, -3, -4, -5, -6, -7]
            if abs(video_start_with) < abs(video_end_with):
                # -1 до -7: создаем список [-1, -2, -3, -4, -5, -6, -7]
                requested_indices = list(range(video_start_with, video_end_with - 1, -1))
            else:
                # -7 до -1: создаем список [-7, -6, -5, -4, -3, -2, -1]
                requested_indices = list(range(video_start_with, video_end_with + 1, 1))
        elif is_reverse_order:
            # Для обратного порядка: от start до end включительно в обратном порядке
            requested_indices = list(range(video_start_with, video_end_with - 1, -1))
        else:
            # Для прямого порядка: от start до end включительно
            requested_indices = list(range(video_start_with, video_start_with + video_count))
    else:
        requested_indices = []
    playlist_indices_all = requested_indices[:] if requested_indices else []
    cached_videos = {}
    uncached_indices = []
    
    # Check active functions (TRIM, SUBS, DUBS) - disable cache if any are active
    from DOWN_AND_UP.always_ask_menu import get_active_functions
    active_funcs = get_active_functions(user_id, url)
    should_disable_cache = active_funcs["should_disable_cache"]
    
    if safe_quality_key and is_playlist:
        # Check if cache should be disabled due to active functions
        if should_disable_cache:
            logger.info(f"[VIDEO CACHE] Active functions detected for user {user_id}, URL: {url}, disabling cache. TRIM: {active_funcs['has_trim']}, SUBS: {active_funcs['has_subs']}, DUBS: {active_funcs['has_dubs']}")
            cached_videos = {}
            uncached_indices = requested_indices
        # Check if Always Ask mode is enabled - if yes, skip cache completely
        elif not is_subs_always_ask(user_id):
            # Check if content is NSFW before looking in cache
            from HELPERS.porn import is_porn
            is_nsfw = is_porn(url, "", "", None) or user_forced_nsfw
            logger.info(f"[FALLBACK] is_porn check for {url}: {is_porn(url, '', '', None)}, user_forced_nsfw: {user_forced_nsfw}, final is_nsfw: {is_nsfw}")
            
            if not is_nsfw:
                cached_videos = get_cached_playlist_videos(get_clean_playlist_url(url), safe_quality_key, requested_indices)
                logger.info(f"[VIDEO CACHE] Checking cache for regular playlist: url={url}, quality={safe_quality_key}")
            else:
                logger.info(f"[VIDEO CACHE] Skipping cache check for NSFW playlist: url={url}, quality={safe_quality_key}")
                cached_videos = {}
        else:
            logger.info(f"[VIDEO CACHE] Skipping cache check for playlist because Always Ask mode is enabled: url={url}, quality={safe_quality_key}")
            cached_videos = {}
        
        uncached_indices = [i for i in requested_indices if i not in cached_videos]
        # First, repost the cached ones (skip if send_as_file is enabled)
        if cached_videos and (not use_range_download or len(uncached_indices) == 0):
            # Check if send_as_file is enabled - if so, skip cache repost
            from COMMANDS.args_cmd import get_user_args
            user_args = get_user_args(user_id)
            send_as_file = user_args.get("send_as_file", False)
            
            if not send_as_file:
                for index in requested_indices:
                    if index in cached_videos:
                        try:
                            # For cached content, always use regular channel (no NSFW/PAID in cache)
                            from_chat_id = get_log_channel("video")
                            channel_type = "regular"
                            
                            logger.info(f"[VIDEO CACHE] Reposting video {index} from channel {from_chat_id} to user {user_id}, message_id={cached_videos[index]}")
                            forward_kwargs = {
                                'chat_id': user_id,
                                'from_chat_id': from_chat_id,
                                'message_ids': [cached_videos[index]]
                            }
                            # Only apply thread_id in groups/channels, not in private chats
                            if getattr(message.chat, "type", None) != enums.ChatType.PRIVATE:
                                thread_id = getattr(message, 'message_thread_id', None)
                                if thread_id:
                                    forward_kwargs['message_thread_id'] = thread_id
                            app.forward_messages(**forward_kwargs)
                        except Exception as e:
                            logger.error(f"down_and_up: error reposting cached video index={index}: {e}")
            else:
                # If send_as_file is enabled, treat all indices as uncached
                logger.info(f"[VIDEO CACHE] send_as_file enabled for user {user_id}, skipping cache repost for playlist")
                uncached_indices = requested_indices
            
            if len(uncached_indices) == 0:
                app.send_message(user_id, safe_get_messages(user_id).PLAYLIST_SENT_FROM_CACHE_MSG.format(cached=len(cached_videos), total=len(requested_indices)), reply_parameters=ReplyParameters(message_id=message.id))
                send_to_logger(message, LoggerMsg.PLAYLIST_VIDEOS_SENT_FROM_CACHE.format(quality=safe_quality_key, user_id=user_id))
                return
            else:
                app.send_message(user_id, safe_get_messages(user_id).CACHE_PARTIAL_MSG.format(cached=len(cached_videos), total=len(requested_indices)), reply_parameters=ReplyParameters(message_id=message.id))
        elif cached_videos:
            logger.info("[VIDEO CACHE] Skipping partial cache replay for negative range to avoid duplicate downloads")
            uncached_indices = requested_indices
        else:
            logger.info(f"[VIDEO CACHE] Skipping cache check for playlist because Always Ask mode is enabled: url={url}, quality={safe_quality_key}")
            # Set all indices as uncached when Always Ask mode is enabled
            uncached_indices = requested_indices
    elif safe_quality_key and not is_playlist:
        # Check if cache should be disabled due to active functions
        if should_disable_cache:
            logger.info(f"[VIDEO CACHE] Active functions detected for user {user_id}, URL: {url}, disabling cache. TRIM: {active_funcs['has_trim']}, SUBS: {active_funcs['has_subs']}, DUBS: {active_funcs['has_dubs']}")
            cached_ids = None
        #found_type = check_subs_availability(url, user_id, safe_quality_key, return_type=True)
        elif not need_subs and not is_subs_always_ask(user_id):
            # Check if content is NSFW before looking in cache
            from HELPERS.porn import is_porn
            is_nsfw = is_porn(url, "", "", None) or user_forced_nsfw
            logger.info(f"[FALLBACK] is_porn check for {url}: {is_porn(url, '', '', None)}, user_forced_nsfw: {user_forced_nsfw}, final is_nsfw: {is_nsfw}")
            
            cached_ids = None
            if not is_nsfw:
                cached_ids = get_cached_message_ids(url, safe_quality_key)
                logger.info(f"[VIDEO CACHE] Checking cache for regular content: url={url}, quality={safe_quality_key}")
            else:
                logger.info(f"[VIDEO CACHE] Skipping cache check for NSFW content: url={url}, quality={safe_quality_key}")
                cached_ids = None
            
            if cached_ids:
                # Check if send_as_file is enabled - if so, skip cache repost
                from COMMANDS.args_cmd import get_user_args
                user_args = get_user_args(user_id)
                send_as_file = user_args.get("send_as_file", False)
                
                if not send_as_file:
                    #found_type = None
                    try:
                        # For cached content, always use regular channel (no NSFW/PAID in cache)
                        from_chat_id = get_log_channel("video")
                        channel_type = "regular"
                        
                        logger.info(f"[VIDEO CACHE] Reposting video from channel {from_chat_id} to user {user_id}, message_ids={cached_ids}")
                        forward_kwargs = {
                            'chat_id': user_id,
                            'from_chat_id': from_chat_id,
                            'message_ids': cached_ids
                        }
                        # Only apply thread_id in groups/channels, not in private chats
                        if getattr(message.chat, "type", None) != enums.ChatType.PRIVATE:
                            thread_id = getattr(message, 'message_thread_id', None)
                            if thread_id:
                                forward_kwargs['message_thread_id'] = thread_id
                        app.forward_messages(**forward_kwargs)
                        app.send_message(user_id, safe_get_messages(user_id).VIDEO_SENT_FROM_CACHE_MSG, reply_parameters=ReplyParameters(message_id=message.id))
                        send_to_logger(message, LoggerMsg.VIDEO_SENT_FROM_CACHE.format(quality=safe_quality_key, user_id=user_id))
                        return
                    except Exception as e:
                        logger.error(f"Error reposting video from cache: {e}")
                        # Always save to cache regardless of subtitles or Always Ask mode
                        # The cache will be used for display purposes (rocket emoji) but not for reposting
                        _save_video_cache_with_logging(url, safe_quality_key, [], original_text="", user_id=user_id, download_sections=download_sections, has_subs=need_subs, has_dubs=has_dubs)
                        # Don't show error message if we successfully got video from cache
                        # The video was already sent successfully in the try block
                else:
                    # If send_as_file is enabled, skip cache repost and continue with download
                    logger.info(f"[VIDEO CACHE] send_as_file enabled for user {user_id}, skipping cache repost for single video")
        else:
            if is_subs_always_ask(user_id):
                logger.info(f"[VIDEO CACHE] Skipping cache check because Always Ask mode is enabled: url={url}, quality={safe_quality_key}")
            elif need_subs:
                logger.info(f"[VIDEO CACHE] Skipping cache check because subtitles are enabled: url={url}, quality={safe_quality_key}")
            else:
                logger.info(f"[VIDEO CACHE] Skipping cache check for other reasons: url={url}, quality={safe_quality_key}")
    else:
        logger.info(f"down_and_up: safe_quality_key is None, skipping cache check")

    status_msg = None
    status_msg_id = None
    hourglass_msg = None
    hourglass_msg_id = None
    anim_thread = None
    stop_anim = threading.Event()
    download_started_msg_id = None
    proc_msg = None
    proc_msg_id = None
    try:
        # Check if there is a saved waiting time
        user_dir = os.path.join("users", str(user_id))
        flood_time_file = os.path.join(user_dir, "flood_wait.txt")

        # We send the initial message
        if os.path.exists(flood_time_file):
            with open(flood_time_file, 'r') as f:
                wait_time = int(f.read().strip())
                hours = wait_time // 3600
                minutes = (wait_time % 3600) // 60
                seconds = wait_time % 60
                time_str = f"{hours}h {minutes}m {seconds}s"
                proc_msg = safe_send_message(user_id, safe_get_messages(user_id).RATE_LIMIT_WITH_TIME_MSG.format(time=time_str), message=message)
        else:
            proc_msg = safe_send_message(user_id, safe_get_messages(user_id).RATE_LIMIT_NO_TIME_MSG, message=message)

        # We are trying to replace with "Download started"
        try:
            app.edit_message_text(
                chat_id=user_id,
                message_id=proc_msg.id,
                text=safe_get_messages(user_id).DOWNLOAD_STARTED_MSG,
                parse_mode=enums.ParseMode.HTML
            )
            try:
                from HELPERS.safe_messeger import schedule_delete_message
                download_started_msg_id = proc_msg.id
                schedule_delete_message(user_id, download_started_msg_id, delete_after_seconds=5)
            except Exception:
                pass
            # If you managed to replace, then there is no flood error
            if os.path.exists(flood_time_file):
                os.remove(flood_time_file)
        except FloodWait as e:
            # Update the counter
            wait_time = e.value
            os.makedirs(user_dir, exist_ok=True)
            with open(flood_time_file, 'w') as f:
                f.write(str(wait_time))
            return
        except Exception as e:
            logger.error(f"Error editing message: {e}")
            # Check if error is related to quality_key
            if "'quality_key'" in str(e):
                _handle_quality_key_error(e, split_msg_ids, is_playlist, successful_uploads, indices_to_download, video_count, user_id, proc_msg_id, message, app)
            # Stop animation before returning
            stop_anim.set()
            if anim_thread:
                anim_thread.join(timeout=1)
            return

        # If there is no flood error, send a normal message
        proc_msg = app.send_message(user_id, safe_get_messages(user_id).PROCESSING_MSG, reply_parameters=ReplyParameters(message_id=message.id))
        # Pin proc/status message for visibility
        try:
            app.pin_chat_message(user_id, proc_msg.id, disable_notification=True)
        except Exception:
            pass
        proc_msg_id = proc_msg.id
        error_message = ""
        hls_file_found = False  # Initialize hls_file_found for HLS stream handling
        status_msg = None
        status_msg_id = None
        hourglass_msg = None
        hourglass_msg_id = None
        anim_thread = None
        # Note: hourglass animation will be started later when hourglass_msg_id is available

        # Check if there's enough disk space (estimate 2GB per video)
        user_dir_name = os.path.abspath(os.path.join("users", str(user_id)))
        create_directory(user_dir_name)

        # Оценка требуемого места: сначала берём из yt-dlp точный/приблизительный размер,
        # затем оцениваем по битрейту и длительности, в крайнем случае 2 ГБ.
        required_bytes = 2 * 1024 * 1024 * 1024
        try:
            # Try to use cached info first for size check
            if cached_video_info:
                info_probe = cached_video_info
                logger.info(f"✅ [OPTIMIZATION] Using cached video info for size check")
            else:
                from DOWN_AND_UP.yt_dlp_hook import get_video_formats
                info_probe = get_video_formats(url, user_id, cookies_already_checked=cookies_already_checked)
                logger.info(f"⚠️ [OPTIMIZATION] Had to fetch video info for size check")
            size = 0
            if isinstance(info_probe, dict):
                size = info_probe.get('filesize') or info_probe.get('filesize_approx') or 0
                if not size:
                    # fallback по tbr*duration
                    tbr = info_probe.get('tbr') or 0  # total bitrate in Kbps
                    duration = info_probe.get('duration') or 0
                    if tbr and duration:
                        # tbr Kbps -> bytes/sec: tbr*1000/8, *duration
                        size = int((float(tbr) * 1000.0 / 8.0) * float(duration))
                    else:
                        # последний шанс: взять максимальный tbr из форматов
                        formats = info_probe.get('formats') or []
                        best_tbr = 0
                        for f in formats:
                            ftbr = f.get('tbr') or 0
                            if ftbr and ftbr > best_tbr:
                                best_tbr = ftbr
                        if best_tbr and duration:
                            size = int((float(best_tbr) * 1000.0 / 8.0) * float(duration))
            if size and size > 0:
                required_bytes = int(size * 1.2)  # 20% запас
        except Exception:
            pass

        if not check_disk_space(user_dir_name, required_bytes):
            send_to_user(message, safe_get_messages(user_id).ERROR_NO_DISK_SPACE_MSG)
            return

        # Create user directory (subscription already checked in video_extractor)
        user_dir = os.path.join("users", str(user_id))
        if not os.path.exists(user_dir):
            os.makedirs(user_dir, exist_ok=True)

        # Try to get download directory from ask_quality_menu first
        from DOWN_AND_UP.always_ask_menu import get_user_download_dir, generate_download_dir_name
        user_dir_name = get_user_download_dir(user_id)
        
        # If no download directory from ask_quality_menu, create one
        if not user_dir_name or not os.path.exists(user_dir_name):
            try:
                # Generate download directory name based on URL
                dir_name = generate_download_dir_name(url)
                unique_download_dir = os.path.join(user_dir, "downloads", dir_name)
                os.makedirs(unique_download_dir, exist_ok=True)
                
                # Update user_dir_name to use the unique directory
                user_dir_name = unique_download_dir
                
                logger.info(f"Created download directory: {unique_download_dir}")
            except Exception as e:
                logger.warning(f"Failed to create download directory, using default: {e}")
                # Fallback to original behavior
                user_dir_name = os.path.abspath(os.path.join("users", str(user_id)))


        # Pre-cleanup: remove all media files from unique download directory before starting
        try:
            logger.info(f"Pre-cleanup: removing old media files from unique directory {user_dir_name}")
            if os.path.exists(user_dir_name):
                for root, dirs, files in os.walk(user_dir_name):
                    for file in files:
                        file_path = os.path.join(root, file)
                        try:
                            # Remove all media files (keep .txt and .json files)
                            if file.lower().endswith((
                                '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff',
                                '.mp4', '.m4v', '.avi', '.mov', '.mkv', '.webm', '.flv',
                                '.mp3', '.wav', '.ogg', '.m4a',
                                '.pdf', '.doc', '.docx', '.zip', '.rar', '.7z'
                            )):
                                os.remove(file_path)
                                logger.info(f"Pre-cleanup: removed file {file_path}")
                        except Exception as e:
                            logger.warning(f"Pre-cleanup: failed to remove file {file_path}: {e}")
                    
                    # Remove empty directories (except unique download root)
                    for dir_name in dirs:
                        dir_path = os.path.join(root, dir_name)
                        try:
                            if os.path.exists(dir_path) and not os.listdir(dir_path) and dir_path != user_dir_name:
                                os.rmdir(dir_path)
                                logger.info(f"Pre-cleanup: removed empty directory {dir_path}")
                        except Exception as e:
                            logger.warning(f"Pre-cleanup: failed to remove directory {dir_path}: {e}")
            
            # Create protection file for parallel downloads
            from HELPERS.filesystem_hlp import is_parallel_download_allowed, create_protection_file
            if is_parallel_download_allowed(message):
                create_protection_file(user_dir_name)
            
            logger.info(f"Pre-cleanup completed for unique directory {user_dir_name}")
        except Exception as e:
            logger.warning(f"Pre-cleanup failed for unique directory {user_dir_name}: {e}")

        # Reset of the flag of errors for the new launch of the playlist
        if playlist_name:
            with playlist_errors_lock:
                error_key = f"{user_id}_{playlist_name}"
                if error_key in playlist_errors:
                    del playlist_errors[error_key]

        # if use_default_format is True, then do not take from format.txt, but use default ones
        custom_format_path = os.path.join(user_dir_name, "format.txt")
        use_default_format = False
        if not format_override and os.path.exists(custom_format_path):
            with open(custom_format_path, "r", encoding="utf-8") as f:
                custom_format = f.read().strip()
            if custom_format == "ALWAYS_ASK":
                use_default_format = True
        if use_default_format:
            format_override = None

        # Get user's merge_output_format preference once
        from COMMANDS.args_cmd import get_user_ytdlp_args
        user_args = get_user_ytdlp_args(user_id, url)
        user_merge_format = user_args.get('merge_output_format', 'mp4')
        
        # Check session MKV override first (from Always Ask menu)
        try:
            from COMMANDS.format_cmd import get_session_mkv_override
            session_mkv = get_session_mkv_override(user_id)
            logger.info(f"Session MKV override for user {user_id}: {session_mkv}")
            if session_mkv is not None:
                # Use session override
                effective_merge_format = 'mkv' if session_mkv else user_merge_format
                logger.info(f"Using session MKV override: effective_merge_format={effective_merge_format}")
            else:
                effective_merge_format = user_merge_format
                logger.info(f"No session override, using user preference: effective_merge_format={effective_merge_format}")
        except Exception as e:
            logger.error(f"Error checking session MKV override: {e}")
            effective_merge_format = user_merge_format
        
        if format_override:
            attempts = [{'format': format_override, 'prefer_ffmpeg': True, 'merge_output_format': effective_merge_format}]
            logger.info(f"Created attempts with format_override and merge_output_format={effective_merge_format}")
        else:
            # if use_default_format is True, then do not take from format.txt, but use default ones
            if use_default_format:
                attempts = [
                    {'format': 'bv*[vcodec*=avc1][height<=1080][height>720]+ba[acodec*=mp4a]/bv*[vcodec*=avc1][height<=1080]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/bv+ba/best', 'prefer_ffmpeg': True, 'merge_output_format': user_merge_format, 'extract_flat': False},
                    {'format': 'best', 'prefer_ffmpeg': False, 'extract_flat': False}
                ]
            else:
                if os.path.exists(custom_format_path):
                    with open(custom_format_path, "r", encoding="utf-8") as f:
                        custom_format = f.read().strip()
                    if custom_format.lower() == "best":
                        attempts = [{'format': custom_format, 'prefer_ffmpeg': False}]
                    else:
                        attempts = [{'format': custom_format, 'prefer_ffmpeg': True, 'merge_output_format': user_merge_format}]
                else:
                    attempts = [
                        {'format': 'bv*[vcodec*=avc1][height<=1080][height>720]+ba[acodec*=mp4a]/bv*[vcodec*=avc1][height<=1080]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/bv+ba/best',
                        'prefer_ffmpeg': True, 'merge_output_format': user_merge_format, 'extract_flat': False},
                        {'format': 'bv*[vcodec*=avc1]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/bestvideo+bestaudio/best/bv+ba/best',
                        'prefer_ffmpeg': True, 'merge_output_format': user_merge_format, 'extract_flat': False},
                        {'format': 'best', 'prefer_ffmpeg': False, 'extract_flat': False}
                    ]

        status_msg = safe_send_message(user_id, safe_get_messages(user_id).VIDEO_PROCESSING_MSG, message=message)
        hourglass_msg = safe_send_message(user_id, safe_get_messages(user_id).PLEASE_WAIT_MSG, message=message)
        try:
            from HELPERS.safe_messeger import schedule_delete_message
            if status_msg and hasattr(status_msg, 'id'):
                schedule_delete_message(user_id, status_msg.id, delete_after_seconds=5)
        except Exception:
            pass
        # We save ID status messages
        status_msg_id = status_msg.id
        hourglass_msg_id = hourglass_msg.id

        anim_thread = start_hourglass_animation(user_id, hourglass_msg_id, stop_anim)

        # Get info_dict to estimate the size of the selected quality
        try:
            ydl_opts = {
                'quiet': True,
                'extractor_args': {
                    'youtubetab': {'skip': ['authcheck']}
                }
            }
            # Try to use cookies from download directory first, then fallback to user root
            download_cookie_path = os.path.join(user_dir_name, "cookie.txt")
            user_cookie_path = os.path.join("users", str(user_id), "cookie.txt")
            
            if os.path.exists(download_cookie_path):
                ydl_opts['cookiefile'] = download_cookie_path
                logger.info(f"Using cookies from download directory: {download_cookie_path}")
            elif os.path.exists(user_cookie_path):
                ydl_opts['cookiefile'] = user_cookie_path
                logger.info(f"Using cookies from user directory: {user_cookie_path}")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                pre_info = ydl.extract_info(url, download=False)
            # Normalize to dict and check None
            if isinstance(pre_info, list):
                pre_info = (pre_info[0] if len(pre_info) > 0 else {})
            elif isinstance(pre_info, dict) and 'entries' in pre_info and isinstance(pre_info['entries'], list) and pre_info['entries']:
                pre_info = pre_info['entries'][0]
            if pre_info is None:
                logger.warning("pre_info is None, skipping size check")
                pre_info = {}
        except Exception as e:
            logger.warning(f"Failed to extract info for size check: {e}")
            pre_info = {}

        # Find format for selected safe_quality_key
        selected_format = None
        for f in pre_info.get('formats', []):
            w = f.get('width')
            h = f.get('height')
            if w and h:
                qk = get_quality_by_min_side(w, h)
                if str(qk) == str(safe_quality_key):
                    selected_format = f
                    break

        # If you did not find the format, STOP downloading!
        #if not selected_format:
            #logger.warning(f"[SIZE CHECK] Could not determine format for quality_key={quality_key}. Download will not start.")
            #app.send_message(
                #user_id,
                #"Unable to determine the file size for the selected quality. Please try another quality or check your cookies.",
                #reply_to_message_id=message.id
            #)
            #return

        
        # Checking the limit
        #from _config import Config
        BYTES_IN_GIB = 1024 ** 3
        max_size_gb = getattr(Config, 'MAX_FILE_SIZE', 10)
        max_size_bytes = int(max_size_gb * BYTES_IN_GIB)
        # Get the file size
        if selected_format is None:
            logger.warning("selected_format is None, skipping size check")
            filesize = 0
            allowed = True  # Allow download if we can't determine the size
        else:
            filesize = selected_format.get('filesize') or selected_format.get('filesize_approx')
            if filesize is None:
                # fallback on rating
                tbr = selected_format.get('tbr')
                duration = selected_format.get('duration')
                if tbr is not None and duration is not None:
                    try:
                        filesize = float(tbr) * float(duration) * 125
                    except (TypeError, ValueError):
                        filesize = None
                else:
                    filesize = None
                
                if filesize is None:
                    width = selected_format.get('width')
                    height = selected_format.get('height')
                    duration = selected_format.get('duration')
                    if width is not None and height is not None and duration is not None:
                        try:
                            filesize = int(width) * int(height) * float(duration) * 0.07
                        except (TypeError, ValueError):
                            filesize = 0
                    else:
                        filesize = 0

            allowed = check_file_size_limit(selected_format, max_size_bytes=max_size_bytes, message=message)
        
        # Secure file size logging
        try:
            filesize_val = float(filesize) if filesize is not None else 0
            if filesize_val > 0:
                size_gb = filesize_val/(1024**3)
                logger.info(f"[SIZE CHECK] safe_quality_key={safe_quality_key}, determined size={size_gb:.2f} GB, limit={max_size_gb} GB, allowed={allowed}")
            else:
                logger.info(f"[SIZE CHECK] safe_quality_key={safe_quality_key}, size unknown, limit={max_size_gb} GB, allowed={allowed}")
        except (TypeError, ValueError):
            logger.info(f"[SIZE CHECK] safe_quality_key={safe_quality_key}, size unknown, limit={max_size_gb} GB, allowed={allowed}")

        if not allowed:
            app.send_message(
                user_id,
                safe_get_messages(user_id).ERROR_FILE_SIZE_LIMIT_MSG.format(limit=max_size_gb),
                reply_parameters=ReplyParameters(message_id=message.id)
            )
            log_error_to_channel(message, safe_get_messages(user_id).SIZE_LIMIT_EXCEEDED.format(max_size_gb=max_size_gb), url)
            logger.warning(f"[SIZE CHECK] Download for safe_quality_key={safe_quality_key} was blocked due to size limit.")
            return
        else:
            logger.info(f"[SIZE CHECK] Download for safe_quality_key={safe_quality_key} is allowed and will proceed.")

        current_total_process = ""
        last_update = 0
        full_bar = "🟩" * 10
        first_progress_update = True  # Flag for tracking the first update
        progress_start_time = time.time()
        # One-time retry guards to avoid infinite retry loops across attempts
        # (already initialized at the beginning of the function)
        
        # Check if this is an HLS stream (needed for progress_func)
        # This will be updated later based on actual format detection
        is_hls = ("m3u8" in url.lower())

        def progress_func(d):
            messages = safe_get_messages(message.chat.id)
            nonlocal last_update, first_progress_update, is_hls
            # Check the timeout
            if check_download_timeout(user_id):
                raise Exception(f"Download timeout exceeded ({safe_get_messages(user_id).DOWNLOAD_TIMEOUT // 3600} hours)")
            current_time = time.time()
            
            def build_progress_metadata(downloaded_bytes, total_bytes):
                info_dict = d.get("info_dict") or {}
                fmt = selected_format or {}
                width = fmt.get("width") or info_dict.get("width")
                height = fmt.get("height") or info_dict.get("height")
                resolution = f"{width}x{height}" if width and height else None
                filesize = (
                    total_bytes
                    or fmt.get("filesize")
                    or fmt.get("filesize_approx")
                    or info_dict.get("filesize")
                    or info_dict.get("filesize_approx")
                )
                duration_val = (
                    fmt.get("duration")
                    or info_dict.get("duration")
                )
                metadata_payload = {
                    "downloaded_bytes": downloaded_bytes,
                    "total_bytes": total_bytes,
                    "filesize": filesize,
                    "duration": duration_val,
                    "resolution": resolution,
                    "quality": fmt.get("format_note") or safe_quality_key,
                    "ext": fmt.get("ext") or info_dict.get("ext"),
                    "speed": d.get("speed"),
                    "eta": d.get("eta"),
                    "domain": urlparse(url).netloc,
                    "thumbnail": info_dict.get("thumbnail"),
                }
                return {k: v for k, v in metadata_payload.items() if v is not None}
            
            # Calculate elapsed time and minutes passed
            elapsed = max(0, current_time - progress_start_time)
            minutes_passed = int(elapsed // 60)
            
            # Adaptive throttle: linear slow-down; after 1h fixed 90s
            if minutes_passed and minutes_passed >= 60:
                interval = 90.0
            else:
                # 0-4 min: 3s, 5-9: 4s, ..., 55-59: 14s
                interval = 3.0 + max(0, minutes_passed // 5)
            
            if current_time - last_update < interval:
                return
                
            if d.get("status") == "downloading":
                downloaded = d.get("downloaded_bytes", 0)
                # yt-dlp may provide only total_bytes_estimate for some sites
                total = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
                percent = (downloaded / total * 100) if total else 0
                blocks = int(percent // 10)
                bar = "🟩" * blocks + "⬜️" * (10 - blocks)
                
                # Обновляем прогресс в статистике
                try:
                    update_download_progress(
                        user_id=user_id,
                        progress=percent,
                        url=url,
                        title=title,
                        metadata=build_progress_metadata(downloaded, total),
                    )
                except Exception as e:
                    logger.debug(f"Failed to update download progress: {e}")
                
                # For HLS, update progress data for cycle animation
                if is_hls and hasattr(progress_func, 'progress_data') and progress_func.progress_data:
                    progress_func.progress_data['downloaded_bytes'] = downloaded
                    progress_func.progress_data['total_bytes'] = total
                try:
                    # With the first renewal of progress, we delete the first posts Processing
                    if first_progress_update:
                        try:
                            # Боты не могут использовать get_chat_history, поэтому просто логируем
                            logger.info("Skipping message cleanup - bots cannot use get_chat_history")
                        except Exception as e:
                            logger.error(f"Error in message cleanup: {e}")
                            # Check if error is related to quality_key
                            if "'quality_key'" in str(e):
                                _handle_quality_key_error(e, split_msg_ids, is_playlist, successful_uploads, indices_to_download, video_count, user_id, proc_msg_id, message, app)
                        first_progress_update = False

                    progress_text = f"{current_total_process}\n{bar}   {percent:.1f}%"
                    logger.info(f"Updating progress for user {user_id}, message {proc_msg_id}: {progress_text}")
                    result = safe_edit_message_text(user_id, proc_msg_id, progress_text)
                    if result is None:
                        logger.warning(f"Failed to update progress message {proc_msg_id} for user {user_id} - message may have been deleted")
                except Exception as e:
                    logger.error(f"Error updating progress: {e}")
                    # Check if error is related to quality_key
                    if "'quality_key'" in str(e):
                        _handle_quality_key_error(e, split_msg_ids, is_playlist, successful_uploads, indices_to_download, video_count, user_id, proc_msg_id, message, app)
            elif d.get("status") == "finished":
                # Обновляем прогресс до 100% при завершении
                total = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
                try:
                    update_download_progress(
                        user_id=user_id,
                        progress=100.0,
                        url=url,
                        title=title,
                        metadata=build_progress_metadata(total or 0, total or 0),
                    )
                except Exception as e:
                    logger.debug(f"Failed to update download progress on finish: {e}")
                try:
                    safe_edit_message_text(user_id, proc_msg_id, safe_get_messages(user_id).VIDEO_DOWNLOAD_COMPLETE_MSG.format(process=current_total_process, bar=full_bar))
                except Exception as e:
                    logger.error(f"Error updating progress: {e}")
                    # Check if error is related to quality_key
                    if "'quality_key'" in str(e):
                        _handle_quality_key_error(e, split_msg_ids, is_playlist, successful_uploads, indices_to_download, video_count, user_id, proc_msg_id, message, app)
            elif d.get("status") == "error":
                # Сбрасываем прогресс при ошибке
                downloaded = d.get("downloaded_bytes", 0)
                total = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
                try:
                    update_download_progress(
                        user_id=user_id,
                        progress=None,
                        url=url,
                        title=title,
                        metadata=build_progress_metadata(downloaded, total),
                    )
                except Exception as e:
                    logger.debug(f"Failed to update download progress on error: {e}")
                logger.error("Error occurred during download.")
                send_error_to_user(message, safe_get_messages(user_id).DOWNLOAD_ERROR_GENERIC)
            last_update = current_time

        successful_uploads = 0

        def try_download(url, attempt_opts):
            messages = safe_get_messages(message.chat.id)
            nonlocal current_total_process, error_message, did_cookie_retry, did_proxy_retry, did_live_from_start_retry, is_hls, error_message_sent, is_reverse_order, use_range_download, current_playlist_items_override, range_entries_metadata, download_sections, hls_file_found
            # Initialize hls_file_found for this download attempt
            hls_file_found = False
            
            # Ensure download directory exists before setting outtmpl
            try:
                os.makedirs(user_dir_name, exist_ok=True)
            except Exception as e:
                logger.error(f"Failed to create download directory {user_dir_name}: {e}")
            
            # Use a very short, ID‑based filename for the first attempt to avoid
            # hitting filesystem "File name too long" limits (especially with
            # long Unicode titles and yt-dlp suffixes like dash/fdash, .part, etc.)
            # We intentionally avoid using the video title in the filename here;
            # the human‑readable title is still preserved separately in captions.
            original_outtmpl = os.path.join(user_dir_name, "%(id)s.%(ext)s")
            
            # First try with original filename
            # Для отрицательных индексов используем весь диапазон сразу
            if current_playlist_items_override:
                playlist_items_str = current_playlist_items_override
            elif is_reverse_order and is_playlist:
                # Для обратного порядка используем формат START:STOP:-1
                playlist_items_str = f"{current_index}:{current_index}:-1"
            else:
                # Для обычных случаев (включая отрицательные индексы, уже преобразованные в положительные)
                playlist_items_str = str(current_index)
            
            # Get user's custom yt-dlp arguments first to check thumbnail settings
            from COMMANDS.args_cmd import get_user_ytdlp_args, log_ytdlp_options
            user_args = get_user_ytdlp_args(user_id, url)
            
            # Check if user wants to embed thumbnail (default is True)
            embed_thumbnail = user_args.get('embed_thumbnail', True)  # Default True
            write_thumbnail = user_args.get('writethumbnail', True)  # Default True
            
            # Warn if embed_thumbnail is enabled but write_thumbnail is not
            if embed_thumbnail and not write_thumbnail:
                logger.info(f"User {user_id} enabled embed_thumbnail but not write_thumbnail. EmbedThumbnail will try to use metadata thumbnails if available.")
            
            # Build postprocessors list based on user settings
            postprocessors = [{'key': 'FFmpegMetadata'}]
            if embed_thumbnail:
                # Add EmbedThumbnail (enabled by default)
                # Note: EmbedThumbnail will work even without write_thumbnail if thumbnail is available in metadata
                # Errors during embedding will be handled gracefully and won't stop download
                postprocessors.insert(0, {'key': 'EmbedThumbnail'})
                logger.info(f"User {user_id} embed_thumbnail={embed_thumbnail}, adding EmbedThumbnail postprocessor")
            
            # Check if user wants to ignore errors (default is False)
            # Note: ignore_errors is converted to ignoreerrors in get_user_ytdlp_args
            ignore_errors = user_args.get('ignoreerrors', False) if user_args else False
            
            common_opts = {
                'playlist_items': playlist_items_str,
                'outtmpl': original_outtmpl,
                'postprocessors': postprocessors,
                # Only use ignoreerrors if user explicitly enabled it via /args
                'ignoreerrors': ignore_errors,
                # Allow Unicode characters in filenames
                'restrictfilenames': False,
                'extractor_args': {
                    'generic': {'impersonate': ['chrome']},
                    'youtubetab': {'skip': ['authcheck']}
                },
                'referer': url,
                'geo_bypass': True,
                # check_certificate and no_check_certificates are set from user_args (default: check_certificate=False, no_check_certificates=True)
                'live_from_start': True if not did_live_from_start_retry else False
                #'socket_timeout': 60,  # Increase socket timeout
                #'retries': 15,  # Increase retries
                #'fragment_retries': 15,  # Increase fragment retries
                #'http_chunk_size': 5242880,  # 5MB chunks for better stability
                #'buffersize': 2048,  # Increase buffer size
                #'sleep_interval': 2,  # Sleep between requests
                #'max_sleep_interval': 10,  # Max sleep between requests
                #'read_timeout': 60,  # Read timeout
                #'connect_timeout': 30  # Connect timeout
            }
            
            # Add download_sections if trim is enabled
            if download_sections:
                common_opts['download_sections'] = [download_sections]
                
                # Extract start and end times from download_sections format: *HH:MM:SS-HH:MM:SS
                import re
                trim_match = re.match(r'\*(\d{2}):(\d{2}):(\d{2})-(\d{2}):(\d{2}):(\d{2})', download_sections)
                if trim_match:
                    start_h, start_m, start_s, end_h, end_m, end_s = map(int, trim_match.groups())
                    start_seconds = start_h * 3600 + start_m * 60 + start_s
                    end_seconds = end_h * 3600 + end_m * 60 + end_s
                    duration_seconds = end_seconds - start_seconds
                    
                    # Format times for ffmpeg: HH:MM:SS
                    start_time_str = f"{start_h:02d}:{start_m:02d}:{start_s:02d}"
                    end_time_str = f"{end_h:02d}:{end_m:02d}:{end_s:02d}"
                    
                    logger.info(f"[TRIM] Extracted trim times: start={start_time_str} ({start_seconds}s), end={end_time_str} ({end_seconds}s), duration={duration_seconds}s")
                    
                    # Note: FFmpegVideoConvertor doesn't support postprocessor_args in yt-dlp
                    # We rely on download_sections for trimming, which is already added to ytdl_opts
                    # Add FFmpegVideoRemuxer for remuxing after download_sections processing
                    has_remuxer = any(pp.get('key') == 'FFmpegVideoRemuxer' for pp in postprocessors)
                    if not has_remuxer:
                        remuxer_index = next((i for i, pp in enumerate(postprocessors) if pp.get('key') == 'FFmpegMetadata'), len(postprocessors))
                        postprocessors.insert(remuxer_index, {
                            'key': 'FFmpegVideoRemuxer',
                            'preferedformat': 'mp4',
                        })
                        logger.info(f"[TRIM] Added FFmpegVideoRemuxer for remuxing after download_sections trim")
                else:
                    logger.warning(f"[TRIM] Could not parse download_sections format: {download_sections}")
                    # Still add remuxer without explicit trim (rely on download_sections)
                    has_remuxer = any(pp.get('key') == 'FFmpegVideoRemuxer' for pp in postprocessors)
                    if not has_remuxer:
                        remuxer_index = next((i for i, pp in enumerate(postprocessors) if pp.get('key') == 'FFmpegMetadata'), len(postprocessors))
                        postprocessors.insert(remuxer_index, {
                            'key': 'FFmpegVideoRemuxer',
                            'preferedformat': 'mp4',
                        })
                logger.info(f"Added download_sections: {download_sections} for user {user_id}")
            
            # Define sanitize_title_for_filename function
            def sanitize_title_for_filename(title):
                messages = safe_get_messages(message.chat.id)
                """Sanitize title for filename using strict sanitization"""
                if not title:
                    return "video"
                from HELPERS.filesystem_hlp import sanitize_filename_strict
                return sanitize_filename_strict(title)
            
            # Add match_filter only if domain is not in NO_FILTER_DOMAINS
            # Add match_filter for domain filtering and title sanitization
            def sanitize_and_filter(info):
                messages = safe_get_messages(message.chat.id)
                # First save original title for caption before sanitizing
                if 'title' in info and info['title']:
                    original_title = info['title']
                    # Save original title for caption
                    info['original_title'] = original_title
                    # Sanitize title for filename
                    sanitized_title = sanitize_title_for_filename(original_title)
                    info['title'] = sanitized_title
                    logger.info(f"Sanitized title: '{original_title}' -> '{sanitized_title}'")
                
                # Then apply domain-specific filtering
                if not is_no_filter_domain(url):
                    return create_smart_match_filter(user_id=user_id, message=message)(info)
                else:
                    logger.info(f"Skipping domain filter for domain in NO_FILTER_DOMAINS: {url}")
                    return None  # Allow download
            
            common_opts['match_filter'] = sanitize_and_filter
            
            # Add user's custom yt-dlp arguments (after postprocessors are set)
            if user_args:
                # Remove embed_thumbnail from user_args as it's already handled via postprocessors
                user_args_copy = user_args.copy()
                user_args_copy.pop('embed_thumbnail', None)
                # ignoreerrors is already set above based on user's ignore_errors setting
                user_args_copy.pop('ignoreerrors', None)
                common_opts.update(user_args_copy)
            
            # Configure subtitle options based on user settings
            if need_subs and is_youtube_url(url):
                # In Always Ask mode with multiple subtitle selection, skip yt-dlp subtitle download
                # (subtitles will be downloaded separately in post-processing)
                if is_always_ask_mode and (subs_all_selected or (selected_subs_langs and len(selected_subs_langs) > 0)):
                    logger.info(f"Always Ask mode with multiple subtitles: skipping yt-dlp subtitle download, will download separately")
                    common_opts['writesubtitles'] = False
                    common_opts['writeautomaticsub'] = False
                else:
                    # Single language mode - use yt-dlp subtitle download
                    subs_lang = get_user_subs_language(user_id)
                    auto_mode = get_user_subs_auto_mode(user_id)
                    
                    if subs_lang and subs_lang not in ["OFF"]:
                        # Enable subtitle writing
                        common_opts['writesubtitles'] = True
                        common_opts['writeautomaticsub'] = auto_mode
                        
                        # Set subtitle language
                        if subs_lang != "auto":
                            common_opts['subtitleslangs'] = [subs_lang]
                        
                        logger.info(f"Enabled subtitle download for user {user_id}: lang={subs_lang}, auto_mode={auto_mode}")
                    else:
                        # Check availability and warn user if subtitles not found
                        from COMMANDS.subtitles_cmd import get_available_subs_languages
                        available_langs = get_available_subs_languages(url, user_id, auto_only=auto_mode)
                        # Flexible check: search for an exact match or any language from the group
                        lang_prefix = subs_lang.split('-')[0] if subs_lang else None
                        found = False
                        for l in available_langs:
                            if l == subs_lang or (subs_lang and (l.startswith(subs_lang + '-') or l.startswith(subs_lang + '.'))) \
                               or (lang_prefix and (l == lang_prefix or l.startswith(lang_prefix + '-') or l.startswith(lang_prefix + '.'))):
                                found = True
                                break
                        if not found and subs_lang:
                            from COMMANDS.subtitles_cmd import LANGUAGES
                            if subs_lang in LANGUAGES:
                                app.send_message(
                                    user_id,
                                    f"⚠️ Subtitles for {LANGUAGES[subs_lang]['flag']} {LANGUAGES[subs_lang]['name']} not found for this video. Download without subtitles.",
                                    reply_parameters=ReplyParameters(message_id=message.id)
                                )
            else:
                # Disable subtitle writing if subtitles are not needed
                common_opts['writesubtitles'] = False
                common_opts['writeautomaticsub'] = False
            
            # Log final yt-dlp options for debugging
            log_ytdlp_options(user_id, common_opts, "video_download")
            
            # Check if we need to use --no-cookies for this domain
            if is_no_cookie_domain(url):
                common_opts['cookiefile'] = None  # Equivalent to --no-cookies
                logger.info(f"Using --no-cookies for domain: {url}")
            else:
                # Check if cookie.txt exists in download directory first, then user's folder
                download_cookie_path = os.path.join(user_dir_name, "cookie.txt")
                user_cookie_path = os.path.join("users", str(user_id), "cookie.txt")
                
                # Для YouTube теперь не устраиваем тяжёлый повторный тест кук перед скачиванием.
                # Логика такая:
                #   * если у пользователя уже есть cookie.txt — просто используем его;
                #   * если нет — скачивание пойдёт без кук, а при реальной cookie‑ошибке
                #     перехватится в DownloadError и запустит retry_download_with_different_cookies.
                if is_youtube_url(url):
                    if os.path.exists(user_cookie_path):
                        common_opts['cookiefile'] = user_cookie_path
                        logger.info(f"[YOUTUBE COOKIES] Using existing user cookie file for download: {user_cookie_path}")
                    else:
                        common_opts['cookiefile'] = None
                        logger.info(f"[YOUTUBE COOKIES] No user cookie file found for download, starting without cookies")
                else:
                    # For non-YouTube URLs, use new cookie fallback system
                    from COMMANDS.cookies_cmd import get_cookie_cache_result, try_non_youtube_cookie_fallback
                    cache_result = get_cookie_cache_result(user_id, url)
                    
                    if cache_result and cache_result['result']:
                        # Use cached successful cookies
                        common_opts['cookiefile'] = cache_result['cookie_path']
                        logger.info(f"Using cached cookies for non-YouTube URL: {url}")
                    else:
                        # Try user cookies first
                        if os.path.exists(user_cookie_path):
                            common_opts['cookiefile'] = user_cookie_path
                            logger.info(f"Using user cookies for non-YouTube URL: {url}")
                        else:
                            # No user cookies, will try fallback during download
                            common_opts['cookiefile'] = None
                            logger.info(f"No user cookies found for non-YouTube URL: {url}, will try fallback during download")
            
            # If this is not a playlist with a range, add --no-playlist to the URL with the list parameter
            if not is_playlist and 'list=' in url:
                common_opts['noplaylist'] = True
            
            # Always use progress_hooks, even for HLS
            common_opts['progress_hooks'] = [progress_func]
            # Respect MKV toggle: remux to mkv when MKV is ON; otherwise prefer mp4
            # Check session override first (from Always Ask menu), then user preference
            try:
                from COMMANDS.format_cmd import get_session_mkv_override, get_user_mkv_preference
                mkv_on = get_session_mkv_override(user_id)
                logger.info(f"MKV session override for user {user_id}: {mkv_on}")
                if mkv_on is None:
                    # Fallback to user preference if no session override
                    mkv_on = get_user_mkv_preference(user_id)
                    logger.info(f"MKV user preference for user {user_id}: {mkv_on}")
                else:
                    logger.info(f"Using MKV session override: {mkv_on}")
            except Exception as e:
                logger.error(f"Error checking MKV preference: {e}")
                mkv_on = False

            # Adjust attempts' merge_output_format based on MKV preference
            try:
                if mkv_on:
                    for _attempt in attempts:
                        if isinstance(_attempt, dict):
                            _attempt['merge_output_format'] = 'mkv'
                    # Also set in common_opts to ensure it's applied
                    common_opts['merge_output_format'] = 'mkv'
                else:
                    for _attempt in attempts:
                        if isinstance(_attempt, dict) and 'merge_output_format' not in _attempt:
                            # Use user's preferred format
                            _attempt['merge_output_format'] = user_merge_format
            except Exception:
                pass

            ytdl_opts = {**common_opts, **attempt_opts}
            
            # Ensure MKV format is applied even if it wasn't in attempts
            if mkv_on:
                ytdl_opts['merge_output_format'] = 'mkv'
                logger.info(f"MKV mode enabled: setting merge_output_format=mkv, remux_video=mkv")
            
            # Add proxy configuration if needed
            if use_proxy:
                # Force proxy for this download
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
                    logger.info(f"Force using proxy for download: {proxy_url}")
                else:
                    logger.warning("Proxy requested but proxy configuration is incomplete")
            else:
                # Add proxy configuration if needed for this domain
                from HELPERS.proxy_helper import add_proxy_to_ytdl_opts
                ytdl_opts = add_proxy_to_ytdl_opts(ytdl_opts, url, user_id)
            
            # Add PO token provider for YouTube domains
            ytdl_opts = add_pot_to_ytdl_opts(ytdl_opts, url)
            
            # If MKV is ON, remux to mkv; else to mp4
            # Ensure merge_output_format is also set correctly
            if mkv_on:
                ytdl_opts['remux_video'] = 'mkv'
                # Force merge_output_format to mkv if not already set
                if 'merge_output_format' not in ytdl_opts or ytdl_opts.get('merge_output_format') != 'mkv':
                    ytdl_opts['merge_output_format'] = 'mkv'
                    logger.info("Forcing merge_output_format=mkv for MKV mode")
            else:
                # Only set remux_video to mp4 if MKV is explicitly OFF
                # But respect merge_output_format if it's already set to mkv
                if 'merge_output_format' in ytdl_opts and ytdl_opts['merge_output_format'] == 'mkv':
                    ytdl_opts['remux_video'] = 'mkv'
                else:
                    ytdl_opts['remux_video'] = 'mp4'
            try:
                logger.info(f"Starting yt-dlp extraction for URL: {url}")
                logger.info(f"yt-dlp options: {ytdl_opts}")
                
                # First, check if the requested format is available using cached info or get_video_formats
                check_info = None
                if cached_video_info:
                    check_info = cached_video_info
                    logger.info("✅ [OPTIMIZATION] Using cached video info for format check")
                else:
                    from DOWN_AND_UP.yt_dlp_hook import get_video_formats
                    logger.info("Checking available formats...")
                    check_info = get_video_formats(url, user_id, cookies_already_checked=cookies_already_checked, use_proxy=use_proxy)
                    logger.info("Format check completed")
                
                # Check if requested format exists
                requested_format = attempt_opts.get('format', '')
                if requested_format and requested_format != 'best':
                    available_formats = check_info.get('formats', [])
                    format_found = False
                    
                    # Check if requested format is available
                    if requested_format.startswith('id:'):
                        # Check for specific format ID
                        requested_id = requested_format.split(':', 1)[1]
                        for fmt in available_formats:
                            if fmt.get('format_id') == requested_id:
                                format_found = True
                                logger.info(f"Format ID {requested_id} found: {fmt.get('ext', 'unknown')} {fmt.get('resolution', 'unknown')}")
                                break
                        
                        if not format_found:
                            logger.warning(f"Format ID {requested_id} not found for this video")
                            # Notify user and stop download
                            try:
                                available_ids = [fmt.get('format_id', 'unknown') for fmt in available_formats[:10]]
                                logger.info(f"Available format IDs: {available_ids}")
                                send_error_to_user(
                                    message,
                                    safe_get_messages(user_id).FORMAT_ID_NOT_FOUND_MSG.format(format_id=requested_id, available_ids=', '.join(available_ids[:10])) +
                                    f"Use /list command to see all available formats."
                                )
                                return None
                            except Exception as e:
                                logger.error(f"Error sending format not found message: {e}")
                            return None
                    elif 'av01' in requested_format:
                        # Check for AV1 format specifically
                        for fmt in available_formats:
                            vcodec = fmt.get('vcodec')
                            if vcodec and vcodec.startswith('av01'):
                                format_found = True
                                break
                        
                        if not format_found:
                            logger.warning(f"AV1 format requested but not available for this video")
                            
                            # Also check if there are any video formats at all
                            video_formats = [fmt for fmt in available_formats if fmt.get('vcodec') and not fmt.get('vcodec').startswith('images')]
                            if not video_formats:
                                logger.warning(f"No video formats available at all for this video")
                            # Notify user and stop download
                            try:
                                # Filter out non-video formats (like storyboards)
                                video_formats = [fmt for fmt in available_formats if fmt.get('vcodec') and not fmt.get('vcodec').startswith('images')]
                                
                                available_formats_list = []
                                for fmt in video_formats[:5]:
                                    vcodec = fmt.get('vcodec', 'unknown')
                                    height = fmt.get('height', 'unknown')
                                    if vcodec and vcodec != 'unknown':
                                        available_formats_list.append(f"• {vcodec} {height}p")
                                
                                formats_text = "\n".join(available_formats_list) if available_formats_list else "• No video formats available"
                                
                                safe_edit_message_text(user_id, proc_msg_id, 
                                    f"{current_total_process}\n{safe_get_messages(user_id).DOWN_UP_AV1_NOT_AVAILABLE_MSG.format(formats_text=formats_text)}")
                            except Exception as e:
                                logger.error(f"Failed to notify user about format unavailability: {e}")
                            
                            # Send error message to user
                            # Filter out non-video formats (like storyboards)
                            video_formats = [fmt for fmt in available_formats if fmt.get('vcodec') and not fmt.get('vcodec').startswith('images')]
                            
                            available_formats_list = []
                            for fmt in video_formats[:5]:
                                vcodec = fmt.get('vcodec', 'unknown')
                                height = fmt.get('height', 'unknown')
                                if vcodec and vcodec != 'unknown':
                                    available_formats_list.append(f"• {vcodec} {height}p")
                            
                            formats_text = "\n".join(available_formats_list) if available_formats_list else "• No video formats available"
                            
                            send_to_user(message, 
                                safe_get_messages(user_id).AV1_FORMAT_NOT_AVAILABLE_MSG.format(formats_text=formats_text) +
                                safe_get_messages(user_id).AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG)
                            
                            return None
                
                # Try with proxy fallback if user proxy is enabled
                def extract_info_operation(opts):
                    messages = safe_get_messages(message.chat.id)
                    try:
                        with yt_dlp.YoutubeDL(opts) as ydl:
                            logger.info("yt-dlp instance created, starting extract_info...")
                            info_dict = ydl.extract_info(url, download=False)
                            logger.info("extract_info completed successfully")
                            return info_dict
                    except Exception as e:
                        error_text = str(e)
                        logger.warning(f"Error in extract_info_operation: {error_text[:200]}")
                        raise  # Re-raise to let caller handle it
                
                from HELPERS.proxy_helper import try_with_proxy_fallback, try_with_impersonate_fallback, is_cloudflare_error
                
                # Track last error for Cloudflare detection
                last_error_info = {'error': None, 'error_text': None}
                
                # Wrapper that catches exceptions and stores error info
                def extract_info_with_error_tracking(opts):
                    try:
                        return extract_info_operation(opts)
                    except Exception as e:
                        error_text = str(e)
                        logger.warning(f"Error in extract_info_with_error_tracking: {error_text[:200]}")
                        last_error_info['error'] = e
                        last_error_info['error_text'] = error_text
                        raise  # Re-raise to let caller handle it
                
                # First, try with original options to detect Cloudflare errors early
                info_dict = None
                original_error_text = None  # Сохраняем оригинальный текст ошибки
                try:
                    info_dict = extract_info_operation(ytdl_opts)
                except Exception as e:
                    error_text = str(e)
                    original_error_text = error_text  # Сохраняем оригинальный текст
                    logger.info(f"Initial extract_info failed: {error_text[:200]}")
                    last_error_info['error'] = e
                    last_error_info['error_text'] = error_text
                    
                    # If it's a Cloudflare error, try impersonate fallback first
                    if is_cloudflare_error(error_text):
                        logger.info(f"Cloudflare error detected for {url}, trying impersonate fallback first")
                        try:
                            impersonate_result = try_with_impersonate_fallback(ytdl_opts, url, user_id, extract_info_operation)
                            if impersonate_result is not None:
                                info_dict = impersonate_result
                                logger.info(f"Impersonate fallback succeeded for {url}")
                            else:
                                # If impersonate fallback failed, try proxy fallback
                                logger.info(f"Impersonate fallback failed for {url}, trying proxy fallback")
                                try:
                                    info_dict = try_with_proxy_fallback(ytdl_opts, url, user_id, extract_info_with_error_tracking)
                                except Exception as e3:
                                    logger.error(f"Proxy fallback also failed: {e3}")
                                    info_dict = None
                                if info_dict is None:
                                    raise Exception("Failed to extract video information with all available proxies and impersonate versions")
                        except Exception as e2:
                            logger.error(f"Impersonate fallback exception: {e2}")
                            # Try proxy fallback as last resort
                            try:
                                info_dict = try_with_proxy_fallback(ytdl_opts, url, user_id, extract_info_with_error_tracking)
                            except:
                                pass
                            if info_dict is None:
                                raise Exception("Failed to extract video information with all available proxies and impersonate versions")
                    else:
                        # Not a Cloudflare error, try proxy fallback
                        logger.info(f"Non-Cloudflare error detected for {url}, trying proxy fallback")
                        try:
                            info_dict = try_with_proxy_fallback(ytdl_opts, url, user_id, extract_info_with_error_tracking)
                        except Exception as e3:
                            logger.error(f"Proxy fallback failed: {e3}")
                            info_dict = None
                        if info_dict is None:
                            # Проверяем, является ли это гео-ошибкой YouTube, и пробуем прокси из файла
                            if is_youtube_url(url) and user_id is not None:
                                from COMMANDS.cookies_cmd import is_youtube_geo_error, retry_download_with_proxy
                                if is_youtube_geo_error(original_error_text if original_error_text else error_text):
                                    logger.info(f"YouTube geo-blocked error detected in extract_info for user {user_id}, attempting retry with proxy from file")
                                    
                                    def extract_with_attempt_opts(url_arg, attempt_opts_dict):
                                        # Используем attempt_opts_dict (который включает proxy) вместо оригинальных opts
                                        if 'geo_bypass' not in attempt_opts_dict:
                                            attempt_opts_dict['geo_bypass'] = True
                                        logger.info(f"extract_with_attempt_opts: proxy={attempt_opts_dict.get('proxy', 'None')}, geo_bypass={attempt_opts_dict.get('geo_bypass', 'None')}, cookiefile={'set' if attempt_opts_dict.get('cookiefile') else 'None'}")
                                        return extract_info_operation(attempt_opts_dict)
                                    
                                    retry_result = retry_download_with_proxy(
                                        user_id, url, extract_with_attempt_opts, url, ytdl_opts, error_message=original_error_text if original_error_text else error_text
                                    )
                                    
                                    if retry_result is not None:
                                        logger.info(f"extract_info retry with proxy from file successful for user {user_id}")
                                        info_dict = retry_result
                                    else:
                                        logger.warning(f"extract_info retry with proxy from file failed for user {user_id}")
                            
                            if info_dict is None:
                                # Сохраняем оригинальный текст ошибки для последующей обработки
                                raise Exception(f"Failed to extract video information: {original_error_text if original_error_text else error_text}")
                
                if info_dict is None:
                    raise Exception("Failed to extract video information with all available proxies")
                # Normalize info_dict to a dict
                if isinstance(info_dict, list):
                    info_dict = (info_dict[0] if len(info_dict) > 0 else {})
                if isinstance(info_dict, dict) and "entries" in info_dict:
                    entries = info_dict["entries"]
                    if not entries:
                        raise Exception(f"No videos found in playlist at index {current_index}")
                    # Для диапазона отрицательных индексов обрабатываем все элементы
                    if use_range_download and len(entries) > 1:
                        # Обрабатываем все элементы из диапазона
                        # entries уже содержит все элементы из диапазона
                        # Обрабатываем их в цикле ниже
                        pass  # Будем обрабатывать в основном цикле
                    elif len(entries) > 1:  # If the video in the playlist is more than one
                        if current_index and current_index < len(entries):
                            info_dict = entries[current_index]
                        else:
                            raise Exception(f"Video index {current_index} out of range (total {len(entries)})")
                    else:
                        # If there is only one video in the playlist, just download it
                        info_dict = entries[0]  # Just take the first video

                # Check if this is a live stream and handle it if detection is disabled
                if info_dict and isinstance(info_dict, dict) and info_dict.get('is_live', False):
                    if not LimitsConfig.ENABLE_LIVE_STREAM_BLOCKING:
                        logger.info(f"Live stream detected but detection is disabled, using live stream downloader for user {user_id}: {url}")
                        from DOWN_AND_UP.live_stream_downloader import download_live_stream_chunked
                        result = download_live_stream_chunked(
                            app, message, url, user_id, user_dir_name, info_dict,
                            proc_msg_id, current_total_process, tags_text,
                            cookies_already_checked, use_proxy,
                            format_override=format_override, quality_key=quality_key
                        )
                        if result:
                            return info_dict
                        else:
                            logger.error("Live stream download failed")
                            return None

                # Detect HLS not only by URL/top-level protocol, but by requested formats too
                requested_formats = []
                try:
                    requested_formats = info_dict.get('requested_formats') or []
                except Exception:
                    requested_formats = []

                hls_in_requested = False
                for _rf in requested_formats:
                    proto = (_rf.get('protocol') or '').lower()
                    if 'm3u8' in proto or 'hls' in proto:
                        hls_in_requested = True
                        break

                if ("m3u8" in url.lower()) or (info_dict and info_dict.get("protocol") in ("m3u8", "m3u8_native")) or hls_in_requested:
                    is_hls = True
                    # Force ffmpeg for HLS and disable chunked HTTP to avoid Conflicting range on fragments
                    ytdl_opts["downloader"] = "ffmpeg"
                    ytdl_opts["hls_prefer_native"] = False
                    ytdl_opts["hls_use_mpegts"] = True
                    ytdl_opts.pop("http_chunk_size", None)
                    # Reduce parallelism for fragile HLS endpoints
                    ytdl_opts["concurrent_fragment_downloads"] = 1
                    
                    # Если используется прокси - добавляем параметры для быстрого прерывания при ошибках 403
                    # чтобы не ждать 20 минут в бесконечном цикле повторов
                    if ytdl_opts.get('proxy'):
                        logger.info("HLS stream with proxy detected - adding fast-fail options to prevent infinite 403 retries")
                        ytdl_opts["fragment_retries"] = 0  # Не повторять при ошибке фрагмента
                        ytdl_opts["hls_fragment_retries"] = 0  # Не повторять HLS-сегменты
                        ytdl_opts["abort_on_unavailable_fragment"] = True  # Прервать при недоступном сегменте
                        ytdl_opts["max_fragments"] = 1  # Максимум 1 сегмент для теста (если ошибка - сразу прервать)
                        logger.info("Fast-fail options applied: fragment_retries=0, hls_fragment_retries=0, abort_on_unavailable_fragment=True, max_fragments=1")
                try:
                    if is_hls:
                        safe_edit_message_text(user_id, proc_msg_id,
                            f"{current_total_process}\n<i>Detected HLS stream.\n{safe_get_messages(user_id).ALWAYS_ASK_DOWNLOADING_HLS_MSG}</i>")
                    else:
                        safe_edit_message_text(user_id, proc_msg_id,
                            f"{current_total_process}\n> <i>{safe_get_messages(user_id).ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG} {ytdl_opts.get('format', 'default')}...</i>")
                except Exception as e:
                    logger.error(f"Status update error: {e}")
                    # Check if error is related to quality_key
                    if "'quality_key'" in str(e):
                        _handle_quality_key_error(e, split_msg_ids, is_playlist, successful_uploads, indices_to_download, video_count, user_id, proc_msg_id, message, app)
                
                logger.info("Starting download phase...")
                # Initialize cycle_stop and cycle_thread for HLS at outer level to ensure cleanup on any error
                cycle_stop = None
                cycle_thread = None
                if is_hls:
                    cycle_stop = threading.Event()
                    progress_data = {'downloaded_bytes': 0, 'total_bytes': 0}
                    cycle_thread = start_cycle_progress(user_id, proc_msg_id, current_total_process, user_dir_name, cycle_stop, progress_data)
                    # Pass cycle_stop and progress_data to progress_func so it can update the cycle animation
                    progress_func.cycle_stop = cycle_stop
                    progress_func.progress_data = progress_data
                
                # Try with proxy fallback if user proxy is enabled
                try:
                    def download_operation(opts):
                        messages = safe_get_messages(user_id)
                        
                        with yt_dlp.YoutubeDL(opts) as ydl:
                            if is_hls:
                                try:
                                    ydl.download([url])
                                except yt_dlp.utils.DownloadError as e:
                                    # Re-raise all errors
                                    raise
                            else:
                                ydl.download([url])
                            return True
                    
                    from HELPERS.proxy_helper import try_with_proxy_fallback
                    result = try_with_proxy_fallback(ytdl_opts, url, user_id, download_operation)
                    if result is None:
                        raise Exception("Failed to download video with all available proxies")
                finally:
                    # Always stop cycle animation, even if error occurred
                    if cycle_stop is not None:
                        cycle_stop.set()
                    if cycle_thread is not None:
                        cycle_thread.join(timeout=1)
                try:
                    safe_edit_message_text(user_id, proc_msg_id, safe_get_messages(user_id).VIDEO_DOWNLOAD_COMPLETE_MSG.format(process=current_total_process, bar=full_bar))
                except Exception as e:
                    logger.error(f"Final progress update error: {e}")
                
                logger.info("Download completed successfully")
                
                # NOTE: Do NOT clear Always Ask menu states here!
                # They are needed for MKV postprocessing (embedding audio tracks and subtitles)
                # States will be cleared AFTER postprocessing is complete
                
                # Cache successful cookie result for future use
                if not is_youtube_url(url):
                    from COMMANDS.cookies_cmd import set_cookie_cache_result
                    cookie_file_path = ytdl_opts.get('cookiefile')
                    if cookie_file_path and os.path.exists(cookie_file_path):
                        set_cookie_cache_result(user_id, url, True, cookie_file_path)
                        logger.info(f"Cached successful cookie result for {url}")
                
                # Remove protection file after successful download
                from HELPERS.filesystem_hlp import remove_protection_file
                remove_protection_file(user_dir_name)
                
                return info_dict
            except yt_dlp.utils.DownloadError as e:
                # Ensure cycle animation is stopped on error
                if 'cycle_stop' in locals() and cycle_stop is not None:
                    cycle_stop.set()
                if 'cycle_thread' in locals() and cycle_thread is not None:
                    cycle_thread.join(timeout=1)
                
                error_message = str(e)
                logger.error(f"DownloadError: {error_message}")
                
                # Special handling for HLS streams: check if file was actually created despite the error
                hls_file_found = False
                if is_hls and "No such file or directory" in error_message and (".part" in error_message or ".mp4" in error_message):
                    logger.info(f"[HLS] DownloadError reported missing file, checking if actual file exists...")
                    video_id = info_dict.get('id') if info_dict else ''
                    if video_id:
                        # Check for files with video ID and HLS extensions
                        try:
                            allfiles = os.listdir(user_dir_name)
                            hls_files = [f for f in allfiles if f.startswith(video_id) and f.endswith(('.mpegts', '.ts', '.mp4'))]
                            if hls_files:
                                logger.info(f"[HLS] Found file(s) despite DownloadError: {hls_files}")
                                # File exists, so download actually succeeded - continue processing
                                # We'll find it in the file search logic below
                                logger.info(f"[HLS] Ignoring DownloadError - file exists, continuing...")
                                # Return info_dict to continue processing (file will be found later)
                                logger.info(f"[HLS] Returning info_dict to continue processing...")
                                return info_dict
                        except Exception as check_e:
                            logger.error(f"[HLS] Error checking for existing file: {check_e}")
                
                # Check for live stream detection (only if detection is enabled)
                if "LIVE_STREAM_DETECTED" in error_message:
                    if LimitsConfig.ENABLE_LIVE_STREAM_BLOCKING:
                        live_stream_message = (
                            safe_get_messages(user_id).LIVE_STREAM_DETECTED_MSG +
                            "• You can see the final video length\n\n"
                            "Once the stream is completed, you'll be able to download it as a regular video."
                        )
                        send_error_to_user(message, live_stream_message)
                        return "LIVE_STREAM"
                    # If detection is disabled, continue with live stream download
                    # This will be handled by the live stream download function
                
                # Check for postprocessing errors (including conversion failures for m3u8 streams)
                if "Postprocessing" in error_message:
                    # Check for thumbnail-related postprocessor errors (non-critical, don't stop download)
                    error_lower = error_message.lower()
                    thumbnail_errors = [
                        "embedthumbnail",
                        "embed_thumbnail", 
                        "writethumbnail",
                        "write_thumbnail",
                        "thumbnail",
                        "cover",
                        "artwork"
                    ]
                    
                    # If error is related to thumbnail postprocessing, log and continue
                    if any(thumb_error in error_lower for thumb_error in thumbnail_errors):
                        logger.warning(f"Thumbnail postprocessor error (non-critical, continuing): {error_message}")
                        # Check if file was actually downloaded (info_dict exists)
                        if info_dict:
                            logger.info("Video file downloaded successfully, continuing despite thumbnail error")
                            return info_dict
                        # If no info_dict, check if file exists on disk anyway
                        # Postprocessors run after download, so file should exist even if info_dict is missing
                        try:
                            # Try to find downloaded file in user directory
                            if os.path.exists(user_dir_name):
                                files = os.listdir(user_dir_name)
                                # Look for video files (common extensions)
                                video_files = [f for f in files if f.endswith(('.mp4', '.mkv', '.webm', '.avi', '.mov', '.flv', '.m4v', '.ts', '.mpegts'))]
                                if video_files:
                                    logger.info(f"Found video file(s) despite thumbnail error: {video_files[0]}, continuing")
                                    # Return None to let the code find the file later
                                    return None
                        except Exception as check_e:
                            logger.debug(f"Error checking for files: {check_e}")
                        # If we can't verify file exists, log warning but don't stop - let normal error handling proceed
                        logger.warning("Thumbnail error detected but cannot verify file existence - letting normal error handling proceed")
                        # Don't return here - let it fall through to normal error handling
                    
                    # Check for conversion failed errors (common with m3u8 streams)
                    if "Conversion failed" in error_message:
                        postprocessing_message = (
                            safe_get_messages(user_id).FILE_PROCESSING_ERROR_INVALID_CHARS_MSG +
                            "**Possible causes:**\n"
                            "• Video format conversion failed (common with HLS/m3u8 streams)\n"
                            "• Corrupted or incomplete download\n"
                            "• Unsupported codec or format\n"
                            "• Insufficient system resources\n\n"
                            "**Solutions:**\n"
                            "• Try downloading again - the system will retry automatically\n"
                            "• Try a different quality or format\n"
                            "• Check if you have enough disk space\n"
                            "• If the problem persists, the stream may be unstable or incompatible\n"
                        )
                        send_error_to_user(message, postprocessing_message)
                        logger.error(f"Postprocessing conversion error: {error_message}")
                        return "POSTPROCESSING_ERROR"
                    elif "Error opening output files" in error_message:
                        postprocessing_message = (
                            safe_get_messages(user_id).FILE_PROCESSING_ERROR_INVALID_CHARS_MSG +
                            "**Solutions:**\n"
                            "• Try downloading again - the system will use a safer filename\n"
                            "• If the problem persists, the video title may contain unsupported characters\n"
                            "• Consider using a different video source if available\n\n"
                            "The download will be retried automatically with a cleaned filename."
                        )
                        send_error_to_user(message, postprocessing_message)
                        logger.error(f"Postprocessing error: {error_message}")
                        return "POSTPROCESSING_ERROR"
                
                # Check for postprocessing errors with Invalid data (non-video files like PDF)
                if "Postprocessing" in error_message and "Invalid data found when processing input" in error_message:
                    logger.error(f"Postprocessing error (Invalid data - non-video file): {error_message}")
                    # Check if downloaded file is actually a video file
                    try:
                        if os.path.exists(user_dir_name):
                            files = os.listdir(user_dir_name)
                            # Check for non-video files
                            non_video_extensions = ('.pdf', '.doc', '.docx', '.txt', '.zip', '.rar', '.7z', '.unknown')
                            non_video_files = [f for f in files if any(f.lower().endswith(ext) for ext in non_video_extensions)]
                            if non_video_files:
                                messages = safe_get_messages(user_id)
                                postprocessing_message = (
                                    messages.FILE_PROCESSING_ERROR_INVALID_CHARS_MSG +
                                    messages.FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG
                                )
                                send_error_to_user(message, postprocessing_message)
                                logger.error(f"Non-video file detected: {non_video_files}")
                                return "POSTPROCESSING_ERROR"
                    except Exception as check_e:
                        logger.debug(f"Error checking file type: {check_e}")
                    # If we can't determine file type, still return error
                    messages = safe_get_messages(user_id)
                    postprocessing_message = (
                        messages.FILE_PROCESSING_ERROR_INVALID_CHARS_MSG +
                        messages.FILE_PROCESSING_ERROR_INVALID_DATA_MSG
                    )
                    send_error_to_user(message, postprocessing_message)
                    return "POSTPROCESSING_ERROR"
                
                # Check for postprocessing errors with Invalid argument
                if "Postprocessing" in error_message and "Invalid argument" in error_message:
                    logger.error(f"Postprocessing error (Invalid argument): {error_message}")
                    return "POSTPROCESSING_ERROR"
                
                # Check for postprocessing errors with .meta file (non-critical, can be ignored)
                if "Postprocessing" in error_message and ".meta" in error_message and "No such file or directory" in error_message:
                    logger.warning(f"Postprocessing .meta file error (non-critical, continuing): {error_message}")
                    # This is a non-critical error, try to continue by returning info_dict if available
                    if info_dict:
                        logger.info("Continuing despite .meta file error")
                        return info_dict
                    return "POSTPROCESSING_ERROR"
                
                # Check for postprocessing map error (can be ignored)
                if "Postprocessing" in error_message and "add a trailing '?' to the map" in error_message:
                    logger.warning(f"Postprocessing map error (non-critical, continuing): {error_message}")
                    # This is a non-critical error, try to continue by returning info_dict if available
                    if info_dict:
                        logger.info("Continuing despite postprocessing map error")
                        return info_dict
                    return "POSTPROCESSING_ERROR"
                
                # Check for HTTP Error 416 (Requested range not satisfiable) - retry without range requests
                if "HTTP Error 416" in error_message or "Requested range not satisfiable" in error_message:
                    logger.warning(f"HTTP 416 error detected (range request issue): {error_message}")
                    # Try to continue if file was partially downloaded
                    if info_dict:
                        logger.info("Attempting to continue despite HTTP 416 error")
                        return info_dict
                    # If retry is needed, return error to trigger retry
                    logger.error(f"HTTP 416 error - download failed: {error_message}")
                    return None
                
                # Check for Read timed out errors - retry with longer timeout
                if "Read timed out" in error_message or "ReadTimeout" in error_message or "timed out" in error_message.lower():
                    logger.warning(f"Read timeout error detected: {error_message}")
                    # Try to continue if file was partially downloaded
                    if info_dict:
                        logger.info("Attempting to continue despite timeout error")
                        return info_dict
                    # Return None to trigger retry
                    logger.error(f"Read timeout error - download failed: {error_message}")
                    return None
                
                # Check for format not available error
                if "Requested format is not available" in error_message:
                    logger.error(f"Format not available error: {error_message}")
                    return "FORMAT_NOT_AVAILABLE"
                
                # Check for --live-from-start error and retry with --no-live-from-start
                if "--live-from-start is passed, but there are no formats that can be downloaded from the start" in error_message and not did_live_from_start_retry:
                    logger.info(f"Live-from-start error detected for user {user_id}, retrying with --no-live-from-start")
                    did_live_from_start_retry = True
                    # Retry the download with live_from_start disabled
                    retry_result = try_download(url, attempt_opts)
                    if retry_result is not None:
                        logger.info(f"Download retry with --no-live-from-start successful for user {user_id}")
                        return retry_result
                    else:
                        logger.warning(f"Download retry with --no-live-from-start failed for user {user_id}")
                        # Continue with normal error handling below
                
                
                # Auto-fallback to gallery-dl (/img) for all supported errors
                if should_fallback_to_gallery_dl(error_message, url):
                    try:
                        from COMMANDS.image_cmd import image_command
                        from HELPERS.safe_messeger import fake_message
                    except Exception as imp_e:
                        logger.error(f"Failed to import gallery-dl fallback handlers: {imp_e}")
                    else:
                        try:
                            safe_edit_message_text(user_id, proc_msg_id,
                                f"{current_total_process}\n🔄 yt-dlp failed, trying gallery-dl…")
                        except Exception:
                            pass
                        try:
                            # Check if content is NSFW for fallback
                            from HELPERS.porn import is_porn
                            is_nsfw = is_porn(url, "", "", None) or user_forced_nsfw
                            logger.info(f"[FALLBACK] is_porn check for {url}: {is_porn(url, '', '', None)}, user_forced_nsfw: {user_forced_nsfw}, final is_nsfw: {is_nsfw}")
                            
                            # ЖЕСТКО: Используем сохраненный оригинальный текст с диапазоном
                            logger.info(f"[FALLBACK DEBUG] Using saved original_message_text: {original_message_text}")
                            
                            # Ищем URL с диапазоном *start*end
                            import re
                            range_url_match = re.search(r'(https?://[^\s\*#]+)\*(\d+)\*(\d+)', original_message_text)
                            if range_url_match:
                                parsed_url = range_url_match.group(1)
                                start_range = int(range_url_match.group(2))
                                end_range = int(range_url_match.group(3))
                                logger.info(f"[FALLBACK DEBUG] FOUND RANGE: {parsed_url} with range {start_range}-{end_range}")
                            else:
                                # Fallback к обычному URL
                                m = re.search(r'https?://[^\s\*#]+', original_message_text)
                                parsed_url = m.group(0) if m else original_message_text
                                start_range = 1
                                end_range = 1
                                logger.info(f"[FALLBACK DEBUG] NO RANGE FOUND, using url: {parsed_url}")
                            
                            # Build fallback command for single item only (not entire range)
                            # Use current_index instead of full range to download only the failed item
                            current_item_index = current_index + 1  # current_index is 0-based, we need 1-based
                            fallback_text = f"/img {current_item_index}-{current_item_index} {parsed_url}"
                            logger.info(f"[FALLBACK] Downloading only failed item {current_item_index} via gallery-dl, fallback_text: {fallback_text}")
                            
                            if tags_text:
                                fallback_text += f" {tags_text}"
                            
                            # Add NSFW tag if content is detected as NSFW
                            if is_nsfw and "#nsfw" not in fallback_text.lower():
                                fallback_text += " #nsfw"
                                logger.info(f"[FALLBACK] Added #nsfw tag for NSFW content: {url}")
                            
                            # For groups, preserve original chat_id and message_thread_id
                            original_chat_id = message.chat.id if hasattr(message, 'chat') else user_id
                            message_thread_id = getattr(message, 'message_thread_id', None) if hasattr(message, 'message_thread_id') else None
                            image_command(app, fake_message(fallback_text, user_id, original_chat_id=original_chat_id, message_thread_id=message_thread_id, original_message=message))
                            logger.info(f"Triggered gallery-dl fallback via /img, is_nsfw={is_nsfw}, range={start_range}-{end_range}")
                            return "IMG"
                        except Exception as call_e:
                            logger.error(f"Failed to trigger gallery-dl fallback: {call_e}")
                
                # YouTube‑специфичные ошибки: сначала пробуем перебор кук, затем гео‑прокси
                if is_youtube_url(url):
                    # 1) Ошибки авторизации/куков (в т.ч. "Sign in to confirm you’re not a bot")
                    if is_youtube_cookie_error(error_message):
                        logger.info(f"YouTube cookie-related error detected for user {user_id}, attempting retry with different cookies")
                        try:
                            retry_result = retry_download_with_different_cookies(
                                user_id, url, try_download, url, attempt_opts
                            )
                        except Exception as cookie_retry_error:
                            logger.error(f"YouTube cookie retry failed with unexpected error for user {user_id}: {cookie_retry_error}")
                            retry_result = None
                        
                        if retry_result is not None:
                            logger.info(f"Download retry with different cookies successful for user {user_id}")
                            return retry_result
                        else:
                            logger.warning(f"All YouTube cookie retry attempts failed for user {user_id}")
                    
                    # 2) Гео‑ошибки (region blocked и т.п.) — пробуем через прокси из файла
                    # Не прерываем скачивание сразу, а пробуем все подходящие прокси
                    logger.info(f"Checking geo-error: is_youtube_geo_error={is_youtube_geo_error(error_message)}, did_proxy_retry={did_proxy_retry}, error_message[:200]={error_message[:200]}")
                    if is_youtube_geo_error(error_message) and not did_proxy_retry:
                        logger.info(f"YouTube geo-blocked error detected for user {user_id}, attempting retry with proxy from file")
                        logger.info(f"Full error message: {error_message}")
                        
                        # Пробуем скачать через прокси (только подходящие по описанию ошибки)
                        retry_result = retry_download_with_proxy(
                            user_id, url, try_download, url, attempt_opts, error_message=error_message
                        )
                        
                        if retry_result is not None:
                            logger.info(f"Download retry with proxy successful for user {user_id}")
                            did_proxy_retry = True
                            return retry_result
                        else:
                            # Все подходящие прокси не помогли - продолжаем обработку ошибки
                            logger.warning(f"All matching proxies from file failed for user {user_id}, will show error to user")
                            did_proxy_retry = True
                            # Не возвращаемся здесь - продолжаем обработку ошибки ниже
                else:
                    # Для не-YouTube сайтов пробуем перебор куки
                    logger.info(f"Non-YouTube download error detected for user {user_id}, attempting cookie fallback")
                    
                    # Проверяем, связана ли ошибка с куки
                    error_str = error_message.lower()
                    if any(keyword in error_str for keyword in ['cookie', 'auth', 'login', 'sign in', '403', '401', 'forbidden', 'unauthorized']):
                        logger.info(f"Error appears to be cookie-related for {url}, trying cookie fallback")
                        
                        # Пробуем перебор куки с новой системой
                        from COMMANDS.cookies_cmd import try_non_youtube_cookie_fallback
                        retry_result = try_non_youtube_cookie_fallback(
                            user_id, url, try_download, url, attempt_opts
                        )
                        
                        if retry_result is not None:
                            logger.info(f"Download retry with cookie fallback successful for user {user_id}")
                            return retry_result
                        else:
                            logger.warning(f"Download retry with cookie fallback failed for user {user_id}")
                    else:
                        logger.info(f"Error appears to be non-cookie-related for {url}, skipping cookie fallback")
                
                # Check if this is a skippable video error (private error for specific video in playlist)
                # This check should be done before sending error message to avoid stopping entire playlist
                if is_playlist and is_skippable_video_error(error_message):
                    logger.info(f"Skipping video at index {current_index} due to skippable error: {error_message[:100]}")
                    # Send a brief notification to user about skipping this video
                    skip_message = f"⏭️ Пропущено видео #{current_index + 1}: {error_message[:150]}"
                    send_to_user(message, skip_message)
                    return "SKIP"  # Skip this video and continue with next
                
                # Send full error message with instructions immediately (only once)
                if not error_message_sent:
                    # Extract error code and description from yt-dlp error
                    error_code = "UNKNOWN_ERROR"
                    error_description = error_message
                    
                    # Try to extract specific error codes
                    if "HTTP Error 403" in error_message:
                        error_code = "HTTP_403_FORBIDDEN"
                        error_description = "Access forbidden - may need cookies or authentication"
                    elif "HTTP Error 401" in error_message:
                        error_code = "HTTP_401_UNAUTHORIZED"
                        error_description = "Authentication required - cookies needed"
                    elif "Video unavailable" in error_message:
                        error_code = "VIDEO_UNAVAILABLE"
                        error_description = "Video is not available or has been removed"
                    elif "Private video" in error_message:
                        error_code = "PRIVATE_VIDEO"
                        error_description = "Video is private and requires authentication"
                    elif "Sign in to confirm" in error_message:
                        error_code = "SIGN_IN_REQUIRED"
                        error_description = "Sign in required - cookies needed"
                        # Автоматический rotate IP при SIGN_IN_REQUIRED
                        try:
                            from services.system_service import rotate_ip
                            logger.warning(f"Auto-rotating IP due to SIGN_IN_REQUIRED error for user {user_id}")
                            rotate_result = rotate_ip()
                            if rotate_result.get("status") == "ok":
                                logger.info(f"IP rotated successfully: IPv4={rotate_result.get('ipv4')}, IPv6={rotate_result.get('ipv6')}")
                            else:
                                logger.error(f"Failed to auto-rotate IP: {rotate_result.get('message')}")
                        except Exception as rotate_error:
                            logger.error(f"Error during auto-rotate IP: {rotate_error}")
                    elif "No video formats found" in error_message:
                        error_code = "NO_FORMATS"
                        error_description = "No downloadable formats available"
                    elif "Unsupported URL" in error_message:
                        error_code = "UNSUPPORTED_URL"
                        error_description = "This URL is not supported by yt-dlp"
                    elif "Network error" in error_message:
                        error_code = "NETWORK_ERROR"
                        error_description = "Network connection failed"
                    elif "ffmpeg exited with code" in error_message or "ERROR: ffmpeg" in error_message:
                        error_code = "FFMPEG_ERROR"
                        # Try to extract more details from error message
                        if "code 1" in error_message:
                            error_description = "FFmpeg processing failed - video format may be incompatible or corrupted"
                        elif "code 2" in error_message:
                            error_description = "FFmpeg error - invalid arguments or unsupported format"
                        else:
                            error_description = "FFmpeg processing error occurred"
                        
                        # Try to extract specific error details
                        import re
                        ffmpeg_details = re.search(r'ffmpeg.*?error[:\s]+(.*?)(?:\n|$)', error_message, re.IGNORECASE | re.DOTALL)
                        if ffmpeg_details:
                            details = ffmpeg_details.group(1).strip()[:200]
                            if details:
                                error_description += f"\n\nDetails: {details}"
                        
                        # Suggest solutions
                        error_description += (
                            "\n\n**Possible solutions:**\n"
                            "• Try downloading with a different quality/format\n"
                            "• The video may be corrupted or in an unsupported format\n"
                            "• Try downloading without post-processing\n"
                            "• Check if ffmpeg is properly installed"
                        )
                    
                    send_error_to_user(
                        message,                   
                        f"<blockquote>{safe_get_messages(user_id).ERROR_CHECK_SUPPORTED_SITES_MSG}</blockquote>\n"
                        f"<blockquote>{safe_get_messages(user_id).ERROR_COOKIE_NEEDED_MSG}</blockquote>\n"
                        f"<blockquote>{safe_get_messages(user_id).ERROR_COOKIE_INSTRUCTIONS_MSG}</blockquote>\n"
                        f"────────────────\n"
                        f"❌ <b>Error Code:</b> <code>{error_code}</code>\n"
                        f"📝 <b>Description:</b> {error_description}\n"
                        f"🔧 <b>Full Error:</b> <code>{error_message}</code>"
                    )
                    error_message_sent = True
                return None
            except Exception as e:
                error_message = str(e)
                logger.error(f"Attempt with format {ytdl_opts.get('format', 'default')} failed: {e}")
                logger.debug(f"Error message for geo-check: {error_message[:500]}")
                # Auto-fallback to gallery-dl for obvious non-video cases
                emsg = str(e)
                if (
                    "No videos found in playlist" in emsg
                    or "Unsupported URL" in emsg
                ):
                    try:
                        from COMMANDS.image_cmd import image_command
                        from HELPERS.safe_messeger import fake_message
                    except Exception as imp_e:
                        logger.error(f"Failed to import gallery-dl fallback handlers (generic): {imp_e}")
                    else:
                        try:
                            safe_edit_message_text(user_id, proc_msg_id,
                                f"{current_total_process}\n🔄 yt-dlp failed, trying gallery-dl…")
                        except Exception:
                            pass
                        try:
                            # Check if content is NSFW for fallback
                            from HELPERS.porn import is_porn
                            is_nsfw = is_porn(url, "", "", None) or user_forced_nsfw
                            logger.info(f"[FALLBACK] is_porn check for {url}: {is_porn(url, '', '', None)}, user_forced_nsfw: {user_forced_nsfw}, final is_nsfw: {is_nsfw}")
                            
                            # ЖЕСТКО: Используем сохраненный оригинальный текст с диапазоном
                            logger.info(f"[FALLBACK DEBUG] Using saved original_message_text: {original_message_text}")
                            
                            # Ищем URL с диапазоном *start*end
                            import re
                            range_url_match = re.search(r'(https?://[^\s\*#]+)\*(\d+)\*(\d+)', original_message_text)
                            if range_url_match:
                                parsed_url = range_url_match.group(1)
                                start_range = int(range_url_match.group(2))
                                end_range = int(range_url_match.group(3))
                                logger.info(f"[FALLBACK DEBUG] FOUND RANGE: {parsed_url} with range {start_range}-{end_range}")
                            else:
                                # Fallback к обычному URL
                                m = re.search(r'https?://[^\s\*#]+', original_message_text)
                                parsed_url = m.group(0) if m else original_message_text
                                start_range = 1
                                end_range = 1
                                logger.info(f"[FALLBACK DEBUG] NO RANGE FOUND, using url: {parsed_url}")
                            
                            # Build fallback command for single item only (not entire range)
                            # Use current_index instead of full range to download only the failed item
                            current_item_index = current_index + 1  # current_index is 0-based, we need 1-based
                            fallback_text = f"/img {current_item_index}-{current_item_index} {parsed_url}"
                            logger.info(f"[FALLBACK] Downloading only failed item {current_item_index} via gallery-dl, fallback_text: {fallback_text}")
                            
                            if tags_text:
                                fallback_text += f" {tags_text}"
                            
                            # Add NSFW tag if content is detected as NSFW
                            if is_nsfw and "#nsfw" not in fallback_text.lower():
                                fallback_text += " #nsfw"
                                logger.info(f"[FALLBACK] Added #nsfw tag for NSFW content: {url}")
                            
                            # For groups, preserve original chat_id and message_thread_id
                            original_chat_id = message.chat.id if hasattr(message, 'chat') else user_id
                            message_thread_id = getattr(message, 'message_thread_id', None) if hasattr(message, 'message_thread_id') else None
                            image_command(app, fake_message(fallback_text, user_id, original_chat_id=original_chat_id, message_thread_id=message_thread_id, original_message=message))
                            logger.info(f"Triggered gallery-dl fallback via /img (generic), is_nsfw={is_nsfw}, range={start_range}-{end_range}")
                            return "IMG"
                        except Exception as call_e:
                            logger.error(f"Failed to trigger gallery-dl fallback (generic): {call_e}")
				
                # Check if this is a "No videos found in playlist" error
                if "No videos found in playlist" in str(e):
                    error_message = safe_get_messages(user_id).DOWN_UP_NO_VIDEOS_PLAYLIST_MSG.format(index=current_index + 1)
                    send_error_to_user(message, error_message)
                    logger.info(f"Stopping download: playlist item at index {current_index} (no video found)")
                    return "STOP"  # New special value for full stop
                
                # Check if this is a TikTok infinite loop error
                if "TikTok API keeps sending the same page" in str(e) and "infinite loop" in str(e):
                    error_message = safe_get_messages(user_id).VIDEO_TIKTOK_API_ERROR_SKIP_MSG.format(index=current_index + 1)
                    send_to_user(message, error_message)
                    logger.info(f"Skipping TikTok video at index {current_index} due to API error")
                    return "SKIP"  # Skip this video and continue with next

                # If HLS file was found, don't return error - continue processing
                if hls_file_found:
                    logger.info(f"[HLS] File found despite DownloadError, continuing processing...")
                    # Don't return None - let the code continue to process the file
                    # The file will be found in the file search logic below
                else:
                    # Отправляем сообщение об ошибке только один раз, чтобы избежать спама
                    if not error_message_sent:
                        send_to_user(message, safe_get_messages(user_id).UNKNOWN_ERROR_MSG.format(error=e))
                        error_message_sent = True
                    return None

        # Для отрицательных индексов используем весь диапазон сразу, а не цикл
        # use_range_download уже объявлена выше (строка 325)
        total_playlist_count = None  # Общее количество видео в плейлисте (для преобразования отрицательных индексов)
        playlist_range_str = None  # Строка диапазона для плейлиста (например, "1:7" или "1:7:-1")
        has_negative_indices_for_download = False  # Флаг для отрицательных индексов (не используем range_entries_metadata)
        if is_playlist and video_start_with is not None and video_end_with is not None:
            if video_start_with < 0 or video_end_with < 0:
                use_range_download = True
                has_negative_indices_for_download = True  # Для отрицательных индексов скачиваем каждый отдельно
                # Для отрицательных индексов playlist_range_str не используется, так как обрабатываем каждый индекс отдельно
                # Для отрицательных индексов нужно получить общее количество видео из плейлиста
                # Делаем предварительный запрос, чтобы получить общее количество видео
                try:
                    from DOWN_AND_UP.yt_dlp_hook import get_video_formats
                    logger.info(f"Getting total playlist count for negative indices conversion...")
                    temp_info = get_video_formats(url, user_id, 1, cookies_already_checked, use_proxy, 1)
                    if temp_info and isinstance(temp_info, dict):
                        if "entries" in temp_info:
                            total_playlist_count = len(temp_info["entries"])
                        elif "_playlist_entries" in temp_info:
                            total_playlist_count = len(temp_info["_playlist_entries"])
                    if total_playlist_count:
                        logger.info(f"Total playlist count: {total_playlist_count}")
                        # Преобразуем отрицательные индексы в положительные
                        # -1 = последнее видео (total_playlist_count), -2 = предпоследнее (total_playlist_count - 1), и т.д.
                        # Формула: positive_index = total_playlist_count + negative_index + 1
                        converted_indices = []
                        for neg_idx in playlist_indices_all:
                            if neg_idx < 0:
                                pos_idx = total_playlist_count + neg_idx + 1
                                converted_indices.append(pos_idx)
                            else:
                                converted_indices.append(neg_idx)
                        # Сортируем в обратном порядке для скачивания от последнего к первому
                        converted_indices.sort(reverse=True)
                        playlist_indices_all = converted_indices
                        logger.info(f"Converted negative indices to positive: {converted_indices}")
                except Exception as e:
                    logger.warning(f"Failed to get total playlist count for negative indices: {e}, using original indices")
            elif video_start_with != video_end_with:
                # Формируем строку диапазона для обычных случаев
                if is_reverse_order:
                    playlist_range_str = f"{video_start_with}:{video_end_with}:-1"
                else:
                    playlist_range_str = f"{video_start_with}:{video_end_with}"
        
        if use_range_download:
            # Для отрицательных индексов используем весь диапазон сразу
            # Теперь indices_to_download содержит уже преобразованные положительные индексы
            # Для отрицательных индексов всегда используем обратный порядок (от последнего к первому)
            # playlist_range_str не используется для отрицательных индексов, так как мы обрабатываем каждый индекс отдельно
            # Обрабатываем каждый индекс из исходного списка в обратном порядке (от последнего к первому)
            indices_to_download = playlist_indices_all  # Уже отсортированы в обратном порядке
        elif is_playlist and safe_quality_key:
            indices_to_download = uncached_indices
        elif is_playlist:
            indices_to_download = playlist_indices_all
        else:
            indices_to_download = range(video_count)
        
        range_entries_metadata = None
        current_playlist_items_override = None
        logger.info(f"🔍 [DEBUG] Starting playlist download: indices_to_download={indices_to_download}, len={len(indices_to_download) if indices_to_download else 0}, use_range_download={use_range_download}, has_negative_indices_for_download={has_negative_indices_for_download}")
        for idx, current_index in enumerate(indices_to_download):
            logger.info(f"🔍 [DEBUG] Processing video {idx + 1}/{len(indices_to_download)}: current_index={current_index}")
            messages = safe_get_messages(message.chat.id)
            total_process = f"""
<b>📶 {safe_get_messages(user_id).TOTAL_PROGRESS_MSG}</b>
<blockquote>{safe_get_messages(user_id).VIDEO_PROGRESS_MSG.format(current=idx + 1, total=len(indices_to_download))}</blockquote>
"""
            current_total_process = total_process

            # Determine rename_name based on the incoming playlist_name:
            if playlist_name and playlist_name.strip():
                # A new name for the playlist is explicitly set - let's use it
                rename_name = sanitize_filename_strict(f"{playlist_name.strip()} - Part {idx + 1}")
            else:
                # No new name set - extract name from metadata
                rename_name = None

            # Reset retry flags for each new item in playlist
            did_cookie_retry = False
            did_proxy_retry = False
            did_live_from_start_retry = False
            error_message_sent = False  # Reset error message flag for each playlist item

            info_dict = None
            skip_item = False
            stop_all = False
            
            # Define safe filename template for fallback
            timestamp = int(time.time())
            safe_outtmpl = os.path.join(user_dir_name, f"download_{timestamp}.%(ext)s")
            
            # Для отрицательных индексов не используем reuse_range_download, скачиваем каждый индекс отдельно
            reuse_range_download = use_range_download and range_entries_metadata is not None and not has_negative_indices_for_download
            if reuse_range_download:
                if idx < len(range_entries_metadata):
                    info_dict = range_entries_metadata[idx]
                    logger.info(f"Reusing cached range download entry #{idx + 1} for playlist index {current_index}")
                else:
                    logger.warning(f"Range download already completed but entry #{idx + 1} missing (total {len(range_entries_metadata)}). Stopping playlist.")
                    info_dict = None
                    stop_all = True
            else:
                if use_range_download:
                    # Для отрицательных индексов playlist_range_str = None, поэтому используем None
                    # В try_download будет использован current_index (уже преобразованный в положительный)
                    current_playlist_items_override = playlist_range_str  # Может быть None для отрицательных индексов
                else:
                    current_playlist_items_override = None

                for attempt in attempts:
                    result = try_download(url, attempt)
                    
                    # If download failed and it's a YouTube URL, try automatic cookie retry
                    if result is None and is_youtube_url(url) and not did_cookie_retry:
                        logger.info(f"Video download failed for user {user_id}, attempting automatic cookie retry")
                        
                        # Try retry with different cookies
                        retry_result = retry_download_with_different_cookies(
                            user_id, url, try_download, url, attempt
                        )
                        
                        if retry_result is not None:
                            logger.info(f"Video download retry with different cookies successful for user {user_id}")
                            result = retry_result
                            did_cookie_retry = True
                        else:
                            logger.warning(f"All cookie retry attempts failed for user {user_id}")
                            did_cookie_retry = True
                    if result == "STOP":
                        stop_all = True
                        break
                    elif result == "SKIP":
                        skip_item = True
                        break
                    elif result == "IMG":
                        # Gallery-dl fallback has been triggered for this specific item
                        logger.info(f"Gallery-dl fallback triggered for item {current_index}, continuing with next item")
                        skip_item = True
                        break
                    elif result is not None and isinstance(result, dict):
                        info_dict = result
                        break
                    elif result is not None and isinstance(result, str):
                        # Handle string return values (like "POSTPROCESSING_ERROR")
                        logger.info(f"Download attempt returned string result: {result}")
                        if result == "POSTPROCESSING_ERROR":
                            # Try again with safe filename if this was the first attempt
                            if attempt == attempts[0]:  # First attempt failed
                                logger.info("First attempt failed with postprocessing error, retrying with safe filename")
                                # Modify the attempt to use safe filename
                                safe_attempt = attempt.copy()
                                safe_attempt['outtmpl'] = safe_outtmpl
                                safe_result = try_download(url, safe_attempt)
                                if safe_result is not None and isinstance(safe_result, dict):
                                    info_dict = safe_result
                                    break
                                elif safe_result is not None and isinstance(safe_result, str):
                                    logger.info(f"Safe filename attempt also failed: {safe_result}")
                                    continue
                            else:
                                # Already tried safe filename, skip this attempt
                                continue
                        else:
                            # Other string results, skip this attempt
                            continue

                current_playlist_items_override = None

                # Для отрицательных индексов не используем range_entries_metadata, скачиваем каждый индекс отдельно
                if use_range_download and info_dict is not None and not has_negative_indices_for_download:
                    entries_list = []
                    if isinstance(info_dict, dict) and "entries" in info_dict:
                        entries_list = info_dict.get("entries") or []
                    elif isinstance(info_dict, list):
                        entries_list = info_dict
                    else:
                        entries_list = [info_dict]

                    if not entries_list:
                        logger.warning("Range download completed but yt-dlp returned no entries.")
                        range_entries_metadata = []
                        info_dict = None
                    else:
                        range_entries_metadata = entries_list
                        if idx < len(range_entries_metadata):
                            info_dict = range_entries_metadata[idx]
                        else:
                            logger.warning(f"Range download returned {len(range_entries_metadata)} entries, but requested entry #{idx + 1} is missing.")
                            info_dict = None
                            stop_all = True

            if stop_all:
                logger.info(f"Stopping all downloads due to playlist error at index {current_index}")
                break

            if skip_item:
                logger.info(f"Skipping item at index {current_index} (no video content)")
                continue

            if info_dict is None:
                # Send error message to user only on final failure
                if error_message and not error_message_sent:
                    # Check for specific error types and send appropriate messages
                    if "Postprocessing" in error_message and "Invalid argument" in error_message:
                        postprocessing_message = (
                            safe_get_messages(user_id).FILE_PROCESSING_ERROR_INVALID_ARG_MSG +
                            "**Possible causes:**\n"
                            "• Corrupted or incomplete download\n"
                            "• Unsupported file format or codec\n"
                            "• File system permissions issue\n"
                            "• Insufficient disk space\n\n"
                            "**Solutions:**\n"
                            "• Try downloading again with different settings\n"
                            "• Check if you have enough disk space\n"
                            "• Try a different quality or format\n"
                            "• If the problem persists, the video source may be corrupted"
                        )
                        send_error_to_user(message, postprocessing_message)
                        error_message_sent = True
                    elif "Requested format is not available" in error_message:
                        format_error_message = (
                            safe_get_messages(user_id).FORMAT_NOT_AVAILABLE_MSG +
                            "**Possible causes:**\n"
                            "• The video doesn't have the requested format (e.g., webm, mp4)\n"
                            "• The video quality is not available in the requested format\n"
                            "• The video source has limited format options\n\n"
                            "**Solutions:**\n"
                            "• Try downloading with a different quality setting\n"
                            "• Use the 'Always Ask' menu to see available formats\n"
                            "• Try changing your format preferences in /args settings\n"
                            "• The system will automatically try alternative formats"
                        )
                        send_error_to_user(message, format_error_message)
                        error_message_sent = True
                
                with playlist_errors_lock:
                    error_key = f"{user_id}_{playlist_name}"
                    if error_key not in playlist_errors:
                        playlist_errors[error_key] = True

                break

            successful_uploads += 1

            video_id = info_dict.get("id", None)
            # Get original title for caption (saved before sanitization in match_filter)
            original_video_title = info_dict.get("original_title", info_dict.get("title", None))  # Original title for caption
            full_video_title = info_dict.get("description", original_video_title)
            video_title = info_dict.get("title", "video")  # Already sanitized title for file operations
            video_page_url = (
                info_dict.get("webpage_url")
                or info_dict.get("original_url")
                or info_dict.get("url")
                or info_dict.get("canonical_url")
                or url
            )
            
            # Сохраняем уникальную ссылку видео для последующего кэширования
            if is_playlist:
                playlist_video_urls[current_index] = video_page_url
                logger.info(f"🔍 [CACHE] Сохранена уникальная ссылка для видео index={current_index}: {video_page_url}")

            # --- Use new centralized function for all tags ---
            tags_list = tags_text.split() if tags_text else []
            tags_text_final = generate_final_tags(url, tags_list, info_dict)
            save_user_tags(user_id, tags_text_final.split())

           # If rename_name is not set, set it equal to video_title
            if rename_name is None:
                rename_name = video_title

            dir_path = user_dir_name

            # Save the full name to a file
            full_title_path = os.path.join(dir_path, "full_title.txt")
            try:
                with open(full_title_path, "w", encoding="utf-8") as f:
                    f.write(full_video_title if full_video_title else original_video_title)
            except Exception as e:
                logger.error(f"Error saving full title: {e}")

            info_text = f"""
{total_process}
<b>{safe_get_messages(user_id).DOWN_UP_VIDEO_INFO_MSG}</b>
<blockquote><b>{safe_get_messages(user_id).DOWN_UP_NUMBER_MSG}:</b> {current_index}</blockquote>
<blockquote><b>{safe_get_messages(user_id).DOWN_UP_TITLE_MSG}:</b> {original_video_title}</blockquote>
<blockquote><b>{safe_get_messages(user_id).DOWN_UP_ID_MSG}:</b> {video_id}</blockquote>
"""

            try:
                safe_edit_message_text(user_id, proc_msg_id,
                    f"{info_text}\n{full_bar}   100.0%\n<i>{safe_get_messages(user_id).DOWN_UP_DOWNLOADED_VIDEO_MSG}\n{safe_get_messages(user_id).DOWN_UP_PROCESSING_UPLOAD_MSG}</i>")
            except Exception as e:
                logger.error(f"Status update error after download: {e}")
                # Check if error is related to quality_key
                if "'quality_key'" in str(e):
                    _handle_quality_key_error(e, split_msg_ids, is_playlist, successful_uploads, indices_to_download, video_count, user_id, proc_msg_id, message, app)

            dir_path = user_dir_name
            downloaded_file = None
            downloaded_abs_path = None
            
            # Get user's preferred video format to determine file extensions
            from COMMANDS.args_cmd import get_user_ytdlp_args
            user_args = get_user_ytdlp_args(user_id, url)
            user_video_format = user_args.get('video_format', 'mp4')
            user_merge_format = user_args.get('merge_output_format', 'mp4')
            
            # Determine which format to look for based on user preferences
            # Priority: video_format > merge_output_format > default
            target_format = user_video_format if user_video_format != 'mp4' else user_merge_format
            
            # Define supported video extensions based on user preference
            if target_format == 'mp4':
                video_extensions = ('.mp4', '.m4v')
            elif target_format == 'webm':
                video_extensions = ('.webm',)
            elif target_format == 'mkv':
                video_extensions = ('.mkv',)
            elif target_format == 'avi':
                video_extensions = ('.avi',)
            elif target_format == 'mov':
                video_extensions = ('.mov',)
            elif target_format == 'flv':
                video_extensions = ('.flv',)
            elif target_format == '3gp':
                video_extensions = ('.3gp', '.3g2')
            elif target_format == 'ogv':
                video_extensions = ('.ogv', '.ogg')
            elif target_format == 'wmv':
                video_extensions = ('.wmv',)
            elif target_format == 'asf':
                video_extensions = ('.asf',)
            else:
                # Fallback to all supported formats (including .mpegts for HLS streams)
                video_extensions = ('.mp4', '.mkv', '.webm', '.ts', '.mpegts', '.avi', '.mov', '.flv', '.3gp', '.ogv', '.wmv', '.asf')
            
            # Try to use exact filename from yt-dlp metadata first
            filename_hints = []
            meta_filename = info_dict.get('_filename')
            if meta_filename:
                filename_hints.append(meta_filename)
            filepath_hint = info_dict.get('filepath')
            if filepath_hint:
                filename_hints.append(filepath_hint)
            requested_downloads = info_dict.get('requested_downloads') or []
            for rd in requested_downloads:
                rd_path = rd.get('filepath') or rd.get('_filename')
                if rd_path:
                    filename_hints.append(rd_path)
            
            for hint in filename_hints:
                if hint and os.path.exists(hint):
                    downloaded_abs_path = os.path.abspath(hint)
                    downloaded_file = os.path.basename(downloaded_abs_path)
                    logger.info(f"Using yt-dlp reported file path: {downloaded_abs_path}")
                    break
            
            if not downloaded_file:
                allfiles = os.listdir(dir_path)
                
                # For HLS streams, also check for files matching the video ID (in case yt-dlp didn't report the path correctly)
                video_id = info_dict.get('id') or ''
                if video_id and is_hls:
                    logger.info(f"[HLS] Searching for files matching video ID: {video_id}")
                    # Check for files starting with video ID (common pattern for HLS downloads)
                    id_matching_files = [fname for fname in allfiles if fname.startswith(video_id) and not fname.endswith(('.txt', '.json', '.jpg', '.jpeg', '.png'))]
                    if id_matching_files:
                        logger.info(f"[HLS] Found files matching video ID: {id_matching_files}")
                        # Prefer .mpegts or .ts files for HLS
                        hls_files = [f for f in id_matching_files if f.endswith(('.mpegts', '.ts', '.mp4'))]
                        if hls_files:
                            downloaded_file = hls_files[0]
                            downloaded_abs_path = os.path.abspath(os.path.join(dir_path, downloaded_file))
                            logger.info(f"[HLS] Using file matching video ID: {downloaded_file}")
                
                if not downloaded_file:
                    files = [fname for fname in allfiles if fname.endswith(video_extensions)]
                    files.sort()
                    
                    # Log all found files for debugging
                    logger.info(f"Found video files in {dir_path}: {files}")
                    
                    # If no files found with preferred format, try to find any video file
                    if not files:
                        logger.warning(f"No files found with preferred format {target_format}, searching for any video file")
                        fallback_extensions = ('.mp4', '.mkv', '.webm', '.ts', '.mpegts', '.avi', '.mov', '.flv', '.3gp', '.ogv', '.wmv', '.asf', '.m4v')
                        files = [fname for fname in allfiles if fname.endswith(fallback_extensions)]
                        files.sort()
                        logger.info(f"Found video files with fallback search: {files}")
                    
                    if not files:
                        send_error_to_user(message, safe_get_messages(user_id).SKIPPING_UNSUPPORTED_FILE_TYPE_MSG.format(index=current_index))
                        continue

                    downloaded_file = files[0]
                    downloaded_abs_path = os.path.abspath(os.path.join(dir_path, downloaded_file))
            
            logger.info(f"Selected downloaded file: {downloaded_file}")
            
            # Apply explicit trimming if download_sections was specified
            # This ensures trimming even if download_sections didn't work (e.g., for HLS streams)
            if download_sections and downloaded_abs_path and os.path.exists(downloaded_abs_path):
                import re
                trim_match = re.match(r'\*(\d{2}):(\d{2}):(\d{2})-(\d{2}):(\d{2}):(\d{2})', download_sections)
                if trim_match:
                    start_h, start_m, start_s, end_h, end_m, end_s = map(int, trim_match.groups())
                    start_seconds = start_h * 3600 + start_m * 60 + start_s
                    end_seconds = end_h * 3600 + end_m * 60 + end_s
                    
                    expected_duration = end_seconds - start_seconds
                    
                    # Check video duration using ffprobe to verify if trimming is needed
                    try:
                        # get_video_info_ffprobe is already imported globally
                        width, height, video_duration = get_video_info_ffprobe(downloaded_abs_path)
                        video_duration = float(video_duration) if video_duration else 0
                        
                        # Always trim if video is longer than expected (download_sections didn't work)
                        # Or if video is significantly different from expected (more than 5 seconds difference)
                        if video_duration > expected_duration + 5:  # Allow 5 seconds tolerance
                            logger.info(f"[TRIM] Video duration ({video_duration}s) is longer than expected ({expected_duration}s), applying explicit trim")
                            logger.info(f"[TRIM] Trimming video from {start_seconds}s to {end_seconds}s")
                            
                            # Create temporary trimmed file with .mp4 extension so FFmpeg can detect format
                            base_path = os.path.splitext(downloaded_abs_path)[0]
                            temp_trimmed_path = base_path + '.trimmed.mp4'
                            from DOWN_AND_UP.ffmpeg import ffmpeg_extract_subclip
                            
                            if ffmpeg_extract_subclip(downloaded_abs_path, start_seconds, end_seconds, temp_trimmed_path):
                                # Verify trimmed file exists and has correct size
                                if os.path.exists(temp_trimmed_path) and os.path.getsize(temp_trimmed_path) > 0:
                                    # Verify trimmed file duration
                                    try:
                                        _, _, trimmed_duration = get_video_info_ffprobe(temp_trimmed_path)
                                        trimmed_duration = float(trimmed_duration) if trimmed_duration else 0
                                        expected_trimmed_duration = end_seconds - start_seconds
                                        
                                        # Allow 5 seconds tolerance for trimmed duration
                                        if abs(trimmed_duration - expected_trimmed_duration) <= 5:
                                            # Replace original with trimmed version
                                            import shutil
                                            shutil.move(temp_trimmed_path, downloaded_abs_path)
                                            logger.info(f"[TRIM] Successfully trimmed video to {trimmed_duration}s (expected {expected_trimmed_duration}s)")
                                            
                                            # Verify replacement was successful
                                            _, _, final_duration = get_video_info_ffprobe(downloaded_abs_path)
                                            final_duration = float(final_duration) if final_duration else 0
                                            logger.info(f"[TRIM] Final file duration after replacement: {final_duration}s")
                                        else:
                                            logger.error(f"[TRIM] Trimmed file duration ({trimmed_duration}s) doesn't match expected ({expected_trimmed_duration}s), keeping original")
                                            # Clean up temp file
                                            if os.path.exists(temp_trimmed_path):
                                                try:
                                                    os.remove(temp_trimmed_path)
                                                except Exception:
                                                    pass
                                    except Exception as verify_error:
                                        logger.error(f"[TRIM] Error verifying trimmed file: {verify_error}, keeping original")
                                        # Clean up temp file
                                        if os.path.exists(temp_trimmed_path):
                                            try:
                                                os.remove(temp_trimmed_path)
                                            except Exception:
                                                pass
                                else:
                                    logger.error(f"[TRIM] Trimmed file is missing or empty, keeping original")
                                    # Clean up temp file if it exists
                                    if os.path.exists(temp_trimmed_path):
                                        try:
                                            os.remove(temp_trimmed_path)
                                        except Exception:
                                            pass
                            else:
                                logger.error(f"[TRIM] Failed to trim video, using original file")
                                # Clean up temp file if it exists
                                if os.path.exists(temp_trimmed_path):
                                    try:
                                        os.remove(temp_trimmed_path)
                                    except Exception:
                                        pass
                        else:
                            logger.info(f"[TRIM] Video duration ({video_duration}s) matches expected ({expected_duration}s), trimming may have worked via download_sections")
                    except Exception as trim_error:
                        # If we can't check duration, still try to trim to be safe
                        logger.warning(f"[TRIM] Error checking video duration: {trim_error}, attempting trim anyway")
                        try:
                            temp_trimmed_path = downloaded_abs_path + '.trimmed.tmp'
                            from DOWN_AND_UP.ffmpeg import ffmpeg_extract_subclip
                            
                            if ffmpeg_extract_subclip(downloaded_abs_path, start_seconds, end_seconds, temp_trimmed_path):
                                # Verify trimmed file exists and has correct size
                                if os.path.exists(temp_trimmed_path) and os.path.getsize(temp_trimmed_path) > 0:
                                    # Verify trimmed file duration
                                    try:
                                        _, _, trimmed_duration = get_video_info_ffprobe(temp_trimmed_path)
                                        trimmed_duration = float(trimmed_duration) if trimmed_duration else 0
                                        expected_trimmed_duration = end_seconds - start_seconds
                                        
                                        # Allow 5 seconds tolerance for trimmed duration
                                        if abs(trimmed_duration - expected_trimmed_duration) <= 5:
                                            # Replace original with trimmed version
                                            import shutil
                                            shutil.move(temp_trimmed_path, downloaded_abs_path)
                                            logger.info(f"[TRIM] Successfully trimmed video to {trimmed_duration}s (expected {expected_trimmed_duration}s, duration check failed)")
                                            
                                            # Verify replacement was successful
                                            _, _, final_duration = get_video_info_ffprobe(downloaded_abs_path)
                                            final_duration = float(final_duration) if final_duration else 0
                                            logger.info(f"[TRIM] Final file duration after replacement: {final_duration}s")
                                        else:
                                            logger.error(f"[TRIM] Trimmed file duration ({trimmed_duration}s) doesn't match expected ({expected_trimmed_duration}s), keeping original")
                                            # Clean up temp file
                                            if os.path.exists(temp_trimmed_path):
                                                try:
                                                    os.remove(temp_trimmed_path)
                                                except Exception:
                                                    pass
                                    except Exception as verify_error:
                                        logger.error(f"[TRIM] Error verifying trimmed file: {verify_error}, keeping original")
                                        # Clean up temp file
                                        if os.path.exists(temp_trimmed_path):
                                            try:
                                                os.remove(temp_trimmed_path)
                                            except Exception:
                                                pass
                                else:
                                    logger.error(f"[TRIM] Trimmed file is missing or empty, keeping original")
                                    # Clean up temp file if it exists
                                    if os.path.exists(temp_trimmed_path):
                                        try:
                                            os.remove(temp_trimmed_path)
                                        except Exception:
                                            pass
                            else:
                                logger.error(f"[TRIM] Failed to trim video")
                        except Exception as trim_exec_error:
                            logger.error(f"[TRIM] Error during trim execution: {trim_exec_error}")
                            import traceback as tb_module
                            logger.error(tb_module.format_exc())
            write_logs(message, url, downloaded_file)
            
            # Save original filename for subtitle search
            original_video_filename = downloaded_file
            original_video_path = downloaded_abs_path or os.path.join(dir_path, original_video_filename)

            if rename_name == video_title:
                caption_name = original_video_title  # Original title for caption
                # Clean up the filename by removing common subtitle indicators
                cleaned_title = original_video_title
                # Remove common subtitle indicators from the title
                subtitle_indicators = [
                    " (English subtitles)",
                    " (English)",
                    " (Subtitles)",
                    " (Subs)",
                    " [English subtitles]",
                    " [English]",
                    " [Subtitles]",
                    " [Subs]",
                    " - English subtitles",
                    " - English",
                    " - Subtitles",
                    " - Subs"
                ]
                for indicator in subtitle_indicators:
                    cleaned_title = cleaned_title.replace(indicator, "")
                
                # Use cleaned title for filename
                final_name = sanitize_filename_strict(cleaned_title + os.path.splitext(downloaded_file)[1])
                if final_name != downloaded_file:
                    old_path = downloaded_abs_path or os.path.join(dir_path, downloaded_file)
                    new_path = os.path.join(dir_path, final_name)
                    try:
                        # Check if source file exists before renaming
                        if not os.path.exists(old_path):
                            # Check if .part file exists and wait for it to complete
                            part_path = old_path + '.part'
                            if os.path.exists(part_path):
                                logger.info(f"Source file {old_path} not found, but .part file exists. Waiting for download to complete...")
                                # Wait for .part file to be renamed by yt-dlp (max 30 seconds)
                                max_wait = 30
                                wait_interval = 0.5
                                waited = 0
                                while waited < max_wait:
                                    if os.path.exists(old_path):
                                        logger.info(f"File {old_path} appeared after waiting {waited} seconds")
                                        break
                                    time.sleep(wait_interval)
                                    waited += wait_interval
                                
                                # If file still doesn't exist, try to rename .part file directly
                                if not os.path.exists(old_path) and os.path.exists(part_path):
                                    try:
                                        logger.info(f"Attempting to rename .part file directly: {part_path} -> {old_path}")
                                        # Check if target directory exists
                                        target_dir = os.path.dirname(old_path)
                                        if not os.path.exists(target_dir):
                                            os.makedirs(target_dir, exist_ok=True)
                                        # Check if old_path starts with '-' which can cause issues
                                        if os.path.basename(old_path).startswith('-'):
                                            logger.warning(f"Target filename starts with '-', using original filename instead")
                                            final_name = downloaded_file
                                            caption_name = original_video_title
                                        else:
                                            os.rename(part_path, old_path)
                                            logger.info(f"Successfully renamed .part file to {old_path}")
                                    except (OSError, FileNotFoundError) as rename_e:
                                        logger.error(f"Failed to rename .part file: {rename_e}")
                                        # Try to find the actual downloaded file
                                        try:
                                            if os.path.exists(dir_path):
                                                files = [f for f in os.listdir(dir_path) if f.endswith(('.mp4', '.mkv', '.webm', '.avi', '.mov', '.flv', '.m4v', '.ts', '.mpegts')) and not f.endswith('.part')]
                                                if files:
                                                    final_name = files[0]
                                                    logger.info(f"Found alternative file: {final_name}")
                                                else:
                                                    final_name = downloaded_file
                                            else:
                                                final_name = downloaded_file
                                        except Exception:
                                            final_name = downloaded_file
                                        caption_name = original_video_title
                                    except Exception as rename_e:
                                        logger.error(f"Unexpected error renaming .part file: {rename_e}")
                                        final_name = downloaded_file
                                        caption_name = original_video_title
                                else:
                                    if not os.path.exists(old_path):
                                        logger.warning(f"File {old_path} still not found after waiting. Using original filename.")
                                        final_name = downloaded_file
                                        caption_name = original_video_title
                            else:
                                logger.error(f"Source file {old_path} not found for renaming")
                                final_name = downloaded_file
                        else:
                            if os.path.exists(new_path):
                                os.remove(new_path)
                            os.rename(old_path, new_path)
                    except Exception as e:
                        logger.error(f"Error renaming file from {old_path} to {new_path}: {e}")
                        final_name = downloaded_file
            else:
                ext = os.path.splitext(downloaded_file)[1]
                # Sanitize filename for disk storage while keeping original title for caption
                final_name = sanitize_filename(rename_name + ext)
                caption_name = rename_name  # Original title for caption
                old_path = downloaded_abs_path or os.path.join(dir_path, downloaded_file)
                new_path = os.path.join(dir_path, final_name)

                if os.path.exists(new_path):
                    try:
                        os.remove(new_path)
                    except Exception as e:
                        logger.error(f"Error removing existing file {new_path}: {e}")

                try:
                    # Check if source file exists before renaming
                    if not os.path.exists(old_path):
                        # Check if .part file exists and wait for it to complete
                        part_path = old_path + '.part'
                        if os.path.exists(part_path):
                            logger.info(f"Source file {old_path} not found, but .part file exists. Waiting for download to complete...")
                            # Wait for .part file to be renamed by yt-dlp (max 30 seconds)
                            max_wait = 30
                            wait_interval = 0.5
                            waited = 0
                            while waited < max_wait:
                                if os.path.exists(old_path):
                                    logger.info(f"File {old_path} appeared after waiting {waited} seconds")
                                    break
                                time.sleep(wait_interval)
                                waited += wait_interval
                            
                            # If file still doesn't exist, try to rename .part file directly
                            if not os.path.exists(old_path) and os.path.exists(part_path):
                                try:
                                    logger.info(f"Attempting to rename .part file directly: {part_path} -> {old_path}")
                                    # Check if target directory exists
                                    target_dir = os.path.dirname(old_path)
                                    if not os.path.exists(target_dir):
                                        os.makedirs(target_dir, exist_ok=True)
                                    # Check if old_path starts with '-' which can cause issues
                                    if os.path.basename(old_path).startswith('-'):
                                        logger.warning(f"Target filename starts with '-', using original filename instead")
                                        final_name = downloaded_file
                                        caption_name = original_video_title
                                    else:
                                        os.rename(part_path, old_path)
                                        logger.info(f"Successfully renamed .part file to {old_path}")
                                except (OSError, FileNotFoundError) as rename_e:
                                    logger.error(f"Failed to rename .part file: {rename_e}")
                                    # Try to find the actual downloaded file
                                    try:
                                        if os.path.exists(dir_path):
                                            files = [f for f in os.listdir(dir_path) if f.endswith(('.mp4', '.mkv', '.webm', '.avi', '.mov', '.flv', '.m4v', '.ts', '.mpegts')) and not f.endswith('.part')]
                                            if files:
                                                final_name = files[0]
                                                logger.info(f"Found alternative file: {final_name}")
                                            else:
                                                final_name = downloaded_file
                                        else:
                                            final_name = downloaded_file
                                    except Exception:
                                        final_name = downloaded_file
                                    caption_name = original_video_title
                                except Exception as rename_e:
                                    logger.error(f"Unexpected error renaming .part file: {rename_e}")
                                    final_name = downloaded_file
                                    caption_name = original_video_title
                            else:
                                if not os.path.exists(old_path):
                                    logger.warning(f"File {old_path} still not found after waiting. Using original filename.")
                                    final_name = downloaded_file
                                    caption_name = original_video_title
                        else:
                            logger.error(f"Source file {old_path} not found for renaming")
                            final_name = downloaded_file
                            caption_name = original_video_title
                    else:
                        os.rename(old_path, new_path)
                except Exception as e:
                    logger.error(f"Error renaming file from {old_path} to {new_path}: {e}")
                    final_name = downloaded_file
                    caption_name = original_video_title  # Original title for caption

            user_vid_path = os.path.join(dir_path, final_name)
            if final_name.lower().endswith((".webm", ".ts", ".mpegts")):
                # Check if source file exists before conversion
                if not os.path.exists(user_vid_path):
                    logger.error(f"Source file for conversion not found: {user_vid_path}")
                    send_error_to_user(message, safe_get_messages(user_id).CONVERSION_TO_MP4_FAILED_MSG.format(error="Source file not found"))
                    continue
                
                try:
                    safe_edit_message_text(user_id, proc_msg_id,
                        f"{info_text}\n{full_bar}   100.0%\nConverting video using ffmpeg... ⏳")
                except Exception as e:
                    logger.error(f"Error updating status before conversion: {e}")

                mp4_basename = sanitize_filename_strict(os.path.splitext(final_name)[0]) + ".mp4"
                mp4_file = os.path.join(dir_path, mp4_basename)

                # Get FFmpeg path using the common function
                from DOWN_AND_UP.ffmpeg import get_ffmpeg_path
                ffmpeg_path = get_ffmpeg_path()
                if not ffmpeg_path:
                    send_error_to_user(message, safe_get_messages(user_id).FFMPEG_NOT_FOUND_MSG)
                    break
                
                # For m3u8 streams, use more robust conversion options
                is_m3u8 = final_name.lower().endswith((".ts", ".mpegts")) or ".m3u8" in url.lower() or is_hls
                if is_m3u8:
                    ffmpeg_cmd = [
                        ffmpeg_path,
                        "-y",
                        "-i", user_vid_path,
                        "-c:v", "libx264",
                        "-preset", "medium",
                        "-crf", "23",
                        "-c:a", "aac",
                        "-b:a", "128k",
                        "-movflags", "+faststart",
                        "-fflags", "+genpts",
                        mp4_file
                    ]
                else:
                    ffmpeg_cmd = [
                        ffmpeg_path,
                        "-y",
                        "-i", user_vid_path,
                        "-c:v", "libx264",
                        "-preset", "fast",
                        "-crf", "23",
                        "-c:a", "aac",
                        "-b:a", "128k",
                        mp4_file
                    ]
                try:
                    result = subprocess.run(ffmpeg_cmd, check=True, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=3600)
                    # Verify output file was created and is not empty
                    if os.path.exists(mp4_file) and os.path.getsize(mp4_file) > 0:
                        try:
                            os.remove(user_vid_path)
                        except Exception as e:
                            logger.warning(f"Failed to remove original file {user_vid_path}: {e}")
                        user_vid_path = mp4_file
                        final_name = mp4_basename
                    else:
                        raise subprocess.CalledProcessError(1, ffmpeg_cmd, "Output file not created or is empty")
                except subprocess.TimeoutExpired:
                    logger.error(f"FFmpeg conversion timeout for {user_vid_path}")
                    error_message = safe_get_messages(user_id).DOWN_UP_VIDEO_CONVERSION_FAILED_MSG
                    error_message += (
                        "**Possible causes:**\n"
                        "• Video file is too large or complex\n"
                        "• Conversion process exceeded time limit\n"
                        "• Insufficient system resources\n\n"
                        "**Solutions:**\n"
                        "• Try downloading with a different quality\n"
                        "• The original file will be sent without conversion\n"
                    )
                    send_error_to_user(message, error_message)
                    continue
                except subprocess.CalledProcessError as e:
                    error_details = f"Return code: {e.returncode}"
                    if e.stderr:
                        error_details += f"\nError output: {e.stderr[:500]}"
                    if e.stdout:
                        error_details += f"\nStandard output: {e.stdout[:500]}"
                    
                    # Check for specific FFmpeg errors
                    if "Invalid argument" in str(e.stderr):
                        error_message = safe_get_messages(user_id).DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG
                        error_message += (
                            "**Possible causes:**\n"
                            "• Unsupported video codec or format\n"
                            "• Corrupted source file\n"
                            "• Incompatible video parameters\n"
                            "• Insufficient system resources\n\n"
                            "**Solutions:**\n"
                            "• Try downloading with a different quality\n"
                            "• Check if the source video is corrupted\n"
                            "• Try a different video source if available\n"
                            "• The original file will be sent without conversion\n\n"
                            f"**Technical details:** {error_details}"
                        )
                    else:
                        error_message = safe_get_messages(user_id).DOWN_UP_VIDEO_CONVERSION_FAILED_MSG
                        error_message += (
                            "**Solutions:**\n"
                            "• Try downloading with a different quality\n"
                            "• The original file will be sent without conversion\n"
                            "• If the problem persists, try a different video source\n\n"
                            f"**Technical details:** {error_details}"
                        )
                    
                    send_error_to_user(message, error_message)
                    logger.error(f"FFmpeg conversion failed: {error_details}")
                    break
                except Exception as e:
                    send_error_to_user(message, safe_get_messages(user_id).CONVERSION_TO_MP4_FAILED_MSG.format(error=e))
                    break

            after_rename_abs_path = os.path.abspath(user_vid_path)
            # --- YouTube thumbnail logic (priority over ffmpeg) ---
            youtube_thumb_path = None
            thumb_dir = None
            duration = 0
            thumb_source_url = video_page_url or url
            
            # Try to download YouTube thumbnail first
            # Безопасная проверка домена через urlparse
            try:
                from urllib.parse import urlparse
                parsed_thumb_url = urlparse(thumb_source_url)
                thumb_hostname = (parsed_thumb_url.hostname or '').lower()
                is_youtube = thumb_hostname in ('youtube.com', 'www.youtube.com', 'youtu.be', 'www.youtu.be') or \
                            thumb_hostname.endswith('.youtube.com') or thumb_hostname.endswith('.youtu.be')
            except Exception:
                is_youtube = False
            
            if is_youtube:
                try:
                    yt_id = video_id or None
                    if not yt_id:
                        try:
                            yt_id = extract_youtube_id(thumb_source_url, user_id)
                        except Exception:
                            yt_id = None
                    if yt_id:
                        youtube_thumb_path = os.path.join(dir_path, f"yt_thumb_{yt_id}.jpg")
                        download_thumbnail(yt_id, youtube_thumb_path, url)
                        if os.path.exists(youtube_thumb_path):
                            thumb_dir = youtube_thumb_path
                            logger.info(f"Downloaded thumbnail to download directory: {youtube_thumb_path}")
                            logger.info(f"Using YouTube thumbnail: {youtube_thumb_path}")
                except Exception as e:
                    logger.warning(f"YouTube thumbnail download failed: {e}")
            # If not YouTube or YouTube thumb not found, try universal thumbnail downloader
            if not thumb_dir:
                try:
                    universal_thumb_path = os.path.join(dir_path, "universal_thumb.jpg")
                    if download_universal_thumbnail(thumb_source_url, universal_thumb_path):
                        if os.path.exists(universal_thumb_path):
                            thumb_dir = universal_thumb_path
                            logger.info(f"Using universal thumbnail: {universal_thumb_path}")
                except Exception as e:
                    logger.info(f"Universal thumbnail not available: {e}")
            
            # Get video duration (always needed)
            try:
                width, height, duration = get_video_info_ffprobe(user_vid_path)
                if duration == 0:
                    logger.warning("Failed to get video duration via get_video_info_ffprobe, trying direct ffmpeg")
                    # Get FFmpeg path using the common function
                    from DOWN_AND_UP.ffmpeg import get_ffmpeg_path
                    ffmpeg_path = get_ffmpeg_path()
                    if not ffmpeg_path:
                        logger.error("ffmpeg not found in PATH or project directory.")
                        duration = 0
                    else:
                        ffmpeg_duration_command = [
                            ffmpeg_path, "-i", user_vid_path, "-f", "null", "-"
                        ]
                        result = subprocess.run(ffmpeg_duration_command, capture_output=True, text=True, timeout=int(30), encoding='utf-8', errors='replace')
                        output = result.stderr  # ffmpeg outputs info to stderr
                        duration_match = re.search(r'Duration: (\d{2}):(\d{2}):(\d{2})\.(\d{2})', output)
                        if duration_match:
                            hours, minutes, seconds, centiseconds = map(int, duration_match.groups())
                            duration = int(hours * 3600 + minutes * 60 + seconds + centiseconds / 100)
            except Exception as e:
                logger.warning(f"Failed to get video duration: {e}")
                duration = 0
            
            # Use ffmpeg thumbnail only as fallback (when both YouTube/universal thumbnails failed)
            if not thumb_dir:
                result = get_duration_thumb(message, dir_path, user_vid_path, sanitize_filename_strict(caption_name))
                if result is None:
                    logger.warning("Failed to create ffmpeg thumbnail fallback")
                    thumb_dir = None
                else:
                    duration_from_ffmpeg, thumb_dir_ffmpeg = result
                    thumb_dir = thumb_dir_ffmpeg
                    if duration == 0:  # Use duration from ffmpeg if we couldn't get it with ffprobe
                        duration = duration_from_ffmpeg
                    logger.info(f"Using ffmpeg thumbnail fallback: {thumb_dir}")
            
            # Check for the existence of a preview and create a default one if needed
            if thumb_dir and not os.path.exists(thumb_dir):
                logger.warning(f"Thumbnail not found at {thumb_dir}, creating default")
                create_default_thumbnail(os.path.join(dir_path, "default_thumb.jpg"))
                thumb_dir = os.path.join(dir_path, "default_thumb.jpg")
                if not os.path.exists(thumb_dir):
                    logger.warning("Failed to create default thumbnail, continuing without thumbnail")
                    thumb_dir = None

            video_size_in_bytes = os.path.getsize(user_vid_path)
            video_size = humanbytes(int(video_size_in_bytes))
            max_size = get_user_split_size(user_id)  # 1.95 GB - close to Telegram's 2GB limit with 50MB safety margin
            if int(video_size_in_bytes) > max_size:
                safe_edit_message_text(user_id, proc_msg_id,
                    f"{info_text}\n{full_bar}   100.0%\n<i>⚠️ Your video size ({video_size}) is too large.</i>\n<i>Splitting file...</i> ✂️")
                returned = split_video_2(dir_path, sanitize_filename_strict(caption_name), after_rename_abs_path, int(video_size_in_bytes), max_size, int(duration), user_id)
                caption_lst = returned.get("video")
                path_lst = returned.get("path")
                # Accumulate all IDs of split video parts
                # Note: split_msg_ids is already initialized at function start, don't reset it here
                for p in range(len(caption_lst) if caption_lst else 0):
                    caption_name = caption_lst[p] if caption_lst and p < len(caption_lst) else f"part_{p+1}"
                    part_result = get_duration_thumb(message, dir_path, path_lst[p], sanitize_filename_strict(caption_name))
                    if part_result is None:
                        continue
                    part_duration, splited_thumb_dir = part_result
                    # --- TikTok: Don't Pass Title ---
                    video_msg = send_videos(message, path_lst[p], '' if force_no_title else caption_name, part_duration, splited_thumb_dir, info_text, proc_msg.id, full_video_title, tags_text_final)
                    if not video_msg:
                        logger.error("send_videos returned None for split part; skipping cache save for this part")
                        continue
                    #found_type = None
                    # Note: Forwarding to log channels is now handled in send_videos function
                    # We need to get the forwarded message IDs from the log channel for caching
                    try:
                        # Determine the correct log channel based on content type
                        from HELPERS.porn import is_porn
                        is_nsfw = is_porn(url, "", "", None) or user_forced_nsfw
                        logger.info(f"[FALLBACK] is_porn check for {url}: {is_porn(url, '', '', None)}, user_forced_nsfw: {user_forced_nsfw}, final is_nsfw: {is_nsfw}")
                        is_private_chat = getattr(message.chat, "type", None) == enums.ChatType.PRIVATE
                        is_paid = is_nsfw and is_private_chat
                        logger.info(f"[VIDEO CACHE] URL analysis: url={url}, is_nsfw={is_nsfw}, is_private_chat={is_private_chat}, is_paid={is_paid}")
                        
                        # Handle different content types according to new logic
                        if is_paid:
                            # For NSFW content in private chat, send_videos already sent paid media to user
                            # Send paid copy to LOGS_PAID_ID and open copy to LOGS_NSFW_ID for history
                            
                            # Send paid copy to LOGS_PAID_ID
                            log_channel_paid = get_log_channel("video", paid=True)
                            try:
                                # Forward the paid video to LOGS_PAID_ID
                                safe_forward_messages(log_channel_paid, user_id, [video_msg.id])
                                logger.info(f"down_and_up: NSFW content paid copy sent to PAID channel")
                            except Exception as e:
                                logger.error(f"down_and_up: failed to send paid copy to PAID channel: {e}")
                            
                            # Send open copy to LOGS_NSFW_ID for history
                            log_channel_nsfw = get_log_channel("video", nsfw=True)
                            if log_channel_nsfw and log_channel_nsfw != 0:
                                try:
                                    # Get video dimensions for proper aspect ratio
                                    try:
                                        v_w, v_h, v_dur = get_video_info_ffprobe(path_lst[p])
                                    except Exception:
                                        v_w, v_h, v_dur = width, height, part_duration
                                    
                                    # Create open copy for history (without stars) - send directly to NSFW channel
                                    open_video_msg = app.send_video(
                                        chat_id=log_channel_nsfw,
                                        video=path_lst[p],
                                        caption=caption_lst[p] if caption_lst and p < len(caption_lst) else f"part_{p+1}",
                                        duration=int(v_dur) if v_dur else part_duration,
                                        width=int(v_w) if v_w else width,
                                        height=int(v_h) if v_h else height,
                                        thumb=splited_thumb_dir,
                                        reply_parameters=ReplyParameters(message_id=message.id)
                                    )
                                    logger.info(f"down_and_up: NSFW content open copy sent to NSFW channel for history")
                                    already_forwarded_to_log = True
                                except Exception as e:
                                    logger.error(f"down_and_up: failed to send open copy to NSFW channel: {e}")
                            else:
                                logger.warning(f"down_and_up: NSFW channel not available (ID: {log_channel_nsfw}), skipping open copy")
                            
                            # Don't cache NSFW content
                            logger.info(f"down_and_up: NSFW content sent to user (paid), PAID channel (paid copy), and NSFW channel (open copy), not cached")
                            forwarded_msgs = None
                            
                        elif is_nsfw:
                            # NSFW content in groups -> LOGS_NSFW_ID only
                            # For split videos, always forward each part to NSFW channel
                            # For playlists, always forward each video to NSFW channel (don't use already_forwarded_to_log)
                            # IMPORTANT: For split videos in playlists, only forward once (split video takes priority)
                            if caption_lst and len(caption_lst) > 1:
                                # This is a split video - always forward each part (even if it's in a playlist)
                                log_channel = get_log_channel("video", nsfw=True)
                                if log_channel and log_channel != 0:
                                    try:
                                        forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                        logger.info(f"down_and_up: NSFW content sent to NSFW channel")
                                    except Exception as e:
                                        logger.error(f"down_and_up: failed to forward to NSFW channel: {e}")
                                        forwarded_msgs = None
                                else:
                                    logger.warning(f"down_and_up: NSFW channel not available (ID: {log_channel}), skipping forward")
                                    forwarded_msgs = None
                            elif is_playlist:
                                # For playlists (non-split videos), always forward each video to NSFW channel
                                log_channel = get_log_channel("video", nsfw=True)
                                if log_channel and log_channel != 0:
                                    try:
                                        forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                        logger.info(f"down_and_up: NSFW content sent to NSFW channel")
                                    except Exception as e:
                                        logger.error(f"down_and_up: failed to forward to NSFW channel: {e}")
                                        forwarded_msgs = None
                                else:
                                    logger.warning(f"down_and_up: NSFW channel not available (ID: {log_channel}), skipping forward")
                                    forwarded_msgs = None
                            elif not already_forwarded_to_log:
                                already_forwarded_to_log = True  # Set flag BEFORE forward to prevent duplicates
                                log_channel = get_log_channel("video", nsfw=True)
                                if log_channel and log_channel != 0:
                                    try:
                                        forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                        logger.info(f"down_and_up: NSFW content sent to NSFW channel")
                                    except Exception as e:
                                        logger.error(f"down_and_up: failed to forward to NSFW channel: {e}")
                                        forwarded_msgs = None
                                else:
                                    logger.warning(f"down_and_up: NSFW channel not available (ID: {log_channel}), skipping forward")
                                    forwarded_msgs = None
                            else:
                                logger.info("down_and_up: skipping forward to NSFW channel - already forwarded to log")
                                forwarded_msgs = None
                            
                            # Don't cache NSFW content
                            logger.info(f"down_and_up: NSFW content sent to NSFW channel, not cached")
                            
                        else:
                            # Regular content -> LOGS_VIDEO_ID and cache
                            # For split videos, always forward each part to log channel
                            # For playlists, always forward each video to log channel (don't use already_forwarded_to_log)
                            # IMPORTANT: For split videos in playlists, only forward once (split video takes priority)
                            if caption_lst and len(caption_lst) > 1:
                                # This is a split video - always forward each part (even if it's in a playlist)
                                log_channel = get_log_channel("video")
                                forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                            elif is_playlist:
                                # For playlists (non-split videos), always forward each video to log channel
                                log_channel = get_log_channel("video")
                                forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                            elif not already_forwarded_to_log:
                                already_forwarded_to_log = True  # Set flag BEFORE forward to prevent duplicates
                                log_channel = get_log_channel("video")
                                forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                            else:
                                logger.info("down_and_up: skipping forward to LOGS_VIDEO_ID - already forwarded to log")
                                forwarded_msgs = None
                        logger.info(f"down_and_up: forwarded_msgs result: {forwarded_msgs}")
                        if forwarded_msgs:
                            logger.info(f"down_and_up: collecting forwarded message IDs for split video: {[m.id for m in forwarded_msgs]}")
                            if is_playlist:
                                # For playlists, save to playlist cache with index
                                current_video_index = current_index
                                rounded_quality_key = safe_quality_key
                                try:
                                    if safe_quality_key.endswith('p'):
                                        rounded_quality_key = f"{ceil_to_popular(int(safe_quality_key[:-1]))}p"
                                except Exception:
                                    pass
                                # Use the already determined subtitle availability
                                # Check if cache should be disabled due to active functions (TRIM/SUBS/DUBS)
                                if not should_disable_cache and not need_subs:
                                    # Only cache regular content (not NSFW)
                                    if not is_nsfw:
                                        # Передаем уникальную ссылку видео для дополнительного кэширования
                                        video_urls_dict = {current_video_index: playlist_video_urls.get(current_video_index)} if current_video_index in playlist_video_urls else None
                                        save_to_playlist_cache(get_clean_playlist_url(url), rounded_quality_key, [current_video_index], [m.id for m in forwarded_msgs], original_text=message.text or message.caption or "", video_urls_dict=video_urls_dict)
                                    else:
                                        logger.info(f"NSFW content not cached (found_type={found_type}, auto_mode={auto_mode})")
                                else:
                                    if should_disable_cache:
                                        logger.info(f"Video not cached due to active functions (TRIM/SUBS/DUBS): TRIM={active_funcs['has_trim']}, SUBS={active_funcs['has_subs']}, DUBS={active_funcs['has_dubs']}")
                                    else:
                                        logger.info(f"Video with subtitles is not cached (found_type={found_type}, auto_mode={auto_mode})")
                                cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), rounded_quality_key, [current_video_index])
                                logger.info(f"Checking the cache immediately after writing: {cached_check}")
                                playlist_indices.append(current_video_index)
                                playlist_msg_ids.extend([m.id for m in forwarded_msgs])
                            else:
                                # Accumulate IDs of parts for split video
                                split_msg_ids.extend([m.id for m in forwarded_msgs])
                        else:
                            logger.info(f"down_and_up: collecting video_msg.id for split video: {video_msg.id}")
                            if is_playlist:
                                # For playlists, save to playlist cache with video index
                                current_video_index = current_index
                                #found_type = check_subs_availability(url, user_id, safe_quality_key, return_type=True)
                                subs_enabled = is_subs_enabled(user_id)
                                auto_mode = get_user_subs_auto_mode(user_id)
                                need_subs = determine_need_subs(subs_enabled, found_type, user_id)
                                # Check if cache should be disabled due to active functions (TRIM/SUBS/DUBS)
                                if not should_disable_cache and not need_subs:
                                    # Передаем уникальную ссылку видео для дополнительного кэширования
                                    video_urls_dict = {current_video_index: playlist_video_urls.get(current_video_index)} if current_video_index in playlist_video_urls else None
                                    save_to_playlist_cache(get_clean_playlist_url(url), safe_quality_key, [current_video_index], [video_msg.id], original_text=message.text or message.caption or "", video_urls_dict=video_urls_dict)
                                else:
                                    if should_disable_cache:
                                        logger.info(f"Video not cached due to active functions (TRIM/SUBS/DUBS): TRIM={active_funcs['has_trim']}, SUBS={active_funcs['has_subs']}, DUBS={active_funcs['has_dubs']}")
                                    else:
                                        logger.info("Video with subtitles (subs.txt found) is not cached!")
                                cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), safe_quality_key, [current_video_index])
                                logger.info(f"Checking the cache immediately after writing: {cached_check}")
                                playlist_indices.append(current_video_index)
                                playlist_msg_ids.append(video_msg.id)
                            else:
                                # Accumulate IDs of parts for split video
                                split_msg_ids.append(video_msg.id)
                                logger.info(f"down_and_up: added video_msg.id to split_msg_ids: {video_msg.id}, current split_msg_ids: {split_msg_ids}")
                    except Exception as e:
                        # Check if error is related to quality_key - if so, ignore it completely
                        if "'quality_key'" in str(e):
                            logger.info(f"quality_key error ignored (non-critical): {e}")
                            # Quality_key errors don't affect functionality, just continue
                        else:
                            logger.error(f"Error forwarding video to logger: {e}")
                        logger.info(f"down_and_up: collecting video_msg.id after error for split video: {video_msg.id}")
                        
                        # PREVENTIVE FIX: Handle split video completion even after quality_key error
                        if split_msg_ids and not is_playlist:
                            logger.info(f"PREVENTIVE FIX: Processing split video completion after quality_key error in loop: {split_msg_ids}")
                            actual_video_count = len(split_msg_ids)
                            success_msg = f"<b>{safe_get_messages(user_id).DOWN_UP_UPLOAD_COMPLETE_MSG}</b> - {actual_video_count} {safe_get_messages(user_id).DOWN_UP_FILES_UPLOADED_MSG}.\n{safe_get_messages(user_id).CREDITS_MSG}"
                            logger.info(f"PREVENTIVE FIX: sending final success message for split video: {success_msg}")
                            safe_edit_message_text(user_id, proc_msg_id, success_msg)
                            send_to_logger(message, safe_get_messages(user_id).VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG)
                            break
                        if is_playlist:
                            # For playlists, save to playlist cache with video index
                            current_video_index = current_index
                            #found_type = check_subs_availability(url, user_id, safe_quality_key, return_type=True)
                            subs_enabled = is_subs_enabled(user_id)
                            auto_mode = get_user_subs_auto_mode(user_id)
                            need_subs = determine_need_subs(subs_enabled, found_type, user_id)
                            # Check if cache should be disabled due to active functions (TRIM/SUBS/DUBS)
                            if not should_disable_cache and not need_subs:
                                # Передаем уникальную ссылку видео для дополнительного кэширования
                                video_urls_dict = {current_video_index: playlist_video_urls.get(current_video_index)} if current_video_index in playlist_video_urls else None
                                save_to_playlist_cache(get_clean_playlist_url(url), safe_quality_key, [current_video_index], [video_msg.id], original_text=message.text or message.caption or "", video_urls_dict=video_urls_dict)
                            else:
                                if should_disable_cache:
                                    logger.info(f"Video not cached due to active functions (TRIM/SUBS/DUBS): TRIM={active_funcs['has_trim']}, SUBS={active_funcs['has_subs']}, DUBS={active_funcs['has_dubs']}")
                                else:
                                    logger.info("Video with subtitles (subs.txt found) is not cached!")
                            cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), safe_quality_key, [current_video_index])
                            logger.info(f"Checking the cache immediately after writing: {cached_check}")
                            playlist_indices.append(current_video_index)
                            playlist_msg_ids.append(video_msg.id)
                        else:
                            # Accumulate IDs of parts for split video
                            split_msg_ids.append(video_msg.id)
                            logger.info(f"down_and_up: added video_msg.id to split_msg_ids after error: {video_msg.id}, current split_msg_ids: {split_msg_ids}")
                            safe_edit_message_text(user_id, proc_msg_id,
                                f"{info_text}\n{full_bar}   100.0%\n<i>{safe_get_messages(user_id).DOWN_UP_SPLITTED_PART_UPLOADED_MSG.format(part=p + 1)}</i>")
                    if caption_lst and p < len(caption_lst) - 1:
                        pass
                    if os.path.exists(splited_thumb_dir):
                        os.remove(splited_thumb_dir)
                    send_mediainfo_if_enabled(user_id, path_lst[p], message)
                    if os.path.exists(path_lst[p]):
                        os.remove(path_lst[p])
                
                # Save all parts of split video to cache after the loop is completed
                logger.info(f"down_and_up: checking split_msg_ids for cache save: {split_msg_ids}, is_playlist={is_playlist}")
                if split_msg_ids and not is_playlist:
                    # Remove duplicates
                    split_msg_ids = list(dict.fromkeys(split_msg_ids))
                    logger.info(f"down_and_up: saving all split video parts to cache: {split_msg_ids}")
                    
                    # Update safe_quality_key to the actual quality used for splitting
                    if quality_key and quality_key != "best":
                        safe_quality_key = quality_key
                        logger.info(f"down_and_up: updated safe_quality_key for split video: {safe_quality_key}")
                    
                    # Check subtitle requirements for split videos
                    found_type = check_subs_availability(url, user_id, safe_quality_key, return_type=True)
                    subs_enabled = is_subs_enabled(user_id)
                    auto_mode = get_user_subs_auto_mode(user_id)
                    need_subs = determine_need_subs(subs_enabled, found_type, user_id)
                    
                    # Only save to cache if subtitles are not needed and functions are not active
                    if not should_disable_cache and not need_subs:
                        _save_video_cache_with_logging(url, safe_quality_key, split_msg_ids, original_text=message.text or message.caption or "", user_id=user_id, download_sections=download_sections, has_subs=need_subs, has_dubs=has_dubs)
                    else:
                        if should_disable_cache:
                            logger.info(f"Split video not cached due to active functions (TRIM/SUBS/DUBS): TRIM={active_funcs['has_trim']}, SUBS={active_funcs['has_subs']}, DUBS={active_funcs['has_dubs']}")
                        else:
                            logger.info(f"Split video with subtitles is not cached (found_type={found_type}, auto_mode={auto_mode}) - different users may need different languages")
                else:
                    logger.warning(f"down_and_up: NOT saving to cache - split_msg_ids={split_msg_ids}, is_playlist={is_playlist}")
                if os.path.exists(thumb_dir):
                    os.remove(thumb_dir)
                if os.path.exists(user_vid_path):
                    os.remove(user_vid_path)
                # Use the actual number of split parts for the success message
                actual_video_count = len(split_msg_ids) if split_msg_ids else video_count
                success_msg = f"<b>{safe_get_messages(user_id).DOWN_UP_UPLOAD_COMPLETE_MSG}</b> - {actual_video_count} {safe_get_messages(user_id).DOWN_UP_FILES_UPLOADED_MSG}.\n{safe_get_messages(user_id).CREDITS_MSG}"
                logger.info(f"down_and_up: sending final success message for split video: {success_msg}")
                safe_edit_message_text(user_id, proc_msg_id, success_msg)
                send_to_logger(message, safe_get_messages(user_id).VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG)
                
            else:
                if final_name:
                    # Read the full name from the file
                    full_caption = caption_name
                    try:
                        if os.path.exists(full_title_path):
                            with open(full_title_path, "r", encoding="utf-8") as f:
                                full_caption = f.read().strip()
                    except Exception as e:
                        logger.error(f"Error reading full title: {e}")

                    # Check for preview existence before sending
                    if thumb_dir and not os.path.exists(thumb_dir):
                        logger.warning(f"Thumbnail not found before sending, creating default")
                        create_default_thumbnail(os.path.join(dir_path, "default_thumb.jpg"))
                        thumb_dir = os.path.join(dir_path, "default_thumb.jpg")
                        if not os.path.exists(thumb_dir):
                            logger.warning("Failed to create default thumbnail before sending, continuing without thumbnail")
                            thumb_dir = None

                    try:
                        # --- TikTok: Don't Pass Title ---
                        # Embed subtitles if needed (only for single videos, not playlists)
                        is_playlist_mode = video_count > 1 or is_playlist_with_range(original_text)
                        if not is_playlist_mode:
                            # Check the limits for subtitles
                            subs_enabled = is_subs_enabled(user_id)
                            # Get the real size of the video
                            try:
                                # get_video_info_ffprobe is already imported globally
                                width, height, _ = get_video_info_ffprobe(after_rename_abs_path)
                                real_file_size = min(width, height)
                            except Exception as e:
                                logger.error(f"[FFPROBE BYPASS] Error while processing video {after_rename_abs_path}: {e}")
                                import traceback as tb_module
                                logger.error(tb_module.format_exc())
                                width, height = 0, 0
                                real_file_size = 0
                            auto_mode = get_user_subs_auto_mode(user_id)
                            if subs_enabled and is_youtube_url(url) and min(width, height) <= Config.MAX_SUB_QUALITY:
                                found_type = check_subs_availability(url, user_id, safe_quality_key, return_type=True)
                                # Use the helper function to determine subtitle availability
                                need_subs = determine_need_subs(subs_enabled, found_type, user_id)
                                logger.info(f"[SUBS EMBED] subs_enabled={subs_enabled}, found_type={found_type}, need_subs={need_subs}, video_size={min(width, height)}, user_id={user_id}")
                                if need_subs:
                                    
                                    # First, download the subtitles separately
                                    video_dir = os.path.dirname(after_rename_abs_path)
                                    # Get available languages from cache
                                    available_langs = _subs_check_cache.get(
                                        f"{url}_{user_id}_{'auto' if found_type == 'auto' else 'normal'}_langs",
                                        []
                                    )
                                    # Fallback: if cache is empty, recompute available languages (union of normal+auto)
                                    if not available_langs:
                                        try:
                                            logger.info("[SUBS] Cached languages empty, recomputing via availability check...")
                                            # Warm cache and compute both normal and auto lists
                                            check_subs_availability(url, user_id, return_type=True)
                                            from COMMANDS.subtitles_cmd import get_available_subs_languages
                                            normal_langs = get_available_subs_languages(url, user_id, auto_only=False)
                                            auto_langs = get_available_subs_languages(url, user_id, auto_only=True)
                                            available_langs = sorted(set(normal_langs) | set(auto_langs))
                                            logger.info(f"[SUBS] Recomputed languages: normal={normal_langs}, auto={auto_langs}")
                                        except Exception as e:
                                            logger.error(f"[SUBS] Failed to recompute available languages: {e}")
                                            available_langs = []

                                    # Try to download subtitles with the best-known languages list
                                    logger.info(f"[SUBS DOWNLOAD] Attempting to download subtitles with languages: {available_langs}")
                                    subs_path = download_subtitles_ytdlp(url, user_id, video_dir, available_langs)
                                    logger.info(f"[SUBS DOWNLOAD] Download result: {subs_path}")

                                    # If failed, one more fallback retry: recompute union and retry once
                                    if not subs_path:
                                        try:
                                            logger.info("[SUBS] First download attempt failed, retrying after forced recompute of languages...")
                                            from COMMANDS.subtitles_cmd import get_available_subs_languages
                                            normal_langs = get_available_subs_languages(url, user_id, auto_only=False)
                                            auto_langs = get_available_subs_languages(url, user_id, auto_only=True)
                                            retry_langs = sorted(set(normal_langs) | set(auto_langs))
                                            if retry_langs:
                                                subs_path = download_subtitles_ytdlp(url, user_id, video_dir, retry_langs)
                                        except Exception as e:
                                            logger.error(f"[SUBS] Retry recompute failed: {e}")

                                    if not subs_path:
                                        app.send_message(user_id, safe_get_messages(user_id).SUBTITLES_FAILED_MSG, reply_parameters=ReplyParameters(message_id=message.id))
                                        #continue
                                    
                                    # Get the real size of the file after downloading
                                    real_file_size = os.path.getsize(after_rename_abs_path) if os.path.exists(after_rename_abs_path) else 0
                                    
                                    # Create info_dict with real data
                                    real_info = {
                                        'duration': duration,  # Real duration
                                        'filesize': real_file_size,  # Real file size
                                        'filesize_approx': real_file_size
                                    }
                                    
                                    if check_subs_limits(real_info, safe_quality_key, message=message, user_id=user_id):
                                        status_msg = app.send_message(user_id, safe_get_messages(user_id).EMBEDDING_SUBTITLES_WARNING_MSG)
                                        def tg_update_callback(progress, eta):
                                            messages = safe_get_messages(user_id)
                                            blocks = int(progress * 10)
                                            bar = '🟩' * blocks + '⬜️' * (10 - blocks)
                                            percent = int(progress * 100)
                                            try:
                                                app.edit_message_text(
                                                    chat_id=user_id,
                                                    message_id=status_msg.id,
                                                    text=f"🔥 Embedding subtitles...\n{bar} {percent}%\nETA: {eta} min"
                                                )
                                            except Exception as e:
                                                logger.error(f"Failed to update subtitle progress: {e}")
                                        # Embed subtitles and get the result
                                        logger.info(f"Calling embed_subs_to_video with path: {after_rename_abs_path}")
                                        logger.info(f"File exists check: {os.path.exists(after_rename_abs_path)}")
                                        logger.info(f"Original video path for subtitle search: {original_video_path}")
                                        # Use renamed path for video processing
                                        embed_result = embed_subs_to_video(after_rename_abs_path, user_id, tg_update_callback, app=app, message=message)
                                        try:
                                            if embed_result:
                                                app.edit_message_text(
                                                    chat_id=user_id,
                                                    message_id=status_msg.id,
                                                    text="Subtitles successfully embedded! ✅"
                                                )
                                            else:
                                                # Check if there are subtitle files
                                                video_dir = os.path.dirname(after_rename_abs_path)
                                                video_name = os.path.splitext(os.path.basename(after_rename_abs_path))[0]
                                                subs_files = glob.glob(os.path.join(video_dir, f"{video_name}*.srt"))
                                                
                                                if not subs_files:
                                                    app.edit_message_text(
                                                        chat_id=user_id,
                                                        message_id=status_msg.id,
                                                        text="⚠️ Subtitles not found for this video"
                                                    )
                                                else:
                                                    app.edit_message_text(
                                                        chat_id=user_id,
                                                        message_id=status_msg.id,
                                                        text="⚠️ Subtitles not embedded: exceeded size/duration limits"
                                                    )
                                        except Exception as e:
                                            logger.error(f"Failed to update subtitle progress (final): {e}")
                                    else:
                                        app.send_message(user_id, safe_get_messages(user_id).SUBTITLES_CANNOT_EMBED_LIMITS_MSG, reply_parameters=ReplyParameters(message_id=message.id))
                                else:
                                    app.send_message(user_id, safe_get_messages(user_id).SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG, reply_parameters=ReplyParameters(message_id=message.id))
                            
                            # Clean up subtitle files after embedding attempt
                            try:
                                cleanup_subtitle_files(user_id)
                            except Exception as e:
                                logger.error(f"Error cleaning up subtitle files: {e}")
                            
                            # Clear
                            clear_subs_check_cache()
                        
                        # MKV postprocessing: embed all audio tracks and subtitles if needed
                        try:
                            from COMMANDS.format_cmd import get_session_mkv_override
                            from DOWN_AND_UP.always_ask_menu import get_filters
                            
                            session_mkv = get_session_mkv_override(user_id)
                            if session_mkv is None:
                                from COMMANDS.format_cmd import get_user_mkv_preference
                                session_mkv = get_user_mkv_preference(user_id)
                            
                            is_mkv = session_mkv and after_rename_abs_path.lower().endswith('.mkv')
                            
                            if is_mkv:
                                # Get filter state to check if we need to download all tracks
                                try:
                                    filters_state = get_filters(user_id)
                                    logger.info(f"[DEBUG] MKV block: filters_state keys: {list(filters_state.keys())}")
                                    logger.info(f"[DEBUG] MKV block: filters_state selected_subs_langs: {filters_state.get('selected_subs_langs', [])}")
                                    logger.info(f"[DEBUG] MKV block: filters_state subs_all_selected: {filters_state.get('subs_all_selected', False)}")
                                    audio_all_dubs = filters_state.get("audio_all_dubs", False)
                                    selected_audio_langs = filters_state.get("selected_audio_langs", []) or []
                                    selected_subs_langs = filters_state.get("selected_subs_langs", []) or []
                                    subs_all_selected = filters_state.get("subs_all_selected", False)
                                    logger.info(f"[DEBUG] MKV block: extracted selected_subs_langs={selected_subs_langs}, subs_all_selected={subs_all_selected}")
                                except Exception as e:
                                    logger.error(f"[DEBUG] MKV block: error reading filters_state: {e}")
                                    import traceback as tb_module
                                    logger.error(tb_module.format_exc())
                                    audio_all_dubs = False
                                    selected_audio_langs = []
                                    selected_subs_langs = []
                                    subs_all_selected = False
                                
                                video_dir = os.path.dirname(after_rename_abs_path)
                                
                                # Download and embed audio tracks if needed (ALL or selected languages)
                                if audio_all_dubs or selected_audio_langs:
                                    try:
                                        # Download selected audio tracks (ALL or specific languages)
                                        if audio_all_dubs:
                                            logger.info("Downloading ALL available audio tracks for MKV")
                                            status_msg = app.send_message(user_id, "🎵 Downloading all audio tracks...")
                                            available_langs = None  # Download all
                                        else:
                                            logger.info(f"Downloading selected audio tracks for MKV: {selected_audio_langs}")
                                            status_msg = app.send_message(user_id, f"🎵 Downloading {len(selected_audio_langs)} audio tracks...")
                                            available_langs = selected_audio_langs  # Download only selected
                                        
                                        from DOWN_AND_UP.ffmpeg import download_all_audio_tracks, embed_all_audio_tracks_to_mkv
                                        # Find the format that was actually downloaded to get its language
                                        downloaded_format = None
                                        if info_dict and 'formats' in info_dict:
                                            # Try to find format by quality_key if available
                                            if quality_key:
                                                for fmt in info_dict['formats']:
                                                    if fmt.get('format_id') == quality_key:
                                                        downloaded_format = fmt
                                                        break
                                            # If not found, try to find the best video+audio format
                                            if not downloaded_format:
                                                for fmt in info_dict['formats']:
                                                    if fmt.get('vcodec') != 'none' and fmt.get('acodec'):
                                                        downloaded_format = fmt
                                                        break
                                        # Pass selected languages or None for all, and pass info_dict to avoid re-fetching
                                        audio_result = download_all_audio_tracks(url, user_id, video_dir, available_langs=available_langs, use_proxy=use_proxy, info_dict=info_dict, downloaded_format=downloaded_format)
                                        
                                        # Extract tracks and original language from result
                                        if isinstance(audio_result, dict):
                                            audio_tracks = audio_result.get('tracks', [])
                                            original_audio_lang = audio_result.get('original_lang')
                                        else:
                                            # Backward compatibility
                                            audio_tracks = audio_result if audio_result else []
                                            original_audio_lang = None
                                        
                                        if audio_tracks or original_audio_lang:
                                            total_tracks = len(audio_tracks) + (1 if original_audio_lang else 0)
                                            logger.info(f"Embedding {len(audio_tracks)} additional audio tracks + 1 original into MKV")
                                            app.edit_message_text(user_id, status_msg.id, "🎵 Embedding audio tracks into MKV...")
                                            
                                            def audio_update_callback(progress, eta):
                                                try:
                                                    blocks = int(progress * 10)
                                                    bar = '🟩' * blocks + '⬜️' * (10 - blocks)
                                                    percent = int(progress * 100)
                                                    app.edit_message_text(
                                                        chat_id=user_id,
                                                        message_id=status_msg.id,
                                                        text=f"🎵 Embedding audio tracks...\n{bar} {percent}%\nETA: {eta} min"
                                                    )
                                                except Exception:
                                                    pass
                                            
                                            embed_result = embed_all_audio_tracks_to_mkv(
                                                after_rename_abs_path, audio_tracks, user_id,
                                                tg_update_callback=audio_update_callback, app=app, message=message,
                                                original_audio_lang=original_audio_lang
                                            )
                                            
                                            if embed_result:
                                                app.edit_message_text(user_id, status_msg.id, f"✅ All {total_tracks} audio tracks embedded successfully!")
                                            else:
                                                app.edit_message_text(user_id, status_msg.id, "⚠️ Failed to embed some audio tracks")
                                        else:
                                            app.edit_message_text(user_id, status_msg.id, "⚠️ No additional audio tracks found")
                                    except Exception as e:
                                        logger.error(f"Error in audio tracks postprocessing: {e}")
                                        import traceback as tb_module
                                        logger.error(tb_module.format_exc())
                                
                                # Download and embed all subtitles if needed
                                logger.info(f"[DEBUG] MKV subtitle check: subs_all_selected={subs_all_selected}, selected_subs_langs={selected_subs_langs}, type={type(selected_subs_langs)}, len={len(selected_subs_langs) if selected_subs_langs else 0}")
                                if subs_all_selected or selected_subs_langs:
                                    try:
                                        logger.info(f"Downloading all subtitles for MKV: all_selected={subs_all_selected}, langs={selected_subs_langs}")
                                        status_msg = app.send_message(user_id, "💬 Downloading all subtitles...")
                                        
                                        # Get available dubs for ALL_DUBS filtering
                                        available_dubs = filters_state.get("available_dubs", []) or []
                                        
                                        logger.info(f"[DEBUG] Calling download_all_subtitles with: selected_langs={selected_subs_langs}, all_selected={subs_all_selected}, available_dubs={available_dubs}")
                                        from DOWN_AND_UP.ffmpeg import download_all_subtitles
                                        try:
                                            subtitle_tracks = download_all_subtitles(
                                                url, user_id, video_dir,
                                                selected_langs=selected_subs_langs if selected_subs_langs else None,
                                                all_selected=subs_all_selected,
                                                available_dubs=available_dubs if subs_all_selected else None
                                            )
                                            # Ensure subtitle_tracks is a list, not None
                                            if subtitle_tracks is None:
                                                logger.warning("download_all_subtitles returned None, converting to empty list")
                                                subtitle_tracks = []
                                            logger.info(f"[DEBUG] download_all_subtitles returned: {len(subtitle_tracks) if subtitle_tracks else 0} tracks")
                                        except Exception as subs_download_error:
                                            logger.error(f"Error in download_all_subtitles: {subs_download_error}")
                                            import traceback as tb_module
                                            logger.error(tb_module.format_exc())
                                            subtitle_tracks = []
                                            app.edit_message_text(user_id, status_msg.id, "⚠️ Failed to download subtitles")
                                        
                                        if subtitle_tracks:
                                            logger.info(f"Embedding {len(subtitle_tracks)} subtitle tracks into MKV")
                                            app.edit_message_text(user_id, status_msg.id, "💬 Embedding subtitles into MKV...")
                                            
                                            # Use existing embed_subs_to_video function which now supports multiple tracks
                                            # (already imported at the top of the file)
                                            
                                            def subs_update_callback(progress, eta):
                                                try:
                                                    blocks = int(progress * 10)
                                                    bar = '🟩' * blocks + '⬜️' * (10 - blocks)
                                                    percent = int(progress * 100)
                                                    app.edit_message_text(
                                                        chat_id=user_id,
                                                        message_id=status_msg.id,
                                                        text=f"💬 Embedding subtitles...\n{bar} {percent}%\nETA: {eta} min"
                                                    )
                                                except Exception:
                                                    pass
                                            
                                            embed_result = embed_subs_to_video(
                                                after_rename_abs_path, user_id,
                                                tg_update_callback=subs_update_callback, app=app, message=message,
                                                subtitle_tracks=subtitle_tracks
                                            )
                                            
                                            if embed_result:
                                                app.edit_message_text(user_id, status_msg.id, "✅ All subtitles embedded successfully!")
                                            else:
                                                app.edit_message_text(user_id, status_msg.id, "⚠️ Failed to embed some subtitles")
                                            
                                            # Clean up subtitle files
                                            for track in subtitle_tracks:
                                                try:
                                                    if os.path.exists(track['path']):
                                                        os.remove(track['path'])
                                                except Exception:
                                                    pass
                                        else:
                                            app.edit_message_text(user_id, status_msg.id, "⚠️ No subtitles found")
                                    except Exception as e:
                                        logger.error(f"Error in subtitles postprocessing: {e}")
                                        import traceback as tb_module
                                        logger.error(tb_module.format_exc())
                        except Exception as e:
                            logger.error(f"Error in MKV postprocessing: {e}")
                            import traceback as tb_module
                            logger.error(tb_module.format_exc())
                        
                        # NOTE: Do NOT clear Always Ask menu states here!
                        # States are needed for all videos in playlist (if it's a playlist)
                        # States will be cleared at the end of the function after ALL videos are processed
                        
                        video_msg = send_videos(message, after_rename_abs_path, '' if force_no_title else original_video_title, duration, thumb_dir, info_text, proc_msg.id, full_video_title, tags_text_final)
                        if not video_msg:
                            logger.error("send_videos returned None for single video; aborting cache save for this item")
                            continue
                        
                        # Save video message ID for caching purposes
                        last_video_msg_id = video_msg.id
                        
                        #found_type = None
                        try:
                            # Determine the correct log channel based on content type
                            from HELPERS.porn import is_porn
                            # Use metadata from info_dict for proper NSFW detection (especially for VK playlists)
                            video_title_for_check = info_dict.get("title", "") if info_dict else ""
                            video_description_for_check = info_dict.get("description", "") if info_dict else ""
                            video_caption_for_check = info_dict.get("caption", "") if info_dict else ""
                            # Get tags from info_dict and tags_text_final
                            video_tags_for_check = None
                            if info_dict and info_dict.get("tags"):
                                if isinstance(info_dict.get("tags"), list):
                                    video_tags_for_check = ' '.join(str(t) for t in info_dict.get("tags"))
                                else:
                                    video_tags_for_check = str(info_dict.get("tags"))
                            # Also check if #nsfw tag is already in tags_text_final (from generate_final_tags)
                            has_nsfw_tag = "#nsfw" in tags_text_final.lower() if tags_text_final else False
                            # Use metadata for NSFW check
                            is_nsfw_from_metadata = is_porn(url, video_title_for_check, video_description_for_check, video_caption_for_check, tags=video_tags_for_check)
                            is_nsfw = is_nsfw_from_metadata or has_nsfw_tag or user_forced_nsfw
                            logger.info(f"[NSFW_CHECK] is_porn check for {url}: is_porn={is_nsfw_from_metadata}, has_nsfw_tag={has_nsfw_tag}, user_forced_nsfw={user_forced_nsfw}, final is_nsfw={is_nsfw}")
                            logger.info(f"[NSFW_CHECK] title='{video_title_for_check[:100]}', description='{video_description_for_check[:100] if video_description_for_check else ''}', tags='{video_tags_for_check[:100] if video_tags_for_check else ''}'")
                            is_private_chat = getattr(message.chat, "type", None) == enums.ChatType.PRIVATE
                            # Detect if actually sent as paid media
                            try:
                                msg_is_paid = (
                                    getattr(video_msg, "media", None) == enums.MessageMediaType.PAID_MEDIA
                                ) or (getattr(video_msg, "paid_media", None) is not None)
                            except Exception:
                                msg_is_paid = False
                            # Для логирования используем is_nsfw and is_private_chat (без учета админа)
                            # чтобы логирование оставалось как для всех остальных
                            # Важно: используем is_nsfw and is_private_chat, а не msg_is_paid,
                            # так как админы с TURN_OFF_LIMITS_FOR_ADMINS = True получают открытый контент
                            is_paid_for_logging = is_nsfw and is_private_chat
                            # Для отправки пользователю проверяем админа
                            from HELPERS.limitter import should_apply_limits_to_admin
                            is_paid_for_user = is_paid_for_logging and should_apply_limits_to_admin(user_id=user_id, message=message)
                            
                            # Handle different content types according to new logic
                            # Используем is_paid_for_logging для логирования (чтобы логирование было как для всех)
                            if is_paid_for_logging:
                                # For NSFW content in private chat, send_videos already sent paid media to user
                                # Send paid copy to LOGS_PAID_ID and open copy to LOGS_NSFW_ID for history
                                
                                # Send paid copy to LOGS_PAID_ID
                                log_channel_paid = get_log_channel("video", paid=True)
                                try:
                                    # Forward the paid video to LOGS_PAID_ID
                                    safe_forward_messages(log_channel_paid, user_id, [video_msg.id])
                                    logger.info(f"down_and_up: NSFW content paid copy sent to PAID channel")
                                except Exception as e:
                                    logger.error(f"down_and_up: failed to send paid copy to PAID channel: {e}")
                                
                                # Send open copy to LOGS_NSFW_ID for history
                                log_channel_nsfw = get_log_channel("video", nsfw=True)
                                try:
                                    # Get video dimensions for proper aspect ratio
                                    try:
                                        v_w, v_h, v_dur = get_video_info_ffprobe(after_rename_abs_path)
                                    except Exception:
                                        v_w, v_h, v_dur = width, height, duration
                                    
                                    # Create open copy for history (without stars) - send directly to NSFW channel
                                    open_video_msg = app.send_video(
                                        chat_id=log_channel_nsfw,
                                        video=after_rename_abs_path,
                                        caption='' if force_no_title else original_video_title,
                                        duration=int(v_dur) if v_dur else duration,
                                        width=int(v_w) if v_w else width,
                                        height=int(v_h) if v_h else height,
                                        thumb=thumb_dir,
                                        reply_parameters=ReplyParameters(message_id=message.id)
                                    )
                                    logger.info(f"down_and_up: NSFW content open copy sent to NSFW channel for history")
                                    already_forwarded_to_log = True
                                except Exception as e:
                                    logger.error(f"down_and_up: failed to send open copy to NSFW channel: {e}")
                                
                                # Don't cache NSFW content
                                logger.info(f"down_and_up: NSFW content sent to user (paid), PAID channel (paid copy), and NSFW channel (open copy), not cached")
                                forwarded_msgs = None
                                
                            elif is_nsfw:
                                # NSFW content in groups -> LOGS_NSFW_ID only
                                # For split videos, always forward each part to NSFW channel
                                # For playlists, always forward each video to NSFW channel (don't use already_forwarded_to_log)
                                # IMPORTANT: For split videos in playlists, only forward once (split video takes priority)
                                if caption_lst and len(caption_lst) > 1:
                                    # This is a split video - always forward each part (even if it's in a playlist)
                                    log_channel = get_log_channel("video", nsfw=True)
                                    forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                elif is_playlist:
                                    # For playlists (non-split videos), always forward each video to NSFW channel
                                    log_channel = get_log_channel("video", nsfw=True)
                                    forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                elif not already_forwarded_to_log:
                                    already_forwarded_to_log = True  # Set flag BEFORE forward to prevent duplicates
                                    log_channel = get_log_channel("video", nsfw=True)
                                    forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                else:
                                    logger.info("down_and_up: skipping forward to NSFW channel - already forwarded to log")
                                    forwarded_msgs = None
                                # Don't cache NSFW content
                                logger.info(f"down_and_up: NSFW content sent to NSFW channel, not cached")
                            else:
                                # Regular content -> LOGS_VIDEO_ID and cache (but never for paid media)
                                if (
                                    getattr(video_msg, "media", None) == enums.MessageMediaType.PAID_MEDIA
                                ) or (getattr(video_msg, "paid_media", None) is not None):
                                    logger.info("down_and_up: skipping forward to LOGS_VIDEO_ID for paid media")
                                    forwarded_msgs = None
                                elif caption_lst and len(caption_lst) > 1:
                                    # This is a split video - always forward each part
                                    log_channel = get_log_channel("video")
                                    forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                elif is_playlist:
                                    # For playlists, always forward each video to log channel (don't use already_forwarded_to_log)
                                    log_channel = get_log_channel("video")
                                    forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                elif not already_forwarded_to_log:
                                    log_channel = get_log_channel("video")
                                    forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                else:
                                    logger.info("down_and_up: skipping forward to LOGS_VIDEO_ID - already forwarded to log")
                                    forwarded_msgs = None
                            logger.info(f"down_and_up: forwarded_msgs result: {forwarded_msgs}")
                            if forwarded_msgs:
                                logger.info(f"down_and_up: saving to cache with forwarded message IDs: {[m.id for m in forwarded_msgs]}")
                                if is_playlist:
                                    # For playlists, save to playlist cache with video index
                                    current_video_index = current_index
                                    #found_type = check_subs_availability(url, user_id, safe_quality_key, return_type=True)
                                    subs_enabled = is_subs_enabled(user_id)
                                    auto_mode = get_user_subs_auto_mode(user_id)
                                    need_subs = determine_need_subs(subs_enabled, found_type, user_id)
                                    # Check if cache should be disabled due to active functions (TRIM/SUBS/DUBS)
                                    if not should_disable_cache and not need_subs:
                                        # Передаем уникальную ссылку видео для дополнительного кэширования
                                        video_urls_dict = {current_video_index: playlist_video_urls.get(current_video_index)} if current_video_index in playlist_video_urls else None
                                        save_to_playlist_cache(get_clean_playlist_url(url), safe_quality_key, [current_video_index], [m.id for m in forwarded_msgs], original_text=message.text or message.caption or "", video_urls_dict=video_urls_dict)
                                    else:
                                        if should_disable_cache:
                                            logger.info(f"Video not cached due to active functions (TRIM/SUBS/DUBS): TRIM={active_funcs['has_trim']}, SUBS={active_funcs['has_subs']}, DUBS={active_funcs['has_dubs']}")
                                        else:
                                            logger.info("Video with subtitles (subs.txt found) is not cached!")
                                    cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), safe_quality_key, [current_video_index])
                                    logger.info(f"Checking the cache immediately after writing: {cached_check}")
                                    playlist_indices.append(current_video_index)
                                    playlist_msg_ids.extend([m.id for m in forwarded_msgs])
                                else:
                                    # For single videos, save to regular cache
                                    # Only save to cache if subtitles are not needed
                                    if not is_nsfw and not need_subs and not has_dubs:
                                        _save_video_cache_with_logging(url, safe_quality_key, [m.id for m in forwarded_msgs], original_text=message.text or message.caption or "", user_id=user_id, download_sections=download_sections, has_subs=need_subs, has_dubs=has_dubs)
                                    elif is_nsfw:
                                        logger.info("NSFW content not cached")
                                    elif need_subs:
                                        logger.info(f"Video with subtitles is not cached - different users may need different languages")
                            else:
                                # If forwarding failed, try to forward manually and get log channel IDs
                                # For playlists, skip manual forward if we already tried to forward (to avoid duplicates)
                                if is_playlist:
                                    logger.info("down_and_up: forwarding failed for playlist video, but skipping manual forward to avoid duplicates")
                                elif 'already_forwarded_to_log' in locals() and already_forwarded_to_log:
                                    logger.info("down_and_up: already forwarded to log; skipping manual forward duplicate")
                                else:
                                    logger.info(f"down_and_up: forwarding failed, trying manual forward for video: {video_msg.id}")
                                    try:
                                        # Determine the correct log channel based on content type
                                        from HELPERS.porn import is_porn
                                        # Use metadata from info_dict for proper NSFW detection (especially for VK playlists)
                                        video_title_for_check = info_dict.get("title", "") if info_dict else ""
                                        video_description_for_check = info_dict.get("description", "") if info_dict else ""
                                        video_caption_for_check = info_dict.get("caption", "") if info_dict else ""
                                        # Get tags from info_dict and tags_text_final
                                        video_tags_for_check = None
                                        if info_dict and info_dict.get("tags"):
                                            if isinstance(info_dict.get("tags"), list):
                                                video_tags_for_check = ' '.join(str(t) for t in info_dict.get("tags"))
                                            else:
                                                video_tags_for_check = str(info_dict.get("tags"))
                                        # Also check if #nsfw tag is already in tags_text_final (from generate_final_tags)
                                        has_nsfw_tag = "#nsfw" in tags_text_final.lower() if tags_text_final else False
                                        # Use metadata for NSFW check
                                        is_nsfw_from_metadata = is_porn(url, video_title_for_check, video_description_for_check, video_caption_for_check, tags=video_tags_for_check)
                                        is_nsfw = is_nsfw_from_metadata or has_nsfw_tag or user_forced_nsfw
                                        logger.info(f"[NSFW_CHECK] is_porn check for {url}: is_porn={is_nsfw_from_metadata}, has_nsfw_tag={has_nsfw_tag}, user_forced_nsfw={user_forced_nsfw}, final is_nsfw={is_nsfw}")
                                        is_private_chat = getattr(message.chat, "type", None) == enums.ChatType.PRIVATE
                                        try:
                                            msg_is_paid = (
                                                getattr(video_msg, "media", None) == enums.MessageMediaType.PAID_MEDIA
                                            ) or (getattr(video_msg, "paid_media", None) is not None)
                                        except Exception:
                                            msg_is_paid = False
                                        is_paid = msg_is_paid or (is_nsfw and is_private_chat)
                                        
                                        # Handle different content types according to new logic
                                        if is_paid:
                                            # For NSFW content in private chat, send to both channels but don't cache
                                            # For NSFW content in private chat, send_videos already sent paid media to user
                                            # No need to forward to LOGS_PAID_ID as it's already sent
                                            
                                            # Send to LOGS_NSFW_ID (for history) - send open copy, not paid media
                                            # LOGS_PAID_ID and LOGS_NSWF_ID were already handled in the main logic above
                                            # No need to send again in manual forward
                                            
                                            # Don't cache NSFW content
                                            logger.info(f"down_and_up: NSFW content already sent to user (paid), PAID channel (paid copy), and NSFW channel (open copy), not cached (manual)")
                                            forwarded_msgs = None
                                            
                                        elif is_nsfw:
                                            # NSFW content in groups -> LOGS_NSFW_ID only
                                            log_channel = get_log_channel("video", nsfw=True)
                                            try:
                                                safe_forward_messages(log_channel, user_id, [video_msg.id])
                                                logger.info(f"down_and_up: NSFW content sent to NSFW channel (manual)")
                                            except Exception as e:
                                                logger.error(f"down_and_up: failed to forward to NSFW channel (manual): {e}")
                                            
                                            # Don't cache NSFW content
                                            logger.info(f"down_and_up: NSFW content sent to NSFW channel, not cached (manual)")
                                            forwarded_msgs = None
                                            
                                        else:
                                            # Regular content -> LOGS_VIDEO_ID and cache (but never for paid media)
                                            if (
                                                getattr(video_msg, "media", None) == enums.MessageMediaType.PAID_MEDIA
                                            ) or (getattr(video_msg, "paid_media", None) is not None):
                                                logger.info("down_and_up: skipping forward to LOGS_VIDEO_ID for paid media (manual)")
                                                forwarded_msgs = None
                                            elif caption_lst and len(caption_lst) > 1:
                                                # This is a split video - always forward each part
                                                log_channel = get_log_channel("video")
                                                forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                            elif not already_forwarded_to_log:
                                                log_channel = get_log_channel("video")
                                                forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                            else:
                                                logger.info("down_and_up: skipping forward to LOGS_VIDEO_ID - already forwarded to log (manual)")
                                                forwarded_msgs = None
                                        if forwarded_msgs:
                                            logger.info(f"down_and_up: manual forward successful, got IDs: {[m.id for m in forwarded_msgs]}")
                                            if is_playlist:
                                                # For playlists, save to playlist cache with video index
                                                current_video_index = current_index
                                                subs_enabled = is_subs_enabled(user_id)
                                                auto_mode = get_user_subs_auto_mode(user_id)
                                                need_subs = determine_need_subs(subs_enabled, found_type, user_id)
                                                # Check if cache should be disabled due to active functions (TRIM/SUBS/DUBS)
                                                if not should_disable_cache and not need_subs:
                                                    # Передаем уникальную ссылку видео для дополнительного кэширования
                                                    video_urls_dict = {current_video_index: playlist_video_urls.get(current_video_index)} if current_video_index in playlist_video_urls else None
                                                    save_to_playlist_cache(get_clean_playlist_url(url), safe_quality_key, [current_video_index], [m.id for m in forwarded_msgs], original_text=message.text or message.caption or "", video_urls_dict=video_urls_dict)
                                                else:
                                                    if should_disable_cache:
                                                        logger.info(f"Video not cached due to active functions (TRIM/SUBS/DUBS): TRIM={active_funcs['has_trim']}, SUBS={active_funcs['has_subs']}, DUBS={active_funcs['has_dubs']}")
                                                    else:
                                                        logger.info("Video with subtitles (subs.txt found) is not cached!")
                                                cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), safe_quality_key, [current_video_index])
                                                logger.info(f"Checking the cache immediately after writing: {cached_check}")
                                                playlist_indices.append(current_video_index)
                                                playlist_msg_ids.extend([m.id for m in forwarded_msgs])
                                            else:
                                                # For single videos, save to regular cache
                                                # Only save to cache if subtitles are not needed
                                                if not is_nsfw and not need_subs:
                                                    _save_video_cache_with_logging(url, safe_quality_key, [m.id for m in forwarded_msgs], original_text=message.text or message.caption or "", user_id=user_id, download_sections=download_sections, has_subs=need_subs, has_dubs=has_dubs)
                                                elif is_nsfw:
                                                    logger.info("NSFW content not cached (manual)")
                                                elif need_subs:
                                                    logger.info(f"Video with subtitles is not cached (manual) - different users may need different languages")
                                        else:
                                            logger.error("Manual forward also failed, cannot cache video")
                                    except Exception as e:
                                        logger.error(f"Error in manual forward: {e}")
                        except Exception as e:
                            # Check if error is related to quality_key - if so, ignore it completely
                            if "'quality_key'" in str(e):
                                logger.info(f"quality_key error ignored (non-critical): {e}")
                                # Quality_key errors don't affect functionality, just continue
                                
                                # PREVENTIVE FIX: Handle split video completion even after quality_key error
                                if split_msg_ids and not is_playlist:
                                    logger.info(f"PREVENTIVE FIX: Processing split video completion after quality_key error in manual forward: {split_msg_ids}")
                                    actual_video_count = len(split_msg_ids)
                                    success_msg = f"<b>{safe_get_messages(user_id).DOWN_UP_UPLOAD_COMPLETE_MSG}</b> - {actual_video_count} {safe_get_messages(user_id).DOWN_UP_FILES_UPLOADED_MSG}.\n{safe_get_messages(user_id).CREDITS_MSG}"
                                    logger.info(f"PREVENTIVE FIX: sending final success message for split video: {success_msg}")
                                    safe_edit_message_text(user_id, proc_msg_id, success_msg)
                                    send_to_logger(message, safe_get_messages(user_id).VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG)
                
                            else:
                                logger.error(f"Error forwarding video to logger: {e}")
                            # Try to forward manually even after error
                            try:
                                # Safe quality_key for error recovery (already defined at function start)
                                
                                # Determine the correct log channel based on content type
                                from HELPERS.porn import is_porn
                                is_nsfw = is_porn(url, "", "", None) or user_forced_nsfw
                                logger.info(f"[FALLBACK] is_porn check for {url}: {is_porn(url, '', '', None)}, user_forced_nsfw: {user_forced_nsfw}, final is_nsfw: {is_nsfw}")
                                is_private_chat = getattr(message.chat, "type", None) == enums.ChatType.PRIVATE
                                is_paid = is_nsfw and is_private_chat
                                
                                # Handle different content types according to new logic
                                if is_paid:
                                    # For NSFW content in private chat, send_videos already sent paid media to user
                                    # Send paid copy to LOGS_PAID_ID and open copy to LOGS_NSFW_ID for history
                                    
                                    # Send paid copy to LOGS_PAID_ID
                                    log_channel_paid = get_log_channel("video", paid=True)
                                    try:
                                        # Forward the paid video to LOGS_PAID_ID
                                        safe_forward_messages(log_channel_paid, user_id, [video_msg.id])
                                        logger.info(f"down_and_up: NSFW content paid copy sent to PAID channel (error recovery)")
                                    except Exception as e:
                                        logger.error(f"down_and_up: failed to send paid copy to PAID channel (error recovery): {e}")
                                    
                                    # Send open copy to LOGS_NSFW_ID for history
                                    log_channel_nsfw = get_log_channel("video", nsfw=True)
                                    try:
                                        # Get video dimensions for proper aspect ratio
                                        try:
                                            v_w, v_h, v_dur = get_video_info_ffprobe(after_rename_abs_path)
                                        except Exception:
                                            v_w, v_h, v_dur = width, height, duration
                                        
                                        # Create open copy for history (without stars) - send directly to NSFW channel
                                        open_video_msg = app.send_video(
                                            chat_id=log_channel_nsfw,
                                            video=after_rename_abs_path,
                                            caption='' if force_no_title else original_video_title,
                                            duration=int(v_dur) if v_dur else duration,
                                            width=int(v_w) if v_w else width,
                                            height=int(v_h) if v_h else height,
                                            thumb=thumb_dir,
                                            reply_parameters=ReplyParameters(message_id=message.id)
                                        )
                                        logger.info(f"down_and_up: NSFW content open copy sent to NSFW channel for history (error recovery)")
                                        already_forwarded_to_log = True
                                    except Exception as e:
                                        logger.error(f"down_and_up: failed to send open copy to NSFW channel (error recovery): {e}")
                                    
                                    # Don't cache NSFW content
                                    logger.info(f"down_and_up: NSFW content sent to user (paid), PAID channel (paid copy), and NSFW channel (open copy), not cached (error recovery)")
                                    forwarded_msgs = None
                                    
                                elif is_nsfw:
                                    # NSFW content in groups -> LOGS_NSFW_ID only
                                    log_channel = get_log_channel("video", nsfw=True)
                                    try:
                                        safe_forward_messages(log_channel, user_id, [video_msg.id])
                                        logger.info(f"down_and_up: NSFW content sent to NSFW channel (error recovery)")
                                    except Exception as e:
                                        logger.error(f"down_and_up: failed to forward to NSFW channel (error recovery): {e}")
                                    
                                    # Don't cache NSFW content
                                    logger.info(f"down_and_up: NSFW content sent to NSFW channel, not cached (error recovery)")
                                    forwarded_msgs = None
                                    
                                else:
                                    # Regular content -> LOGS_VIDEO_ID and cache
                                    if caption_lst and len(caption_lst) > 1:
                                        # This is a split video - always forward each part
                                        log_channel = get_log_channel("video")
                                        forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                    elif not already_forwarded_to_log:
                                        log_channel = get_log_channel("video")
                                        forwarded_msgs = safe_forward_messages(log_channel, user_id, [video_msg.id])
                                    else:
                                        logger.info("down_and_up: skipping forward to LOGS_VIDEO_ID - already forwarded to log (error recovery)")
                                        forwarded_msgs = None
                                if forwarded_msgs:
                                    logger.info(f"down_and_up: manual forward after error successful, got IDs: {[m.id for m in forwarded_msgs]}")
                                    if is_playlist:
                                        # For playlists, save to playlist cache with video index
                                        current_video_index = current_index
                                        subs_enabled = is_subs_enabled(user_id)
                                        auto_mode = get_user_subs_auto_mode(user_id)
                                        need_subs = determine_need_subs(subs_enabled, found_type, user_id)
                                        # Check if cache should be disabled due to active functions (TRIM/SUBS/DUBS)
                                        if not should_disable_cache and not need_subs:
                                            # Передаем уникальную ссылку видео для дополнительного кэширования
                                            video_urls_dict = {current_video_index: playlist_video_urls.get(current_video_index)} if current_video_index in playlist_video_urls else None
                                            save_to_playlist_cache(get_clean_playlist_url(url), safe_quality_key, [current_video_index], [m.id for m in forwarded_msgs], original_text=message.text or message.caption or "", video_urls_dict=video_urls_dict)
                                        else:
                                            if should_disable_cache:
                                                logger.info(f"Video not cached due to active functions (TRIM/SUBS/DUBS): TRIM={active_funcs['has_trim']}, SUBS={active_funcs['has_subs']}, DUBS={active_funcs['has_dubs']}")
                                            else:
                                                logger.info("Video with subtitles (subs.txt found) is not cached!")
                                        cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), safe_quality_key, [current_video_index])
                                        logger.info(f"Checking the cache immediately after writing: {cached_check}")
                                        playlist_indices.append(current_video_index)
                                        playlist_msg_ids.extend([m.id for m in forwarded_msgs])
                                    else:
                                        # For single videos, save to regular cache
                                        # Only save to cache if subtitles are not needed
                                        if not is_nsfw and not need_subs:
                                            _save_video_cache_with_logging(url, safe_quality_key, [m.id for m in forwarded_msgs], original_text=message.text or message.caption or "", user_id=user_id, download_sections=download_sections, has_subs=need_subs, has_dubs=has_dubs)
                                        elif is_nsfw:
                                            logger.info("NSFW content not cached (error recovery)")
                                        elif need_subs:
                                            logger.info(f"Video with subtitles is not cached (error recovery) - different users may need different languages")
                                else:
                                    logger.error("Manual forward after error also failed, cannot cache video")
                            except Exception as e2:
                                # Check if error is related to quality_key - if so, ignore it completely
                                if "'quality_key'" in str(e2):
                                    logger.info(f"quality_key error ignored (non-critical): {e2}")
                                    # Quality_key errors don't affect functionality, just continue
                                    
                                    # PREVENTIVE FIX: Handle split video completion even after quality_key error
                                    if split_msg_ids and not is_playlist:
                                        logger.info(f"PREVENTIVE FIX: Processing split video completion after quality_key error in manual forward after error: {split_msg_ids}")
                                        actual_video_count = len(split_msg_ids)
                                        success_msg = f"<b>{safe_get_messages(user_id).DOWN_UP_UPLOAD_COMPLETE_MSG}</b> - {actual_video_count} {safe_get_messages(user_id).DOWN_UP_FILES_UPLOADED_MSG}.\n{safe_get_messages(user_id).CREDITS_MSG}"
                                        logger.info(f"PREVENTIVE FIX: sending final success message for split video: {success_msg}")
                                        safe_edit_message_text(user_id, proc_msg_id, success_msg)
                                        send_to_logger(message, safe_get_messages(user_id).VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG)
                # end-of-task subs cache clearing handled in unified success branches below
                                else:
                                    logger.error(f"Error in manual forward after error: {e2}")
                        safe_edit_message_text(user_id, proc_msg_id,
                            f"{info_text}\n{full_bar}   100.0%\n<b>{safe_get_messages(user_id).DOWN_UP_VIDEO_DURATION_MSG}</b> <i>{TimeFormatter(duration * 1000)}</i>\n{safe_get_messages(user_id).DOWN_UP_ONE_FILE_UPLOADED_MSG}")
                        send_mediainfo_if_enabled(user_id, after_rename_abs_path, message)
                        
                        # Clean up video file and thumbnail
                        if os.path.exists(after_rename_abs_path):
                            os.remove(after_rename_abs_path)
                        if thumb_dir and os.path.exists(thumb_dir):
                            os.remove(thumb_dir)
                        pass
                    except Exception as e:
                        logger.error(f"Error sending video: {e}")
                        import traceback as tb_module
                        logger.error(tb_module.format_exc())
                        send_error_to_user(message, safe_get_messages(user_id).ERROR_SENDING_VIDEO_MSG.format(error=str(e)))
                        continue
        if successful_uploads == len(indices_to_download):
            success_msg = f"<b>{safe_get_messages(user_id).DOWN_UP_UPLOAD_COMPLETE_MSG}</b> - {video_count} {safe_get_messages(user_id).DOWN_UP_FILES_UPLOADED_MSG}.\n{safe_get_messages(user_id).CREDITS_MSG}"
            safe_edit_message_text(user_id, proc_msg_id, success_msg)
            send_to_logger(message, success_msg)
            try:
                from COMMANDS.subtitles_cmd import clear_subs_cache_for
                from DOWN_AND_UP.always_ask_menu import delete_subs_langs_cache
                delete_subs_langs_cache(user_id, url)
                cleared = clear_subs_cache_for(user_id, url)
                logger.info(f"[SUBS] End of task: cleared {cleared} subtitle cache entries for user={user_id}")
            except Exception as _e:
                logger.debug(f"[SUBS] Failed to clear end cache: {_e}")
            
            # Clean up download subdirectory after successful upload
            try:
                from DOWN_AND_UP.always_ask_menu import get_user_download_dir
                download_dir = get_user_download_dir(user_id)
                if download_dir and os.path.exists(download_dir):
                    logger.info(f"Cleaning up download subdirectory after successful upload: {download_dir}")
                    import shutil
                    shutil.rmtree(download_dir)
                    logger.info(f"Successfully removed download subdirectory: {download_dir}")
            except Exception as cleanup_error:
                logger.error(f"Error cleaning up download subdirectory for user {user_id}: {cleanup_error}")

        if is_playlist and safe_quality_key:
            total_sent = len(cached_videos) + successful_uploads
            app.send_message(user_id, safe_get_messages(user_id).PLAYLIST_VIDEOS_SENT_MSG.format(sent=total_sent, total=len(requested_indices)), reply_parameters=ReplyParameters(message_id=message.id))
            send_to_logger(message, safe_get_messages(user_id).PLAYLIST_VIDEOS_SENT_LOG_MSG.format(sent=total_sent, total=len(requested_indices), quality=safe_quality_key, user_id=user_id))

    except Exception as e:
        import traceback as tb_module
        error_traceback = tb_module.format_exc()
        logger.error(f"Exception caught in down_and_up: type={type(e)}, value={e}, traceback:\n{error_traceback}")
        
        if e is None:
            logger.error("CRITICAL: Exception object is None! This should never happen.")
            error_msg = "Unknown error (exception was None)"
        elif "Download timeout exceeded" in str(e):
            send_to_user(message, safe_get_messages(user_id).DOWNLOAD_CANCELLED_TIMEOUT_MSG)
            log_error_to_channel(message, LoggerMsg.DOWNLOAD_TIMEOUT_LOG, url)
        elif "'quality_key'" in str(e):
            # Quality_key errors are non-critical and should be completely ignored
            logger.info(f"quality_key error ignored (non-critical): {e}")
            # Quality_key errors don't affect functionality, just continue normally
            
            # HARD FIX: Handle split videos completion even after quality_key error
            if split_msg_ids and not is_playlist:
                logger.info(f"HARD FIX: Processing split video completion after quality_key error: {split_msg_ids}")
                actual_video_count = len(split_msg_ids)
                success_msg = f"<b>{safe_get_messages(user_id).DOWN_UP_UPLOAD_COMPLETE_MSG}</b> - {actual_video_count} {safe_get_messages(user_id).DOWN_UP_FILES_UPLOADED_MSG}.\n{safe_get_messages(user_id).CREDITS_MSG}"
                logger.info(f"HARD FIX: sending final success message for split video: {success_msg}")
                safe_edit_message_text(user_id, proc_msg_id, success_msg)
                send_to_logger(message, safe_get_messages(user_id).VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG)
                try:
                    from COMMANDS.subtitles_cmd import clear_subs_cache_for
                    from DOWN_AND_UP.always_ask_menu import delete_subs_langs_cache
                    delete_subs_langs_cache(user_id, url)
                    cleared = clear_subs_cache_for(user_id, url)
                    logger.info(f"[SUBS] End of task: cleared {cleared} subtitle cache entries for user={user_id}")
                except Exception as _e:
                    logger.debug(f"[SUBS] Failed to clear end cache: {_e}")
        else:
            logger.error(f"Error in video download: {e}")
            error_msg = str(e) if e else "Unknown error"
            send_to_user(message, safe_get_messages(user_id).FAILED_DOWNLOAD_VIDEO_MSG.format(error=error_msg))
        
        # Immediate cleanup of temporary status messages on error
        try:
            if status_msg_id:
                safe_delete_messages(chat_id=user_id, message_ids=[status_msg_id], revoke=True)
            if hourglass_msg_id:
                safe_delete_messages(chat_id=user_id, message_ids=[hourglass_msg_id], revoke=True)
            if download_started_msg_id:
                safe_delete_messages(chat_id=user_id, message_ids=[download_started_msg_id], revoke=True)
            stop_anim.set()
        except Exception:
            pass
        
        # Clean up temporary files on error
        try:
            cleanup_user_temp_files(user_id)
        except Exception as cleanup_error:
            logger.error(f"Error cleaning up temp files after error for user {user_id}: {cleanup_error}")
    finally:
        # Always stop hourglass animation to prevent resource leaks
        try:
            stop_anim.set()
            if anim_thread:
                anim_thread.join(timeout=1)  # Wait for animation thread with timeout
        except Exception as e:
            logger.error(f"Error stopping hourglass animation: {e}")
        
        set_active_download(user_id, False)
        clear_download_start_time(user_id)  # Clear the download start time
        if playlist_name:
            with playlist_errors_lock:
                error_key = f"{user_id}_{playlist_name}"
                if error_key in playlist_errors:
                    del playlist_errors[error_key]

        # Clean up temporary files
        try:
            cleanup_user_temp_files(user_id)
        except Exception as e:
            logger.error(f"Error cleaning up temp files for user {user_id}: {e}")

        try:
            if status_msg_id:
                safe_delete_messages(chat_id=user_id, message_ids=[status_msg_id], revoke=True)
            if hourglass_msg_id:
                safe_delete_messages(chat_id=user_id, message_ids=[hourglass_msg_id], revoke=True)
        except Exception as e:
            logger.error(f"Error deleting status messages: {e}")
        # Also try to delete the 'Download started' message if it still exists
        try:
            if download_started_msg_id:
                safe_delete_messages(chat_id=user_id, message_ids=[download_started_msg_id], revoke=True)
        except Exception:
            pass

        # --- ADDED: summary of cache after cycle ---
        if is_playlist and playlist_indices and playlist_msg_ids:
            #found_type = check_subs_availability(url, user_id, safe_quality_key, return_type=True)
            subs_enabled = is_subs_enabled(user_id)
            auto_mode = get_user_subs_auto_mode(user_id)
            need_subs = determine_need_subs(subs_enabled, found_type, user_id)
            # Check if cache should be disabled due to active functions (TRIM/SUBS/DUBS)
            if not should_disable_cache and not need_subs:
                # Передаем все уникальные ссылки видео для дополнительного кэширования
                save_to_playlist_cache(get_clean_playlist_url(url), safe_quality_key, playlist_indices, playlist_msg_ids, original_text=message.text or message.caption or "", video_urls_dict=playlist_video_urls if playlist_video_urls else None)
            else:
                if should_disable_cache:
                    logger.info(f"Playlist not cached due to active functions (TRIM/SUBS/DUBS): TRIM={active_funcs['has_trim']}, SUBS={active_funcs['has_subs']}, DUBS={active_funcs['has_dubs']}")
                else:
                    logger.info("Video with subtitles (subs.txt found) is not cached!")
            cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), safe_quality_key, playlist_indices)
            summary = "\n".join([f"Index {idx}: msg_id={cached_check.get(idx, '-')}" for idx in playlist_indices])
            logger.info(f"[SUMMARY] Playlist cache (quality {safe_quality_key}):\n{summary}")
        
        # Clear Always Ask menu states (TRIM, SUBS, DUBS) at the end of function
        # This ensures states are cleared after all postprocessing (including MKV embedding) is complete
        try:
            from DOWN_AND_UP.always_ask_menu import clear_all_ask_menu_states
            clear_all_ask_menu_states(user_id)
        except Exception as e:
            logger.error(f"Failed to clear Always Ask menu states at end of function: {e}")

#########################################
