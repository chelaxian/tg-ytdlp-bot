"""Live browser session shared by the admin dashboard and the bot.

An admin logs into any web service in a real Chrome that is driven from the
dashboard's "Browser" tab. When Xvfb is installed Chrome runs as a normal
windowed browser on a virtual screen (no headless traits, no script patches,
so sites see an ordinary Linux desktop); otherwise it falls back to headless. The bot then reads the *current*
cookies of that session whenever a user runs /cookies_from_browser or taps a
service button in /cookie, so cookies never have to be exported and sent by hand.

Design
* Chromium runs as its own long-lived process (detached), with a persistent
  profile, so restarting the dashboard (cron does it every 4 hours) or the bot
  does not log anybody out. Its DevTools (CDP) port listens on 127.0.0.1 only.
* Dashboard and bot talk to it over CDP with the standard library only: a small
  HTTP client for /json and a minimal RFC 6455 websocket client. No pip packages.
* Cookies are read live (Storage.getCookies) and rendered as a Netscape file
  that the existing cookie validation accepts.

Everything here is synchronous and short-lived: each call opens its own
connection, so it is safe to call from several threads and processes.
"""

from __future__ import annotations

import base64
import http.client
import ipaddress
import json
import logging
import os
import re
import secrets
import shutil
import socket
import struct
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

PROJECT_DIR = Path(os.environ.get("TG_DASHBOARD_PROJECT_DIR", str(Path(__file__).resolve().parent.parent)))
PROFILE_DIR = PROJECT_DIR / "CONFIG" / ".browser_profile"
PID_FILE = PROJECT_DIR / "CONFIG" / ".browser_session.pid"
XVFB_PID_FILE = PROJECT_DIR / "CONFIG" / ".browser_xvfb.pid"
TZ_CACHE_FILE = PROJECT_DIR / "CONFIG" / ".browser_timezone"
AUTOSTART_FILE = PROJECT_DIR / "CONFIG" / ".browser_autostart"   # present while the admin wants the browser running
PARK_URL = "about:blank#tg-park"                                   # the hub's resting tab, never shown in the panel
TABS_FILE = PROJECT_DIR / "CONFIG" / ".browser_tabs.json"           # last open tabs, reopened after a restart
SCREEN = (1920, 1080)                 # virtual screen of the windowed browser (an ordinary Full HD monitor)
WINDOW_UI_HEIGHT = 87                 # tab strip + toolbar of a normal Chrome window
_TZ_RE = re.compile(r"[A-Za-z_]{2,32}(/[A-Za-z0-9_+\-]{1,32}){0,2}")
_PROXY_RE = re.compile(r"(https?|socks5h?|socks4)://[A-Za-z0-9.\-:\[\]]+")

CDP_HOST = "127.0.0.1"
VIEWPORT = (1280, 800)
CONNECT_TIMEOUT = 3.0
CALL_TIMEOUT = 12.0

# Services the /cookie buttons ask for -> cookie domains that belong to them.
SERVICE_DOMAINS: Dict[str, Tuple[str, ...]] = {
    "youtube": ("youtube.com", "youtu.be", "youtube-nocookie.com", "google.com", "googlevideo.com"),
    "twitter": ("x.com", "twitter.com", "t.co", "twimg.com"),
    "instagram": ("instagram.com", "cdninstagram.com"),
    "vk": ("vk.com", "vk.ru", "vk.me", "vkvideo.ru", "vkontakte.ru", "vk-cdn.net", "vkuser.net", "userapi.com"),
    "tiktok": ("tiktok.com", "tiktokv.com", "tiktokv.eu", "tiktokw.eu", "tiktokcdn.com", "tiktokcdn-us.com"),
}
# /cookies_from_browser hands the bot only these services; every other cookie of the browser session stays in the browser
COOKIE_SERVICES: Tuple[str, ...] = ("youtube", "twitter", "instagram", "vk", "tiktok")

_BLOCKED_HOSTS = {"localhost", "localhost.localdomain", "ip6-localhost", "metadata.google.internal"}


class BrowserError(Exception):
    """Raised for every failure talking to / starting the browser."""


# --------------------------------------------------------------------------------------
# Settings (all optional; read lazily so the module imports without Config)
# --------------------------------------------------------------------------------------

def _cfg(name: str, default: Any) -> Any:
    try:
        from CONFIG.config import Config
        return getattr(Config, name, default)
    except Exception:
        return default


def enabled() -> bool:
    return bool(_cfg("BROWSER_SESSION_ENABLED", True))


def cdp_port() -> int:
    try:
        port = int(_cfg("BROWSER_CDP_PORT", 9223))
    except (TypeError, ValueError):
        port = 9223
    return port if 1024 <= port <= 65535 else 9223


def proxy_url() -> str:
    """Optional Config.BROWSER_PROXY on the server; empty (default) = the browser leaves from the server itself."""
    candidate = str(_cfg("BROWSER_PROXY", "") or "").strip()
    return candidate if candidate and _PROXY_RE.fullmatch(candidate) else ""


_REACH_CACHE: Dict[str, Tuple[float, bool]] = {}


