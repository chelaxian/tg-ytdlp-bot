#!/usr/bin/env python3
"""
Script for downloading Firebase Realtime Database dump
Run this script once a day to update the local cache
"""

import json
import os
import sys
import time
from datetime import datetime

# Add parent directory to path for imports BEFORE importing modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from HELPERS.logger import logger
    from CONFIG.messages import safe_get_messages
except ImportError:
    # Fallback logger if HELPERS is not available
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    # Fallback for messages
    class FallbackMessages:
        DB_DEPENDENCY_NOT_AVAILABLE_MSG = "❌ Requests dependency missing"
        DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Firebase config/user/password not set"
        DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Starting Firebase dump download at {datetime}"
        DB_DATABASE_URL_NOT_SET_MSG = "❌ databaseURL is not configured"
        DB_API_KEY_NOT_SET_MSG = "❌ apiKey is not configured"
        ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Downloading database dump..."
        DB_DATABASE_EMPTY_MSG = "⚠️ Firebase database seems empty"
        DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Error downloading Firebase dump: {error}"
    def safe_get_messages(_user_id=None):
        return FallbackMessages()

try:
    from CONFIG.config import Config
    from CONFIG.messages import safe_get_messages
except ImportError as e:
    print(f"Import error: {e}")
    print("Config not found")
    sys.exit(1)

try:
    import requests
    from requests import Session
    from requests.exceptions import Timeout, RequestException
except ImportError:
    requests = None
    Session = None
    Timeout = None
    RequestException = None

# All parameters are taken from config.py
FIREBASE_CONFIG = getattr(Config, 'FIREBASE_CONF', None)
FIREBASE_USER = getattr(Config, 'FIREBASE_USER', None)
FIREBASE_PASSWORD = getattr(Config, 'FIREBASE_PASSWORD', None)
OUTPUT_FILE = getattr(Config, 'FIREBASE_CACHE_FILE', 'firebase_cache.json')

if not FIREBASE_CONFIG or not FIREBASE_USER or not FIREBASE_PASSWORD:
    print(safe_get_messages().DB_NOT_ALL_PARAMETERS_SET_MSG)
    sys.exit(1)

