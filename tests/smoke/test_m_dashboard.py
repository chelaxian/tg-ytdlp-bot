"""Smoke test of the dashboard: auth, CSRF, headers, secrets, validation, speed.

Run: python tests/smoke/test_m_dashboard.py   (needs fastapi, httpx)
"""
import ast
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
from dashboard_fixture import DEMO_PASSWORD, DEMO_USER, TMP, Config, install_stubs  # noqa: E402

app, collector = install_stubs()
from fastapi.testclient import TestClient  # noqa: E402

from CONFIG import overrides  # noqa: E402
from services import lists_service  # noqa: E402
from web import security  # noqa: E402

ok = fail = 0
BASE = "http://testserver"
SAME = {"Origin": BASE}


def check(name, cond, info=""):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name} {info}")


def client():
    return TestClient(app, base_url=BASE)


def login(c, user=DEMO_USER, password=DEMO_PASSWORD):
    r = c.post("/api/login", json={"username": user, "password": password}, headers=SAME)
    if r.status_code != 200:
        return r, None
    return r, c.get("/api/session").json()["csrf"]


# ---------------------------------------------------------------- unauthenticated
c = client()
check("api requires auth", c.get("/api/overview").status_code == 401)
check("page redirects to login", c.get("/", follow_redirects=False).status_code == 303)
r = c.get("/login")
check("login page renders", r.status_code == 200 and "login.js" in r.text)
csp = r.headers.get("content-security-policy", "")
check("strict CSP: no unsafe-inline", "unsafe-inline" not in csp and "script-src 'self'" in csp and "frame-ancestors 'none'" in csp)
check("security headers", r.headers.get("x-frame-options") == "DENY" and r.headers.get("x-content-type-options") == "nosniff")
check("no docs/openapi", c.get("/docs", follow_redirects=False).status_code in (303, 401, 404) and c.get("/openapi.json", follow_redirects=False).status_code in (303, 401, 404))
check("health is public", c.get("/health").json() == {"status": "ok"})
check("login without Origin rejected", c.post("/api/login", json={"username": DEMO_USER, "password": DEMO_PASSWORD}).status_code == 403)
check("login from other origin rejected",
      c.post("/api/login", json={"username": DEMO_USER, "password": DEMO_PASSWORD}, headers={"Origin": "https://evil.example"}).status_code == 403)

# ---------------------------------------------------------------- throttling
c = client()
codes = [c.post("/api/login", json={"username": DEMO_USER, "password": "wrong"}, headers=SAME).status_code for _ in range(5)]
check("first wrong attempts are 401", codes == [401] * 5, codes)
r = c.post("/api/login", json={"username": DEMO_USER, "password": DEMO_PASSWORD}, headers=SAME)
check("locked after 5 failures, even with the right password", r.status_code == 429 and r.json().get("retry_after", 0) <= 60, r.text)
security.throttle = security.LoginThrottle()

# ---------------------------------------------------------------- session + CSRF
c = client()
r, csrf = login(c)
check("login ok", r.status_code == 200 and csrf, r.text)
cookie = r.headers.get("set-cookie", "")
check("session cookie HttpOnly + SameSite=Strict", "httponly" in cookie.lower() and "samesite=strict" in cookie.lower())
check("session file has no raw token", c.cookies.get(security.SESSION_COOKIE) not in (TMP / ".dashboard_sessions.json").read_text())
H = {**SAME, "X-CSRF-Token": csrf}
check("POST without CSRF rejected", c.post("/api/block-user", json={"user_id": 5}, headers=SAME).status_code == 403)
check("POST with wrong CSRF rejected", c.post("/api/block-user", json={"user_id": 5}, headers={**SAME, "X-CSRF-Token": "x"}).status_code == 403)
check("POST with CSRF ok", c.post("/api/block-user", json={"user_id": 5}, headers=H).status_code == 200)
check("unblock ok", c.post("/api/unblock-user", json={"user_id": 5}, headers=H).status_code == 200)
check("audit log written", (TMP / ".dashboard_audit.log").exists() and "block_user" in (TMP / ".dashboard_audit.log").read_text())

