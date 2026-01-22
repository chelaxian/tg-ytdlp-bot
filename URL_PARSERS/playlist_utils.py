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

    # Look for patterns like *1*3, 1*1000, *5*10, *-1*-100, or just * for full playlist (поддерживаем отрицательные числа)
    range_pattern = r'\*-?\d+\*-?\d+|-?\d+\*-?\d+|\*'
    return bool(re.search(range_pattern, text))

def is_playlist_url(url: str) -> bool:
    """
    Checks if the URL is a playlist URL by pattern matching.
    For YouTube: checks for https://youtube.com/playlist?list= pattern.
    Returns True if URL appears to be a playlist, False otherwise.
    """
    if not isinstance(url, str):
        return False
    
    url_lower = url.lower()
    
    # Check for YouTube playlist pattern: https://youtube.com/playlist?list= or https://www.youtube.com/playlist?list=
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
    if 'playlist_count' in info_dict and info_dict.get('playlist_count', 0) > 1:
        return True
    
    # Check for playlist_id (indicates playlist, even if only 1 entry)
    if 'playlist_id' in info_dict and info_dict.get('playlist_id'):
        return True
    
    return False 