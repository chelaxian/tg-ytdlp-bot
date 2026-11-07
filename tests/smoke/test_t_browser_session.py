"""Smoke test: live browser session (HELPERS/browser_session + dashboard /api/browser/*).

Run: python tests/smoke/test_t_browser_session.py
Offline checks always run; the live part needs a Chromium/Chrome binary and is skipped without one.
"""
import os
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
TMPDIR = Path(tempfile.mkdtemp(prefix="br_test_"))
os.environ["TG_DASHBOARD_PROJECT_DIR"] = str(TMPDIR)
os.environ["TG_BROWSER_KEEPER"] = "0"          # no background upkeep thread in tests
(TMPDIR / "CONFIG").mkdir()

from dashboard_fixture import DEMO_PASSWORD, DEMO_USER, install_stubs  # noqa: E402

app, _collector = install_stubs()
from fastapi.testclient import TestClient  # noqa: E402

from HELPERS import browser_session as bs  # noqa: E402
from HELPERS.cookie_file import validate_cookie_bytes  # noqa: E402

ok = fail = 0


def check(name, cond, info=""):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name} {info}")


def blocked(url):
    try:
        bs.normalize_url(url)
        return False
    except bs.BrowserError:
        return True


# ---- URL policy
check("plain host gets https", bs.normalize_url("x.com/home") == "https://x.com/home")
check("http kept", bs.normalize_url("http://example.com") == "http://example.com")
check("host:port ok", bs.normalize_url("example.com:8443/a") == "https://example.com:8443/a")
for bad in ("javascript:alert(1)", "data:text/html,x", "file:///etc/passwd", "about:blank", "chrome://settings",
            "http://127.0.0.1:5555", "http://localhost", "localhost:3000", "http://10.1.2.3", "http://192.168.0.1",
            "http://169.254.169.254/latest", "http://[::1]/", "http://2130706433/", "http://0x7f.1/", "http://foo.internal",
            "http://a b.com", "", "http://x.localhost"):
    check(f"blocked: {bad!r}", blocked(bad))
check("public IP allowed", not blocked("http://1.1.1.1/"))

# ---- Netscape output is accepted by the bot's own validator
cookies = [
    {"name": "auth_token", "value": "abc", "domain": ".x.com", "path": "/", "secure": True, "httpOnly": True, "expires": 2000000000},
    {"name": "sid", "value": "s", "domain": "www.tiktok.com", "path": "/", "secure": False, "httpOnly": False, "expires": -1},
    {"name": "c_user", "value": "1", "domain": ".facebook.com", "path": "/", "secure": True, "httpOnly": False, "expires": 0},
    {"name": "evil\tname", "value": "va\nlue", "domain": ".vk.com", "path": "/", "expires": 2000000000},
]
text = bs.to_netscape(cookies)
good, reason = validate_cookie_bytes(text.encode(), require_entries=True)
check("netscape passes validate_cookie_bytes", good, reason)
check("httpOnly prefix", "#HttpOnly_.x.com\tTRUE\t/\tTRUE\t2000000000\tauth_token\tabc" in text)
check("host-only cookie flag FALSE", "www.tiktok.com\tFALSE\t/\tFALSE\t" in text)
body = [ln for ln in text.splitlines() if "\t" in ln]
check("session cookie gets a future expiry", all(int(ln.split("\t")[4]) > time.time() for ln in body))
check("tabs/newlines stripped from fields", "evilname" in text and "value" in text and "va\nlue" not in text)
tw = bs.filter_cookies(cookies, services=["twitter"])
check("service filter twitter", [c["name"] for c in tw] == ["auth_token"])
check("service filter keeps subdomains", [c["name"] for c in bs.filter_cookies(cookies, services=["tiktok"])] == ["sid"])
check("no false suffix match", not bs.domain_matches("notx.com", ["x.com"]) and bs.domain_matches(".api.x.com", ["x.com"]))
check("no filter = everything", len(bs.filter_cookies(cookies)) == 4)

