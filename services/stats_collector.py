from __future__ import annotations

import json
import os
import threading
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Deque, Dict, Iterable, List, Optional, Set, Tuple
from urllib.parse import urlparse

import requests
import logging

from CONFIG.config import Config

logger = logging.getLogger(__name__)
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------------------
# Утилиты
# --------------------------------------------------------------------------------------

NSFW_KEYWORDS = {
    "nsfw",
    "porn",
    "xxx",
    "onlyfans",
    "sex",
    "xvideos",
    "xhamster",
    "redtube",
    "brazzers",
    "adult",
    "18+",
    "leaked",
}

PLAYLIST_KEYWORDS = {
    "playlist",
    "list=",
    "sets",
    "mix",
    "watch_videos",
    "index=",
}


def _safe_int(value: Any) -> int:
    try:
        return int(float(value))
    except Exception:
        return 0


def _domain_from_url(url: str) -> str:
    try:
        parsed = urlparse(url or "")
        if not parsed.netloc:
            return ""
        host = parsed.netloc.lower()
        if host.startswith("www."):
            host = host[4:]
        return host
    except Exception:
        return ""


def _is_nsfw(url: str, title: str) -> bool:
    src = f"{url} {title}".lower()
    return any(token in src for token in NSFW_KEYWORDS)


def _is_playlist(url: str, title: str) -> bool:
    src = f"{url} {title}".lower()
    return any(token in src for token in PLAYLIST_KEYWORDS)


def _estimate_registration_date_from_user_id(user_id: int) -> Optional[int]:
    """
    Оценивает дату регистрации пользователя на основе его user_id.
    Использует приблизительную оценку на основе известных диапазонов ID.
    
    Примечание: Это приблизительная оценка, точность зависит от периода регистрации.
    Для старых аккаунтов (до 2015) точность выше, для новых - ниже.
    """
    if not user_id or user_id <= 0:
        return None
    
    # Известные опорные точки для оценки (ID -> примерная дата регистрации)
    # Основано на анализе распределения ID в Telegram
    reference_points = [
        (100000000, datetime(2013, 8, 1, tzinfo=timezone.utc).timestamp()),  # ~2013
        (500000000, datetime(2015, 1, 1, tzinfo=timezone.utc).timestamp()),  # ~2015
        (1000000000, datetime(2017, 6, 1, tzinfo=timezone.utc).timestamp()),  # ~2017
        (2000000000, datetime(2019, 12, 1, tzinfo=timezone.utc).timestamp()),  # ~2019
        (3000000000, datetime(2021, 3, 1, tzinfo=timezone.utc).timestamp()),  # ~2021
        (4000000000, datetime(2022, 6, 1, tzinfo=timezone.utc).timestamp()),  # ~2022
        (5000000000, datetime(2023, 9, 1, tzinfo=timezone.utc).timestamp()),  # ~2023
        (6000000000, datetime(2024, 12, 1, tzinfo=timezone.utc).timestamp()),  # ~2024
        (7000000000, datetime(2025, 12, 1, tzinfo=timezone.utc).timestamp()),  # ~2025
    ]
    
    # Если ID меньше минимального опорного значения
    if user_id < reference_points[0][0]:
        return int(reference_points[0][1])
    
    # Если ID больше максимального опорного значения - оцениваем как недавний
    if user_id >= reference_points[-1][0]:
        # Для очень новых ID используем линейную экстраполяцию
        last_id, last_ts = reference_points[-1]
        prev_id, prev_ts = reference_points[-2]
        
        id_diff = user_id - last_id
        id_span = last_id - prev_id
        ts_span = last_ts - prev_ts
        
        if id_span > 0 and ts_span > 0:
            estimated_ts = last_ts + (id_diff / id_span) * ts_span
            # Ограничиваем максимальной датой (не позже текущего момента)
            max_ts = datetime.now(tz=timezone.utc).timestamp()
            return int(min(estimated_ts, max_ts))
        return int(last_ts)
    
    # Линейная интерполяция между опорными точками
    for i in range(len(reference_points) - 1):
        id_left, ts_left = reference_points[i]
        id_right, ts_right = reference_points[i + 1]
        
        if id_left <= user_id < id_right:
            id_span = id_right - id_left
            ts_span = ts_right - ts_left
            
            if id_span > 0 and ts_span > 0:
                frac = (user_id - id_left) / id_span
                estimated_ts = ts_left + frac * ts_span
                return int(estimated_ts)
    
    # Fallback - возвращаем дату последней опорной точки
    return int(reference_points[-1][1])


def _country_code_from_language(lang: Optional[str]) -> Optional[str]:
    if not lang:
        return None
    lang = lang.lower()
    mapping = {
        "ru": "RU",
        "uk": "UA",
        "en": "US",
        "es": "ES",
        "pt": "BR",
        "ar": "AE",
        "fa": "IR",
        "tr": "TR",
        "hi": "IN",
        "in": "IN",  # Hindi alternative code
        "bn": "BD",
        "id": "ID",
        "de": "DE",
        "fr": "FR",
        "it": "IT",
        "pl": "PL",
        "uz": "UZ",
        "kk": "KZ",
        "az": "AZ",
        "tg": "TJ",
        "th": "TH",
        "zh": "CN",
        "ja": "JP",
        "ko": "KR",
        "vi": "VN",
        "ur": "PK",
        "tl": "PH",  # Tagalog -> Philippines
        "ha": "NG",  # Hausa -> Nigeria
    }
    return mapping.get(lang)


def _flag_from_country(country_code: Optional[str]) -> str:
    if not country_code or len(country_code) != 2:
        return "🏳"
    code = country_code.upper()
    try:
        return chr(ord(code[0]) - 65 + 0x1F1E6) + chr(ord(code[1]) - 65 + 0x1F1E6)
    except Exception:
        return "🏳"


def _guess_gender(first_name: Optional[str]) -> str:
    if not first_name:
        return "unknown"
    name = first_name.strip().lower()
    if not name:
        return "unknown"
    female_suffixes = ("a", "ia", "ya", "na", "la", "ra", "ta", "sa")
    male_suffixes = ("o", "iy", "ei", "er", "as", "us", "an", "ton", "non")
    if name.endswith(female_suffixes):
        return "female"
    if name.endswith(male_suffixes):
        return "male"
    return "unknown"


def _guess_age_from_text(text: Optional[str]) -> Optional[int]:
    if not text:
        return None
    numbers = []
    for token in text.split():
        token = token.strip(",.()[]{}")
        if not token.isdigit():
            continue
        value = int(token)
        if 5 <= value <= 90:
            numbers.append(value)
    return numbers[0] if numbers else None


def _window_bounds(period: str) -> Tuple[int, Optional[int]]:
    """
    Возвращает (window_start_ts, window_end_ts|None) для периода.
    all -> (0, None)
    """
    delta_map = {
        "today": timedelta(days=1),
        "week": timedelta(days=7),
        "month": timedelta(days=30),
        "all": None,
    }
    window_delta = delta_map.get(period)
    if window_delta is None:
        return 0, None
    now = datetime.now(tz=timezone.utc)
    return int((now - window_delta).timestamp()), int(now.timestamp())


# --------------------------------------------------------------------------------------
# Датаклассы
# --------------------------------------------------------------------------------------


