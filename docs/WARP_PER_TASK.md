# Per-task WARP tunnels (`WARP_PER_TASK = True`)

## Why

YouTube and other sites throttle or block an IP that downloads a lot. The old
setup sent *all* server traffic through one system-wide WARP tunnel
(`wg-quick@wgcf`) and restarted it to get a new egress IP. Every restart cut the
bot's Telegram connections and every running download at once (DE: ~35
restarts a day, each followed by a reconnect storm).

## How it works now

* The bot itself — Telegram (MTProto), Firebase/database, localhost services —
  uses the server's **direct** internet connection and is never affected by
  WARP.
* Every **user task** (one handler run: a link, a quality click, `/img`,
  `/link`, `/list`, `/cookie`, subtitles/dubs inside a download, gallery-dl
  fallbacks...) that reaches an external site gets **its own WARP tunnel**:
  a private `wireproxy` process (userspace WireGuard, no interfaces, no routes)
  with an HTTP proxy on a local port. Each new tunnel = new WireGuard session =
  **new Cloudflare egress IPv6** (IPv6 is preferred; IPv4-only sites still work
  through WARP IPv4). The IP stays the same for the whole task, which YouTube
  needs (media URLs are bound to the requesting IP).
* The tunnel starts on the task's first external request (~0.1–0.3 s) and is
  stopped when the task ends; tasks served from the cache never start one.
  Concurrent tasks run in separate tunnels.
* Routing without touching call sites:
  * every `yt_dlp.YoutubeDL` created without an explicit `proxy`;
  * gallery-dl (library mode via the `proxy` config key, CLI via
    `HTTP(S)_PROXY`);
  * `requests` inside a task to external hosts (localhost, private networks,
    Telegram, Firebase/Google APIs stay direct).
* A proxy you chose (`/proxy`, `PROXY_*` domain lists) always takes
  precedence.
* "Sign in to confirm you're not a bot" no longer restarts any shared tunnel:
  the next task simply runs on a new egress.
* Safety: at most `WARP_MAX_TUNNELS` tunnels (overflow uses one shared fallback
  tunnel, never the server IP); tunnels die with the bot (PDEATHSIG) and
  leftovers are killed at startup; account keys live in `CONFIG/warp/` (0600)
  and per-tunnel configs are deleted when the tunnel stops.

Measured on Oracle Cloud (DE): tunnel ready in 110–220 ms; four concurrent
tunnels on one WARP account each downloaded 100 MB at 18–27 MB/s with four
different, stable IPv6 addresses.

## Setup (systemd deployment)

```bash
scripts/warp/setup_warp_per_task.sh --bot-dir /root/Telegram/tg-ytdlp-bot --direct-route
```

* installs `wireproxy` and `wgcf` (pinned versions, SHA-256 verified);
* registers a WARP account into `CONFIG/warp/account-1.conf` (Cloudflare
  rate-limits registrations — the script waits and retries; one account is
  enough, `--accounts N` only spreads load);
* `--direct-route` is only needed when the server also runs a system-wide
  `wg-quick@wgcf` (e.g. as a VPN exit): packets of the bot's user get WARP's
  own fwmark (`iptables -t mangle OUTPUT -m owner --uid-owner 0 -j MARK`, unit
  `tg-ytdlp-direct-route.service`), so wg-quick's `not fwmark ... lookup 51820`
  rule lets them use the main table, while forwarded VPN/container traffic keeps
  using WARP. (A `uidrange` ip rule does not work: wg-quick inserts its rules
  ahead of all others again on every restart.)

Then in `CONFIG/config.py`:

```python
WARP_PER_TASK = True
WARP_PROXY_HOST = "172.17.0.1"  # docker0 address when the bgutil PO-token container runs on Docker
```

The bgutil provider fetches its challenge through the same proxy yt-dlp uses,
so the proxy must be reachable from that container; `127.0.0.1` is fine when
bgutil runs on the host.

Logs: `[WARP] tunnel up for <task> in N ms, egress=<IPv6>` /
`[WARP] tunnel down for <task> after Ns`.

The Docker Compose deployment still uses the shared `warp` container; this mode
is off there by default.