# ---- dashboard API (browser not running)
BASE = "http://testserver"
SAME = {"Origin": BASE}
c = TestClient(app, base_url=BASE)
check("browser api needs auth", c.get("/api/browser").status_code == 401)
bs.PROFILE_DIR = TMPDIR / "CONFIG" / ".browser_profile"
bs.PID_FILE = TMPDIR / "CONFIG" / ".browser_session.pid"
bs.cdp_port = lambda: 9331
c.post("/api/login", json={"username": DEMO_USER, "password": DEMO_PASSWORD}, headers=SAME)
csrf = c.get("/api/session").json()["csrf"]
H = {**SAME, "X-CSRF-Token": csrf}
d = c.get("/api/browser").json()
check("summary when stopped", d["running"] is False and d["tabs"] == [] and d["cookies"]["count"] == 0)
check("input without browser -> 409", c.post("/api/browser/input", json={"id": "A" * 12, "kind": "key", "key": "Enter"}, headers=H).status_code == 409)
check("bad tab id rejected", c.post("/api/browser/tab/close", json={"id": "../etc/passwd"}, headers=H).status_code == 422)
check("post needs csrf", c.post("/api/browser/start", json={}, headers=SAME).status_code == 403)
check("blocked url refused", c.post("/api/browser/navigate", json={"id": "A" * 12, "url": "http://127.0.0.1"}, headers=H).status_code in (400, 409))

# the read-only preview blocks everything except the browser tab
import web.dashboard_app as dash  # noqa: E402
dash.PREVIEW_READ_ONLY = True
check("read-only: browser start still allowed (409 = reached the handler or started)",
      c.post("/api/browser/tab", json={"url": "about:blank"}, headers=H).status_code in (200, 409))
check("read-only: settings stay blocked", c.post("/api/settings", json={"PROXY_PORT": 1}, headers=H).status_code == 403)
check("read-only: jobs stay blocked", c.post("/api/jobs/restart-bot", json={"mode": "now"}, headers=H).status_code == 403)
dash.PREVIEW_READ_ONLY = False

# ---- websocket stream: auth first
from starlette.websockets import WebSocketDisconnect  # noqa: E402

try:
    with TestClient(app, base_url=BASE) as anon:
        with anon.websocket_connect("/api/browser/ws", headers={"origin": BASE}):
            pass
    check("websocket without a session is refused", False)
except WebSocketDisconnect as exc:
    check("websocket without a session is refused", exc.code == 4403)
try:
    with c.websocket_connect("/api/browser/ws", headers={"origin": "https://evil.example"}):
        pass
    check("websocket from another origin is refused", False)
except WebSocketDisconnect as exc:
    check("websocket from another origin is refused", exc.code == 4403)
try:
    with c.websocket_connect("/api/browser/ws", headers={"origin": BASE}) as sock:
        sock.send_json({"op": "hello", "csrf": "wrong"})
        sock.receive_json()
    check("websocket with a wrong CSRF token is refused", False)
except WebSocketDisconnect as exc:
    check("websocket with a wrong CSRF token is refused", exc.code == 4403)

# ---- egress: the browser is independent, it leaves from the server (no tunnel to the admin's PC)
import socket as _socket  # noqa: E402

check("no proxy by default", bs.proxy_url() == "" and d["proxy"]["enabled"] is False)
check("no PC tunnel switch in the panel", c.post("/api/browser/proxy", json={"enabled": True}, headers=H).status_code in (404, 405))
check("no PC tunnel leftovers", not hasattr(bs, "PC_PROXY_URL") and not hasattr(bs, "set_proxy_enabled"))
check("no listener -> not reachable", bs.proxy_reachable("socks5://127.0.0.1:1", max_age=0) is False)
listener = _socket.socket()
listener.bind(("127.0.0.1", 0))
listener.listen(1)
live_url = f"socks5://127.0.0.1:{listener.getsockname()[1]}"
check("listener -> reachable", bs.proxy_reachable(live_url, max_age=0) is True)
listener.close()
check("closed listener -> not reachable", bs.proxy_reachable(live_url, max_age=0) is False)
_orig_cfg = bs._cfg
bs._cfg = lambda name, default: "file:///etc/passwd" if name == "BROWSER_PROXY" else _orig_cfg(name, default)
check("bad proxy values are ignored", bs.proxy_url() == "")
bs._cfg = lambda name, default: "socks5://127.0.0.1:1080" if name == "BROWSER_PROXY" else _orig_cfg(name, default)
check("server-side BROWSER_PROXY is used", bs.proxy_url() == "socks5://127.0.0.1:1080")
bs._cfg = _orig_cfg
# time zone of the browser follows its exit address (configurable, validated)
bs._cfg = lambda name, default: "Europe/Berlin" if name == "BROWSER_TIMEZONE" else _orig_cfg(name, default)
check("BROWSER_TIMEZONE is used", bs.browser_timezone() == "Europe/Berlin")
bs._cfg = lambda name, default: "../../etc/passwd" if name == "BROWSER_TIMEZONE" else _orig_cfg(name, default)
check("bad BROWSER_TIMEZONE is ignored", bs.browser_timezone() == "")
bs._cfg = lambda name, default: True if name == "BROWSER_HEADLESS" else _orig_cfg(name, default)
check("BROWSER_HEADLESS=True: no virtual screen", bs._xvfb_binary() is None)
bs._cfg = _orig_cfg
check("no virtual screen -> not windowed", bs.is_windowed() is False)

