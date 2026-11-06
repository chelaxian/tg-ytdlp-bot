"""Persistent control channel to the live browser, used by the dashboard.

Why it exists: opening a new DevTools connection and polling a screenshot for every
frame made the browser tab feel slow (about 1 frame per second, every click paid a
handshake). The hub keeps ONE websocket to the browser and multiplexes every page
over it (CDP "flat" sessions):

* frames are pushed by Chromium (Page.startScreencast) only when the picture
  changes, already scaled down and JPEG-compressed; a static login page costs nothing;
* clicks and keys go over the open connection;
* page zoom is an emulated viewport (Emulation.setDeviceMetricsOverride): zoom 50%
  makes the page lay out in a window twice as large, so more of it fits;
* every page gets a normal-Chrome identity (client-hint brands, no webdriver flag, no
  passkey prompts, a real-looking WebGL vendor) so Google sign-in does not treat it as an
  unsupported "automated" browser.

The hub lives in the dashboard process and reconnects by itself. The browser process
and its cookies are unaffected when the dashboard restarts.
"""

from __future__ import annotations

import base64
import json
import logging
import platform
import queue
import threading
import time
from typing import Any, Dict, Optional, Tuple

from HELPERS import browser_session as bs
from HELPERS.browser_session import BrowserError

logger = logging.getLogger(__name__)

BASE_W, BASE_H = 1280, 800                      # viewport at 100% zoom
ZOOM_MIN, ZOOM_MAX = 0.5, 2.0
# jpeg quality, max frame width, minimum seconds between frames: Chromium paints ~60 times a second and a login page
# does not need that; delaying the acknowledgement of a frame throttles it and the last change is still delivered
PROFILES = {"fast": (35, 800, 0.12), "normal": (55, 1100, 0.08), "sharp": (75, 1500, 0.05)}
# no video or streaming media: it only burns CPU (TikTok and YouTube autoplay on their login pages)
BLOCKED_MEDIA = ["*.mp4", "*.mp4?*", "*.webm", "*.webm?*", "*.m3u8", "*.m3u8?*", "*.m4s", "*.m4s?*", "*.mpd", "*.mpd?*",
                 "*/video/tos/*", "*googlevideo.com/videoplayback*"]
CAST_IDLE = 15.0                                # stop screencasting a tab nobody looks at
# While nobody has the panel open the browser rests: a blank "parking" tab is brought to the front and the service tabs
# are frozen (no JS, no painting; logins and cookies stay in the profile). Every tab is woken and reloaded now and
# then so its session stays alive and rotating cookies are refreshed for the bot.
PARK_URL = "about:blank#tg-park"
IDLE_PARK = 60.0                                # seconds without a viewer before the browser rests
KEEPALIVE_EVERY = 3 * 3600.0                    # each tab is reloaded about this often while resting
KEEPALIVE_WAIT = 45.0                           # how long a reloaded tab may run before it is frozen again
KEEPER_TICK = 20.0
CALL_TIMEOUT = 10.0

# Only for the headless fallback (no Xvfb): a windowed Chrome needs no patches at all. Kept to the two traits headless
# really differs in; everything else (webdriver, languages, WebGL, WebRTC, passkeys) is native.
STEALTH = r"""(() => { try {
  try { Object.defineProperty(window, 'outerWidth', { get: () => window.innerWidth, configurable: true }); } catch (e) {}
  try { Object.defineProperty(window, 'outerHeight', { get: () => window.innerHeight + 87, configurable: true }); } catch (e) {}
  try {
    if (!window.Notification) {
      const N = function Notification() {};
      N.requestPermission = () => Promise.resolve('default');
      window.Notification = N;
    }
    Object.defineProperty(Notification, 'permission', { get: () => 'default', configurable: true });
  } catch (e) {}
} catch (e) {} })();"""


class Frame:
    __slots__ = ("seq", "data", "vw", "vh")

    def __init__(self, seq: int, data: bytes, vw: int, vh: int):
        self.seq, self.data, self.vw, self.vh = seq, data, vw, vh


