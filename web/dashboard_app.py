"""tg-ytdlp-bot admin dashboard (FastAPI).

Run: uvicorn web.dashboard_app:app --host 127.0.0.1 --port 5555

Design rules
* Every handler is a plain `def`: FastAPI runs it in its threadpool, so slow I/O
  never blocks the event loop and one slow request never freezes the panel.
* Reads come from in-memory caches (services.stats_service); long actions are
  background jobs (services.jobs) and return at once.
* Auth: session cookie (HttpOnly, SameSite=Strict, Secure on HTTPS) plus a
  per-session CSRF token on every POST and a same-origin check.
* Strict CSP without inline code or styles; no third-party resources.
* The panel never writes CONFIG/config.py; settings go to CONFIG/overrides.py.
"""

from __future__ import annotations

import hashlib
import os
import logging
import pathlib
import time
from enum import Enum
from urllib.parse import urlparse
from typing import Any, Dict, List, Optional

from fastapi import Body, FastAPI, HTTPException, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.gzip import GZipMiddleware

from CONFIG import overrides
from CONFIG.config import Config

overrides.apply(Config)  # settings saved from the dashboard (same as the bot does)

from services import jobs, lists_service, stats_service, system_service  # noqa: E402
from services.stats_collector import enable_background_profiles  # noqa: E402
from web import security  # noqa: E402

logger = logging.getLogger("dashboard")

BASE_DIR = pathlib.Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def _asset_version() -> str:
    digest = hashlib.sha256()
    for path in sorted(STATIC_DIR.glob("*")):
        if path.is_file():
            digest.update(path.name.encode())
            digest.update(path.read_bytes())
    return digest.hexdigest()[:12]


ASSET_VERSION = _asset_version()
AUDIT_FILE = pathlib.Path(os.environ.get("TG_DASHBOARD_PROJECT_DIR", str(BASE_DIR.parent))) / "CONFIG" / ".dashboard_audit.log"
PREVIEW_READ_ONLY = os.environ.get("TG_DASHBOARD_READ_ONLY", "1") != "0"

app = FastAPI(title="tg-ytdlp dashboard", docs_url=None, redoc_url=None, openapi_url=None)


class _Static(StaticFiles):
    async def get_response(self, path, scope):
        response = await super().get_response(path, scope)
        if response.status_code == 200:
            if b"v=" in scope.get("query_string", b""):
                # page URLs carry ?v=<content hash>, so these copies never go stale
                response.headers["Cache-Control"] = "public, max-age=31536000, immutable"
            else:
                # module imports (no version): revalidate with the ETag, a cheap 304
                response.headers["Cache-Control"] = "no-cache"
        return response


app.mount("/static", _Static(directory=str(STATIC_DIR)), name="static")

CSP = ("default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; "
       "connect-src 'self'; font-src 'self'; manifest-src 'self'; base-uri 'none'; "
       "form-action 'self'; frame-ancestors 'none'")

PUBLIC_PATHS = {"/login", "/api/login", "/health"}


class GuardMiddleware(BaseHTTPMiddleware):
    """Security headers, authentication and CSRF for every request."""

    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        request.state.session = None
        request.state.token = None
        public = path in PUBLIC_PATHS or path.startswith("/static/")

        if not public:
            token = request.cookies.get(security.SESSION_COOKIE)
            session = security.sessions.get(token)
            if session is None:
                if path.startswith("/api/"):
                    return self._headers(JSONResponse({"error": "unauthorized"}, status_code=401), request)
                return self._headers(RedirectResponse("/login", status_code=303), request)
            allowed_while_must_change = {"/", "/api/session", "/api/change-password", "/api/logout"}
            if session.must_change and path not in allowed_while_must_change:
                return self._headers(JSONResponse({"error": "password_change_required"}, status_code=403), request)
            request.state.session = session
            request.state.token = token

        if request.method not in ("GET", "HEAD", "OPTIONS"):
            # The browser tab only drives the separate Chromium session; it cannot change bot settings,
            # bans or restarts, so it stays usable in the read-only preview.
            if PREVIEW_READ_ONLY and path not in {"/api/login", "/api/logout", "/api/change-password"}                     and not path.startswith("/api/browser/"):
                return self._headers(JSONResponse({"error": "preview_read_only"}, status_code=403), request)
            if not security.same_origin(request):
                return self._headers(JSONResponse({"error": "bad_origin"}, status_code=403), request)
            session = request.state.session
            if session is not None:
                sent = request.headers.get(security.CSRF_HEADER, "")
                import hmac
                if not sent or not hmac.compare_digest(sent, session.csrf):
                    return self._headers(JSONResponse({"error": "csrf"}, status_code=403), request)

        response = await call_next(request)
        return self._headers(response, request)

    @staticmethod
    def _headers(response, request):
        h = response.headers
        h["Content-Security-Policy"] = CSP
        h["X-Content-Type-Options"] = "nosniff"
        h["X-Frame-Options"] = "DENY"
        h["Referrer-Policy"] = "same-origin"
        h["Permissions-Policy"] = "camera=(), microphone=(), geolocation=(), payment=(), usb=()"
        h["Cross-Origin-Opener-Policy"] = "same-origin"
        h["Cross-Origin-Resource-Policy"] = "same-origin"
        if security.is_https(request):
            h["Strict-Transport-Security"] = "max-age=31536000"
        if request.url.path.startswith("/api/") or request.url.path in ("/", "/login"):
            h["Cache-Control"] = "no-store"
        return response


