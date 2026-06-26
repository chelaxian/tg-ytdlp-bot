# Dubs (audio tracks) command
import os
import math
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from HELPERS.app_instance import get_app
from HELPERS.decorators import reply_with_keyboard, background_handler
from HELPERS.logger import logger, send_to_logger
from HELPERS.limitter import is_user_in_channel
from HELPERS.filesystem_hlp import create_directory
from CONFIG.config import Config
from CONFIG.messages import safe_get_messages
from COMMANDS.subtitles_cmd import LANGUAGES, get_flag

app = get_app()


def _dubs_file_path(user_id) -> str:
    return os.path.join("users", str(user_id), "dubs.txt")


def get_user_dubs_language(user_id):
    """Get user's preferred dub (audio track) language."""
    try:
        path = _dubs_file_path(user_id)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                lang = f.read().strip()
                return lang if lang and lang != "OFF" else None
    except Exception as e:
        logger.debug(f"get_user_dubs_language error: {e}")
    return None


def save_user_dubs_language(user_id, lang_code):
    """Save (or clear) user's preferred dub language."""
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    path = _dubs_file_path(user_id)
    if lang_code in ("OFF", None, ""):
        if os.path.exists(path):
            os.remove(path)
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(lang_code)
    logger.info(f"Saved dubs preference for user {user_id}: {lang_code}")


def is_dubs_enabled(user_id) -> bool:
    """Whether the user has a persistent default dub language set."""
    return get_user_dubs_language(user_id) is not None


def apply_dubs_preference(user_id, filters_state: dict) -> dict:
    """Inject the persistent /dubs preference into the Always Ask filters state.

    Called before format-string construction and the MKV audio-embedding block.
    Manual selections made in the Always Ask menu take precedence over the
    /dubs default. Returns the (possibly modified) filters_state dict.

    If the current video does not support dubs (has_dubs=False in state),
    the persistent preference is NOT applied.
    """
    try:
        dubs_lang = get_user_dubs_language(user_id)
        if not dubs_lang:
            return filters_state

        # Do not apply dubs preference for videos that don't support dubs
        if filters_state.get("has_dubs") is False:
            logger.debug(f"[DUBS] Skipping /dubs preference: video has no dubs for user {user_id}")
            return filters_state

        audio_all_dubs = filters_state.get("audio_all_dubs", False)
        selected_audio_langs = filters_state.get("selected_audio_langs", []) or []
        sel_audio_lang = filters_state.get("audio_lang")

        # Only inject the default when nothing was manually picked in the menu
        if not audio_all_dubs and not selected_audio_langs:
            filters_state["selected_audio_langs"] = [dubs_lang]
            logger.info(f"[DUBS] Applied /dubs default '{dubs_lang}' to selected_audio_langs for user {user_id}")

        if not sel_audio_lang or sel_audio_lang == "ALL":
            filters_state["audio_lang"] = dubs_lang
            logger.info(f"[DUBS] Applied /dubs default '{dubs_lang}' to audio_lang for user {user_id}")

        return filters_state
    except Exception as e:
        logger.warning(f"apply_dubs_preference error: {e}")
        return filters_state


# ===================== Interactive paginated menu =====================

def _dubs_status_text(user_id) -> str:
    """Build the status line for the dubs menu."""
    current_lang = get_user_dubs_language(user_id)
    if current_lang:
        lang_info = LANGUAGES.get(current_lang, {"name": current_lang, "flag": get_flag(current_lang)})
        return safe_get_messages(user_id).DUBS_CURRENT_MSG.format(
            flag=lang_info['flag'], name=lang_info['name']
        )
    return safe_get_messages(user_id).DUBS_NONE_MSG


