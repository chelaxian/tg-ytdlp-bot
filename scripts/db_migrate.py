#!/usr/bin/env python3
"""Copy the bot database between engines: firebase, json (dump.json), sqlite, postgres.

The data model is the same everywhere (the Firebase Realtime Database tree), so
any engine can be copied to any other, and back to Firebase.

Examples (run from the bot directory, connection settings come from CONFIG/config.py):
  # Firebase -> SQLite (downloads a fresh dump first: one full download of the quota)
  python scripts/db_migrate.py --from firebase --to sqlite --verify
  # existing dump.json -> PostgreSQL
  python scripts/db_migrate.py --from json --json-file dump.json --to postgres --verify
  # PostgreSQL -> dump.json (Firebase-importable JSON: Console > Import JSON)
  python scripts/db_migrate.py --from postgres --to json --json-file export.json
  # SQLite -> Firebase (writes in batches over REST)
  python scripts/db_migrate.py --from sqlite --to firebase --yes

An existing non-empty target is replaced only with --yes.
"""
import argparse
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.chdir(ROOT)

from CONFIG.config import Config  # noqa: E402
from DATABASE.sql_store import (  # noqa: E402
    SqlTreeStore, assemble, flatten, store_params_from_config,
)

ENGINES = ("firebase", "json", "sqlite", "postgres")


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def normalize(tree):
    """The tree as Firebase would return it (nulls/empties dropped, arrays rule)."""
    return assemble(flatten(tree or {}), "") or {}


def leaf_count(tree):
    return sum(1 for _ in flatten(tree or {}))


# ------------------------------------------------------------------ firebase
def _firebase_session():
    import requests
    conf = getattr(Config, "FIREBASE_CONF", {}) or {}
    api_key, url = conf.get("apiKey"), (conf.get("databaseURL") or "").rstrip("/")
    if not api_key or not url:
        sys.exit("FIREBASE_CONF.apiKey / databaseURL are not configured")
    s = requests.Session()
    r = s.post(f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}",
               json={"email": Config.FIREBASE_USER, "password": Config.FIREBASE_PASSWORD,
                     "returnSecureToken": True}, timeout=(10, 30))
    r.raise_for_status()
    return s, url, r.json()["idToken"]


def read_firebase(args):
    from DATABASE.download_firebase import download_firebase_dump, OUTPUT_FILE
    log("Downloading a fresh Firebase dump (one full read of the database)...")
    if not download_firebase_dump():
        sys.exit("Firebase dump download failed")
    with open(OUTPUT_FILE, encoding="utf-8") as f:
        return json.load(f)


def write_firebase(tree, args):
    s, url, token = _firebase_session()
    log("Replacing the Firebase database root...")
    batch_keys = 2000

    def patch(path, data):
        for attempt in range(4):
            try:
                r = s.patch(f"{url}/{path}.json", params={"auth": token}, json=data, timeout=(10, 120))
                r.raise_for_status()
                return
            except Exception as e:
                if attempt == 3:
                    raise
                log(f"  PATCH {path or '/'} failed ({type(e).__name__}), retrying")
                time.sleep(3 * (attempt + 1))

    s.put(f"{url}/.json", params={"auth": token}, json={}, timeout=(10, 120)).raise_for_status()

    def send(path, node):
        # large objects are split so one request stays well below the 256 MB limit
        if isinstance(node, dict) and len(node) > batch_keys:
            items = list(node.items())
            for i in range(0, len(items), batch_keys):
                patch(path, dict(items[i:i + batch_keys]))
            log(f"  {path}: {len(items)} keys")
        elif isinstance(node, dict):
            big = {k: v for k, v in node.items() if isinstance(v, dict) and len(v) > batch_keys}
            small = {k: v for k, v in node.items() if k not in big}
            if small:
                patch(path, small)
            for k, v in big.items():
                send(f"{path}/{k}" if path else k, v)
        else:
            patch(path.rsplit("/", 1)[0] if "/" in path else "", {path.rsplit("/", 1)[-1]: node})

    send("", tree)


# ------------------------------------------------------------------ json / sql
def read_json(args):
    path = args.json_file or getattr(Config, "FIREBASE_CACHE_FILE", "dump.json")
    log(f"Reading {path}")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        sys.exit(f"{path}: the root is not a JSON object")
    return data


def write_json(tree, args):
    from HELPERS.atomic_io import atomic_write_json
    path = args.json_file or getattr(Config, "FIREBASE_CACHE_FILE", "dump.json")
    if os.path.exists(path) and os.path.getsize(path) > 2 and not args.yes:
        sys.exit(f"{path} exists and is not empty: add --yes to replace it")
    if os.path.exists(path):
        backup = f"{path}.bak"
        os.replace(path, backup)
        log(f"Previous {path} kept as {backup}")
    atomic_write_json(path, tree, ensure_ascii=False, indent=2)
    log(f"Written {path}")


def open_sql(engine, args):
    params = store_params_from_config(Config, engine)
    if engine == "sqlite" and args.sqlite_path:
        params["path"] = args.sqlite_path
    if engine == "postgres" and args.pg_dsn:
        params["dsn"] = args.pg_dsn
    return SqlTreeStore(engine, **params)


def read_sql(engine, args):
    store = open_sql(engine, args)
    try:
        log(f"Reading {engine} ({store.count()} leaves)")
        return store.export_tree()
    finally:
        store.close()


def write_sql(engine, tree, args):
    store = open_sql(engine, args)
    try:
        existing = store.count()
        if existing and not args.yes:
            sys.exit(f"{engine} already holds {existing} leaves: add --yes to replace them")
        t0 = time.time()
        n = store.import_tree(tree, replace=True,
                              progress=lambda done: log(f"  {done} leaves..."))
        log(f"Imported {n} leaves into {engine} in {time.time() - t0:.1f}s")
    finally:
        store.close()


def read(engine, args):
    if engine == "firebase":
        return read_firebase(args)
    if engine == "json":
        return read_json(args)
    return read_sql(engine, args)


def write(engine, tree, args):
    if engine == "firebase":
        if not args.yes:
            sys.exit("Writing to Firebase replaces the whole cloud database: add --yes")
        return write_firebase(tree, args)
    if engine == "json":
        return write_json(tree, args)
    return write_sql(engine, tree, args)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from", dest="src", choices=ENGINES, required=True)
    ap.add_argument("--to", dest="dst", choices=ENGINES, required=True)
    ap.add_argument("--json-file", help="dump file for the json engine (default: FIREBASE_CACHE_FILE)")
    ap.add_argument("--sqlite-path", help="SQLite file (default: SQLITE_DB_PATH)")
    ap.add_argument("--pg-dsn", help="PostgreSQL DSN (default: POSTGRES_* settings)")
    ap.add_argument("--verify", action="store_true", help="read the target back and compare with the source")
    ap.add_argument("--yes", action="store_true", help="replace a non-empty target")
    args = ap.parse_args()
    if args.src == args.dst:
        sys.exit("source and target are the same engine")

    tree = read(args.src, args)
    log(f"Source: {leaf_count(tree)} leaves, top-level keys: {sorted(tree)}")
    write(args.dst, tree, args)
    if args.verify:
        log("Verifying...")
        back = read(args.dst, args) if args.dst != "firebase" else None
        if back is None:
            log("Skipped (verifying Firebase would cost another full download)")
        elif normalize(back) == normalize(tree):
            log(f"OK: target equals source ({leaf_count(back)} leaves)")
        else:
            sys.exit("VERIFY FAILED: target differs from source")
    log("Done")


if __name__ == "__main__":
    main()