def proxy_reachable(url: str, max_age: float = 5.0) -> bool:
    """TCP connect to the proxy (a few seconds of cache: the panel polls this)."""
    now = time.monotonic()
    cached = _REACH_CACHE.get(url)
    if cached and now - cached[0] < max_age:
        return cached[1]
    parsed = urlparse(url)
    ok = False
    try:
        with socket.create_connection((parsed.hostname, parsed.port or 1080), timeout=1.5):
            ok = True
    except (OSError, TypeError, ValueError):
        ok = False
    _REACH_CACHE[url] = (now, ok)
    return ok


def find_executable() -> Optional[str]:
    configured = str(_cfg("BROWSER_EXECUTABLE", "") or "").strip()
    if configured:
        return configured if os.path.isfile(configured) else None
    import glob
    for name in ("google-chrome-stable", "google-chrome"):   # the real Chrome first: its identity needs no patching
        found = shutil.which(name)
        if found:
            return found
    for pattern in ("/opt/tg-browser/browsers/chromium-*/chrome-linux*/chrome",
                    os.path.expanduser("~/.cache/ms-playwright/chromium-*/chrome-linux*/chrome")):
        found = sorted(glob.glob(pattern))          # Playwright-installed Chromium (the only ARM64 build)
        if found:
            return found[-1]
    for name in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome",
                 "microsoft-edge", "msedge", "brave-browser"):
        found = shutil.which(name)
        if found:
            return found
    for path in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                 r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                 r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                 r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"):
        if os.path.isfile(path):
            return path
    return None


# --------------------------------------------------------------------------------------
# URL policy for the address bar
# --------------------------------------------------------------------------------------

def normalize_url(raw: str) -> str:
    """Turn address-bar input into a safe http(s) URL, or raise BrowserError.

    Loopback / private / link-local targets are refused: the browser must not
    become a way to reach the server's own services (dashboard, CDP, metadata).
    """
    text = (raw or "").strip()
    if not text or len(text) > 2048 or re.search(r"[\x00-\x1f\x7f\s]", text):
        raise BrowserError("bad_url")
    if "://" not in text:
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", text) and not re.match(r"^[^/]+:\d+(/|$)", text):
            raise BrowserError("bad_url")           # javascript:, data:, file:, about: ...
        text = "https://" + text
    parsed = urlparse(text)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise BrowserError("bad_url")
    host = parsed.hostname.lower().rstrip(".")
    if host in _BLOCKED_HOSTS or host.endswith((".localhost", ".local", ".internal")):
        raise BrowserError("blocked_host")
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        # decimal / hex / octal IPv4 tricks ("2130706433", "0x7f.1") are not real domain names
        if re.fullmatch(r"(0x[0-9a-f]+|\d+)(\.(0x[0-9a-f]+|\d+)){0,3}", host):
            raise BrowserError("blocked_host")
    else:
        if not ip.is_global:
            raise BrowserError("blocked_host")
    return text


# --------------------------------------------------------------------------------------
# CDP transport (stdlib): HTTP endpoints + a tiny websocket client
# --------------------------------------------------------------------------------------

def _http(path: str, method: str = "GET", timeout: float = CONNECT_TIMEOUT) -> Any:
    conn = http.client.HTTPConnection(CDP_HOST, cdp_port(), timeout=timeout)
    try:
        conn.request(method, path)
        resp = conn.getresponse()
        body = resp.read()
        if resp.status >= 400:
            raise BrowserError(f"cdp_http_{resp.status}")
        if not body:
            return None
        try:
            return json.loads(body)
        except ValueError:
            return body.decode("utf-8", "replace")
    except (OSError, http.client.HTTPException) as exc:
        raise BrowserError("not_running") from exc
    finally:
        conn.close()