# survives a restart of the dashboard service: own systemd scope, privileges dropped with setpriv
_env = dict(os.environ)
os.environ.pop("INVOCATION_ID", None)
kw = {"user": 1000, "group": 1000, "extra_groups": []}
check("not under systemd: command unchanged", bs._outside_service(["chrome"], dict(kw), "x") == ["chrome"])
if sys.platform.startswith("linux") and hasattr(os, "geteuid") and os.geteuid() == 0 and os.path.isdir("/run/systemd/system"):
    os.environ["INVOCATION_ID"] = "test"
    kw2 = dict(kw)
    cmd = bs._outside_service(["chrome", "--a"], kw2, "tg-ytdlp-browser")
    check("under systemd: own scope", cmd[1:3] == ["--scope", "--quiet"] and cmd[-2:] == ["chrome", "--a"], cmd)
    check("under systemd: privileges dropped after the scope", "user" not in kw2 and any("--reuid=1000" in c for c in cmd), cmd)
os.environ.clear(); os.environ.update(_env)
# saved tabs: only public http(s) addresses come back
bs.save_tabs(["https://x.com/robots.txt", "about:blank", "chrome://settings", "http://127.0.0.1:5555/"])
check("saved tabs keep public pages only", bs.saved_tabs() == ["https://x.com/robots.txt"], bs.saved_tabs())
bs.TABS_FILE.write_text('["file:///etc/passwd", "https://vk.ru/robots.txt"]')
check("tampered tab file is filtered", bs.saved_tabs() == ["https://vk.ru/robots.txt"], bs.saved_tabs())
check("nothing listening -> not alive", bs.is_alive() is False)
import HELPERS.browser_hub as _bh  # noqa: E402
check("keep-alive goes to the service start page",
      _bh._home_of("https://www.youtube.com/robots.txt") == "https://www.youtube.com/"
      and _bh._home_of("https://vk.ru/robots.txt") == "https://vk.ru/feed" and _bh._home_of("https://example.com/") is None)

exe = bs.find_executable()
if not exe:
    print("SKIP live browser tests: no Chromium/Chrome found")
