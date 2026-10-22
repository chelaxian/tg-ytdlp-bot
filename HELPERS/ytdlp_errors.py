"""Retryability classification of yt-dlp / gallery-dl error strings.

Single source of truth for "does retrying this request make sense?". Used by
format discovery (get_video_formats), the download format cascade and the
proxy/cookie fallback chains so that a deterministic failure stops the whole
pipeline instead of producing one ERROR line per format/proxy/cookie attempt
(retry storms: issues #323, #352, #360, #362, #386, #468, #476, #477, #479).

yt-dlp exposes no stable error codes for extractor failures, so matching is
done on lower-cased message fragments. Keep every fragment here, not inline.
"""
import re

# Category codes returned by classify_retryability()
RATE_LIMITED = 'RATE_LIMITED'
PERMANENT = 'PERMANENT'
AUTH_REQUIRED = 'AUTH_REQUIRED'
CLIENT_HTTP_ERROR = 'CLIENT_HTTP_ERROR'
LOCAL_FILE_ERROR = 'LOCAL_FILE_ERROR'
FORMAT_UNAVAILABLE = 'FORMAT_UNAVAILABLE'
TRANSIENT = 'TRANSIENT'

RATE_LIMIT_INDICATORS = (
    'rate limit', 'rate-limit', 'rate-limited', 'too many requests',
    'http error 429', 'has been rate-limited',
    # YouTube "Please try again later" (issue #446) — server-side throttle;
    # retrying immediately only worsens it.
    'try again later', 'please try again',
)

PERMANENT_UNAVAILABLE_INDICATORS = (
    'does not exist', 'not exist',
    'no longer available', 'video unavailable', 'is unavailable', 'private video',
    "this content isn't available", 'this content is not available',
    'removed for violating', 'terms of service', 'has been removed',
    # Premiere not started yet (issue #387)
    'premieres in', 'premieres on',
    # YouTube bot-detection / PO token (issue #394) and the frontend
    # "page needs to be reloaded" challenge (issue #436): cookie/proxy/format
    # rotation never fixes them within one request.
    'sign in to confirm', 'not a bot', 'page needs to be reloaded',
    # Bot-check page without the expected player config: yt-dlp reports an
    # internal KeyError('INNERTUBE_CONTEXT') (issue #475).
    'innertube_context',
    # Members-only content (issue #352)
    'join this channel', 'members-only', "available to this channel's members",
    'members only content',
    # Age-restricted content (issue #360)
    'confirm your age', 'verify your age', 'age verification required',
    'inappropriate for some users',
    # YouTube community post / tab page (issue #391)
    'does not have a',
    # Upstream extractor regressions (issues #445, #450, #452)
    'unexpected response from webpage request',
    'skipping unsupported file type',
    # Facebook extractor found no video data in the page (photo/text post or
    # upstream breakage, issues #328, #484). A login wall is reported
    # separately by yt-dlp (login required), so cookies/proxies cannot help.
    'cannot parse data',
    # ok.ru extractor called json.loads() on an already-parsed dict (upstream
    # yt-dlp#17585, fixed in yt-dlp 2026.10.21; issues #469, #471).
    'the json object must be str, bytes or bytearray',
    # Instagram post inaccessible without an account (issue #373)
    'empty media response',
    'live event has ended',
)

# Errors fixable only by user-supplied cookies: one cookie fallback pass is
# allowed, after that the request is terminal (Douyin, issue #386).
AUTH_REQUIRED_INDICATORS = (
    'fresh cookies', 'cookies are needed', 'cookies needed', 'login required',
    'requires login', 'log in for access', 'authentication required',
)

# Local filesystem failures: the same attempt will fail again until the
# directory/file problem is fixed (issues #451, #460, #468, #478).
LOCAL_FILE_INDICATORS = (
    'does not look like a netscape format cookies file',
    'disk quota exceeded', 'no space left on device',
)

FORMAT_UNAVAILABLE_INDICATORS = (
    'requested format is not available',
    'requested format not available',
)

TRANSIENT_NETWORK_INDICATORS = (
    'read timed out', 'timed out', 'connection reset', 'connection aborted',
    'connection refused', 'temporary failure in name resolution',
    'name or service not known', 'remote end closed connection',
    'http error 500', 'http error 502', 'http error 503', 'http error 504',
)

# 4xx responses that no cookie, proxy or format change can turn into a
# success. 401/403 are excluded: cookies/impersonation legitimately fix them.
_CLIENT_HTTP_ERROR_RE = re.compile(r'http error (400|404|405|410|451)\b')


def _lower(error_text):
    return str(error_text or '').lower()


def is_rate_limited(error_text):
    low = _lower(error_text)
    return any(k in low for k in RATE_LIMIT_INDICATORS)


def is_permanent_unavailable(error_text):
    low = _lower(error_text)
    matches = [k for k in PERMANENT_UNAVAILABLE_INDICATORS if k in low]
    if not matches:
        return False
    # «Video unavailable» бывает префиксом геоблокировки. Не запрещаем
    # настроенный geo-proxy, если нет более конкретного признака удаления.
    from CONFIG.errors import is_geo_block_error
    ambiguous = {
        'video unavailable', 'is unavailable',
        "this content isn't available", 'this content is not available',
    }
    if is_geo_block_error(low) and all(k in ambiguous for k in matches):
        return False
    return True


def is_auth_required(error_text):
    low = _lower(error_text)
    return any(k in low for k in AUTH_REQUIRED_INDICATORS)


def is_client_http_error(error_text):
    return bool(_CLIENT_HTTP_ERROR_RE.search(_lower(error_text)))


def is_missing_local_file(error_text):
    """ENOENT on a local path (missing cookie file / download dir)."""
    low = _lower(error_text)
    return 'errno 2' in low or 'no such file or directory' in low


def is_local_file_error(error_text):
    low = _lower(error_text)
    return any(k in low for k in LOCAL_FILE_INDICATORS) or is_missing_local_file(low)


def is_format_unavailable(error_text):
    low = _lower(error_text)
    return any(k in low for k in FORMAT_UNAVAILABLE_INDICATORS)


def is_transient_network_error(error_text):
    low = _lower(error_text)
    return any(k in low for k in TRANSIENT_NETWORK_INDICATORS)


def classify_retryability(error_text):
    """Return a category code for an error string, or None if unknown.

    Order matters: rate limits and content state win over transport noise
    that often trails them in the same message.
    """
    if not error_text:
        return None
    if is_rate_limited(error_text):
        return RATE_LIMITED
    if is_permanent_unavailable(error_text):
        return PERMANENT
    if is_auth_required(error_text):
        return AUTH_REQUIRED
    if is_client_http_error(error_text):
        return CLIENT_HTTP_ERROR
    if is_local_file_error(error_text):
        return LOCAL_FILE_ERROR
    if is_format_unavailable(error_text):
        return FORMAT_UNAVAILABLE
    if is_transient_network_error(error_text):
        return TRANSIENT
    return None


def should_abort_retries(error_text):
    """True when no further format/proxy/cookie attempt can succeed.

    AUTH_REQUIRED is terminal here: callers run their single cookie fallback
    before consulting this helper.
    """
    return classify_retryability(error_text) in (
        RATE_LIMITED, PERMANENT, AUTH_REQUIRED, CLIENT_HTTP_ERROR, LOCAL_FILE_ERROR,
    )