app.add_middleware(GuardMiddleware)
app.add_middleware(GZipMiddleware, minimum_size=800)


@app.exception_handler(RequestValidationError)
def _validation_error(request: Request, exc: RequestValidationError):
    fields = [".".join(str(p) for p in err.get("loc", [])[1:]) for err in exc.errors()]
    return JSONResponse({"error": "invalid_request", "fields": fields[:10]}, status_code=422)


@app.exception_handler(Exception)
def _unhandled(request: Request, exc: Exception):
    logger.exception("[dashboard] %s %s failed", request.method, request.url.path)
    return JSONResponse({"error": "internal_error"}, status_code=500)


@app.on_event("startup")
def _startup() -> None:
    enable_background_profiles()
    # firebase_init may have created the collector before its SQL store existed.
    # Refresh once now that imports are complete, before accepting HTTP requests.
    collector = stats_service.get_stats_collector()
    reload_stats = getattr(collector, "reload_from_dump", None)
    if callable(reload_stats):
        reload_stats()
    system_service.get_external_ip_cached()   # starts the first lookup in the background
    try:
        import psutil
        psutil.cpu_percent(interval=None)      # prime the CPU sampler
    except Exception:
        pass


def _audit(request: Request, action: str, **details: Any) -> None:
    session = getattr(request.state, "session", None)
    user = session.user if session else "-"
    record = {"ts": int(time.time()), "user": user, "ip": security.client_ip(request), "action": action}
    record.update({k: v for k, v in details.items() if v is not None})
    try:
        import json
        path = AUDIT_FILE
        if path.exists() and path.stat().st_size > 5 * 1024 * 1024:
            path.replace(path.with_suffix(".log.1"))
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError:
        pass
    logger.info("[audit] %s %s", user, action)


def _user(request: Request) -> str:
    return request.state.session.user if request.state.session else "-"


# --------------------------------------------------------------------------------------
# Pages and session
# --------------------------------------------------------------------------------------

def _page(request: Request, name: str) -> HTMLResponse:
    return templates.TemplateResponse(request, name, {
        "v": ASSET_VERSION,
        "bot_name": str(getattr(Config, "BOT_NAME_FOR_USERS", "tg-ytdlp-bot")),
    })


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    if security.sessions.get(request.cookies.get(security.SESSION_COOKIE)):
        return RedirectResponse("/", status_code=303)
    return _page(request, "login.html")


@app.get("/", response_class=HTMLResponse)
def dashboard_page(request: Request):
    return _page(request, "dashboard.html")


class LoginBody(BaseModel):
    username: str = Field(..., min_length=1, max_length=128)
    password: str = Field(..., min_length=1, max_length=256)


@app.post("/api/login")
def api_login(body: LoginBody, request: Request):
    ip = security.client_ip(request)
    keys = (f"ip:{ip}", f"user:{body.username.lower()}")
    wait = security.throttle.retry_after(*keys)
    if wait:
        return JSONResponse({"error": "locked", "retry_after": wait}, status_code=429,
                            headers={"Retry-After": str(wait)})
    valid, must_change = security.check_credentials(body.username, body.password)
    if not valid:
        security.throttle.fail(*keys)
        _audit(request, "login_failed", username=body.username[:64])
        return JSONResponse({"error": "invalid_credentials"}, status_code=401)
    security.throttle.success(*keys)
    token, session = security.sessions.create(body.username, ip, must_change)
    request.state.session = session
    _audit(request, "login")
    response = JSONResponse({"ok": True, "must_change_password": must_change})
    response.set_cookie(security.SESSION_COOKIE, token, httponly=True, samesite="strict",
                        secure=security.is_https(request) or bool(getattr(Config, "DASHBOARD_COOKIE_SECURE", False)),
                        max_age=security.ABSOLUTE_TTL, path="/")
    return response


