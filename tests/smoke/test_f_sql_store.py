"""Offline tests: SqlTreeStore keeps Firebase RTDB semantics (SQLite; PostgreSQL
when TG_TEST_PG_DSN is set, e.g. a throwaway docker container).
Run: python test_f_sql_store.py [repo_root]
"""
import os
import sys
import tempfile
import threading

REPO = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])
sys.path.insert(0, REPO)

from DATABASE.sql_store import SqlTreeStore, assemble, flatten, push_id  # noqa: E402

PASSED = []


def check(name, cond, detail=""):
    if not cond:
        raise AssertionError(f"FAIL {name}: {detail}")
    PASSED.append(name)
    print(f"ok  {name}")


def run(store, tag):
    c = lambda name, cond, detail="": check(f"{tag}:{name}", cond, detail)
    store.import_tree({}, replace=True)
    c("empty_root", store.get("") is None)

    store.set("bot/tgytdlp_bot/users/123", {"ID": 123, "timestamp": 1700000000})
    c("get_object", store.get("bot/tgytdlp_bot/users/123") == {"ID": 123, "timestamp": 1700000000})
    c("get_leaf_types", store.get(["bot", "tgytdlp_bot", "users", "123", "ID"]) == 123)
    c("exists", store.exists("bot/tgytdlp_bot/users/123") and not store.exists("bot/tgytdlp_bot/users/12"))

    # prefix isolation: "users/12" must not see "users/123", "a/b" not "a/bc"
    store.set("x/ab", "1")
    store.set("x/abc", "2")
    store.set("x/ab/deep", None)
    c("prefix_isolation", store.get("x/ab") == "1" and store.get("x/abc") == "2")

    # set replaces the subtree
    store.set("bot/video_cache/h1", {"720p": "11", "1080p": "12"})
    store.set("bot/video_cache/h1", {"480p": "10"})
    c("set_replaces", store.get("bot/video_cache/h1") == {"480p": "10"})

    # update merges children; multi-segment keys allowed
    store.update("bot/video_cache/h1", {"720p": "11", "meta/title": "t"})
    c("update_merges", store.get("bot/video_cache/h1") == {"480p": "10", "720p": "11", "meta": {"title": "t"}})

    # writing under a leaf turns it into an object
    store.set("leaf", "scalar")
    store.set("leaf/child", 5)
    c("leaf_becomes_object", store.get("leaf") == {"child": 5})

    # null / empty delete
    store.set("bot/video_cache/h1/480p", None)
    store.update("bot/video_cache/h1", {"720p": None})
    c("null_deletes", store.get("bot/video_cache/h1") == {"meta": {"title": "t"}})
    store.set("tmp", {})
    c("empty_object_absent", store.get("tmp") is None and not store.exists("tmp"))

    store.remove("bot/video_cache/h1")
    c("remove", store.get("bot/video_cache/h1") is None)

    # Firebase array rule
    store.set("bot/video_cache/playlists/p1/720p", ["a", None, "c"])
    c("array_roundtrip", store.get("bot/video_cache/playlists/p1/720p") == ["a", None, "c"])
    store.set("arr", {"0": "x", "1": "y"})
    c("int_keys_become_array", store.get("arr") == ["x", "y"])
    store.set("sparse", {"0": "x", "9": "y"})
    c("sparse_stays_object", store.get("sparse") == {"0": "x", "9": "y"})
    store.set("bigids", {"5000000001": {"ID": 1}})
    c("telegram_ids_stay_object", isinstance(store.get("bigids"), dict))
    store.set("lead0", {"01": "a", "1": "b"})
    c("leading_zero_not_int", store.get("lead0") == {"01": "a", "1": "b"})

    # push ids: sortable, unique, stored
    k1 = store.push("bot/logs", {"n": 1})
    k2 = store.push("bot/logs", {"n": 2})
    c("push_ids_ordered", len(k1) == 20 and k1 < k2, (k1, k2))
    c("push_stored", store.get("bot/logs") == {k1: {"n": 1}, k2: {"n": 2}})

    c("child_keys", sorted(store.child_keys("x")) == ["ab", "abc"])

    # unicode / floats / bools survive
    store.set("u", {"name": "Пётр 🚀", "f": 1.5, "b": False, "n": 0})
    c("scalar_fidelity", store.get("u") == {"name": "Пётр 🚀", "f": 1.5, "b": False, "n": 0})

    # invalid keys rejected like Firebase
    try:
        store.set("bad", {"a.b": 1})
        bad = False
    except ValueError:
        bad = True
    c("invalid_key_rejected", bad and store.get("bad") is None)

    # concurrent writers do not lose updates or fail
    errors = []

    def writer(n):
        try:
            for i in range(40):
                store.set(f"conc/w{n}/{i}", {"v": i})
                store.update(f"conc/w{n}", {"last": i})
        except Exception as e:  # pragma: no cover
            errors.append(e)

    ths = [threading.Thread(target=writer, args=(n,)) for n in range(8)]
    [t.start() for t in ths]
    [t.join() for t in ths]
    conc = store.get("conc")
    c("concurrent_writes", not errors and len(conc) == 8 and all(len(v) == 41 and v["last"] == 39 for v in conc.values()),
      errors or {k: len(v) for k, v in conc.items()})

    # bulk import / export round trip of a dump-shaped tree
    tree = {
        "bot": {
            "tgytdlp_bot": {
                "users": {"0": {"ID": "0", "timestamp": 1}, "6000000000": {"ID": 6000000000, "timestamp": 2}},
                "blocked_users": {"77": {"ID": "77", "blocked_reason": "manual", "timestamp": "3"}},
                "logs": {"6000000000": {"1700000000": {"ID": "6000000000", "title": "t", "urls": "u"}}},
            },
            "video_cache": {
                "h": {"720p": "123", "mp3": "456"},
                "playlists": {"p": {"720p": [None, "1", None, "3"]}},
                "images": {"i": {"1": "5,6"}},
            },
        }
    }
    n = store.import_tree(tree, replace=True, batch=3)
    c("import_count", n == len(list(flatten(tree))), n)
    c("export_equals_import", store.export_tree() == assemble(flatten(tree), ""))
    c("export_keeps_lists", store.get("bot/video_cache/playlists/p/720p") == [None, "1", None, "3"])
    c("count", store.count("bot/tgytdlp_bot/users") == 4)


tmp = tempfile.mkdtemp(prefix="sqlstore_")
s = SqlTreeStore("sqlite", path=os.path.join(tmp, "t.sqlite3"))
run(s, "sqlite")
s.close()
# a second store on the same file sees the data (other process / dashboard)
s2 = SqlTreeStore("sqlite", path=os.path.join(tmp, "t.sqlite3"))
check("sqlite:persistent", s2.get("bot/video_cache/h") == {"720p": "123", "mp3": "456"})
s2.close()

ids = [push_id() for _ in range(2000)]
check("push_id_unique_monotonic", len(set(ids)) == 2000 and ids == sorted(ids))

dsn = os.environ.get("TG_TEST_PG_DSN")
if dsn:
    pg = SqlTreeStore("postgres", dsn=dsn)
    run(pg, "postgres")
    pg.close()
else:
    print("skip postgres (set TG_TEST_PG_DSN)")

print("ALL", len(PASSED), "CHECKS PASSED")