# ---------------------------------------------------------------- reads: shape, bounds, speed
paths = ["/api/overview", "/api/active-users?minutes=15&limit=50", "/api/top-downloaders?period=week&limit=200",
         "/api/top-domains?period=all", "/api/top-countries", "/api/gender-stats", "/api/age-stats", "/api/channel-join-stats",
         "/api/top-nsfw-users", "/api/top-nsfw-domains", "/api/top-playlist-users", "/api/top-multi-url-users",
         "/api/format-users", "/api/power-users?min_urls=5&days=3", "/api/suspicious-users", "/api/blocked-users",
         "/api/channel-events", "/api/user-history?user_id=100001", "/api/system-metrics", "/api/package-versions",
         "/api/settings", "/api/lists-stats", "/api/domain-lists", "/api/jobs"]
slow = []
for p in paths:
    t = time.perf_counter()
    r = c.get(p)
    dt = (time.perf_counter() - t) * 1000
    if r.status_code != 200:
        check(f"GET {p}", False, r.status_code)
    elif dt > 1500:
        slow.append((p, round(dt)))
check("all GET endpoints answer 200", True)
check("all GET endpoints fast", not slow, slow)
check("bad period -> 422", c.get("/api/top-domains?period=year").status_code == 422)
check("limit bound -> 422", c.get("/api/top-domains?limit=100000").status_code == 422)
check("user_id bound -> 422", c.get("/api/user-history?user_id=-1").status_code == 422)

# The production preview must reject every administrative mutation, even with a valid session and CSRF.
from web import dashboard_app as dashboard_module
dashboard_module.PREVIEW_READ_ONLY = True
for path, body in [("/api/block-user", {"user_id": 5}), ("/api/settings", {"PROXY_IP": "example.com"}),
                   ("/api/jobs/restart-bot", {"mode": "now"}), ("/api/jobs/update-engines", {})]:
    r = c.post(path, json=body, headers=H)
    check(f"preview blocks {path}", r.status_code == 403 and r.json().get("error") == "preview_read_only")
check("preview retains read access", c.get("/api/overview").status_code == 200)
dashboard_module.PREVIEW_READ_ONLY = False

# ---------------------------------------------------------------- secrets never leave the server
settings = c.get("/api/settings").json()
blob = str(settings)
check("proxy password not returned", "secret-proxy-pass" not in blob)
check("bot token not returned", "SECRET-TOKEN" not in blob and "BOT_TOKEN" not in blob)
check("dashboard password not returned", DEMO_PASSWORD not in blob)
check("ADMIN not editable", "ADMIN" not in {i["key"] for i in settings["items"]})
pw = next(i for i in settings["items"] if i["key"] == "PROXY_PASSWORD")
check("secret shown as is_set only", pw.get("is_set") is True and "value" not in pw)

# ---------------------------------------------------------------- settings: typed, no code injection
evil = {
    "PROXY_IP": 'x" ; __import__("os").system("id") #',
    "PROXY_PORT": "1; import os",
    "LOGS_ID": "__import__('os')",
    "MINIAPP_URL": "javascript:alert(1)",
    "PROXY_USER": "a\nADMIN = [1]",
    "ALLOWED_GROUP": ["1, __import__('os')"],
}
for key, value in evil.items():
    r = c.post("/api/settings", json={key: value}, headers=H)
    check(f"rejects injection in {key}", r.status_code == 400 and key in r.json().get("fields", {}), r.text)
check("rejects unknown key ADMIN", c.post("/api/settings", json={"ADMIN": [5]}, headers=H).status_code == 400)
r = c.post("/api/settings", json={"PROXY_IP": "203.0.113.7", "PROXY_PORT": "8080", "ALLOWED_GROUP": "-1001, -1002",
                                   "PROXY_PASSWORD": "newsecret"}, headers=H)
