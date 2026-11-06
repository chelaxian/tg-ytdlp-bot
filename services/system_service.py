from __future__ import annotations

try:
    import psutil
except ImportError:  # optional: only the web dashboard reads system metrics (requirements-dashboard.txt)
    psutil = None
import time
import subprocess
import re
import requests
import logging
import shutil
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any
from importlib import import_module, metadata

from CONFIG.config import Config
from DATABASE.cache_db import get_next_reload_time

logger = logging.getLogger(__name__)
BOT_CONTAINER_NAME = os.environ.get("BOT_CONTAINER_NAME", "tg-ytdlp-bot")
WARP_CONTAINER_NAME = os.environ.get("WARP_CONTAINER_NAME", "tg-ytdlp-warp")
# Имя контейнера bgutil-provider должно совпадать с тем, что используется в скриптах / docker-compose.
# По умолчанию это "bgutil-provider" (см. update_bgutil_provider.sh) 
BGUTIL_CONTAINER_NAME = os.environ.get("BGUTIL_CONTAINER_NAME", "bgutil-provider")
# Имена контейнера и systemd-сервиса панели управления (можно переопределить через переменные окружения)
DASHBOARD_CONTAINER_NAME = os.environ.get("DASHBOARD_CONTAINER_NAME", "tg-ytdlp-dashboard")
DASHBOARD_SERVICE_NAME = os.environ.get("DASHBOARD_SERVICE_NAME", "tg-ytdlp-dashboard")


def _has_docker() -> bool:
    """Проверяет наличие docker CLI и сокета."""
    docker_path = shutil.which("docker")
    return bool(docker_path) and Path("/var/run/docker.sock").exists()

def _container_exists(name: str) -> bool:
    """Проверяет, что контейнер с именем name существует (docker ps -a)."""
    if not _has_docker():
        return False
    try:
        result = _run_docker_cmd(
            ["docker", "ps", "-a", "--filter", f"name={name}", "--format", "{{.Names}}"],
            timeout=5,
        )
        if result.returncode != 0:
            logger.warning(f"docker ps failed for container {name}: {result.stderr}")
            return False
        names = [n.strip() for n in result.stdout.splitlines() if n.strip()]
        found = any(n == name for n in names)
        if not found:
            logger.debug(f"Container {name} not found. Available containers: {names}")
        return found
    except Exception as e:
        logger.error(f"Error checking container {name}: {e}")
        return False


def _container_is_running(name: str) -> bool:
    """Проверяет, что контейнер с именем name запущен (docker ps)."""
    if not _has_docker():
        return False
    try:
        result = _run_docker_cmd(
            ["docker", "ps", "--filter", f"name={name}", "--format", "{{.Names}}"],
            timeout=5,
        )
        if result.returncode != 0:
            return False
        names = [n.strip() for n in result.stdout.splitlines() if n.strip()]
        return any(n == name for n in names)
    except Exception as e:
        logger.error(f"Error checking if container {name} is running: {e}")
        return False


def _is_running_in_docker() -> bool:
    """Проверяет, запущен ли текущий процесс внутри Docker контейнера."""
    # Проверяем наличие .dockerenv файла
    if Path("/.dockerenv").exists():
        return True
    # Проверяем cgroup (более надежный способ)
    try:
        with open("/proc/self/cgroup", "r") as f:
            content = f.read()
            # Если находимся в Docker, в cgroup будет упоминание docker
            if "docker" in content or "/docker/" in content:
                return True
    except Exception:
        pass
    return False


def _systemctl_available() -> bool:
    return bool(shutil.which("systemctl"))


def _run_docker_cmd(cmd: list[str], timeout: int = 60, cwd: str | None = None):
    """Запускает docker-cli команду и возвращает CompletedProcess."""
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
        cwd=cwd,
    )


def _run_in_bot(command: list[str], timeout: int = 300):
    """Выполняет команду внутри контейнера с ботом через docker exec."""
    docker_path = shutil.which("docker")
    if not docker_path:
        raise RuntimeError("docker CLI не найден внутри панели")
    cmd = [docker_path, "exec", BOT_CONTAINER_NAME] + command
    return _run_docker_cmd(cmd, timeout=timeout)

# Кеш для скорости сети
_network_speed_cache = {"last_check": 0, "last_sent": 0, "last_recv": 0, "speed_sent": 0, "speed_recv": 0}


