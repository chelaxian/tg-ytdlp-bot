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
    CREDITS_MSG = "<blockquote><i>Dikelola oleh</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Ubah bahasa: /lang</b>"
    TO_USE_MSG = "<i>Untuk menggunakan bot ini, Anda perlu berlangganan ke saluran Telegram @tg_ytdlp.</i>\nSetelah Anda bergabung dengan saluran, <b>kirim ulang tautan video Anda dan bot akan mengunduhnya untuk Anda</b> ❤️\n\n<blockquote>P.S. Mengunduh konten 🔞NSFW dan file dari ☁️Penyimpanan Cloud berbayar! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Jangan tinggalkan saluran - Anda akan dilarang menggunakan bot ⛔️</blockquote>"

    ERROR1 = "Tautan URL tidak ditemukan. Silakan masukkan URL dengan <b>https://</b> atau <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Daftar Putar (yt-dlp)</b>

Untuk mengunduh daftar putar, kirim URL-nya dengan rentang <code>*mulai*akhir</code> di akhir. Misalnya: <code>URL*1*5</code> (5 video pertama dari 1 hingga 5 termasuk). <code>URL*-1*-5</code> (5 video terakhir dari 1 hingga 5 termasuk).
Atau Anda dapat menggunakan <code>/vid DARI-KE URL</code>. Misalnya: <code>/vid 3-7 URL</code> (mengunduh video dari 3 hingga 7 termasuk dari awal). <code>/vid -3-7 URL</code> (mengunduh video dari 3 hingga 7 termasuk dari akhir). Juga berfungsi untuk perintah <code>/audio</code>.

<b>Contoh:</b>