class _WebSocket:
    """Client-side RFC 6455 websocket: text frames, masking, ping/pong, fragments."""

    def __init__(self, url: str, timeout: float = CALL_TIMEOUT):
        parsed = urlparse(url)
        host, port = parsed.hostname, parsed.port
        if host != CDP_HOST or port != cdp_port():
            raise BrowserError("bad_ws_url")             # never follow a ws URL to another host
        self.sock = socket.create_connection((host, port), timeout=CONNECT_TIMEOUT)
        self.sock.settimeout(timeout)
        key = base64.b64encode(secrets.token_bytes(16)).decode()
        path = parsed.path + (f"?{parsed.query}" if parsed.query else "")
        self.sock.sendall((f"GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\nUpgrade: websocket\r\n"
                           f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\n"
                           f"Sec-WebSocket-Version: 13\r\n\r\n").encode())
        head = b""
        while b"\r\n\r\n" not in head:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise BrowserError("ws_handshake_failed")
            head += chunk
            if len(head) > 65536:
                raise BrowserError("ws_handshake_failed")
        head, _, self._buf = head.partition(b"\r\n\r\n")
        if b" 101 " not in head.split(b"\r\n", 1)[0] + b" ":
            raise BrowserError("ws_handshake_failed")

    def close(self) -> None:
        try:
            self.sock.close()
        except OSError:
            pass

    def _read(self, n: int) -> bytes:
        while len(self._buf) < n:
            chunk = self.sock.recv(65536)
            if not chunk:
                raise BrowserError("ws_closed")
            self._buf += chunk
        data, self._buf = self._buf[:n], self._buf[n:]
        return data

    def readable(self, timeout: float) -> bool:
        """True when a frame can be read now (data already buffered or arriving within `timeout`)."""
        if self._buf:
            return True
        import select
        try:
            return bool(select.select([self.sock], [], [], timeout)[0])
        except (OSError, ValueError):
            return True            # let recv() report the closed socket

    def send(self, text: str) -> None:
        payload = text.encode("utf-8")
        header = bytearray([0x81])
        n = len(payload)
        if n < 126:
            header.append(0x80 | n)
        elif n < 65536:
            header += bytes([0x80 | 126]) + struct.pack(">H", n)
        else:
            header += bytes([0x80 | 127]) + struct.pack(">Q", n)
        mask = secrets.token_bytes(4)
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload)) if n < 4096 else _xor(payload, mask)
        self.sock.sendall(bytes(header) + mask + masked)

    def recv(self) -> str:
        message = b""
        while True:
            b0, b1 = self._read(2)
            fin, opcode = b0 & 0x80, b0 & 0x0F
            length = b1 & 0x7F
            if length == 126:
                length = struct.unpack(">H", self._read(2))[0]
            elif length == 127:
                length = struct.unpack(">Q", self._read(8))[0]
            if length > 64 * 1024 * 1024:
                raise BrowserError("ws_frame_too_large")
            payload = self._read(length) if length else b""
            if opcode == 0x8:
                raise BrowserError("ws_closed")
            if opcode == 0x9:                            # ping -> pong
                self.sock.sendall(bytes([0x8A, 0x80 | len(payload)]) + b"\0\0\0\0" + payload[:125])
                continue
            if opcode == 0xA:
                continue
            message += payload
            if fin:
                return message.decode("utf-8", "replace")