else:
    try:
        r = c.post("/api/browser/start", json={}, headers=H)
        check("start", r.status_code == 200 and r.json()["ok"], r.text)
        d = c.get("/api/browser").json()
        check("running with one tab", d["running"] and len(d["tabs"]) >= 1, d)
        tab = d["tabs"][0]["id"]
        shot = c.get(f"/api/browser/screen?id={tab}")
        check("screenshot is a jpeg", shot.status_code == 200 and shot.content[:3] == b"\xff\xd8\xff"
              and shot.headers["content-type"] == "image/jpeg")
        # websocket: pushed frames, input and zoom over one connection
        import struct as _struct
        with c.websocket_connect("/api/browser/ws", headers={"origin": BASE}) as sock:
            sock.send_json({"op": "hello", "csrf": csrf})
            sock.send_json({"op": "watch", "id": tab, "profile": "fast", "gen": 7})
            frame = sock.receive_bytes()
            gen, vw, vh, seq = _struct.unpack(">HHHI", frame[:10])
            check("ws: first frame is a jpeg with the view number", frame[10:13] == b"\xff\xd8\xff" and gen == 7 and (vw, vh) == (1280, 800), (gen, vw, vh))
            sock.send_json({"op": "zoom", "id": tab, "zoom": 0.5, "gen": 8})
            answer = sock.receive_json()
            check("ws: zoom answered", answer.get("op") == "zoom" and answer.get("zoom") == 0.5, answer)
            for _ in range(20):
                frame = sock.receive_bytes()
                gen, vw, vh, seq = _struct.unpack(">HHHI", frame[:10])
                if gen == 8:
                    break
            check("ws: frames of the new zoom carry the new view number and size", gen == 8 and (vw, vh) == (2560, 1600), (gen, vw, vh))
            sock.send_json({"op": "zoom", "id": tab, "zoom": 1.0, "gen": 9})
            sock.send_json({"op": "input", "id": tab, "kind": "key", "key": "Nope"})
            err = None
            for _ in range(10):
                m = sock.receive()
                if m.get("text") and '"error"' in m["text"]:
                    err = m["text"]
                    break
            check("ws: bad input reports an error and keeps the connection", err is not None and "bad_key" in err, err)
            sock.send_json({"op": "ping"})
        check("blocked navigation 400", c.post("/api/browser/navigate", json={"id": tab, "url": "http://127.0.0.1:9331"}, headers=H).status_code == 400)
        r = c.post("/api/browser/tab", json={"url": "about:blank"}, headers=H)
        check("new tab", r.status_code == 200 and r.json()["id"], r.text)
        new_id = r.json()["id"]
        inputs = (
            {"id": new_id, "kind": "click", "x": 10, "y": 10}, {"id": new_id, "kind": "text", "text": "a"},
            {"id": new_id, "kind": "text", "text": "hello world"}, {"id": new_id, "kind": "key", "key": "Enter"},
            {"id": new_id, "kind": "scroll", "x": 5, "y": 5, "dy": 100},
        )
        check("click/key/text accepted", all(c.post("/api/browser/input", json=b, headers=H).status_code == 200 for b in inputs))
        check("unknown key rejected", c.post("/api/browser/input", json={"id": new_id, "kind": "key", "key": "F13"}, headers=H).status_code == 400)
        check("close tab", c.post("/api/browser/tab/close", json={"id": new_id}, headers=H).status_code == 200)
        # cookies set the way a login would (CDP), then read as the bot does
        bs._cdp(bs._browser_ws(), [("Storage.setCookies", {"cookies": [
            {"name": "auth_token", "value": "TOPSECRET", "domain": ".x.com", "path": "/", "secure": True,
             "httpOnly": True, "expires": time.time() + 86400},
            {"name": "sessionid", "value": "IGSECRET", "domain": ".instagram.com", "path": "/", "secure": True},
            {"name": "other", "value": "v", "domain": "example.org", "path": "/"}]})])
        d = c.get("/api/browser").json()
        check("summary lists domains, never values", d["cookies"]["count"] == 3
              and "TOPSECRET" not in str(d) and "IGSECRET" not in str(d), d)
        data, n, doms = bs.export_netscape(services=["twitter"])
        check("export twitter only", n == 1 and b"TOPSECRET" in data and b"IGSECRET" not in data and doms == ["x.com"])
        good, why = validate_cookie_bytes(data)
        check("export valid for the bot", good, why)
        check("summary marks which domains reach the bot",
              {d["domain"]: d["shared"] for d in c.get("/api/browser").json()["cookies"]["domains"]} == {"x.com": True, "instagram.com": True, "example.org": False})
        data, n, doms = bs.export_netscape()
        check("export all tabs/services", n == 3 and b"IGSECRET" in data and {ln.split("	")[0] for ln in data.decode().splitlines()}.issuperset({"example.org"}))
        check("nothing for a service without cookies", bs.export_netscape(services=["vk"]) == (None, 0, []))
        r = c.post("/api/browser/cookies/clear", json={"domain": "x.com"}, headers=H)
        check("clear one domain", r.status_code == 200 and r.json()["removed"] == 1, r.text)
        check("the rest remains", bs.export_netscape()[1] == 2)
        r = c.post("/api/browser/cookies/clear", json={}, headers=H)
        check("clear all", r.status_code == 200 and bs.export_netscape()[1] == 0, r.text)
    finally:
        bs.stop()
    check("stop", not bs.is_running())

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
