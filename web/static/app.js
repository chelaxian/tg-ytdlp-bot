import { t, getLang, setLang, translateStatic, settingLabel } from "./i18n.js";
import {
  h, clear, api, setCsrf, errorText, toast, openDialog, closeDialog, initDialog, confirmDialog,
  num, duration, ago, dateTime, bytes, debounce, userName, userLink, matches,
} from "./ui.js";
import { buildBrowser } from "./browser.js";

const state = { section: null, session: null, timers: [], bot: null, built: new Map() };

// ================================================================= building blocks

/** A titled block with loading / error / empty states and a "data age" stamp. */
function panel({ title, sub, tools = [], span = 1, flush = false }) {
  const body = h("div", { class: "panel-body" + (flush ? " flush" : "") });
  const stamp = h("span", { class: "stamp" });
  const refreshBtn = h("button", { type: "button", class: "icon-btn", "aria-label": t("common.refresh"), title: t("common.refresh") }, "↻");
  const el = h("section", { class: `panel span-${span}` },
    h("header", { class: "panel-head" },
      h("div", { class: "panel-titles" }, h("h2", null, title), sub ? h("p", { class: "panel-sub" }, sub) : null),
      h("div", { class: "panel-tools" }, tools, refreshBtn)),
    body,
    h("footer", { class: "panel-foot" }, stamp));
  const p = {
    el, body, stamp, refreshBtn, loaded: false,
    loading() { if (!p.loaded) body.replaceChildren(h("div", { class: "skeleton" }, h("span"), h("span"), h("span"))); el.setAttribute("aria-busy", "true"); },
    done() { p.loaded = true; el.removeAttribute("aria-busy"); stamp.textContent = t("common.updated", { age: t("common.now") }); stamp.dataset.ts = String(Date.now() / 1000); },
    error(err, retry) {
      el.removeAttribute("aria-busy");
      body.replaceChildren(h("div", { class: "state state-error", role: "alert" },
        h("p", null, errorText(err)), retry ? h("button", { type: "button", class: "ghost", onclick: retry }, t("common.retry")) : null));
      p.loaded = false;
    },
    empty(text) { body.replaceChildren(h("p", { class: "state" }, text || t("common.empty"))); },
  };
  return p;
}

/** Runs `load(panel)` with states; the panel's refresh button calls it too. */
function bindLoader(section, p, load) {
  const run = async () => {
    p.loading();
    try { await load(p); p.done(); } catch (err) { if (err.status !== 401) p.error(err, run); }
  };
  p.refreshBtn.addEventListener("click", run);
  section.loaders.push(run);
  return run;
}

function select(options, value, onChange, label) {
  const el = h("select", { "aria-label": label },
    options.map(([v, text]) => h("option", { value: v, selected: String(v) === String(value) }, text)));
  el.addEventListener("change", () => onChange(el.value));
  return el;
}

const periodOptions = () => ["today", "week", "month", "all"].map((p) => [p, t(`period.${p}`)]);
function periodSelect(value, onChange) { return select(periodOptions(), value, onChange, t("common.period")); }

function searchBox(onInput, placeholder) {
  const input = h("input", { type: "search", placeholder: placeholder || t("common.search.users"), "aria-label": t("common.search"), autocomplete: "off", spellcheck: "false" });
  input.addEventListener("input", debounce(() => onInput(input.value), 150));
  return input;
}

/** A searchable list of users with one metric each and per-row actions. */
function userList(p, { metric, sub, unblock = false, limit = 10 }) {
  let items = [];
  let query = "";
  let expanded = false;
  const list = h("ul", { class: "rows" });
  const more = h("button", { type: "button", class: "link-btn" });
  const search = searchBox((q) => { query = q; render(); });
  more.addEventListener("click", () => { expanded = !expanded; render(); });
  p.body.replaceChildren(h("div", { class: "list-tools" }, search), list, more);

  function render() {
    const filtered = items.filter((u) => matches(u, query));
    const shown = expanded || query ? filtered.slice(0, 500) : filtered.slice(0, limit);
    list.replaceChildren(...shown.map((u) => userRow(u, { metric, sub, unblock })));
    if (!filtered.length) list.replaceChildren(h("li", { class: "state" }, t("common.empty")));
    more.hidden = query || filtered.length <= limit;
    more.textContent = expanded ? t("common.showLess") : t("common.showAll", { n: num(filtered.length) });
  }
  return {
    set(next) {
      items = Array.isArray(next) ? next : [];
      if (!p.body.contains(list)) p.body.replaceChildren(h("div", { class: "list-tools" }, search), list, more);
      render();
    },
  };
}

function userRow(u, { metric, sub, unblock }) {
  const link = userLink(u);
  const name = h("span", { class: "row-name" }, userName(u));
  const who = h("div", { class: "row-main" },
    h("div", { class: "row-title" },
      u.flag && u.flag !== "🏳" ? h("span", { class: "flag", "aria-hidden": "true" }, u.flag) : null,
      link ? h("a", { href: link, target: "_blank", rel: "noopener noreferrer", title: t("user.open") }, name) : name),
    h("div", { class: "row-sub" },
      u.username ? h("span", null, `@${u.username}`) : null,
      h("span", { class: "mono-id" }, String(u.user_id || "")),
      sub ? sub(u) : null));
  const actions = h("div", { class: "row-actions" },
    h("button", { type: "button", class: "icon-btn", title: t("user.history"), "aria-label": `${t("user.history")}: ${userName(u)}`, onclick: () => openHistory(u) }, "☰"),
    unblock
      ? h("button", { type: "button", class: "icon-btn ok", title: t("user.unblock"), "aria-label": `${t("user.unblock")}: ${userName(u)}`, onclick: () => unblockUser(u) }, "↺")
      : h("button", { type: "button", class: "icon-btn danger", title: t("user.block"), "aria-label": `${t("user.block")}: ${userName(u)}`, onclick: () => blockUser(u) }, "⦸"));
  return h("li", { class: "row" }, who, metric ? h("span", { class: "metric" }, metric(u)) : null, actions);
}

