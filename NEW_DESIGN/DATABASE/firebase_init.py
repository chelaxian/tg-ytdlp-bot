import pyrebase
import math
import time
import threading
import os
from CONFIG.config import Config
from HELPERS.logger import logger
from HELPERS.filesystem_hlp import create_directory
from HELPERS.logger import send_to_all

# Global variable for timing
starting_point = []

# Initialize Firebase
firebase = pyrebase.initialize_app(Config.FIREBASE_CONF)
auth = firebase.auth()

# Authenticate user
try:
    user = auth.sign_in_with_email_and_password(Config.FIREBASE_USER, Config.FIREBASE_PASSWORD)
    logger.info("✅ Firebase signed in")
except Exception as e:
    logger.error(f"❌ Firebase authentication error: {e}")
    raise

# Extract idToken
id_token = user.get("idToken")
if not id_token:
    raise Exception("idToken is missing")

# Setup database with authentication
base_db = firebase.database()

class AuthedDB:
    def __init__(self, db, token):
        self.db = db
        self.token = token

    def child(self, *path_parts):
        db_ref = self.db
        for part in path_parts:
            db_ref = db_ref.child(part)
        return AuthedDB(db_ref, self.token)

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
	    

# Create authed db wrapper
db = AuthedDB(base_db, id_token)

# Optional write to verify it's working
try:
    db_path = Config.BOT_DB_PATH.rstrip("/")
    payload = {"ID": "0", "timestamp": math.floor(time.time())}
    db.child(f"{db_path}/users/0").set(payload)
    logger.info("✅ Initial Firebase write successful")
except Exception as e:
    logger.error(f"❌ Error writing to Firebase: {e}")
    raise

# Background thread to refresh idToken every 50 minutes
def token_refresher():
    global db, user
    while True:
        time.sleep(3000)  # 50 minutes
        try:
            new_user = auth.refresh(user["refreshToken"])
            new_id_token = new_user["idToken"]
            db.token = new_id_token
            user = new_user
            logger.info("🔁 Firebase token refreshed")
        except Exception as e:
            logger.error(f"❌ Token refresh error: {e}")

token_thread = threading.Thread(target=token_refresher, daemon=True)
token_thread.start()

# ###############################################################################################

def db_child_by_path(db, path):
    for part in path.strip("/").split("/"):
        db = db.child(part)
    return db



# Cheking Users are in Main User Directory in DB

def check_user(message):
    user_id_str = str(message.chat.id)

    # Create The User Folder Inside The "Users" Directory
    user_dir = os.path.join("users", user_id_str)
    create_directory(user_dir)

    # Updated path for cookie.txt
    cookie_src = os.path.join(os.getcwd(), "cookies", "cookie.txt")
    cookie_dest = os.path.join(user_dir, os.path.basename(Config.COOKIE_FILE_PATH))

    # Copy Cookie.txt to the User's Folder if Not Already Present
    if os.path.exists(cookie_src) and not os.path.exists(cookie_dest):
        import shutil
        shutil.copy(cookie_src, cookie_dest)

    # Register the User in the Database if Not Already Registered
    user_db = db.child("bot").child("tgytdlp_bot").child("users").get().each()
    users = [user.key() for user in user_db] if user_db else []
    if user_id_str not in users:
        data = {"ID": message.chat.id, "timestamp": math.floor(time.time())}
        db.child("bot").child("tgytdlp_bot").child("users").child(user_id_str).set(data)


# Checking user is Blocked or not

def is_user_blocked(message):
    blocked = db.child("bot").child("tgytdlp_bot").child("blocked_users").get().each()
    blocked_users = [int(b_user.key()) for b_user in blocked]
    if int(message.chat.id) in blocked_users:
        send_to_all(message, "🚫 You are banned from the bot!")
        return True
    else:
        return False

def write_logs(message, video_url, video_title):
    ts = str(math.floor(time.time()))
    data = {"ID": str(message.chat.id), "timestamp": ts,
            "name": message.chat.first_name, "urls": str(video_url), "title": video_title}
    db.child("bot").child("tgytdlp_bot").child("logs").child(str(message.chat.id)).child(str(ts)).set(data)
    logger.info("Log for user added")
# ####################################################################################
# ####################################################################################
#####################################################################################
_format = {"ID": '0', "timestamp": math.floor(time.time())}
db.child("bot").child("tgytdlp_bot").child("users").child("0").set(_format)
db.child("bot").child("tgytdlp_bot").child("blocked_users").child("0").set(_format)
db.child("bot").child("tgytdlp_bot").child("unblocked_users").child("0").set(_format)
logger.info("db created")
starting_point.append(time.time())
logger.info("Bot started")