def get_network_speed() -> Dict[str, Any]:
    """Вычисляет текущую скорость сети на основе активных потоков."""
    global _network_speed_cache
    if psutil is None:
        return {"speed_sent_mbps": 0, "speed_recv_mbps": 0}
    try:
        now = time.time()
        net_io = psutil.net_io_counters()
        
        # Если прошло меньше секунды с последней проверки, возвращаем кеш
        if now - _network_speed_cache["last_check"] < 1:
            return {
                "speed_sent_mbps": round(_network_speed_cache["speed_sent"] / (1024**2) * 8, 2),
                "speed_recv_mbps": round(_network_speed_cache["speed_recv"] / (1024**2) * 8, 2),
            }
        
        # Вычисляем скорость
        if _network_speed_cache["last_check"] > 0:
            time_diff = now - _network_speed_cache["last_check"]
            sent_diff = net_io.bytes_sent - _network_speed_cache["last_sent"]
            recv_diff = net_io.bytes_recv - _network_speed_cache["last_recv"]
            
            _network_speed_cache["speed_sent"] = sent_diff / time_diff if time_diff > 0 else 0
            _network_speed_cache["speed_recv"] = recv_diff / time_diff if time_diff > 0 else 0
        else:
            _network_speed_cache["speed_sent"] = 0
            _network_speed_cache["speed_recv"] = 0
        
        _network_speed_cache["last_check"] = now
        _network_speed_cache["last_sent"] = net_io.bytes_sent
        _network_speed_cache["last_recv"] = net_io.bytes_recv
        
        return {
            "speed_sent_mbps": round(_network_speed_cache["speed_sent"] / (1024**2) * 8, 2),
            "speed_recv_mbps": round(_network_speed_cache["speed_recv"] / (1024**2) * 8, 2),
        }
    except Exception as e:
        return {"error": str(e)}


_ip_cache = {"value": {"ipv4": "unknown", "ipv6": "unknown"}, "ts": 0.0, "running": False}
_ip_lock = __import__("threading").Lock()
EXTERNAL_IP_TTL = 600


def get_external_ip_cached() -> Dict[str, Any]:
    """External IPs from cache; refreshed in a background thread every 10 min.

    The lookup itself (curl via the WARP container or direct HTTP) can take
    seconds, so a request never waits for it.
    """
    import threading
    now = time.time()
    with _ip_lock:
        stale = now - _ip_cache["ts"] > EXTERNAL_IP_TTL
        if stale and not _ip_cache["running"]:
            _ip_cache["running"] = True

            def _refresh():
                try:
                    value = get_external_ip()
                except Exception:
                    value = {"ipv4": "unknown", "ipv6": "unknown"}
                with _ip_lock:
                    _ip_cache.update(value=value, ts=time.time(), running=False)

            threading.Thread(target=_refresh, name="external_ip", daemon=True).start()
        result = dict(_ip_cache["value"])
        result["checked_at"] = int(_ip_cache["ts"]) or None
    return result