/** Label / count bars (countries, gender, age, joins, domains). */
function barList(p, rows, { label, filter = "" }) {
  const shown = rows.filter((r) => !filter || String(label(r)).toLowerCase().includes(filter.toLowerCase()));
  if (!shown.length) return p.empty();
  const max = Math.max(1, ...shown.map((r) => Number(r.count) || 0));
  p.body.replaceChildren(h("ul", { class: "bars" }, shown.slice(0, 100).map((r) =>
    h("li", { class: "bar" },
      h("span", { class: "bar-label" }, label(r)),
      h("meter", { min: 0, max, value: Number(r.count) || 0, "aria-hidden": "true" }),
      h("span", { class: "bar-value" }, num(r.count))))));
}

// ================================================================= user actions

async function blockUser(u) {
  const ok = await confirmDialog({ title: t("confirm.block.title"), text: t("confirm.block.text", { name: userName(u) }), confirm: t("user.block"), danger: true });
  if (!ok) return;
  try { await api("/api/block-user", { method: "POST", body: { user_id: Number(u.user_id) } }); toast(t("toast.blocked"), "ok"); refreshSection(); }
  catch (err) { toast(errorText(err), "error"); }
}

async function unblockUser(u) {
  const ok = await confirmDialog({ title: t("confirm.unblock.title"), text: t("confirm.unblock.text", { name: userName(u) }), confirm: t("user.unblock") });
  if (!ok) return;
  try { await api("/api/unblock-user", { method: "POST", body: { user_id: Number(u.user_id) } }); toast(t("toast.unblocked"), "ok"); refreshSection(); }
  catch (err) { toast(errorText(err), "error"); }
}

const META_KEYS = ["progress", "downloaded", "size", "speed", "eta", "duration", "resolution", "quality", "ext", "domain"];

function detailsList(pairs) {
  return h("dl", { class: "facts" }, pairs.filter(([, v]) => v !== null && v !== undefined && v !== "").map(([k, v]) =>
    h("div", null, h("dt", null, k), h("dd", null, v))));
}

function openUser(u) {
  const meta = u.metadata || {};
  const pairs = [
    [t("meta.last"), u.last_event_ts ? `${dateTime(u.last_event_ts)} · ${ago(u.last_event_ts)}` : null],
    [t("meta.first"), u.first_seen_ts ? dateTime(u.first_seen_ts) : null],
    [t("meta.country"), u.country_code ? `${u.flag || ""} ${u.country_code}` : null],
    [t("meta.title"), u.title || null],
    [t("meta.url"), u.url ? h("a", { href: u.url, target: "_blank", rel: "noopener noreferrer" }, u.url) : null],
    ...META_KEYS.map((k) => [t(`meta.${k}`), k === "progress" && u.progress !== null && u.progress !== undefined ? `${Math.round(u.progress)}%` : meta[k] !== undefined ? String(meta[k]) : null]),
  ];
  openDialog({
    title: userName(u),
    body: [h("p", { class: "muted" }, u.username ? `@${u.username} · ` : "", t("user.id", { id: u.user_id })), detailsList(pairs)],
    actions: [
      h("button", { type: "button", class: "ghost", onclick: () => openHistory(u) }, t("user.history")),
      h("button", { type: "button", class: "danger", onclick: () => { closeDialog(); blockUser(u); } }, t("user.block")),
    ],
  });
}

async function openHistory(u) {
  const list = h("ul", { class: "history" });
  const count = h("p", { class: "muted", "aria-live": "polite" });
  let period = "all"; let query = ""; let items = []; let limit = 200;
  const more = h("button", { type: "button", class: "link-btn", onclick: () => { limit += 300; render(); } });
  const bounds = { today: 86400, week: 7 * 86400, month: 30 * 86400 };
  function render() {
    const now = Date.now() / 1000;
    const filtered = items.filter((it) => (period === "all" || it.timestamp >= now - bounds[period]) && (!query || matches(it, query) || (it.url || "").toLowerCase().includes(query.toLowerCase())));
    list.replaceChildren(...filtered.slice(0, limit).map((it) => h("li", null,
      h("div", { class: "history-main" },
        h("span", { class: "history-title" }, it.title || it.url || "—"),
        it.url ? h("a", { href: it.url, target: "_blank", rel: "noopener noreferrer", class: "history-url" }, it.url) : null),
      h("div", { class: "history-side" },
        h("span", null, dateTime(it.timestamp)),
        h("span", { class: "muted" }, it.domain || ""),
        it.is_nsfw ? h("span", { class: "tag warn" }, t("hist.badge.nsfw")) : null,
        it.is_playlist ? h("span", { class: "tag" }, t("hist.badge.playlist")) : null))));
    if (!filtered.length) list.replaceChildren(h("li", { class: "state" }, t("hist.empty")));
    count.textContent = t("hist.items", { shown: num(Math.min(limit, filtered.length)), total: num(filtered.length) });
    more.hidden = filtered.length <= limit;
    more.textContent = t("common.showAll", { n: num(filtered.length) });
  }
  const tools = h("div", { class: "list-tools" },
    searchBox((q) => { query = q; limit = 200; render(); }, t("hist.filter")),
    periodSelect(period, (v) => { period = v; limit = 200; render(); }));
  openDialog({ title: `${t("hist.title")}: ${userName(u)}`, wide: true, body: [tools, count, h("div", { class: "skeleton" }, h("span"), h("span"))] });
  try {
    items = await api(`/api/user-history?user_id=${encodeURIComponent(u.user_id)}&period=all&limit=2000`);
    const dialog = document.getElementById("dialog");
    const body = dialog.querySelector(".dialog-body");
    if (!body) return;
    body.replaceChildren(tools, count, list, more);
    render();
  } catch (err) {
    const body = document.querySelector("#dialog .dialog-body");
    if (body) body.replaceChildren(h("p", { class: "state state-error" }, errorText(err)));
  }
}

// ================================================================= jobs

const JOB_KINDS = ["restart-bot", "restart-panel", "update-engines", "update-lists"];

async function startJob(path, body, name) {
  try {
    const res = await api(path, { method: "POST", body: body || {} });
    toast(t("job.started", { name }), "info");
    watchJob(res.job.id, name);
    refreshSection();
    return res.job;
  } catch (err) {
    toast(err.body && err.body.error === "need_urls" ? t("lists.text") : errorText(err), "error");
    return null;
  }
}

