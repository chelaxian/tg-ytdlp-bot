"""Per-task Cloudflare WARP tunnels (WARP_PER_TASK = True).

The bot itself (Telegram, Firebase, localhost services) uses the server's
direct internet connection. Every user task (one handler run: a link, a
quality click, /img, /link, /list, /cookie ...) that reaches an external site
gets its own WARP tunnel: a private wireproxy process (userspace WireGuard, no
routes, no interfaces) exposing an HTTP proxy on a local port. Each new
WireGuard session gets a new Cloudflare egress IPv6, the tunnel is shared by
nothing else, and it is shut down when the task ends — so a banned egress or a
dropped tunnel never affects Telegram or other users' downloads.

Hooks (install_hooks) route traffic into the current task's tunnel without
touching every call site:
  * every yt_dlp.YoutubeDL created without an explicit proxy;
  * gallery-dl library mode (config key "proxy");
  * requests made inside a task to external hosts (localhost, private
    networks, Telegram, Firebase/Google APIs stay direct).
An explicitly chosen proxy (/proxy, PROXY_* domain lists) always wins.

Tunnels start lazily on the first external request of a task, so tasks served
from the cache never start one. Calls outside any task (rare background paths)
use one shared fallback tunnel, never the server IP.
"""
from __future__ import annotations

import atexit
import concurrent.futures
import contextlib
import ipaddress
import os
import signal
import socket
import subprocess
import threading
import time
import urllib.request
from typing import Dict, Optional
from urllib.parse import urlsplit

from HELPERS.logger import logger

_DEFAULTS = {
    "WARP_PER_TASK": False,
    "WARP_WIREPROXY_BIN": "/usr/local/bin/wireproxy",
    "WARP_PROFILES_DIR": "CONFIG/warp",
    "WARP_ENDPOINT": "162.159.192.1:2408",
    "WARP_DNS": "1.1.1.1, 2606:4700:4700::1111",
    "WARP_PROXY_HOST": "127.0.0.1",
    "WARP_MAX_TUNNELS": 40,
    "WARP_SLOT_WAIT_SECONDS": 30,
    "WARP_STARTUP_TIMEOUT": 10,
    "WARP_PROBE_URL": "https://www.cloudflare.com/cdn-cgi/trace",
    "WARP_RUNTIME_DIR": ".warp-run",
    "WARP_DIRECT_HOSTS": (),
}
_DIRECT_SUFFIXES = (
    "localhost", "telegram.org", "t.me", "telegram.me", "firebaseio.com",
    "firebasedatabase.app", "googleapis.com", "cloudflareclient.com",
)


def _cfg(name):
    try:
        from CONFIG.config import Config
        return getattr(Config, name, _DEFAULTS[name])
    except Exception:
        return _DEFAULTS[name]


def enabled() -> bool:
    return bool(_cfg("WARP_PER_TASK"))


# --------------------------------------------------------------------- process spawning
# PR_SET_PDEATHSIG is tied to the thread that forks; spawning from one
# long-lived thread makes every tunnel die with the bot (even on SIGKILL) and
# never with a short-lived worker thread.
_spawner = concurrent.futures.ThreadPoolExecutor(max_workers=1, thread_name_prefix="warp-spawn")


def _pdeathsig():  # runs in the child before exec
    try:
        import ctypes
        ctypes.CDLL("libc.so.6", use_errno=True).prctl(1, signal.SIGTERM)  # PR_SET_PDEATHSIG
    except Exception:
        pass


def _spawn(argv, log_path):
    def run():
        log = open(log_path, "ab")
        try:
            return subprocess.Popen(
                argv, stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
                preexec_fn=_pdeathsig if os.name == "posix" else None, close_fds=True,
            )
        finally:
            log.close()
    return _spawner.submit(run).result(timeout=15)


def _runtime_dir() -> str:
    path = os.path.abspath(str(_cfg("WARP_RUNTIME_DIR")))
    os.makedirs(path, mode=0o700, exist_ok=True)
    try:
        os.chmod(path, 0o700)
    except OSError:
        pass
    return path


