"""Netscape cookie file validation, quarantine and atomic writes.

yt-dlp loads cookie files through http.cookiejar.MozillaCookieJar, which
rejects any file whose FIRST line does not match "#( Netscape)? HTTP Cookie File"
with "'<path>' does not look like a Netscape format cookies file". An empty or
truncated file (e.g. written while the disk quota was exceeded, Errno 122) or
an HTML/JSON error page saved as cookie.txt failed every request of the user
(issue #478: 25x/24h). Helpers here let callers validate before use, move a
broken file out of the way (so the user falls back to no-cookie mode instead
of retrying with the same broken file) and write cookie files atomically.

Dependency-free on purpose (no Pyrogram/app imports): used by the bot, the
downloads janitor and isolated tests.
"""
import logging
import os
import re

from HELPERS.atomic_io import atomic_write_bytes

logger = logging.getLogger(__name__)

# Same pattern http.cookiejar.MozillaCookieJar.magic_re uses (re.search on line 1)
_NETSCAPE_MAGIC_RE = re.compile(r"#( Netscape)? HTTP Cookie File")
_COOKIE_ENTRY_FIELDS = 7
_HTTPONLY_PREFIX = "#HttpOnly_"
# Larger files are not plausible cookie jars (the bot also rejects >100 KB downloads)
MAX_COOKIE_FILE_BYTES = 1024 * 1024


def validate_cookie_bytes(content, require_entries=True):
    """Return (ok, reason) for raw cookie file content."""
    if not content:
        return False, "empty file"
    if len(content) > MAX_COOKIE_FILE_BYTES:
        return False, f"file too large ({len(content)} bytes)"
    text = content.decode("utf-8", errors="replace")
    lines = text.splitlines()
    first = lines[0] if lines else ""
    if not _NETSCAPE_MAGIC_RE.search(first):
        stripped = text.lstrip()
        if stripped[:1] in ("{", "["):
            return False, "JSON content, not Netscape format"
        if stripped[:1] == "<":
            return False, "HTML content, not Netscape format"
        return False, "missing '# Netscape HTTP Cookie File' header"
    entries = 0
    for line in lines[1:]:
        if line.startswith(_HTTPONLY_PREFIX):
            line = line[len(_HTTPONLY_PREFIX):]
        if not line.strip() or line.startswith("#"):
            continue
        fields = line.split("\t")
        if len(fields) != _COOKIE_ENTRY_FIELDS:
            return False, "malformed cookie entry (expected 7 tab-separated fields)"
        domain, domain_flag, path, secure, expires, name, value = fields
        if domain_flag not in ('TRUE', 'FALSE') or secure not in ('TRUE', 'FALSE'):
            return False, "invalid cookie boolean field"
        if (domain_flag == 'TRUE') != domain.startswith('.'):
            return False, "cookie domain flag does not match domain"
        if expires and not expires.isdigit():
            return False, "invalid cookie expiration"
        entries += 1
    if require_entries and not entries:
        return False, "no cookie entries"
    return True, ""


def validate_cookie_file(path, require_entries=False):
    """Return (ok, reason) for a cookie file on disk.

    By default only the header is required: that is exactly what yt-dlp
    rejects. Pass require_entries=True for freshly downloaded content.
    """
    try:
        size = os.path.getsize(path)
        if size > MAX_COOKIE_FILE_BYTES:
            return False, f"file too large ({size} bytes)"
        with open(path, "rb") as fh:
            content = fh.read()
    except FileNotFoundError:
        return False, "missing"
    except OSError as e:
        return False, f"unreadable: {e}"
    return validate_cookie_bytes(content, require_entries=require_entries)


def quarantine_cookie_file(path, reason=""):
    """Move a broken cookie file aside (<path>.invalid, previous one replaced).

    Returns True if the file was moved. The content is kept for diagnostics but
    no code path picks it up any more, so the user falls back to no-cookie mode.
    """
    target = f"{path}.invalid"
    try:
        os.replace(path, target)
    except FileNotFoundError:
        return False
    except OSError as e:
        logger.warning(f"[cookies] Could not quarantine invalid cookie file {path}: {e}")
        return False
    logger.warning(f"[cookies] Invalid cookie file quarantined: {path} -> {target} ({reason})")
    return True


def ensure_valid_cookie_file(path):
    """Return path if it is a valid Netscape cookie file, else None.

    An existing but invalid file is quarantined so it is never passed to
    yt-dlp again (issue #478); a missing file simply returns None.
    """
    if not path:
        return None
    ok, reason = validate_cookie_file(path)
    if ok:
        return path
    if reason != "missing":
        quarantine_cookie_file(path, reason)
    return None


# yt-dlp hands HLS/DASH to ffmpeg without any network timeout: when the server
# stops answering, ffmpeg waits in poll() forever (2026-11-05: four downloads hung
# for ~3 h with 0 bytes, the task never finished and kept the bot "busy").
# -rw_timeout (microseconds) applies to connect and every read, and the HLS demuxer
# passes it on to each segment request.
FFMPEG_STALL_TIMEOUT_US = 60_000_000


def with_ffmpeg_stall_timeout(options):
    """Return options with an ffmpeg input -rw_timeout, unless ffmpeg input args are already set."""
    extra = options.get('external_downloader_args')
    if extra is None:
        extra = {}
    elif isinstance(extra, dict):
        extra = dict(extra)
    else:
        return options  # a plain list applies to every downloader: leave the user's choice alone
    if any(key in extra for key in ('ffmpeg_i', 'ffmpeg_i1')):
        return options
    extra['ffmpeg_i'] = ['-rw_timeout', str(FFMPEG_STALL_TIMEOUT_US)]
    result = options.copy()
    result['external_downloader_args'] = extra
    return result


def validated_cookie_options(options):
    """Проверить cookiefile непосредственно перед созданием YoutubeDL (#478).

    Also the single choke point before almost every YoutubeDL(): adds the ffmpeg
    stall timeout (see with_ffmpeg_stall_timeout).
    """
    result = with_ffmpeg_stall_timeout(options.copy())
    if result.get('cookiefile'):
        result['cookiefile'] = ensure_valid_cookie_file(result['cookiefile'])
    return result


def write_cookie_file(path, content):
    """Atomically write cookie content (bytes or str) to path.

    A failed write (disk quota, ENOSPC) leaves the previous file intact instead
    of a truncated one that yt-dlp would reject (issues #460, #478).
    Raises OSError on failure.
    """
    if isinstance(content, str):
        content = content.encode("utf-8")
    ok, reason = validate_cookie_bytes(content, require_entries=False)
    if not ok:
        raise ValueError(f'Invalid Netscape cookie content: {reason}')
    atomic_write_bytes(path, content)
