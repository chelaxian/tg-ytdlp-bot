"""Firebase Realtime Database data model on SQLite or PostgreSQL.

The whole RTDB JSON tree is stored as one row per leaf:

    rtdb_nodes(path TEXT PRIMARY KEY, value TEXT)   -- value = JSON scalar
    "bot/video_cache/<hash>/720p" -> "\"12345\""

A subtree is a prefix range on the primary key (byte-ordered collation, so
"a/b/" .. "a/b0" covers exactly the children of "a/b"); get/set/update/remove/
push keep RTDB semantics:
  * set(None) / set({}) deletes the node, empty objects never exist;
  * writing under a leaf replaces the leaf with an object;
  * objects with array-like integer keys read back as lists, with the same rule
    the Firebase SDK/REST API applies (maxKey < 2 * count), so the exported tree
    is identical to a Firebase export of the same data;
  * push() generates Firebase-style chronological push IDs.

Engines: "sqlite" (stdlib sqlite3, WAL, per-thread connections) and
"postgres" (psycopg 3 + connection pool, TLS).
"""
from __future__ import annotations

import json
import logging
import os
import random
import re
import threading
import time
from contextlib import contextmanager
from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple

logger = logging.getLogger(__name__)

TABLE = "rtdb_nodes"
SCHEMA_VERSION = 1
_SEP = "/"
_FORBIDDEN_KEY_CHARS = re.compile(r"[.$#\[\]/\x00-\x1f\x7f]")
_INT_KEY = re.compile(r"^(0|[1-9][0-9]*)$")
_INT32_MAX = 2 ** 31 - 1


# --------------------------------------------------------------------------- paths
def split_path(path: Any) -> List[str]:
    if isinstance(path, (list, tuple)):
        parts = []
        for p in path:
            parts.extend(split_path(p))
        return parts
    return [p for p in str(path or "").split(_SEP) if p]


def join_path(parts: Iterable[str]) -> str:
    return _SEP.join(parts)


def _check_key(key: str) -> str:
    key = str(key)
    if not key or _FORBIDDEN_KEY_CHARS.search(key):
        raise ValueError(f"Invalid key {key!r}: keys can't be empty or contain . $ # [ ] / or control chars")
    return key


# --------------------------------------------------------------------------- tree <-> rows
def flatten(value: Any, prefix: str = "") -> Iterator[Tuple[str, str]]:
    """Yield (path, json_scalar) for every leaf under value; None/empty produce nothing."""
    if isinstance(value, dict):
        for k, v in value.items():
            k = _check_key(k)
            yield from flatten(v, f"{prefix}{_SEP}{k}" if prefix else k)
    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            yield from flatten(v, f"{prefix}{_SEP}{i}" if prefix else str(i))
    elif value is None:
        return
    elif isinstance(value, (str, bool, int, float)):
        if not prefix:
            raise ValueError("The database root must be an object")
        yield prefix, json.dumps(value, ensure_ascii=False)
    else:
        raise TypeError(f"Unsupported value type {type(value).__name__} at {prefix!r}")


def _rtdb_arrays(node: Any) -> Any:
    """Apply the Firebase rule: an object whose keys are all non-negative int32
    integers and whose max key < 2 * number of keys is returned as a list."""
    if not isinstance(node, dict):
        return node
    for k, v in node.items():
        node[k] = _rtdb_arrays(v)
    max_key = -1
    for k in node:
        if not _INT_KEY.match(k):
            return node
        ik = int(k)
        if ik > _INT32_MAX:
            return node
        max_key = max(max_key, ik)
    if node and max_key < 2 * len(node):
        arr: List[Any] = [None] * (max_key + 1)
        for k, v in node.items():
            arr[int(k)] = v
        return arr
    return node


def assemble(rows: Iterable[Tuple[str, str]], base: str) -> Any:
    """Build the value of node `base` from its leaf rows."""
    base_len = len(base) + 1 if base else 0
    root: Dict[str, Any] = {}
    leaf_value = None
    have_children = False
    for path, raw in rows:
        value = json.loads(raw)
        if path == base:
            leaf_value = value
            continue
        have_children = True
        parts = path[base_len:].split(_SEP)
        cur = root
        for part in parts[:-1]:
            nxt = cur.get(part)
            if not isinstance(nxt, dict):
                nxt = cur[part] = {}
            cur = nxt
        cur[parts[-1]] = value
    if not have_children:
        return leaf_value
    return _rtdb_arrays(root)


# --------------------------------------------------------------------------- push ids
_PUSH_CHARS = "-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz"
_push_lock = threading.Lock()
_last_push_ms = 0
_last_rand = [0] * 12


