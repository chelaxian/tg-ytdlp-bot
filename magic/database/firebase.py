"""
Firebase database utilities
"""
import time
import math
import threading
from typing import Optional, Any
import logging
from config import Config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AuthedDB:
    """
    Authenticated Database wrapper
    """
    def __init__(self, db, token):
        self.db = db
        self.token = token

    def child(self, path):
        return self.db.child(path)

    def set(self, data, *args, **kwargs):
        return self.db.set(data, self.token, *args, **kwargs)

    def get(self, *args, **kwargs):
        return self.db.get(self.token, *args, **kwargs)

    def push(self, data, *args, **kwargs):
        return self.db.push(data, self.token, *args, **kwargs)

    def update(self, data, *args, **kwargs):
        return self.db.update(data, self.token, *args, **kwargs)

    def remove(self, *args, **kwargs):
        return self.db.remove(self.token, *args, **kwargs)


def token_refresher():
    """
    Token refresher for Firebase authentication
    This function should be called periodically to refresh the auth token
    """
    import pyrebase
    from config import Config
    import logging
    
    logger = logging.getLogger(__name__)
    
    try:
        firebase = pyrebase.initialize_app(Config.FIREBASE_CONF)
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(Config.FIREBASE_USER, Config.FIREBASE_PASSWORD)
        
        # Return the new token
        return user['idToken']
    except Exception as e:
        logger.error(f"Error refreshing Firebase token: {e}")
        return None


def db_child_by_path(db, path):
    """
    Navigate to a database child by path string
    
    Args:
        db: Firebase database reference
        path: String path like "path/to/child"
    
    Returns:
        Database reference to the child
    """
    if not path or path in ('', '/'):
        return db
    
    parts = path.strip('/').split('/')
    ref = db
    for part in parts:
        if part:  # Skip empty parts
            ref = ref.child(part)
    
    return ref


def write_logs(message, video_url, video_title):
    """
    Write download logs to database and user file
    """
    import logging
    import os
    from config import Config
    from magic.utils.filesystem import create_directory
    
    logger = logging.getLogger(__name__)
    
    try:
        user_id = message.chat.id
        user_name = getattr(message.from_user, 'first_name', 'Unknown')
        
        # Prepare log data
        log_data = {
            'user_id': user_id,
            'user_name': user_name,
            'video_url': video_url,
            'video_title': video_title,
            'timestamp': time.time(),
            'date': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        }
        
        # Write to user's local log file
        user_dir = os.path.join("users", str(user_id))
        create_directory(user_dir)
        
        log_file = os.path.join(user_dir, "logs.txt")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{log_data['date']} - {video_title} - {video_url}\n")
        
        logger.info(f"Logged download for user {user_id}: {video_title}")
        
    except Exception as e:
        logger.error(f"Error writing logs: {e}")


def fake_message(text, user_id, command=None):
    """
    Create a fake message object for internal function calls
    """
    class FakeUser:
        def __init__(self, user_id):
            self.id = user_id
            self.first_name = f"User{user_id}"
    
    class FakeChat:
        def __init__(self, user_id):
            self.id = user_id
    
    class FakeMessage:
        def __init__(self, text, user_id, command=None):
            self.text = text
            self.chat = FakeChat(user_id)
            self.from_user = FakeUser(user_id)
            self.id = int(time.time())
            if command:
                self.command = [command]
            else:
                self.command = []
    
    return FakeMessage(text, user_id, command)


# User checking and blocking functions
def is_user_blocked(message, db):
    """
    Check if user is blocked
    """
    try:
        blocked = db.child("bot").child("tgytdlp_bot").child("blocked_users").get().each()
        if blocked:
            blocked_users = [int(b_user.key()) for b_user in blocked]
            return int(message.chat.id) in blocked_users
        return False
    except Exception:
        return False


def check_user(message, db):
    """
    Check if user exists in database and add if not
    """
    import logging
    from config import Config
    
    logger = logging.getLogger(__name__)
    
    try:
        user_id = message.chat.id
        users = db.child("bot").child("tgytdlp_bot").child("users").get().each()
        
        if users:
            user_ids = [int(user.key()) for user in users]
            if user_id not in user_ids:
                # Add new user
                _format = {"ID": user_id, "timestamp": math.floor(time.time())}
                db.child("bot").child("tgytdlp_bot").child("users").child(str(user_id)).set(_format)
                logger.info(f"Added new user {user_id} to database")
        else:
            # First user
            _format = {"ID": user_id, "timestamp": math.floor(time.time())}
            db.child("bot").child("tgytdlp_bot").child("users").child(str(user_id)).set(_format)
            logger.info(f"Added first user {user_id} to database")
            
    except Exception as e:
        logger.error(f"Error checking/adding user: {e}")


def is_user_in_channel(app, message):
    """
    Check if user is subscribed to the required channel
    """
    from config import Config
    import logging
    
    logger = logging.getLogger(__name__)
    
    try:
        user_id = message.chat.id
        
        # Skip check for admins
        if user_id in Config.ADMIN:
            return True
        
        # Check if user is in the required channel
        member = app.get_chat_member(Config.SUBSCRIBE_CHANNEL, user_id)
        
        # Allow if user is member, administrator, or creator
        return member.status in ["member", "administrator", "creator"]
        
    except Exception as e:
        logger.error(f"Error checking channel membership for user {user_id}: {e}")
        return False


def send_to_logger(message, msg):
    """
    Send message to log channel
    """
    from config import Config
    import logging
    
    logger = logging.getLogger(__name__)
    
    try:
        # This should be imported from the main magic.py where app is defined
        from magic import app
        
        log_text = f"User: {message.from_user.first_name} ({message.chat.id})\n{msg}"
        app.send_message(Config.LOGS_ID, log_text)
        
    except Exception as e:
        logger.error(f"Error sending to logger: {e}")


def send_to_user(message, msg):
    """
    Send message to user
    """
    import logging
    
    logger = logging.getLogger(__name__)
    
    try:
        from magic import app
        app.send_message(message.chat.id, msg, reply_to_message_id=message.id)
        
    except Exception as e:
        logger.error(f"Error sending to user: {e}")


def send_to_all(message, msg):
    """
    Send message to both user and logger
    """
    send_to_user(message, msg)
    send_to_logger(message, msg)


# Global db reference (will be set in main file)
db = None 