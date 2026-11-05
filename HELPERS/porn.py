import functools
import importlib
import re
import threading
import time
import types
from urllib.parse import urlparse, parse_qs, unquote

import tldextract

from CONFIG.config import Config
from CONFIG.messages import Messages, safe_get_messages
from CONFIG.domains import DomainsConfig
from HELPERS.logger import logger


# ---------------------------------------------------------------------------
#  Redirect URL unwrapping
# ---------------------------------------------------------------------------

def unwrap_redirect_url(url: str) -> str:
    """
    Unwrap common redirect links (Google, Facebook, etc.) by extracting the first
    http(s) URL from known query parameters like url, u, q, redirect, redir, target, to, dest, destination, r, s.
    Performs up to 2 unwrapping passes.
    """
    try:
        current = url
        for _ in range(2):
            parsed = urlparse(current)
            qs = parse_qs(parsed.query or "")
            candidate = None
            for key in [
                "url", "u", "q", "redirect", "redir", "target", "to",
                "dest", "destination", "r", "s",
            ]:
                values = qs.get(key)
                if not values:
                    continue
                for v in values:
                    v = unquote(v)
                    m = re.search(r"https?://[^\s]+", v)
                    if m:
                        candidate = m.group(0)
                        break
                if candidate:
                    break
            if candidate:
                current = candidate
                continue
            break
        return current
    except Exception:
        return url


# ---------------------------------------------------------------------------
#  Domain lists (loaded from files)
# ---------------------------------------------------------------------------

PORN_DOMAINS: set = set()
SUPPORTED_SITES: set = set()
PORN_KEYWORDS: set = set()

_REDIRECT_PARAMS = (
    "url", "u", "q", "redirect", "redir", "target", "to",
    "dest", "destination", "r", "s",
)


def load_domain_lists():
    """Load PORN_DOMAINS, PORN_KEYWORDS, SUPPORTED_SITES from text files."""
    global PORN_DOMAINS, SUPPORTED_SITES, PORN_KEYWORDS
    file_map = {
        "PORN_DOMAINS": (getattr(Config, "PORN_DOMAINS_FILE", ""), "PORN_DOMAINS"),
        "PORN_KEYWORDS": (getattr(Config, "PORN_KEYWORDS_FILE", ""), "PORN_KEYWORDS"),
        "SUPPORTED_SITES": (getattr(Config, "SUPPORTED_SITES_FILE", ""), "SUPPORTED_SITES"),
    }
    for attr_name, (filepath, label) in file_map.items():
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                data = set(line.strip().lower() for line in f if line.strip())
            globals()[attr_name] = data
            logger.info(f"Loaded {len(data)} entries from {filepath}. Example: {list(data)[:5]}")
        except Exception as e:
            logger.error(f"Failed to load {filepath}: {e}")
            globals()[attr_name] = set()
    # results depend on the lists: forget memoised verdicts (matchers rebuild lazily)
    cache = globals().get("_is_porn_cached")
    if cache is not None:
        cache.cache_clear()
    # compile the keyword matchers now (~2 s for 15k keywords) instead of inside the first request
    if globals().get("_get_keyword_matchers") is not None:
        threading.Thread(target=_get_keyword_matchers, name="porn-matchers", daemon=True).start()


load_domain_lists()


# ---------------------------------------------------------------------------
#  Metadata text extraction for keyword check
# ---------------------------------------------------------------------------

METADATA_KEYS_FOR_KEYWORD_CHECK = (
    "uploader", "uploader_id", "channel", "channel_id", "creator", "artist",
    "album", "track",
    "series", "season", "episode",
    "playlist", "playlist_title", "playlist_id",
    "alt_title", "genre", "location", "license",
)


def get_metadata_text_for_keyword_check(info_dict):
    """
    Collects text from info_dict fields that may contain keywords (author names,
    album/series/playlist names, etc.). Used for NSFW check across all popular services.
    Returns raw string (keeps underscores) so white keywords can match literally.
    """
    if not info_dict or not isinstance(info_dict, dict):
        return ""
    parts: list[str] = []
    for key in METADATA_KEYS_FOR_KEYWORD_CHECK:
        val = info_dict.get(key)
        if val is None:
            continue
        if isinstance(val, str) and val.strip():
            parts.append(val.strip())
        elif isinstance(val, (int, float)) and key in ("season", "episode"):
            parts.append(str(val))
    for cat in info_dict.get("categories") or []:
        if isinstance(cat, str) and cat.strip():
            parts.append(cat.strip())
    for ch in info_dict.get("chapters") or []:
        if isinstance(ch, dict):
            t = ch.get("title")
            if isinstance(t, str) and t.strip():
                parts.append(t.strip())
    return " ".join(parts) or ""