@app.post("/api/logout")
def api_logout(request: Request):
    security.sessions.drop(request.state.token)
    response = JSONResponse({"ok": True})
    response.delete_cookie(security.SESSION_COOKIE, path="/")
    return response


@app.get("/api/session")
def api_session(request: Request):
    s = request.state.session
    return {"user": s.user, "csrf": s.csrf, "must_change_password": s.must_change,
            "read_only": PREVIEW_READ_ONLY, "idle_timeout": security.IDLE_TTL, "bot_name": str(getattr(Config, "BOT_NAME_FOR_USERS", ""))}


class PasswordBody(BaseModel):
    current_password: str = Field(..., min_length=1, max_length=256)
    new_password: str = Field(..., min_length=1, max_length=256)
    username: Optional[str] = Field(default=None, max_length=64, pattern=r"^[A-Za-z0-9._@-]{3,64}$")


@app.post("/api/change-password")
def api_change_password(body: PasswordBody, request: Request):
    s = request.state.session
    ip = security.client_ip(request)
    keys = (f"pw:{ip}",)
    if security.throttle.retry_after(*keys):
        return JSONResponse({"error": "locked"}, status_code=429)
    valid, _ = security.check_credentials(s.user, body.current_password)
    if not valid:
        security.throttle.fail(*keys)
        return JSONResponse({"error": "wrong_current_password"}, status_code=400)
    problem = security.password_problem(body.new_password)
    if problem:
        return JSONResponse({"error": problem, "min_length": security.MIN_PASSWORD_LENGTH}, status_code=400)
    username = body.username or s.user
    security.set_password(username, body.new_password)
    security.sessions.drop_all()                       # every other session must log in again
    token, session = security.sessions.create(username, ip, False)
    request.state.session = session
    _audit(request, "password_changed")
    response = JSONResponse({"ok": True})
    response.set_cookie(security.SESSION_COOKIE, token, httponly=True, samesite="strict",
                        secure=security.is_https(request) or bool(getattr(Config, "DASHBOARD_COOKIE_SECURE", False)),
                        max_age=security.ABSOLUTE_TTL, path="/")
    return response


@app.post("/api/reset-lockdown")
def api_reset_lockdown(request: Request):
    security.throttle.success(f"ip:{security.client_ip(request)}")
    return {"ok": True}


@app.get("/health")
def health():
    return {"status": "ok"}


# --------------------------------------------------------------------------------------
# Statistics
# --------------------------------------------------------------------------------------

class Period(str, Enum):
    today = "today"
    week = "week"
    month = "month"
    all = "all"


Limit = Query(default=50, ge=1, le=500)


@app.get("/api/overview")
def api_overview():
    from HELPERS import runtime_status
    return {"stats": stats_service.fetch_overview(), "bot": runtime_status.read()}


@app.get("/api/active-users")
def api_active_users(limit: int = Limit, minutes: int = Query(default=15, ge=1, le=1440)):
    return stats_service.fetch_active_users(limit=limit, minutes=minutes)


@app.get("/api/top-downloaders")
def api_top_downloaders(period: Period = Period.today, limit: int = Limit):
    return stats_service.fetch_top_downloaders(period.value, limit)


@app.get("/api/top-domains")
def api_top_domains(period: Period = Period.today, limit: int = Limit):
    return stats_service.fetch_top_domains(period.value, limit)


@app.get("/api/top-countries")
def api_top_countries(period: Period = Period.today, limit: int = Limit):
    return stats_service.fetch_top_countries(period.value, limit)


@app.get("/api/gender-stats")
def api_gender(period: Period = Period.today):
    return stats_service.fetch_gender_stats(period.value)


@app.get("/api/age-stats")
def api_age(period: Period = Period.today):
    return stats_service.fetch_age_stats(period.value)


@app.get("/api/channel-join-stats")
def api_channel_joins(period: Period = Period.today):
    return stats_service.fetch_channel_join_stats(period.value)


@app.get("/api/top-nsfw-users")
def api_nsfw_users(limit: int = Limit):
    return stats_service.fetch_top_nsfw_users(limit)