def push_id() -> str:
    """Firebase-compatible push ID: 8 time chars + 12 random chars, sortable by creation."""
    global _last_push_ms
    with _push_lock:
        now = int(time.time() * 1000)
        if now == _last_push_ms:
            for i in range(11, -1, -1):
                if _last_rand[i] != 63:
                    _last_rand[i] += 1
                    break
                _last_rand[i] = 0
        else:
            _last_push_ms = now
            for i in range(12):
                _last_rand[i] = random.randrange(64)
        ts_chars = []
        for _ in range(8):
            ts_chars.append(_PUSH_CHARS[now % 64])
            now //= 64
        return "".join(reversed(ts_chars)) + "".join(_PUSH_CHARS[r] for r in _last_rand)


# --------------------------------------------------------------------------- store
class StoreError(RuntimeError):
    pass


class SqlTreeStore:
    """Thread-safe RTDB-style tree store. Paths are "a/b/c" strings or part lists."""

    _RETRY_DELAYS = (0.5, 2.0)

    def __init__(self, engine: str, **params: Any):
        self.engine = engine
        self._params = params
        self._local = threading.local()
        self._sqlite_conns: List[Any] = []
        self._pool = None
        self._closed = False
        if engine == "sqlite":
            self._ph = "?"
            path = params.get("path") or "DATABASE/data/tgytdlp.sqlite3"
            self._sqlite_path = os.path.abspath(path)
            os.makedirs(os.path.dirname(self._sqlite_path), exist_ok=True)
        elif engine == "postgres":
            self._ph = "%s"
            self._open_pg_pool()
        else:
            raise ValueError(f"Unsupported SQL engine {engine!r}")
        self._create_schema()

    # ------------------------------------------------------------ connections
    def _open_pg_pool(self) -> None:
        try:
            import psycopg  # noqa: F401
            from psycopg_pool import ConnectionPool
        except ImportError as e:
            raise StoreError("PostgreSQL engine needs: pip install 'psycopg[binary]' psycopg-pool") from e
        p = self._params
        conninfo = p.get("dsn") or ""
        kwargs = {}
        if not conninfo:
            kwargs = {k: v for k, v in {
                "host": p.get("host"), "port": p.get("port"), "dbname": p.get("dbname"),
                "user": p.get("user"), "password": p.get("password"),
                "sslmode": p.get("sslmode"), "sslrootcert": p.get("sslrootcert"),
                "sslcert": p.get("sslcert"), "sslkey": p.get("sslkey"),
            }.items() if v not in (None, "")}
        kwargs.setdefault("connect_timeout", int(p.get("connect_timeout") or 10))
        kwargs.setdefault("application_name", p.get("application_name") or "tg-ytdlp-bot")
        # A dead TCP peer (VM reboot, tunnel flap) must not hang a query forever
        kwargs.setdefault("keepalives", 1)
        kwargs.setdefault("keepalives_idle", 30)
        kwargs.setdefault("keepalives_interval", 10)
        kwargs.setdefault("keepalives_count", 3)
        kwargs.setdefault("options", f"-c statement_timeout={int(p.get('statement_timeout_ms') or 30000)}")
        self._pool = ConnectionPool(
            conninfo,
            kwargs=kwargs,
            min_size=int(p.get("pool_min") or 1),
            max_size=int(p.get("pool_max") or 16),
            timeout=float(p.get("pool_timeout") or 30),
            check=ConnectionPool.check_connection,
            name="tgytdlp-db",
            open=False,
        )
        self._pool.open(wait=True, timeout=float(p.get("connect_wait") or 30))

    def _sqlite_conn(self):
        conn = getattr(self._local, "conn", None)
        if conn is None:
            import sqlite3
            conn = sqlite3.connect(self._sqlite_path, timeout=30, isolation_level=None, check_same_thread=False)
            conn.execute("PRAGMA journal_mode=WAL")
            conn.execute("PRAGMA synchronous=NORMAL")
            conn.execute("PRAGMA busy_timeout=30000")
            conn.execute("PRAGMA foreign_keys=OFF")
            self._local.conn = conn
            self._sqlite_conns.append(conn)
        return conn

    @contextmanager
    def _tx(self, write: bool):
        """Yield a cursor inside a transaction (committed on success)."""
        if self._closed:
            raise StoreError("database store is closed")
        if self.engine == "sqlite":
            conn = self._sqlite_conn()
            cur = conn.cursor()
            cur.execute("BEGIN IMMEDIATE" if write else "BEGIN")
            try:
                yield cur
                cur.execute("COMMIT")
            except BaseException:
                cur.execute("ROLLBACK")
                raise
        else:
            with self._pool.connection() as conn:
                with conn.transaction():
                    with conn.cursor() as cur:
                        yield cur

    def _transient(self, exc: BaseException) -> bool:
        if self.engine == "sqlite":
            import sqlite3
            return isinstance(exc, sqlite3.OperationalError) and "locked" in str(exc).lower()
        import psycopg
        from psycopg_pool import PoolTimeout
        return isinstance(exc, (psycopg.OperationalError, PoolTimeout))

    def _run(self, write: bool, fn):
        attempts = len(self._RETRY_DELAYS) + 1
        for attempt in range(1, attempts + 1):
            try:
                with self._tx(write) as cur:
                    return fn(cur)
            except Exception as e:
                if attempt >= attempts or not self._transient(e):
                    raise
                delay = self._RETRY_DELAYS[attempt - 1]
                logger.warning(f"[DB] {self.engine} transient error (attempt {attempt}/{attempts}), "
                               f"retrying in {delay}s: {type(e).__name__}: {e}")
                time.sleep(delay)

    # ------------------------------------------------------------ schema
    def _create_schema(self) -> None:
        collate = ' COLLATE "C"' if self.engine == "postgres" else ""

        def create(cur):
            cur.execute(f"CREATE TABLE IF NOT EXISTS {TABLE} (path TEXT{collate} PRIMARY KEY, value TEXT NOT NULL)")
            cur.execute("CREATE TABLE IF NOT EXISTS rtdb_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
            cur.execute(self._upsert_sql("rtdb_meta", "key"), ("schema_version", str(SCHEMA_VERSION)))

        self._run(True, create)

    def _upsert_sql(self, table: str = TABLE, key: str = "path") -> str:
        ph = self._ph
        col = "value"
        return (f"INSERT INTO {table} ({key}, {col}) VALUES ({ph}, {ph}) "
                f"ON CONFLICT ({key}) DO UPDATE SET {col} = excluded.{col}")

    # ------------------------------------------------------------ primitives (inside a tx)
    def _subtree_where(self, path: str) -> Tuple[str, tuple]:
        if not path:
            return "1=1", ()
        ph = self._ph
        # One index range [p, p0) (p0 = p with "/" + 1) holds the node and all its
        # descendants; the second condition drops siblings such as "p-x" that sort
        # inside it. A bare "path = p OR (...)" made PostgreSQL's generic plan fall
        # back to a sequential scan: ~70 ms per missing key on 750k rows.
        return (f"(path >= {ph} AND path < {ph} AND (path = {ph} OR path > {ph}))",
                (path, path + chr(ord(_SEP) + 1), path, path + _SEP))

    def _select(self, cur, path: str) -> List[Tuple[str, str]]:
        where, args = self._subtree_where(path)
        cur.execute(f"SELECT path, value FROM {TABLE} WHERE {where}", args)
        return cur.fetchall()

    def _delete(self, cur, path: str) -> None:
        where, args = self._subtree_where(path)
        cur.execute(f"DELETE FROM {TABLE} WHERE {where}", args)

    def _write(self, cur, path: str, value: Any) -> None:
        """RTDB set: replace the node at path (and turn leaf ancestors into objects)."""
        rows = list(flatten(value, path))
        if not path and not isinstance(value, (dict, list, tuple, type(None))):
            raise ValueError("The database root must be an object")
        self._delete(cur, path)
        parts = split_path(path)
        if len(parts) > 1 and rows:
            ancestors = [join_path(parts[:i]) for i in range(1, len(parts))]
            marks = ",".join([self._ph] * len(ancestors))
            cur.execute(f"DELETE FROM {TABLE} WHERE path IN ({marks})", ancestors)
        if rows:
            cur.executemany(self._upsert_sql(), rows)

    # ------------------------------------------------------------ public API
    def get(self, path: Any = "") -> Any:
        p = join_path(split_path(path))
        rows = self._run(False, lambda cur: self._select(cur, p))
        return assemble(rows, p)

    def exists(self, path: Any) -> bool:
        p = join_path(split_path(path))
        where, args = self._subtree_where(p)

        def q(cur):
            cur.execute(f"SELECT 1 FROM {TABLE} WHERE {where} LIMIT 1", args)
            return cur.fetchone() is not None

        return self._run(False, q)

    def child_keys(self, path: Any) -> List[str]:
        """Direct child keys of path (no values are decoded)."""
        p = join_path(split_path(path))
        where, args = self._subtree_where(p)
        start = len(p) + 1 if p else 0

        def q(cur):
            cur.execute(f"SELECT path FROM {TABLE} WHERE {where}", args)
            return cur.fetchall()

        keys = []
        seen = set()
        for (row_path,) in self._run(False, q):
            if row_path == p:
                continue
            k = row_path[start:].split(_SEP, 1)[0]
            if k not in seen:
                seen.add(k)
                keys.append(k)
        return keys

    def set(self, path: Any, value: Any) -> None:
        p = join_path(split_path(path))
        self._run(True, lambda cur: self._write(cur, p, value))

    def update(self, path: Any, values: Dict[str, Any]) -> None:
        """RTDB update: set each child (keys may be multi-segment paths) atomically."""
        if not isinstance(values, dict):
            raise TypeError("update() expects a dict")
        base = split_path(path)
        targets = [(join_path(base + split_path(k)), v) for k, v in values.items()]

        def tx(cur):
            for p, v in targets:
                self._write(cur, p, v)

        self._run(True, tx)

    def remove(self, path: Any) -> None:
        p = join_path(split_path(path))
        self._run(True, lambda cur: self._delete(cur, p))

    def push(self, path: Any, value: Any) -> str:
        key = push_id()
        self.set(split_path(path) + [key], value)
        return key

    def count(self, path: Any = "") -> int:
        p = join_path(split_path(path))
        where, args = self._subtree_where(p)

        def q(cur):
            cur.execute(f"SELECT COUNT(*) FROM {TABLE} WHERE {where}", args)
            return int(cur.fetchone()[0])

        return self._run(False, q)

    def import_tree(self, tree: Dict[str, Any], *, replace: bool = True, batch: int = 20000,
                    progress=None) -> int:
        """Bulk-load a whole RTDB export (e.g. dump.json). Returns the number of leaves."""
        if not isinstance(tree, dict):
            raise ValueError("The database root must be an object")
        rows = flatten(tree)
        total = 0

        def load(cur):
            nonlocal total
            if replace:
                cur.execute(f"DELETE FROM {TABLE}")
            if self.engine == "postgres" and replace:
                with cur.copy(f"COPY {TABLE} (path, value) FROM STDIN") as cp:
                    for row in rows:
                        cp.write_row(row)
                        total += 1
                        if progress and total % batch == 0:
                            progress(total)
                return
            buf = []
            sql = self._upsert_sql()
            for row in rows:
                buf.append(row)
                if len(buf) >= batch:
                    cur.executemany(sql, buf)
                    total += len(buf)
                    buf.clear()
                    if progress:
                        progress(total)
            if buf:
                cur.executemany(sql, buf)
                total += len(buf)

        self._run(True, load)
        if self.engine == "postgres":
            self._run(True, lambda cur: cur.execute(f"ANALYZE {TABLE}"))
        return total

    def export_tree(self) -> Dict[str, Any]:
        return self.get("") or {}

    def ping(self) -> bool:
        def q(cur):
            cur.execute("SELECT 1")
            return cur.fetchone() is not None

        return self._run(False, q)

    def close(self) -> None:
        self._closed = True
        for conn in self._sqlite_conns:
            try:
                conn.close()
            except Exception:
                pass
        self._sqlite_conns.clear()
        if self._pool is not None:
            try:
                self._pool.close()
            except Exception:
                pass


def store_params_from_config(config, engine: str) -> Dict[str, Any]:
    """Connection parameters for engine from CONFIG.config.Config."""
    if engine == "sqlite":
        return {"path": getattr(config, "SQLITE_DB_PATH", "DATABASE/data/tgytdlp.sqlite3")}
    g = lambda name, default=None: getattr(config, name, default)
    return {
        "dsn": g("POSTGRES_DSN", ""),
        "host": g("POSTGRES_HOST", "127.0.0.1"),
        "port": g("POSTGRES_PORT", 5432),
        "dbname": g("POSTGRES_DB", "tgytdlp"),
        "user": g("POSTGRES_USER", "tgytdlp"),
        "password": g("POSTGRES_PASSWORD", ""),
        "sslmode": g("POSTGRES_SSLMODE", "verify-full"),
        "sslrootcert": g("POSTGRES_SSLROOTCERT", ""),
        "sslcert": g("POSTGRES_SSLCERT", ""),
        "sslkey": g("POSTGRES_SSLKEY", ""),
        "pool_max": g("POSTGRES_POOL_MAX", 16),
        "statement_timeout_ms": g("POSTGRES_STATEMENT_TIMEOUT_MS", 30000),
    }


def open_store_from_config(config, engine: str) -> SqlTreeStore:
    return SqlTreeStore(engine, **store_params_from_config(config, engine))
