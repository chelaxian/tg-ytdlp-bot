from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import enums

from HELPERS.app_instance import get_app
from HELPERS.safe_messeger import fake_message
from HELPERS.logger import logger
from CONFIG.messages import Messages, safe_get_messages

app = get_app()

# Mapping: callback_data -> (clean_command, message_attribute)
_CLEAN_OPTIONS = {
    "cookies": ("cookie", "CLEAN_COOKIES_CLEANED_MSG"),
    "logs": ("logs", "CLEAN_LOGS_CLEANED_MSG"),
    "tags": ("tags", "CLEAN_TAGS_CLEANED_MSG"),
    "format": ("format", "CLEAN_FORMAT_CLEANED_MSG"),
    "split": ("split", "CLEAN_SPLIT_CLEANED_MSG"),
    "mediainfo": ("mediainfo", "CLEAN_MEDIAINFO_CLEANED_MSG"),
    "subs": ("subs", "CLEAN_SUBS_CLEANED_MSG"),
    "keyboard": ("keyboard", "CLEAN_KEYBOARD_CLEANED_MSG"),
    "args": ("args", "CLEAN_ARGS_CLEANED_MSG"),
    "nsfw": ("nsfw", "CLEAN_NSFW_CLEANED_MSG"),
    "proxy": ("proxy", "CLEAN_PROXY_CLEANED_MSG"),
    "flood_wait": ("flood_wait", "CLEAN_FLOOD_WAIT_CLEANED_MSG"),
    "all": ("all", "CLEAN_ALL_CLEANED_MSG"),
}


@app.on_callback_query(filters.regex(r"^clean_option\|"))
def clean_option_callback(app, callback_query):
    user_id_obj = getattr(callback_query, 'from_user', None) or getattr(callback_query, 'user', None)
    if user_id_obj is None:
        return
    user_id = getattr(user_id_obj, 'id', None)
    if user_id is None:
        return

    messages = safe_get_messages(user_id)
    from URL_PARSERS.url_extractor import url_distractor
    data = callback_query.data.split("|")[1]

    if data in _CLEAN_OPTIONS:
        cmd_name, msg_attr = _CLEAN_OPTIONS[data]
        url_distractor(app, fake_message(f"/clean {cmd_name}", user_id))
        callback_query.answer(getattr(messages, msg_attr))
        return

    if data == "back":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(messages.CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG,
                                  callback_data="settings__cmd__download_cookie")],
            [InlineKeyboardButton(messages.CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG,
                                  callback_data="settings__cmd__cookies_from_browser")],
            [InlineKeyboardButton(messages.CLEAN_CHECK_COOKIE_BUTTON_MSG,
                                  callback_data="settings__cmd__check_cookie")],
            [InlineKeyboardButton(messages.CLEAN_SAVE_AS_COOKIE_BUTTON_MSG,
                                  callback_data="settings__cmd__save_as_cookie")],
            [InlineKeyboardButton("🔙Back", callback_data="settings__menu__back")]
        ])
        callback_query.edit_message_text(
            messages.CLEAN_COOKIES_MENU_TITLE_MSG,
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