class BrowserHub:
    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._cond = threading.Condition(self._lock)
        self._send_lock = threading.Lock()
        self._attach_lock = threading.Lock()
        self._ws: Optional[bs._WebSocket] = None
        self._thread: Optional[threading.Thread] = None
        self._next_id = 0
        self._pending: Dict[int, list] = {}
        self._sessions: Dict[str, str] = {}          # targetId -> sessionId
        self._by_session: Dict[str, str] = {}
        self._zoom: Dict[str, float] = {}
        self._frames: Dict[str, Frame] = {}
        self._cast: Dict[str, Tuple[int, int, int, int, float]] = {}   # active screencast: quality, width, vw, vh, min gap
        self._want: Dict[str, float] = {}
        self._seq = 0
        self._attach_q: "queue.Queue[tuple]" = queue.Queue()
        self._ua: Optional[Dict[str, Any]] = None
        self._is_headless: Optional[bool] = None
        self._last_view = 0.0                          # monotonic time the panel last looked at / typed into a tab
        self._parked = False
        self._frozen: set = set()
        self._refreshed: Dict[str, float] = {}          # targetId -> wall time of the last keep-alive reload
        self._keeper: Optional[threading.Thread] = None
        self._last_frame: Dict[str, float] = {}
        self._ready: set = set()                       # targets whose identity script / emulation is installed

    # ------------------------------------------------------------ connection
    def ensure(self) -> None:
        """Connect (or reconnect) and attach to every open page. Raises BrowserError when the browser is down."""
        with self._lock:
            if self._ws is not None and self._thread is not None and self._thread.is_alive():
                return
            ws = bs._WebSocket(bs._browser_ws(), timeout=15)
            self._ws = ws
            self._sessions.clear(); self._by_session.clear(); self._frames.clear(); self._cast.clear(); self._want.clear()
            self._ready.clear()
            self._is_headless = None                     # the browser may have restarted in another mode
            self._parked = False
            self._frozen.clear()
            self._thread = threading.Thread(target=self._run, args=(ws,), daemon=True, name="browser-hub")
            self._thread.start()
            threading.Thread(target=self._attach_worker, args=(ws,), daemon=True, name="browser-hub-attach").start()
        self._call("Target.setDiscoverTargets", {"discover": True})
        # Every new page, popups included (Sign in with Google, SSO windows), is paused until it has the browser
        # identity, so even its very first request looks like regular Chrome.
        self._call("Target.setAutoAttach", {"autoAttach": True, "waitForDebuggerOnStart": True, "flatten": True})
        existing = [i["targetId"] for i in (self._call("Target.getTargets").get("targetInfos") or []) if i.get("type") == "page"]
        deadline = time.monotonic() + 0.6
        while time.monotonic() < deadline and any(t not in self._sessions for t in existing):
            time.sleep(0.05)
        for tid in existing:
            if tid not in self._sessions:
                self._attach(tid)

    def _teardown(self, ws) -> None:
        with self._lock:
            if self._ws is ws:
                self._ws = None
            self._sessions.clear(); self._by_session.clear(); self._cast.clear(); self._want.clear()
            for slot in self._pending.values():
                slot[1] = {"_error": "not_running"}
                slot[0].set()
            self._pending.clear()
            self._cond.notify_all()
        ws.close()

    def _run(self, ws) -> None:
        try:
            while self._ws is ws:
                if not ws.readable(1.0):
                    self._tick()
                    continue
                self._dispatch(json.loads(ws.recv()))
                self._tick()
        except (BrowserError, OSError, ValueError) as exc:
            logger.info("[browser-hub] connection closed: %s", exc)
        except Exception:
            logger.exception("[browser-hub] reader failed")
        finally:
            self._teardown(ws)

    def _attach_worker(self, ws) -> None:
        while self._ws is ws:
            try:
                tid, sid, waiting = self._attach_q.get(timeout=1.0)
            except queue.Empty:
                continue
            try:
                self._setup(tid, sid)
            except BrowserError as exc:
                logger.debug("[browser-hub] setup of %s failed: %s", tid, exc)
            finally:
                if waiting:                                   # never leave a page paused
                    try:
                        self._send("Runtime.runIfWaitingForDebugger", {}, sid, None)
                    except BrowserError:
                        pass

    # ------------------------------------------------------------ messaging
    def _send(self, method: str, params: Optional[dict], session: Optional[str], slot: Optional[list]) -> None:
        with self._send_lock:
            ws = self._ws
            if ws is None:
                raise BrowserError("not_running")
            with self._lock:
                self._next_id += 1
                mid = self._next_id
                if slot is not None:
                    self._pending[mid] = slot
            msg: Dict[str, Any] = {"id": mid, "method": method, "params": params or {}}
            if session:
                msg["sessionId"] = session
            try:
                ws.send(json.dumps(msg))
            except OSError as exc:
                raise BrowserError("not_running") from exc

    def _call(self, method: str, params: Optional[dict] = None, session: Optional[str] = None,
              timeout: float = CALL_TIMEOUT) -> dict:
        slot = [threading.Event(), None]
        self._send(method, params, session, slot)
        if not slot[0].wait(timeout):
            raise BrowserError("cdp_timeout")
        result = slot[1] or {}
        if "_error" in result:
            raise BrowserError(result["_error"])
        return result

    def _dispatch(self, msg: dict) -> None:
        if "id" in msg:
            with self._lock:
                slot = self._pending.pop(msg["id"], None)
            if slot is not None:
                if "error" in msg:
                    slot[1] = {"_error": "cdp_error: " + str(msg["error"].get("message", ""))[:200]}
                else:
                    slot[1] = msg.get("result") or {}
                slot[0].set()
            return
        method, params = msg.get("method"), msg.get("params") or {}
        if method == "Page.screencastFrame":
            session = msg.get("sessionId")
            with self._lock:
                tid = self._by_session.get(session or "")
                cast = self._cast.get(tid or "")
                now = time.monotonic()
                gap = cast[4] if cast else 0.0
                delay = max(0.0, gap - (now - self._last_frame.get(tid or "", 0.0)))
                self._last_frame[tid or ""] = now + delay
            ack = {"sessionId": params.get("sessionId")}
            if delay > 0.005:
                threading.Timer(delay, self._ack_late, args=(ack, session)).start()
            else:
                self._ack_late(ack, session)
            with self._lock:
                if tid:
                    vw, vh = self._viewport(tid)
                    self._seq += 1
                    self._frames[tid] = Frame(self._seq, base64.b64decode(params.get("data", "")), vw, vh)
                    self._cond.notify_all()
        elif method == "Target.attachedToTarget":
            self._on_attached(params)
        elif method in ("Target.targetDestroyed", "Target.detachedFromTarget"):
            tid = params.get("targetId") or self._by_session.get(params.get("sessionId") or "")
            if tid:
                self._forget(tid)

    def _on_attached(self, params: dict) -> None:
        sid = params.get("sessionId") or ""
        info = params.get("targetInfo") or {}
        tid = info.get("targetId") or ""
        waiting = bool(params.get("waitingForDebugger"))
        if info.get("type") != "page":
            if waiting:                                       # workers etc.: just let them run
                try:
                    self._send("Runtime.runIfWaitingForDebugger", {}, sid, None)
                    self._send("Target.detachFromTarget", {"sessionId": sid}, None, None)
                except BrowserError:
                    pass
            return
        with self._lock:
            if sid in self._by_session or tid in self._sessions:
                if waiting:
                    try:
                        self._send("Runtime.runIfWaitingForDebugger", {}, sid, None)
                    except BrowserError:
                        pass
                return
            self._sessions[tid] = sid
            self._by_session[sid] = tid
        self._attach_q.put((tid, sid, waiting))

    def _forget(self, tid: str) -> None:
        with self._lock:
            sid = self._sessions.pop(tid, None)
            if sid:
                self._by_session.pop(sid, None)
            self._ready.discard(tid)
            for table in (self._zoom, self._frames, self._cast, self._want):
                table.pop(tid, None)
            self._cond.notify_all()

    def _tick(self) -> None:
        """Stop the screencast of tabs nobody has asked a frame from for a while."""
        now = time.monotonic()
        with self._lock:
            idle = [tid for tid in list(self._cast) if self._want.get(tid, 0) < now]
        for tid in idle:
            sid = self._sessions.get(tid)
            with self._lock:
                self._cast.pop(tid, None)
            if sid:
                try:
                    self._send("Page.stopScreencast", {}, sid, None)
                except BrowserError:
                    pass

    def _ack_late(self, ack: dict, session: Optional[str]) -> None:
        try:
            self._send("Page.screencastFrameAck", ack, session, None)
        except BrowserError:
            pass

    # ------------------------------------------------------------ pages
    def _headless(self) -> bool:
        """Headless fallback only: a windowed Chrome (Xvfb) keeps its own, genuine identity."""
        if self._is_headless is None:
            self._is_headless = not bs.is_windowed()
        return self._is_headless

    def _identity(self) -> Dict[str, Any]:
        if self._ua is None:
            info = self._call("Browser.getVersion")
            product = str(info.get("product", "Chrome/156.0.0.0"))
            full = product.split("/", 1)[-1]
            major = full.split(".", 1)[0]
            arch = "arm" if platform.machine().lower() in ("aarch64", "arm64") else "x86"
            self._ua = {
                "userAgent": f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{major}.0.0.0 Safari/537.36",
                "acceptLanguage": "en-US,en",            # Chrome adds the q-values to the header itself
                "platform": "Linux x86_64",
                "userAgentMetadata": {
                    "brands": [{"brand": "Not:A-Brand", "version": "8"}, {"brand": "Chromium", "version": major},
                               {"brand": "Google Chrome", "version": major}],
                    "fullVersionList": [{"brand": "Not:A-Brand", "version": "8.0.0.0"}, {"brand": "Chromium", "version": full},
                                        {"brand": "Google Chrome", "version": full}],
                    "platform": "Linux", "platformVersion": "6.5.0", "architecture": arch, "model": "",
                    "mobile": False, "bitness": "64", "wow64": False,
                },
            }
        return self._ua

    def _setup(self, tid: str, sid: str) -> None:
        for method, params in (
            ("Page.enable", {}),
            ("Network.enable", {}),
            ("Network.setBlockedURLs", {"urls": BLOCKED_MEDIA}),
            *((("Emulation.setUserAgentOverride", self._identity()),
               ("Page.addScriptToEvaluateOnNewDocument", {"source": STEALTH}),
               ("Runtime.evaluate", {"expression": STEALTH})) if self._headless() else ()),
        ):
            try:
                self._call(method, params, sid)
            except BrowserError as exc:
                logger.debug("[browser-hub] %s failed: %s", method, exc)
        self._apply_zoom(tid, sid)
        with self._lock:
            self._ready.add(tid)
            self._cond.notify_all()

    def _attach(self, tid: str) -> str:
        """Explicit attach (pages that existed before the hub connected)."""
        with self._attach_lock:
            with self._lock:
                if tid in self._sessions:
                    return self._sessions[tid]
            res = self._call("Target.attachToTarget", {"targetId": tid, "flatten": True})
            sid = res.get("sessionId")
            if not sid:
                raise BrowserError("no_such_tab")
            with self._lock:
                self._sessions[tid] = sid
                self._by_session[sid] = tid
            self._setup(tid, sid)
            return sid

    def _session(self, tid: str, wait: float = 3.0) -> str:
        bs._check_id(tid)
        self.ensure()
        with self._cond:
            sid = self._sessions.get(tid)
            if sid:
                end = time.monotonic() + wait
                while tid not in self._ready and time.monotonic() < end:
                    self._cond.wait(0.1)
                return sid
        deadline = time.monotonic() + wait
        quick = time.monotonic() + 0.5                         # a fresh tab is attached by auto-attach: give it a moment
        while time.monotonic() < quick:
            with self._cond:
                sid = self._sessions.get(tid)
                if sid:
                    end = time.monotonic() + wait
                    while tid not in self._ready and time.monotonic() < end:
                        self._cond.wait(0.1)
                    return sid
            time.sleep(0.05)
        while True:
            try:
                return self._attach(tid)
            except BrowserError as exc:
                if time.monotonic() > deadline or str(exc) not in ("no_such_tab", "cdp_error: No target with given id found"):
                    raise BrowserError("no_such_tab") from exc
                time.sleep(0.2)

    def _viewport(self, tid: str) -> Tuple[int, int]:
        z = self._zoom.get(tid, 1.0)
        return round(BASE_W / z), round(BASE_H / z)

    def _apply_zoom(self, tid: str, sid: str) -> None:
        vw, vh = self._viewport(tid)
        self._call("Emulation.setDeviceMetricsOverride",
                   {"width": vw, "height": vh, "deviceScaleFactor": 1, "mobile": False,
                    "screenWidth": bs.SCREEN[0], "screenHeight": bs.SCREEN[1]}, sid)

    # ------------------------------------------------------------ public API
    def zoom(self, tid: str) -> float:
        return self._zoom.get(tid, 1.0)

    def set_zoom(self, tid: str, zoom: float) -> float:
        sid = self._session(tid)
        z = max(ZOOM_MIN, min(ZOOM_MAX, round(float(zoom), 2)))
        with self._lock:
            self._zoom[tid] = z
            self._cast.pop(tid, None)
            self._frames.pop(tid, None)
        self._apply_zoom(tid, sid)
        try:
            self._send("Page.stopScreencast", {}, sid, None)
        except BrowserError:
            pass
        return z

    def new_tab(self, url: str = "about:blank") -> str:
        """Create a tab, give it the browser identity, then open the URL (so even the first request is covered)."""
        target = "about:blank" if url == "about:blank" else bs.normalize_url(url)
        self.ensure()
        tid = self._call("Target.createTarget", {"url": "about:blank"}).get("targetId", "")
        sid = self._session(tid)
        if target != "about:blank":
            self._call("Page.navigate", {"url": target}, sid)
        return tid

    def close_tab(self, tid: str) -> None:
        bs._check_id(tid)
        self.ensure()
        self._call("Target.closeTarget", {"targetId": tid})

    def activate(self, tid: str) -> None:
        bs._check_id(tid)
        self.ensure()
        self._wake()
        self._call("Target.activateTarget", {"targetId": tid})

    def navigate(self, tid: str, url: str) -> None:
        self._call("Page.navigate", {"url": bs.normalize_url(url)}, self._session(tid))

    def history(self, tid: str, action: str) -> None:
        sid = self._session(tid)
        if action == "reload":
            self._call("Page.reload", {}, sid)
            return
        if action not in ("back", "forward"):
            raise BrowserError("bad_action")
        hist = self._call("Page.getNavigationHistory", {}, sid)
        index = hist.get("currentIndex", 0) + (-1 if action == "back" else 1)
        entries = hist.get("entries") or []
        if 0 <= index < len(entries):
            self._call("Page.navigateToHistoryEntry", {"entryId": entries[index]["id"]}, sid)

    def input(self, tid: str, kind: str, **p: Any) -> None:
        sid = self._session(tid)
        self._wake(tid)
        vw, vh = self._viewport(tid)
        for method, params in bs.build_input_calls(kind, vw, vh, **p):
            self._send(method, params, sid, None)         # in order, no round trip per event
        with self._lock:
            self._want[tid] = time.monotonic() + CAST_IDLE

    def evaluate(self, tid: str, expression: str) -> Any:
        res = self._call("Runtime.evaluate", {"expression": expression, "returnByValue": True, "awaitPromise": True},
                         self._session(tid))
        if res.get("exceptionDetails"):
            raise BrowserError("js_error")
        return (res.get("result") or {}).get("value")

    def frame(self, tid: str, since: int = 0, profile: str = "fast", wait: float = 3.0) -> Optional[Frame]:
        """The next picture newer than `since`; None when nothing changed within `wait` seconds."""
        sid = self._session(tid)
        self._wake(tid)
        quality, max_w, gap = PROFILES.get(profile, PROFILES["fast"])
        vw, vh = self._viewport(tid)
        wanted = (quality, max_w, vw, vh, gap)
        with self._lock:
            self._want[tid] = time.monotonic() + CAST_IDLE
            current = self._cast.get(tid)
        if current != wanted:
            with self._lock:
                self._cast[tid] = wanted
                self._frames.pop(tid, None)               # a picture of another quality/size is stale now
            if current is not None:
                self._send("Page.stopScreencast", {}, sid, None)
            self._send("Page.startScreencast", {"format": "jpeg", "quality": quality, "maxWidth": max_w,
                                                "maxHeight": max(1, round(max_w * vh / vw)), "everyNthFrame": 1}, sid, None)
        started = time.monotonic()
        deadline = started + wait
        with self._cond:
            while True:
                fr = self._frames.get(tid)
                if fr is not None and fr.seq > since:
                    return fr
                now = time.monotonic()
                if now >= deadline:
                    break
                if fr is None and now - started > 1.0:
                    break                                   # a still page may never emit a frame: take one picture
                self._cond.wait(min(0.25, deadline - now))
        if self._frames.get(tid) is None or since == 0:
            try:
                res = self._call("Page.captureScreenshot", {
                    "format": "jpeg", "quality": quality, "optimizeForSpeed": True,
                    "clip": {"x": 0, "y": 0, "width": vw, "height": vh, "scale": min(1.0, max_w / vw)}}, sid)
                with self._lock:
                    self._seq += 1
                    fr = Frame(self._seq, base64.b64decode(res["data"]), vw, vh)
                    self._frames[tid] = fr
                return fr
            except (BrowserError, KeyError, ValueError):
                return None
        return None


    # ------------------------------------------------------------ resting while nobody watches
    def _wake(self, tid: Optional[str] = None) -> None:
        """The panel is looking: thaw the tabs and bring the watched one back to the front."""
        self._last_view = time.monotonic()
        if not self._parked and not self._frozen:
            return
        with self._lock:
            frozen, self._frozen = list(self._frozen), set()
            parked, self._parked = self._parked, False
        for other in frozen:
            sid = self._sessions.get(other)
            if sid:
                try:
                    self._call("Page.setWebLifecycleState", {"state": "active"}, sid)
                except BrowserError:
                    pass
        if parked and tid:
            try:
                self._call("Target.activateTarget", {"targetId": tid})
            except BrowserError:
                pass

    def _pages(self) -> list:
        return [t for t in (bs._http("/json/list") or []) if t.get("type") == "page" and t.get("id")]

    def _freeze(self, tid: str) -> None:
        try:
            self._call("Page.setWebLifecycleState", {"state": "frozen"}, self._session(tid))
            with self._lock:
                self._frozen.add(tid)
        except BrowserError as exc:                   # a page still visible cannot be frozen: next tick
            logger.debug("[browser-hub] freeze %s: %s", tid, exc)

    def rest(self) -> None:
        """Park the browser (blank tab in front) and freeze the service tabs."""
        self.ensure()
        pages = self._pages()
        park = next((t for t in pages if str(t.get("url", "")).startswith(PARK_URL)), None)
        if park is None:
            park_id = self._call("Target.createTarget", {"url": PARK_URL}).get("targetId", "")
        else:
            park_id = park["id"]
        if not self._parked:
            self._call("Target.activateTarget", {"targetId": park_id})
            with self._lock:
                self._parked = True
            time.sleep(1.0)                               # let the other tabs become hidden first
        for t in pages:
            if t["id"] != park_id and t["id"] not in self._frozen:
                self._freeze(t["id"])

    def keep_alive(self) -> Optional[str]:
        """While resting: wake and reload the tab whose session was refreshed longest ago (one per call)."""
        now = time.time()
        pages = [t for t in self._pages() if not str(t.get("url", "")).startswith(PARK_URL)
                 and str(t.get("url", "")).startswith("http")]
        for i, t in enumerate(pages):                     # first sight: spread the tabs over the interval
            self._refreshed.setdefault(t["id"], now - KEEPALIVE_EVERY + (i + 1) * KEEPALIVE_EVERY / max(1, len(pages)))
        due = [t for t in pages if now - self._refreshed[t["id"]] >= KEEPALIVE_EVERY]
        if not due:
            return None
        tab = min(due, key=lambda t: self._refreshed[t["id"]])
        tid = tab["id"]
        self._refreshed[tid] = now
        sid = self._session(tid)
        with self._lock:
            self._frozen.discard(tid)
        self._call("Page.setWebLifecycleState", {"state": "active"}, sid)
        self._call("Page.reload", {}, sid)
        logger.info("[browser-hub] keep-alive reload of %s", str(tab.get("url", ""))[:80])
        deadline = time.monotonic() + KEEPALIVE_WAIT
        while time.monotonic() < deadline:
            if time.monotonic() - self._last_view < IDLE_PARK:
                return tid                                 # the panel opened meanwhile: leave it running
            time.sleep(1.0)
        self._freeze(tid)
        return tid

    def _keep_tick(self) -> None:
        if not bs.enabled():
            return
        if not bs.is_running():
            if bs.wants_autostart():                      # it ran before a crash / reboot: bring it back
                try:
                    bs.start()
                    logger.info("[browser-hub] browser restarted (it was running before)")
                except BrowserError as exc:
                    logger.warning("[browser-hub] browser autostart failed: %s", exc)
            return
        if time.monotonic() - self._last_view < IDLE_PARK:
            return
        self.rest()
        self.keep_alive()

    def start_keeper(self) -> None:
        """Background upkeep (dashboard process only): rest when idle, keep sessions alive, restart after a crash."""
        if self._keeper is not None and self._keeper.is_alive():
            return

        def loop() -> None:
            while True:
                try:
                    self._keep_tick()
                except BrowserError as exc:
                    logger.debug("[browser-hub] keeper: %s", exc)
                except Exception:
                    logger.exception("[browser-hub] keeper failed")
                time.sleep(KEEPER_TICK)

        self._keeper = threading.Thread(target=loop, daemon=True, name="browser-keeper")
        self._keeper.start()


hub = BrowserHub()
