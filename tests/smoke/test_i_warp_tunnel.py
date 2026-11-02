"""Offline tests: per-task WARP tunnels (HELPERS/warp_tunnel.py).

A fake `wireproxy` (tiny HTTP proxy reading the same config) stands in for the
real one: tunnels start lazily per task, are isolated between concurrent tasks,
stop with the task, keys never outlive it, and yt-dlp / requests / gallery-dl
are routed into the task tunnel while localhost stays direct.
Linux only (spawns an executable). Run: python test_i_warp_tunnel.py [repo_root]
"""
import http.server
import os
import socket
import stat
import sys
import tempfile
import threading
import time

REPO = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])
if os.name != "posix":
    print("skip (posix only)")
    sys.exit(0)
sys.path.insert(0, REPO)
WORK = tempfile.mkdtemp(prefix="warp_test_")
os.chdir(WORK)
PASSED = []


def check(name, cond, detail=""):
    if not cond:
        raise AssertionError(f"FAIL {name}: {detail}")
    PASSED.append(name)
    print(f"ok  {name}")


FAKE = os.path.join(WORK, "fake-wireproxy")
with open(FAKE, "w") as f:
    f.write(f"""#!{sys.executable}
import socket, sys, threading
conf = open(sys.argv[sys.argv.index("-c") + 1]).read()
bind = [l.split("=", 1)[1].strip() for l in conf.splitlines() if l.startswith("BindAddress")][0]
host, port = bind.rsplit(":", 1)
srv = socket.socket(); srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((host, int(port))); srv.listen(50)
def serve(c):
    data = c.recv(65536)
    body = ("proxied:" + port).encode()
    c.sendall(b"HTTP/1.1 200 OK\\r\\nContent-Length: " + str(len(body)).encode() + b"\\r\\nConnection: close\\r\\n\\r\\n" + body)
    c.close()
while True:
    c, _ = srv.accept()
    threading.Thread(target=serve, args=(c,), daemon=True).start()
""")
os.chmod(FAKE, 0o755)
profiles = os.path.join(WORK, "warp")
os.makedirs(profiles)
with open(os.path.join(profiles, "account-1.conf"), "w") as f:
    f.write("[Interface]\nPrivateKey = SECRETKEY=\nAddress = 172.16.0.2/32, 2606:4700:110:1::1/128\n"
            "DNS = 1.1.1.1\nMTU = 1280\n[Peer]\nPublicKey = PEERKEY=\nAllowedIPs = 0.0.0.0/0, ::/0\n"
            "Endpoint = engage.cloudflareclient.com:2408\n")

from CONFIG.config import Config  # noqa: E402
Config.WARP_PER_TASK = True
Config.WARP_WIREPROXY_BIN = FAKE
Config.WARP_PROFILES_DIR = profiles
Config.WARP_PROBE_URL = ""
Config.WARP_RUNTIME_DIR = os.path.join(WORK, "run")
Config.WARP_MAX_TUNNELS = 3
Config.WARP_SLOT_WAIT_SECONDS = 0.3

from HELPERS import warp_tunnel as wt  # noqa: E402

check("installed", wt.install_hooks() is True)
run_dir = os.path.abspath(Config.WARP_RUNTIME_DIR)
check("runtime_dir_private", stat.S_IMODE(os.stat(run_dir).st_mode) == 0o700)


def procs():
    return [t.proc.pid for t in wt._active.values() if t.alive()]


# lazy start: a task that makes no external request never starts a tunnel
with wt.task_scope("cache-hit") as s:
    pass
check("lazy_no_tunnel_without_request", s.tunnel is None and not wt._active)

# one task: one tunnel, stable URL, nested scope reuses, stopped on exit
with wt.task_scope("task-A") as a:
    u1 = wt.proxy_url()
    u2 = wt.proxy_url()
    with wt.task_scope("nested") as inner:
        u3 = wt.proxy_url()
    conf_path = a.tunnel._conf
    check("tunnel_started", a.tunnel is not None and a.tunnel.alive())
    check("stable_url_in_task", u1 == u2 == u3 and inner is a, (u1, u2, u3))
    mode = stat.S_IMODE(os.stat(conf_path).st_mode)
    check("key_file_0600", mode == 0o600, oct(mode))
    check("conf_uses_configured_endpoint", "Endpoint = 162.159.192.1:2408" in open(conf_path).read())
    pid_a = a.tunnel.proc.pid
    old_proc = a.tunnel.proc
    # rotation: same URL, new process (new WireGuard session = new egress)
    a.rotate()
    check("rotate_keeps_url_new_process", wt.proxy_url() == u1 and a.tunnel.proc.pid != pid_a)
    check("rotate_stops_old_process", old_proc.poll() is not None)
    live_proc = a.tunnel.proc
