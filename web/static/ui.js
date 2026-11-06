// DOM, network and formatting helpers. No innerHTML anywhere: text goes through
// textContent, attributes through setAttribute, links through safeHref().
import { t, getLang } from "./i18n.js";

export function h(tag, attrs, ...children) {
  const el = document.createElement(tag);
  if (attrs) {
    for (const [key, value] of Object.entries(attrs)) {
      if (value === undefined || value === null || value === false) continue;
      if (key === "class") el.className = value;
      else if (key === "text") el.textContent = value;
      else if (key === "dataset") Object.assign(el.dataset, value);
      else if (key.startsWith("on") && typeof value === "function") el.addEventListener(key.slice(2), value);
      else if (key === "href") { const safe = safeHref(value); if (safe) el.setAttribute("href", safe); }
      else if (value === true) el.setAttribute(key, "");
      else el.setAttribute(key, String(value));
    }
  }
  append(el, children);
  return el;
}

function append(el, children) {
  for (const child of children) {
    if (child === null || child === undefined || child === false) continue;
    if (Array.isArray(child)) append(el, child);
    else el.append(child instanceof Node ? child : document.createTextNode(String(child)));
  }
}

export function safeHref(url) {
  if (typeof url !== "string") return null;
  const value = url.trim();
  if (/^tg:\/\/user\?id=\d{1,16}$/.test(value)) return value;
  try {
    const parsed = new URL(value, window.location.origin);
    if (parsed.protocol === "https:" || parsed.protocol === "http:") return parsed.href;
  } catch { /* not a URL */ }
  return null;
}

export function clear(el) { el.replaceChildren(); return el; }

// ---------------------------------------------------------------- network

let csrfToken = "";
export function setCsrf(token) { csrfToken = token || ""; }
export function getCsrf() { return csrfToken; }

export class ApiError extends Error {
  constructor(status, body) {
    super((body && (body.error || body.detail)) || `http_${status}`);
    this.status = status;
    this.body = body || {};
  }
}

export async function api(path, { method = "GET", body, timeout = 20000, signal } = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeout);
  if (signal) signal.addEventListener("abort", () => controller.abort(), { once: true });
  const headers = { Accept: "application/json" };
  if (method !== "GET") {
    headers["Content-Type"] = "application/json";
    headers["X-CSRF-Token"] = csrfToken;
  }
  let res;
  try {
    res = await fetch(path, {
      method, headers, credentials: "same-origin", signal: controller.signal,
      body: body === undefined ? undefined : JSON.stringify(body),
    });
  } catch (err) {
    clearTimeout(timer);
    throw new ApiError(0, { error: err.name === "AbortError" ? "timeout" : "network" });
  }
  clearTimeout(timer);
  const data = await res.json().catch(() => ({}));
  if (res.status === 401) {
    toast(t("toast.sessionExpired"), "warn");
    setTimeout(() => window.location.replace("/login"), 900);
    throw new ApiError(401, data);
  }
  if (!res.ok) throw new ApiError(res.status, data);
  return data;
}

export function errorText(err) {
  if (!(err instanceof ApiError)) return t("common.error");
  if (err.status === 0) return t("toast.network");
  if (err.status === 403 && err.body.error === "preview_read_only") return t("preview.notice");
  if (err.status === 403) return t("toast.forbidden");
  if (err.status === 409) return t("toast.busy");
  return t("toast.failed", { msg: err.message });
}

// ---------------------------------------------------------------- toasts

export function toast(text, kind = "info", ms = 4200) {
  const box = document.getElementById("toasts");
  if (!box) return;
  const el = h("div", { class: `toast toast-${kind}`, role: kind === "error" ? "alert" : "status" }, text);
  box.append(el);
  setTimeout(() => { el.classList.add("leaving"); setTimeout(() => el.remove(), 250); }, ms);
}

// ---------------------------------------------------------------- dialog

let lastFocus = null;

