from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path
from typing import Dict, Any, List
import shutil
from urllib.parse import urlparse
import ipaddress

from CONFIG.domains import DomainsConfig
from CONFIG.config import Config


def get_file_line_count(file_path: str) -> int:
    """Подсчитывает количество строк в файле."""
    try:
        if not os.path.exists(file_path):
            return 0
        with open(file_path, "r", encoding="utf-8") as f:
            return sum(1 for _ in f if _.strip())
    except Exception:
        return 0


def get_lists_stats() -> Dict[str, Any]:
    """Возвращает статистику по файлам списков."""
    base_dir = Path(__file__).parent.parent
    return {
        "porn_domains": get_file_line_count(base_dir / Config.PORN_DOMAINS_FILE),
        "porn_keywords": get_file_line_count(base_dir / Config.PORN_KEYWORDS_FILE),
        "supported_sites": get_file_line_count(base_dir / Config.SUPPORTED_SITES_FILE),
    }


def get_domain_lists() -> Dict[str, List[str]]:
    """Возвращает все списки доменов из CONFIG/domains.py."""
    return {
        "WHITE_KEYWORDS": list(getattr(DomainsConfig, "WHITE_KEYWORDS", [])),
        "GALLERYDL_ONLY_DOMAINS": list(getattr(DomainsConfig, "GALLERYDL_ONLY_DOMAINS", [])),
        "GALLERYDL_ONLY_PATH": list(getattr(DomainsConfig, "GALLERYDL_ONLY_PATH", [])),
        "GALLERYDL_FALLBACK_DOMAINS": list(getattr(DomainsConfig, "GALLERYDL_FALLBACK_DOMAINS", [])),
        "YTDLP_ONLY_DOMAINS": list(getattr(DomainsConfig, "YTDLP_ONLY_DOMAINS", [])),
        "WHITELIST": list(getattr(DomainsConfig, "WHITELIST", [])),
        "GREYLIST": list(getattr(DomainsConfig, "GREYLIST", [])),
        "NO_COOKIE_DOMAINS": list(getattr(DomainsConfig, "NO_COOKIE_DOMAINS", [])),
        "PROXY_DOMAINS": list(getattr(DomainsConfig, "PROXY_DOMAINS", [])),
        "PROXY_2_DOMAINS": list(getattr(DomainsConfig, "PROXY_2_DOMAINS", [])),
        "NO_FILTER_DOMAINS": list(getattr(DomainsConfig, "NO_FILTER_DOMAINS", [])),
        "TIKTOK_DOMAINS": list(getattr(DomainsConfig, "TIKTOK_DOMAINS", [])),
        "CLEAN_QUERY": list(getattr(DomainsConfig, "CLEAN_QUERY", [])),
        "BLACK_LIST": list(getattr(DomainsConfig, "BLACK_LIST", [])),
    }