check("tunnel_stopped_with_task", live_proc.poll() is not None and not wt._active)
check("key_file_removed_with_task", not os.path.exists(conf_path))

# concurrent tasks get separate tunnels
urls, barrier = {}, threading.Barrier(3)


def task(n):
    with wt.task_scope(f"user-{n}"):
        urls[n] = wt.proxy_url()
        barrier.wait(5)


ths = [threading.Thread(target=task, args=(n,)) for n in range(3)]
[t.start() for t in ths]
[t.join(10) for t in ths]
check("concurrent_tasks_isolated", len(set(urls.values())) == 3, urls)
check("all_stopped_after_tasks", not wt._active)

# over the limit: extra task falls back to the shared tunnel instead of failing
hold, release = [], threading.Event()


def holder(n):
    with wt.task_scope(f"hold-{n}"):
        hold.append(wt.proxy_url())
        release.wait(5)


hs = [threading.Thread(target=holder, args=(n,)) for n in range(3)]
[t.start() for t in hs]
while len(hold) < 3:
    time.sleep(0.02)
with wt.task_scope("overflow"):
    over = wt.proxy_url()
shared = wt._shared.get("t")
check("overflow_uses_shared_tunnel", shared is not None and over == shared.url and over not in hold)
release.set()
[t.join(5) for t in hs]

# outside any task: shared tunnel, never direct
check("no_task_uses_shared", wt.proxy_url() == shared.url)

# yt-dlp hook
try:
    import yt_dlp
    with wt.task_scope("ytdlp") as y:
        ydl = yt_dlp.YoutubeDL({"quiet": True})
        explicit = yt_dlp.YoutubeDL({"quiet": True, "proxy": "http://user-proxy:3128"})
        v6 = yt_dlp.YoutubeDL({"quiet": True, "source_address": "::"})
        check("ytdlp_gets_task_proxy", ydl.params.get("proxy") == y.tunnel.url)
        check("ytdlp_explicit_proxy_wins", explicit.params.get("proxy") == "http://user-proxy:3128")
        check("ytdlp_force_ipv6_bind_dropped", "source_address" not in v6.params)
except ImportError:
    print("skip ytdlp hook (yt_dlp not installed)")

# requests hook: external host via the task tunnel, localhost direct
import requests  # noqa: E402


class Local(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"direct"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Local)
threading.Thread(target=srv.serve_forever, daemon=True).start()
with wt.task_scope("http") as h:
    r_ext = requests.get("http://example.invalid/thumb.jpg", timeout=5).text
    r_loc = requests.get(f"http://127.0.0.1:{srv.server_port}/", timeout=5).text
    port = h.tunnel.port
check("requests_external_via_task_tunnel", r_ext == f"proxied:{port}", r_ext)
check("requests_localhost_direct", r_loc == "direct", r_loc)
r_out = requests.get(f"http://127.0.0.1:{srv.server_port}/", timeout=5).text
check("requests_outside_task_untouched", r_out == "direct")
for host, direct in (("api.telegram.org", True), ("x.firebasedatabase.app", True), ("10.1.0.3", True),
                     ("www.youtube.com", False), ("i.ytimg.com", False), ("2a09:bac5::1", False)):
    check(f"direct_host_{host}", wt.is_direct_host(host) is direct)

# gallery-dl hook
try:
    from gallery_dl import config as gconfig
    with wt.task_scope("gdl") as g:
        check("gallery_dl_gets_task_proxy", gconfig.interpolate(("extractor",), "proxy") == g.tunnel.url)
    env = wt.subprocess_env({})
    check("subprocess_env_has_proxy", env.get("HTTPS_PROXY") == shared.url and "localhost" in env.get("NO_PROXY", ""))
except ImportError:
    print("skip gallery-dl hook (not installed)")

# orphan cleanup: a tunnel left by a crashed bot process is killed at startup
import subprocess  # noqa: E402
orphan_conf = os.path.join(run_dir, "t1.conf")
with open(orphan_conf, "w") as f:
    f.write(f"BindAddress = 127.0.0.1:{wt._free_port('127.0.0.1')}\n")
orphan = subprocess.Popen([FAKE, "-c", orphan_conf, "-s"])
time.sleep(0.5)
wt._kill_orphans()
orphan.wait(5)
check("orphan_killed", orphan.poll() is not None)

wt.shutdown()
check("shutdown_stops_shared", shared.proc is None)
Config.WARP_PER_TASK = False
check("disabled_no_proxy", wt.proxy_url() is None)
with wt.task_scope("off") as off:
    pass
check("disabled_scope_noop", off is None)
print("ALL", len(PASSED), "CHECKS PASSED")
