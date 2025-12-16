from __future__ import annotations

import psutil
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
                    [docker_path, "exec", WARP_CONTAINER_NAME, "curl", "-s", "-4", "https://ifconfig.io"],
                    timeout=10,
                )
                if ipv4_result.returncode == 0 and ipv4_result.stdout.strip():
                    ipv4 = ipv4_result.stdout.strip()
                
                # Получаем IPv6 через warp контейнер
                ipv6_result = _run_docker_cmd(
                    [docker_path, "exec", WARP_CONTAINER_NAME, "curl", "-s", "-6", "https://ifconfig.io"],
                    timeout=10,
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
                ["curl", "-6", "ifconfig.io"],
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
    try:
        cpu_percent = psutil.cpu_percent(interval=0.1)
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
        
        # Внешний IP
        external_ip = get_external_ip()
        
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
        return {"error": str(e)}


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
            result = _run_in_bot(["bash", "/app/engines_updater.sh"], timeout=300)
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
        updater = base_dir / "engines_updater.sh"
        provider = base_dir / "update_bgutil_provider.sh"
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
    """Удаляет файлы из папок пользователей (кроме системных)."""
    try:
        base_dir = Path(__file__).resolve().parent.parent
        users_dir = getattr(Config, "USERS_DIR", "users")
        users_path = Path(users_dir)
        if not users_path.is_absolute():
            users_path = base_dir / users_path
        result = subprocess.run(
            [
                "/usr/bin/find",
                str(users_path),
                "-type", "f",
                "!", "-name", "lang.txt",
                "!", "-name", "args.txt",
                "!", "-name", "keyboard.txt",
                "!", "-name", "subs.txt",
                "!", "-name", "subs_auto.txt",
                "!", "-name", "mediainfo.txt",
                "!", "-name", "split.txt",
                "!", "-name", "tags.txt",
                "!", "-name", "cookie.txt",
                "!", "-name", "logs.txt",
                "!", "-name", "format.txt",
                "-delete",
            ],
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
        if result.returncode == 0:
            return {"status": "ok", "message": "User files cleaned up successfully"}
        else:
            return {"status": "error", "message": result.stderr or "Failed to cleanup files"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def update_lists() -> Dict[str, Any]:
    """Обновляет списки через script.sh."""
    try:
        script_path = "/root/Telegram/tg-ytdlp-bot/script.sh"
        result = subprocess.run(
            ["bash", script_path],
            capture_output=True,
            text=True,
            timeout=300,  # 5 минут
            check=False,
        )
        if result.returncode == 0:
            return {"status": "ok", "message": "Lists updated successfully", "output": result.stdout}
        else:
            return {"status": "error", "message": result.stderr or "Failed to update lists"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def get_config_settings() -> Dict[str, Any]:
    """Возвращает редактируемые настройки из конфига."""
    # Собираем все YouTube cookie URLs, включая пустые значения
    # Используем getattr с дефолтом "" для безопасной обработки отсутствующих атрибутов
    youtube_cookie_urls = []
    try:
        # Основной URL
        main_url = getattr(Config, "YOUTUBE_COOKIE_URL", "")
        youtube_cookie_urls.append(str(main_url) if main_url else "")
    except (AttributeError, TypeError):
        youtube_cookie_urls.append("")
    
    # Дополнительные URL (1-10)
    for idx in range(1, 11):
        try:
            url = getattr(Config, f"YOUTUBE_COOKIE_URL_{idx}", "")
            youtube_cookie_urls.append(str(url) if url else "")
        except (AttributeError, TypeError):
            youtube_cookie_urls.append("")
    return {
        "proxy": {
            "type": getattr(Config, "PROXY_TYPE", ""),
            "ip": getattr(Config, "PROXY_IP", ""),
            "port": getattr(Config, "PROXY_PORT", ""),
            "user": getattr(Config, "PROXY_USER", ""),
            "password": getattr(Config, "PROXY_PASSWORD", ""),
        },
        "proxy_2": {
            "type": getattr(Config, "PROXY_2_TYPE", ""),
            "ip": getattr(Config, "PROXY_2_IP", ""),
            "port": getattr(Config, "PROXY_2_PORT", ""),
            "user": getattr(Config, "PROXY_2_USER", ""),
            "password": getattr(Config, "PROXY_2_PASSWORD", ""),
        },
        "proxy_select": getattr(Config, "PROXY_SELECT", "random"),
        "cookies": {
            "youtube": getattr(Config, "YOUTUBE_COOKIE_URL", ""),
            "instagram": getattr(Config, "INSTAGRAM_COOKIE_URL", ""),
            "tiktok": getattr(Config, "TIKTOK_COOKIE_URL", ""),
            "twitter": getattr(Config, "TWITTER_COOKIE_URL", ""),
            "vk": getattr(Config, "VK_COOKIE_URL", ""),
        },
        "youtube_cookies": {
            "order": getattr(Config, "YOUTUBE_COOKIE_ORDER", "round_robin"),
            "test_url": getattr(Config, "YOUTUBE_COOKIE_TEST_URL", ""),
            "cookie_url": getattr(Config, "COOKIE_URL", ""),
            "pot_base_url": getattr(Config, "YOUTUBE_POT_BASE_URL", ""),
            "list": youtube_cookie_urls,
        },
        "channels": {
            "logs_id": getattr(Config, "LOGS_ID", ""),
            "logs_video_id": getattr(Config, "LOGS_VIDEO_ID", ""),
            "logs_nsfw_id": getattr(Config, "LOGS_NSFW_ID", ""),
            "logs_img_id": getattr(Config, "LOGS_IMG_ID", ""),
            "logs_paid_id": getattr(Config, "LOGS_PAID_ID", ""),
            "log_exception": getattr(Config, "LOG_EXCEPTION", ""),
            "subscribe_channel": getattr(Config, "SUBSCRIBE_CHANNEL", ""),
        },
        "allowed_groups": getattr(Config, "ALLOWED_GROUP", []),
        "admins": getattr(Config, "ADMIN", []),
        "miniapp_url": getattr(Config, "MINIAPP_URL", ""),
        "subscribe_channel_url": getattr(Config, "SUBSCRIBE_CHANNEL_URL", ""),
        "dashboard": {
            "username": getattr(Config, "DASHBOARD_USERNAME", "admin"),
            "password": getattr(Config, "DASHBOARD_PASSWORD", ""),  # Не показываем пароль в API
        },
    }


def update_config_setting(key: str, value: Any) -> bool:
    """Обновляет настройку в CONFIG/config.py."""
    config_path = Path(__file__).parent.parent / "CONFIG" / "config.py"
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        # Простое обновление через поиск строки
        patterns = {
            "PROXY_TYPE": r'^\s*PROXY_TYPE\s*=',
            "PROXY_IP": r'^\s*PROXY_IP\s*=',
            "PROXY_PORT": r'^\s*PROXY_PORT\s*=',
            "PROXY_USER": r'^\s*PROXY_USER\s*=',
            "PROXY_PASSWORD": r'^\s*PROXY_PASSWORD\s*=',
            "PROXY_2_TYPE": r'^\s*PROXY_2_TYPE\s*=',
            "PROXY_2_IP": r'^\s*PROXY_2_IP\s*=',
            "PROXY_2_PORT": r'^\s*PROXY_2_PORT\s*=',
            "PROXY_2_USER": r'^\s*PROXY_2_USER\s*=',
            "PROXY_2_PASSWORD": r'^\s*PROXY_2_PASSWORD\s*=',
            "PROXY_SELECT": r'^\s*PROXY_SELECT\s*=',
            "MINIAPP_URL": r'^\s*MINIAPP_URL\s*=',
            "SUBSCRIBE_CHANNEL_URL": r'^\s*SUBSCRIBE_CHANNEL_URL\s*=',
            "YOUTUBE_COOKIE_URL": r'^\s*YOUTUBE_COOKIE_URL\s*=',
            "INSTAGRAM_COOKIE_URL": r'^\s*INSTAGRAM_COOKIE_URL\s*=',
            "TIKTOK_COOKIE_URL": r'^\s*TIKTOK_COOKIE_URL\s*=',
            "TWITTER_COOKIE_URL": r'^\s*TWITTER_COOKIE_URL\s*=',
            "VK_COOKIE_URL": r'^\s*VK_COOKIE_URL\s*=',
            "COOKIE_URL": r'^\s*COOKIE_URL\s*=',
            "YOUTUBE_COOKIE_ORDER": r'^\s*YOUTUBE_COOKIE_ORDER\s*=',
            "YOUTUBE_COOKIE_TEST_URL": r'^\s*YOUTUBE_COOKIE_TEST_URL\s*=',
            "YOUTUBE_POT_BASE_URL": r'^\s*YOUTUBE_POT_BASE_URL\s*=',
            "LOGS_ID": r'^\s*LOGS_ID\s*=',
            "LOGS_VIDEO_ID": r'^\s*LOGS_VIDEO_ID\s*=',
            "LOGS_NSFW_ID": r'^\s*LOGS_NSFW_ID\s*=',
            "LOGS_IMG_ID": r'^\s*LOGS_IMG_ID\s*=',
            "LOGS_PAID_ID": r'^\s*LOGS_PAID_ID\s*=',
            "LOG_EXCEPTION": r'^\s*LOG_EXCEPTION\s*=',
            "SUBSCRIBE_CHANNEL": r'^\s*SUBSCRIBE_CHANNEL\s*=',
            "DASHBOARD_USERNAME": r'^\s*DASHBOARD_USERNAME\s*=',
            "DASHBOARD_PASSWORD": r'^\s*DASHBOARD_PASSWORD\s*=',
        }
        integer_keys = {
            "LOGS_ID",
            "LOGS_VIDEO_ID",
            "LOGS_NSFW_ID",
            "LOGS_IMG_ID",
            "LOGS_PAID_ID",
            "LOG_EXCEPTION",
            "SUBSCRIBE_CHANNEL",
            "PROXY_PORT",
            "PROXY_2_PORT",
        }
        
        updated = False
        for i, line in enumerate(lines):
            if key in patterns and re.match(patterns[key], line):
                if key in integer_keys:
                    try:
                        coerced = int(value)
                        lines[i] = f"    {key} = {coerced}\n"
                    except (ValueError, TypeError):
                        # Если не удалось преобразовать в int, сохраняем как строку
                        lines[i] = f"    {key} = \"{value}\"\n"
                elif isinstance(value, (int, float)) and key not in integer_keys:
                    lines[i] = f"    {key} = {value}\n"
                elif isinstance(value, bool):
                    lines[i] = f"    {key} = {str(value)}\n"
                else:
                    # Экранируем кавычки в строке
                    escaped_value = str(value).replace('"', '\\"')
                    lines[i] = f"    {key} = \"{escaped_value}\"\n"
                updated = True
                break
            elif key == "ADMIN" and re.match(r'^\s*ADMIN\s*=', line):
                if isinstance(value, list):
                    list_str = ", ".join(str(v) for v in value)
                    lines[i] = f"    ADMIN = [{list_str}]\n"
                    updated = True
                    break
            elif key == "ALLOWED_GROUP" and re.match(r'^\s*ALLOWED_GROUP\s*=', line):
                if isinstance(value, list):
                    list_str = ", ".join(str(v) for v in value)
                    lines[i] = f"    ALLOWED_GROUP = [{list_str}]\n"
                    updated = True
                    break
            elif key.startswith("YOUTUBE_COOKIE_URL"):
                # Проверяем активную строку (приоритет)
                active_match = re.match(rf'^\s*{re.escape(key)}\s*=', line)
                if active_match:
                    # Обрабатываем пустые значения корректно
                    escaped_value = str(value).replace('"', '\\"') if value else ""
                    lines[i] = f"    {key} = \"{escaped_value}\"\n"
                    updated = True
                    break
                # Проверяем закомментированную строку (если активной не нашли)
                commented_match = re.match(rf'^\s*#\s*{re.escape(key)}\s*=', line)
                if commented_match and not updated:
                    # Обрабатываем пустые значения корректно
                    escaped_value = str(value).replace('"', '\\"') if value else ""
                    # Раскомментируем строку и обновляем значение
                    lines[i] = f"    {key} = \"{escaped_value}\"\n"
                    updated = True
                    break
            elif key == "DASHBOARD_PASSWORD" and re.match(r'^\s*DASHBOARD_PASSWORD\s*=', line):
                # Для пароля обновляем только если передано непустое значение
                if value and str(value).strip():
                    escaped_value = str(value).replace('"', '\\"')
                    lines[i] = f"    DASHBOARD_PASSWORD = \"{escaped_value}\"\n"
                    updated = True
                break
        
        if not updated and key.startswith("YOUTUBE_COOKIE_URL"):
            # Ищем место после последнего YOUTUBE_COOKIE_URL (активного или закомментированного) или перед INSTAGRAM_COOKIE_URL
            insert_at = len(lines)
            # Сначала ищем последний YOUTUBE_COOKIE_URL (активный или закомментированный)
            for idx in range(len(lines) - 1, -1, -1):
                # Проверяем как активную, так и закомментированную строку
                if re.match(r'^\s*#?\s*YOUTUBE_COOKIE_URL', lines[idx]):
                    insert_at = idx + 1
                    break
            # Если не нашли, ищем перед INSTAGRAM_COOKIE_URL
            if insert_at == len(lines):
                insert_at = next(
                    (idx for idx, line in enumerate(lines) if "INSTAGRAM_COOKIE_URL" in line),
                    len(lines),
                )
            # Обрабатываем пустые значения корректно
            escaped_value = str(value).replace('"', '\\"') if value else ""
            lines.insert(insert_at, f"    {key} = \"{escaped_value}\"\n")
            updated = True
        elif not updated and key == "DASHBOARD_PASSWORD":
            # Ищем место после DASHBOARD_USERNAME
            insert_at = next(
                (idx for idx, line in enumerate(lines) if "DASHBOARD_USERNAME" in line),
                len(lines),
            )
            if insert_at < len(lines):
                lines.insert(insert_at + 1, f"    DASHBOARD_PASSWORD = \"{value}\"\n")
            else:
                lines.append(f"    DASHBOARD_PASSWORD = \"{value}\"\n")
            updated = True
        elif not updated and key in patterns:
            if key in integer_keys:
                try:
                    coerced = int(value)
                except Exception:
                    coerced = value
                lines.append(f"    {key} = {coerced}\n")
            else:
                lines.append(f"    {key} = \"{value}\"\n")
            updated = True
        
        if updated:
            with open(config_path, "w", encoding="utf-8") as f:
                f.writelines(lines)
            
            # Если обновили логин или пароль дашборда, перезагружаем конфиг в auth_service
            if key in ("DASHBOARD_USERNAME", "DASHBOARD_PASSWORD"):
                try:
                    from services.auth_service import get_auth_service
                    auth_service = get_auth_service()
                    auth_service.reload_config()
                except Exception as auth_error:
                    logger.warning(f"Failed to reload auth config: {auth_error}")
            
            return True
        return False
    except Exception as e:
        logger.error(f"Error updating config: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False

