// "Browser" section: a remote Chromium the admin logs into. The bot reads the live cookies
// of this session (/cookies_from_browser and the service buttons of /cookie).
// The page is shown as JPEG frames painted on a <canvas> (no blob:/inline needed by the CSP);
// clicks, wheel and keys are posted back. No innerHTML anywhere.
import { t } from "./i18n.js";
import { h, api, toast, errorText, confirmDialog, num, getCsrf } from "./ui.js";

const MAX_FAILS = 4;
// each service lives in its own tab: its start page and its robots.txt (a light page to leave the tab on) open there
const BOOKMARKS = [
  { name: "YouTube", home: "https://www.youtube.com/", robots: "https://www.youtube.com/robots.txt", hosts: ["youtube.com"] },
  { name: "X", home: "https://x.com/home", robots: "https://x.com/robots.txt", hosts: ["x.com", "twitter.com"] },
  { name: "Instagram", home: "https://www.instagram.com/", robots: "https://www.instagram.com/robots.txt", hosts: ["instagram.com"] },
  { name: "VK", home: "https://vk.ru/feed", robots: "https://vk.ru/robots.txt", hosts: ["vk.ru", "vk.com"] },
  { name: "TikTok", home: "https://www.tiktok.com/", robots: "https://www.tiktok.com/robots.txt", hosts: ["tiktok.com"] },
];
const PROFILES = ["fast", "normal", "sharp"];     // picture quality: fast = smallest frames, the default
const KA_STEPS = [[0, "br.ka.off"], [1800, "br.ka.30m"], [3600, "br.ka.1h"], [3 * 3600, "br.ka.3h"],
  [6 * 3600, "br.ka.6h"], [12 * 3600, "br.ka.12h"], [24 * 3600, "br.ka.24h"]];
const kaLabel = (sec) => { const hit = KA_STEPS.find(([v]) => v === sec); return (hit && t(hit[1])) || t("br.ka.custom", { h: Math.round(sec / 360) / 10 }); };

function brError(err) {
  const code = err && err.body && err.body.error;
  const text = code ? t(`br.err.${code}`) : null;
  return text && !text.startsWith("br.err.") ? text : errorText(err);
}

function post(path, body) { return api(path, { method: "POST", body: body || {}, timeout: 30000 }); }