def get_external_ip() -> Dict[str, str]:
    """Получает внешний IPv4 и IPv6 адреса через warp контейнер (если доступен) или напрямую."""
    ipv4 = "unknown"
    ipv6 = "unknown"
    
    # Если есть Docker и контейнер warp запущен, получаем IP через него
    has_docker = _has_docker()
    warp_running = _container_is_running(WARP_CONTAINER_NAME) if has_docker else False
    
    if has_docker and warp_running:
        docker_path = shutil.which("docker")
        if docker_path:
            try:
                # Получаем IPv4 через warp контейнер
                ipv4_result = _run_docker_cmd(
                    [docker_path, "exec", WARP_CONTAINER_NAME, "curl", "-s", "-4", "--max-time", "4", "https://ifconfig.io"],
                    timeout=8,
                )
                if ipv4_result.returncode == 0 and ipv4_result.stdout.strip():
                    ipv4 = ipv4_result.stdout.strip()
                
                # Получаем IPv6 через warp контейнер
                ipv6_result = _run_docker_cmd(
                    [docker_path, "exec", WARP_CONTAINER_NAME, "curl", "-s", "-6", "--max-time", "4", "https://ifconfig.io"],
                    timeout=8,
                )
                if ipv6_result.returncode == 0 and ipv6_result.stdout.strip():
                    ipv6 = ipv6_result.stdout.strip()
                
                # Если получили IP через warp, возвращаем
                if ipv4 != "unknown" or ipv6 != "unknown":
                    return {"ipv4": ipv4, "ipv6": ipv6}
            except Exception as e:
                logger.warning(f"Failed to get IP from warp container: {e}")
                pass
    
    # Fallback: получаем IP напрямую (локальный режим или если warp недоступен)
    try:
        # Получаем IPv4
        ipv4_services = [
            "https://api.ipify.org",
            "https://ifconfig.me/ip",
            "https://icanhazip.com",
        ]
        for service in ipv4_services:
            try:
                response = requests.get(service, timeout=3)
                if response.status_code == 200:
                    ipv4 = response.text.strip()
                    break
            except Exception:
                continue
        
        # Получаем IPv6 через curl -6 ifconfig.io
        try:
            result = subprocess.run(
                ["curl", "-s", "-6", "--max-time", "4", "https://ifconfig.io"],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                ipv6 = result.stdout.strip()
        except Exception:
            pass
        
        # Если IPv6 не получен через curl, пробуем через requests с IPv6
        if ipv6 == "unknown":
            try:
                # Попытка получить IPv6 через специальный сервис
                response = requests.get("https://api64.ipify.org?format=json", timeout=3)
                if response.status_code == 200:
                    data = response.json()
                    if "ip" in data:
                        ipv6_candidate = data["ip"]
                        # Проверяем, что это IPv6 (содержит :)
                        if ":" in ipv6_candidate:
                            ipv6 = ipv6_candidate
            except Exception:
                pass
        
    except Exception:
        pass
    
    return {"ipv4": ipv4, "ipv6": ipv6}


def get_system_metrics() -> Dict[str, Any]:
    """Возвращает метрики системы."""
    if psutil is None:
        return {"error": "psutil is not installed (pip install -r requirements-dashboard.txt)"}
    try:
        cpu_percent = psutil.cpu_percent(interval=None)  # vs. the previous call: never blocks
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        net_io = psutil.net_io_counters()
        boot_time = psutil.boot_time()
        uptime_seconds = time.time() - boot_time
        uptime_days = int(uptime_seconds // 86400)
        uptime_hours = int((uptime_seconds % 86400) // 3600)
        uptime_minutes = int((uptime_seconds % 3600) // 60)
        
        # Время до следующего reload_cache
        interval_hours = getattr(Config, "RELOAD_CACHE_EVERY", 4)
        next_reload = get_next_reload_time(interval_hours)
        now = datetime.now()
        delta = next_reload - now
        reload_seconds = int(delta.total_seconds())
        
        # Скорость сети
        network_speed = get_network_speed()
        
        # Внешний IP (cached, refreshed in the background)
        external_ip = get_external_ip_cached()
        
        return {
            "cpu_percent": round(cpu_percent, 1),
            "memory": {
                "total_gb": round(memory.total / (1024**3), 2),
                "used_gb": round(memory.used / (1024**3), 2),
                "percent": memory.percent,
            },
            "disk": {
                "total_gb": round(disk.total / (1024**3), 2),
                "used_gb": round(disk.used / (1024**3), 2),
                "free_gb": round(disk.free / (1024**3), 2),
                "percent": round(disk.used / disk.total * 100, 1),
            },
            "network": {
                "bytes_sent_mb": round(net_io.bytes_sent / (1024**2), 2),
                "bytes_recv_mb": round(net_io.bytes_recv / (1024**2), 2),
                "speed_sent_mbps": network_speed.get("speed_sent_mbps", 0),
                "speed_recv_mbps": network_speed.get("speed_recv_mbps", 0),
            },
            "external_ip": external_ip,
            "uptime": {
                "days": uptime_days,
                "hours": uptime_hours,
                "minutes": uptime_minutes,
            },
            "next_reload": {
                "datetime": next_reload.isoformat(),
                "seconds": reload_seconds,
            },
            "status": "online",
        }
    except Exception as e:
        logger.warning("[system] metrics failed: %s", e)
        return {"error": "metrics unavailable"}


_versions_cache = {"value": None, "ts": 0.0}


def get_package_versions_cached(max_age: int = 600) -> Dict[str, str]:
    if _versions_cache["value"] is None or time.time() - _versions_cache["ts"] > max_age:
        _versions_cache["value"] = get_package_versions()
        _versions_cache["ts"] = time.time()
    return dict(_versions_cache["value"])


def invalidate_package_versions() -> None:
    _versions_cache["value"] = None


def _read_package_version(
    package_name: str,
    module_name: str | None = None,
    cli_command: list[str] | None = None,
) -> str:
    """Пытается определить версию пакета несколькими способами."""
    try:
        return metadata.version(package_name)
    except metadata.PackageNotFoundError:
        pass
    except Exception:
        pass
    
    if module_name:
        try:
            module = import_module(module_name)
            version = getattr(module, "__version__", None)
            if version:
                return str(version)
        except Exception:
            pass
    
    if cli_command:
        try:
            result = subprocess.run(
                cli_command,
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
            if result.returncode == 0:
                return result.stdout.strip().split()[0]
        except Exception:
            pass
    
    return "unknown"


def _get_bgutil_provider_info() -> str:
    """Возвращает информацию о docker-контейнере bgutil-provider."""
    # Проверяем Docker режим
    if not _has_docker():
        return "docker missing"
    
    # Пытаемся определить контейнер с именем из настроек (по умолчанию "bgutil-provider")
    bgutil_container = BGUTIL_CONTAINER_NAME
    try:
        # Проверяем существование контейнера (строгое совпадение имени)
        if not _container_exists(bgutil_container):
            return "not running"
        
        # Получаем информацию о контейнере
        result = _run_docker_cmd(
            [
                "docker",
                "ps",
                "-a",
                "--filter",
                f"name={bgutil_container}",
                "--format",
                "{{.Names}}|{{.Image}}|{{.Status}}",
            ],
            timeout=5,
        )
        if result.returncode != 0:
            return "docker unavailable"
        line = result.stdout.strip()
        if not line:
            return "not running"
        parts = line.split("|")
        name = parts[0] if len(parts) > 0 else bgutil_container
        image = parts[1] if len(parts) > 1 else "unknown image"
        status = parts[2] if len(parts) > 2 else "unknown status"
        return f"{name} ({image}) — {status}"
    except Exception as e:
        logger.error(f"Error getting bgutil-provider info: {e}")
        return "unknown"


def get_package_versions() -> Dict[str, str]:
    """Возвращает версии установленных пакетов."""
    return {
        "yt-dlp": _read_package_version("yt-dlp", module_name="yt_dlp", cli_command=["yt-dlp", "--version"]),
        "gallery-dl": _read_package_version("gallery-dl", module_name="gallery_dl", cli_command=["gallery-dl", "--version"]),
        "pyrotgfork": _read_package_version("pyrotgfork", module_name="pyrotgfork"),
        "bgutil-provider": _get_bgutil_provider_info(),
    }


def rotate_ip() -> Dict[str, Any]:
    """Ротирует IP: если есть warp-контейнер, рестартуем его; иначе systemctl wgcf."""
    # Проверяем Docker режим: контейнер должен быть запущен, а не просто существовать
    has_docker = _has_docker()
    warp_running = _container_is_running(WARP_CONTAINER_NAME) if has_docker else False
    
    # Docker режим: рестартуем warp контейнер (только если он запущен)
    if has_docker and warp_running:
        docker_path = shutil.which("docker")
        if not docker_path:
            return {"status": "error", "message": "docker CLI not found"}
        try:
            restart = _run_docker_cmd([docker_path, "restart", WARP_CONTAINER_NAME], timeout=40)
            if restart.returncode != 0:
                return {"status": "error", "message": restart.stderr or "Не удалось перезапустить warp"}
            time.sleep(5)  # Даем время на переподключение
            
            # Получаем новый IP через warp контейнер
            ipv4_result = _run_docker_cmd(
                [docker_path, "exec", WARP_CONTAINER_NAME, "curl", "-s", "-4", "https://ifconfig.io"],
                timeout=10,
            )
            ipv4 = ipv4_result.stdout.strip() if ipv4_result.returncode == 0 else "unknown"
            
            ipv6_result = _run_docker_cmd(
                [docker_path, "exec", WARP_CONTAINER_NAME, "curl", "-s", "-6", "https://ifconfig.io"],
                timeout=10,
            )
            ipv6 = ipv6_result.stdout.strip() if ipv6_result.returncode == 0 else "unknown"
            
            return {
                "status": "ok",
                "message": "IP rotated successfully",
                "ipv4": ipv4,
                "ipv6": ipv6,
            }
        except Exception as e:
            logger.error(f"Error rotating IP in Docker mode: {e}")
            return {"status": "error", "message": str(e)}
    
    # Локальный режим - только если Docker точно недоступен
    if not _systemctl_available():
        return {"status": "error", "message": "systemctl is not available (likely running inside Docker)"}
    try:
        cmd = ["systemctl", "restart", "wg-quick@wgcf"]
        if shutil.which("sudo"):
            cmd.insert(0, "sudo")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if result.returncode == 0:
            time.sleep(2)
            new_ips = get_external_ip()
            return {
                "status": "ok",
                "message": "IP rotated successfully",
                "ipv4": new_ips.get("ipv4", "unknown"),
                "ipv6": new_ips.get("ipv6", "unknown"),
            }
        return {"status": "error", "message": result.stderr or "Failed to rotate IP"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def restart_service() -> Dict[str, Any]:
    """Перезапускает сервис: если есть контейнер бота — docker restart, иначе systemctl tg-ytdlp-bot."""
    # Проверяем Docker режим: контейнер должен быть запущен, а не просто существовать
    has_docker = _has_docker()
    bot_running = _container_is_running(BOT_CONTAINER_NAME) if has_docker else False
    
    # Docker режим: перезапускаем контейнер бота (только если он запущен)
    if has_docker and bot_running:
        docker_path = shutil.which("docker")
        if not docker_path:
            return {"status": "error", "message": "docker CLI not found"}
        try:
            result = _run_docker_cmd([docker_path, "restart", BOT_CONTAINER_NAME], timeout=60)
            if result.returncode == 0:
                return {"status": "ok", "message": "Bot container restarted"}
            return {"status": "error", "message": result.stderr or "Failed to restart bot"}
        except Exception as e:
            logger.error(f"Error restarting bot container: {e}")
            return {"status": "error", "message": str(e)}
    
    # Локальный режим - только если Docker точно недоступен
    if not _systemctl_available():
        return {"status": "error", "message": "systemctl is not available (likely running inside Docker)"}
    try:
        cmd = ["systemctl", "restart", "tg-ytdlp-bot"]
        if shutil.which("sudo"):
            cmd.insert(0, "sudo")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if result.returncode == 0:
            return {"status": "ok", "message": "Service restarted successfully"}
        return {"status": "error", "message": result.stderr or "Failed to restart service"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def restart_panel() -> Dict[str, Any]:
    """
    Перезапускает панель управления.
    - В Docker-режиме: docker restart DASHBOARD_CONTAINER_NAME.
    - В локальном режиме: systemctl restart tg-ytdlp-dashboard (или имя из DASHBOARD_SERVICE_NAME).
    """
    has_docker = _has_docker()
    dashboard_running = _container_is_running(DASHBOARD_CONTAINER_NAME) if has_docker else False

    if has_docker and dashboard_running:
        docker_path = shutil.which("docker")
        if not docker_path:
            return {"status": "error", "message": "docker CLI not found"}
        try:
            result = _run_docker_cmd([docker_path, "restart", DASHBOARD_CONTAINER_NAME], timeout=60)
            if result.returncode == 0:
                return {"status": "ok", "message": "Dashboard container restarted"}
            return {"status": "error", "message": result.stderr or "Failed to restart dashboard container"}
        except Exception as e:
            logger.error(f"Error restarting dashboard container: {e}")
            return {"status": "error", "message": str(e)}

    if not _systemctl_available():
        return {"status": "error", "message": "systemctl is not available (likely running inside Docker without dedicated container)"}
    try:
        cmd = ["systemctl", "restart", DASHBOARD_SERVICE_NAME]
        if shutil.which("sudo"):
            cmd.insert(0, "sudo")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if result.returncode == 0:
            return {"status": "ok", "message": "Dashboard service restarted successfully"}
        return {"status": "error", "message": result.stderr or "Failed to restart dashboard service"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def update_engines() -> Dict[str, Any]:
    """Обновляет движки: если есть контейнер бота — docker exec; иначе локальные скрипты."""
    # Docker режим: обновляем через docker exec и docker pull
    # Проверяем наличие Docker и что контейнер бота запущен
    has_docker = _has_docker()
    bot_running = _container_is_running(BOT_CONTAINER_NAME) if has_docker else False
    
    if has_docker and bot_running:
        docker_path = shutil.which("docker")
        if not docker_path:
            return {"status": "error", "message": "docker CLI not found"}
        
        outputs = []
        try:
            # Обновляем yt-dlp и gallery-dl в контейнере бота
            result = _run_in_bot(["bash", "/app/scripts/engines_updater.sh"], timeout=300)
            if result.returncode != 0:
                return {
                    "status": "error",
                    "message": f"yt-dlp/gallery-dl update failed: {result.stderr or 'Update failed'}",
                }
            outputs.append(f"yt-dlp/gallery-dl:\n{result.stdout.strip()}")
            
            # Обновляем bgutil-provider контейнер (он находится вне контейнера dashboard)
            bgutil_container = BGUTIL_CONTAINER_NAME
            if _container_exists(bgutil_container):
                try:
                    # Останавливаем старый контейнер
                    stop_result = _run_docker_cmd([docker_path, "stop", bgutil_container], timeout=30)
                    if stop_result.returncode != 0:
                        logger.warning(f"Failed to stop bgutil-provider: {stop_result.stderr}")
                    
                    # Удаляем старый контейнер
                    rm_result = _run_docker_cmd([docker_path, "rm", bgutil_container], timeout=30)
                    if rm_result.returncode != 0:
                        logger.warning(f"Failed to remove bgutil-provider: {rm_result.stderr}")
                    
                    # Обновляем образ
                    pull_result = _run_docker_cmd(
                        [docker_path, "pull", "brainicism/bgutil-ytdlp-pot-provider:latest"],
                        timeout=120,
                    )
                    if pull_result.returncode != 0:
                        outputs.append(f"bgutil-provider: Failed to pull image: {pull_result.stderr}")
                    else:
                        # Запускаем новый контейнер через docker-compose
                        # Нужно перейти в директорию с docker-compose.yml
                        compose_dir = Path(__file__).resolve().parent.parent
                        compose_result = _run_docker_cmd(
                            [docker_path, "compose", "-f", str(compose_dir / "docker-compose.yml"), "up", "-d", "bgutil-provider"],
                            timeout=60,
                            cwd=str(compose_dir),
                        )
                        if compose_result.returncode == 0:
                            outputs.append("bgutil-provider: Container updated and restarted successfully")
                        else:
                            outputs.append(f"bgutil-provider: Warning - failed to restart: {compose_result.stderr}")
                except Exception as e:
                    logger.error(f"Error updating bgutil-provider: {e}")
                    outputs.append(f"bgutil-provider: Error - {str(e)}")
            else:
                outputs.append("bgutil-provider: Container not found, skipping update")
            
            return {
                "status": "ok",
                "message": "Engines updated successfully",
                "output": "\n\n".join(outputs),
            }
        except Exception as e:
            logger.error(f"Error in update_engines (Docker mode): {e}")
            return {"status": "error", "message": str(e)}
    
    # Локальный режим — старое поведение, проверяем наличие скриптов
    try:
        base_dir = Path(__file__).resolve().parent.parent
        updater = base_dir / "scripts" / "engines_updater.sh"
        provider = base_dir / "scripts" / "update_bgutil_provider.sh"
        if not updater.exists():
            return {"status": "error", "message": f"{updater} not found"}
        if not provider.exists():
            return {"status": "error", "message": f"{provider} not found"}
        commands = [
            ("yt-dlp/gdl", ["bash", str(updater)]),
            ("bgutil-provider", ["bash", str(provider)]),
        ]
        outputs = []
        for label, command in commands:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=300,
                check=False,
                cwd=str(base_dir),
            )
            if result.returncode != 0:
                return {
                    "status": "error",
                    "message": f"{label} failed: {result.stderr or 'Unknown error'}",
                }
            outputs.append(f"{label}:\n{result.stdout.strip()}")
        return {"status": "ok", "message": "Engines updated successfully", "output": "\n\n".join(outputs)}
    except Exception as e:
        logger.error(f"Error in update_engines (local mode): {e}")
        return {"status": "error", "message": str(e)}


def cleanup_user_files() -> Dict[str, Any]:
    """Fail closed: dashboard runs outside the bot's active-task registry.

    A recursive find -delete here removed active .part / split files (#385,
    #460). Importing the in-memory registry in the dashboard does NOT share
    the bot's state. Cleanup must run in the bot process with its task locks.
    """
    return {
        "status": "error",
        "message": (
            "Manual dashboard cleanup is disabled to protect active downloads. "
            "Use the bot /clean command; stale download temp directories are "
            "purged automatically by the bot (default age: 48 hours)."
        ),
    }
