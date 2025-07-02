# Version 3.0.0
import logging
import math
import os
import re
import shutil
import subprocess
import threading
import time
import signal
from datetime import datetime
from types import SimpleNamespace
from typing import Tuple
from urllib.parse import urlparse, parse_qs, urlunparse, unquote, urlencode

import pyrebase
import requests
import tldextract
from moviepy.editor import VideoFileClip
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

from config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('bot.log')
    ]
)
logger = logging.getLogger(__name__)

# Import all functions from modules
from magic.utils.helpers import get_main_reply_keyboard, send_reply_keyboard_always, reply_with_keyboard
from magic.utils.filesystem import *
from magic.utils.formatters import *
from magic.processing.url_parser import *
from magic.database.firebase import *
from magic.processing.tags import *
from magic.download.cache import *
from magic.download.quality import *
from magic.handlers.commands import *
from magic.handlers.admin import *
from magic.handlers.settings import *
from magic.processing.video import *
from magic.utils.communication import *
from magic.download.downloader import *
from magic.user.settings import *

# Pyrogram App Initialization
app = Client(
    "magic",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

if __name__ == "__main__":
    app.run()
