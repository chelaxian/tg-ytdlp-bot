from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path
from typing import Dict, Any, List
import shutil

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
        for i, line in enumerate(lines):
            if re.match(rf'^\s*{list_name}\s*=\s*\[', line):
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
            return bool(shutil.which("docker")) and Path("/var/run/docker.sock").exists()

        def _container_exists(name: str) -> bool:
            if not _has_docker():
                return False
            result = subprocess.run(
                ["docker", "ps", "-a", "--filter", f"name={name}", "--format", "{{.Names}}"],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
            if result.returncode != 0:
                return False
            names = [n.strip() for n in result.stdout.splitlines() if n.strip()]
            return any(n == name for n in names)

        # Docker режим: возвращаем специальный статус для запроса URL
        if _has_docker() and _container_exists("tg-ytdlp-bot"):
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


def update_lists_from_urls(porn_domains_url: str, porn_keywords_url: str) -> Dict[str, Any]:
    """
    Обновляет списки из URL (для Docker режима).
    Скачивает файлы по URL и сохраняет их в соответствующие файлы.
    """
    import requests
    base_dir = Path(__file__).resolve().parent.parent
    
    try:
        # Скачиваем porn_domains.txt
        if porn_domains_url:
            try:
                response = requests.get(porn_domains_url, timeout=30)
                response.raise_for_status()
                domains_file = base_dir / Config.PORN_DOMAINS_FILE
                domains_file.parent.mkdir(parents=True, exist_ok=True)
                with open(domains_file, "w", encoding="utf-8") as f:
                    f.write(response.text)
            except Exception as e:
                return {"status": "error", "message": f"Failed to download porn_domains: {str(e)}"}
        
        # Скачиваем porn_keywords.txt
        if porn_keywords_url:
            try:
                response = requests.get(porn_keywords_url, timeout=30)
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

