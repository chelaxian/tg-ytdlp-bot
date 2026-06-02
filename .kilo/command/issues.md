---
name: issues
description: Triages all open GitHub issues — classifies into code bugs (fix+close), already-fixed (close), or external/infrastructure (won't fix). Commits fixes and closes issues with detailed comments.
---

# /issues — GitHub Issue Triage & Fix Pipeline

You are running a **full triage pipeline** for all open issues in the repository `chelaxian/tg-ytdlp-bot`.

## Input

The user may optionally pass `$ARGUMENTS` to override the GitHub repo (default: `chelaxian/tg-ytdlp-bot`). Otherwise use the default repo from git remote.

## Step-by-Step Procedure

### Phase 1: Gather Issues

1. Run `gh issue list --repo <REPO> --state open --limit 50` to get all open issues.
2. If no open issues exist, report "No open issues found" and STOP.
3. For each issue, fetch full details: `gh issue view <NUMBER> --repo <REPO> --json title,body,labels` and `gh issue view <NUMBER> --repo <REPO> --comments`.
4. Read and analyze issue body + all comments for context about prior fixes, status updates, and root cause analysis.

### Phase 2: Understand Project Code

5. Explore the project structure focusing on key directories: `DOWN_AND_UP/`, `DATABASE/`, `URL_PARSERS/`, `HELPERS/`, `COMMANDS/`, `CONFIG/`.
6. For each issue, identify the relevant code files and functions mentioned in the error messages.
7. Read the relevant source code to verify whether the bug still exists.

### Phase 3: Classify Each Issue

For each issue, assign exactly one category:

#### Category A: Code Bug (fix required)
- The issue describes a reproducible error in the bot's own code.
- After reading the source, the bug is **confirmed to still exist**.
- **Action**: Fix the bug, commit, push, then close issue with fix comment.

#### Category B: Already Fixed
- Comments on the issue say "Fixed in PR #XXX".
- **OR** after reading the current source code, the described fix is already present (e.g., `isinstance()` checks added, retry logic implemented, fallback mechanism exists).
- **Action**: Close with comment confirming the fix exists in current code.

#### Category C: External / Infrastructure / Won't Fix
- Platform-side restrictions: DRM, rate limiting, IP blocking, geo-restrictions.
- Authentication requirements: YouTube "sign in", Instagram cookies expired, age verification.
- Content unavailability: deleted videos, private accounts, copyright claims.
- Infrastructure issues: outdated pip packages on server, network timeouts, Firebase connectivity.
- Third-party bugs: yt-dlp extractor errors, gallery-dl unsupported URLs.
- User errors: unsupported URL types, forbidden content, APK files.
- **Action**: Close with `--reason "not planned"` and a clear "Won't fix" comment explaining why it cannot be resolved in code.

### Phase 4: Execute

8. **Process Category A first** (code bugs):
   - Make minimal surgical fixes to the identified code.
   - Run `git status` and `git diff` to review changes.
   - Commit with descriptive message referencing the issue number.
   - Push to current branch (or create a new branch if changes are risky).
   - Close the issue with: `gh issue close <NUM> --repo <REPO> --comment "<fix description>"`.

9. **Process Category B** (already fixed):
   - Close each with: `gh issue close <NUM> --repo <REPO> --comment "Confirmed fixed in current code. <details>"`.

10. **Process Category C** (won't fix):
    - Close each with: `gh issue close <NUM> --repo <REPO> --reason "not planned" --comment "Won't fix: <reason>. Cannot be resolved at the code level."`.

### Phase 5: Report

11. Print a summary table:

| Category | Count | Issue Numbers |
|----------|-------|---------------|
| Fixed (code bug) | N | #xxx, #yyy |
| Already fixed (closed) | N | #xxx, #yyy |
| Won't fix (external) | N | #xxx, #yyy |

12. Report total issues processed and confirm zero open issues remain.

## Important Rules

- **Always verify against current code** — never assume an issue is still valid just because it's open. Many issues may have been fixed in later commits.
- **Never make risky changes** — if a code fix seems dangerous or could break existing functionality, create a new branch.
- **Small safe fixes** can be committed directly to the current branch without asking.
- **When in doubt** about whether a fix is safe, ask the user before proceeding.
- **Close issues with meaningful comments** — explain what was done and why.
- **Respect the language rules** — respond in Russian, code comments in English.
- After fixing code bugs, always do `git push` to the remote.
