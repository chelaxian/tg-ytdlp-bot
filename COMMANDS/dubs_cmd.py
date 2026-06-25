# Dubs (audio tracks) command
import os
from pyrogram import filters, enums
from HELPERS.app_instance import get_app
from HELPERS.decorators import reply_with_keyboard, background_handler
from HELPERS.logger import logger, send_to_logger
from HELPERS.limitter import is_user_in_channel
from HELPERS.filesystem_hlp import create_directory
from CONFIG.config import Config
from CONFIG.messages import safe_get_messages
from COMMANDS.subtitles_cmd import LANGUAGES

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
    """
    try:
        dubs_lang = get_user_dubs_language(user_id)
        if not dubs_lang:
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


@app.on_message(filters.command("dubs") & filters.private)
@reply_with_keyboard
@background_handler(label="dubs_command")
def dubs_command(app, message):
    """Handle /dubs command - set default dub (audio track) language.

    Usage:
        /dubs            - show current status
        /dubs en         - set default dub language
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
            "• <code>/dubs en</code> - set default dub language\n"
            "• <code>/dubs off</code> - disable dubs\n"
            "• <code>/dubs</code> - show current status",
            parse_mode=enums.ParseMode.HTML,
            message=message,
        )
        return

    # No arguments - show status
    current_lang = get_user_dubs_language(user_id)
    if current_lang:
        lang_info = LANGUAGES.get(current_lang, {"name": current_lang, "flag": "🌐"})
        flag = lang_info['flag']
        name = lang_info['name']
        status_text = safe_get_messages(user_id).DUBS_CURRENT_MSG.format(flag=flag, name=name)
    else:
        status_text = safe_get_messages(user_id).DUBS_NONE_MSG

    safe_send_message(
        user_id,
        f"{status_text}\n\n"
        "<b>Quick commands:</b>\n"
        "• <code>/dubs en</code> - set default dub language\n"
        "• <code>/dubs off</code> - disable dubs\n\n"
        "Multiple audio tracks are embedded only in MKV format. "
        "For other formats, the selected dub language is used as the audio track.",
        parse_mode=enums.ParseMode.HTML,
        message=message,
    )
    send_to_logger(message, f"Dubs menu opened by user {user_id}")
