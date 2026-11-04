"""Long dashboard actions run as background jobs.

A request only starts a job and returns its id at once; the page polls
/api/jobs/<id> for state and the tail of the output. One job per kind may run at
a time (a second start gets "busy"), so a double click never runs an update or a
restart twice. Child processes are never killed on a timeout (pip killed halfway
leaves a broken venv); a job can be cancelled explicitly where that is safe.
"""

from __future__ import annotations

import logging
import os
import secrets
import shutil
import subprocess
import threading
import time
from collections import deque
from pathlib import Path
from typing import Any, Callable, Deque, Dict, List, Optional

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
MAX_HISTORY = 30


def _euid() -> int:
    return os.geteuid() if hasattr(os, "geteuid") else 0


class JobBusy(RuntimeError):
    pass


class JobCancelled(RuntimeError):
    pass


class Job:
    def __init__(self, kind: str, user: str, params: Dict[str, Any]):
        self.id = secrets.token_hex(6)
        self.kind = kind
        self.user = user
        self.params = params
        self.state = "running"          # running | waiting | succeeded | failed | cancelled
        self.message = ""
        self.started = time.time()
        self.finished: Optional[float] = None
        self.lines: Deque[str] = deque(maxlen=200)
        self.cancel_event = threading.Event()
        self.cancellable = False
        self._proc: Optional[subprocess.Popen] = None

    def log(self, line: str) -> None:
        line = line.rstrip()
        if line:
            self.lines.append(line[:500])

    def check_cancel(self) -> None:
        if self.cancel_event.is_set():
            raise JobCancelled()

    def public(self) -> Dict[str, Any]:
        return {
            "id": self.id, "kind": self.kind, "state": self.state, "message": self.message,
            "started": int(self.started), "finished": int(self.finished) if self.finished else None,
            "cancellable": self.cancellable and self.state in ("running", "waiting"),
            "params": {k: v for k, v in self.params.items() if k in ("mode",)},
            "output": list(self.lines)[-80:],
        }

    def run_command(self, argv: List[str], cwd: Optional[Path] = None, env: Optional[dict] = None) -> int:
        """Run a fixed argv (never a shell string), streaming its output into the job log."""
        self.log("$ " + " ".join(os.path.basename(argv[0]) if i == 0 else a for i, a in enumerate(argv)))
        proc = subprocess.Popen(
            argv, cwd=str(cwd or BASE_DIR), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, bufsize=1, env=env, stdin=subprocess.DEVNULL,
        )
        self._proc = proc
        assert proc.stdout is not None
        for line in proc.stdout:
            self.log(line)
        code = proc.wait()
        self._proc = None
        self.log(f"exit code {code}")
        return code


class JobManager:
    def __init__(self):
        self._lock = threading.Lock()
        self._jobs: Dict[str, Job] = {}
        self._running: Dict[str, str] = {}   # kind -> job id

    def start(self, kind: str, user: str, target: Callable[[Job], str], params: Optional[Dict[str, Any]] = None,
              cancellable: bool = False) -> Job:
        with self._lock:
            running_id = self._running.get(kind)
            if running_id and self._jobs[running_id].state in ("running", "waiting"):
                raise JobBusy(running_id)
            job = Job(kind, user, params or {})
            job.cancellable = cancellable
            self._jobs[job.id] = job
            self._running[kind] = job.id
            self._trim_locked()
        threading.Thread(target=self._run, args=(job, target), name=f"job_{kind}", daemon=True).start()
        logger.info("[jobs] %s started by %s (%s)", kind, user, job.id)
        return job

    def _run(self, job: Job, target: Callable[[Job], str]) -> None:
        try:
            job.message = target(job) or ""
            job.state = "succeeded"
        except JobCancelled:
            job.state = "cancelled"
            job.message = "cancelled"
        except Exception as exc:
            job.state = "failed"
            job.message = str(exc)[:300] if isinstance(exc, (RuntimeError, ValueError)) else "failed"
            logger.exception("[jobs] %s failed", job.kind)
        finally:
            job.finished = time.time()
            logger.info("[jobs] %s finished: %s", job.kind, job.state)

    def running_id(self, kind: str) -> Optional[str]:
        """Id of the job of this kind that is still running, if any."""
        with self._lock:
            job_id = self._running.get(kind)
            job = self._jobs.get(job_id) if job_id else None
            return job.id if job and job.state in ("running", "waiting") else None

    def get(self, job_id: str) -> Optional[Job]:
        with self._lock:
            return self._jobs.get(job_id)

    def list(self) -> List[Dict[str, Any]]:
        with self._lock:
            jobs = sorted(self._jobs.values(), key=lambda j: j.started, reverse=True)
        return [j.public() for j in jobs[:MAX_HISTORY]]

    def cancel(self, job_id: str) -> bool:
        job = self.get(job_id)
        if not job or not job.cancellable or job.state not in ("running", "waiting"):
            return False
        job.cancel_event.set()
        return True

    def _trim_locked(self) -> None:
        if len(self._jobs) <= MAX_HISTORY:
            return
        done = sorted((j for j in self._jobs.values() if j.finished), key=lambda j: j.started)
        for job in done[: len(self._jobs) - MAX_HISTORY]:
            self._jobs.pop(job.id, None)