# ---------------------------------------------------------------------------
#  Domain extraction & domain-level check
# ---------------------------------------------------------------------------

def extract_domain_parts(url):
    """Return ([all_domain_variants], base_domain) for a URL."""
    try:
        unwrapped = unwrap_redirect_url(url)
        ext = tldextract.extract(unwrapped)
        if ext.domain and ext.suffix:
            full_domain = f"{ext.domain}.{ext.suffix}".lower()
            subdomain = ext.subdomain.lower() if ext.subdomain else ""
            parts = [full_domain]
            if subdomain:
                sub_parts = subdomain.split(".")
                for i in range(len(sub_parts)):
                    parts.append(".".join(sub_parts[i:] + [full_domain]))
            return parts, ext.domain.lower()
        elif ext.domain:
            return [ext.domain.lower()], ext.domain.lower()
        else:
            return [url.lower()], url.lower()
    except Exception:
        parsed = urlparse(url)
        if parsed.netloc:
            return [parsed.netloc.lower()], parsed.netloc.lower()
        return [url.lower()], url.lower()


_LIST_SETS: dict = {}


def _config_set(name):
    """Config.WHITELIST / GREYLIST as a set, rebuilt only when the list object changes
    (reload_all_porn_caches assigns a new list)."""
    lst = getattr(Config, name, None) or ()
    cached = _LIST_SETS.get(name)
    if cached is None or cached[0] is not lst:
        cached = (lst, frozenset(str(d).lower() for d in lst))
        _LIST_SETS[name] = cached
    return cached[1]


def is_porn_domain(domain_parts):
    """Check if any domain variant is in PORN_DOMAINS (respects WHITELIST and GREYLIST)."""
    if _check_domain_whitelist(domain_parts):
        return False
    grey = _config_set("GREYLIST")
    if any(dom in grey for dom in domain_parts):
        return False
    return any(dom in PORN_DOMAINS for dom in domain_parts)


def _check_domain_whitelist(domain_parts):
    """Return True if any domain part is in WHITELIST."""
    white = _config_set("WHITELIST")
    return any(dom in white for dom in domain_parts)


# ---------------------------------------------------------------------------
#  Keyword matchers — compiled ONCE per keyword list, not per call
# ---------------------------------------------------------------------------
#
# PORN_KEYWORDS holds ~15k entries. The text check is one `\b(kw1|kw2|...)\b`
# regex and the URL check one delimiter-aware regex for all keywords (words of
# a keyword may be separated by any non-alphanumeric run: "big tits" matches
# "big-tits", "big_tits", "big%20tits"). Both are built as a trie so the regex
# engine does not try 15k alternatives at every position. Matching semantics are
# exactly those of the former per-call / per-keyword regexes.

_END = None
_URL_JOINER = r"[^A-Za-z0-9]+"


def _trie_regex(sequences, sep: str) -> str:
    """Regex alternation equivalent to `seq1|seq2|...`, factored as a trie.

    Each sequence is a list of literal tokens; consecutive tokens are joined by
    `sep` (empty for characters, the delimiter class for URL words).
    """
    root: dict = {}
    for seq in sequences:
        node = root
        for tok in seq:
            node = node.setdefault(tok, {})
        node[_END] = True

    def render(node) -> str:
        opts = []
        for tok in sorted(k for k in node if k is not _END):
            child = node[tok]
            piece = re.escape(tok)
            while len(child) == 1 and _END not in child:  # collapse single chains
                (nxt, child), = child.items()
                piece += sep + re.escape(nxt)
            if _END in child and len(child) == 1:
                opts.append(piece)
            else:
                opts.append(f"{piece}(?:{sep}{render(child)}){'?' if _END in child else ''}")
        return opts[0] if len(opts) == 1 else "(?:" + "|".join(opts) + ")"

    return render(root) if root else r"a^"


class _KeywordMatchers:
    __slots__ = ("source", "text_re", "url_re")

    def __init__(self, keywords):
        self.source = keywords
        kws = sorted({kw.lower() for kw in keywords if kw.strip()})
        if not kws:
            self.text_re = self.url_re = None
            return
        self.text_re = re.compile(r"\b(" + _trie_regex([list(kw) for kw in kws], "") + r")\b",
                                  flags=re.IGNORECASE)
        words = [kw.split() for kw in kws]
        self.url_re = re.compile(
            r"(?<![A-Za-z0-9])(?:" + _trie_regex([w for w in words if w], _URL_JOINER) + r")(?![A-Za-z0-9])",
            flags=re.IGNORECASE,
        )


