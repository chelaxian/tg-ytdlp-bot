#!/usr/bin/env python3
"""
Script for downloading Firebase Realtime Database dump
Run this script once a day to update the local cache
"""

import json
import os
import sys
import time
import tempfile
import re
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
    print(f"DUMP FAILED: config import error: {e}", file=sys.stderr)
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
TMP_OUTPUT_FILE = f"{OUTPUT_FILE}.tmp"

if not FIREBASE_CONFIG or not FIREBASE_USER or not FIREBASE_PASSWORD:
    print(safe_get_messages().DB_NOT_ALL_PARAMETERS_SET_MSG)
    print("DUMP FAILED: FIREBASE_CONF / FIREBASE_USER / FIREBASE_PASSWORD not set", file=sys.stderr)
    sys.exit(1)

# Timeouts are (connect, read) tuples; the read timeout applies to every
# socket read while streaming, not to the whole transfer. The former 1200s read
# timeout kept a stalled stream hanging for 20 minutes (issue #464), and three
# such stalls exceeded the 1500s budget of the /reload_cache runner (issue #487).
AUTH_TIMEOUT = (10, 30)
DOWNLOAD_TIMEOUT = (10, 60)
# Attempts for the whole "GET + stream to disk" cycle. Previously only the
# initial GET was retried: a connection reset / read timeout in the middle of
# the stream failed the whole dump (~every 3rd day, issue #487).
MAX_ATTEMPTS = 4
BACKOFF_SECONDS = (10, 30, 90)
# Stay below the subprocess timeout used by the /reload_cache runner (1500s).
TOTAL_DEADLINE_SECONDS = 1200
_RETRYABLE_HTTP_STATUSES = {429, 500, 502, 503, 504}


class DumpError(Exception):
    """Dump failure with a human readable reason (retries already exhausted)."""


def _safe_error(exc):
    return re.sub(r'([?&](?:auth|key)=)[^&\s]+', r'\1[REDACTED]', str(exc))


def _fail(reason):
    """Report the failure reason on stderr so the runner can show it (issue #487)."""
    print(f"DUMP FAILED: {reason}", file=sys.stderr, flush=True)


def _is_retryable(exc):
    if isinstance(exc, requests.exceptions.HTTPError):
        resp = getattr(exc, 'response', None)
        return resp is not None and resp.status_code in _RETRYABLE_HTTP_STATUSES
    return isinstance(exc, (requests.exceptions.Timeout,
                            requests.exceptions.ConnectionError,
                            requests.exceptions.ChunkedEncodingError))


def _backoff(attempt, deadline, what, exc):
    """Sleep before the next attempt or raise DumpError when out of attempts/time."""
    if attempt >= MAX_ATTEMPTS:
        raise DumpError(f"{what} failed after {attempt} attempts: {type(exc).__name__}: {_safe_error(exc)}")
    wait = BACKOFF_SECONDS[min(attempt, len(BACKOFF_SECONDS)) - 1]
    if time.time() + wait > deadline:
        raise DumpError(
            f"{what} failed after {attempt} attempts (time budget {TOTAL_DEADLINE_SECONDS}s "
            f"exhausted): {type(exc).__name__}: {_safe_error(exc)}"
        )
    print(f"⏱️  {what} attempt {attempt}/{MAX_ATTEMPTS} failed ({type(exc).__name__}), retrying in {wait}s...", flush=True)
    time.sleep(wait)


def _authenticate(session, api_key, deadline):
    auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
    payload = {"email": FIREBASE_USER, "password": FIREBASE_PASSWORD, "returnSecureToken": True}
    attempt = 0
    while True:
        attempt += 1
        try:
            resp = session.post(auth_url, json=payload, timeout=AUTH_TIMEOUT)
            resp.raise_for_status()
            token = resp.json().get("idToken")
        except ValueError as e:  # invalid JSON body
            raise DumpError(f"authentication returned invalid JSON: {e}")
        except RequestException as e:
            if not _is_retryable(e):
                raise DumpError(f"authentication failed: {type(e).__name__}: {_safe_error(e)}")
            _backoff(attempt, deadline, "authentication", e)
            continue
        if not token:
            raise DumpError("authentication response has no idToken")
        print("✅ Authentication successful", flush=True)
        return token