@app.get("/api/top-nsfw-domains")
def api_nsfw_domains(limit: int = Limit):
    return stats_service.fetch_top_nsfw_domains(limit)


@app.get("/api/top-playlist-users")
def api_playlist_users(limit: int = Limit):
    return stats_service.fetch_top_playlist_users(limit)


@app.get("/api/top-multi-url-users")
def api_multi_url_users(period: Period = Period.today, limit: int = Limit):
    return stats_service.fetch_top_multi_url_users(period.value, limit)


@app.get("/api/format-users")
def api_format_users(limit: int = Limit):
    return stats_service.fetch_format_users(limit)


@app.get("/api/power-users")
def api_power_users(min_urls: int = Query(default=10, ge=1, le=1000), days: int = Query(default=7, ge=1, le=30),
                    limit: int = Limit):
    return stats_service.fetch_power_users(min_urls=min_urls, days=days, limit=limit)


@app.get("/api/suspicious-users")
def api_suspicious(period: Period = Period.today, limit: int = Limit):
    return stats_service.fetch_suspicious_users(period.value, limit)


@app.get("/api/blocked-users")
def api_blocked(limit: int = Query(default=200, ge=1, le=5000)):
    return stats_service.fetch_blocked_users(limit)


@app.get("/api/channel-events")
def api_channel_events(hours: int = Query(default=48, ge=1, le=48), limit: int = Query(default=200, ge=1, le=500)):
    return stats_service.fetch_recent_channel_events(hours=hours, limit=limit)


@app.get("/api/user-history")
def api_user_history(user_id: int = Query(..., gt=0, lt=10 ** 16), period: Period = Period.all,
                     limit: int = Query(default=500, ge=1, le=2000)):
    return stats_service.fetch_user_history(user_id, period.value, limit)


class BlockBody(BaseModel):
    user_id: int = Field(..., gt=0, lt=10 ** 16)
    reason: Optional[str] = Field(default=None, max_length=120, pattern=r"^[^\x00-\x1f\x7f]*$")


@app.post("/api/block-user")
def api_block(body: BlockBody, request: Request):
    stats_service.block_user(body.user_id, reason=body.reason or "dashboard")
    _audit(request, "block_user", target=body.user_id)
    return {"ok": True}


@app.post("/api/unblock-user")
def api_unblock(body: BlockBody, request: Request):
    stats_service.unblock_user(body.user_id)
    _audit(request, "unblock_user", target=body.user_id)
    return {"ok": True}


# --------------------------------------------------------------------------------------
# System, settings, lists
# --------------------------------------------------------------------------------------

@app.get("/api/system-metrics")
def api_system_metrics():
    return system_service.get_system_metrics()


@app.get("/api/package-versions")
def api_package_versions():
    return system_service.get_package_versions_cached()


@app.get("/api/settings")
def api_settings():
    stored = overrides.load().get("values") or {}
    items = []
    for key, field in overrides.SCHEMA.items():
        current = getattr(Config, key, None)
        item: Dict[str, Any] = {"key": key, "section": field.section, "kind": field.kind,
                                "choices": list(field.choices), "overridden": key in stored}
        if field.kind == "secret":
            item["is_set"] = bool(current)
        else:
            item["value"] = current if isinstance(current, (str, int, float, bool, list)) or current is None else str(current)
        items.append(item)
    return {"items": items, "sections": list(overrides.SECTIONS), "username": security.current_username()}


@app.post("/api/settings")
def api_settings_save(request: Request, changes: Dict[str, Any] = Body(...)):
    if not changes or len(changes) > 80:
        return JSONResponse({"error": "invalid_request"}, status_code=422)
    clean, errors = overrides.save_values(changes)
    if errors:
        return JSONResponse({"error": "invalid_settings", "fields": errors}, status_code=400)
    overrides.apply(Config)
    stats_service.invalidate()
    _audit(request, "settings_saved", keys=sorted(clean))
    return {"ok": True, "saved": sorted(clean), "restart_required": True}


class ResetBody(BaseModel):
    keys: List[str] = Field(..., min_length=1, max_length=80)


@app.post("/api/settings/reset")
def api_settings_reset(body: ResetBody, request: Request):
    removed = overrides.reset_keys([k for k in body.keys if k in overrides.SCHEMA])
    overrides.apply(Config)
    _audit(request, "settings_reset", keys=removed)
    return {"ok": True, "reset": removed, "restart_required": bool(removed)}


@app.get("/api/lists-stats")
def api_lists_stats():
    return {**lists_service.get_lists_stats(), "can_run_script": lists_service.local_update_script() is not None}