class _WhiteMatcher:
    __slots__ = ("source", "regex")

    def __init__(self, keywords):
        self.source = keywords
        kws = [re.escape(kw.lower().strip()) for kw in keywords if kw.strip()]
        self.regex = re.compile(r"\b(" + "|".join(kws) + r")\b", flags=re.IGNORECASE) if kws else None


_matchers_lock = threading.Lock()
_kw_matchers = None
_white_matcher = None


def _get_keyword_matchers() -> "_KeywordMatchers":
    global _kw_matchers
    m = _kw_matchers
    if m is None or m.source is not PORN_KEYWORDS:
        with _matchers_lock:
            m = _kw_matchers
            if m is None or m.source is not PORN_KEYWORDS:
                t0 = time.perf_counter()
                m = _kw_matchers = _KeywordMatchers(PORN_KEYWORDS)
                logger.info(f"porn: compiled keyword matchers for {len(PORN_KEYWORDS)} keywords "
                            f"in {(time.perf_counter() - t0) * 1000:.0f} ms")
    return m


def _get_white_matcher() -> "_WhiteMatcher":
    global _white_matcher
    src = getattr(Config, "WHITE_KEYWORDS", None) or []
    m = _white_matcher
    if m is None or m.source is not src:
        m = _white_matcher = _WhiteMatcher(src)
    return m


def _prepare_lower(val):
    """Safely lowercase a string, returning empty string for None."""
    val = _as_text(val)
    return str(val).lower() if val else ""


def _check_white_keywords(combined_text):
    """Return (hit, matches) for white keywords (literal, word-boundary)."""
    regex = _get_white_matcher().regex
    if regex is None:
        return False, []
    matches = regex.findall(combined_text)
    return bool(matches), matches


def _check_text_keywords(text_to_check, keyword_pattern):
    """Find keyword matches in text. Returns list of matched keywords."""
    if not text_to_check or keyword_pattern is None:
        return []
    return keyword_pattern.findall(text_to_check)


def _check_url_keywords(url_lower, url_pattern=None):
    """Find keyword matches in URL using the delimiter-aware pattern."""
    if url_pattern is None:
        url_pattern = _get_keyword_matchers().url_re
    if url_pattern is None or not url_lower:
        return []
    return url_pattern.findall(url_lower)


# ---------------------------------------------------------------------------
#  is_porn  — fast boolean check (memoised)
# ---------------------------------------------------------------------------

def is_porn(url, title, description, caption=None, tags=None, uploader=None):
    """
    Fast boolean check: is content pornographic?
    Checks domain, title, description, caption, tags, URL, uploader via keywords.
    Domain whitelist has highest priority.

    The same URL is checked many times per request (menus, proxy choice, tags,
    sender, log routing), so results are memoised; the cache is dropped whenever
    the lists are reloaded.
    """
    args = tuple(_as_text(a) for a in (url, title, description, caption, tags, uploader))
    try:
        return _is_porn_cached(*args)
    except TypeError:  # still unhashable (exotic object): check without the cache
        return _is_porn_impl(*args)


def _as_text(val):
    """Lists/tuples/sets of tags or names -> one space-joined string (callers mix both)."""
    if isinstance(val, (list, tuple, set, frozenset)):
        return " ".join(str(v) for v in val if v is not None)
    return val


@functools.lru_cache(maxsize=1024)
def _is_porn_cached(url, title, description, caption, tags, uploader):
    return _is_porn_impl(url, title, description, caption, tags, uploader)