manager = JobManager()


# --------------------------------------------------------------------------------------
# Actions
# --------------------------------------------------------------------------------------

def _system():
    from services import system_service
    return system_service


def _docker_bot_mode() -> bool:
    ss = _system()
    return ss._has_docker() and ss._container_is_running(ss.BOT_CONTAINER_NAME)


def restart_bot(job: Job) -> str:
    from HELPERS import runtime_status
    mode = job.params.get("mode", "now")
    max_wait = int(job.params.get("max_wait", 1800))
    if mode == "idle":
        job.state = "waiting"
        job.log("Waiting until the bot has no running or queued tasks")
        quiet_since = None
        deadline = time.time() + max_wait
        while True:
            job.check_cancel()
            status = runtime_status.read()
            busy = int(status.get("running") or 0) + int(status.get("queued") or 0)
            if not status.get("alive"):
                raise RuntimeError("cannot confirm idle state: bot heartbeat is missing")
            if busy == 0:
                quiet_since = quiet_since or time.time()
                if time.time() - quiet_since >= 10:
                    job.log("Idle for 10 s")
                    break
            else:
                quiet_since = None
            if time.time() > deadline:
                raise RuntimeError("the bot did not become idle in time")
            time.sleep(2)
        job.state = "running"
    before = runtime_status.read()
    restarted_at = time.time()
    ss = _system()
    if _docker_bot_mode():
        code = job.run_command([shutil.which("docker") or "docker", "restart", "-t", "60", ss.BOT_CONTAINER_NAME])
    else:
        cmd = ["systemctl", "restart", "tg-ytdlp-bot"]
        if _euid() != 0 and shutil.which("sudo"):
            cmd.insert(0, "sudo")
        code = job.run_command(cmd)
    if code != 0:
        raise RuntimeError("restart command failed")
    job.log("Waiting for the bot to report in")
    deadline = time.time() + 180
    while time.time() < deadline:
        status = runtime_status.read()
        if status.get("alive") and int(status.get("started_at") or 0) >= int(restarted_at) - 1 \
                and status.get("pid") != before.get("pid"):
            return "bot restarted"
        time.sleep(2)
    raise RuntimeError("restart command sent but bot recovery was not confirmed")


def restart_panel(job: Job) -> str:
    ss = _system()

    def later():
        time.sleep(1.5)
        try:
            if ss._has_docker() and ss._container_is_running(ss.DASHBOARD_CONTAINER_NAME):
                subprocess.Popen([shutil.which("docker") or "docker", "restart", ss.DASHBOARD_CONTAINER_NAME])
            else:
                cmd = ["systemctl", "restart", ss.DASHBOARD_SERVICE_NAME]
                if _euid() != 0 and shutil.which("sudo"):
                    cmd.insert(0, "sudo")
                subprocess.Popen(cmd)
        except Exception:
            logger.exception("[jobs] panel restart failed")

    threading.Thread(target=later, daemon=True).start()
    job.log("Panel restart scheduled")
    return "panel restarting"


def update_engines(job: Job) -> str:
    ss = _system()
    if _docker_bot_mode():
        code = job.run_command([shutil.which("docker") or "docker", "exec", ss.BOT_CONTAINER_NAME,
                                "bash", "/app/scripts/engines_updater.sh"])
        if code != 0:
            raise RuntimeError("engines update failed")
    else:
        updater = BASE_DIR / "scripts" / "engines_updater.sh"
        if not updater.exists():
            raise RuntimeError("scripts/engines_updater.sh not found")
        if job.run_command(["bash", str(updater)]) != 0:
            raise RuntimeError("engines update failed")
        provider = BASE_DIR / "scripts" / "update_bgutil_provider.sh"
        if provider.exists() and job.run_command(["bash", str(provider)]) != 0:
            job.log("bgutil provider update failed (engines are updated)")
    ss.invalidate_package_versions()
    job.log("Restart the bot to load the new versions")
    return "engines updated"


def update_lists(job: Job) -> str:
    from services import lists_service
    urls = job.params.get("urls") or {}
    if urls:
        counts = lists_service.update_lists_from_urls(urls.get("porn_domains", ""), urls.get("porn_keywords", ""),
                                                      log=job.log)
        return ", ".join(f"{k}: {v}" for k, v in counts.items())
    script = lists_service.local_update_script()
    if script is None:
        raise RuntimeError("need_urls")
    if job.run_command(["bash", str(script)]) != 0:
        raise RuntimeError("list update script failed")
    return "lists updated"