def update_domain_list(list_name: str, items: List[str]) -> bool:
    """Обновляет список доменов в CONFIG/domains.py."""
    domains_path = Path(__file__).parent.parent / "CONFIG" / "domains.py"
    try:
        with open(domains_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        # Ищем начало списка
        start_idx = None
        end_idx = None
        indent = "    "
        # Экранируем специальные символы regex для безопасности
        escaped_list_name = re.escape(list_name)
        for i, line in enumerate(lines):
            if re.match(rf'^\s*{escaped_list_name}\s*=\s*\[', line):
                start_idx = i
                # Определяем отступ
                indent_match = re.match(r'^(\s*)', line)
                if indent_match:
                    indent = indent_match.group(1)
                break
        
        if start_idx is None:
            return False
        
        # Ищем конец списка
        bracket_count = 0
        found_open = False
        for i in range(start_idx, len(lines)):
            line = lines[i]
            for char in line:
                if char == '[':
                    bracket_count += 1
                    found_open = True
                elif char == ']':
                    bracket_count -= 1
                    if found_open and bracket_count == 0:
                        end_idx = i
                        break
            if end_idx is not None:
                break
        
        if end_idx is None:
            return False
        
        # Формируем новый список
        new_lines = [f"{indent}{list_name} = [\n"]
        for item in items:
            new_lines.append(f'{indent}    "{item}",\n')
        new_lines.append(f"{indent}]\n")
        
        # Заменяем старый список новым
        lines[start_idx:end_idx + 1] = new_lines
        
        with open(domains_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        return True
    except Exception as e:
        print(f"Error updating domain list {list_name}: {e}")
        return False


def update_lists() -> Dict[str, Any]:
    """
    Обновляет списки.
    - Если есть docker и контейнер бота: возвращает специальный статус для запроса URL.
    - Иначе: запускаем локальный script.sh (старое поведение).
    """
    try:
        def _has_docker() -> bool:
            """Проверяет наличие docker CLI и сокета."""
            docker_path = shutil.which("docker")
            docker_sock = Path("/var/run/docker.sock")
            return bool(docker_path) and docker_sock.exists()

        def _container_is_running(name: str) -> bool:
            """Проверяет, что контейнер с именем name запущен (docker ps)."""
            if not _has_docker():
                return False
            try:
                result = subprocess.run(
                    ["docker", "ps", "--filter", f"name={name}", "--format", "{{.Names}}"],
                    capture_output=True,
                    text=True,
                    timeout=5,
                    check=False,
                )
                if result.returncode != 0:
                    return False
                names = [n.strip() for n in result.stdout.splitlines() if n.strip()]
                return any(n == name for n in names)
            except Exception:
                return False

        # Docker режим: возвращаем специальный статус для запроса URL (только если контейнер запущен)
        if _has_docker() and _container_is_running("tg-ytdlp-bot"):
            return {
                "status": "need_urls",
                "message": "Please provide .txt URLs for porn_domains and porn_keywords",
            }

        # Локальный режим — старое поведение
        script_path = Path(__file__).resolve().parent.parent / "script.sh"
        if not script_path.exists():
            return {"status": "error", "message": f"{script_path} not found"}
        result = subprocess.run(
            ["bash", str(script_path)],
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


def _validate_url_for_ssrf(url: str) -> tuple[bool, str]:
    """
    Валидирует URL для предотвращения SSRF атак.
    Возвращает (is_valid, error_message).
    """
    if not url:
        return False, "URL is empty"
    
    try:
        parsed = urlparse(url)
        
        # Разрешаем только HTTP и HTTPS
        if parsed.scheme not in ('http', 'https'):
            return False, f"Invalid scheme: {parsed.scheme}. Only http and https are allowed"
        
        # Проверяем хост
        host = parsed.hostname
        if not host:
            return False, "URL must have a hostname"
        
        host_lower = host.lower()
        
        # Блокируем localhost и его варианты
        blocked_hosts = {
            'localhost',
            '127.0.0.1',
            '0.0.0.0',
            '::1',
            '[::1]',
        }
        if host_lower in blocked_hosts:
            return False, f"Blocked hostname: {host}"
        
        # Блокируем внутренние IP адреса
        try:
            ip = ipaddress.ip_address(host)
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
                return False, f"Blocked private/reserved IP: {host}"
            # Блокируем метаданные облачных сервисов (169.254.169.254)
            if str(ip) == '169.254.169.254':
                return False, f"Blocked metadata service IP: {host}"
        except ValueError:
            # Не IP адрес, проверяем домен
            # Блокируем домены, которые могут указывать на внутренние ресурсы
            if host_lower.endswith('.local') or host_lower.endswith('.internal'):
                return False, f"Blocked internal domain: {host}"
            # Блокируем домены, содержащие localhost
            if 'localhost' in host_lower:
                return False, f"Blocked hostname containing localhost: {host}"
        
        return True, ""
    except Exception as e:
        return False, f"URL validation error: {str(e)}"


def _safe_get_with_redirect_validation(url: str, timeout: int = 30) -> requests.Response:
    """
    Безопасный GET запрос с валидацией редиректов для предотвращения SSRF.
    """
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    from urllib.parse import urljoin
    
    # Валидация входного URL для предотвращения SSRF
    is_valid, error_msg = _validate_url_for_ssrf(url)
    if not is_valid:
        raise ValueError(f"Invalid URL: {error_msg}")
    
    session = requests.Session()
    
    # Настраиваем retry стратегию
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    # Отключаем автоматические редиректы и обрабатываем их вручную с валидацией
    current_url = url
    response = session.get(current_url, timeout=timeout, allow_redirects=False)
    
    # Обрабатываем редиректы вручную с валидацией
    max_redirects = 10
    redirect_count = 0
    while response.status_code in (301, 302, 303, 307, 308) and redirect_count < max_redirects:
        redirect_location = response.headers.get('Location')
        if not redirect_location:
            break
        
        # Обрабатываем относительные редиректы
        if redirect_location.startswith('/'):
            redirect_url = urljoin(current_url, redirect_location)
        elif not redirect_location.startswith(('http://', 'https://')):
            redirect_url = urljoin(current_url, redirect_location)
        else:
            redirect_url = redirect_location
        
        # Валидируем URL редиректа
        is_valid, error_msg = _validate_url_for_ssrf(redirect_url)
        if not is_valid:
            raise ValueError(f"Invalid redirect URL: {error_msg}")
        
        redirect_count += 1
        current_url = redirect_url
        response = session.get(current_url, timeout=timeout, allow_redirects=False)
    
    if redirect_count >= max_redirects:
        raise ValueError("Too many redirects")
    
    return response


def update_lists_from_urls(porn_domains_url: str, porn_keywords_url: str) -> Dict[str, Any]:
    """
    Обновляет списки из URL (для Docker режима).
    Скачивает файлы по URL и сохраняет их в соответствующие файлы.
    """
    base_dir = Path(__file__).resolve().parent.parent
    
    try:
        # Скачиваем porn_domains.txt
        if porn_domains_url:
            # Валидация URL для предотвращения SSRF
            is_valid, error_msg = _validate_url_for_ssrf(porn_domains_url)
            if not is_valid:
                return {"status": "error", "message": f"Invalid porn_domains URL: {error_msg}"}
            
            try:
                response = _safe_get_with_redirect_validation(porn_domains_url, timeout=30)
                response.raise_for_status()
                domains_file = base_dir / Config.PORN_DOMAINS_FILE
                domains_file.parent.mkdir(parents=True, exist_ok=True)
                with open(domains_file, "w", encoding="utf-8") as f:
                    f.write(response.text)
            except Exception as e:
                return {"status": "error", "message": f"Failed to download porn_domains: {str(e)}"}
        
        # Скачиваем porn_keywords.txt
        if porn_keywords_url:
            # Валидация URL для предотвращения SSRF
            is_valid, error_msg = _validate_url_for_ssrf(porn_keywords_url)
            if not is_valid:
                return {"status": "error", "message": f"Invalid porn_keywords URL: {error_msg}"}
            
            try:
                response = _safe_get_with_redirect_validation(porn_keywords_url, timeout=30)
                response.raise_for_status()
                keywords_file = base_dir / Config.PORN_KEYWORDS_FILE
                keywords_file.parent.mkdir(parents=True, exist_ok=True)
                with open(keywords_file, "w", encoding="utf-8") as f:
                    f.write(response.text)
            except Exception as e:
                return {"status": "error", "message": f"Failed to download porn_keywords: {str(e)}"}
        
        return {"status": "ok", "message": "Lists updated successfully from URLs"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

