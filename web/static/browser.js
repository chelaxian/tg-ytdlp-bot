// "Browser" section: a remote Chromium the admin logs into. The bot reads the live cookies
// of this session (/cookies_from_browser and the service buttons of /cookie).
// The page is shown as JPEG frames painted on a <canvas> (no blob:/inline needed by the CSP);
// clicks, wheel and keys are posted back. No innerHTML anywhere.
import { t } from "./i18n.js";
import { h, api, toast, errorText, confirmDialog, num, getCsrf } from "./ui.js";

const MAX_FAILS = 4;
const BOOKMARKS = [["YouTube", "https://www.youtube.com/"], ["X", "https://x.com/"], ["Instagram", "https://www.instagram.com/"],
  ["VK", "https://vk.com/"], ["TikTok", "https://www.tiktok.com/"]];
const PROFILES = ["fast", "normal", "sharp"];     // picture quality: fast = smallest frames, the default

function brError(err) {
  const code = err && err.body && err.body.error;
  const text = code ? t(`br.err.${code}`) : null;
  return text && !text.startsWith("br.err.") ? text : errorText(err);
}

function post(path, body) { return api(path, { method: "POST", body: body || {}, timeout: 30000 }); }

export function buildBrowser(s, { panel, bindLoader }) {
  const view = panel({ title: t("br.session"), sub: t("br.session.sub"), span: 2 });
  const cookies = panel({ title: t("br.cookies"), sub: t("br.cookies.sub") });
  s.root.append(h("div", { class: "grid" }, view.el, cookies.el));

  const st = { data: null, tab: null, ui: null, running: false, known: null, order: [], queue: Promise.resolve(), ws: null, reqGen: 0, useLongPoll: false, wsFails: 0,
    decoding: false, pending: null, lastWatched: null, lastErr: 0, zoomTimer: null, watcher: null, wheel: 0, seq: 0, vw: 1280, vh: 800,
    abort: null, zoom: 1, profile: PROFILES.includes(localStorage.getItem("dash.br.profile")) ? localStorage.getItem("dash.br.profile") : "fast" };

  // a new picture is needed (tab, zoom or quality changed): forget the last frame and cancel the pending long poll
  const restartStream = () => {
    st.seq = 0;
    if (st.ws && st.ws.readyState === 1) watchNow();
    else if (st.abort) st.abort.abort();
  };

  // ------------------------------------------------------------ actions
  const act = async (fn, okText) => {
    try { const r = await fn(); if (okText) toast(okText, "ok"); await reload(); return r; }
    catch (err) { toast(brError(err), "error"); return null; }
  };

  const sendInput = (body) => {
    if (!st.tab) return;
    if (st.ws && st.ws.readyState === 1) { st.ws.send(JSON.stringify({ op: "input", id: st.tab, ...body })); return; }
    const payload = { id: st.tab, ...body };
    st.queue = st.queue.then(() => post("/api/browser/input", payload)).catch((err) => toast(brError(err), "error"));
  };

  const selectTab = async (id) => {
    st.tab = id;
    restartStream();
    renderTabs();
    try { await post("/api/browser/tab/activate", { id }); } catch { /* the frame loop reports real problems */ }
  };

  // ------------------------------------------------------------ ui skeleton
  function buildUi() {
    const statusPill = h("span", { class: "pill" });
    const power = h("button", { type: "button", class: "primary" });
    power.addEventListener("click", () => {
      if (st.data && st.data.running) {
        confirmDialog({ title: t("br.stop"), text: t("br.stop.text"), confirm: t("br.stop"), danger: true })
          .then((yes) => { if (yes) act(() => post("/api/browser/stop"), t("br.stopped")); });
      } else {
        power.disabled = true;
        act(() => post("/api/browser/start"), t("br.started")).finally(() => { power.disabled = false; });
      }
    });

    const tabs = h("div", { class: "br-tabs", role: "tablist", "aria-label": t("br.tabs") });
    const addTab = h("button", { type: "button", class: "icon-btn", "aria-label": t("br.newTab"), title: t("br.newTab") }, "+");
    addTab.addEventListener("click", async () => {
      const r = await act(() => post("/api/browser/tab", { url: "about:blank" }));
      if (r && r.id) { await selectTab(r.id); address.focus(); }
    });

    const nav = (action, label, glyph) => {
      const b = h("button", { type: "button", class: "ghost icon-btn", "aria-label": label, title: label }, glyph);
      b.addEventListener("click", () => { if (st.tab) act(() => post("/api/browser/history", { id: st.tab, action })); });
      return b;
    };
    // bookmarks: switch to the tab of that site if it is open, reuse a blank tab, else open a new tab
    const siteHost = (url) => { try { return new URL(url).hostname.replace(/^www\./, ""); } catch { return ""; } };
    const openBookmark = async (url) => {
      const host = siteHost(url);
      const tabs = (st.data && st.data.tabs) || [];
      const same = tabs.find((x) => { const other = siteHost(x.url); return other && (other === host || other.endsWith(`.${host}`)); });
      if (same) { await selectTab(same.id); return; }
      const current = tabs.find((x) => x.id === st.tab);
      if (current && (!current.url || current.url === "about:blank")) { act(() => post("/api/browser/navigate", { id: st.tab, url })); return; }
      const created = await act(() => post("/api/browser/tab", { url }));
      if (created && created.id) await selectTab(created.id);
    };
    const bookmarks = h("div", { class: "br-bookmarks", role: "group", "aria-label": t("br.bookmarks") },
      BOOKMARKS.map(([name, url]) => h("button", { type: "button", class: "ghost", title: url, onclick: () => openBookmark(url) }, name)));
    const address = h("input", { type: "text", class: "br-address", inputmode: "url", autocomplete: "off", spellcheck: "false",
      autocapitalize: "off", "aria-label": t("br.address"), placeholder: t("br.address.ph") });
    const go = h("button", { type: "submit", class: "primary" }, t("br.go"));
    const bar = h("form", { class: "br-toolbar", novalidate: true },
      nav("back", t("br.back"), "←"), nav("forward", t("br.forward"), "→"), nav("reload", t("br.reload"), "↻"), address, go);
    bar.addEventListener("submit", async (e) => {
      e.preventDefault();
      const url = address.value.trim();
      if (!url) return;
      if (!st.tab) { const r = await act(() => post("/api/browser/tab", { url })); if (r && r.id) await selectTab(r.id); return; }
      act(() => post("/api/browser/navigate", { id: st.tab, url }));
    });

    const canvas = h("canvas", { class: "br-canvas", width: 1280, height: 800, tabindex: 0, role: "application",
      "aria-label": t("br.screen") });
    // page zoom (zoom out = more of the page fits) and picture quality
    const zoomLabel = h("output", { class: "br-zoom-label", "aria-live": "polite" }, "100%");
    const zoomRange = h("input", { type: "range", class: "br-zoom-range", min: 50, max: 200, step: 10, value: 100, "aria-label": t("br.zoom") });
    const applyZoom = async (percent) => {
      const value = Math.max(50, Math.min(200, Math.round(percent / 10) * 10));
      zoomRange.value = String(value);
      zoomLabel.textContent = `${value}%`;
      if (!st.tab) return;
      const mine = ((st.data && st.data.tabs) || []).find((x) => x.id === st.tab);
      if (st.ws && st.ws.readyState === 1) {
        // over the open socket: no round trip, the new picture follows by itself
        st.reqGen = (st.reqGen + 1) & 0xFFFF;
        st.seq = 0;
        st.zoom = value / 100;
        if (mine) mine.zoom = st.zoom;
        st.ws.send(JSON.stringify({ op: "zoom", id: st.tab, zoom: st.zoom, gen: st.reqGen }));
        return;
      }
      try {
        const r = await post("/api/browser/zoom", { id: st.tab, zoom: value / 100 });
        st.zoom = r.zoom;
        const tab = ((st.data && st.data.tabs) || []).find((x) => x.id === st.tab);
        if (tab) tab.zoom = r.zoom;
        restartStream();
      } catch (err) { toast(brError(err), "error"); }
    };
    zoomRange.addEventListener("input", () => {
      zoomLabel.textContent = `${zoomRange.value}%`;
      clearTimeout(st.zoomTimer);
      st.zoomTimer = setTimeout(() => applyZoom(Number(zoomRange.value)), 100);   // follow the slider while it moves
    });
    const stepBtn = (label, glyph, delta) => h("button", { type: "button", class: "ghost icon-btn", "aria-label": label, title: label,
      onclick: () => applyZoom(Number(zoomRange.value) + delta) }, glyph);
    const quality = h("select", { class: "br-quality", "aria-label": t("br.quality") },
      PROFILES.map((p) => h("option", { value: p, selected: p === st.profile }, t(`br.q.${p}`))));
    quality.addEventListener("change", () => { st.profile = quality.value; localStorage.setItem("dash.br.profile", st.profile); restartStream(); });
    const zoomBar = h("div", { class: "br-zoombar", role: "group", "aria-label": t("br.zoom") },
      stepBtn(t("br.zoomOut"), "−", -10), zoomRange, stepBtn(t("br.zoomIn"), "+", 10),
      zoomLabel, h("button", { type: "button", class: "ghost", onclick: () => applyZoom(100) }, t("br.zoomReset")), quality);
    const empty = h("p", { class: "state br-empty" });
    const screen = h("div", { class: "br-screen" }, canvas, empty);

    // mouse
    // the picture is scaled down; clicks are sent in page pixels (the viewport size the server reports)
    const point = (e) => {
      const r = canvas.getBoundingClientRect();
      return { x: Math.round(((e.clientX - r.left) / r.width) * st.vw), y: Math.round(((e.clientY - r.top) / r.height) * st.vh) };
    };
    canvas.addEventListener("click", (e) => { canvas.focus(); if (e.detail < 2) sendInput({ kind: "click", ...point(e) }); });
    canvas.addEventListener("dblclick", (e) => sendInput({ kind: "dblclick", ...point(e) }));
    canvas.addEventListener("contextmenu", (e) => { e.preventDefault(); sendInput({ kind: "click", button: "right", ...point(e) }); });
    canvas.addEventListener("wheel", (e) => {
      e.preventDefault();
      const now = Date.now();
      if (now - st.wheel < 60) return;
      st.wheel = now;
      sendInput({ kind: "scroll", dx: Math.round(e.deltaX), dy: Math.round(e.deltaY), ...point(e) });
    }, { passive: false });
    // keyboard: printable keys as text, editing keys as key events; Tab stays with the panel (see buttons)
    const keyMap = new Set(["Enter", "Backspace", "Escape", "Delete", "ArrowLeft", "ArrowUp", "ArrowRight", "ArrowDown", "Home", "End", "PageUp", "PageDown"]);
    canvas.addEventListener("keydown", (e) => {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      if (keyMap.has(e.key)) { e.preventDefault(); sendInput({ kind: "key", key: e.key, shift: e.shiftKey }); }
      else if (e.key.length === 1) { e.preventDefault(); sendInput({ kind: "text", text: e.key }); }
    });
    canvas.addEventListener("paste", (e) => {
      const text = (e.clipboardData && e.clipboardData.getData("text")) || "";
      if (text) { e.preventDefault(); sendInput({ kind: "text", text }); }
    });

    // text box for IME / mobile / password managers, plus keys that would leave the page
    const textInput = h("input", { type: "text", class: "br-text", autocomplete: "off", spellcheck: "false", "aria-label": t("br.text"), placeholder: t("br.text.ph") });
    const sendText = () => { if (textInput.value) { sendInput({ kind: "text", text: textInput.value }); textInput.value = ""; } };
    textInput.addEventListener("keydown", (e) => { if (e.key === "Enter") { e.preventDefault(); sendText(); } });
    const keyBtn = (key, label) => h("button", { type: "button", class: "ghost", onclick: () => sendInput({ kind: "key", key }) }, label);
    const keys = h("div", { class: "br-keys" }, textInput,
      h("button", { type: "button", class: "ghost", onclick: sendText }, t("br.send")),
      keyBtn("Tab", "Tab"), keyBtn("Enter", "Enter"), keyBtn("Backspace", "⌫"), keyBtn("Escape", "Esc"));

    const help = h("p", { class: "muted br-help" }, t("br.help"));
    const missing = h("div", { class: "state" });
    const live = h("div", { class: "br-live" }, bookmarks, tabs, bar, zoomBar, screen, keys, help);

    const top = h("div", { class: "br-top" }, statusPill, power);
    view.body.replaceChildren(top, missing, live);
    return { statusPill, power, tabs, addTab, address, canvas, empty, live, missing, zoomRange, zoomLabel };
  }

  function renderTabs() {
    const ui = st.ui;
    if (!ui) return;
    const list = (st.data && st.data.tabs) || [];
    ui.tabs.replaceChildren(...list.map((tab) => {
      const on = tab.id === st.tab;
      const label = tab.title || tab.url || t("br.blank");
      const pick = h("button", { type: "button", class: "br-tab" + (on ? " on" : ""), role: "tab", "aria-selected": String(on), title: tab.url || label }, label);
      pick.addEventListener("click", () => selectTab(tab.id));
      const close = h("button", { type: "button", class: "br-tab-close", "aria-label": t("br.closeTab"), title: t("br.closeTab") }, "×");
      close.addEventListener("click", async () => { await act(() => post("/api/browser/tab/close", { id: tab.id })); });
      return h("div", { class: "br-tab-wrap" }, pick, close);
    }), ui.addTab);
    const current = list.find((x) => x.id === st.tab);
    if (current && document.activeElement !== ui.address) ui.address.value = current.url === "about:blank" ? "" : current.url;
    if (current && document.activeElement !== ui.zoomRange) {
      const percent = Math.round((current.zoom || 1) * 100);
      ui.zoomRange.value = String(percent);
      ui.zoomLabel.textContent = `${percent}%`;
    }
  }

  // ------------------------------------------------------------ data
  async function reload() {
    const data = await api("/api/browser");
    st.data = data;
    if (!st.ui) st.ui = buildUi();
    const ui = st.ui;
    const ready = data.enabled && data.executable;
    ui.statusPill.textContent = !data.enabled ? t("br.state.off") : !data.executable ? t("br.state.nobrowser") : data.running ? t("br.state.running") : t("br.state.stopped");
    ui.power.textContent = data.running ? t("br.stop") : t("br.start");
    ui.power.hidden = !ready;
    ui.missing.hidden = ready;
    ui.missing.textContent = !data.enabled ? t("br.disabled") : t("br.nobrowser");
    ui.live.hidden = !data.running;
    if (data.running) {
      const ids = (data.tabs || []).map((x) => x.id);
      // a window the page opened itself (Sign in with Google, SSO) is shown at once; when it closes we return
      // to the tab the user came from
      const fresh = st.known ? ids.filter((id) => !st.known.has(id)) : [];
      st.known = new Set(ids);
      if (fresh.length) {
        if (st.tab && ids.includes(st.tab)) st.order.push(st.tab);
        st.tab = fresh[fresh.length - 1];
        restartStream();
        post("/api/browser/tab/activate", { id: st.tab }).catch(() => {});
      } else if (!ids.includes(st.tab)) {
        st.order = st.order.filter((id) => ids.includes(id));
        st.tab = st.order.length ? st.order.pop() : (ids[0] || null);
        restartStream();
      }
      renderTabs();
      ui.empty.hidden = !!st.tab;
      ui.empty.textContent = st.tab ? "" : t("br.notabs");
      startLoop();
    } else {
      st.tab = null;
      st.known = null;
      st.order = [];
    }
    renderCookies(data);
  }

  function renderCookies(data) {
    const body = cookies.body;
    const info = (data && data.cookies) || { count: 0, domains: [] };
    if (!data || !data.running) { body.replaceChildren(h("p", { class: "state" }, t("br.cookies.off"))); return; }
    const clearAll = h("button", { type: "button", class: "danger", disabled: !info.count }, t("br.clearAll"));
    clearAll.addEventListener("click", async () => {
      if (await confirmDialog({ title: t("br.clearAll"), text: t("br.clearAll.text"), confirm: t("br.clearAll"), danger: true }))
        act(() => post("/api/browser/cookies/clear", {}), t("br.cleared"));
    });
    const rows = info.domains.map((d) => {
      const rm = h("button", { type: "button", class: "ghost", "aria-label": t("br.remove", { d: d.domain }) }, t("br.removeShort"));
      rm.addEventListener("click", async () => {
        if (await confirmDialog({ title: t("br.remove", { d: d.domain }), text: t("br.remove.text", { d: d.domain }), confirm: t("br.removeShort"), danger: true }))
          act(() => post("/api/browser/cookies/clear", { domain: d.domain }), t("br.cleared"));
      });
      return h("li", { class: "row" }, h("span", { class: "row-main" }, d.domain), h("span", { class: "tag" }, num(d.count)), rm);
    });
    body.replaceChildren(
      h("p", null, t("br.cookies.total", { n: num(info.count), d: num(info.domains.length) })),
      rows.length ? h("ul", { class: "rows" }, rows) : h("p", { class: "state" }, t("br.cookies.none")),
      h("div", { class: "panel-actions" }, clearAll));
  }

  // ------------------------------------------------------------ websocket stream
  // One open connection: the server pushes a picture whenever the page changes, clicks, keys and zoom go back
  // without a request each. Older browsers or proxies that refuse it fall back to the long poll below.
  function watchNow() {
    if (!st.ws || st.ws.readyState !== 1) return;
    if (st.lastWatched !== st.tab && st.ui) {                 // another tab: do not leave the old picture under it
      const canvas = st.ui.canvas;
      canvas.getContext("2d").clearRect(0, 0, canvas.width, canvas.height);
      st.lastWatched = st.tab;
    }
    st.reqGen = (st.reqGen + 1) & 0xFFFF;
    st.seq = 0;
    st.ws.send(JSON.stringify({ op: "watch", id: st.tab, profile: st.profile, gen: st.reqGen }));
  }

  async function decodeFrames(canvas) {
    st.decoding = true;
    const ctx = canvas.getContext("2d");
    while (st.pending) {
      const buf = st.pending;
      st.pending = null;
      try {
        const bmp = await createImageBitmap(new Blob([buf], { type: "image/jpeg" }));
        if (canvas.width !== bmp.width || canvas.height !== bmp.height) { canvas.width = bmp.width; canvas.height = bmp.height; }
        ctx.drawImage(bmp, 0, 0);
        if (bmp.close) bmp.close();
      } catch { /* a broken frame is skipped, the next one repaints */ }
    }
    st.decoding = false;
  }

  function onSocketMessage(data) {
    const canvas = st.ui && st.ui.canvas;
    if (!canvas) return;
    if (typeof data === "string") {
      let msg = null;
      try { msg = JSON.parse(data); } catch { return; }
      if (msg.op === "zoom" && typeof msg.zoom === "number") {
        st.zoom = msg.zoom;
        const tab = ((st.data && st.data.tabs) || []).find((x) => x.id === msg.id);
        if (tab) tab.zoom = msg.zoom;
      } else if (msg.op === "error") {
        if (msg.code === "not_running") { reload().catch(() => {}); return; }
        if (Date.now() - st.lastErr > 3000) {
          st.lastErr = Date.now();
          const text = t(`br.err.${msg.code}`);
          if (text && !text.startsWith("br.err.")) toast(text, "error");
        }
      }
      return;
    }
    const view = new DataView(data);
    if (data.byteLength < 11 || view.getUint16(0) !== st.reqGen) return;            // a picture of an older view
    st.vw = view.getUint16(2);
    st.vh = view.getUint16(4);
    st.seq = view.getUint32(6);
    st.pending = data.slice(10);
    if (!st.decoding) decodeFrames(canvas);
  }

  function ensureSocket() {
    if (st.ws || !st.ui || !st.data || !st.data.running) return;
    const ui = st.ui;
    const ws = new WebSocket(`${window.location.protocol === "https:" ? "wss" : "ws"}://${window.location.host}/api/browser/ws`);
    ws.binaryType = "arraybuffer";
    st.ws = ws;
    let opened = false;
    ws.onopen = () => {
      opened = true;
      st.wsFails = 0;
      ws.send(JSON.stringify({ op: "hello", csrf: getCsrf() }));
      if (st.tab) watchNow();
    };
    ws.onmessage = (ev) => onSocketMessage(ev.data);
    ws.onerror = () => { /* onclose follows */ };
    ws.onclose = (ev) => {
      if (st.ws === ws) st.ws = null;
      if (!ui.canvas.isConnected || !st.data || !st.data.running || document.hidden) return;
      if (ev && ev.code >= 4400) { st.useLongPoll = true; startLoop(); return; }     // refused: use plain requests
      if (!opened && ++st.wsFails >= 3) { st.useLongPoll = true; startLoop(); return; }
      setTimeout(ensureSocket, Math.min(5000, 400 * (st.wsFails + 1)));
    };
    if (!st.watcher) {                                      // leaving the section closes the stream
      st.watcher = setInterval(() => {
        if (st.ws && !ui.canvas.isConnected) st.ws.close();
        if (st.ws && document.hidden) st.ws.close();
      }, 4000);
    }
  }

  // ------------------------------------------------------------ frame loop (fallback)
  // Long poll: the server answers when the picture changed (204 after a few quiet seconds), so a still page
  // costs nothing and a change shows up as soon as the browser paints it.
  function startLoop() {
    if (!st.useLongPoll) { ensureSocket(); return; }
    if (st.running) return;
    st.running = true;
    const canvas = st.ui.canvas;
    const ctx = canvas.getContext("2d");
    const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
    (async () => {
      let fails = 0;
      while (canvas.isConnected && st.data && st.data.running) {
        if (document.hidden || !st.tab || document.getElementById("dialog").open) { await sleep(400); continue; }
        const tab = st.tab;
        st.abort = new AbortController();
        try {
          const res = await fetch(`/api/browser/screen?id=${encodeURIComponent(tab)}&since=${st.seq}&profile=${st.profile}`,
            { cache: "no-store", credentials: "same-origin", signal: st.abort.signal });
          if (res.status === 401) { window.location.replace("/login"); return; }
          if (tab !== st.tab) continue;
          if (res.status === 204) { fails = 0; continue; }
          if (!res.ok) throw new Error(String(res.status));
          const bmp = await createImageBitmap(await res.blob());
          if (tab !== st.tab) { if (bmp.close) bmp.close(); continue; }
          st.seq = Number(res.headers.get("X-Frame-Seq")) || 0;
          st.vw = Number(res.headers.get("X-Viewport-Width")) || st.vw;
          st.vh = Number(res.headers.get("X-Viewport-Height")) || st.vh;
          if (canvas.width !== bmp.width || canvas.height !== bmp.height) { canvas.width = bmp.width; canvas.height = bmp.height; }
          ctx.drawImage(bmp, 0, 0);
          if (bmp.close) bmp.close();
          fails = 0;
        } catch (err) {
          if (err && err.name === "AbortError") continue;
          fails += 1;
          if (fails >= MAX_FAILS) { fails = 0; reload().catch(() => {}); await sleep(3000); } else await sleep(400 * fails);
        }
      }
      st.running = false;
    })();
  }

  bindLoader(s, view, async () => { await reload(); });
  cookies.refreshBtn.addEventListener("click", () => reload().catch(() => {}));
  cookies.loaded = true;
  cookies.body.replaceChildren(h("p", { class: "state" }, t("common.loading")));
}
