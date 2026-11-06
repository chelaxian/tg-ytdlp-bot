"""Live browser session shared by the admin dashboard and the bot.

An admin logs into any web service in a real (headless) Chromium that is
driven from the dashboard's "Browser" tab. The bot then reads the *current*
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

CDP_HOST = "127.0.0.1"
VIEWPORT = (1280, 800)
CONNECT_TIMEOUT = 3.0
CALL_TIMEOUT = 12.0

# Services the /cookie buttons ask for -> cookie domains that belong to them.
SERVICE_DOMAINS: Dict[str, Tuple[str, ...]] = {
    "twitter": ("x.com", "twitter.com", "t.co", "twimg.com"),
    "tiktok": ("tiktok.com", "tiktokv.com", "tiktokcdn.com"),
    "vk": ("vk.com", "vk.ru", "vkontakte.ru", "vk-cdn.net", "userapi.com"),
    "instagram": ("instagram.com", "cdninstagram.com"),
    "facebook": ("facebook.com", "fbcdn.net"),
    "youtube": ("youtube.com", "google.com", "googlevideo.com", "youtu.be"),
}

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


def find_executable() -> Optional[str]:
    configured = str(_cfg("BROWSER_EXECUTABLE", "") or "").strip()
    if configured:
        return configured if os.path.isfile(configured) else None
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


def start() -> Dict[str, Any]:
    """Launch Chromium (detached) unless it is already up."""
    if not enabled():
        raise BrowserError("disabled")
    if is_running():
        return {"started": False}
    exe = find_executable()
    if not exe:
        raise BrowserError("no_browser")
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(PROFILE_DIR, 0o700)
    except OSError:
        pass
    args = [
        exe, "--headless=new", f"--remote-debugging-port={cdp_port()}", f"--remote-debugging-address={CDP_HOST}",
        f"--user-data-dir={PROFILE_DIR}", f"--window-size={VIEWPORT[0]},{VIEWPORT[1]}",
        "--force-device-scale-factor=1", "--no-first-run", "--no-default-browser-check",
        "--disable-blink-features=AutomationControlled", "--disable-background-networking",
        "--disable-sync", "--disable-dev-shm-usage", "--password-store=basic", "--lang=en-US",
        "--mute-audio", "--disable-notifications",
    ]
    proxy = str(_cfg("BROWSER_PROXY", "") or "").strip()
    if proxy and re.fullmatch(r"(https?|socks5h?|socks4)://[A-Za-z0-9.\-:\[\]]+", proxy):
        args.append(f"--proxy-server={proxy}")
    ua = _user_agent_fix(exe)
    if ua:
        args.append(f"--user-agent={ua}")
    if hasattr(os, "geteuid") and os.geteuid() == 0:
        args.append("--no-sandbox")                      # Chromium refuses to run as root otherwise
    args.append("about:blank")
    kwargs: Dict[str, Any] = {"stdin": subprocess.DEVNULL, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
    if sys.platform == "win32":
        kwargs["creationflags"] = 0x00000008 | 0x00000200   # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    else:
        kwargs["start_new_session"] = True                  # survives dashboard / bot restarts
    try:
        proc = subprocess.Popen(args, **kwargs)
    except OSError as exc:
        raise BrowserError(f"launch_failed: {exc}") from exc
    try:
        PID_FILE.write_text(str(proc.pid))
    except OSError:
        pass
    deadline = time.monotonic() + 20
    while time.monotonic() < deadline:
        if is_running():
            return {"started": True, "pid": proc.pid}
        if proc.poll() is not None:
            raise BrowserError("launch_failed: exited early")
        time.sleep(0.3)
    raise BrowserError("launch_timeout")


def stop() -> bool:
    """Close the browser gracefully (profile and persistent cookies are flushed)."""
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
    return not is_running()


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
        if t.get("type") == "page" and t.get("id"):
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


def _coord(value: Any, upper: int) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise BrowserError("bad_input") from exc
    if not (0 <= number <= upper):
        raise BrowserError("bad_input")
    return number


def send_input(tab_id: str, kind: str, **p: Any) -> None:
    """kind: click | dblclick | scroll | text | key"""
    ws = _tab_ws(tab_id)
    calls: List[Tuple[str, Dict[str, Any]]] = []
    if kind in ("click", "dblclick"):
        x, y = _coord(p.get("x"), VIEWPORT[0]), _coord(p.get("y"), VIEWPORT[1])
        button = p.get("button") if p.get("button") in ("left", "right", "middle") else "left"
        base = {"x": x, "y": y, "button": button}
        calls.append(("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": x, "y": y}))
        for count in ((1, 2) if kind == "dblclick" else (1,)):
            calls.append(("Input.dispatchMouseEvent", {**base, "type": "mousePressed", "clickCount": count}))
            calls.append(("Input.dispatchMouseEvent", {**base, "type": "mouseReleased", "clickCount": count}))
    elif kind == "scroll":
        x, y = _coord(p.get("x"), VIEWPORT[0]), _coord(p.get("y"), VIEWPORT[1])
        dx = max(-5000.0, min(5000.0, float(p.get("dx") or 0)))
        dy = max(-5000.0, min(5000.0, float(p.get("dy") or 0)))
        calls.append(("Input.dispatchMouseEvent", {"type": "mouseWheel", "x": x, "y": y, "deltaX": dx, "deltaY": dy}))
    elif kind == "text":
        text = str(p.get("text") or "")[:5000]
        if not text:
            return
        if len(text) > 1 or not text.isprintable():
            calls.append(("Input.insertText", {"text": text}))       # paste-like, one shot
        else:
            calls.append(("Input.dispatchKeyEvent", {"type": "keyDown", "text": text, "unmodifiedText": text, "key": text}))
            calls.append(("Input.dispatchKeyEvent", {"type": "keyUp", "key": text}))
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
    _cdp(ws, calls)


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
    info: Dict[str, Any] = {"enabled": enabled(), "executable": bool(find_executable()),
                            "running": False, "tabs": [], "cookies": {"count": 0, "domains": []},
                            "viewport": {"width": VIEWPORT[0], "height": VIEWPORT[1]}}
    if not info["enabled"] or not is_running():
        return info
    info["running"] = True
    try:
        info["tabs"] = list_tabs()
        per: Dict[str, int] = {}
        total = 0
        for c in get_cookies():
            key = str(c["domain"]).lstrip(".").lower()
            per[key] = per.get(key, 0) + 1
            total += 1
        info["cookies"] = {"count": total,
                           "domains": [{"domain": d, "count": n} for d, n in sorted(per.items())][:300]}
    except BrowserError as exc:
        info["error"] = str(exc)
    return info