@app.get("/api/domain-lists")
def api_domain_lists():
    return {"lists": lists_service.get_domain_lists(), "kinds": lists_service.EDITABLE_LISTS}


class DomainListBody(BaseModel):
    items: List[str] = Field(..., max_length=lists_service.MAX_ITEMS)


@app.post("/api/domain-lists/{name}")
def api_domain_list_save(name: str, body: DomainListBody, request: Request):
    if name not in lists_service.EDITABLE_LISTS:
        raise HTTPException(404)
    try:
        stored = lists_service.update_domain_list(name, body.items)
    except lists_service.ListError:
        # build the answer from the input, never from the exception text
        bad = lists_service.first_invalid_item(name, body.items)
        detail = f"invalid_item:{bad}" if bad is not None else "invalid_list"
        return JSONResponse({"error": "invalid_list", "detail": detail}, status_code=400)
    _audit(request, "domain_list_saved", target=name, count=len(stored))
    return {"ok": True, "count": len(stored), "restart_required": True}


# --------------------------------------------------------------------------------------
# Jobs
# --------------------------------------------------------------------------------------

class RestartBody(BaseModel):
    mode: str = Field(default="now", pattern="^(now|idle)$")


class ListUrlsBody(BaseModel):
    porn_domains: str = Field(default="", max_length=2000)
    porn_keywords: str = Field(default="", max_length=2000)


def _start(request: Request, kind: str, target, params=None, cancellable=False):
    try:
        job = jobs.manager.start(kind, _user(request), target, params, cancellable=cancellable)
    except jobs.JobBusy:
        # the running job's id comes from the job registry, not from the exception
        return JSONResponse({"error": "busy", "job_id": jobs.manager.running_id(kind)}, status_code=409)
    _audit(request, f"job_{kind}", mode=(params or {}).get("mode"))
    return {"ok": True, "job": job.public()}


@app.post("/api/jobs/restart-bot")
def api_job_restart_bot(body: RestartBody, request: Request):
    return _start(request, "restart-bot", jobs.restart_bot, {"mode": body.mode}, cancellable=body.mode == "idle")


@app.post("/api/jobs/restart-panel")
def api_job_restart_panel(request: Request):
    return _start(request, "restart-panel", jobs.restart_panel)


@app.post("/api/jobs/update-engines")
def api_job_update_engines(request: Request):
    return _start(request, "update-engines", jobs.update_engines)


@app.post("/api/jobs/update-lists")
def api_job_update_lists(request: Request, body: ListUrlsBody = Body(default=ListUrlsBody())):
    urls = {k: v.strip() for k, v in body.model_dump().items() if v.strip()}
    if not urls and lists_service.local_update_script() is None:
        return JSONResponse({"error": "need_urls"}, status_code=400)
    return _start(request, "update-lists", jobs.update_lists, {"urls": urls})


@app.get("/api/jobs")
def api_jobs():
    return {"jobs": jobs.manager.list()}


@app.get("/api/jobs/{job_id}")
def api_job(job_id: str):
    job = jobs.manager.get(job_id) if len(job_id) == 12 else None
    if job is None:
        raise HTTPException(404)
    return job.public()


@app.post("/api/jobs/{job_id}/cancel")
def api_job_cancel(job_id: str, request: Request):
    if not jobs.manager.cancel(job_id):
        return JSONResponse({"error": "not_cancellable"}, status_code=400)
    _audit(request, "job_cancel", target=job_id)
    return {"ok": True}


# --------------------------------------------------------------------------------------
# Browser: a live Chromium session the admin logs into; the bot reads its cookies
# --------------------------------------------------------------------------------------

from fastapi.responses import Response  # noqa: E402
from HELPERS import browser_session  # noqa: E402

_BROWSER_CLIENT_ERRORS = ("bad_url", "blocked_host", "bad_tab", "no_such_tab", "bad_action", "bad_input", "bad_key")
_BROWSER_STATE_ERRORS = ("not_running", "no_browser", "disabled")


def _browser_error_response(exc: Exception) -> JSONResponse:
    """Only fixed error codes reach the client, never text taken from the exception."""
    code = str(exc).split(":", 1)[0]
    for known in _BROWSER_CLIENT_ERRORS:
        if code == known:
            return JSONResponse({"error": known}, status_code=400)
    for known in _BROWSER_STATE_ERRORS:
        if code == known:
            return JSONResponse({"error": known}, status_code=409)
    logger.warning("[dashboard] browser: %s", exc)
    return JSONResponse({"error": "browser_error"}, status_code=502)