function watchJob(id, name) {
  const tick = async () => {
    try {
      const job = await api(`/api/jobs/${id}`);
      if (job.state === "running" || job.state === "waiting") { setTimeout(tick, 2000); return; }
      toast(`${name}: ${t(`job.${job.state}`)}${job.message && job.state !== "succeeded" ? ` — ${job.message}` : ""}`, job.state === "succeeded" ? "ok" : "error", 6000);
      refreshSection();
    } catch (err) {
      if (err.status === 0) setTimeout(tick, 3000);
    }
  };
  setTimeout(tick, 1500);
}

function jobList(container, jobs, { compact = false } = {}) {
  if (!jobs.length) { container.replaceChildren(h("p", { class: "state" }, t(compact ? "ov.jobs.empty" : "sys.jobs.empty"))); return; }
  container.replaceChildren(h("ul", { class: "jobs" }, jobs.slice(0, compact ? 4 : 20).map((job) => {
    const name = JOB_KINDS.includes(job.kind) ? t(`job.kind.${job.kind}`) : job.kind;
    const row = h("li", { class: `job job-${job.state}` },
      h("div", { class: "job-head" },
        h("span", { class: "job-name" }, name, job.params && job.params.mode === "idle" ? ` · ${t("restart.idle").toLowerCase()}` : ""),
        h("span", { class: `pill pill-${job.state}` }, t(`job.${job.state}`)),
        h("span", { class: "muted" }, ago(job.started))),
      job.message && job.state !== "succeeded" ? h("p", { class: "muted" }, job.message) : null);
    if (job.cancellable) row.append(h("button", { type: "button", class: "ghost small", onclick: async () => { await api(`/api/jobs/${job.id}/cancel`, { method: "POST" }).catch((e) => toast(errorText(e), "error")); refreshSection(); } }, t("job.cancel")));
    if (!compact && job.output && job.output.length) {
      row.append(h("details", null, h("summary", null, t("job.output")), h("pre", { class: "output" }, job.output.join("\n"))));
    }
    return row;
  })));
}

async function restartBotDialog() {
  let bot = {};
  try { bot = (await api("/api/overview")).bot || {}; } catch { /* shown as unknown */ }
  const running = Number(bot.running || 0); const queued = Number(bot.queued || 0);
  const text = !bot.alive ? t("restart.text.unknown") : running + queued === 0 ? t("restart.text.idle") : t("restart.text", { running, queued });
  const go = (mode) => { closeDialog(); startJob("/api/jobs/restart-bot", { mode }, t("job.kind.restart-bot")); };
  openDialog({
    title: t("restart.title"),
    body: h("p", null, text),
    actions: [
      h("button", { type: "button", class: "ghost", onclick: () => closeDialog() }, t("common.cancel")),
      h("button", { type: "button", class: running + queued > 0 ? "primary" : "ghost", onclick: () => go("idle") }, t("restart.idle")),
      h("button", { type: "button", class: running + queued > 0 ? "danger" : "primary", onclick: () => go("now") }, t("restart.now")),
    ],
  });
}

async function restartPanel() {
  const ok = await confirmDialog({ title: t("restart.panel.title"), text: t("restart.panel.text"), confirm: t("sys.restartPanel") });
  if (!ok) return;
  try { await api("/api/jobs/restart-panel", { method: "POST", body: {} }); } catch (err) { toast(errorText(err), "error"); return; }
  toast(t("restart.panel.text"), "info", 8000);
  let wentDown = false; let tries = 0;
  const poll = async () => {
    tries += 1;
    try {
      const res = await fetch("/health", { cache: "no-store" });
      if (res.ok && (wentDown || tries > 6)) { toast(t("job.panelBack"), "ok"); setTimeout(() => window.location.reload(), 600); return; }
      if (!res.ok) wentDown = true;
    } catch { wentDown = true; }
    if (tries < 60) setTimeout(poll, 1000);
  };
  setTimeout(poll, 1500);
}

async function updateEngines() {
  const ok = await confirmDialog({ title: t("engines.title"), text: t("engines.text"), confirm: t("sys.updateEngines") });
  if (ok) startJob("/api/jobs/update-engines", {}, t("job.kind.update-engines"));
}

async function updateListsDialog(canRunScript) {
  const domains = h("input", { type: "url", inputmode: "url", placeholder: "https://…/porn_domains.txt", autocomplete: "off", spellcheck: "false" });
  const words = h("input", { type: "url", inputmode: "url", placeholder: "https://…/porn_keywords.txt", autocomplete: "off", spellcheck: "false" });
  const run = () => {
    const body = { porn_domains: domains.value.trim(), porn_keywords: words.value.trim() };
    if (!canRunScript && !body.porn_domains && !body.porn_keywords) { domains.focus(); return; }
    closeDialog();
    startJob("/api/jobs/update-lists", body, t("job.kind.update-lists"));
  };
  openDialog({
    title: t("lists.title"),
    body: [
      h("p", null, canRunScript ? t("lists.text.script") : t("lists.text")),
      h("label", { class: "field" }, h("span", null, t("lists.domainsUrl")), domains),
      h("label", { class: "field" }, h("span", null, t("lists.keywordsUrl")), words),
    ],
    actions: [h("button", { type: "button", class: "ghost", onclick: () => closeDialog() }, t("common.cancel")),
      h("button", { type: "button", class: "primary", onclick: run }, t("lists.run"))],
  });
}

// ================================================================= sections

function grid(...panels) { return h("div", { class: "grid" }, panels.map((p) => p.el)); }

const SECTIONS = [
  { id: "overview", every: 5, build: buildOverview },
  { id: "activity", every: 10, build: buildActivity },
  { id: "users", every: 60, build: buildUsers },
  { id: "content", every: 60, build: buildContent },
  { id: "moderation", every: 30, build: buildModeration },
  { id: "history", every: 0, build: buildHistory },
  { id: "system", every: 5, build: buildSystem },
  { id: "settings", every: 0, build: buildSettings },
  { id: "lists", every: 0, build: buildLists },
  { id: "browser", every: 3, build: (s) => buildBrowser(s, { panel, bindLoader }) },
];

