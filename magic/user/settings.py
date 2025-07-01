"""
User settings and preferences management
"""
import os
import logging
from typing import Optional, Dict, Any
from config import Config
from ..database.firebase import db_child_by_path
from ..database.firebase import logger


logger = logging.getLogger(__name__)


def get_user_setting(user_id: int, setting_name: str, default_value: Any = None) -> Any:
    """
    Get user setting from file
    
    Args:
        user_id: User ID
        setting_name: Name of the setting file (without .txt extension)
        default_value: Default value if setting doesn't exist
        
    Returns:
        Setting value or default_value
    """
    from magic.utils.filesystem import create_directory
    
    try:
        user_dir = os.path.join("users", str(user_id))
        setting_file = os.path.join(user_dir, f"{setting_name}.txt")
        
        if os.path.exists(setting_file):
            with open(setting_file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                
                # Try to convert to appropriate type
                if content.lower() in ('true', 'false'):
                    return content.lower() == 'true'
                elif content.isdigit():
                    return int(content)
                elif content.replace('.', '').isdigit():
                    return float(content)
                else:
                    return content
        
        return default_value
        
    except Exception as e:
        logger.error(f"Error getting user setting {setting_name} for user {user_id}: {e}")
        return default_value


def set_user_setting(user_id: int, setting_name: str, value: Any) -> bool:
    """
    Set user setting to file
    
    Args:
        user_id: User ID
        setting_name: Name of the setting file (without .txt extension)
        value: Value to set
        
    Returns:
        True if successful, False otherwise
    """
    from magic.utils.filesystem import create_directory
    
    try:
        user_dir = os.path.join("users", str(user_id))
        create_directory(user_dir)
        
        setting_file = os.path.join(user_dir, f"{setting_name}.txt")
        
        with open(setting_file, "w", encoding="utf-8") as f:
            f.write(str(value))
        
        logger.info(f"Set user setting {setting_name}={value} for user {user_id}")
        return True
        
    except Exception as e:
        logger.error(f"Error setting user setting {setting_name} for user {user_id}: {e}")
        return False


def delete_user_setting(user_id: int, setting_name: str) -> bool:
    """
    Delete user setting file
    
    Args:
        user_id: User ID
        setting_name: Name of the setting file (without .txt extension)
        
    Returns:
        True if successful, False otherwise
    """
    try:
        user_dir = os.path.join("users", str(user_id))
        setting_file = os.path.join(user_dir, f"{setting_name}.txt")
        
        if os.path.exists(setting_file):
            os.remove(setting_file)
            logger.info(f"Deleted user setting {setting_name} for user {user_id}")
            return True
        
        return False
        
    except Exception as e:
        logger.error(f"Error deleting user setting {setting_name} for user {user_id}: {e}")
        return False


def get_user_quality(user_id: int) -> str:
    """Get user's preferred quality setting"""
    from config import Config
    
    quality = get_user_setting(user_id, "format", Config.DEFAULT_QUALITY)
    
    # Validate quality
    if quality not in Config.QUALITY_KEYWORDS:
        quality = Config.DEFAULT_QUALITY
        set_user_setting(user_id, "format", quality)
    
    return quality


def set_user_quality(user_id: int, quality: str) -> bool:
    """Set user's preferred quality setting"""
    from config import Config
    
    if quality not in Config.QUALITY_KEYWORDS:
        return False
    
    return set_user_setting(user_id, "format", quality)


def get_user_split_size(user_id: int) -> int:
    """Get user's preferred split size for large videos"""
    try:
        # This will be set up properly when db is available
        from ..database.firebase import db, db_child_by_path, logger
        data = db_child_by_path(db, f"user_settings/{user_id}/split_size").get().val()
        if data and isinstance(data, (int, float)) and data > 0:
            return int(data)
        return Config.DEFAULT_SPLIT_SIZE if hasattr(Config, 'DEFAULT_SPLIT_SIZE') else None
    except Exception as e:
        print(f"Error getting user split size: {e}")
        return None


def set_user_split_size(user_id: int, size_bytes: int) -> bool:
    """Set user's preferred split size"""
    try:
        from ..database.firebase import db, db_child_by_path, logger
        db_child_by_path(db, f"user_settings/{user_id}/split_size").set(size_bytes)
        print(f"Split size updated for user {user_id}: {size_bytes}")
        return True
    except Exception as e:
        print(f"Error setting user split size: {e}")
        return False


def get_user_mediainfo_enabled(user_id: int) -> bool:
    """Check if user has mediainfo enabled"""
    return get_user_setting(user_id, "mediainfo", False)


def set_user_mediainfo_enabled(user_id: int, enabled: bool) -> bool:
    """Set user's mediainfo setting"""
    return set_user_setting(user_id, "mediainfo", enabled)


def get_user_thumbnail_enabled(user_id: int) -> bool:
    """Check if user has custom thumbnails enabled"""
    return get_user_setting(user_id, "thumbnail", True)


def set_user_thumbnail_enabled(user_id: int, enabled: bool) -> bool:
    """Set user's thumbnail setting"""
    return set_user_setting(user_id, "thumbnail", enabled)


def get_user_caption_enabled(user_id: int) -> bool:
    """Check if user has captions enabled"""
    return get_user_setting(user_id, "caption", True)


def set_user_caption_enabled(user_id: int, enabled: bool) -> bool:
    """Set user's caption setting"""
    return set_user_setting(user_id, "caption", enabled)


def get_user_auto_tags_enabled(user_id: int) -> bool:
    """Check if user has auto tags enabled"""
    return get_user_setting(user_id, "auto_tags", True)


def set_user_auto_tags_enabled(user_id: int, enabled: bool) -> bool:
    """Set user's auto tags setting"""
    return set_user_setting(user_id, "auto_tags", enabled)


def get_all_user_settings(user_id: int) -> Dict[str, Any]:
    """Get all user settings as a dictionary"""
    from config import Config
    
    settings = {
        'quality': get_user_quality(user_id),
        'split_size_mb': get_user_split_size(user_id),
        'mediainfo': get_user_mediainfo_enabled(user_id),
        'thumbnail': get_user_thumbnail_enabled(user_id),
        'caption': get_user_caption_enabled(user_id),
        'auto_tags': get_user_auto_tags_enabled(user_id)
    }
    
    return settings


def format_settings_text(user_id: int) -> str:
    """Format user settings for display"""
    settings = get_all_user_settings(user_id)
    
    text = "🔧 <b>Your Current Settings:</b>\n\n"
    
    text += f"📺 <b>Quality:</b> {settings['quality']}\n"
    text += f"✂️ <b>Split Size:</b> {settings['split_size_mb']} MB\n"
    text += f"📊 <b>MediaInfo:</b> {'✅ Enabled' if settings['mediainfo'] else '❌ Disabled'}\n"
    text += f"🖼 <b>Thumbnails:</b> {'✅ Enabled' if settings['thumbnail'] else '❌ Disabled'}\n"
    text += f"📝 <b>Captions:</b> {'✅ Enabled' if settings['caption'] else '❌ Disabled'}\n"
    text += f"🏷 <b>Auto Tags:</b> {'✅ Enabled' if settings['auto_tags'] else '❌ Disabled'}\n"
    
    return text


def reset_user_settings(user_id: int) -> bool:
    """Reset all user settings to defaults"""
    from config import Config
    
    try:
        settings = {
            'format': Config.DEFAULT_QUALITY,
            'split_size': Config.DEFAULT_SPLIT_SIZE_MB,
            'mediainfo': False,
            'thumbnail': True,
            'caption': True,
            'auto_tags': True
        }
        
        for setting_name, default_value in settings.items():
            set_user_setting(user_id, setting_name, default_value)
        
        logger.info(f"Reset all settings for user {user_id}")
        return True
        
    except Exception as e:
        logger.error(f"Error resetting settings for user {user_id}: {e}")
        return False


def export_user_settings(user_id: int) -> Optional[str]:
    """Export user settings as a string"""
    try:
        settings = get_all_user_settings(user_id)
        
        export_data = []
        for key, value in settings.items():
            export_data.append(f"{key}={value}")
        
        return "|".join(export_data)
        
    except Exception as e:
        logger.error(f"Error exporting settings for user {user_id}: {e}")
        return None


def import_user_settings(user_id: int, settings_string: str) -> bool:
    """Import user settings from a string"""
    try:
        settings_pairs = settings_string.split("|")
        
        for pair in settings_pairs:
            if "=" not in pair:
                continue
                
            key, value = pair.split("=", 1)
            
            # Convert value to appropriate type
            if value.lower() in ('true', 'false'):
                value = value.lower() == 'true'
            elif value.isdigit():
                value = int(value)
            elif value.replace('.', '').isdigit():
                value = float(value)
            
            # Set the setting
            if key == 'quality':
                set_user_quality(user_id, value)
            elif key == 'split_size_mb':
                set_user_split_size(user_id, value)
            elif key == 'mediainfo':
                set_user_mediainfo_enabled(user_id, value)
            elif key == 'thumbnail':
                set_user_thumbnail_enabled(user_id, value)
            elif key == 'caption':
                set_user_caption_enabled(user_id, value)
            elif key == 'auto_tags':
                set_user_auto_tags_enabled(user_id, value)
        
        logger.info(f"Imported settings for user {user_id}")
        return True
        
    except Exception as e:
        logger.error(f"Error importing settings for user {user_id}: {e}")
        return False


def has_cookies(user_id: int) -> bool:
    """Check if user has uploaded cookies"""
    from config import Config
    
    user_dir = os.path.join("users", str(user_id))
    cookie_file = os.path.join(user_dir, Config.COOKIE_FILE_PATH)
    
    return os.path.exists(cookie_file) and os.path.getsize(cookie_file) > 0


def get_cookies_status(user_id: int) -> str:
    """Get user cookies status as formatted text"""
    if has_cookies(user_id):
        return "🍪 <b>Cookies:</b> ✅ Uploaded"
    else:
        return "🍪 <b>Cookies:</b> ❌ Not uploaded"


def is_mediainfo_enabled(user_id: int) -> bool:
    """Check if mediainfo is enabled for user"""
    try:
        from ..database.firebase import db, db_child_by_path, logger
        data = db_child_by_path(db, f"user_settings/{user_id}/mediainfo_enabled").get().val()
        return bool(data) if data is not None else False
    except Exception as e:
        print(f"Error checking mediainfo setting: {e}")
        return False


def toggle_mediainfo(user_id: int) -> bool:
    """Toggle mediainfo setting for user"""
    try:
        from ..database.firebase import db, db_child_by_path, logger
        current = is_mediainfo_enabled(user_id)
        new_value = not current
        db_child_by_path(db, f"user_settings/{user_id}/mediainfo_enabled").set(new_value)
        print(f"MediaInfo toggled for user {user_id}: {new_value}")
        return new_value
    except Exception as e:
        print(f"Error toggling mediainfo: {e}")
        return False


        return "🍪 <b>Cookies:</b> ❌ Not uploaded" 