def _xor(data: bytes, mask: bytes) -> bytes:
    key = (mask * (len(data) // 4 + 1))[:len(data)]
    return (int.from_bytes(data, "big") ^ int.from_bytes(key, "big")).to_bytes(len(data), "big")


def _cdp(ws_url: str, calls: List[Tuple[str, Dict[str, Any]]], timeout: float = CALL_TIMEOUT) -> List[Any]:
    """Run CDP commands in order on one connection; return each result (raises on error)."""
    ws = _WebSocket(ws_url, timeout=timeout)
    results: List[Any] = []
    try:
        for i, (method, params) in enumerate(calls, start=1):
            ws.send(json.dumps({"id": i, "method": method, "params": params or {}}))
            deadline = time.monotonic() + timeout
            while True:
                if time.monotonic() > deadline:
                    raise BrowserError("cdp_timeout")
                try:
                    msg = json.loads(ws.recv())
                except socket.timeout as exc:
                    raise BrowserError("cdp_timeout") from exc
                if msg.get("id") == i:
                    if "error" in msg:
                        raise BrowserError("cdp_error: " + str(msg["error"].get("message", ""))[:200])
                    results.append(msg.get("result") or {})
                    break
    except OSError as exc:
        raise BrowserError("not_running") from exc
    finally:
        ws.close()
    return results


# --------------------------------------------------------------------------------------
# Process lifecycle
# --------------------------------------------------------------------------------------

def is_running() -> bool:
    try:
        info = _http("/json/version", timeout=1.5)
    except BrowserError:
        return False
    return isinstance(info, dict) and "webSocketDebuggerUrl" in info


def is_alive() -> bool:
    """The browser exists, even if it is too busy to answer right now (DevTools port taken or the profile locked).

    Used before an automatic restart: starting a second Chrome on a live profile only hands the command line to the
    running one, so a slow browser must never be "restarted".
    """
    if is_running():
        return True
    try:
        with socket.create_connection((CDP_HOST, cdp_port()), timeout=1.5):
            return True
    except OSError:
        pass
    try:
        target = os.readlink(_profile_dir() / "SingletonLock")      # "<host>-<pid>" while a Chrome owns the profile
        os.kill(int(target.rsplit("-", 1)[1]), 0)
        return True
    except (OSError, ValueError, IndexError):
        return False


def _outside_service(cmd: List[str], kwargs: Dict[str, Any], name: str) -> List[str]:
    """Run `cmd` in a systemd scope of its own when the caller is a systemd service.

    Otherwise restarting the dashboard service (cron does it every few hours) kills the browser with it: systemd stops
    every process of the service's cgroup, whatever session or process group they are in. The scope is created as root
    and the browser then drops to its unprivileged user with setpriv.
    """
    if not sys.platform.startswith("linux") or not hasattr(os, "geteuid") or os.geteuid() != 0:
        return cmd
    if not os.path.isdir("/run/systemd/system") or not os.environ.get("INVOCATION_ID"):
        return cmd                                          # not started by systemd: nothing would kill it
    run = shutil.which("systemd-run")
    if not run:
        return cmd
    wrapped = [run, "--scope", "--quiet", "--collect", f"--unit={name}-{cdp_port()}-{int(time.time() * 1000)}"]
    uid, gid = kwargs.pop("user", None), kwargs.pop("group", None)
    kwargs.pop("extra_groups", None)
    if uid is not None:
        setpriv = shutil.which("setpriv")
        if not setpriv:
            kwargs.update(user=uid, group=gid, extra_groups=[])  # cannot drop privileges after the scope: stay inside
            return cmd
        wrapped += ["--", setpriv, f"--reuid={uid}", f"--regid={gid}", "--clear-groups", "--"]
    else:
        wrapped.append("--")
    return wrapped + cmd


def save_tabs(urls: List[str]) -> None:
    keep = [u for u in urls if u.startswith(("http://", "https://"))][:20]
    if not keep:
        return
    try:
        TABS_FILE.write_text(json.dumps(keep), encoding="utf-8")
    except OSError:
        pass


def saved_tabs() -> List[str]:
    try:
        data = json.loads(TABS_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    out = []
    for url in data if isinstance(data, list) else []:
        try:
            out.append(normalize_url(str(url)))
        except BrowserError:
            continue
    return out[:20]


def _browser_ws() -> str:
    info = _http("/json/version")
    if not isinstance(info, dict) or not info.get("webSocketDebuggerUrl"):
        raise BrowserError("not_running")
    return info["webSocketDebuggerUrl"]


def _user_agent_fix(executable: str) -> Optional[str]:
    """Headless Chromium announces 'HeadlessChrome', which many sites refuse to log in; drop it."""
    try:
        out = subprocess.run([executable, "--version"], capture_output=True, text=True, timeout=15).stdout
        version = re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", out)
        if not version:
            return None
        major = version.group(1)
        platform = ("Windows NT 10.0; Win64; x64" if sys.platform == "win32"
                    else "X11; Linux x86_64")
        return (f"Mozilla/5.0 ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) "
                f"Chrome/{major}.0.0.0 Safari/537.36")
    except Exception:
        return None


def _run_as():
    """(pw_entry) of the unprivileged user Chromium should run as, or None (run as the current user)."""
    if not hasattr(os, "geteuid") or os.geteuid() != 0:
        return None
    name = str(_cfg("BROWSER_RUN_AS", "tgbrowser") or "").strip()
    if not name:
        return None
    try:
        import pwd
        entry = pwd.getpwnam(name)
    except (ImportError, KeyError):
        return None
    return entry if entry.pw_uid != 0 else None


def _profile_dir() -> Path:
    entry = _run_as()
    return Path(entry.pw_dir) / "tg-browser-profile" if entry else PROFILE_DIR


def _pid_alive(pid_file: Path) -> Optional[int]:
    try:
        pid = int(pid_file.read_text().strip())
        os.kill(pid, 0)
        return pid
    except (OSError, ValueError):
        return None


def _xvfb_binary() -> Optional[str]:
    """Xvfb lets Chrome run as an ordinary windowed browser; BROWSER_HEADLESS=True forces headless instead."""
    if sys.platform == "win32" or bool(_cfg("BROWSER_HEADLESS", False)):
        return None
    return shutil.which("Xvfb")


def _start_display(xvfb: str, popen_kwargs: Dict[str, Any]) -> Optional[str]:
    """Start (or reuse) the virtual screen; returns the DISPLAY value or None when it cannot start."""
    num = 90 + cdp_port() % 10
    display = f":{num}"
    sock = Path(f"/tmp/.X11-unix/X{num}")
    if _pid_alive(XVFB_PID_FILE) and sock.exists():
        return display
    lock = Path(f"/tmp/.X{num}-lock")
    try:                                                    # a lock left by a crashed server blocks the display
        if lock.exists():
            os.kill(int(lock.read_text().strip()), 0)
    except (OSError, ValueError):
        for stale in (lock, sock):
            try:
                stale.unlink()
            except OSError:
                pass
    try:
        kw = dict(popen_kwargs)
        cmd = _outside_service([xvfb, display, "-screen", "0", f"{SCREEN[0]}x{SCREEN[1]}x24", "-nolisten", "tcp",
                                "-dpi", "96", "-nocursor"], kw, "tg-ytdlp-xvfb")
        proc = subprocess.Popen(cmd, **kw)
    except OSError as exc:
        logger.warning("[browser] Xvfb did not start: %s", exc)
        return None
    for _ in range(50):
        if sock.exists():
            try:
                XVFB_PID_FILE.write_text(str(proc.pid))
            except OSError:
                pass
            return display
        if proc.poll() is not None:
            break
        time.sleep(0.1)
    logger.warning("[browser] Xvfb did not come up, falling back to headless")
    try:
        proc.kill()
    except OSError:
        pass
    return None


def is_windowed() -> bool:
    """True when the running browser is a normal window on the virtual screen (not headless)."""
    return bool(_pid_alive(XVFB_PID_FILE))


def _stop_display() -> None:
    pid = _pid_alive(XVFB_PID_FILE)
    if pid:
        try:
            os.kill(pid, 15)
        except OSError:
            pass
    try:
        XVFB_PID_FILE.unlink()
    except OSError:
        pass


def browser_timezone() -> str:
    """Time zone of the place the browser leaves from: BROWSER_TIMEZONE, else looked up once for the server's IP.

    A browser in UTC whose address is in Frankfurt is an obvious mismatch for anti-bot checks.
    """
    configured = str(_cfg("BROWSER_TIMEZONE", "") or "").strip()
    if configured:
        return configured if _TZ_RE.fullmatch(configured) else ""
    try:
        cached = TZ_CACHE_FILE.read_text(encoding="utf-8").strip()
        if _TZ_RE.fullmatch(cached) and time.time() - TZ_CACHE_FILE.stat().st_mtime < 7 * 86400:
            return cached
    except OSError:
        pass
    found = ""
    try:
        conn = http.client.HTTPConnection("ip-api.com", 80, timeout=4)
        conn.request("GET", "/json/?fields=timezone")
        found = str(json.loads(conn.getresponse().read(2048) or b"{}").get("timezone") or "")
    except (OSError, ValueError, http.client.HTTPException):
        found = ""
    if not _TZ_RE.fullmatch(found):
        return ""
    try:
        TZ_CACHE_FILE.write_text(found, encoding="utf-8")
    except OSError:
        pass
    return found


def start() -> Dict[str, Any]:
    """Launch Chrome (detached) unless it is already up."""
    if not enabled():
        raise BrowserError("disabled")
    if is_running():
        return {"started": False}
    if is_alive():
        raise BrowserError("busy")                       # alive but not answering yet: never start a second one
    exe = find_executable()
    if not exe:
        raise BrowserError("no_browser")
    entry = _run_as()
    profile = _profile_dir()
    profile.mkdir(parents=True, exist_ok=True)
    try:
        if entry:
            os.chown(profile, entry.pw_uid, entry.pw_gid)
        os.chmod(profile, 0o700)
    except OSError:
        pass
    kwargs: Dict[str, Any] = {"stdin": subprocess.DEVNULL, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
    if entry:
        kwargs.update(user=entry.pw_uid, group=entry.pw_gid, extra_groups=[],
                      env={"HOME": entry.pw_dir, "PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LANG": "C.UTF-8"})
    elif sys.platform != "win32":
        kwargs["env"] = dict(os.environ)
    if sys.platform == "win32":
        kwargs["creationflags"] = 0x00000008 | 0x00000200   # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    else:
        kwargs["start_new_session"] = True                  # survives dashboard / bot restarts
        tz = browser_timezone()
        if tz:
            kwargs["env"]["TZ"] = tz
    xvfb = _xvfb_binary()
    display = _start_display(xvfb, dict(kwargs)) if xvfb else None
    if display:
        kwargs["env"]["DISPLAY"] = display
        # an ordinary Chrome window on a Full HD virtual screen: nothing to hide, nothing patched
        mode = [f"--window-size={VIEWPORT[0]},{VIEWPORT[1] + WINDOW_UI_HEIGHT}", "--window-position=0,0",
                "--test-type",                              # no "unsupported command-line flag" bar over the page
                "--ignore-gpu-blocklist", "--use-angle=gl"]  # WebGL through Mesa (llvmpipe), like any Linux box without a GPU
    else:
        mode = ["--headless=new", f"--window-size={VIEWPORT[0]},{VIEWPORT[1]}"]
    args = [
        exe, *mode, f"--remote-debugging-port={cdp_port()}", f"--remote-debugging-address={CDP_HOST}",
        f"--user-data-dir={profile}", "--force-device-scale-factor=1", "--no-first-run", "--no-default-browser-check",
        "--disable-blink-features=AutomationControlled", "--disable-background-networking",
        "--restore-last-session",                   # after a crash or reboot the tabs (and session cookies) come back
        "--disable-sync", "--disable-dev-shm-usage", "--password-store=basic", "--lang=en-US", "--accept-lang=en-US,en",
        "--mute-audio",
        # lean profile: the browser is only used to log in (none of these is visible to a web page)
        "--disable-extensions", "--disable-breakpad", "--disable-component-update", "--no-pings",
        "--disable-default-apps", "--disable-hang-monitor", "--disable-smooth-scrolling", "--disable-lcd-text",
        "--disable-domain-reliability", "--disable-client-side-phishing-detection", "--metrics-recording-only",
        # FedCm: "Sign in with Google" would open a browser dialog the panel cannot show; without it Google uses a popup
        "--disable-features=Translate,BackForwardCache,MediaRouter,OptimizationHints,InterestFeedContentSuggestions,FedCm",
        "--renderer-process-limit=3",
        # login pages need no video: no autoplay, no hardware decode (the server also runs the bot's ffmpeg jobs)
        "--autoplay-policy=user-gesture-required", "--disable-accelerated-video-decode",
    ]
    extra = str(_cfg("BROWSER_EXTRA_ARGS", "") or "").split()
    args.extend(a for a in extra if re.fullmatch(r"--[A-Za-z0-9][A-Za-z0-9=,.:_/\-]{0,200}", a))
    proxy = proxy_url()
    using_proxy = False
    if proxy:
        if proxy_reachable(proxy, max_age=0):
            args.append(f"--proxy-server={proxy}")
            # WebRTC could still reveal the server's own address around the proxy
            args.append("--force-webrtc-ip-handling-policy=disable_non_proxied_udp")
            using_proxy = True
        else:
            logger.warning("[browser] proxy %s is not reachable, starting without it", proxy)
    ua = None if display else _user_agent_fix(exe)       # only headless announces itself as "HeadlessChrome"
    if ua:
        args.append(f"--user-agent={ua}")
    if hasattr(os, "geteuid") and os.geteuid() == 0 and not entry:
        args.append("--no-sandbox")                      # Chromium refuses to run as root otherwise
    sessions = profile / "Default" / "Sessions"
    try:
        restoring = sessions.is_dir() and any(sessions.iterdir())
    except OSError:
        restoring = False
    if not restoring:                                # a saved session brings its own tabs back (no blank tab pile-up)
        args.append("about:blank")
    try:
        niceness = int(_cfg("BROWSER_NICE", 0) or 0)       # 0 = normal priority (an interactive login must stay responsive)
    except (TypeError, ValueError):
        niceness = 0
    if niceness > 0 and hasattr(os, "nice"):
        kwargs["preexec_fn"] = lambda: os.nice(niceness)
    for attempt in (0, 1):
        launch = args if attempt == 0 or "--no-sandbox" in args else args + ["--no-sandbox"]
        kw = dict(kwargs)
        launch = _outside_service(launch, kw, "tg-ytdlp-browser")
        try:
            proc = subprocess.Popen(launch, **kw)
        except OSError as exc:
            raise BrowserError(f"launch_failed: {exc}") from exc
        try:
            PID_FILE.write_text(str(proc.pid))
        except OSError:
            pass
        if niceness < 0 and hasattr(os, "setpriority"):
            try:
                os.setpriority(os.PRIO_PROCESS, proc.pid, niceness)
            except OSError:
                pass
        deadline = time.monotonic() + 20
        while time.monotonic() < deadline:
            if is_running():
                try:
                    AUTOSTART_FILE.write_text("1")
                except OSError:
                    pass
                return {"started": True, "pid": proc.pid, "sandbox": "--no-sandbox" not in launch,
                        "headed": bool(display), "proxy": using_proxy, "proxy_wanted": bool(proxy)}
            if proc.poll() is not None:
                break                                    # died: retry once without the sandbox
            time.sleep(0.3)
        else:
            raise BrowserError("launch_timeout")
        if "--no-sandbox" in launch:
            break
    raise BrowserError("launch_failed: exited early")


def wants_autostart() -> bool:
    return AUTOSTART_FILE.exists()


def stop(keep_autostart: bool = False) -> bool:
    """Close the browser gracefully (profile and persistent cookies are flushed).

    An explicit stop also means "do not bring it back by itself" unless keep_autostart is set.
    """
    if not keep_autostart:
        try:
            AUTOSTART_FILE.unlink()
        except OSError:
            pass
    try:
        _cdp(_browser_ws(), [("Browser.close", {})], timeout=5)
    except BrowserError:
        pass
    for _ in range(30):
        if not is_running():
            break
        time.sleep(0.2)
    try:
        PID_FILE.unlink()
    except OSError:
        pass
    stopped = not is_running()
    if stopped:
        _stop_display()
    return stopped


# --------------------------------------------------------------------------------------
# Tabs and page interaction
# --------------------------------------------------------------------------------------

_TARGET_ID = re.compile(r"^[A-Za-z0-9]{8,64}$")


def _check_id(tab_id: str) -> str:
    if not isinstance(tab_id, str) or not _TARGET_ID.fullmatch(tab_id):
        raise BrowserError("bad_tab")
    return tab_id


def list_tabs() -> List[Dict[str, str]]:
    tabs = []
    for t in _http("/json/list") or []:
        if t.get("type") == "page" and t.get("id") and not str(t.get("url") or "").startswith(PARK_URL):
            tabs.append({"id": t["id"], "title": str(t.get("title") or "")[:200], "url": str(t.get("url") or "")[:2048]})
    return tabs


def _tab_ws(tab_id: str) -> str:
    _check_id(tab_id)
    for t in _http("/json/list") or []:
        if t.get("id") == tab_id and t.get("webSocketDebuggerUrl"):
            return t["webSocketDebuggerUrl"]
    raise BrowserError("no_such_tab")


def new_tab(url: str = "about:blank") -> Dict[str, str]:
    target = "about:blank" if url == "about:blank" else normalize_url(url)
    ws = _browser_ws()
    res = _cdp(ws, [("Target.createTarget", {"url": target})])[0]
    return {"id": res.get("targetId", "")}


def close_tab(tab_id: str) -> None:
    _check_id(tab_id)
    _cdp(_browser_ws(), [("Target.closeTarget", {"targetId": tab_id})])


def activate_tab(tab_id: str) -> None:
    _check_id(tab_id)
    _http(f"/json/activate/{tab_id}")


def navigate(tab_id: str, url: str) -> None:
    _cdp(_tab_ws(tab_id), [("Page.navigate", {"url": normalize_url(url)})])


def history_step(tab_id: str, action: str) -> None:
    ws = _tab_ws(tab_id)
    if action == "reload":
        _cdp(ws, [("Page.reload", {})])
        return
    if action not in ("back", "forward"):
        raise BrowserError("bad_action")
    hist = _cdp(ws, [("Page.getNavigationHistory", {})])[0]
    index = hist.get("currentIndex", 0) + (-1 if action == "back" else 1)
    entries = hist.get("entries") or []
    if 0 <= index < len(entries):
        _cdp(ws, [("Page.navigateToHistoryEntry", {"entryId": entries[index]["id"]})])


def screenshot(tab_id: str, quality: int = 55) -> bytes:
    ws = _tab_ws(tab_id)
    res = _cdp(ws, [("Page.captureScreenshot", {"format": "jpeg", "quality": max(20, min(90, quality)),
                                                "optimizeForSpeed": True})])[0]
    try:
        return base64.b64decode(res["data"])
    except (KeyError, ValueError) as exc:
        raise BrowserError("no_screenshot") from exc


_KEYS = {  # key -> (code, windowsVirtualKeyCode, text)
    "Enter": ("Enter", 13, "\r"), "Backspace": ("Backspace", 8, ""), "Tab": ("Tab", 9, ""),
    "Escape": ("Escape", 27, ""), "Delete": ("Delete", 46, ""), "ArrowLeft": ("ArrowLeft", 37, ""),
    "ArrowUp": ("ArrowUp", 38, ""), "ArrowRight": ("ArrowRight", 39, ""), "ArrowDown": ("ArrowDown", 40, ""),
    "Home": ("Home", 36, ""), "End": ("End", 35, ""), "PageUp": ("PageUp", 33, ""), "PageDown": ("PageDown", 34, ""),
}
_MODIFIERS = {"alt": 1, "ctrl": 2, "meta": 4, "shift": 8}


def _coord(value: Any, upper: float) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise BrowserError("bad_input") from exc
    if not (0 <= number <= upper):
        raise BrowserError("bad_input")
    return number


def _char_key(ch: str) -> Dict[str, Any]:
    """KeyboardEvent fields for one typed character (sites such as Google read code / keyCode)."""
    if "a" <= ch.lower() <= "z" and ch.isascii():
        return {"code": "Key" + ch.upper(), "windowsVirtualKeyCode": ord(ch.upper())}
    if ch.isdigit() and ch.isascii():
        return {"code": "Digit" + ch, "windowsVirtualKeyCode": ord(ch)}
    if ch == " ":
        return {"code": "Space", "windowsVirtualKeyCode": 32}
    return {}


def build_input_calls(kind: str, vw: float = VIEWPORT[0], vh: float = VIEWPORT[1], **p: Any) -> List[Tuple[str, Dict[str, Any]]]:
    """CDP commands for one input event. kind: click | dblclick | scroll | text | key.

    x / y are CSS pixels inside the page viewport (vw x vh)."""
    calls: List[Tuple[str, Dict[str, Any]]] = []
    if kind in ("click", "dblclick"):
        x, y = _coord(p.get("x"), vw), _coord(p.get("y"), vh)
        button = p.get("button") if p.get("button") in ("left", "right", "middle") else "left"
        base = {"x": x, "y": y, "button": button}
        calls.append(("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": x, "y": y}))
        for count in ((1, 2) if kind == "dblclick" else (1,)):
            calls.append(("Input.dispatchMouseEvent", {**base, "type": "mousePressed", "clickCount": count}))
            calls.append(("Input.dispatchMouseEvent", {**base, "type": "mouseReleased", "clickCount": count}))
    elif kind == "scroll":
        x, y = _coord(p.get("x"), vw), _coord(p.get("y"), vh)
        dx = max(-5000.0, min(5000.0, float(p.get("dx") or 0)))
        dy = max(-5000.0, min(5000.0, float(p.get("dy") or 0)))
        calls.append(("Input.dispatchMouseEvent", {"type": "mouseWheel", "x": x, "y": y, "deltaX": dx, "deltaY": dy}))
    elif kind == "text":
        text = str(p.get("text") or "")[:5000]
        if not text:
            return calls
        if len(text) > 1 or not text.isprintable():
            calls.append(("Input.insertText", {"text": text}))       # paste-like, one shot
        else:
            fields = _char_key(text)
            mods = 8 if text.isupper() else 0
            calls.append(("Input.dispatchKeyEvent", {"type": "keyDown", "text": text, "unmodifiedText": text.lower() if mods else text,
                                                     "key": text, "modifiers": mods, **fields}))
            calls.append(("Input.dispatchKeyEvent", {"type": "keyUp", "key": text, "modifiers": mods, **fields}))
    elif kind == "key":
        key = str(p.get("key") or "")
        if key not in _KEYS:
            raise BrowserError("bad_key")
        code, vk, text = _KEYS[key]
        mods = sum(bit for name, bit in _MODIFIERS.items() if p.get(name))
        down = {"type": "keyDown" if not text else "rawKeyDown", "key": key, "code": code,
                "windowsVirtualKeyCode": vk, "nativeVirtualKeyCode": vk, "modifiers": mods}
        calls.append(("Input.dispatchKeyEvent", down))
        if text:
            calls.append(("Input.dispatchKeyEvent", {**down, "type": "char", "text": text}))
        calls.append(("Input.dispatchKeyEvent", {**down, "type": "keyUp"}))
    else:
        raise BrowserError("bad_input")
    return calls


def send_input(tab_id: str, kind: str, **p: Any) -> None:
    """One-shot variant (own connection); the dashboard uses the persistent hub instead."""
    _cdp(_tab_ws(tab_id), build_input_calls(kind, **p))


# --------------------------------------------------------------------------------------
# Cookies
# --------------------------------------------------------------------------------------

def get_cookies() -> List[Dict[str, Any]]:
    """Every cookie of the live session, all tabs and domains combined."""
    res = _cdp(_browser_ws(), [("Storage.getCookies", {})])[0]
    cookies = res.get("cookies") or []
    return [c for c in cookies if isinstance(c, dict) and c.get("name") is not None and c.get("domain")]


def domain_matches(cookie_domain: str, wanted: Iterable[str]) -> bool:
    host = cookie_domain.lstrip(".").lower()
    return any(host == d or host.endswith("." + d) for d in wanted)


def filter_cookies(cookies: List[Dict[str, Any]], services: Optional[Iterable[str]] = None,
                   domains: Optional[Iterable[str]] = None) -> List[Dict[str, Any]]:
    wanted: List[str] = [d.lower() for d in (domains or [])]
    for name in services or []:
        wanted.extend(SERVICE_DOMAINS.get(name, ()))
    if not wanted:
        return list(cookies)
    return [c for c in cookies if domain_matches(str(c["domain"]), wanted)]


def _clean(value: Any) -> str:
    return re.sub(r"[\t\r\n\x00]", "", str(value))


def to_netscape(cookies: List[Dict[str, Any]], session_ttl: int = 7 * 24 * 3600) -> str:
    """Netscape cookie file in the exact shape HELPERS.cookie_file.validate_cookie_bytes accepts."""
    now = int(time.time())
    lines = ["# Netscape HTTP Cookie File", "# Exported from the live dashboard browser session", ""]
    for c in sorted(cookies, key=lambda c: (str(c["domain"]), str(c.get("path", "/")), str(c["name"]))):
        domain = _clean(c["domain"])
        include_sub = domain.startswith(".")
        expires = c.get("expires")
        # session cookies (expires -1/0) live as long as the browser: give them a finite expiry
        exp = int(expires) if isinstance(expires, (int, float)) and expires > 0 else now + session_ttl
        prefix = "#HttpOnly_" if c.get("httpOnly") else ""
        lines.append("\t".join([
            prefix + domain, "TRUE" if include_sub else "FALSE", _clean(c.get("path") or "/"),
            "TRUE" if c.get("secure") else "FALSE", str(exp), _clean(c["name"]), _clean(c.get("value", "")),
        ]))
    return "\n".join(lines) + "\n"


def export_netscape(services: Optional[Iterable[str]] = None,
                    domains: Optional[Iterable[str]] = None) -> Tuple[Optional[bytes], int, List[str]]:
    """(netscape bytes or None, cookie count, sorted registrable-ish domain list).

    Raises BrowserError when the browser is not running.
    """
    chosen = filter_cookies(get_cookies(), services, domains)
    if not chosen:
        return None, 0, []
    names = sorted({str(c["domain"]).lstrip(".") for c in chosen})
    return to_netscape(chosen).encode("utf-8"), len(chosen), names


def clear_cookies(domain: Optional[str] = None) -> int:
    """Delete cookies of one domain (and subdomains) or all; returns how many were removed."""
    ws = _browser_ws()
    cookies = get_cookies()
    victims = [c for c in cookies if not domain or domain_matches(str(c["domain"]), [domain.lower()])]
    if not domain:
        _cdp(ws, [("Storage.clearCookies", {})])
        return len(cookies)
    if not victims:
        return 0
    tabs = list_tabs()
    page_ws = _tab_ws(tabs[0]["id"]) if tabs else _tab_ws(new_tab()["id"])   # Network.* lives on page targets
    _cdp(page_ws, [("Network.deleteCookies", {"name": c["name"], "domain": c["domain"], "path": c.get("path", "/")})
                   for c in victims])
    return len(victims)


def summary() -> Dict[str, Any]:
    """Dashboard overview: never contains cookie values."""
    wanted = proxy_url()
    info: Dict[str, Any] = {"enabled": enabled(), "executable": bool(find_executable()),
                            "proxy": {"enabled": bool(wanted), "reachable": proxy_reachable(wanted) if wanted else False},
                            "running": False, "tabs": [], "cookies": {"count": 0, "domains": []},
                            "viewport": {"width": VIEWPORT[0], "height": VIEWPORT[1]}}
    if not info["enabled"] or not is_running():
        return info
    info["running"] = True
    try:
        info["tabs"] = list_tabs()
        per: Dict[str, int] = {}
        shared_map: Dict[str, bool] = {}
        total = 0
        for c in get_cookies():
            key = str(c["domain"]).lstrip(".").lower()
            per[key] = per.get(key, 0) + 1
            if key not in shared_map:
                shared_map[key] = domain_matches(key, [d for name in COOKIE_SERVICES for d in SERVICE_DOMAINS[name]])
            total += 1
        info["cookies"] = {"count": total,
                           "domains": [{"domain": d, "count": n, "shared": shared_map.get(d, False)} for d, n in sorted(per.items())][:300]}
    except BrowserError as exc:
        info["error"] = str(exc)
    return info