function buildOverview(s) {
  const kpis = h("div", { class: "counters", role: "list" });
  const counter = (key) => {
    const value = h("span", { class: "counter-value" }, "—");
    kpis.append(h("div", { class: "counter", role: "listitem" }, value, h("span", { class: "counter-label" }, t(key))));
    return value;
  };
  const c = { downloads_today: counter("ov.downloads"), downloads_week: counter("ov.week"), users_today: counter("ov.users"),
    active_15m: counter("ov.active"), blocked_total: counter("ov.blocked") };
  const age = h("p", { class: "muted data-age" });

  const live = panel({ title: t("ov.live"), span: 2, flush: true });
  live.el.classList.add("live");
  const bot = panel({ title: t("ov.bot") });
  const recent = panel({ title: t("ov.jobs") });

  s.root.append(h("div", { class: "hero" }, kpis, age), grid(live, bot, recent));

  bindLoader(s, bot, async (p) => {
    const data = await api("/api/overview");
    const st = data.stats || {};
    for (const [k, el] of Object.entries(c)) el.textContent = num(st[k]);
    age.textContent = st.data_loaded_at ? t("ov.dataAge", { age: ago(st.data_loaded_at) }) : "";
    const b = data.bot || {};
    renderStatus(b);
    p.body.replaceChildren(detailsList([
      [t("ov.running"), b.alive ? num(b.running) : "—"],
      [t("ov.queued"), b.alive ? num(b.queued) : "—"],
      [t("ov.tunnels"), b.alive ? num(b.warp_tunnels) : "—"],
      [t("ov.uptime"), b.started_at ? `${dateTime(b.started_at)} · ${ago(b.started_at)}` : "—"],
    ]), h("div", { class: "panel-actions" }, h("button", { type: "button", class: "ghost", onclick: restartBotDialog }, t("sys.restartBot"))));
  });
  bindLoader(s, live, async (p) => {
    const data = await api("/api/active-users?minutes=15&limit=50");
    const now = Date.now() / 1000;
    const items = (data.items || []).filter((u) => now - Number(u.last_event_ts || 0) < 15 * 60);
    live.el.classList.toggle("recording", items.some((u) => u.progress !== null && u.progress !== undefined && u.progress < 100 && now - u.last_event_ts < 120));
    if (!items.length) return p.empty(t("ov.live.empty"));
    p.body.replaceChildren(h("ul", { class: "tape" }, items.map((u) => liveRow(u, now))));
  });
  bindLoader(s, recent, async (p) => { jobList(p.body, (await api("/api/jobs")).jobs || [], { compact: true }); });
}

function liveRow(u, now) {
  const meta = u.metadata || {};
  const inProgress = u.progress !== null && u.progress !== undefined && u.progress < 100 && now - u.last_event_ts < 120;
  const facts = [meta.resolution || meta.quality, meta.speed, meta.eta ? `${t("meta.eta").toLowerCase()} ${meta.eta}` : null].filter(Boolean).join(" · ");
  return h("li", { class: "tape-row" + (inProgress ? " on" : "") },
    h("button", { type: "button", class: "tape-who", onclick: () => openUser(u) },
      h("span", { class: "tape-name" }, userName(u)),
      h("span", { class: "tape-title" }, u.title || u.url || "")),
    inProgress
      ? h("div", { class: "tape-progress" }, h("progress", { max: 100, value: Math.max(0, Math.min(100, Number(u.progress))), "aria-label": t("meta.progress") }), h("span", null, `${Math.round(u.progress)}%`), facts ? h("span", { class: "muted" }, facts) : null)
      : h("span", { class: "muted tape-time" }, ago(u.last_event_ts)));
}

function buildActivity(s) {
  let minutes = 15; let topPeriod = "today"; let suspPeriod = "today";
  const active = panel({ title: t("act.active"), sub: t("act.active.sub"), span: 2,
    tools: [select([5, 15, 30, 60].map((m) => [m, t("common.minutes", { n: m })]), minutes, (v) => { minutes = Number(v); runActive(); }, t("act.window"))] });
  const top = panel({ title: t("act.top"), tools: [periodSelect(topPeriod, (v) => { topPeriod = v; runTop(); })] });
  const susp = panel({ title: t("act.suspicious"), sub: t("act.suspicious.sub"), tools: [periodSelect(suspPeriod, (v) => { suspPeriod = v; runSusp(); })] });
  const formats = panel({ title: t("act.formats"), sub: t("act.formats.sub") });
  s.root.append(grid(active, top, susp, formats));

  const activeList = userList(active, { metric: (u) => (u.progress !== null && u.progress !== undefined && u.progress < 100 ? `${Math.round(u.progress)}%` : ago(u.last_event_ts)), sub: (u) => (u.title ? h("button", { type: "button", class: "link-btn row-link", onclick: () => openUser(u) }, u.title) : null), limit: 15 });
  const topList = userList(top, { metric: (u) => t("metric.downloads", { n: num(u.count) }) });
  const suspList = userList(susp, { metric: (u) => t("metric.maxGap", { v: duration(u.max_gap_seconds) }), sub: (u) => h("span", null, t("metric.downloads", { n: num(u.downloads) })) });
  const fmtList = userList(formats, { metric: (u) => String(u.format || "").slice(0, 28), sub: (u) => (u.updated_ts ? h("span", null, dateTime(u.updated_ts)) : null) });
  const runActive = bindLoader(s, active, async () => { activeList.set((await api(`/api/active-users?minutes=${minutes}&limit=200`)).items); });
  const runTop = bindLoader(s, top, async () => topList.set(await api(`/api/top-downloaders?period=${topPeriod}&limit=200`)));
  const runSusp = bindLoader(s, susp, async () => suspList.set(await api(`/api/suspicious-users?period=${suspPeriod}&limit=100`)));
  bindLoader(s, formats, async () => fmtList.set(await api("/api/format-users?limit=200")));
}

