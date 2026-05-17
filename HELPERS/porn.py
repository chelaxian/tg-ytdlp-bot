import importlib
import re
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


def is_porn_domain(domain_parts):
    """Check if any domain variant is in PORN_DOMAINS (respects WHITELIST and GREYLIST)."""
    for dom in domain_parts:
        if dom in Config.WHITELIST:
            return False
    for dom in domain_parts:
        if dom in Config.GREYLIST:
            return False
    for dom in domain_parts:
        if dom in PORN_DOMAINS:
            return True
    return False


# ---------------------------------------------------------------------------
#  Shared helpers for keyword matching
# ---------------------------------------------------------------------------

def _compile_url_keyword_regex(raw_keyword: str) -> re.Pattern:
    """Build delimiter-aware regex for keyword matching inside URLs."""
    words = [re.escape(w) for w in raw_keyword.split() if w]
    if not words:
        return re.compile(r"a^")
    joiner = r"[^A-Za-z0-9]+"
    core = joiner.join(words)
    return re.compile(rf"(?<![A-Za-z0-9])(?:{core})(?![A-Za-z0-9])", flags=re.IGNORECASE)


def _prepare_lower(val):
    """Safely lowercase a string, returning empty string for None."""
    return val.lower() if val else ""


def _check_domain_whitelist(domain_parts):
    """Return True if any domain part is in WHITELIST."""
    return any(dom in Config.WHITELIST for dom in domain_parts)


def _check_white_keywords(combined_text):
    """Return True if any white keyword matches (literal, word-boundary)."""
    white_keywords = getattr(Config, "WHITE_KEYWORDS", [])
    if not white_keywords:
        return False, []
    white_kws = [re.escape(kw.lower().strip()) for kw in white_keywords if kw.strip()]
    if not white_kws:
        return False, []
    pattern = re.compile(r"\b(" + "|".join(white_kws) + r")\b", flags=re.IGNORECASE)
    matches = pattern.findall(combined_text)
    return bool(matches), matches


def _check_text_keywords(text_to_check, keyword_pattern):
    """Find keyword matches in text. Returns list of matched keywords."""
    if not text_to_check:
        return []
    return keyword_pattern.findall(text_to_check)


def _check_url_keywords(url_lower, raw_keywords):
    """Find keyword matches in URL using delimiter-aware patterns."""
    matches = []
    for raw_kw in raw_keywords:
        url_pattern = _compile_url_keyword_regex(raw_kw)
        found = url_pattern.findall(url_lower)
        if found:
            matches.extend(found)
    return matches


def _build_text_pattern():
    """Compile the porn-keywords word-boundary regex from PORN_KEYWORDS."""
    text_kws = [re.escape(kw.lower()) for kw in PORN_KEYWORDS if kw.strip()]
    if not text_kws:
        return None, []
    pattern = re.compile(r"\b(" + "|".join(text_kws) + r")\b", flags=re.IGNORECASE)
    return pattern, [kw.lower() for kw in PORN_KEYWORDS if kw.strip()]


# ---------------------------------------------------------------------------
#  is_porn  — fast boolean check
# ---------------------------------------------------------------------------

def is_porn(url, title, description, caption=None, tags=None, uploader=None):
    """
    Fast boolean check: is content pornographic?
    Checks domain, title, description, caption, tags, URL, uploader via keywords.
    Domain whitelist has highest priority.
    """
    # 1. Domain check
    clean_url = unwrap_redirect_url(url).lower()
    domain_parts, _ = extract_domain_parts(clean_url)

    if _check_domain_whitelist(domain_parts):
        logger.info(f"is_porn: domain in WHITELIST: {domain_parts}")
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
        logger.info("is_porn: all text fields, uploader and URL empty")
        return False

    # 3. White keywords (raw text, preserves underscores)
    combined_white = " ".join([title_lower, description_lower, caption_lower, tags_lower_raw, uploader_lower_raw, url_lower])
    white_hit, _ = _check_white_keywords(combined_white)
    if white_hit:
        logger.info("is_porn: white keyword match found, content considered clean")
        return False

    # 4. Build keyword pattern
    text_pattern, url_kws = _build_text_pattern()
    if text_pattern is None:
        return False

    # 5. Text fields check
    text_to_check = " ".join([title_lower, description_lower, caption_lower, tags_lower, uploader_lower])
    if text_pattern.search(text_to_check):
        logger.info(f"is_porn: keyword match in text fields (regex): {text_pattern.pattern}")
        return True

    # 6. URL check with delimiter-aware patterns
    if _check_url_keywords(url_lower, url_kws):
        logger.info("is_porn: keyword match in URL with delimiters")
        return True

    logger.info("is_porn: no keyword matches found")
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
        matching = [dom for dom in domain_parts if dom in Config.WHITELIST]
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

    # 4. Build keyword pattern
    text_pattern, url_kws = _build_text_pattern()
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
    url_matches = _check_url_keywords(url_lower, url_kws)
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
      GREYLIST, PROXY_DOMAINS, PROXY_2_DOMAINS, CLEAN_QUERY, NO_COOKIE_DOMAINS,
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
            "WHITE_KEYWORDS", "WHITELIST", "GREYLIST", "PROXY_DOMAINS", "PROXY_2_DOMAINS",
            "CLEAN_QUERY", "NO_COOKIE_DOMAINS", "BLACK_LIST", "TIKTOK_DOMAINS", "PIPED_DOMAIN",
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

    counts = {
        "porn_domains": len(PORN_DOMAINS),
        "porn_keywords": len(PORN_KEYWORDS),
        "supported_sites": len(SUPPORTED_SITES),
        "whitelist": len(getattr(Config, "WHITELIST", []) or []),
        "greylist": len(getattr(Config, "GREYLIST", []) or []),
        "black_list": len(getattr(Config, "BLACK_LIST", []) or []),
        "white_keywords": len(getattr(Config, "WHITE_KEYWORDS", []) or []),
        "proxy_domains": len(getattr(Config, "PROXY_DOMAINS", []) or []),
        "proxy_2_domains": len(getattr(Config, "PROXY_2_DOMAINS", []) or []),
        "clean_query": len(getattr(Config, "CLEAN_QUERY", []) or []),
        "no_cookie_domains": len(getattr(Config, "NO_COOKIE_DOMAINS", []) or []),
    }
    return counts
