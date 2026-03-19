from __future__ import annotations

import json
import os
from typing import Any, Dict, Optional


def _bot_api_url() -> str:
    # Late import to avoid import cycles at module import time.
    from CONFIG.config import Config

    return f"https://api.telegram.org/bot{Config.BOT_TOKEN}"


def bot_api_call(method: str, payload: Dict[str, Any], *, timeout: float = 30.0) -> Optional[Dict[str, Any]]:
    """
    Minimal Telegram HTTP Bot API caller.
    Returns parsed JSON on success, None on failure.
    """
    try:
        import requests

        url = f"{_bot_api_url()}/{method}"
        # Bot API supports multipart for local files. If we detect a local file path in common media fields,
        # send as multipart/form-data.
        file_field = None
        file_path = None
        for k in ("photo", "document", "video", "animation", "audio", "voice"):
            v = payload.get(k)
            if isinstance(v, str) and os.path.exists(v) and os.path.isfile(v):
                file_field = k
                file_path = v
                break

        if file_field and file_path:
            data = {}
            files = {}
            try:
                for key, val in payload.items():
                    if key == file_field:
                        continue
                    if key == "reply_markup" and isinstance(val, (dict, list)):
                        data[key] = json.dumps(val, ensure_ascii=False)
                    else:
                        data[key] = val
                with open(file_path, "rb") as f:
                    files[file_field] = f
                    resp = requests.post(url, data=data, files=files, timeout=timeout)
            except Exception:
                # fall back to json
                resp = requests.post(url, json=payload, timeout=timeout)
        else:
            resp = requests.post(url, json=payload, timeout=timeout)
        data = resp.json()
        if isinstance(data, dict) and data.get("ok"):
            return data
        return data if isinstance(data, dict) else None
    except Exception:
        return None