def _free_port(host: str) -> int:
    family = socket.AF_INET6 if ":" in host else socket.AF_INET
    with socket.socket(family, socket.SOCK_STREAM) as s:
        s.bind((host, 0))
        return s.getsockname()[1]


# --------------------------------------------------------------------- profiles
def _read_profile(path: str) -> Dict[str, Dict[str, str]]:
    """Parse a wgcf-profile.conf (INI-like, keys may repeat-free)."""
    sections: Dict[str, Dict[str, str]] = {}
    current = None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("[") and line.endswith("]"):
                current = sections.setdefault(line[1:-1].strip().lower(), {})
            elif "=" in line and current is not None:
                k, v = line.split("=", 1)
                current[k.strip().lower()] = v.strip()
    for need in (("interface", "privatekey"), ("interface", "address"), ("peer", "publickey")):
        if need[1] not in sections.get(need[0], {}):
            raise ValueError(f"{path}: missing {need[0]}.{need[1]}")
    return sections


_profiles_cache = {"mtime": None, "list": []}
_profile_rr = [0]
_profile_lock = threading.Lock()


def _next_profile() -> Dict[str, Dict[str, str]]:
    folder = os.path.abspath(str(_cfg("WARP_PROFILES_DIR")))
    with _profile_lock:
        try:
            files = sorted(os.path.join(folder, n) for n in os.listdir(folder) if n.endswith(".conf"))
        except FileNotFoundError:
            files = []
        stamp = tuple((p, os.path.getmtime(p)) for p in files)
        if stamp != _profiles_cache["mtime"]:
            parsed = []
            for p in files:
                try:
                    parsed.append(_read_profile(p))
                except Exception as e:
                    logger.error(f"[WARP] bad profile {p}: {e}")
            _profiles_cache.update(mtime=stamp, list=parsed)
        profiles = _profiles_cache["list"]
        if not profiles:
            raise RuntimeError(f"no WARP profiles (*.conf) in {folder}; see docs/WARP_PER_TASK.md")
        profile = profiles[_profile_rr[0] % len(profiles)]
        _profile_rr[0] += 1
        return profile


