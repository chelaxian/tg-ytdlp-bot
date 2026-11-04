import { t, getLang, setLang, translateStatic } from "./i18n.js";

const form = document.getElementById("login-form");
const errorEl = document.getElementById("login-error");
const submit = document.getElementById("login-submit");
const langBtn = document.getElementById("lang-toggle");

function render() {
  translateStatic();
  langBtn.textContent = t("top.lang");
  langBtn.setAttribute("aria-label", t("top.lang.label"));
  document.title = t("login.title");
}

function showError(text) {
  errorEl.textContent = text;
  errorEl.hidden = !text;
}

langBtn.addEventListener("click", () => { setLang(getLang() === "ru" ? "en" : "ru"); render(); });

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  showError("");
  const data = new FormData(form);
  const username = String(data.get("username") || "").trim();
  const password = String(data.get("password") || "");
  if (!username || !password) {
    form.querySelector(username ? "[name=password]" : "[name=username]").focus();
    return;
  }
  submit.disabled = true;
  submit.textContent = t("login.wait");
  try {
    const res = await fetch("/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
      credentials: "same-origin",
    });
    const body = await res.json().catch(() => ({}));
    if (res.ok) {
      window.location.replace("/");
      return;
    }
    if (res.status === 429) showError(t("login.err.locked", { s: body.retry_after || 30 }));
    else if (body.error === "invalid_credentials") showError(t("login.err.invalid_credentials"));
    else showError(t("login.err.generic"));
    form.querySelector("[name=password]").select();
  } catch {
    showError(t("login.err.network"));
  } finally {
    submit.disabled = false;
    submit.textContent = t("login.submit");
  }
});

render();
form.querySelector("[name=username]").focus();