def _is_porn_impl(url, title, description, caption=None, tags=None, uploader=None):
    # 1. Domain check
    clean_url = unwrap_redirect_url(url).lower()
    domain_parts, _ = extract_domain_parts(clean_url)

    if _check_domain_whitelist(domain_parts):
        logger.debug(f"is_porn: domain in WHITELIST: {domain_parts}")
        return False

    if is_porn_domain(domain_parts):
        logger.info(f"is_porn: domain match: {domain_parts}")
        return True

    # 2. Prepare text
    title_lower = _prepare_lower(title)
    description_lower = _prepare_lower(description)
    caption_lower = _prepare_lower(caption)
    uploader_lower_raw = _prepare_lower(uploader)
    uploader_lower = uploader_lower_raw.replace("_", " ")
    tags_lower_raw = _prepare_lower(tags)
    tags_lower = tags_lower_raw.replace("_", " ") if tags else ""
    url_lower = clean_url

    if not any([title_lower, description_lower, caption_lower, tags_lower, uploader_lower, url_lower]):
        logger.debug("is_porn: all text fields, uploader and URL empty")
        return False

    # 3. White keywords (raw text, preserves underscores)
    combined_white = " ".join([title_lower, description_lower, caption_lower, tags_lower_raw, uploader_lower_raw, url_lower])
    white_hit, _ = _check_white_keywords(combined_white)
    if white_hit:
        logger.info("is_porn: white keyword match found, content considered clean")
        return False

    # 4. Keyword matchers (compiled once)
    matchers = _get_keyword_matchers()
    if matchers.text_re is None:
        return False

    # 5. Text fields check
    text_to_check = " ".join([title_lower, description_lower, caption_lower, tags_lower, uploader_lower])
    hit = matchers.text_re.search(text_to_check)
    if hit:
        logger.info(f"is_porn: keyword match in text fields: {hit.group(0)!r}")
        return True

    # 6. URL check with delimiter-aware patterns
    hit = matchers.url_re.search(url_lower)
    if hit:
        logger.info(f"is_porn: keyword match in URL: {hit.group(0)!r}")
        return True

    logger.debug("is_porn: no keyword matches found")
    return False


# ---------------------------------------------------------------------------
#  check_porn_detailed  — returns (bool, explanation_string)
# ---------------------------------------------------------------------------

def check_porn_detailed(url, title, description, caption=None, uploader=None):
    """
    Detailed porn check returning (is_porn, explanation).
    Delegates to shared helpers to avoid duplicating logic with is_porn().
    """
    _messages = safe_get_messages(None)
    explanation_parts: list[str] = []

    # 1. Domain check
    clean_url = unwrap_redirect_url(url).lower()
    domain_parts, _ = extract_domain_parts(clean_url)

    if _check_domain_whitelist(domain_parts):
        white = _config_set("WHITELIST")
        matching = [dom for dom in domain_parts if dom in white]
        explanation_parts.append(_messages.PORN_DOMAIN_WHITELIST_MSG.format(domain=matching[0]))
        return False, " | ".join(explanation_parts)

    if is_porn_domain(domain_parts):
        explanation_parts.append(_messages.PORN_DOMAIN_BLACKLIST_MSG.format(domain_parts=domain_parts))
        return True, " | ".join(explanation_parts)

    # 2. Prepare text
    title_lower = _prepare_lower(title)
    description_lower = _prepare_lower(description)
    caption_lower = _prepare_lower(caption)
    uploader_lower_raw = _prepare_lower(uploader)
    uploader_lower = uploader_lower_raw.replace("_", " ")
    url_lower = clean_url

    if not any([title_lower, description_lower, caption_lower, uploader_lower, url_lower]):
        explanation_parts.append(_messages.PORN_ALL_TEXT_FIELDS_EMPTY_MSG)
        return False, " | ".join(explanation_parts)

    # 3. White keywords
    combined_white = " ".join([title_lower, description_lower, caption_lower, uploader_lower_raw, url_lower])
    white_hit, white_matches = _check_white_keywords(combined_white)
    if white_hit:
        explanation_parts.append(
            _messages.PORN_WHITELIST_KEYWORDS_MSG.format(keywords=", ".join(set(white_matches)))
        )
        return False, " | ".join(explanation_parts)

    # 4. Keyword matchers (compiled once)
    matchers = _get_keyword_matchers()
    text_pattern = matchers.text_re
    if text_pattern is None:
        explanation_parts.append("ℹ️ No porn keywords loaded")
        return False, " | ".join(explanation_parts)

    # 5. Per-field text check with explanations
    def _kw_msg(key, keywords, default_fmt):
        msg = getattr(_messages, key, None)
        return (msg.format(keywords=keywords) if msg else default_fmt.format(keywords=keywords))

    field_checks = [
        (title_lower, "PORN_KEYWORDS_IN_TITLE_MSG", "❌ NSFW keywords in title: {keywords}"),
        (description_lower, "PORN_KEYWORDS_IN_DESCRIPTION_MSG", "❌ NSFW keywords in description: {keywords}"),
        (caption_lower, "PORN_KEYWORDS_IN_CAPTION_MSG", "❌ NSFW keywords in caption: {keywords}"),
        (uploader_lower, "PORN_KEYWORDS_IN_UPLOADER_MSG", "❌ NSFW keywords in channel/uploader/author: {keywords}"),
    ]

    found_any = False
    for text, msg_key, default_fmt in field_checks:
        matches = _check_text_keywords(text, text_pattern)
        if matches:
            explanation_parts.append(_kw_msg(msg_key, ", ".join(set(matches)), default_fmt))
            found_any = True

    if found_any:
        return True, " | ".join(explanation_parts)

    # 6. URL check
    url_matches = _check_url_keywords(url_lower, matchers.url_re)
    if url_matches:
        explanation_parts.append(f"🔗 NSFW keywords found in URL: {', '.join(set(url_matches))}")
        return True, " | ".join(explanation_parts)

    explanation_parts.append(_messages.PORN_NO_KEYWORDS_FOUND_MSG)
    return False, " | ".join(explanation_parts)


