# Playlist utilities
# This module contains functions for playlist detection and processing

import re
from HELPERS.logger import logger

def is_playlist_with_range(text: str) -> bool:
    """
    Checks if the text contains a playlist range pattern like *1*3, 1*1000, *5*10, *-1*-100, or just * for full playlist.
    Returns True if a range is detected, False otherwise.
    """
    if not isinstance(text, str):
        return False

    # Look for patterns like *1*3, 1*1000, *5*10, *-1*-100, or standalone * for full playlist.
    # The bare * must be a standalone token (surrounded by whitespace or string
    # boundary), otherwise it matches asterisks inside URLs/words and wrongly
    # classifies single-video messages as playlists (issue #389).
    range_pattern = r'\*-?\d+\*-?\d+|-?\d+\*-?\d+|(?<!\S)\*(?!\S)'
    return bool(re.search(range_pattern, text))

# Хост music.youtube.com ищем только в позиции настоящего URL (после http(s)://),
# чтобы подстрока в query-параметре чужого сайта не давала ложного срабатывания
# (CodeQL py/incomplete-url-substring-sanitization).
_YT_MUSIC_URL_RE = re.compile(r'https?://(?:[a-z0-9-]+\.)*music\.youtube\.com(?=[/:?#]|$)', re.IGNORECASE)


def is_youtube_music_url(url: str) -> bool:
    """Return True if the text contains an http(s) URL pointing to YouTube Music (music.youtube.com)."""
    if not isinstance(url, str):
        return False
    return bool(_YT_MUSIC_URL_RE.search(url))


def is_playlist_url(url: str) -> bool:
    """
    Checks if the URL is a playlist URL by pattern matching.
    For YouTube: checks for https://youtube.com/playlist? list= pattern.
    Returns True if URL appears to be a playlist, False otherwise.
    """
    if not isinstance(url, str):
        return False
    
    url_lower = url.lower()
    
    # YouTube Music playlists reject the *N*M range / playlist_items syntax with HTTP 400
    # (issue #370). Treat them as non-playlist so no range is auto-appended and none is
    # parsed from a user-typed *N*M suffix.
    if is_youtube_music_url(url):
        return False
    
    # Check for YouTube playlist pattern: https://youtube.com/playlist? list= or https://www.youtube.com/playlist? list=
    if 'youtube.com/playlist' in url_lower and 'list=' in url_lower:
        return True
    if 'youtu.be' in url_lower and 'list=' in url_lower:
        return True
    
    # Can be extended for other platforms that use playlist URLs
    return False

def is_playlist_from_info_dict(info_dict: dict) -> bool:
    """
    Checks if the content is a playlist based on yt-dlp info_dict.
    Returns True if info_dict indicates a playlist, False otherwise.
    
    Args:
        info_dict: Dictionary returned by yt-dlp extract_info()
    
    Returns:
        True if playlist, False otherwise
    """
    try:
        if not isinstance(info_dict, dict):
            return False
        
        # Check for playlist type indicator
        if info_dict.get('_type') == 'playlist':
            return True
        
        # Check for entries list (playlists have entries)
        if 'entries' in info_dict:
            entries = info_dict.get('entries')
            # If entries is a list with more than 1 item, it's a playlist
            if isinstance(entries, list) and len(entries) > 1:
                return True
            # If entries is a list with 1 item, it might be a playlist or single video
            # Check if there's a playlist_count or playlist_id to confirm
            if isinstance(entries, list) and len(entries) == 1:
                if 'playlist_count' in info_dict or 'playlist_id' in info_dict:
                    return True
        
        # Check for _playlist_entries (alternative key used in some cases)
        if '_playlist_entries' in info_dict:
            playlist_entries = info_dict.get('_playlist_entries')
            if isinstance(playlist_entries, list) and len(playlist_entries) > 1:
                return True
        
        # Check for playlist_count (indicates playlist)
        playlist_count = info_dict.get('playlist_count')
        if playlist_count is not None and playlist_count > 1:
            return True
        
        # Check for playlist_id (indicates playlist, even if only 1 entry)
        if 'playlist_id' in info_dict and info_dict.get('playlist_id'):
            return True
        
        return False
    except Exception as e:
        logger.error(f"Error in is_playlist_from_info_dict: {e}", exc_info=True)
        return False

