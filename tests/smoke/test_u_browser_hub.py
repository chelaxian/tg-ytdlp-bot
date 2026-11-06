"""Smoke test: persistent browser hub (push frames, zoom, identity, input) against a real Chromium.

Run: python tests/smoke/test_u_browser_hub.py   (skipped without Chromium/Chrome)
"""
import os
import sys
import tempfile
import time
from pathlib import Path

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)
TMP = Path(tempfile.mkdtemp(prefix="hub_test_"))
os.environ["TG_DASHBOARD_PROJECT_DIR"] = str(TMP)
(TMP / "CONFIG").mkdir()

from HELPERS import browser_hub as bh  # noqa: E402
from HELPERS import browser_session as bs  # noqa: E402

ok = fail = 0


def check(name, cond, info=""):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name} {info}")


# ---- pure parts
calls = bs.build_input_calls("text", 1280, 800, text="a")
check("typed letter carries code and key code", calls[0][1].get("code") == "KeyA" and calls[0][1].get("windowsVirtualKeyCode") == 65)
calls = bs.build_input_calls("text", 1280, 800, text="Q")
check("capital letter sets shift", calls[0][1]["modifiers"] == 8 and calls[0][1]["unmodifiedText"] == "q")
check("digit has Digit code", bs.build_input_calls("text", text="7")[0][1]["code"] == "Digit7")
check("long text is inserted in one go", bs.build_input_calls("text", text="hello@example.com")[0][0] == "Input.insertText")
try:
    bs.build_input_calls("click", 640, 400, x=700, y=10)
    check("click outside the viewport rejected", False)
except bs.BrowserError:
    check("click outside the viewport rejected", True)
check("click inside a zoomed-out viewport accepted", len(bs.build_input_calls("click", 2560, 1600, x=2000, y=1500)) == 3)

exe = bs.find_executable()
if not exe:
    print("SKIP live hub tests: no Chromium/Chrome found")
