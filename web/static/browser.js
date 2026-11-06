// "Browser" section: a remote Chromium the admin logs into. The bot reads the live cookies
// of this session (/cookies_from_browser and the service buttons of /cookie).
// The page is shown as JPEG frames painted on a <canvas> (no blob:/inline needed by the CSP);
// clicks, wheel and keys are posted back. No innerHTML anywhere.
import { t } from "./i18n.js";
import { h, api, toast, errorText, confirmDialog, num } from "./ui.js";

const FRAME_MS = 700;      // pause between frames while idle
const FAST_MS = 120;       // pause right after an input
const MAX_FAILS = 4;

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

  const st = { data: null, tab: null, ui: null, loop: 0, fails: 0, queue: Promise.resolve(), wake: null, wheel: 0 };

  // ------------------------------------------------------------ actions
  const act = async (fn, okText) => {
    try { const r = await fn(); if (okText) toast(okText, "ok"); await reload(); return r; }
    catch (err) { toast(brError(err), "error"); return null; }
  };

  const sendInput = (body) => {
    if (!st.tab) return;
    const payload = { id: st.tab, ...body };
    st.queue = st.queue.then(() => post("/api/browser/input", payload)).catch((err) => toast(brError(err), "error"))
      .then(() => { if (st.wake) st.wake(FAST_MS); });
  };

  const selectTab = async (id) => {
    st.tab = id;
    renderTabs();
    try { await post("/api/browser/tab/activate", { id }); } catch { /* the frame loop reports real problems */ }
    if (st.wake) st.wake(0);
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
    const empty = h("p", { class: "state br-empty" });
    const screen = h("div", { class: "br-screen" }, canvas, empty);

    // mouse
    const point = (e) => {
      const r = canvas.getBoundingClientRect();
      return { x: Math.round(((e.clientX - r.left) / r.width) * canvas.width), y: Math.round(((e.clientY - r.top) / r.height) * canvas.height) };
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
    const live = h("div", { class: "br-live" }, tabs, bar, screen, keys, help);

    const top = h("div", { class: "br-top" }, statusPill, power);
    view.body.replaceChildren(top, missing, live);
    return { statusPill, power, tabs, addTab, address, canvas, empty, live, missing };
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
      if (!(data.tabs || []).some((x) => x.id === st.tab)) st.tab = data.tabs && data.tabs[0] ? data.tabs[0].id : null;
      renderTabs();
      ui.empty.hidden = !!st.tab;
      ui.empty.textContent = st.tab ? "" : t("br.notabs");
      startLoop();
    } else {
      st.tab = null;
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

  // ------------------------------------------------------------ frame loop
  function startLoop() {
    if (st.wake) { st.wake(0); return; }               // already running: just ask for a frame now
    const my = ++st.loop;
    const canvas = st.ui.canvas;
    const ctx = canvas.getContext("2d");
    const sleep = (ms) => new Promise((resolve) => { const timer = setTimeout(resolve, ms); st.wake = (next) => { clearTimeout(timer); setTimeout(resolve, next); }; });
    (async () => {
      let delay = 0;
      while (my === st.loop) {
        await sleep(delay);
        delay = FRAME_MS;
        if (!canvas.isConnected || !st.data || !st.data.running) break;      // other section / stopped
        if (document.hidden || !st.tab || document.getElementById("dialog").open) continue;
        try {
          const res = await fetch(`/api/browser/screen?id=${encodeURIComponent(st.tab)}`, { cache: "no-store", credentials: "same-origin" });
          if (res.status === 401) { window.location.replace("/login"); return; }
          if (!res.ok) throw new Error(String(res.status));
          const bmp = await createImageBitmap(await res.blob());
          if (canvas.width !== bmp.width || canvas.height !== bmp.height) { canvas.width = bmp.width; canvas.height = bmp.height; }
          ctx.drawImage(bmp, 0, 0);
          if (bmp.close) bmp.close();
          st.fails = 0;
        } catch {
          if (++st.fails >= MAX_FAILS) { st.fails = 0; reload().catch(() => {}); delay = 3000; }
        }
      }
      if (my === st.loop) st.wake = null;
    })();
  }

  bindLoader(s, view, async () => { await reload(); });
  cookies.refreshBtn.addEventListener("click", () => reload().catch(() => {}));
  cookies.loaded = true;
  cookies.body.replaceChildren(h("p", { class: "state" }, t("common.loading")));
}
