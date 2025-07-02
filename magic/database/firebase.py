"""Database and Firebase functions"""
import logging
import time
import threading
import math
import os
import shutil
from types import SimpleNamespace
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
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

# Get the base database object
base_db = firebase.database()

# Additional check: Execute a test GET request to the root node
try:
    test_data = base_db.get(idToken)
    logger.info("Test GET operation succeeded. Data:", test_data.val())
except Exception as e:
    logger.error("Test GET operation failed:", e)

# Define a wrapper class to automatically pass the idToken for all database operations
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


# Function to periodically refresh the idToken using the refreshToken
def token_refresher():
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

# Create authenticated database instance  
db = AuthedDB(base_db, user["idToken"])

# Initialize database with test data
try:
    db_path = Config.BOT_DB_PATH.rstrip("/")
    _format = {"ID": "0", "timestamp": math.floor(time.time())}
    # Try writing data to the path: bot/tgytdlp_bot/users/0
    result = db.child(f"{db_path}/users/0").set(_format)
    logger.info("Data written successfully. Result:", result)
except Exception as e:
    logger.error("Error writing data to Firebase:", e)
    raise


def write_logs(message, video_url, video_title):
    ts = str(math.floor(time.time()))
    data = {"ID": str(message.chat.id), "timestamp": ts,
            "name": message.chat.first_name, "urls": str(video_url), "title": video_title}
    db.child("bot").child("tgytdlp_bot").child("logs").child(str(message.chat.id)).child(str(ts)).set(data)
    logger.info("Log for user added")

def fake_message(text, user_id, command=None):
    m = SimpleNamespace()
    m.chat = SimpleNamespace()
    m.chat.id = user_id
    m.chat.first_name = "User"
    m.text = text
    m.first_name = m.chat.first_name
    m.reply_to_message = None
    m.id = 0
    if command is not None:
        m.command = command
    return m

def check_user(message):
    """Checking Users are in Main User Directory in DB"""
    user_id_str = str(message.chat.id)

    # Create The User Folder Inside The "Users" Directory
    from magic.utils.filesystem import create_directory
    user_dir = os.path.join("users", user_id_str)
    create_directory(user_dir)

    # Updated path for cookie.txt
    cookie_src = os.path.join(os.getcwd(), "TXT", "cookie.txt")
    cookie_dest = os.path.join(user_dir, os.path.basename(Config.COOKIE_FILE_PATH))

    # Copy Cookie.txt to the User's Folder if Not Already Present
    if os.path.exists(cookie_src) and not os.path.exists(cookie_dest):
        shutil.copy(cookie_src, cookie_dest)

    # Register the User in the Database if Not Already Registered
    try:
        user_db = db.child("bot").child("tgytdlp_bot").child("users").get().each()
        users = [user.key() for user in user_db] if user_db else []
        if user_id_str not in users:
            data = {"ID": message.chat.id, "timestamp": math.floor(time.time())}
            db.child("bot").child("tgytdlp_bot").child("users").child(user_id_str).set(data)
    except Exception as e:
        logger.error(f"Error registering user in database: {e}")

def db_child_by_path(db, path):
    for part in path.split("/"):
        db = db.child(part)
    return db

# Check the USAGE of the BOT
def is_user_in_channel(app, message):
    try:
        cht_member = app.get_chat_member(
            Config.SUBSCRIBE_CHANNEL, message.chat.id)
        if cht_member.status == ChatMemberStatus.MEMBER or cht_member.status == ChatMemberStatus.OWNER or cht_member.status == ChatMemberStatus.ADMINISTRATOR:
            return True

    except:

        text = f"{Config.TO_USE_MSG}\n \n{Config.CREDITS_MSG}"
        button = InlineKeyboardButton(
            "Join Channel", url=Config.SUBSCRIBE_CHANNEL_URL)
        keyboard = InlineKeyboardMarkup([[button]])
        # Use the send_message () Method to send the message with the button
        app.send_message(
            chat_id=message.chat.id,
            text=text,
            reply_markup=keyboard
        )
        return False

# Initialize database structure
try:
    _format = {"ID": '0', "timestamp": math.floor(time.time())}
    db.child("bot").child("tgytdlp_bot").child("users").child("0").set(_format)
    db.child("bot").child("tgytdlp_bot").child("blocked_users").child("0").set(_format)
    db.child("bot").child("tgytdlp_bot").child("unblocked_users").child("0").set(_format)
    logger.info("Database initialized successfully")
except Exception as e:
    logger.error(f"Error initializing database structure: {e}")

logger.info("Firebase module loaded")