#!/usr/bin/env python3
import datetime as _dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path


REPO = os.environ.get("GITHUB_ISSUES_REPO", "chelaxian/tg-ytdlp-bot")
BASE_BRANCH = os.environ.get("AUTOISSUE_BASE", "autoissue")
LABEL = os.environ.get("AUTOISSUE_LABEL", "autoissue")
WORKDIR = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = WORKDIR / "AUTOISSUE"


def sh(args, check=True, capture=True, cwd=WORKDIR, env=None) -> subprocess.CompletedProcess:
    e = os.environ.copy()
    if env:
        e.update(env)
    return subprocess.run(
        args,
        cwd=str(cwd),
        env=e,
        check=check,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
        text=True,
    )


def gh_json(args) -> object:
    cp = sh(["gh", *args], check=True, capture=True)
    if not cp.stdout.strip():
        return None
    return json.loads(cp.stdout)


def utc_now_iso() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).isoformat(timespec="seconds")


def normalize_branch_name(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:50] or "issue"


def snapshot_path(issue_number: int) -> Path:
    return SNAPSHOT_DIR / f"issue-{issue_number}.md"


def build_snapshot(issue: dict) -> str:
    n = issue["number"]
    title = issue.get("title", "").strip()
    body = (issue.get("body") or "").rstrip()
    url = issue.get("url") or issue.get("html_url") or ""
    labels = [l["name"] for l in (issue.get("labels") or []) if isinstance(l, dict) and "name" in l]
    labels_str = ", ".join(labels) if labels else "-"
    updated = issue.get("updatedAt") or issue.get("updated_at") or "-"
    return (
        f"# Issue #{n}: {title}\n\n"
        f"- Repo: `{REPO}`\n"
        f"- URL: `{url}`\n"
        f"- Labels: {labels_str}\n"
        f"- Issue updatedAt: `{updated}`\n"
        f"- Snapshot updatedAt: `{utc_now_iso()}`\n\n"
        "## Body\n\n"
        "```text\n"
        f"{body}\n"
        "```\n"
    )


def ensure_repo_clean():
    cp = sh(["git", "status", "--porcelain"])
    if cp.stdout.strip():
        raise RuntimeError("Working tree is not clean")


def git_fetch_origin():
    sh(["git", "fetch", "origin", "--prune"], capture=False)


def ensure_base_branch_exists():
    # Ensure origin/<BASE_BRANCH> exists locally
    sh(["git", "fetch", "origin", BASE_BRANCH], capture=False)


def checkout_branch(branch: str):
    sh(["git", "checkout", "-B", branch, f"origin/{branch}"] if branch != BASE_BRANCH else ["git", "checkout", BASE_BRANCH])


def create_branch_from_base(branch: str):
    sh(["git", "checkout", "-B", branch, f"origin/{BASE_BRANCH}"])


def commit_if_needed(message: str) -> bool:
    cp = sh(["git", "status", "--porcelain"])
    if not cp.stdout.strip():
        return False
    sh(["git", "add", "-A"])
    sh(["git", "commit", "-m", message], capture=False)
    return True


def push_branch(branch: str):
    sh(["git", "push", "-u", "origin", branch], capture=False)


def try_merge_base_into_branch(branch: str) -> bool:
    """
    Merge origin/<BASE_BRANCH> into branch. Returns True if merge commit created and pushed.
    If merge fails, returns False (and leaves branch unchanged thanks to abort).
    """
    sh(["git", "checkout", branch], capture=False)
    # Fast-forward base ref
    sh(["git", "fetch", "origin", BASE_BRANCH], capture=False)
    try:
        sh(["git", "merge", "--no-edit", f"origin/{BASE_BRANCH}"], capture=False)
    except subprocess.CalledProcessError:
        # abort merge
        try:
            sh(["git", "merge", "--abort"], check=False, capture=False)
        except Exception:
            pass
        return False
    # If merge produced no changes, git merge exits 0 but may still say "Already up to date."
    sh(["git", "push", "origin", branch], capture=False)
    return True


