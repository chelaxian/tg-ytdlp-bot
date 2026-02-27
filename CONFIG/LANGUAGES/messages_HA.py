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
    CREDITS_MSG = "<blockquote><i>Ana gudanar da shi ta</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Canza harshe: /lang</b>"
    TO_USE_MSG = "<i>Don amfani da wannan bot kuna buƙatar yin rajista zuwa tashar Telegram @tg_ytdlp.</i>\nBayan kun shiga tashar, <b>sake aika hanyar bidiyon ku kuma bot zai sauke shi gare ku</b> ❤️\n\n<blockquote>P.S. Saboda yuwuwar 🔞NSFW abun ciki - saukewa daga ☁️<b>Ajiyar Girgije</b>, 📁<b>Raba Fayiloli</b>, 🔗<b>Gajeriyar URL</b> da 🔞<b>Shafukan batsa</b> ana biya! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Kada ku 🗑<b>share/i-unsubscribe tashar @tg_ytdlp</b> kuma kada ku 🤖<b>yi spam da URL/umarni da yawa ga bot</b> - za a hana ku amfani da bot ta atomatik ⛔️</blockquote>"

    ERROR1 = "Ba a sami hanyar url ba. Da fatan za a shigar da url tare da <b>https://</b> ko <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Jerin Bidiyo (yt-dlp)</b>

Don sauke jerin bidiyo aika URL tare da <code>*start*end</code> ranges a ƙarshe. Misali: <code>URL*1*5</code> (bidiyo 5 na farko daga 1 zuwa 5 ciki).<code>URL*-1*-5</code> (bidiyo 5 na ƙarshe daga 1 zuwa 5 ciki).
Ko kuma zaka iya amfani da <code>/vid DAGA-ZUWA URL</code>. Misali: <code>/vid 3-7 URL</code> (yana sauke bidiyo daga 3 zuwa 7 ciki daga farko). <code>/vid -3-7 URL</code> (yana sauke bidiyo daga 3 zuwa 7 ciki daga ƙarshe). Hakanan yana aiki don umarnin <code>/audio</code>.

<b>Misalai:</b>