else:
    bs.PROFILE_DIR = TMP / "profile"
    bs.PID_FILE = TMP / "pid"
    bs.cdp_port = lambda: 9344
    hub = bh.BrowserHub()
    try:
        check("start browser", bs.start().get("started") is True)
        hub.ensure()
        tid = hub.new_tab("about:blank")
        check("new tab attached", bool(tid) and tid in hub._sessions)

        # identity: what Google sees (client hints exist on secure pages only)
        hub.navigate(tid, "https://example.com")
        time.sleep(2.5)
        ident = hub.evaluate(tid, "JSON.stringify({wd: navigator.webdriver, brands: navigator.userAgentData.brands.map(b => b.brand), "
                                  "pk: typeof window.PublicKeyCredential, ua: navigator.userAgent, chrome: typeof window.chrome})")
        import json
        ident = json.loads(ident)
        check("webdriver is false", ident["wd"] is False)
        check("client hints include Google Chrome", "Google Chrome" in ident["brands"], ident)
        check("user agent is not headless", "Headless" not in ident["ua"], ident["ua"])
        check("no passkey API (no passkey prompts)", ident["pk"] == "undefined", ident)
        check("window.chrome exists", ident["chrome"] == "object")
        hub.navigate(tid, "https://example.com")
        time.sleep(2.5)
        check("identity survives navigation", hub.evaluate(tid, "typeof window.PublicKeyCredential") == "undefined")

        # frames
        t0 = time.time()
        fr = hub.frame(tid, 0, "fast", wait=5)
        check("first frame arrives", fr is not None and fr.data[:3] == b"\xff\xd8\xff", fr)
        first_ms = (time.time() - t0) * 1000
        check("frame is small (fast profile)", len(fr.data) < 120_000, len(fr.data))
        check("viewport at 100%", (fr.vw, fr.vh) == (1280, 800), (fr.vw, fr.vh))
        t0 = time.time()
        quiet = hub.frame(tid, fr.seq, "fast", wait=1.5)
        check("still page: nothing new (204) after the wait", quiet is None or quiet.seq > fr.seq)
        # a change is pushed quickly
        hub.evaluate(tid, "document.body.style.background = 'red'")
        t0 = time.time()
        changed = hub.frame(tid, (quiet or fr).seq, "fast", wait=3)
        check("page change is pushed", changed is not None and changed.seq > fr.seq, changed)
        check("push latency under 1 s", changed is not None and (time.time() - t0) < 1.0, time.time() - t0)

        # zoom
        z = hub.set_zoom(tid, 0.5)
        check("zoom out accepted", z == 0.5)
        zf = hub.frame(tid, 0, "fast", wait=5)
        check("zoomed out: layout viewport doubles", zf is not None and (zf.vw, zf.vh) == (2560, 1600), zf and (zf.vw, zf.vh))
        check("page really lays out wider", hub.evaluate(tid, "innerWidth") == 2560)
        check("zoom is clamped", hub.set_zoom(tid, 9) == bh.ZOOM_MAX and hub.set_zoom(tid, 0.1) == bh.ZOOM_MIN)
        hub.set_zoom(tid, 1.0)
        check("zoom reset", hub.evaluate(tid, "innerWidth") == 1280)

        # input over the open connection
        hub.navigate(tid, "https://example.com")
        time.sleep(2)
        hub.evaluate(tid, "document.body.innerHTML = '<input id=a autofocus><button id=b onclick=\"window.hit=1\" style=\"position:fixed;left:10px;top:100px;width:200px;height:60px\">go</button>'; document.getElementById('a').focus()")
        for ch in "Hi 1":
            hub.input(tid, "text", text=ch)
        time.sleep(0.4)
        check("typed text reaches the field", hub.evaluate(tid, "document.getElementById('a').value") == "Hi 1",
              hub.evaluate(tid, "document.getElementById('a').value"))
        hub.input(tid, "click", x=50, y=120)
        time.sleep(0.4)
        check("click reaches the page", hub.evaluate(tid, "window.hit") == 1)

        # tabs
        tid2 = hub.new_tab("about:blank")
        check("second tab has the same identity", hub.evaluate(tid2, "typeof window.PublicKeyCredential") == "undefined")
        hub.close_tab(tid2)
        time.sleep(0.5)
        check("closed tab is forgotten", tid2 not in hub._sessions)
        try:
            hub.navigate(tid, "http://127.0.0.1:9344")
            check("internal address refused", False)
        except bs.BrowserError:
            check("internal address refused", True)
        # popups (Sign in with Google / SSO windows): same identity from the very first request, opener kept
        import http.server
        import json as _json
        import threading
        seen = {}

        class Handler(http.server.BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def do_GET(self):
                if self.path.startswith("/b"):
                    seen["sec_ch_ua"] = self.headers.get("Sec-CH-UA", "")
                    body = ("<script>opener.postMessage({pk: typeof PublicKeyCredential, hasOpener: !!window.opener, "
                            "brands: navigator.userAgentData.brands.map(b => b.brand), wd: navigator.webdriver}, '*')</script>popup")
                else:
                    body = ("<script>window.msgs = []; addEventListener('message', e => msgs.push(e.data));</script>"
                            "<button style='position:fixed;left:10px;top:100px;width:300px;height:80px' "
                            "onclick=\"window.open('/b', 'pop', 'width=500,height=600')\">open</button>")
                data = body.encode()
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{srv.server_address[1]}"
        tab_a = hub.new_tab("about:blank")
        hub._call("Page.navigate", {"url": base + "/a"}, hub._session(tab_a))
        time.sleep(1.2)
        before = {t["id"] for t in bs.list_tabs()}
        hub.input(tab_a, "click", x=50, y=130)
        time.sleep(2.0)
        after = {t["id"] for t in bs.list_tabs()}
        popup = list(after - before)
        check("popup opened as a new tab", len(popup) == 1, after - before)
        check("popup got the browser identity before its first request", "Google Chrome" in seen.get("sec_ch_ua", ""), seen)
        msgs = _json.loads(hub.evaluate(tab_a, "JSON.stringify(window.msgs)") or "[]")
        check("popup talks to its opener", bool(msgs) and msgs[0].get("hasOpener") is True, msgs)
        check("popup identity: brands, no passkey, no webdriver", bool(msgs) and "Google Chrome" in msgs[0].get("brands", [])
              and msgs[0].get("pk") == "undefined" and msgs[0].get("wd") is False, msgs)
        if popup:
            check("popup is controllable by the hub", hub.evaluate(popup[0], "document.body.innerText") == "popup")
            hub.close_tab(popup[0])
        srv.shutdown()

        # reconnect after the connection drops
        hub._ws.close()
        time.sleep(1.5)
        hub.ensure()
        check("hub reconnects", hub.evaluate(tid, "1+1") == 2)
    finally:
        bs.stop()

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