def find_pr_for_issue(issue_number: int, prs: list[dict]) -> dict | None:
    needle = f"#{issue_number}"
    for pr in prs:
        body = pr.get("body") or ""
        title = pr.get("title") or ""
        if needle in title or f"Fixes #{issue_number}" in body or f"Closes #{issue_number}" in body:
            return pr
    return None


def retarget_pr_base(pr_number: int):
    # Use REST API to avoid gh pr edit GraphQL issues
    sh(
        [
            "gh",
            "api",
            "--method",
            "PATCH",
            "-H",
            "Accept: application/vnd.github+json",
            f"/repos/{REPO}/pulls/{pr_number}",
            "-f",
            f"base={BASE_BRANCH}",
        ],
        capture=False,
    )


def add_label_to_pr(pr_number: int):
    try:
        sh(["gh", "pr", "edit", str(pr_number), "--repo", REPO, "--add-label", LABEL], capture=False)
    except subprocess.CalledProcessError:
        # label may not exist; ignore
        pass


def comment_pr(pr_number: int, body: str):
    sh(["gh", "pr", "comment", str(pr_number), "--repo", REPO, "--body", body], capture=False)


def main() -> int:
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    ensure_repo_clean()
    git_fetch_origin()
    ensure_base_branch_exists()

    # Get open issues
    issues = gh_json(
        [
            "issue",
            "list",
            "--repo",
            REPO,
            "--state",
            "open",
            "--limit",
            "200",
            "--json",
            "number,title,body,labels,updatedAt,url",
        ]
    ) or []

    # Get open PRs (base can be anything; we retarget)
    prs = gh_json(
        [
            "pr",
            "list",
            "--repo",
            REPO,
            "--state",
            "open",
            "--limit",
            "200",
            "--json",
            "number,title,body,headRefName,baseRefName,url",
        ]
    ) or []

    for issue in issues:
        n = int(issue["number"])
        title = (issue.get("title") or "").strip()
        pr = find_pr_for_issue(n, prs)
        desired_branch = f"autoissue/issue-{n}-{normalize_branch_name(title)}"

        if pr is None:
            # Create branch + snapshot file + PR
            create_branch_from_base(desired_branch)
            sp = snapshot_path(n)
            sp.write_text(build_snapshot(issue), encoding="utf-8")
            committed = commit_if_needed(f"chore(autoissue): snapshot issue #{n}")
            if committed:
                push_branch(desired_branch)
                pr_url = sh(
                    [
                        "gh",
                        "pr",
                        "create",
                        "--repo",
                        REPO,
                        "--head",
                        desired_branch,
                        "--base",
                        BASE_BRANCH,
                        "--title",
                        f"autoissue: issue #{n} - {title}",
                        "--body",
                        f"Automated snapshot PR for issue #{n}.\n\nFixes #{n}\n",
                        "--draft",
                    ]
                ).stdout.strip()
                # Label it if possible
                try:
                    pr_num = int(re.search(r"/pull/(\\d+)$", pr_url).group(1)) if pr_url else None
                except Exception:
                    pr_num = None
                if pr_num:
                    add_label_to_pr(pr_num)
            continue

        pr_number = int(pr["number"])
        head = pr.get("headRefName")
        base = pr.get("baseRefName")

        # Ensure base branch is correct
        if base != BASE_BRANCH:
            retarget_pr_base(pr_number)

        # Sync branch with base (best effort)
        if head:
            # Ensure local branch exists
            sh(["git", "fetch", "origin", head], capture=False, check=False)
            sh(["git", "checkout", "-B", head, f"origin/{head}"], capture=False)
            merged = try_merge_base_into_branch(head)
            if not merged:
                comment_pr(
                    pr_number,
                    f"⚠️ Autoissue bot: не смог автоматически смержить `{BASE_BRANCH}` в `{head}` (конфликт или состояние ветки).",
                )

            # Update snapshot if exists and differs
            sp = snapshot_path(n)
            if sp.exists():
                current = sp.read_text(encoding="utf-8")
                desired = build_snapshot(issue)
                if current != desired:
                    sp.write_text(desired, encoding="utf-8")
                    if commit_if_needed(f"chore(autoissue): refresh snapshot issue #{n}"):
                        push_branch(head)

        add_label_to_pr(pr_number)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(f"autoissue_daily failed: {e}", file=sys.stderr)
        raise