def download_firebase_dump():
    """Downloads the entire Firebase Realtime Database dump"""
    if requests is None or Session is None:
        print(safe_get_messages().DB_DEPENDENCY_NOT_AVAILABLE_MSG)
        return False

    # Create managed session for connection pooling
    from HELPERS.http_manager import get_managed_session
    session_manager = get_managed_session("firebase-download")
    session = session_manager.get_session()
    
    # Timeout configuration (connect_timeout, read_timeout)
    AUTH_CONNECT_TIMEOUT = 30
    AUTH_READ_TIMEOUT = 180    # increase auth read timeout
    DOWNLOAD_CONNECT_TIMEOUT = 30
    DOWNLOAD_READ_TIMEOUT = 600  # increase dump read timeout

    # Retry configuration
    MAX_AUTH_RETRIES = 3
    MAX_DOWNLOAD_RETRIES = 2
    RETRY_DELAY = 5

    try:
        print(safe_get_messages().DB_STARTING_FIREBASE_DUMP_MSG.format(datetime=datetime.now()))

        database_url = FIREBASE_CONFIG.get("databaseURL")
        if not database_url:
            print(safe_get_messages().DB_DATABASE_URL_NOT_SET_MSG)
            return False

        # For downloading dump we use REST API and custom token/ID token.
        # Preferably ID token via REST signInWithPassword.
        key = FIREBASE_CONFIG.get("apiKey")
        if not key:
            print(safe_get_messages().DB_API_KEY_NOT_SET_MSG)
            return False

        # Authentication with retry logic
        auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={key}"
        auth_payload = {
            "email": FIREBASE_USER,
            "password": FIREBASE_PASSWORD,
            "returnSecureToken": True,
        }
        auth_timeout = (AUTH_CONNECT_TIMEOUT, AUTH_READ_TIMEOUT)

        id_token = None
        for attempt in range(1, MAX_AUTH_RETRIES + 1):
            try:
                if attempt > 1:
                    print(f"🔐 Authentication retry {attempt}/{MAX_AUTH_RETRIES}...")
                resp = session.post(auth_url, json=auth_payload, timeout=auth_timeout)
                resp.raise_for_status()
                id_token = resp.json()["idToken"]
                print("✅ Authentication successful")
                break
            except Timeout:
                if attempt < MAX_AUTH_RETRIES:
                    wait_time = RETRY_DELAY * attempt
                    print(f"⏱️  Auth timeout, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    print(f"❌ Authentication failed after {MAX_AUTH_RETRIES} attempts (timeout {AUTH_READ_TIMEOUT}s)")
                    raise
            except RequestException as e:
                print(f"❌ Authentication error: {e}")
                if attempt >= MAX_AUTH_RETRIES:
                    raise
                wait_time = RETRY_DELAY * attempt
                print(f"⏱️  Retrying auth in {wait_time}s...")
                time.sleep(wait_time)

        if not id_token:
            print("❌ Failed to obtain authentication token")
            return False

        # Downloading data with retry logic
        print(safe_get_messages().ALWAYS_ASK_DOWNLOADING_DATABASE_MSG)
        url = f"{database_url}/.json?auth={id_token}"
        download_timeout = (DOWNLOAD_CONNECT_TIMEOUT, DOWNLOAD_READ_TIMEOUT)

        response = None
        for attempt in range(1, MAX_DOWNLOAD_RETRIES + 1):
            try:
                if attempt > 1:
                    print(f"🔄 Download retry {attempt}/{MAX_DOWNLOAD_RETRIES}...")
                response = session.get(url, timeout=download_timeout, stream=True)
                response.raise_for_status()
                break
            except Timeout:
                if attempt < MAX_DOWNLOAD_RETRIES:
                    wait_time = RETRY_DELAY * attempt
                    print(f"⏱️  Download timeout, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    print(f"❌ Download failed after {MAX_DOWNLOAD_RETRIES} attempts (timeout {DOWNLOAD_READ_TIMEOUT}s)")
                    raise
            except RequestException as e:
                print(f"❌ Download error: {e}")
                if attempt >= MAX_DOWNLOAD_RETRIES:
                    raise
                wait_time = RETRY_DELAY * attempt
                print(f"⏱️  Retrying download in {wait_time}s...")
                time.sleep(wait_time)

        if response is None:
            print("❌ Failed to start download")
            return False

        # Saving to file without loading entire dump into memory
        print("💾 Saving database dump to file...")
        bytes_written = 0
        chunk_count = 0
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            for chunk in response.iter_content(chunk_size=1024 * 512, decode_unicode=True):
                if chunk:
                    f.write(chunk)
                    bytes_written += len(chunk.encode("utf-8"))
                    chunk_count += 1
                    if chunk_count % 100 == 0:
                        print(f"  📊 Progress: {bytes_written / (1024*1024):.2f} MB downloaded...")

        print(f"✅ Download complete: {bytes_written / (1024*1024):.2f} MB")

        data = None
        file_size = os.path.getsize(OUTPUT_FILE)
        if file_size <= 50 * 1024 * 1024:  # only parse stats for reasonably sized dumps
            try:
                with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except (ValueError, json.JSONDecodeError, OSError) as stats_err:
                logger.warning("Failed to parse Firebase dump for stats: %s", stats_err)

        if data:
            total_keys = len(data)
            print("✅ Firebase database downloaded successfully!")
            print(f"📊 Total root nodes: {total_keys}")
            print(f"💾 Saved to: {OUTPUT_FILE}")
            print(f"📏 File size: {file_size} bytes")

            print("\n📋 Database structure:")
            for key in data.keys():
                if isinstance(data[key], dict):
                    sub_keys = len(data[key])
                    print(f"  - {key}: {sub_keys} sub-nodes")
                else:
                    print(f"  - {key}: {type(data[key]).__name__}")
        else:
            print(safe_get_messages().DB_DATABASE_EMPTY_MSG)
            print(f"💾 Saved to: {OUTPUT_FILE}")
            print(f"📏 File size: {file_size} bytes")

        return True

    except Timeout as e:
        error_msg = f"Request timeout: {e}"
        print(safe_get_messages().DB_ERROR_DOWNLOADING_DUMP_MSG.format(error=error_msg))
        logger.error("Firebase download timeout: %s", e)
        return False
    except RequestException as e:
        error_msg = f"HTTP request error: {e}"
        print(safe_get_messages().DB_ERROR_DOWNLOADING_DUMP_MSG.format(error=error_msg))
        logger.error("Firebase download request error: %s", e)
        return False
    finally:
        # Always close the managed session
        session_manager.close()

def main():
    print("🚀 Firebase Database Dumper (config-driven)")
    print("=" * 40)
    
    # Check config
    if not FIREBASE_CONFIG or not FIREBASE_USER or not FIREBASE_PASSWORD:
        print(safe_get_messages().DB_NOT_ALL_PARAMETERS_SET_MSG)
        return False
    
    # Download dump
    success = download_firebase_dump()
    
    if success:
        print(f"\n🎉 Firebase dump completed at {datetime.now()}")
        print("💡 You can now restart your bot to use the updated cache")
    else:
        print(f"\n💥 Firebase dump failed at {datetime.now()}")
        return False
    
    return True

if __name__ == "__main__":
    main_success = main()
    sys.exit(0 if main_success else 1) 
