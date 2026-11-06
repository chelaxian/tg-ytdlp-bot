import os
import json
import time
import threading

def encode_playlist_cache_index(index: int) -> str:
    """Encode playlist index for cache storage (uses real positive indices)."""
    # Убрана логика с префиксом 1000 для отрицательных индексов
    # Теперь отрицательные индексы преобразуются в положительные перед сохранением в кэш
    try:
        idx = int(index)
        # Используем реальный индекс (уже преобразованный в положительный)
        return str(idx)
    except (TypeError, ValueError):
        return str(index)
import re
from datetime import datetime, timedelta
from urllib.parse import urlparse
from CONFIG.config import Config
from CONFIG.messages import Messages, safe_get_messages
from CONFIG.logger_msg import LoggerMsg
from HELPERS.app_instance import get_app
from HELPERS.logger import logger, send_to_user, send_to_logger

from DATABASE.firebase_init import db
# NOTE: To avoid circular imports during module load, import URL_PARSERS modules lazily inside functions.
from HELPERS.qualifier import ceil_to_popular
from DATABASE.firebase_init import db_child_by_path
from DATABASE.download_firebase import download_firebase_dump
from DATABASE.db_mode import active_engine, is_firebase, is_json, is_sql

# Get app instance
app = get_app()


def _normalize_playlist_urls(playlist_url: str) -> list:
    """Normalize a playlist URL into all variant forms for cache lookup.
    Returns a deduplicated list of normalized URLs (original + short/long for YouTube).
    """
    from URL_PARSERS.normalizer import normalize_url_for_cache, strip_range_from_url
    from URL_PARSERS.youtube import is_youtube_url, youtube_to_short_url, youtube_to_long_url

    urls = [normalize_url_for_cache(strip_range_from_url(playlist_url))]
    if is_youtube_url(playlist_url):
        urls.extend([
            normalize_url_for_cache(strip_range_from_url(youtube_to_short_url(playlist_url))),
            normalize_url_for_cache(strip_range_from_url(youtube_to_long_url(playlist_url))),
        ])
    return urls


def _expand_quality_keys(quality_key: str) -> list:
    """Return [quality_key] plus a rounded variant if different (e.g. '721p' -> ['721p', '1080p']).
    A dub suffix is kept: '721p@de-DE' -> ['721p@de-DE', '1080p@de-DE']."""
    quality_keys = [quality_key]
    try:
        base, lang = split_dub_cache_key(quality_key)
        if base.endswith('p'):
            h = int(base[:-1])
            rounded = f"{ceil_to_popular(h)}p"
            if rounded != base:
                quality_keys.append(dub_cache_key(rounded, lang))
    except Exception:
        pass
    return quality_keys


# Alternative audio tracks (DUBS). A video downloaded with a dubbed audio track
# is cached under "<quality>@<lang>" ("720p@en-US"); the plain key ("720p")
# always means the default/original audio. Only the keys whose download applies
# the audio-language filter ([language^=<lang>], see askq_callback_logic) get the
# suffix: "best" and "<height>p". mp3 is always the default audio ("ba").
DUB_KEY_SEP = "@"
_DUB_QUALITY_RE = re.compile(r"^(best|\d+p)$")
_DUB_LANG_FILTER_RE = re.compile(r"\[language\^=([^\]]+)\]")


def _clean_dub_lang(audio_lang):
    if not audio_lang or str(audio_lang).upper() in ("ALL", "OFF"):
        return None
    lang = re.sub(r"[^A-Za-z0-9_-]", "", str(audio_lang))
    return lang or None


def dub_cache_key(quality_key, audio_lang):
    """Cache key of quality_key downloaded with audio track audio_lang (None = default audio)."""
    lang = _clean_dub_lang(audio_lang)
    if not quality_key or not lang or not _DUB_QUALITY_RE.match(str(quality_key)):
        return quality_key
    return f"{quality_key}{DUB_KEY_SEP}{lang}"


def split_dub_cache_key(key):
    """'720p@en-US' -> ('720p', 'en-US'); '720p' -> ('720p', None)."""
    key = str(key)
    base, sep, lang = key.partition(DUB_KEY_SEP)
    if sep and lang and _DUB_QUALITY_RE.match(base):
        return base, lang
    return key, None


def audio_lang_from_format(format_spec):
    """Audio language a yt-dlp format string selects ("...+ba[language^=de]..." -> "de")."""
    m = _DUB_LANG_FILTER_RE.search(str(format_spec or ""))
    return m.group(1) if m else None


def qualities_for_audio(keys, audio_lang) -> set:
    """Cached quality keys usable for the given audio track, with the dub suffix removed:
    with a dub selected only "<q>@<lang>" entries count for best/<N>p (other keys,
    e.g. mp3, are not dub-specific); without one only plain entries count."""
    out = set()
    for key in keys or ():
        base, lang = split_dub_cache_key(key)
        if dub_cache_key(base, audio_lang) == key:
            out.add(base)
    return out

