"""Smoke test: the web dashboard and the browser integration are optional.

The bot must import and run without fastapi / uvicorn / jinja2 / psutil / a browser, the cookie helper must never
raise, and the packaging (requirements, Dockerfile, compose) must keep the panel off by default.

Run: python tests/smoke/test_v_optional_dashboard.py   (offline)
"""
import ast
import logging
import os
import subprocess
import sys
import textwrap

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ok = fail = 0


def check(name, cond, info=""):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name} {info}")


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


# ---- 1. bot-side modules import with every panel package blocked
PROBE = textwrap.dedent('''
    import importlib.abc, sys, types

    BLOCKED = ("fastapi", "starlette", "uvicorn", "jinja2", "psutil", "multipart", "pydantic")

    class Block(importlib.abc.MetaPathFinder):
        def find_spec(self, name, path=None, target=None):
            if name.split(".")[0] in BLOCKED:
                raise ImportError(f"{name} is blocked (optional dashboard package)")

    sys.meta_path.insert(0, Block())
    sys.path.insert(0, ROOT)

    cfg = types.ModuleType("CONFIG.config")
    cfg.Config = type("Config", (), {})
    sys.modules["CONFIG.config"] = cfg
    cache_db = types.ModuleType("DATABASE.cache_db")
    cache_db.get_next_reload_time = lambda hours: None
    sys.modules["DATABASE.cache_db"] = cache_db

    # bot internals that pull Pyrogram: not what is checked here
    import logging
    fb = types.ModuleType("DATABASE.firebase_init"); fb.db = None; fb.is_user_blocked = lambda *a, **k: False
    sys.modules["DATABASE.firebase_init"] = fb
    cg = types.ModuleType("HELPERS.channel_guard"); cg.get_channel_guard = lambda: None
    sys.modules["HELPERS.channel_guard"] = cg
    lg = types.ModuleType("HELPERS.logger"); lg.logger = logging.getLogger("probe")
    sys.modules["HELPERS.logger"] = lg

    import importlib
    for name in ("services.system_service", "services.stats_collector", "services.stats_events", "services.stats_service",
                 "services.lists_service", "HELPERS.browser_session", "HELPERS.runtime_status"):
        importlib.import_module(name)
    from services import system_service
    assert system_service.psutil is None, "psutil should be optional"
    assert "error" in system_service.get_system_metrics()
    assert system_service.get_network_speed() == {"speed_sent_mbps": 0, "speed_recv_mbps": 0}
    leaked = [m for m in sys.modules if m.split(".")[0] in BLOCKED]
    assert not leaked, leaked
    from HELPERS import browser_session as bs
    assert bs.enabled() in (True, False)
    assert bs.is_running() is False          # no browser, no dashboard: simply "not running"
    print("PROBE-OK")
''')
env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
proc = subprocess.run([sys.executable, "-I", "-c", f"ROOT = {ROOT!r}\n" + PROBE], capture_output=True, text=True, env=env,
                      cwd=ROOT, timeout=60)
check("bot-side modules import without the panel packages", "PROBE-OK" in proc.stdout, (proc.stdout + proc.stderr)[-600:])

# ---- 2. the cookie helper never raises
src = read("COMMANDS/cookies_cmd.py")
tree = ast.parse(src)
wanted = {"_save_live_browser_cookies"}
fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "_save_live_browser_cookies")
ns = {"logger": logging.getLogger("t")}


def boom(*a, **k):
    raise ImportError("HELPERS.browser_session is missing")


ns["_save_live_browser_cookies_impl"] = boom
exec(ast.get_source_segment(src, fn), ns)
check("helper answers 'unavailable' instead of raising", ns["_save_live_browser_cookies"](None, 1) == "unavailable")
ns["_save_live_browser_cookies_impl"] = lambda *a, **k: (_ for _ in ()).throw(OSError("refused"))
check("helper survives a refused connection", ns["_save_live_browser_cookies"](None, 1, ["vk"]) == "unavailable")
ns["_save_live_browser_cookies_impl"] = lambda *a, **k: "saved"
check("helper passes a normal answer through", ns["_save_live_browser_cookies"](None, 1) == "saved")

# ---- 3. packaging keeps the panel optional
req = [ln.strip() for ln in read("requirements.txt").splitlines() if ln.strip() and not ln.startswith("#")]
panel = {"fastapi", "uvicorn[standard]", "jinja2", "python-multipart", "psutil"}
check("requirements.txt has no panel packages", not (panel & set(req)), sorted(panel & set(req)))
dash_req = {ln.strip() for ln in read("requirements-dashboard.txt").splitlines() if ln.strip() and not ln.startswith("#")}
check("requirements-dashboard.txt has them", panel <= dash_req, dash_req)
docker = read("Dockerfile")
check("Dockerfile: dashboard and browser are off by default",
      "ARG INSTALL_DASHBOARD=0" in docker and "ARG INSTALL_BROWSER=0" in docker)
base_apt = docker.split("RUN apt-get update && apt-get install -y --no-install-recommends \\\n", 1)[1].split("&&", 1)[0]
check("Dockerfile: the docker CLI package only with the dashboard", base_apt.split().count("docker.io") == 0 and docker.count("install -y --no-install-recommends docker.io") == 1)
compose = read("docker-compose.yml")
dash_block = compose.split("  dashboard:\n", 1)[1].split("\n  bgutil-provider:", 1)[0]
check("compose: dashboard is a profile (not started by `up -d`)", 'profiles: ["dashboard"]' in dash_block)
check("compose: dashboard image installs the panel", 'INSTALL_DASHBOARD: "1"' in dash_block)
bot_block = compose.split("  bot:\n", 1)[1].split("\n  # OPTIONAL web dashboard", 1)[0]
check("compose: the bot does not depend on the dashboard", "dashboard" not in bot_block)
check("bot entrypoint does not start the panel", "uvicorn" not in read("scripts/docker-entrypoint.sh"))
check("update script keeps an installed dashboard", "COMPOSE_PROFILES=dashboard" in read("scripts/UPDATE_DOCKER.sh"))
check("requirements-dashboard.txt travels with updates", "requirements-dashboard.txt" in read("scripts/update_from_repo.py"))

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
