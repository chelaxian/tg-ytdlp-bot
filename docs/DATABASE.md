# Database engines

The bot stores everything (users, blocked/ignored lists, download logs, the
shared video/playlist/image cache, ChannelGuard state) in one tree with the
Firebase Realtime Database layout:

```
bot/
  <BOT_NAME_FOR_USERS>/users|blocked_users|unblocked_users|ignored_users|logs|channel_guard
  video_cache/<url-hash>/<quality>            -> "msg_id[,msg_id...]"
  video_cache/playlists/<hash>/<quality>/<i>  -> "msg_id"
  video_cache/images/<hash>/<post>            -> "msg_id,..."
```

The same tree can live in four engines, selected in `CONFIG/config.py`:

| Setting | Engine | When to use |
|---|---|---|
| `USE_FIREBASE = True` | Google Firebase RTDB | legacy cloud setup; reads come from a `dump.json` copy refreshed every `RELOAD_CACHE_EVERY` hours (free download quota) |
| `USE_FIREBASE = False`, `DB_ENGINE = "json"` | `dump.json` file | tiny bots only: every write rewrites the whole file |
| `USE_FIREBASE = False`, `DB_ENGINE = "sqlite"` | SQLite file `SQLITE_DB_PATH` | one bot on one VM, zero setup |
| `USE_FIREBASE = False`, `DB_ENGINE = "postgres"` | PostgreSQL (local or remote, TLS) | several bots sharing one database, best concurrency |

A config without `DB_ENGINE` behaves as before (`USE_FIREBASE = False` = json).

SQL engines are always current — there is no dump download, `/reload_cache`
just confirms that, and the auto-reloader does not run. Reads go straight to the
database (indexed key lookups), so a cache entry written by one bot is visible
to every other bot sharing the database immediately.

## How the tree is stored

One row per leaf in `rtdb_nodes(path PRIMARY KEY, value)`:
`bot/video_cache/ab12…/720p → "12345"` (value is a JSON scalar, so strings,
numbers and booleans keep their types). A node is the prefix range of its path
on a byte-ordered key, so `get`, `set`, `update`, `remove`, `push` keep the
exact Firebase semantics: `null`/empty objects delete, writing below a leaf
replaces it, objects with array-like integer keys read back as lists (the
Firebase rule `maxKey < 2·count`), push IDs are Firebase-style. An export is
therefore identical to a Firebase export of the same data and can be imported
back into Firebase.

## SQLite (local)

```python
USE_FIREBASE = False
DB_ENGINE = "sqlite"
SQLITE_DB_PATH = "DATABASE/data/tgytdlp.sqlite3"
```

WAL mode, one connection per thread; the dashboard process reads the same file.
Backup: `sqlite3 DATABASE/data/tgytdlp.sqlite3 ".backup '/backup/tgytdlp-$(date +%F).sqlite3'"`
or `python scripts/db_migrate.py --from sqlite --to json --json-file backup.json`.

Docker Compose: the project directory is mounted into the containers (`.:/app`),
so `DATABASE/data/` stays on the host and survives rebuilds. Run the migration
inside the bot container, e.g.
`docker compose run --rm --no-deps bot python scripts/db_migrate.py --from firebase --to sqlite --verify`,
then set `USE_FIREBASE = False` / `DB_ENGINE = "sqlite"` and `docker compose up -d`.

## PostgreSQL (local or on a dedicated VM)

On the database VM (Debian/Ubuntu, as root):

```bash
scripts/db/setup_postgres_server.sh --name db.example.com --name 203.0.113.10 \
    --allow 198.51.100.7/32 --allow 192.0.2.44/32 --bot-dir /root/Telegram/tg-ytdlp-bot
```

* installs PostgreSQL, creates its own CA and a server certificate for the
  given names, enables TLS ≥ 1.2 and SCRAM-SHA-256;
* creates database/role `tgytdlp` with a random password (stored in
  `/root/.tgytdlp-db/tgytdlp.password`);
* remote clients are accepted only from `--allow` networks and only over TLS
  (`hostssl` lines); without `--allow` it listens on localhost only;
* `--client-cert` additionally requires client certificates (mutual TLS),
  `--issue-client NAME` issues one per bot VM;
* re-running is safe (keeps password/certificates; `--rotate-password` to change).

Open TCP 5432 only for the bot VMs: in the VM firewall and in the cloud
security list (Oracle Cloud: VCN → Security List / NSG ingress rule).

On every bot VM copy `/etc/postgresql/tgytdlp-tls/ca.crt` to
`CONFIG/db/ca.crt` (and the client certificate/key when mutual TLS is on), then:

```python
USE_FIREBASE = False
DB_ENGINE = "postgres"
POSTGRES_HOST = "db.example.com"     # must match a --name of the server certificate
POSTGRES_DB = "tgytdlp"
POSTGRES_USER = "tgytdlp"
POSTGRES_PASSWORD = "..."
POSTGRES_SSLMODE = "verify-full"     # encrypted, server certificate + hostname verified
POSTGRES_SSLROOTCERT = "CONFIG/db/ca.crt"
```

`verify-full` protects against eavesdropping and man-in-the-middle; with
`require` the traffic is encrypted but the server is not authenticated, so use
it only inside a trusted private network. Connections use a pool, TCP
keepalives and a 30 s statement timeout, so a dead network never hangs the bot.

Bots that share a database share the global `bot/video_cache` (as with a shared
Firebase project) and keep their own `bot/<BOT_NAME_FOR_USERS>` subtree.

Backup: `pg_dump -Fc tgytdlp > /backup/tgytdlp-$(date +%F).dump` (cron), or a
JSON export with `scripts/db_migrate.py`.

## Moving data between engines

`scripts/db_migrate.py` copies the whole tree between any two engines and can
verify the result:

```bash
# Firebase -> PostgreSQL (one full download of the Firebase quota)
python scripts/db_migrate.py --from firebase --to postgres --verify
# the dump.json you already have -> SQLite
python scripts/db_migrate.py --from json --json-file dump.json --to sqlite --verify
# PostgreSQL -> Firebase-importable JSON / back to Firebase
python scripts/db_migrate.py --from postgres --to json --json-file export.json
python scripts/db_migrate.py --from postgres --to firebase --yes
```

A non-empty target is replaced only with `--yes`. Cut-over procedure:

1. stop the bot (`systemctl stop tg-ytdlp-bot`) so nothing is written meanwhile;
2. run the migration with `--verify`;
3. set `USE_FIREBASE = False` and `DB_ENGINE`, start the bot;
4. keep Firebase untouched for a while: switching back is just
   `USE_FIREBASE = True` (plus a `--to firebase` copy if the new data matters).