# ---------------------------------------------------------------------------
#  Runtime reload
# ---------------------------------------------------------------------------

def reload_all_porn_caches():
    """
    Reloads:
    - Text-based caches: PORN_DOMAINS, PORN_KEYWORDS, SUPPORTED_SITES
    - Config-based arrays from CONFIG/domains.py: WHITE_KEYWORDS, WHITELIST,
      GREYLIST, PROXY_1_DOMAINS, PROXY_2_DOMAINS, CLEAN_QUERY, NO_COOKIE_DOMAINS,
      BLACK_LIST, TIKTOK_DOMAINS, PIPED_DOMAIN.
    Returns a dict with counts for confirmation output.
    """
    try:
        import CONFIG.domains as domains_module
        domains_module = importlib.reload(domains_module)
    except Exception as e:
        logger.error(f"Failed to reload CONFIG.domains: {e}")
        domains_module = None

    try:
        DomainsCfg = domains_module.DomainsConfig if isinstance(domains_module, types.ModuleType) else DomainsConfig
        attrs_to_copy = [
            "WHITE_KEYWORDS", "WHITELIST", "GREYLIST", "PROXY_1_DOMAINS", "PROXY_2_DOMAINS",
            "CLEAN_QUERY", "NO_COOKIE_DOMAINS", "BLACK_LIST", "TIKTOK_DOMAINS", "PIPED_DOMAIN",
            "NO_PROXY_DOMAINS", "AUTO_PROXY_DOMAINS", "PROXY_ALL_NSFW",
        ]
        for name in attrs_to_copy:
            if hasattr(DomainsCfg, name):
                try:
                    setattr(Config, name, getattr(DomainsCfg, name))
                except Exception:
                    pass
    except Exception as e:
        logger.error(f"Failed to apply DomainsConfig to Config: {e}")

    load_domain_lists()

    try:
        from HELPERS.proxy_helper import _nsfw_proxy_cache
        _nsfw_proxy_cache.clear()
        logger.info("Cleared NSFW auto-proxy cache after reload")
    except Exception as e:
        logger.warning(f"Failed to clear NSFW auto-proxy cache: {e}")

    counts = {
        "porn_domains": len(PORN_DOMAINS),
        "porn_keywords": len(PORN_KEYWORDS),
        "supported_sites": len(SUPPORTED_SITES),
        "whitelist": len(getattr(Config, "WHITELIST", []) or []),
        "greylist": len(getattr(Config, "GREYLIST", []) or []),
        "black_list": len(getattr(Config, "BLACK_LIST", []) or []),
        "white_keywords": len(getattr(Config, "WHITE_KEYWORDS", []) or []),
        "proxy_domains": len(getattr(Config, "PROXY_1_DOMAINS", []) or []),
        "proxy_2_domains": len(getattr(Config, "PROXY_2_DOMAINS", []) or []),
        "clean_query": len(getattr(Config, "CLEAN_QUERY", []) or []),
        "no_cookie_domains": len(getattr(Config, "NO_COOKIE_DOMAINS", []) or []),
        "no_proxy_domains": len(getattr(Config, "NO_PROXY_DOMAINS", []) or []),
        "auto_proxy_domains": len(getattr(Config, "AUTO_PROXY_DOMAINS", []) or []),
        "ytdlp_only_domains": len(getattr(Config, "YTDLP_ONLY_DOMAINS", []) or []),
        "gallerydl_only_domains": len(getattr(Config, "GALLERYDL_ONLY_DOMAINS", []) or []),
        "gallerydl_only_path": len(getattr(Config, "GALLERYDL_ONLY_PATH", []) or []),
        "gallerydl_fallback_domains": len(getattr(Config, "GALLERYDL_FALLBACK_DOMAINS", []) or []),
        "no_filter_domains": len(getattr(Config, "NO_FILTER_DOMAINS", []) or []),
        "tiktok_domains": len(getattr(Config, "TIKTOK_DOMAINS", []) or []),
        "proxy_all_nsfw": getattr(Config, "PROXY_ALL_NSFW", False),
    }
    return counts