# Global variable for local cache Firebase
firebase_cache = {}
# True once firebase_cache holds dump.json: LocalDBAdapter then writes through it
_mirror_loaded = False

# Auto-reload flags and state
auto_cache_enabled = getattr(Config, 'AUTO_CACHE_RELOAD_ENABLED', True)
auto_cache_thread = None
reload_interval_hours = getattr(Config, 'RELOAD_CACHE_EVERY', 4)
_thread_lock = threading.RLock()

###################################################

def _sync_local_cache_to_file():
    """Синхронизирует локальный кэш с файлом (используется при USE_FIREBASE=False)."""
    global firebase_cache
    if is_json():
        # Atomic write (tmp + os.replace): the dump is read concurrently by
        # stats_collector / the dashboard, and a plain open('w') exposed a
        # truncated file to them (or left one behind on Errno 122) (issue #316).
        from HELPERS.atomic_io import atomic_write_json
        cache_file = getattr(Config, 'FIREBASE_CACHE_FILE', 'dump.json')
        for attempt in (1, 2):
            try:
                with _thread_lock:
                    atomic_write_json(cache_file, firebase_cache, ensure_ascii=False, indent=2)
                break
            except RuntimeError as e:
                # "dictionary changed size during iteration": a writer that does
                # not hold _thread_lock mutated the cache; retry once.
                if attempt == 2:
                    logger.error(f"Ошибка синхронизации локального кэша: {e}")
            except (OSError, TypeError, ValueError) as e:
                logger.error(f"Ошибка синхронизации локального кэша: {e}")
                break

def get_from_local_cache(path_parts):
    """
    Receives data from a local cache along the way, divided into parts
    For example: get_from_local_cache (['Bot', 'Video_cache', 'Hash123', '720p'])
    """
    global firebase_cache
    if is_sql():
        # SQLite/PostgreSQL are always current: read the store, not a dump copy
        from DATABASE.firebase_init import get_sql_store
        try:
            value = get_sql_store().get(list(path_parts))
        except Exception as e:
            logger.error(f"DB read {'/'.join(map(str, path_parts))} failed: {type(e).__name__}: {e}")
            value = None
        log_firebase_access_attempt(path_parts, success=value is not None)
        return value
    current = firebase_cache
    for part in path_parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            log_firebase_access_attempt(path_parts, success=False)
            return None
    
    log_firebase_access_attempt(path_parts, success=True)
    return current

def log_firebase_access_attempt(path_parts, success=True):
    """
    Logs attempts to turn to a local cache (to track the remaining .get () calls)
    """
    # Show the path in JSON format for local cache
    path_str = ' -> '.join(path_parts)  # For example: "bot -> video_cache -> playlists -> url_hash -> quality"
    status = "SUCCESS" if success else "MISS"
    try:
        logger.debug(LoggerMsg.DB_FIREBASE_CACHE_ACCESS_LOG_MSG.format(path=path_str, status=status))
    except Exception:
        pass

def load_firebase_cache():
    messages = safe_get_messages(None)
    """Load local Firebase cache from JSON file."""
    global firebase_cache, _mirror_loaded
    if is_sql():
        firebase_cache = {}
        print(f"ℹ️ Database engine {active_engine()}: data is read from the database, no dump to load")
        return
    try:
        cache_file = getattr(Config, 'FIREBASE_CACHE_FILE', 'dump.json')
        use_firebase = getattr(Config, 'USE_FIREBASE', True)
        if os.path.exists(cache_file):
            with open(cache_file, "r", encoding="utf-8") as f:
                firebase_cache = json.load(f)
            if use_firebase:
                print(safe_get_messages().DB_FIREBASE_CACHE_LOADED_MSG.format(count=len(firebase_cache)))
            else:
                print(f"✅ Локальный кэш загружен из {cache_file} ({len(firebase_cache)} записей)")
        else:
            if use_firebase:
                print(safe_get_messages().DB_FIREBASE_CACHE_NOT_FOUND_MSG.format(cache_file=cache_file))
            else:
                print(f"ℹ️ Локальный кэш не найден, создан новый файл: {cache_file}")
            firebase_cache = {}
        # not on a read error: an empty mirror would then overwrite the file
        _mirror_loaded = True
    except Exception as e:
        use_firebase = getattr(Config, 'USE_FIREBASE', True)
        if use_firebase:
            print(safe_get_messages().DB_FAILED_LOAD_FIREBASE_CACHE_MSG.format(error=e))
        else:
            print(f"⚠️ Ошибка загрузки локального кэша: {e}")
        firebase_cache = {}

def reload_firebase_cache():
    messages = safe_get_messages(None)
    """Reloading the local Firebase cache from JSON file"""
    global firebase_cache
    if is_sql():
        return True
    try:
        cache_file = getattr(Config, 'FIREBASE_CACHE_FILE', 'firebase_cache.json')
        if os.path.exists(cache_file):
            with open(cache_file, "r", encoding="utf-8") as f:
                firebase_cache = json.load(f)
            print(safe_get_messages().DB_FIREBASE_CACHE_RELOADED_MSG.format(count=len(firebase_cache)))
            return True
        else:
            print(safe_get_messages().DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG.format(cache_file=cache_file))
            return False
    except Exception as e:
        print(safe_get_messages().DB_FAILED_RELOAD_FIREBASE_CACHE_MSG.format(error=e))
        return False