# ---------------------------------------------------------------------------
# Playlist ranges: URL*start*end (also /vid start-end URL)
#   *1*5   -> 1, 2, 3, 4, 5            (forward)
#   *5*1   -> 5, 4, 3, 2, 1            (reverse)
#   *-1*-5 -> last, 2nd from end ... 5th from end
#   *-5*-1 -> 5th from end ... last
# One definition of "how many" and "which, in what order" for every caller.
# ---------------------------------------------------------------------------

def range_count(start: int, end: int) -> int:
    """Number of items in an inclusive playlist range, in either direction."""
    return abs(int(end) - int(start)) + 1


def range_indices(start: int, end: int) -> list:
    """Indices of an inclusive range in the order the user asked for."""
    start, end = int(start), int(end)
    step = 1 if end >= start else -1
    return list(range(start, end + step, step))


def resolve_negative_indices(indices, total: int) -> list:
    """Map negative (from-the-end) indices to 1-based positions; order is kept.

    Positions outside 1..total are dropped (a range longer than the playlist).
    """
    out = []
    for i in indices:
        pos = total + i + 1 if i < 0 else i
        if 1 <= pos <= total:
            out.append(pos)
    return out


_TOTAL_CACHE = {}
_TOTAL_CACHE_TTL = 600  # seconds: the menu and the download that follows reuse one lookup


def get_playlist_total(url: str, user_id=None, cookies_already_checked: bool = True, use_proxy: bool = False):
    """Real number of items in a playlist, or None if it cannot be determined.

    Asks yt-dlp for the LAST item only (playlist_items='-1'): its playlist_index is
    the playlist length. The old code asked for item 1 and took len(entries), which
    is always 1, so *-1*-5 was mapped to positions 1, 0, -1...
    """
    import time
    key = (user_id, url)
    hit = _TOTAL_CACHE.get(key)
    now = time.time()
    if hit and now - hit[1] < _TOTAL_CACHE_TTL:
        return hit[0]
    total = None
    try:
        from DOWN_AND_UP.yt_dlp_hook import get_video_formats
        info = get_video_formats(url, user_id, -1, cookies_already_checked, use_proxy, None)
        if isinstance(info, dict) and not info.get('error'):
            for k in ('playlist_count', 'playlist_index'):
                v = info.get(k)
                if isinstance(v, int) and v > 0:
                    total = v
                    break
    except Exception as e:
        logger.warning(f"get_playlist_total failed for {url}: {e}")
    if total:
        _TOTAL_CACHE[key] = (total, now)
        if len(_TOTAL_CACHE) > 512:
            for k in sorted(_TOTAL_CACHE, key=lambda k: _TOTAL_CACHE[k][1])[:256]:
                _TOTAL_CACHE.pop(k, None)
    logger.info(f"get_playlist_total: {url} -> {total}")
    return total


def playlist_indices_for_range(start: int, end: int, url: str = None, user_id=None,
                               cookies_already_checked: bool = True, use_proxy: bool = False) -> list:
    """Positive 1-based indices for a range, resolving from-the-end indices once.

    If the playlist length is unknown, negative indices are returned unchanged
    (yt-dlp itself understands them).
    """
    idx = range_indices(start, end)
    if min(start, end) < 0 and url:
        total = get_playlist_total(url, user_id, cookies_already_checked, use_proxy)
        if total:
            return resolve_negative_indices(idx, total)
    return idx

_CMD_RANGE_RE = re.compile(r'^(-?\d+)-(-?\d*)$')


def command_args_to_range_text(args, max_items: int):
    """'/vid 3-7 URL #tag' arguments -> 'URL*3*7 #tag' (also used by /audio).

    args: the words after the command. Returns None when args[0] is not a range.
      3-7   -> *3*7        -3-7 / -3--7 -> *-3*-7 (counted from the end)
      3-    -> *3*(3+max-1)   -3- -> *-3*(-3-max+1)   (open end: up to the limit)
    The range is attached to the URL itself, so words after the URL (#tags,
    a playlist name) no longer swallow it.
    """
    if len(args) < 2:
        return None
    m = _CMD_RANGE_RE.match(args[0])
    if not m:
        return None
    start = int(m.group(1))
    if start == 0:
        return None
    if m.group(2) == '':
        step = 1 if start > 0 else -1
        end = start + step * (max(1, int(max_items)) - 1)
    else:
        end = int(m.group(2))
        if start < 0 and end > 0:
            end = -end
        if end == 0 or (start > 0 and end < 0):
            return None
    url, rest = args[1], args[2:]
    return ' '.join([f"{url}*{start}*{end}"] + list(rest))