# --------------------------------------------------------------------- tunnel
class Tunnel:
    """One wireproxy process = one WireGuard session = one egress IP."""

    def __init__(self, label: str):
        self.label = label
        self.host = str(_cfg("WARP_PROXY_HOST"))
        self.port = _free_port(self.host)
        self.proc: Optional[subprocess.Popen] = None
        self.egress: Optional[str] = None
        self.started_at = 0.0
        self.startup_ms = 0.0
        name = f"t{self.port}"
        self._conf = os.path.join(_runtime_dir(), f"{name}.conf")
        self._log = os.path.join(_runtime_dir(), f"{name}.log")

    @property
    def url(self) -> str:
        host = f"[{self.host}]" if ":" in self.host else self.host
        return f"http://{host}:{self.port}"

    def _write_conf(self) -> None:
        p = _next_profile()
        i, peer = p["interface"], p["peer"]
        lines = [
            "[Interface]",
            f"PrivateKey = {i['privatekey']}",
            f"Address = {i['address']}",
            f"DNS = {_cfg('WARP_DNS')}",
            f"MTU = {i.get('mtu', '1280')}",
            "",
            "[Peer]",
            f"PublicKey = {peer['publickey']}",
            f"Endpoint = {_cfg('WARP_ENDPOINT') or peer.get('endpoint')}",
            "",
            "[http]",
            f"BindAddress = {self.host}:{self.port}" if ":" not in self.host else f"BindAddress = [{self.host}]:{self.port}",
            "",
        ]
        fd = os.open(self._conf, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w") as f:
            f.write("\n".join(lines))

    def start(self) -> "Tunnel":
        self._write_conf()
        t0 = time.monotonic()
        self.proc = _spawn([str(_cfg("WARP_WIREPROXY_BIN")), "-c", self._conf, "-s"], self._log)
        deadline = t0 + float(_cfg("WARP_STARTUP_TIMEOUT"))
        last_err = None
        while time.monotonic() < deadline:
            if self.proc.poll() is not None:
                raise RuntimeError(f"wireproxy exited with {self.proc.returncode}: {self._tail_log()}")
            try:
                self.egress = self._probe()
                self.started_at = time.monotonic()
                self.startup_ms = (self.started_at - t0) * 1000
                return self
            except Exception as e:
                last_err = e
                time.sleep(0.1)
        self.stop()
        raise RuntimeError(f"WARP tunnel not ready in {_cfg('WARP_STARTUP_TIMEOUT')}s: {last_err}")

    def _probe(self) -> Optional[str]:
        probe = _cfg("WARP_PROBE_URL")
        if not probe:
            with socket.create_connection((self.host, self.port), timeout=1):
                return None
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({"http": self.url, "https": self.url}))
        with opener.open(probe, timeout=3) as r:
            body = r.read(4096).decode("utf-8", "replace")
        for line in body.splitlines():
            if line.startswith("ip="):
                return line[3:].strip()
        return None

    def _tail_log(self) -> str:
        try:
            with open(self._log, "rb") as f:
                return f.read()[-400:].decode("utf-8", "replace").strip()
        except OSError:
            return ""

    def alive(self) -> bool:
        return self.proc is not None and self.proc.poll() is None

    def stop(self) -> None:
        proc, self.proc = self.proc, None
        if proc is not None and proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=3)
        for path in (self._conf, self._log):
            try:
                os.unlink(path)
            except OSError:
                pass

    def restart(self) -> "Tunnel":
        """New WireGuard session (= new egress IP) on the same proxy port."""
        self.stop()
        return self.start()


# --------------------------------------------------------------------- task scopes
_active: Dict[int, Tunnel] = {}
_active_lock = threading.Lock()
_slots: Optional[threading.BoundedSemaphore] = None
_local = threading.local()
_shared: Dict[str, Tunnel] = {}
_shared_lock = threading.Lock()


def _slot_sem() -> threading.BoundedSemaphore:
    global _slots
    if _slots is None:
        with _active_lock:
            if _slots is None:
                _slots = threading.BoundedSemaphore(int(_cfg("WARP_MAX_TUNNELS")))
    return _slots


class TaskScope:
    def __init__(self, label: str):
        self.label = label
        self.tunnel: Optional[Tunnel] = None
        self._has_slot = False
        self._lock = threading.Lock()
        self.opened = time.monotonic()

    def proxy_url(self) -> Optional[str]:
        with self._lock:
            if self.tunnel is not None and self.tunnel.alive():
                return self.tunnel.url
            if self.tunnel is not None:  # died: same port, new session
                try:
                    return self.tunnel.restart().url
                except Exception as e:
                    logger.error(f"[WARP] restart for {self.label} failed: {e}")
                    self._release()
            if not self._has_slot:
                self._has_slot = _slot_sem().acquire(timeout=float(_cfg("WARP_SLOT_WAIT_SECONDS")))
                if not self._has_slot:
                    logger.warning(f"[WARP] all {_cfg('WARP_MAX_TUNNELS')} tunnels busy; {self.label} uses the shared tunnel")
                    return _shared_proxy_url()
            for attempt in (1, 2):
                try:
                    tunnel = Tunnel(self.label).start()
                    with _active_lock:
                        _active[id(tunnel)] = tunnel
                        active = len(_active)
                    self.tunnel = tunnel
                    logger.info(f"[WARP] tunnel up for {self.label} in {tunnel.startup_ms:.0f} ms, "
                                f"egress={tunnel.egress or '?'} (active={active})")
                    return tunnel.url
                except Exception as e:
                    logger.error(f"[WARP] tunnel for {self.label} failed (attempt {attempt}/2): {e}")
            self._release()
            return _shared_proxy_url()

    def rotate(self) -> Optional[str]:
        """Give this task a new egress IP (same proxy URL); other tasks are untouched."""
        with self._lock:
            if self.tunnel is None or not self.tunnel.alive():
                return None
            old = self.tunnel.egress
            try:
                self.tunnel.restart()
                logger.info(f"[WARP] rotated {self.label}: {old} -> {self.tunnel.egress}")
                return self.tunnel.egress
            except Exception as e:
                logger.error(f"[WARP] rotate for {self.label} failed: {e}")
                return None

    def _release(self) -> None:
        if self.tunnel is not None:
            with _active_lock:
                _active.pop(id(self.tunnel), None)
            self.tunnel.stop()
            self.tunnel = None
        if self._has_slot:
            self._has_slot = False
            _slot_sem().release()

    def close(self) -> None:
        with self._lock:
            had = self.tunnel
            egress = had.egress if had else None
            self._release()
        if had is not None:
            logger.info(f"[WARP] tunnel down for {self.label} after {time.monotonic() - self.opened:.0f}s "
                        f"(egress={egress or '?'}, active={len(_active)})")


