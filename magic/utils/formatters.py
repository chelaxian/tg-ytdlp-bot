"""
Formatting utilities for file sizes, time, captions, and filenames
"""
import re
import os
from typing import Tuple


def humanbytes(size):
    """
    Convert bytes to human readable format
    https://stackoverflow.com/a/49361727/4723940
    2 ** 10 = 1024
    """
    if not size:
        return "0B"
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    """
    Format milliseconds to human readable time format
    """
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]


def truncate_caption(
    title: str,
    description: str,
    url: str,
    tags_text: str = '',
    max_length: int = 1000  # Reduced from 1024 to be safe with encoding issues
) -> Tuple[str, str, str, str, str, bool]:
    """
    Truncate caption to fit Telegram limits while preserving important information
    
    Returns:
        Tuple of (title, description, url, tags_text, formatted_caption, was_truncated)
    """
    # Clean inputs
    title = title.strip() if title else "Video"
    description = description.strip() if description else ""
    url = url.strip() if url else ""
    tags_text = tags_text.strip() if tags_text else ""
    
    # Start building caption
    caption_parts = []
    
    # Title (always include, but may truncate)
    if title:
        caption_parts.append(f"<b>{title}</b>")
    
    # Tags (high priority)
    if tags_text:
        caption_parts.append(tags_text)
    
    # URL (medium priority)  
    if url:
        caption_parts.append(f"🔗 {url}")
    
    # Description (lowest priority, most likely to be truncated)
    if description:
        caption_parts.append(description)
    
    # Join parts and check length
    caption = "\n\n".join(caption_parts)
    was_truncated = False
    
    # If too long, start truncating from the end
    if len(caption) > max_length:
        was_truncated = True
        
        # Try removing description first
        if description:
            caption_parts = caption_parts[:-1]  # Remove description
            caption = "\n\n".join(caption_parts)
        
        # If still too long, truncate URL
        if len(caption) > max_length and url:
            caption_parts = [part for part in caption_parts if not part.startswith("🔗")]
            caption = "\n\n".join(caption_parts)
        
        # If still too long, truncate title
        if len(caption) > max_length:
            # Keep tags, truncate title
            available_length = max_length - len(tags_text) - 10  # Buffer
            if available_length > 20:  # Minimum viable title length
                truncated_title = title[:available_length-3] + "..."
                caption_parts[0] = f"<b>{truncated_title}</b>"
                caption = "\n\n".join(caption_parts)
            else:
                # Extreme case: just show truncated title
                caption = f"<b>{title[:max_length-10]}...</b>"
    
    # Final safety check
    if len(caption) > max_length:
        caption = caption[:max_length-3] + "..."
        was_truncated = True
    
    return title, description, url, tags_text, caption, was_truncated


def sanitize_filename(filename, max_length=150):
    """
    Sanitize filename for safe file system usage
    
    Args:
        filename: Original filename
        max_length: Maximum length for the filename
        
    Returns:
        Sanitized filename
    """
    if not filename:
        return "video"
    
    # Remove or replace problematic characters
    # Replace path separators and other dangerous chars
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    
    # Replace multiple spaces with single space
    filename = re.sub(r'\s+', ' ', filename)
    
    # Remove leading/trailing spaces and dots
    filename = filename.strip(' .')
    
    # Remove control characters
    filename = ''.join(char for char in filename if ord(char) >= 32)
    
    # Handle very long filenames
    if len(filename) > max_length:
        # Try to preserve file extension if present
        name_parts = filename.rsplit('.', 1)
        if len(name_parts) == 2 and len(name_parts[1]) <= 10:
            # Has extension
            name, ext = name_parts
            available_length = max_length - len(ext) - 1
            filename = name[:available_length] + '.' + ext
        else:
            # No extension or extension too long
            filename = filename[:max_length]
    
    # Ensure we don't have empty filename
    if not filename or filename.isspace():
        filename = "video"
    
    return filename 