🟥 <b>Kewayon bidiyo daga jerin bidiyo na YouTube:</b> (ana buƙatar 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(yana sauke bidiyo 5 na farko daga 1 zuwa 5 ciki)
🟥 <b>Bidiyo guda ɗaya daga jerin bidiyo na YouTube:</b> (ana buƙatar 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(yana sauke bidiyo na 3 kawai)

⬛️ <b>Bayani na TikTok:</b> (ana buƙatar 🍪 naka)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(yana sauke bidiyo 10 na farko daga bayanin mai amfani)

🟪 <b>Labarun Instagram:</b> (ana buƙatar 🍪 naka)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(yana sauke labarai 3 na farko)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(yana sauke labarai 10 na farko daga kundi)

🟦 <b>Bidiyoyin VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(yana sauke bidiyo 3 na farko daga bayanin mai amfani/ƙungiya)

⬛️<b>Tashoshin Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(yana sauke bidiyo daga 2 zuwa 4 ciki daga tashar)

🟪 <b>Guntayen Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(yana sauke guntaye 3 na farko daga tashar)

🟦 <b>Ƙungiyoyin Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(yana sauke bidiyo 2 na farko daga ƙungiya)

🟧 <b>Samfuran Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(yana sauke bidiyo 2 na farko daga bayanin samfura)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(yana sauke bidiyo 3 na farko daga sakamakon bincike ta hanyar neman ku)

da sauransu...
duba <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">jerin shafukan da aka goyan baya</a>
</blockquote>

<blockquote expandable>🖼 <b>Hotuna (gallery-dl)</b>

Yi amfani da <code>/img URL</code> don sauke hotuna/hoto/kundin hotuna daga dandamali da yawa.

<b>Misalai:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Kewayon:</b>
<code>/img 11-20 https://example.com/album</code> — abubuwa 11..20
<code>/img 11- https://example.com/album</code> — daga 11 zuwa ƙarshe (ko iyakar bot)

<i>Dandamali da aka goyan baya sun haɗa da vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, da sauransu. Cikakken jerin:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">shafukan da gallery-dl ke goyan baya</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Bot na Saukewa Bidiyo - Taimako</b>

📥 <b>Amfani na Asali:</b>
• Aika kowane hanyar haɗi → bot yana saukewa
  <i>bot yana ƙoƙarin saukewa bidiyo ta hanyar yt-dlp da hotuna ta hanyar gallery-dl.</i>
• <b>URLs da yawa:</b> A cikin yanayin zaɓin inganci (<code>/format</code>) zaka iya aika har zuwa <b>10 URLs</b> a cikin saƙo ɗaya. Kowane URL akan sabon layi ko rabu da sarari.
• <code>/audio URL</code> → fitar da sauti
• <code>/link [quality] URL</code> → sami hanyoyin haɗi kai tsaye
• <code>/proxy</code> → kunna/kashe proxy don duk saukewa
• Amsa bidiyo da rubutu → canza taken

📋 <b>Jerin Bidiyo & Kewayon:</b>
• <code>URL*1*5</code> → sauke bidiyo 5 na farko
• <code>URL*-1*-5</code> → sauke bidiyo 5 na ƙarshe
• <code>/vid 3-7 URL</code> → ya zama <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → ya zama <code>URL*-3*-7</code>

🍪 <b>Cookies & Private:</b>
• Loda *.txt cookie don bidiyoyi masu zaman kansu
• <code>/cookie [service]</code> → sauke cookies (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → zaɓi tushe ta fihirisa (1–N)
• <code>/cookies_from_browser</code> → fitar daga browser
• <code>/check_cookie</code> → tabbatar da cookie
• <code>/save_as_cookie</code> → adana rubutu azaman cookie

🧹 <b>Tsabtacewa:</b>
• <code>/clean</code> → fayilolin kafofin watsa labarai kawai
• <code>/clean all</code> → komai
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Saituna:</b>
• <code>/settings</code> → menu na saituna
• <code>/format</code> → inganci & tsari
• <code>/split</code> → raba bidiyo zuwa sassa
• <code>/mediainfo on/off</code> → bayanin kafofin watsa labarai
• <code>/nsfw on/off</code> → blur NSFW
• <code>/tags</code> → duba tags da aka adana
• <code>/sub on/off</code> → rubutun ƙasa
• <code>/keyboard</code> → keyboard (OFF/1x3/2x3)

🏷️ <b>Tags:</b>
• Ƙara <code>#tag1#tag2</code> bayan URL
• Tags suna bayyana a cikin taken
• <code>/tags</code> → duba duk tags

🔗 <b>Hanyoyin Haɗi Kai Tsaye:</b>
• <code>/link URL</code> → mafi kyawun inganci
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → inganci na musamman

⚙️ <b>Umarni na Gaggawa:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → saita inganci
• <code>/keyboard off/1x3/2x3/full</code> → tsarin keyboard
• <code>/split 100mb-2000mb</code> → canza girman ɓangare
• <code>/subs off/ru/en auto</code> → yaren rubutun ƙasa
• <code>/list URL</code> → jerin tsarukan da ake samu
• <code>/mediainfo on/off</code> → kunna/kashe bayanin kafofin watsa labarai
• <code>/proxy on/off</code> → kunna/kashe proxy don duk saukewa

📊 <b>Bayani:</b>
• <code>/usage</code> → tarihin saukewa
• <code>/search</code> → bincike na cikin layi ta hanyar @vid

🖼 <b>Hotuna:</b>
• <code>URL</code> → sauke hotuna URL
• <code>/img URL</code> → sauke hotuna daga URL
• <code>/img 11-20 URL</code> → sauke kewayon na musamman
• <code>/img 11- URL</code> → sauke daga na 11 zuwa ƙarshe

👨‍💻 <i>Mai Haɓakawa:</i> @upekshaip
🤝 <i>Mai Ba da Gudummawa:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Kawai adana cookie naka azaman <b><u>cookie.txt</u></b> kuma aika shi zuwa bot azaman takarda.\n\n"
        "Hakanan zaka iya aika cookies azaman rubutu mai sauƙi tare da umarnin <b><u>/save_as_cookie</u></b>.\n"
        "<b>Amfani da <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>Umarni:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message
    SEARCH_MSG = """
🔍 <b>Binciken Bidiyo</b>

Danna maɓallin da ke ƙasa don kunna bincike na cikin layi ta hanyar @vid.

<blockquote>A kan PC kawai rubuta <b>"@vid Your_Search_Query"</b> a cikin kowane tattaunawa.</blockquote>
    """
    
    # Settings and Hints
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Umarnin Saukewa Hotuna</b>\n\n"
        "Amfani: <code>/img URL</code>\n\n"
        "<b>Misalai:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Dandamali da aka goyan baya (misalai):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, da sauransu — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">cikakken jerin</a></blockquote>"
        "Hakanan duba: "
    )
    
    LINK_HINT_MSG = (
        "Sami hanyoyin haɗi kai tsaye na bidiyo tare da zaɓin inganci.\n\n"
        "Amfani: /link + URL \n\n"
        "(misali. /link https://youtu.be/abc123)\n"
        "(misali. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Ƙara Bot zuwa Ƙungiya</b>

Ƙara bots dina zuwa ƙungiyoyin ku don samun ingantattun fasaloli da iyakoki masu girma!
————————————
📊 <b>Iyaka na KYAUTA na Yanzu (a cikin DM na Bot):</b>
<blockquote>•🗑 Dattin dattin daga duk fayilolin da ba a tsara su ba 👎
• Matsakaicin girman fayil 1: <b>8 GB </b>
• Matsakaicin ingancin fayil 1: <b>BA IYAKA</b>
• Matsakaicin tsawon fayil 1: <b>BA IYAKA</b>
• Matsakaicin adadin saukewa: <b>BA IYAKA</b>
• Matsakaicin URLs a cikin saƙo ɗaya: <b>10</b> (kawai a cikin yanayin zaɓin inganci)
• Matsakaicin abubuwan jerin bidiyo a kowane lokaci 1: <b>50</b>
• Matsakaicin bidiyoyin TikTok a kowane lokaci 1: <b>500</b>
• Matsakaicin hotuna a kowane lokaci 1: <b>1000</b>
• Iyakokin ƙimar URL: <b>5/min, 60/hour, 1000/day</b>
• Iyakar umarni: <b>20/min</b>
• 1 Saukewa matsakaicin lokaci: <b>sa'o'i 2</b>
• 🔞 Abun ciki na NSFW ana biya! 1⭐️ = $0.02
• 🆓 DUK SAURAN KAFOFIN WATSAN LABARAI SUNA KYAU GABAN ɗAYA
• 📝 Duk tarihin abun ciki & caching zuwa tashoshin log dina don sake bugawa nan take lokacin sake saukewa</blockquote>

💬<b>Wannan iyakoki kawai don bidiyo tare da rubutun ƙasa:</b>
<blockquote>• Matsakaicin tsawon bidiyo+rubutun ƙasa: <b>sa'o'i 1.5</b>
• Matsakaicin girman fayil na bidiyo+rubutun ƙasa: <b>500 MB</b>
• Matsakaicin ingancin bidiyo+rubutun ƙasa: <b>720p</b></blockquote>
————————————
🚀 <b>Fa'idodin Ƙungiyar da Ake Biya (Iyaka 2️⃣x):</b>
<blockquote>•  🗂 Rumbun kafofin watsa labarai masu tsari da aka tsara ta batutuwa 👍
•  📁 Bots suna amsawa a cikin batun da kuka kira su
•  📌 Auto pin saƙon matsayi tare da ci gaban saukewa
•  🖼 Umarnin /img yana saukewa kafofin watsa labarai azaman kundin abubuwa 10
• Matsakaicin girman fayil 1: <b>16 GB</b> ⬆️
• Matsakaicin URLs a cikin saƙo ɗaya: <b>20</b> ⬆️ (kawai a cikin yanayin zaɓin inganci)
• Matsakaicin abubuwan jerin bidiyo a kowane lokaci 1: <b>100</b> ⬆️
• Matsakaicin bidiyoyin TikTok a kowane lokaci 1: 1000 ⬆️
• Matsakaicin hotuna a kowane lokaci 1: 2000 ⬆️
• Iyakokin ƙimar URL: <b>10/min, 120/hour, 2000/day</b> ⬆️
• Iyakar umarni: <b>40/min</b> ⬆️
• 1 Saukewa matsakaicin lokaci: <b>sa'o'i 4</b> ⬆️
• 🔞 Abun ciki na NSFW: Kyauta tare da cikakken metadata 🆓
• 📢 Ba lallai ba ne yin rajista zuwa tashar tawa don ƙungiyoyi
• 👥 Duk membobin ƙungiya za su sami damar ayyukan da ake biya!
• 🗒 Babu logs / babu cache zuwa tashoshin log dina! Zaka iya ƙi kwafi/sake bugawa a cikin saitunan ƙungiya</blockquote>

💬 <b>Iyaka 2️⃣x don bidiyo tare da rubutun ƙasa:</b>
<blockquote>• Matsakaicin tsawon bidiyo+rubutun ƙasa: <b>sa'o'i 3</b> ⬆️
• Matsakaicin girman fayil na bidiyo+rubutun ƙasa: <b>1000 MB</b> ⬆️
• Matsakaicin ingancin bidiyo+rubutun ƙasa: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Farashi & Saitawa:</b>
<blockquote>• Farashi: <b>$5/wata</b> don kowane bot 1 a cikin ƙungiya
• Saitawa: Tuntuɓi @iilililiiillliiliililliilliliiil
• Biyan kuɗi: 💎TON ko wasu hanyoyi💲
• Taimako: Cikakken tallafin fasaha ya haɗa</blockquote>
————————————
Zaka iya ƙara bots dina zuwa ƙungiyar ku don buɗe kyauta 🔞<b>NSFW</b> kuma don ninka (x2️⃣) duk iyakoki.
Tuntuɓe ni idan kana son in ba ƙungiyar ku damar amfani da bots dina @iilililiiillliiliililliilliliiil
————————————
💡<b>SHAWARA:</b> <blockquote>Zaka iya ba da kuɗi tare da kowane adadin abokanka (misali mutane 100) kuma ka yi siyayya 1 don dukan ƙungiya - DUK MEMBONIN ƘUNGIYA ZA SU SAMI CIKAKKIYAR DAMAR BA IYAKA ga duk ayyukan bots a cikin wannan ƙungiya don kawai <b>$0.05</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>Yanayin NSFW: KUNNA✅</b>

• Abun ciki na NSFW zai bayyana ba tare da blur ba.
• Spoilers ba za su yi aiki ba ga kafofin watsa labarai na NSFW.
• Abun ciki zai bayyana nan take

<i>Yi amfani da /nsfw off don kunna blur</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>Yanayin NSFW: KASHE</b>

⚠️ <b>Blur ya kunna</b>
• Abun ciki na NSFW zai ɓoye a ƙarƙashin spoiler   
• Don duba, zaka buƙaci danna kafofin watsa labarai
• Spoilers za su yi aiki ga kafofin watsa labarai na NSFW.

<i>Yi amfani da /nsfw on don kashe blur</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Parameter mara inganci</b>

Yi amfani da:
• <code>/nsfw on</code> - kashe blur
• <code>/nsfw off</code> - kunna blur
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Ana duba cache...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Ana sarrafawa..."
    DOWNLOADING_MSG = "📥 <b>Ana saukewa kafofin watsa labarai...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Ana saukewa hoto...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Saukewa ya cika</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "An sauke:"
    SENT_STATUS_MSG = "An aika:"
    PENDING_TO_SEND_STATUS_MSG = "Ana jira aika:"
    TITLE_LABEL_MSG = "Take:"
    MEDIA_COUNT_LABEL_MSG = "Adadin kafofin watsa labarai:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Saukewa ya ƙare, ana sarrafa sauti..."
    VIDEO_PROCESSING_MSG = "📽 Bidiyo yana sarrafawa..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>An aika daga cache</b>\n\nKundin da aka aika: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ An aika bidiyo cikin nasara daga cache."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ An aika bidiyoyin jerin bidiyo daga cache ({cached}/{total} fayiloli)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} bidiyoyi an aika daga cache, ana saukewa waɗanda suka ɓace..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ An aika daga cache: {cached}\n🔄 Ana ci gaba da saukewa..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Ba za a iya nazarin kafofin watsa labarai ba, ana ci gaba da matsakaicin kewayon da aka yarda (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Ba za a iya ƙayyade adadin kafofin watsa labarai ba, ana ci gaba da matsakaicin kewayon da aka yarda (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Ba za a iya ƙayyade jimillar adadin kafofin watsa labarai ba, ana ci gaba da kewayon da aka ƙayyade {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>URL mara inganci</b>\n\nDa fatan za a ba da URL mai inganci wanda ya fara da http:// ko https://"

    ERROR_OCCURRED_MSG = "❌ <b>Kuskure ya faru</b>\n\n<code>{url}</code>\n\nKuskure: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Kuskure wajen aika aika: {error}"
    ERROR_UNKNOWN_MSG = "❌ Kuskure da ba a sani ba: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Babu isasshen sarari na diski don saukewa bidiyoyi."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Girman fayil ya wuce iyakar {limit} GB. Da fatan za a zaɓi fayil ƙarami a cikin girman da aka yarda."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>An kasa saukar da bidiyo tare da duk wakilcin da ake da shi</b>\n\nDuk ƙoƙarin saukewa ta hanyar wakilci sun gaza.\nGwada:\n• Bincika aikin wakilci\n• Gwada wani wakilci daga jerin\n• Saukewa ba tare da wakilci ba (idan zai yiwu)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Kuskure wajen samun hanyar haɗi:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram ya iyakance aika saƙo.\n⏳ Da fatan za a jira: {time}\nDon sabunta lokaci aika URL sake sau 2."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram ya iyakance aika saƙo.\n⏳ Da fatan za a jira: \nDon sabunta lokaci aika URL sake sau 2."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ An gaza saukewa rubutun ƙasa"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Hanyoyin Haɗi Kai Tsaye na Stream</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Take:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Tsawon lokaci:</b> {duration} daƙiƙa\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Kuskure: Ba a sami saƙon asali ba."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{tag} ya ƙunshi haruffa da aka haramta. Haruffa, lambobi da _ kawai ana yarda.\nDa fatan za a yi amfani da: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ An aika bidiyoyin jerin bidiyo: {sent}/{total} fayiloli."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>Shawara game da jerin bidiyo</b>

Kun aika hanyar haɗin jerin bidiyo ba tare da ƙayyade kewayon ba. Bot ya zazzage bidiyon farko ta atomatik (<code>*1*1</code>).

<b>Don zazzage bidiyo da yawa daga jerin bidiyo, ƙayyade kewayon:</b>
• <code>URL*1*5</code> — bidiyo 5 na farko (daga 1 zuwa 5 ciki har da)
• <code>URL*3*3</code> — bidiyo na 3 kawai
• <code>/vid 1-10 URL</code> — tsarin madadin

Koyi ƙari: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ An aika daga cache: {cached}/{total} fayiloli."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ An gaza samun hanyoyin haɗi na stream"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Zaɓi browser don saukewa cookies daga:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Ba a sami browsers a kan wannan tsarin ba. Zaka iya buɗa cookies daga URL mai nisa ko saka idanu kamar browser:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Bude Browser</b> - don saka idanu da browser a cikin mini-app"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Bude Browser"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 tashar daga URL Mai Nisa"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ An sauke fayil cookies na YouTube ta hanyar fallback kuma an adana shi azaman cookies.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Ba a sami browsers da aka goyan baya ba kuma ba a saita COOKIE_URL ba. Yi amfani da /cookie ko loda cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ COOKIE_URL fallback dole ne ya nuna zuwa fayil .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fayil cookie fallback ya yi girma (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Tushen cookie fallback ba ya samuwa (matsayi {status}). Gwada /cookie ko loda cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Kuskure wajen saukewa cookie fallback. Gwada /cookie ko loda cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Kuskure da ba zato ba tsammani yayin saukewa cookie fallback."
    BTN_CLOSE = "🔚Rufe"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Ƙimar boolean mara inganci"
    ARGS_CLOSED_MSG = "An rufe"
    ARGS_ALL_RESET_MSG = "✅ An sake saita duk hujjoji"
    ARGS_RESET_ERROR_MSG = "❌ Kuskure wajen sake saita hujjoji"
    ARGS_INVALID_PARAM_MSG = "❌ Parameter mara inganci"
    ARGS_BOOL_SET_MSG = "An saita zuwa {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "An riga an saita zuwa {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Ƙimar zaɓi mara inganci"
    ARGS_VALUE_SET_MSG = "An saita zuwa {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "An riga an saita zuwa {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Ƙimar yanzu:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Misalai:</b>\n• <code>default</code> - Yi amfani da dabarar XFF ta asali\n• <code>never</code> - Kada a taɓa amfani da kan XFF\n• <code>US</code> - Lambar ƙasa ta Amurka\n• <code>GB</code> - Lambar ƙasa ta Burtaniya\n• <code>DE</code> - Lambar ƙasa ta Jamus\n• <code>FR</code> - Lambar ƙasa ta Faransa\n• <code>JP</code> - Lambar ƙasa ta Japan\n• <code>192.168.1.0/24</code> - Rukunin IP (CIDR)\n• <code>10.0.0.0/8</code> - Kewayon IP na sirri\n• <code>203.0.113.0/24</code> - Rukunin IP na jama'a\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Lura:</b> Wannan yana maye gurbin zaɓuɓɓukan --geo-bypass. Yi amfani da kowane lambar ƙasa ta haruffa 2 ko rukunin IP a cikin alamar CIDR.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Misali:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Da fatan za a aika ƙimar sabuwar ku."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Kewayon:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Da fatan za a aika lamba."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Misalai:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Lura:</b> Waɗannan kawunan za a ƙara su zuwa kawunan Referer da User-Agent da suka wanzu.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Hujjojin yt-dlp na Yanzu:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - Sauye-sauye na Gaskiya/Ƙarya\n• 📋 <b>Zaɓi</b> - Zaɓi daga zaɓuɓɓuka\n• 🔢 <b>Lamba</b> - Shigar da lamba\n• 📝🔧 <b>Rubutu</b> - Shigar da Rubutu/JSON</blockquote>\n\nWaɗannan saitunan za a yi amfani da su ga duk saukewan ku."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "Tilasta haɗin IPv6",
        "force_ipv4": "Tilasta haɗin IPv4", 
        "no_live_from_start": "Kada a sauke streams na kai tsaye daga farko",
        "live_from_start": "Sauke streams na kai tsaye daga farko",
        "no_check_certificates": "Kashe tabbatarwar takardar shaida HTTPS",
        "check_certificate": "Duba takardar shaida SSL",
        "no_playlist": "Sauke bidiyo guda ɗaya kawai, ba jerin bidiyo ba",
        "embed_metadata": "Saka metadata a cikin fayil bidiyo",
        "embed_thumbnail": "Saka thumbnail a cikin fayil bidiyo",
        "write_thumbnail": "Rubuta thumbnail zuwa fayil",
        "ignore_errors": "Yi watsi da kurakuran saukewa kuma ci gaba",
        "legacy_server_connect": "Ba da izinin haɗin uwar garken tsoho",
        "concurrent_fragments": "Adadin guntayen da za a sauke a lokaci guda",
        "xff": "Dabarar kan X-Forwarded-For",
        "user_agent": "Kan User-Agent",
        "impersonate": "Kwaikwayon browser",
        "referer": "Kan Referer",
        "geo_bypass": "Ketare haniyyoyin yanki",
        "hls_use_mpegts": "Yi amfani da MPEG-TS don HLS",
        "no_part": "Kada a yi amfani da fayilolin .part",
        "no_continue": "Kada a ci gaba da saukewa na ɓangare",
        "audio_format": "Tsarin sauti",
        "video_format": "Tsarin bidiyo",
        "merge_output_format": "Tsarin fitarwa na haɗawa",
        "send_as_file": "Aika azaman fayil",
        "username": "Sunan mai amfani",
        "password": "Kalmar sirri",
        "twofactor": "Lambar tabbatarwa ta hanyoyi biyu",
        "min_filesize": "Matsakaicin girman fayil (MB)",
        "max_filesize": "Matsakaicin girman fayil (MB)",
        "playlist_items": "Abubuwan jerin bidiyo",
        "date": "Kwanan wata",
        "datebefore": "Kwanan wata kafin",
        "dateafter": "Kwanan wata bayan",
        "http_headers": "Kawunan HTTP",
        "sleep_interval": "Tazarar bacci",
        "max_sleep_interval": "Matsakaicin tazarar bacci",
        "retries": "Adadin sake gwadawa",
        "http_chunk_size": "Girman chunk HTTP",
        "sleep_subtitles": "Bacci don rubutun ƙasa"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ Saitunan Hujjojin yt-dlp</b>\n\n<blockquote>📋 <b>Ƙungiyoyi:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ Saitunan Hujjojin yt-dlp</b>\n\n"
        "<blockquote>📋 <b>Ƙungiyoyi:</b>\n"
        "• ✅/❌ <b>Boolean</b> - Sauye-sauye na Gaskiya/Ƙarya\n"
        "• 📋 <b>Zaɓi</b> - Zaɓi daga zaɓuɓɓuka\n"
        "• 🔢 <b>Lamba</b> - Shigar da lamba\n"
        "• 📝🔧 <b>Rubutu</b> - Shigar da Rubutu/JSON</blockquote>\n\n"
        "Waɗannan saitunan za a yi amfani da su ga duk saukewan ku."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Da fatan za a jira..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Kuskure ya faru"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ yanayin yanayin ya rufe ta saboda rashin aiki (minti 5)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Shigarwa ta ƙunshi abun ciki mai haɗari: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Shigarwa ta yi tsayi (matsakaici 1000 haruffa)"
    ARGS_INVALID_URL_MSG = "❌ Tsarin URL mara inganci. Dole ne ya fara da http:// ko https://"
    ARGS_INVALID_JSON_MSG = "❌ Tsarin JSON mara inganci"
    ARGS_NUMBER_RANGE_MSG = "❌ Lamba dole ne ta kasance tsakanin {min_val} da {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Tsarin lamba mara inganci"
    ARGS_DATE_FORMAT_MSG = "❌ Kwanan wata dole ne ya kasance a cikin tsarin YYYYMMDD (misali, 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Shekara dole ne ta kasance tsakanin 1900 da 2100"
    ARGS_MONTH_RANGE_MSG = "❌ Wata dole ne ya kasance tsakanin 01 da 12"
    ARGS_DAY_RANGE_MSG = "❌ Rana dole ne ta kasance tsakanin 01 da 31"
    ARGS_INVALID_DATE_MSG = "❌ Tsarin kwanan wata mara inganci"
    ARGS_INVALID_XFF_MSG = "❌ XFF dole ne ya zama 'default', 'never', lambar ƙasa (misali, US), ko rukunin IP (misali, 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "Ba a saita hujjoji na al'ada ba. Duk ma'auni suna amfani da ƙimomin asali."
    ARGS_RESET_SUCCESS_MSG = "✅ An sake saita duk hujjoji zuwa na asali."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Rubutu ya yi tsayi. Matsakaici haruffa 500."
    ARGS_ERROR_PROCESSING_MSG = "❌ Kuskure wajen sarrafa shigarwa. Da fatan za a sake gwadawa."
    ARGS_BOOL_INPUT_MSG = "❌ Da fatan za a shigar da 'True' ko 'False' don zaɓin Aika Azaman Fayil."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Da fatan za a ba da lamba mai inganci."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Da fatan za a aika <code>True</code> ko <code>False</code> don kunna/kashe wannan zaɓi."
    ARGS_JSON_VALUE_REQUEST_MSG = "Da fatan za a aika JSON mai inganci."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Ba ka da tags tukuna."
    TAGS_MESSAGE_CLOSED_MSG = "An rufe saƙon tags."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ An kashe rubutun ƙasa kuma an kashe yanayin Luôn Hỏi."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ An kunna SUBS Luôn Hỏi."
    SUBS_LANGUAGE_SET_MSG = "✅ An saita yaren rubutu zuwa: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️GARGADI: saboda tasirin CPU mai girma wannan aikin yana da sannu a hankali (kusa da lokaci na gaske) kuma an iyakance shi zuwa:\n"
        "- Matsakaicin inganci 720p\n"
        "- Matsakaicin tsawon lokaci sa'o'i 1.5\n"
        "- Matsakaicin girman bidiyo 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Umarni masu sauri:</b>\n"
        "• <code>/subs off</code> - kashe rubutun ƙasa\n"
        "• <code>/subs on</code> - kunna yanayin Luôn Hỏi\n"
        "• <code>/subs ru</code> - saita yare\n"
        "• <code>/subs ru auto</code> - saita yare tare da AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 An kashe rubutun ƙasa"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Yaren da aka zaɓa: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Ana saukewa rubutun ƙasa..."
    SUBS_DISABLED_ERROR_MSG = "❌ An kashe rubutun ƙasa. Yi amfani da /subs don saita."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Saukewa rubutun ƙasa yana goyan baya kawai don YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Rubutun ƙasa</b>\n\n"
        "<b>Bidiyo:</b> {title}\n"
        "<b>Yare:</b> {lang}\n"
        "<b>Nau'i:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 An aika fayil SRT na rubutun ƙasa zuwa mai amfani."
    SUBS_ERROR_PROCESSING_MSG = "❌ Kuskure wajen sarrafa fayil rubutun ƙasa."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ An gaza saukewa rubutun ƙasa."
    SUBS_ERROR_MSG = "❌ Kuskure wajen saukewa rubutun ƙasa: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ An saita girman ɓangaren raba zuwa: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **Girman mara inganci!**\n\n"
        "**Kewayon mai inganci:** 100MB zuwa 2GB\n\n"
        "**Tsare-tsare masu inganci:**\n"
        "• `100mb` zuwa `2000mb` (megabytes)\n"
        "• `0.1gb` zuwa `2gb` (gigabytes)\n\n"
        "**Misalai:**\n"
        "• `/split 100mb` - megabytes 100\n"
        "• `/split 500mb` - megabytes 500\n"
        "• `/split 1.5gb` - gigabytes 1.5\n"
        "• `/split 2gb` - gigabytes 2\n"
        "• `/split 2000mb` - megabytes 2000 (2GB)\n\n"
        "**Saitunan da aka saita:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Zaɓi matsakaicin girman ɓangare don raba bidiyo:**\n\n"
        "**Kewayon:** 100MB zuwa 2GB\n\n"
        "**Umarni masu sauri:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Misalai:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "An rufe menu."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Saitunan Bot</b>\n\nZaɓi rukuni:"
    SETTINGS_MENU_CLOSED_MSG = "An rufe menu."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Zaɓuɓɓukan Tsabtacewa</b>\n\nZaɓi abin da za a tsabtace:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nZaɓi aiki:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 KAFOFIN WATSA LABARAI</b>\n\nZaɓi aiki:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 BAYANI</b>\n\nZaɓi aiki:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ ƘARIN UMARNI</b>\n\nZaɓi aiki:"
    SETTINGS_COMMAND_EXECUTED_MSG = "An aiwatar da umarni."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Iyakar flood. Gwada daga baya."
    SETTINGS_HINT_SENT_MSG = "An aika shawara."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "An buɗe mataimakin bincike."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Umarni da ba a sani ba."
    SETTINGS_HINT_CLOSED_MSG = "An rufe shawara."
    SETTINGS_HELP_SENT_MSG = "Aika rubutun taimako zuwa mai amfani"
    SETTINGS_MENU_OPENED_MSG = "An buɗe menu /settings"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 An rufe mataimakin bincike"
    SEARCH_CLOSED_MSG = "An rufe"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Wakili {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Kuskure wajen adana saitunan proxy."
    PROXY_MENU_TEXT_MSG = "Kunna ko kashe amfani da uwar garken proxy don duk ayyukan yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Kunna ko kashe ta amfani da sabar wakili ({config_count} + {file_count} akwai) don duk ayyukan yt-dlp?\n\nLokacin da aka kunna DUKA (AUTO), za a zaɓi proxies ta hanyar bazuwar hanya."
    PROXY_MENU_CLOSED_MSG = "An rufe menu."
    PROXY_ENABLED_CONFIRM_MSG = "✅ An kunna proxy. Duk ayyukan yt-dlp za su yi amfani da proxy."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ An kunna proxy. Duk ayyukan yt-dlp za su yi amfani da uwar garken proxy {count} tare da hanyar zaɓi {method}."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ An kunna wakili (duk yanayin AUTO).\n\n📊 Bot zai gwada proxies ta wannan tsari:\n1️⃣ {config_count} proxies daga Config.py\n2️⃣ {file_count} proxies daga TXT/proxy.txt fayil\n\n🔄 Duk proxies za a gwada su bi da bi har sai an yi nasarar haɗin gwiwa."
    PROXY_DISABLED_MSG = "❌ An kashe proxy."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Kuskure wajen adana saitunan proxy."
    PROXY_ENABLED_CALLBACK_MSG = "An kunna proxy."
    PROXY_DISABLED_CALLBACK_MSG = "An kashe proxy."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ JIRA HAR SAUKEWAN DA YA GABATA YA ƘARE"
    AUDIO_HELP_MSG = (
        "<b>🎧 Umarnin Saukewa Sauti</b>\n\n"
        "Amfani: <code>/audio URL</code>\n\n"
        "<b>Misalai:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Hakanan duba: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "An rufe shawara sauti."
    PLAYLIST_HELP_CLOSED_MSG = "An rufe taimakon jerin bidiyo."
    USERLOGS_CLOSED_MSG = "An rufe saƙon logs."
    HELP_CLOSED_MSG = "An rufe taimako."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>Saitunan Blur NSFW</b>\n\nAbun ciki na NSFW yana <b>{status}</b>.\n\nZaɓi ko za a blur abun ciki na NSFW:"
    NSFW_MENU_CLOSED_MSG = "An rufe menu."
    NSFW_BLUR_DISABLED_MSG = "An kashe blur NSFW."
    NSFW_BLUR_ENABLED_MSG = "An kunna blur NSFW."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "An kashe blur NSFW."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "An kunna blur NSFW."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Kunna ko kashe aika MediaInfo don fayilolin da aka sauke?"
    MEDIAINFO_MENU_CLOSED_MSG = "An rufe menu."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ An kunna MediaInfo. Bayan saukewa, za a aika bayanin fayil."
    MEDIAINFO_DISABLED_MSG = "❌ An kashe MediaInfo."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "An kunna MediaInfo."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "An kashe MediaInfo."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Jerin Tsare-tsare Masu Samuwa</b>\n\n"
        "Sami tsare-tsare na bidiyo/sauti masu samuwa don URL.\n\n"
        "<b>Amfani:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Misalai:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Yadda ake amfani da ID na tsari:</b>\n"
        "Bayan samun jerin, yi amfani da ID na tsari na musamman:\n"
        "• <code>/format id 401</code> - sauke tsari 401\n"
        "• <code>/format id401</code> - iri ɗaya da na sama\n"
        "• <code>/format id140 audio</code> - sauke tsari 140 azaman sauti MP3\n\n"
        "Wannan umarni zai nuna duk tsare-tsare masu samuwa waɗanda za a iya saukewa."
    )
    LIST_PROCESSING_MSG = "🔄 Ana samun tsare-tsare masu samuwa..."
    LIST_INVALID_URL_MSG = "❌ Da fatan za a ba da URL mai inganci wanda ya fara da http:// ko https://"
    LIST_CAPTION_MSG = (
        "📃 Tsare-tsare masu samuwa don:\n<code>{url}</code>\n\n"
        "💡 <b>Yadda ake saita tsari:</b>\n"
        "• <code>/format id 134</code> - Sauke ID na tsari na musamman\n"
        "• <code>/format 720p</code> - Sauke ta inganci\n"
        "• <code>/format best</code> - Sauke mafi kyawun inganci\n"
        "• <code>/format ask</code> - Luôn tambayi inganci\n\n"
        "{audio_note}\n"
        "📋 Yi amfani da ID na tsari daga jerin da ke sama"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Tsare-tsare na sauti kawai:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Sauke tsari 140 azaman sauti MP3\n"
        "• <code>/format id140 audio</code> - iri ɗaya da na sama\n"
        "Waɗannan za a sauke su azaman fayilolin sauti MP3.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Kuskure wajen aika fayil tsare-tsare: {error}"
    LIST_ERROR_GETTING_MSG = "❌ An gaza samun tsare-tsare:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Kuskure ya faru yayin sarrafa umarni"
    LIST_ERROR_CALLBACK_MSG = "Kuskure ya faru"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Yadda ake amfani da ID na tsari:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Bayan samun jerin, yi amfani da ID na tsari na musamman:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - sauke tsari 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - iri ɗaya da na sama\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - sauke tsari 140 azaman sauti MP3\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - iri ɗaya da na sama\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 An gano tsare-tsare na sauti kawai: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Waɗannan tsare-tsare za a sauke su azaman fayilolin sauti MP3.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Tsare-tsare na bidiyo kawai:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Yi amfani da ID na tsari daga jerin da ke sama"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Amfani:</b>\n"
        "<code>/link [inganci] URL</code>\n\n"
        "<b>Misalai:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - mafi kyawun inganci\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p ko ƙasa\n"
        "• /link 720p https://youtube.com/watch?v=... - iri ɗaya da na sama\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K ko ƙasa\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K ko ƙasa"
        "</blockquote>\n\n"
        "<b>Inganci:</b> daga 1 zuwa 10000 (misali, 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Da fatan za a ba da URL mai inganci"
    LINK_PROCESSING_MSG = "🔗 Ana samun hanyar haɗi kai tsaye..."
    LINK_DURATION_MSG = "⏱ <b>Tsawon lokaci:</b> {duration} daƙiƙa\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Stream na bidiyo:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Stream na sauti:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **An sabunta saitin keyboard!**\n\nSaitin sabo: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Hujja mara inganci!**\n\n"
        "Zaɓuɓɓuka masu inganci: `off`, `1x3`, `2x3`, `full`\n\n"
        "Misali: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Saitunan Keyboard**\n\n"
        "Na yanzu: **{current}**\n\n"
        "Zaɓi zaɓi:\n\n"
        "Ko kuma yi amfani da: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 kunna keyboard!"
    KEYBOARD_HIDDEN_MSG = "⌨️ An ɓoye keyboard"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 An kunna keyboard 1x3!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 An kunna keyboard 2x3!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 An kunna keyboard emoji!"
    KEYBOARD_ERROR_APPLYING_MSG = "Kuskure wajen amfani da saitin keyboard {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ An saita tsari zuwa: Luôn Tambayi. Za a tambaye ka inganci a kowane lokacin da ka aika URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ An saita tsari zuwa: Luôn Tambayi. Yanzu za a tambaye ka inganci a kowane lokacin da ka aika URL."
    FORMAT_BEST_UPDATED_MSG = "✅ An sabunta tsari zuwa mafi kyawun inganci (fifiko na AVC+MP4):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ An sabunta tsari zuwa ID {id}:\n{format}\n\n💡 <b>Lura:</b> Idan wannan tsari ne na sauti kawai, za a sauke shi azaman fayil sauti MP3."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ An sabunta tsari zuwa ID {id} (sauti kawai):\n{format}\n\n💡 Wannan zai sauke azaman fayil sauti MP3."
    FORMAT_QUALITY_UPDATED_MSG = "✅ An sabunta tsari zuwa inganci {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ An sabunta tsari zuwa:\n{format}"
    FORMAT_MENU_MSG = (
        "Zaɓi zaɓin tsari ko aika na al'ada ta amfani da:\n"
        "• <code>/format &lt;format_string&gt;</code> - custom format\n"
        "• <code>/format 720</code> - 720p quality\n"
        "• <code>/format 4k</code> - 4K quality\n"
        "• <code>/format 8k</code> - 8K quality\n"
        "• <code>/format id 401</code> - specific format ID\n"
        "• <code>/format ask</code> - always show menu\n"
        "• <code>/format best</code> - bv+ba/best quality"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Don amfani da tsari na al'ada, aika umarni a cikin tsari mai zuwa:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Maye gurbin <code>bestvideo+bestaudio/best</code> da kirtar tsari da kake so."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Zaɓi ƙuduri da codec da kake so:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ An saita tsari zuwa: Luôn Tambayi. Yanzu za a tambaye ka inganci a kowane lokacin da ka aika URL."
    FORMAT_UPDATED_MSG = "✅ An sabunta tsari zuwa:\n{format}"
    FORMAT_SAVED_MSG = "✅ An adana tsari."
    FORMAT_CHOICE_UPDATED_MSG = "✅ An sabunta zaɓin tsari."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "An rufe menu tsari na al'ada"
    FORMAT_CODEC_SET_MSG = "✅ An saita codec zuwa {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ An sabunta zaɓin browser."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ An ƙi dama. Admin kawai."
    ACCESS_DENIED_ADMIN = "❌ An ƙi dama. Admin kawai."
    WELCOME_MASTER = "Barka da zuwa Jagora 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Yi hakuri... Wani kuskure ya faru yayin saukewa."
    SIZE_LIMIT_EXCEEDED = "❌ Girman fayil ya wuce iyakar {max_size_gb} GB. Da fatan za a zaɓi fayil ƙarami a cikin girman da aka yarda."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Ba a sami script ba: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Ana saukewa sabon Firebase dump ta amfani da {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ An sake loda cache na Firebase cikin nasara!"
    ADMIN_CACHE_FAILED_MSG = "❌ An gaza sake loda cache na Firebase. Duba idan {cache_file} yana wanzuwa."
    ADMIN_ERROR_RELOADING_MSG = "❌ Kuskure wajen sake loda cache: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Kuskure wajen gudanar da {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ An aika saƙon talla zuwa duk wasu masu amfani</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Ba za a iya aika saƙon talla ba. Gwada amsa saƙo\nKo wani kuskure ya faru</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ Mai amfani bai sauke wani abun ciki tukuna ba...</b> Ba ya wanzu a cikin logs"
    ADMIN_INVALID_COMMAND_MSG = "❌ Umarni mara inganci"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ Ba a sami bayanai a cikin cache don <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Jeri ya fadi — babu wanda ya bar tashar tukuna."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Jeri na ban</b>\nAna jira jimla: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (hagu: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… da ƙarin masu amfani {extra}."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Yi amfani da /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ An toshe masu amfani daga jerin: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ An kunna toshe ta atomatik: sabbin masu barin za a hana su nan take."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ An kashe toshe ta atomatik."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ An saita taga toshe ta atomatik na tsarawa zuwa kowane {interval}."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Log ayyukan tashar don sa'o'i {hours} na ƙarshe (kwanaki 2)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 Sa'o'i {hours} na ƙarshe (kwanaki 2): {joined} sun shiga, {left} sun bar."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Babu aiki don sa'o'i {hours} na ƙarshe (kwanaki 2)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Jimla: 🟢 {joined} sun shiga, 🔴 {left} sun bar."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Babu dama zuwa log ayyukan tashar. Bots ba za su iya karanta logs na admin ba. Ka ba da CHANNEL_GUARD_SESSION_STRING a cikin config tare da session mai amfani don kunna wannan fasalin."
    BAN_TIME_USAGE_MSG = "❌ Amfani: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Yi amfani da tsare-tsare kamar 10s, 6m, 5h, 4d, 3w, 2M ko 1y."
    BAN_TIME_SET_MSG = "🕒 An saita tazarar binciken log tashar zuwa {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Rahoton binciken tashar\n"
        "An gudanar a: {run_ts}\n"
        "Tazara: {interval}\n"
        "Sabbin masu barin: {new_leavers}\n"
        "Ban ta atomatik: {auto_banned}\n"
        "Ana jira: {pending}\n"
        "ID na taron ƙarshe: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Amfani: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Admin ba zai iya share admin ba"
    ADMIN_USER_BLOCKED_MSG = "An toshe mai amfani 🔒❌\n \nID: <code>{user_id}</code>\nKwanan wata toshe: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> an riga an toshe shi ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Yi hakuri! Kai ba admin ba ne"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Amfani: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "An cire toshe mai amfani 🔓✅\n \nID: <code>{user_id}</code>\nKwanan wata cire toshe: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> an riga an cire toshe shi ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ An cire toshe masu amfani: {count}\n⏱ Alamar lokaci: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Amfani: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "An yi watsi da mai amfani 👁️❌\n \nID: <code>{user_id}</code>\nKwanan wata an yi watsi: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> an riga an yi watsi da shi ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Amfani: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Mai amfani ba a yi watsi da shi ba kuma 👁️✅\n \nID: <code>{user_id}</code>\nKwanan wata an cire watsi: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> ba a yi watsi da shi ba ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Lokacin gudanar da bot -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Da fatan za a ba da URL don share cache.\nAmfani: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Da fatan za a ba da URL mai inganci.\nAmfani: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ An share cache cikin nasara don URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Ba a sami cache don wannan hanyar haɗi ba."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Kuskure wajen share cache: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ An ƙi dama. Admin kawai."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Ana gudanar da script sabunta jerin batsa: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ An kammala script cikin nasara!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ An kammala script cikin nasara!\n\nFitarwa:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Script ya gaza tare da lambar dawowa {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Kuskure wajen gudanar da script: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Ana sake loda caches na batsa da na yanki..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ An sake loda caches na batsa cikin nasara!\n\n"
        "📊 Matsayin cache na yanzu:\n"
        "• Yankuna na batsa: {porn_domains}\n"
        "• Kalmomin batsa: {porn_keywords}\n"
        "• Shafukan da aka goyan baya: {supported_sites}\n"
        "• WHITELIST: {whitelist}\n"
        "• GREYLIST: {greylist}\n"
        "• BLACK_LIST: {black_list}\n"
        "• WHITE_KEYWORDS: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Kuskuren sake loda ma'ajiyar batsa: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Da fatan za a ba da URL don duba.\nYadda ake amfani: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Da fatan za a ba da URL mai inganci.\nYadda ake amfani: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Ana duba URL don abun ciki na NSFW...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Sakamakon Binciken Porn</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Matsayi:</b> <b>{status_text}</b>\n\n"
        "<b>Explanation:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Kuskuren duba URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "An tsabtace cookies."
    CLEAN_LOGS_CLEANED_MSG = "an tsabtace logs."
    CLEAN_TAGS_CLEANED_MSG = "an tsabtace tags."
    CLEAN_FORMAT_CLEANED_MSG = "an tsabtace tsari."
    CLEAN_SPLIT_CLEANED_MSG = "an tsabtace raba."
    CLEAN_MEDIAINFO_CLEANED_MSG = "an tsabtace mediainfo."
    CLEAN_SUBS_CLEANED_MSG = "An tsabtace saitunan rubutun ƙasa."
    CLEAN_KEYBOARD_CLEANED_MSG = "An tsabtace saitunan keyboard."
    CLEAN_ARGS_CLEANED_MSG = "An tsabtace saitunan hujjoji."
    CLEAN_NSFW_CLEANED_MSG = "An tsabtace saitunan NSFW."
    CLEAN_PROXY_CLEANED_MSG = "An tsabtace saitunan proxy."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "An tsabtace saitunan jiran flood."
    CLEAN_ALL_CLEANED_MSG = "An tsabtace duk fayiloli."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nZaɓi aiki:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ An adana fayil cookie"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ An tsallake tabbatarwa don cookies waɗanda ba YouTube ba"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Fayil cookie yana wanzuwa amma yana da tsari mara inganci"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Ba a sami fayil cookie ba."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Ana fara gwajin cookies na YouTube...\n\nDa fatan za a jira yayin da nake duba kuma tabbatar da cookies ɗin ku."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Cookies ɗin ku na YouTube na yanzu suna aiki da kyau!\n\nBa lallai ba ne saukewa sababbi."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Cookies ɗin ku na YouTube na yanzu sun ƙare ko ba su da inganci.\n\n🔄 Ana saukewa sabbin cookies..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ Tushen cookie na {service} ba a saita shi ba!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ Tushen cookie na {service} dole ne ya zama fayil .txt!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Iyakar kewayon ta wuce: an nemi fayiloli {range_count} (matsakaici {max_img_files}).\n\nYi amfani da ɗaya daga cikin waɗannan umarni don saukewa matsakaicin fayiloli masu samuwa:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Rufe"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Iyakar kafofin watsa labarai ta wuce: an nemi fayiloli {count} (matsakaici {max_count}).\n\nYi amfani da ɗaya daga cikin waɗannan umarni don saukewa matsakaicin fayiloli masu samuwa:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 An sami <b>{count}</b> abubuwan kafofin watsa labarai daga hanyar haɗi"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Zaɓi kewayon saukewa:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Kwaikwayon browser"
    ARGS_REFERER_DESC_MSG = "Kan Referer"
    ARGS_USER_AGENT_DESC_MSG = "Kan User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "Ketare haniyyoyin yanki"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Duba takardar shaida SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "Sauke streams na kai tsaye daga farko"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Kada a sauke streams na kai tsaye daga farko"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Yi amfani da kwantena MPEG-TS don bidiyoyin HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "Sauke bidiyo guda ɗaya kawai, ba jerin bidiyo ba"
    ARGS_NO_PART_DESC_MSG = "Kada a yi amfani da fayilolin .part"
    ARGS_NO_CONTINUE_DESC_MSG = "Kada a ci gaba da saukewa na ɓangare"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Tsarin sauti don fitarwa"
    ARGS_EMBED_METADATA_DESC_MSG = "Saka metadata a cikin fayil bidiyo"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Saka thumbnail a cikin fayil bidiyo"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Rubuta thumbnail zuwa fayil"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Yawan gutsuttsura lokaci guda don saukewa"
    ARGS_FORCE_IPV4_DESC_MSG = "Tilasta haɗin IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "Tilasta haɗin IPv6"
    ARGS_XFF_DESC_MSG = "X-Forwarded-Don dabarun kai"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "Girman guntu na HTTP (bytes)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Barci kafin saukar da subtitle (dakika)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Bada damar haɗin gwiwar uwar garken gado"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Manne tabbataccen takaddar HTTPS"
    ARGS_USERNAME_DESC_MSG = "Sunan mai amfani da asusun"
    ARGS_PASSWORD_DESC_MSG = "Kalmar sirrin asusun"
    ARGS_TWOFACTOR_DESC_MSG = "Lambar tabbatar da abubuwa biyu"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Yi watsi da kurakuran saukewa kuma ci gaba"
    ARGS_MIN_FILESIZE_DESC_MSG = "Mafi ƙarancin girman fayil (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Matsakaicin girman fayil (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Abubuwan lissafin waƙa don saukewa (misali, 1,3,5 ko 1-5)"
    ARGS_DATE_DESC_MSG = "Zazzage bidiyon da aka ɗorawa a wannan kwanan wata (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Zazzage bidiyon da aka ɗorawa kafin wannan kwanan wata (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Zazzage bidiyon da aka ɗorawa bayan wannan kwanan wata (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Kawunan HTTP na al'ada (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Tazarar barci tsakanin buƙatun (daƙiƙa)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Matsakaicin tazarar barci (dakika)"
    ARGS_RETRIES_DESC_MSG = "Yawan sake gwadawa"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Tsarin ganga na bidiyo"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Tsarin ganga mai fitarwa don haɗawa"
    ARGS_SEND_AS_FILE_DESC_MSG = "Aika duk kafofin watsa labarai azaman takarda maimakon kafofin watsa labarai"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Kwaikwaya"
    ARGS_REFERER_SHORT_MSG = "Mai Magana"
    ARGS_GEO_BYPASS_SHORT_MSG = "Geo Bypass"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Duba Takaddun shaida"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Fara Live"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Ba Live Start"
    ARGS_USER_AGENT_SHORT_MSG = "Wakilin mai amfani"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Babu Jerin Bidiyo"
    ARGS_NO_PART_SHORT_MSG = "Babu Sashe"
    ARGS_NO_CONTINUE_SHORT_MSG = "A'a Ci gaba"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Tsarin Sauti"
    ARGS_EMBED_METADATA_SHORT_MSG = "Shigar Meta"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Shigar Babban Yatsan hannu"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Rubuta Babban Yatsan hannu"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Daidaitawa"
    ARGS_FORCE_IPV4_SHORT_MSG = "Ƙaddamar da IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Ƙaddamar da IPv6"
    ARGS_XFF_SHORT_MSG = "Hoton XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Girman Chunk"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Subs na barci"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Legacy Connect"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Babu Takaddun Bincike"
    ARGS_USERNAME_SHORT_MSG = "Sunan mai amfani"
    ARGS_PASSWORD_SHORT_MSG = "Kalmar wucewa"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Yi watsi da Kurakurai"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Min Girman"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Girman Girma"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Abubuwan Jerin Bidiyo"
    ARGS_DATE_SHORT_MSG = "Kwanan wata"
    ARGS_DATEBEFORE_SHORT_MSG = "Kwanan wata Kafin"
    ARGS_DATEAFTER_SHORT_MSG = "Kwanan Wata"
    ARGS_HTTP_HEADERS_SHORT_MSG = "Kawunan HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Tazarar Barci"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Max Barci"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Tsarin Bidiyo"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Tsarin Haɗawa"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Aika azaman Fayil"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ Fayil ɗin ya yi girma da yawa. Matsakaicin girman shine 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Fayiloli na wannan tsari ne kawai aka yarda .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ Fayil ɗin baya kama kuki.txt (babu layi '# Netscape HTTP Fayil kuki')."
    COOKIES_ERROR_READING_MSG = "❌ Kuskuren karanta fayil: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Fayil na kuki yana wanzu kuma yana da tsari daidai"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {size} Fayil na kuki yayi girma da yawa! Matsakaicin 100KB, ya samu {service}"
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} an zazzage fayil ɗin kuki kuma an adana shi azaman kuki.txt a cikin babban fayil ɗin ku.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ Tushen kuki na {service} baya samuwa (matsayi {status}). Da fatan za a sake gwadawa daga baya."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Kuskure wajen saukewa fayil cookie na {service}. Da fatan za a sake gwadawa daga baya."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Mai amfani ya ba da sabon fayil ɗin kuki.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ An sabunta kuki cikin nasara:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Ba kuki mai inganci ba.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ Ba a saita tushen kuki na YouTube ba!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ An hana shiga. Admin kawai."
    ADMIN_USER_LOGS_TOTAL_MSG = "Jimlar: <b>{total}</b>\n<b>{user_id}</b> - rajistan ayyuka (Na Ƙarshe 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 keyboard an kunna!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ An saita harshen taken zuwa: {name}__ {flag}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ An saita harshen subtitle zuwa: {name}__ {flag}tare da kunna AUTO/TRANS."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "An rufe menu harshen subtitr."
    SUBS_DOWNLOADING_MSG = "💬 Ana saukewa subtitr..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Sake loda cache na Firebase zuwa ƙwaƙwalwar ajiya..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Babu COOKIE_URL da aka saita. Yi amfani da /kuki ko loda cookies.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Ana saukar da kukis daga URL mai nisa..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Komawa COOKIE_URL dole ne ya nuna fayil .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fayil ɗin kuki na faɗuwa ya yi girma sosai (> 100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Fayil kuki na YouTube wanda aka zazzage ta hanyar faduwa kuma an adana shi azaman kuki.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Tushen kuki na fallback baya samuwa (matsayi {status}). Gwada /cookie ko loda cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Kuskure wajen saukewa cookie fallback. Gwada /cookie ko loda cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Kuskure da ba zato ba tsammani yayin saukewa cookie fallback."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser}__ ba a shigar da mai binciken ba."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Kukis da aka ajiye ta amfani da burauza: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ An kasa ajiye kukis: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ Kukis na YouTube suna aiki daidai"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube cookies are expired or invalid\n\nUse /cookie to get new cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - tsari na al'ada\n• <code>/format 720</code> - ingancin 720p\n• <code>/format 4k</code> - ingancin 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "An aika shawara."
    FORMAT_MKV_TOGGLE_MSG = "MKV yanzu {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Babu URL mai nisa da aka saita"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Tsarin fayil mara inganci"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Fayil ya yi girma sosai"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ An sauke kukis cikin nasara"
    COOKIES_SERVER_ERROR_MSG = "❌ Kuskuren uwar garken {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ saukewa ya kasa"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Kuskuren da ba a zata ba"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Ba a shigar da Browser ba."
    COOKIES_MENU_CLOSED_MSG = "An rufe menu."
    COOKIES_HINT_CLOSED_MSG = "An rufe shawara cookie."
    IMG_HELP_CLOSED_MSG = "An rufe taimako."
    SUBS_LANGUAGE_UPDATED_MSG = "An sabunta saitunan harshen subtitr."
    SUBS_MENU_CLOSED_MSG = "An rufe menu harshen subtitr."
    KEYBOARD_SET_TO_MSG = "An saita keyboard zuwa {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Kuskure wajen sarrafa saiti"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "An kunna MediaInfo."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "An kashe MediaInfo."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "An kashe blur NSFW."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "An kunna blur NSFW."
    SETTINGS_MENU_CLOSED_MSG = "An rufe menu."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Jiran flood yana aiki. Gwada daga baya."
    OTHER_HELP_CLOSED_MSG = "An rufe taimako."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "An rufe saƙon logs."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menu ya rufe."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Girman mara inganci."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Kuskure wajen aika MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Kuskure ya faru: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - duk rajistan ayyukan"
    ADMIN_BOT_DATA_CAPTION_MSG = "{path} - duk {bot_name}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Zazzagewa daga URL mai nisa"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Buɗe Browser"
    SELECT_BROWSER_MSG = "Zaɓi browser don saukewa cookies daga:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Ba a sami masu bincike akan wannan tsarin ba. Kuna iya zazzage kukis daga URL mai nisa ko sanya ido kan matsayin mai bincike:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Buɗe Mai Binciken Bincike</b> - don saka idanu akan matsayin mai bincike a cikin ƙaramin app"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ An kasa gudanar da /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Iyakar ambaliya. Gwada daga baya."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ An kasa buɗe menu na kuki mai lilo"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Ajiye kamar yadda aka rufe alamar kuki."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Yadda ake amfani:</b>\n<code>/link [quality] URL</code>\n\n<b>Misalai:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - mafi kyawun inganci\n• /link 720 https://youtube.com/watch?v=... - 720p ko ƙasa\n• /link 720p https://youtube.com/watch?v=... - iri ɗaya da na sama\n• /link 4k https://youtube.com/watch?v=... - 4K ko ƙasa\n• /link 8k https://youtube.com/watch?v=... - 8K ko ƙasa</blockquote>\n\n<b>Inganci:</b> daga 1 zuwa 10000 (misali, 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K quality"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ An gaza samun hanyoyin rafi"
    LINK_ERROR_GETTING_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Fihirisar kuki mara inganci na YouTube: {total_urls}. Akwai kewayon{selected_index}0__"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Ana saukewa da duba kukis na YouTube...\n\nƘoƙari {attempt} na {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Ana saukewa da duba kukis na YouTube...\n\nƘoƙari {attempt} na {total}\n🔍 Ana gwada kukis..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ An sauke da tabbatar da kukis na YouTube cikin nasara!\n\nAn yi amfani da tushe {source} na {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Duk kukis na YouTube sun ƙare ko ba su samuwa!\n\nTuntuɓi mai kula da bot don maye gurbinsu."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ An wuce iyakar sake gwadawa na kuki na YouTube!\n\n🔢 Matsakaici: {limit} ƙoƙari a kowane awa\n⏰ Da fatan za a sake gwadawa daga baya"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Alama #{wrong} tana ɗauke da haruffa da aka haramta. Haruffa, lambobi da _ kawai ne ake yarda da su.\nDa fatan za a yi amfani da: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Hujja mara inganci!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Saitin harshe mai taken: {name}__ {flag}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Misali: `/ subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Yaren da aka zaɓa: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Yanayin Always Ask {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 An kashe subtitr"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Saitunan subtitr</b>\n\n{status_text}\n\nZaɓi harshen subtitr:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - kashe subtitr\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Saitunan subtitr</b>\n\n{status_text}\n\nZaɓi harshen subtitr:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Take:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Tsawon lokaci:</b> {duration} sec\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Rafin bidiyo:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 720p matsakaicin inganci\n- 1.5 awa matsakaicin tsawon lokaci\n- 500mb matsakaicin girman bidiyo</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️GARGADI: saboda babban tasirin CPU wannan aikin yana da sauri sosai (kusa da lokaci na gaske) kuma an iyakance shi zuwa:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Umarni masu sauri:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - kashe subtitr\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - kunna yanayin Always Ask\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - saita harshe\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - saita harshe tare da kunna AUTO/TRANS\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - kunna yanayin Always Ask\n"
    SUBS_AUTO_SUBS_TEXT = " (auto-subtitr)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Yanayin auto-subtitr {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "An kashe SUBS ta hanyar umarni: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Koyaushe Tambayi yana kunna ta hanyar umarni: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "An saita harshen SUBS ta hanyar umarni: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "Harshen SUBS + an saita yanayin atomatik ta hanyar umarni: {arg}__ auto"
    SUBS_MENU_OPENED_LOG_MSG = "Mai amfani ya buɗe/subs menu."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Mai amfani ya saita yaren magana zuwa: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Mai amfani ya canza yanayin AUTO/TRANS zuwa: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Mai amfani yana juyawa Koyaushe Tambayi yanayin zuwa: {new_always_ask}__"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Mai amfani ya nemi kukis daga mai lilo."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Maɓallin zaɓin mai lilo da aka aika tare da shigar masu bincike kawai."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "An rufe zaɓin mai lilo."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "Komawa COOKIE_URL an yi amfani da shi cikin nasara (an ɓoye tushen)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "Komawa COOKIE_URL ya kasa: matsayi ={status}__ (boye)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Komawa COOKIE_URL kuskuren bazata: {error}__: {error_type}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Browser {browser}__ ba a sanya shi ba."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Ajiye kukis ta amfani da burauza: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "An ajiye fayil ɗin kuki don mai amfani {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "Fayil ɗin kuki yana wanzu, yana da tsari daidai, kuma kukis na YouTube suna aiki."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Fayil ɗin kuki yana wanzu kuma yana da tsari daidai, amma kukis na YouTube ya ƙare."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Fayil ɗin kuki yana wanzu kuma yana da tsari daidai."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Fayil ɗin kuki yana wanzu amma yana da tsarin da ba daidai ba."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Ba a sami fayil ɗin kuki ba."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{user_id} URL kuki babu komai ga mai amfani {service}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} URL kuki ba .txt (boye) bane"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{size} Fayil ɗin kuki yayi girma sosai: {service}bytes (an ɓoye tushen)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{user_id} Fayil ɗin kuki da aka zazzage don mai amfani {service} (an ɓoye tushen)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Ba a samo rubutun ba: {user_id}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "An kasa aika saƙon matsayi na farko"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Kuskure wajen gudanar da {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Sake loda cache na Firebase ta ɗawainiya ta atomatik."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Admin ya sake shigar da cache na Firebase."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Kuskuren sake loda ma'ajiyar Wuta: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "An fara watsa shirye-shirye. Rubutu:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "An aika saƙon watsa shirye-shirye ga duk masu amfani."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "An kasa watsa saƙo: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Admin {user_id} share cache don URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Admin {script_path}__ ya fara rubutun sabunta jerin bat{user_id}_0__"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Rubutun sabunta jerin batsa ya kammala cikin nasara daga admin {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Rubutun sabunta jerin batsa ya gaza daga admin {error}__: {user_id}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Admin {script_path}__ yayi kokarin gudanar da rubutun da babu s{user_id}_0__"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Kuskuren gudanar da rubutun sabunta batsa daga admin {error}: {user_id}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Admin {user_id}__ ya fara sake kunna cache na batsa"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Kuskuren sake loda cache na batsa daga admin {error}__: {user_id}"
    ADMIN_PORN_CHECK_LOG_MSG = "Admin {status}__ an duba URL na NSFW: _{url}_ - Sakamako: __VAR{user_id}"
    
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
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "An rufe menu tsari na al'ada"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "An fitar da hanyar haɗin kai tsaye don mai amfani {user_id} daga {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "An kasa cire hanyar haɗin kai tsaye don mai amfani {user_id} daga {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Kuskure a cikin umarnin hanyar haɗin yanar gizo don mai amfani {error}: {user_id}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Mai amfani {setting}__ saita madannai zuwa {user_id}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Mai amfani {setting}__ saita madannai zuwa {user_id}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "An saita MediaInfo ta hanyar umarni: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Mai amfani ya buɗe /menun info."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: rufe."
    MEDIAINFO_ENABLED_LOG_MSG = "An kunna MediaInfo."
    MEDIAINFO_DISABLED_LOG_MSG = "An kashe MediaInfo."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "An saita girman da aka saita zuwa {size}__ bytes ta hanyar muhawara."
    SPLIT_MENU_OPENED_LOG_MSG = "Mai amfani ya buɗe / raba menu."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "An rufe zaɓin raba."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "An saita girman da aka saita zuwa {size}__ bytes."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Saitin wakili ta hanyar umarni: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Mai amfani ya buɗe/menu na wakili."
    PROXY_MENU_CLOSED_LOG_MSG = "Wakili: rufe."
    PROXY_ENABLED_LOG_MSG = "An kunna wakili"
    PROXY_DISABLED_LOG_MSG = "An kashe wakili"
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "An rufe saƙon taimako."
    AUDIO_HELP_SHOWN_LOG_MSG = "An nuna/taimakon audio"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Mai amfani ya nemi taimakon lissafin waƙa."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "An rufe taimakon lissafin waƙa."
    AUDIO_HINT_CLOSED_LOG_MSG = "An rufe alamar sauti."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Menu na hanyar haɗin kai kai tsaye ƙirƙira ta hanyar maɓallin LINK don mai amfani {user_id} daga {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "An kasa cire hanyar haɗin kai tsaye ta hanyar maɓallin LINK don mai amfani {error} daga {url}: {user_id}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "An aiwatar da umarnin LIST don mai amfani {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Saurin Shiga: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Koyaushe Tambayi Menu da aka aika don {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Ƙirƙiri menu na halaye masu kyau don mai amfani {error}__ bayan kuskure: {user_id}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Tambayi kuskuren menu koyaushe don {error}: {url}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Ana gyara tsari ta hanyar /args settings"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Audio"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Bidiyo"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Bidiyo"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Na gaba ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Baya"
    SUBTITLES_NEXT_BUTTON_MSG = "Na gaba ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Duk filayen rubutu babu kowa"
    SENDER_VIDEO_DURATION_MSG = "Tsawon lokacin bidiyo:"
    SENDER_UPLOADING_FILE_MSG = "📤 Ana loda fayil..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Ana Loda Video..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Tsawon Bidiyo:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "An loda fayil 1."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Bayanin Bidiyo"
    DOWN_UP_NUMBER_MSG = "Lamba"
    DOWN_UP_TITLE_MSG = "Take"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Zazzage bidiyo."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Ana aiwatar da upload..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Rarrabe bangare {part} an loda fayil"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ An gama yin lodi"
    DOWN_UP_FILES_UPLOADED_MSG = "fayilolin uploaded"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Rufe"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼 CODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBS"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 SUBS"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Browser"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "Ƙaddamar da VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Yadda ake samun link din kai tsaye..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Ana samun tsare-tsare masu samuwa..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Ana samun bayanin bidiyo..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Kuskure wajen samun bayani: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Bayanin bidiyo ba ya samuwa"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Kuskure wajen aika bayani: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Bayanin bidiyo da aka aika ga mai amfani {title}__ don {url} ({user_id}"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Fara gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Lokaci:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Mai bincike:</b> Buɗe a cikin burauzar gidan yanar gizo"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Tsare-tsare masu samuwa don"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Yadda ake amfani da ID na tsari:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Bayan samun jerin, yi amfani da ID na tsari na musamman:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - sauke tsari 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - iri ɗaya da na sama"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - sauke tsari 140 azaman sauti MP3"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 An gano tsare-tsare na sauti kawai"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Waɗannan tsare-tsare za a sauke su azaman fayilolin sauti MP3."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Yadda ake saita tsari:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Sauke ID na tsari na musamman"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Sauke ta inganci"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Sauke mafi kyawun inganci"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Koyaushe tambayi inganci"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Tsare-tsare na sauti kawai:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Sauke tsari 140 azaman sauti MP3"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Waɗannan za a sauke su azaman fayilolin sauti MP3."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Yi amfani da ID na tsari daga jerin da ke sama"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Kuskure: Ba a sami saƙon asali ba."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Shafin tsare-tsare"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Kuskure wajen nuna menu na tsare-tsare"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Kuskure wajen samun tsare-tsare"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Kuskure wajen samun tsare-tsare masu samuwa."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Da fatan za a sake gwadawa daga baya."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp ba zai iya sarrafa wannan abun ciki ba"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Tsarin yana ba da shawara yin amfani da gallery-dl maimakon haka."
    ALWAYS_ASK_OPTIONS_MSG = "**Zaɓuɓɓuka:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Don hotunan hotuna: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Don hotuna guda: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl yakan yi aiki mafi kyau don Instagram, Twitter, da sauran abubuwan cikin kafofin watsa labarun."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Gwada Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Tsarin da aka gyara ta hanyar /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Subtitles"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Mai rikodin sauti"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 - Ana samun fassarar labarai"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 - Zaɓi harshe subtitle"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Ba a sami biyan kuɗi ba kuma ba za a saka su ba"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 - Maimaita kai tsaye daga cache"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 - Zaɓi yaren mai jiwuwa"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ - Ana biyan 🔞NSFW (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 - Zaɓi ingancin zazzagewa"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 - Zazzage hoto (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 - Samun hanyar haɗi kai tsaye zuwa bidiyo"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 - Nuna jerin abubuwan da ake samuwa"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 - Canza bidiyo ext/codec"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Embed"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 - Cire sauti kawai"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ - Ana biyan 🔞NSFW (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 - Maimaita kai tsaye daga cache"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 - Zaɓi yaren mai jiwuwa"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Mafi kyau"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Sauran"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝sub kawai"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Ƙungiya mai wayo"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Ƙara layin maɓallin aiki (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Ƙara layuka na maɓallin aiki (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Ƙara maɓallin ƙasa zuwa jere na yanzu"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "An ƙirƙira sabuwar layin ƙasa"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Ba a sami bidiyo a lissafin waƙa ba"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "URL mara tallafi"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Ba a iya samun bidiyo ba"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Babu bidiyon da aka samu"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Ba a sami kafofin watsa labarai ba"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Wannan tweet ba ya ƙunshi"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Kuskure maido da bayanan bidiyo:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Kuskure maido da bayanin bidiyo"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Gwada umarnin <code>/clean</code> sannan a sake gwadawa. Idan kuskuren ya ci gaba, YouTube yana buƙatar izini. Sabunta cookies.txt ta hanyar <code>/cookie</code> ko <code>/cookies_from_browser</code> sannan a sake gwadawa."
    ALWAYS_ASK_MENU_CLOSED_MSG = "An rufe menu."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Zaɓin Inganci na Hannu"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Zaɓi inganci da hannu tunda ganowa ta atomatik ta gaza:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Duk Tsare-tsare Masu Samuwa"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Abubuwan da ake samuwa (daga cache)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Yin amfani da halayen da aka adana - sabbin tsare-tsare bazai samuwa ba"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Zazzage tsarin"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Zazzagewa"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Ana saukewa tare da bin diddigin ci gaba..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Zazzagewa ta amfani da tsari:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Zazzage sauti ta amfani da tsari:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Ana saukar da mafi kyawun inganci ..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Ana saukar da jujjuya bayanai..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Zazzagewa"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Shafi na Formats"
    ALWAYS_ASK_FROM_CACHE_MSG = "(daga cache)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Kuskure: Ba a sami saƙon asali ba. Wataƙila an share shi. Da fatan za a sake aika hanyar haɗin gwiwa."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Kuskure: Ba a samo asalin URL ba. Da fatan za a sake aika hanyar haɗin gwiwa."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>An sami hanyar haɗin kai tsaye</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Title:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Lokaci:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Rashin bidiyo:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Rashin sauti:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ An gaza samun hanyoyin rafi"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Ana fitar da hanyar haɗin kai tsaye ta Tambayi Menu na Koyaushe don mai amfani {user_id} daga {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "An kasa cire hanyar haɗin kai tsaye ta Koyaushe Tambayi menu don mai amfani {error}__ daga {url}: {user_id}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "An fitar da hanyar haɗin kai tsaye ta hanyar ƙasa_da_up_with_format don mai amfani {user_id} daga {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "An kasa cire hanyar haɗin kai tsaye ta hanyar ƙasa_da_up_with_format don mai amfani {error}__ daga {url}: {user_id}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Ana fitar da hanyar haɗin kai tsaye ta down_da_audio don mai amfani {user_id} daga {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "An kasa cire hanyar haɗin kai tsaye ta hanyar ƙasa_da_audio don mai amfani {error}__ daga {url}: {user_id}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Ana aika sauti daga cache."
    AUDIO_PROCESSING_MSG = "🎙️ Audio yana sarrafa..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Ana saukewa sauti:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Kuskure ya faru yayin zazzagewar odiyo."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ An kasa fitar da bayanin mai jiwuwa"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Tsallake nau'in fayil mara tallafi a lissafin waƙa a index {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "Fayil mai jiwuwa ba a samo shi ba bayan zazzagewa."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ An kasa aika saukar audio: Girman fayil yana daidai da 0 B (fihirisa jerin wasan {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ Fayil ɗin audio har yanzu yana saukewa, da fatan za a jira..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Ana loda fayil ɗin sauti...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ An kasa aika sauti: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "An aika sautin jigon waƙa: {user_id}/ {quality}__ fayiloli (mai inganci={total}) ga mai amfani{sent}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ An kasa sauke sauti: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ An soke zazzagewa saboda ƙarewar lokaci (awanni 2)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Ba a samo fayil ɗin bidiyo ba: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ An kasa aika saukar bidiyo: Girman fayil yana daidai da 0 B (fihirisa jerin wasan {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ Fayil ɗin bidiyo har yanzu yana saukewa, da fatan za a jira..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Kuskuren sarrafa bidiyo: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Kuskuren aika fayil bayanin: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 idan kuna son canza taken bidiyo - amsa bidiyo tare da sabon rubutu</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Ba a gano fassarar magana ba"
    VIDEO_PROGRESS_MSG = "<b>Bidiyo: </b> {total}__ / {current}"
    AUDIO_PROGRESS_MSG = "<b>Audio: </b> {total}__ / {current}"
    URL_PROGRESS_MSG = "<b>URL:</b> {total}__ / {current}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL ya wuce: {limit}/{count}"
    MULTI_URL_COMPLETED_MSG = "An gama aiwatarwa"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Ba a ba da izinin jeri na waƙa a yanayin URL da yawa. Aika URL guda ɗaya kawai ba tare da jeri ba (*1*5, /vid 1-10, da sauransu)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Duba <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>nan</a> idan rukunin yanar gizon ku yana goyan bayan"
    ERROR_COOKIE_NEEDED_MSG = "Kuna iya buƙatar <code>kuki</code> don zazzage wannan bidiyon. Da farko, tsaftace filin aikinku ta hanyar <b>/mai tsabta</b> umarni"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Don Youtube - sami <code>kuki</code> ta hanyar <b>/kuki</b> umarni. Don kowane rukunin yanar gizon da ake goyan baya - aika kuki ɗin ku (<a href='https://t.me/tg_ytdlp/203'>guide1</a>) (<a href='https://t.me/tg_ytdlp/214'>guide2</a>) sannan bayan haka sake aika hanyar haɗin bidiyo."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Zaɓi harshe subtitle"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Babu madadin harsunan mai jiwuwa"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Zaɓi harshe mai jiwuwa"
    PAGE_NUMBER_MSG = "Shafi {page}"
    TOTAL_PROGRESS_MSG = "Jimlar Ci gaba"
    SUBTITLE_MENU_CLOSED_MSG = "Menu na subtitle ya rufe."
    SUBTITLE_LANGUAGE_SET_MSG = "Saitin harshe mai taken: {value}"
    AUDIO_SET_MSG = "Saitin sauti: {value}"
    FILTERS_UPDATED_MSG = "An sabunta masu tacewa"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙 Komawa"
    CLOSE_BUTTON_TEXT = "🔚Rufe"
    LIST_BUTTON_TEXT = "📃Lissafi"
    IMAGE_BUTTON_TEXT = "🖼 Hoto"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Ba a gano inganci ta atomatik ba\nYi amfani da maɓallin 'Sauran' don ganin duk tsare-tsare da ake samu.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **An Gano Rafi Kai Tsaye**\n\nBa a yarda da zazzage rafukan kai tsaye masu gudana ko marasa iyaka.\n\nDa fatan za a jira rafin ya ƙare kuma ku sake gwadawa lokacin:\n• An san tsawon rafi\n• Rafin ya ƙare\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Zazzagewar Rafi kai tsaye</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Ciki {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Matsakaicin girman: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Jimlar tsawon lokaci: {duration}__ dakika"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Rafi Kai Tsaye - Bangare {chunk}</b>\n⏱ Tsawon lokaci: {duration} sec\n📦 Girma: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Ciki {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Kammala Zazzagewar Rafi Kai tsaye</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "An zazzage {chunks}__ guntun (s)"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Jimlar tsawon lokaci: {duration}__ dakika"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>An Dakatar Da Zazzagewar Rafi Kai Tsaye</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "An share littafin adireshin mai amfani (wataƙila ta / tsaftataccen umarni)"
    LIVE_STREAM_FILE_DELETED_MSG = "An share fayil ɗin chunk (wataƙila ta / tsaftataccen umarni)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Ruwa ya ƙare"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Da fatan za a zaɓi wani tsari daban ta amfani da umarnin `/format`."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>An sami hanyar haɗi kai tsaye</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Title:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Kuskuren Sarrafa Fayil**\n\nAn sauke bidiyon amma ba za a iya sarrafa shi ba saboda haruffa marasa inganci a cikin sunan fayil.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Kuskuren Sarrafa Fayil**\n\nAn sauke bidiyon amma ba za a iya sarrafa shi ba saboda kuskuren hujja mara inganci.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Dalili:**\n"
        "• Fayil ɗin da aka saukar ba fayil bidiyo ba ne\n"
        "• Yana iya zama takarda (PDF, DOC, da sauransu) ko kuma archive\n\n"
        "**Magani:**\n"
        "• Bincika hanyar haɗi - yana iya kaiwa ga takarda, ba bidiyo ba\n"
        "• Gwada hanyar haɗi ko tushe daban\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Dalili:**\n"
        "• Ba za a iya sarrafa fayil ɗin a matsayin bidiyo ba\n"
        "• Yana iya zama ba fayil bidiyo ba ne ko kuma fayil ɗin ya lalace\n\n"
        "**Magani:**\n"
        "• Bincika hanyar haɗi - yana iya kaiwa ga takarda, ba bidiyo ba\n"
        "• Gwada hanyar haɗi ko tushe daban\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Tsari Ba Ya Samuwa**\n\nTsarin bidiyon da aka nema baya samuwa don wannan bidiyon.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Ba a sami ID na Tsari {format_id} don wannan bidiyon.\n\nID na Tsari da Ake Samu: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **Tsarin AV1 baya samuwa don wannan bidiyon.**\n\n**Tsare-tsare da Ake Samu:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Kuskuren Sarrafa Fayil**\n\nAn sauke sautin amma ba za a iya sarrafa shi ba saboda haruffa marasa inganci a cikin sunan fayil.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Kuskuren Sarrafa Fayil**\n\nAn sauke sautin amma ba za a iya sarrafa shi ba saboda kuskuren hujja mara inganci.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Mai amfani ya shigar da abun ciki haramun. Ba za a iya saukewa ba."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "NSFW blur saita ta hanyar umarni: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Mai amfani ya buɗe /nsfw menu."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: rufe."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "An kasa sauke {status}__ kuki: matsayi=_{service}(an ɓoye url)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Kuskuren zazzage {error}__ kuki: {service} (an ɓoye url)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Kuskuren da ba a zata ba yayin zazzage {error}__ kuki (ɓoye url): {error_type}:{service}_"
    COOKIES_FILE_UPDATED_LOG_MSG = "An sabunta fayil ɗin kuki don mai amfani {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Abun cikin kuki mara inganci wanda mai amfani {user_id} ya bayar."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "Kuki URLs na YouTube fanko ne ga mai amfani {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "An sauke cookies ɗin YouTube kuma an inganta su don mai amfani {source}__ daga tushen _{user_id}"
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Duk tushen kuki na YouTube sun kasa ga mai amfani {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Kuskuren check_batsa daga admin {error}__: {admin_id}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Saitin girman ɓangaren saiti zuwa {size}__ bytes."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "An gama loda bidiyo tare da tsagawar fayil."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Bidiyon lissafin waƙa da aka aika: {user_id}/ {quality}__ fayiloli (mai inganci={total}) ga mai amfani {sent}"
    UNKNOWN_ERROR_MSG = "❌ Kuskuren da ba a sani ba: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Tsallake nau'in fayil mara tallafi a lissafin waƙa a index {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg not found. Please install FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Juya zuwa MP4 ya kasa: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Saka subtitr na iya ɗaukar lokaci mai tsawo (har zuwa minti 1 a kowane minti 1 na bidiyo)!\n🔥 Ana fara ƙone subtitr..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Ba za a iya shigar da rubutun kalmomi ba saboda iyaka (inganci / tsawon lokaci / girman)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Babu rubutun ra'ayi don harshen da aka zaɓa"
    ERROR_SENDING_VIDEO_MSG = "❌ Kuskuren aika bidiyo: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Bidiyon lissafin waƙa da aka aika: {total}__/{sent} fayiloli."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ An soke zazzagewa saboda ƙarewar lokaci (awanni 2)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ An kasa zazzage bidiyo: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Kuskure: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON dole ne ya zama abu (kamus)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Tsarin JSON mara inganci. Da fatan za a ba da ingantaccen JSON."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Dole ne kimar ta kasance tsakanin {max_val} da {min_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {value}__ saita zuwa: <code>{description} </code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Gaskiya"
    ARGS_FALSE_BUTTON_MSG = "❌ Karya"
    ARGS_BACK_BUTTON_MSG = "🔙 dawo"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Rufe"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Gaskiya"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Karya"
    ARGS_NOT_SET_MSG = "Ba a saita ba"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ Tsarin AV1 baya samuwa don wannan bidiyon.\n\nTsare-tsare da Ake Samu:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Kuskuren saukewa: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ Ba a sami bidiyo a lissafin waƙa a index {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Juyar da Bidiyo Ya Gaza**\n\nBa za a iya juyar da bidiyon zuwa MP4 ba saboda kuskuren hujja mara inganci.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Juyar da Bidiyo Ya Gaza**\n\nBa za a iya juyar da bidiyon zuwa MP4 ba.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ An kasa samun hanyoyin shiga rafi"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ Babu abun ciki da aka samu a index {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Kuskure: Ba a sami saƙon asali ba."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Kuskure: URL bai samu ba."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Ba za a iya saka wannan URL ɗin ba."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec}__ codec babu don wannan bidiyon"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format}__ babu shi don wannan bidiyon"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood limit. Try later."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Duba Kuki"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ DUK (AUT)"
    PROXY_OFF_BUTTON_MSG = "❌ KASHE"
    PROXY_CLOSE_BUTTON_MSG = "🔚Rufe"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Zaɓi Ƙasa:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Share Zaɓin Ƙasa"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Ƙasar da aka zaɓa: {ƙasar} (lambar: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Akwai proxies: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Bot zai fara gwada HTTP, sannan SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Ana kunna wakili ta atomatik don zaɓin ƙasa"
    PROXY_COUNTRY_CLEARED_MSG = "✅ An share zaɓin ƙasa"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ An share zaɓin ƙasa"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Kasar da aka zaba: {kasa}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Amfani da ƙasa daga fayil: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Akwai ƙasashe daga fayil: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 Ƙasar da aka zaɓa: {ƙasa} (lambar: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ An ba da izinin wakili ga wannan ƙasa"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ An kashe wakili (latsa ALL (AUTO) don kunnawa)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ ON"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ KASHE"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Rufe"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ ON (Babu blur)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ KUNNA (Babu Blur)"
    NSFW_OFF_BLUR_MSG = "✅ KASHE (Blur)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ KASHE (Blur)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Tsaftace"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Kuskuren sarrafa saƙon amsa ga mai amfani {error}__: {user}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Kuskuren aika watsa shirye-shirye ga mai amfani {error}: {user}"
    ADMIN_LOGS_FORMAT_MSG = "Rajistan ayyuka na {bot_name}\nMai amfani: {user_id}\nJimlar rajistan ayyuka: {total}\nLokaci na yanzu: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nJimlar {path}: {count}\nLokaci na yanzu: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Jimlar Masu Amfani: {count}</i>\nNa Ƙarshe 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Ma'ajiyar batsa ta admin {admin_id}. Yankunan: {domains}, Kalmomin: {keywords}, Shafukan: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Kuskuren aika saƙon ƙarewar lokaci: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Zaɓi harshe</b>"
    LANG_CHANGED_MSG = "✅ An canza harshe zuwa {lang_name}"
    LANG_ERROR_MSG = "❌ Kuskure wajen canza harshe"
    LANG_CLOSED_MSG = "An rufe zaɓin harshe"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] dawo da kira: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Ƙara maɓallin sa ido na burauza tare da URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "Ba a saita URL na mai bincike ba: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Keyboard setting updated!**\n\nNew setting: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "An kasa ɓoye maɓallan madannai: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Yin amfani da kukis na YouTube masu aiki don haɓaka hanyar haɗi don mai amfani {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Babu kukis na YouTube masu aiki don haɓaka hanyar haɗin yanar gizo don mai amfani {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Amfani da kukis na YouTube don haɓaka hanyar haɗin yanar gizo don mai amfani {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Babu kukis na YouTube da aka samo don cire haɗin haɗin mai amfani {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "An kwafi fayil ɗin kuki na duniya zuwa ga mai amfani {user_id}__ babban fayil don cire haɗin haɗin"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Mai amfani {user_id}__ ya nemi umarnin mediyainfo"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Mai amfani {is_admin}__ shine admin:{user_id}_"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Mai amfani {is_in_channel}__ yana cikin ta{user_id}AR_0____"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] An hana mai amfani {user_id}__ damar - ba admin ba kuma ba cikin tashar ba"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] An ba da damar mai amfani {user_id}"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] sake kiran waya: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Wannan umarnin yana samuwa ne kawai ga masu gudanarwa."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ An gama zazzagewa tare da tallafin alamar PO"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Iyakar ambaliya. Gwada daga baya."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST kuskuren wartsakewa: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Kuskuren rufe zaman Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Kuskuren fara tsarin db tushe: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Ba a saita duk sigogi a cikin config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.Ba a saita tushen bayanaiURL ba"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey ba a saita don samun idToken ba"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Kuskuren zazzage juji na Firebase: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Ba a yi nasarar sauke juji na Firebase ta hanyar REST ba"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Kuskure a cikin _zazzagewa_da_sakewa_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Kuskure yana tafiyar da cache ta atomatik (kokarin {error}__/{max_retries}){attempt}__"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Duk ƙoƙarin sake gwadawa ya ci tura"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Fara saukar da juji na Firebase a {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Babu Dogara: buƙatu ko Zama"
    DB_DATABASE_EMPTY_MSG = "⚠️ Database ba komai"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Kuskuren rufe logger: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Kuskure yayin tsaftacewa: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Kuskuren clone: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Lokacin ƙarewar Clone"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Banda Clone: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Mai amfani ya soke sabuntawa"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ An rufe ma'ajiyar cikin nasara"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Ajiyayyen an koma _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Ana loda dukkan kayayyaki"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Ana gama tsaftacewa yayin fita"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 An karɓi sigina {signal}, ana rufewa cikin kyakkyawan yanayi..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Don Allah jira..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Zazzage rafin HLS:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "jiran gutsuttsura"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Ba a sami Ajiyayyen {ts} a cikin _maajiyar/"
    RESTORE_FAILED_RESTORE_MSG = "❌ An kasa dawo da {e}__ -> {dest_path}VA{src}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ An dawo dashi: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Cikakkun Bayanai:</b> {error_details}\n\nAn dakatar da saukewa saboda kuskure mai mahimmanci.\n\n💡 <b>Shawara:</b> Idan kuna samun kuskuren 401 Ba a ba da izini ba, gwada amfani da umarnin <code>/cookie instagram</code> ko aika kukis ɗinku don tabbatar da asusun tare da Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domain in the blacklist: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ An samo kalmomin batsa: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domain in whitelist: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ An samo mahimmin kalmomi masu farar fata: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Ba a sami kalmomin batsa ba"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Kuskuren TikTok API a index {index},, tsallakewa zuwa sauti na gaba..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Kuskuren API na TikTok a index {index},, tsallake zuwa bidiyo na gaba..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "Mai amfani ya shigar da <b>url</b>\n <b>sunan mai amfani:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>Mai amfani ya shigar kamar haka:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Shiga Channel"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Mai Rijista: {func_name}__ {handler_type}____"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥/kuki - Zazzage kukis na 5"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Samu kuki na YT-browser"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Tabbatar da fayil ɗin kuki ɗin ku"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Loda kuki na al'ada"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Rufe"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Akwai tsari don: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Rufe"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Rufe"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Rufe"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Rufe"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Taimako ya rufe."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "An rufe"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Kuskure ya faru"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "Ba a sami ffmpeg a cikin PATH ko kundin tsarin aiki. Da fatan za a shigar da FFmpeg."
    YTDLP_NOT_FOUND_MSG = "yt-dlp binary ba a samo shi a cikin PATH ko kundin tsarin aiki ba. Da fatan za a shigar da yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Za a raba bidiyon zuwa sassa {rounds}, wanda zai iya zama mai yawa"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Ana raba bangaren bidiyo {current}/{total}: {start_time:.2f}s zuwa {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "An kasa ƙirƙirar bangaren raba {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "An ƙirƙiri bangaren raba {part} cikin nasara: {target_name} ({size} bytes)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Kuskure wajen raba bangaren bidiyo {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "An raba bidiyon zuwa sassa {count} cikin nasara"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Kuskure a cikin tsarin raba bidiyo: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Kuskure yayin sarrafa bidiyo {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Fayil ɗin bidiyo baya wanzu: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Kuskure wajen fassara girma '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Ba za a iya tantance girmar bidiyo daga '{size_result}' ba, ana amfani da na asali: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Kuskure wajen ƙirƙirar ƙaramin hoto: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Kuskure wajen fassara tsawon bidiyo: {error}, sakamakon ya kasance: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Ba a ƙirƙiri ƙaramin hoto a {thumb_dir}, ana amfani da na asali"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Kuskuren aiwatar da umarni: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Kuskure wajen ƙirƙirar ƙaramin hoto tare da FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Tsallake sashin daidaitawa mara-dict: {opts}={section}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Saita {value}__.{key} = {section}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Amfani da kukis mai amfani: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Amfani da kukis na YouTube don mai amfani {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "An kwafi fayil ɗin kuki na duniya zuwa babban fayil ɗin mai amfani {user_id}"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Amfani da kwafin kukis na duniya azaman kukis masu amfani: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "An kasa yin kwafin fayil ɗin kuki na duniya don mai amfani {error}__: {user_id}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Amfani --no-kukis don yanki: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "An nemi wakili amma ya kasa shigo da/samun daidaitawa: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Tilasta amfani da wakili don gallery-dl: {proxy_url}__"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "An nemi wakili amma saitin wakili bai cika ba"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Mataimakin wakili ya kasa: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Ana nazarin abubuwan cirewa..."
    GALLERY_DL_ITEM_COUNT_MSG = "Abu {item}: {count}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "An samo metadata (tag 2): {info}__"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "An samo URL (tag 3): {metadata}, metadata:{url}_"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "An samo metadata (gado): {info}__"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "An samo URL (gado): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Sunan fayil da aka samo: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "An samo littafin adireshi: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "An sami tsawo: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "An rarraba {fallback}__ abubuwa, bayani:{info}___, koma baya: {count}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Saita tsarin gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Dabarun Gwajin A: extractor.find + abubuwa()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor module ba a samu"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() babu a cikin wannan ginin"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Mai cire kira.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Babu mai cirewa da ya dace da URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Saita kukis akan mai cirewa: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "An kasa saita kukis akan mai cirewa: {error}__"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "An samo mai cirewa, kira abubuwa()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Dabarun A ya yi nasara, ya sami bayani: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Dabarun A: extractor.items() ya dawo babu ingantaccen bayani"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Dabarar A (extractor.find) ta kasa: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Bayanan da aka dawo daga --get-urls: jimlar={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Duk dabarun sun kasa samun metadata"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "An kasa fitar da bayanin hoto: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job module ba a samu (karshe shigar?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadAiki ba ya samuwa a cikin wannan ginin"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Neman fayilolin da aka sauke a cikin littafin gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Ƙoƙarin nemo fayiloli ta sunaye daga mai cirewa"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Kuskuren karanta args mai amfani ga {error}: {user_id}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Kuskure yayin sarrafa bidiyo {error}__: {video_path}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Mai amfani {user_id}__ ya kunna send_as_file, yana aikawa azaman takarda"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video ya ƙare akai-akai; komawa zuwa send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Taken ya yi tsayi sosai, yana ƙoƙari tare da ƙaramin taken"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (ƙaramin taken) ya ƙare; koma baya zuwa send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Kuskuren aika bidiyo tare da ƙaramin taken: {error}__"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Kuskuren aika cikakken bayanin fayil: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Kuskuren cire fayil ɗin bayanin ɗan lokaci: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Tsallake match_filter don yanki a cikin NO_FILTER_DOMAINS: {url}__"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Duba kukis na YouTube na yanzu akan URL na mai amfani don gano tsarin ga mai amfani {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Kukis na YouTube da suka wanzu suna aiki akan URL na mai amfani don gano tsari ga mai amfani {user_id} - ta amfani da su"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Kukis ɗin YouTube ɗin da suka wanzu sun gaza akan URL na mai amfani, suna ƙoƙarin samun sababbi don gano tsari ga mai amfani {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Ana gwada tushen kuki na YouTube {user_id}__ don gano tsari don mai amfani {i}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "Kukis na YouTube daga tushen {user_id}__ suna aiki akan URL na mai amfani don gano tsari ga mai amfani {i}_ - an adana shi zuwa babban fayil ɗin mai amfani"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "Kukis na YouTube daga tushen {user_id}__ basa aiki akan URL na mai amfani don gano tsarin ga mai amfani {i}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "An kasa sauke kukis na YouTube daga tushen {user_id}__ don gano tsarin ga mai amfani {i}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Duk tushen kuki na YouTube sun gaza don gano tsarin mai amfani {user_id}, ba tare da kukis ba"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Babu tushen kuki na YouTube da aka saita don gano tsari don mai amfani {user_id}, da zai gwada ba tare da kukis"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Babu kukis na YouTube da aka samo don gano tsarin mai amfani {user_id}, yana ƙoƙarin samun sababbi"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Amfani da kukis na YouTube don gano tsari ga mai amfani {user_id} (an riga an inganta shi a cikin Menu na Tambayi Koyaushe)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Babu kukis na YouTube da aka samo don gano tsarin mai amfani {user_id}, yana ƙoƙarin maidowa..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "An kwafi fayil ɗin kuki na duniya zuwa ga mai amfani {user_id}__ babban fayil don gano tsari"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "An kasa yin kwafin fayil ɗin kuki na duniya don mai amfani {error}__: {user_id}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Amfani da --no-kukis don yanki a cikin tsarin get_video_formats: {url}__"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "App har yanzu ba a fara aiki ba. Ba za a iya shiga {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Caption:</b> <code>{caption}</code>\n<b>User id:</b> <code>{user_id}</code>\n<b>User first name:</b> <code>{users_name}</code>\n<b>Video file id:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Kuskure a cikin taken_edita: {error}__"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Kuskuren da ba a zata ba a cikin taken_edita: {error}__"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL na Bidiyo</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL ba ya cikin tsari"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin ya fara"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken an sabunta shi"
    DB_LOG_FOR_USER_ADDED_MSG = "Shiga don ƙara mai amfani"
    DB_DATABASE_CREATED_MSG = "db ya yi"
    DB_BOT_STARTED_MSG = "Bot ya fara"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_KOWA ya dage don daidaitawa.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "An riga an adana ɓangaren lissafin waƙa: {path_parts}, tsallakewa"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: babu cache da aka samo don kowane URL / bambance-bambancen inganci, maido da komai."
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: ƙidaya mai sauri don babban kewayo: {cached_count}__ bidiyo da aka adana"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: ba a sami cache don hash {quality_key}__, inga{url_hash}_0__"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: babu cache da aka samo don kowane bambance-bambancen URL, dawo da Babu"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ An hana shiga. Admin kawai."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Auto Firebase cache reloading updated!\n\n📊 Status: {status}\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Hujja mara inganci. Yi amfani da /auto_cache akan | kashe | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Dole ne tazarar ta kasance tsakanin sa'o'i 1 zuwa 168"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ An kasa saita tazara"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Auto Firebase cache interval updated!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Auto Firebase cache reloading started!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "ANA SANYA sake lodi ta atomatik; na gaba a {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Mai gudanarwa ya RUSHE."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "An saita tazarar sake lodi ta atomatik zuwa {next_exec}h; na gaba {interval}__"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "An fara saukewa ta atomatik; na gaba a {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Admin ya dakatar da sake kunnawa ta atomatik."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ An loda cache na Firebase: {count}__ tushen nodes"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Ba a samo fayil ɗin cache na Firebase ba, yana farawa da ma'ajin mara komai: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ An kasa loda cache na wuta: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Sake loda cache na Firebase: {count}__ tushen nodes"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Ba a samo fayil ɗin cache na Firebase: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Ba a yi nasarar sake shigar da cache na wuta ba: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 An hana ku daga bot! Don cire haram, tuntuɓi {Config.ADMIN_USERNAME}\n<blockquote>P.S. Kada ka bar tashar - za a hana ka kai tsaye ⛔️</blockquote>\n🌍Canza harshe /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Ba a sami tsarin bidiyo ba. Ana ƙoƙarin mai saukar da hoto…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram ya iyakance aika saƙonni.\n⏳ Da fatan za a jira: {time_str}\nDon sabunta lokaci aika URL kuma sau 2."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Danna maɓalli don kwafi URL na rafi, sannan liƙa shi a cikin app na VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Danna maɓalli don kwafi URL na rafi, sannan liƙa shi a cikin app na VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Kuskure wajen samun hanyar haɗi:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Kuskuren aika fayil ɗin tsari: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ An kasa samun tsare-tsare:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Ana nazari... (jiran dakika 6)"
    AA_PROCESSING_MSG = "🔎 Ana nazarin..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Alama #{wrong} tana ɗauke da haruffa da aka haramta. Haruffa, lambobi da _ kawai ne ake yarda da su.\nDa fatan za a yi amfani da: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Для работы в группе боту нужны права администратора. Пожалуйsta, sdelayte bota adminom эtoy ruppy."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Sannu {first_name},\n \n<i>Wannan bot🤖 na iya zazzage kowane bidiyo zuwa telegram kai tsaye.😊 Don ƙarin bayani danna <b>/help</b></i> 👈\n\n<blockquote>P.S. Zazzagewar abun ciki na 🔞NSFW da fayiloli daga ☁️Cloud Storage ana biya! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Kada ku bar tashar - za a hana ku amfani da bot ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Babu fayilolin da za a cire."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 All files removed successfully!\n\nRemoved files:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ KA JIRA HAR SAUKAR DA SAUKAR DA AKA BAYA"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "Misalin aikace-aikacen babu wanda yake cikin check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict ba komai bane, yana bada izinin saukewa"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict ba komai ba ne, yana ba da izinin saka juzu'i"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_sub_liits: iyakoki - max_quality={max_size}p, max_duration{max_duration}___s, max{max_quality}AR_0__MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_liits: info_dict keys: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Ƙaddamar da rubutun da aka tsallake: tsawon lokaci {max_duration}__ ya wuce i{duration}R_0__s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Ƙirƙirar rubutun da aka tsallake: girman {size_mb:.2f}MB ya wuce iyaka {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Ƙaddamar da rubutun da aka tsallake: ingancin {max_quality}{min_side}_2____ (gefen{height}R_1__p) ya wuce iy{width}_0__p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "lissafin waƙa"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ An wuce iyakar kewayon don {service}: {count} (matsakaici {max_count}).\n\nYi amfani da ɗaya daga cikin waɗannan umarnin don zazzage fayiloli masu yawa da ake samu:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ An wuce iyakar kewayon don {service}: {count} (matsakaici {max_count})\nID na Mai Amfani: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "An kashe mai ba da alamar PO a cikin saitin"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url}__ ba yanki ba ne na YouTube, yana tsallake alamar PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "Babu mai ba da alamar PO a {base_url}__, yana komawa zuwa daidaitaccen hakar YouTube"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "An share cache mai bada alamar PO, zai duba samuwa akan buƙatu na gaba"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Misalin app bai samuwa tukuna"
    HELPER_USER_NAME_MSG = "Mai amfani"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "An gano jiran ambaliyar ruwa, barci na tsawon {wait_seconds}__"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "An gano jirar ambaliya amma ba a iya cire lokaci ba, barci na tsawon {retry_delay}__"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno an gano kuskure, barci na {retry_delay}__"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Tsarin wakili bai cika ba, ta amfani da haɗin kai tsaye"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Rufe"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Rufe"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Rufe"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 An cire fayil ɗin rajista."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 An cire fayil ɗin tags."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 An cire fayil ɗin tsari."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 An cire fayil ɗin Raba."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 An cire fayil ɗin Mediainfo."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 An cire saitin rubutu."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 An cire saitunan allo."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 An cire saitunan Args."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 An cire saitunan NSFW."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 An cire saitunan wakili."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 An cire saitunan jiran ambaliya."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Rufe"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Umurnin Download Video"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Amfani: <code>/ URL URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Misalai:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (direct order)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (reverse order)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Hakanan duba: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Mai amfani {user_id}__ add_bot_to_group umarni"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "An kasa fitar da ID na YouTube"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "An kasa sauke thumbnail ko ya yi girma da yawa"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Zaɓi harshe mai jiwuwa"
    AA_NO_SUBTITLES_DETECTED_MSG = "Ba a gano fassarar magana ba"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Zaɓi harshe subtitle"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Kuskuren Tabbatarwa"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Ba a Samu Asusu ba"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Account Unavailable"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Ƙimar Ƙimar Ya Wuce"
    GALLERY_DL_NETWORK_ERROR_MSG = "Kuskuren hanyar sadarwa"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Content Unavailable"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Ƙuntataccen yanki"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Ana Bukatar Tabbatarwa"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Cin zarafin Siyasa"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Kuskuren da ba a sani ba"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ An fara saukewa</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Rufe"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Umarnin Zazzage Bidiyo</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Amfani: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Misalai:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Hakanan duba: /audio, /img, /help, /jerin waƙa, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Flood limit. Try later."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Cookie Command Usage</b>

<code>/cookie</code> - Show cookie menu
<code>/cookie youtube</code> - Download YouTube cookies
<code>/cookie instagram</code> - Download Instagram cookies
<code>/cookie tiktok</code> - Download TikTok cookies
<code>/cookie x</code> or <code>/cookie twitter</code> - Download Twitter/X cookies
<code>/cookie facebook</code> - Download Facebook cookies
<code>/cookie custom</code> - Show custom cookie instructions

<i>Available services depend on bot configuration.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 An cire fayil ɗin kuki kuma an share cache."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Prev"
    SUBS_BACK_BUTTON_MSG = "🔙 Komawa"
    SUBS_OFF_BUTTON_MSG = "🚫 KASHE"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - saita harshe"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - saita harshe tare da AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Zaɓuɓɓuka masu inganci:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 HARSHE"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 TSAFTA"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 KUKI"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MEDIA"
    SETTINGS_INFO_BUTTON_MSG = "📖 BAYANI"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ KARA"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Kukis kawai"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Logs"
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Tags"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Format"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Raba"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Subtitles"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Keyboard"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Args"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Wakili"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Jiran ambaliya"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑 Duk fayiloli"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥/kuki - Zazzage kukis na 5"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Samu kuki na YT-browser"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Tabbatar da fayil ɗin kuki ɗin ku"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Loda kuki na al'ada"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 / tsari - Canja inganci & tsari"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Kunna / KASHE MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ / tsaga - Canja girman ɓangaren bidiyo"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 / audio - Zazzage bidiyo azaman sauti"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 / subs - Saitunan harshe subtitles"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ / lissafin waƙa - Yadda ake saukar da lissafin waƙa"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 / img - Zazzage hotuna ta hanyar gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Aika #tags ɗin ku"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /taimako - Samun umarni"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃/usage -Aika rajistan ayyukan ku"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /jerin waƙa - Taimakon lissafin waƙa"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 / add_bot_zuwa_group - yadda ake"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Samu hanyoyin haɗin bidiyo kai tsaye"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /wakili - Kunna / kashe wakili"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /Allon madannai - Tsarin allon madannai"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍/bincike - Mai taimakawa neman layi"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp muhawara"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 / nsfw - NSFW blur saituna"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Zaɓuɓɓukan Tsaftacewa</b>\n\nZaɓi abin da za a tsaftace:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Wayar hannu: Kunna @vid search"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Wayar hannu: Kunna @vid search"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 KASHE"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 CIKE"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1 x3"
    KEYBOARD_2X3_BUTTON_MSG = "2x3 ku"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[Hotuna URL]({url})"
    IMAGE_ERROR_MSG = "❌ Kuskure: {error}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Back"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - tsari na al'ada"
    FORMAT_720P_MSG = "• <code>/format 720</code> - ingancin 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - ingancin 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - ingancin 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - ID na tsari na musamman"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - koyaushe nuna menu"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/mafi kyawun inganci"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Koyaushe Tambaya (menu + maɓallai)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Sauran (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (mafi kyau don PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (mafi kyau don wayar hannu Telegram)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (MAX quality)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Custom (enter your own)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Daga Browser"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Naku"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Yanayin shigarwa ta atomatik yana rufe saboda rashin aiki (minti 5)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Sake saita Duk"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Duba Yanzu"
    ARGS_BACK_BUTTON_MSG = "🔙 dawo"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Tura wannan saƙon zuwa waɗanda kuka fi so don adana waɗannan saitunan azaman samfuri.</i> \n\n<i>Tura wannan saƙon baya nan don amfani da waɗannan saitunan.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Hujjojin yt-dlp na Yanzu:\n\nBa a saita saitunan al'ada ba.\n\n---\n\n<i>Tura wannan saƙon zuwa waɗanda kuka fi so don adana waɗannan saitunan azaman samfuri.</i> \n\n<i>Tura wannan saƙon baya nan don amfani da waɗannan saitunan.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Hujjojin yt-dlp na Yanzu:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Saitunan fitarwa"
    ARGS_SETTINGS_READY_MSG = "Saituna suna shirye don fitarwa! Tura wannan saƙon zuwa abubuwan da kuka fi so don adanawa."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Hujjojin yt-dlp na Yanzu:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ An gaza gane saituna a cikin saƙo. Ka tabbata ka aika samfurin saituna daidai."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ An shigo da saituna cikin nasara!\n\nMa'auni da aka yi amfani: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Saitunan mahimmanci:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Kuskure wajen adana saitunan da aka shigo."
    ARGS_ERROR_IMPORTING_MSG = "❌ Kuskure ya faru yayin shigo da saituna."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Sauke Fayilolin Cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Zaɓi sabis don saukewa fayil cookie."
    COOKIE_MENU_SAVE_INFO_MSG = "Fayilolin cookie za a adana su azaman cookie.txt a cikin babban fayil ɗin ku."
    COOKIE_MENU_TIP_HEADER_MSG = "Shawara: Hakanan zaka iya amfani da umarni kai tsaye:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – sauke kuma tabbatar da cookies"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – yi amfani da tushe na musamman ta fihirisa (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Sannan tabbatar da <code>/check_cookie</code> (gwaji akan RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Luôn Tambayi"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/MATSAYI"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Hanyar Haɗi"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Watch"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Taken"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ YANKE"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Yanke Bidiyo</b>\n\nTsawon bidiyo: <b>{start_time} - {end_time}</b>\n\nDa fatan za a aika lokacin da ake so a cikin tsari:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nMisali: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Tsari mara inganci. Da fatan za a yi amfani: <code>HH:MM:SS-HH:MM:SS</code>\n\nMisali: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Range mara inganci. Lokacin farawa dole ne ya zama ƙasa da lokacin ƙarshe."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ Lokacin lokaci yana waje da iyakokin bidiyo.\n\nTsawon bidiyo: <b>{start_time} - {end_time}</b>\n\nDole ne kewayon ku ya kasance cikin waɗannan iyakoki."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>Bidiyo za a yanke:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ An kammala wani ɓangare - {successful_uploads}/{total_files} fayilolin sauti an loda su."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ An sauke sauti cikin nasara kuma an aika - {total_files} fayiloli an loda su."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Asusun TikTok na Sirri</b>\n\n"
        "Wannan asusun TikTok na sirri ne ko duk bidiyoyi na sirri ne.\n\n"
        "<b>💡 Magani:</b>\n"
        "1. Bi asusun @{username}\n"
        "2. Aika cookies ɗin ku zuwa bot ta amfani da umarnin <code>/cookie</code>\n"
        "3. Gwada sake\n\n"
        "<b>Bayan sabunta cookies, gwada sake!</b>"
    )

    #######################################################
