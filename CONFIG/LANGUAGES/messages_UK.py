# Messages Configuration
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# Removed circular import
from CONFIG.config import Config

class Messages(object):
    #######################################################
    # Messages and errors
    #######################################################
    CREDITS_MSG = "<blockquote><i>Керується</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Змінити мову: /lang</b>"
    TO_USE_MSG = "<i>Щоб використовувати цього бота, потрібно підписатися на канал Telegram @tg_ytdlp.</i>\nПісля приєднання до каналу <b>надішліть знову посилання на відео — бот завантажить його для вас</b> ❤️\n\n<blockquote>P.S. Через можливий 🔞NSFW контент — завантаження з ☁️<b>хмарного сховища</b>, 📁<b>обміну файлами</b>, 🔗<b>скорочувачів URL</b> та 🔞<b>порно-сайтів</b> платне! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ НЕ 🗑<b>видаляйте/не відписуйтесь від каналу @tg_ytdlp</b> і НЕ 🤖<b>надсилайте зайвого спаму URL/командами боту</b> — вас автоматично заблокують ⛔️</blockquote>"

    ERROR1 = "Посилання URL не знайдено. Будь ласка, введіть URL з <b>https://</b> або <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Плейлисти (yt-dlp)</b>

Для завантаження плейлистів надішліть їх URL з діапазонами <code>*start*end</code> в кінці. Наприклад: <code>URL*1*5</code> (перші 5 відео з 1 по 5 включно).<code>URL*-1*-5</code> (останні 5 відео з 1 по 5 включно).
Або ви можете використовувати <code>/vid ВІД-ДО URL</code>. Наприклад: <code>/vid 3-7 URL</code> (завантажує відео з 3 по 7 включно з початку). <code>/vid -3-7 URL</code> (завантажує відео з 3 по 7 включно з кінця). Також працює для команди <code>/audio</code>.

<b>Приклади:</b>