export function buildBrowser(s, { panel, bindLoader }) {
  // the browser gets the whole width and almost all the height; one slim toolbar, like a remote desktop (neko)
  const viewBody = h("div", { class: "br-body" });
  const view = { el: h("section", { class: "panel br-panel", "aria-label": t("br.session") }, viewBody), body: viewBody };
  const cookies = panel({ title: t("br.cookies"), sub: t("br.cookies.sub"), span: "full" });
  s.root.append(view.el, h("div", { class: "grid br-below" }, cookies.el));

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
    const statusPill = h("span", { class: "br-dot", role: "status" });
    const power = h("button", { type: "button", class: "primary br-power" });
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
    // bookmarks: the service's own tab if it is open (switched to this page), else a blank tab, else a new tab
    const siteHost = (url) => { try { return new URL(url).hostname.replace(/^www\./, ""); } catch { return ""; } };
    const ofService = (svc, url) => { const host = siteHost(url); return !!host && svc.hosts.some((d) => host === d || host.endsWith(`.${d}`)); };
    const openBookmark = async (svc, url) => {
      const tabs = (st.data && st.data.tabs) || [];
      const same = tabs.find((x) => x.id === st.tab && ofService(svc, x.url)) || tabs.find((x) => ofService(svc, x.url));
      if (same) {
        if (same.id !== st.tab) await selectTab(same.id);
        if (same.url.replace(/\/$/, "") !== url.replace(/\/$/, "")) act(() => post("/api/browser/navigate", { id: same.id, url }));
        return;
      }
      const current = tabs.find((x) => x.id === st.tab);
      if (current && (!current.url || current.url === "about:blank")) { act(() => post("/api/browser/navigate", { id: st.tab, url })); return; }
      const created = await act(() => post("/api/browser/tab", { url }));
      if (created && created.id) await selectTab(created.id);
    };
    const bookmarks = h("div", { class: "br-bookmarks", role: "group", "aria-label": t("br.bookmarks") },
      BOOKMARKS.map((svc) => h("div", { class: "br-bm" },
        h("button", { type: "button", class: "br-bm-home", title: svc.home, onclick: () => openBookmark(svc, svc.home) }, svc.name),
        h("button", { type: "button", class: "br-bm-robots", title: `${svc.robots} — ${t("br.robots.title")}`,
          "aria-label": `${svc.name} robots.txt`, onclick: () => openBookmark(svc, svc.robots) }, "robots"))));
    const address = h("input", { type: "text", class: "br-address", inputmode: "url", autocomplete: "off", spellcheck: "false",
      autocapitalize: "off", "aria-label": t("br.address"), placeholder: t("br.address.ph") });
    const bar = h("form", { class: "br-toolbar", novalidate: true },
      nav("back", t("br.back"), "←"), nav("forward", t("br.forward"), "→"), nav("reload", t("br.reload"), "↻"), address);
    bar.addEventListener("submit", async (e) => {
      e.preventDefault();
      const url = address.value.trim();
      if (!url) return;
      if (!st.tab) { const r = await act(() => post("/api/browser/tab", { url })); if (r && r.id) await selectTab(r.id); return; }
      act(() => post("/api/browser/navigate", { id: st.tab, url }));
    });

    const canvas = h("canvas", { class: "br-canvas", width: 1280, height: 800, tabindex: 0, role: "application",
      "aria-label": t("br.screen"), title: t("br.help") });
    // page zoom (zoom out = more of the page fits) and picture quality
    const zoomLabel = h("output", { class: "br-zoom-label", "aria-live": "polite" }, "100%");
    const zoomRange = h("input", { type: "range", class: "br-zoom-range", min: 50, max: 200, step: 10, value: 100, "aria-label": t("br.zoom"), title: t("br.zoom") });
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
    // how often each resting tab is woken to refresh its login cookies
    const keepalive = h("select", { class: "br-quality br-ka", "aria-label": t("br.ka"), title: t("br.ka.title") },
      KA_STEPS.map(([v, key]) => h("option", { value: String(v) }, t(key))));
    keepalive.addEventListener("change", async () => {
      try { const r = await post("/api/browser/keepalive", { seconds: Number(keepalive.value) }); toast(t("br.ka.apply", { v: r.seconds ? kaLabel(r.seconds) : t("br.ka.off") }), "ok"); }
      catch (err) { toast(brError(err), "error"); }
    });
    zoomLabel.title = t("br.zoomReset");
    zoomLabel.addEventListener("click", () => applyZoom(100));
    const zoomBar = h("div", { class: "br-zoombar", role: "group", "aria-label": t("br.zoom") },
      stepBtn(t("br.zoomOut"), "−", -10), zoomRange, stepBtn(t("br.zoomIn"), "+", 10), zoomLabel, quality, keepalive);
    const empty = h("p", { class: "state br-empty" });
    const screen = h("div", { class: "br-screen" }, canvas, empty);

    // mouse
    // the picture is scaled down; clicks are sent in page pixels (the viewport size the server reports)
    // the canvas fills the screen area and the picture is letterboxed inside it (object-fit: contain)
    const point = (e) => {
      const r = canvas.getBoundingClientRect();
      const scale = Math.min(r.width / canvas.width, r.height / canvas.height) || 1;
      const w = canvas.width * scale;
      const hgt = canvas.height * scale;
      const x = (e.clientX - r.left - (r.width - w) / 2) / w;
      const y = (e.clientY - r.top - (r.height - hgt) / 2) / hgt;
      return { x: Math.round(Math.max(0, Math.min(1, x)) * st.vw), y: Math.round(Math.max(0, Math.min(1, y)) * st.vh) };
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
    const keyBtn = (key, label) => h("button", { type: "button", class: "br-chip", onclick: () => sendInput({ kind: "key", key }) }, label);
    const keys = h("div", { class: "br-keys", hidden: true }, textInput,
      h("button", { type: "button", class: "br-chip", onclick: sendText }, t("br.send")),
      keyBtn("Tab", "Tab"), keyBtn("Enter", "Enter"), keyBtn("Backspace", "⌫"), keyBtn("Escape", "Esc"));
    // extra keys and a text box (passwords from a manager, IME): out of the way until asked for
    const kbd = h("button", { type: "button", class: "ghost icon-btn", "aria-pressed": "false", "aria-label": t("br.keyboard"), title: t("br.keyboard") }, "⌨");
    kbd.addEventListener("click", () => {
      keys.hidden = !keys.hidden;
      kbd.setAttribute("aria-pressed", String(!keys.hidden));
      if (!keys.hidden) textInput.focus();
    });
    const full = h("button", { type: "button", class: "ghost icon-btn", "aria-label": t("br.fullscreen"), title: t("br.fullscreen") }, "⛶");
    full.addEventListener("click", () => {
      if (document.fullscreenElement) document.exitFullscreen().catch(() => {});
      else if (view.el.requestFullscreen) view.el.requestFullscreen().catch(() => {});
    });

    const missing = h("div", { class: "state" });
    const controls = h("div", { class: "br-controls" }, bar, bookmarks, zoomBar, kbd, full);
    const live = h("div", { class: "br-live" }, tabs, screen, keys);
    const top = h("div", { class: "br-top" }, statusPill, power, controls);
    view.body.replaceChildren(top, missing, live);
    return { statusPill, power, controls, tabs, addTab, address, canvas, empty, live, missing, zoomRange, zoomLabel, keepalive };
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
    const state = !data.enabled ? t("br.state.off") : !data.executable ? t("br.state.nobrowser")
      : data.running ? t("br.state.running") : data.busy ? t("br.state.busy") : t("br.state.stopped");
    ui.statusPill.title = state;
    ui.statusPill.setAttribute("aria-label", state);
    ui.statusPill.classList.toggle("on", !!data.running);
    // running: a small power icon; stopped: the one button there is to press; busy: it comes back on its own
    ui.power.textContent = data.running ? "⏻" : t("br.start");
    ui.power.title = data.running ? t("br.stop") : t("br.start");
    ui.power.hidden = !ready || !!data.busy;
    ui.power.setAttribute("aria-label", ui.power.title);
    ui.power.classList.toggle("icon-btn", !!data.running);
    if (ui.keepalive && data.keepalive !== undefined && document.activeElement !== ui.keepalive) {
      ui.keepalive.value = String(data.keepalive);
      if (!ui.keepalive.selectedOptions.length) ui.keepalive.value = "";     // a value between the offered steps
      ui.keepalive.title = data.keepalive ? `${t("br.ka.title")} ${kaLabel(data.keepalive)}` : t("br.ka.off");
    }

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
    const clearAll = h("button", { type: "button", class: "br-ck-clear", disabled: !info.count }, t("br.clearAll"));
    clearAll.addEventListener("click", async () => {
      if (await confirmDialog({ title: t("br.clearAll"), text: t("br.clearAll.text"), confirm: t("br.clearAll"), danger: true }))
        act(() => post("/api/browser/cookies/clear", {}), t("br.cleared"));
    });
    // compact grid: domain, count, a mark when the bot takes it, × to delete
    const rows = [...info.domains].sort((a, b) => (b.shared ? 1 : 0) - (a.shared ? 1 : 0) || a.domain.localeCompare(b.domain)).map((d) => {
      const rm = h("button", { type: "button", class: "br-ck-rm", "aria-label": t("br.remove", { d: d.domain }), title: t("br.remove", { d: d.domain }) }, "×");
      rm.addEventListener("click", async () => {
        if (await confirmDialog({ title: t("br.remove", { d: d.domain }), text: t("br.remove.text", { d: d.domain }), confirm: t("br.removeShort"), danger: true }))
          act(() => post("/api/browser/cookies/clear", { domain: d.domain }), t("br.cleared"));
      });
      return h("li", { class: "br-ck" + (d.shared ? " bot" : ""), title: d.shared ? t("br.shared") : "" },
        h("span", { class: "br-ck-dom" }, d.domain), h("span", { class: "br-ck-n" }, num(d.count)), rm);
    });
    body.replaceChildren(
      h("div", { class: "br-ck-head" },
        h("span", null, t("br.cookies.total", { n: num(info.count), d: num(info.domains.length) })),
        h("span", { class: "br-ck-legend" }, h("span", { class: "br-ck-mark", "aria-hidden": "true" }), t("br.shared")), clearAll),
      rows.length ? h("ul", { class: "br-ck-grid" }, rows) : h("p", { class: "state" }, t("br.cookies.none")));
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

  // the browser area has no panel chrome of its own: the cookies panel carries the refresh button and the error state
  cookies.loaded = true;
  cookies.body.replaceChildren(h("p", { class: "state" }, t("common.loading")));
  bindLoader(s, cookies, async () => { await reload(); });
}
