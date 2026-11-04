"""Domain lists (CONFIG/domains.py) and NSFW word lists (TXT/*.txt) for the dashboard.

Writes are safe by construction:
* only the lists shown in the dashboard can be changed (whitelist);
* every item is validated (printable, no quotes/backslashes/newlines, length cap);
* the new block is generated with repr(), the whole file is checked with
  ast.parse() before it replaces the old one atomically, and a backup is kept.
"""

from __future__ import annotations

import ast
import ipaddress
import os
import re
import shutil
import socket
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urljoin, urlparse

from CONFIG.config import Config

BASE_DIR = Path(os.environ.get("TG_DASHBOARD_PROJECT_DIR", str(Path(__file__).resolve().parent.parent)))
DOMAINS_FILE = BASE_DIR / "CONFIG" / "domains.py"

EDITABLE_LISTS: Dict[str, str] = {
    # name: kind -> validator
    "WHITE_KEYWORDS": "keyword",
    "GALLERYDL_ONLY_DOMAINS": "domain",
    "GALLERYDL_ONLY_PATH": "path",
    "GALLERYDL_FALLBACK_DOMAINS": "domain",
    "YTDLP_ONLY_DOMAINS": "domain",
    "WHITELIST": "domain",
    "GREYLIST": "domain",
    "NO_COOKIE_DOMAINS": "domain",
    "PROXY_1_DOMAINS": "domain",
    "PROXY_2_DOMAINS": "domain",
    "NO_FILTER_DOMAINS": "domain",
    "TIKTOK_DOMAINS": "domain",
    "CLEAN_QUERY": "domain",
    "BLACK_LIST": "domain",
}

MAX_ITEMS = 20_000
MAX_ITEM_LEN = 200
_DOMAIN = re.compile(r"^[A-Za-z0-9*](?:[A-Za-z0-9*._-]{0,198}[A-Za-z0-9])?$")
_PATH = re.compile(r"^[A-Za-z0-9._~:/?#@!$&()*+,;=%\[\]-]{1,200}$")
_KEYWORD = re.compile(r"^[^\"'\\\x00-\x1f\x7f]{1,200}$")

DOWNLOAD_LIMIT = 20 * 1024 * 1024
MIN_LIST_LINES = 10


class ListError(ValueError):
    pass


# --------------------------------------------------------------------------------------
# Reading
# --------------------------------------------------------------------------------------

def get_file_line_count(file_path) -> int:
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            return sum(1 for line in f if line.strip())
    except OSError:
        return 0


def get_lists_stats() -> Dict[str, Any]:
    return {
        "porn_domains": get_file_line_count(BASE_DIR / Config.PORN_DOMAINS_FILE),
        "porn_keywords": get_file_line_count(BASE_DIR / Config.PORN_KEYWORDS_FILE),
        "supported_sites": get_file_line_count(BASE_DIR / Config.SUPPORTED_SITES_FILE),
    }


def _list_nodes(tree: ast.AST) -> Dict[str, ast.Assign]:
    """`NAME = [...]` assignments inside class DomainsConfig (or at module level)."""
    found: Dict[str, ast.Assign] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            if isinstance(node.value, (ast.List, ast.Tuple)) and node.targets[0].id in EDITABLE_LISTS:
                found.setdefault(node.targets[0].id, node)
    return found


def get_domain_lists() -> Dict[str, List[str]]:
    """Current lists, read from the file (not the imported module) so edits show at once."""
    source = DOMAINS_FILE.read_text(encoding="utf-8")
    nodes = _list_nodes(ast.parse(source))
    result: Dict[str, List[str]] = {}
    for name in EDITABLE_LISTS:
        node = nodes.get(name)
        if node is None:
            continue
        try:
            value = ast.literal_eval(node.value)
        except Exception:
            continue
        result[name] = [str(v) for v in value]
    return result


# --------------------------------------------------------------------------------------
# Writing
# --------------------------------------------------------------------------------------

def first_invalid_item(list_name: str, items: List[Any]) -> Optional[str]:
    """The first item the validator would reject (for the UI), without raising."""
    kind = EDITABLE_LISTS.get(list_name)
    if kind is None or not isinstance(items, list):
        return None
    pattern = {"domain": _DOMAIN, "path": _PATH, "keyword": _KEYWORD}[kind]
    for raw in items:
        if not isinstance(raw, str):
            return ""
        item = raw.strip().lower() if kind == "domain" else raw.strip()
        if item and (len(item) > MAX_ITEM_LEN or not pattern.match(item)):
            return item[:60]
    return None