function buildUsers(s) {
  let period = "week"; let multiPeriod = "week"; let minUrls = 10; let days = 7;
  const demoTools = [periodSelect(period, (v) => { period = v; demo.forEach((run) => run()); })];
  const countries = panel({ title: t("usr.countries"), tools: demoTools });
  const gender = panel({ title: t("usr.gender") });
  const age = panel({ title: t("usr.age") });
  const joins = panel({ title: t("usr.joins") });
  const nsfw = panel({ title: t("usr.nsfw") });
  const playlists = panel({ title: t("usr.playlists") });
  const multi = panel({ title: t("usr.multi"), tools: [periodSelect(multiPeriod, (v) => { multiPeriod = v; runMulti(); })] });
  const urlsIn = h("input", { type: "number", min: 1, max: 1000, value: minUrls, inputmode: "numeric", "aria-label": t("usr.minUrls"), class: "num" });
  const daysIn = h("input", { type: "number", min: 1, max: 30, value: days, inputmode: "numeric", "aria-label": t("usr.days"), class: "num" });
  const power = panel({ title: t("usr.power"), sub: t("usr.power.sub", { urls: minUrls, days }),
    tools: [h("form", { class: "inline-form", onsubmit: (e) => { e.preventDefault(); minUrls = Math.min(1000, Math.max(1, Number(urlsIn.value) || 10)); days = Math.min(30, Math.max(1, Number(daysIn.value) || 7)); power.el.querySelector(".panel-sub").textContent = t("usr.power.sub", { urls: minUrls, days }); runPower(); } },
      h("label", { class: "mini" }, h("span", null, t("usr.minUrls")), urlsIn), h("label", { class: "mini" }, h("span", null, t("usr.days")), daysIn),
      h("button", { type: "submit", class: "ghost small" }, t("usr.apply")))] });
  s.root.append(h("h2", { class: "group-title" }, t("usr.demo")), grid(countries, gender, age, joins), grid(nsfw, playlists, multi, power));

  const demo = [
    bindLoader(s, countries, async (p) => barList(p, await api(`/api/top-countries?period=${period}&limit=60`), { label: (r) => `${r.flag || ""} ${r.country_code || "—"}` })),
    bindLoader(s, gender, async (p) => barList(p, await api(`/api/gender-stats?period=${period}`), { label: (r) => t(`gender.${r.gender}`) })),
    bindLoader(s, age, async (p) => barList(p, await api(`/api/age-stats?period=${period}`), { label: (r) => r.age_group })),
    bindLoader(s, joins, async (p) => barList(p, await api(`/api/channel-join-stats?period=${period}`), { label: (r) => r.join_date })),
  ];
  const nsfwList = userList(nsfw, { metric: (u) => t("metric.downloads", { n: num(u.count) }) });
  const plList = userList(playlists, { metric: (u) => t("metric.downloads", { n: num(u.count) }) });
  const multiList = userList(multi, { metric: (u) => t("metric.avg", { v: u.avg_urls }), sub: (u) => h("span", null, `${t("metric.messages", { n: num(u.messages) })}, ${t("metric.urls", { n: num(u.total_urls) })}`) });
  const powerList = userList(power, { metric: (u) => t("metric.streak", { n: num(u.streak) }) });
  bindLoader(s, nsfw, async () => nsfwList.set(await api("/api/top-nsfw-users?limit=200")));
  bindLoader(s, playlists, async () => plList.set(await api("/api/top-playlist-users?limit=200")));
  const runMulti = bindLoader(s, multi, async () => multiList.set(await api(`/api/top-multi-url-users?period=${multiPeriod}&limit=100`)));
  const runPower = bindLoader(s, power, async () => powerList.set(await api(`/api/power-users?min_urls=${minUrls}&days=${days}&limit=100`)));
}

function buildContent(s) {
  let period = "week"; let filter = ""; let rows = [];
  const domains = panel({ title: t("cnt.domains"), span: 2,
    tools: [searchBox((q) => { filter = q; barList(domains, rows, { label: (r) => r.domain, filter }); }, t("cnt.filter")), periodSelect(period, (v) => { period = v; runDomains(); })] });
  const nsfw = panel({ title: t("cnt.nsfw") });
  s.root.append(grid(domains, nsfw));
  const runDomains = bindLoader(s, domains, async (p) => { rows = await api(`/api/top-domains?period=${period}&limit=200`); barList(p, rows, { label: (r) => r.domain, filter }); });
  bindLoader(s, nsfw, async (p) => barList(p, await api("/api/top-nsfw-domains?limit=100"), { label: (r) => r.domain }));
}

function buildModeration(s) {
  const blocked = panel({ title: t("mod.blocked"), sub: t("mod.blocked.sub") });
  const events = panel({ title: t("mod.events"), sub: t("mod.events.sub") });
  s.root.append(grid(blocked, events));
  const list = userList(blocked, { unblock: true, metric: (u) => dateTime(u.timestamp), sub: (u) => (u.reason ? h("span", null, t("mod.reason", { r: u.reason })) : null), limit: 20 });
  bindLoader(s, blocked, async () => list.set(await api("/api/blocked-users?limit=2000")));
  bindLoader(s, events, async (p) => {
    const rows = await api("/api/channel-events?hours=48&limit=300");
    if (!rows.length) return p.empty();
    p.body.replaceChildren(h("ul", { class: "rows" }, rows.map((ev) => {
      const u = { user_id: ev.user_id, name: ev.name, username: ev.username };
      return userRow(u, { metric: () => dateTime(ev.timestamp), sub: () => h("span", { class: ev.type === "join" ? "tag ok" : "tag warn" }, t(ev.type === "join" ? "mod.join" : "mod.leave")) });
    })));
  });
}

function buildHistory(s) {
  const lookup = panel({ title: t("hist.lookup"), sub: t("hist.lookup.sub"), span: 2 });
  s.root.append(grid(lookup));
  const idInput = h("input", { type: "text", inputmode: "numeric", pattern: "[0-9]{1,16}", placeholder: t("hist.id"), "aria-label": t("hist.id"), class: "num wide-num" });
  const form = h("form", { class: "inline-form", onsubmit: (e) => { e.preventDefault(); const id = idInput.value.trim(); if (/^\d{1,16}$/.test(id)) openHistory({ user_id: Number(id) }); else idInput.focus(); } },
    idInput, h("button", { type: "submit", class: "primary small" }, t("hist.open")));
  const holder = { body: h("div", { class: "lookup-list" }) };
  const list = userList(holder, { metric: (u) => (u.count ? t("metric.downloads", { n: num(u.count) }) : ""), limit: 30 });
  bindLoader(s, lookup, async (p) => {
    const [top, susp] = await Promise.all([api("/api/top-downloaders?period=all&limit=500"), api("/api/suspicious-users?period=all&limit=200")]);
    const seen = new Map();
    for (const u of [...top, ...susp]) if (!seen.has(u.user_id)) seen.set(u.user_id, u);
    if (!p.body.contains(holder.body)) p.body.replaceChildren(form, holder.body);
    list.set([...seen.values()]);
  });
}

