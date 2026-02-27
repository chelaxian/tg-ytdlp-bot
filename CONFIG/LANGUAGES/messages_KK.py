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
    CREDITS_MSG = "<blockquote><i>Басқарушы</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Тілді өзгерту: /lang</b>"
    TO_USE_MSG = "<i>Бұл ботты пайдалану үшін @tg_ytdlp Telegram арнасына жазылуыңыз керек.</i>\nАрнаға қосылғаннан кейін <b>бейне сілтемеңізді қайта жіберіңіз, бот оны сіз үшін жүктейді</b> ❤️\n\n<blockquote>P.S. 🔞NSFW контент мүмкіндігіне байланысты - ☁️<b>Бұлттық сақтау</b>, 📁<b>Файл бөлісу</b>, 🔗<b>URL қысқартқыштар</b> және 🔞<b>Порно сайттары</b>нан жүктеу ақылы! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ @tg_ytdlp арнасын 🗑<b>жоймаңыз/жазылымнан шықпаңыз</b> және ботқа 🤖<b>URL/командаларды тым көп спамдамаңыз</b> - ботты пайдаланудан автоматты түрде тыйым салынасыз ⛔️</blockquote>"

    ERROR1 = "URL сілтемесі табылмады. <b>https://</b> немесе <b>http://</b> бар URL енгізіңіз"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Плейлистер (yt-dlp)</b>

Плейлисттерді жүктеу үшін оның URL мекенжайын соңында <code>*start*end</code> диапазондарымен жіберіңіз. Мысалы: <code>URL*1*5</code> (1-ден 5-ке дейін алғашқы 5 бейне).<code>URL*-1*-5</code> (1-ден 5-ке дейін соңғы 5 бейне).
Немесе <code>/vid БАСТАП-ДЕЙІН URL</code> пайдалана аласыз. Мысалы: <code>/vid 3-7 URL</code> (басынан 3-тен 7-ге дейін бейнелерді жүктейді). <code>/vid -3-7 URL</code> (соңынан 3-тен 7-ге дейін бейнелерді жүктейді). <code>/audio</code> командасы үшін де жұмыс істейді.

<b>Мысалдар:</b>

🟥 <b>YouTube плейлистінен бейне диапазоны:</b> (🍪 қажет)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(1-ден 5-ке дейін алғашқы 5 бейнені жүктейді)
🟥 <b>YouTube плейлистінен бір бейне:</b> (🍪 қажет)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(тек 3-ші бейнені жүктейді)

⬛️ <b>TikTok профилі:</b> (сіздің 🍪 қажет)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(пайдаланушы профилінен алғашқы 10 бейнені жүктейді)

🟪 <b>Instagram әңгімелері:</b> (сіздің 🍪 қажет)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(алғашқы 3 әңгімені жүктейді)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(альбомнан алғашқы 10 әңгімені жүктейді)

🟦 <b>VK бейнелері:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(пайдаланушы/топ профилінен алғашқы 3 бейнені жүктейді)

⬛️<b>Rutube арналары:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(арнадан 2-ден 4-ке дейін бейнелерді жүктейді)

🟪 <b>Twitch клиптері:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(арнадан алғашқы 3 клипті жүктейді)

🟦 <b>Vimeo топтары:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(топтан алғашқы 2 бейнені жүктейді)

🟧 <b>Pornhub модельдері:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(модель профилінен алғашқы 2 бейнені жүктейді)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(сіздің сұрауыңыз бойынша іздеу нәтижелерінен алғашқы 3 бейнені жүктейді)

және т.б...
<a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">қолдау көрсетілетін сайттар тізімі</a>н қараңыз
</blockquote>

<blockquote expandable>🖼 <b>Суреттер (gallery-dl)</b>

Көптеген платформалардан суреттер/фото/альбомдарды жүктеу үшін <code>/img URL</code> пайдаланыңыз.

<b>Мысалдар:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Диапазондар:</b>
<code>/img 11-20 https://example.com/album</code> — элементтер 11..20
<code>/img 11- https://example.com/album</code> — 11-ден соңына дейін (немесе бот лимиті)

<i>Қолдау көрсетілетін платформалар vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor және т.б. Толық тізім:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">gallery-dl қолдайтын сайттар</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Бейне Жүктеу Боты - Көмек</b>

📥 <b>Негізгі Пайдалану:</b>
• Кез келген сілтемені жіберіңіз → бот оны жүктейді
  <i>бот yt-dlp арқылы бейнелерді және gallery-dl арқылы суреттерді жүктеуге автоматты түрде тырысады.</i>
• <b>Бірнеше URL:</b> Сапа таңдау режимінде (<code>/format</code>) бір хабарламада <b>10 URL</b>-ға дейін жібере аласыз. Әр URL жаңа жолда немесе бос орындармен бөлінген.
• <code>/audio URL</code> → дыбысты шығару
• <code>/link [quality] URL</code> → тікелей сілтемелерді алу
• <code>/proxy</code> → барлық жүктеулер үшін проксиді қосу/өшіру
• Бейнеге мәтінмен жауап беру → тақырыпты өзгерту

📋 <b>Плейлистер және Диапазондар:</b>
• <code>URL*1*5</code> → алғашқы 5 бейнені жүктеу
• <code>URL*-1*-5</code> → соңғы 5 бейнені жүктеу
• <code>/vid 3-7 URL</code> → <code>URL*3*7</code> болады
• <code>/vid -3-7 URL</code> → <code>URL*-3*-7</code> болады

🍪 <b>Cookie және Жеке:</b>
• Жеке бейнелер үшін *.txt cookie жүктеу
• <code>/cookie [service]</code> → cookie'лерді жүктеу (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → индекске сәйкес көзді таңдау (1–N)
• <code>/cookies_from_browser</code> → браузерден шығару
• <code>/check_cookie</code> → cookie'ді тексеру
• <code>/save_as_cookie</code> → мәтінді cookie ретінде сақтау

🧹 <b>Тазалау:</b>
• <code>/clean</code> → тек медиа файлдары
• <code>/clean all</code> → бәрі
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Баптаулар:</b>
• <code>/settings</code> → баптаулар мәзірі
• <code>/format</code> → сапа және формат
• <code>/split</code> → бейнені бөліктерге бөлу
• <code>/mediainfo on/off</code> → медиа ақпараты
• <code>/nsfw on/off</code> → NSFW бұлыңғырлау
• <code>/tags</code> → сақталған тегтерді көру
• <code>/sub on/off</code> → субтитрлер
• <code>/keyboard</code> → пернетақта (OFF/1x3/2x3)

🏷️ <b>Тегтер:</b>
• URL кейін <code>#tag1#tag2</code> қосу
• Тегтер тақырыптарда пайда болады
• <code>/tags</code> → барлық тегтерді көру

🔗 <b>Тікелей Сілтемелер:</b>
• <code>/link URL</code> → ең жақсы сапа
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → нақты сапа

⚙️ <b>Жылдам Бұйрықтар:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → сапаны орнату
• <code>/keyboard off/1x3/2x3/full</code> → пернетақта орналасуы
• <code>/split 100mb-2000mb</code> → бөлік өлшемін өзгерту
• <code>/subs off/ru/en auto</code> → субтитр тілі
• <code>/list URL</code> → қолжетімді форматтар тізімі
• <code>/mediainfo on/off</code> → медиа ақпаратын қосу/өшіру
• <code>/proxy on/off</code> → барлық жүктеулер үшін проксиді қосу/өшіру

📊 <b>Ақпарат:</b>
• <code>/usage</code> → жүктеу тарихы
• <code>/search</code> → @vid арқылы ішкі іздеу

🖼 <b>Суреттер:</b>
• <code>URL</code> → сурет URL'лерін жүктеу
• <code>/img URL</code> → URL'ден суреттерді жүктеу
• <code>/img 11-20 URL</code> → нақты диапазонды жүктеу
• <code>/img 11- URL</code> → 11-ден соңына дейін жүктеу