🟥 <b>Діапазон відео з плейлиста YouTube:</b> (потрібні 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(завантажує перші 5 відео з 1 по 5 включно)
🟥 <b>Одне відео з плейлиста YouTube:</b> (потрібні 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(завантажує лише 3-тє відео)

⬛️ <b>Профіль TikTok:</b> (потрібні ваші 🍪)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(завантажує перші 10 відео з профілю користувача)

🟪 <b>Історії Instagram:</b> (потрібні ваші 🍪)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(завантажує перші 3 історії)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(завантажує перші 10 історій з альбому)

🟦 <b>Відео VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(завантажує перші 3 відео з профілю користувача/групи)

⬛️<b>Канали Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(завантажує відео з 2 по 4 включно з каналу)

🟪 <b>Кліпи Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(завантажує перші 3 кліпи з каналу)

🟦 <b>Групи Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(завантажує перші 2 відео з групи)

🟧 <b>Моделі Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(завантажує перші 2 відео з профілю моделі)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(завантажує перші 3 відео з результатів пошуку за вашим запитом)

і так далі...
див. <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">список підтримуваних сайтів</a>
</blockquote>

<blockquote expandable>🖼 <b>Зображення (gallery-dl)</b>

Використовуйте <code>/img URL</code> для завантаження зображень/фото/альбомів з багатьох платформ.

<b>Приклади:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Діапазони:</b>
<code>/img 11-20 https://example.com/album</code> — елементи 11..20
<code>/img 11- https://example.com/album</code> — з 11 до кінця (або ліміт бота)

<i>Підтримувані платформи включають vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor тощо. Повний список:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">сайти, підтримувані gallery-dl</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Бот Завантаження Відео - Довідка</b>

📥 <b>Основне Використання:</b>
• Надішліть будь-яке посилання → бот завантажить його
  <i>бот автоматично намагається завантажувати відео через yt-dlp та зображення через gallery-dl.</i>
• <b>Кілька URL:</b> У режимі вибору якості (<code>/format</code>) ви можете надіслати до <b>10 URL</b> в одному повідомленні. Кожен URL на новому рядку або розділений пробілами.
• <code>/audio URL</code> → витягти аудіо
• <code>/link [quality] URL</code> → отримати прямі посилання
• <code>/proxy</code> → увімкнути/вимкнути проксі для всіх завантажень
• Відповісти на відео текстом → змінити підпис

📋 <b>Плейлисти та Діапазони:</b>
• <code>URL*1*5</code> → завантажити перші 5 відео
• <code>URL*-1*-5</code> → завантажити останні 5 відео
• <code>/vid 3-7 URL</code> → стає <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → стає <code>URL*-3*-7</code>

🍪 <b>Куки та Приватні:</b>
• Завантажити *.txt cookie для приватних відео
• <code>/cookie [service]</code> → завантажити куки (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → вибрати джерело за індексом (1–N)
• <code>/cookies_from_browser</code> → витягти з браузера
• <code>/check_cookie</code> → перевірити cookie
• <code>/save_as_cookie</code> → зберегти текст як cookie

🧹 <b>Очищення:</b>
• <code>/clean</code> → лише медіафайли
• <code>/clean all</code> → все
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Налаштування:</b>
• <code>/settings</code> → меню налаштувань
• <code>/format</code> → якість та формат
• <code>/split</code> → розділити відео на частини
• <code>/mediainfo on/off</code> → інформація про медіа
• <code>/nsfw on/off</code> → розмиття NSFW
• <code>/tags</code> → переглянути збережені теги
• <code>/sub on/off</code> → субтитри
• <code>/keyboard</code> → клавіатура (OFF/1x3/2x3)

🏷️ <b>Теги:</b>
• Додати <code>#tag1#tag2</code> після URL
• Теги з'являються в підписах
• <code>/tags</code> → переглянути всі теги

🔗 <b>Прямі Посилання:</b>
• <code>/link URL</code> → найкраща якість
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → конкретна якість

⚙️ <b>Швидкі Команди:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → встановити якість
• <code>/keyboard off/1x3/2x3/full</code> → макет клавіатури
• <code>/split 100mb-2000mb</code> → змінити розмір частини
• <code>/subs off/ru/en auto</code> → мова субтитрів
• <code>/list URL</code> → список доступних форматів
• <code>/mediainfo on/off</code> → увімкнути/вимкнути інформацію про медіа
• <code>/proxy on/off</code> → увімкнути/вимкнути проксі для всіх завантажень

📊 <b>Інформація:</b>
• <code>/usage</code> → історія завантажень
• <code>/search</code> → вбудований пошук через @vid

🖼 <b>Зображення:</b>
• <code>URL</code> → завантажити URL зображень
• <code>/img URL</code> → завантажити зображення з URL
• <code>/img 11-20 URL</code> → завантажити конкретний діапазон
• <code>/img 11- URL</code> → завантажити з 11-го до кінця

👨‍💻 <i>Розробник:</i> @upekshaip
🤝 <i>Учасник:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Просто збережіть ваш cookie як <b><u>cookie.txt</u></b> і надішліть його боту як документ.\n\n"
        "Ви також можете надіслати куки як звичайний текст за допомогою команди <b><u>/save_as_cookie</u></b>.\n"
        "<b>Використання <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>Інструкції:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message
    SEARCH_MSG = """
🔍 <b>Пошук відео</b>

Натисніть кнопку нижче, щоб активувати вбудований пошук через @vid.

<blockquote>На ПК просто введіть <b>"@vid Your_Search_Query"</b> в будь-якому чаті.</blockquote>
    """
    
    # Settings and Hints
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Команда Завантаження Зображень</b>\n\n"
        "Використання: <code>/img URL</code>\n\n"
        "<b>Приклади:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Підтримувані платформи (приклади):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor тощо — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">повний список</a></blockquote>"
        "Також див.: "
    )
    
    LINK_HINT_MSG = (
        "Отримайте прямі посилання на відео з вибором якості.\n\n"
        "Використання: /link + URL \n\n"
        "(напр. /link https://youtu.be/abc123)\n"
        "(напр. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Додати Бота до Групи</b>

Додайте моїх ботів до ваших груп, щоб отримати розширені функції та вищі ліміти!
————————————
📊 <b>Поточні БЕЗКОШТОВНІ Ліміти (в DM Бота):</b>
<blockquote>•🗑 Безлад з усіх файлів невідсортованих 👎
• Макс. розмір 1 файлу: <b>8 GB </b>
• Макс. якість 1 файлу: <b>НЕОБМЕЖЕНО</b>
• Макс. тривалість 1 файлу: <b>НЕОБМЕЖЕНО</b>
• Макс. кількість завантажень: <b>НЕОБМЕЖЕНО</b>
• Макс. URL в одному повідомленні: <b>10</b> (лише в режимі вибору якості)
• Макс. елементів плейлиста за 1 раз: <b>50</b>
• Макс. відео TikTok за 1 раз: <b>500</b>
• Макс. зображень за 1 раз: <b>1000</b>
• Ліміти швидкості URL: <b>5/хв, 60/год, 1000/день</b>
• Ліміт команд: <b>20/хв</b>
• Макс. час 1 завантаження: <b>2 години</b>
• 🔞 Контент NSFW платний! 1⭐️ = $0.02
• 🆓 ВСІ ІНШІ МЕДІА ПОВНІСТЮ БЕЗКОШТОВНІ
• 📝 Всі логи контенту та кешування до моїх лог-каналів для миттєвого репосту при повторному завантаженні</blockquote>

💬<b>Ці ліміти лише для відео з субтитрами:</b>
<blockquote>• Макс. тривалість відео+субтитри: <b>1.5 години</b>
• Макс. розмір файлу відео+субтитри: <b>500 MB</b>
• Макс. якість відео+субтитри: <b>720p</b></blockquote>
————————————
🚀 <b>Переваги Платної Групи (2️⃣x Ліміти):</b>
<blockquote>•  🗂 Структуроване акуратне сховище медіа, відсортоване за темами 👍
•  📁 Боти відповідають в темі, в якій ви їх викликаєте
•  📌 Автоматичне закріплення повідомлення статусу з прогресом завантаження
•  🖼 Команда /img завантажує медіа як альбоми з 10 елементів
• Макс. розмір 1 файлу: <b>16 GB</b> ⬆️
• Макс. URL в одному повідомленні: <b>20</b> ⬆️ (лише в режимі вибору якості)
• Макс. елементів плейлиста за 1 раз: <b>100</b> ⬆️
• Макс. відео TikTok за 1 раз: 1000 ⬆️
• Макс. зображень за 1 раз: 2000 ⬆️
• Ліміти швидкості URL: <b>10/хв, 120/год, 2000/день</b> ⬆️
• Ліміт команд: <b>40/хв</b> ⬆️
• Макс. час 1 завантаження: <b>4 години</b> ⬆️
• 🔞 Контент NSFW: Безкоштовно з повними метаданими 🆓
• 📢 Не потрібно підписуватися на мій канал для груп
• 👥 Всі учасники групи матимуть доступ до платних функцій!
• 🗒 Немає логів / немає кешу до моїх лог-каналів! Ви можете відхилити копіювання/репост в налаштуваннях групи</blockquote>

💬 <b>2️⃣x ліміти для відео з субтитрами:</b>
<blockquote>• Макс. тривалість відео+субтитри: <b>3 години</b> ⬆️
• Макс. розмір файлу відео+субтитри: <b>1000 MB</b> ⬆️
• Макс. якість відео+субтитри: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Ціни та Налаштування:</b>
<blockquote>• Ціна: <b>$5/місяць</b> за 1 бота в групі
• Налаштування: Зв'яжіться з @iilililiiillliiliililliilliliiil
• Оплата: 💎TON або інші методи💲
• Підтримка: Повна технічна підтримка включена</blockquote>
————————————
Ви можете додати моїх ботів до вашої групи, щоб розблокувати безкоштовний 🔞<b>NSFW</b> та подвоїти (x2️⃣) всі ліміти.
Зв'яжіться зі мною, якщо хочете, щоб я дозволив вашій групі використовувати моїх ботів @iilililiiillliiliililliilliliiil
————————————
💡<b>ПОРАДА:</b> <blockquote>Ви можете зібрати гроші з будь-якою кількістю ваших друзів (наприклад, 100 осіб) і зробити 1 покупку для всієї групи - ВСІ УЧАСНИКИ ГРУПИ МАТИМУТЬ ПОВНИЙ НЕОБМЕЖЕНИЙ ДОСТУП до всіх функцій ботів у цій групі всього за <b>0.05$</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>Режим NSFW: УВІМКНЕНО✅</b>

• Контент NSFW буде відображатися без розмиття.
• Спойлери не застосовуватимуться до медіа NSFW.
• Контент буде видимий одразу

<i>Використовуйте /nsfw off, щоб увімкнути розмиття</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>Режим NSFW: ВИМКНЕНО</b>

⚠️ <b>Розмиття увімкнено</b>
• Контент NSFW буде приховано під спойлером   
• Для перегляду вам потрібно буде натиснути на медіа
• Спойлери застосовуватимуться до медіа NSFW.

<i>Використовуйте /nsfw on, щоб вимкнути розмиття</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Недійсний параметр</b>

Використовуйте:
• <code>/nsfw on</code> - вимкнути розмиття
• <code>/nsfw off</code> - увімкнути розмиття
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Перевірка кешу...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Обробка..."
    DOWNLOADING_MSG = "📥 <b>Завантаження медіа...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Завантаження зображення...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Завантаження завершено</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Завантажено:"
    SENT_STATUS_MSG = "Відправлено:"
    PENDING_TO_SEND_STATUS_MSG = "Очікує відправки:"
    TITLE_LABEL_MSG = "Назва:"
    MEDIA_COUNT_LABEL_MSG = "Кількість медіа:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Завантаження завершено, обробка аудіо..."
    VIDEO_PROCESSING_MSG = "📽 Відео обробляється..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Відправлено з кешу</b>\n\nВідправлені альбоми: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Відео успішно відправлено з кешу."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Відео з плейлиста відправлені з кешу ({cached}/{total} файлів)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} відео відправлено з кешу, завантаження відсутніх..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Відправлено з кешу: {cached}\n🔄 Продовження завантаження..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Не вдалося проаналізувати медіа, продовження з максимально дозволеним діапазоном (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Не вдалося визначити кількість медіа, продовження з максимально дозволеним діапазоном (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Не вдалося визначити загальну кількість медіа, продовження з вказаним діапазоном {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>Недійсний URL</b>\n\nБудь ласка, надайте дійсний URL, що починається з http:// або https://"

    ERROR_OCCURRED_MSG = "❌ <b>Сталася помилка</b>\n\n<code>{url}</code>\n\nПомилка: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Помилка відправки відео: {error}"
    ERROR_UNKNOWN_MSG = "❌ Невідома помилка: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Недостатньо місця на диску для завантаження відео."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Розмір файлу перевищує ліміт {limit} GB. Будь ласка, виберіть менший файл у дозволеному розмірі."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>Не вдалося завантажити відео з усіма доступними проксі</b>\n\nУсі спроби завантаження через проксі завершилися невдачею.\nСпробуйте:\n• Перевірити працездатність проксі\n• Спробувати інший проксі зі списку\n• Завантажити без проксі (якщо можливо)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Помилка отримання посилання:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram обмежив відправку повідомлень.\n⏳ Будь ласка, зачекайте: {time}\nЩоб оновити таймер, надішліть URL знову 2 рази."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram обмежив відправку повідомлень.\n⏳ Будь ласка, зачекайте: \nЩоб оновити таймер, надішліть URL знову 2 рази."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Не вдалося завантажити субтитри"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Прямі Посилання Стріму</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Назва:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Тривалість:</b> {duration} сек\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Помилка: Оригінальне повідомлення не знайдено."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Тег #{tag} містить заборонені символи. Дозволені лише літери, цифри та _.\nБудь ласка, використовуйте: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Відео з плейлиста відправлені: {sent}/{total} файлів."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>Підказка щодо плейлистів</b>

Ви надіслали посилання на плейлист без вказання діапазону. Бот автоматично завантажив перше відео (<code>*1*1</code>).

<b>Щоб завантажити кілька відео з плейлиста, вкажіть діапазон:</b>
• <code>URL*1*5</code> — перші 5 відео (від 1 до 5 включно)
• <code>URL*3*3</code> — лише 3-є відео
• <code>/vid 1-10 URL</code> — альтернативний формат

Дізнатися більше: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ Відправлено з кешу: {cached}/{total} файлів."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Не вдалося отримати посилання стріму"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Виберіть браузер для завантаження куків:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Браузер не знайдено в цій системі. Ви можете завантажити куки з віддаленого URL або відстежити статус браузера:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Відкрити Браузер</b> - для моніторингу статусу браузера в міні-додатку"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Відкрити Браузер"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Завантажити з Віддаленого URL"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Файл cookie YouTube завантажено через запасний файл і збережено як cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Підтримувані браузери не знайдено і COOKIE_URL не налаштовано. Використовуйте /cookie або завантажте cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Резервний URL-адресу COOKIE_URL необхідно вказати у файлі .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Запасний файл cookie занадто великий (>100 КБ)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Джерело cookie fallback недоступне (статус {status}). Спробуйте /cookie або завантажте cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Помилка завантаження резервного файлу cookie. Спробуйте /cookie або завантажте cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Неочікувана помилка під час завантаження файлів cookie."
    BTN_CLOSE = "🔚Закрити"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Недійсне логічне значення"
    ARGS_CLOSED_MSG = "Закрито"
    ARGS_ALL_RESET_MSG = "✅ Всі аргументи скинуто"
    ARGS_RESET_ERROR_MSG = "❌ Помилка при скиданні аргументів"
    ARGS_INVALID_PARAM_MSG = "❌ Недійсний параметр"
    ARGS_BOOL_SET_MSG = "Встановлено на {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "Вже встановлено на {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Недійсне значення вибору"
    ARGS_VALUE_SET_MSG = "Встановлено на {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "Вже встановлено на {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Поточне значення:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Приклади:</b>\n• <code>default</code> - Використовувати стратегію XFF за замовчуванням\n• <code>never</code> - Ніколи не використовувати заголовок XFF\n• <code>US</code> - Код країни Сполучені Штати\n• <code>GB</code> - Код країни Велика Британія\n• <code>DE</code> - Код країни Німеччина\n• <code>FR</code> - Код країни Франція\n• <code>JP</code> - Код країни Японія\n• <code>192.168.1.0/24</code> - IP блок (CIDR)\n• <code>10.0.0.0/8</code> - Приватний діапазон IP\n• <code>203.0.113.0/24</code> - Публічний IP блок\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Примітка:</b> Це замінює опції --geo-bypass. Використовуйте будь-який 2-літерний код країни або IP блок у нотації CIDR.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Приклад:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Будь ласка, надішліть ваше нове значення."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Діапазон:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Будь ласка, надішліть число."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Приклади:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Примітка:</b> Ці заголовки будуть додані до існуючих заголовків Referer та User-Agent.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Поточні Аргументи yt-dlp:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - Перемикачі True/False\n• 📋 <b>Select</b> - Виберіть з опцій\n• 🔢 <b>Numeric</b> - Введення числа\n• 📝🔧 <b>Text</b> - Введення тексту/JSON</blockquote>\n\nЦі налаштування будуть застосовані до всіх ваших завантажень."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "Примусові з'єднання IPv6",
        "force_ipv4": "Примусові з'єднання IPv4", 
        "no_live_from_start": "Не завантажувати стріми наживо з початку",
        "live_from_start": "Завантажувати стріми наживо з початку",
        "no_check_certificates": "Придушити перевірку сертифікатів HTTPS",
        "check_certificate": "Перевірити SSL сертифікат",
        "no_playlist": "Завантажувати лише одне відео, не плейлист",
        "embed_metadata": "Вбудувати метадані в файл відео",
        "embed_thumbnail": "Вбудувати мініатюру в файл відео",
        "write_thumbnail": "Записати мініатюру в файл",
        "ignore_errors": "Ігнорувати помилки завантаження та продовжувати",
        "legacy_server_connect": "Дозволити з'єднання з серверами legacy",
        "concurrent_fragments": "Кількість одночасних фрагментів для завантаження",
        "xff": "Стратегія заголовка X-Forwarded-For",
        "user_agent": "Заголовок User-Agent",
        "impersonate": "Персоніфікація браузера",
        "referer": "Заголовок Referer",
        "geo_bypass": "Обійти географічні обмеження",
        "hls_use_mpegts": "Використовувати MPEG-TS для HLS",
        "no_part": "Не використовувати файли .part",
        "no_continue": "Не відновлювати часткові завантаження",
        "audio_format": "Формат аудіо",
        "video_format": "Формат відео",
        "merge_output_format": "Формат виводу злиття",
        "send_as_file": "Відправити як файл",
        "username": "Ім'я користувача",
        "password": "Пароль",
        "twofactor": "Код двофакторної аутентифікації",
        "min_filesize": "Мінімальний розмір файлу (MB)",
        "max_filesize": "Максимальний розмір файлу (MB)",
        "playlist_items": "Елементи плейлиста",
        "date": "Дата",
        "datebefore": "Дата до",
        "dateafter": "Дата після",
        "http_headers": "HTTP заголовки",
        "sleep_interval": "Інтервал очікування",
        "max_sleep_interval": "Максимальний інтервал очікування",
        "retries": "Кількість повторних спроб",
        "http_chunk_size": "Розмір фрагмента HTTP",
        "sleep_subtitles": "Очікування для субтитрів"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ Конфігурація Аргументів yt-dlp</b>\n\n<blockquote>📋 <b>Групи:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ Конфігурація Аргументів yt-dlp</b>\n\n"
        "<blockquote>📋 <b>Групи:</b>\n"
        "• ✅/❌ <b>Boolean</b> - Перемикачі True/False\n"
        "• 📋 <b>Select</b> - Виберіть з опцій\n"
        "• 🔢 <b>Numeric</b> - Введення числа\n"
        "• 📝🔧 <b>Text</b> - Введення тексту/JSON</blockquote>\n\n"
        "Ці налаштування будуть застосовані до всіх ваших завантажень."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Будь ласка, зачекайте..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Сталася помилка"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Режим введення автоматично закрито через бездіяльність (5 хвилин)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Введення містить потенційно небезпечний вміст: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Введення занадто довге (макс. 1000 символів)"
    ARGS_INVALID_URL_MSG = "❌ Недійсний формат URL. Повинен починатися з http:// або https://"
    ARGS_INVALID_JSON_MSG = "❌ Недійсний формат JSON"
    ARGS_NUMBER_RANGE_MSG = "❌ Число повинно бути між {min_val} та {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Недійсний формат числа"
    ARGS_DATE_FORMAT_MSG = "❌ Дата повинна бути у форматі YYYYMMDD (напр., 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Рік повинен бути між 1900 та 2100"
    ARGS_MONTH_RANGE_MSG = "❌ Місяць повинен бути між 01 та 12"
    ARGS_DAY_RANGE_MSG = "❌ День повинен бути між 01 та 31"
    ARGS_INVALID_DATE_MSG = "❌ Недійсний формат дати"
    ARGS_INVALID_XFF_MSG = "❌ XFF повинен бути 'default', 'never', код країни (напр., US) або IP блок (напр., 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "Немає встановлених користувацьких аргументів. Всі параметри використовують значення за замовчуванням."
    ARGS_RESET_SUCCESS_MSG = "✅ Всі аргументи скинуто до значень за замовчуванням."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Текст занадто довгий. Максимум 500 символів."
    ARGS_ERROR_PROCESSING_MSG = "❌ Помилка обробки введення. Спробуйте ще раз."
    ARGS_BOOL_INPUT_MSG = "❌ Будь ласка, введіть 'True' або 'False' для опції Відправити як файл."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Будь ласка, введіть дійсне число."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Будь ласка, надішліть <code>True</code> або <code>False</code> для увімкнення/вимкнення цієї опції."
    ARGS_JSON_VALUE_REQUEST_MSG = "Будь ласка, надішліть дійсний JSON."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "У вас ще немає тегів."
    TAGS_MESSAGE_CLOSED_MSG = "Повідомлення тегів закрито."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Субтитри вимкнено та режим Always Ask вимкнено."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Always Ask увімкнено."
    SUBS_LANGUAGE_SET_MSG = "✅ Мову субтитрів встановлено на: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️ПОПЕРЕДЖЕННЯ: через високе навантаження на CPU ця функція дуже повільна (майже в реальному часі) та обмежена:\n"
        "- максимальна якість 720p\n"
        "- максимальна тривалість 1.5 години\n"
        "- максимальний розмір відео 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Швидкі команди:</b>\n"
        "• <code>/subs off</code> - вимкнути субтитри\n"
        "• <code>/subs on</code> - увімкнути режим Always Ask\n"
        "• <code>/subs ru</code> - встановити мову\n"
        "• <code>/subs ru auto</code> - встановити мову з AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Субтитри виділено"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Вибрана мова: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Завантаження субтитрів..."
    SUBS_DISABLED_ERROR_MSG = "❌ Субтитри вимкнено. Використовуйте /subs для налаштування."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Завантаження субтитрів підтримується лише для YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Subtitles</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Language:</b> {lang}\n"
        "<b>Type:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Файл субтитрів SRT надіслано користувачу."
    SUBS_ERROR_PROCESSING_MSG = "❌ Помилка обробки файлу субтитрів."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Не вдалося завантажити субтитри."
    SUBS_ERROR_MSG = "❌ Помилка завантаження субтитрів: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Розмір розділеної частини встановлено на: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **Недійсний розмір!**\n\n"
        "**Дійсний діапазон:** 100MB до 2GB\n\n"
        "**Дійсні формати:**\n"
        "• `100mb` до `2000mb` (мегабайти)\n"
        "• `0.1gb` до `2gb` (гігабайти)\n\n"
        "**Приклади:**\n"
        "• `/split 100mb` - 100 megabytes\n"
        "• `/split 500mb` - 500 megabytes\n"
        "• `/split 1.5gb` - 1.5 gigabytes\n"
        "• `/split 2gb` - 2 gigabytes\n"
        "• `/split 2000mb` - 2000 megabytes (2GB)\n\n"
        "**Presets:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Choose max part size for video splitting:**\n\n"
        "**Range:** 100MB to 2GB\n\n"
        "**Quick commands:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Examples:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Меню закрито."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Налаштування бота</b>\n\nВиберіть категорію:"
    SETTINGS_MENU_CLOSED_MSG = "Меню закрито."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Опції очищення</b>\n\nВиберіть, що очистити:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nВиберіть дію:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 МЕДІА</b>\n\nВиберіть дію:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 ІНФО</b>\n\nВиберіть дію:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ БІЛЬШЕ КОМАНД</b>\n\nВиберіть дію:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Команда виконана."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Межа повені. Спробуйте пізніше."
    SETTINGS_HINT_SENT_MSG = "Підказка надіслана."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Пошуковий помічник відкрито."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Невідома команда."
    SETTINGS_HINT_CLOSED_MSG = "Підказку закрито."
    SETTINGS_HELP_SENT_MSG = "Надіслано файл довідки txt користувачу"
    SETTINGS_MENU_OPENED_MSG = "Відкрито меню /settings"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Помічник із пошуку закрито"
    SEARCH_CLOSED_MSG = "ЗАЧИНЕНО"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Проксі {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Помилка збереження налаштувань проксі."
    PROXY_MENU_TEXT_MSG = "Увімкнути або вимкнути використання проксі-сервера для всіх операцій yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Увімкнути або вимкнути використання проксі-серверів (доступно {config_count} + {file_count}) для всіх операцій yt-dlp?\n\nЯкщо ввімкнено ВСІ (АВТО), проксі-сервери будуть вибрані випадковим методом."
    PROXY_MENU_CLOSED_MSG = "Меню закрито."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Проксі увімкнено. Всі операції yt-dlp використовуватимуть проксі."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Проксі увімкнено. Всі операції yt-dlp використовуватимуть {count} проксі-серверів з методом вибору {method}."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Проксі ввімкнено (режим ALL AUTO).\n\n📊 Бот спробує проксі-сервери в такому порядку:\n1️⃣ {config_count} проксі з Config.py\n2️⃣ {file_count} проксі з файлу TXT/proxy.txt\n\n🔄 Усі проксі-сервери будуть випробувані послідовно до успішного підключення."
    PROXY_DISABLED_MSG = "❌ Проксі вимкнено."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Помилка збереження налаштувань проксі."
    PROXY_ENABLED_CALLBACK_MSG = "Проксі ввімкнено."
    PROXY_DISABLED_CALLBACK_MSG = "Проксі вимкнено."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ ЗАЧЕКАЙТЕ, ДОКИ ЗАВЕРШИТЬСЯ ВАШЕ ПОПЕРЕДнє ЗАВАНТАЖЕННЯ"
    AUDIO_HELP_MSG = (
        "<b>🎧 Audio Download Command</b>\n\n"
        "Usage: <code>/audio URL</code>\n\n"
        "<b>Examples:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Also see: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Підказка аудіо закрито."
    PLAYLIST_HELP_CLOSED_MSG = "Довідка плейлиста закрито."
    USERLOGS_CLOSED_MSG = "Повідомлення журналів закрито."
    HELP_CLOSED_MSG = "Допомога закрита."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>Налаштування розмиття NSFW</b>\n\nКонтент NSFW <b>{status}</b>.\n\nВиберіть, чи розмивати контент NSFW:"
    NSFW_MENU_CLOSED_MSG = "Меню закрито."
    NSFW_BLUR_DISABLED_MSG = "Розмиття NSFW вимкнено."
    NSFW_BLUR_ENABLED_MSG = "Увімкнено розмиття NSFW."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Розмиття NSFW вимкнено."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Увімкнено розмиття NSFW."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Увімкнути або вимкнути надсилання MediaInfo для завантажених файлів?"
    MEDIAINFO_MENU_CLOSED_MSG = "Меню закрито."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo увімкнено. Після завантаження інформація про файл буде надіслана."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo вимкнено."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo увімкнено."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo виділено."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Список доступних форматів</b>\n\n"
        "Отримати доступні формати відео/аудіо для URL.\n\n"
        "<b>Використання:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Приклади:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Як використовувати ID форматів:</b>\n"
        "Після отримання списку використовуйте конкретний ID формату:\n"
        "• <code>/format id 401</code> - завантажити формат 401\n"
        "• <code>/format id401</code> - те саме, що вище\n"
        "• <code>/format id140 audio</code> - завантажити формат 140 як аудіо MP3\n\n"
        "Ця команда покаже всі доступні формати, які можна завантажити."
    )
    LIST_PROCESSING_MSG = "🔄 Отримання доступних форматів..."
    LIST_INVALID_URL_MSG = "❌ Будь ласка, введіть дійсний URL, що починається з http:// або https://"
    LIST_CAPTION_MSG = (
        "📃 Доступні формати для:\n<code>{url}</code>\n\n"
        "💡 <b>Як встановити формат:</b>\n"
        "• <code>/format id 134</code> - Завантажити конкретний ID формату\n"
        "• <code>/format 720p</code> - Завантажити за якістю\n"
        "• <code>/format best</code> - Завантажити найкращу якість\n"
        "• <code>/format ask</code> - Завжди питати якість\n\n"
        "{audio_note}\n"
        "📋 Використовуйте ID формату зі списку вище"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Формати лише аудіо:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Завантажити формат 140 як аудіо MP3\n"
        "• <code>/format id140 audio</code> - те саме, що вище\n"
        "Вони будуть завантажені як файли аудіо MP3.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Помилка надсилання файлу форматів: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Не вдалося отримати формати:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Під час обробки команди сталася помилка"
    LIST_ERROR_CALLBACK_MSG = "Сталася помилка"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Як використовувати ID форматів:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Після отримання списку використовуйте конкретний ID формату:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - завантажити формат 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - те саме, що вище\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - завантажити формат 140 як аудіо MP3\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - те саме, що вище\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Виявлено формати лише аудіо: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Ці формати будуть завантажені як файли аудіо MP3.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Формати лише відео:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Використовуйте ID формату зі списку вище"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Usage:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>Examples:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - best quality\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p or lower\n"
        "• /link 720p https://youtube.com/watch?v=... - same as above\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K or lower\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K or lower"
        "</blockquote>\n\n"
        "<b>Quality:</b> from 1 to 10000 (e.g., 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Будь ласка, введіть дійсний URL"
    LINK_PROCESSING_MSG = "🔗 Отримання прямого посилання..."
    LINK_DURATION_MSG = "⏱ <b>Тривалість:</b> {duration} сек\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Відео потік:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Аудіо потік:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Keyboard setting updated!**\n\nNew setting: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Недійсний аргумент!**\n\n"
        "Valid options: `off`, `1x3`, `2x3`, `full`\n\n"
        "Example: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Keyboard Settings**\n\n"
        "Current: **{current}**\n\n"
        "Choose an option:\n\n"
        "Or use: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 клавіатуру активовано!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Клавіатура прихована"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 Клавіатура 1x3 активована!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 Клавіатура 2x3 активована!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Клавіатура Emoji активована!"
    KEYBOARD_ERROR_APPLYING_MSG = "Помилка застосування налаштування клавіатури {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Формат встановлено на: Always Ask. Вас запитують про якість кожного разу, коли ви надсилаєте URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Формат встановлено на: Always Ask. Тепер вас запитують про якість кожного разу, коли ви надсилаєте URL."
    FORMAT_BEST_UPDATED_MSG = "✅ Формат оновлено до найкращої якості (пріоритет AVC+MP4):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Формат оновлено до ID {id}:\n{format}\n\n💡 <b>Примітка:</b> Якщо це аудіо-формат, він буде завантажено як MP3 аудіо файл."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Формат оновлено до ID {id} (тільки аудіо):\n{format}\n\n💡 Це буде завантажено як MP3 аудіо файл."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Формат оновлено до якості {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Формат оновлено до:\n{format}"
    FORMAT_MENU_MSG = (
        "Виберіть опцію формату або надішліть власну, використовуючи:\n"
        "• <code>/format &lt;format_string&gt;</code> - власний формат\n"
        "• <code>/format 720</code> - якість 720p\n"
        "• <code>/format 4k</code> - якість 4K\n"
        "• <code>/format 8k</code> - якість 8K\n"
        "• <code>/format id 401</code> - конкретний ID формату\n"
        "• <code>/format ask</code> - завжди показувати меню\n"
        "• <code>/format best</code> - bv+ba/найкраща якість"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Щоб використати власний формат, надішліть команду в такому вигляді:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Замініть <code>bestvideo+bestaudio/best</code> на потрібний рядок формату."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Виберіть бажану роздільну здатність та кодек:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Формат встановлено на: Always Ask. Тепер вас запитують про якість кожного разу, коли ви надсилаєте URL."
    FORMAT_UPDATED_MSG = "✅ Формат оновлено до:\n{format}"
    FORMAT_SAVED_MSG = "✅ Формат збережено."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Вибір формату оновлено."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Меню користувацького формату закрито"
    FORMAT_CODEC_SET_MSG = "✅ Кодек встановлено на {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Вибір браузера оновлено."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Доступ заборонено. Лише адміністратор."
    ACCESS_DENIED_ADMIN = "❌ Доступ заборонено. Лише адміністратор."
    WELCOME_MASTER = "Ласкаво просимо, Майстре 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Вибачте... Під час завантаження сталася помилка."
    SIZE_LIMIT_EXCEEDED = "❌ Розмір файлу перевищує {max_size_gb} Гб. Будь ласка, виберіть менший файл у межах дозволеного розміру."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Сценарій не знайдено: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Завантажується новий дамп Firebase за допомогою {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Кеш Firebase успішно перезавантажено!"
    ADMIN_CACHE_FAILED_MSG = "❌ Не вдалося перезавантажити кеш Firebase. Перевірте, чи існує {cache_file}."
    ADMIN_ERROR_RELOADING_MSG = "❌ Помилка перезавантаження кешу: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Помилка виконання {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Усім іншим користувачам надіслано рекламне повідомлення</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Неможливо надіслати рекламне повідомлення. Спробуйте відповісти на повідомлення\nАбо сталася помилка</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ Користувач ще не завантажив жодного вмісту...</b> Не існує в журналах"
    ADMIN_INVALID_COMMAND_MSG = "❌ Недійсна команда"
    ADMIN_NO_DATA_FOUND_MSG = "❌ У кеші не знайдено даних для <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Черга порожня — з каналу ще ніхто не вийшов."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Черга банів</b>\nВсього очікує: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (зліва: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… і ще {extra} користувачів."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Використовуйте /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Заблоковані користувачі з черги: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Автоматичне блокування ввімкнено: нові користувачі будуть негайно забанені."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Автоматичне блокування вимкнено."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Вікно автоматичного блокування за розкладом встановлюється кожні {interval}."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Журнал активності каналу за останні {hours} годин (2 дні)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 Останні {hours} години (2 дні): приєднався {joined}, залишив {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Жодної активності протягом останніх {hours} годин (2 дні)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Усього: 🟢 {joined} приєднався, 🔴 {left} залишився."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Немає доступу до журналу активності каналу. Боти не можуть читати журнали адміністратора. Надайте CHANNEL_GUARD_SESSION_STRING у конфігурації з сеансом користувача, щоб увімкнути цю функцію."
    BAN_TIME_USAGE_MSG = "❌ Використання: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Використовуйте такі формати, як 10s, 6m, 5h, 4d, 3w, 2M або 1y."
    BAN_TIME_SET_MSG = "🕒 Інтервал сканування журналу каналу встановлено на {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Channel scan report\n"
        "Run at: {run_ts}\n"
        "Interval: {interval}\n"
        "New leavers: {new_leavers}\n"
        "Auto bans: {auto_banned}\n"
        "Pending: {pending}\n"
        "Last event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Використання: /block_user <id_користувача>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Адміністратор не може видалити адміністратора"
    ADMIN_USER_BLOCKED_MSG = "Користувача заблоковано 🔒❌\n \nID: <code>{user_id}</code>\nДата блокування: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> уже заблоковано ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Вибачте! Ви не адмін"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Використання: /unblock_user <id_користувача>"
    ADMIN_USER_UNBLOCKED_MSG = "Користувача розблоковано 🔓✅\n \nID: <code>{user_id}</code>\nДата розблокування: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> уже розблоковано ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Unblocked users: {count}\n⏱ Timestamp: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Використання: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Користувача проігноровано 👁️❌\n \nID: <code>{user_id}</code>\nДата ігнорування: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> вже проігноровано ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Використання: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Користувача більше не ігнорується 👁️✅\n \nID: <code>{user_id}</code>\nДата зняття ігнорування: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> не ігнорується ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Час роботи бота -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Будь ласка, надайте URL для очищення кешу.\nВикористання: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Будь ласка, надайте дійсний URL.\nВикористання: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Кеш успішно очищено для URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Для цього посилання не знайдено кешу."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Помилка очищення кешу: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Доступ заборонено. Лише адміністратор."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Запуск сценарію оновлення списку порно: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Сценарій виконано успішно!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Скрипт успішно завершено!\n\nВивід:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Скрипт не вдався з кодом повернення {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Помилка запуску сценарію: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Перезавантаження кешу, пов’язаного з порно та доменом..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Кеш порно успішно перезавантажено!\n\n"
        "📊 Поточний статус кешу:\n"
        "• Домени порно: {porn_domains}\n"
        "• Ключові слова порно: {porn_keywords}\n"
        "• Підтримувані сайти: {supported_sites}\n"
        "• БІЛИЙ СПИСОК: {whitelist}\n"
        "• СІРИЙ СПИСОК: {greylist}\n"
        "• ЧОРНИЙ СПИСОК: {black_list}\n"
        "• БІЛІ КЛЮЧОВІ СЛОВА: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Помилка перезавантаження порно кешу: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Будь ласка, надайте URL для перевірки.\nВикористання: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Будь ласка, надайте валідний URL.\nВикористання: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Перевірка URL на NSFW контент...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Результат перевірки на порнографію</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Статус:</b> <b>{status_text}</b>\n\n"
        "<b>Пояснення:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Помилка перевірки URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Печиво очищене."
    CLEAN_LOGS_CLEANED_MSG = "колоди очищені."
    CLEAN_TAGS_CLEANED_MSG = "теги очищені."
    CLEAN_FORMAT_CLEANED_MSG = "формат очищений."
    CLEAN_SPLIT_CLEANED_MSG = "розкол очищений."
    CLEAN_MEDIAINFO_CLEANED_MSG = "медіаінфо очищено."
    CLEAN_SUBS_CLEANED_MSG = "Налаштування субтитрів очищено."
    CLEAN_KEYBOARD_CLEANED_MSG = "Налаштування клавіатури очищено."
    CLEAN_ARGS_CLEANED_MSG = "Параметри аргументів очищено."
    CLEAN_NSFW_CLEANED_MSG = "Налаштування NSFW очищено."
    CLEAN_PROXY_CLEANED_MSG = "Налаштування проксі очищено."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Налаштування очікування флуду видалено."
    CLEAN_ALL_CLEANED_MSG = "Всі файли очищені."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nВиберіть дію:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Файл cookie збережено"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Пропущено перевірку файлів cookie, які не належать до YouTube"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Файл cookie існує, але має неправильний формат"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Файл cookie не знайдено."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Starting YouTube cookies test...\n\nPlease wait while I check and validate your cookies."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Your existing YouTube cookies are working properly!\n\nNo need to download new ones."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Your existing YouTube cookies are expired or invalid.\n\n🔄 Downloading new cookies..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} джерело файлів cookie не налаштовано!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} файл cookie має бути файлом .txt!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Range limit exceeded: {range_count} files requested (maximum {max_img_files}).\n\nUse one of these commands to download maximum available files:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Закрити"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Перевищено обмеження медіа: запитано {count} файлів (максимум {max_count}).\n\nВикористовуйте одну з цих команд для завантаження максимальної кількості доступних файлів:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Знайдено <b>{count}</b> медіафайлів за посиланням"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Виберіть діапазон завантаження:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Уособлення браузера"
    ARGS_REFERER_DESC_MSG = "Заголовок посилання"
    ARGS_USER_AGENT_DESC_MSG = "Заголовок User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "Обійти географічні обмеження"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Перевірте сертифікат SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "Завантажте прямі трансляції з початку"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Не завантажуйте прямі трансляції з самого початку"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Використовуйте контейнер MPEG-TS для відео HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "Завантажуйте лише одне відео, а не список відтворення"
    ARGS_NO_PART_DESC_MSG = "Не використовуйте файли .part"
    ARGS_NO_CONTINUE_DESC_MSG = "Не відновлюйте часткові завантаження"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Аудіоформат для вилучення"
    ARGS_EMBED_METADATA_DESC_MSG = "Вставити метадані у відеофайл"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Вставити мініатюру у відеофайл"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Записати ескіз у файл"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Кількість одночасних фрагментів для завантаження"
    ARGS_FORCE_IPV4_DESC_MSG = "Примусове підключення IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "Примусове підключення IPv6"
    ARGS_XFF_DESC_MSG = "Стратегія заголовка X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "Розмір блоку HTTP (байти)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Перехід у режим сну перед завантаженням субтитрів (секунди)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Дозволити підключення до застарілого сервера"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Припинити перевірку сертифіката HTTPS"
    ARGS_USERNAME_DESC_MSG = "Ім'я користувача облікового запису"
    ARGS_PASSWORD_DESC_MSG = "Пароль облікового запису"
    ARGS_TWOFACTOR_DESC_MSG = "Код двофакторної аутентифікації"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Ігноруйте помилки завантаження та продовжуйте"
    ARGS_MIN_FILESIZE_DESC_MSG = "Мінімальний розмір файлу (МБ)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Максимальний розмір файлу (МБ)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Елементи списку відтворення для завантаження (наприклад, 1,3,5 або 1-5)"
    ARGS_DATE_DESC_MSG = "Завантажити відео, завантажені на цю дату (РРРРММДД)"
    ARGS_DATEBEFORE_DESC_MSG = "Завантажити відео, завантажені до цієї дати (РРРРММДД)"
    ARGS_DATEAFTER_DESC_MSG = "Завантажити відео, завантажені після цієї дати (РРРРММДД)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Спеціальні заголовки HTTP (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Інтервал сну між запитами (секунди)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Максимальний інтервал сну (секунд)"
    ARGS_RETRIES_DESC_MSG = "Кількість повторних спроб"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Формат відеоконтейнера"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Формат вихідного контейнера для злиття"
    ARGS_SEND_AS_FILE_DESC_MSG = "Надіслати всі медіа як документ замість медіа"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Видавати себе за іншу особу"
    ARGS_REFERER_SHORT_MSG = "Реферер"
    ARGS_GEO_BYPASS_SHORT_MSG = "Геообхід"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Перевірте сертифікат"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Живий старт"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Немає прямого старту"
    ARGS_USER_AGENT_SHORT_MSG = "Агент користувача"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Без плейлисту"
    ARGS_NO_PART_SHORT_MSG = "Без частини"
    ARGS_NO_CONTINUE_SHORT_MSG = "Ні Продовжити"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Аудіоформат"
    ARGS_EMBED_METADATA_SHORT_MSG = "Вставити мета"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Вставити великий палець"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Напишіть великий палець"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Одночасний"
    ARGS_FORCE_IPV4_SHORT_MSG = "Примусово використовувати IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Примусовий IPv6"
    ARGS_XFF_SHORT_MSG = "Заголовок XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Розмір шматка"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Sleep Subs"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Legacy Connect"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Немає перевірки сертифіката"
    ARGS_USERNAME_SHORT_MSG = "Ім'я користувача"
    ARGS_PASSWORD_SHORT_MSG = "Пароль"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Ігнорувати помилки"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Мінімальний розмір"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Максимальний розмір"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Елементи плейлисту"
    ARGS_DATE_SHORT_MSG = "Дата"
    ARGS_DATEBEFORE_SHORT_MSG = "Дата до"
    ARGS_DATEAFTER_SHORT_MSG = "Дата після"
    ARGS_HTTP_HEADERS_SHORT_MSG = "Заголовки HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Інтервал сну"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Максимальний сон"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Формат відео"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Формат злиття"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Надіслати як файл"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ Файл завеликий. Максимальний розмір – 100 КБ."
    COOKIES_INVALID_FORMAT_MSG = "❌ Дозволяються лише файли такого формату .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ Файл не схожий на cookie.txt (немає рядка «# Netscape HTTP Cookie File»)."
    COOKIES_ERROR_READING_MSG = "❌ Помилка читання файлу: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Файл cookie існує та має правильний формат"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} файл cookie завеликий! Макс. 100 КБ, отримано {service} КБ."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} файл cookie завантажено та збережено як cookie.txt у вашій папці.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} cookie source is unavailable (status {status}). Please try again later."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Помилка завантаження {service} файлу cookie. Спробуйте пізніше."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Користувач надав новий файл cookie.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie successfully updated:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Недійсний файл cookie.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ Джерела файлів cookie YouTube не налаштовано!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Доступ заборонено. Лише адміністратор."
    ADMIN_USER_LOGS_TOTAL_MSG = "Всього: <b>{total}</b>\n<b>{user_id}</b> - логи (Останні 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 клавіатуру активовано!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Вибрано мову субтитрів: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Вибрано мову субтитрів: {flag} {name} з увімкненим AUTO/TRANS."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Меню мови субтитрів закрито."
    SUBS_DOWNLOADING_MSG = "💬 Завантаження субтитрів..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Перезавантаження кешу Firebase у пам’ять..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Не налаштовано COOKIE_URL. Використовуйте /cookie або завантажте cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Завантаження файлів cookie з віддаленої URL-адреси..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Резервна URL-адреса COOKIE_URL має вказувати на файл .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Резервний файл cookie завеликий (>100 КБ)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Файл cookie YouTube, завантажений через резервний варіант і збережений як cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Резервне джерело cookie недоступне (статус {status}). Спробуйте /cookie або завантажте cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Помилка завантаження резервного файлу cookie. Спробуйте /cookie або завантажте cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Неочікувана помилка під час резервного завантаження cookie."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} браузер не встановлено."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Файли cookie, збережені за допомогою браузера: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Не вдалося зберегти файли cookie: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ Файли cookie YouTube працюють належним чином"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube cookies are expired or invalid\n\nUse /cookie to get new cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - власний формат\n• <code>/format 720</code> - якість 720p\n• <code>/format 4k</code> - якість 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Підказку надіслано."
    FORMAT_MKV_TOGGLE_MSG = "MKV тепер {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Віддалена URL-адреса не налаштована"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Недійсний формат файлу"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Файл завеликий"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Файли cookie успішно завантажено"
    COOKIES_SERVER_ERROR_MSG = "❌ Помилка сервера {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Помилка завантаження"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Неочікувана помилка"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Браузер не встановлено."
    COOKIES_MENU_CLOSED_MSG = "Меню закрито."
    COOKIES_HINT_CLOSED_MSG = "Підказку щодо файлів cookie закрито."
    IMG_HELP_CLOSED_MSG = "Допомога закрита."
    SUBS_LANGUAGE_UPDATED_MSG = "Налаштування мови субтитрів оновлено."
    SUBS_MENU_CLOSED_MSG = "Меню мови субтитрів закрито."
    KEYBOARD_SET_TO_MSG = "Для клавіатури встановлено {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Помилка обробки налаштування"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo увімкнено."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo вимкнено."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Розмиття NSFW вимкнено."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Увімкнено розмиття NSFW."
    SETTINGS_MENU_CLOSED_MSG = "Меню закрито."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Очікування повені активне. Спробуйте пізніше."
    OTHER_HELP_CLOSED_MSG = "Допомога закрита."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Повідомлення журналів закрито."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Меню закрито."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Недійсний розмір."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Помилка надсилання MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Сталася помилка: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - усі журнали"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - усі {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Завантажте з Remote URL"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Відкрийте браузер"
    SELECT_BROWSER_MSG = "Виберіть браузер для завантаження файлів cookie:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "У цій системі не знайдено жодного браузера. Ви можете завантажити файли cookie з віддаленої URL-адреси або відстежувати стан браузера:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Відкрити браузер</b> - щоб відстежувати стан браузера в міні-програмі"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Не вдалося запустити /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Межа повені. Спробуйте пізніше."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Не вдалося відкрити меню файлів cookie браузера"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Підказка \"Зберегти як файл cookie\" закрита."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Usage:</b>\n<code>/link [quality] URL</code>\n\n<b>Examples:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - best quality\n• /link 720 https://youtube.com/watch?v=... - 720p or lower\n• /link 720p https://youtube.com/watch?v=... - same as above\n• /link 4k https://youtube.com/watch?v=... - 4K or lower\n• /link 8k https://youtube.com/watch?v=... - 8K or lower</blockquote>\n\n<b>Quality:</b> from 1 to 10000 (e.g., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K quality"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Не вдалося отримати посилання на потік"
    LINK_ERROR_GETTING_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Недійсний індекс файлів cookie YouTube: {selected_index}. Доступний діапазон 1-{selected_index}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}\n🔍 Testing cookies..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube cookies successfully downloaded and validated!\n\nUsed source {source} of {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ All YouTube cookies are expired or unavailable!\n\nContact the bot administrator to replace them."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube cookie retry limit exceeded!\n\n🔢 Maximum: {limit} attempts per hour\n⏰ Please try again later"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Тег #{wrong} містить заборонені символи. Дозволені лише літери, цифри та _.\nБудь ласка, використовуйте: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Недійсний аргумент!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Вибрана мова субтитрів: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Приклад: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Вибрана мова: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Режим Always Ask {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Субтитри вимкнені"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Налаштування субтитрів</b>\n\n{status_text}\n\nВиберіть мову субтитрів:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - вимкнути субтитри\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Налаштування субтитрів</b>\n\n{status_text}\n\nВиберіть мову субтитрів:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Title:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- максимальна якість 720p\n- максимальна тривалість 1.5 години\n- максимальний розмір відео 500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️ПОПЕРЕДЖЕННЯ: через високе навантаження на CPU ця функція дуже повільна (майже в реальному часі) і обмежена:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Швидкі команди:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - вимкнути субтитри\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - увімкнути режим Завжди питати\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - set language\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - set language with AUTO/TRANS enabled\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - enable Always Ask mode\n"
    SUBS_AUTO_SUBS_TEXT = "(автоматичні заміни)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Режим автопідписів {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS вимкнено за допомогою команди: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Always Ask увімкнено за допомогою команди: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "Мова SUBS, встановлена за допомогою команди: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "Мова SUBS + автоматичний режим, встановлений командою: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Користувач відкрив меню /subs."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Користувач встановив мову субтитрів: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Користувач перемкнув режим AUTO/TRANS на: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Користувач перемкнув режим «Завжди запитувати» на: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Користувач запросив файли cookie з браузера."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Клавіатура вибору браузера надсилається лише разом із встановленими браузерами."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Вибір браузера закрито."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "Резервний COOKIE_URL використано успішно (джерело приховано)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "Помилка резервної URL-адреси COOKIE_URL: status={status} (приховано)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Неочікувана помилка резервного COOKIE_URL: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Браузер {browser} не встановлено."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Файли cookie, збережені за допомогою браузера: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "Файл cookie збережено для користувача {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "Файл cookie існує, має правильний формат, а файли cookie YouTube працюють."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Файл cookie існує та має правильний формат, але термін дії файлів cookie YouTube минув."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Файл cookie існує та має правильний формат."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Файл cookie існує, але має неправильний формат."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Файл cookie не знайдено."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{service} URL-адреса файлів cookie порожня для користувача {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} URL-адреса файлу cookie не є .txt (приховано)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} файл cookie завеликий: {size} байт (джерело приховано)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{service} файл cookie завантажено для користувача {user_id} (джерело приховано)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Сценарій не знайдено: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Не вдалося надіслати початкове повідомлення про статус"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Помилка виконання {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Кеш Firebase перезавантажено за допомогою автоматичного завдання."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Адміністратор перезавантажив кеш Firebase."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Помилка перезавантаження кешу Firebase: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Розсилку ініційовано. Текст:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Широкомовне повідомлення, надіслане всім користувачам."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Не вдалося передати повідомлення: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Адміністратор {user_id} очистив кеш для URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Адміністратор {user_id} запустив сценарій оновлення списку порно: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Сценарій оновлення списку порнофайлів успішно виконано адміністратором {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Адміністратор не вдався до оновлення сценарію списку порно {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Адміністратор {user_id} намагався запустити неіснуючий скрипт: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Помилка запуску сценарію оновлення порно від адміністратора {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Адміністратор {user_id} розпочав перезавантаження порно кешу"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Помилка перезавантаження порно кешу адміністратором {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Адміністратор {user_id} перевірив URL-адресу для NSFW: {url} - Результат: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "User requested format change."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "Format set to ALWAYS_ASK."
    FORMAT_UPDATED_BEST_LOG_MSG = "Format updated to best: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "Format updated to ID {format_id}: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "Format updated to ID {format_id} (audio-only): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "Format updated to quality {quality}: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "Format updated to: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "Format menu sent."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "Format selection closed."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "Custom format hint sent."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "Format resolution menu sent."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "Returned to main format menu."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "Format updated to: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "Format set to ALWAYS_ASK."
    FORMAT_CODEC_SET_LOG_MSG = "Codec preference set to {codec}"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Custom format menu closed"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "Пряме посилання для користувача {url} отримано з {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Не вдалося отримати пряме посилання для користувача {user_id} з {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Помилка в команді посилання для користувача {error}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Користувач {user_id} встановив клавіатуру на {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Користувач {user_id} встановив клавіатуру на {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo встановлюється за допомогою команди: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Користувач відкрив меню /mediainfo."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: закрито."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo увімкнено."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo вимкнено."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "За допомогою аргументу встановлено розмір розділеного {size} байтів."
    SPLIT_MENU_OPENED_LOG_MSG = "Користувач відкрив меню /split."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Розділений вибір закрито."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Для розділеного розміру встановлено {size} байтів."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Проксі встановлено за допомогою команди: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Користувач відкрив меню /проксі."
    PROXY_MENU_CLOSED_LOG_MSG = "Проксі: закрито."
    PROXY_ENABLED_LOG_MSG = "Проксі ввімкнено."
    PROXY_DISABLED_LOG_MSG = "Проксі вимкнено."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Повідомлення довідки закрито."
    AUDIO_HELP_SHOWN_LOG_MSG = "Показав /аудіодовідку"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Користувач запитав допомогу зі списком відтворення."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Довідку про список відтворення закрито."
    AUDIO_HINT_CLOSED_LOG_MSG = "Аудіопідказку закрито."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Меню прямого посилання, створене за допомогою кнопки LINK для користувача {user_id} з {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Не вдалося отримати пряме посилання за допомогою кнопки LINK для користувача {error} з {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "Команда LIST виконана для користувача {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Швидке вставлення: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Меню \"Завжди запитувати\" надіслано для {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Створено меню кешованих якостей для користувача {error} після помилки: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Помилка меню «Завжди запитувати» для {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Формат фіксується за допомогою параметрів /args"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Аудіо"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "відео"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "відео"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Далі ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Поперед"
    SUBTITLES_NEXT_BUTTON_MSG = "Далі ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Усі текстові поля порожні"
    SENDER_VIDEO_DURATION_MSG = "Тривалість відео:"
    SENDER_UPLOADING_FILE_MSG = "📤 Завантаження файлу..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Завантаження відео..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Тривалість відео:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 файл завантажено."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Інформація про відео"
    DOWN_UP_NUMBER_MSG = "Номер"
    DOWN_UP_TITLE_MSG = "Назва"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Завантажене відео."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Обробка для завантаження..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Файл розділеної частини {part} завантажено"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Завантаження завершено"
    DOWN_UP_FILES_UPLOADED_MSG = "завантажених файлів"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Закрити"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼КОДЕК"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 ДУБЛЮВАННЯ"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 ПІДПИСКИ"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Браузер"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Отримання прямого посилання..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Отримання доступних форматів..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Отримання опису відео..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Помилка отримання опису: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Опис відео недоступний"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Помилка надсилання опису: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Опис відео надіслано користувачу {user_id} для {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Запуск gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Тривалість:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Формат:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Браузер:</b> відкрити у веб-браузері"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Доступні формати для"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Як використовувати ідентифікатори формату:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Після отримання списку використовуйте певний ідентифікатор формату:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - завантажити формат 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - те саме, що й вище"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - завантажити формат 140 як MP3 аудіо"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Виявлено формати лише аудіо"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Ці формати будуть завантажені як аудіофайли MP3."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Як встановити формат:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> – завантажте певний ідентифікатор формату"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Завантажувати за якістю"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - завантажте найкращу якість"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> – завжди запитуйте якість"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Формати лише аудіо:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - завантажте формат 140 як MP3-аудіо"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Вони будуть завантажені як аудіофайли MP3."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Використовуйте ідентифікатор формату зі списку вище"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Помилка: оригінальне повідомлення не знайдено."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Сторінка форматів"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Помилка відображення меню форматів"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Помилка отримання форматів"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Помилка отримання доступних форматів."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Спробуйте пізніше."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp не може обробити цей вміст"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Натомість система рекомендує використовувати gallery-dl."
    ALWAYS_ASK_OPTIONS_MSG = "**Опції:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Для галерей зображень: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Для окремих зображень: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl часто працює краще для Instagram, Twitter та іншого вмісту соціальних мереж."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Спробуйте Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Формат виправлено через /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Субтитри"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Дубльоване аудіо"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — доступні субтитри"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Виберіть мову субтитрів"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Підписки не знайдено та не вставляються"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Миттєвий репост із кешу"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Виберіть мову аудіо"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW платний (⭐️$0,02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Виберіть якість завантаження"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Завантажити зображення (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Отримайте пряме посилання на відео"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Показати список доступних форматів"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Змінити розширення/кодек відео"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Вставити"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Витягніть лише аудіо"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW платний (⭐️$0,02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Миттєвий репост із кешу"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Виберіть мову аудіо"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Найкращий"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Інше"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝лише суб"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Розумне групування"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Додано рядок кнопок дії (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Додано рядки кнопок дій (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "До існуючого рядка додано нижні кнопки"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Створено новий нижній ряд"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "У списку відтворення не знайдено відео"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "Непідтримувана URL-адреса"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Відео не знайдено"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Відео не знайдено"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Медіа не знайдено"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Цей твіт не містить"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Помилка під час отримання інформації про відео:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Помилка отримання інформації про відео"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Спробуйте команду <code>/clean</code> і повторіть спробу. Якщо помилка не зникає, YouTube вимагає авторизації. Оновіть файл cookies.txt за допомогою <code>/cookie</code> або <code>/cookies_from_browser</code> і повторіть спробу."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Меню закрито."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Ручний вибір якості"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Виберіть якість вручну, оскільки автоматичне визначення не вдалося:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Усі доступні формати"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Доступні якості (з кешу)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Використання кешованих якостей - нові формати можуть бути недоступними"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Формат завантаження"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Завантаження"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Завантаження з відстеженням прогресу..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Завантаження у форматі:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Завантаження аудіо у форматі:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Завантаження найкращої якості..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Завантаження дампа бази даних..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Завантаження"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Сторінка форматів"
    ALWAYS_ASK_FROM_CACHE_MSG = "(з кешу)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Помилка: оригінальне повідомлення не знайдено. Можливо, його видалили. Надішліть посилання ще раз."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Помилка: вихідну URL-адресу не знайдено. Надішліть посилання ще раз."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Отримано пряме посилання</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Назва:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Тривалість:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Формат:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Відеопотік:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Аудіопотік:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Не вдалося отримати посилання на потік"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Пряме посилання, отримане через меню «Завжди запитувати» для користувача {url} з {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Не вдалося отримати пряме посилання через меню «Завжди запитувати» для користувача {error} з {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Пряме посилання, отримане через down_and_up_with_format для користувача {url} з {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Не вдалося отримати пряме посилання через down_and_up_with_format для користувача {error} з {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Пряме посилання, отримане через down_and_audio для користувача {url} з {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Не вдалося отримати пряме посилання через down_and_audio для користувача {error} з {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Аудіо надіслано з кешу."
    AUDIO_PROCESSING_MSG = "🎙️ Аудіо обробляється..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Завантаження аудіо:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Під час завантаження аудіо сталася помилка."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Не вдалося отримати аудіоінформацію"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Пропуск непідтримуваного типу файлу в списку відтворення за індексом {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "Аудіофайл не знайдено після завантаження."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ Не вдалося надіслати аудіо: Розмір файлу дорівнює 0 B (індекс плейлиста {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ Аудіо файл ще завантажується, будь ласка, зачекайте..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Uploading audio file...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Не вдалося надіслати аудіо: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Аудіо зі списку відтворення надіслано: {sent}/{total} файли (якість={quality}) користувачеві{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Не вдалося завантажити аудіо: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Завантаження скасовано через час очікування (2 години)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Відеофайл не знайдено: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ Не вдалося надіслати відео: Розмір файлу дорівнює 0 B (індекс плейлиста {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ Відео файл ще завантажується, будь ласка, зачекайте..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Помилка обробки відео: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Помилка надсилання файлу опису: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 якщо ви хочете змінити підпис до відео - дайте відповідь на відео з новим текстом</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Субтитри не виявлено"
    VIDEO_PROGRESS_MSG = "<b>Відео:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Аудіо:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ Перевищено ліміт URL-адрес: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Обробку завершено"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Діапазони списків відтворення заборонені в режимі кількох URL-адрес. Надсилайте лише окремі URL-адреси без діапазонів (*1*5, /vid 1-10 тощо)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Перевірте <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>тут</a>, чи ваш сайт підтримує"
    ERROR_COOKIE_NEEDED_MSG = "Вам може знадобитися <code>cookie</code> для завантаження цього відео. Спочатку очистіть своє робоче середовище за допомогою команди <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Для Youtube – отримати <code>cookie</code> за допомогою команди <b>/cookie</b>. Для будь-якого іншого підтримуваного сайту надішліть власний файл cookie (<a href='https://t.me/tg_ytdlp/203'>guide1</a>) (<a href='https://t.me/tg_ytdlp/214'>guide2</a>), а потім знову надішліть посилання на відео."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Виберіть мову субтитрів"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Немає альтернативних мов аудіо"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Виберіть мову аудіо"
    PAGE_NUMBER_MSG = "Сторінка {page}"
    TOTAL_PROGRESS_MSG = "Повний прогрес"
    SUBTITLE_MENU_CLOSED_MSG = "Меню субтитрів закрито."
    SUBTITLE_LANGUAGE_SET_MSG = "Вибрана мова субтитрів: {value}"
    AUDIO_SET_MSG = "Набір аудіо: {value}"
    FILTERS_UPDATED_MSG = "Фільтри оновлено"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Назад"
    CLOSE_BUTTON_TEXT = "🔚Закрити"
    LIST_BUTTON_TEXT = "📃Список"
    IMAGE_BUTTON_TEXT = "🖼Зображення"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Якості не визначено автоматично\nВикористовуйте кнопку 'Інше', щоб побачити всі доступні формати.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Виявлено пряму трансляцію**\n\nЗавантаження поточних або нескінченних прямих трансляцій заборонено.\n\nБудь ласка, зачекайте, поки трансляція закінчиться, і спробуйте завантажити знову, коли:\n• Тривалість трансляції відома\n• Трансляція закінчилася\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Завантаження прямої трансляції</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Чанк {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Максимальний розмір: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Загальна тривалість: {duration} сек"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Пряма трансляція - Частина {chunk}</b>\n⏱ Тривалість: {duration} сек\n📦 Розмір: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Чанк {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Завантаження прямої трансляції завершено</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "Завантажено фрагмент(и) {chunks}"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Загальна тривалість: {duration} сек"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Завантаження прямої трансляції зупинено</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Каталог користувача видалено (ймовірно, командою /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "Файл фрагмента було видалено (ймовірно, командою /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Потік закінчився"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Виберіть інший формат за допомогою команди `/format`."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Отримано пряме посилання</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Title:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **File Processing Error**\n\nThe video was downloaded but couldn't be processed due to invalid characters in the filename.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **File Processing Error**\n\nThe video was downloaded but couldn't be processed due to an invalid argument error.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Причина:**\n"
        "• Завантажений файл не є відео файлом\n"
        "• Це може бути документ (PDF, DOC тощо) або архів\n\n"
        "**Рішення:**\n"
        "• Перевірте посилання - воно може вести до документа, а не до відео\n"
        "• Спробуйте інше посилання або джерело\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Причина:**\n"
        "• Файл не може бути оброблений як відео\n"
        "• Це може не бути відео файл або файл пошкоджений\n\n"
        "**Рішення:**\n"
        "• Перевірте посилання - воно може вести до документа, а не до відео\n"
        "• Спробуйте інше посилання або джерело\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Format Not Available**\n\nThe requested video format is not available for this video.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Format ID {format_id} not found for this video.\n\nAvailable format IDs: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **Формат AV1 недоступний для цього відео.**\n\n**Доступні формати:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **File Processing Error**\n\nThe audio was downloaded but couldn't be processed due to invalid characters in the filename.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **File Processing Error**\n\nThe audio was downloaded but couldn't be processed due to an invalid argument error.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Користувач ввів заборонений вміст. Неможливо завантажити."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "Розмиття NSFW встановлено за допомогою команди: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Користувач відкрив меню /nsfw."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: закрито."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Не вдалося завантажити {service} cookie: status={status} (URL-адреса прихована)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Помилка завантаження {service} cookie: {error} (URL-адресу приховано)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Неочікувана помилка під час завантаження {service} cookie (URL-адресу приховано): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Файл cookie оновлено для користувача {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Недійсний вміст файлів cookie, наданий користувачем {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "URL-адреси файлів cookie YouTube порожні для користувача {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "Файли cookie YouTube завантажено та перевірено для користувача {source} з джерела {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Для користувача {user_id} не вдалося створити всі джерела файлів cookie YouTube."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Помилка в команді check_porn адміністратора {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Розмір розділеної частини встановлено на {size} байтів."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Завантаження відео завершено з розділенням файлу."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Відео зі списків відтворення надіслано: {sent}/{total} файли (якість={quality}) користувачу {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Невідома помилка: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Пропуск непідтримуваного типу файлу в списку відтворення за індексом {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg not found. Please install FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Помилка перетворення в MP4: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Вбудовування субтитрів може зайняти багато часу (до 1 хв на 1 хв відео)!\n🔥 Початок вбудовування субтитрів..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Субтитри не можна вставляти через обмеження (якість/тривалість/розмір)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Субтитри недоступні для вибраної мови"
    ERROR_SENDING_VIDEO_MSG = "❌ Помилка надсилання відео: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Надіслані відео зі списку відтворення: {sent}/{total} файлів."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Завантаження скасовано через час очікування (2 години)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Не вдалося завантажити відео: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Помилка: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON має бути об’єктом (словником)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Недійсний формат JSON. Надайте дійсний JSON."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Значення має бути між {min_val} і {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} встановлено: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Правда"
    ARGS_FALSE_BUTTON_MSG = "❌ Неправда"
    ARGS_BACK_BUTTON_MSG = "🔙 Back"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Закрити"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Правда"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Неправда"
    ARGS_NOT_SET_MSG = "Не встановлено"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ Формат AV1 недоступний для цього відео.\n\nДоступні формати:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Помилка завантаження: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ У списку відтворення за індексом {index} не знайдено відео."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Конвертація відео не вдалася**\n\nВідео не вдалося конвертувати в MP4 через помилку недійсного аргументу.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Конвертація відео не вдалася**\n\nВідео не вдалося конвертувати в MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Не вдалося отримати посилання на потік"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ Немає вмісту за індексом {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Помилка: оригінальне повідомлення не знайдено."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Помилка: URL не знайдено."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Цю URL-адресу неможливо вставити."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} кодек недоступний для цього відео"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} формат недоступний для цього відео"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Обмеження повені. Спробуйте пізніше."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Перевірте файли cookie"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ ВСІ (АВТО)"
    PROXY_OFF_BUTTON_MSG = "❌ ВИМКНЕНО"
    PROXY_CLOSE_BUTTON_MSG = "🔚Закрити"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Виберіть країну:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Очистити вибір країни"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Вибрано країну: {country} (код: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Доступні проксі: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Бот спочатку спробує HTTP, а потім SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Проксі автоматично вмикається для вибраної країни"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Вибір країни знято"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Вибір країни знято"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Вибрана країна: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Використовується країна з файлу: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Доступні країни з файлу: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 Вибрана країна: {country} (код: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ Проксі ввімкнено для цієї країни"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ Проксі вимкнено (натисніть ALL (AUTO), щоб увімкнути)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ УВІМКНЕНО"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ ВИМКНЕНО"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Закрити"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV: ON"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV: OFF"
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ УВІМКНЕНО (без розмиття)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ УВІМК. (Без розмиття)"
    NSFW_OFF_BLUR_MSG = "✅ ВИМК. (Розмиття)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ ВИМК. (Розмиття)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "чистий"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Помилка обробки повідомлення-відповіді для користувача {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Помилка надсилання трансляції користувачу {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Логи {bot_name}\nКористувач: {user_id}\nВсього логів: {total}\nПоточний час: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nВсього {path}: {count}\nПоточний час: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Всього користувачів: {count}</i>\nОстанні 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Кеші порно оновлено адміністратором {admin_id}. Домени: {domains}, ключові слова: {keywords}, сайти: {sites}, БІЛИЙ СПИСОК: {whitelist}, СІРИЙ СПИСОК: {greylist}, ЧОРНИЙ СПИСОК: {black_list}, БІЛІ_КЛЮЧОВІ СЛОВА: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Помилка надсилання повідомлення про час очікування: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Виберіть мову</b>"
    LANG_CHANGED_MSG = "✅ Мову змінено на {lang_name}"
    LANG_ERROR_MSG = "❌ Помилка при зміні мови"
    LANG_CLOSED_MSG = "Вибір мови закрито"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "Зворотний виклик [BROWSER]: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Додавання кнопки моніторингу браузера з URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "URL-адресу моніторингу браузера не налаштовано: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Налаштування клавіатури оновлено!**\n\nНове налаштування: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Не вдалося приховати клавіатуру: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Використання робочих файлів cookie YouTube для отримання посилань для користувача {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Немає робочих файлів cookie YouTube для отримання посилань для користувача {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Використання наявних файлів cookie YouTube для отримання посилань для користувача {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Не знайдено файлів cookie YouTube для отримання посилань для користувача {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Глобальний файл cookie скопійовано в папку користувача {user_id} для вилучення посилання"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Користувач {user_id} запитав команду mediainfo"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Користувач {user_id} є адміністратором: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Користувач {user_id} перебуває на каналі: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[МЕДІЯІНФОРМАЦІЯ] Користувачу {user_id} заборонено доступ – він не адміністратор і не в каналі"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Доступ користувача {user_id} надано"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] зворотний виклик: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Ця команда доступна лише для адміністраторів."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Завантаження завершено з підтримкою маркера PO"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Межа повені. Спробуйте пізніше."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ Помилка оновлення маркера REST: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Помилка закриття сеансу Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Помилка ініціалізації базової структури бази даних: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Не всі параметри встановлюються в config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL не встановлено"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey не встановлено для отримання idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Помилка завантаження дампа Firebase: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Не вдалося завантажити дамп Firebase через REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Помилка в _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Помилка запуску auto reload_cache (спроба {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Усі повторні спроби не вдалися"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Початок завантаження дампа Firebase з {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Залежність недоступна: запити або сеанс"
    DB_DATABASE_EMPTY_MSG = "⚠️ База даних порожня"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Помилка закриття журналу: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Помилка під час очищення: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Помилка клонування: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Час очікування клонування"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Виняток клону: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Оновлення скасовано користувачем"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Репозиторій успішно клоновано"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Резервні копії переміщено до _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Всі модулі завантажені"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Очищення завершено після виходу"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Отримано сигнал {signal}, коректне завершення роботи..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Будь ласка, зачекайте..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Завантаження потоку HLS:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "в очікуванні фрагментів"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Резервну копію {ts} не знайдено в _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Не вдалося відновити {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Відновлено: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Details:</b> {error_details}\n\nDownload stopped due to critical error.\n\n💡 <b>Tip:</b> If you're getting 401 Unauthorized error, try using <code>/cookie instagram</code> command or send your own cookies to authenticate with Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Домен у чорному списку порно: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Знайдено порно ключові слова: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Домен у білому списку: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Знайдено ключові слова білого списку: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Ключові слова порнографії не знайдено"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Помилка API TikTok за індексом {index}, перехід до наступного аудіо..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Помилка API TikTok за індексом {index}, перехід до наступного відео..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "User entered a <b>url</b>\n <b>user's name:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>User entered like this:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Приєднатися до каналу"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Обробник реєстрації: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Завантажте мої 5 файлів cookie"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - отримати YT-cookie браузера"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Перевірте свій файл cookie"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Завантажте власні файли cookie"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Закрити"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Доступні формати для: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Закрити"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Закрити"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Закрити"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Закрити"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Допомога закрита."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "ЗАЧИНЕНО"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Сталася помилка"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg не знайдено в PATH або каталозі проекту. Будь ласка, встановіть FFmpeg."
    YTDLP_NOT_FOUND_MSG = "Двійковий файл yt-dlp не знайдено в PATH або каталозі проекту. Будь ласка, встановіть yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Відео буде розділено на {rounds} частин, що може бути надмірним"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Розділення частини відео {current}/{total}: {start_time:.2f}с до {end_time:.2f}с"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Не вдалося створити частину розділення {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Успішно створено частину розділення {part}: {target_name} ({size} байт)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Помилка розділення частини відео {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Відео успішно розділено на {count} частин"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Помилка в процесі розділення відео: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Помилка під час обробки відео {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Відеофайл не існує: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Помилка парсингу розмірів '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Не вдалося визначити розміри відео з '{size_result}', використовується за замовчуванням: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Помилка створення мініатюри: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Помилка парсингу тривалості відео: {error}, результат був: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Мініатюра не створена в {thumb_dir}, використовується за замовчуванням"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Помилка виконання команди: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Помилка створення мініатюри з FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Пропускання розділу конфігурації non-dict: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Налаштування {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Використання файлів cookie користувача: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Використання файлів cookie YouTube для користувача {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Глобальний файл cookie скопійовано в папку користувача {user_id}"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Використання скопійованих глобальних файлів cookie як файлів cookie користувача: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Не вдалося скопіювати глобальний файл cookie для користувача {error}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Використання --no-cookies для домену: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Проксі-сервер запитав, але не вдалося імпортувати/отримати конфігурацію: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Примусово використовувати проксі для gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Проксі-сервер запитується, але налаштування проксі-сервера не завершено"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Помилка проксі-сервера: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Розбір елементів екстрактора..."
    GALLERY_DL_ITEM_COUNT_MSG = "Пункт {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Знайдено метадані (тег 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "Знайдено URL (тег 3): {url}, метадані: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Знайдено метадані (застарілі): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "Знайдено URL (застаріла): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Назва знайденого файлу: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Знайдено каталог: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Знайдено розширення: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Проаналізовано {count} елементів, інформація: {info}, запасний варіант: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Налаштування конфігурації gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Спроба стратегії A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "модуль gallery_dl.extractor не знайдено"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() недоступний у цій збірці"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Виклик extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Жоден екстрактор не відповідає URL-адресі"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Налаштування файлів cookie для екстрактора: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Не вдалося встановити файли cookie для екстрактора: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Екстрактор знайдено, виклик елементів()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Стратегія A виконана успішно, отримано інформацію: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Стратегія A: extractor.items() не повернув дійсну інформацію"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Стратегія A (extractor.find) не вдалася: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Запасні метадані з --get-urls: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Усім стратегіям не вдалося отримати метадані"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Не вдалося отримати інформацію про зображення: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "модуль gallery_dl.job не знайдено (порушена інсталяція?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob недоступний у цій збірці"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Пошук завантажених файлів у каталозі gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Спроба знайти файли за іменами з екстрактора"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Помилка читання аргументів користувача для {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Помилка під час обробки відео{video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Користувач {user_id} увімкнув send_as_file, надсилаючи як документ"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "тайм-аут send_video неодноразово минув; повернення до send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Підпис задовгий, спробуйте створити мінімальну кількість підписів"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (мінімальний титр) минув; повернення до send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Помилка надсилання відео з мінімальною кількістю субтитрів: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Помилка надсилання файлу повного опису: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Помилка видалення тимчасового файлу опису: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Пропуск match_filter для домену в NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Перевірка наявних файлів cookie YouTube на URL-адресі користувача для визначення формату для користувача {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Існуючі файли cookie YouTube працюють з URL-адресою користувача для визначення формату для користувача {user_id} — їх використання"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Помилка існуючих файлів cookie YouTube на URL-адресі користувача, спроба отримати нові для визначення формату для користувача {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Випробування джерела файлів cookie YouTube {i} для виявлення формату для користувача {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "Файли cookie YouTube із джерела {i} працюють над URL-адресою користувача для визначення формату користувача {user_id} - зберігаються в папці користувача"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "Файли cookie YouTube із джерела {i} не працюють з URL-адресою користувача для визначення формату користувача {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Не вдалося завантажити файли cookie YouTube із джерела {i} для визначення формату для користувача {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Усім джерелам файлів cookie YouTube не вдалося визначити формат для користувача {user_id}, буде спроба без файлів cookie"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Жодне джерело файлів cookie YouTube не налаштовано для визначення формату для користувача {user_id}, намагатиметься без файлів cookie"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Файли cookie YouTube не знайдено для визначення формату для користувача {user_id}, спроба отримати нові"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Використання файлів cookie YouTube для визначення формату для користувача {user_id} (вже перевірено в меню «Завжди запитувати»)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Файли cookie YouTube не знайдено для визначення формату для користувача {user_id}, намагаючись відновити..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Глобальний файл cookie скопійовано в папку користувача {user_id} для визначення формату"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Не вдалося скопіювати глобальний файл cookie для користувача {error}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Використання --no-cookies для домену в get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "Додаток ще не ініціалізовано. Неможливо отримати доступ до {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Caption:</b> <code>{caption}</code>\n<b>User id:</b> <code>{user_id}</code>\n<b>User first name:</b> <code>{users_name}</code>\n<b>Video file id:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Помилка в caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Неочікувана помилка в caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL-адреса відео</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL відсутній у конфігурації"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin ініціалізовано"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken оновлено"
    DB_LOG_FOR_USER_ADDED_MSG = "Журнал для користувача додано"
    DB_DATABASE_CREATED_MSG = "db створено"
    DB_BOT_STARTED_MSG = "Бот запущений"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY зберігається в config.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Частина списку відтворення вже кешована: {path_parts}, пропуск"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: кеш не знайдено для будь-якого варіанта URL/якості, повертає порожній dict"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: швидкий підрахунок для великого діапазону: {cached_count} кешованих відео"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: кеш не знайдено для хешу {quality_key}, які{url_hash}_0__"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: кеш не знайдено для будь-якого варіанту URL-адреси, повертає None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Доступ заборонено. Лише адміністратор."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Auto Firebase cache reloading updated!\n\n📊 Status: {status}\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Недійсний аргумент. Використовуйте /auto_cache на | вимкнено | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Інтервал має бути від 1 до 168 годин"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Не вдалося встановити інтервал"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Auto Firebase cache interval updated!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Auto Firebase cache reloading started!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Автоматичне перезавантаження УВІМКНЕНО; наступний о {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Автоматичне перезавантаження ВИМКНЕНО адміністратором."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Інтервал автоматичного перезавантаження встановлено на {next_exec}h; наступний {interval}__"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Розпочато автоматичне перезавантаження; наступний о {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Автоматичне перезавантаження зупинено адміністратором."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Завантажено кеш Firebase: {count} кореневих вузлів"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Файл кешу Firebase не знайдено, починається з порожнього кешу: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Не вдалося завантажити кеш firebase: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Перезавантажено кеш Firebase: {count} кореневих вузлів"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Файл кешу Firebase не знайдено: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Не вдалося перезавантажити кеш Firebase: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 Ви забанені в роботі бота! Для розблокування зверніться до {Config.ADMIN_USERNAME}\n<blockquote>P.S. Не покидайте канал - ви будете автоматично заблоковані ⛔️</blockquote>\n🌍Змінити мову /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Відеоформати не знайдено. Спроба завантажувача зображень…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram обмежив надсилання повідомлень.\n⏳ Будь ласка, зачекайте: {time_str}\nЩоб оновити таймер, надішліть URL ще 2 рази."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Натисніть кнопку, щоб скопіювати URL потоку, потім вставте його в додаток VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Натисніть кнопку, щоб скопіювати URL потоку, потім вставте його в додаток VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Помилка отримання посилання:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Помилка надсилання файлу форматів: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Не вдалося отримати формати:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Аналіз... (зачекайте 6 секунд)"
    AA_PROCESSING_MSG = "🔎 Аналізуємо..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Тег #{wrong} містить заборонені символи. Дозволені лише літери, цифри та _.\nБудь ласка, використовуйте: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Для роботи в групі потрібні права адміністратора. Будь ласка, зробіть роботу адміном цієї групи."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Привіт {first_name},\n \n<i>Цей бот🤖 може завантажувати будь-які відео в telegram безпосередньо.😊 Для отримання додаткової інформації натисніть <b>/help</b></i> 👈\n\n<blockquote>P.S. Завантаження 🔞NSFW контенту та файлів з ☁️Cloud Storage платне! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Не покидайте канал - вас заблокують від використання бота ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Немає файлів для видалення."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 All files removed successfully!\n\nRemoved files:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ ЗАЧЕКАЙТЕ, ДОКИ ЗАВЕРШИТЬСЯ ВАШЕ ПОПЕРЕДнє ЗАВАНТАЖЕННЯ"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "Екземпляр програми None у check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict має значення None, що дозволяє завантажувати"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict має значення None, що дозволяє вставляти субтитри"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: обмеження перевірки - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: ключі info_dict: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Вбудовування субтитрів пропущено: тривалість {duration}с перевищує обмеження {max_duration}с"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Вбудовування субтитрів пропущено: розмір {size_mb:.2f}MB перевищує обмеження {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Вбудовування субтитрів пропущено: якість {width}x{height} (мінімальна сторона {min_side}p) перевищує обмеження {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "список відтворення"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Range limit exceeded for {service}: {count} (maximum {max_count}).\n\nUse one of these commands to download maximum available files:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Range limit exceeded for {service}: {count} (maximum {max_count})\nUser ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "Постачальник маркерів PO вимкнено в конфігурації"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} не є доменом YouTube, пропускаючи маркер PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "Постачальник маркерів PO недоступний на {base_url}, повертаючись до стандартного вилучення YouTube"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "Кеш постачальника токенів PO очищено, доступність буде перевірено під час наступного запиту"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Екземпляр програми ще не доступний"
    HELPER_USER_NAME_MSG = "Користувач"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Виявлено очікування повені, сплячий режим {wait_seconds} секунд"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Виявлено очікування повені, але не вдалося отримати час, сплячий режим {retry_delay} секунд"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "Виявлено помилку msg_seqno, сплячий режим {retry_delay} секунд"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Конфігурація проксі не завершена, використовується пряме підключення"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Закрити"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Закрити"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Закрити"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Файл журналів видалено."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Файл тегів видалено."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Файл форматування видалено."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Видалено розділений файл."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Файл Mediainfo видалено."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Налаштування субтитрів видалено."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Налаштування клавіатури видалено."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Налаштування аргументів видалено."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 Налаштування NSFW видалено."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Налаштування проксі видалено."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Налаштування очікування повені видалено."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Закрити"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Команда завантаження відео"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Використання: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Приклади:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (direct order)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (reverse order)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Див. також: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Користувач {user_id} закрив команду add_bot_to_group"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Не вдалося отримати ідентифікатор YouTube"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Не вдалося завантажити мініатюру або вона завелика"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Виберіть мову аудіо"
    AA_NO_SUBTITLES_DETECTED_MSG = "Субтитри не виявлено"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Виберіть мову субтитрів"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Помилка автентифікації"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Обліковий запис не знайдено"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Обліковий запис недоступний"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Обмеження швидкості перевищено"
    GALLERY_DL_NETWORK_ERROR_MSG = "Помилка мережі"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Контент недоступний"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Географічні обмеження"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Потрібна перевірка"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Порушення політики"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Невідома помилка"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Завантаження розпочато</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Закрити"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Команда завантаження відео</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Використання: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Приклади:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Див. також: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Обмеження повені. Спробуйте пізніше."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Використання команди Cookie</b>

<code>/cookie</code> - Показати меню cookie
<code>/cookie youtube</code> - Завантажити YouTube cookies
<code>/cookie instagram</code> - Завантажити Instagram cookies
<code>/cookie tiktok</code> - Завантажити TikTok cookies
<code>/cookie x</code> або <code>/cookie twitter</code> - Завантажити Twitter/X cookies
<code>/cookie facebook</code> - Завантажити Facebook cookies
<code>/cookie custom</code> - Показати інструкції для власних cookies

<i>Доступні сервіси залежать від конфігурації бота.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Файл cookie видалено та кеш очищено."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Попереднє"
    SUBS_BACK_BUTTON_MSG = "🔙Назад"
    SUBS_OFF_BUTTON_MSG = "🚫 ВИМК"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - встановити мову"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - встановити мову з AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Дійсні опції:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 МОВА"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Контроль GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 ЧИСТО"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 ПЕЧИВО"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 ЗМІ"
    SETTINGS_INFO_BUTTON_MSG = "📖 ІНФО"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ БІЛЬШЕ"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Тільки cookies"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Логи "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Теги"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Формат"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Розділити"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 MediaInfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Субтитри"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Клавіатура"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Аргументи"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Проксі"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Чекайте повені"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Всі файли"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Завантажити мої 5 cookies"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Отримати YT-cookie браузера"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Перевірити файл cookie"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Завантажити власний cookie"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Змінити якість та формат"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Увімкнути/вимкнути MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Змінити розмір частини відео"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Завантажити відео як аудіо"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Налаштування мови субтитрів"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Як завантажувати плейлисти"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Завантажити зображення через gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Надіслати ваші #теги"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Отримати інструкції"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Надіслати ваші логи"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Довідка плейлиста"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - як це зробити"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Отримати прямі посилання на відео"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Увімкнути/вимкнути проксі"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Розкладка клавіатури"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Інлайн пошуковий помічник"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - аргументи yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - Налаштування розмиття NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Опції очищення</b>\n\nВиберіть, що очистити:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Мобільний: Активувати @vid пошук"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Мобільний: активуйте пошук @vid"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 ВИМКНЕНО"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 ПОВНИЙ"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2х3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL-адреса зображень]({url})"
    IMAGE_ERROR_MSG = "❌ Помилка: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Назад"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - власний формат"
    FORMAT_720P_MSG = "• <code>/format 720</code> - якість 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - якість 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - якість 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - конкретний ID формату"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - завжди показувати меню"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/найкраща якість"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Завжди питати (меню + кнопки)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Інші (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (найкраще для PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (найкраще для мобільного Telegram)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (МАКС якість)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Власний (введіть свій)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 З браузера"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Вконтакте"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Власний"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Режим введення автоматично закрито через неактивність (5 хвилин)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Скинути все"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Переглянути поточні"
    ARGS_BACK_BUTTON_MSG = "🔙 Назад"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Переслайте це повідомлення до ваших обраних, щоб зберегти ці налаштування як шаблон.</i> \n\n<i>Переслайте це повідомлення сюди назад, щоб застосувати ці налаштування.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Поточні аргументи yt-dlp:\n\nНемає налаштованих власних налаштувань.\n\n---\n\n<i>Переслайте це повідомлення до ваших обраних, щоб зберегти ці налаштування як шаблон.</i> \n\n<i>Переслайте це повідомлення сюди назад, щоб застосувати ці налаштування.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Поточні аргументи yt-dlp:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Експортувати налаштування"
    ARGS_SETTINGS_READY_MSG = "Налаштування готові до експорту! Переслайте це повідомлення до обраних, щоб зберегти."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Поточні аргументи yt-dlp:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Не вдалося розпізнати налаштування в повідомленні. Переконайтеся, що ви надіслали правильний шаблон налаштувань."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Налаштування успішно імпортовано!\n\nЗастосовані параметри: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Ключові налаштування:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Помилка збереження імпортованих налаштувань."
    ARGS_ERROR_IMPORTING_MSG = "❌ Під час імпорту налаштувань сталася помилка."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Завантажити файли Cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Виберіть сервіс для завантаження файлу cookie."
    COOKIE_MENU_SAVE_INFO_MSG = "Файли cookie будуть збережені як cookie.txt у вашій папці."
    COOKIE_MENU_TIP_HEADER_MSG = "Порада: Ви також можете використати пряму команду:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – завантажити та перевірити cookies"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – використати конкретне джерело за індексом (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Потім перевірте за допомогою <code>/check_cookie</code> (тестує на RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Завжди питати"
    SUBS_AUTO_TRANS_BUTTON_MSG = "АВТО/ПЕРЕКЛАД"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Посилання"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Дивитися"  # ТИМЧАСОВО ВИМКНЕНО: сервіс poketube не працює
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Опис"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ ОБРІЗКА"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Обрізка відео</b>\n\nТривалість відео: <b>{start_time} - {end_time}</b>\n\nБудь ласка, надішліть бажаний діапазон часу у форматі:\n<code>ГГ:ХХ:СС-ГГ:ХХ:СС</code>\n\nПриклад: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Невірний формат. Будь ласка, використовуйте: <code>ГГ:ХХ:СС-ГГ:ХХ:СС</code>\n\nПриклад: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Невірний діапазон. Час початку повинен бути меншим за час закінчення."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ Діапазон часу виходить за межі відео.\n\nТривалість відео: <b>{start_time} - {end_time}</b>\n\nВаш діапазон повинен бути в межах цих обмежень."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>Відео буде обрізано:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Частково завершено - {successful_uploads}/{total_files} аудіо файлів завантажено."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Аудіо успішно завантажено та надіслано - {total_files} файлів завантажено."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Приватний обліковий запис TikTok</b>\n\n"
        "Цей обліковий запис TikTok є приватним або всі відео є приватним.\n\n"
        "<b>💡 Рішення:</b>\n"
        "1. Підпишіться на обліковий запис @{username}\n"
        "2. Надішліть ваші cookies боту, використовуючи команду <code>/cookie</code>\n"
        "3. Спробуйте знову\n\n"
        "<b>Після оновлення cookies, спробуйте знову!</b>"
    )

    #######################################################
