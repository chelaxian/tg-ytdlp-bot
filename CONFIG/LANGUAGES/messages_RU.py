# Messages Configuration
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from CONFIG.config import Config

class Messages(object):
    #######################################################
    # Messages and errors
    #######################################################
    CREDITS_MSG = "<blockquote><i>Администрирует</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Сменить язык: /lang</b>"
    TO_USE_MSG = "<i>Чтобы пользоваться этим ботом, нужно подписаться на канал Telegram @tg_ytdlp.</i>\nПосле вступления в канал <b>отправьте ссылку на видео снова — бот скачает её для вас</b> ❤️\n\n<blockquote>P.S. Из-за возможного 🔞NSFW контента — скачивание с ☁️<b>облачного хранилища</b>, 📁<b>файлообменников</b>, 🔗<b>сокращателей URL</b> и 🔞<b>порно-сайтов</b> платное! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ НЕ 🗑<b>удаляйте канал @tg_ytdlp и не отписывайтесь от него</b>, НЕ 🤖<b>спамьте боту ссылками/командами</b> — иначе будете автоматически заблокированы ⛔️</blockquote>"

    ERROR1 = "Ссылка не найдена. Пожалуйста, введите URL с <b>https://</b> или <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Плейлисты (yt-dlp)</b>

Для скачивания плейлистов отправьте URL с диапазонами <code>*начало*конец</code> в конце. Например: <code>URL*1*5</code> (первые 5 видео с 1 по 5 включительно). <code>URL*-1*-5</code> (последние 5 видео с 1 по 5 включительно).
Или используйте <code>/vid ОТ-ДО URL</code>. Например: <code>/vid 3-7 URL</code> (скачивает видео с 3 по 7 включительно с начала). <code>/vid -3-7 URL</code> (скачивает видео с 3 по 7 включительно с конца). Также работает для команды <code>/audio</code>.

<b>Примеры:</b>