def _stream_to_tmp(session, url, tmp_path, deadline):
    """Stream the dump to TMP_OUTPUT_FILE; return the number of bytes written."""
    bytes_written = 0
    chunk_count = 0
    if time.time() >= deadline:
        raise DumpError('total dump time budget exhausted before GET')
    with session.get(url, timeout=DOWNLOAD_TIMEOUT, stream=True) as response:
        response.raise_for_status()
        with open(tmp_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 512):
                if time.time() >= deadline:
                    raise DumpError('total dump time budget exhausted during transfer')
                if not chunk:
                    continue
                f.write(chunk)
                bytes_written += len(chunk)
                chunk_count += 1
                if chunk_count % 100 == 0:
                    print(f"  📊 Progress: {bytes_written / (1024*1024):.2f} MB downloaded...", flush=True)
            f.flush()
            os.fsync(f.fileno())
    return bytes_written


def _validate_tmp_dump(tmp_path):
    """Cheap structural check of the streamed file before it replaces the cache:
    a truncated stream must never become the live dump (issues #316, #487)."""
    size = os.path.getsize(tmp_path)
    if size == 0:
        raise DumpError("downloaded dump is empty")
    with open(tmp_path, "rb") as f:
        head = f.read(64).lstrip()
        f.seek(max(0, size - 64))
        tail = f.read().rstrip()
    if size <= 50 * 1024 * 1024:
        # Validate before publishing, not only for stats AFTER os.replace.
        try:
            with open(tmp_path, 'r', encoding='utf-8') as fh:
                value = json.load(fh)
            if value is not None and not isinstance(value, dict):
                raise DumpError('downloaded dump root is not a JSON object')
        except (ValueError, UnicodeError) as exc:
            raise DumpError(f'downloaded dump is not a complete JSON object: {exc}') from exc
        return
    if head.strip() == b"null" and tail.strip() == b"null":
        return
    if not (head.startswith(b"{") and tail.endswith(b"}")):
        raise DumpError(f"downloaded dump is not a complete JSON object ({size} bytes)")


def _remove_tmp(tmp_path):
    if tmp_path is None:
        return
    try:
        os.remove(tmp_path)
    except FileNotFoundError:
        pass
    except OSError as e:
        print(f"⚠️  Could not remove temp file {tmp_path}: {e}", file=sys.stderr)