def get_dubs_keyboard(page=0, user_id=None, per_page_rows=8):
    """Generate paginated keyboard with dub language buttons (3 per row)."""
    keyboard = []
    LANGS_PER_ROW = 3
    ROWS_PER_PAGE = per_page_rows  # 8 rows -> 24 langs per page

    all_langs = list(LANGUAGES.items())
    total_languages = len(all_langs)
    total_pages = max(1, math.ceil(total_languages / (LANGS_PER_ROW * ROWS_PER_PAGE)))

    # Clamp page
    if page < 0:
        page = 0
    if page > total_pages - 1:
        page = total_pages - 1

    start_idx = page * LANGS_PER_ROW * ROWS_PER_PAGE
    end_idx = start_idx + LANGS_PER_ROW * ROWS_PER_PAGE
    current_page_langs = all_langs[start_idx:end_idx]

    current_lang = get_user_dubs_language(user_id) if user_id else None

    # Language buttons: 3 per row
    for i in range(0, len(current_page_langs), LANGS_PER_ROW):
        row = []
        for j in range(LANGS_PER_ROW):
            if i + j < len(current_page_langs):
                lang_code, lang_info = current_page_langs[i + j]
                checkmark = "✅ " if lang_code == current_lang else ""
                flag = lang_info.get('flag', get_flag(lang_code))
                name = lang_info.get('name', lang_code)
                row.append(InlineKeyboardButton(
                    f"{checkmark}{flag} {name}",
                    callback_data=f"dubs_lang|{lang_code}"
                ))
        keyboard.append(row)

    # Navigation row
    nav_row = []
    if page > 0:
        nav_row.append(InlineKeyboardButton(
            safe_get_messages(user_id).SUBS_PREV_BUTTON_MSG,
            callback_data=f"dubs_page|{page - 1}"
        ))
    if page < total_pages - 1:
        nav_row.append(InlineKeyboardButton(
            safe_get_messages(user_id).SUBTITLES_NEXT_BUTTON_MSG,
            callback_data=f"dubs_page|{page + 1}"
        ))
    if nav_row:
        keyboard.append(nav_row)

    # OFF + Close row
    keyboard.append([
        InlineKeyboardButton(
            safe_get_messages(user_id).SUBS_OFF_BUTTON_MSG,
            callback_data="dubs_lang|OFF"
        ),
        InlineKeyboardButton(
            safe_get_messages(user_id).URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG,
            callback_data="dubs_lang_close|close"
        ),
    ])

    return InlineKeyboardMarkup(keyboard)


@app.on_callback_query(filters.regex(r"^dubs_page\|"))
def dubs_page_callback(app, callback_query):
    """Handle page navigation in dubs language selection menu."""
    user_id = callback_query.from_user.id
    page = int(callback_query.data.split("|")[1])

    status_text = _dubs_status_text(user_id)
    try:
        menu_text = safe_get_messages(user_id).DUBS_SETTINGS_MENU_MSG.format(status_text=status_text)
    except Exception:
        menu_text = f"{status_text}\n\nSelect dub language:"

    try:
        callback_query.edit_message_text(
            menu_text,
            reply_markup=get_dubs_keyboard(page, user_id=user_id),
            parse_mode=enums.ParseMode.HTML,
        )
    except Exception:
        pass
    callback_query.answer()


@app.on_callback_query(filters.regex(r"^dubs_lang\|"))
def dubs_lang_callback(app, callback_query):
    """Handle language selection in dubs language menu."""
    user_id = callback_query.from_user.id
    lang_code = callback_query.data.split("|")[1]
    page = 0

    save_user_dubs_language(user_id, lang_code)

    if lang_code == "OFF":
        status = safe_get_messages(user_id).DUBS_DISABLED_MSG
        notification = safe_get_messages(user_id).DUBS_DISABLED_MSG
    else:
        lang_info = LANGUAGES.get(lang_code, {"flag": get_flag(lang_code), "name": lang_code})
        status = safe_get_messages(user_id).DUBS_LANGUAGE_SET_MSG.format(
            flag=lang_info['flag'], name=lang_info['name']
        )
        notification = safe_get_messages(user_id).DUBS_LANGUAGE_SET_MSG.format(
            flag=lang_info['flag'], name=lang_info['name']
        )

    status_text = _dubs_status_text(user_id)
    try:
        menu_text = safe_get_messages(user_id).DUBS_SETTINGS_MENU_MSG.format(status_text=status_text)
    except Exception:
        menu_text = f"{status_text}\n\nSelect dub language:"

    try:
        callback_query.edit_message_text(
            menu_text,
            reply_markup=get_dubs_keyboard(page, user_id=user_id),
            parse_mode=enums.ParseMode.HTML,
        )
    except Exception:
        pass
    callback_query.answer(notification, show_alert=False)
    send_to_logger(callback_query.message, f"Dubs language set to '{lang_code}' by user {user_id}")