@dataclass
class ProfileInfo:
    user_id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None
    country_code: Optional[str] = None
    flag: str = "🏳"
    gender: str = "unknown"
    age: Optional[int] = None
    registration_date: Optional[int] = None  # Unix timestamp даты регистрации
    last_refresh_ts: float = field(default_factory=lambda: time.time())

    def update_from_payload(self, payload: Dict[str, Any]) -> None:
        if not payload:
            return
        self.first_name = payload.get("first_name") or self.first_name
        self.last_name = payload.get("last_name") or self.last_name
        self.username = payload.get("username") or self.username
        self.language_code = payload.get("language_code") or self.language_code
        country = payload.get("country_code") or _country_code_from_language(self.language_code)
        if country:
            self.country_code = country.upper()
            self.flag = _flag_from_country(self.country_code)
        if "flag" in payload:
            self.flag = payload["flag"]
        self.gender = payload.get("gender") or self.gender or _guess_gender(self.first_name)
        age = payload.get("age")
        if age:
            try:
                self.age = int(age)
            except Exception:
                pass
        registration_date = payload.get("registration_date")
        if registration_date:
            try:
                self.registration_date = int(registration_date)
            except Exception:
                pass
        self.last_refresh_ts = time.time()

    def to_public_dict(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "name": " ".join(filter(None, [self.first_name, self.last_name])).strip() or self.first_name or "",
            "username": self.username,
            "flag": self.flag,
            "country_code": self.country_code,
            "gender": self.gender,
            "age": self.age,
        }


@dataclass
class DownloadRecord:
    user_id: int
    timestamp: int
    url: str
    title: str
    domain: str
    is_nsfw: bool
    is_playlist: bool
    multi_total: int = 1  # сколько URL было в исходном сообщении


@dataclass
class ActiveSession:
    user_id: int
    last_event_ts: float
    current_url: Optional[str]
    title: Optional[str]
    progress: Optional[float] = None  # Progress percentage (0-100)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class BlockRecord:
    user_id: int
    timestamp: int
    reason: Optional[str] = None


@dataclass
class ChannelActivity:
    entry_type: str
    timestamp: float
    user_id: Optional[int]
    name: Optional[str]
    username: Optional[str]
    description: str


# --------------------------------------------------------------------------------------
# Telegram profile fetcher
# --------------------------------------------------------------------------------------


class TelegramProfileFetcher:
    """Локальный кеш для запросов к Telegram Bot API (getChat) и Pyrogram API."""

    def __init__(self, ttl_seconds: int = 6 * 3600):
        self._token = getattr(Config, "BOT_TOKEN", None)
        self._session = requests.Session() if self._token else None
        self._ttl = ttl_seconds
        self._cache: Dict[int, ProfileInfo] = {}
        self._lock = threading.Lock()
        self._pending_fetches: Set[int] = set()
        self._fetch_lock = threading.Lock()
        self._pyro_app = None  # Будет установлен позже через set_pyro_app

    def set_pyro_app(self, app):
        """Устанавливает Pyrogram Client для получения расширенной информации о пользователях."""
        self._pyro_app = app

    @property
    def ttl(self) -> int:
        return self._ttl

    def _get_registration_date_from_pyrogram(self, user_id: int) -> Optional[int]:
        """Получает дату регистрации через Pyrogram MTProto API."""
        if not self._pyro_app:
            return None
        try:
            # Используем Pyrogram MTProto API для получения полной информации о пользователе
            try:
                from pyrogram.raw.functions.users import GetFullUser
                
                # Получаем InputUser для пользователя
                peer = self._pyro_app.resolve_peer(user_id)
                # Вызываем GetFullUser для получения полной информации
                full_user = self._pyro_app.invoke(GetFullUser(id=peer))
                
                # В некоторых версиях Telegram API дата регистрации может быть доступна
                # через различные поля. Проверяем доступные атрибуты
                # Примечание: стандартный Bot API не предоставляет дату регистрации,
                # но через MTProto API может быть доступна дополнительная информация
                
                # Для большинства случаев дата регистрации недоступна напрямую,
                # но можно использовать приблизительный метод через user_id
                # Пока возвращаем None, так как точная дата регистрации недоступна через Bot API
                _ = full_user  # Используем переменную чтобы избежать предупреждения
                return None
            except ImportError:
                # Если импорт не удался, пробуем без него
                return None
            except Exception as e:
                logger.debug(f"[stats] Pyrogram resolve_peer/getFullUser failed for {user_id}: {e}")
                return None
        except Exception as exc:
            logger.debug(f"[stats] Pyrogram getFullUser failed for {user_id}: {exc}")
        return None
    
    def _estimate_registration_date_from_user_id(self, user_id: int) -> Optional[int]:
        """
        Приблизительно вычисляет дату регистрации из user_id.
        Работает только для старых аккаунтов (до ~2015 года).
        Для новых аккаунтов возвращает None.
        """
        try:
            # Для старых аккаунтов первые 32 бита user_id содержат timestamp создания
            # Это работает только для аккаунтов, созданных до определенного времени
            # Проверяем, является ли это старым аккаунтом (user_id < определенного порога)
            # Примерно до 2015 года user_id содержал timestamp в первых битах
            
            # Если user_id очень большой (новые аккаунты), этот метод не работает
            if user_id > 2**31:  # Примерный порог для новых аккаунтов
                return None
            
            # Для очень старых аккаунтов можно попробовать извлечь timestamp
            # Но это неточный метод и работает не всегда
            return None  # Пока отключаем, так как неточный
        except Exception:
            return None

    def get_profile(self, user_id: int, force_refresh: bool = False) -> Optional[ProfileInfo]:
        if not self._token:
            return None
        now = time.time()
        with self._lock:
            cached = self._cache.get(user_id)
            if cached and not force_refresh and (now - cached.last_refresh_ts) < self._ttl:
                return cached
        try:
            url = f"https://api.telegram.org/bot{self._token}/getChat"
            resp = self._session.get(url, params={"chat_id": user_id}, timeout=10)
            resp.raise_for_status()
            data = resp.json().get("result", {})
        except Exception as exc:
            logger.debug(f"[stats] getChat failed for {user_id}: {exc}")
            return cached if cached else None
        payload = {
            "first_name": data.get("first_name"),
            "last_name": data.get("last_name"),
            "username": data.get("username"),
            "bio": data.get("bio"),
        }
        profile = ProfileInfo(user_id=user_id)
        profile.update_from_payload(payload)
        age_guess = _guess_age_from_text(data.get("bio"))
        if age_guess:
            profile.age = age_guess
        
        # Пытаемся получить дату регистрации через Pyrogram
        try:
            registration_date = self._get_registration_date_from_pyrogram(user_id)
            if registration_date:
                profile.registration_date = registration_date  # type: ignore
        except Exception:
            pass  # Если не удалось получить дату регистрации, продолжаем без неё
        
        with self._lock:
            self._cache[user_id] = profile
        return profile

    def batch_fetch_profiles(self, user_ids: List[int], max_workers: int = 5) -> Dict[int, ProfileInfo]:
        """Массово получает профили для списка пользователей."""
        from concurrent.futures import ThreadPoolExecutor, as_completed
        results = {}
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.get_profile, uid): uid for uid in user_ids}
            for future in as_completed(futures):
                user_id = futures[future]
                try:
                    profile = future.result()
                    if profile:
                        results[user_id] = profile
                except Exception as exc:
                    logger.debug(f"[stats] batch fetch failed for {user_id}: {exc}")
        return results