@contextlib.contextmanager
def task_scope(label: str):
    """Everything the current thread does inside gets one private WARP tunnel
    (started on first use, stopped on exit). Nested scopes reuse the outer one."""
    if not enabled() or getattr(_local, "scope", None) is not None:
        yield getattr(_local, "scope", None)
        return
    scope = TaskScope(label)
    _local.scope = scope
    try:
        yield scope
    finally:
        _local.scope = None
        scope.close()


def current_scope() -> Optional[TaskScope]:
    return getattr(_local, "scope", None)


def bind_scope(fn):
    """Run fn in another thread under the caller's task tunnel (without owning it)."""
    scope = current_scope()

    def run(*a, **k):
        if scope is None or current_scope() is not None:
            return fn(*a, **k)
        _local.scope = scope
        try:
            return fn(*a, **k)
        finally:
            _local.scope = None

    return run


def _shared_proxy_url() -> Optional[str]:
    with _shared_lock:
        tunnel = _shared.get("t")
        if tunnel is not None and tunnel.alive():
            return tunnel.url
        try:
            if tunnel is not None:
                tunnel.restart()
            else:
                tunnel = Tunnel("shared").start()
                _shared["t"] = tunnel
            logger.info(f"[WARP] shared tunnel up, egress={tunnel.egress or '?'}")
            return tunnel.url
        except Exception as e:
            logger.error(f"[WARP] shared tunnel failed: {e}; request goes direct")
            return None


def proxy_url() -> Optional[str]:
    """WARP proxy for an external request made now (task tunnel, else shared)."""
    if not enabled():
        return None
    scope = current_scope()
    return scope.proxy_url() if scope is not None else _shared_proxy_url()


def rotate_current_task() -> Optional[str]:
    scope = current_scope()
    return scope.rotate() if scope is not None else None


def active_count() -> int:
    return len(_active)


def is_direct_host(host: str) -> bool:
    """Hosts that never go through WARP: loopback/private, Telegram, Firebase."""
    host = (host or "").strip("[]").lower().rstrip(".")
    if not host:
        return True
    try:
        ip = ipaddress.ip_address(host)
        return ip.is_loopback or ip.is_private or ip.is_link_local
    except ValueError:
        pass
    extra = tuple(h.lower() for h in (_cfg("WARP_DIRECT_HOSTS") or ()))
    return any(host == s or host.endswith("." + s) for s in _DIRECT_SUFFIXES + extra)


# --------------------------------------------------------------------- hooks
def _patch_ytdlp() -> None:
    import yt_dlp
    cls = yt_dlp.YoutubeDL
    if getattr(cls.__init__, "_warp_hook", False):
        return
    original = cls.__init__

    def __init__(self, params=None, *args, **kwargs):
        if enabled():
            params = dict(params or {})
            if not params.get("proxy"):
                url = proxy_url()
                if url:
                    params["proxy"] = url
                    # "::" (force IPv6) can't reach an IPv4 local proxy; the
                    # tunnel already prefers IPv6 egress on its own
                    if params.get("source_address") == "::":
                        params.pop("source_address")
        return original(self, params, *args, **kwargs)

    __init__._warp_hook = True
    __init__.__wrapped__ = original
    cls.__init__ = __init__