👨‍💻 <i>Әзірлеуші:</i> @upekshaip
🤝 <i>Үлес қосушы:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Cookie файлыңызды <b><u>cookie.txt</u></b> ретінде сақтап, ботқа құжат ретінде жіберіңіз.\n\n"
        "Сіз cookie'лерді <b><u>/save_as_cookie</u></b> командасымен жай мәтін ретінде де жібере аласыз.\n"
        "<b><b><u>/save_as_cookie</u></b> пайдалану:</b>\n\n"
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
        "<b><u>Нұсқаулар:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message
    SEARCH_MSG = """
🔍 <b>Бейне іздеу</b>

@vid арқылы ішкі іздеуді іске қосу үшін төмендегі батырманы басыңыз.

<blockquote>ПК-де кез келген чатта <b>"@vid Your_Search_Query"</b> теру жеткілікті.</blockquote>
    """
    
    # Settings and Hints
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Сурет Жүктеу Командасы</b>\n\n"
        "Пайдалану: <code>/img URL</code>\n\n"
        "<b>Мысалдар:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Қолдау көрсетілетін платформалар (мысалдар):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor және т.б. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">толық тізім</a></blockquote>"
        "Сондай-ақ қараңыз: "
    )
    
    LINK_HINT_MSG = (
        "Сапа таңдауымен тікелей бейне сілтемелерін алыңыз.\n\n"
        "Пайдалану: /link + URL \n\n"
        "(мысалы /link https://youtu.be/abc123)\n"
        "(мысалы /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Топқа Бот Қосу</b>

Жақсартылған мүмкіндіктер мен жоғары лимиттер алу үшін боттарымды топтарыңызға қосыңыз!
————————————
📊 <b>Ағымдағы ТЕГІН Лимиттер (Боттың DM-інде):</b>
<blockquote>•🗑 Сұрыпталмаған барлық файлдардан шатаскан қоқыс 👎
• 1 файлдың максималды өлшемі: <b>8 GB </b>
• 1 файлдың максималды сапасы: <b>ШЕКСІЗ</b>
• 1 файлдың максималды ұзақтығы: <b>ШЕКСІЗ</b>
• Жүктеулердің максималды саны: <b>ШЕКСІЗ</b>
• Бір хабарламадағы максималды URL: <b>10</b> (тек сапа таңдау режимінде)
• 1 реттегі максималды плейлист элементтері: <b>50</b>
• 1 реттегі максималды TikTok бейнелері: <b>500</b>
• 1 реттегі максималды суреттер: <b>1000</b>
• URL жылдамдық лимиттері: <b>5/мин, 60/сағ, 1000/күн</b>
• Команда лимиті: <b>20/мин</b>
• 1 жүктеудің максималды уақыты: <b>2 сағат</b>
• 🔞 NSFW контенті ақылы! 1⭐️ = $0.02
• 🆓 БАСҚА БАРЛЫҚ МЕДИА ТОЛЫҚЫМЕН ТЕГІН
• 📝 Барлық контент логтары және кэштеу қайта жүктеу кезінде лезде қайталау үшін менің лог-арналарыма</blockquote>

💬<b>Бұл лимиттер тек субтитрі бар бейне үшін:</b>
<blockquote>• Максималды бейне+субтитр ұзақтығы: <b>1.5 сағат</b>
• Максималды бейне+субтитр файл өлшемі: <b>500 MB</b>
• Максималды бейне+субтитр сапасы: <b>720p</b></blockquote>
————————————
🚀 <b>Ақылы Топ Артықшылықтары (2️⃣x Лимиттер):</b>
<blockquote>•  🗂 Тақырыптар бойынша сұрыпталған құрылымдық таза медиа қоймасы 👍
•  📁 Боттар сіз оларды шақырған тақырыпта жауап береді
•  📌 Жүктеу прогрессімен автоматты түрде бекітілген мәртебе хабарламасы
•  🖼 /img командасы медианы 10 элементті альбомдар ретінде жүктейді
• 1 файлдың максималды өлшемі: <b>16 GB</b> ⬆️
• Бір хабарламадағы максималды URL: <b>20</b> ⬆️ (тек сапа таңдау режимінде)
• 1 реттегі максималды плейлист элементтері: <b>100</b> ⬆️
• 1 реттегі максималды TikTok бейнелері: 1000 ⬆️
• 1 реттегі максималды суреттер: 2000 ⬆️
• URL жылдамдық лимиттері: <b>10/мин, 120/сағ, 2000/күн</b> ⬆️
• Команда лимиті: <b>40/мин</b> ⬆️
• 1 жүктеудің максималды уақыты: <b>4 сағат</b> ⬆️
• 🔞 NSFW контенті: Толық метадеректермен тегін 🆓
• 📢 Топтар үшін менің арнама жазылудың қажеті жоқ
• 👥 Топтың барлық мүшелері ақылы функцияларға қол жеткізе алады!
• 🗒 Логтар жоқ / менің лог-арналарыма кэш жоқ! Топ баптауларында көшіру/қайталауды бас тарта аласыз</blockquote>

💬 <b>Субтитрі бар бейне үшін 2️⃣x лимиттер:</b>
<blockquote>• Максималды бейне+субтитр ұзақтығы: <b>3 сағат</b> ⬆️
• Максималды бейне+субтитр файл өлшемі: <b>1000 MB</b> ⬆️
• Максималды бейне+субтитр сапасы: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Баға және Орнату:</b>
<blockquote>• Баға: <b>$5/ай</b> топтағы 1 бот үшін
• Орнату: @iilililiiillliiliililliilliliiil-мен байланысыңыз
• Төлем: 💎TON немесе басқа әдістер💲
• Қолдау: Толық техникалық қолдау қосылған</blockquote>
————————————
Сіз боттарымды топыңызға қосып, тегін 🔞<b>NSFW</b>-ді ашып, барлық лимиттерді екі есеге (x2️⃣) көбейте аласыз.
Егер сіз топыңызға боттарымды пайдалануға рұқсат беруді қаласаңыз, маған хабарласыңыз @iilililiiillliiliililliilliliiil
————————————
💡<b>КЕҢЕС:</b> <blockquote>Сіз достарыңызбен кез келген соманы (мысалы, 100 адам) жинап, бүкіл топ үшін 1 сатып алу жасай аласыз - ТОПТЫҢ БАРЛЫҚ МҮШЕЛЕРІ ОСЫ ТОПТАҒЫ БОТТЫҢ БАРЛЫҚ ФУНКЦИЯЛАРЫНА ТОЛЫҚ ШЕКСІЗ ҚОЛ ЖЕТКІЗЕ АЛАДЫ тек <b>0.05$</b> үшін</blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW Режимі: ҚОСУЛҒАН✅</b>

• NSFW контенті бұлыңғырлаусыз көрсетіледі.
• Спойлерлер NSFW медиаға қолданылмайды.
• Контент бірден көрінетін болады

<i>Бұлыңғырлауды іске қосу үшін /nsfw off пайдаланыңыз</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW Режимі: ӨШІРІЛГЕН</b>

⚠️ <b>Бұлыңғырлау іске қосылды</b>
• NSFW контенті спойлер астында жасырылады   
• Көру үшін медиаға басу керек
• Спойлерлер NSFW медиаға қолданылады.

<i>Бұлыңғырлауды өшіру үшін /nsfw on пайдаланыңыз</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Жарамсыз параметр</b>

Пайдаланыңыз:
• <code>/nsfw on</code> - бұлыңғырлауды өшіру
• <code>/nsfw off</code> - bұлыңғырлауды іске қосу
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Кэшті тексеру...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Өңделуде..."
    DOWNLOADING_MSG = "📥 <b>Медиа жүктелуде...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Сурет жүктелуде...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Жүктеу аяқталды</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Жүктелді:"
    SENT_STATUS_MSG = "Жіберілді:"
    PENDING_TO_SEND_STATUS_MSG = "Жіберу күтуде:"
    TITLE_LABEL_MSG = "Тақырып:"
    MEDIA_COUNT_LABEL_MSG = "Медиа саны:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Жүктеу аяқталды, дыбыс өңделуде..."
    VIDEO_PROCESSING_MSG = "📽 Бейне өңделуде..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Кэштен жіберілді</b>\n\nЖіберілген альбомдар: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Бейне кэштен сәтті жіберілді."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Плейлист бейнелері кэштен жіберілді ({cached}/{total} файл)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} бейне кэштен жіберілді, жетіспейтіндер жүктелуде..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Кэштен жіберілді: {cached}\n🔄 Жүктеу жалғасуда..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Медианы талдау мүмкін болмады, максималды рұқсат етілген диапазонмен жалғастыру (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Медиа санын анықтау мүмкін болмады, максималды рұқсат етілген диапазонмен жалғастыру (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Жалпы медиа санын анықтау мүмкін болмады, көрсетілген диапазонмен жалғастыру {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>Жарамсыз URL</b>\n\nhttp:// немесе https:// басталатын жарамды URL енгізіңіз"

    ERROR_OCCURRED_MSG = "❌ <b>Қате орын алды</b>\n\n<code>{url}</code>\n\nҚате: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Бейне бұл қатесі: {error}"
    ERROR_UNKNOWN_MSG = "❌ Белгісіз қате: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Бейнелерді жүктеу үшін дискіде жеткілікті орын жоқ."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Файл өлшемі {limit} GB лимитінен асып кетті. Рұқсат етілген өлшем ішінде кішірек файл таңдаңыз."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>Барлық қолжетімді прокси-серверлермен бейнені жүктеу сәтсіз аяқталды</b>\n\nПрокси-сервер арқылы барлық жүктеу әрекеттері сәтсіз аяқталды.\nКөріңіз:\n• Прокси-сервердің жұмыс істеуін тексеріңіз\n• Тізімнен басқа прокси-серверді көріңіз\n• Прокси-серверсіз жүктеңіз (егер мүмкін болса)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Сілтеме алу қатесі:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram хабарлама жіберуді шектеді.\n⏳ Күтіңіз: {time}\nТаймерді жаңарту үшін URL-ді қайта 2 рет жіберіңіз."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram хабарлама жіберуді шектеді.\n⏳ Күтіңіз: \nТаймерді жаңарту үшін URL-ді қайта 2 рет жіберіңіз."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Субтитрлерді жүктеу сәтсіз аяқталды"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Тікелей Стрим Сілтемелері</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Тақырып:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Ұзақтығы:</b> {duration} сек\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Қате: Түпнұсқа хабарлама табылмады."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Тег #{tag} тыйым салынған таңбаларды қамтиды. Тек әріптер, сандар және _ рұқсат етілген.\nПайдаланыңыз: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Плейлист бейнелері жіберілді: {sent}/{total} файл."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>Плейлист бойынша кеңес</b>

Сіз диапазонды көрсетпей плейлист сілтемесін жібердіңіз. Бот автоматты түрде бірінші бейнені жүктеді (<code>*1*1</code>).

<b>Плейлисттен бірнеше бейнені жүктеу үшін диапазонды көрсетіңіз:</b>
• <code>URL*1*5</code> — алғашқы 5 бейне (1-ден 5-ке дейін, соның ішінде)
• <code>URL*3*3</code> — тек 3-бейне
• <code>/vid 1-10 URL</code> — балама формат

Көбірек біліңіз: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ Кэштен жіберілді: {cached}/{total} файл."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Стрим сілтемелерін алу сәтсіз аяқталды"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Cookie файлдарын жүктеу үшін браузерді қолдану:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Бұл жүйеде браузер табылмады. Сіз cookie файлдарын URL-ден жүктей аласыз немесе серверді таңдай аласыз:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Браузерді Ашу</b> - мини-қосымшада браузер мәртебесін бақылау"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Браузерді Ашу"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Қашықтықтағы URL-ден Жүктеу"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie файлы fallback арқылы орнатылды және cookie.txt ретінде сақталды"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Қолдау көрсету браузерлер табылмады және COOKIE_URL бапталмаған. /cookie файл немесе cookie.txt жүктеңіз."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL .txt файлына сілтеуі керек."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fallback cookie файлы тым үлкен (>100 КБ)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fallback cookie көзі қолжетімсіз (мәртебе {status}). /cookie көріңіз немесе cookie.txt жүктеңіз."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Fallback cookie файлын жүктеу қатесі. /cookie файлын көріңіз немесе cookie.txt файлын жүктеңіз."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Fallback cookie жүктеу кезінде күтпеген қате."
    BTN_CLOSE = "🔚Жабу"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Жарамсыз boolean мәні"
    ARGS_CLOSED_MSG = "Жабылды"
    ARGS_ALL_RESET_MSG = "✅ Барлық аргументтер қалпына келтірілді"
    ARGS_RESET_ERROR_MSG = "❌ Аргументтерді қалпына келтіру кезінде қате"
    ARGS_INVALID_PARAM_MSG = "❌ Жарамсыз параметр"
    ARGS_BOOL_SET_MSG = "{value} деп орнатылды"
    ARGS_BOOL_ALREADY_SET_MSG = "Қазірдің өзінде {value} деп орнатылған"
    ARGS_INVALID_SELECT_MSG = "❌ Жарамсыз таңдау мәні"
    ARGS_VALUE_SET_MSG = "{value} деп орнатылды"
    ARGS_VALUE_ALREADY_SET_MSG = "Қазірдің өзінде {value} деп орнатылған"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Ағымдағы мән:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Мысалдар:</b>\n• <code>default</code> - Бастапқы XFF стратегиясын пайдалану\n• <code>never</code> - XFF тақырыпшасын ешқашан пайдаланбау\n• <code>US</code> - АҚШ ел коды\n• <code>GB</code> - Ұлыбритания ел коды\n• <code>DE</code> - Германия ел коды\n• <code>FR</code> - Франция ел коды\n• <code>JP</code> - Жапония ел коды\n• <code>192.168.1.0/24</code> - IP блок (CIDR)\n• <code>10.0.0.0/8</code> - Жеке IP диапазоны\n• <code>203.0.113.0/24</code> - Жалпы IP блок\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Ескерту:</b> Бұл --geo-bypass опцияларын ауыстырады. CIDR белгілеуінде кез келген 2 әріпті ел кодын немесе IP блокты пайдаланыңыз.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Мысал:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Жаңа мәніңізді жіберіңіз."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Диапазон:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Сан жіберіңіз."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Мысалдар:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Ескерту:</b> Бұл тақырыпшалар бар Referer және User-Agent тақырыпшаларына қосылады.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Ағымдағы yt-dlp Аргументтері:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - True/False ауыстырғыштары\n• 📋 <b>Select</b> - Опциялардан таңдау\n• 🔢 <b>Numeric</b> - Сан енгізу\n• 📝🔧 <b>Text</b> - Мәтін/JSON енгізу</blockquote>\n\nБұл баптаулар барлық жүктеулеріңізге қолданылады."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "IPv6 қосылымдарын мәжбүрлеу",
        "force_ipv4": "IPv4 қосылымдарын мәжбүрлеу", 
        "no_live_from_start": "Тікелей эфирлерді басынан бастап жүктемейді",
        "live_from_start": "Тікелей эфирлерді басынан бастап жүктеу",
        "no_check_certificates": "HTTPS сертификат тексеруін басу",
        "check_certificate": "SSL сертификатты тексеру",
        "no_playlist": "Тек бір бейнені жүктеу, плейлист емес",
        "embed_metadata": "Бейне файлына метадеректерді енгізу",
        "embed_thumbnail": "Бейне файлына эскизді енгізу",
        "write_thumbnail": "Эскизді файлға жазу",
        "ignore_errors": "Жүктеу қателерін елемеу және жалғастыру",
        "legacy_server_connect": "Ескі сервер қосылымдарын рұқсат ету",
        "concurrent_fragments": "Бір мезгілде жүктелетін фрагменттер саны",
        "xff": "X-Forwarded-For тақырыпшасы стратегиясы",
        "user_agent": "User-Agent тақырыпшасы",
        "impersonate": "Браузерді эмуляциялау",
        "referer": "Referer тақырыпшасы",
        "geo_bypass": "Географиялық шектеулерді айналып өту",
        "hls_use_mpegts": "HLS үшін MPEG-TS пайдалану",
        "no_part": ".part файлдарын пайдаланбау",
        "no_continue": "Жартылай жүктеулерді жалғастырмау",
        "audio_format": "Дыбыс форматы",
        "video_format": "Бейне форматы",
        "merge_output_format": "Біріктіру шығыс форматы",
        "send_as_file": "Файл ретінде жіберу",
        "username": "Пайдаланушы аты",
        "password": "Құпия сөз",
        "twofactor": "Екі факторлы аутентификация коды",
        "min_filesize": "Минималды файл өлшемі (MB)",
        "max_filesize": "Максималды файл өлшемі (MB)",
        "playlist_items": "Плейлист элементтері",
        "date": "Күні",
        "datebefore": "Күні бұрын",
        "dateafter": "Күні кейін",
        "http_headers": "HTTP тақырыпшалары",
        "sleep_interval": "Ұйықтау интервалы",
        "max_sleep_interval": "Максималды ұйықтау интервалы",
        "retries": "Қайталау саны",
        "http_chunk_size": "HTTP фрагмент өлшемі",
        "sleep_subtitles": "Субтитрлер үшін ұйықтау"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp Аргументтерін Баптау</b>\n\n<blockquote>📋 <b>Топтар:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp Аргументтерін Баптау</b>\n\n"
        "<blockquote>📋 <b>Топтар:</b>\n"
        "• ✅/❌ <b>Boolean</b> - True/False ауыстырғыштары\n"
        "• 📋 <b>Select</b> - Опциялардан таңдау\n"
        "• 🔢 <b>Numeric</b> - Сан енгізу\n"
        "• 📝🔧 <b>Text</b> - Мәтін/JSON енгізу</blockquote>\n\n"
        "Бұл баптаулар барлық жүктеулеріңізге қолданылады."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Күтіңіз..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Қате орын алды"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Енгізу режимі белсенділік жоқтығынан желіде жабылды (5 минут)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Енгізу ықтимал қауіпті мазмұнды қамтиды: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Енгізу тым ұзын (максимум 1000 таңба)"
    ARGS_INVALID_URL_MSG = "❌ Жарамсыз URL форматы. http:// немесе https:// басталуы керек"
    ARGS_INVALID_JSON_MSG = "❌ Жарамсыз JSON форматы"
    ARGS_NUMBER_RANGE_MSG = "❌ Сан {min_val} және {max_val} арасында болуы керек"
    ARGS_INVALID_NUMBER_MSG = "❌ Жарамсыз сан форматы"
    ARGS_DATE_FORMAT_MSG = "❌ Күн YYYYMMDD форматында болуы керек (мысалы, 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Жыл 1900 және 2100 арасында болуы керек"
    ARGS_MONTH_RANGE_MSG = "❌ Ай 01 және 12 арасында болуы керек"
    ARGS_DAY_RANGE_MSG = "❌ Күн 01 және 31 арасында болуы керек"
    ARGS_INVALID_DATE_MSG = "❌ Жарамсыз күн форматы"
    ARGS_INVALID_XFF_MSG = "❌ XFF 'default', 'never', ел коды (мысалы, US) немесе IP блок (мысалы, 192.168.1.0/24) болуы керек"
    ARGS_NO_CUSTOM_MSG = "Арнайы аргументтер орнатылмаған. Барлық параметрлер бастапқы мәндерді пайдаланады."
    ARGS_RESET_SUCCESS_MSG = "✅ Барлық аргументтер бастапқы мәндерге қалпына келтірілді."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Мәтін тым ұзын. Максимум 500 таңба."
    ARGS_ERROR_PROCESSING_MSG = "❌ Кіріс өңдеу кезінде қате орын алды. Қайталап көріңіз."
    ARGS_BOOL_INPUT_MSG = "❌ Файл ретінде жіберу опциясы үшін 'True' немесе 'False' енгізіңіз."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Жарамды сан беріңіз."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Бұл опцияны қосу/өшіру үшін <code>True</code> немесе <code>False</code> жіберіңіз."
    ARGS_JSON_VALUE_REQUEST_MSG = "Жарамды JSON жіберіңіз."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Сізде әлі тегтер жоқ."
    TAGS_MESSAGE_CLOSED_MSG = "Тег хабарламасы жабылды."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Субтитрлер өшірілді және Always Ask режимі өшірілді."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Always Ask қосылды."
    SUBS_LANGUAGE_SET_MSG = "✅ Субтитр тілі мынаған орнатылды: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️ЕСКЕРТПЕ: жоғары CPU әсеріне байланысты бұл функция өте баяу (нақты уақытқа жақын) және мыналармен шектеледі:\n"
        "- 720p максималды сапа\n"
        "- 1.5 сағат максималды ұзақтық\n"
        "- 500mb максималды бейне өлшемі</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Жылдам командалар:</b>\n"
        "• <code>/subs off</code> - субтитрлерді өшіру\n"
        "• <code>/subs on</code> - Always Ask режимін қосу\n"
        "• <code>/subs ru</code> - тілді орнату\n"
        "• <code>/subs ru auto</code> - AUTO/TRANS арқылы тілді орнату"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Субтитрлер өшірілген"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Таңдалған тіл: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Субтитрлер орнатылуда..."
    SUBS_DISABLED_ERROR_MSG = "❌ Субтитрлер өшірілген. Баптау үшін /subs пайдаланыңыз."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Субтитрлерді жүктеу тек YouTube үшін қолдайды."
    SUBS_CAPTION_MSG = (
        "<b>💬 Субтитрлер</b>\n\n"
        "<b>Бейне:</b> {title}\n"
        "<b>Тіл:</b> {lang}\n"
        "<b>Түрі:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Субтитрлер SRT файлы пайдаланушыға жіберілді."
    SUBS_ERROR_PROCESSING_MSG = "❌ Субтитр файлын өңдеу кезінде қате."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Субтитрлерді жүктеу сәтсіз аяқталды."
    SUBS_ERROR_MSG = "❌ Субтитрлерді жүктеу кезінде қате: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Бөлшек өлшемін келесіге орнату: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **Жарамсыз өлшем!**\n\n"
        "**Жарамды диапазон:** 100MB-ден 2GB-ға дейін\n\n"
        "**Жарамды форматтар:**\n"
        "• `100mb` - `2000mb` (мегабайт)\n"
        "• `0.1gb` - `2gb` (гигабайт)\n\n"
        "**Мысалдар:**\n"
        "• `/split 100mb` - 100 мегабайт\n"
        "• `/split 500mb` - 500 мегабайт\n"
        "• `/split 1.5gb` - 1.5 гигабайт\n"
        "• `/split 2gb` - 2 гигабайт\n"
        "• `/split 2000mb` - 2000 мегабайт (2GB)\n\n"
        "**Алдын ала орнатылғандар:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Бейнені бөлу үшін максималды бөлік өлшемін таңдаңыз:**\n\n"
        "**Диапазон:** 100MB-ден 2GB-ға дейін\n\n"
        "**Жылдам командалар:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Мысалдар:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Меню жабылды."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Бот параметрлері</b>\n\nКатегория таңдаңыз:"
    SETTINGS_MENU_CLOSED_MSG = "Меню жабылды."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Clean Options</b>\n\nChoose what to clean:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nChoose an action:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIA</b>\n\nChoose an action:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nChoose an action:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ MORE COMMANDS</b>\n\nChoose an action:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Команда орындалды."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Су тасқыны шегі. Кейінірек көріңіз."
    SETTINGS_HINT_SENT_MSG = "Анықтама жіберілді."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Іздеу көмекшісі ашылды."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Белгісіз пәрмен."
    SETTINGS_HINT_CLOSED_MSG = "Кеңес жабық."
    SETTINGS_HELP_SENT_MSG = "Пайдаланушыға көмек txt жіберілді"
    SETTINGS_MENU_OPENED_MSG = "/settings менюсі ашылды"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Іздеу көмекшісі жабылды"
    SEARCH_CLOSED_MSG = "Жабық"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Прокси {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Прокси параметрлерін сақтау қатесі."
    PROXY_MENU_TEXT_MSG = "Барлық yt-dlp операциялары үшін прокси серверін пайдалануды қосу немесе өшіру?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Барлық yt-dlp операциялары үшін прокси серверлерді ({config_count} + {file_count} қолжетімді) пайдалануды қосу немесе өшіру керек пе?\n\nБАРЛЫҚ (АВТО) қосылған кезде проксилер кездейсоқ әдіс арқылы таңдалады."
    PROXY_MENU_CLOSED_MSG = "Меню жабылды."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Прокси қосылған. Барлық yt-dlp операциялары проксиді пайдаланады."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Прокси қосылған. Барлық yt-dlp әрекеттері {count} прокси сервері{method}h {әдіс} таңдау әдісін пайдаланады."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Прокси қосылған (БАРЛЫҚ АВТО режимі).\n\n📊 Бот прокси-серверлерді келесі ретпен сынап көреді:\nConfig.py сайтынан 1️⃣ {config_count} прокси\nTXT/proxy.txt файлынан 2️⃣ {file_count} прокси\n\n🔄 Барлық прокси-серверлер сәтті қосылымға дейін дәйекті түрде сыналады."
    PROXY_DISABLED_MSG = "❌ Прокси өшірілген."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Прокси параметрлерін сақтау қатесі."
    PROXY_ENABLED_CALLBACK_MSG = "Прокси қосылды."
    PROXY_DISABLED_CALLBACK_MSG = "Прокси өшірілген."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ АЛДЫҢҒЫ ЖҮКТЕП АЛУ АЯТҚАНДАЙ КҮТІҢІЗ"
    AUDIO_HELP_MSG = (
        "<b>🎧 Аудио Жүктеу Командасы</b>\n\n"
        "Қолдану: <code>/audio URL</code>\n\n"
        "<b>Мысалдар:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Сондай-ақ қараңыз: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Аудио кеңесі жабылды."
    PLAYLIST_HELP_CLOSED_MSG = "Плейлист көмегі жабылды."
    USERLOGS_CLOSED_MSG = "Журналдар хабары жабылды."
    HELP_CLOSED_MSG = "Анықтама жабылды."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW Blur Settings</b>\n\nNSFW content is <b>{status}</b>.\n\nChoose whether to blur NSFW content:"
    NSFW_MENU_CLOSED_MSG = "Меню жабылды."
    NSFW_BLUR_DISABLED_MSG = "NSFW бұлыңғырлығы өшірілген."
    NSFW_BLUR_ENABLED_MSG = "NSFW бұлыңғырлау қосылды."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW бұлыңғырлығы өшірілген."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW бұлыңғырлау қосылды."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Жүктелген файлдар үшін MediaInfo жіберуді қосу немесе өшіру?"
    MEDIAINFO_MENU_CLOSED_MSG = "Меню жабылды."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo қосылды. Жүктеуден кейін файл ақпараты жіберіледі."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo өшірілген."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo қосылды."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo өшірілген."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Қолжетімді форматтар тізімі</b>\n\n"
        "URL үшін қолжетімді бейне/аудио форматтарын алыңыз.\n\n"
        "<b>Пайдалану:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Мысалдар:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Формат ID-лерін қалай пайдалануға болады:</b>\n"
        "Тізімді алғаннан кейін нақты формат ID пайдаланыңыз:\n"
        "• <code>/format id 401</code> - формат 401 жүктеу\n"
        "• <code>/format id401</code> - жоғарыдағыдай\n"
        "• <code>/format id140 audio</code> - формат 140-ты MP3 аудио ретінде жүктеу\n\n"
        "Бұл команда жүктеуге болатын барлық қолжетімді форматтарды көрсетеді."
    )
    LIST_PROCESSING_MSG = "🔄 Қолжетімді форматтарды алуда..."
    LIST_INVALID_URL_MSG = "❌ http:// немесе https:// басталатын жарамды URL енгізіңіз"
    LIST_CAPTION_MSG = (
        "📃 Қолжетімді форматтар:\n<code>{url}</code>\n\n"
        "💡 <b>Форматты қалай орнатуға болады:</b>\n"
        "• <code>/format id 134</code> - Нақты формат ID жүктеу\n"
        "• <code>/format 720p</code> - Сапа бойынша жүктеу\n"
        "• <code>/format best</code> - Ең жақсы сапаны жүктеу\n"
        "• <code>/format ask</code> - Әрдайым сапаны сұрау\n\n"
        "{audio_note}\n"
        "📋 Жоғарыдағы тізімнен формат ID пайдаланыңыз"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Тек аудио форматтары:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Формат 140-ті MP3 аудио ретінде жүктеу\n"
        "• <code>/format id140 audio</code> - жоғарыдағыдай\n"
        "Бұлар MP3 аудио файлдары ретінде жүктеледі.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Формат файлын жіберу қатесі: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Форматтарды алу мүмкін болмады:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Команданы өңдеу кезінде қате орын алды"
    LIST_ERROR_CALLBACK_MSG = "Қате орын алды"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Формат ID-лерін қалай пайдалануға болады:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Тізімді алғаннан кейін нақты формат ID пайдаланыңыз:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - формат 401 жүктеу\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - жоғарыдағыдай\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - формат 140-ті MP3 аудио ретінде жүктеу\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - жоғарыдағыдай\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Тек аудио форматтары анықталды: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Бұл форматтар MP3 аудио файлдары ретінде жүктеледі.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Тек бейне форматтары:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Жоғарыдағы тізімнен формат ID пайдаланыңыз"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Қолдану:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>Мысалдар:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - ең жақсы сапа\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p немесе төменірек\n"
        "• /link 720p https://youtube.com/watch?v=... - жоғарыдағыдай\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K немесе төменірек\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K немесе төменірек"
        "</blockquote>\n\n"
        "<b>Сапа:</b> 1-ден 10000-ге дейін (мысалы, 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Жарамды URL енгізіңіз"
    LINK_PROCESSING_MSG = "🔗 Тікелей сілтемені алуда..."
    LINK_DURATION_MSG = "⏱ <b>Ұзақтығы:</b> {duration} сек\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Бейне ағыны:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Аудио ағыны:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Пернетақта параметрі жаңартылды!**\n\nЖаңа параметр: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Жарамсыз аргумент!**\n\n"
        "Жарамды опциялар: `off`, `1x3`, `2x3`, `full`\n\n"
        "Мысал: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Пернетақта параметрлері**\n\n"
        "Ағымдағы: **{current}**\n\n"
        "Опция таңдаңыз:\n\n"
        "Немесе қолданыңыз: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 пернетақта іске қосылды!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Пернетақта жасырылды"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3 пернетақта іске қосылды!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3 пернетақта іске қосылды!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Эмодзи пернетақтасы іске қосылды!"
    KEYBOARD_ERROR_APPLYING_MSG = "Пернетақта параметрін {setting} қолдану қатесі: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Формат орнатылды: Әрдайым Сұрау. URL жіберген сайын сапаны сұрайды."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Формат орнатылды: Әрдайым Сұрау. URL жіберген сайын сапы сұрайды."
    FORMAT_BEST_UPDATED_MSG = "✅ Формат ең жақсы сапаға жаңартылды (AVC+MP4 басымдық):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Формат ID {id} жаңартылды:\n{format}\n\n💡 <b>Ескерту:</b> Егер бұл тек аудио формат болса, ол MP3 аудио файлы ретінде жүктеледі."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Формат ID {id} жаңартылды (тек аудио):\n{format}\n\n💡 Бұл MP3 аудио файлы ретінде жүктеледі."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Формат сапа {quality} жаңартылды:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Формат жаңартылды:\n{format}"
    FORMAT_MENU_MSG = (
        "Формат опциясын таңдаңыз немесе пайдалана отырып теңшелетін жіберіңіз:\n"
        "• <code>/format &lt;format_string&gt;</code> - теңшелетін формат\n"
        "• <code>/format 720</code> - 720p сапа\n"
        "• <code>/format 4k</code> - 4K сапа\n"
        "• <code>/format 8k</code> - 8K сапа\n"
        "• <code>/format id 401</code> - нақты формат ID\n"
        "• <code>/format ask</code> - әрдайым мәзірді көрсету\n"
        "• <code>/format best</code> - bv+ba/best сапа"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Теңшелетін форматты пайдалану үшін, команданы келесі пішінде жіберіңіз:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "<code>bestvideo+bestaudio/best</code> орнына қалаған формат жолын қойыңыз."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Қалаған ажыратымдылық пен кодекті таңдаңыз:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Пішім: Әрқашан сұрау. Енді URL мекенжайын жіберген сайын сізге сапа сұралады."
    FORMAT_UPDATED_MSG = "✅ Формат жаңартылды:\n{format}"
    FORMAT_SAVED_MSG = "✅ Формат сақталды."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Формат таңдауы жаңартылды."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Теңшелетін формат мәзірі жабылды"
    FORMAT_CODEC_SET_MSG = "✅ Кодек {codec} орнатылды"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Браузер таңдауы жаңартылды."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Қол жеткізу қол жетімсіз. Тек әкімші."
    ACCESS_DENIED_ADMIN = "❌ Қол жеткізу қол жетімсіз. Тек әкімші."
    WELCOME_MASTER = "Қош келдіңіз, Қожайын 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Кешіріңіз... Жүктеу кезінде қате орын алды."
    SIZE_LIMIT_EXCEEDED = "❌ Файл өлшемі {max_size_gb} GB шегінен асып кетті. Рұқсат етілген өлшем ішінде кішірек файлды таңдаңыз."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Скрипт табылмады: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ {script_path} пайдаланып жаңа Firebase дампты жүктеуде ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase кэш сәтті қайта жүктелді!"
    ADMIN_CACHE_FAILED_MSG = "❌ Firebase кэшін қайта жүктеу мүмкін болмады. {cache_file} бар екенін тексеріңіз."
    ADMIN_ERROR_RELOADING_MSG = "❌ Кэшті қайта жүктеу қатесі: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ {script_path} іске қосу қатесі:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Промо хабарлама барлық басқа пайдаланушыларға жіберілді</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Промо хабарламаны жібере алмайды. Хабарламаға жауап беруге тырысыңыз\nНемесе қандай да бір қате орын алды</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ Пайдаланушы әлі ешбір мазмұн жүктемеді...</b> Логтарда жоқ"
    ADMIN_INVALID_COMMAND_MSG = "❌ Жарамсыз команда"
    ADMIN_NO_DATA_FOUND_MSG = "❌ Кэште <code>{path}</code> үшін деректер табылмады"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Кезек бос — әлі ешкім арнадан шыққан жоқ."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Тыйым салу кезегі</b>\nКүтудегі жалпы: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (кетті: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… және тағы {extra} пайдаланушылар."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "/block_user show • барлығы • авто • 10с пайдаланыңыз"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Бөгелген пайдаланушылар кезекте: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Автоматты блоктау қосылды: жаңа шыққандарға бірден тыйым салынады."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Автоматты блоктау өшірілген."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Жоспарланған автоматты блоктау терезесі әрбір {interval} үшін орнатылды."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Соңғы {hours} сағаттағы арна белсенділігі журналы (2 күн)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 Соңғы {hours} сағат (2 күн{joined}PLACEHOLDER_2__oined}, сол жақта {сол жақта)."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Соңғы {hours} сағатта (2 күн) әрекет жоқ."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Барлығы: 🟢 {joined} j{left} 🔴 {сол жақта} қалды."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Арна әрекеттерінің журналына кіру мүмкін емес. Боттар әкімші журналдарын оқи алмайды. Бұл мүмкіндікті қосу үшін CHANNEL_GUARD_SESSION_STRING конфигурациясын пайдаланушы сеансымен қамтамасыз етіңіз."
    BAN_TIME_USAGE_MSG = "❌ Қолданылуы: {command} <10с|6мин|5сағ|4д|3ж|2М|1ж>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ 10s, 6m, 5h, 4d, 3w, 2M немесе 1y сияқты пішімдерді пайдаланыңыз."
    BAN_TIME_SET_MSG = "🕒 Арна журналын сканерлеу аралығы {interval} мәніне орнатылды."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Арна сканерлеу есебі\n"
        "Орындалды: {run_ts}\n"
        "Аралық: {interval}\n"
        "Жаңа кетушілер: {new_leavers}\n"
        "Автоматты тыйым салулар: {auto_banned}\n"
        "Күтуде: {pending}\n"
        "Соңғы event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Қолдану: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Әкімші әкімшіні жоюға құқығы жоқ"
    ADMIN_USER_BLOCKED_MSG = "Пайдаланушы бұғатталды 🔒❌\n \nID: <code>{user_id}</code>\nБұғаттау күні: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> қазірдің өзінде бұғатталған ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Кешіріңіз! Сіз әкімші емессіз"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Қолдану: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Пайдаланушы бұғаттан босатылды 🔓✅\n \nID: <code>{user_id}</code>\nБұғаттан босату күні: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> қазірдің өзінде бұғаттан босатылған ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Бұғаттан босатылған пайдаланушылар: {count}\n⏱ Уақыт белгісі: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Қолдану: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Пайдаланушы елемеуден өткізілді 👁️❌\n \nID: <code>{user_id}</code>\nЕлемеуден өткізілген күні: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> қазірдің өзінде елемеуден өткізілген ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Қолдану: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Пайдаланушы енді елемеуден өткізілмейді 👁️✅\n \nID: <code>{user_id}</code>\nЕлемеуден өткізілмеген күні: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> елемеуден өткізілмейді ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Бот жұмыс уақыты -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Кэшті тазарту үшін URL енгізіңіз.\nҚолдану: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Жарамды URL енгізіңіз.\nҚолдану: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ URL үшін кэш сәтті тазартылды:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Бұл сілтеме үшін кэш табылмады."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Кэшті тазарту қатесі: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Қол жеткізу қол жетімсіз. Тек әкімші."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Порн тізімін жаңарту скрипті іске қосылды: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Скрипт сәтті аяқталды!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Скрипт сәтті аяқталды!\n\nШығару:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Скрипт {returncode} қайтару кодымен сәтсіз аяқталды:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Скриптті іске қосу қатесі: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Порн және доменмен байланысты кэштерді қайта жүктеуде..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Порн кэштері сәтті қайта жүктелді!\n\n"
        "📊 Ағымдағы кэш мәртебесі:\n"
        "• Порн домендері: {porn_domains}\n"
        "• Порн кілт сөздері: {porn_keywords}\n"
        "• Қолдау көрсетілетін сайттар: {supported_sites}\n"
        "• АҚ ТІЗІМ: {whitelist}\n"
        "• СҰР ТІЗІМ: {greylist}\n"
        "• ҚАРА ТІЗІМ: {black_list}\n"
        "• АҚ КІЛТ СӨЗДЕР: {white_keywords}\n"
        "• ПРОКСИ ДОМЕНДЕР: {proxy_domains}\n"
        "• ПРОКСИ_2 ДОМЕНДЕР: {proxy_2_domains}\n"
        "• ТАЗА СҰРАУ: {clean_query}\n"
        "• COOKIE ЖОҚ ДОМЕНДЕР: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Порн кэшін қайта жүктеу қатесі: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Тексеру үшін URL енгізіңіз.\nҚолдану: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Жарамды URL енгізіңіз.\nҚолдану: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 URL-ді NSFW мазмұны үшін тексеруде...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Порн тексеру нәтижесі</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Мәртебе:</b> <b>{status_text}</b>\n\n"
        "<b>Түсіндіру:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ URL-ді тексеру қатесі: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Cookie-лар тазартылды."
    CLEAN_LOGS_CLEANED_MSG = "логтар тазартылды."
    CLEAN_TAGS_CLEANED_MSG = "тегтер тазартылды."
    CLEAN_FORMAT_CLEANED_MSG = "пішімі тазартылды."
    CLEAN_SPLIT_CLEANED_MSG = "бөлінген."
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfo тазартылды."
    CLEAN_SUBS_CLEANED_MSG = "Субтитр параметрлері тазартылды."
    CLEAN_KEYBOARD_CLEANED_MSG = "Пернетақта параметрлері тазартылды."
    CLEAN_ARGS_CLEANED_MSG = "Args параметрлері тазартылды."
    CLEAN_NSFW_CLEANED_MSG = "NSFW параметрлері тазартылды."
    CLEAN_PROXY_CLEANED_MSG = "Прокси параметрлері тазартылды."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Су тасқынын күту параметрлері тазартылды."
    CLEAN_ALL_CLEANED_MSG = "Барлық файлдар тазартылды."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nӘрекетті таңдаңыз:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Cookie файлы сақталды"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ YouTube емес cookie файлдары үшін тексеру өткізіп жіберілді"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Cookie файлы бар, бірақ пішімі дұрыс емес"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Cookie файлы табылмады."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 YouTube cookie файлдарын тексеру басталуда...\n\nCookie файлдарыңызды тексеріп, растау кезінде күтіңіз."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Сіздің YouTube cookie файлдарыңыз дұрыс жұмыс істейді!\n\nЖаңаларын жүктеудің қажеті жоқ."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Сіздің YouTube cookie файлдарыңыздың мерзімі аяқталған немесе жарамсыз.\n\n🔄 Жаңа cookie файлдарын жүктеуде..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} cookie файлының көзі конфигурацияланбаған!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} cookie файлының көзі .txt файлы болуы керек!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Range limit exceeded: {range_count} files requested (maximum {max_img_files}).\n\nUse one of these commands to download maximum available files:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Жабу"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Медиа шегінен асып кетті: {count} файл сұралды (максимум {max_count}).\n\nМаксималды қолжетімді файлдарды жүктеу үшін мына командалардың бірін пайдаланыңыз:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Сілтемеден <b>{count}</b> медиа элементі табылды"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Жүктеп алу ауқымын таңдаңыз:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Браузер имитациясы"
    ARGS_REFERER_DESC_MSG = "Анықтама тақырыбы"
    ARGS_USER_AGENT_DESC_MSG = "Пайдаланушы-агент тақырыбы"
    ARGS_GEO_BYPASS_DESC_MSG = "Географиялық шектеулерді айналып өту"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "SSL сертификатын тексеріңіз"
    ARGS_LIVE_FROM_START_DESC_MSG = "Тікелей трансляцияларды басынан жүктеп алыңыз"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Тікелей эфирлерді басынан жүктеп алмаңыз"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "HLS бейнелері үшін MPEG-TS контейнерін пайдаланыңыз"
    ARGS_NO_PLAYLIST_DESC_MSG = "Ойнату тізімін емес, жалғыз бейнені жүктеп алыңыз"
    ARGS_NO_PART_DESC_MSG = ".part файлдарын пайдаланбаңыз"
    ARGS_NO_CONTINUE_DESC_MSG = "Ішінара жүктеулерді жалғастырмаңыз"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Шығару үшін аудио пішімі"
    ARGS_EMBED_METADATA_DESC_MSG = "Бейне файлға метадеректерді ендіріңіз"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Бейне файлға нобайды ендіру"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Файлға нобай жазу"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Жүктеп алынатын қатарлас фрагменттердің саны"
    ARGS_FORCE_IPV4_DESC_MSG = "IPv4 қосылымдарын мәжбүрлеу"
    ARGS_FORCE_IPV6_DESC_MSG = "IPv6 қосылымдарын мәжбүрлеу"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For тақырып стратегиясы"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP бөлігінің өлшемі (байт)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Субтитрді жүктеп алу алдында ұйықтау (секундтар)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Бұрынғы сервер қосылымдарына рұқсат беріңіз"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "HTTPS сертификатын тексеруді болдырмау"
    ARGS_USERNAME_DESC_MSG = "Тіркелгі пайдаланушы аты"
    ARGS_PASSWORD_DESC_MSG = "Тіркелгі құпия сөзі"
    ARGS_TWOFACTOR_DESC_MSG = "Екі факторлы аутентификация коды"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Жүктеп алу қателерін елемеңіз және жалғастырыңыз"
    ARGS_MIN_FILESIZE_DESC_MSG = "Ең аз файл өлшемі (МБ)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Максималды файл өлшемі (МБ)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Жүктеп алынатын ойнату тізімінің элементтері (мысалы, 1,3,5 немесе 1-5)"
    ARGS_DATE_DESC_MSG = "Осы күні жүктеп салынған бейнелерді жүктеп алу (ЖЖЖЖАА)"
    ARGS_DATEBEFORE_DESC_MSG = "Осы күнге дейін жүктеп салынған бейнелерді жүктеп алу (ЖЖЖЖАА)"
    ARGS_DATEAFTER_DESC_MSG = "Осы күннен кейін жүктеп салынған бейнелерді жүктеп алу (ЖЖЖЖАА)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Арнаулы HTTP тақырыптары (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Сұраулар арасындағы ұйқы аралығы (секунд)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Максималды ұйқы аралығы (секунд)"
    ARGS_RETRIES_DESC_MSG = "Қайталаулар саны"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Бейне контейнер пішімі"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Біріктіруге арналған шығыс контейнер пішімі"
    ARGS_SEND_AS_FILE_DESC_MSG = "Барлық медианы баспа құралының орнына құжат ретінде жіберіңіз"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Еліктеу"
    ARGS_REFERER_SHORT_MSG = "Анықтамашы"
    ARGS_GEO_BYPASS_SHORT_MSG = "Гео айналып өту"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Сертификатты тексеру"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Тікелей бастау"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Тікелей бастау жоқ"
    ARGS_USER_AGENT_SHORT_MSG = "Пайдаланушы агенті"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Плейлист жоқ"
    ARGS_NO_PART_SHORT_MSG = "Бөлім жоқ"
    ARGS_NO_CONTINUE_SHORT_MSG = "Жалғастыру жоқ"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Аудио пішімі"
    ARGS_EMBED_METADATA_SHORT_MSG = "Мета енгізу"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Бас бармақ енгізу"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Бас бармақ жазу"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Бір мезгілде"
    ARGS_FORCE_IPV4_SHORT_MSG = "IPv4. мәжбүрлеу"
    ARGS_FORCE_IPV6_SHORT_MSG = "IPv6 мәжбүрлеу"
    ARGS_XFF_SHORT_MSG = "XFF тақырыбы"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Бөлшек өлшемі"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Sleep Subs"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Legacy Connect"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Тексеру сертификаты жоқ"
    ARGS_USERNAME_SHORT_MSG = "Пайдаланушы аты"
    ARGS_PASSWORD_SHORT_MSG = "Құпия сөз"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Қателерді елемеу"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Минималды өлшем"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Максималды өлшем"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Плейлист элементтері"
    ARGS_DATE_SHORT_MSG = "Күн"
    ARGS_DATEBEFORE_SHORT_MSG = "Бұрынғы күн"
    ARGS_DATEAFTER_SHORT_MSG = "Кейінгі күн"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP тақырыптары"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Ұйқы аралығы"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Максималды ұйқы"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Бейне форматы"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Біріктіру пішімі"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Файл ретінде жіберу"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ Файл тым үлкен. Максималды өлшем - 100 КБ."
    COOKIES_INVALID_FORMAT_MSG = "❌ Тек келесі пішімдегі файлдарға рұқсат етілген .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ Файл cookie.txt файлына ұқсамайды («# Netscape HTTP cookie файлы» жолы жоқ)."
    COOKIES_ERROR_READING_MSG = "❌ Файлды оқу қатесі: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Cookie файлы бар және дұрыс пішімге ие"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} cookie файлы тым үлкен! Ең көбі 100{size}t {size}КБ."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} cookie файлы жүктеліп, қалтаңызда cookie.txt ретінде сақталды.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} cookie көзі қолжетімсіз (статус {status}). Кейінірек қайталап көріңіз."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ {service} cookie файлын жүктеп алу қатесі. Тағы жасауды сәл кейінірек көріңізді өтінеміз."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Пайдаланушы жаңа cookie файлын ұсынды.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie сәтті жаңартылды:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Жарамды cookie файлы емес.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube cookie файлдарының көздері конфигурацияланбаған!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 YouTube cookie файлдарын жүктеп, тексеруде...\n\n{attempt} сыныптамада {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Қол жеткізу қол жетімсіз. Тек әкімші."
    ADMIN_USER_LOGS_TOTAL_MSG = "Барлығы: <b>{total}</b>\n<b>{user_id}</b> - логтар (Соңғы 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 пернетақта іске қосылды!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Субтитр тілі келесіге орнатылды: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Субтитр тілі: {flag} {name}, AUTO/TRANS қосулы."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Субтитр тілі мәзірі жабылды."
    SUBS_DOWNLOADING_MSG = "💬 Субтитрлер жүктелуде..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Firebase кэші жадқа қайта жүктелуде..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ COOKIE_URL конфигурацияланбаған. /cookie файлын пайдаланыңыз немесе cookie.txt файлын жүктеп салыңыз."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Қашықтағы URL мекенжайынан cookie файлдары жүктелуде..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Қосымша COOKIE_URL .txt файлын көрсетуі керек."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Қосымша cookie файлы тым үлкен (>100 КБ)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie файлы қалпына келтіру арқылы жүктеліп, cookie.txt ретінде сақталады"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Резервті cookie көзі қолжетімсіз (статус {status}). /cookie пайдаланыңыз немесе cookie.txt жүктеңіз."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Қосымша cookie файлын жүктеп алу қатесі. /cookie файлын қолданып көріңіз немесе cookie.txt файлын жүктеңіз."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Қосымша cookie файлын жүктеп алу кезінде күтпеген қате."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} браузер орнатылмаған."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Браузер арқылы сақталған cookie файлдары: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Cookie файлдары сақталмады: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube cookie файлдары дұрыс жұмыс істейді"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube cookie файлдарының мерзімі аяқталған немесе жарамсыз\n\nЖаңа cookie файлдарын алу үшін /cookie пайдаланыңыз"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - custom format\n• <code>/format 720</code> - 720p quality\n• <code>/format 4k</code> - 4K quality"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Анықтама жіберілді."
    FORMAT_MKV_TOGGLE_MSG = "MKV енді {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Қашықтағы URL конфигурацияланбаған"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Файл пішімі жарамсыз"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Файл тым үлкен"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookie файлдары сәтті жүктелді"
    COOKIES_SERVER_ERROR_MSG = "❌ Сервер қатесі {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Жүктеп алу сәтсіз аяқталды"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Күтпеген қате"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Браузер орнатылмаған."
    COOKIES_MENU_CLOSED_MSG = "Мәзір жабық."
    COOKIES_HINT_CLOSED_MSG = "Cookie анықтамасы жабылды."
    IMG_HELP_CLOSED_MSG = "Анықтама жабылды."
    SUBS_LANGUAGE_UPDATED_MSG = "Субтитр тілі параметрлері жаңартылды."
    SUBS_MENU_CLOSED_MSG = "Субтитр тілі мәзірі жабылды."
    KEYBOARD_SET_TO_MSG = "Пернетақта {setting} орнатылды"
    KEYBOARD_ERROR_PROCESSING_MSG = "Параметрді өңдеу қатесі"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo қосылды."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo өшірілген."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW бұлыңғырлығы өшірілген."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW бұлыңғырлау қосылды."
    SETTINGS_MENU_CLOSED_MSG = "Мәзір жабық."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Су тасқынын күту белсенді. Кейінірек көріңіз."
    OTHER_HELP_CLOSED_MSG = "Анықтама жабылды."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Журналдар хабары жабылды."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Мәзір жабық."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Жарамсыз өлшем."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ MediaInfo жіберу қатесі: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Қате орын алды: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - барлық логтар"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - барлық {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Қашықтағы URL-ден жүктеу"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Браузерді ашу"
    SELECT_BROWSER_MSG = "Cookie файлдарын жүктеп алу үшін браузерді таңдаңыз:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Бұл жүйеде браузерлер табылмады. Қашықтағы URL мекенжайынан cookie файлдарын жүктеп алуға немесе шолғыш күйін бақылауға болады:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Браузерді ашу</b> - шағын қолданбадағы шолғыш күйін бақылау үшін"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ /check_cookie іске қосылмады"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Су тасқыны шегі. Кейінірек көріңіз."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Браузер куки мәзірін ашу сәтсіз аяқталды"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Cookie анықтамасы ретінде сақтау жабылды."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Қолдану:</b>\n<code>/link [сапа] URL</code>\n\n<b>Мысалдар:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - ең жақсы сапа\n• /link 720 https://youtube.com/watch?v=... - 720p немесе төменірек\n• /link 720p https://youtube.com/watch?v=... - жоғарыдағыдай\n• /link 4k https://youtube.com/watch?v=... - 4K немесе төменірек\n• /link 8k https://youtube.com/watch?v=... - 8K немесе төменірек</blockquote>\n\n<b>Сапа:</b> 1-ден 10000-ге дейін (мысалы, 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K сапасы"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Тікелей сілтеме алынды</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Формат:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Аудио ағыны:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Ағындық сілтемелер алынбады"
    LINK_ERROR_GETTING_MSG = "❌ <b>Сілтеме алу қатесі:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Жарамсыз YouTube cookie индексі: {selected_index}. Қолжетімді ауқым: 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 YouTube cookie файлдарын жүктеп алу және тексеру...\n\nӘрекет {attempt}/{total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 YouTube cookie файлдарын жүктеп алу және тексеру...\n\nӘрекет {attempt}/{total}\n🔍 Cookie файлдарын тексеру..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube cookie файлдары сәтті жүктеліп, тексерілді!\n\nПайдаланылған көз {source}/{total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Барлық YouTube cookie файлдарының мерзімі аяқталған немесе қолжетімсіз!\n\nОларды ауыстыру үшін бот әкімшісіне хабарласыңыз."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube cookie қайталау шегінен асып кетті!\n\n🔢 Максимум: сағатына {limit} әрекет\n⏰ Кейінірек қайталап көріңіз"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ #{wrong} тегі тыйым салынған таңбаларды қамтиды. Тек әріптер, сандар және _ рұқсат етілген.\nҚолданыңыз: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Жарамсыз аргумент!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Субтитр тілі жинағы: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Мысал: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Таңдалған тіл: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Always Ask режимі {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Субтитрлер өшірілген"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Субтитр баптаулары</b>\n\n{status_text}\n\nСубтитр тілін таңдаңыз:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - субтитрлерді өшіру\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Субтитр баптаулары</b>\n\n{status_text}\n\nСубтитр тілін таңдаңыз:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Атауы:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Ұзақтығы:</b> {duration} сек\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Бейне ағыны:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 720p максималды сапа\n- 1.5 сағат максималды ұзақтық\n- 500mb максималды бейне өлшемі</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️ЕСКЕРТПЕ: жоғары CPU әсеріне байланысты бұл функция өте баяу (нақты уақытқа жақын) және мыналармен шектеледі:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Жылдам командалар:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - субтитрлерді өшіру\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - Always Ask режимін қосу\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - тілді орнату\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - AUTO/TRANS арқылы тілді орнату\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - Always Ask режимін қосу\n"
    SUBS_AUTO_SUBS_TEXT = " (автоматты жазылушылар)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Автоматты жазылу режимі {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS пәрмені арқылы өшірілді: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Әрқашан сұрау пәрмені арқылы қосылды: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "SUBS тілі пәрмен арқылы орнатылады: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "SUBS тілі + пәрмен арқылы орнатылған автоматты режим: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Пайдаланушы /қосалқылар мәзірін ашты."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Пайдаланушы субтитр тілін келесіге орнатты: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Пайдаланушы AUTO/TRANS режимін келесіге ауыстырды: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Пайдаланушы «Әрқашан сұрау» режимін келесіге ауыстырды: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Пайдаланушы браузерден cookie файлдарын сұрады."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Браузерді таңдау пернетақтасы тек орнатылған браузерлермен жіберіледі."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Браузер таңдау жабылды."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "Қосымша COOKIE_URL сәтті пайдаланылды (көз жасырын)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "Қосымша COOKIE_URL орындалмады: күйі={status} (жасырын)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Қосымша COOKIE_URL күтпеген қате: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "{browser} браузері орнатылмаған."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Браузер арқылы сақталған cookie файлдары: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "Cookie файлы {user_id} пайдаланушысы үшін сақталды."
    COOKIES_FILE_WORKING_LOG_MSG = "Cookie файлы бар, пішімі дұрыс және YouTube cookie файлдары жұмыс істейді."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Cookie файлы бар және дұрыс пішімге ие, бірақ YouTube cookie файлдарының мерзімі аяқталды."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Cookie файлы бар және дұрыс пішімге ие."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Cookie файлы бар, бірақ пішімі дұрыс емес."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Cookie файлы табылмады."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{service} cookie файлының URL мекенжайы бос f{user_id}user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} cookie файлының URL мекенжайы .txt емес (жасырын)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} cookie файлы да{size}: {size} байт (көз жасырын)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{service} cookie файлы жүктеп алынды f{user_id}user_id} (көз жасырын)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Script not found: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Бастапқы мәртебе хабарламасын жіберу мүмкін болмады"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "{script_path} іске қосу қатесі: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Firebase кэші автоматты тапсырма арқылы қайта жүктелді."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Firebase кэші әкімші арқылы қайта жүктелді."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Firebase кэшін қайта жүктеу қатесі: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Хабарлама басталды. Мәтін:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Хабарлама барлық пайдаланушыларға жіберілді."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Хабарламаны жіберу мүмкін болмады: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Әкімші {user_id} URL үшін кэшті тазартты: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Әкімші {user_id} порн тізімін жаңарту скриптің бастады: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Порн тізімін жаңарту скрипті әкімші {user_id} арқылы сәтті аяқталды"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Порн тізімін жаңарту скрипті әкімші {user_id} арқылы сәтсіз аяқталды: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Әкімші {user_id} жоқ скриптті іске қосуға тырысты: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Әкімші {user_id} арқылы порн жаңарту скриптің іске қосу қатесі: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Әкімші {user_id} порн кэшін қайта жүктеуді бастады"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Әкімші {user_id} арқылы порн кэшін қайта жүктеу қатесі: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Әкімші {user_id} URL-ді NSFW үшін тексерді: {url} - Нәтиже: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "Пайдаланушы пішімді өзгертуді сұрады."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "Пішім ALWAYS_SOR ретінде орнатылды."
    FORMAT_UPDATED_BEST_LOG_MSG = "Пішім ең жақсы болып жаңартылды: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "Пішім ID {format_id}: {format} болып жаңартылды"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "Пішім {format_id} идентификаторына жаңартылды (аудио-тек): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "Пішім сапа {quality}: {format} жаңартылды"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "Пішім: {format} болып жаңартылды"
    FORMAT_MENU_SENT_LOG_MSG = "Пішім мәзірі жіберілді."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "Пішім таңдау жабылды."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "Арнаулы пішім туралы кеңес жіберілді."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "Пішім ажыратымдылығы мәзірі жіберілді."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "Негізгі пішім мәзіріне оралды."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "Пішім: {format} болып жаңартылды"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "Пішім ALWAYS_SOR ретінде орнатылды."
    FORMAT_CODEC_SET_LOG_MSG = "Кодек параметрі {codec} болып орнатылды"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Арнаулы пішім мәзірі жабылды"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "Тікелей сілтеме {user_id} пайдаланушысы үшін {url} шығарылды"
    LINK_EXTRACTION_FAILED_LOG_MSG = "{user_id} пайдаланушысының {url} тікелей сілтемесін шығару мүмкін болмады: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Пайдаланушы {user_id} үшін сілтеме пәрменіндегі қате: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Пайдаланушы {user_id} перне орнату{setting}параметрі}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Пайдаланушы {user_id} перне орнату{setting}параметрі}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo пәрмені арқылы орнатылды: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Пайдаланушы /mediainfo мәзірін ашты."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: жабық."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo қосылды."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo өшірілген."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Бөлу өлшемі аргумент арқылы {size} байтқа орнатылды."
    SPLIT_MENU_OPENED_LOG_MSG = "Пайдаланушы мәзірді ашты/бөлді."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Бөлінген таңдау жабылды."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Бөлу өлшемі {size} байтқа орнатылды."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Пәрмен арқылы прокси орнатылды: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Пайдаланушы /прокси мәзірін ашты."
    PROXY_MENU_CLOSED_LOG_MSG = "Прокси: жабық."
    PROXY_ENABLED_LOG_MSG = "Прокси қосылды."
    PROXY_DISABLED_LOG_MSG = "Прокси өшірілген."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Анықтама хабары жабылды."
    AUDIO_HELP_SHOWN_LOG_MSG = "Көрсетілді /аудио анықтама"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Пайдаланушы ойнату тізіміне көмек сұрады."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Ойнату тізімінің анықтамасы жабылды."
    AUDIO_HINT_CLOSED_LOG_MSG = "Аудио кеңес жабылды."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "{user_id}PLACEHOLDER_1__om {url} пайдаланушысы үшін LINK түймесі арқылы жасалған тікелей сілтеме мәзірі"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Пайдаланушы {user_id}PLACE{error}1__om {url} үшін LINK түймесі арқылы тікелей сілтемені шығару мүмкін болмады: {қате}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "LIST пәрмені {user_id}_PLACEHOLDER_1__l пайдаланушысы үшін орындалды: {url}"
    QUICK_EMBED_LOG_MSG = "Жылдам енгізу: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "{url} үшін жіберілген \"Әрқашан сұрау\" мәзірі"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "{error} {қатеден кейін {user_id} пайдаланушы үшін кэштелген сапалар мәзірі жасалды."
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "\"Әрқашан сұрау\" мәзір қатесі {url} үшін: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Пішім /args параметрлері арқылы бекітіледі"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Аудио"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Бейне"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Бейне"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Келесі ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Алдыңғы"
    SUBTITLES_NEXT_BUTTON_MSG = "Келесі ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Барлық мәтін өрістері бос"
    SENDER_VIDEO_DURATION_MSG = "Бейне ұзақтығы:"
    SENDER_UPLOADING_FILE_MSG = "📤 Файл жүктеп салынуда..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Бейне жүктеп салынуда..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Бейне ұзақтығы:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 файл жүктелді."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Бейне ақпараты"
    DOWN_UP_NUMBER_MSG = "Нөмір"
    DOWN_UP_TITLE_MSG = "Атауы"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Бейне жүктелді."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Жүктеуге дайындауда..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Бөлінген бөлік {part} файл жүктелді"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Жүктеу аяқталды"
    DOWN_UP_FILES_UPLOADED_MSG = "файлдар жүктелді"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Жабу"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBS"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 SUBS"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Браузер"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Тікелей сілтеме алу..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Қол жетімді форматтар алынуда..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Бейне сипаттамасын алуда..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Сипаттаманы алу қатесі: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Бейне сипаттамасы қолжетімсіз"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Сипаттаманы жіберу қатесі: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Бейне сипаттамасы {user_id} пайдаланушысына {url} ({title}) үшін жіберілді"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Galery-dl басталуда…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Ұзақтығы:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Пішімі:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Браузер:</b> Веб-шолғышта ашыңыз"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "үшін қолжетімді пішімдер"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Пішім идентификаторларын пайдалану жолы:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Тізімді алғаннан кейін арнайы пішім идентификаторын пайдаланыңыз:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - жүктеп алу пішімі 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - жоғарыдағыдай"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 аудио - 140 форматын MP3 аудио ретінде жүктеп алу"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Тек аудио форматтары анықталды"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Бұл пішімдер MP3 аудио файлдары ретінде жүктеледі."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Пішімді орнату жолы:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Арнайы пішім идентификаторын жүктеп алыңыз"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Сапа бойынша жүктеп алу"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Ең жақсы сапаны жүктеп алыңыз"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Әрқашан сапаны сұраңыз"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Тек аудио форматтары:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 аудио</code> - 140 форматын MP3 аудио ретінде жүктеп алу"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Олар MP3 аудио файлдары ретінде жүктеледі."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Жоғарыдағы тізімдегі пішім идентификаторын пайдаланыңыз"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Қате: бастапқы хабар табылмады."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Форматтар беті"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Пішімдер мәзірін көрсету қатесі"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Пішімдерді алу қатесі"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Қол жетімді пішімдерді алу қатесі."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Тағы жасауды сәл кейінірек көріңізді өтінеміз."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp бұл мазмұнды өңдей алмайды"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Оның орнына жүйе gallery-dl пайдалануды ұсынады."
    ALWAYS_ASK_OPTIONS_MSG = "**Опциялар:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Сурет галереялары үшін: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Жалғыз кескіндер үшін: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl жиі Instagram, Twitter және басқа әлеуметтік медиа мазмұны үшін жақсы жұмыс істейді."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Gallery-dl көріңіз"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Пішім /args арқылы бекітілді"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Субтитрлер"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Дубляждалған аудио"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Субтитрлер қолжетімді"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Субтитр тілін таңдаңыз"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Жазылымдар табылмады және ендірілмейді"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — кэштен лезде репост жасау"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Аудио тілін таңдаңыз"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW төленеді (⭐️$0,02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Жүктеп алу сапасын таңдаңыз"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Суретті жүктеп алу (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Бейнеге тікелей сілтеме алыңыз"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Қол жетімді пішімдердің тізімін көрсету"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Бейненің ішкі/кодекін өзгерту"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Ендіру"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Тек аудионы шығарып алу"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW төленеді (⭐️$0,02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — кэштен лезде репост жасау"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Аудио тілін таңдаңыз"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Ең жақсы"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Басқа"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝тек субтитр"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Ақылды топтастыру"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Қосылған әрекет түймесі жолы (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Әрекет түймелерінің жолдары қосылды (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Бар жолға төменгі түймелер қосылды"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Жаңа төменгі жол жасалды"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Ойнату тізімінде бейнелер табылмады"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "Қолдау көрсетілмейтін URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Бейне табылмады"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Бейне табылмады"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Ешбір медиа табылмады"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Бұл твиттерде жоқ"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Бейне ақпаратын алу қатесі:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Бейне ақпаратын алу қатесі"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "<code>/clean</code> пәрменін орындап, әрекетті қайталаңыз. Қате жойылмаса, YouTube авторизацияны қажет етеді. Cookies.txt файлын <code>/cookie</code> немесе <code>/cookies_from_browser</code> арқылы жаңартып, әрекетті қайталаңыз."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Мәзір жабық."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Сапаны қолмен таңдау"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Автоматты анықтау сәтсіз болғандықтан сапаны қолмен таңдаңыз:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Барлық қолжетімді форматтар"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Қолжетімді сапалар (кэштен)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Кэштелген сапаларды пайдалану - жаңа пішімдер қолжетімді болмауы мүмкін"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Жүктеп алу пішімі"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Жүктеп алынуда"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Орындалу барысын бақылау арқылы жүктеп алынуда..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Форматты пайдаланып жүктеп алу:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Пішім арқылы аудионы жүктеп алу:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Ең жақсы сапа жүктелуде..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Дерекқор қоқысы жүктелуде..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Жүктеп алынуда"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Форматтар беті"
    ALWAYS_ASK_FROM_CACHE_MSG = "(кэштен)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Қате: бастапқы хабар табылмады. Ол жойылған болуы мүмкін. Сілтемені қайта жіберіңіз."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Қате: бастапқы URL мекенжайы табылмады. Сілтемені қайта жіберіңіз."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Тікелей сілтеме алынды</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Атауы:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Ұзақтығы:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Пішімі:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Бейне ағыны:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Аудио ағыны:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Ағындық сілтемелер алынбады"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Тікелей сілтеме {user_id}PLACEHOLDER_1__om {url} пайдаланушысы үшін Әрқашан сұрау мәзірі арқылы шығарылды"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Пайдаланушы {user_id}PLACE{error}1__om {url} үшін Әрқашан сұрау мәзірі арқылы тікелей сілтемені шығару мүмкін болмады: {қате}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Тікелей сілтеме {user_id}PLACEHOLDER_1__om {url} пайдаланушысы үшін down_and_up_with_format арқылы шығарылды"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Пайдаланушы {user_id}PLACE{error}1__om {url} үшін down_and_up_with_format арқылы тікелей сілтемені шығару мүмкін болмады: {қате}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Тікелей сілтеме {user_id}PLACEHOLDER_1__om {url} пайдаланушысы үшін down_and_audio арқылы шығарылды"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "{user_id}PLACE{error}1__om {url} пайдаланушысы үшін down_and_audio арқылы тікелей сілтеме шығарылмады: {қате}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Дыбыс кэштен жіберілді."
    AUDIO_PROCESSING_MSG = "🎙️ Аудио өңделуде..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Аудио жүктелуде:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Аудио жүктеп алу кезінде қате орын алды."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Аудио ақпаратты шығару мүмкін болмады"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "{index} индексіндегі ойнату тізіміндегі қолдау көрсетілмейтін файл түрін өткізіп жіберу"
    AUDIO_FILE_NOT_FOUND_MSG = "Жүктеп алғаннан кейін аудио файл табылмады."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ Аудио жіберу сәтсіз: Файл өлшемі 0 B тең (плейлист индексі {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ Аудио файлы әлі жүктелуде, күте тұрыңыз..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Аудио файлы жүктелуде...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Аудио жіберілмеді: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Ойнату тізімінің аудиосы жіберілді: {sent}/{total} файлдар (сапа={quality}) {user_id} пайдаланушыға"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Аудионы жүктеп алу мүмкін болмады: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Жүктеп алу күту уақытының аяқталуына байланысты тоқтатылды (2 сағат)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Бейне файлы табылмады: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ Бейне жіберу сәтсіз: Файл өлшемі 0 B тең (плейлист индексі {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ Бейне файлы әлі жүктелуде, күте тұрыңыз..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Бейнені өңдеу қатесі: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Сипаттама файлын жіберу қатесі: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 егер бейненің тақырыбын өзгерткіңіз келсе - бейнеге жаңа мәтінмен жауап беріңіз</blockquote>"
    
    # Always Ask Menu Mess    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Тікелей сілтеме алынды</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Атауы:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Ұзақтығы:</b> {duration} сек\n"
    FORMAT_FIELD_MSG = "🎛 <b>Формат:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Бейне ағыны:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Аудио ағыны:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Файлды өңдеу қатесі**\n\nБейне жүктелді, бірақ файл атауындағы жарамсыз таңбаларға байланысты өңдеу мүмкін болмады.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Файлды өңдеу қатесі**\n\nБейне жүктелді, бірақ жарамсыз аргумент қатесіне байланысты өңдеу мүмкін болмады.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Себеп:**\n"
        "• Жүктелген файл бейне файлы емес\n"
        "• Бұл құжат (PDF, DOC, т.б.) немесе архив болуы мүмкін\n\n"
        "**Шешу:**\n"
        "• Сілтемені тексеріңіз - ол бейнеге емес, құжатқа алып кетуі мүмкін\n"
        "• Басқа сілтеме немесе көзді көріңіз\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Себеп:**\n"
        "• Файлды бейне ретінде өңдеу мүмкін емес\n"
        "• Бұл бейне файлы болмауы мүмкін немесе файл бүлінген болуы мүмкін\n\n"
        "**Шешу:**\n"
        "• Сілтемені тексеріңіз - ол бейнеге емес, құжатқа алып кетуі мүмкін\n"
        "• Басқа сілтеме немесе көзді көріңіз\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Формат қолжетімсіз**\n\nСұралған бейне форматы осы бейне үшін қолжетімсіз.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Формат ID {format_id} осы бейне үшін табылмады.\n\nҚолжетімді формат ID-лері: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **AV1 форматы осы бейне үшін қолжетімсіз.**\n\n**Қолжетімді форматтар:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Файлды өңдеу қатесі**\n\nАудио жүктелді, бірақ файл атауындағы жарамсыз таңбаларға байланысты өңдеу мүмкін болмады.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Файлды өңдеу қатесі**\n\nАудио жүктелді, бірақ жарамсыз аргумент қатесіне байланысты өңдеу мүмкін болмады.\n\n"
    
    NO_SUBTITLES_DETECTED_MSG = "Субтитрлер анықталмады"
    VIDEO_PROGRESS_MSG = "<b>Бейне:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Аудио:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL шегінен асып кетті: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Өңдеу аяқталды"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Бірнеше URL режимінде ойнату тізімінің ауқымдарына рұқсат етілмейді. Ауқымсыз жалғыз URL мекенжайларын жіберіңіз (*1*5, /видео 1-10, т.б.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Сайтыңызға қолдау көрсетілсе, <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>осы жерден</a> тексеріңіз."
    ERROR_COOKIE_NEEDED_MSG = "Бұл бейнені жүктеп алу үшін сізге <code>cookie</code> қажет болуы мүмкін. Алдымен <b>/clean</b> пәрмені арқылы жұмыс кеңістігін тазалаңыз"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Youtube үшін - <b>cookie</b> пәрмені арқылы <code>cookie</code> алыңыз. Қолдау көрсетілетін кез келген басқа сайт үшін - жеке cookie файлыңызды (<a href='https://t.me/tg_ytdlp/203'>guide1</a>) (<a href='https://t.me/tg_ytdlp/214'>guide2</a>) жіберіңіз, содан кейін бейне сілтемесін қайта жіберіңіз."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Субтитр тілін таңдаңыз"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Балама аудио тілдері жоқ"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Аудио тілін таңдаңыз"
    PAGE_NUMBER_MSG = "Бет {page}"
    TOTAL_PROGRESS_MSG = "Жалпы прогресс"
    SUBTITLE_MENU_CLOSED_MSG = "Субтитр мәзірі жабылды."
    SUBTITLE_LANGUAGE_SET_MSG = "Субтитр тілі жинағы: {value}"
    AUDIO_SET_MSG = "Аудио жинағы: {value}"
    FILTERS_UPDATED_MSG = "Сүзгілер жаңартылды"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Артқа"
    CLOSE_BUTTON_TEXT = "🔚Жабу"
    LIST_BUTTON_TEXT = "📃Тізім"
    IMAGE_BUTTON_TEXT = "🖼Сурет"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Qualities not auto-detected\nUse 'Other' button to see all available formats.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Тікелей трансляция анықталды**\n\nЖалғасып жатқан немесе шексіз тікелей трансляцияларды жүктеуге тыйым салынады.\n\nТрансляция аяқталғанға дейін күтіңіз және келесі жағдайларда қайта жүктеуді байқаңыз:\n• Трансляция ұзақтығы белгілі болғанда\n• Трансляция аяқталғанда\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Тікелей трансляцияны жүктеп алу</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Бөлшек {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Максималды өлшем: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Жалпы ұзақтығы: {duration} сек"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Тікелей трансляция - Бөлшек {chunk}</b>\n⏱ Ұзақтығы: {duration} сек\n📦 Өлшемі: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Бөлшек {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Тікелей трансляцияны жүктеп алу аяқталды</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "Жүктеп алынған {chunks} бөлік(тер)"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Жалпы ұзақтығы: {duration} сек"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Тікелей трансляцияны жүктеп алу тоқтатылды</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Пайдаланушы каталогы жойылды (мүмкін /clean командасы арқылы)"
    LIVE_STREAM_FILE_DELETED_MSG = "Бөлшек файл жойылды (мүмкін /clean командасы арқылы)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Трансляция аяқталды"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "`/format` пәрменін пайдаланып басқа пішімді таңдаңыз."
    
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Пайдаланушы тыйым салынған мазмұнды енгізді. Жүктеп алу мүмкін емес."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "NSFW бұлыңғырлығы пәрмен арқылы орнатылды: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Пайдаланушы /nsfw мәзірін ашты."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: жабық."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "{service} cookie файлын жүктеп алу мүмкін болмады:{status}{status} (url жасырын)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "{service} {error} жүктеп алу қатесі {қате} (url жасырын)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "{service} cookie файлын жүктеп алу кезінде күтпеген қате (url жасырын): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Cookie файлы {user_id} пайдаланушысы үшін жаңартылды."
    COOKIES_INVALID_CONTENT_LOG_MSG = "{user_id} пайдаланушы берген жарамсыз cookie мазмұны."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "YouTube cookie файлының URL мекенжайлары {user_id} пайдаланушысы үшін бос."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "YouTube cookie файлдары {source}{source} сайтынан {user_id} пайдаланушысы үшін жүктеліп, тексерілді."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Барлық YouTube cookie файлдары {user_id} пайдаланушысы үшін сәтсіз аяқталды."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Әкімші {admin_id} арқылы check_porn командасындағы қате: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Бөлшек өлшемі {size} байтқа орнатылды."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Бейнені жүктеп салу файлды бөлумен аяқталды."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Ойнату тізімі бейнелері жіберілді: {sent}/{total} файлдар (сапа={quality}) {user_id} пайдаланушыға"
    UNKNOWN_ERROR_MSG = "❌ Белгісіз қате: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "{index} индексіндегі ойнату тізіміндегі қолдау көрсетілмейтін файл түрін өткізіп жіберу"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg табылмады. FFmpeg орнатыңыз."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ MP4 түрлендіру сәтсіз аяқталды: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Embedding subtitles may take a long time (up to 1 min per 1 min of video)!\n🔥 Starting to burn subtitles..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Субтитрлерді шектеулерге байланысты енгізу мүмкін емес (сапа/ұзақтық/өлшем)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Таңдалған тіл үшін субтитрлер қолжетімді емес"
    ERROR_SENDING_VIDEO_MSG = "❌ Бейнені жіберу қатесі: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Жіберілген ойнату тізімі бейнелері: {sent}/{total} файл."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Жүктеп алу күту уақытының аяқталуына байланысты тоқтатылды (2 сағат)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Бейнені жүктеп алу мүмкін болмады: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Қате: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON нысан (сөздік) болуы керек."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Жарамсыз JSON пішімі. Жарамды JSON жіберіңіз."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Мән {min_val} және {max_val} арасында болуы керек."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} орнатылды: <c{value}lue}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ True"
    ARGS_FALSE_BUTTON_MSG = "❌ False"
    ARGS_BACK_BUTTON_MSG = "🔙 Back"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Close"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Рас"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Жалған"
    ARGS_NOT_SET_MSG = "Орнатылмаған"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ AV1 формат бұл бейне үшін қолжетімсіз.\n\nҚолжетімді форматтар:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Жүктеу қатесі: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ Плейлистте {index} индексінде бейнелер табылмады."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Бейне түрлендіру сәтсіз**\n\nБейнені жарамсыз аргумент қатесіне байланысты MP4-ке түрлендіру мүмкін болмады.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Бейне түрлендіру сәтсіз**\n\nБейнені MP4-ке түрлендіру мүмкін болмады.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Ағын сілтемелерін алу мүмкін болмады"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Сілтемені алу қатесі:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ {index} индексінде мазмұн табылмады"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Қате: Бастапқы хабар табылмады."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Қате: URL табылмады."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Бұл URL енгізілуі мүмкін емес."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} кодек бұл бейне үшін қолжетімсіз"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} формат бұл бейне үшін қолжетімсіз"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Су тасқыны шегі. Кейінірек көріңіз."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Cookie тексеру"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ БАРЛЫҒЫ (АВТО)"
    PROXY_OFF_BUTTON_MSG = "❌ ӨШІРІЛГЕН"
    PROXY_CLOSE_BUTTON_MSG = "🔚Жабу"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Елді таңдаңыз:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Елді таңдауды өшіру"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Таңдалған ел: {country} (код: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Қолжетімді проксилер: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Бот алдымен HTTP, содан кейін SOCKS5 әрекетін жасайды"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Таңдалған ел үшін прокси автоматты түрде қосылады"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Ел таңдау жойылды"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Ел таңдау жойылды"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Таңдалған ел: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Файлдағы елді пайдалану: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Файлдағы қолжетімді елдер: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 Таңдалған ел: {ел} (коды: {ел_коды})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ Осы ел үшін прокси қосылған"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ Прокси өшірілген (қосу үшін БАРЛЫҚ (АВТО) түймесін басыңыз)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ ҚОСУЛЫ"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ ӨШІРІЛГЕН"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Жабу"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ ҚОСУЛЫ (Бұлыңғыр емес)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ON (No Blur)"
    NSFW_OFF_BLUR_MSG = "✅ ӨШІРУ (бұлыңғыр)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ OFF (Blur)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"  # Аббревиатура, не переводится
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Таза"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Пайдаланушы {user} үшін жауап хабарламасын өңдеу қатесі: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Пайдаланушы {user} үшін хабарламаны жіберу қатесі: {error}"
    ADMIN_LOGS_FORMAT_MSG = "{bot_name} логтары\nПайдаланушы: {user_id}\nБарлық логтар: {total}\nАғымдағы уақыт: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nБарлық {path}: {count}\nАғымдағы уақыт: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Жалпы пайдаланушылар: {count}</i>\nСоңғы 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Порн кэштері әкімші {admin_id} арқылы қайта жүктелді. Домендер: {domains}, Кілт сөздер: {keywords}, Сайттар: {sites}, АҚ ТІЗІМ: {whitelist}, СҰР ТІЗІМ: {greylist}, ҚАРА ТІЗІМ: {black_list}, АҚ КІЛТ СӨЗДЕР: {white_keywords}, ПРОКСИ ДОМЕНДЕР: {proxy_domains}, ПРОКСИ_2 ДОМЕНДЕР: {proxy_2_domains}, ТАЗА СҰРАУ: {clean_query}, COOKIE ЖОҚ ДОМЕНДЕР: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Күту уақыты туралы хабарды жіберу қатесі: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Тілді таңдаңыз</b>"
    LANG_CHANGED_MSG = "✅ Тіл {lang_name} деп өзгертілді"
    LANG_ERROR_MSG = "❌ Тілді өзгерту кезінде қате"
    LANG_CLOSED_MSG = "Тіл таңдауы жабылды"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] кері қоңырау: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "URL мекенжайы бар шолғышты бақылау түймесі қосылуда: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "Браузерді бақылау URL мекенжайы конфигурацияланбаған: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Пернетақта баптауы жаңартылды!**\n\nЖаңа баптау: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Пернетақтаны жасыру мүмкін болмады: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "{user_id} пайдаланушысының сілтемесін алу үшін жұмыс істейтін YouTube cookie файлдарын пайдалану"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "{user_id} пайдаланушысы үшін сілтеме алу үшін жұмыс істейтін YouTube cookie файлдары қолжетімді емес."
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "{user_id} пайдаланушысының сілтемесін алу үшін бар YouTube cookie файлдарын пайдалану"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "{user_id} пайдаланушысының сілтемесін алу үшін YouTube cookie файлдары табылмады."
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Сілтемені шығару үшін ғаламдық cookie файлы пайдаланушы {user_id} қалтасына көшірілді"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Пайдаланушы {user_id} mediainfo пәрменін сұрады"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Пайдаланушы {user_id} — {is_admin}s_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Пайдаланушы {user_id} c{is_in_channel}арнасында"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Пайдаланушыға {user_id} кіруге тыйым салынды - әкімші емес және арнада емес"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] {user_id} пайдаланушыға рұқсат берілді"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] кері қоңырау: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Бұл пәрмен тек әкімшілер үшін қол жетімді."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Жүктеу PO таңбалауышын қолдауымен аяқталды"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Су тасқыны шегі. Кейінірек көріңіз."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST таңбалауышын жаңарту қатесі: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Firebase сеансын жабу қатесі: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Негізгі дерекқор құрылымын инициализациялау қатесі: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Барлық параметрлер config.py ішінде орнатылмаған (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL орнатылмаған"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey idToken алу үшін орнатылмаған"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Firebase демпін жүктеп алу қатесі: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Firebase демпін REST арқылы жүктеп алу мүмкін болмады"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ _жүктеп алу_және_қайта_жүктеу_кэшіндегі қате: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Auto reload_cache іске қосу қатесі (әрекет {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Барлық қайталау әрекеттері сәтсіз аяқталды"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 {datetime} мекенжайында Firebase демпін жүктеп алуды бастау"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Тәуелділік қолжетімді емес: сұраулар немесе сессия"
    DB_DATABASE_EMPTY_MSG = "⚠️ Деректер базасы бос"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Журналды жабу қатесі: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Тазалау кезінде қате: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Клондау қатесі: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Клондау күту уақыты"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Клондау ерекшелігі: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Пайдаланушы жаңартудан бас тартты"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Репозиторий сәтті клондалды"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Сақтық көшірмелер _сақтық көшірмеге/ көшірілді"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Барлық модульдер жүктелді"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Шығу кезінде тазалау аяқталды"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Received signal {signal}, shutting down gracefully..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Күте тұрыңыз..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 HLS ағыны жүктелуде:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "фрагменттерді күту"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Сақтық көшірме {ts} _backup/ ішінде табылмады."
    RESTORE_FAILED_RESTORE_MSG = "❌ Қалпына келтіру сәтсіз {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Қалпына келтірілді: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Details:</b> {error_details}\n\nDownload stopped due to critical error.\n\n💡 <b>Tip:</b> If you're getting 401 Unauthorized error, try using <code>/cookie instagram</code> command or send your own cookies to authenticate with Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Порно қара тізімдегі домен: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Порно кілт сөздері табылды: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Ақ тізімдегі домен: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Ақ тізімдегі кілт сөздерді тапты: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Порно кілт сөздері табылмады"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ {index} индексіндегі TikTok API қатесі, келесі аудиоға өту..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ {index} индексіндегі TikTok API қатесі, келесі бейнеге өту..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "Пайдаланушы <b>url</b> енгізді\n <b>пайдаланушы аты:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>Пайдаланушы мынадай енгізді:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Арнаға қосылу"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Тіркеу өңдеушісі: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Менің 5 cookie файлымды жүктеу"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Браузердің YT-cookie алу"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Cookie файлыңызды тексеру"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Арнайы cookie жүктеу"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Жабу"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Қолжетімді форматтар: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Жабу"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Жабу"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Жабу"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Жабу"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Анықтама жабылды."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Жабық"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Қате орын алды"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg PATH немесе жоба каталогында табылмады. FFmpeg орнатыңыз."
    YTDLP_NOT_FOUND_MSG = "yt-dlp екілік файлы PATH немесе жоба каталогында табылмады. yt-dlp орнатыңыз."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Бейне {rounds} бөліктерге бөлінеді, бұл шамадан тыс болуы мүмкін"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Бейне бөлігін бөлу {current}/{total}: {start_time:.2f}с - {end_time:.2f}с"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Бөлінген бөлік жасалмады {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Бөлінген бөлік сәтті жасалды {part}: {target_name} ({size} байт)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Бейне бөлігін бөлу қатесі {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Бейне {count} бөліктерге сәтті бөлінді"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Бейнені бөлу процесіндегі қате: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Бейнені өңдеу кезіндегі қате {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Бейне файлы жоқ: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "'{size_result}_PLACEHOLDER_1__ror} өлшемдерін талдау қатесі"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "\"{size_result}\" бейне өлшемдерін анықтау мүмкін болмады, әдепкі: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Нобай жасау қатесі: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Бейне ұзақтығын талдау қатесі: {error}, қайта {result}: {нәтиже}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Әдепкі бойынша нобай {thumb_dir} орнында жасалмады"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Пәрменді орындау қатесі: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "FFmpeg көмегімен нобай жасау қатесі: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Дикттен тыс конфигурация бөлімін өткізіп жіберу: {key}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Gallery-dl конфигурациясын орнату: {key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Пайдаланушы cookie файлдарын пайдалану: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "{user_id} пайдаланушысы үшін YouTube cookie файлдарын пайдалану"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Жаһандық cookie файлы пайдаланушы {user_id} қалтасына көшірілді"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Көшірілген жаһандық cookie файлдарын пайдаланушы cookie файлдары ретінде пайдалану: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Пайдаланушы {user_id} үшін ғаламдық cookie файлын көшіру мүмкін болмады: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Домен үшін --no-cookies пайдалану: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Прокси сұралды, бірақ конфигурацияны импорттау/алу мүмкін болмады: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Gallery-dl үшін проксиді пайдалануға мәжбүрлеу: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Прокси сұралды, бірақ прокси конфигурациясы аяқталмады"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Прокси көмекшісі орындалмады: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Экстрактор элементтерін талдау..."
    GALLERY_DL_ITEM_COUNT_MSG = "Элемент {item}: {element}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Табылған метадеректер (2-тег): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "Табылған URL (3-тег): {url}{metadata}: {метадеректер}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Табылған метадеректер (бұрынғы): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "Табылған URL (бұрынғы): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Табылған файл атауы: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Табылған каталог: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Табылған кеңейтім: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Талданған {count} ite{info}f{fallback} қалпына келтіру: {қайтару}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Gallery-dl конфигурациясын орнату: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "A стратегиясын қолданып көру: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor модулі табылмады"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() бұл құрылымда қол жетімді емес"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Extractor.find ({url}) шақырылуда"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "URL мекенжайына ешбір экстрактор сәйкес келмеді"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Экстрактордағы cookie файлдарын орнату: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Экстракторға cookie файлдары орнатылмады: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Экстрактор табылды, элементтерді шақыруда()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "А стратегиясы орындалды, ақпарат алды: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "A стратегиясы: extractor.items() ешқандай жарамды ақпаратты қайтармады"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "A стратегиясы (extractor.find) орындалмады: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "--get-urls ішінен кері метадеректер: барлығы={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Барлық стратегиялар метадеректерді ала алмады"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Кескін туралы ақпаратты шығару мүмкін болмады: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job модулі табылмады (бұзылған орнату?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob бұл құрылымда қол жетімді емес"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Жүктелген файлдарды gallery-dl каталогында іздеу"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Экстрактордан файлдарды аттары бойынша табуға тырысуда"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Пайдаланушы {user_id} үшін дәлелдерін оқу қатесі: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Бейнені өңдеу кезіндегі қате {video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Пайдаланушы {user_id} файл ретінде жіберуді қосты, құжат ретінде жіберу"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video қайта-қайта күту уақыты бітті; жіберу_құжатына қайта оралу"
    SENDER_CAPTION_TOO_LONG_MSG = "Субтитр тым ұзын, ең аз жазумен әрекет ету"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (ең аз субтитр) уақыты аяқталды; жіберу_құжатына кері қайтару"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Минималды жазуы бар бейнені жіберу қатесі: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Толық сипаттама файлын жіберу қатесі: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Уақытша сипаттама файлын жою қатесі: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "NO_FILTER_DOMAINS доменіне арналған сәйкестік_сүзгісін өткізіп жіберу: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Пайдаланушы {user_id} пішімін анықтау үшін пайдаланушының URL мекенжайындағы бар YouTube cookie файлдарын тексеру"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Қолданыстағы YouTube cookie файлдары {user_id} пайдаланушы үшін пішімді анықтау үшін пайдаланушының URL мекенжайында жұмыс істейді - оларды пайдалану"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Қолданыстағы YouTube cookie файлдары пайдаланушының URL мекенжайында сәтсіз аяқталды, пайдаланушы {user_id} үшін пішімді анықтау үшін жаңаларын алуға әрекеттенді."
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Detec{user_id}пайдаланушы {user_id} пішімі үшін {i} YouTube cookie көзі қолданылуда"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "{i} дереккөзіндегі YouTube cookie файлдары detec{user_id}user {user_id} пішіміне арналған пайдаланушы URL мекенжайында жұмыс істейді - пайдаланушы қалтасына сақталған"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "{i} дереккөзіндегі YouTube cookie файлдары detec{user_id}user {user_id} пішімі үшін пайдаланушының URL мекенжайында жұмыс істемейді"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Detec{user_id}user {user_id} пішімі үшін {i} көзінен YouTube cookie файлдарын жүктеп алу мүмкін болмады"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Барлық YouTube cookie файлдары {user_id} пайдаланушысы үшін пішімді анықтау мүмкін болмады, cookie файлдарынсыз әрекет етеді"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "{user_id} пайдаланушысы үшін пішімді анықтау үшін конфигурацияланған YouTube cookie файлдарының ешбір көздері cookie файлдарынсыз әрекет етпейді"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Жаңаларын алуға әрекеттеніп жатқан {user_id} пайдаланушысы үшін пішімді анықтауға арналған YouTube cookie файлдары табылмады."
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "{user_id} пайдаланушысы үшін пішімді анықтау үшін YouTube cookie файлдарын пайдалану (Әрдайым сұрау мәзірінде әлдеқашан тексерілген)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "{user_id} пайдаланушысы үшін пішімді анықтау үшін YouTube cookie файлдары табылмады, қалпына келтіру әрекеті..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Пішімді анықтау үшін ғаламдық cookie файлы пайдаланушы {user_id} қалтасына көшірілді"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Пайдаланушы {user_id} үшін ғаламдық cookie файлын көшіру мүмкін болмады: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "get_video_formats доменіне арналған --no-cookie файлдарын пайдалану: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "Қолданба әлі іске қосылмаған. {name} кіру мүмкін емес"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Сипаттама:</b> <code>{caption}</code>\n<b>Пайдаланушы ID:</b> <code>{user_id}</code>\n<b>Пайдаланушы аты:</b> <code>{users_name}</code>\n<b>Бейне файл ID:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Caption_редакторындағы қате: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Caption_editor ішіндегі күтпеген қате: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 Video URL</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL конфигурацияда жауап береді"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin іске қосылды"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken жаңартылды"
    DB_LOG_FOR_USER_ADDED_MSG = "Қосылған пайдаланушы үшін журнал"
    DB_DATABASE_CREATED_MSG = "db құрылды"
    DB_BOT_STARTED_MSG = "Бот басталды"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY config.py үшін сақталды: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Ойнату тізімінің бөлігі әлдеқашан кэштелген: {path_parts}, өткізіп жіберу"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: кез келген URL/сапа нұсқасы үшін кэш табылмады, бос дикт қайтарылады"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: үлкен ауқым үшін жылдам санау: {cached_count} кэштелген бейнелер"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: хэш үшін кэш табылмады {url_hash}, q{quality_key}ty_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: кез келген URL нұсқасы үшін кэш табылмады, ол None қайтарады"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Қол жеткізуге тыйым салынды. Тек админ."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Автоматты Firebase кэш қайта жүктеу жаңартылды!\n\n📊 Статус: {status}\n⏰ Кесте: 00:00-ден бастап әр {interval} сағат сайын\n🕒 Келесі қайта жүктеу: {next_exec} ({delta_min} минуттан кейін)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Автоматты Firebase кэш қайта жүктеу тоқтатылды!\n\n📊 Статус: ❌ ӨШІРІЛГЕН\n💡 Қайта қосу үшін /auto_cache on пайдаланыңыз"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Жарамсыз аргумент. /auto_cache on | off | N (1..168) параметрін пайдаланыңыз"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Аралық 1 мен 168 сағат арасында болуы керек"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Аралық орнату сәтсіз аяқталды"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Автоматты Firebase кэш аралығы жаңартылды!\n\n📊 Статус: ✅ ҚОСУЛЫ\n⏰ Кесте: 00:00-ден бастап әр {interval} сағат сайын\n🕒 Келесі қайта жүктеу: {next_exec} ({delta_min} минуттан кейін)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Автоматты Firebase кэш қайта жүктеу басталды!\n\n📊 Статус: ✅ ҚОСУЛЫ\n⏰ Кесте: 00:00-ден бастап әр {interval} сағат сайын\n🕒 Келесі қайта жүктеу: {next_exec} ({delta_min} минуттан кейін)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Автоматты Firebase кэш қайта жүктеу тоқтатылды!\n\n📊 Статус: ❌ ӨШІРІЛГЕН\n💡 Қайта қосу үшін /auto_cache on пайдаланыңыз"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Автоматты қайта жүктеу ҚОСУ; келесіде {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Автоматты қайта жүктеуді әкімші ӨШІРІЛДІ."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Автоматты қайта жүктеу аралығы {interval}сағ мәніне орнатылды; n{next_exec}t_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Автоматты қайта жүктеу басталды; келесіде {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Автоматты қайта жүктеуді әкімші тоқтатты."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase кэші жүктелді: {count} түбірлік түйіндер"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Firebase кэш файлы табылмады, бос кэштен басталады: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Firebase кэші жүктелмеді: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase кэші қайта жүктелді: {count} түбірлік түйіндер"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Firebase кэш файлы табылмады: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Firebase кэшін қайта жүктеу мүмкін болмады: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 Сізге ботқа кіруге тыйым салынды! Бұғаттауды алу үшін {Config.ADMIN_USERNAME} хабарласыңыз\n<blockquote>P.S. Арнаны тастамаңыз - сіз автоматты түрде бұғатталасыз ⛔️</blockquote>\n🌍Тілді өзгерту /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Бейне форматтары табылмады. Сурет жүктегішін сынаймыз…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram хабарлама жіберуді шектеді.\n⏳ Күте тұрыңыз: {time_str}\nТаймерді жаңарту үшін URL-ді тағы 2 рет жіберіңіз."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Ағын URL-ін көшіру үшін батырманы басыңыз, содан кейін VLC қолданбасына қойыңыз</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Ағын URL-ін көшіру үшін батырманы басыңыз, содан кейін VLC қолданбасына қойыңыз</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Сілтемені алу қатесі:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Формат файлын жіберу қатесі: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Форматтарды алу мүмкін болмады:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Талдауда... (6 секунд күтіңіз)"
    AA_PROCESSING_MSG = "🔎 Талдауда..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ #{wrong} тегі тыйым салынған таңбаларды қамтиды. Тек әріптер, сандар және _ рұқсат етілген.\nҚолданыңыз: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Топта жұмыс істеу үшін ботқа әкімші құқықтары қажет. Ботты осы топтың әкімшісі етіп тағайындаңыз."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Сәлем {first_name},\n \n<i>Бұл бот🤖 кез келген бейнелерді Telegram-ға тікелей жүктей алады.😊 Көбірек ақпарат алу үшін <b>/help</b> басыңыз</i> 👈\n\n<blockquote>P.S. 🔞NSFW контент мүмкіндігіне байланысты - ☁️<b>Бұлттық сақтау</b>, 📁<b>Файл бөлісу</b>, 🔗<b>URL қысқартқыштар</b> және 🔞<b>Порно сайттары</b>нан жүктеу ақылы! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ @tg_ytdlp арнасын 🗑<b>жоймаңыз/жазылымнан шықпаңыз</b> және ботқа 🤖<b>URL/командаларды тым көп спамдамаңыз</b> - ботты пайдаланудан автоматты түрде тыйым салынасыз ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Жойылатын файлдар жоқ."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 Барлық файлдар сәтті жойылды!\n\nЖойылған файлдар:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ АЛДЫҢҒЫ ЖҮКТЕП АЛУ АЯТҚАНДАЙ КҮТІҢІЗ"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "Қолданба данасы check_user ішіндегі None"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict - Жоқ, жүктеп алуға мүмкіндік береді"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict — Ешбір, субтитрді ендіруге мүмкіндік береді"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: тексеру шектеулері - max_quality={max_quality}p, max_duration={max_duration}с, max_size={max_size}МБ"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: info_dict кілттері: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Субтитрді ендіру өткізілмеді: ұзақтығы {duration}с {max_duration}с шегінен асады"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Субтитрді ендіру өткізілмеді: {size_mb:.2f}МБ өлшемі {max_size}МБ шегінен асады"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Субтитрді ендіру өткізіп жіберді: сапа {width}x{height} (мин жағы {min_side}p) {max_quality}p шегінен асып кетті"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "ойнату тізімі"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ {service} үшін диапазон шегінен асып кетті: {count} (максимум {max_count}).\n\nМаксималды қолжетімді файлдарды жүктеу үшін мына командалардың бірін пайдаланыңыз:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ {service} үшін диапазон шегінен асып кетті: {count} (максимум {max_count})\nПайдаланушы ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "PO таңбалауышы провайдері конфигурацияда өшірілген"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} YouTube домені емес, PO белгісін өткізіп жібереді"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO таңбалауышы провайдері {base_url} мекенжайында қолжетімді емес, бұл стандартты YouTube экстракциясына қайта оралады"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO таңбалауышы провайдерінің кэші тазартылды, келесі сұрауда қолжетімділікті тексереді"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Қолданба данасы әлі қолжетімді емес"
    HELPER_USER_NAME_MSG = "Пайдаланушы"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Тасқын күту анықталды, {wait_seconds} секунд ұйықтап жатыр"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Су тасқынын күту анықталды, бірақ уақытты шығара алмады, {retry_delay} секунд ұйықтап жатыр"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno қатесі анықталды, {retry_delay} секунд ұйықтап жатыр"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Тікелей қосылымды пайдалану арқылы прокси конфигурациясы толық емес"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Жабу"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Жабу"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Жабу"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Журналдар файлы жойылды."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Тегтер файлы жойылды."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Пішім файлы жойылды."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Бөлінген файл жойылды."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Mediainfo файлы жойылды."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Субтитр параметрлері жойылды."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Пернетақта параметрлері жойылды."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Args параметрлері жойылды."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 NSFW параметрлері жойылды."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Прокси параметрлері жойылды."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Су тасқынын күту параметрлері жойылды."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Жабу"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Бейне жүктеп алу пәрмені"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Қолданылуы: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Мысалдар:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (direct order)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (reverse order)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Сондай-ақ қараңыз: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Пайдаланушы {user_id} тобына қосу_bot_пәрменін жауып тастады"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "YouTube идентификаторы шығарылмады"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Нобайды жүктеп алу мүмкін болмады немесе ол тым үлкен"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Аудио тілін таңдаңыз"
    AA_NO_SUBTITLES_DETECTED_MSG = "Субтитрлер анықталмады"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Субтитр тілін таңдаңыз"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Аутентификация қатесі"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Есептік жазба табылмады"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Account Unavailable"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Тариф шегінен асып кетті"
    GALLERY_DL_NETWORK_ERROR_MSG = "Желі қатесі"

    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Географиялық шектеулер"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Тексеру қажет"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Саясаттың бұзылуы"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Белгісіз қате"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Жүктеп алу басталды</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Жабу"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Бейне Жүктеу Командасы</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Қолдану: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Мысалдар:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Сондай-ақ қараңыз: /аудио, /img, /анықтама, /ойнату тізімі, /параметрлер"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Су тасқыны шегі. Кейінірек көріңіз."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Cookie Командасы Қолдануы</b>

<code>/cookie</code> - Cookie мәзірін көрсету
<code>/cookie youtube</code> - YouTube cookie файлдарын жүктеу
<code>/cookie instagram</code> - Instagram cookie файлдарын жүктеу
<code>/cookie tiktok</code> - TikTok cookie файлдарын жүктеу
<code>/cookie x</code> немесе <code>/cookie twitter</code> - Twitter/X cookie файлдарын жүктеу
<code>/cookie facebook</code> - Facebook cookie файлдарын жүктеу
<code>/cookie custom</code> - Арнайы cookie нұсқауларын көрсету

<i>Қолжетімді қызметтер бот конфигурациясына байланысты.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Cookie файлы жойылды және кэш тазартылды."
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 ТІЛ"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 ТАЗАЛАУ"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIES"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 МЕДИА"
    SETTINGS_INFO_BUTTON_MSG = "📖 АҚПАРАТ"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ КӨБІРЕК"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Тек cookies"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Журналдар "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Тегтер"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Формат"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Бөлу"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Субтитрлер"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Пернетақта"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Аргументтер"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Прокси"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Су тасқынын күту"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Барлық файлдар"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Менің 5 cookie файлымды жүктеу"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Браузердің YT-cookie алу"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Cookie файлыңызды тексеру"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Арнайы cookie жүктеу"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Сапа мен форматты өзгерту"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - MediaInfo қосу/өшіру"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Бөлінген бейне бөлігінің өлшемін өзгерту"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Бейнені аудио ретінде жүктеу"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Субтитр тілі баптаулары"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Плейлистерді қалай жүктеуге болады"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - gallery-dl арқылы суреттерді жүктеу"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - #тегтеріңізді жіберу"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Нұсқаулар алу"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Журналдарыңызды жіберу"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Плейлист көмегі"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - қалай"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Тікелей бейне сілтемелерін алу"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Проксиді қосу/өшіру"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Пернетақта орналасуы"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Ішкі іздеу көмекшісі"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp аргументтері"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - NSFW бұлыңғырлау баптаулары"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Тазалау Опциялары</b>\n\nНені тазалау керектігін таңдаңыз:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Ұялы телефон: @vid іздеуді белсендіріңіз"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Ұялы телефон: @vid іздеуді белсендіріңіз"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 OFF"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 FULL"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[Суреттердің URL мекенжайы]({url})"
    IMAGE_ERROR_MSG = "❌ Қате: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Артқа"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - теңшелетін пішім"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p сапасы"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K сапасы"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K сапасы"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - арнайы пішім идентификаторы"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - әрқашан мәзірді көрсету"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/ең жақсы сапа"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Always Ask (мәзір + батырмалар)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Басқалар (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (PC/Mac Telegram үшін ең жақсы)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (ұялы Telegram үшін ең жақсы)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (МАКС сапа)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Теңшелетін (өздеріңізді енгізіңіз)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Браузерден"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Өздеріңізді"
        
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Алдыңғы"
    SUBS_BACK_BUTTON_MSG = "🔙Артқа"
    SUBS_OFF_BUTTON_MSG = "🚫 ӨШІРУ"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - тілді орнату"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - AUTO/TRANS көмегімен тілді орнату"
    SUBS_VALID_OPTIONS_MSG = "Жарамды опциялар:"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Енгізу режимі әрекетсіздікке байланысты автоматты түрде жабылады (5 минут)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Барлығын қалпына келтіру"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Ағымдағыны көру"
    ARGS_BACK_BUTTON_MSG = "🔙 Артқа"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Бұл параметрлерді үлгі ретінде сақтау үшін осы хабарды таңдаулыларға бағыттаңыз.</i> \n\n<i>Бұл параметрлерді қолдану үшін осы хабарды осы жерге қайта бағыттаңыз.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Ағымдағы yt-dlp аргументтері:\n\nАрнайы параметрлер конфигурацияланбаған.\n\n---\n\n<i>Бұл параметрлерді үлгі ретінде сақтау үшін осы хабарды таңдаулыларға бағыттаңыз.</i> \n\n<i>Бұл параметрлерді қолдану үшін осы хабарды осы жерге қайта бағыттаңыз.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Ағымдағы yt-dlp аргументтері:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Параметрлерді экспорттау"
    ARGS_SETTINGS_READY_MSG = "Параметрлер экспорттауға дайын! Сақтау үшін осы хабарды таңдаулыларға бағыттаңыз."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Ағымдағы yt-dlp аргументтері:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Хабарламадағы параметрлерді тану мүмкін болмады. Дұрыс параметрлер үлгісін жібергеніңізге көз жеткізіңіз."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Параметрлер сәтті импортталды!\n\nҚолданылған параметрлер: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Негізгі параметрлер:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Импортталған параметрлерді сақтау қатесі."
    ARGS_ERROR_IMPORTING_MSG = "❌ Параметрлерді импорттау кезінде қате орын алды."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Cookie файлдарын жүктеп алу</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Cookie файлын жүктеп алу үшін қызметті таңдаңыз."
    COOKIE_MENU_SAVE_INFO_MSG = "Cookie файлдары қалтаңызда cookie.txt ретінде сақталады."
    COOKIE_MENU_TIP_HEADER_MSG = "Кеңес: Сондай-ақ, тікелей пәрменді пайдалануға болады:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – cookie файлдарын жүктеп алыңыз және растаңыз"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – индекс бойынша белгілі бір көзді пайдаланыңыз (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Содан кейін <code>/check_cookie</code> арқылы растаңыз (RickRoll жүйесіндегі сынақтар)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Әрқашан Сұрау"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Сілтеме"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Watch"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Сипаттама"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ КЕСУ"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Бейне кесу</b>\n\nБейне ұзақтығы: <b>{start_time} - {end_time}</b>\n\nӨтінеміз, қалаған уақыт аралығын форматта жіберіңіз:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nМысал: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Жарамсыз формат. Өтінеміз, пайдаланыңыз: <code>HH:MM:SS-HH:MM:SS</code>\n\nМысал: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Жарамсыз аралық. Басталу уақыты аяқталу уақытынан кіші болуы керек."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ Уақыт аралығы бейненің шекараларынан тыс.\n\nБейне ұзақтығы: <b>{start_time} - {end_time}</b>\n\nСіздің аралығыңыз осы шектеулер ішінде болуы керек."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>Бейне қиылады:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Ішінара аяқталды - {successful_uploads}/{to{total_files}dio файлдары жүктеп салынды."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Аудио сәтті жүктеліп, жіберілді - {total_files} файлдар жүктеп салынды."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Жеке TikTok Аккаунты</b>\n\n"
        "Бұл TikTok аккаунты жеке немесе барлық бейнелер жеке.\n\n"
        "<b>💡 Шешу жолы:</b>\n"
        "1. @{username} аккаунтына жазылыңыз\n"
        "2. Ботқа cookie файлдарыңызды <code>/cookie</code> командасы арқылы жіберіңіз\n"
        "3. Қайталап көріңіз\n\n"
        "<b>Cookie файлдарын жаңартқаннан кейін қайталап көріңіз!</b>"
    )

    #######################################################