🟥 <b>Rentang video dari daftar putar YouTube:</b> (perlu 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(mengunduh 5 video pertama dari 1 hingga 5 termasuk)
🟥 <b>Video tunggal dari daftar putar YouTube:</b> (perlu 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(mengunduh hanya video ke-3)

⬛️ <b>Profil TikTok:</b> (perlu 🍪 Anda)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(mengunduh 10 video pertama dari profil pengguna)

🟪 <b>Cerita Instagram:</b> (perlu 🍪 Anda)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(mengunduh 3 cerita pertama)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(mengunduh 10 cerita pertama dari album)

🟦 <b>Video VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(mengunduh 3 video pertama dari profil pengguna/grup)

⬛️<b>Saluran Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(mengunduh video dari 2 hingga 4 termasuk dari saluran)

🟪 <b>Klip Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(mengunduh 3 klip pertama dari saluran)

🟦 <b>Grup Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(mengunduh 2 video pertama dari grup)

🟧 <b>Model Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(mengunduh 2 video pertama dari profil model)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(mengunduh 3 video pertama dari hasil pencarian berdasarkan prompt Anda)

dan seterusnya...
lihat <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">daftar situs yang didukung</a>
</blockquote>

<blockquote expandable>🖼 <b>Gambar (gallery-dl)</b>

Gunakan <code>/img URL</code> untuk mengunduh gambar/foto/album dari banyak platform.

<b>Contoh:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Rentang:</b>
<code>/img 11-20 https://example.com/album</code> — item 11..20
<code>/img 11- https://example.com/album</code> — dari 11 hingga akhir (atau batas bot)

<i>Platform yang didukung termasuk vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReActor, dll. Daftar lengkap:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">situs yang didukung gallery-dl</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Bot Unduh Video - Bantuan</b>

📥 <b>Penggunaan Dasar:</b>
• Kirim tautan apa pun → bot mengunduhnya
  <i>bot secara otomatis mencoba mengunduh video melalui yt-dlp dan gambar melalui gallery-dl.</i>
• <b>Beberapa URL:</b> Dalam mode pemilihan kualitas (<code>/format</code>) Anda dapat mengirim hingga <b>10 URL</b> dalam satu pesan. Setiap URL pada baris baru atau dipisahkan oleh spasi.
• <code>/audio URL</code> → ekstrak audio
• <code>/link [kualitas] URL</code> → dapatkan tautan langsung
• <code>/proxy</code> → aktifkan/nonaktifkan proxy untuk semua unduhan
• Balas video dengan teks → ubah keterangan

📋 <b>Daftar Putar & Rentang:</b>
• <code>URL*1*5</code> → unduh 5 video pertama
• <code>URL*-1*-5</code> → unduh 5 video terakhir
• <code>/vid 3-7 URL</code> → menjadi <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → menjadi <code>URL*-3*-7</code>

🍪 <b>Cookies & Privat:</b>
• Unggah cookie *.txt untuk video privat
• <code>/cookie [layanan]</code> → unduh cookies (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → pilih sumber berdasarkan indeks (1–N)
• <code>/cookies_from_browser</code> → ekstrak dari browser
• <code>/check_cookie</code> → verifikasi cookie
• <code>/save_as_cookie</code> → simpan teks sebagai cookie

🧹 <b>Pembersihan:</b>
• <code>/clean</code> → hanya file media
• <code>/clean all</code> → semuanya
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Pengaturan:</b>
• <code>/settings</code> → menu pengaturan
• <code>/format</code> → kualitas & format
• <code>/split</code> → bagi video menjadi beberapa bagian
• <code>/mediainfo on/off</code> → info media
• <code>/nsfw on/off</code> → blur NSFW
• <code>/tags</code> → lihat tag yang disimpan
• <code>/sub on/off</code> → subtitle
• <code>/keyboard</code> → keyboard (OFF/1x3/2x3)

🏷️ <b>Tag:</b>
• Tambahkan <code>#tag1#tag2</code> setelah URL
• Tag muncul di keterangan
• <code>/tags</code> → lihat semua tag

🔗 <b>Tautan Langsung:</b>
• <code>/link URL</code> → kualitas terbaik
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → kualitas spesifik

⚙️ <b>Perintah Cepat:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → atur kualitas
• <code>/keyboard off/1x3/2x3/full</code> → tata letak keyboard
• <code>/split 100mb-2000mb</code> → ubah ukuran bagian
• <code>/subs off/id/en auto</code> → bahasa subtitle
• <code>/list URL</code> → daftar format yang tersedia
• <code>/mediainfo on/off</code> → aktifkan/nonaktifkan info media
• <code>/proxy on/off</code> → aktifkan/nonaktifkan proxy untuk semua unduhan

📊 <b>Info:</b>
• <code>/usage</code> → riwayat unduhan
• <code>/search</code> → pencarian inline melalui @vid

🖼 <b>Gambar:</b>
• <code>URL</code> → unduh gambar URL
• <code>/img URL</code> → unduh gambar dari URL
• <code>/img 11-20 URL</code> → unduh rentang spesifik
• <code>/img 11- URL</code> → unduh dari ke-11 hingga akhir

👨‍💻 <i>Pengembang:</i> @upekshaip
🤝 <i>Kontributor:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Just save your cookie as <b><u>cookie.txt</u></b> and send it to bot as a document.\n\n"
        "You can also send cookies as plain text with <b><u>/save_as_cookie</u></b> command.\n"
        "<b>Usage of <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>Instructions:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>Video search</b>

Press the button below to activate inline search via @vid.

<blockquote>On PC just type <b>"@vid Your_Search_Query"</b> in any chat.</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Image Download Command</b>\n\n"
        "Usage: <code>/img URL</code>\n\n"
        "<b>Examples:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Supported platforms (examples):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, etc. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">full list</a></blockquote>"
        "Also see: "
    )
    
    LINK_HINT_MSG = (
        "Get direct video links with quality selection.\n\n"
        "Usage: /link + URL \n\n"
        "(ex. /link https://youtu.be/abc123)\n"
        "(ex. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Add Bot to Group</b>

Add my bots to your groups to get enhanced features and higher limits!
————————————
📊 <b>Current FREE Limits (in Bot's DM):</b>
<blockquote>•🗑 Messy junk from all the files unsorted 👎
• Max 1 file size: <b>8 GB </b>
• Max 1 file quality: <b>UNLIM</b>
• Max 1 file duration: <b>UNLIM</b>
• Max number of downloads: <b>UNLIM</b>
• Max URLs in one message: <b>10</b> (only in quality selection mode)
• Max playlist items per 1 time: <b>50</b>
• Max TikTok videos per 1 time: <b>500</b>
• Max images per 1 time: <b>1000</b>
• URL rate limits: <b>5/min, 60/hour, 1000/day</b>
• Command limit: <b>20/min</b>
• 1 Download max time: <b>2 hours</b>
• 🔞 NSFW content is paid! 1⭐️ = $0.02
• 🆓 ALL OTHER MEDIA ARE TOTALY FREE
• 📝 All content logs & caching to my log-channels for instant repost when re-downloading</blockquote>

💬<b>This limits only for video with subtitles:</b>
<blockquote>• Max video+subs duration: <b>1.5 hours</b>
• Max video+subs file size: <b>500 MB</b>
• Max video+subs quality: <b>720p</b></blockquote>
————————————
🚀 <b>Paid Group Benefits (2️⃣x Limits):</b>
<blockquote>•  🗂 Structured neat media vault sorted by topics 👍
•  📁 Bots reply in the topic you call them
•  📌 Auto pin status message with download progress
•  🖼 /img command downloads media as 10-item albums
• Max 1 file size: <b>16 GB</b> ⬆️
• Max URLs in one message: <b>20</b> ⬆️ (only in quality selection mode)
• Max playlist items per 1 time: <b>100</b> ⬆️
• Max TikTok videos per 1 time: 1000 ⬆️
• Max images per 1 time: 2000 ⬆️
• URL rate limits: <b>10/min, 120/hour, 2000/day</b> ⬆️
• Command limit: <b>40/min</b> ⬆️
• 1 Download max time: <b>4 hours</b> ⬆️
• 🔞 NSFW content: Free with full metadata 🆓
• 📢 No need to subscribe to my channel for groups
• 👥 All group members will have access to paid functions!
• 🗒 No logs / no cache to my log-channels! You can reject copy/repost in group settings</blockquote>

💬 <b>2️⃣x limits for video with subtitles:</b>
<blockquote>• Max video+subs duration: <b>3 hours</b> ⬆️
• Max video+subs file size: <b>1000 MB</b> ⬆️
• Max video+subs quality: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Pricing & Setup:</b>
<blockquote>• Price: <b>$5/month</b> per 1 bot in group
• Setup: Contact @iilililiiillliiliililliilliliiil
• Payment: 💎TON or other methods💲
• Support: Full technical support included</blockquote>
————————————
You can add my bots to your group to unblock free 🔞<b>NSFW</b> and to double (x2️⃣) all limits.
Contact me if you want me to allow your group to use my bots @iilililiiillliiliililliilliliiil
————————————
💡<b>TIP:</b> <blockquote>You can chip in money with any amount of your friends (for example 100 people) and made 1 purchase for whole group - ALL GROUP MEMBERS WILL HAVE FULL UNLIMITED ACCESS to all bots functions in that group for just <b>0.05$</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW Mode: ON✅</b>

• NSFW content will be displayed without blurring.
• Spoilers will not apply to NSFW media.
• The content will be visible immediately

<i>Use /nsfw off to enable blur</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW Mode: OFF</b>

⚠️ <b>Blur enabled</b>
• NSFW content will be hidden under spoiler   
• To view, you will need to click on the media
• Spoilers will apply to NSFW media.

<i>Use /nsfw on to disable blur</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Invalid parameter</b>

Use:
• <code>/nsfw on</code> - disable blur
• <code>/nsfw off</code> - enable blur
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Checking cache...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Memproses..."
    DOWNLOADING_MSG = "📥 <b>Downloading media...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Downloading image...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Download complete</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Diunduh:"
    SENT_STATUS_MSG = "Terkirim:"
    PENDING_TO_SEND_STATUS_MSG = "Menunggu pengiriman:"
    TITLE_LABEL_MSG = "Judul:"
    MEDIA_COUNT_LABEL_MSG = "Jumlah media:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Pengunduhan selesai, memproses audio..."
    VIDEO_PROCESSING_MSG = "📽 Video sedang diproses..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Sent from cache</b>\n\nSent albums: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Video berhasil dikirim dari cache."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Daftar putar video yang dikirim dari cache ({cached}/{total} file)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} video dikirim dari cache, download yang hilang..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Sent from cache: {cached}\n🔄 Continuing download..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Could not analyze media, proceeding with maximum allowed range (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Could not determine media count, proceeding with maximum allowed range (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Could not determine total media count, proceeding with specified range {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>Invalid URL</b>\n\nPlease provide a valid URL starting with http:// or https://"

    ERROR_OCCURRED_MSG = "❌ <b>Error occurred</b>\n\n<code>{url}</code>\n\nError: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Kesalahan saat mengirim video: {error}"
    ERROR_UNKNOWN_MSG = "❌ Kesalahan tidak diketahui: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Ruang disk tidak cukup untuk mengunduh video."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Ukuran file melebihi batas {limit} GB. Silakan pilih file yang lebih kecil dalam ukuran yang diizinkan."

    ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram has limited message sending.\n⏳ Please wait: {time}\nTo update timer send URL again 2 times."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram has limited message sending.\n⏳ Please wait: \nTo update timer send URL again 2 times."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Gagal mengunduh subtitle"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Direct Stream Links</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Title:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Duration:</b> {duration} sec\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Kesalahan: Pesan asli tidak ditemukan."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{tag} contains forbidden characters. Only letters, digits and _ are allowed.\nPlease use: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Video playlist yang dikirimkan: {sent}/{total} file."
    PLAYLIST_CACHE_SENT_MSG = "✅ Dikirim dari cache: {cached}/{total} file."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Failed to get stream links"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Select a browser to download cookies from:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "No browsers found on this system. You can download cookies from remote URL or monitor browser status:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Open Browser</b> - to monitor browser status in mini-app"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Open Browser"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Download from Remote URL"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie file downloaded via fallback and saved as cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ No supported browsers found and no COOKIE_URL configured. Use /cookie or upload cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL must point to a .txt file."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fallback cookie file is too large (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fallback cookie source unavailable (status {status}). Try /cookie or upload cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Error downloading fallback cookie. Try /cookie or upload cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Unexpected error during fallback cookie download."
    BTN_CLOSE = "🔚Tutup"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Nilai boolean tidak valid"
    ARGS_CLOSED_MSG = "Ditutup"
    ARGS_ALL_RESET_MSG = "✅ Semua argumen direset"
    ARGS_RESET_ERROR_MSG = "❌ Kesalahan mereset argumen"
    ARGS_INVALID_PARAM_MSG = "❌ Parameter tidak valid"
    ARGS_BOOL_SET_MSG = "Diatur ke {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "Sudah diatur ke {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Nilai pilihan tidak valid"
    ARGS_VALUE_SET_MSG = "Diatur ke {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "Sudah diatur ke {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Current value:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Examples:</b>\n• <code>default</code> - Use default XFF strategy\n• <code>never</code> - Never use XFF header\n• <code>US</code> - United States country code\n• <code>GB</code> - United Kingdom country code\n• <code>DE</code> - Germany country code\n• <code>FR</code> - France country code\n• <code>JP</code> - Japan country code\n• <code>192.168.1.0/24</code> - IP block (CIDR)\n• <code>10.0.0.0/8</code> - Private IP range\n• <code>203.0.113.0/24</code> - Public IP block\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Note:</b> This replaces --geo-bypass options. Use any 2-letter country code or IP block in CIDR notation.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Example:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Silakan kirimkan nilai baru Anda."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Range:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Silakan kirim nomor."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Examples:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Note:</b> These headers will be added to existing Referer and User-Agent headers.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Current yt-dlp Arguments:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - True/False switches\n• 📋 <b>Select</b> - Choose from options\n• 🔢 <b>Numeric</b> - Number input\n• 📝🔧 <b>Text</b> - Text/JSON input</blockquote>\n\nThese settings will be applied to all your downloads."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "Force IPv6 connections",
        "force_ipv4": "Force IPv4 connections", 
        "no_live_from_start": "Do not download live streams from start",
        "live_from_start": "Download live streams from start",
        "no_check_certificates": "Suppress HTTPS certificate validation",
        "check_certificate": "Check SSL certificate",
        "no_playlist": "Download only single video, not playlist",
        "embed_metadata": "Embed metadata in video file",
        "embed_thumbnail": "Embed thumbnail in video file",
        "write_thumbnail": "Write thumbnail to file",
        "ignore_errors": "Ignore download errors and continue",
        "legacy_server_connect": "Allow legacy server connections",
        "concurrent_fragments": "Number of concurrent fragments to download",
        "xff": "X-Forwarded-For header strategy",
        "user_agent": "User-Agent header",
        "impersonate": "Browser impersonation",
        "referer": "Referer header",
        "geo_bypass": "Bypass geographic restrictions",
        "hls_use_mpegts": "Use MPEG-TS for HLS",
        "no_part": "Do not use .part files",
        "no_continue": "Do not resume partial downloads",
        "audio_format": "Audio format",
        "video_format": "Video format",
        "merge_output_format": "Merge output format",
        "send_as_file": "Send as file",
        "username": "Username",
        "password": "Password",
        "twofactor": "Two-factor authentication code",
        "min_filesize": "Minimum file size (MB)",
        "max_filesize": "Maximum file size (MB)",
        "playlist_items": "Playlist items",
        "date": "Date",
        "datebefore": "Date before",
        "dateafter": "Date after",
        "http_headers": "HTTP headers",
        "sleep_interval": "Sleep interval",
        "max_sleep_interval": "Maximum sleep interval",
        "retries": "Number of retries",
        "http_chunk_size": "HTTP chunk size",
        "sleep_subtitles": "Sleep for subtitles"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp Arguments Configuration</b>\n\n<blockquote>📋 <b>Groups:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp Arguments Configuration</b>\n\n"
        "<blockquote>📋 <b>Groups:</b>\n"
        "• ✅/❌ <b>Boolean</b> - True/False switches\n"
        "• 📋 <b>Select</b> - Choose from options\n"
        "• 🔢 <b>Numeric</b> - Number input\n"
        "• 📝🔧 <b>Text</b> - Text/JSON input</blockquote>\n\n"
        "These settings will be applied to all your downloads."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Harap tunggu..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Terjadi kesalahan"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Input mode automatically closed due to inactivity (5 minutes)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Masukan berisi konten yang berpotensi berbahaya: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Input terlalu panjang (maks 1000 karakter)"
    ARGS_INVALID_URL_MSG = "❌ Format URL tidak valid. Harus dimulai dengan http:// atau https://"
    ARGS_INVALID_JSON_MSG = "❌ Format JSON tidak valid"
    ARGS_NUMBER_RANGE_MSG = "❌ Nomor harus antara {min_val} dan {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Format angka tidak valid"
    ARGS_DATE_FORMAT_MSG = "❌ Tanggal harus dalam format YYYYMMDD (misalnya 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Tahun harus antara tahun 1900 dan 2100"
    ARGS_MONTH_RANGE_MSG = "❌ Bulan harus antara 01 dan 12"
    ARGS_DAY_RANGE_MSG = "❌ Hari harus antara 01 dan 31"
    ARGS_INVALID_DATE_MSG = "❌ Format tanggal tidak valid"
    ARGS_INVALID_XFF_MSG = "❌ XFF harus 'default', 'tidak pernah', kode negara (mis., AS), atau blok IP (mis., 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "Tidak ada argumen khusus yang ditetapkan. Semua parameter menggunakan nilai default."
    ARGS_RESET_SUCCESS_MSG = "✅ Semua argumen disetel ulang ke default."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Kirim pesan terlalu panjang. Maksimum 500 karakter."
    ARGS_ERROR_PROCESSING_MSG = "❌ Kesalahan saat memproses masukan. Silakan coba lagi."
    ARGS_BOOL_INPUT_MSG = "❌ Silakan masukkan 'True' atau 'False' untuk opsi Kirim Sebagai File."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Silakan berikan nomor yang valid."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Silakan kirim <code>True</code> atau <code>False</code> untuk mengaktifkan/menonaktifkan opsi ini."
    ARGS_JSON_VALUE_REQUEST_MSG = "Silakan kirim JSON yang valid."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Anda belum memiliki tag."
    TAGS_MESSAGE_CLOSED_MSG = "Pesan tag ditutup."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Subtitle dinonaktifkan dan mode Selalu Tanya dimatikan."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUB Selalu Tanya diaktifkan."
    SUBS_LANGUAGE_SET_MSG = "✅ Bahasa subtitle diatur ke: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️PERINGATAN: karena dampak CPU tinggi, fungsi ini sangat lambat (hampir real-time) dan dibatasi hingga:\n"
        "- Kualitas maksimum 720p\n"
        "- Durasi maksimum 1.5 jam\n"
        "- Ukuran video maksimum 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Perintah cepat:</b>\n"
        "• <code>/subs off</code> - nonaktifkan subtitle\n"
        "• <code>/subs on</code> - aktifkan mode Selalu Tanya\n"
        "• <code>/subs id</code> - atur bahasa\n"
        "• <code>/subs id auto</code> - atur bahasa dengan AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Subtitle dinonaktifkan"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Bahasa yang dipilih: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Mengunduh subtitle..."
    SUBS_DISABLED_ERROR_MSG = "❌ Subtitle dinonaktifkan. Gunakan /subs untuk mengonfigurasi."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Pengunduhan subtitle hanya didukung untuk YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Subtitle</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Bahasa:</b> {lang}\n"
        "<b>Tipe:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 File SRT subtitle dikirim ke pengguna."
    SUBS_ERROR_PROCESSING_MSG = "❌ Kesalahan memproses file subtitle."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Gagal mengunduh subtitle."
    SUBS_ERROR_MSG = "❌ Kesalahan mengunduh subtitle: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Ukuran bagian split diatur ke: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **Ukuran tidak valid!**\n\n"
        "**Rentang valid:** 100MB hingga 2GB\n\n"
        "**Format valid:**\n"
        "• `100mb` hingga `2000mb` (megabyte)\n"
        "• `0.1gb` hingga `2gb` (gigabyte)\n\n"
        "**Contoh:**\n"
        "• `/split 100mb` - 100 megabyte\n"
        "• `/split 500mb` - 500 megabyte\n"
        "• `/split 1.5gb` - 1.5 gigabyte\n"
        "• `/split 2gb` - 2 gigabyte\n"
        "• `/split 2000mb` - 2000 megabyte (2GB)\n\n"
        "**Preset:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Pilih ukuran bagian maksimum untuk pemisahan video:**\n\n"
        "**Rentang:** 100MB hingga 2GB\n\n"
        "**Perintah cepat:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Contoh:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Menu ditutup."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Pengaturan Bot</b>\n\nPilih kategori:"
    SETTINGS_MENU_CLOSED_MSG = "Menu ditutup."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Opsi Pembersihan</b>\n\nPilih yang akan dibersihkan:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nPilih tindakan:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIA</b>\n\nPilih tindakan:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nPilih tindakan:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ PERINTAH LAINNYA</b>\n\nPilih tindakan:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Perintah dieksekusi."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Batas flood. Coba lagi nanti."
    SETTINGS_HINT_SENT_MSG = "Petunjuk dikirim."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Pembantu pencarian dibuka."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Perintah tidak dikenal."
    SETTINGS_HINT_CLOSED_MSG = "Petunjuk ditutup."
    SETTINGS_HELP_SENT_MSG = "Kirim teks bantuan ke pengguna"
    SETTINGS_MENU_OPENED_MSG = "Menu /settings dibuka"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Pembantu pencarian ditutup"
    SEARCH_CLOSED_MSG = "Ditutup"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proksi {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Kesalahan menyimpan pengaturan proxy."
    PROXY_MENU_TEXT_MSG = "Aktifkan atau nonaktifkan penggunaan server proxy untuk semua operasi yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Aktifkan atau nonaktifkan penggunaan server proxy ({count} tersedia) untuk semua operasi yt-dlp?\n\nKetika diaktifkan, proxy akan dipilih menggunakan metode {method}."
    PROXY_MENU_CLOSED_MSG = "Menu ditutup."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy diaktifkan. Semua operasi yt-dlp akan menggunakan proxy."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy diaktifkan. Semua operasi yt-dlp akan menggunakan {count} server proxy dengan metode pemilihan {method}."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Proksi diaktifkan (SEMUA mode OTOMATIS).\n\n📊 Bot akan mencoba proxy dengan urutan sebagai berikut:\n1️⃣ {config_count} proksi dari Config.py\n2️⃣ {file_count} proxy dari file TXT/proxy.txt\n\n🔄 Semua proxy akan dicoba secara berurutan hingga koneksi berhasil."
    PROXY_DISABLED_MSG = "❌ Proxy dinonaktifkan."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Kesalahan menyimpan pengaturan proxy."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy diaktifkan."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy dinonaktifkan."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ TUNGGU SAMPAI UNDUHAN SEBELUMNYA SELESAI"
    AUDIO_HELP_MSG = (
        "<b>🎧 Perintah Unduh Audio</b>\n\n"
        "Penggunaan: <code>/audio URL</code>\n\n"
        "<b>Contoh:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Lihat juga: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Petunjuk audio ditutup."
    PLAYLIST_HELP_CLOSED_MSG = "Bantuan daftar putar ditutup."
    USERLOGS_CLOSED_MSG = "Pesan log ditutup."
    HELP_CLOSED_MSG = "Bantuan ditutup."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>Pengaturan Blur NSFW</b>\n\nKonten NSFW adalah <b>{status}</b>.\n\nPilih apakah akan memburamkan konten NSFW:"
    NSFW_MENU_CLOSED_MSG = "Menu ditutup."
    NSFW_BLUR_DISABLED_MSG = "Blur NSFW dinonaktifkan."
    NSFW_BLUR_ENABLED_MSG = "Blur NSFW diaktifkan."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Blur NSFW dinonaktifkan."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Blur NSFW diaktifkan."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ Info Media {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Aktifkan atau nonaktifkan pengiriman MediaInfo untuk file yang diunduh?"
    MEDIAINFO_MENU_CLOSED_MSG = "Menu ditutup."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo diaktifkan. Setelah mengunduh, info file akan dikirim."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo dinonaktifkan."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo diaktifkan."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo dinonaktifkan."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Daftar Format yang Tersedia</b>\n\n"
        "Dapatkan format video/audio yang tersedia untuk URL.\n\n"
        "<b>Penggunaan:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Contoh:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Cara menggunakan ID format:</b>\n"
        "Setelah mendapatkan daftar, gunakan ID format spesifik:\n"
        "• <code>/format id 401</code> - unduh format 401\n"
        "• <code>/format id401</code> - sama seperti di atas\n"
        "• <code>/format id140 audio</code> - unduh format 140 sebagai audio MP3\n\n"
        "Perintah ini akan menampilkan semua format yang tersedia yang dapat diunduh."
    )
    LIST_PROCESSING_MSG = "🔄 Mendapatkan format yang tersedia..."
    LIST_INVALID_URL_MSG = "❌ Silakan berikan URL yang valid yang dimulai dengan http:// atau https://"
    LIST_CAPTION_MSG = (
        "📃 Format yang tersedia untuk:\n<code>{url}</code>\n\n"
        "💡 <b>Cara mengatur format:</b>\n"
        "• <code>/format id 134</code> - Unduh ID format spesifik\n"
        "• <code>/format 720p</code> - Unduh berdasarkan kualitas\n"
        "• <code>/format best</code> - Unduh kualitas terbaik\n"
        "• <code>/format ask</code> - Selalu tanya kualitas\n\n"
        "{audio_note}\n"
        "📋 Gunakan ID format dari daftar di atas"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Format hanya audio:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Unduh format 140 sebagai audio MP3\n"
        "• <code>/format id140 audio</code> - sama seperti di atas\n"
        "Ini akan diunduh sebagai file audio MP3.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Kesalahan mengirim file format: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Gagal mendapatkan format:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Terjadi kesalahan saat memproses perintah"
    LIST_ERROR_CALLBACK_MSG = "Terjadi kesalahan"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Cara menggunakan ID format:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Setelah mendapatkan daftar, gunakan ID format spesifik:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - unduh format 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - sama seperti di atas\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - unduh format 140 sebagai audio MP3\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - sama seperti di atas\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Format hanya audio terdeteksi: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Format ini akan diunduh sebagai file audio MP3.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Format hanya video:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Gunakan ID format dari daftar di atas"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Penggunaan:</b>\n"
        "<code>/link [kualitas] URL</code>\n\n"
        "<b>Contoh:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - kualitas terbaik\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p atau lebih rendah\n"
        "• /link 720p https://youtube.com/watch?v=... - sama seperti di atas\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K atau lebih rendah\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K atau lebih rendah"
        "</blockquote>\n\n"
        "<b>Kualitas:</b> dari 1 hingga 10000 (mis., 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Silakan berikan URL yang valid"
    LINK_PROCESSING_MSG = "🔗 Mendapatkan tautan langsung..."
    LINK_DURATION_MSG = "⏱ <b>Durasi:</b> {duration} detik\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Stream video:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Stream audio:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Pengaturan keyboard diperbarui!**\n\nPengaturan baru: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Argumen tidak valid!**\n\n"
        "Opsi valid: `off`, `1x3`, `2x3`, `full`\n\n"
        "Contoh: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Pengaturan Keyboard**\n\n"
        "Saat ini: **{current}**\n\n"
        "Pilih opsi:\n\n"
        "Atau gunakan: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 keyboard diaktifkan!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Keyboard disembunyikan"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 Keyboard 1x3 diaktifkan!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 Keyboard 2x3 diaktifkan!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Keyboard emoji diaktifkan!"
    KEYBOARD_ERROR_APPLYING_MSG = "Kesalahan menerapkan pengaturan keyboard {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Format diatur ke: Selalu Tanya. Anda akan diminta kualitas setiap kali mengirim URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format diatur ke: Selalu Tanya. Sekarang Anda akan diminta kualitas setiap kali mengirim URL."
    FORMAT_BEST_UPDATED_MSG = "✅ Format diperbarui ke kualitas terbaik (prioritas AVC+MP4):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Format diperbarui ke ID {id}:\n{format}\n\n💡 <b>Catatan:</b> Jika ini adalah format hanya audio, akan diunduh sebagai file audio MP3."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Format diperbarui ke ID {id} (hanya audio):\n{format}\n\n💡 Ini akan diunduh sebagai file audio MP3."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Format diperbarui ke kualitas {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Format diperbarui ke:\n{format}"
    FORMAT_MENU_MSG = (
        "Pilih opsi format atau kirim yang kustom menggunakan:\n"
        "• <code>/format &lt;format_string&gt;</code> - format kustom\n"
        "• <code>/format 720</code> - kualitas 720p\n"
        "• <code>/format 4k</code> - kualitas 4K\n"
        "• <code>/format 8k</code> - kualitas 8K\n"
        "• <code>/format id 401</code> - ID format spesifik\n"
        "• <code>/format ask</code> - selalu tampilkan menu\n"
        "• <code>/format best</code> - bv+ba/kualitas terbaik"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Untuk menggunakan format kustom, kirim perintah dalam bentuk berikut:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Ganti <code>bestvideo+bestaudio/best</code> dengan string format yang Anda inginkan."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Pilih resolusi dan codec yang Anda inginkan:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format diatur ke: Selalu Tanya. Sekarang Anda akan diminta kualitas setiap kali mengirim URL."
    FORMAT_UPDATED_MSG = "✅ Format diperbarui ke:\n{format}"
    FORMAT_SAVED_MSG = "✅ Format disimpan."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Pilihan format diperbarui."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Menu format kustom ditutup"
    FORMAT_CODEC_SET_MSG = "✅ Codec diatur ke {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Pilihan browser diperbarui."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Akses ditolak. Hanya admin."
    ACCESS_DENIED_ADMIN = "❌ Akses ditolak. Hanya admin."
    WELCOME_MASTER = "Selamat Datang Tuan 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Maaf... Terjadi kesalahan saat mengunduh."
    SIZE_LIMIT_EXCEEDED = "❌ Ukuran file melebihi batas {max_size_gb} GB. Silakan pilih file yang lebih kecil dalam ukuran yang diizinkan."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Script tidak ditemukan: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Mengunduh dump Firebase baru menggunakan {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Cache Firebase dimuat ulang dengan sukses!"
    ADMIN_CACHE_FAILED_MSG = "❌ Gagal memuat ulang cache Firebase. Periksa apakah {cache_file} ada."
    ADMIN_ERROR_RELOADING_MSG = "❌ Kesalahan memuat ulang cache: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Kesalahan menjalankan {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Pesan promo dikirim ke semua pengguna lain</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Tidak dapat mengirim pesan promo. Coba balas pesan\nAtau terjadi kesalahan</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ Pengguna belum mengunduh konten apa pun...</b> Tidak ada di log"
    ADMIN_INVALID_COMMAND_MSG = "❌ Perintah tidak valid"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ Tidak ada data ditemukan di cache untuk <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Antrian kosong — belum ada yang meninggalkan saluran."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Antrian ban</b>\nTotal tertunda: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (keluar: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… dan {extra} pengguna lagi."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Gunakan /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Pengguna yang diblokir dari antrian: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Auto-blocking diaktifkan: yang keluar baru akan dilarang segera."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Auto-blocking dinonaktifkan."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Jendela auto-block terjadwal diatur ke setiap {interval}."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Log aktivitas saluran untuk {hours} jam terakhir (2 hari)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 {hours} jam terakhir (2 hari): bergabung {joined}, keluar {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Tidak ada aktivitas untuk {hours} jam terakhir (2 hari)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Total: 🟢 {joined} bergabung, 🔴 {left} keluar."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Tidak ada akses ke log aktivitas saluran. Bot tidak dapat membaca log admin. Berikan CHANNEL_GUARD_SESSION_STRING di config dengan sesi pengguna untuk mengaktifkan fitur ini."
    BAN_TIME_USAGE_MSG = "❌ Penggunaan: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Gunakan format seperti 10s, 6m, 5h, 4d, 3w, 2M atau 1y."
    BAN_TIME_SET_MSG = "🕒 Interval pemindaian log saluran diatur ke {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Laporan pemindaian saluran\n"
        "Dijalankan pada: {run_ts}\n"
        "Interval: {interval}\n"
        "Yang keluar baru: {new_leavers}\n"
        "Ban otomatis: {auto_banned}\n"
        "Tertunda: {pending}\n"
        "event_id terakhir: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Penggunaan: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Admin tidak dapat menghapus admin"
    ADMIN_USER_BLOCKED_MSG = "Pengguna diblokir 🔒❌\n \nID: <code>{user_id}</code>\nTanggal Diblokir: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> sudah diblokir ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Maaf! Anda bukan admin"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Penggunaan: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Pengguna tidak diblokir 🔓✅\n \nID: <code>{user_id}</code>\nTanggal Tidak Diblokir: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> sudah tidak diblokir ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Pengguna yang tidak diblokir: {count}\n⏱ Timestamp: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Penggunaan: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Pengguna diabaikan 👁️❌\n \nID: <code>{user_id}</code>\nTanggal diabaikan: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> sudah diabaikan ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Penggunaan: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Pengguna tidak lagi diabaikan 👁️✅\n \nID: <code>{user_id}</code>\nTanggal tidak diabaikan: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> tidak diabaikan ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Waktu berjalan bot -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Silakan berikan URL untuk membersihkan cache.\nPenggunaan: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Silakan berikan URL yang valid.\nPenggunaan: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Cache berhasil dibersihkan untuk URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Tidak ada cache ditemukan untuk tautan ini."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Kesalahan membersihkan cache: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Akses ditolak. Hanya admin."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Menjalankan skrip pembaruan daftar porn: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Skrip selesai dengan sukses!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Skrip selesai dengan sukses!\n\nOutput:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Skrip gagal dengan kode return {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Kesalahan menjalankan skrip: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Memuat ulang cache porno dan terkait domain..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Cache pornografi berhasil dimuat ulang!\n\n"
        "📊 Status cache saat ini:\n"
        "• Domain pornografi: {porn_domains}\n"
        "• Kata kunci pornografi: {porn_keywords}\n"
        "• Situs yang didukung: {supported_sites}\n"
        "• DAFTAR PUTIH: {whitelist}\n"
        "• DAFTAR ABU-ABU: {greylist}\n"
        "• DAFTAR HITAM: {black_list}\n"
        "• KATA KUNCI PUTIH: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Kesalahan saat memuat ulang cache porno: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Harap berikan URL untuk diperiksa.\nPenggunaan: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Harap berikan URL yang valid.\nPenggunaan: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Memeriksa URL untuk konten NSFW...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Hasil Pemeriksaan Pornografi</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Status:</b> <b>{status_text}</b>\n\n"
        "<b>Penjelasan:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Kesalahan memeriksa URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Cookies telah dibersihkan."
    CLEAN_LOGS_CLEANED_MSG = "Logs telah dibersihkan."
    CLEAN_TAGS_CLEANED_MSG = "Tag telah dibersihkan."
    CLEAN_FORMAT_CLEANED_MSG = "Format telah dibersihkan."
    CLEAN_SPLIT_CLEANED_MSG = "Split telah dibersihkan."
    CLEAN_MEDIAINFO_CLEANED_MSG = "MediaInfo telah dibersihkan."
    CLEAN_SUBS_CLEANED_MSG = "Pengaturan subtitle dibersihkan."
    CLEAN_KEYBOARD_CLEANED_MSG = "Pengaturan keyboard dibersihkan."
    CLEAN_ARGS_CLEANED_MSG = "Pengaturan argumen dibersihkan."
    CLEAN_NSFW_CLEANED_MSG = "Pengaturan NSFW dibersihkan."
    CLEAN_PROXY_CLEANED_MSG = "Pengaturan proxy dibersihkan."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Pengaturan flood wait dibersihkan."
    CLEAN_ALL_CLEANED_MSG = "Semua file dibersihkan."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nPilih tindakan:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ File cookie disimpan"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Validasi dilewati untuk cookies non-YouTube"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ File cookie ada tetapi formatnya salah"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ File cookie tidak ditemukan."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Memulai tes cookies YouTube...\n\nHarap tunggu sementara saya memeriksa dan memvalidasi cookies Anda."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Cookies YouTube yang ada berfungsi dengan baik!\n\nTidak perlu mengunduh yang baru."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Cookies YouTube yang ada telah kedaluwarsa atau tidak valid.\n\n🔄 Mengunduh cookies baru..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ Sumber cookie {service} tidak dikonfigurasi!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ Sumber cookie {service} harus berupa file .txt!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Batas rentang terlampaui: {range_count} file diminta (maksimum {max_img_files}).\n\nGunakan salah satu perintah ini untuk mengunduh file maksimum yang tersedia:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Tutup"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Batas media terlampaui: {count} file diminta (maksimum {max_count}).\n\nGunakan salah satu perintah ini untuk mengunduh file maksimum yang tersedia:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Ditemukan <b>{count}</b> item media dari tautan"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Pilih rentang unduhan:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Peniruan browser"
    ARGS_REFERER_DESC_MSG = "Header Referer"
    ARGS_USER_AGENT_DESC_MSG = "Header User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "Bypass pembatasan geografis"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Periksa sertifikat SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "Unduh streaming langsung dari awal"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Jangan unduh streaming langsung dari awal"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Gunakan kontainer MPEG-TS untuk video HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "Unduh hanya video tunggal, bukan daftar putar"
    ARGS_NO_PART_DESC_MSG = "Jangan gunakan file .part"
    ARGS_NO_CONTINUE_DESC_MSG = "Jangan lanjutkan unduhan sebagian"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Format audio untuk ekstraksi"
    ARGS_EMBED_METADATA_DESC_MSG = "Sematkan metadata dalam file video"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Sematkan thumbnail dalam file video"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Tulis thumbnail ke file"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Jumlah fragmen bersamaan untuk diunduh"
    ARGS_FORCE_IPV4_DESC_MSG = "Paksa koneksi IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "Paksa koneksi IPv6"
    ARGS_XFF_DESC_MSG = "Strategi header X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "Ukuran chunk HTTP (byte)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Tunda sebelum unduh subtitle (detik)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Izinkan koneksi server lama"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Tekan validasi sertifikat HTTPS"
    ARGS_USERNAME_DESC_MSG = "Nama pengguna akun"
    ARGS_PASSWORD_DESC_MSG = "Kata sandi akun"
    ARGS_TWOFACTOR_DESC_MSG = "Kode autentikasi dua faktor"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Abaikan kesalahan unduhan dan lanjutkan"
    ARGS_MIN_FILESIZE_DESC_MSG = "Ukuran file minimum (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Ukuran file maksimum (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Item daftar putar untuk diunduh (mis., 1,3,5 atau 1-5)"
    ARGS_DATE_DESC_MSG = "Unduh video yang diunggah pada tanggal ini (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Unduh video yang diunggah sebelum tanggal ini (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Unduh video yang diunggah setelah tanggal ini (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Header HTTP kustom (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Interval tunda antar permintaan (detik)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Interval tunda maksimum (detik)"
    ARGS_RETRIES_DESC_MSG = "Jumlah percobaan ulang"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Format kontainer video"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Format kontainer output untuk penggabungan"
    ARGS_SEND_AS_FILE_DESC_MSG = "Kirim semua media sebagai dokumen bukan media"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Meniru"
    ARGS_REFERER_SHORT_MSG = "Referensi"
    ARGS_GEO_BYPASS_SHORT_MSG = "Lewati Geo"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Cek Sertifikat"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Mulai Langsung"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Tidak Mulai Langsung"
    ARGS_USER_AGENT_SHORT_MSG = "Agen Pengguna"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Tidak Ada Daftar Putar"
    ARGS_NO_PART_SHORT_MSG = "Tidak Ada Bagian"
    ARGS_NO_CONTINUE_SHORT_MSG = "Tidak Lanjutkan"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Format Audio"
    ARGS_EMBED_METADATA_SHORT_MSG = "Sematkan Meta"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Sematkan Thumb"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Tulis Thumb"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Bersamaan"
    ARGS_FORCE_IPV4_SHORT_MSG = "Paksa IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Paksa IPv6"
    ARGS_XFF_SHORT_MSG = "Header XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Ukuran Chunk"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Tunda Subs"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Koneksi Lama"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Tidak Cek Sertifikat"
    ARGS_USERNAME_SHORT_MSG = "Nama Pengguna"
    ARGS_PASSWORD_SHORT_MSG = "Kata Sandi"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Abaikan Kesalahan"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Ukuran Min"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Ukuran Maks"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Item Daftar Putar"
    ARGS_DATE_SHORT_MSG = "Tanggal"
    ARGS_DATEBEFORE_SHORT_MSG = "Tanggal Sebelum"
    ARGS_DATEAFTER_SHORT_MSG = "Tanggal Sesudah"
    ARGS_HTTP_HEADERS_SHORT_MSG = "Header HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Interval Tunda"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Tunda Maks"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Format Video"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Format Gabungan"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Kirim Sebagai File"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ File terlalu besar. Ukuran maksimum adalah 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Hanya file dengan format .txt yang diizinkan."
    COOKIES_INVALID_COOKIE_MSG = "❌ File tidak terlihat seperti cookie.txt (tidak ada baris '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ Kesalahan membaca file: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ File cookie ada dan memiliki format yang benar"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ File cookie {service} terlalu besar! Maks 100KB, mendapat {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ File cookie {service} diunduh dan disimpan sebagai cookie.txt di folder Anda.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ Sumber cookie {service} tidak tersedia (status {status}). Silakan coba lagi nanti."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Kesalahan mengunduh file cookie {service}. Silakan coba lagi nanti."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Pengguna menyediakan file cookie baru.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie berhasil diperbarui:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Bukan cookie yang valid.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ Sumber cookie YouTube tidak dikonfigurasi!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Mengunduh dan memeriksa cookies YouTube...\n\nPercobaan {attempt} dari {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Akses ditolak. Hanya admin."
    ADMIN_USER_LOGS_TOTAL_MSG = "Total: <b>{total}</b>\n<b>{user_id}</b> - log (10 terakhir):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 keyboard diaktifkan!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Bahasa subtitle diatur ke: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Bahasa subtitle diatur ke: {flag} {name} dengan AUTO/TRANS diaktifkan."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Menu bahasa subtitle ditutup."
    SUBS_DOWNLOADING_MSG = "💬 Mengunduh subtitle..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Memuat ulang cache Firebase ke memori..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Tidak ada COOKIE_URL yang dikonfigurasi. Gunakan /cookie atau unggah cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Mengunduh cookies dari URL remote..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL harus menunjuk ke file .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ File cookie fallback terlalu besar (>100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ File cookie YouTube diunduh melalui fallback dan disimpan sebagai cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Sumber cookie fallback tidak tersedia (status {status}). Coba /cookie atau unggah cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Kesalahan mengunduh cookie fallback. Coba /cookie atau unggah cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Kesalahan tak terduga selama pengunduhan cookie fallback."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ Browser {browser} tidak terpasang."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookies disimpan menggunakan browser: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Gagal menyimpan cookies: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ Cookies YouTube berfungsi dengan baik"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ Cookies YouTube telah kedaluwarsa atau tidak valid\n\nGunakan /cookie untuk mendapatkan cookies baru"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - format kustom\n• <code>/format 720</code> - kualitas 720p\n• <code>/format 4k</code> - kualitas 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Petunjuk dikirim."
    FORMAT_MKV_TOGGLE_MSG = "MKV sekarang {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Tidak ada URL remote yang dikonfigurasi"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Format file tidak valid"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ File terlalu besar"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookies berhasil diunduh"
    COOKIES_SERVER_ERROR_MSG = "❌ Kesalahan server {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Unduhan gagal"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Kesalahan tak terduga"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Browser tidak terpasang."
    COOKIES_MENU_CLOSED_MSG = "Menu ditutup."
    COOKIES_HINT_CLOSED_MSG = "Petunjuk cookie ditutup."
    IMG_HELP_CLOSED_MSG = "Bantuan ditutup."
    SUBS_LANGUAGE_UPDATED_MSG = "Pengaturan bahasa subtitle diperbarui."
    SUBS_MENU_CLOSED_MSG = "Menu bahasa subtitle ditutup."
    KEYBOARD_SET_TO_MSG = "Keyboard diatur ke {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Kesalahan memproses pengaturan"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo diaktifkan."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo dinonaktifkan."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Blur NSFW dinonaktifkan."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Blur NSFW diaktifkan."
    SETTINGS_MENU_CLOSED_MSG = "Menu ditutup."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Flood wait aktif. Coba lagi nanti."
    OTHER_HELP_CLOSED_MSG = "Bantuan ditutup."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Pesan log ditutup."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menu ditutup."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Ukuran tidak valid."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Kesalahan mengirim MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Terjadi kesalahan: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - semua log"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - semua {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Unduh dari URL Remote"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Buka Browser"
    SELECT_BROWSER_MSG = "Pilih browser untuk mengunduh cookies:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Tidak ada browser ditemukan di sistem ini. Anda dapat mengunduh cookies dari URL remote atau memantau status browser:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Buka Browser</b> - untuk memantau status browser di mini-app"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Gagal menjalankan /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Batas flood. Coba lagi nanti."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Gagal membuka menu cookie browser"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Petunjuk simpan sebagai cookie ditutup."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Penggunaan:</b>\n<code>/link [kualitas] URL</code>\n\n<b>Contoh:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - kualitas terbaik\n• /link 720 https://youtube.com/watch?v=... - 720p atau lebih rendah\n• /link 720p https://youtube.com/watch?v=... - sama seperti di atas\n• /link 4k https://youtube.com/watch?v=... - 4K atau lebih rendah\n• /link 8k https://youtube.com/watch?v=... - 8K atau lebih rendah</blockquote>\n\n<b>Kualitas:</b> dari 1 hingga 10000 (mis., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - kualitas 8K"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Tautan langsung diperoleh</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Stream audio:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Gagal mendapatkan tautan stream"
    LINK_ERROR_GETTING_MSG = "❌ <b>Kesalahan mendapatkan tautan:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Indeks cookie YouTube tidak valid: {selected_index}. Rentang yang tersedia adalah 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Mengunduh dan memeriksa cookies YouTube...\n\nPercobaan {attempt} dari {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Mengunduh dan memeriksa cookies YouTube...\n\nPercobaan {attempt} dari {total}\n🔍 Menguji cookies..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ Cookies YouTube berhasil diunduh dan divalidasi!\n\nMenggunakan sumber {source} dari {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Semua cookies YouTube telah kedaluwarsa atau tidak tersedia!\n\nHubungi administrator bot untuk menggantinya."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ Batas percobaan ulang cookie YouTube terlampaui!\n\n🔢 Maksimum: {limit} percobaan per jam\n⏰ Silakan coba lagi nanti"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Tag #{wrong} berisi karakter terlarang. Hanya huruf, angka dan _ yang diizinkan.\nSilakan gunakan: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Argumen tidak valid!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Bahasa subtitle diatur: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Contoh: `/subs id auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Bahasa yang dipilih: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Mode Selalu Tanya {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Subtitle dinonaktifkan"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Pengaturan subtitle</b>\n\n{status_text}\n\nPilih bahasa subtitle:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - nonaktifkan subtitle\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Pengaturan subtitle</b>\n\n{status_text}\n\nPilih bahasa subtitle:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Judul:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Durasi:</b> {duration} detik\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Stream video:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- Kualitas maksimum 720p\n- Durasi maksimum 1.5 jam\n- Ukuran video maksimum 500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️PERINGATAN: karena dampak CPU tinggi, fungsi ini sangat lambat (hampir real-time) dan dibatasi hingga:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Perintah cepat:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - nonaktifkan subtitle\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - aktifkan mode Selalu Tanya\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs id` - atur bahasa\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs id auto` - atur bahasa dengan AUTO/TRANS diaktifkan\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - aktifkan mode Selalu Tanya\n"
    SUBS_AUTO_SUBS_TEXT = "(berlangganan otomatis)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Mode auto-subs {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS dinonaktifkan melalui perintah: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Selalu Tanya diaktifkan melalui perintah: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "Bahasa SUBS diatur melalui perintah: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "Bahasa SUBS + mode otomatis diatur melalui perintah: {arg} otomatis"
    SUBS_MENU_OPENED_LOG_MSG = "Pengguna membuka /subs menu."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Pengguna mengatur bahasa subtitle ke: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Pengguna mengalihkan mode AUTO/TRANS ke: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Pengguna mengalihkan mode Selalu Tanya ke: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Pengguna meminta cookie dari browser."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Keyboard pilihan browser dikirim hanya dengan browser yang diinstal."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Pilihan browser ditutup."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "COOKIE_URL cadangan berhasil digunakan (sumber tersembunyi)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "COOKIE_URL pengganti gagal: status={status} (tersembunyi)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Kesalahan tak terduga COOKIE_URL cadangan: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Peramban {browser} tidak terpasang."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Cookie disimpan menggunakan browser: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "File cookie disimpan untuk pengguna {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "File cookie ada, formatnya benar, dan cookie YouTube berfungsi."
    COOKIES_FILE_EXPIRED_LOG_MSG = "File cookie ada dan memiliki format yang benar, namun cookie YouTube telah kedaluwarsa."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "File cookie ada dan memiliki format yang benar."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "File cookie ada tetapi formatnya salah."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "File kue tidak ditemukan."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{service} URL cookie kosong untuk pengguna {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} URL cookie bukan .txt (tersembunyi)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} file cookie terlalu besar: {size} bytes (sumber tersembunyi)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{service} file cookie diunduh untuk pengguna {user_id} (sumber tersembunyi)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Skrip tidak ditemukan: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Gagal mengirim pesan status awal"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Error running {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Cache Firebase dimuat ulang dengan tugas otomatis."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Cache Firebase dimuat ulang oleh admin."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Terjadi kesalahan saat memuat ulang cache Firebase: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Siaran dimulai. Teks:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Pesan siaran dikirim ke semua pengguna."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Gagal menyiarkan pesan: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Admin {user_id} membersihkan cache untuk URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Admin {user_id} memulai skrip pembaruan daftar porno: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Skrip pembaruan daftar porno berhasil diselesaikan oleh admin {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Skrip pembaruan daftar porno gagal oleh admin {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Admin {user_id} mencoba menjalankan skrip yang tidak ada: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Kesalahan saat menjalankan skrip pembaruan porno oleh admin {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Admin {user_id} memulai reload cache porn"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Kesalahan saat memuat ulang cache porno oleh admin {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Admin {user_id} memeriksa URL untuk NSFW: {url} - Hasil: {status}"
    
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
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Menu format kustom ditutup"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "Tautan langsung diekstraksi untuk pengguna {user_id} dari {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Gagal mengekstrak tautan langsung untuk pengguna {user_id} dari {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Kesalahan dalam perintah tautan untuk pengguna {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Pengguna {user_id} menyetel keyboard ke {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Pengguna {user_id} menyetel keyboard ke {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo diatur melalui perintah: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Pengguna membuka menu /mediainfo."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: ditutup."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo diaktifkan."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo dinonaktifkan."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Ukuran pemisahan diatur ke {size} byte melalui argumen."
    SPLIT_MENU_OPENED_LOG_MSG = "Pengguna membuka/membagi menu."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Seleksi terpisah ditutup."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Ukuran pemisahan diatur ke {size} byte."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Proxy diatur melalui perintah: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Pengguna membuka / menu proxy."
    PROXY_MENU_CLOSED_LOG_MSG = "Proksi: ditutup."
    PROXY_ENABLED_LOG_MSG = "Proksi diaktifkan."
    PROXY_DISABLED_LOG_MSG = "Proksi dinonaktifkan."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Pesan bantuan ditutup."
    AUDIO_HELP_SHOWN_LOG_MSG = "Menampilkan bantuan /audio"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Bantuan daftar putar yang diminta pengguna."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Bantuan daftar putar ditutup."
    AUDIO_HINT_CLOSED_LOG_MSG = "Petunjuk audio ditutup."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Menu tautan langsung dibuat melalui tombol LINK untuk pengguna {user_id} dari {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Gagal mengekstrak tautan langsung melalui tombol LINK untuk pengguna {user_id} dari {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "Perintah LIST dijalankan untuk pengguna {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Penyematan Cepat: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Menu Selalu Tanya dikirimkan untuk {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Membuat menu kualitas cache untuk pengguna {user_id} setelah kesalahan: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Selalu Tanya kesalahan menu untuk {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Format ditetapkan melalui pengaturan /args"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Audio"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Video"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Video"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Selanjutnya ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Sebelumnya"
    SUBTITLES_NEXT_BUTTON_MSG = "Selanjutnya ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Semua kolom teks kosong"
    SENDER_VIDEO_DURATION_MSG = "Durasi video:"
    SENDER_UPLOADING_FILE_MSG = "📤 Mengunggah berkas..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Mengunggah Video..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Durasi video:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 file diunggah."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Info Video"
    DOWN_UP_NUMBER_MSG = "Nomor"
    DOWN_UP_TITLE_MSG = "Judul"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Video yang diunduh."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Sedang diproses untuk diunggah..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Bagian file {part} yang terpecah diunggah"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Pengunggahan selesai"
    DOWN_UP_FILES_UPLOADED_MSG = "file diunggah"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Tutup"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼KODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUB"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 SUB"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Peramban"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Mendapatkan tautan langsung..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Mendapatkan format yang tersedia..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Mendapatkan deskripsi video..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Error mendapatkan deskripsi: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Deskripsi video tidak tersedia"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Error mengirim deskripsi: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Deskripsi video dikirim ke pengguna {user_id} untuk {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Memulai galeri-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Durasi:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Browser:</b> Buka di browser web"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Format yang tersedia untuk"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Cara menggunakan ID format:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Setelah mendapatkan daftar, gunakan ID format spesifik:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - unduh format 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - sama seperti di atas"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - unduh format 140 sebagai audio MP3"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Format hanya audio terdeteksi"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Format ini akan diunduh sebagai file audio MP3."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Cara mengatur format:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Unduh ID format spesifik"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Unduh berdasarkan kualitas"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Unduh kualitas terbaik"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Selalu tanya kualitas"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Format hanya audio:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Unduh format 140 sebagai audio MP3"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Ini akan diunduh sebagai file audio MP3."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Gunakan ID format dari daftar di atas"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Kesalahan: Pesan asli tidak ditemukan."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Halaman format"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Kesalahan menampilkan menu format"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Kesalahan mendapatkan format"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Kesalahan mendapatkan format yang tersedia."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Silakan coba lagi nanti."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp tidak dapat memproses konten ini"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Sistem merekomendasikan menggunakan gallery-dl sebagai gantinya."
    ALWAYS_ASK_OPTIONS_MSG = "**Opsi:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Untuk galeri gambar: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Untuk gambar tunggal: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl sering bekerja lebih baik untuk konten Instagram, Twitter, dan media sosial lainnya."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Coba Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Format diperbaiki via /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Subtitle"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Audio dubbing"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Subtitle tersedia"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Pilih bahasa subtitle"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Subtitle tidak ditemukan & tidak akan disematkan"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Repost instan dari cache"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Pilih bahasa audio"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW berbayar (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Pilih kualitas unduhan"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Unduh gambar (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Tonton video di poketube"  # SEMENTARA DINONAKTIFKAN: layanan poketube sedang down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Dapatkan tautan langsung ke video"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Tampilkan daftar format yang tersedia"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Ubah ekstensi/codec video"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Sematkan"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Ekstrak hanya audio"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW berbayar (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Repost instan dari cache"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Tonton video di poketube"  # SEMENTARA DINONAKTIFKAN: layanan poketube sedang down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Pilih bahasa audio"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Terbaik"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Lainnya"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝hanya sub"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Pengelompokan pintar"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Baris tombol aksi ditambahkan (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Baris tombol aksi ditambahkan (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Tombol bawah ditambahkan ke baris yang ada"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Baris bawah baru dibuat"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Tidak ada video ditemukan dalam daftar putar"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "URL tidak didukung"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Tidak ada video yang dapat ditemukan"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Tidak ada video ditemukan"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Tidak ada media ditemukan"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Tweet ini tidak berisi"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Kesalahan mengambil informasi video:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Kesalahan mengambil informasi video"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Coba perintah <code>/clean</code> dan coba lagi. Jika kesalahan berlanjut, YouTube memerlukan otorisasi. Perbarui cookies.txt via <code>/cookie</code> atau <code>/cookies_from_browser</code> dan coba lagi."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Menu ditutup."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Seleksi Kualitas Manual"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Pilih kualitas secara manual karena deteksi otomatis gagal:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Semua Format yang Tersedia"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Kualitas yang Tersedia (dari cache)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Menggunakan kualitas cache - format baru mungkin tidak tersedia"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Mengunduh format"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Mengunduh"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Mengunduh dengan pelacakan progres..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Mengunduh menggunakan format:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Mengunduh audio menggunakan format:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Mengunduh kualitas terbaik..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Mengunduh dump database..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Mengunduh"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Halaman format"
    ALWAYS_ASK_FROM_CACHE_MSG = "(dari cache)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Kesalahan: Pesan asli tidak ditemukan. Mungkin telah dihapus. Silakan kirim tautan lagi."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Kesalahan: URL asli tidak ditemukan. Silakan kirim tautan lagi."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Tautan langsung diperoleh</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Judul:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Durasi:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Stream video:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Stream audio:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Gagal mendapatkan tautan stream"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Tautan langsung diekstraksi melalui menu Selalu Tanya untuk pengguna {user_id} dari {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Gagal mengekstrak tautan langsung melalui menu Selalu Tanya untuk pengguna {user_id} dari {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Tautan langsung diekstrak melalui down_and_up_with_format untuk pengguna {user_id} dari {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Gagal mengekstrak tautan langsung melalui down_and_up_with_format untuk pengguna {user_id} dari {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Tautan langsung diekstraksi melalui down_and_audio untuk pengguna {user_id} dari {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Gagal mengekstrak tautan langsung melalui down_and_audio untuk pengguna {user_id} dari {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Audio dikirim dari cache."
    AUDIO_PROCESSING_MSG = "🎙️ Audio sedang diproses..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Mengunduh audio:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Kesalahan terjadi selama pengunduhan audio."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Gagal mengekstrak informasi audio"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Melewati tipe file yang tidak didukung dalam daftar putar pada indeks {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "File audio tidak ditemukan setelah pengunduhan."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Mengunggah file audio...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Gagal mengirim audio: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Audio daftar putar dikirim: {sent}/{total} file (kualitas={quality}) ke pengguna{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Gagal mengunduh audio: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Unduhan dibatalkan karena timeout (2 jam)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ File video tidak ditemukan: {filename}"
    VIDEO_PROCESSING_ERROR_MSG = "❌ Kesalahan memproses video: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Kesalahan mengirim file deskripsi: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 jika Anda ingin mengubah keterangan video - balas video dengan teks baru</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Tidak ada subtitle terdeteksi"
    VIDEO_PROGRESS_MSG = "<b>Video:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Audio:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ Batas URL terlampaui: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Pemrosesan selesai"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Rentang daftar putar tidak diizinkan dalam mode URL ganda. Kirim hanya URL tunggal tanpa rentang (*1*5, /vid 1-10, dll.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Periksa <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>di sini</a> jika situs Anda didukung"
    ERROR_COOKIE_NEEDED_MSG = "Anda mungkin memerlukan <code>cookie</code> untuk mengunduh video ini. Pertama, bersihkan ruang kerja Anda via perintah <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Untuk Youtube - dapatkan <code>cookie</code> via perintah <b>/cookie</b>. Untuk situs yang didukung lainnya - kirim cookie Anda sendiri (<a href='https://t.me/tg_ytdlp/203'>panduan1</a>) (<a href='https://t.me/tg_ytdlp/214'>panduan2</a>) dan setelah itu kirim tautan video Anda lagi."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Pilih bahasa subtitle"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Tidak ada bahasa audio alternatif"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Pilih bahasa audio"
    PAGE_NUMBER_MSG = "Halaman {page}"
    TOTAL_PROGRESS_MSG = "Total Progres"
    SUBTITLE_MENU_CLOSED_MSG = "Menu subtitle ditutup."
    SUBTITLE_LANGUAGE_SET_MSG = "Bahasa subtitle diatur: {value}"
    AUDIO_SET_MSG = "Audio diatur: {value}"
    FILTERS_UPDATED_MSG = "Filter diperbarui"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Kembali"
    CLOSE_BUTTON_TEXT = "🔚Tutup"
    LIST_BUTTON_TEXT = "📃Daftar"
    IMAGE_BUTTON_TEXT = "🖼Gambar"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Kualitas tidak terdeteksi otomatis\nGunakan tombol 'Lainnya' untuk melihat semua format yang tersedia.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Stream Langsung Terdeteksi**\n\nMengunduh stream langsung yang sedang berlangsung atau tak terbatas tidak diizinkan.\n\nHarap tunggu stream berakhir dan coba unduh lagi ketika:\n• Durasi stream diketahui\n• Stream telah selesai\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Unduhan Stream Langsung</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Potongan {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Ukuran maks: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Total durasi: {duration} detik"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Stream Langsung - Chunk {chunk}</b>\n⏱ Durasi: {duration} detik\n📦 Ukuran: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Potongan {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Unduhan Stream Langsung Selesai</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "Diunduh {chunks} potongan"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Total durasi: {duration} detik"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Unduhan Stream Langsung Dihentikan</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Direktori pengguna dihapus (mungkin oleh perintah /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "File chunk dihapus (mungkin oleh perintah /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Stream telah berakhir"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Silakan pilih format yang berbeda menggunakan perintah <code>/format</code>."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Tautan langsung diperoleh</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Judul:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Durasi:</b> {duration} detik\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Stream video:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Stream audio:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Kesalahan Pemrosesan File**\n\nVideo diunduh tetapi tidak dapat diproses karena karakter tidak valid dalam nama file.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Kesalahan Pemrosesan File**\n\nVideo diunduh tetapi tidak dapat diproses karena kesalahan argumen tidak valid.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Alasan:**\n"
        "• File yang diunduh bukan file video\n"
        "• Mungkin berupa dokumen (PDF, DOC, dll.) atau arsip\n\n"
        "**Solusi:**\n"
        "• Periksa tautan - mungkin mengarah ke dokumen, bukan video\n"
        "• Coba tautan atau sumber lain\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Alasan:**\n"
        "• File tidak dapat diproses sebagai video\n"
        "• Mungkin bukan file video atau file rusak\n\n"
        "**Solusi:**\n"
        "• Periksa tautan - mungkin mengarah ke dokumen, bukan video\n"
        "• Coba tautan atau sumber lain\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Format Tidak Tersedia**\n\nFormat video yang diminta tidak tersedia untuk video ini.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Format ID {format_id} tidak ditemukan untuk video ini.\n\nFormat ID yang tersedia: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **Format AV1 tidak tersedia untuk video ini.**\n\n**Format yang tersedia:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Kesalahan Pemrosesan File**\n\nAudio diunduh tetapi tidak dapat diproses karena karakter tidak valid dalam nama file.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Kesalahan Pemrosesan File**\n\nAudio diunduh tetapi tidak dapat diproses karena kesalahan argumen tidak valid.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Pengguna memasukkan konten terlarang. Tidak dapat diunduh."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "NSFW blur diatur melalui perintah: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Pengguna membuka menu /nsfw."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: ditutup."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Gagal mengunduh {service} cookie: status={status} (url disembunyikan)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Kesalahan mengunduh cookie {error}: {service}url tersembunyi)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Kesalahan tak terduga saat mengunduh cookie {service} (url tersembunyi): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "File cookie diperbarui untuk pengguna {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Konten cookie yang disediakan oleh pengguna tidak valid {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "URL cookie YouTube kosong untuk pengguna {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "Cookie YouTube diunduh dan divalidasi untuk pengguna {user_id} dari sumber {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Semua sumber cookie YouTube gagal untuk pengguna {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Kesalahan pada perintah check_porn oleh admin {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Pisahkan ukuran bagian yang disetel ke {size} byte."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Upload video selesai dengan pemisahan file."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Video playlist yang dikirim: {sent}/{total} file (kualitas={quality}) ke pengguna {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Kesalahan tidak diketahui: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Melewati jenis file yang tidak didukung dalam daftar putar di indeks {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg not found. Please install FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Konversi ke MP4 gagal: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Embedding subtitles may take a long time (up to 1 min per 1 min of video)!\n🔥 Starting to burn subtitles..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Subtitle tidak dapat disematkan karena batasan (kualitas/durasi/ukuran)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Subtitle tidak tersedia untuk bahasa yang dipilih"
    ERROR_SENDING_VIDEO_MSG = "❌ Kesalahan saat mengirim video: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Video playlist yang dikirimkan: {sent}/{total} file."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Pengunduhan dibatalkan karena waktu habis (2 jam)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Failed to download video: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Kesalahan: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON harus berupa objek (kamus)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Format JSON tidak valid. Harap berikan JSON yang valid."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Nilai harus antara {min_val} dan {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} disetel ke: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Benar"
    ARGS_FALSE_BUTTON_MSG = "❌ Salah"
    ARGS_BACK_BUTTON_MSG = "🔙 Back"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Tutup"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Benar"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Salah"
    ARGS_NOT_SET_MSG = "Tidak diatur"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ AV1 format is not available for this video.\n\nAvailable formats:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Kesalahan saat mengunduh: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ Tidak ada video yang ditemukan dalam daftar putar di indeks {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Video Conversion Failed**\n\nThe video couldn't be converted to MP4 due to an invalid argument error.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Video Conversion Failed**\n\nThe video couldn't be converted to MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Gagal mendapatkan tautan streaming"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ Tidak ditemukan konten di indeks {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Kesalahan: Pesan asli tidak ditemukan."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Kesalahan: URL tidak ditemukan."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ URL ini tidak dapat disematkan."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} codec tidak tersedia untuk video ini"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} format tidak tersedia untuk video ini"
    
    # Always Ask Menu button texts
    AA_AVC_BUTTON_MSG = "✅AVC"
    AA_AVC_BUTTON_INACTIVE_MSG = "☑️ AVC"
    AA_AVC_BUTTON_UNAVAILABLE_MSG = "❌ AVC"
    AA_AV1_BUTTON_MSG = "✅ AV1"
    AA_AV1_BUTTON_INACTIVE_MSG = "☑️ AV1"
    AA_AV1_BUTTON_UNAVAILABLE_MSG = "❌ AV1"
    AA_VP9_BUTTON_MSG = "✅ Wakil Presiden9"
    AA_VP9_BUTTON_INACTIVE_MSG = "☑️ VP9"
    AA_VP9_BUTTON_UNAVAILABLE_MSG = "❌ VP9"
    AA_MP4_BUTTON_MSG = "✅MP4"
    AA_MP4_BUTTON_INACTIVE_MSG = "☑️ MP4"
    AA_MP4_BUTTON_UNAVAILABLE_MSG = "❌ MP4"
    AA_MKV_BUTTON_MSG = "✅ MKV"
    AA_MKV_BUTTON_INACTIVE_MSG = "☑️ MKV"
    AA_MKV_BUTTON_UNAVAILABLE_MSG = "❌ MKV"

    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood limit. Try later."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Periksa Kue"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ SEMUA (OTOMATIS)"
    PROXY_OFF_BUTTON_MSG = "❌ MATI"
    PROXY_CLOSE_BUTTON_MSG = "🔚Tutup"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Pilih Negara:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Hapus Pilihan Negara"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Negara yang dipilih: {country} (kode: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Proksi yang tersedia: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Bot akan mencoba HTTP terlebih dahulu, lalu SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Proksi diaktifkan secara otomatis untuk negara yang dipilih"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Pilihan negara dihapus"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Pilihan negara dihapus"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Negara yang dipilih: {negara}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Menggunakan negara dari file: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Negara yang tersedia dari file: {count}"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ AKTIF"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ MATI"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Tutup"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ AKTIF (Tanpa Buram)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ON (No Blur)"
    NSFW_OFF_BLUR_MSG = "✅ MATI (Blur)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ OFF (Blur)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Bersih"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Terjadi kesalahan saat memproses pesan balasan untuk pengguna {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Kesalahan saat mengirim siaran ke pengguna {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Log dari {bot_name}\nPengguna: {user_id}\nTotal log: {total}\nWaktu saat ini: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nTotal {path}: {count}\nWaktu saat ini: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Total Pengguna: {count}</i>\n20 Terakhir {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Cache porno dimuat ulang oleh admin {admin_id}. Domain: {domains}, Kata kunci: {keywords}, Situs: {sites}, DAFTAR PUTIH: {whitelist}, DAFTAR GREY: {greylist}, DAFTAR_BLACK: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Kesalahan saat mengirim pesan batas waktu: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Pilih bahasa</b>"
    LANG_CHANGED_MSG = "✅ Bahasa diubah menjadi {lang_name}"
    LANG_ERROR_MSG = "❌ Kesalahan saat mengubah bahasa"
    LANG_CLOSED_MSG = "Pemilihan bahasa ditutup"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "Panggilan balik [BROWSER]: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Menambahkan tombol pemantauan browser dengan URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "URL pemantauan browser tidak dikonfigurasi: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Keyboard setting updated!**\n\nNew setting: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Gagal menyembunyikan keyboard: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Menggunakan cookie YouTube yang berfungsi untuk ekstraksi tautan bagi pengguna {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Tidak ada cookie YouTube yang berfungsi untuk ekstraksi tautan bagi pengguna {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Menggunakan cookie YouTube yang ada untuk ekstraksi tautan bagi pengguna {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Cookie YouTube tidak ditemukan untuk ekstraksi tautan untuk pengguna {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "File cookie global disalin ke folder pengguna {user_id} untuk ekstraksi tautan"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Pengguna {user_id} meminta perintah mediainfo"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Pengguna {user_id} adalah admin: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Pengguna {user_id} ada di saluran: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Akses pengguna {user_id} ditolak - bukan admin dan bukan di saluran"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Akses pengguna {user_id} diberikan"
    MEDIAINFO_CALLBACK_MSG = "Panggilan balik [MEDIAINFO]: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Perintah ini hanya tersedia untuk administrator."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Pengunduhan selesai dengan dukungan token PO"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Batas banjir. Coba nanti."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ Kesalahan penyegaran token REST: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Kesalahan saat menutup sesi Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Kesalahan menginisialisasi struktur db dasar: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Tidak semua parameter disetel di config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL tidak disetel"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey tidak disetel untuk mendapatkan idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Kesalahan saat mengunduh Firebase dump: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Gagal mengunduh Firebase dump melalui REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Kesalahan dalam _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Error saat menjalankan auto reload_cache (percobaan {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Semua upaya percobaan ulang gagal"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Memulai pengunduhan dump Firebase di {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Ketergantungan tidak tersedia: permintaan atau Sesi"
    DB_DATABASE_EMPTY_MSG = "⚠️ Basis data kosong"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Kesalahan saat menutup pencatat: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Kesalahan saat pembersihan: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Kesalahan kloning: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Batas waktu klon habis"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Pengecualian klon: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Pembaruan dibatalkan oleh pengguna"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Repositori berhasil dikloning"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Cadangan dipindahkan ke _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Semua modul dimuat"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Pembersihan selesai saat keluar"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Received signal {signal}, shutting down gracefully..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Harap tunggu..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Mengunduh stream HLS:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "menunggu fragmen"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Cadangan {ts} tidak ditemukan di _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Gagal memulihkan {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Dipulihkan: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Details:</b> {error_details}\n\nDownload stopped due to critical error.\n\n💡 <b>Tip:</b> If you're getting 401 Unauthorized error, try using <code>/cookie instagram</code> command or send your own cookies to authenticate with Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domain dalam daftar hitam porno: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Ditemukan kata kunci porno: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domain dalam daftar putih: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Menemukan kata kunci daftar putih: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Tidak ditemukan kata kunci porno"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Kesalahan API TikTok pada indeks {index}, melompat ke audio berikutnya..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Kesalahan API TikTok pada indeks {index}, melompat ke video berikutnya..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "User entered a <b>url</b>\n <b>user's name:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>User entered like this:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Bergabung dengan Saluran"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Pengendali pendaftaran: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Unduh 5 cookies saya"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Dapatkan cookie YT browser"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Validasi file cookie Anda"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Unggah cookie kustom"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Tutup"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Format yang tersedia untuk: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Tutup"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Tutup"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Tutup"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Tutup"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Bantuan ditutup."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Ditutup"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Terjadi kesalahan"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg not found in PATH or project directory. Please install FFmpeg."
    YTDLP_NOT_FOUND_MSG = "Biner yt-dlp tidak ditemukan di PATH atau direktori proyek. Silakan instal yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Video akan dibagi menjadi {rounds} bagian, yang mungkin berlebihan"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Membagi bagian video {current}/{total}: {start_time:.2f}s hingga {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Gagal membuat bagian split {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Berhasil membuat bagian split {part}: {target_name} ({size} bytes)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Error membagi bagian video {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Video berhasil dibagi menjadi {count} bagian"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Error dalam proses pembagian video: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Error saat memproses video {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "File video tidak ada: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Error memparsing dimensi '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Tidak dapat menentukan dimensi video dari '{size_result}', menggunakan default: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Error membuat thumbnail: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Error memparsing durasi video: {error}, hasilnya: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Thumbnail tidak dibuat di {thumb_dir}, menggunakan default"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Error eksekusi perintah: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Error membuat thumbnail dengan FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Melewati bagian konfigurasi non-dict: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Mengatur {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Menggunakan cookie pengguna: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Menggunakan cookie YouTube untuk pengguna {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "File cookie global disalin ke folder pengguna {user_id}"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Menggunakan cookie global yang disalin sebagai cookie pengguna: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Gagal menyalin file cookie global untuk pengguna {user_id}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Menggunakan --no-cookies untuk domain: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy diminta tetapi gagal mengimpor/mendapatkan konfigurasi: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Memaksa menggunakan proxy untuk gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy diminta tetapi konfigurasi proxy tidak lengkap"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Helper proxy gagal: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Mengurai item ekstraktor..."
    GALLERY_DL_ITEM_COUNT_MSG = "Barang {item}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Metadata ditemukan (tag 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL ditemukan (tag 3): {url}, metadata: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Metadata ditemukan (legacy): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL ditemukan (legacy): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Nama file ditemukan: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Direktori ditemukan: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Ekstensi ditemukan: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Mengurai {count} item, info: {info}, fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Mengatur konfigurasi gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Mencoba Strategi A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "Modul gallery_dl.extractor tidak ditemukan"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() tidak tersedia dalam build ini"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Memanggil extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Tidak ada ekstraktor yang cocok dengan URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Mengatur cookie pada ekstraktor: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Gagal mengatur cookie pada ekstraktor: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Ekstraktor ditemukan, memanggil items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Strategi A berhasil, mendapat info: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Strategi A: extractor.items() tidak mengembalikan info yang valid"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Strategi A (extractor.find) gagal: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Metadata fallback dari --get-urls: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Semua strategi gagal memperoleh metadata"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Gagal mengekstrak info gambar: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "Modul gallery_dl.job tidak ditemukan (instalasi rusak?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob tidak tersedia dalam build ini"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Mencari file yang diunduh di direktori gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Mencoba menemukan file berdasarkan nama dari ekstraktor"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Error membaca argumen pengguna untuk {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Error saat memproses video{video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Pengguna {user_id} memiliki send_as_file diaktifkan, mengirim sebagai dokumen"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video timeout berulang kali; kembali ke send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Keterangan terlalu panjang, mencoba dengan keterangan minimal"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (keterangan minimal) timeout; kembali ke send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Error mengirim video dengan keterangan minimal: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Error mengirim file deskripsi lengkap: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Error menghapus file deskripsi sementara: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Melewatkan match_filter untuk domain di NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Memeriksa cookie YouTube yang ada pada URL pengguna untuk deteksi format untuk pengguna {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Cookie YouTube yang ada bekerja pada URL pengguna untuk deteksi format untuk pengguna {user_id} - menggunakan mereka"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Cookie YouTube yang ada gagal pada URL pengguna, mencoba mendapatkan yang baru untuk deteksi format untuk pengguna {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Mencoba sumber cookie YouTube {i} untuk deteksi format untuk pengguna {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "Cookie YouTube dari sumber {i} bekerja pada URL pengguna untuk deteksi format untuk pengguna {user_id} - disimpan ke folder pengguna"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "Cookie YouTube dari sumber {i} tidak bekerja pada URL pengguna untuk deteksi format untuk pengguna {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Gagal mengunduh cookie YouTube dari sumber {i} untuk deteksi format untuk pengguna {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Semua sumber cookie YouTube gagal untuk deteksi format untuk pengguna {user_id}, akan mencoba tanpa cookie"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Tidak ada sumber cookie YouTube yang dikonfigurasi untuk deteksi format untuk pengguna {user_id}, akan mencoba tanpa cookie"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Tidak ada cookie YouTube yang ditemukan untuk deteksi format untuk pengguna {user_id}, mencoba mendapatkan yang baru"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Menggunakan cookie YouTube untuk deteksi format untuk pengguna {user_id} (sudah divalidasi di menu Always Ask)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Tidak ada cookie YouTube yang ditemukan untuk deteksi format untuk pengguna {user_id}, mencoba memulihkan..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "File cookie global disalin ke folder pengguna {user_id} untuk deteksi format"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Gagal menyalin file cookie global untuk pengguna {user_id}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Menggunakan --no-cookies untuk domain di get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "Aplikasi belum diinisialisasi. Tidak dapat mengakses {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Keterangan:</b> <code>{caption}</code>\n<b>ID pengguna:</b> <code>{user_id}</code>\n<b>Nama depan pengguna:</b> <code>{users_name}</code>\n<b>ID file video:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Error di caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Error tak terduga di caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL Video</a>{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL hilang dalam konfigurasi"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin diinisialisasi"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken diperbarui"
    DB_LOG_FOR_USER_ADDED_MSG = "Log untuk pengguna ditambahkan"
    DB_DATABASE_CREATED_MSG = "db dibuat"
    DB_BOT_STARTED_MSG = "Bot dimulai"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY disimpan ke config.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Bagian playlist sudah di-cache: {path_parts}, dilewati"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: tidak ada cache ditemukan untuk varian URL/kualitas apa pun, mengembalikan dict kosong"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: hitungan cepat untuk rentang besar: {cached_count} video di-cache"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: tidak ada cache ditemukan untuk hash {url_hash}, kualitas {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: tidak ada cache ditemukan untuk varian URL apa pun, mengembalikan None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Akses ditolak. Hanya admin."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Memuat ulang cache Firebase otomatis diperbarui!\n\n📊 Status: {status}\n⏰ Jadwal: setiap {interval} jam dari 00:00\n🕒 Memuat ulang berikutnya: {next_exec} (dalam {delta_min} menit)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Memuat ulang cache Firebase otomatis dihentikan!\n\n📊 Status: ❌ DINONAKTIFKAN\n💡 Gunakan /auto_cache on untuk mengaktifkan kembali"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Argumen tidak valid. Gunakan /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Interval harus antara 1 dan 168 jam"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Gagal mengatur interval"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Interval memuat ulang cache Firebase otomatis diperbarui!\n\n📊 Status: ✅ DIAKTIFKAN\n⏰ Jadwal: setiap {interval} jam dari 00:00\n🕒 Memuat ulang berikutnya: {next_exec} (dalam {delta_min} menit)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Memuat ulang cache Firebase otomatis dimulai!\n\n📊 Status: ✅ DIAKTIFKAN\n⏰ Jadwal: setiap {interval} jam dari 00:00\n🕒 Memuat ulang berikutnya: {next_exec} (dalam {delta_min} menit)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Memuat ulang cache Firebase otomatis dihentikan!\n\n📊 Status: ❌ DINONAKTIFKAN\n💡 Gunakan /auto_cache on untuk mengaktifkan kembali"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Memuat ulang otomatis DIAKTIFKAN; berikutnya pada {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Memuat ulang otomatis DINONAKTIFKAN oleh admin."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Interval memuat ulang otomatis diatur ke {interval}h; berikutnya pada {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Memuat ulang otomatis dimulai; berikutnya pada {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Memuat ulang otomatis dihentikan oleh admin."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Cache Firebase dimuat: {count} node root"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ File cache Firebase tidak ditemukan, memulai dengan cache kosong: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Gagal memuat cache firebase: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Cache Firebase dimuat ulang: {count} node root"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ File cache Firebase tidak ditemukan: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Gagal memuat ulang cache firebase: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 Anda dilarang menggunakan bot! Untuk membatalkan larangan, hubungi {Config.ADMIN_USERNAME}\n<blockquote>P.S. Jangan tinggalkan channel - Anda akan otomatis dilarang ⛔️</blockquote>\n🌍Ubah bahasa /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Tidak ada format video ditemukan. Mencoba pengunduh gambar…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram telah membatasi pengiriman pesan.\n⏳ Harap tunggu: {time_str}\nUntuk memperbarui timer kirim URL lagi 2 kali."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Klik tombol untuk menyalin URL streaming, lalu tempel di aplikasi VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Klik tombol untuk menyalin URL streaming, lalu tempel di aplikasi VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Error mendapatkan tautan:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Error mengirim file format: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Gagal mendapatkan format:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Menganalisis... (tunggu 6 detik)"
    AA_PROCESSING_MSG = "🔎 Menganalisis..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{wrong} berisi karakter terlarang. Hanya huruf, angka dan _ yang diizinkan.\nHarap gunakan: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Bot memerlukan hak administrator untuk bekerja di grup. Harap jadikan bot sebagai admin grup ini."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Halo {first_name},\n \n<i>Bot ini🤖 dapat mengunduh video apa pun langsung ke telegram.😊 Untuk informasi lebih lanjut tekan <b>/help</b></i> 👈\n\n<blockquote>P.S. Mengunduh konten 🔞NSFW dan file dari ☁️Cloud Storage berbayar! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Jangan tinggalkan saluran - Anda akan dilarang menggunakan bot ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Tidak ada file untuk dihapus."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 Semua file berhasil dihapus!\n\nFile yang dihapus:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ TUNGGU SAMPAI UNDUHAN SEBELUMNYA SELESAI"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "Instance aplikasi adalah None di check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict adalah None, mengizinkan unduhan"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict adalah None, mengizinkan penyisipan subtitle"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: memeriksa batas - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: kunci info_dict: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Penyisipan subtitle dilewati: durasi {duration}s melebihi batas {max_duration}s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Penyisipan subtitle dilewati: ukuran {size_mb:.2f}MB melebihi batas {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Penyisipan subtitle dilewati: kualitas {width}x{height} (sisi min {min_side}p) melebihi batas {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "daftar putar"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Batas rentang terlampaui untuk {service}: {count} (maksimum {max_count}).\n\nGunakan salah satu perintah ini untuk mengunduh file maksimum yang tersedia:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Batas rentang terlampaui untuk {service}: {count} (maksimum {max_count})\nID pengguna: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "Penyedia token PO dinonaktifkan dalam konfigurasi"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} bukan domain YouTube, melewatkan token PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "Penyedia token PO tidak tersedia di {base_url}, kembali ke ekstraksi YouTube standar"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "Cache penyedia token PO dibersihkan, akan memeriksa ketersediaan pada permintaan berikutnya"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Instance aplikasi belum tersedia"
    HELPER_USER_NAME_MSG = "Pengguna"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood wait terdeteksi, menunggu {wait_seconds} detik"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood wait terdeteksi tetapi tidak dapat mengekstrak waktu, menunggu {retry_delay} detik"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "Error msg_seqno terdeteksi, menunggu {retry_delay} detik"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Konfigurasi proxy tidak lengkap, menggunakan koneksi langsung"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Tutup"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Tutup"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Tutup"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 File log dihapus."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 File tag dihapus."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 File format dihapus."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 File split dihapus."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 File mediainfo dihapus."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Pengaturan subtitle dihapus."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Pengaturan keyboard dihapus."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Pengaturan argumen dihapus."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 Pengaturan NSFW dihapus."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Pengaturan proxy dihapus."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Pengaturan flood wait dihapus."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Tutup"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Perintah Unduhan Video"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Penggunaan: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Contoh:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (urutan langsung)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (urutan terbalik)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Lihat juga: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Pengguna {user_id} menutup perintah add_bot_to_group"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Gagal mengekstrak ID YouTube"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Gagal mengunduh thumbnail atau terlalu besar"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Pilih bahasa audio"
    AA_NO_SUBTITLES_DETECTED_MSG = "Tidak ada subtitle terdeteksi"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Pilih bahasa subtitle"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Error Autentikasi"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Akun Tidak Ditemukan"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Akun Tidak Tersedia"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Batas Kecepatan Terlampaui"
    GALLERY_DL_NETWORK_ERROR_MSG = "Error Jaringan"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Konten Tidak Tersedia"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Pembatasan Geografis"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Verifikasi Diperlukan"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Pelanggaran Kebijakan"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Error Tidak Dikenal"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Unduhan dimulai</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Tutup"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Perintah Unduhan Video</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Penggunaan: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Contoh:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Lihat juga: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Batas flood. Coba lagi nanti."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Penggunaan Perintah Cookie</b>

<code>/cookie</code> - Tampilkan menu cookie
<code>/cookie youtube</code> - Unduh cookie YouTube
<code>/cookie instagram</code> - Unduh cookie Instagram
<code>/cookie tiktok</code> - Unduh cookie TikTok
<code>/cookie x</code> atau <code>/cookie twitter</code> - Unduh cookie Twitter/X
<code>/cookie facebook</code> - Unduh cookie Facebook
<code>/cookie custom</code> - Tampilkan instruksi cookie kustom

<i>Layanan yang tersedia bergantung pada konfigurasi bot.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 File cookie dihapus dan cache dibersihkan."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Sebelumnya"
    SUBS_BACK_BUTTON_MSG = "🔙Kembali"
    SUBS_OFF_BUTTON_MSG = "🚫 MATI"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs id</code> - atur bahasa"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs id auto</code> - atur bahasa dengan AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Opsi yang valid:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 BAHASA"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Pengembang GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Kontrol GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 BERSIHKAN"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 kue"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MEDIA"
    SETTINGS_INFO_BUTTON_MSG = "📖 INFORMASI"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ LEBIH"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Hanya cookies"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Log "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Tag"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Format"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Bagi"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Subtitle"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Papan ketik"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Argumen"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Proksi"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Tunggu flood"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Semua file"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Unduh 5 cookie saya"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Dapatkan cookie YT dari browser"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Validasi file cookie Anda"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Unggah cookie kustom"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Ubah kualitas & format"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Nyalakan / Matikan MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Ubah ukuran bagian video yang dibagi"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Unduh video sebagai audio"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Pengaturan bahasa subtitle"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Cara mengunduh daftar putar"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Unduh gambar via gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Kirim #tag Anda"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Dapatkan instruksi"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Kirim log Anda"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Bantuan daftar putar"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - cara"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Dapatkan tautan video langsung"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Aktifkan/nonaktifkan proxy"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Tata letak keyboard"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Pembantu pencarian inline"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - argumen yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - Pengaturan blur NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Opsi Pembersihan</b>\n\nPilih apa yang akan dibersihkan:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: Aktifkan pencarian @vid"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: Aktifkan pencarian @vid"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 MATI"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 PENUH"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL Gambar]({url})"
    IMAGE_ERROR_MSG = "❌ Kesalahan: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Kembali"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - format kustom"
    FORMAT_720P_MSG = "• <code>/format 720</code> - kualitas 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - kualitas 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - kualitas 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - ID format spesifik"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - selalu tampilkan menu"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/kualitas terbaik"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Selalu Tanya (menu + tombol)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Lainnya (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (terbaik untuk PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (terbaik untuk Telegram mobile)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (kualitas MAKS)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Kustom (masukkan sendiri)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Dari Browser"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Milik Anda"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Mode input ditutup otomatis karena tidak aktif (5 menit)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Reset Semua"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Lihat Saat Ini"
    ARGS_BACK_BUTTON_MSG = "🔙 Kembali"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Teruskan pesan ini ke favorit Anda untuk menyimpan pengaturan ini sebagai template.</i> \n\n<i>Teruskan pesan ini kembali ke sini untuk menerapkan pengaturan ini.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Argumen yt-dlp Saat Ini:\n\nTidak ada pengaturan kustom yang dikonfigurasi.\n\n---\n\n<i>Teruskan pesan ini ke favorit Anda untuk menyimpan pengaturan ini sebagai template.</i> \n\n<i>Teruskan pesan ini kembali ke sini untuk menerapkan pengaturan ini.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Argumen yt-dlp Saat Ini:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Ekspor Pengaturan"
    ARGS_SETTINGS_READY_MSG = "Pengaturan siap untuk diekspor! Teruskan pesan ini ke favorit untuk menyimpan."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Argumen yt-dlp Saat Ini:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Gagal mengenali pengaturan dalam pesan. Pastikan Anda mengirim template pengaturan yang benar."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Pengaturan berhasil diimpor!\n\nParameter yang diterapkan: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Pengaturan kunci:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Error menyimpan pengaturan yang diimpor."
    ARGS_ERROR_IMPORTING_MSG = "❌ Terjadi error saat mengimpor pengaturan."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Unduh File Cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Pilih layanan untuk mengunduh file cookie."
    COOKIE_MENU_SAVE_INFO_MSG = "File cookie akan disimpan sebagai cookie.txt di folder Anda."
    COOKIE_MENU_TIP_HEADER_MSG = "Tip: Anda juga dapat menggunakan perintah langsung:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – unduh dan validasi cookie"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – gunakan sumber spesifik berdasarkan indeks (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Kemudian verifikasi dengan <code>/check_cookie</code> (tes di RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Selalu Tanya"
    SUBS_AUTO_TRANS_BUTTON_MSG = "OTOMATIS/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Tautan"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Tonton"  # SEMENTARA DINONAKTIFKAN: layanan poketube sedang down
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Deskripsi"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ POTONG"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Potong Video</b>\n\nDurasi video: <b>{start_time} - {end_time}</b>\n\nSilakan kirim rentang waktu yang diinginkan dalam format:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nContoh: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Format tidak valid. Silakan gunakan: <code>HH:MM:SS-HH:MM:SS</code>\n\nContoh: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Rentang tidak valid. Waktu mulai harus kurang dari waktu akhir."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ Rentang waktu berada di luar batas video.\n\nDurasi video: <b>{start_time} - {end_time}</b>\n\nRentang Anda harus berada dalam batas ini."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>Video akan dipotong:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Selesai sebagian - {successful_uploads}/{total_files} file audio diunggah."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Audio berhasil diunduh dan dikirim - {total_files} file diunggah."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Akun TikTok Pribadi</b>\n\n"
        "Akun TikTok ini bersifat pribadi atau semua videonya pribadi.\n\n"
        "<b>💡 Solusi:</b>\n"
        "1. Ikuti akun @{username}\n"
        "2. Kirim cookie Anda ke bot menggunakan perintah <code>/cookie</code>\n"
        "3. Coba lagi\n\n"
        "<b>Setelah memperbarui cookie, coba lagi!</b>"
    )

    #######################################################