def validate_items(list_name: str, items: List[Any]) -> List[str]:
    kind = EDITABLE_LISTS.get(list_name)
    if kind is None:
        raise ListError("unknown_list")
    if not isinstance(items, list) or len(items) > MAX_ITEMS:
        raise ListError("too_many_items")
    pattern = {"domain": _DOMAIN, "path": _PATH, "keyword": _KEYWORD}[kind]
    clean: List[str] = []
    seen = set()
    for raw in items:
        if not isinstance(raw, str):
            raise ListError("invalid_item")
        item = raw.strip()
        if kind == "domain":
            item = item.lower()
        if not item:
            continue
        if len(item) > MAX_ITEM_LEN or not pattern.match(item):
            raise ListError(f"invalid_item:{item[:60]}")
        if item not in seen:
            seen.add(item)
            clean.append(item)
    return clean


def _atomic_write_text(path: Path, text: str) -> None:
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        try:
            shutil.copymode(path, tmp)
        except OSError:
            pass
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def update_domain_list(list_name: str, items: List[Any]) -> List[str]:
    """Replace one list in CONFIG/domains.py. Returns the stored items; raises ListError."""
    clean = validate_items(list_name, items)
    raw = DOMAINS_FILE.read_bytes()
    newline = "\r\n" if b"\r\n" in raw else "\n"
    source = raw.decode("utf-8").replace("\r\n", "\n")
    node = _list_nodes(ast.parse(source)).get(list_name)
    if node is None:
        raise ListError("list_not_found")
    lines = source.split("\n")
    start, end = node.lineno - 1, node.end_lineno - 1
    indent = re.match(r"\s*", lines[start]).group(0)
    block = [f"{indent}{list_name} = ["] + [f"{indent}    {item!r}," for item in clean] + [f"{indent}]"]
    # keep anything after the closing bracket on its line (e.g. a comment)
    tail = lines[end][node.end_col_offset:]
    if tail.strip():
        block[-1] += tail
    new_source = "\n".join(lines[:start] + block + lines[end + 1:])
    check = _list_nodes(ast.parse(new_source)).get(list_name)  # raises SyntaxError if broken
    if check is None or ast.literal_eval(check.value) != clean:
        raise ListError("verify_failed")
    backup_dir = BASE_DIR / "CONFIG" / ".backups"
    backup_dir.mkdir(exist_ok=True)
    shutil.copy2(DOMAINS_FILE, backup_dir / f"domains.py.{int(time.time())}")
    _prune_backups(backup_dir, "domains.py.", keep=20)
    _atomic_write_text(DOMAINS_FILE, new_source.replace("\n", newline))
    return clean


def _prune_backups(folder: Path, prefix: str, keep: int) -> None:
    copies = sorted(folder.glob(prefix + "*"), key=lambda p: p.stat().st_mtime)
    for old in copies[:-keep]:
        try:
            old.unlink()
        except OSError:
            pass


# --------------------------------------------------------------------------------------
# NSFW lists from URLs (Docker mode, where script.sh is not available)
# --------------------------------------------------------------------------------------

def _bad_ip(ip: ipaddress._BaseAddress) -> bool:
    # ::ffff:127.0.0.1 and similar: judge the embedded IPv4 address, not the wrapper
    mapped = getattr(ip, "ipv4_mapped", None)
    if mapped is not None:
        ip = mapped
    return (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved
            or ip.is_multicast or ip.is_unspecified or not ip.is_global)


def _validate_url_for_ssrf(url: str) -> Tuple[bool, str]:
    if not url or len(url) > 2000:
        return False, "empty_or_long"
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return False, "scheme"
    host = parsed.hostname
    if not host:
        return False, "host"
    lowered = host.lower()
    if lowered in {"localhost", "0.0.0.0"} or "localhost" in lowered or lowered.endswith((".local", ".internal")):
        return False, "internal_host"
    try:
        if _bad_ip(ipaddress.ip_address(host)):
            return False, "internal_ip"
    except ValueError:
        pass
    try:
        infos = socket.getaddrinfo(host, parsed.port or (443 if parsed.scheme == "https" else 80))
    except socket.gaierror:
        return False, "dns"
    for *_, sockaddr in infos:
        try:
            if _bad_ip(ipaddress.ip_address(sockaddr[0].split("%")[0])):
                return False, "internal_ip"
        except ValueError:
            continue
    return True, ""


