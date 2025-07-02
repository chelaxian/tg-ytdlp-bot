"""Database and Firebase functions"""
import logging
import time
import threading
import math
from types import SimpleNamespace
from config import Config
import pyrebase

logger = logging.getLogger(__name__)

# Firebase Initialization with Authentication
firebase = pyrebase.initialize_app(Config.FIREBASE_CONF)

# Create auth object from pyrebase
auth = firebase.auth()

# Sign in using email and password (ensure these credentials are set in your Config)
try:
    user = auth.sign_in_with_email_and_password(Config.FIREBASE_USER, Config.FIREBASE_PASSWORD)
    # Debug: Print essential details of the user object
    logger.info("User signed in successfully.")
    logger.info(f"User email: {user.get('email')}")
    logger.info(f"User localId: {user.get('localId')}")
    # If available, check email verification status
    if "emailVerified" in user:
        logger.info(f"Email verified: {user['emailVerified']}")
    else:
        logger.info("Email verification status not available in user object.")
except Exception as e:
    logger.error(f"Error during Firebase authentication: {e}")
    raise

# Debug: Print a portion of idToken
idToken = user.get("idToken")
if idToken:
    logger.info(f"Firebase idToken (first 20 chars): {idToken[:20]}")
else:
    logger.error("No idToken received!")
    raise Exception("idToken is empty.")

class AuthedDB:
    def __init__(self, db, token):
        self.db = db
        self.token = token

    def child(self, path):
        return AuthedDB(self.db.child(path), self.token)

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


# Create authenticated database instance  
db = AuthedDB(firebase.database(), idToken)

# Initialize database with test data
db_path = Config.BOT_DB_PATH.rstrip("/") if hasattr(Config, 'BOT_DB_PATH') else "bot/tgytdlp_bot"
_format = {"ID": "0", "timestamp": math.floor(time.time())}
try:
    # Try writing data to the path: bot/tgytdlp_bot/users/0
    result = db.child(f"{db_path}/users/0").set(_format)
    logger.info("Data written successfully. Result:", result)
except Exception as e:
    logger.error("Error writing data to Firebase:", e)


def token_refresher():
    """Function to periodically refresh the idToken using the refreshToken"""
    global db, user
    while True:
        # Sleep for 50 minutes (3000 seconds)
        time.sleep(3000)
        try:
            new_user = auth.refresh(user["refreshToken"])
            new_idToken = new_user["idToken"]
            db.token = new_idToken
            user = new_user
            logger.info("Firebase idToken refreshed successfully. New token (first 20 chars):", new_idToken[:20])
        except Exception as e:
            logger.error("Error refreshing Firebase idToken:", e)


# Start the token refresher thread as a daemon
token_thread = threading.Thread(target=token_refresher, daemon=True)
token_thread.start()


def write_logs(message, video_url, video_title):
    """Write logs to Firebase"""
    try:
        user_id = message.chat.id
        current_time = time.time()
        data = {
            "user_id": user_id,
            "video_url": video_url,
            "video_title": video_title,
            "timestamp": current_time
        }
        db.child("logs").push(data)
    except Exception as e:
        logger.error(f"Error writing logs: {e}")

def fake_message(text, user_id, command=None):
    """Create fake message object"""
    class FakeMessage:
        def __init__(self, text, user_id):
            self.text = text
            self.chat = SimpleNamespace(id=user_id, first_name=f"User{user_id}")
            self.from_user = SimpleNamespace(first_name=f"User{user_id}")
            self.id = int(time.time())
    
    return FakeMessage(text, user_id)

def is_user_blocked(message):
    """Check if user is blocked"""
    try:
        user_id = message.chat.id
        blocked_users = db.child("blocked_users").get().val() or {}
        return str(user_id) in blocked_users
    except:
        return False

def check_user(message):
    """Check user in database"""
    try:
        user_id = message.chat.id
        user_data = {
            "user_id": user_id,
            "first_name": message.chat.first_name,
            "last_seen": time.time()
        }
        db.child("users").child(str(user_id)).set(user_data)
        return True
    except Exception as e:
        logger.error(f"Error checking user: {e}")
        return False

def is_user_in_channel(app, message):
    """Check if user is in channel"""
    try:
        if not hasattr(Config, 'CHANNEL_ID') or not Config.CHANNEL_ID:
            return True
        
        user_id = message.chat.id
        member = app.get_chat_member(Config.CHANNEL_ID, user_id)
        return member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except:
        return False

def db_child_by_path(db, path):
    """Get database child by path"""
    return db.child(path)