function buildSystem(s) {
  const metrics = panel({ title: t("sys.metrics") });
  const controls = panel({ title: t("sys.actions") });
  const versions = panel({ title: t("sys.versions") });
  const log = panel({ title: t("sys.jobs"), span: 2 });
  s.root.append(grid(metrics, controls, versions, log));
  let canRunScript = true;
  controls.body.replaceChildren(h("div", { class: "actions" },
    h("button", { type: "button", class: "action", onclick: restartBotDialog }, t("sys.restartBot")),
    h("button", { type: "button", class: "action", onclick: restartPanel }, t("sys.restartPanel")),
    h("button", { type: "button", class: "action", onclick: updateEngines }, t("sys.updateEngines")),
    h("button", { type: "button", class: "action", onclick: () => updateListsDialog(canRunScript) }, t("sys.updateLists"))),
  h("p", { class: "muted note" }, t("sys.cleanup.note")));
  controls.done();
  controls.refreshBtn.hidden = true;
  bindLoader(s, metrics, async (p) => {
    const m = await api("/api/system-metrics");
    if (m.error) throw Object.assign(new Error(m.error), { status: 500 });
    const meter = (label, pct, text) => h("div", { class: "gauge" }, h("div", { class: "gauge-head" }, h("span", null, label), h("span", null, text)),
      h("meter", { min: 0, max: 100, low: 70, high: 90, optimum: 20, value: Number(pct) || 0, "aria-label": label }));
    const ip = m.external_ip || {};
    const up = m.uptime || {};
    p.body.replaceChildren(
      meter(t("sys.cpu"), m.cpu_percent, `${m.cpu_percent}%`),
      meter(t("sys.ram"), m.memory.percent, `${m.memory.used_gb} / ${m.memory.total_gb} ${t("unit.gb")}`),
      meter(t("sys.disk"), m.disk.percent, `${m.disk.used_gb} / ${m.disk.total_gb} ${t("unit.gb")}`),
      detailsList([
        [t("sys.net"), t("sys.net.value", { up: `${m.network.speed_sent_mbps} ${t("unit.mbps")}`, down: `${m.network.speed_recv_mbps} ${t("unit.mbps")}` })],
        [t("sys.traffic"), `↑ ${bytes(m.network.bytes_sent_mb * 1048576) || "—"} · ↓ ${bytes(m.network.bytes_recv_mb * 1048576) || "—"}`],
        [t("sys.ip"), h("span", { class: "ip" }, [ip.ipv4, ip.ipv6].filter((v) => v && v !== "unknown").join("  ") || "—", ip.checked_at ? h("span", { class: "muted" }, ` (${t("sys.ip.checked", { age: ago(ip.checked_at) })})`) : null)],
        [t("sys.uptime"), `${up.days || 0} ${t("unit.d")} ${up.hours || 0} ${t("unit.h")}`],
      ]));
  });
  bindLoader(s, versions, async (p) => {
    const v = await api("/api/package-versions");
    canRunScript = (await api("/api/lists-stats")).can_run_script;
    p.body.replaceChildren(detailsList(Object.entries(v).map(([k, val]) => [k, h("span", { class: "mono" }, String(val))])));
  });
  bindLoader(s, log, async (p) => jobList(p.body, (await api("/api/jobs")).jobs || []));
}

function settingInput(item) {
  const id = `set-${item.key}`;
  let input;
  if (item.kind === "enum") {
    input = h("select", { id }, item.choices.map((c) => h("option", { value: c, selected: c === item.value }, c)));
  } else if (item.kind === "secret") {
    input = h("input", { id, type: "password", autocomplete: "new-password", placeholder: t("set.secretChange") });
  } else if (item.kind === "id_list") {
    input = h("input", { id, type: "text", value: (item.value || []).join(", "), inputmode: "numeric", placeholder: t("set.list.hint"), spellcheck: "false" });
  } else {
    const numeric = item.kind === "port" || item.kind === "tg_id";
    input = h("input", { id, type: numeric ? "text" : item.kind === "url" ? "url" : "text", inputmode: numeric ? "numeric" : item.kind === "url" ? "url" : null,
      value: item.value === null || item.value === undefined ? "" : String(item.value), spellcheck: "false", autocomplete: "off" });
  }
  input.dataset.key = item.key;
  input.dataset.initial = item.kind === "secret" ? "" : input.value;
  return input;
}

function buildSettings(s) {
  const account = panel({ title: t("set.account"), sub: t("set.account.sub") });
  const sections = {};
  for (const sec of ["proxy", "cookies", "channels"]) sections[sec] = panel({ title: t(`set.${sec}`), sub: t(`set.${sec}.sub`), span: sec === "cookies" ? 2 : 1 });
  s.root.append(grid(sections.proxy, sections.channels, sections.cookies, account));
  buildAccount(account);
  const load = async () => {
    const data = await api("/api/settings");
    for (const sec of Object.keys(sections)) renderSettings(sections[sec], data.items.filter((i) => i.section === sec), load);
    account.body.querySelector("[name=username]").value = data.username || "";
  };
  const run = async () => {
    Object.values(sections).forEach((p) => p.loading());
    try { await load(); Object.values(sections).forEach((p) => p.done()); }
    catch (err) { if (err.status !== 401) Object.values(sections).forEach((p) => p.error(err, run)); }
  };
  Object.values(sections).forEach((p) => p.refreshBtn.addEventListener("click", run));
  account.refreshBtn.hidden = true;
  s.loaders.push(run);
}