@app.on_callback_query(filters.regex(r"^dubs_lang_close\|"))
def dubs_lang_close_callback(app, callback_query):
    """Close the dubs language menu."""
    try:
        callback_query.message.delete()
    except Exception:
        callback_query.edit_message_reply_markup(reply_markup=None)
    callback_query.answer()
    return


# ===================== Command handler =====================

@app.on_message(filters.command("dubs") & filters.private)
@reply_with_keyboard
@background_handler(label="dubs_command")
def dubs_command(app, message):
    """Handle /dubs command - set default dub (audio track) language.

    Usage:
        /dubs            - show interactive language menu
        /dubs en         - set default dub language (quick)
        /dubs off        - disable dubs
    """
    user_id = message.from_user.id
    is_admin = int(user_id) in Config.ADMIN

    # Permission checks (mirror /subs)
    text = getattr(message, 'text', '').strip() if hasattr(message, 'text') else ''
    is_ignore_command = text.startswith(Config.IGNORE_USER_COMMAND) or text.startswith(Config.UNIGNORE_USER_COMMAND)

    if not is_ignore_command:
        from DATABASE.firebase_init import is_user_ignored
        if is_user_ignored(message):
            return

    if not is_admin:
        from DATABASE.firebase_init import is_user_blocked
        if is_user_blocked(message):
            return

    if not is_admin and not is_user_in_channel(app, message):
        return

    from HELPERS.safe_messeger import safe_send_message

    parts = (message.text or "").split()

    if len(parts) >= 2:
        arg = parts[1].lower()

        if arg == "off":
            save_user_dubs_language(user_id, "OFF")
            safe_send_message(user_id, safe_get_messages(user_id).DUBS_DISABLED_MSG, message=message)
            send_to_logger(message, f"Dubs disabled by user {user_id}")
            return

        if arg in LANGUAGES:
            save_user_dubs_language(user_id, arg)
            lang_info = LANGUAGES[arg]
            flag = lang_info['flag']
            name = lang_info['name']
            safe_send_message(
                user_id,
                safe_get_messages(user_id).DUBS_LANGUAGE_SET_MSG.format(flag=flag, name=name),
                message=message,
            )
            send_to_logger(message, f"Dubs language set to '{arg}' by user {user_id}")
            return

        # Invalid argument
        safe_send_message(
            user_id,
            "⚠️ Invalid argument.\n\n"
            "<b>Usage:</b>\n"
            "• <code>/dubs</code> - open language menu\n"
            "• <code>/dubs en</code> - set default dub language\n"
            "• <code>/dubs off</code> - disable dubs",
            parse_mode=enums.ParseMode.HTML,
            message=message,
        )
        return

    # No arguments - show interactive paginated menu
    status_text = _dubs_status_text(user_id)
    try:
        menu_text = safe_get_messages(user_id).DUBS_SETTINGS_MENU_MSG.format(status_text=status_text)
    except Exception:
        menu_text = (
            f"{status_text}\n\n"
            "Select dub language:\n\n"
            "Multiple audio tracks are embedded only in MKV format."
        )

    safe_send_message(
        user_id,
        menu_text,
        reply_markup=get_dubs_keyboard(page=0, user_id=user_id),
        parse_mode=enums.ParseMode.HTML,
        message=message,
    )
    send_to_logger(message, f"Dubs menu opened by user {user_id}")
