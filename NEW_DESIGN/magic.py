# Version 4.0.0 # split monolith code into multiple modules
###########################################################
#        GLOBAL IMPORTS
###########################################################
import glob
from sdnotify import SystemdNotifier
from datetime import datetime, timedelta
import hashlib
import io
import json
import logging
import math
import os
import re
import requests
import shutil
import subprocess
import random
import sys
import threading
import time
from datetime import datetime
from PIL import Image
from types import SimpleNamespace
from typing import Tuple
from urllib.parse import urlparse, parse_qs, urlunparse, unquote, urlencode
import traceback
import pyrebase
import tldextract
# from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pyrogram import Client, filters
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    ReplyParameters
)
from yt_dlp import YoutubeDL
import yt_dlp

# Config is now imported from CONFIG.config

import chardet
###########################################################
#        MODULE IMPORTS
###########################################################
# CONFIG
from CONFIG.config import Config

# HELPERS
from HELPERS.app_instance import set_app
from HELPERS.caption import *
from HELPERS.download_status import *
from HELPERS.filesystem_hlp import *
from HELPERS.limitter import *
from HELPERS.logger import *
from HELPERS.porn import *
from HELPERS.qualifier import *
from HELPERS.safe_messeger import *

# DATABASE
from DATABASE.cache_db import *
from DATABASE.download_firebase import *
from DATABASE.firebase_init import *

# URL_PARSERS
from URL_PARSERS.embedder import *
from URL_PARSERS.nocookie import *
from URL_PARSERS.normalizer import *
from URL_PARSERS.tags import *
from URL_PARSERS.tiktok import *
from URL_PARSERS.url_extractor import *
from URL_PARSERS.video_extractor import *
from URL_PARSERS.youtube import *

# COMMANDS
from COMMANDS.admin_cmd import *
from COMMANDS.clean_cmd import *
from COMMANDS.cookies_cmd import *
from COMMANDS.format_cmd import *
from COMMANDS.mediainfo_cmd import *
from COMMANDS.other_handlers import *
from COMMANDS.settings_cmd import *
from COMMANDS.split_sizer import *
from COMMANDS.subtitles_cmd import *
from COMMANDS.tag_cmd import *

# DOWN_AND_UP
from DOWN_AND_UP.always_ask_menu import *
from DOWN_AND_UP.down_and_audio import *
from DOWN_AND_UP.down_and_up import *
from DOWN_AND_UP.ffmpeg import *
from DOWN_AND_UP.sender import *
from DOWN_AND_UP.yt_dlp_hook import *

###########################################################
#        APP INITIALIZATION
###########################################################
# Pyrogram App Initialization
app = Client(
    "magic",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# Set global app instance
set_app(app)

# Apply all registered handlers
from HELPERS.handler_registry import apply_all_handlers
apply_all_handlers(app)

###########################################################
#        BOT KEYBOARD
###########################################################
# --- Function for permanent reply-keyboard ---
def get_main_reply_keyboard():
    return ReplyKeyboardMarkup(
        [
            ["/clean", "/download_cookie"],
            ["/playlist", "/settings", "/help"]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )


# eternal reply-keyboard and reliable work with files
reply_keyboard_msg_ids = {}  # user_id: message_id


def send_reply_keyboard_always(user_id):
    global reply_keyboard_msg_ids
    try:
        msg_id = reply_keyboard_msg_ids.get(user_id)
        if msg_id:
            try:
                app.edit_message_text(user_id, msg_id, "\u2063", reply_markup=get_main_reply_keyboard())
                return
            except Exception as e:
                # Log only if the error is not MESSAGE_ID_INVALID
                if 'MESSAGE_ID_INVALID' not in str(e):
                    logger.warning(f"Failed to edit persistent reply keyboard: {e}")
                # If it didn't work, we delete the id to avoid getting stuck
                reply_keyboard_msg_ids.pop(user_id, None)
        # Always after failure or if there is no id - send a new one
        msg = app.send_message(user_id, "\u2063", reply_markup=get_main_reply_keyboard())
        # If there was another service msg_id (and it is not equal to the new one), we try to delete the old message
        if msg_id and msg_id != msg.id:
            try:
                app.delete_messages(user_id, [msg_id])
            except Exception as e:
                logger.warning(f"Failed to delete old reply keyboard message: {e}")
        reply_keyboard_msg_ids[user_id] = msg.id
    except Exception as e:
        logger.warning(f"Failed to send persistent reply keyboard: {e}")


# --- Wrapper for any custom action ---
def reply_with_keyboard(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Determine user_id from arguments (Pyrogram message/chat)
        user_id = None
        if 'message' in kwargs:
            user_id = getattr(kwargs['message'].chat, 'id', None)
        elif len(args) > 0 and hasattr(args[0], 'chat'):
            user_id = getattr(args[0].chat, 'id', None)
        elif len(args) > 1 and hasattr(args[1], 'chat'):
            user_id = getattr(args[1].chat, 'id', None)
        if user_id:
            send_reply_keyboard_always(user_id)
        return result

    return wrapper

# --- Example of using wrapper for any handler ---
# @reply_with_keyboard
# def your_handler(...):
# ...

###########################################################
#        APP STARTS
###########################################################
# ###############################################################################################
# Global starting point list (do not modify)
starting_point = []

# ###############################################################################################

# Run the automatic loading of the Firebase cache
start_auto_cache_reloader()

app.run()