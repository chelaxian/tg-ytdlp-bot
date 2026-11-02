"""Offline integration: the bot's DB helpers on the sqlite and json engines.

Each engine runs in its own subprocess (the DB modules initialise at import).
No Telegram: messages are stubs, app is not started.
Run: python test_g_db_integration.py [repo_root]
"""
import json
import os
import subprocess
import sys
import tempfile
import types

REPO = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])


def check(name, cond, detail=""):
    if not cond:
        raise AssertionError(f"FAIL {name}: {detail}")
    print(f"ok  {name}")


def child(engine, workdir):
    sys.path.insert(0, REPO)
    os.chdir(workdir)
    from CONFIG.config import Config
    Config.USE_FIREBASE = False
    Config.DB_ENGINE = engine
    Config.SQLITE_DB_PATH = os.path.join(workdir, "bot.sqlite3")
    Config.FIREBASE_CACHE_FILE = os.path.join(workdir, "dump.json")
    Config.BOT_NAME_FOR_USERS = "testbot"
    t = lambda n, c, d="": check(f"{engine}:{n}", c, d)

    import DATABASE.firebase_init as fi
    import DATABASE.cache_db as cdb
    from DATABASE.db_mode import active_engine
    t("engine_selected", active_engine() == engine, active_engine())
    t("sql_store_only_for_sql", (fi.get_sql_store() is not None) == (engine != "json"))

    msg = lambda uid: types.SimpleNamespace(chat=types.SimpleNamespace(id=uid, first_name="T"), from_user=None)
    fi.check_user(msg(111))
    t("check_user_registers", fi._user_list_has("users", 111))
    t("not_blocked", fi.is_user_blocked(msg(111)) is False)
    fi.db.child("bot").child("testbot").child("blocked_users").child("111").set({"ID": "111", "timestamp": "1"})
    if engine == "json":
        cdb.reload_firebase_cache()
    t("blocked_after_write", fi.is_user_blocked(msg(111)) is True)
    fi.db.child("bot").child("testbot").child("unblocked_users").child("111").set({"ID": "111"})
    if engine == "json":
        cdb.reload_firebase_cache()
    t("unblocked_overrides", fi.is_user_blocked(msg(111)) is False)
    t("not_ignored", fi.is_user_ignored(msg(111)) is False)

    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    cdb.save_to_video_cache(url, "720p", [4242])
    t("video_cache_visible_immediately", cdb.get_cached_message_ids(url, "720p") == [4242],
      cdb.get_cached_message_ids(url, "720p"))
    cdb.save_to_video_cache(url, "1080p", [1, 2, 3])
    t("split_video_cache", cdb.get_cached_message_ids(url, "1080p") == [1, 2, 3])

    # json: users written through db.child() must survive the next mirror sync
    fi.check_user(msg(222))
    cdb.save_to_video_cache("https://example.com/v.mp4", "best", [7])
    if engine == "json":
        with open(Config.FIREBASE_CACHE_FILE, encoding="utf-8") as f:
            on_disk = json.load(f)
        users = on_disk["bot"]["testbot"]["users"]
        t("json_users_survive_cache_sync", "111" in users and "222" in users, list(users))
    else:
        t("no_dump_written_in_sql_mode", not os.path.exists(Config.FIREBASE_CACHE_FILE))
        from services.stats_collector import _load_bot_tree_from_sql
        tree = _load_bot_tree_from_sql()
        t("stats_reads_sql", "222" in tree["bot"]["testbot"]["users"], tree)
    print("CHILD OK")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        child(sys.argv[2], sys.argv[3])
        sys.exit(0)
    for engine in ("sqlite", "json"):
        wd = tempfile.mkdtemp(prefix=f"dbint_{engine}_")
        r = subprocess.run([sys.executable, __file__, REPO, engine, wd], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=300)
        out = "\n".join(l for l in r.stdout.splitlines() if l.startswith(("ok ", "CHILD", "FAIL")))
        print(out)
        if r.returncode != 0 or "CHILD OK" not in r.stdout:
            print(r.stdout[-3000:])
            print(r.stderr[-3000:])
            raise SystemExit(f"FAIL engine {engine}")
    print("ALL ENGINES PASSED")