check("valid settings saved", r.status_code == 200, r.text)
stored = overrides.load()["values"]
check("stored typed values", stored.get("PROXY_PORT") == 8080 and stored.get("ALLOWED_GROUP") == [-1001, -1002], stored)
check("applied to Config", Config.PROXY_IP == "203.0.113.7" and Config.PROXY_PASSWORD == "newsecret")
check("overrides file is JSON, not Python", (TMP / ".dashboard_overrides.json").read_text().lstrip().startswith("{"))
r = c.post("/api/settings/reset", json={"keys": ["PROXY_IP"]}, headers=H)
check("reset to config.py", r.status_code == 200 and Config.PROXY_IP == "" and "PROXY_IP" not in overrides.load()["values"])
(TMP / ".dashboard_overrides.json").write_text('{"values": {"PROXY_PORT": "oops", "LOGS_ID": -5, "ADMIN": [9]}}')
before_admin = list(Config.ADMIN)
overrides.apply(Config)
check("damaged overrides file never crashes / never sets ADMIN", Config.LOGS_ID == -5 and Config.ADMIN == before_admin)

# ---------------------------------------------------------------- domain lists
r = c.post("/api/domain-lists/WHITELIST", json={"items": ["example.com", "Sub.Example.org"]}, headers=H)
check("domain list saved", r.status_code == 200, r.text)
src = lists_service.DOMAINS_FILE.read_text(encoding="utf-8")
tree = ast.parse(src)
check("domains.py still valid Python", True)
check("list content stored", lists_service.get_domain_lists()["WHITELIST"] == ["example.com", "sub.example.org"])
for bad in ['x",\n__import__("os")#', "a\nb", 'evil"]; import os; x=["', "\\x"]:
    r = c.post("/api/domain-lists/WHITELIST", json={"items": [bad]}, headers=H)
    check(f"rejects bad list item {bad[:12]!r}", r.status_code == 400)
check("domains.py untouched by rejected writes", lists_service.DOMAINS_FILE.read_text(encoding="utf-8") == src)
check("unknown list -> 404", c.post("/api/domain-lists/CDN_REJECT_DOMAINS", json={"items": []}, headers=H).status_code == 404)

# ---------------------------------------------------------------- jobs
from services import jobs  # noqa: E402

started = []


def slow_job(job):
    started.append(job.id)
    time.sleep(0.5)
    return "done"


j1 = jobs.manager.start("demo", "t", slow_job)
try:
    jobs.manager.start("demo", "t", slow_job)
    check("second job of the same kind is refused", False)
except jobs.JobBusy:
    check("second job of the same kind is refused", True)
time.sleep(0.8)
check("job finished", jobs.manager.get(j1.id).state == "succeeded")
check("list update without URLs in docker mode -> need_urls",
      c.post("/api/jobs/update-lists", json={}, headers=H).json().get("error") == "need_urls")

# ---------------------------------------------------------------- password change + forced change
r = c.post("/api/change-password", json={"current_password": "nope", "new_password": "x" * 12}, headers=H)
check("wrong current password refused", r.status_code == 400 and r.json()["error"] == "wrong_current_password")
r = c.post("/api/change-password", json={"current_password": DEMO_PASSWORD, "new_password": "short"}, headers=H)
check("short password refused", r.status_code == 400 and r.json()["error"] == "too_short")
r = c.post("/api/change-password", json={"current_password": DEMO_PASSWORD, "new_password": "a-much-better-pass"}, headers=H)
check("password changed", r.status_code == 200)
auth = overrides.get_auth()
check("password stored as hash", auth["password_hash"].startswith("pbkdf2_sha256$") and "a-much-better-pass" not in str(auth))
c2 = client()
check("old password no longer works", login(c2)[0].status_code == 401)
check("new password works", login(c2, password="a-much-better-pass")[0].status_code == 200)
(TMP / ".dashboard_overrides.json").unlink()
Config.DASHBOARD_PASSWORD = "admin123"
security.throttle = security.LoginThrottle()
c3 = client()
r, csrf3 = login(c3, password="admin123")
check("default password logs in only to change it", r.status_code == 200 and r.json()["must_change_password"] is True)
check("other APIs blocked until changed", c3.get("/api/overview").status_code == 403)

H = {**SAME, "X-CSRF-Token": c.get("/api/session").json()["csrf"]}  # new session after the password change
c.post("/api/logout", headers=H)
check("logout ends session", c.get("/api/overview").status_code == 401)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
