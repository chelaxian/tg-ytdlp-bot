# Messages Configuration
import sys
import os
import logging

# Setup logger
logger = logging.getLogger(__name__)

# Add the LANGUAGES directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'LANGUAGES'))

try:
    from language_router import get_messages, get_message, set_user_language
except ImportError:
    # Fallback if language router is not available
    def get_messages(user_id=None, language_code=None):
        return {}
    def get_message(message_key, user_id=None, language_code=None):
        return f"[{message_key}]"
    def set_user_language(user_id, language_code):
        return False

class Messages(object):
    def __init__(self, user_id=None, language_code=None):
        """
        Initialize Messages with user-specific language
        """
        self.user_id = user_id
        self.language_code = language_code
        try:
            logger.info(f"🔍 [Messages.__init__] Loading messages for user_id={user_id}, language_code={language_code}")
            self._messages = get_messages(user_id, language_code)
            logger.info(f"🔍 [Messages.__init__] Got messages dict with {len(self._messages)} keys")
            # Debug: log if messages dict is empty
            if not self._messages:
                logger.warning(f"⚠️ Warning: Empty messages dict for user_id={user_id}, language_code={language_code}")
                # Try to get default language
                if language_code != 'en':
                    logger.info(f"🔄 Trying to load default language 'en'...")
                    self._messages = get_messages(None, 'en')
                    logger.info(f"🔍 [Messages.__init__] Default language dict has {len(self._messages)} keys")
        except Exception as e:
            logger.error(f"❌ Error getting messages for user_id={user_id}, language_code={language_code}: {e}")
            import traceback
            logger.error(traceback.format_exc())
            self._messages = {}
    
    def __getattr__(self, name):
        """
        Get message by name from user's selected language ONLY
        """
        if name.startswith('_'):
            return super().__getattribute__(name)
        
        # STRICT: Only use language-specific messages, NO fallback to English
        if hasattr(self, '_messages') and self._messages and name in self._messages:
            return self._messages[name]
        
        # Debug: log missing message (only first few to avoid spam)
        if hasattr(self, '_messages') and self._messages:
            if not hasattr(self, '_missing_logged'):
                self._missing_logged = set()
            if name not in self._missing_logged and len(self._missing_logged) < 5:
                logger.warning(f"⚠️ Message '{name}' not found in language dict (user_id={self.user_id}, lang={self.language_code}, dict_size={len(self._messages)})")
                logger.info(f"🔍 Sample keys in dict: {list(self._messages.keys())[:10]}")
                self._missing_logged.add(name)
        elif not hasattr(self, '_messages') or not self._messages:
            if not hasattr(self, '_empty_logged'):
                logger.error(f"❌ Messages dict is empty or missing! (user_id={self.user_id}, lang={self.language_code})")
                self._empty_logged = True
        
        # If message not found in selected language, return placeholder
        return f"[{name}]"
    
    # All messages are now loaded dynamically from language-specific files
    # through the language router. No static variables needed here.

# Global function to get Messages instance with user language
def get_messages_instance(user_id=None, language_code=None):
    """
    Get Messages instance with user-specific language
    """
    return Messages(user_id, language_code)

# GLOBAL PROTECTION: Safe function that NEVER fails
def safe_get_messages(user_id=None, language_code=None):
    """
    SAFE function that NEVER raises NameError for 'messages'
    This function is GUARANTEED to return a Messages object
    """
    try:
        # Convert user_id to int if it's a string (for compatibility)
        if user_id is not None and isinstance(user_id, str):
            try:
                user_id = int(user_id)
            except (ValueError, TypeError):
                pass  # Keep as string if conversion fails
        
        return get_messages_instance(user_id, language_code)
    except Exception as e:
        logger.error(f"❌ Error in safe_get_messages: {e}")
        import traceback
        logger.error(traceback.format_exc())
        # If everything fails, return a minimal Messages object
        return Messages(None, None)

# GLOBAL PROTECTION: Safe function for any context
def safe_messages(user_id=None):
    """
    ULTRA-SAFE function that works in ANY context
    """
    try:
        return get_messages_instance(user_id)
    except:
        try:
            return get_messages_instance(None)
        except:
            # Last resort - return a dummy object
            class DummyMessages:
                def __getattr__(self, name):
                    return f"[{name}]"
            return DummyMessages()

# Backward compatibility - create default instance with English language
messages = Messages(None, 'en')