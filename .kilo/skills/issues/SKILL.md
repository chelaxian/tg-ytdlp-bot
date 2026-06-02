---
name: issues
description: Triages all open GitHub issues — classifies into code bugs (fix+close), already-fixed (close), or external/infrastructure (won't fix). Commits fixes and closes issues with detailed comments.
---

# Skill: GitHub Issue Triage & Fix Pipeline

## Overview

This skill automates the complete lifecycle of processing open GitHub issues for the `tg-ytdlp-bot` project. It reads all open issues, cross-references them against the current codebase, classifies each issue, performs fixes where needed, and closes issues with appropriate comments.

## When to Use

- User runs `/issues` command
- Scheduled daily cron execution at 19:00 MSK
- Manual request to "check open issues" or "triage issues"

## Key Project Context

This is a **Telegram bot** (`tg-ytdlp-bot`) that downloads video/audio from various platforms using `yt-dlp`, `gallery-dl`, and `ffmpeg`. It runs on multiple server instances (uae, fr, it, uk).

### Architecture Overview

| Directory | Purpose |
|-----------|---------|
| `DOWN_AND_UP/` | Core download/upload: yt-dlp hook, gallery-dl hook, ffmpeg, sender, live streams |
| `DATABASE/` | Firebase init, cache DB (video/playlist caching), Firebase dump loader |
| `URL_PARSERS/` | URL extraction, normalization, engine routing, thumbnail download, tags |
| `HELPERS/` | Utilities: logging, proxies, rate limiting, filename sanitization, captions |
| `COMMANDS/` | Telegram command handlers: /cookies, /settings, /proxy, /img, /search, etc. |
| `CONFIG/` | Configuration: config.py, limits, domains, messages, 26 languages |
| `services/` | Stats, auth, system services |
| `cookies/` | Cookie storage for platform auth |

### Key Files to Check for Common Issues

| Issue Type | Files to Check |
|------------|---------------|
| Cover/thumbnail embedding | `DOWN_AND_UP/down_and_audio.py` (`embed_cover_mp3`), `DOWN_AND_UP/down_and_up.py` (postprocessors) |
| Cache corruption | `DATABASE/cache_db.py` (`get_cached_playlist_videos`, `save_to_playlist_cache`) |
| Filename sanitization | `HELPERS/filesystem_hlp.py` (`sanitize_filename`), `DOWN_AND_UP/down_and_up.py` (match_filter) |
| Telegram send errors | `DOWN_AND_UP/sender.py` (retry/backoff logic, FloodWait handling) |
| Format fallback | `DOWN_AND_UP/down_and_audio.py`, `DOWN_AND_UP/yt_dlp_hook.py` |
| Proxy handling | `HELPERS/proxy_helper.py`, `HELPERS/fallback_helper.py` |
| Cookie management | `COMMANDS/cookies_cmd.py` |
| Gallery-dl fallback | `DOWN_AND_UP/gallery_dl_hook.py`, `HELPERS/fallback_helper.py` |

## Classification Criteria

### Category A: Code Bug (fix and close)

The issue describes an error traceable to bot code:
- `subprocess.run()` with `text=True` causing decode errors on binary data
- Cache data type mismatches (dict vs list) without type guards
- Missing error handling for specific exceptions
- Incorrect logic in fallback chains

**Required actions:**
1. Read the specific source file and function
2. Confirm the bug still exists in current code
3. Make minimal surgical fix
4. `git commit -m "fix: <description> (issue #N)"` → `git push`
5. `gh issue close N --repo chelaxian/tg-ytdlp-bot --comment "<fix details>"`

### Category B: Already Fixed (close with confirmation)

Indicators that an issue is already resolved:
- Comment says "Fixed in PR #XXX" — verify the fix exists in code
- `isinstance()` type guards already present where `TypeError` was reported
- Retry/backoff logic already implemented where timeouts were reported
- Fallback mechanisms already in place where missing features were requested
- `sanitize_filename()` or `match_filter` already handling filename issues

**Required actions:**
1. Read the relevant code to confirm the fix is present
2. `gh issue close N --repo chelaxian/tg-ytdlp-bot --comment "Confirmed fixed in current code: <details>"`

### Category C: External / Won't Fix (close as not planned)

Common external causes that **cannot** be fixed in bot code:
- **Platform rate limiting**: HTTP 429 from YouTube, TikTok, Instagram, Twitter
- **IP blocking**: TikTok, Instagram blocking server IP
- **DRM protection**: Spotify, Crunchyroll — fundamentally unsupported
- **Authentication walls**: YouTube "Sign in to confirm you're not a bot", age verification
- **Content unavailability**: Deleted videos, private accounts, copyright claims, removed by uploader
- **Geo-restrictions**: "blocked in your country on copyright grounds"
- **Infrastructure**: Outdated pip packages on server (pyrotgfork), Firebase timeouts, network issues
- **Third-party bugs**: yt-dlp extractor errors for specific platforms (Yandex Music)
- **Unsupported URLs**: YouTube channel URLs, APK files, GitHub releases
- **Cookie expiration**: User's Instagram/YouTube cookies expired
- **Telegram API limits**: FloodWait, upload slots busy — already handled in code

**Required actions:**
1. `gh issue close N --repo chelaxian/tg-ytdlp-bot --reason "not planned" --comment "Won't fix: <reason>. Cannot be resolved at the code level."`

## Execution Checklist

```
[ ] 1. gh issue list — get all open issues
[ ] 2. For each issue: read body + comments
[ ] 3. For each issue: read relevant source code
[ ] 4. Classify: A (code bug) / B (already fixed) / C (won't fix)
[ ] 5. Fix Category A issues → commit → push → close
[ ] 6. Close Category B issues with confirmation comments
[ ] 7. Close Category C issues as "not planned"
[ ] 8. Print summary table
[ ] 9. Verify zero open issues remain
```

## Cron Schedule

This skill runs daily at **19:00 MSK (UTC+3)** = **16:00 UTC** via Windows Task Scheduler.

See `scripts/issues_cron.ps1` for the scheduled task setup script.