🟥 <b>Диапазон видео из YouTube плейлиста:</b> (нужны 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(скачивает видео с 1 по 5 включительно)
🟥 <b>Одно видео из YouTube плейлиста:</b> (нужны 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(скачивает только 3-е видео)

⬛️ <b>Профиль TikTok:</b> (нужны ваши 🍪)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(скачивает первые 10 видео из профиля пользователя)

🟪 <b>Истории Instagram:</b> (нужны ваши 🍪)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(скачивает первые 3 истории)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(скачивает первые 10 историй из альбома)

🟦 <b>Видео VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(скачивает первые 3 видео из профиля пользователя/группы)

⬛️<b>Каналы Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(скачивает видео с 2 по 4 включительно из канала)

🟪 <b>Клипы Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(скачивает первые 3 клипа из канала)

🟦 <b>Группы Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(скачивает первые 2 видео из группы)

🟧 <b>Модели Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(скачивает первые 2 видео из профиля модели)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(скачивает первые 3 видео из результатов поиска по вашему запросу)

и так далее...
см. <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">список поддерживаемых сайтов</a>
</blockquote>

<blockquote expandable>🖼 <b>Изображения (gallery-dl)</b>

Используйте <code>/img URL</code> для скачивания изображений/фото/альбомов с множества платформ.

<b>Примеры:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Диапазоны:</b>
<code>/img 11-20 https://example.com/album</code> — элементы 11..20
<code>/img 11- https://example.com/album</code> — с 11 до конца (или лимит бота)

<i>Поддерживаемые платформы включают vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor и др. Полный список:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">поддерживаемые сайты gallery-dl</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Бот для скачивания видео - Помощь</b>

📥 <b>Основное использование:</b>
• Отправьте любую ссылку → бот скачает её
  <i>бот автоматически попробует скачать видео через yt-dlp и изображения через gallery-dl.</i>
• <b>Несколько ссылок:</b> В режиме с выбранным качеством (<code>/format</code>) можно отправить до <b>10 ссылок</b> в одном сообщении. Каждая ссылка на новой строке или через пробел.
• <code>/audio URL</code> → извлечь аудио
• <code>/link [качество] URL</code> → получить прямые ссылки
• <code>/proxy</code> → включить/выключить прокси для всех загрузок
• Ответьте на видео текстом → изменить подпись

📋 <b>Плейлисты и диапазоны:</b>
• <code>URL*1*5</code> → скачать первые 5 видео
• <code>URL*-1*-5</code> → скачать последние 5 видео
• <code>/vid 3-7 URL</code> → становится <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → становится <code>URL*-3*-7</code>

🍪 <b>Cookies и приватные:</b>
• Загрузите *.txt cookie для приватных видео
• <code>/cookie [сервис]</code> → скачать куки (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → выбрать источник по индексу (1–N)
• <code>/cookies_from_browser</code> → извлечь из браузера
• <code>/check_cookie</code> → проверить cookie
• <code>/save_as_cookie</code> → сохранить текст как cookie

🧹 <b>Очистка:</b>
• <code>/clean</code> → только медиа файлы
• <code>/clean all</code> → всё
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Настройки:</b>
• <code>/settings</code> → меню настроек
• <code>/format</code> → качество и формат
• <code>/split</code> → разделить видео на части
• <code>/mediainfo on/off</code> → информация о медиа
• <code>/nsfw on/off</code> → размытие NSFW
• <code>/tags</code> → просмотр сохранённых тегов
• <code>/sub on/off</code> → субтитры
• <code>/keyboard</code> → клавиатура (OFF/1x3/2x3)

🏷️ <b>Теги:</b>
• Добавьте <code>#тег1#тег2</code> после URL
• Теги появляются в подписях
• <code>/tags</code> → просмотр всех тегов

🔗 <b>Прямые ссылки:</b>
• <code>/link URL</code> → лучшее качество
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → конкретное качество

⚙️ <b>Быстрые команды:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → установить качество
• <code>/keyboard off/1x3/2x3/full</code> → раскладка клавиатуры
• <code>/split 100mb-2000mb</code> → изменить размер части
• <code>/subs off/ru/en auto</code> → язык субтитров
• <code>/list URL</code> → список доступных форматов
• <code>/mediainfo on/off</code> → вкл/выкл медиаинфо
• <code>/proxy on/off</code> → включить/выключить прокси для всех загрузок

📊 <b>Информация:</b>
• <code>/usage</code> → история загрузок
• <code>/search</code> → поиск через @vid

🖼 <b>Изображения:</b>
• <code>URL</code> → скачать изображения с URL
• <code>/img URL</code> → скачать изображения с URL
• <code>/img 11-20 URL</code> → скачать конкретный диапазон
• <code>/img 11- URL</code> → скачать с 11-го до конца

👨‍💻 <i>Developer:</i> @upekshaip
🤝 <i>Contributor:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Просто сохраните ваш cookie как <b><u>cookie.txt</u></b> и отправьте его боту как документ.\n\n"
        "Вы также можете отправить cookies как обычный текст с помощью команды <b><u>/save_as_cookie</u></b>.\n"
        "<b>Использование <b><u>/save_as_cookie</u></b>:</b>\n\n"
        "<pre>"
        "/save_as_cookie\n"
        "# Netscape HTTP Cookie File\n"
        "# http://curl.haxx.se/rfc/cookie_spec.html\n"
        "# This file was generated by Cookie-Editor\n"
        ".youtube.com  TRUE  /  FALSE  111  ST-xxxxx  session_logininfo=AAA\n"
        ".youtube.com  TRUE  /  FALSE  222  ST-xxxxx  session_logininfo=BBB\n"
        ".youtube.com  TRUE  /  FALSE  33333  ST-xxxxx  session_logininfo=CCC\n"
        "</pre>\n"
        "<blockquote>"
        "<b><u>Инструкции:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (Russian)
    SEARCH_MSG = """
🔍 <b>Поиск видео</b>

Нажмите кнопку ниже для активации встроенного поиска через @vid.

<blockquote>На ПК просто введите <b>"@vid Ваш_Поисковый_Запрос"</b> в любом чате.</blockquote>
    """
    
    # Settings and Hints (Russian)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Команда загрузки изображений</b>\n\n"
        "Использование: <code>/img URL</code>\n\n"
        "<b>Примеры:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Поддерживаемые платформы (примеры):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor и др. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">полный список</a></blockquote>"
        "Также см.: "
    )
    
    LINK_HINT_MSG = (
        "Получить прямые ссылки на видео с выбором качества.\n\n"
        "Использование: /link + URL \n\n"
        "(например: /link https://youtu.be/abc123)\n"
        "(например: /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Добавить бота в группу</b>

Добавьте моих ботов в ваши группы для получения расширенных функций и увеличенных лимитов!
————————————
📊 <b>Текущие БЕСПЛАТНЫЕ лимиты (в ЛС бота):</b>
<blockquote>•🗑 Беспорядочный мусор из всех файлов неотсортированный 👎
• Макс. размер 1 файла: <b>8 ГБ</b>
• Макс. качество 1 файла: <b>БЕЗЛИМИТ</b>
• Макс. длительность 1 файла: <b>БЕЗЛИМИТ</b>
• Макс. количество загрузок: <b>БЕЗЛИМИТ</b>
• Макс. ссылок в одном сообщении: <b>10</b> (только в режиме с выбранным качеством)
• Макс. элементов плейлиста за 1 раз: <b>50</b>
• Макс. видео TikTok за 1 раз: <b>500</b>
• Макс. изображений за 1 раз: <b>1000</b>
• Лимиты на отправку ссылок: <b>5/мин, 60/час, 1000/день</b>
• Лимит команд: <b>20/мин</b>
• 1 загрузка макс. время: <b>2 часа</b>
• 🔞 NSFW контент платный! 1⭐️ = $0.02
• 🆓 ВСЕ ОСТАЛЬНЫЕ МЕДИА ПОЛНОСТЬЮ БЕСПЛАТНЫ
• 📝 Все логи контента и кэширование в мои лог-каналы для мгновенного репоста при повторной загрузке</blockquote>

💬<b>Эти лимиты только для видео с субтитрами:</b>
<blockquote>• Макс. длительность видео+субтитры: <b>1.5 часа</b>
• Макс. размер видео+субтитры: <b>500 МБ</b>
• Макс. качество видео+субтитры: <b>720p</b></blockquote>
————————————
🚀 <b>Преимущества платной группы (2️⃣x лимиты):</b>
<blockquote>•  🗂 Структурированное аккуратное медиа хранилище, отсортированное по темам 👍
•  📁 Боты отвечают в теме, в которой вы их вызываете
•  📌 Автозакрепление статусного сообщения с прогрессом загрузки
•  🖼 Команда /img загружает медиа как альбомы по 10 элементов
• Макс. размер 1 файла: <b>16 ГБ</b> ⬆️
• Макс. ссылок в одном сообщении: <b>20</b> ⬆️ (только в режиме с выбранным качеством)
• Макс. элементов плейлиста за 1 раз: <b>100</b> ⬆️
• Макс. видео TikTok за 1 раз: 1000 ⬆️
• Макс. изображений за 1 раз: 2000 ⬆️
• Лимиты на отправку ссылок: <b>10/мин, 120/час, 2000/день</b> ⬆️
• Лимит команд: <b>40/мин</b> ⬆️
• 1 загрузка макс. время: <b>4 часа</b> ⬆️
• 🔞 NSFW контент: Бесплатно с полными метаданными 🆓
• 📢 Не нужно подписываться на мой канал для групп
• 👥 Все участники группы получат доступ к платным функциям!
• 🗒 Нет логов / нет кэша в мои лог-каналы! Вы можете отключить копирование/репост в настройках группы</blockquote>

💬 <b>2️⃣x лимиты для видео с субтитрами:</b>
<blockquote>• Макс. длительность видео+субтитры: <b>3 часа</b> ⬆️
• Макс. размер видео+субтитры: <b>1000 МБ</b> ⬆️
• Макс. качество видео+субтитры: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Цены и настройка:</b>
<blockquote>• Цена: <b>$5/месяц</b> за 1 бота в группе
• Настройка: Свяжитесь с @iilililiiillliiliililliilliliiil
• Оплата: 💎TON или другие методы💲
• Поддержка: Полная техническая поддержка включена</blockquote>
————————————
Вы можете добавить моих ботов в вашу группу, чтобы разблокировать бесплатный 🔞<b>NSFW</b> и удвоить (x2️⃣) все лимиты.
Свяжитесь со мной, если хотите, чтобы я разрешил вашей группе использовать моих ботов @iilililiiillliiliililliilliliiil
————————————
💡<b>СОВЕТ:</b> <blockquote>Вы можете скинуться деньгами с любым количеством ваших друзей (например, 100 человек) и сделать 1 покупку для всей группы - ВСЕ УЧАСТНИКИ ГРУППЫ ПОЛУЧАТ ПОЛНЫЙ НЕОГРАНИЧЕННЫЙ ДОСТУП ко всем функциям ботов в этой группе всего за <b>0.05$</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW режим: ВКЛ✅</b>

• NSFW контент будет отображаться без размытия.
• Спойлеры не будут применяться к NSFW медиа.
• Контент будет виден сразу

<i>Используйте /nsfw off для включения размытия</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW режим: ВЫКЛ</b>

⚠️ <b>Размытие включено</b>
• NSFW контент будет скрыт под спойлером   
• Для просмотра нужно будет нажать на медиа
• Спойлеры будут применяться к NSFW медиа.

<i>Используйте /nsfw on для отключения размытия</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Неверный параметр</b>

Используйте:
• <code>/nsfw on</code> - отключить размытие
• <code>/nsfw off</code> - включить размытие
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Проверка кэша...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Обработка..."
    DOWNLOADING_MSG = "📥 <b>Загрузка медиа...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Загрузка изображения...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Загрузка завершена</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Загружено:"
    SENT_STATUS_MSG = "Отправлено:"
    PENDING_TO_SEND_STATUS_MSG = "Ожидает отправки:"
    TITLE_LABEL_MSG = "Название:"
    MEDIA_COUNT_LABEL_MSG = "Количество медиа:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Загрузка завершена, обработка аудио..."
    VIDEO_PROCESSING_MSG = "📽 Видео обрабатывается..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Отправлено из кэша</b>\n\nОтправлено альбомов: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Видео успешно отправлено из кэша."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Видео плейлиста отправлены из кэша ({cached}/{total} файлов)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} видео отправлены из кэша, загружаем недостающие..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Отправлено из кэша: {cached}\n🔄 Продолжаем загрузку..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Не удалось проанализировать медиа, продолжаем с максимально допустимым диапазоном (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Не удалось определить количество медиа, продолжаем с максимально допустимым диапазоном (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Не удалось определить общее количество медиа, продолжаем с указанным диапазоном {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>Неверный URL</b>\n\nПожалуйста, предоставьте действительный URL, начинающийся с http:// или https://"

    ERROR_OCCURRED_MSG = "❌ <b>Произошла ошибка</b>\n\n<code>{url}</code>\n\nОшибка: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Ошибка отправки видео: {error}"
    ERROR_UNKNOWN_MSG = "❌ Неизвестная ошибка: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Недостаточно места на диске для загрузки видео."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Размер файла превышает лимит {limit} ГБ. Пожалуйста, выберите файл меньшего размера в пределах допустимого."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>Не удалось скачать видео со всеми доступными прокси</b>\n\nВсе попытки скачивания через прокси завершились неудачей.\nПопробуйте:\n• Проверить работоспособность прокси\n• Попробовать другой прокси из списка\n• Скачать без прокси (если возможно)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Ошибка получения ссылки:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram ограничил отправку сообщений.\n⏳ Пожалуйста, подождите: {time}\nДля обновления таймера отправьте URL еще 2 раза."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram ограничил отправку сообщений.\n⏳ Пожалуйста, подождите: \nДля обновления таймера отправьте URL еще 2 раза."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Не удалось загрузить субтитры"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Прямые ссылки на поток</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Название:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Длительность:</b> {duration} сек\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Ошибка: Исходное сообщение не найдено."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Тег #{tag} содержит запрещённые символы. Разрешены только буквы, цифры и _.\nПожалуйста, используйте: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Видео плейлиста отправлены: {sent}/{total} файлов."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>Подсказка по плейлистам</b>

Вы отправили ссылку на плейлист без указания диапазона. Бот автоматически скачал первое видео (<code>*1*1</code>).

<b>Для скачивания нескольких видео из плейлиста укажите диапазон:</b>
• <code>URL*1*5</code> — первые 5 видео (с 1 по 5 включительно)
• <code>URL*3*3</code> — только 3-е видео
• <code>/vid 1-10 URL</code> — альтернативный формат

Подробнее: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ Отправлено из кэша: {cached}/{total} файлов."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Не удалось получить ссылки на поток"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Выберите браузер для загрузки cookies:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "На этой системе браузеры не найдены. Вы можете загрузить cookies с удалённого URL или мониторить статус браузера:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Открыть браузер</b> - для мониторинга статуса браузера в мини-приложении"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Открыть браузер"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Загрузить cookie c URL"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie файл загружен через резервный источник и сохранён как cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Поддерживаемые браузеры не найдены и COOKIE_URL не настроен. Используйте /cookie или загрузите cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Резервный COOKIE_URL должен указывать на .txt файл."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Резервный cookie файл слишком большой (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Резервный источник cookie недоступен (статус {status}). Попробуйте /cookie или загрузите cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Ошибка загрузки резервного cookie. Попробуйте /cookie или загрузите cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Неожиданная ошибка при загрузке резервного cookie."
    BTN_CLOSE = "🔚Закрыть"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Неверное булево значение"
    ARGS_CLOSED_MSG = "Закрыто"
    ARGS_ALL_RESET_MSG = "✅ Все аргументы сброшены"
    ARGS_RESET_ERROR_MSG = "❌ Ошибка сброса аргументов"
    ARGS_INVALID_PARAM_MSG = "❌ Неверный параметр"
    ARGS_BOOL_SET_MSG = "Установлено в {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "Уже установлено в {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Неверное значение выбора"
    ARGS_VALUE_SET_MSG = "Установлено в {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "Уже установлено в {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Текущее значение:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Примеры:</b>\n• <code>default</code> - Использовать стратегию XFF по умолчанию\n• <code>never</code> - Никогда не использовать XFF заголовок\n• <code>US</code> - Код страны США\n• <code>GB</code> - Код страны Великобритании\n• <code>DE</code> - Код страны Германии\n• <code>FR</code> - Код страны Франции\n• <code>JP</code> - Код страны Японии\n• <code>192.168.1.0/24</code> - IP блок (CIDR)\n• <code>10.0.0.0/8</code> - Приватный IP диапазон\n• <code>203.0.113.0/24</code> - Публичный IP блок\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Примечание:</b> Это заменяет опции --geo-bypass. Используйте любой 2-буквенный код страны или IP блок в нотации CIDR.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Пример:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Пожалуйста, отправьте ваше новое значение."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Диапазон:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Пожалуйста, отправьте число."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Примеры:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Примечание:</b> Эти заголовки будут добавлены к существующим Referer и User-Agent заголовкам.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Текущие аргументы yt-dlp:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - Переключатели True/False\n• 📋 <b>Select</b> - Выбор из опций\n• 🔢 <b>Numeric</b> - Числовой ввод\n• 📝🔧 <b>Text</b> - Текстовый/JSON ввод</blockquote>\n\nЭти настройки будут применены ко всем вашим загрузкам."
    
    # Локализованные названия параметров для отображения
    ARGS_PARAM_NAMES = {
        "force_ipv6": "Принудительные IPv6 подключения",
        "force_ipv4": "Принудительные IPv4 подключения", 
        "no_live_from_start": "Не загружать прямые трансляции с начала",
        "live_from_start": "Загружать прямые трансляции с начала",
        "no_check_certificates": "Подавить проверку HTTPS сертификата",
        "check_certificate": "Проверить SSL сертификат",
        "no_playlist": "Загружать только одно видео, не плейлист",
        "embed_metadata": "Встроить метаданные в видеофайл",
        "embed_thumbnail": "Встроить миниатюру в видеофайл",
        "write_thumbnail": "Записать миниатюру в файл",
        "ignore_errors": "Игнорировать ошибки загрузки и продолжать",
        "legacy_server_connect": "Разрешить устаревшие подключения к серверу",
        "concurrent_fragments": "Количество одновременных фрагментов для загрузки",
        "xff": "Стратегия заголовка X-Forwarded-For",
        "user_agent": "Заголовок User-Agent",
        "impersonate": "Имитация браузера",
        "referer": "Заголовок Referer",
        "geo_bypass": "Обход географических ограничений",
        "hls_use_mpegts": "Использовать MPEG-TS для HLS",
        "no_part": "Не использовать .part файлы",
        "no_continue": "Не возобновлять частичные загрузки",
        "audio_format": "Формат аудио",
        "video_format": "Формат видео",
        "merge_output_format": "Формат слияния",
        "send_as_file": "Отправлять как файл",
        "username": "Имя пользователя",
        "password": "Пароль",
        "twofactor": "Код двухфакторной аутентификации",
        "min_filesize": "Минимальный размер файла (МБ)",
        "max_filesize": "Максимальный размер файла (МБ)",
        "playlist_items": "Элементы плейлиста",
        "date": "Дата",
        "datebefore": "Дата до",
        "dateafter": "Дата после",
        "http_headers": "HTTP заголовки",
        "sleep_interval": "Интервал задержки",
        "max_sleep_interval": "Максимальный интервал задержки",
        "retries": "Количество повторов",
        "http_chunk_size": "Размер HTTP чанка",
        "sleep_subtitles": "Задержка для субтитров"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ Конфигурация аргументов yt-dlp</b>\n\n<blockquote>📋 <b>Группы:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ Конфигурация аргументов yt-dlp</b>\n\n"
        "<blockquote>📋 <b>Группы:</b>\n"
        "• ✅/❌ <b>Boolean</b> - Переключатели True/False\n"
        "• 📋 <b>Select</b> - Выбор из опций\n"
        "• 🔢 <b>Numeric</b> - Числовой ввод\n"
        "• 📝🔧 <b>Text</b> - Текстовый/JSON ввод</blockquote>\n\n"
        "Эти настройки будут применены ко всем вашим загрузкам."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Пожалуйста, подождите..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Произошла ошибка"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Режим ввода автоматически закрыт из-за неактивности (5 минут)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Ввод содержит потенциально опасный контент: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Ввод слишком длинный (макс. 1000 символов)"
    ARGS_INVALID_URL_MSG = "❌ Неверный формат URL. Должен начинаться с http:// или https://"
    ARGS_INVALID_JSON_MSG = "❌ Неверный формат JSON"
    ARGS_NUMBER_RANGE_MSG = "❌ Число должно быть между {min_val} и {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Неверный формат числа"
    ARGS_DATE_FORMAT_MSG = "❌ Дата должна быть в формате YYYYMMDD (например, 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Год должен быть между 1900 и 2100"
    ARGS_MONTH_RANGE_MSG = "❌ Месяц должен быть между 01 и 12"
    ARGS_DAY_RANGE_MSG = "❌ День должен быть между 01 и 31"
    ARGS_INVALID_DATE_MSG = "❌ Неверный формат даты"
    ARGS_INVALID_XFF_MSG = "❌ XFF должен быть 'default', 'never', код страны (например, US) или IP блок (например, 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "Пользовательские аргументы не установлены. Все параметры используют значения по умолчанию."
    ARGS_RESET_SUCCESS_MSG = "✅ Все аргументы сброшены к значениям по умолчанию."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Текст слишком длинный. Максимум 500 символов."
    ARGS_ERROR_PROCESSING_MSG = "❌ Ошибка обработки ввода. Пожалуйста, попробуйте снова."
    ARGS_BOOL_INPUT_MSG = "❌ Пожалуйста, введите 'True' или 'False' для опции Send As File."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Пожалуйста, предоставьте действительное число."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Пожалуйста, отправьте <code>True</code> или <code>False</code> для включения/отключения этой опции."
    ARGS_JSON_VALUE_REQUEST_MSG = "Пожалуйста, отправьте действительный JSON."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "У вас пока нет тегов."
    TAGS_MESSAGE_CLOSED_MSG = "Сообщение с тегами закрыто."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Субтитры отключены и режим Always Ask выключен."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ Субтитры Always Ask включён."
    SUBS_LANGUAGE_SET_MSG = "✅ Язык субтитров установлен: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️ПРЕДУПРЕЖДЕНИЕ: из-за высокой нагрузки на CPU эта функция очень медленная (почти в реальном времени) и ограничена:\n"
        "- 720p максимальное качество\n"
        "- 1.5 часа максимальная длительность\n"
        "- 500мб максимальный размер видео</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Быстрые команды:</b>\n"
        "• <code>/subs off</code> - отключить субтитры\n"
        "• <code>/subs on</code> - включить режим Always Ask\n"
        "• <code>/subs ru</code> - установить язык\n"
        "• <code>/subs ru auto</code> - установить язык с AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Субтитры отключены"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Выбранный язык: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Загрузка субтитров..."
    SUBS_DISABLED_ERROR_MSG = "❌ Субтитры отключены. Используйте /subs для настройки."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Загрузка субтитров поддерживается только для YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Субтитры</b>\n\n"
        "<b>Видео:</b> {title}\n"
        "<b>Язык:</b> {lang}\n"
        "<b>Тип:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 SRT-файл субтитров отправлен пользователю."
    SUBS_ERROR_PROCESSING_MSG = "❌ Ошибка обработки файла субтитров."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Не удалось загрузить субтитры."
    SUBS_ERROR_MSG = "❌ Ошибка загрузки субтитров: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Размер части для разделения установлен: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **Неверный размер!**\n\n"
        "**Допустимый диапазон:** 100МБ до 2ГБ\n\n"
        "**Допустимые форматы:**\n"
        "• `100mb` до `2000mb` (мегабайты)\n"
        "• `0.1gb` до `2gb` (гигабайты)\n\n"
        "**Примеры:**\n"
        "• `/split 100mb` - 100 мегабайт\n"
        "• `/split 500mb` - 500 мегабайт\n"
        "• `/split 1.5gb` - 1.5 гигабайта\n"
        "• `/split 2gb` - 2 гигабайта\n"
        "• `/split 2000mb` - 2000 мегабайт (2ГБ)\n\n"
        "**Предустановки:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Выберите максимальный размер части для разделения видео:**\n\n"
        "**Диапазон:** 100МБ до 2ГБ\n\n"
        "**Быстрые команды:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Примеры:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Меню закрыто."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Настройки бота</b>\n\nВыберите категорию:"
    SETTINGS_MENU_CLOSED_MSG = "Меню закрыто."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Опции очистки</b>\n\nВыберите что очистить:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nВыберите действие:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 МЕДИА</b>\n\nВыберите действие:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 ИНФОРМАЦИЯ</b>\n\nВыберите действие:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ ДОПОЛНИТЕЛЬНЫЕ КОМАНДЫ</b>\n\nВыберите действие:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Команда выполнена."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Лимит флуда. Попробуйте позже."
    SETTINGS_HINT_SENT_MSG = "Подсказка отправлена."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Помощник поиска открыт."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Неизвестная команда."
    SETTINGS_HINT_CLOSED_MSG = "Подсказка закрыта."
    SETTINGS_HELP_SENT_MSG = "Отправить справку пользователю"
    SETTINGS_MENU_OPENED_MSG = "Открыто меню /settings"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Помощник поиска закрыт"
    SEARCH_CLOSED_MSG = "Закрыто"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Прокси {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Ошибка сохранения настроек прокси."
    PROXY_MENU_TEXT_MSG = "Включить или отключить использование прокси сервера для всех операций yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Включить или отключить использование прокси серверов ({config_count} + {file_count} доступно) для всех операций yt-dlp?\n\nПри включении ALL (AUTO) прокси подбираются автоматически по разрешённым странам (из ошибки YouTube)."
    PROXY_MENU_CLOSED_MSG = "Меню закрыто."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Прокси включён. Все операции yt-dlp будут использовать прокси."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Прокси включён. Все операции yt-dlp будут использовать {count} прокси серверов с методом выбора {method}."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Прокси включен (АВТО по ошибке YouTube).\n\nПри ошибке гео-блокировки YouTube бот будет пробовать только прокси из стран, указанных в тексте ошибки (без перебора всех прокси подряд)."
    PROXY_DISABLED_MSG = "❌ Прокси отключён."
    PROXY_TRYING_COUNTRY_MSG = "🔄 Пробуем прокси: {country} ({current}/{total})"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Ошибка сохранения настроек прокси."
    PROXY_ENABLED_CALLBACK_MSG = "Прокси включён."
    PROXY_DISABLED_CALLBACK_MSG = "Прокси отключён."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ ЖДИТЕ ПОКА ВАША ПРЕДЫДУЩАЯ ЗАГРУЗКА НЕ ЗАВЕРШИТСЯ"
    AUDIO_HELP_MSG = (
        "<b>🎧 Команда загрузки аудио</b>\n\n"
        "Использование: <code>/audio URL</code>\n\n"
        "<b>Примеры:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Также см.: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Подсказка по аудио закрыта."
    PLAYLIST_HELP_CLOSED_MSG = "Справка по плейлистам закрыта."
    USERLOGS_CLOSED_MSG = "Сообщение с логами закрыто."
    HELP_CLOSED_MSG = "Справка закрыта."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>Настройки размытия NSFW</b>\n\nNSFW контент <b>{status}</b>.\n\nВыберите размывать ли NSFW контент:"
    NSFW_MENU_CLOSED_MSG = "Меню закрыто."
    NSFW_BLUR_DISABLED_MSG = "Размытие NSFW отключено."
    NSFW_BLUR_ENABLED_MSG = "Размытие NSFW включено."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Размытие NSFW отключено."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Размытие NSFW включено."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Включить или отключить отправку MediaInfo для загруженных файлов?"
    MEDIAINFO_MENU_CLOSED_MSG = "Меню закрыто."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo включён. После загрузки информация о файле будет отправлена."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo отключён."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo включён."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo отключён."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Список доступных форматов</b>\n\n"
        "Получить доступные видео/аудио форматы для URL.\n\n"
        "<b>Использование:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Примеры:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Как использовать ID форматов:</b>\n"
        "После получения списка используйте конкретный ID формата:\n"
        "• <code>/format id 401</code> - скачать формат 401\n"
        "• <code>/format id401</code> - то же самое\n"
        "• <code>/format id140 audio</code> - скачать формат 140 как MP3 аудио\n\n"
        "Эта команда покажет все доступные форматы, которые можно скачать."
    )
    LIST_PROCESSING_MSG = "🔄 Получение доступных форматов..."
    LIST_INVALID_URL_MSG = "❌ Пожалуйста, предоставьте действительный URL, начинающийся с http:// или https://"
    LIST_CAPTION_MSG = (
        "📃 Доступные форматы для:\n<code>{url}</code>\n\n"
        "💡 <b>Как установить формат:</b>\n"
        "• <code>/format id 134</code> - Скачать конкретный ID формата\n"
        "• <code>/format 720p</code> - Скачать по качеству\n"
        "• <code>/format best</code> - Скачать лучшее качество\n"
        "• <code>/format ask</code> - Всегда спрашивать качество\n\n"
        "{audio_note}\n"
        "📋 Используйте ID формата из списка выше"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Только аудио форматы:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Скачать формат 140 как MP3 аудио\n"
        "• <code>/format id140 audio</code> - то же самое\n"
        "Эти форматы будут скачаны как MP3 аудио файлы.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Ошибка отправки файла форматов: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Не удалось получить форматы:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Произошла ошибка при обработке команды"
    LIST_ERROR_CALLBACK_MSG = "Произошла ошибка"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Как использовать ID форматов:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "После получения списка используйте конкретный ID формата:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - скачать формат 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - то же самое\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - скачать формат 140 как MP3 аудио\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - то же самое\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Обнаружены только аудио форматы: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Эти форматы будут скачаны как MP3 аудио файлы.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Только видео форматы:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Используйте ID формата из списка выше"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Использование:</b>\n"
        "<code>/link [качество] URL</code>\n\n"
        "<b>Примеры:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - лучшее качество\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p или ниже\n"
        "• /link 720p https://youtube.com/watch?v=... - то же самое\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K или ниже\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K или ниже"
        "</blockquote>\n\n"
        "<b>Качество:</b> от 1 до 10000 (например, 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Пожалуйста, предоставьте действительный URL"
    LINK_PROCESSING_MSG = "🔗 Получение прямой ссылки..."
    LINK_DURATION_MSG = "⏱ <b>Длительность:</b> {duration} сек\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Видео поток:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Аудио поток:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Настройка клавиатуры обновлена!**\n\nНовая настройка: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Неверный аргумент!**\n\n"
        "Допустимые опции: `off`, `1x3`, `2x3`, `full`\n\n"
        "Пример: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Настройки клавиатуры**\n\n"
        "Текущая: **{current}**\n\n"
        "Выберите опцию:\n\n"
        "Или используйте: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 клавиатура активирована!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Клавиатура скрыта"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3 клавиатура активирована!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3 клавиатура активирована!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Эмодзи клавиатура активирована!"
    KEYBOARD_ERROR_APPLYING_MSG = "Ошибка применения настройки клавиатуры {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Формат установлен: Всегда спрашивать. Вам будет предложено выбрать качество каждый раз при отправке URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Формат установлен: Всегда спрашивать. Теперь вам будет предложено выбрать качество каждый раз при отправке URL."
    FORMAT_BEST_UPDATED_MSG = "✅ Формат обновлен до лучшего качества (приоритет AVC+MP4):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Формат обновлен до ID {id}:\n{format}\n\n💡 <b>Примечание:</b> Если это только аудио формат, он будет скачан как MP3 аудио файл."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Формат обновлен до ID {id} (только аудио):\n{format}\n\n💡 Это будет скачано как MP3 аудио файл."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Формат обновлен до качества {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Формат обновлен до:\n{format}"
    FORMAT_MENU_MSG = (
        "Выберите опцию формата или отправьте пользовательский используя:\n"
        "• <code>/format &lt;format_string&gt;</code> - пользовательский формат\n"
        "• <code>/format 720</code> - качество 720p\n"
        "• <code>/format 4k</code> - качество 4K\n"
        "• <code>/format 8k</code> - качество 8K\n"
        "• <code>/format id 401</code> - конкретный ID формата\n"
        "• <code>/format ask</code> - всегда показывать меню\n"
        "• <code>/format best</code> - bv+ba/лучшее качество"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Чтобы использовать пользовательский формат, отправьте команду в следующем виде:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Замените <code>bestvideo+bestaudio/best</code> на желаемую строку формата."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Выберите желаемое разрешение и кодек:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Формат установлен: Всегда спрашивать. Теперь вам будет предложено выбрать качество каждый раз при отправке URL."
    FORMAT_UPDATED_MSG = "✅ Формат обновлен до:\n{format}"
    FORMAT_SAVED_MSG = "✅ Формат сохранен."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Выбор формата обновлен."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Меню пользовательского формата закрыто"
    FORMAT_CODEC_SET_MSG = "✅ Кодек установлен в {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Выбор браузера обновлен."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Доступ запрещен. Только для администраторов."
    ACCESS_DENIED_ADMIN = "❌ Доступ запрещен. Только для администраторов."
    WELCOME_MASTER = "Добро пожаловать, Мастер 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Извините... Произошла ошибка во время загрузки."
    SIZE_LIMIT_EXCEEDED = "❌ Размер файла превышает лимит {max_size_gb} ГБ. Пожалуйста, выберите файл меньшего размера в пределах допустимого."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Скрипт не найден: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Загрузка свежего дампа Firebase используя {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Кэш Firebase успешно перезагружен!"
    ADMIN_CACHE_FAILED_MSG = "❌ Не удалось перезагрузить кэш Firebase. Проверьте, существует ли {cache_file}."
    ADMIN_ERROR_RELOADING_MSG = "❌ Ошибка перезагрузки кэша: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Ошибка выполнения {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Промо сообщение отправлено всем остальным пользователям</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Не удалось отправить промо сообщение. Попробуйте ответить на сообщение\nИли произошла ошибка</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ Пользователь еще не скачивал контент...</b> Не существует в логах"
    ADMIN_INVALID_COMMAND_MSG = "❌ Неверная команда"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ Данные не найдены в кэше для <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Очередь пуста — никто из подписчиков ещё не покинул канал."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Очередь на бан</b>\nВсего в ожидании: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (вышел: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… и ещё {extra} пользователей."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Команды: /block_user all • /block_user auto • /block_user 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Заблокировано пользователей из очереди: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Авто-блокировка включена: новые выходы будут блокироваться сразу."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Авто-блокировка отключена."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Авто-блокировка по окну установлена на каждые {interval}."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Журнал действий канала за последние {hours} ч. (2 дня)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 За последние {hours} ч. (2 дня): вступило {joined}, покинуло {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Нет действий за последние {hours} ч. (2 дня)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Итого: 🟢 {joined} вступили, 🔴 {left} покинули."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Нет доступа к журналу действий канала. Боты не могут читать admin logs. Укажите CHANNEL_GUARD_SESSION_STRING в конфиге с сессией пользователя для доступа к этой функции."
    BAN_TIME_USAGE_MSG = "❌ Использование: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Укажите интервал в формате 10s, 6m, 5h, 4d, 3w, 2M или 1y."
    BAN_TIME_SET_MSG = "🕒 Период проверки логов канала установлен на {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Отчёт проверки канала\n"
        "Время запуска: {run_ts}\n"
        "Интервал: {interval}\n"
        "Новых выходов: {new_leavers}\n"
        "Авто-банов: {auto_banned}\n"
        "В очереди: {pending}\n"
        "Последний event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Использование: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Администратор не может удалить администратора"
    ADMIN_USER_BLOCKED_MSG = "Пользователь заблокирован 🔒❌\n \nID: <code>{user_id}</code>\nДата блокировки: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> уже заблокирован ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Извините! Вы не администратор"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Использование: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Пользователь разблокирован 🔓✅\n \nID: <code>{user_id}</code>\nДата разблокировки: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> уже разблокирован ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Разблокировано пользователей: {count}\n⏱ Дата операции: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Использование: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Пользователь игнорирован 👁️❌\n \nID: <code>{user_id}</code>\nДата игнорирования: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> уже игнорируется ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Использование: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Пользователь больше не игнорируется 👁️✅\n \nID: <code>{user_id}</code>\nДата снятия игнорирования: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> не игнорируется ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Время работы бота -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Пожалуйста, предоставьте URL для очистки кэша.\nИспользование: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Пожалуйста, предоставьте действительный URL.\nИспользование: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Кэш успешно очищен для URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Кэш не найден для этой ссылки."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Ошибка очистки кэша: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Доступ запрещен. Только для администраторов."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Запуск скрипта обновления списка порно: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Скрипт успешно завершен!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Скрипт успешно завершен!\n\nВывод:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Скрипт завершился с кодом возврата {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Ошибка выполнения скрипта: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Перезагрузка кэшей порно и доменов..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Кэши порно успешно перезагружены!\n\n"
        "📊 Текущий статус кэша:\n"
        "• Порно домены: {porn_domains}\n"
        "• Порно ключевые слова: {porn_keywords}\n"
        "• Поддерживаемые сайты: {supported_sites}\n"
        "• БЕЛЫЙ СПИСОК: {whitelist}\n"
        "• СЕРЫЙ СПИСОК: {greylist}\n"
        "• ЧЕРНЫЙ СПИСОК: {black_list}\n"
        "• БЕЛЫЕ КЛЮЧЕВЫЕ СЛОВА: {white_keywords}\n"
        "• ПРОКСИ ДОМЕНЫ: {proxy_domains}\n"
        "• ПРОКСИ_2_ДОМЕНЫ: {proxy_2_domains}\n"
        "• ОЧИСТКА_ЗАПРОСА: {clean_query}\n"
        "• ДОМЕНЫ_БЕЗ_КУКИ: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Ошибка перезагрузки кэша порно: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Пожалуйста, предоставьте URL для проверки.\nИспользование: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Пожалуйста, предоставьте действительный URL.\nИспользование: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Проверка URL на NSFW контент...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Результат проверки порно</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Статус:</b> <b>{status_text}</b>\n\n"
        "<b>Объяснение:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Ошибка проверки URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Куки очищены."
    CLEAN_LOGS_CLEANED_MSG = "Логи очищены."
    CLEAN_TAGS_CLEANED_MSG = "Теги очищены."
    CLEAN_FORMAT_CLEANED_MSG = "Формат очищен."
    CLEAN_SPLIT_CLEANED_MSG = "Разделение очищено."
    CLEAN_MEDIAINFO_CLEANED_MSG = "MediaInfo очищен."
    CLEAN_SUBS_CLEANED_MSG = "Настройки субтитров очищены."
    CLEAN_KEYBOARD_CLEANED_MSG = "Настройки клавиатуры очищены."
    CLEAN_ARGS_CLEANED_MSG = "Настройки аргументов очищены."
    CLEAN_NSFW_CLEANED_MSG = "Настройки NSFW очищены."
    CLEAN_PROXY_CLEANED_MSG = "Настройки прокси очищены."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Настройки флуд-лимита очищены."
    CLEAN_ALL_CLEANED_MSG = "Все файлы очищены."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 КУКИ</b>\n\nВыберите действие:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Файл cookie сохранен"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Пропущена валидация для не-YouTube cookies"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Файл cookie существует, но имеет неверный формат"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Файл cookie не найден."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Запуск теста YouTube cookies...\n\nПожалуйста, подождите, пока я проверю и валидирую ваши cookies."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Ваши существующие YouTube cookies работают правильно!\n\nНет необходимости загружать новые."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Ваши существующие YouTube cookies истекли или недействительны.\n\n🔄 Загрузка новых cookies..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ Источник cookie {service} не настроен!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ Источник cookie {service} должен быть .txt файлом!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Превышен лимит диапазона: запрошено {range_count} файлов (максимум {max_img_files}).\n\nИспользуйте одну из этих команд для загрузки максимально доступных файлов:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Закрыть"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Превышен лимит медиа: запрошено {count} файлов (максимум {max_count}).\n\nИспользуйте одну из этих команд для загрузки максимально доступных файлов:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Найдено <b>{count}</b> медиафайлов по ссылке"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Выберите диапазон загрузки:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Имитация браузера"
    ARGS_REFERER_DESC_MSG = "Referer заголовок"
    ARGS_USER_AGENT_DESC_MSG = "User-Agent заголовок"
    ARGS_GEO_BYPASS_DESC_MSG = "Обход географических ограничений"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Проверка SSL сертификата"
    ARGS_LIVE_FROM_START_DESC_MSG = "Скачивать прямые трансляции с начала"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Не скачивать прямые трансляции с начала"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Использовать MPEG-TS контейнер для HLS видео"
    ARGS_NO_PLAYLIST_DESC_MSG = "Скачивать только одно видео, не плейлист"
    ARGS_NO_PART_DESC_MSG = "Не использовать .part файлы"
    ARGS_NO_CONTINUE_DESC_MSG = "Не возобновлять частичные загрузки"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Формат аудио для извлечения"
    ARGS_EMBED_METADATA_DESC_MSG = "Встраивать метаданные в видео файл"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Встраивать превью в видео файл"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Записывать превью в файл"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Количество одновременных фрагментов для загрузки"
    ARGS_FORCE_IPV4_DESC_MSG = "Принудительные IPv4 соединения"
    ARGS_FORCE_IPV6_DESC_MSG = "Принудительные IPv6 соединения"
    ARGS_XFF_DESC_MSG = "Стратегия заголовка X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "Размер HTTP чанка (байты)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Задержка перед загрузкой субтитров (секунды)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Разрешить устаревшие серверные соединения"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Подавить валидацию HTTPS сертификата"
    ARGS_USERNAME_DESC_MSG = "Имя пользователя аккаунта"
    ARGS_PASSWORD_DESC_MSG = "Пароль аккаунта"
    ARGS_TWOFACTOR_DESC_MSG = "Код двухфакторной аутентификации"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Игнорировать ошибки загрузки и продолжать"
    ARGS_MIN_FILESIZE_DESC_MSG = "Минимальный размер файла (МБ)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Максимальный размер файла (МБ)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Элементы плейлиста для скачивания (например, 1,3,5 или 1-5)"
    ARGS_DATE_DESC_MSG = "Скачивать видео, загруженные в эту дату (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Скачивать видео, загруженные до этой даты (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Скачивать видео, загруженные после этой даты (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Пользовательские HTTP заголовки (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Интервал задержки между запросами (секунды)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Максимальный интервал задержки (секунды)"
    ARGS_RETRIES_DESC_MSG = "Количество повторных попыток"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Формат видео контейнера"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Формат выходного контейнера для слияния"
    ARGS_SEND_AS_FILE_DESC_MSG = "Отправлять все медиа как документ вместо медиа"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Имитация"
    ARGS_REFERER_SHORT_MSG = "Реферер"
    ARGS_GEO_BYPASS_SHORT_MSG = "Гео Обход"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Проверка Сертификата"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Прямая с Начала"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Без Прямой с Начала"
    ARGS_USER_AGENT_SHORT_MSG = "User-Agent"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Без Плейлиста"
    ARGS_NO_PART_SHORT_MSG = "Без Частей"
    ARGS_NO_CONTINUE_SHORT_MSG = "Без Продолжения"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Формат Аудио"
    ARGS_EMBED_METADATA_SHORT_MSG = "Встроить Мета"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Встроить Превью"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Записать Превью"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Одновременно"
    ARGS_FORCE_IPV4_SHORT_MSG = "Принудительный IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Принудительный IPv6"
    ARGS_XFF_SHORT_MSG = "XFF Заголовок"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Размер Чанка"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Задержка Субтитров"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Устаревшее Соединение"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Без Проверки Сертификата"
    ARGS_USERNAME_SHORT_MSG = "Имя Пользователя"
    ARGS_PASSWORD_SHORT_MSG = "Пароль"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Игнорировать Ошибки"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Мин Размер"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Макс Размер"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Элементы Плейлиста"
    ARGS_DATE_SHORT_MSG = "Дата"
    ARGS_DATEBEFORE_SHORT_MSG = "Дата До"
    ARGS_DATEAFTER_SHORT_MSG = "Дата После"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP Заголовки"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Интервал Задержки"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Макс Задержка"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Формат Видео"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Формат Слияния"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Отправлять как Файл"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ Файл слишком большой. Максимальный размер 100 КБ."
    COOKIES_INVALID_FORMAT_MSG = "❌ Разрешены только файлы формата .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ Файл не похож на cookie.txt (нет строки '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ Ошибка чтения файла: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Файл cookie существует и имеет правильный формат"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ Файл cookie {service} слишком большой! Макс 100КБ, получено {size}КБ."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ Файл cookie {service} загружен и сохранен как cookie.txt в вашей папке.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ Источник cookie {service} недоступен (статус {status}). Попробуйте позже."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Ошибка загрузки файла cookie {service}. Попробуйте позже."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Пользователь предоставил новый файл cookie.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie успешно обновлен:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Недействительный cookie.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ Источники YouTube cookie не настроены!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Загрузка и проверка YouTube cookies...\n\nПопытка {attempt} из {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Доступ запрещен. Только для администраторов."
    ADMIN_USER_LOGS_TOTAL_MSG = "Всего: <b>{total}</b>\n<b>{user_id}</b> - логи (Последние 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 клавиатура активирована!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Язык субтитров установлен: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Язык субтитров установлен: {flag} {name} с включенным AUTO/TRANS."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Меню языка субтитров закрыто."
    SUBS_DOWNLOADING_MSG = "💬 Загрузка субтитров..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Перезагрузка кэша Firebase в память..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ COOKIE_URL не настроен. Используйте /cookie или загрузите cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Загрузка cookies с удаленного URL..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Резервный COOKIE_URL должен указывать на .txt файл."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Резервный файл cookie слишком большой (>100КБ)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Файл YouTube cookie загружен через резервный источник и сохранен как cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Резервный источник cookie недоступен (статус {status}). Попробуйте /cookie или загрузите cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Ошибка загрузки резервного cookie. Попробуйте /cookie или загрузите cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Неожиданная ошибка при загрузке резервного cookie."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ Браузер {browser} не установлен."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookies сохранены используя браузер: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Не удалось сохранить cookies: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube cookies работают правильно"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube cookies истекли или недействительны\n\nИспользуйте /cookie для получения новых cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - пользовательский формат\n• <code>/format 720</code> - качество 720p\n• <code>/format 4k</code> - качество 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Подсказка отправлена."
    FORMAT_MKV_TOGGLE_MSG = "MKV теперь {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Удаленный URL не настроен"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Неверный формат файла"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Файл слишком большой"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookies успешно загружены"
    COOKIES_SERVER_ERROR_MSG = "❌ Ошибка сервера {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Загрузка не удалась"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Неожиданная ошибка"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Браузер не установлен."
    COOKIES_MENU_CLOSED_MSG = "Меню закрыто."
    COOKIES_HINT_CLOSED_MSG = "Подсказка cookie закрыта."
    IMG_HELP_CLOSED_MSG = "Справка закрыта."
    SUBS_LANGUAGE_UPDATED_MSG = "Настройки языка субтитров обновлены."
    SUBS_MENU_CLOSED_MSG = "Меню языка субтитров закрыто."
    KEYBOARD_SET_TO_MSG = "Клавиатура установлена в {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Ошибка обработки настройки"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo включен."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo отключен."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Размытие NSFW отключено."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Размытие NSFW включено."
    SETTINGS_MENU_CLOSED_MSG = "Меню закрыто."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Активен флуд-лимит. Попробуйте позже."
    OTHER_HELP_CLOSED_MSG = "Справка закрыта."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Сообщение с логами закрыто."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Меню закрыто."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Неверный размер."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Ошибка отправки MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Произошла ошибка: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - все логи"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - все {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Загрузить cookie c URL"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Открыть браузер"
    SELECT_BROWSER_MSG = "Выберите браузер для загрузки cookies:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "На этой системе браузеры не найдены. Вы можете загрузить cookies с удаленного URL или мониторить статус браузера:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Открыть браузер</b> - для мониторинга статуса браузера в мини-приложении"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Не удалось выполнить /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Лимит флуда. Попробуйте позже."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Не удалось открыть меню cookie браузера"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Подсказка 'Сохранить как cookie' закрыта."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Использование:</b>\n<code>/link [качество] URL</code>\n\n<b>Примеры:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - лучшее качество\n• /link 720 https://youtube.com/watch?v=... - 720p или ниже\n• /link 720p https://youtube.com/watch?v=... - то же самое\n• /link 4k https://youtube.com/watch?v=... - 4K или ниже\n• /link 8k https://youtube.com/watch?v=... - 8K или ниже</blockquote>\n\n<b>Качество:</b> от 1 до 10000 (например, 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - качество 8K"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Прямая ссылка получена</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Формат:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Аудио поток:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Не удалось получить ссылки на потоки"
    LINK_ERROR_GETTING_MSG = "❌ <b>Ошибка получения ссылки:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Неверный индекс YouTube cookie: {selected_index}. Доступный диапазон 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Загрузка и проверка YouTube cookies...\n\nПопытка {attempt} из {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Загрузка и проверка YouTube cookies...\n\nПопытка {attempt} из {total}\n🔍 Тестирование cookies..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube cookies успешно загружены и валидированы!\n\nИспользован источник {source} из {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Все YouTube cookies истекли или недоступны!\n\nОбратитесь к администратору бота для их замены."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ Превышен лимит попыток перебора YouTube cookies!\n\n🔢 Максимум: {limit} попыток в час\n⏰ Попробуйте позже"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Тег #{wrong} содержит запрещенные символы. Разрешены только буквы, цифры и _.\nПожалуйста, используйте: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Неверный аргумент!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Язык субтитров установлен: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Пример: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Выбранный язык: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Режим 'Всегда спрашивать' {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Субтитры отключены"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Настройки субтитров</b>\n\n{status_text}\n\nВыберите язык субтитров:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - отключить субтитры\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Настройки субтитров</b>\n\n{status_text}\n\nВыберите язык субтитров:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Название:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Длительность:</b> {duration} сек\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Видео поток:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- Максимальное качество 720p\n- Максимальная длительность 1.5 часа\n- Максимальный размер видео 500мб</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️ПРЕДУПРЕЖДЕНИЕ: из-за высокой нагрузки на CPU эта функция очень медленная (почти в реальном времени) и ограничена:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Быстрые команды:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - отключить субтитры\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - включить режим 'Всегда спрашивать'\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - установить язык\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - установить язык с включенным AUTO/TRANS\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - включить режим 'Всегда спрашивать'\n"
    SUBS_AUTO_SUBS_TEXT = " (авто-субтитры)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Режим авто-субтитров {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "Субтитры отключены через команду: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "Режим 'Всегда спрашивать' субтитров включен через команду: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "Язык субтитров установлен через команду: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "Язык субтитров + авто режим установлен через команду: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Пользователь открыл меню /subs."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Пользователь установил язык субтитров: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Пользователь переключил режим AUTO/TRANS: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Пользователь переключил режим 'Всегда спрашивать': {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Пользователь запросил cookies из браузера."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Клавиатура выбора браузера отправлена только с установленными браузерами."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Выбор браузера закрыт."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "Резервный COOKIE_URL использован успешно (источник скрыт)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "Резервный COOKIE_URL не удался: статус={status} (скрыт)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Резервный COOKIE_URL неожиданная ошибка: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Браузер {browser} не установлен."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Cookies сохранены используя браузер: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "Файл cookie сохранен для пользователя {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "Файл cookie существует, имеет правильный формат, и YouTube cookies работают."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Файл cookie существует и имеет правильный формат, но YouTube cookies истекли."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Файл cookie существует и имеет правильный формат."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Файл cookie существует, но имеет неверный формат."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Файл cookie не найден."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "URL cookie {service} пуст для пользователя {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "URL cookie {service} не .txt (скрыт)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "Файл cookie {service} слишком большой: {size} байт (источник скрыт)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "Файл cookie {service} загружен для пользователя {user_id} (источник скрыт)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Скрипт не найден: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Не удалось отправить начальное статусное сообщение"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Ошибка выполнения {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Кэш Firebase перезагружен автоматической задачей."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Кэш Firebase перезагружен администратором."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Ошибка перезагрузки кэша Firebase: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Трансляция инициирована. Текст:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Трансляционное сообщение отправлено всем пользователям."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Не удалось транслировать сообщение: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Администратор {user_id} очистил кэш для URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Администратор {user_id} запустил скрипт обновления списка порно: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Скрипт обновления списка порно успешно завершен администратором {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Скрипт обновления списка порно не удался администратором {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Администратор {user_id} попытался запустить несуществующий скрипт: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Ошибка выполнения скрипта обновления порно администратором {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Администратор {user_id} запустил перезагрузку кэша порно"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Ошибка перезагрузки кэша порно администратором {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Администратор {user_id} проверил URL на NSFW: {url} - Результат: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "Пользователь запросил изменение формата."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "Формат установлен в ALWAYS_ASK."
    FORMAT_UPDATED_BEST_LOG_MSG = "Формат обновлен до лучшего: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "Формат обновлен до ID {format_id}: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "Формат обновлен до ID {format_id} (только аудио): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "Формат обновлен до качества {quality}: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "Формат обновлен до: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "Меню формата отправлено."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "Выбор формата закрыт."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "Подсказка пользовательского формата отправлена."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "Меню разрешения формата отправлено."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "Возврат в главное меню формата."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "Формат обновлен до: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "Формат установлен в ALWAYS_ASK."
    FORMAT_CODEC_SET_LOG_MSG = "Предпочтение кодека установлено в {codec}"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Меню пользовательского формата закрыто"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "Прямая ссылка извлечена для пользователя {user_id} из {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Не удалось извлечь прямую ссылку для пользователя {user_id} из {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Ошибка в команде link для пользователя {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Пользователь {user_id} установил клавиатуру в {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Пользователь {user_id} установил клавиатуру в {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo установлен через команду: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Пользователь открыл меню /mediainfo."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: закрыто."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo включен."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo отключен."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Размер разделения установлен в {size} байт через аргумент."
    SPLIT_MENU_OPENED_LOG_MSG = "Пользователь открыл меню /split."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Выбор разделения закрыт."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Размер разделения установлен в {size} байт."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Прокси установлен через команду: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Пользователь открыл меню /proxy."
    PROXY_MENU_CLOSED_LOG_MSG = "Прокси: закрыто."
    PROXY_ENABLED_LOG_MSG = "Прокси включен."
    PROXY_DISABLED_LOG_MSG = "Прокси отключен."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Сообщение справки закрыто."
    AUDIO_HELP_SHOWN_LOG_MSG = "Показана справка /audio"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Пользователь запросил справку по плейлистам."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Справка по плейлистам закрыта."
    AUDIO_HINT_CLOSED_LOG_MSG = "Подсказка по аудио закрыта."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Меню прямой ссылки создано через кнопку LINK для пользователя {user_id} из {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Не удалось извлечь прямую ссылку через кнопку LINK для пользователя {user_id} из {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "Команда LIST выполнена для пользователя {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Быстрая вставка: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Меню 'Всегда спрашивать' отправлено для {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Создано меню кэшированных качеств для пользователя {user_id} после ошибки: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Ошибка меню 'Всегда спрашивать' для {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Формат зафиксирован через настройки /args"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Аудио"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Видео"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Видео"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Далее ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Предыд."
    SUBTITLES_NEXT_BUTTON_MSG = "Далее ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Все текстовые поля пусты"
    SENDER_VIDEO_DURATION_MSG = "Длительность видео:"
    SENDER_UPLOADING_FILE_MSG = "📤 Загрузка файла..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Загрузка видео..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Длительность видео:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 файл загружен."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Информация о видео"
    DOWN_UP_NUMBER_MSG = "Номер"
    DOWN_UP_TITLE_MSG = "Название"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Видео скачано."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Обработка для загрузки..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Часть {part} разделенного файла загружена"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Загрузка завершена"
    DOWN_UP_FILES_UPLOADED_MSG = "файлов загружено"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Закрыть"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼КОДЕК"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 ДУБЛЯЖ"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 СУБТИТРЫ"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Браузер"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Получение прямой ссылки..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Получение доступных форматов..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Получение описания видео..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Ошибка получения описания: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Описание видео недоступно"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Ошибка отправки описания: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Описание видео отправлено пользователю {user_id} для {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Запуск gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Длительность:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Формат:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Браузер:</b> Открыть в веб-браузере"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Доступные форматы для"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Как использовать ID форматов:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "После получения списка используйте конкретный ID формата:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - скачать формат 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - то же самое"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - скачать формат 140 как MP3 аудио"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Обнаружены только аудио форматы"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Эти форматы будут скачаны как MP3 аудио файлы."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Как установить формат:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Скачать конкретный ID формата"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Скачать по качеству"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Скачать лучшее качество"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Всегда спрашивать качество"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Только аудио форматы:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Скачать формат 140 как MP3 аудио"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Эти будут скачаны как MP3 аудио файлы."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Используйте ID формата из списка выше"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Ошибка: Исходное сообщение не найдено."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Страница форматов"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Ошибка показа меню форматов"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Ошибка получения форматов"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Ошибка получения доступных форматов."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Пожалуйста, попробуйте позже."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp не может обработать этот контент"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Система рекомендует использовать gallery-dl вместо этого."
    ALWAYS_ASK_OPTIONS_MSG = "**Опции:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Для галерей изображений: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Для отдельных изображений: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl часто работает лучше для Instagram, Twitter и другого контента социальных сетей."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Попробовать Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Формат зафиксирован через /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Субтитры"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Дублированное аудио"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Субтитры доступны"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Выберите язык субтитров"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Субтитры не найдены и не будут встроены"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Мгновенный репост из кэша"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Выберите язык аудио"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW платный (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Выберите качество загрузки"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Скачать изображение (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Смотреть видео в poketube"  # ВРЕМЕННО ОТКЛЮЧЕНО: сервис poketube упал
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Получить прямую ссылку на видео"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Показать список доступных форматов"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Изменить расширение/кодек видео"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Встроить"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Извлечь только аудио"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW платный (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Мгновенный репост из кэша"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Смотреть видео в poketube"  # ВРЕМЕННО ОТКЛЮЧЕНО: сервис poketube упал
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Выбрать язык аудио"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Лучшее"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Другое"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝только субтитры"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Умная группировка"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Добавлен ряд кнопок действий (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Добавлены ряды кнопок действий (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Добавлены нижние кнопки к существующему ряду"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Создан новый нижний ряд"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "В плейлисте не найдено видео"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "Неподдерживаемый URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Не удалось найти видео"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Видео не найдено"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Медиа не найдено"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Этот твит не содержит"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Ошибка получения информации о видео:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Ошибка получения информации о видео"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Попробуйте команду <code>/clean</code> и попробуйте снова. Если ошибка сохраняется, YouTube требует авторизации. Обновите cookies.txt через <code>/cookie</code> или <code>/cookies_from_browser</code> и попробуйте снова."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Меню закрыто."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Ручной выбор качества"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Выберите качество вручную, поскольку автоматическое определение не удалось:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Все доступные форматы"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Доступные качества (из кэша)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Используются кэшированные качества - новые форматы могут быть недоступны"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Скачивание формата"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Скачивание"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Скачивание с отслеживанием прогресса..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Скачивание с использованием формата:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Скачивание аудио с использованием формата:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Скачивание лучшего качества..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Скачивание дампа базы данных..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Скачивание"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Страница форматов"
    ALWAYS_ASK_FROM_CACHE_MSG = "(из кэша)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Ошибка: Исходное сообщение не найдено. Возможно, оно было удалено. Пожалуйста, отправьте ссылку снова."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Ошибка: Исходный URL не найден. Пожалуйста, отправьте ссылку снова."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Прямая ссылка получена</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Название:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Длительность:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Формат:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Видео поток:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Аудио поток:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Не удалось получить ссылки на потоки"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Прямая ссылка извлечена через меню 'Всегда спрашивать' для пользователя {user_id} из {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Не удалось извлечь прямую ссылку через меню 'Всегда спрашивать' для пользователя {user_id} из {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Прямая ссылка извлечена через down_and_up_with_format для пользователя {user_id} из {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Не удалось извлечь прямую ссылку через down_and_up_with_format для пользователя {user_id} из {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Прямая ссылка извлечена через down_and_audio для пользователя {user_id} из {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Не удалось извлечь прямую ссылку через down_and_audio для пользователя {user_id} из {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Аудио отправлено из кэша."
    AUDIO_PROCESSING_MSG = "🎙️ Аудио обрабатывается..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Скачивание аудио:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Произошла ошибка во время скачивания аудио."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Не удалось извлечь информацию об аудио"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Пропуск неподдерживаемого типа файла в плейлисте по индексу {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "Аудио файл не найден после скачивания."
    AUDIO_FILE_SIZE_ZERO_MSG = "❌ Не удалось отправить аудио: Размер файла равен 0 B (индекс плейлиста {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ Аудио файл все еще скачивается, пожалуйста, подождите..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Загрузка аудио файла...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Не удалось отправить аудио: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Аудио плейлиста отправлено: {sent}/{total} файлов (качество={quality}) пользователю {user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Не удалось скачать аудио: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Скачивание отменено из-за таймаута (2 часа)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Видео файл не найден: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ Не удалось отправить видео: Размер файла равен 0 B (индекс плейлиста {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ Видео файл все еще скачивается, пожалуйста, подождите..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Ошибка обработки видео: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Ошибка отправки файла описания: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 если вы хотите изменить подпись к видео - ответьте на видео новым текстом</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Субтитры не обнаружены"
    VIDEO_PROGRESS_MSG = "<b>Видео:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Аудио:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>Ссылка:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ Превышен лимит ссылок: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Обработка завершена"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Диапазоны плейлистов не разрешены при множественной загрузке. Отправьте только одиночные ссылки без диапазонов (*1*5, /vid 1-10 и т.д.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Проверьте <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>здесь</a>, поддерживается ли ваш сайт"
    ERROR_COOKIE_NEEDED_MSG = "Возможно, вам нужен <code>cookie</code> для скачивания этого видео. Сначала очистите рабочее пространство командой <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Для YouTube - получите <code>cookie</code> командой <b>/cookie</b>. Для любого другого поддерживаемого сайта - отправьте свой собственный cookie (<a href='https://t.me/tg_ytdlp/203'>руководство1</a>) (<a href='https://t.me/tg_ytdlp/214'>руководство2</a>) и после этого отправьте ссылку на видео снова."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Выберите язык субтитров"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Нет альтернативных языков аудио"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Выберите язык аудио"
    PAGE_NUMBER_MSG = "Страница {page}"
    TOTAL_PROGRESS_MSG = "Общий прогресс"
    SUBTITLE_MENU_CLOSED_MSG = "Меню субтитров закрыто."
    SUBTITLE_LANGUAGE_SET_MSG = "Язык субтитров установлен: {value}"
    AUDIO_SET_MSG = "Аудио установлено: {value}"
    FILTERS_UPDATED_MSG = "Фильтры обновлены"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Назад"
    CLOSE_BUTTON_TEXT = "🔚Закрыть"
    LIST_BUTTON_TEXT = "📃Список"
    IMAGE_BUTTON_TEXT = "🖼Изображение"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Качества не определены автоматически\nИспользуйте кнопку 'Другое' чтобы увидеть все доступные форматы.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Обнаружена прямая трансляция**\n\nСкачивание текущих или бесконечных прямых трансляций не разрешено.\n\nПожалуйста, дождитесь окончания трансляции и попробуйте скачать снова, когда:\n• Длительность трансляции известна\n• Трансляция завершена\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Скачивание прямой трансляции</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Часть {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Макс. размер: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Общая длительность: {duration} сек"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Прямая трансляция - Часть {chunk}</b>\n⏱ Длительность: {duration} сек\n📦 Размер: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Часть {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Скачивание прямой трансляции завершено</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "Скачано частей: {chunks}"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Общая длительность: {duration} сек"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Скачивание прямой трансляции остановлено</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Директория пользователя была удалена (вероятно, командой /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "Файл части был удален (вероятно, командой /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Трансляция завершена"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Пожалуйста, выберите другой формат используя команду `/format`."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Прямая ссылка получена</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Название:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Длительность:</b> {duration} сек\n"
    FORMAT_FIELD_MSG = "🎛 <b>Формат:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Видео поток:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Аудио поток:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Ошибка обработки файла**\n\nВидео было скачано, но не может быть обработано из-за недопустимых символов в имени файла.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Ошибка обработки файла**\n\nВидео было скачано, но не может быть обработано из-за ошибки недопустимого аргумента.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Причина:**\n"
        "• Загруженный файл не является видео файлом\n"
        "• Возможно, это документ (PDF, DOC и т.д.) или архив\n\n"
        "**Решение:**\n"
        "• Проверьте ссылку - возможно, она ведет на документ, а не на видео\n"
        "• Попробуйте другую ссылку или источник\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Причина:**\n"
        "• Файл не может быть обработан как видео\n"
        "• Возможно, это не видео файл или файл поврежден\n\n"
        "**Решение:**\n"
        "• Проверьте ссылку - возможно, она ведет на документ, а не на видео\n"
        "• Попробуйте другую ссылку или источник\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Формат недоступен**\n\nЗапрошенный формат видео недоступен для этого видео.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ ID формата {format_id} не найден для этого видео.\n\nДоступные ID форматов: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **Формат AV1 недоступен для этого видео.**\n\n**Доступные форматы:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Ошибка обработки файла**\n\nАудио было скачано, но не может быть обработано из-за недопустимых символов в имени файла.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Ошибка обработки файла**\n\nАудио было скачано, но не может быть обработано из-за ошибки недопустимого аргумента.\n\n"
    
    # Keyboard Buttons
    CLEAN_EMOJI = "🧹"
    COOKIE_EMOJI = "🍪" 
    SETTINGS_EMOJI = "⚙️"
    PROXY_EMOJI = "🌐"
    IMAGE_EMOJI = "🖼"
    SEARCH_EMOJI = "🔍"
    VIDEO_EMOJI = "📼"
    USAGE_EMOJI = "📊"
    SPLIT_EMOJI = "✂️"
    AUDIO_EMOJI = "🎧"
    SUBTITLE_EMOJI = "💬"
    LANGUAGE_EMOJI = "🌎"
    TAG_EMOJI = "#️⃣"
    HELP_EMOJI = "🆘"
    LIST_EMOJI = "📃"
    PLAY_EMOJI = "⏯️"
    KEYBOARD_EMOJI = "🎹"
    LINK_EMOJI = "🔗"
    ARGS_EMOJI = "🧰"
    NSFW_EMOJI = "🔞"
    LIST_EMOJI = "📃"
    
    # NSFW Content Messages
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Пользователь ввел запрещенный контент. Не может быть скачан."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "Размытие NSFW установлено через команду: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Пользователь открыл меню /nsfw."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: закрыто."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Не удалось загрузить cookie {service}: статус={status} (url скрыт)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Ошибка загрузки cookie {service}: {error} (url скрыт)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Неожиданная ошибка при загрузке cookie {service} (url скрыт): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Файл cookie обновлен для пользователя {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Недействительное содержимое cookie предоставлено пользователем {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "URL YouTube cookie пусты для пользователя {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "YouTube cookies загружены и валидированы для пользователя {user_id} из источника {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Все источники YouTube cookie не удались для пользователя {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Ошибка в команде check_porn администратором {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Размер части разделения установлен в {size} байт."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Загрузка видео завершена с разделением файла."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Видео плейлиста отправлены: {sent}/{total} файлов (качество={quality}) пользователю {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Неизвестная ошибка: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Пропуск неподдерживаемого типа файла в плейлисте по индексу {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg не найден. Пожалуйста, установите FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Конвертация в MP4 не удалась: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Встраивание субтитров может занять много времени (до 1 мин на 1 мин видео)!\n🔥 Начинаем вжигание субтитров..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Субтитры не могут быть встроены из-за лимитов (качество/длительность/размер)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Субтитры недоступны для выбранного языка"
    ERROR_SENDING_VIDEO_MSG = "❌ Ошибка отправки видео: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Видео плейлиста отправлены: {sent}/{total} файлов."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Скачивание отменено из-за таймаута (2 часа)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Не удалось скачать видео: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Ошибка: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON должен быть объектом (словарем)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Неверный формат JSON. Пожалуйста, предоставьте действительный JSON."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Значение должно быть между {min_val} и {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} установлено в: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Истина"
    ARGS_FALSE_BUTTON_MSG = "❌ Ложь"
    ARGS_BACK_BUTTON_MSG = "🔙 Назад"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Закрыть"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Истина"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Ложь"
    ARGS_NOT_SET_MSG = "Не установлено"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["Да", "да", "True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["Нет", "нет", "False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ Формат AV1 недоступен для этого видео.\n\nДоступные форматы:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Ошибка скачивания: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ В плейлисте не найдено видео по индексу {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Конвертация видео не удалась**\n\nВидео не может быть конвертировано в MP4 из-за ошибки недопустимого аргумента.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Конвертация видео не удалась**\n\nВидео не может быть конвертировано в MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Не удалось получить ссылки на потоки"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Ошибка получения ссылки:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ Контент не найден по индексу {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Ошибка: Исходное сообщение не найдено."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Ошибка: URL не найден."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Этот URL не может быть встроен."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ Кодек {codec} недоступен для этого видео"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ Формат {format} недоступен для этого видео"
    
    # Always Ask Menu button texts
    AA_AVC_BUTTON_MSG = "✅ AVC"
    AA_AVC_BUTTON_INACTIVE_MSG = "☑️ AVC"
    AA_AVC_BUTTON_UNAVAILABLE_MSG = "❌ AVC"
    AA_AV1_BUTTON_MSG = "✅ AV1"
    AA_AV1_BUTTON_INACTIVE_MSG = "☑️ AV1"
    AA_AV1_BUTTON_UNAVAILABLE_MSG = "❌ AV1"
    AA_VP9_BUTTON_MSG = "✅ VP9"
    AA_VP9_BUTTON_INACTIVE_MSG = "☑️ VP9"
    AA_VP9_BUTTON_UNAVAILABLE_MSG = "❌ VP9"
    AA_MP4_BUTTON_MSG = "✅ MP4"
    AA_MP4_BUTTON_INACTIVE_MSG = "☑️ MP4"
    AA_MP4_BUTTON_UNAVAILABLE_MSG = "❌ MP4"
    AA_MKV_BUTTON_MSG = "✅ MKV"
    AA_MKV_BUTTON_INACTIVE_MSG = "☑️ MKV"
    AA_MKV_BUTTON_UNAVAILABLE_MSG = "❌ MKV"

    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Лимит флуда. Попробуйте позже."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Проверить Cookie"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ АВТО (по ошибке YouTube)"
    PROXY_OFF_BUTTON_MSG = "❌ ВЫКЛ"
    PROXY_CLOSE_BUTTON_MSG = "🔚Закрыть"

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Выбор страны:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Сбросить выбор страны"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Выбрана страна: {country} (код: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Доступно прокси: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Бот будет пробовать сначала HTTP, затем SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Прокси автоматически включен для выбранной страны"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Выбор страны сброшен"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Выбор страны сброшен"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Выбрана страна: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Используется страна из файла: {country}"
    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Доступно стран из файла: {count}"
    PROXY_COUNTRY_NOT_AVAILABLE_MSG = "❌ Прокси для этой страны недоступны. Попробуйте другую страну."
    PROXY_COUNTRY_SET_BY_COMMAND_MSG = "✅ Прокси установлен: страна {country} (код: {country_code})"
    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 Выбрана страна: {country} (код: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ Прокси включен для этой страны"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ Прокси выключен (нажмите ALL (AUTO) для включения)"
    
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ ВКЛ"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ ВЫКЛ"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Закрыть"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV: ВКЛ"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV: ВЫКЛ"
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ ВКЛ (Без размытия)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ВКЛ (Без размытия)"
    NSFW_OFF_BLUR_MSG = "✅ ВЫКЛ (Размытие)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ ВЫКЛ (Размытие)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Чистый"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Ошибка обработки ответного сообщения для пользователя {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Ошибка отправки трансляции пользователю {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Логи {bot_name}\nПользователь: {user_id}\nВсего логов: {total}\nТекущее время: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nВсего {path}: {count}\nТекущее время: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Всего пользователей: {count}</i>\nПоследние 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Кэши порно перезагружены администратором {admin_id}. Домены: {domains}, Ключевые слова: {keywords}, Сайты: {sites}, БЕЛЫЙ СПИСОК: {whitelist}, СЕРЫЙ СПИСОК: {greylist}, ЧЕРНЫЙ СПИСОК: {black_list}, БЕЛЫЕ КЛЮЧЕВЫЕ СЛОВА: {white_keywords}, ПРОКСИ ДОМЕНЫ: {proxy_domains}, ПРОКСИ_2_ДОМЕНЫ: {proxy_2_domains}, ЧИСТЫЙ ЗАПРОС: {clean_query}, БЕЗ_КУКИ_ДОМЕНЫ: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Ошибка отправки сообщения о таймауте: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Выберите язык</b>"
    LANG_CHANGED_MSG = "✅ Язык изменен на {lang_name}"
    LANG_ERROR_MSG = "❌ Ошибка изменения языка"
    LANG_CLOSED_MSG = "Выбор языка закрыт"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[БРАУЗЕР] callback: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Добавление кнопки мониторинга браузера с URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "URL мониторинга браузера не настроен: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Настройка клавиатуры обновлена!**\n\nНовая настройка: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Не удалось скрыть клавиатуру: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Используются рабочие YouTube cookies для извлечения ссылки для пользователя {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Нет рабочих YouTube cookies для извлечения ссылки для пользователя {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Используются существующие YouTube cookies для извлечения ссылки для пользователя {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "YouTube cookies не найдены для извлечения ссылки для пользователя {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Глобальный файл cookie скопирован в папку пользователя {user_id} для извлечения ссылки"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Пользователь {user_id} запросил команду mediainfo"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Пользователь {user_id} администратор: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Пользователь {user_id} в канале: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Пользователю {user_id} доступ запрещен - не администратор и не в канале"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Пользователю {user_id} доступ разрешен"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Эта команда доступна только администраторам."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Скачивание завершено с поддержкой PO токена"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Лимит флуда. Попробуйте позже."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ Ошибка обновления REST токена: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Ошибка закрытия сессии Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Ошибка инициализации базовой структуры БД: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Не все параметры установлены в config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL не установлен"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey не установлен для получения idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Ошибка загрузки дампа Firebase: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Не удалось загрузить дамп Firebase через REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Ошибка в _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Ошибка запуска автоматической reload_cache (попытка {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Все попытки повтора не удались"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Начало загрузки дампа Firebase в {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Зависимость недоступна: requests или Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ База данных пуста"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Ошибка закрытия логгера: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Ошибка во время очистки: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Ошибка клонирования: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Таймаут клонирования"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Исключение клонирования: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Обновление отменено пользователем"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Репозиторий успешно клонирован"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Резервные копии перемещены в _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Все модули загружены"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Очистка завершена при выходе"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Получен сигнал {signal}, корректное завершение работы..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Пожалуйста, подождите..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Скачивание HLS потока:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "ожидание фрагментов"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Резервная копия {ts} не найдена в _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Не удалось восстановить {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Восстановлено: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Детали:</b> {error_details}\n\nСкачивание остановлено из-за критической ошибки.\n\n💡 <b>Совет:</b> Если вы получаете ошибку 401 Unauthorized, попробуйте использовать команду <code>/cookie instagram</code> или отправить свои собственные cookies для аутентификации в Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Домен в черном списке порно: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Найдены порно ключевые слова: {keywords}"
    PORN_KEYWORDS_IN_TITLE_MSG = "❌ Ключевые слова в названии: {keywords}"
    PORN_KEYWORDS_IN_DESCRIPTION_MSG = "❌ Ключевые слова в описании: {keywords}"
    PORN_KEYWORDS_IN_CAPTION_MSG = "❌ Ключевые слова в подписи: {keywords}"
    PORN_KEYWORDS_IN_UPLOADER_MSG = "❌ Ключевые слова в имени канала/автора/загрузчика: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Домен в белом списке: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Найдены ключевые слова белого списка: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Порно ключевые слова не найдены"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Ошибка TikTok API по индексу {index}, переход к следующему аудио..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Ошибка TikTok API по индексу {index}, переход к следующему видео..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "Пользователь ввел <b>url</b>\n <b>имя пользователя:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>Пользователь ввел так:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Присоединиться к каналу"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Регистрация обработчика: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Загрузить мои 5 cookies"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Получить YT-cookie из браузера"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Проверить ваш файл cookie"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Загрузить свои cookie"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Закрыть"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Доступные форматы для: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Закрыть"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Закрыть"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Закрыть"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Закрыть"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Справка закрыта."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Закрыто"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Произошла ошибка"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg не найден в PATH или директории проекта. Пожалуйста, установите FFmpeg."
    YTDLP_NOT_FOUND_MSG = "yt-dlp бинарный файл не найден в PATH или директории проекта. Пожалуйста, установите yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Видео будет разделено на {rounds} частей, что может быть избыточно"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Разделение части видео {current}/{total}: {start_time:.2f}с до {end_time:.2f}с"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Не удалось создать часть разделения {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Успешно создана часть разделения {part}: {target_name} ({size} байт)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Ошибка разделения части видео {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Видео успешно разделено на {count} частей"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Ошибка в процессе разделения видео: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Ошибка при обработке видео {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Видео файл не существует: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Ошибка парсинга размеров '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Не удалось определить размеры видео из '{size_result}', используем по умолчанию: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Ошибка создания миниатюры: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Ошибка парсинга длительности видео: {error}, результат был: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Миниатюра не создана в {thumb_dir}, используется по умолчанию"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Ошибка выполнения команды: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Ошибка создания миниатюры с FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Пропуск секции конфигурации не-словарь: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Установка {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Использование пользовательских cookies: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Использование YouTube cookies для пользователя {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Глобальный файл cookie скопирован в папку пользователя {user_id}"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Использование скопированных глобальных cookies как пользовательских: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Не удалось скопировать глобальный файл cookie для пользователя {user_id}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Использование --no-cookies для домена: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Прокси запрошен, но не удалось импортировать/получить конфигурацию: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Принудительное использование прокси для gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Прокси запрошен, но конфигурация прокси неполная"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Помощник прокси не удался: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Парсинг элементов экстрактора..."
    GALLERY_DL_ITEM_COUNT_MSG = "Элемент {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Найдены метаданные (тег 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "Найден URL (тег 3): {url}, метаданные: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Найдены метаданные (устаревшие): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "Найден URL (устаревший): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Найдено имя файла: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Найдена директория: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Найдено расширение: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Распарсено {count} элементов, информация: {info}, резерв: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Установка конфигурации gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Пробуем Стратегию A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "Модуль gallery_dl.extractor не найден"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() недоступен в этой сборке"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Вызов extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Ни один экстрактор не подошел к URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Установка cookies на экстрактор: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Не удалось установить cookies на экстрактор: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Экстрактор найден, вызов items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Стратегия A успешна, получена информация: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Стратегия A: extractor.items() вернул недействительную информацию"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Стратегия A (extractor.find) не удалась: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Резервные метаданные из --get-urls: всего={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Все стратегии не удались для получения метаданных"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Не удалось извлечь информацию об изображении: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "Модуль gallery_dl.job не найден (сломанная установка?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob недоступен в этой сборке"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Поиск скачанных файлов в директории gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Попытка найти файлы по именам из экстрактора"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Ошибка чтения аргументов пользователя для {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Ошибка при обработке видео{video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "У пользователя {user_id} включена отправка как файл, отправляем как документ"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video таймаут повторно; переходим к send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Подпись слишком длинная, пробуем с минимальной подписью"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (минимальная подпись) таймаут; переходим к send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Ошибка отправки видео с минимальной подписью: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Ошибка отправки полного файла описания: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Ошибка удаления временного файла описания: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Ошибка: Не удалось разрезать файл на части\nРазмер файла: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Часть {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Часть {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Часть {part_num}.{subpart_num}"
    
    # YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Пропуск match_filter для домена в NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Проверка существующих YouTube cookies на URL пользователя для определения формата для пользователя {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Существующие YouTube cookies работают на URL пользователя для определения формата для пользователя {user_id} - используем их"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Существующие YouTube cookies не удались на URL пользователя, пытаемся получить новые для определения формата для пользователя {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Пробуем источник YouTube cookie {i} для определения формата для пользователя {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "YouTube cookies из источника {i} работают на URL пользователя для определения формата для пользователя {user_id} - сохранены в папку пользователя"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "YouTube cookies из источника {i} не работают на URL пользователя для определения формата для пользователя {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Не удалось загрузить YouTube cookies из источника {i} для определения формата для пользователя {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Все источники YouTube cookies не удались для определения формата для пользователя {user_id}, попробуем без cookies"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Нет настроенных источников YouTube cookies для определения формата для пользователя {user_id}, попробуем без cookies"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "YouTube cookies не найдены для определения формата для пользователя {user_id}, пытаемся получить новые"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Использование YouTube cookies для определения формата для пользователя {user_id} (уже валидированы в меню Always Ask)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "YouTube cookies не найдены для определения формата для пользователя {user_id}, пытаемся восстановить..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Глобальный файл cookie скопирован в папку пользователя {user_id} для определения формата"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Не удалось скопировать глобальный файл cookie для пользователя {user_id}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Использование --no-cookies для домена в get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "Приложение еще не инициализировано. Нельзя получить доступ к {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Подпись:</b> <code>{caption}</code>\n<b>ID пользователя:</b> <code>{user_id}</code>\n<b>Имя пользователя:</b> <code>{users_name}</code>\n<b>ID видео файла:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Ошибка в caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Неожиданная ошибка в caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL видео</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL отсутствует в конфигурации"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin initialized"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken refreshed"
    DB_LOG_FOR_USER_ADDED_MSG = "Лог для пользователя добавлен"
    DB_DATABASE_CREATED_MSG = "База данных создана"
    DB_BOT_STARTED_MSG = "Бот запущен"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY сохранено в config.py: {hours}ч"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Часть плейлиста уже в кэше: {path_parts}, пропускаем"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: кэш не найден для любого URL/качества варианта, возвращаем пустой словарь"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: быстрый подсчет для большого диапазона: {cached_count} кэшированных видео"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: кэш не найден для хэша {url_hash}, качество {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: кэш не найден для любого варианта URL, возвращаем None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Доступ запрещен. Только администратор."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Автоматическая перезагрузка кэша Firebase обновлена!\n\n📊 Статус: {status}\n⏰ Расписание: каждые {interval} часов с 00:00\n🕒 Следующая перезагрузка: {next_exec} (через {delta_min} минут)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Автоматическая перезагрузка кэша Firebase остановлена!\n\n📊 Статус: ❌ ОТКЛЮЧЕНО\n💡 Используйте /auto_cache on для повторного включения"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Неверный аргумент. Используйте /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Интервал должен быть между 1 и 168 часами"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Не удалось установить интервал"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Интервал автоматической перезагрузки кэша Firebase обновлен!\n\n📊 Статус: ✅ ВКЛЮЧЕНО\n⏰ Расписание: каждые {interval} часов с 00:00\n🕒 Следующая перезагрузка: {next_exec} (через {delta_min} минут)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Автоматическая перезагрузка кэша Firebase запущена!\n\n📊 Статус: ✅ ВКЛЮЧЕНО\n⏰ Расписание: каждые {interval} часов с 00:00\n🕒 Следующая перезагрузка: {next_exec} (через {delta_min} минут)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Автоматическая перезагрузка кэша Firebase остановлена!\n\n📊 Статус: ❌ ОТКЛЮЧЕНО\n💡 Используйте /auto_cache on для повторного включения"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Автоматическая перезагрузка ВКЛЮЧЕНА; следующая в {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Автоматическая перезагрузка ОТКЛЮЧЕНА администратором."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Интервал автоматической перезагрузки установлен на {interval}ч; следующая в {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Автоматическая перезагрузка запущена; следующая в {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Автоматическая перезагрузка остановлена администратором."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Кэш Firebase загружен: {count} корневых узлов"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Файл кэша Firebase не найден, начинаем с пустого кэша: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Не удалось загрузить кэш Firebase: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Кэш Firebase перезагружен: {count} корневых узлов"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Файл кэша Firebase не найден: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Не удалось перезагрузить кэш Firebase: {error}"
    
    # Database user ban messages 
    DB_USER_BANNED_MSG = f"🚫 Вы заблокированы в боте! Для разблокировки обратитесь к {Config.ADMIN_USERNAME}\n<blockquote>P.S. Не покидайте канал - вы будете автоматически заблокированы ⛔️</blockquote>\n🌍Изменить язык /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Видео форматы не найдены. Пробуем загрузчик изображений…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram ограничил отправку сообщений.\n⏳ Пожалуйста, подождите: {time_str}\nДля обновления таймера отправьте URL еще 2 раза."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Нажмите кнопку чтобы скопировать URL потока, затем вставьте его в приложение VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Нажмите кнопку чтобы скопировать URL потока, затем вставьте его в приложение VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Ошибка получения ссылки:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Ошибка отправки файла форматов: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Не удалось получить форматы:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Анализ... (подождите 6 сек)"
    AA_PROCESSING_MSG = "🔎 Анализ..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Тег #{wrong} содержит запрещенные символы. Разрешены только буквы, цифры и _.\nПожалуйста, используйте: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Для работы в группе боту нужны права администратора. Пожалуйста, сделайте бота админом этой группы."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Привет {first_name},\n \n<i>Этот бот🤖 может скачивать любые видео непосредственно в telegram.😊 Для большей информации нажмите <b>/help</b></i> 👈\n\n<blockquote>P.S. Из-за возможного 🔞NSFW контента — скачивание с ☁️<b>облачного хранилища</b>, 📁<b>файлообменников</b>, 🔗<b>сокращателей URL</b> и 🔞<b>порно-сайтов</b> платное! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ НЕ 🗑<b>удаляйте канал @tg_ytdlp и не отписывайтесь от него</b>, НЕ 🤖<b>спамьте боту ссылками/командами</b> — иначе будете автоматически заблокированы ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Нет файлов для удаления."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 Все файлы успешно удалены!\n\nУдаленные файлы:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ ПОДОЖДИТЕ, ПОКА ВАШЕ ПРЕДЫДУЩЕЕ СКАЧИВАНИЕ НЕ ЗАВЕРШИТСЯ"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "Экземпляр приложения равен None в check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict равен None, разрешаем скачивание"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict равен None, разрешаем встраивание субтитров"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: проверка лимитов - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: ключи info_dict: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Встраивание субтитров пропущено: длительность {duration}с превышает лимит {max_duration}с"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Встраивание субтитров пропущено: размер {size_mb:.2f}MB превышает лимит {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Встраивание субтитров пропущено: качество {width}x{height} (мин сторона {min_side}p) превышает лимит {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "плейлист"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Превышен лимит диапазона для {service}: {count} (максимум {max_count}).\n\nИспользуйте одну из этих команд для скачивания максимального количества доступных файлов:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Превышен лимит диапазона для {service}: {count} (максимум {max_count})\nПользователь ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "Провайдер PO токена отключен в конфигурации"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} не является доменом YouTube, пропускаем PO токен"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "Провайдер PO токена недоступен по {base_url}, переходим к стандартному извлечению YouTube"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "Кэш провайдера PO токена очищен, проверим доступность при следующем запросе"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Экземпляр приложения еще недоступен"
    HELPER_USER_NAME_MSG = "Пользователь"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Обнаружен таймер флуда, спим {wait_seconds} секунд"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Обнаружен таймер флуда, но не удалось извлечь время, спим {retry_delay} секунд"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "Обнаружена ошибка msg_seqno, спим {retry_delay} секунд"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Конфигурация прокси неполная, используем прямое соединение"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Закрыть"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Закрыть"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Закрыть"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Файл логов удален."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Файл тегов удален."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Файл формата удален."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Файл разделения удален."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Файл Mediainfo удален."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Настройки субтитров удалены."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Настройки клавиатуры удалены."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Настройки Args удалены."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 Настройки NSFW удалены."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Настройки прокси удалены."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Настройки Flood wait удалены."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Закрыть"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Команда скачивания видео"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Использование: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Примеры:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (прямой порядок)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (обратный порядок)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Также смотрите: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Пользователь {user_id} закрыл команду add_bot_to_group"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Не удалось извлечь YouTube ID"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Не удалось загрузить миниатюру или она слишком большая"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Выберите язык аудио"
    AA_NO_SUBTITLES_DETECTED_MSG = "Субтитры не обнаружены"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Выберите язык субтитров"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Ошибка аутентификации"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Аккаунт не найден"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Аккаунт недоступен"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Превышен лимит запросов"
    GALLERY_DL_NETWORK_ERROR_MSG = "Ошибка сети"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Контент недоступен"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Географические ограничения"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Требуется проверка"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Нарушение политики"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Неизвестная ошибка"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Скачивание началось</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Закрыть"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Команда скачивания видео</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Использование: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Примеры:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Также смотрите: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Лимит флуда. Попробуйте позже."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Использование команды Cookie</b>

<code>/cookie</code> - Показать меню cookie
<code>/cookie youtube</code> - Загрузить YouTube cookies
<code>/cookie instagram</code> - Загрузить Instagram cookies
<code>/cookie tiktok</code> - Загрузить TikTok cookies
<code>/cookie x</code> или <code>/cookie twitter</code> - Загрузить Twitter/X cookies
<code>/cookie facebook</code> - Загрузить Facebook cookies
<code>/cookie custom</code> - Показать инструкции по пользовательским cookies

<i>Доступные сервисы зависят от конфигурации бота.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Файл cookie удален и кэш очищен."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Предыд."
    SUBS_BACK_BUTTON_MSG = "🔙Назад"
    SUBS_OFF_BUTTON_MSG = "🚫 ВЫКЛ"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - установить язык"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - установить язык с AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Допустимые опции:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 ЯЗЫК"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 GitHub автора"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 GitHub разработчика"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 ОЧИСТКА"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIES"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 МЕДИА"
    SETTINGS_INFO_BUTTON_MSG = "📖 ИНФО"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ ЕЩЕ"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Только cookies"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Логи "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Теги"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Формат"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Разделение"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Субтитры"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Клавиатура"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Аргументы"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Прокси"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Таймер флуда"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Все файлы"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Загрузить мои 5 cookies"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Получить YT-cookie из браузера"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Проверить ваш файл cookie"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Загрузить свои cookie"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Изменить качество и формат"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Включить/выключить MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Изменить размер части разделения видео"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Скачать видео как аудио"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Настройки языка субтитров"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Как скачивать плейлисты"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Скачивать изображения через gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Показать ваши #теги"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Получить инструкции"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Показать ваши логи"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Справка по плейлистам"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - инструкция"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Получить прямые ссылки на видео"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Включить/выключить прокси"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Раскладка клавиатуры"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Помощник встроенного поиска"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - аргументы yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - Настройки размытия NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Опции очистки</b>\n\nВыберите, что очистить:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Мобильный: Активировать @vid поиск"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Мобильный: Активировать @vid поиск"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 ВЫКЛ"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 ПОЛНАЯ"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL изображений]({url})"
    IMAGE_ERROR_MSG = "❌ Ошибка: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Назад"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - пользовательский формат"
    FORMAT_720P_MSG = "• <code>/format 720</code> - качество 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - качество 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - качество 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - конкретный ID формата"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - всегда показывать меню"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/лучшее качество"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Всегда спрашивать (меню + кнопки)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Другие (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (лучшее для PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (лучшее для мобильного Telegram)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (МАКС качество)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Пользовательский (введите свой)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Из браузера"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Ваши собственные"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Режим ввода автоматически закрыт из-за неактивности (5 минут)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Сбросить все"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Посмотреть текущие"
    ARGS_BACK_BUTTON_MSG = "🔙 Назад"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Перешлите это сообщение в избранное, чтобы сохранить эти настройки как шаблон.</i> \n\n<i>Перешлите это сообщение обратно сюда, чтобы применить эти настройки.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Текущие аргументы yt-dlp:\n\nНет настроенных пользовательских настроек.\n\n---\n\n<i>Перешлите это сообщение в избранное, чтобы сохранить эти настройки как шаблон.</i> \n\n<i>Перешлите это сообщение обратно сюда, чтобы применить эти настройки.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Текущие аргументы yt-dlp:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Экспорт настроек"
    ARGS_SETTINGS_READY_MSG = "Настройки готовы к экспорту! Перешлите это сообщение в избранное для сохранения."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Текущие аргументы yt-dlp:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Не удалось распознать настройки в сообщении. Убедитесь, что вы отправили правильный шаблон настроек."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Настройки успешно импортированы!\n\nПримененные параметры: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Ключевые настройки:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Ошибка сохранения импортированных настроек."
    ARGS_ERROR_IMPORTING_MSG = "❌ Произошла ошибка при импорте настроек."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Загрузка файлов Cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Выберите сервис для загрузки файла cookie."
    COOKIE_MENU_SAVE_INFO_MSG = "Файлы cookie будут сохранены как cookie.txt в вашей папке."
    COOKIE_MENU_TIP_HEADER_MSG = "Tip: Вы также можете использовать прямую команду:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – загрузить и проверить cookies"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – использовать конкретный источник по индексу (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Затем проверьте с помощью <code>/check_cookie</code> (тестирует на RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Всегда Спрашивать"
    SUBS_AUTO_TRANS_BUTTON_MSG = "АВТО/ПЕРЕВОД"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Ссылка"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Смотреть"  # ВРЕМЕННО ОТКЛЮЧЕНО: сервис poketube упал
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Описание"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ ОБРЕЗКА"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Обрезка видео</b>\n\nДлительность видео: <b>{start_time} - {end_time}</b>\n\nПожалуйста, отправьте желаемый диапазон времени в формате:\n<code>ЧЧ:ММ:СС-ЧЧ:ММ:СС</code>\n\nПример: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Неверный формат. Используйте: <code>ЧЧ:ММ:СС-ЧЧ:ММ:СС</code>\n\nПример: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Неверный диапазон. Время начала должно быть меньше времени окончания."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ Диапазон времени выходит за границы видео.\n\nДлительность видео: <b>{start_time} - {end_time}</b>\n\nВаш диапазон должен быть в пределах этих границ."
    AA_ERROR_VIDEO_DURATION_UNKNOWN_MSG = "❌ Не удалось определить длительность видео. Попробуйте еще раз или используйте другое видео."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>Видео будет обрезано:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Частично завершено - {successful_uploads}/{total_files} аудио файлов загружено."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Аудио успешно скачано и отправлено - {total_files} файлов загружено."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Приватный TikTok аккаунт</b>\n\n"
        "Этот TikTok аккаунт приватный или все видео приватные.\n\n"
        "<b>💡 Решение:</b>\n"
        "1. Подпишитесь на аккаунт @{username}\n"
        "2. Отправьте боту свои cookies через команду <code>/cookie</code>\n"
        "3. Попробуйте снова\n\n"
        "<b>После обновления cookies попробуйте снова!</b>"
    )

    #######################################################