def _browser_call(fn, *args, **kwargs):
    """Run a browser action; a BrowserError becomes a short JSON error code."""
    try:
        return fn(*args, **kwargs), None
    except browser_session.BrowserError as exc:
        return None, _browser_error_response(exc)


class BrowserUrlBody(BaseModel):
    url: str = Field(default="about:blank", max_length=2048)


class BrowserTabBody(BaseModel):
    id: str = Field(..., min_length=8, max_length=64, pattern=r"^[A-Za-z0-9]+$")


class BrowserNavBody(BrowserTabBody):
    url: str = Field(..., min_length=1, max_length=2048)


class BrowserHistoryBody(BrowserTabBody):
    action: str = Field(..., pattern="^(back|forward|reload)$")


class BrowserInputBody(BrowserTabBody):
    kind: str = Field(..., pattern="^(click|dblclick|scroll|text|key)$")
    x: Optional[float] = Field(default=None, ge=0, le=5000)
    y: Optional[float] = Field(default=None, ge=0, le=5000)
    dx: float = Field(default=0, ge=-5000, le=5000)
    dy: float = Field(default=0, ge=-5000, le=5000)
    button: str = Field(default="left", pattern="^(left|right|middle)$")
    text: str = Field(default="", max_length=5000)
    key: str = Field(default="", max_length=20)
    ctrl: bool = False
    alt: bool = False
    shift: bool = False
    meta: bool = False


class BrowserClearBody(BaseModel):
    domain: Optional[str] = Field(default=None, max_length=253, pattern=r"^[A-Za-z0-9.-]+$")


@app.get("/api/browser")
def api_browser():
    data, err = _browser_call(browser_session.summary)
    return err or data


@app.post("/api/browser/start")
def api_browser_start(request: Request):
    data, err = _browser_call(browser_session.start)
    if err:
        return err
    _audit(request, "browser_start")
    return {"ok": True, **data}


@app.post("/api/browser/stop")
def api_browser_stop(request: Request):
    data, err = _browser_call(browser_session.stop)
    if err:
        return err
    _audit(request, "browser_stop")
    return {"ok": bool(data)}


@app.post("/api/browser/tab")
def api_browser_new_tab(body: BrowserUrlBody, request: Request):
    data, err = _browser_call(browser_session.new_tab, body.url)
    if err:
        return err
    if body.url != "about:blank":
        _audit(request, "browser_open", host=urlparse(browser_session.normalize_url(body.url)).hostname)
    return {"ok": True, **data}


@app.post("/api/browser/tab/close")
def api_browser_close_tab(body: BrowserTabBody):
    _, err = _browser_call(browser_session.close_tab, body.id)
    return err or {"ok": True}


@app.post("/api/browser/tab/activate")
def api_browser_activate(body: BrowserTabBody):
    _, err = _browser_call(browser_session.activate_tab, body.id)
    return err or {"ok": True}


@app.post("/api/browser/navigate")
def api_browser_navigate(body: BrowserNavBody, request: Request):
    _, err = _browser_call(browser_session.navigate, body.id, body.url)
    if err:
        return err
    _audit(request, "browser_navigate", host=urlparse(browser_session.normalize_url(body.url)).hostname)
    return {"ok": True}


@app.post("/api/browser/history")
def api_browser_history(body: BrowserHistoryBody):
    _, err = _browser_call(browser_session.history_step, body.id, body.action)
    return err or {"ok": True}


@app.post("/api/browser/input")
def api_browser_input(body: BrowserInputBody):
    params = body.model_dump(exclude={"id", "kind"})
    _, err = _browser_call(browser_session.send_input, body.id, body.kind, **params)
    return err or {"ok": True}


@app.get("/api/browser/screen")
def api_browser_screen(id: str = Query(..., min_length=8, max_length=64, pattern=r"^[A-Za-z0-9]+$")):
    data, err = _browser_call(browser_session.screenshot, id)
    if err:
        return err
    return Response(content=data, media_type="image/jpeg", headers={"Cache-Control": "no-store"})


@app.post("/api/browser/cookies/clear")
def api_browser_clear(body: BrowserClearBody, request: Request):
    data, err = _browser_call(browser_session.clear_cookies, body.domain)
    if err:
        return err
    _audit(request, "browser_cookies_clear", domain=body.domain or "*", removed=data)
    return {"ok": True, "removed": data}
