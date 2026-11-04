# Dashboard preview (RU / EN)

The rewritten dashboard has been tested against the DE bot's live data. It uses local JavaScript modules and system fonts, with no CDN or frontend build step. Light/dark themes, search, user history, moderation lists and server metrics are available.

## Release scope

This is a **read-only preview**, not the completed administrative rewrite. By default `TG_DASHBOARD_READ_ONLY=1` blocks settings changes, bans and maintenance operations on the server. Login, logout and password changes remain available. The interface displays a preview banner.

Do not disable read-only mode on production yet. The write handlers exist for offline testing but still need integration and safety review, including bot restart coordination, credential-bearing configuration URLs, background jobs and Docker privileges. The dashboard must not be exposed publicly.

The bot-side heartbeat and overrides startup hooks are **not included in this release**. A missing heartbeat is displayed as unknown; it is not proof that the bot is offline. No bot restart is required to use the read-only panel.

## Start and access

Use the existing Python environment and project configuration:

```bash
python -m uvicorn web.dashboard_app:app --host 127.0.0.1 --port 5555 --no-proxy-headers
```

Use a single worker; authentication sessions are not shared between worker processes. The supplied systemd service listens on loopback. Docker Compose publishes port 5555 only on the host's loopback address.

Forward the port over SSH; use a configured SSH host alias and key:

```bash
ssh -N -L 127.0.0.1:15555:127.0.0.1:5555 your-bot-host
```

Open `http://127.0.0.1:15555/`. If the bot is inside an LXC container, the SSH endpoint must forward into that container's loopback, not merely the Proxmox host's loopback. On the user's DE deployment the existing `de-dash` alias and desktop shortcut already implement this route.

Login initially uses `DASHBOARD_USERNAME` and `DASHBOARD_PASSWORD` from `CONFIG/config.py`. A default or too-short password requires changing it before viewing statistics. Passwords changed in the dashboard are hashed and stored separately in `CONFIG/.dashboard_overrides.json`; other sessions are invalidated. Do not commit runtime state, overrides, backups or audit files.

## Isolated live testing

`TG_DASHBOARD_PROJECT_DIR` points to the live bot project when the dashboard code is installed separately. The DE preview is under `/root/Telegram/.dashboard-releases/preview-20261104-v1` with its own launcher. A systemd drop-in selects it; the running bot's module files are not replaced.

For the DE rollback, move the `preview.conf` drop-in out of `/etc/systemd/system/tg-ytdlp-dashboard.service.d/`, reload systemd, and restart **only** `tg-ytdlp-dashboard`. The original dashboard code and service backup are retained. Do not restart `tg-ytdlp-bot` for a panel rollback.

## Validation

With FastAPI, httpx, Jinja2, requests and psutil installed:

```bash
python tests/smoke/test_m_dashboard.py
```

These tests use temporary configuration and fake bot services. They explicitly enable write handlers only for fixtures. They do not prove that production maintenance actions are safe.

For a local visual demo:

```bash
python tests/smoke/dashboard_fixture.py --serve 8765
```

Demo login: `demo` / `demo-password-123`. Never deploy the demo fixture as a production service.

## Known limitations

- Statistics still refresh from the existing collector snapshot; not every value is live.
- First load can take longer than a warm cached request, especially large user/history lists.
- Country, gender and account-age statistics are estimates, not verified demographic data.
- No guarantee of zero vulnerabilities: the production read-only gate remains in place while administrative actions are validated.