def _patch_gallery_dl() -> None:
    try:
        from gallery_dl import config as gconfig
    except ImportError:
        return
    if getattr(gconfig.interpolate, "_warp_hook", False):
        return
    original = gconfig.interpolate

    def interpolate(path, key, *args, **kwargs):
        value = original(path, key, *args, **kwargs)
        if key == "proxy" and not value and enabled():
            return proxy_url() or value
        return value

    interpolate._warp_hook = True
    gconfig.interpolate = interpolate


def _patch_requests() -> None:
    import requests
    cls = requests.Session
    if getattr(cls.request, "_warp_hook", False):
        return
    original = cls.request

    def request(self, method, url, *args, **kwargs):
        # only inside a user task, only for external hosts, never over an
        # explicitly chosen proxy
        if enabled() and current_scope() is not None and not kwargs.get("proxies") and not self.proxies:
            try:
                host = urlsplit(str(url)).hostname or ""
            except ValueError:
                host = ""
            if not is_direct_host(host):
                proxy = proxy_url()
                if proxy:
                    kwargs["proxies"] = {"http": proxy, "https": proxy}
        return original(self, method, url, *args, **kwargs)

    request._warp_hook = True
    cls.request = request


def subprocess_env(base=None) -> dict:
    """Environment for a child process (gallery-dl CLI) that should use WARP."""
    env = dict(os.environ if base is None else base)
    url = proxy_url()
    if url:
        env.update(HTTP_PROXY=url, HTTPS_PROXY=url, http_proxy=url, https_proxy=url,
                   NO_PROXY="localhost,127.0.0.1,::1", no_proxy="localhost,127.0.0.1,::1")
    return env


def _kill_orphans() -> None:
    """wireproxy left from a previous bot process (crash) still holds keys/ports."""
    marker = _runtime_dir()
    for pid in os.listdir("/proc") if os.path.isdir("/proc") else ():
        if not pid.isdigit() or int(pid) == os.getpid():
            continue
        try:
            with open(f"/proc/{pid}/cmdline", "rb") as f:
                cmd = f.read().decode("utf-8", "replace")
        except OSError:
            continue
        if "wireproxy" in cmd and marker in cmd:
            try:
                os.kill(int(pid), signal.SIGTERM)
                logger.info(f"[WARP] killed orphan tunnel pid {pid}")
            except OSError:
                pass
    for name in os.listdir(marker):
        if name.endswith((".conf", ".log")):
            try:
                os.unlink(os.path.join(marker, name))
            except OSError:
                pass


def shutdown() -> None:
    with _active_lock:
        tunnels = list(_active.values())
        _active.clear()
    tunnels += list(_shared.values())
    _shared.clear()
    for t in tunnels:
        try:
            t.stop()
        except Exception:
            pass


_installed = [False]


def install_hooks() -> bool:
    """Called once at startup. No-op unless WARP_PER_TASK is on."""
    if _installed[0] or not enabled():
        return False
    binary = str(_cfg("WARP_WIREPROXY_BIN"))
    if not os.path.isfile(binary) or not os.access(binary, os.X_OK):
        logger.error(f"[WARP] WARP_PER_TASK is on but {binary} is missing; tasks will go direct")
    _kill_orphans()
    _patch_ytdlp()
    _patch_gallery_dl()
    _patch_requests()
    atexit.register(shutdown)
    _installed[0] = True
    logger.info(f"[WARP] per-task tunnels enabled (max {_cfg('WARP_MAX_TUNNELS')}, "
                f"proxy host {_cfg('WARP_PROXY_HOST')}, endpoint {_cfg('WARP_ENDPOINT')})")
    return True
