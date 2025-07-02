"""Settings handlers"""
import logging

logger = logging.getLogger(__name__)

# ===================== /settings =====================
@app.on_message(filters.command("settings") & filters.private)
@reply_with_keyboard
def settings_command(app, message):
    user_id = message.chat.id
    # Main settings menu
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🧹 CLEAN", callback_data="settings__menu__clean")],
        [InlineKeyboardButton("🍪 COOKIES", callback_data="settings__menu__cookies")],
        [InlineKeyboardButton("🎞 MEDIA", callback_data="settings__menu__media")],
        [InlineKeyboardButton("📖 INFO", callback_data="settings__menu__logs")],
        [InlineKeyboardButton("🔙 Close", callback_data="settings__menu__close")]
    ])
    app.send_message(
        user_id,
        "<b>Bot Settings</b>\n\nChoose a category:",
        reply_markup=keyboard,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=message.id
    )
    send_to_logger(message, "Opened /settings menu")

@app.on_callback_query(filters.regex(r"^settings__menu__"))
@reply_with_keyboard
def settings_menu_callback(app, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data.split("__")[-1]
    if data == "close":
        callback_query.message.delete()
        callback_query.answer("Menu closed.")
        return
    if data == "clean":
        # Show the cleaning menu
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🍪 Cookies", callback_data="clean_option|cookies")],
            [InlineKeyboardButton("📃 Logs ", callback_data="clean_option|logs")],
            [InlineKeyboardButton("#️⃣ Tags", callback_data="clean_option|tags")],
            [InlineKeyboardButton("📼 Format", callback_data="clean_option|format")],
            [InlineKeyboardButton("✂️ Split", callback_data="clean_option|split")],
            [InlineKeyboardButton("📊 Mediainfo", callback_data="clean_option|mediainfo")],
            [InlineKeyboardButton("🗑  All files", callback_data="clean_option|all")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__back")]
        ])
        callback_query.edit_message_text(
            "<b>🧹 Clean Options</b>\n\nChoose what to clean:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return
    if data == "cookies":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📥 /download_cookie - Download my YouTube cookie",
                                  callback_data="settings__cmd__download_cookie")],
            [InlineKeyboardButton("🌐 /cookies_from_browser - Get cookies from browser",
                                  callback_data="settings__cmd__cookies_from_browser")],
            [InlineKeyboardButton("🔎 /check_cookie - Check cookie file in your folder",
                                  callback_data="settings__cmd__check_cookie")],
            [InlineKeyboardButton("🔖 /save_as_cookie - Send text to save as cookie",
                                  callback_data="settings__cmd__save_as_cookie")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__back")]
        ])
        callback_query.edit_message_text(
            "<b>🍪 COOKIES</b>\n\nChoose an action:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return
    if data == "media":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📼 /format - Change quality & format", callback_data="settings__cmd__format")],
            [InlineKeyboardButton("📊 /mediainfo - Turn ON / OFF MediaInfo", callback_data="settings__cmd__mediainfo")],
            [InlineKeyboardButton("✂️ /split - Change split video part size", callback_data="settings__cmd__split")],
            [InlineKeyboardButton("🎧 /audio - Download video as audio", callback_data="settings__cmd__audio")],
            [InlineKeyboardButton("📋 /playlist - How to download playlists", callback_data="settings__cmd__playlist")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__back")]
        ])
        callback_query.edit_message_text(
            "<b>🎞 MEDIA</b>\n\nChoose an action:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return
    if data == "logs":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("#️⃣ /tags - Send your #tags", callback_data="settings__cmd__tags")],
            [InlineKeyboardButton("🆘 /help - Get instructions", callback_data="settings__cmd__help")],
            [InlineKeyboardButton("📃 /usage -Send your logs", callback_data="settings__cmd__usage")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__back")]
        ])
        callback_query.edit_message_text(
            "<b>📖 INFO</b>\n\nChoose an action:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return
    if data == "back":
        # Return to main menu
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🧹 CLEAN", callback_data="settings__menu__clean")],
            [InlineKeyboardButton("🍪 COOKIES", callback_data="settings__menu__cookies")],
            [InlineKeyboardButton("🎞 MEDIA", callback_data="settings__menu__media")],
            [InlineKeyboardButton("📖 INFO", callback_data="settings__menu__logs")],
            [InlineKeyboardButton("🔙 Close", callback_data="settings__menu__close")]
        ])
        callback_query.edit_message_text(
            "<b>Bot Settings</b>\n\nChoose a category:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return

@app.on_callback_query(filters.regex(r"^settings__cmd__"))
@reply_with_keyboard
def settings_cmd_callback(app, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data.split("__")[2]

    # For commands that are processed only via url_distractor, create a temporary Message
    if data == "clean":
        # Show the cleaning menu instead of direct execution
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🍪 Cookies only", callback_data="clean_option|cookies")],
            [InlineKeyboardButton("📃 Logs ", callback_data="clean_option|logs")],
            [InlineKeyboardButton("#️⃣ Tags", callback_data="clean_option|tags")],
            [InlineKeyboardButton("📼 Format", callback_data="clean_option|format")],
            [InlineKeyboardButton("✂️ Split", callback_data="clean_option|split")],
            [InlineKeyboardButton("📊 Mediainfo", callback_data="clean_option|mediainfo")],
            [InlineKeyboardButton("🗑  All files", callback_data="clean_option|all")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__cookies")]
        ])
        callback_query.edit_message_text(
            "<b>🧹 Clean Options</b>\n\nChoose what to clean:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return
    if data == "download_cookie":
        url_distractor(app, fake_message("/download_cookie", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "cookies_from_browser":
        cookies_from_browser(app, fake_message("/cookies_from_browser", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "check_cookie":
        url_distractor(app, fake_message("/check_cookie", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "save_as_cookie":
        app.send_message(user_id, Config.SAVE_AS_COOKIE_HINT, reply_to_message_id=callback_query.message.id,
                         parse_mode=enums.ParseMode.HTML)
        callback_query.answer("Hint sent.")
        return
    if data == "format":
        # Add the command attribute for set_format to work correctly
        set_format(app, fake_message("/format", user_id, command=["format"]))
        callback_query.answer("Command executed.")
        return
    if data == "mediainfo":
        mediainfo_command(app, fake_message("/mediainfo", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "split":
        split_command(app, fake_message("/split", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "audio":
        # We just send a hint on how to use it
        app.send_message(user_id,
                         "Download only audio from video source.\nUsage: /audio + URL (ex. /audio https://youtu.be/abc123)",
                         reply_to_message_id=callback_query.message.id)
        callback_query.answer("Hint sent.")
        return
    if data == "tags":
        tags_command(app, fake_message("/tags", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "help":
        command2(app, fake_message("/help", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "usage":
        url_distractor(app, fake_message("/usage", user_id))
        callback_query.answer("Command executed.")
        return
    if data == "playlist":
        playlist_command(app, fake_message("/playlist", user_id))
        callback_query.answer("Command executed.")
        return
    callback_query.answer("Unknown command.", show_alert=True)

@app.on_callback_query(filters.regex(r"^clean_option\|"))
@reply_with_keyboard
def clean_option_callback(app, callback_query):
    user_id = callback_query.from_user.id
    data = callback_query.data.split("|")[1]

    if data == "cookies":
        url_distractor(app, fake_message("/clean cookie", user_id))
        callback_query.answer("Cookies cleaned.")
        return
    elif data == "logs":
        url_distractor(app, fake_message("/clean logs", user_id))
        callback_query.answer("logs cleaned.")
        return
    elif data == "tags":
        url_distractor(app, fake_message("/clean tags", user_id))
        callback_query.answer("tags cleaned.")
        return
    elif data == "format":
        url_distractor(app, fake_message("/clean format", user_id))
        callback_query.answer("format cleaned.")
        return
    elif data == "split":
        url_distractor(app, fake_message("/clean split", user_id))
        callback_query.answer("split cleaned.")
        return
    elif data == "mediainfo":
        url_distractor(app, fake_message("/clean mediainfo", user_id))
        callback_query.answer("mediainfo cleaned.")
        return
    elif data == "all":
        url_distractor(app, fake_message("/clean all", user_id))
        callback_query.answer("All files cleaned.")
        return
    elif data == "back":
        # Back to the cookies menu
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📥 /download_cookie - Download my YouTube cookie",
                                  callback_data="settings__cmd__download_cookie")],
            [InlineKeyboardButton("🌐 /cookies_from_browser - Get cookies from browser",
                                  callback_data="settings__cmd__cookies_from_browser")],
            [InlineKeyboardButton("🔎 /check_cookie - Check cookie file in your folder",
                                  callback_data="settings__cmd__check_cookie")],
            [InlineKeyboardButton("🔖 /save_as_cookie - Send text to save as cookie",
                                  callback_data="settings__cmd__save_as_cookie")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings__menu__back")]
        ])
        callback_query.edit_message_text(
            "<b>🍪 COOKIES</b>\n\nChoose an action:",
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.HTML
        )
        callback_query.answer()
        return

# /Mediainfo Command
@app.on_message(filters.command("mediainfo") & filters.private)
@reply_with_keyboard
def mediainfo_command(app, message):
    user_id = message.chat.id
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    buttons = [
        [InlineKeyboardButton("✅ ON", callback_data="mediainfo_option|on")],
        [InlineKeyboardButton("❌ OFF", callback_data="mediainfo_option|off")],
        [InlineKeyboardButton("🔙 Cancel", callback_data="mediainfo_option|cancel")]
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    app.send_message(
        user_id,
        "Enable or disable sending MediaInfo for downloaded files?",
        reply_markup=keyboard
    )
    send_to_logger(message, "User opened /mediainfo menu.")

@app.on_callback_query(filters.regex(r"^mediainfo_option\|"))
@reply_with_keyboard
def mediainfo_option_callback(app, callback_query):
    logger.info(f"[MEDIAINFO] callback: {callback_query.data}")
    user_id = callback_query.from_user.id
    data = callback_query.data.split("|")[1]
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    mediainfo_file = os.path.join(user_dir, "mediainfo.txt")
    if callback_query.data == "mediainfo_option|cancel":
        callback_query.edit_message_text("🔚 MediaInfo: cancelled.")
        callback_query.answer("Menu closed.")
        send_to_logger(callback_query.message, "MediaInfo: cancelled.")
        return
    if data == "on":
        with open(mediainfo_file, "w", encoding="utf-8") as f:
            f.write("ON")
        callback_query.edit_message_text("✅ MediaInfo enabled. After downloading, file info will be sent.")
        send_to_logger(callback_query.message, "MediaInfo enabled.")
        callback_query.answer("MediaInfo enabled.")
        return
    if data == "off":
        with open(mediainfo_file, "w", encoding="utf-8") as f:
            f.write("OFF")
        callback_query.edit_message_text("❌ MediaInfo disabled.")
        send_to_logger(callback_query.message, "MediaInfo disabled.")
        callback_query.answer("MediaInfo disabled.")
        return

@app.on_message(filters.command("split") & filters.private)
@reply_with_keyboard
def split_command(app, message):
    user_id = message.chat.id
    # Subscription check for non-admines
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    # 2-3 row buttons
    sizes = [
        ("250 MB", 250 * 1024 * 1024),
        ("500 MB", 500 * 1024 * 1024),
        ("1 GB", 1024 * 1024 * 1024),
        ("1.5 GB", 1536 * 1024 * 1024),
        ("2 GB (default)", 1950 * 1024 * 1024)
    ]
    buttons = []
    # Pass the buttons in 2-3 rows
    for i in range(0, len(sizes), 2):
        row = []
        for j in range(2):
            if i + j < len(sizes):
                text, size = sizes[i + j]
                row.append(InlineKeyboardButton(text, callback_data=f"split_size|{size}"))
        buttons.append(row)
    buttons.append([InlineKeyboardButton("🔙 Cancel", callback_data="split_size|cancel")])
    keyboard = InlineKeyboardMarkup(buttons)
    app.send_message(user_id, "Choose max part size for video splitting:", reply_markup=keyboard)
    send_to_logger(message, "User opened /split menu.")

@app.on_callback_query(filters.regex(r"^split_size\|"))
@reply_with_keyboard
def split_size_callback(app, callback_query):
    logger.info(f"[SPLIT] callback: {callback_query.data}")
    user_id = callback_query.from_user.id
    data = callback_query.data.split("|")[1]
    if data == "cancel":
        callback_query.edit_message_text("🔚 Split size selection canceled.")
        callback_query.answer("✅ Split choice updated.")
        send_to_logger(callback_query.message, "Split selection canceled.")
        return
    try:
        size = int(data)
    except Exception:
        callback_query.answer("Invalid size.")
        return
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    split_file = os.path.join(user_dir, "split.txt")
    with open(split_file, "w", encoding="utf-8") as f:
        f.write(str(size))
    callback_query.edit_message_text(f"✅ Split part size set to: {humanbytes(size)}")
    send_to_logger(callback_query.message, f"Split size set to {size} bytes.")