def get_next_reload_time(interval_hours: int) -> datetime:
    """
    Returns Datetime the following reloading point,
    aligned according to the N-hour step from 00:00.
    """
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds_since_midnight = (now - midnight).total_seconds()
    interval_seconds = max(1, interval_hours) * 3600
    intervals_passed = int(seconds_since_midnight // interval_seconds)
    return midnight + timedelta(seconds=(intervals_passed + 1) * interval_seconds)

def _download_and_reload_cache() -> bool:
    """Download dump via REST and reload local JSON into memory."""
    messages = safe_get_messages(None)
    try:
        ok = download_firebase_dump()
        if not ok:
            print(safe_get_messages().DB_FAILED_DOWNLOAD_DUMP_REST_MSG)
            return False
        return reload_firebase_cache()
    except Exception as e:
        print(safe_get_messages().DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG.format(error=e))
        return False

def auto_reload_firebase_cache():
    messages = safe_get_messages(None)
    """Background thread that reloads local cache every N hours by downloading dump first."""
    global auto_cache_enabled
    
    # Dump download/reload only makes sense for Firebase (quota-limited copy)
    if not is_firebase():
        print("ℹ️ Автоматическая перезагрузка кэша отключена в локальном режиме")
        return

    while auto_cache_enabled:
        interval_hours_local = max(1, int(reload_interval_hours))
        next_exec = get_next_reload_time(interval_hours_local)
        now = datetime.now()
        wait_seconds = (next_exec - now).total_seconds()
        if wait_seconds and wait_seconds < 0:
            wait_seconds = 0
        print(
            f"⏳ Waiting until {next_exec.strftime('%Y-%m-%d %H:%M:%S')} "
            f"to refresh Firebase cache (every {interval_hours_local}h; wait {wait_seconds/3600:.2f}h)"
        )
        # Smart sleep with 1-second granularity, allowing dynamic interval changes or stop
        end_time = time.time() + wait_seconds
        while auto_cache_enabled and time.time() < end_time:
            time.sleep(min(1, end_time - time.time()))
            # If interval changed dynamically, break early to recalc next_exec
            if interval_hours_local != max(1, int(reload_interval_hours)):
                break
        if not auto_cache_enabled:
            print("🛑 Auto Firebase cache reloader stopped by admin")
            return
        if interval_hours_local != max(1, int(reload_interval_hours)):
            # Interval changed; recompute loop without running job
            continue
        # Run the refresh by triggering /reload_cache command as admin
        max_retries = 3
        retry_delay = 60  # 1 minute between retries
        
        for attempt in range(max_retries):
            try:
                print(f"🔄 Triggering /reload_cache as admin (attempt {attempt + 1}/{max_retries})...")
                # Get first admin ID
                admin_id = Config.ADMIN[0] if isinstance(Config.ADMIN, (list, tuple)) else Config.ADMIN
                print(f"🔄 Triggering /reload_cache as admin (user_id={admin_id})")
                
                # Create fake message and run command
                from types import SimpleNamespace
                msg = SimpleNamespace()
                msg.chat = SimpleNamespace()
                msg.chat.id = admin_id
                msg.chat.first_name = "Admin"
                msg.text = "/reload_cache"
                msg.first_name = msg.chat.first_name
                msg.reply_to_message = None
                msg.id = 0
                msg.from_user = SimpleNamespace()
                msg.from_user.id = admin_id
                msg.from_user.first_name = msg.chat.first_name
                # Mark as fake message for proper handling
                msg._is_fake_message = True
                
                # Import and run the command handler
                from COMMANDS.admin_cmd import reload_firebase_cache_command
                reload_firebase_cache_command(get_app(), msg)
                
                print("✅ Auto /reload_cache command executed successfully!")
                break  # Success, exit retry loop
                
            except Exception as e:
                print(safe_get_messages().DB_ERROR_RUNNING_AUTO_RELOAD_MSG.format(attempt=attempt + 1, max_retries=max_retries, error=e))
                if attempt and attempt < max_retries - 1:
                    print(f"⏳ Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    print(safe_get_messages().DB_ALL_RETRY_ATTEMPTS_FAILED_MSG)
                    import traceback; traceback.print_exc()

def start_auto_cache_reloader():
    """Start the auto-reload background thread (idempotent)."""
    global auto_cache_thread, auto_cache_enabled
    with _thread_lock:
        # Check if thread is already running
        if auto_cache_thread is not None and auto_cache_thread.is_alive():
            print("🔄 Auto Firebase cache reloader is already running")
            return auto_cache_thread
            
        if auto_cache_enabled:
            auto_cache_thread = threading.Thread(
                target=auto_reload_firebase_cache,
                daemon=True
            )
            auto_cache_thread.start()
            print(
                f"🚀 Auto Firebase cache reloader started "
                f"(every {max(1, int(reload_interval_hours))}h from 00:00)"
            )
    return auto_cache_thread

def stop_auto_cache_reloader():
    """Stop the auto-reload background thread."""
    global auto_cache_enabled, auto_cache_thread
    with _thread_lock:
        auto_cache_enabled = False
        if auto_cache_thread and auto_cache_thread.is_alive():
            print("🛑 Auto Firebase cache reloader stopping...")
        auto_cache_thread = None

def set_auto_cache_enabled(enabled: bool):
    """Enable/disable auto cache reloader safely."""
    global auto_cache_enabled
    with _thread_lock:
        auto_cache_enabled = bool(enabled)
        if auto_cache_enabled:
            start_auto_cache_reloader()
        else:
            stop_auto_cache_reloader()

def _persist_reload_interval_in_config(new_hours: int) -> bool:
    """Write RELOAD_CACHE_EVERY = <new_hours> back to CONFIG/config.py.
    Keeps formatting/comments around the assignment line intact where possible.
    Also repairs previously corrupted lines if found.
    """
    messages = safe_get_messages(None)
    try:
        cfg_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'CONFIG', 'config.py')
        if not os.path.exists(cfg_path):
            logger.warning(LoggerMsg.DB_CONFIG_NOT_FOUND_LOG_MSG.format(path=cfg_path))
            return False
        with open(cfg_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 1) Repair accidentally corrupted backreference artifacts
        #    e.g. a line like: \g<1>4\g<3>
        content = re.sub(r"^\\g<1>\d+\\g<3>\s*$", "", content, flags=re.MULTILINE)

        # 2) Replace existing assignment, preserving prefix/suffix
        pattern = re.compile(r"^(\s*RELOAD_CACHE_EVERY\s*=\s*)(\d+)(\s*(#.*)?)$", re.MULTILINE)
        def _repl(m: re.Match) -> str:
            return f"{m.group(1)}{int(new_hours)}{m.group(3)}"
        new_content, n_sub = pattern.subn(_repl, content)

        if n_sub == 0:
            # Append new assignment if not present
            new_content = content.rstrip() + f"\nRELOAD_CACHE_EVERY = {int(new_hours)}  # in hours\n"

        with open(cfg_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        logger.info(safe_get_messages().DB_RELOAD_CACHE_EVERY_PERSISTED_MSG.format(hours=int(new_hours)))
        return True
    except Exception as e:
        logger.error(LoggerMsg.DB_FAILED_PERSIST_RELOAD_CACHE_EVERY_LOG_MSG.format(error=e))
        return False

def set_reload_interval_hours(new_hours: int) -> bool:
    """Set a new reload interval in hours (1..168). Restarts the reloader if needed and persists to config.py."""
    global reload_interval_hours, auto_cache_enabled
    try:
        new_val = int(new_hours)
    except Exception:
        return False
    if new_val is None or new_val < 1 or new_val > 168:
        return False
    with _thread_lock:
        reload_interval_hours = new_val
        # Update in-memory Config for consistency
        try:
            setattr(Config, 'RELOAD_CACHE_EVERY', new_val)
        except Exception:
            pass
        # Persist to CONFIG/config.py
        _persist_reload_interval_in_config(new_val)
        # Restart thread if running so new interval applies immediately
        running = auto_cache_enabled
        if running:
            stop_auto_cache_reloader()
            # preserve enabled state and start again
            auto_cache_enabled = True
            start_auto_cache_reloader()
    return True

def close_all_firebase_connections():
    """Close all Firebase connections to prevent file descriptor leaks"""
    try:
        from DATABASE.firebase_init import db
        if hasattr(db, 'close'):
            db.close()
            print("✅ Firebase connections closed successfully")
    except Exception as e:
        print(f"❌ Error closing Firebase connections: {e}")

def toggle_auto_cache_reloader():
    """Toggle auto-reload mode, returns new state (True/False)."""
    global auto_cache_enabled
    with _thread_lock:
        auto_cache_enabled = not auto_cache_enabled
        if auto_cache_enabled:
            start_auto_cache_reloader()
        else:
            stop_auto_cache_reloader()
        return auto_cache_enabled

# Load cache on module import
load_firebase_cache()

# ================= /auto_cache command =================

def auto_cache_command(app, message):
    messages = safe_get_messages(message.chat.id)
    """Command handler to control automatic Firebase cache loading.

    Supports:
      /auto_cache on
      /auto_cache off
      /auto_cache N   (N in 1..168 hours)
    """
    try:
        if int(message.chat.id) not in Config.ADMIN:
            send_to_user(message, safe_get_messages().DB_AUTO_CACHE_ACCESS_DENIED_MSG)
            return

        text = (message.text or "").strip()
        parts = text.split()
        arg = parts[1].lower() if len(parts) > 1 else None

        if arg in ("on", "off"):
            enable = arg == "on"
            set_auto_cache_enabled(enable)
            status = "✅ ENABLED" if enable else "❌ DISABLED"
            if enable:
                interval = max(1, int(reload_interval_hours))
                next_exec = get_next_reload_time(interval)
                delta_min = int((next_exec - datetime.now()).total_seconds() // 60)
                send_to_user(
                    message,
                    safe_get_messages().DB_AUTO_CACHE_RELOADING_UPDATED_MSG.format(
                        status=status,
                        interval=interval,
                        next_exec=next_exec.strftime('%H:%M'),
                        delta_min=delta_min
                    )
                )
                send_to_logger(message, safe_get_messages().DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG.format(next_exec=next_exec))
            else:
                send_to_user(message, safe_get_messages().DB_AUTO_CACHE_RELOADING_STOPPED_MSG)
                send_to_logger(message, safe_get_messages().DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG)
            return

        # Try numeric interval
        if arg is not None:
            try:
                n = int(arg)
            except Exception:
                send_to_user(message, safe_get_messages().DB_AUTO_CACHE_INVALID_ARGUMENT_MSG)
                return
            if n is None or n < 1 or n > 168:
                send_to_user(message, safe_get_messages().DB_AUTO_CACHE_INTERVAL_RANGE_MSG)
                return
            ok = set_reload_interval_hours(n)
            if not ok:
                send_to_user(message, safe_get_messages().DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG)
                return
            interval = max(1, int(reload_interval_hours))
            next_exec = get_next_reload_time(interval)
            delta_min = int((next_exec - datetime.now()).total_seconds() // 60)
            send_to_user(
                message,
                safe_get_messages().DB_AUTO_CACHE_INTERVAL_UPDATED_MSG.format(
                    status='✅ ENABLED' if auto_cache_enabled else '❌ DISABLED',
                    interval=interval,
                    next_exec=next_exec.strftime('%H:%M'),
                    delta_min=delta_min
                )
            )
            send_to_logger(message, safe_get_messages().DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG.format(interval=interval, next_exec=next_exec))
            return

        # No args: toggle legacy behavior
        new_state = toggle_auto_cache_reloader()
        interval = max(1, int(reload_interval_hours))
        if new_state:
            next_exec = get_next_reload_time(interval)
            delta_min = int((next_exec - datetime.now()).total_seconds() // 60)
            send_to_user(
                message,
                safe_get_messages().DB_AUTO_CACHE_RELOADING_STARTED_MSG.format(
                    interval=interval,
                    next_exec=next_exec.strftime('%H:%M'),
                    delta_min=delta_min
                )
            )
            send_to_logger(message, safe_get_messages().DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG.format(next_exec=next_exec))
        else:
            send_to_user(message, safe_get_messages().DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG)
            send_to_logger(message, safe_get_messages().DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG)
    except Exception as e:
        logger.error(LoggerMsg.DB_AUTO_CACHE_HANDLER_ERROR_LOG_MSG.format(error=e))


# ================= media cache (video / playlist / image) =================
#
# Layout (same in Firebase, dump.json and SQL):
#   bot/video_cache/<url_hash>/<quality>            -> "id" or "id,id,..." (split video)
#   bot/video_cache/playlists/<url_hash>/<quality>/<index> -> "id" or "id,id,..."
#   bot/video_cache/images/<url_hash>/<post_index>  -> "id,id,..."
# message ids point at the regular video log channel.
#
# Reads go through _read_node(): one read per URL hash node (all qualities at
# once), memoized for a few seconds, so building a quality menu costs a few
# reads instead of one per quality and URL variant. Writes go through
# _write_values(): one SQL transaction / one dump.json rewrite per save.

_MEMO_TTL = 5.0
_MEMO_MAX = 512
_memo = {}
_memo_lock = threading.Lock()


def invalidate_media_cache_memo():
    """Forget memoized cache nodes (call after writing the cache outside this module)."""
    with _memo_lock:
        _memo.clear()


def _read_node(path_parts):
    """Value of a cache node; SQL reads are memoized for _MEMO_TTL seconds."""
    if not is_sql():
        return get_from_local_cache(path_parts)
    key = tuple(path_parts)
    now = time.monotonic()
    with _memo_lock:
        hit = _memo.get(key)
        if hit is not None and now - hit[0] < _MEMO_TTL:
            return hit[1]
    value = get_from_local_cache(path_parts)
    with _memo_lock:
        if len(_memo) >= _MEMO_MAX:
            _memo.clear()
        _memo[key] = (now, value)
    return value


def _set_in_mirror(path: str, value):
    """Apply one write to the in-memory dump copy (firebase_cache); value None deletes."""
    parts = _split_path_to_parts(path)
    if not parts:
        return
    current = firebase_cache
    for part in parts[:-1]:
        nxt = current.get(part) if isinstance(current, dict) else None
        if isinstance(nxt, list):
            nxt = {str(i): v for i, v in enumerate(nxt) if v is not None}
            current[part] = nxt
        elif not isinstance(nxt, dict):
            if value is None:
                return
            nxt = {}
            current[part] = nxt
        current = nxt
    if value is None:
        current.pop(parts[-1], None)
    else:
        current[parts[-1]] = value


def _write_values(values: dict) -> bool:
    """Write {path: value} (value None deletes) in one batch. Returns True on success."""
    if not values:
        return True
    invalidate_media_cache_memo()
    try:
        if is_sql():
            from DATABASE.firebase_init import get_sql_store
            get_sql_store().update("", values)  # one transaction
            return True
        if is_json() and _mirror_loaded:
            with _thread_lock:
                for path, value in values.items():
                    _set_in_mirror(path, value)
            _sync_local_cache_to_file()  # one dump.json rewrite
            return True
        for path, value in values.items():
            ref = db_child_by_path(db, path)
            if value is None:
                ref.remove()
            else:
                ref.set(value)
        if is_firebase():
            # keep the in-memory dump copy current, so the entry is usable before the next reload
            with _thread_lock:
                for path, value in values.items():
                    _set_in_mirror(path, value)
        return True
    except Exception as e:
        logger.error(f"[CACHE] write of {len(values)} value(s) failed: {type(e).__name__}: {e}")
        return False


def _parse_ids(value) -> list:
    if value is None or isinstance(value, (dict, list, bool)):
        return []
    try:
        return [int(x) for x in str(value).split(",") if str(x).strip()]
    except (TypeError, ValueError):
        return []


def _node_value(node, key):
    """Child `key` of a node that may have come back as a dict or (int keys) as a list."""
    if isinstance(node, dict):
        return node.get(str(key))
    if isinstance(node, list):
        try:
            i = int(key)
        except (TypeError, ValueError):
            return None
        return node[i] if 0 <= i < len(node) else None
    return None


def _video_url_hashes(url: str) -> list:
    """Hashes of every form a video URL is cached under (YouTube: also short/long)."""
    from URL_PARSERS.normalizer import normalize_url_for_cache
    from URL_PARSERS.youtube import is_youtube_url, youtube_to_short_url, youtube_to_long_url
    urls = [normalize_url_for_cache(url)]
    if is_youtube_url(url):
        urls += [normalize_url_for_cache(youtube_to_short_url(url)),
                 normalize_url_for_cache(youtube_to_long_url(url))]
    return list(dict.fromkeys(get_url_hash(u) for u in urls))


def _playlist_url_hashes(playlist_url: str) -> list:
    return list(dict.fromkeys(get_url_hash(u) for u in _normalize_playlist_urls(playlist_url)))


def _video_paths(url: str, quality_key: str) -> list:
    return [f"{Config.VIDEO_CACHE_DB_PATH}/{h}/{quality_key}" for h in _video_url_hashes(url)]


def save_to_playlist_cache(playlist_url: str, quality_key: str, video_indices: list, message_ids: list,
                           messages=None,
                           clear: bool = False, original_text: str = None, video_urls_dict: dict = None):
    """Cache playlist items: index -> message id(s) in the log channel.

    One index with several message ids (a split video) is stored as "id,id,...";
    otherwise indices and ids are paired one to one."""
    if not quality_key:
        logger.warning(LoggerMsg.DB_QUALITY_KEY_EMPTY_LOG_MSG.format(playlist_url=playlist_url))
        return
    if not getattr(Config, 'PLAYLIST_CACHE_DB_PATH', None) or Config.PLAYLIST_CACHE_DB_PATH.strip() in ('', '/', '.'):
        logger.error(LoggerMsg.DB_PLAYLIST_CACHE_PATH_INVALID_LOG_MSG.format(playlist_url=playlist_url))
        return
    try:
        hashes = _playlist_url_hashes(playlist_url)
        values = {}
        if clear:
            for h in hashes:
                values[f"{Config.PLAYLIST_CACHE_DB_PATH}/{h}/{quality_key}"] = None
        else:
            if not message_ids or not video_indices:
                logger.warning(f"[CACHE] playlist save skipped (no ids/indices): {playlist_url}, quality: {quality_key}")
                return
            if len(video_indices) == 1:
                pairs = [(video_indices[0], ",".join(map(str, message_ids)))]
            else:
                pairs = [(i, str(m)) for i, m in zip(video_indices, message_ids)]
            for h in hashes:
                for index, ids in pairs:
                    values[f"{Config.PLAYLIST_CACHE_DB_PATH}/{h}/{quality_key}/{encode_playlist_cache_index(index)}"] = ids
            # each item is also cached under its own video URL
            for index, ids in pairs:
                video_url = (video_urls_dict or {}).get(index)
                if video_url:
                    for path in _video_paths(video_url, quality_key):
                        values[path] = ids
        if _write_values(values):
            logger.info(f"[CACHE] playlist {'cleared' if clear else 'saved'}: quality={quality_key}, "
                        f"indices={video_indices}, ids={message_ids}, paths={len(values)}")
    except Exception as e:
        logger.error(f"Failed to save to playlist cache: {e}")


def remove_playlist_cache_entries(playlist_url: str, quality_key: str, indices) -> None:
    """Drop the given playlist items (e.g. their log-channel messages were deleted)."""
    if not quality_key or not indices:
        return
    try:
        values = {}
        for h in _playlist_url_hashes(playlist_url):
            for qk in _expand_quality_keys(quality_key):
                for index in indices:
                    values[f"{Config.PLAYLIST_CACHE_DB_PATH}/{h}/{qk}/{encode_playlist_cache_index(index)}"] = None
        _write_values(values)
        logger.info(f"[CACHE] dropped stale playlist entries: quality={quality_key}, indices={list(indices)}")
    except Exception as e:
        logger.error(f"Failed to drop playlist cache entries: {e}")


def get_cached_playlist_message_ids(playlist_url: str, quality_key: str, requested_indices: list) -> dict:
    """{index: [message ids]} for the requested playlist items found in the cache."""
    if not quality_key or not requested_indices:
        return {}
    found = {}
    try:
        quality_keys = _expand_quality_keys(quality_key)
        for h in _playlist_url_hashes(playlist_url):
            node = _read_node(["bot", "video_cache", "playlists", h])
            if not node:
                continue
            for qk in quality_keys:
                data = _node_value(node, qk)
                if not data:
                    continue
                for index in requested_indices:
                    if index in found:
                        continue
                    ids = _parse_ids(_node_value(data, encode_playlist_cache_index(index)))
                    if ids:
                        found[index] = ids
            if len(found) == len(requested_indices):
                break
    except Exception as e:
        logger.error(f"Failed to get from playlist cache: {e}")
        return {}
    logger.debug(f"[CACHE] playlist lookup quality={quality_key}: {len(found)}/{len(requested_indices)} cached")
    return found


def get_cached_playlist_videos(playlist_url: str, quality_key: str, requested_indices: list) -> dict:
    """{index: first message id} for cached playlist items (see get_cached_playlist_message_ids)."""
    return {i: ids[0] for i, ids in get_cached_playlist_message_ids(playlist_url, quality_key, requested_indices).items()}


def get_cached_playlist_qualities(playlist_url: str) -> set:
    """Gets all available qualities for a cached playlist."""
    try:
        all_qualities = set()
        for url_hash in _playlist_url_hashes(playlist_url):
            data = _read_node(["bot", "video_cache", "playlists", url_hash])
            if data and isinstance(data, dict):
                all_qualities.update(data.keys())
            elif is_firebase():
                # the dump copy may predate items saved by another instance: ask Firebase
                try:
                    firebase_data = db.child(f"{Config.PLAYLIST_CACHE_DB_PATH}/{url_hash}").get()
                    val = firebase_data.val() if firebase_data else None
                    if isinstance(val, dict):
                        all_qualities.update(val.keys())
                        with _thread_lock:
                            firebase_cache.setdefault("bot", {}).setdefault("video_cache", {}).setdefault("playlists", {})[url_hash] = val
                except Exception as e:
                    logger.warning(f"get_cached_playlist_qualities: error checking Firebase for hash {url_hash}: {e}")
        return all_qualities
    except Exception as e:
        logger.error(f"Failed to get cached playlist qualities: {e}")
        return set()


def is_any_playlist_index_cached(playlist_url, quality_key, indices):
    """Checks if at least one index from the range is in the playlist cache."""
    return bool(get_cached_playlist_message_ids(playlist_url, quality_key, indices))


def get_cached_qualities(url: str) -> set:
    """All cached quality keys for a video URL (any of its cached URL forms)."""
    try:
        qualities = set()
        for url_hash in _video_url_hashes(url):
            data = _read_node(["bot", "video_cache", url_hash])
            if isinstance(data, dict):
                qualities.update(k for k, v in data.items() if v and not isinstance(v, (dict, list)))
        return qualities
    except Exception as e:
        logger.error(f"Failed to get cached qualities: {e}")
        return set()


def get_cached_playlist_count(playlist_url: str, quality_key: str, indices: list = None) -> int:
    """Number of cached playlist items for quality_key (only `indices` if given)."""
    try:
        if indices is not None:
            return len(get_cached_playlist_message_ids(playlist_url, quality_key, indices))
        found = set()
        quality_keys = _expand_quality_keys(quality_key)
        for h in _playlist_url_hashes(playlist_url):
            node = _read_node(["bot", "video_cache", "playlists", h])
            for qk in quality_keys:
                data = _node_value(node, qk)
                if isinstance(data, dict):
                    found.update(k for k, v in data.items() if v is not None)
                elif isinstance(data, list):
                    found.update(str(i) for i, v in enumerate(data) if v is not None)
        return len(found)
    except Exception as e:
        logger.error(f"get_cached_playlist_count error: {e}")
        return 0


def get_url_hash(url: str) -> str:
    """Returns a hash of the URL for use as a cache key."""
    import hashlib
    return hashlib.md5(url.encode()).hexdigest()


def _split_path_to_parts(path: str) -> list:
    try:
        return [p for p in str(path).strip('/').split('/') if p]
    except Exception:
        return ["bot", "image_cache"]


def save_to_image_cache(url: str, post_index: int, message_ids: list):
    """Save sent album (post) message IDs for an image URL:
    <IMAGE_CACHE_DB_PATH>/<url_hash>/<post_index> -> "id,id,..." (existing entries are kept)."""
    from URL_PARSERS.normalizer import normalize_url_for_cache
    try:
        if not url or not message_ids or post_index is None:
            logger.warning("[IMG CACHE] save_to_image_cache skipped: empty args")
            return
        url_hash = get_url_hash(normalize_url_for_cache(url))
        image_root = getattr(Config, 'IMAGE_CACHE_DB_PATH', 'bot/video_cache/images')
        local_path_parts = _split_path_to_parts(image_root) + [url_hash, str(int(post_index))]
        if get_from_local_cache(local_path_parts):
            logger.info(f"[IMG CACHE] Skip save: already cached: {'/'.join(local_path_parts)}")
            return
        if _write_values({"/".join(local_path_parts): ",".join(map(str, message_ids))}):
            logger.info(f"[IMG CACHE] Saved album to cache: {'/'.join(local_path_parts)}")
    except Exception as e:
        logger.error(f"[IMG CACHE] Failed to save image cache: {e}")


def _image_posts_node(url: str):
    from URL_PARSERS.normalizer import normalize_url_for_cache
    url_hash = get_url_hash(normalize_url_for_cache(url))
    image_root = getattr(Config, 'IMAGE_CACHE_DB_PATH', 'bot/video_cache/images')
    return _read_node(_split_path_to_parts(image_root) + [url_hash])


def _image_post_items(base):
    """(1-based post index, raw value) pairs of an image cache node (dict or list layout)."""
    if isinstance(base, dict):
        for k, v in base.items():
            try:
                yield int(k), v
            except (TypeError, ValueError):
                continue
    elif isinstance(base, list):
        # [None, "ids", ...] is 1-based already; ["ids", ...] gets shifted to 1-based
        start_from_one = len(base) > 1 and base[0] in (None, "", [])
        for i, v in enumerate(base):
            if start_from_one:
                if i == 0:
                    continue
                yield i, v
            else:
                yield i + 1, v


def get_cached_image_posts(url: str, requested_indices: list | None = None) -> dict:
    """Return dict {post_index: [msg_ids]} for cached image posts for URL.
    If requested_indices is provided, only return intersection.
    """
    try:
        result = {}
        for idx, v in _image_post_items(_image_posts_node(url)):
            if requested_indices is not None and idx not in requested_indices:
                continue
            if isinstance(v, list):
                ids = [int(x) for x in v if x]
            else:
                ids = _parse_ids(v)
            if ids:
                result[idx] = ids
        return result
    except Exception as e:
        logger.error(f"Failed to get cached image posts: {e}")
        return {}


def get_cached_image_post_indices(url: str) -> set:
    """Return set of cached post indices for image URL."""
    try:
        return {idx for idx, v in _image_post_items(_image_posts_node(url)) if v}
    except Exception as e:
        logger.error(f"Failed to get cached image indices: {e}")
        return set()


def save_to_video_cache(url: str, quality_key: str, message_ids: list, clear: bool = False, original_text: str = None, user_id: int = None):
    """Cache (or with clear=True drop) the log-channel message ids of a video for quality_key."""
    from URL_PARSERS.playlist_utils import is_playlist_with_range

    if not quality_key:
        logger.warning(f"save_to_video_cache: quality_key is empty, skipping cache save for URL: {url}")
        return
    if not clear and original_text and is_playlist_with_range(original_text):
        logger.info(f"Playlist with range detected, skipping cache save for URL: {url}")
        return
    if not clear and not message_ids:
        logger.warning(f"save_to_video_cache: message_ids is empty for URL: {url}, quality: {quality_key}")
        return
    try:
        value = None if clear else ",".join(map(str, message_ids))
        if _write_values({path: value for path in _video_paths(url, quality_key)}):
            logger.info(f"[CACHE] video {'cleared' if clear else 'saved'}: url={url}, quality={quality_key}, ids={message_ids}")
    except Exception as e:
        logger.error(f"Failed to save to video cache: {e}")


def get_cached_message_ids(url: str, quality_key: str) -> list:
    """Cached log-channel message ids of a video (any cached URL form), or None."""
    if not quality_key:
        return None
    try:
        for url_hash in _video_url_hashes(url):
            ids = _parse_ids(_node_value(_read_node(["bot", "video_cache", url_hash]), quality_key))
            if ids:
                logger.info(f"[CACHE] hit: url={url}, quality={quality_key}, ids={ids}")
                return ids
        logger.debug(f"[CACHE] miss: url={url}, quality={quality_key}")
        return None
    except Exception as e:
        logger.error(f"Failed to get from cache: {e}")
        return None