function renderSettings(p, items, reload) {
  const errors = h("div", { class: "form-error", role: "alert", hidden: true });
  const form = h("form", { class: "settings", novalidate: true });
  for (const item of items) {
    const input = settingInput(item);
    const extra = [];
    if (item.kind === "secret") extra.push(h("span", { class: `tag ${item.is_set ? "ok" : ""}` }, item.is_set ? t("set.secretSet") : t("set.secretEmpty")));
    if (item.overridden) {
      extra.push(h("span", { class: "tag accent" }, t("set.fromPanel")));
      extra.push(h("button", { type: "button", class: "link-btn small", onclick: async () => {
        const ok = await confirmDialog({ title: t("set.reset.title"), text: `${settingLabel(item.key)}: ${t("set.reset.text")}`, confirm: t("set.reset") });
        if (!ok) return;
        try { await api("/api/settings/reset", { method: "POST", body: { keys: [item.key] } }); restartNote(); reload(); } catch (err) { toast(errorText(err), "error"); }
      } }, t("set.reset")));
    }
    form.append(h("div", { class: "setting" },
      h("label", { for: input.id }, settingLabel(item.key)), input, extra.length ? h("div", { class: "setting-meta" }, extra) : null));
  }
  const save = h("button", { type: "submit", class: "primary" }, t("set.saveSection"));
  form.append(errors, h("div", { class: "form-actions" }, save));
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const changes = {};
    form.querySelectorAll("[data-key]").forEach((el) => {
      if (el.type === "password") { if (el.value) changes[el.dataset.key] = el.value; }
      else if (el.value !== el.dataset.initial) changes[el.dataset.key] = el.value;
    });
    form.querySelectorAll(".invalid").forEach((el) => el.classList.remove("invalid"));
    errors.hidden = true;
    if (!Object.keys(changes).length) { toast(t("common.saved"), "ok"); return; }
    save.disabled = true;
    try {
      await api("/api/settings", { method: "POST", body: changes });
      toast(t("common.saved"), "ok");
      restartNote();
      reload();
    } catch (err) {
      const fields = (err.body && err.body.fields) || {};
      const lines = Object.entries(fields).map(([k, v]) => { const el = form.querySelector(`[data-key="${k}"]`); if (el) el.classList.add("invalid"); return `${settingLabel(k)}: ${v}`; });
      errors.replaceChildren(h("strong", null, t("set.err.title")), h("ul", null, lines.map((l) => h("li", null, l))));
      errors.hidden = !lines.length;
      if (!lines.length) toast(errorText(err), "error");
    } finally { save.disabled = false; }
  });
  p.body.replaceChildren(form);
}

function restartNote() {
  const box = document.getElementById("toasts");
  const el = h("div", { class: "toast toast-info", role: "status" }, t("set.restartNote"),
    h("button", { type: "button", class: "ghost small", onclick: () => { el.remove(); restartBotDialog(); } }, t("set.restartNow")));
  box.append(el);
  setTimeout(() => el.remove(), 12000);
}

function buildAccount(p, { forced = false } = {}) {
  const field = (name, label, type, auto) => h("label", { class: "field" }, h("span", null, label), h("input", { name, type, autocomplete: auto, required: type === "password", maxlength: 256 }));
  const error = h("p", { class: "form-error", role: "alert", hidden: true });
  const form = h("form", { class: "settings", novalidate: true },
    field("username", t("set.username"), "text", "username"),
    field("current", t("set.current"), "password", "current-password"),
    field("new", t("set.new"), "password", "new-password"),
    field("repeat", t("set.repeat"), "password", "new-password"),
    error, h("div", { class: "form-actions" }, h("button", { type: "submit", class: "primary" }, t("set.changePassword"))));
  if (state.session) form.querySelector("[name=username]").value = state.session.user;
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const v = Object.fromEntries(new FormData(form).entries());
    const fail = (text) => { error.textContent = text; error.hidden = false; };
    error.hidden = true;
    if (v.new !== v.repeat) return fail(t("set.err.mismatch"));
    if ((v.new || "").length < 10) return fail(t("set.err.too_short", { n: 10 }));
    try {
      await api("/api/change-password", { method: "POST", body: { current_password: v.current, new_password: v.new, username: v.username || undefined } });
      toast(t("set.pwChanged"), "ok");
      if (forced) { window.location.reload(); return; }
      form.reset();
      await loadSession();
      form.querySelector("[name=username]").value = state.session.user;
    } catch (err) {
      const code = err.body && err.body.error;
      fail(code ? t(`set.err.${code}`, { n: err.body.min_length || 10 }) : errorText(err));
    }
  });
  p.body.replaceChildren(form);
}

function buildLists(s) {
  const files = panel({ title: t("lst.files") });
  const editor = panel({ title: t("lst.domain"), sub: t("lst.domain.sub"), span: 2 });
  s.root.append(grid(files, editor));
  bindLoader(s, files, async (p) => {
    const st = await api("/api/lists-stats");
    p.body.replaceChildren(detailsList(["porn_domains", "porn_keywords", "supported_sites"].map((k) => [t(`lst.${k}`), t("lst.lines", { n: num(st[k]) })])),
      h("div", { class: "panel-actions" }, h("button", { type: "button", class: "ghost", onclick: () => updateListsDialog(st.can_run_script) }, t("sys.updateLists"))));
  });
  let current = null;
  bindLoader(s, editor, async (p) => {
    const data = await api("/api/domain-lists");
    const names = Object.keys(data.lists);
    current = current && names.includes(current) ? current : names[0];
    const area = h("textarea", { rows: 14, spellcheck: "false", "aria-label": t("lst.domain") });
    const desc = h("p", { class: "muted" });
    const count = h("span", { class: "muted" });
    const error = h("p", { class: "form-error", role: "alert", hidden: true });
    const show = () => {
      area.value = (data.lists[current] || []).join("\n");
      desc.textContent = t(`lst.desc.${current}`);
      count.textContent = t("lst.count", { n: num((data.lists[current] || []).length) });
      error.hidden = true;
    };
    area.addEventListener("input", debounce(() => { count.textContent = t("lst.count", { n: num(area.value.split("\n").filter((l) => l.trim()).length) }); }, 200));
    const picker = select(names.map((n) => [n, n]), current, (v) => { current = v; show(); }, t("lst.pick"));
    const save = h("button", { type: "button", class: "primary", onclick: async () => {
      const items = area.value.split("\n").map((l) => l.trim()).filter(Boolean);
      save.disabled = true; error.hidden = true;
      try {
        const res = await api(`/api/domain-lists/${encodeURIComponent(current)}`, { method: "POST", body: { items } });
        data.lists[current] = items; count.textContent = t("lst.count", { n: num(res.count) });
        toast(t("lst.saved"), "ok"); restartNote();
      } catch (err) {
        const detail = (err.body && err.body.detail) || "";
        error.textContent = detail.startsWith("invalid_item:") ? t("lst.invalid", { v: detail.slice(13) }) : errorText(err);
        error.hidden = false;
      } finally { save.disabled = false; }
    } }, t("common.save"));
    p.body.replaceChildren(h("div", { class: "list-tools" }, picker, count), desc, area, error, h("div", { class: "form-actions" }, save));
    show();
  });
}

// ================================================================= shell