# --------------------------------------------------------------------------------------
# Основной коллектор
# --------------------------------------------------------------------------------------


class StatsCollector:
    """Агрегирует статистику на основе локального дампа и событий во время работы."""

    def __init__(
        self,
        dump_path: Optional[str] = None,
        *,
        reload_interval: int = 180,
        active_timeout: int = 900,
        start_background: bool = True,
    ):
        self.dump_path = dump_path or getattr(Config, "FIREBASE_CACHE_FILE", "dump.json")
        self.reload_interval = int(getattr(Config, "STATS_DUMP_RELOAD_INTERVAL", reload_interval))
        self.active_timeout = int(getattr(Config, "STATS_ACTIVE_TIMEOUT", active_timeout))

        self._lock = threading.RLock()
        self._historical_downloads: List[DownloadRecord] = []
        self._live_downloads: Deque[DownloadRecord] = deque(maxlen=10_000)
        self._download_timestamps: List[int] = []
        self._active_sessions: Dict[int, ActiveSession] = {}
        self._profiles: Dict[int, ProfileInfo] = {}
        self._blocked_users: Dict[int, BlockRecord] = {}
        self._channel_events: Deque[ChannelActivity] = deque(maxlen=500)
        # multi-url события: список кортежей (user_id, urls_count, timestamp)
        self._multi_url_events: List[Tuple[int, int, int]] = []
        # timestamp первой зафиксированной активности пользователя
        self._first_seen: Dict[int, int] = {}
        self._latest_dump_ts: int = 0
        self._last_reload_ts: float = 0
        self._profile_fetcher = TelegramProfileFetcher()
        self._active_sessions_file = Path(
            getattr(
                Config,
                "ACTIVE_SESSIONS_FILE",
                BASE_DIR / "CONFIG" / ".active_sessions.json",
            )
        )
        # Файл для хранения multi-url событий, чтобы дашборд и бот делили одну статистику
        self._multi_url_events_file = Path(
            getattr(
                Config,
                "MULTI_URL_EVENTS_FILE",
                BASE_DIR / "CONFIG" / ".multi_url_events.json",
            )
        )
        self._active_sessions_mtime: float = 0.0
        self._last_sessions_persist_ts: float = 0.0

        self._reload_thread: Optional[threading.Thread] = None
        if start_background:
            self._reload_thread = threading.Thread(target=self._reload_loop, daemon=True)
            self._reload_thread.start()

        # Первичное заполнение
        try:
            self.reload_from_dump()
        except Exception as exc:
            logger.warning(f"[stats] initial dump load failed: {exc}")
        self._load_active_sessions_from_disk()
        self._load_multi_url_events_from_disk()

    # ------------------------------------------------------------------
    # Вспомогательные методы
    # ------------------------------------------------------------------

    def _reload_loop(self) -> None:
        while True:
            time.sleep(self.reload_interval)
            try:
                self.reload_from_dump()
            except Exception as exc:
                logger.error(f"[stats] dump reload failed: {exc}")

    def _load_multi_url_events_from_disk(self) -> None:
        """Загружает multi-url события из файла, если он существует."""
        try:
            if not self._multi_url_events_file.exists():
                return
            with self._multi_url_events_file.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
            if not isinstance(data, list):
                return
            events: List[Tuple[int, int, int]] = []
            for item in data:
                if (
                    isinstance(item, list)
                    and len(item) == 3
                    and isinstance(item[0], int)
                    and isinstance(item[1], int)
                    and isinstance(item[2], int)
                ):
                    events.append((item[0], item[1], item[2]))
            with self._lock:
                self._multi_url_events = events[-5000:]
        except Exception as exc:
            logger.warning(f"[stats] failed to load multi-url events: {exc}")

    def _register_multi_event(self, user_id: int, urls_count: int, timestamp: int) -> None:
        """Запоминает факт множественной отправки URL в одном сообщении."""
        if not user_id or urls_count <= 1:
            return
        with self._lock:
            ts = timestamp or int(time.time())
            self._multi_url_events.append((user_id, urls_count, ts))
            # Ограничиваем размер, чтобы не росло бесконечно
            if len(self._multi_url_events) > 5000:
                self._multi_url_events = self._multi_url_events[-5000:]
            # Пишем на диск, чтобы дашборд видел эти события даже в другом процессе
            try:
                from HELPERS.filesystem_hlp import atomic_write_json
                self._multi_url_events_file.parent.mkdir(parents=True, exist_ok=True)
                atomic_write_json(str(self._multi_url_events_file), self._multi_url_events, indent=None)
            except Exception as exc:
                logger.debug(f"[stats] failed to persist multi-url events: {exc}")

    def reload_from_dump(self) -> None:
        if not os.path.exists(self.dump_path):
            return
        try:
            with open(self.dump_path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception as exc:
            logger.error(f"[stats] unable to read dump {self.dump_path}: {exc}")
            return
        bot_root = (
            data.get("bot", {})
            .get(getattr(Config, "BOT_NAME_FOR_USERS", "tgytdlp_bot"), {})
        )
        download_records: List[DownloadRecord] = []
        first_seen: Dict[int, int] = {}
        blocked_users: Dict[int, BlockRecord] = {}
        channel_events: List[ChannelActivity] = []
        latest_ts = 0

        logs = bot_root.get("logs")
        if isinstance(logs, dict):
            for user_id_str, entries in logs.items():
                if not isinstance(entries, dict):
                    continue
                for ts_str, payload in entries.items():
                    record = self._record_from_payload(user_id_str, ts_str, payload)
                    if not record:
                        continue
                    download_records.append(record)
                    prev = first_seen.get(record.user_id)
                    if not prev or record.timestamp < prev:
                        first_seen[record.user_id] = record.timestamp
                    latest_ts = max(latest_ts, record.timestamp)
        else:
            if logs not in (None, {}):
                logger.debug("[stats] unexpected logs payload type: %s", type(logs).__name__)

        blocked_source = bot_root.get("blocked_users")
        if isinstance(blocked_source, dict):
            iterator = blocked_source.items()
        else:
            iterator = []
            if blocked_source not in (None, {}):
                logger.debug("[stats] unexpected blocked_users payload type: %s", type(blocked_source).__name__)
        for user_id_str, payload in iterator:
            if not isinstance(payload, dict):
                continue
            uid = _safe_int(user_id_str)
            blocked_users[uid] = BlockRecord(
                user_id=uid,
                timestamp=_safe_int(payload.get("timestamp")),
                reason=str(payload.get("blocked_reason") or "manual"),
            )

        channel_guard = bot_root.get("channel_guard")
        if not isinstance(channel_guard, dict):
            channel_guard = {}
            if bot_root.get("channel_guard") not in (None, {}):
                logger.debug("[stats] unexpected channel_guard payload type: %s", type(bot_root.get("channel_guard")).__name__)
        leavers = channel_guard.get("leavers")
        if isinstance(leavers, dict):
            for user_id_str, payload in leavers.items():
                if not isinstance(payload, dict):
                    continue
                entry = ChannelActivity(
                    entry_type="leave",
                    timestamp=float(payload.get("last_left_ts") or payload.get("first_left_ts") or 0),
                    user_id=_safe_int(user_id_str),
                    name=payload.get("name"),
                    username=payload.get("username"),
                    description="Покинул(а) канал",
                )
                channel_events.append(entry)

        channel_events.sort(key=lambda item: item.timestamp)

        with self._lock:
            self._historical_downloads = sorted(download_records, key=lambda rec: rec.timestamp)
            self._download_timestamps = [rec.timestamp for rec in self._historical_downloads]
            self._blocked_users = blocked_users
            self._latest_dump_ts = latest_ts
            self._channel_events = deque(channel_events[-500:], maxlen=500)
            self._last_reload_ts = time.time()
            # Сбрасываем live-записи, которые уже попали в дамп
            self._live_downloads = deque(
                [rec for rec in self._live_downloads if rec.timestamp > self._latest_dump_ts],
                maxlen=10_000,
            )
            # обновляем карту первой активности
            self._first_seen = first_seen
        logger.debug(
            "[stats] dump reloaded: downloads=%s blocked=%s events=%s latest_ts=%s",
            len(self._historical_downloads),
            len(self._blocked_users),
            len(self._channel_events),
            self._latest_dump_ts,
        )

    def _record_from_payload(
        self, user_id_str: str, ts_str: str, payload: Dict[str, Any]
    ) -> Optional[DownloadRecord]:
        if not isinstance(payload, dict):
            return None
        user_id = _safe_int(user_id_str)
        timestamp = _safe_int(ts_str or payload.get("timestamp")) or int(time.time())
        urls_field = payload.get("urls") or payload.get("url")
        multi_total = 1
        url = ""
        if isinstance(urls_field, list):
            urls_list = [str(u) for u in urls_field if u]
            if urls_list:
                url = urls_list[0]
            multi_total = max(1, len(urls_list))
            if multi_total > 1:
                self._register_multi_event(user_id, multi_total, timestamp)
        else:
            url = str(urls_field or "")
        title = str(payload.get("title") or "")
        if not user_id or not url:
            return None
        domain = _domain_from_url(url)
        return DownloadRecord(
            user_id=user_id,
            timestamp=timestamp,
            url=url,
            title=title,
            domain=domain,
            is_nsfw=_is_nsfw(url, title),
            is_playlist=_is_playlist(url, title),
            multi_total=multi_total,
        )

    def _get_all_downloads(self) -> List[DownloadRecord]:
        with self._lock:
            return list(self._historical_downloads) + list(self._live_downloads)

    def _filter_downloads(self, period: str) -> List[DownloadRecord]:
        delta_map = {
            "today": timedelta(days=1),
            "week": timedelta(days=7),
            "month": timedelta(days=30),
            "all": None,
        }
        window = delta_map.get(period, None)
        if window is None:
            return self._get_all_downloads()
        threshold = int((datetime.now(tz=timezone.utc) - window).timestamp())
        return [rec for rec in self._get_all_downloads() if rec.timestamp >= threshold]

    def _get_profile(self, user_id: int, hints: Optional[Dict[str, Any]] = None) -> ProfileInfo:
        with self._lock:
            profile = self._profiles.get(user_id)
            if not profile:
                profile = ProfileInfo(user_id=user_id)
                self._profiles[user_id] = profile
        if hints:
            profile.update_from_payload(hints)
        # Если данных мало — попробуем Telegram API (но не чаще TTL)
        now = time.time()
        if (now - profile.last_refresh_ts) > self._profile_fetcher.ttl:
            fetched = self._profile_fetcher.get_profile(user_id)
            if fetched:
                payload = {
                    "first_name": fetched.first_name,
                    "last_name": fetched.last_name,
                    "username": fetched.username,
                    "language_code": fetched.language_code,
                    "country_code": fetched.country_code,
                    "flag": fetched.flag,
                    "gender": fetched.gender,
                    "age": fetched.age,
                    "registration_date": fetched.registration_date,
                }
                profile.update_from_payload(payload)
        if not profile.country_code and profile.language_code:
            profile.country_code = _country_code_from_language(profile.language_code)
            profile.flag = _flag_from_country(profile.country_code)
        if profile.gender == "unknown":
            profile.gender = _guess_gender(profile.first_name)
        return profile

    def _update_active_session(
        self,
        user_id: int,
        timestamp: float,
        url: Optional[str],
        title: Optional[str],
        progress: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        metadata = self._sanitize_metadata(metadata)
        with self._lock:
            existing = self._active_sessions.get(user_id)
            if existing:
                # Обновляем существующую сессию
                existing.last_event_ts = timestamp
                if url:
                    existing.current_url = url
                if title:
                    existing.title = title
                if progress is not None:
                    existing.progress = progress
                if metadata:
                    existing.metadata.update(metadata)
            else:
                # Создаем новую сессию
                self._active_sessions[user_id] = ActiveSession(
                    user_id=user_id,
                    last_event_ts=timestamp,
                    current_url=url,
                    title=title,
                    progress=progress,
                    metadata=metadata or {},
                )
            self._persist_active_sessions_locked()
    
    def _purge_expired_sessions(self) -> None:
        expiry = time.time() - self.active_timeout
        with self._lock:
            stale = [uid for uid, session in self._active_sessions.items() if session.last_event_ts < expiry]
            for uid in stale:
                self._active_sessions.pop(uid, None)
            if stale:
                self._persist_active_sessions_locked(force=True)
    
    def _sanitize_metadata(self, metadata: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        if not metadata:
            return {}
        safe: Dict[str, Any] = {}
        for key, value in metadata.items():
            if isinstance(value, (str, int, float, bool)) or value is None:
                safe[key] = value
            elif isinstance(value, dict):
                safe[key] = self._sanitize_metadata(value)
            else:
                safe[key] = str(value)
        return safe
    
    def _persist_active_sessions_locked(self, force: bool = False) -> None:
        now = time.time()
        if not force and (now - self._last_sessions_persist_ts) < 2:
            return
        self._last_sessions_persist_ts = now
        try:
            payload = {
                str(uid): {
                    "user_id": session.user_id,
                    "last_event_ts": session.last_event_ts,
                    "current_url": session.current_url,
                    "title": session.title,
                    "progress": session.progress,
                    "metadata": session.metadata,
                }
                for uid, session in self._active_sessions.items()
            }
            path = self._active_sessions_file
            tmp_path = path.with_suffix(".tmp")
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(tmp_path, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, ensure_ascii=False)
            tmp_path.replace(path)
            try:
                self._active_sessions_mtime = path.stat().st_mtime
            except OSError:
                self._active_sessions_mtime = time.time()
        except Exception as exc:
            logger.debug(f"[stats] failed to persist active sessions: {exc}")
    
    def _load_active_sessions_from_disk(self) -> None:
        path = self._active_sessions_file
        if not path.exists():
            return
        try:
            with open(path, "r", encoding="utf-8") as fh:
                raw = json.load(fh)
        except Exception as exc:
            logger.debug(f"[stats] failed to read active sessions file: {exc}")
            return
        sessions: Dict[int, ActiveSession] = {}
        now = time.time()
        for uid_str, data in raw.items():
            try:
                uid = int(uid_str)
            except Exception:
                continue
            sessions[uid] = ActiveSession(
                user_id=uid,
                last_event_ts=float(data.get("last_event_ts", now)),
                current_url=data.get("current_url"),
                title=data.get("title"),
                progress=data.get("progress"),
                metadata=self._sanitize_metadata(data.get("metadata")),
            )
        with self._lock:
            self._active_sessions = sessions
            try:
                self._active_sessions_mtime = path.stat().st_mtime
            except OSError:
                self._active_sessions_mtime = time.time()
    
    def _maybe_reload_active_sessions_from_disk(self) -> None:
        path = self._active_sessions_file
        try:
            mtime = path.stat().st_mtime
        except FileNotFoundError:
            return
        except OSError:
            return
        if mtime <= self._active_sessions_mtime:
            return
        self._load_active_sessions_from_disk()

    # ------------------------------------------------------------------
    # Публичный интерфейс
    # ------------------------------------------------------------------

    def record_download(
        self,
        *,
        user_id: int,
        url: str,
        title: str,
        timestamp: Optional[int] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        record = DownloadRecord(
            user_id=user_id,
            timestamp=timestamp or int(time.time()),
            url=url,
            title=title,
            domain=_domain_from_url(url),
            is_nsfw=_is_nsfw(url, title),
            is_playlist=_is_playlist(url, title),
        )
        profile_hints = metadata or {}
        profile = self._get_profile(user_id, profile_hints)
        if "language_code" in profile_hints and not profile.language_code:
            profile.language_code = profile_hints["language_code"]
            profile.country_code = profile_hints.get("country_code") or _country_code_from_language(profile.language_code)
            profile.flag = _flag_from_country(profile.country_code)
        with self._lock:
            self._live_downloads.append(record)
            ts = record.timestamp
            prev = self._first_seen.get(user_id)
            if not prev or ts < prev:
                self._first_seen[user_id] = ts
        self._update_active_session(user_id, record.timestamp, record.url, record.title)

    def update_download_progress(
        self,
        user_id: int,
        progress: float,
        url: Optional[str] = None,
        title: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Обновляет прогресс загрузки для активной сессии пользователя."""
        timestamp = time.time()
        self._update_active_session(user_id, timestamp, url, title, progress, metadata)

    def handle_db_event(self, path: str, operation: str, payload: Any) -> None:
        """Обновляет кеш на основе структур в БД."""
        parts = [segment for segment in path.strip("/").split("/") if segment]
        if len(parts) < 3:
            return
        _, bot_name, section, *rest = parts
        if bot_name != getattr(Config, "BOT_NAME_FOR_USERS", bot_name):
            return
        if section == "logs" and rest and operation in {"set", "update"} and isinstance(payload, dict):
            user_id = _safe_int(rest[0])
            timestamp = rest[1] if len(rest) > 1 else payload.get("timestamp")
            record = self._record_from_payload(str(user_id), str(timestamp), payload)
            if not record:
                return
            with self._lock:
                self._live_downloads.append(record)
                ts = record.timestamp
                prev = self._first_seen.get(user_id)
                if not prev or ts < prev:
                    self._first_seen[user_id] = ts
            self._update_active_session(user_id, record.timestamp, record.url, record.title)
        elif section == "blocked_users":
            user_id = _safe_int(rest[0]) if rest else _safe_int(payload.get("ID"))
            if not user_id:
                return
            if operation == "remove":
                with self._lock:
                    self._blocked_users.pop(user_id, None)
            else:
                ts = _safe_int(payload.get("timestamp")) or int(time.time())
                reason = str(payload.get("blocked_reason") or "manual")
                with self._lock:
                    self._blocked_users[user_id] = BlockRecord(user_id=user_id, timestamp=ts, reason=reason)
        elif section == "unblocked_users" and rest:
            user_id = _safe_int(rest[0])
            with self._lock:
                self._blocked_users.pop(user_id, None)
        elif section == "channel_guard" and rest:
            subsection = rest[0]
            if subsection == "leavers" and len(rest) >= 2 and isinstance(payload, dict):
                self._channel_events.append(
                    ChannelActivity(
                        entry_type="leave",
                        timestamp=float(payload.get("last_left_ts") or time.time()),
                        user_id=_safe_int(rest[1]),
                        name=payload.get("name"),
                        username=payload.get("username"),
                        description="Покинул(а) канал",
                    )
                )

    def get_active_users(self, limit: int = 10, minutes: Optional[int] = None) -> Dict[str, Any]:
        self._maybe_reload_active_sessions_from_disk()
        self._purge_expired_sessions()
        # Также учитываем последние загрузки из дампа для активных пользователей
        now = time.time()
        window = (minutes or 0) * 60
        threshold = now - (window or self.active_timeout)
        recent_downloads = [
            rec for rec in self._get_all_downloads()
            if rec.timestamp >= threshold
        ]
        user_last_activity: Dict[int, Tuple[float, Optional[str], Optional[str], Optional[float], Dict[str, Any]]] = {}
        for rec in recent_downloads:
            existing = user_last_activity.get(rec.user_id, (0, None, None, None, {}))
            if rec.timestamp > existing[0]:
                user_last_activity[rec.user_id] = (rec.timestamp, rec.url, rec.title, None, {})
        with self._lock:
            for session in self._active_sessions.values():
                existing = user_last_activity.get(session.user_id, (0, None, None, None, {}))
                if session.last_event_ts > existing[0]:
                    user_last_activity[session.user_id] = (
                        session.last_event_ts,
                        session.current_url,
                        session.title,
                        session.progress,
                        session.metadata,
                    )
        sessions = [
            {
                "user_id": uid,
                "last_event_ts": ts,
                "url": url,
                "title": title,
                "progress": progress,
                "metadata": metadata or {},
            }
            for uid, (ts, url, title, progress, metadata) in user_last_activity.items()
        ]
        sessions.sort(key=lambda s: s["last_event_ts"], reverse=True)
        total = len(sessions)
        items = []
        user_ids = [s["user_id"] for s in sessions[:limit]]
        # Массовая загрузка профилей
        fetched_profiles = self._profile_fetcher.batch_fetch_profiles(user_ids)
        for session in sessions[:limit]:
            user_id = session["user_id"]
            if user_id in fetched_profiles:
                profile = fetched_profiles[user_id]
                with self._lock:
                    self._profiles[user_id] = profile
            else:
                profile = self._get_profile(user_id)
            items.append(
                {
                    **profile.to_public_dict(),
                    "last_event_ts": session["last_event_ts"],
                    "url": session["url"],
                    "title": session["title"],
                    "progress": session["progress"],
                    "metadata": session.get("metadata") or {},
                    "first_seen_ts": self._first_seen.get(user_id),
                }
            )
        return {"total": total, "items": items}

    def get_suspicious_users(self, period: str, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Пользователи, которые практически непрерывно что‑то качают в указанный период.

        Логика:
        - Берём все загрузки в окне [window_start, now] (или весь дамп для "all").
        - Для каждого пользователя считаем:
            * internal gaps — интервалы между соседними загрузками (НЕ учитываем
              паузы от начала окна до первой загрузки и от последней до "сейчас").
            * active_span = last_ts - first_ts.
            * coverage = active_span / window_span.
        - В "подозрительные" попадают только те, у кого:
            * достаточно много событий (MIN_EVENTS);
            * coverage >= MIN_COVERAGE — т.е. пользователь был активен большую
              часть периода, а не сделал 2 запроса и ушёл.
        - В результате сортируем по максимальной внутренней паузе (чем меньше,
          тем более "беспрерывный" пользователь).
        """
        # Определяем окно периода
        delta_map = {
            "today": timedelta(days=1),
            "week": timedelta(days=7),
            "month": timedelta(days=30),
            "all": None,
        }
        window_delta = delta_map.get(period)
        now = int(time.time())
        if window_delta is None:
            window_start = 0
            window_end = None
        else:
            window_end = now
            window_start = int((datetime.now(tz=timezone.utc) - window_delta).timestamp())

        # Собираем таймстемпы по пользователям в пределах окна
        with self._lock:
            blocked_user_ids = set(self._blocked_users.keys())
        per_user: Dict[int, List[int]] = defaultdict(list)
        for record in self._get_all_downloads():
            if record.user_id in blocked_user_ids:
                continue
            if window_delta is not None and record.timestamp < window_start:
                continue
            per_user[record.user_id].append(record.timestamp)

        MIN_EVENTS = 10
        MIN_COVERAGE = 0.5

        suspicious: List[Tuple[int, int, int, int]] = []
        for user_id, timestamps in per_user.items():
            if len(timestamps) < MIN_EVENTS:
                continue
            timestamps.sort()
            first_ts, last_ts = timestamps[0], timestamps[-1]
            # внутренние паузы между соседними загрузками
            internal_gaps = [
                second - first
                for first, second in zip(timestamps, timestamps[1:])
                if second >= first
            ]
            if not internal_gaps:
                continue
            max_internal_gap = max(internal_gaps)

            # Покрытие окна активностью пользователя
            effective_window_end = window_end or last_ts
            window_span = max(effective_window_end - window_start, 1)
            active_span = max(last_ts - first_ts, 0)
            coverage = active_span / window_span
            if coverage < MIN_COVERAGE:
                # пользователь был активен только в небольшой части окна — не считаем подозрительным
                continue

            suspicious.append((user_id, max_internal_gap, len(timestamps), last_ts))

        # Чем меньше максимальная пауза и чем больше загрузок, тем "подозрительнее"
        suspicious.sort(key=lambda item: (item[1], -item[2], -item[3]))

        result: List[Dict[str, Any]] = []
        for user_id, max_gap, count, last_ts in suspicious[:limit]:
            profile = self._get_profile(user_id)
            result.append(
                {
                    **profile.to_public_dict(),
                    "max_gap_seconds": max_gap,
                    "downloads": count,
                    "last_event_ts": last_ts,
                }
            )
        return result

    def _aggregate_by_user(self, downloads: Iterable[DownloadRecord]) -> Counter:
        counter: Counter = Counter()
        for record in downloads:
            counter[record.user_id] += 1
        return counter

    def get_top_downloaders(self, period: str, limit: int = 10) -> List[Dict[str, Any]]:
        downloads = self._filter_downloads(period)
        counter = self._aggregate_by_user(downloads)
        top = counter.most_common(limit * 2)
        # Filter out blocked users
        with self._lock:
            blocked_user_ids = set(self._blocked_users.keys())
        filtered_top = [(user_id, count) for user_id, count in top if user_id not in blocked_user_ids]
        user_ids = [user_id for user_id, _ in filtered_top[:limit]]
        # Массовая загрузка профилей
        fetched_profiles = self._profile_fetcher.batch_fetch_profiles(user_ids)
        result = []
        for user_id, count in filtered_top[:limit]:
            if user_id in fetched_profiles:
                profile = fetched_profiles[user_id]
                with self._lock:
                    self._profiles[user_id] = profile
            else:
                profile = self._get_profile(user_id)
            result.append({**profile.to_public_dict(), "count": count})
        return result

    def get_top_domains(self, period: str, limit: int = 10) -> List[Dict[str, Any]]:
        downloads = self._filter_downloads(period)
        counter: Counter = Counter(record.domain for record in downloads if record.domain)
        return [{"domain": domain, "count": count} for domain, count in counter.most_common(limit)]

    def get_top_countries(self, period: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Получает статистику стран на основе файла lang.txt в папке пользователя.
        Если файла нет - считается как английский (en -> US).
        Считает уникальных пользователей, а не количество скачиваний.
        """
        downloads = self._filter_downloads(period)
        with self._lock:
            blocked_user_ids = set(self._blocked_users.keys())
        
        # Собираем уникальных пользователей
        user_ids = {rec.user_id for rec in downloads if rec.user_id not in blocked_user_ids}
        
        # Получаем путь к папке пользователей
        users_dir = Path(getattr(Config, "USERS_DIR", "users"))
        if not users_dir.is_absolute():
            users_dir = BASE_DIR / users_dir
        
        counter: Counter = Counter()
        for user_id in user_ids:
            # Читаем lang.txt из папки пользователя
            lang_file = users_dir / str(user_id) / "lang.txt"
            lang_code = "en"  # По умолчанию английский
            
            if lang_file.exists():
                try:
                    lang_code = lang_file.read_text(encoding="utf-8").strip().lower()
                    if not lang_code:
                        lang_code = "en"
                except Exception:
                    lang_code = "en"
            
            # Преобразуем код языка в код страны
            country = _country_code_from_language(lang_code) or "UN"
            counter[country] += 1
        
        result = []
        for country, count in counter.most_common(limit):
            flag = _flag_from_country(country if country != "UN" else None)
            result.append({"country_code": country, "flag": flag, "count": count})
        return result

    def get_gender_stats(self, period: str) -> List[Dict[str, Any]]:
        """
        Статистика по полу пользователей.
        Считает уникальных пользователей, а не количество скачиваний.
        """
        downloads = self._filter_downloads(period)
        with self._lock:
            blocked_user_ids = set(self._blocked_users.keys())
        # Собираем уникальных пользователей
        user_ids = {rec.user_id for rec in downloads if rec.user_id not in blocked_user_ids}
        counter: Counter = Counter()
        for user_id in user_ids:
            profile = self._get_profile(user_id)
            counter[profile.gender or "unknown"] += 1
        return [{"gender": gender, "count": count} for gender, count in counter.most_common()]

    def get_age_stats(self, period: str) -> List[Dict[str, Any]]:
        """
        Статистика по «возрасту» аккаунта: дата регистрации пользователя в Telegram.
        
        Для периода "all": показывает всех пользователей, сортирует по дате (старые сначала).
        Для периодов "month/week/today": показывает только пользователей, зарегистрировавшихся в этот период.
        
        Использует дату регистрации из Telegram API, если доступна, иначе оценивает по user_id.
        """
        with self._lock:
            blocked_user_ids = set(self._blocked_users.keys())
        
        # Определяем временные границы периода для фильтрации по дате регистрации
        window_start, window_end = _window_bounds(period)
        
        # Для периода "all" собираем всех пользователей из дампа
        # Для других периодов собираем только активных в этот период
        if period == "all":
            # Для "all" используем всех пользователей из _first_seen
            user_ids = set(self._first_seen.keys())
        else:
            downloads = self._filter_downloads(period)
            user_ids = {rec.user_id for rec in downloads if rec.user_id not in blocked_user_ids}
        
        counter: Counter = Counter()
        for user_id in user_ids:
            if user_id in blocked_user_ids:
                continue
            
            # Пытаемся получить дату регистрации из профиля (через Telegram API)
            profile = self._get_profile(user_id)
            registration_ts = None
            
            if profile and profile.registration_date:
                # Используем дату регистрации из Telegram API
                registration_ts = profile.registration_date
            
            # Если дата регистрации недоступна через API, оцениваем по user_id
            if not registration_ts:
                registration_ts = _estimate_registration_date_from_user_id(user_id)
            
            # Фильтруем по периоду регистрации (если не "all")
            if period != "all" and registration_ts:
                if window_start and registration_ts < window_start:
                    continue
                if window_end and registration_ts > window_end:
                    continue
            
            if registration_ts:
                dt = datetime.fromtimestamp(registration_ts, tz=timezone.utc)
                # Группируем по годам, так как точность оценки только годовая
                bucket = dt.strftime("%Y")
            else:
                # Для "unknown" не фильтруем по периоду, но показываем только если период "all"
                if period != "all":
                    continue
                bucket = "unknown"
            counter[bucket] += 1
        
        # Сортируем по дате (старые сначала), "unknown" в конце
        result_items = []
        date_items = []
        unknown_count = counter.get("unknown", 0)
        
        for bucket, count in counter.items():
            if bucket == "unknown":
                continue
            # Преобразуем bucket (год) в timestamp для сортировки
            try:
                dt = datetime.strptime(bucket, "%Y").replace(tzinfo=timezone.utc)
                date_items.append((dt.timestamp(), bucket, count))
            except Exception:
                continue
        
        # Сортируем по дате (старые сначала)
        date_items.sort(key=lambda x: x[0])
        result_items = [{"age_group": bucket, "count": count} for _, bucket, count in date_items]
        
        # Добавляем "unknown" в конец, если есть
        if unknown_count > 0:
            result_items.append({"age_group": "unknown", "count": unknown_count})
        
        return result_items
    
    def get_channel_join_stats(self, period: str) -> List[Dict[str, Any]]:
        """
        Статистика по дате присоединения к каналу (первая активность в боте).
        Использует _first_seen из дампа.
        
        Группировка:
        - All time: по месяцам (YYYY-MM) - показывает всех пользователей
        - Month: по неделям (YYYY-MM-WW) - только пользователи, присоединившиеся в этот месяц
        - Week: по дням (YYYY-MM-DD) - только пользователи, присоединившиеся в эту неделю
        - Today: одна строка "today" - только пользователи, присоединившиеся сегодня
        """
        with self._lock:
            blocked_user_ids = set(self._blocked_users.keys())
            first_seen_copy = dict(self._first_seen)
        
        # Определяем временные границы периода
        window_start, window_end = _window_bounds(period)
        
        counter: Counter = Counter()
        for user_id, first_ts in first_seen_copy.items():
            if user_id in blocked_user_ids:
                continue
            
            # Фильтруем по периоду присоединения
            if window_start and first_ts < window_start:
                continue
            if window_end and first_ts > window_end:
                continue
            
            dt = datetime.fromtimestamp(first_ts, tz=timezone.utc)
            
            if period == "all":
                # Группировка по месяцам
                bucket = dt.strftime("%Y-%m")
            elif period == "month":
                # Группировка по неделям (неделя в месяце)
                # Вычисляем номер недели в месяце (1-5)
                first_day = dt.replace(day=1)
                week_in_month = ((dt - first_day).days // 7) + 1
                bucket = f"{dt.strftime('%Y-%m')}-W{week_in_month}"
            elif period == "week":
                # Группировка по дням
                bucket = dt.strftime("%Y-%m-%d")
            elif period == "today":
                # Одна строка для сегодня
                bucket = "today"
            else:
                bucket = dt.strftime("%Y-%m")
            
            counter[bucket] += 1
        
        # Сортируем результаты
        if period == "all":
            # Для "all" сортируем по дате (старые сначала)
            result = sorted(counter.items(), key=lambda x: x[0])
        elif period == "month":
            # Для "month" сортируем по дате
            result = sorted(counter.items(), key=lambda x: x[0])
        elif period == "week":
            # Для "week" сортируем по дате
            result = sorted(counter.items(), key=lambda x: x[0])
        else:
            # Для "today" и других - просто по количеству
            result = counter.most_common()
        
        return [{"join_date": group, "count": count} for group, count in result]

    def _filter_downloads_by_flag(
        self,
        predicate,
        limit: int = 10,
    ) -> List[Dict[str, Any]]:
        counter: Counter = Counter()
        for record in self._get_all_downloads():
            if predicate(record):
                counter[record.user_id] += 1
        result = []
        for user_id, count in counter.most_common(limit):
            profile = self._get_profile(user_id)
            result.append({**profile.to_public_dict(), "count": count})
        return result

    def get_top_nsfw_users(self, limit: int = 10) -> List[Dict[str, Any]]:
        return self._filter_downloads_by_flag(lambda rec: rec.is_nsfw, limit=limit)

    def get_top_nsfw_domains(self, limit: int = 10) -> List[Dict[str, Any]]:
        counter: Counter = Counter()
        for record in self._get_all_downloads():
            if record.is_nsfw and record.domain:
                counter[record.domain] += 1
        return [{"domain": domain, "count": count} for domain, count in counter.most_common(limit)]

    def get_top_playlist_users(self, limit: int = 10) -> List[Dict[str, Any]]:
        return self._filter_downloads_by_flag(lambda rec: rec.is_playlist, limit=limit)

    def get_top_multi_url_users(self, period: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Пользователи, которые чаще всего отправляют несколько URL в одном сообщении."""
        window_start, window_end = _window_bounds(period)
        with self._lock:
            blocked_user_ids = set(self._blocked_users.keys())
            events = list(self._multi_url_events)

        filtered: List[Tuple[int, int, int]] = []
        for user_id, urls_count, ts in events:
            if user_id in blocked_user_ids:
                continue
            if window_end is not None and ts < window_start:
                continue
            filtered.append((user_id, urls_count, ts))

        # Если явных событий нет (старые дампы/версии), пытаемся восстановить статистику
        # из исторических записей, используя поле multi_total > 1.
        if not filtered:
            for rec in self._filter_downloads(period):
                if rec.user_id in blocked_user_ids:
                    continue
                if rec.multi_total and rec.multi_total > 1:
                    filtered.append((rec.user_id, rec.multi_total, rec.timestamp))

        # агрегируем по пользователям
        per_user: Dict[int, Dict[str, Any]] = defaultdict(lambda: {"messages": 0, "total_urls": 0, "last_ts": 0})
        for user_id, urls_count, ts in filtered:
            agg = per_user[user_id]
            agg["messages"] += 1
            agg["total_urls"] += urls_count
            agg["last_ts"] = max(agg["last_ts"], ts)

        ranked = sorted(
            per_user.items(),
            key=lambda item: (-(item[1]["total_urls"]), -(item[1]["messages"]), -(item[1]["last_ts"])),
        )

        user_ids = [uid for uid, _ in ranked[:limit]]
        fetched_profiles = self._profile_fetcher.batch_fetch_profiles(user_ids)
        result = []
        for user_id, stats in ranked[:limit]:
            profile = fetched_profiles.get(user_id) or self._get_profile(user_id)
            result.append(
                {
                    **profile.to_public_dict(),
                    "messages": stats["messages"],
                    "total_urls": stats["total_urls"],
                    "last_event_ts": stats["last_ts"],
                    "avg_urls": round(stats["total_urls"] / stats["messages"], 2) if stats["messages"] else stats["total_urls"],
                }
            )
        return result

    def get_format_users(self, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Пользователи с выбранным форматом (format.txt != ALWAYS_ASK).
        Сортируем по времени изменения файла (свежее выше).
        """
        users_dir = Path(getattr(Config, "USERS_DIR", "users"))
        if not users_dir.is_absolute():
            users_dir = BASE_DIR / users_dir
        if not users_dir.exists():
            return []

        entries: List[Tuple[int, float, str]] = []
        for format_file in users_dir.glob("*/format.txt"):
            try:
                user_id = int(format_file.parent.name)
            except Exception:
                continue
            try:
                content = format_file.read_text(encoding="utf-8").strip()
            except Exception:
                continue
            if not content or content.upper() == "ALWAYS_ASK":
                continue
            mtime = format_file.stat().st_mtime
            entries.append((user_id, mtime, content))

        entries.sort(key=lambda item: item[1], reverse=True)
        result = []
        for user_id, mtime, fmt in entries[:limit]:
            profile = self._get_profile(user_id)
            result.append(
                {
                    **profile.to_public_dict(),
                    "format": fmt,
                    "updated_ts": int(mtime),
                }
            )
        return result

    def get_power_users(self, min_urls: int = 10, days: int = 7, limit: int = 10) -> List[Dict[str, Any]]:
        """Пользователи, которые N дней подряд отправляли >M ссылок."""
        downloads = self._get_all_downloads()
        with self._lock:
            blocked_user_ids = set(self._blocked_users.keys())
        per_user_per_day: Dict[int, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        for record in downloads:
            if record.user_id in blocked_user_ids:
                continue
            day = datetime.fromtimestamp(record.timestamp, tz=timezone.utc).strftime("%Y-%m-%d")
            per_user_per_day[record.user_id][day] += 1
        qualified: List[Tuple[int, int]] = []
        for user_id, day_counts in per_user_per_day.items():
            days_sorted = sorted(day_counts.items())
            streak = 0
            best_streak = 0
            for _, count in days_sorted:
                if count >= min_urls:
                    streak += 1
                    best_streak = max(best_streak, streak)
                else:
                    streak = 0
            if best_streak >= days:
                qualified.append((user_id, best_streak))
        qualified.sort(key=lambda item: item[1], reverse=True)
        result = []
        for user_id, streak in qualified[:limit]:
            profile = self._get_profile(user_id)
            result.append({**profile.to_public_dict(), "streak": streak})
        return result

    def get_user_history(self, user_id: int, period: str = "all", limit: int = 100) -> List[Dict[str, Any]]:
        """Получить историю загрузок пользователя из dump.json (logs)"""
        result = []
        
        # Получаем логи напрямую из dump.json
        if not os.path.exists(self.dump_path):
            return result
        
        try:
            with open(self.dump_path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception as exc:
            logger.error(f"[stats] unable to read dump {self.dump_path}: {exc}")
            return result
        
        bot_root = (
            data.get("bot", {})
            .get(getattr(Config, "BOT_NAME_FOR_USERS", "tgytdlp_bot"), {})
        )
        
        logs = bot_root.get("logs", {})
        if not isinstance(logs, dict):
            return result
        
        user_id_str = str(user_id)
        user_logs = logs.get(user_id_str, {})
        if not isinstance(user_logs, dict):
            return result
        
        # Обрабатываем все логи пользователя
        for ts_str, payload in user_logs.items():
            try:
                timestamp = int(ts_str)
            except (ValueError, TypeError):
                continue
            
            # Фильтр по периоду
            if period != "all":
                delta_map = {
                    "today": timedelta(days=1),
                    "week": timedelta(days=7),
                    "month": timedelta(days=30),
                }
                if period in delta_map:
                    window_start = int((datetime.now(tz=timezone.utc) - delta_map[period]).timestamp())
                    if timestamp < window_start:
                        continue
            
            # Извлекаем данные из payload
            url = payload.get("urls", "") or payload.get("url", "")
            title = payload.get("title", "") or payload.get("name", "")
            domain = ""
            if url:
                try:
                    from urllib.parse import urlparse
                    parsed = urlparse(url)
                    domain = parsed.netloc or ""
                except Exception:
                    pass
            
            is_nsfw = payload.get("is_nsfw", False) or payload.get("nsfw", False)
            is_playlist = payload.get("is_playlist", False) or payload.get("playlist", False)
            
            result.append({
                "timestamp": timestamp,
                "url": url,
                "title": title,
                "domain": domain,
                "is_nsfw": bool(is_nsfw),
                "is_playlist": bool(is_playlist),
            })
        
        # Сортировка по времени (новые сначала)
        result.sort(key=lambda x: x["timestamp"], reverse=True)
        
        # Ограничение количества
        return result[:limit]

    def get_blocked_users(self, limit: int = 50) -> List[Dict[str, Any]]:
        with self._lock:
            blocked = list(self._blocked_users.values())
        blocked.sort(key=lambda rec: rec.timestamp, reverse=True)
        result = []
        for record in blocked[:limit]:
            profile = self._get_profile(record.user_id)
            result.append(
                {
                    **profile.to_public_dict(),
                    "timestamp": record.timestamp,
                    "reason": record.reason,
                }
            )
        return result

    def get_recent_channel_events(self, hours: int = 48, limit: int = 100) -> List[Dict[str, Any]]:
        threshold = time.time() - hours * 3600
        with self._lock:
            events = [event for event in self._channel_events if event.timestamp >= threshold]
        events.sort(key=lambda e: e.timestamp, reverse=True)
        result = []
        for event in events[:limit]:
            result.append(
                {
                    "type": event.entry_type,
                    "timestamp": event.timestamp,
                    "user_id": event.user_id,
                    "name": event.name,
                    "username": event.username,
                    "description": event.description,
                }
            )
        return result

    def block_user_local(self, user_id: int, reason: str = "manual") -> None:
        with self._lock:
            self._blocked_users[user_id] = BlockRecord(
                user_id=user_id,
                timestamp=int(time.time()),
                reason=reason,
            )

    def unblock_user_local(self, user_id: int) -> None:
        with self._lock:
            self._blocked_users.pop(user_id, None)

    def update_user_metadata(self, user_id: int, metadata: Dict[str, Any]) -> None:
        if not metadata:
            return
        self._get_profile(user_id, metadata)


# --------------------------------------------------------------------------------------
# Глобальный экземпляр
# --------------------------------------------------------------------------------------


stats_collector = StatsCollector()


def get_stats_collector() -> StatsCollector:
    return stats_collector