def _download_text(url: str, timeout: int = 30) -> str:
    """Fetch only public endpoints; pin DNS before connecting, including redirects.

    HTTP Host and TLS SNI still use the original hostname. No environment proxy,
    cookies or authorization are forwarded. Total time and body size are bounded.
    """
    import http.client
    import ssl
    current = url
    deadline = time.monotonic() + timeout
    for _ in range(6):
        parsed = urlparse(current)
        if (parsed.scheme not in ("http", "https") or not parsed.hostname
                or parsed.username is not None or parsed.password is not None
                or any(ord(c) < 33 for c in current)):
            raise ListError("url_rejected:invalid_url")
        host = parsed.hostname
        try:
            port = parsed.port or (443 if parsed.scheme == "https" else 80)
            addresses = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
        except (OSError, ValueError):
            raise ListError("url_rejected:dns") from None
        if not addresses or any(_bad_ip(ipaddress.ip_address(a[4][0].split("%")[0])) for a in addresses):
            raise ListError("url_rejected:internal_ip")
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise ListError("download_timeout")
        family, socktype, proto, _, sockaddr = addresses[0]
        sock = socket.socket(family, socktype, proto)
        conn = http.client.HTTPConnection(host, port, timeout=min(remaining, 10))
        try:
            sock.settimeout(min(remaining, 10))
            sock.connect(sockaddr)  # validated address, no second DNS resolution
            if parsed.scheme == "https":
                sock = ssl.create_default_context().wrap_socket(sock, server_hostname=host)
            conn.sock = sock
            path = parsed.path or "/"
            if parsed.query:
                path += "?" + parsed.query
            conn.request("GET", path, headers={"User-Agent": "tg-ytdlp-dashboard",
                                               "Accept-Encoding": "identity"})
            resp = conn.getresponse()
            if resp.status in (301, 302, 303, 307, 308) and resp.getheader("Location"):
                current = urljoin(current, resp.getheader("Location"))
                continue
            if resp.status != 200:
                raise ListError("download_http_error")
            chunks, size = [], 0
            while True:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise ListError("download_timeout")
                sock.settimeout(min(remaining, 10))
                chunk = resp.read1(64 * 1024)
                if not chunk:
                    break
                size += len(chunk)
                if size > DOWNLOAD_LIMIT:
                    raise ListError("too_large")
                chunks.append(chunk)
            return b"".join(chunks).decode("utf-8", errors="strict")
        finally:
            conn.close()
            sock.close()
    raise ListError("too_many_redirects")


def _check_list_text(text: str) -> str:
    head = text[:2000].lower()
    if "<html" in head or "<!doctype" in head:
        raise ListError("not_a_list")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) < MIN_LIST_LINES:
        raise ListError("too_few_lines")
    return "\n".join(lines) + "\n"


def update_lists_from_urls(porn_domains_url: str, porn_keywords_url: str, log=None) -> Dict[str, int]:
    """Download, validate and atomically replace the NSFW lists. Raises ListError."""
    targets = [(porn_domains_url, Config.PORN_DOMAINS_FILE), (porn_keywords_url, Config.PORN_KEYWORDS_FILE)]
    staged = []
    for url, rel in targets:
        if not url:
            continue
        if log:
            log(f"Downloading {urlparse(url).netloc}{urlparse(url).path}")
        staged.append((BASE_DIR / rel, _check_list_text(_download_text(url))))
    if not staged:
        raise ListError("no_urls")
    counts = {}
    for path, text in staged:
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            shutil.copy2(path, path.with_name(path.name + ".bak"))
        _atomic_write_text(path, text)
        counts[path.name] = text.count("\n")
        if log:
            log(f"{path.name}: {counts[path.name]} lines")
    return counts


def local_update_script() -> Optional[Path]:
    """script.sh next to the bot (systemd installs); None in Docker."""
    script = BASE_DIR / "script.sh"
    return script if script.exists() else None