function renderStatus(bot) {
  state.bot = bot;
  const el = document.getElementById("bot-status");
  const known = !!(bot && bot.ts);
  const alive = known && bot.alive;
  el.dataset.state = !known ? "unknown" : bot.stopping ? "warn" : alive ? "ok" : "down";
  el.querySelector(".status-text").textContent = !known ? t("bot.unknown") : bot.stopping ? t("bot.stopping") : alive ? t("bot.alive") : t("bot.dead");
  el.querySelector(".status-tasks").textContent = alive ? t("bot.tasks", { running: num(bot.running), queued: num(bot.queued) }) : "";
}

async function pollStatus() {
  if (document.hidden) return;
  try { renderStatus((await api("/api/overview")).bot); } catch { /* the next poll retries */ }
}

function buildNav() {
  const nav = document.getElementById("nav");
  nav.replaceChildren(...SECTIONS.map((sec) => h("button", {
    type: "button", role: "tab", id: `tab-${sec.id}`, "aria-controls": `section-${sec.id}`, class: "nav-item",
    dataset: { section: sec.id }, onclick: () => show(sec.id, true),
  }, h("span", { class: `nav-icon i-${sec.id}`, "aria-hidden": "true" }), h("span", null, t(`nav.${sec.id}`)))));
  nav.addEventListener("keydown", (e) => {
    const tabs = [...nav.querySelectorAll("[role=tab]")];
    const i = tabs.indexOf(document.activeElement);
    if (i < 0) return;
    let next = null;
    if (e.key === "ArrowDown" || e.key === "ArrowRight") next = tabs[(i + 1) % tabs.length];
    if (e.key === "ArrowUp" || e.key === "ArrowLeft") next = tabs[(i - 1 + tabs.length) % tabs.length];
    if (e.key === "Home") next = tabs[0];
    if (e.key === "End") next = tabs[tabs.length - 1];
    if (next) { e.preventDefault(); next.focus(); show(next.dataset.section, true); }
  });
}

function markNav(id) {
  document.querySelectorAll("#nav [role=tab]").forEach((tab) => {
    const on = tab.dataset.section === id;
    tab.setAttribute("aria-selected", String(on));
    tab.tabIndex = on ? 0 : -1;
  });
}

function show(id, push) {
  const sec = SECTIONS.find((x) => x.id === id) || SECTIONS[0];
  state.section = sec.id;
  if (push) history.replaceState(null, "", `#${sec.id}`);
  markNav(sec.id);
  const main = document.getElementById("main");
  let built = state.built.get(sec.id);
  if (!built) {
    const root = h("div", { class: "section", id: `section-${sec.id}`, role: "tabpanel", "aria-labelledby": `tab-${sec.id}` },
      h("h1", { class: "section-title" }, t(`nav.${sec.id}`)));
    built = { root, loaders: [] };
    sec.build(built);
    state.built.set(sec.id, built);
    built.loaders.forEach((run) => run());
  } else {
    built.loaders.forEach((run) => run());
  }
  main.replaceChildren(...(state.session?.read_only ? [h("p", {class: "preview-notice", role: "note"}, t("preview.notice"))] : []), built.root);
  document.title = `${t(`nav.${sec.id}`)} · ${state.session ? state.session.bot_name : ""}`;
  schedule(sec);
}

function schedule(sec) {
  state.timers.forEach(clearInterval);
  state.timers = [];
  if (sec.every) state.timers.push(setInterval(() => { if (!document.hidden && !document.getElementById("dialog").open) refreshSection(); }, sec.every * 1000));
  state.timers.push(setInterval(tickStamps, 15000));
}

function refreshSection() {
  const built = state.built.get(state.section);
  if (built) built.loaders.forEach((run) => run());
}

function tickStamps() {
  document.querySelectorAll(".stamp[data-ts]").forEach((el) => { el.textContent = t("common.updated", { age: ago(Number(el.dataset.ts)) }); });
}

function renderChrome() {
  translateStatic();
  const langBtn = document.getElementById("lang-toggle");
  langBtn.textContent = t("top.lang");
  langBtn.setAttribute("aria-label", t("top.lang.label"));
  const theme = document.documentElement.dataset.theme || "auto";
  const themeBtn = document.getElementById("theme-toggle");
  themeBtn.textContent = `${t("top.theme")}: ${t(`top.theme.${theme}`)}`;
  document.getElementById("logout").textContent = t("top.logout");
  buildNav();
  if (state.bot) renderStatus(state.bot);
}

async function loadSession() {
  state.session = await api("/api/session");
  setCsrf(state.session.csrf);
}

function forcedPasswordScreen() {
  const main = document.getElementById("main");
  const p = panel({ title: t("set.forced.title"), sub: t("set.forced.text") });
  p.refreshBtn.hidden = true;
  buildAccount(p, { forced: true });
  main.replaceChildren(h("div", { class: "section narrow" }, p.el));
  document.getElementById("nav").replaceChildren();
}

async function init() {
  initDialog();
  try { await loadSession(); } catch { return; }
  renderChrome();
  document.getElementById("lang-toggle").addEventListener("click", () => {
    setLang(getLang() === "ru" ? "en" : "ru");
    state.built.clear();
    renderChrome();
    if (state.session.must_change_password) forcedPasswordScreen(); else show(state.section, false);
  });
  document.getElementById("theme-toggle").addEventListener("click", () => {
    const order = ["auto", "light", "dark"];
    const next = order[(order.indexOf(document.documentElement.dataset.theme || "auto") + 1) % order.length];
    document.documentElement.dataset.theme = next;
    localStorage.setItem("dash.theme", next);
    renderChrome();
    if (!state.session.must_change_password) markNav(state.section); else document.getElementById("nav").replaceChildren();
  });
  document.getElementById("logout").addEventListener("click", async () => {
    try { await api("/api/logout", { method: "POST", body: {} }); } catch { /* go to login anyway */ }
    window.location.replace("/login");
  });
  if (state.session.must_change_password) { forcedPasswordScreen(); return; }
  const initial = (window.location.hash || "").slice(1);
  show(SECTIONS.some((x) => x.id === initial) ? initial : "overview", false);
  pollStatus();
  setInterval(pollStatus, 10000);
  document.addEventListener("visibilitychange", () => { if (!document.hidden) { pollStatus(); refreshSection(); } });
}

init();
