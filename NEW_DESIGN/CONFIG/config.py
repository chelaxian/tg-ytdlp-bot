# Main Configuration
# This file combines all configuration classes into one unified Config class

from CONFIG.commands import CommandsConfig
from CONFIG.messages import MessagesConfig
from CONFIG.domains import DomainsConfig
from CONFIG.limits import LimitsConfig

###########################################################
#        START FILL IN YOUR CUSTOM VALUES HERE
###########################################################
class Config(object):
    #######################################################    
    # Your bot name - Required (str)
    BOT_NAME = "NAME_YOUR_BOT"
    # A name for users - Required (str)
    BOT_NAME_FOR_USERS = "tg-ytdlp-bot" #name in database
    # Add all admin id's as a list - Required (lst[int])
    ADMIN = [0000000000]
    # Add your telegram API ID - Required (int)
    API_ID = 0000000
    # Add your Telegram API HASH - Required (str)
    API_HASH = ""
    # Add your telegram bot token (str)
    BOT_TOKEN = ""
    # Add telegram Log channel Id - Required (int)
    LOGS_ID = -0000000000000 
    # Add main channel to subscribe - Required (int)
    SUBSCRIBE_CHANNEL = -0000000000000
    # Add subscription channel - Required (str)
    SUBSCRIBE_CHANNEL_URL = "https://t.me/YOUR_CHANNEL_NAME"
    
    # Cookie file URL
    # EX: "https://path/to/your/cookie-file.txt"
    COOKIE_URL = ""
    YOUTUBE_COOKIE_URL = ""
    INSTAGRAM_COOKIE_URL = ""
    TWITTER_COOKIE_URL = ""
    TIKTOK_COOKIE_URL = ""
    FACEBOOK_COOKIE_URL = ""
    # Do not chanege this
    COOKIE_FILE_PATH = "TXT/cookie.txt"
    # Do not chanege this
    PIC_FILE_PATH = "pic.jpg"
    FIREBASE_CACHE_FILE = "dump.json"
    RELOAD_CACHE_EVERY = 4 # in hours
    DOWNLOAD_FIREBASE_SCRIPT_PATH = "DATABASE/download_firebase.py"
    AUTO_CACHE_RELOAD_ENABLED = True # Enable/disable automatic cache reloading
    #######################################################
    # Firebase initialization
    # your firebase DB path
    BOT_DB_PATH = f"bot/{BOT_NAME_FOR_USERS}/"
    VIDEO_CACHE_DB_PATH = f"bot/video_cache"
    PLAYLIST_CACHE_DB_PATH = f"bot/video_cache/playlists"
    # Firebase Config - Required (str for all)
    FIREBASE_USER = "YOUR@E.MAIL"
    FIREBASE_PASSWORD = "YOUR_PASSWORD"
    FIREBASE_CONF = {
        'apiKey': "",
        'authDomain': "",
        'projectId': "",
        'storageBucket': "",
        'messagingSenderId': "",
        'appId': "",
        'databaseURL': ""
    }
    ###########################################################
    ###########################################################
    #        STOP FILL IN YOUR CUSTOM VALUES HERE
    ###########################################################
    # Commands configuration
    DOWNLOAD_COOKIE_COMMAND = CommandsConfig.DOWNLOAD_COOKIE_COMMAND
    SUBS_COMMAND = CommandsConfig.SUBS_COMMAND
    CHECK_COOKIE_COMMAND = CommandsConfig.CHECK_COOKIE_COMMAND
    SAVE_AS_COOKIE_COMMAND = CommandsConfig.SAVE_AS_COOKIE_COMMAND
    AUDIO_COMMAND = CommandsConfig.AUDIO_COMMAND
    UNCACHE_COMMAND = CommandsConfig.UNCACHE_COMMAND
    PLAYLIST_COMMAND = CommandsConfig.PLAYLIST_COMMAND
    FORMAT_COMMAND = CommandsConfig.FORMAT_COMMAND
    MEDIINFO_COMMAND = CommandsConfig.MEDIINFO_COMMAND
    SETTINGS_COMMAND = CommandsConfig.SETTINGS_COMMAND
    COOKIES_FROM_BROWSER_COMMAND = CommandsConfig.COOKIES_FROM_BROWSER_COMMAND
    BLOCK_USER_COMMAND = CommandsConfig.BLOCK_USER_COMMAND
    UNBLOCK_USER_COMMAND = CommandsConfig.UNBLOCK_USER_COMMAND
    RUN_TIME = CommandsConfig.RUN_TIME
    GET_USER_LOGS_COMMAND = CommandsConfig.GET_USER_LOGS_COMMAND
    CLEAN_COMMAND = CommandsConfig.CLEAN_COMMAND
    USAGE_COMMAND = CommandsConfig.USAGE_COMMAND
    TAGS_COMMAND = CommandsConfig.TAGS_COMMAND
    BROADCAST_MESSAGE = CommandsConfig.BROADCAST_MESSAGE
    GET_USER_DETAILS_COMMAND = CommandsConfig.GET_USER_DETAILS_COMMAND
    SPLIT_COMMAND = CommandsConfig.SPLIT_COMMAND
    RELOAD_CACHE_COMMAND = CommandsConfig.RELOAD_CACHE_COMMAND
    AUTO_CACHE_COMMAND = CommandsConfig.AUTO_CACHE_COMMAND
    
    # Messages configuration
    CREDITS_MSG = MessagesConfig.CREDITS_MSG
    TO_USE_MSG = MessagesConfig.TO_USE_MSG
    MSG1 = MessagesConfig.MSG1
    MSG2 = MessagesConfig.MSG2
    ERROR1 = MessagesConfig.ERROR1
    INDEX_ERROR = MessagesConfig.INDEX_ERROR
    PLAYLIST_HELP_MSG = MessagesConfig.PLAYLIST_HELP_MSG
    HELP_MSG = MessagesConfig.HELP_MSG
    
    # Domains configuration
    BLACK_LIST = DomainsConfig.BLACK_LIST
    PORN_DOMAINS_FILE = DomainsConfig.PORN_DOMAINS_FILE
    PORN_KEYWORDS_FILE = DomainsConfig.PORN_KEYWORDS_FILE
    SUPPORTED_SITES_FILE = DomainsConfig.SUPPORTED_SITES_FILE
    WHITELIST = DomainsConfig.WHITELIST
    NO_COOKIE_DOMAINS = DomainsConfig.NO_COOKIE_DOMAINS
    TIKTOK_DOMAINS = DomainsConfig.TIKTOK_DOMAINS
    CLEAN_QUERY = DomainsConfig.CLEAN_QUERY
    
    # Messages configuration (additional)
    SAVE_AS_COOKIE_HINT = MessagesConfig.SAVE_AS_COOKIE_HINT
    
    # Limits configuration
    MAX_FILE_SIZE_GB = LimitsConfig.MAX_FILE_SIZE_GB
    DOWNLOAD_TIMEOUT = LimitsConfig.DOWNLOAD_TIMEOUT
    MAX_SUB_QUALITY = LimitsConfig.MAX_SUB_QUALITY
    MAX_SUB_DURATION = LimitsConfig.MAX_SUB_DURATION
    MAX_SUB_SIZE = LimitsConfig.MAX_SUB_SIZE
    MAX_PLAYLIST_COUNT = LimitsConfig.MAX_PLAYLIST_COUNT
    MAX_TIKTOK_COUNT = LimitsConfig.MAX_TIKTOK_COUNT
    #######################################################