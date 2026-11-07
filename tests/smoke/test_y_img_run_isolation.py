"""Smoke test: parallel /img runs of one user must not delete each other's files.

Both runs live under users/<id>/<domain>/<unique>/. The pre-cleanup of a newly
started run (remove_media) used to rmtree the shared users/<id>/<domain>/ because
only the unique directory carried a protection file, destroying the files of the
run that was still downloading/sending ("Failed to decode ... The value does not
represent an existing local file", observed 2026-11-07 on DE).

Run from the bot root: python tests/smoke/test_y_img_run_isolation.py
"""
import ast
import importlib.util
import logging
import os
import shutil
import sys
import tempfile
from types import SimpleNamespace

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

def _install_stubs():
    """Offline stand-ins for Telegram/config modules (CONFIG/config.py holds secrets)."""
    import types

    class _Msgs(type):
        def __getattr__(cls, name):
            return ""

    def module(name, **attrs):
        mod = types.ModuleType(name)
        mod.__dict__.update(attrs)
        sys.modules[name] = mod
        return mod

    class Config:
        ADMIN = []

    class LoggerMsg(metaclass=_Msgs):
        pass

    module("HELPERS.app_instance", get_app=lambda: None)
    module("HELPERS.logger", logger=logging.getLogger("img-isolation-test"))
    module("HELPERS.limitter", humanbytes=str)
    module("CONFIG.config", Config=Config)
    module("CONFIG.logger_msg", LoggerMsg=LoggerMsg)
    pyrogram = module("pyrogram")
    pyrogram.enums = module("pyrogram.enums")


def _load_filesystem_hlp():
    spec = importlib.util.spec_from_file_location("HELPERS.filesystem_hlp", os.path.join(ROOT, "HELPERS", "filesystem_hlp.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["HELPERS.filesystem_hlp"] = mod  # image_cmd imports it lazily: same registry
    spec.loader.exec_module(mod)
    return mod


try:
    fs = _load_filesystem_hlp()
except ImportError:  # no bot venv / no CONFIG/config.py: run against stubs
    _install_stubs()
    fs = _load_filesystem_hlp()

# the real _cleanup_run_dir, taken from the source without importing Telegram
src = open(os.path.join(ROOT, "COMMANDS", "image_cmd.py"), encoding="utf-8").read()
node = next(n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef) and n.name == "_cleanup_run_dir")
env = {"os": os, "shutil": shutil, "logger": logging.getLogger("t")}
exec(compile(ast.Module(body=[node], type_ignores=[]), "image_cmd", "exec"), env)
cleanup_run_dir = env["_cleanup_run_dir"]

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


UID = 990000002
message = SimpleNamespace(chat=SimpleNamespace(id=UID))


def make_runs(tmp):
    runs = []
    for name in ("fd_100_1111", "fd_200_2222"):
        run = os.path.join("users", str(UID), "2ch.su", name)
        os.makedirs(run)
        with open(os.path.join(run, "pic.jpg"), "w") as f:
            f.write("x")
        runs.append(run)
    return runs


def in_tmp(fn):
    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        os.chdir(tmp)
        try:
            fn(tmp)
        finally:
            os.chdir(cwd)


fs.is_parallel_download_allowed = lambda m: True  # admin / group: the case that lost files


def unregistered(tmp):
    a, b = make_runs(tmp)
    fs.remove_media(message)
    check("old behaviour: unregistered runs are wiped by a parallel pre-cleanup",
          not os.path.exists(a) and not os.path.exists(b))


def registered(tmp):
    a, b = make_runs(tmp)
    fs.acquire_download_dir(a)
    fs.acquire_download_dir(b)
    fs.remove_media(message)
    check("registered runs survive a parallel pre-cleanup",
          os.path.exists(os.path.join(a, "pic.jpg")) and os.path.exists(os.path.join(b, "pic.jpg")))

    cleanup_run_dir(a)  # run A finishes
    check("finished run A is gone, its own registration released", not os.path.exists(a)
          and not fs.is_download_dir_in_use(a))
    check("shared parent stays while run B is active", os.path.isdir(os.path.dirname(b)))
    fs.remove_media(message)
    check("run B still intact after another pre-cleanup", os.path.exists(os.path.join(b, "pic.jpg")))

    cleanup_run_dir(b)  # run B finishes
    check("no litter: shared parent removed once the last run is done",
          not os.path.exists(os.path.join("users", str(UID), "2ch.su")))
    check("registry is empty", not fs._ACTIVE_DOWNLOAD_DIRS)


def double_release_is_harmless(tmp):
    a, _b = make_runs(tmp)
    fs.acquire_download_dir(a)
    cleanup_run_dir(a)
    cleanup_run_dir(a)  # the except-path and the finally both call it
    fs.release_download_dir(a)
    check("repeated cleanup/release does not corrupt the registry", not fs._ACTIVE_DOWNLOAD_DIRS)


for scenario in (unregistered, registered, double_release_is_harmless):
    fs._ACTIVE_DOWNLOAD_DIRS.clear()
    in_tmp(scenario)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