def download_firebase_dump():
    """Downloads the entire Firebase Realtime Database dump.

    Returns True on success. On failure prints a single "DUMP FAILED: <reason>"
    line to stderr (shown by the runner, issue #487) and returns False.
    """
    if requests is None or Session is None:
        print(safe_get_messages().DB_DEPENDENCY_NOT_AVAILABLE_MSG)
        _fail("python 'requests' dependency is missing")
        return False

    # Create managed session for connection pooling
    from HELPERS.http_manager import get_managed_session
    session_manager = get_managed_session("firebase-download")
    session = session_manager.get_session()
    deadline = time.time() + TOTAL_DEADLINE_SECONDS
    tmp_path = None

    try:
        directory = os.path.dirname(os.path.abspath(OUTPUT_FILE))
        fd, tmp_path = tempfile.mkstemp(dir=directory, prefix='.firebase-dump-', suffix='.tmp')
        os.close(fd)
        print(safe_get_messages().DB_STARTING_FIREBASE_DUMP_MSG.format(datetime=datetime.now()), flush=True)

        database_url = FIREBASE_CONFIG.get("databaseURL")
        if not database_url:
            print(safe_get_messages().DB_DATABASE_URL_NOT_SET_MSG)
            _fail("databaseURL is not configured")
            return False

        # For downloading dump we use REST API and ID token via signInWithPassword.
        key = FIREBASE_CONFIG.get("apiKey")
        if not key:
            print(safe_get_messages().DB_API_KEY_NOT_SET_MSG)
            _fail("apiKey is not configured")
            return False

        # Валидация URL для предотвращения SSRF
        from urllib.parse import urlparse
        import ipaddress
        url_host = (urlparse(database_url).hostname or '').lower()
        if url_host in ('localhost', '127.0.0.1', '0.0.0.0', '::1', '[::1]') or \
           url_host.endswith('.local') or url_host.endswith('.internal') or \
           'localhost' in url_host:
            try:
                ip = ipaddress.ip_address(url_host)
                if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or str(ip) == '169.254.169.254':
                    _fail("blocked SSRF attempt: invalid database URL")
                    return False
            except ValueError:
                pass

        id_token = _authenticate(session, key, deadline)

        print(safe_get_messages().ALWAYS_ASK_DOWNLOADING_DATABASE_MSG, flush=True)
        reauthed = False
        attempt = 0
        while True:
            attempt += 1
            url = f"{database_url}/.json?auth={id_token}"
            try:
                _remove_tmp(tmp_path)
                bytes_written = _stream_to_tmp(session, url, tmp_path, deadline)
                break
            except RequestException as e:
                _remove_tmp(tmp_path)
                status = getattr(getattr(e, 'response', None), 'status_code', None)
                if status == 401 and not reauthed and attempt < MAX_ATTEMPTS:
                    # idToken expired/revoked between auth and download: re-auth once
                    print(f"🔐 Download got HTTP {status}, re-authenticating...", flush=True)
                    id_token = _authenticate(session, key, deadline)
                    reauthed = True
                    continue
                if not _is_retryable(e):
                    raise DumpError(f"download failed: {type(e).__name__}: {_safe_error(e)}")
                _backoff(attempt, deadline, "download", e)

        print(f"✅ Download complete: {bytes_written / (1024*1024):.2f} MB", flush=True)
        _validate_tmp_dump(tmp_path)
        # Atomically replace the target file to avoid partial reads by other services
        os.replace(tmp_path, OUTPUT_FILE)

        data = None
        file_size = os.path.getsize(OUTPUT_FILE)
        if file_size <= 50 * 1024 * 1024:  # only parse stats for reasonably sized dumps
            try:
                with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except (ValueError, OSError) as stats_err:
                logger.warning("Failed to parse Firebase dump for stats: %s", stats_err)

        if isinstance(data, dict) and data:
            print("✅ Firebase database downloaded successfully!")
            print(f"📊 Total root nodes: {len(data)}")
            print(f"💾 Saved to: {OUTPUT_FILE}")
            print(f"📏 File size: {file_size} bytes")
            print("\n📋 Database structure:")
            for node_key, node_value in data.items():
                if isinstance(node_value, dict):
                    print(f"  - {node_key}: {len(node_value)} sub-nodes")
                else:
                    print(f"  - {node_key}: {type(node_value).__name__}")
        else:
            print(safe_get_messages().DB_DATABASE_EMPTY_MSG)
            print(f"💾 Saved to: {OUTPUT_FILE}")
            print(f"📏 File size: {file_size} bytes")

        return True

    except DumpError as e:
        _remove_tmp(tmp_path)
        print(safe_get_messages().DB_ERROR_DOWNLOADING_DUMP_MSG.format(error=e))
        logger.error("Firebase dump failed: %s", e)
        _fail(str(e))
        return False
    except OSError as e:
        # Local write problems (disk quota / ENOSPC, Errno 122 on DE - issue #460)
        _remove_tmp(tmp_path)
        logger.error("Firebase dump local I/O error: %s", e)
        _fail(f"local I/O error: {e}")
        return False
    finally:
        _remove_tmp(tmp_path)
        # Always close the managed session
        session_manager.close()

def main():
    print("🚀 Firebase Database Dumper (config-driven)")
    print("=" * 40)

    # Check config
    if not FIREBASE_CONFIG or not FIREBASE_USER or not FIREBASE_PASSWORD:
        print(safe_get_messages().DB_NOT_ALL_PARAMETERS_SET_MSG)
        _fail("FIREBASE_CONF / FIREBASE_USER / FIREBASE_PASSWORD not set")
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