export function openDialog({ title, body, actions = [], wide = false, onClose }) {
  const dialog = document.getElementById("dialog");
  lastFocus = document.activeElement;
  dialog.className = wide ? "wide" : "";
  const closeBtn = h("button", { type: "button", class: "icon-btn", "aria-label": t("common.close"), onclick: () => closeDialog() }, "✕");
  const footer = actions.length ? h("div", { class: "dialog-actions" }, actions) : null;
  dialog.replaceChildren(
    h("div", { class: "dialog-head" }, h("h2", { id: "dialog-title" }, title), closeBtn),
    h("div", { class: "dialog-body" }, body),
    footer,
  );
  dialog._onClose = onClose;
  if (!dialog.open) dialog.showModal();
  const first = dialog.querySelector("[autofocus]") || dialog.querySelector(".dialog-actions .primary, .dialog-actions .danger") || closeBtn;
  first.focus();
  return dialog;
}

export function closeDialog() {
  const dialog = document.getElementById("dialog");
  if (dialog.open) dialog.close();
}

export function initDialog() {
  const dialog = document.getElementById("dialog");
  dialog.addEventListener("close", () => {
    const cb = dialog._onClose; dialog._onClose = null;
    dialog.replaceChildren();
    if (cb) cb();
    if (lastFocus && document.contains(lastFocus)) lastFocus.focus();
  });
  dialog.addEventListener("click", (e) => { if (e.target === dialog) closeDialog(); });
}

export function confirmDialog({ title, text, confirm, danger = false, extra }) {
  return new Promise((resolve) => {
    let result = false;
    const yes = h("button", { type: "button", class: danger ? "danger" : "primary", onclick: () => { result = true; closeDialog(); } }, confirm);
    const no = h("button", { type: "button", class: "ghost", onclick: () => closeDialog() }, t("common.cancel"));
    openDialog({ title, body: [h("p", null, text), extra || null], actions: [no, yes], onClose: () => resolve(result) });
  });
}

// ---------------------------------------------------------------- formatting

const nf = () => new Intl.NumberFormat(getLang() === "ru" ? "ru-RU" : "en-US");
export const num = (n) => (n === null || n === undefined || Number.isNaN(Number(n)) ? "—" : nf().format(Number(n)));

export function duration(seconds) {
  const s = Math.max(0, Math.round(Number(seconds) || 0));
  if (s < 60) return `${s} ${t("unit.s")}`;
  const m = Math.floor(s / 60);
  if (m < 60) return `${m} ${t("unit.m")}`;
  const hrs = Math.floor(m / 60);
  if (hrs < 48) return `${hrs} ${t("unit.h")} ${m % 60 ? `${m % 60} ${t("unit.m")}` : ""}`.trim();
  return `${Math.floor(hrs / 24)} ${t("unit.d")} ${hrs % 24 ? `${hrs % 24} ${t("unit.h")}` : ""}`.trim();
}

export function ago(ts) {
  if (!ts) return t("common.never");
  const diff = Date.now() / 1000 - Number(ts);
  if (diff < 20) return t("common.now");
  return t("common.ago", { v: duration(diff) });
}

export function dateTime(ts) {
  if (!ts) return "—";
  const d = new Date(Number(ts) * 1000);
  return d.toLocaleString(getLang() === "ru" ? "ru-RU" : "en-GB", { day: "2-digit", month: "short", hour: "2-digit", minute: "2-digit" });
}

export function bytes(value) {
  const n = Number(value);
  if (!Number.isFinite(n) || n <= 0) return null;
  const units = ["B", "KB", "MB", "GB", "TB"];
  let i = 0; let v = n;
  while (v >= 1024 && i < units.length - 1) { v /= 1024; i += 1; }
  return `${v >= 10 || i === 0 ? Math.round(v) : v.toFixed(1)} ${units[i]}`;
}

export function debounce(fn, ms = 150) {
  let timer;
  return (...args) => { clearTimeout(timer); timer = setTimeout(() => fn(...args), ms); };
}

export function userName(u) {
  return (u && (u.name || (u.username ? `@${u.username}` : ""))) || t("user.noname");
}

export function userLink(u) {
  if (u && u.username && /^[A-Za-z0-9_]{3,64}$/.test(u.username)) return `https://t.me/${u.username}`;
  if (u && u.user_id) return `tg://user?id=${Number(u.user_id)}`;
  return null;
}

export function matches(u, query) {
  if (!query) return true;
  const q = query.trim().toLowerCase().replace(/^@/, "");
  return [u.name, u.username, String(u.user_id || ""), u.domain, u.title].some((v) => v && String(v).toLowerCase().includes(q));
}
