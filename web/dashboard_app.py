from __future__ import annotations

import pathlib
import logging
from typing import Any, List

from fastapi import FastAPI, HTTPException, Query, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from CONFIG.config import Config
from services import stats_service
from services import system_service, lists_service
from services.auth_service import get_auth_service

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = pathlib.Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app = FastAPI(title="TG YTDLP Dashboard", version="2.0.0", docs_url=None, redoc_url=None, openapi_url=None)

# Используем кастомный StaticFiles с cache-control для статики.
class CachedStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        response = await super().get_response(path, scope)
        if response.status_code == 200:
            response.headers["Cache-Control"] = "public, max-age=86400"
        return response


app.mount("/static", CachedStaticFiles(directory=str(BASE_DIR / "static")), name="static")


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Добавляет security-заголовки ко всем ответам."""

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault("Permissions-Policy", "geolocation=(), microphone=(), camera=()")
        # CSP: script-src — только self (no inline scripts / handlers).
        # style-src — 'unsafe-inline' разрешён, т.к. JS генерирует динамический контент со стилями.
        response.headers.setdefault(
            "Content-Security-Policy",
            "default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self'; "
            "connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'",
        )
        return response


class AuthMiddleware(BaseHTTPMiddleware):
    """Проверяет авторизацию для всех путей, кроме публичных."""

    PUBLIC_PREFIXES = ("/login", "/api/login", "/static", "/health")

    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        if any(path.startswith(prefix) for prefix in self.PUBLIC_PREFIXES):
            return await call_next(request)

        token = request.cookies.get("auth_token")
        auth_service = get_auth_service()

        if not token or not auth_service.verify_token(token):
            if path.startswith("/api/"):
                return JSONResponse(status_code=401, content={"detail": "Unauthorized"})
            return RedirectResponse(url="/login", status_code=302)

        response = await call_next(request)
        if path != "/api/logout":
            response.set_cookie(
                key="auth_token",
                value=token,
                httponly=True,
                secure=getattr(Config, "DASHBOARD_COOKIE_SECURE", False),
                samesite="lax",
                max_age=auth_service.session_ttl,
            )
        return response


# Порядок важен: security-заголовки применяются последними (внешний middleware).
app.add_middleware(AuthMiddleware)
app.add_middleware(SecurityHeadersMiddleware)


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html")


class LoginRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=128)
    password: str = Field(..., min_length=1, max_length=256)


@app.post("/api/login")
async def api_login(payload: LoginRequest, request: Request):
    auth_service = get_auth_service()
    auth_service.reload_config()
    client_ip = request.client.host if request.client else "unknown"

    try:
        token = auth_service.login(payload.username, payload.password, client_ip)
    except ValueError as e:
        return JSONResponse(status_code=401, content={"detail": str(e)})

    response = JSONResponse(content={"status": "ok"})
    response.set_cookie(
        key="auth_token",
        value=token,
        httponly=True,
        secure=getattr(Config, "DASHBOARD_COOKIE_SECURE", False),
        samesite="lax",
        max_age=auth_service.session_ttl,
    )
    return response


@app.post("/api/reset-lockdown")
async def api_reset_lockdown(request: Request):
    """Сбрасывает блокировку для текущего IP. Требует авторизации."""
    auth_service = get_auth_service()
    client_ip = request.client.host if request.client else "unknown"
    auth_service.reset_lockdown(client_ip)
    return {"status": "ok", "message": f"Lockdown reset for IP {client_ip}"}


@app.post("/api/logout")
async def api_logout(request: Request):
    token = request.cookies.get("auth_token")
    if token:
        auth_service = get_auth_service()
        auth_service.logout(token)
    response = JSONResponse(content={"status": "ok"})
    response.delete_cookie("auth_token")
    return response


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {
            "title": "Bot statistics",
            "config": {
                "STATS_ACTIVE_TIMEOUT": getattr(Config, "STATS_ACTIVE_TIMEOUT", 900),
            },
        },
    )


# ---------------------------------------------------------------------------
# Statistics API
# ---------------------------------------------------------------------------

@app.get("/api/active-users")
async def api_active_users(
    limit: int = 10,
    minutes: int | None = Query(default=None, ge=1, le=3600),
):
    return stats_service.fetch_active_users(limit=limit, minutes=minutes)


@app.get("/api/top-downloaders")
async def api_top_downloaders(
    period: str = Query(default="today", pattern="^(today|week|month|all)$"),
    limit: int = 10,
):
    return stats_service.fetch_top_downloaders(period=period, limit=limit)


@app.get("/api/top-domains")
async def api_top_domains(period: str = "today", limit: int = 10):
    return stats_service.fetch_top_domains(period=period, limit=limit)


@app.get("/api/top-countries")
async def api_top_countries(period: str = "today", limit: int = 10):
    return stats_service.fetch_top_countries(period=period, limit=limit)


@app.get("/api/gender-stats")
async def api_gender_stats(period: str = "today"):
    return stats_service.fetch_gender_stats(period)


@app.get("/api/age-stats")
async def api_age_stats(period: str = "today"):
    return stats_service.fetch_age_stats(period)


@app.get("/api/channel-join-stats")
async def api_channel_join_stats(period: str = "today"):
    return stats_service.fetch_channel_join_stats(period)


@app.get("/api/top-nsfw-users")
async def api_nsfw_users(limit: int = 10):
    return stats_service.fetch_top_nsfw_users(limit)


@app.get("/api/top-nsfw-domains")
async def api_nsfw_domains(limit: int = 10):
    return stats_service.fetch_top_nsfw_domains(limit)


@app.get("/api/top-playlist-users")
async def api_playlist_users(limit: int = 10):
    return stats_service.fetch_top_playlist_users(limit)


@app.get("/api/top-multi-url-users")
async def api_multi_url_users(
    period: str = Query(default="today", pattern="^(today|week|month|all)$"),
    limit: int = 10,
):
    return stats_service.fetch_top_multi_url_users(period=period, limit=limit)


@app.get("/api/format-users")
async def api_format_users(limit: int = 20):
    return stats_service.fetch_format_users(limit=limit)


@app.get("/api/power-users")
async def api_power_users(min_urls: int = 10, days: int = 7, limit: int = 10):
    return stats_service.fetch_power_users(min_urls=min_urls, days=days, limit=limit)


@app.get("/api/blocked-users")
async def api_blocked_users(limit: int = 50):
    return stats_service.fetch_blocked_users(limit)


@app.get("/api/channel-events")
async def api_channel_events(hours: int = 48, limit: int = 100):
    return stats_service.fetch_recent_channel_events(hours=hours, limit=limit)


@app.get("/api/suspicious-users")
async def api_suspicious_users(
    period: str = Query(default="today", pattern="^(today|week|month|all)$"),
    limit: int = 20,
):
    return stats_service.fetch_suspicious_users(period=period, limit=limit)


@app.get("/api/user-history")
async def api_user_history(
    user_id: int = Query(..., gt=0),
    period: str = Query(default="all", pattern="^(today|week|month|all)$"),
    limit: int = Query(default=100, le=1000),
):
    return stats_service.fetch_user_history(user_id, period, limit)


class BlockRequest(BaseModel):
    user_id: int = Field(..., gt=0)
    reason: str | None = Field(default=None, max_length=120)


@app.post("/api/block-user")
async def api_block_user(payload: BlockRequest):
    try:
        stats_service.block_user(payload.user_id, reason=payload.reason or "manual")
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"status": "ok"}


@app.post("/api/unblock-user")
async def api_unblock_user(payload: BlockRequest):
    try:
        stats_service.unblock_user(payload.user_id)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# System API
# ---------------------------------------------------------------------------

@app.get("/api/system-metrics")
async def api_system_metrics():
    return system_service.get_system_metrics()


@app.get("/api/package-versions")
async def api_package_versions():
    return system_service.get_package_versions()


@app.get("/api/config-settings")
async def api_config_settings():
    return system_service.get_config_settings()


class ConfigUpdateRequest(BaseModel):
    key: str = Field(...)
    value: Any


@app.post("/api/update-config")
async def api_update_config(payload: ConfigUpdateRequest):
    try:
        success = system_service.update_config_setting(payload.key, payload.value)
        if not success:
            raise HTTPException(status_code=400, detail="Failed to update config")
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"status": "ok"}


@app.get("/api/lists-stats")
async def api_lists_stats():
    return lists_service.get_lists_stats()


@app.get("/api/domain-lists")
async def api_domain_lists():
    return lists_service.get_domain_lists()


class DomainListUpdateRequest(BaseModel):
    list_name: str = Field(...)
    items: List[str] = Field(...)


class ListsUpdateFromUrlsRequest(BaseModel):
    porn_domains_url: str = ""
    porn_keywords_url: str = ""


@app.post("/api/update-domain-list")
async def api_update_domain_list(payload: DomainListUpdateRequest):
    try:
        success = lists_service.update_domain_list(payload.list_name, payload.items)
        if not success:
            raise HTTPException(status_code=400, detail="Failed to update domain list")
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"status": "ok"}


@app.post("/api/rotate-ip")
async def api_rotate_ip():
    return system_service.rotate_ip()


@app.post("/api/restart-service")
async def api_restart_service():
    return system_service.restart_service()


@app.post("/api/restart-panel")
async def api_restart_panel():
    return system_service.restart_panel()


@app.post("/api/update-engines")
async def api_update_engines():
    return system_service.update_engines()


@app.post("/api/cleanup-user-files")
async def api_cleanup_user_files():
    return system_service.cleanup_user_files()


@app.post("/api/update-lists")
async def api_update_lists():
    return lists_service.update_lists()


@app.post("/api/update-lists-from-urls")
async def api_update_lists_from_urls(payload: ListsUpdateFromUrlsRequest):
    return lists_service.update_lists_from_urls(payload.porn_domains_url, payload.porn_keywords_url)


@app.get("/health")
async def health():
    return {"status": "ok"}
