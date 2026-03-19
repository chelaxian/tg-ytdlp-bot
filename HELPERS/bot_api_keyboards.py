from __future__ import annotations

from typing import Any, Dict, List, Optional

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def _btn_to_bot_api_dict(btn: InlineKeyboardButton) -> Dict[str, Any]:
    d: Dict[str, Any] = {"text": btn.text}
    # Keep common Bot API fields
    for field in (
        "url",
        "callback_data",
        "web_app",
        "login_url",
        "switch_inline_query",
        "switch_inline_query_current_chat",
        "callback_game",
        "pay",
        "copy_text",
    ):
        val = getattr(btn, field, None)
        if val is None:
            continue
        # pyrogram objects may need dict conversion
        try:
            if hasattr(val, "to_dict"):
                d[field] = val.to_dict()
            else:
                d[field] = val
        except Exception:
            d[field] = val
    return d


def _is_close_or_back(btn_dict: Dict[str, Any]) -> bool:
    t = str(btn_dict.get("text", "")).strip().lower()
    cd = str(btn_dict.get("callback_data", "")).strip().lower()
    if t.endswith("close") or t.endswith("back"):
        return True
    if cd.endswith("close") or cd.endswith("|close") or cd.endswith("__close"):
        return True
    if cd.endswith("back") or cd.endswith("|back") or cd.endswith("__back"):
        return True
    return False


def inline_keyboard_with_styles(
    reply_markup: InlineKeyboardMarkup,
    *,
    pressed_callback_data: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Builds Bot API reply_markup dict with:
    - Close/Back => style='danger'
    - Pressed button => style='success'
    """
    rows: List[List[Dict[str, Any]]] = []
    for row in reply_markup.inline_keyboard:
        out_row: List[Dict[str, Any]] = []
        for btn in row:
            b = _btn_to_bot_api_dict(btn)
            cd = b.get("callback_data")
            if pressed_callback_data and cd == pressed_callback_data:
                b["style"] = "success"
            elif _is_close_or_back(b):
                b["style"] = "danger"
            out_row.append(b)
        rows.append(out_row)
    return {"inline_keyboard": rows}

