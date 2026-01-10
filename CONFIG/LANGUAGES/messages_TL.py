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
    CREDITS_MSG = "<blockquote><i>Pinamamahalaan ni</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Baguhin ang wika: /lang</b>"
    TO_USE_MSG = "<i>Upang magamit ang bot na ito, kailangan mong mag-subscribe sa @tg_ytdlp Telegram channel.</i>\nPagkatapos mong sumali sa channel, <b>ipadala ulit ang iyong video link at i-download ito ng bot para sa iyo</b> ❤️\n\n<blockquote>P.S. Ang pag-download ng 🔞NSFW content at mga file mula sa ☁️Cloud Storage ay may bayad! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Huwag umalis sa channel - mababan ka sa paggamit ng bot ⛔️</blockquote>"

    ERROR1 = "Hindi nahanap ang url link. Mangyaring maglagay ng url na may <b>https://</b> o <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Mga Playlist (yt-dlp)</b>

Upang mag-download ng mga playlist, ipadala ang URL nito na may <code>*start*end</code> na mga range sa dulo. Halimbawa: <code>URL*1*5</code> (unang 5 na video mula 1 hanggang 5 kasama).<code>URL*-1*-5</code> (huling 5 na video mula 1 hanggang 5 kasama).
O maaari mong gamitin ang <code>/vid FROM-TO URL</code>. Halimbawa: <code>/vid 3-7 URL</code> (nagda-download ng mga video mula 3 hanggang 7 kasama mula sa simula). <code>/vid -3-7 URL</code> (nagda-download ng mga video mula 3 hanggang 7 kasama mula sa dulo). Gumagana din para sa <code>/audio</code> command.

<b>Mga Halimbawa:</b>

🟥 <b>Video range mula sa YouTube playlist:</b> (kailangan ng 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(nagda-download ng unang 5 na video mula 1 hanggang 5 kasama)
🟥 <b>Isang video mula sa YouTube playlist:</b> (kailangan ng 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(nagda-download lamang ng ika-3 na video)

⬛️ <b>TikTok profile:</b> (kailangan ang iyong 🍪)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(nagda-download ng unang 10 na video mula sa user profile)

🟪 <b>Instagram stories:</b> (kailangan ang iyong 🍪)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(nagda-download ng unang 3 na stories)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(nagda-download ng unang 10 na stories mula sa album)

🟦 <b>VK videos:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(nagda-download ng unang 3 na video mula sa user/group profile)

⬛️<b>Rutube channels:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(nagda-download ng mga video mula 2 hanggang 4 kasama mula sa channel)

🟪 <b>Twitch clips:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(nagda-download ng unang 3 na clips mula sa channel)

🟦 <b>Vimeo groups:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(nagda-download ng unang 2 na video mula sa group)

🟧 <b>Pornhub models:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(nagda-download ng unang 2 na video mula sa model profile)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(nagda-download ng unang 3 na video mula sa search results ayon sa iyong prompt)

at iba pa...
tingnan ang <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">listahan ng suportadong sites</a>
</blockquote>

<blockquote expandable>🖼 <b>Mga Larawan (gallery-dl)</b>

Gamitin ang <code>/img URL</code> upang mag-download ng mga larawan/photo/album mula sa maraming platform.

<b>Mga Halimbawa:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Mga Range:</b>
<code>/img 11-20 https://example.com/album</code> — mga item 11..20
<code>/img 11- https://example.com/album</code> — mula 11 hanggang dulo (o bot limit)

<i>Kabilang sa mga suportadong platform ang vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, atbp. Buong listahan:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">gallery-dl suportadong sites</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Video Download Bot - Tulong</b>

📥 <b>Pangunahing Paggamit:</b>
• Magpadala ng anumang link → i-download ito ng bot
  <i>ang bot ay awtomatikong sinusubukang mag-download ng mga video sa pamamagitan ng yt-dlp at mga larawan sa pamamagitan ng gallery-dl.</i>
• <b>Maraming URL:</b> Sa quality selection mode (<code>/format</code>) maaari kang magpadala ng hanggang <b>10 URL</b> sa isang mensahe. Bawat URL sa isang bagong linya o pinaghihiwalay ng mga puwang.
• <code>/audio URL</code> → kunin ang audio
• <code>/link [quality] URL</code> → kumuha ng direktang link
• <code>/proxy</code> → paganahin/huwag paganahin ang proxy para sa lahat ng download
• Tumugon sa video gamit ang text → baguhin ang caption

📋 <b>Mga Playlist at Range:</b>
• <code>URL*1*5</code> → i-download ang unang 5 na video
• <code>URL*-1*-5</code> → i-download ang huling 5 na video
• <code>/vid 3-7 URL</code> → nagiging <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → nagiging <code>URL*-3*-7</code>

🍪 <b>Mga Cookie at Private:</b>
• Mag-upload ng *.txt cookie para sa mga pribadong video
• <code>/cookie [service]</code> → i-download ang mga cookie (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → pumili ng source ayon sa index (1–N)
• <code>/cookies_from_browser</code> → kunin mula sa browser
• <code>/check_cookie</code> → i-verify ang cookie
• <code>/save_as_cookie</code> → i-save ang text bilang cookie

🧹 <b>Paglinis:</b>
• <code>/clean</code> → media files lamang
• <code>/clean all</code> → lahat
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Mga Setting:</b>
• <code>/settings</code> → settings menu
• <code>/format</code> → quality at format
• <code>/split</code> → hatiin ang video sa mga bahagi
• <code>/mediainfo on/off</code> → media info
• <code>/nsfw on/off</code> → NSFW blur
• <code>/tags</code> → tingnan ang naka-save na tags
• <code>/sub on/off</code> → subtitles
• <code>/keyboard</code> → keyboard (OFF/1x3/2x3)

🏷️ <b>Mga Tag:</b>
• Magdagdag ng <code>#tag1#tag2</code> pagkatapos ng URL
• Lumilitaw ang mga tag sa captions
• <code>/tags</code> → tingnan ang lahat ng tags

🔗 <b>Direktang Link:</b>
• <code>/link URL</code> → pinakamahusay na quality
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → tiyak na quality

⚙️ <b>Mabilis na Command:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → itakda ang quality
• <code>/keyboard off/1x3/2x3/full</code> → keyboard layout
• <code>/split 100mb-2000mb</code> → baguhin ang part size
• <code>/subs off/ru/en auto</code> → subtitle language
• <code>/list URL</code> → listahan ng available na format
• <code>/mediainfo on/off</code> → on/off media info
• <code>/proxy on/off</code> → paganahin/huwag paganahin ang proxy para sa lahat ng download

📊 <b>Impormasyon:</b>
• <code>/usage</code> → download history
• <code>/search</code> → inline search sa pamamagitan ng @vid

🖼 <b>Mga Larawan:</b>
• <code>URL</code> → i-download ang images URL
• <code>/img URL</code> → i-download ang mga larawan mula sa URL
• <code>/img 11-20 URL</code> → i-download ang tiyak na range
• <code>/img 11- URL</code> → i-download mula sa ika-11 hanggang dulo

👨‍💻 <i>Developer:</i> @upekshaip
🤝 <i>Contributor:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "I-save lamang ang iyong cookie bilang <b><u>cookie.txt</u></b> at ipadala ito sa bot bilang isang dokumento.\n\n"
        "Maaari mo ring ipadala ang mga cookie bilang plain text gamit ang command na <b><u>/save_as_cookie</u></b>.\n"
        "<b>Paggamit ng <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>Mga Tagubilin:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message
    SEARCH_MSG = """
🔍 <b>Paghahanap ng Video</b>

Pindutin ang button sa ibaba upang i-activate ang inline search sa pamamagitan ng @vid.

<blockquote>Sa PC, i-type lamang ang <b>"@vid Your_Search_Query"</b> sa anumang chat.</blockquote>
    """
    
    # Settings and Hints
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Command sa Pag-download ng Larawan</b>\n\n"
        "Paggamit: <code>/img URL</code>\n\n"
        "<b>Mga Halimbawa:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Mga suportadong platform (mga halimbawa):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, atbp. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">buong listahan</a></blockquote>"
        "Tingnan din: "
    )
    
    LINK_HINT_MSG = (
        "Kumuha ng direktang video links na may quality selection.\n\n"
        "Paggamit: /link + URL \n\n"
        "(hal. /link https://youtu.be/abc123)\n"
        "(hal. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Magdagdag ng Bot sa Grupo</b>

Magdagdag ng aking mga bot sa inyong mga grupo upang makakuha ng mas mahusay na features at mas mataas na limits!
————————————
📊 <b>Kasalukuyang LIBRENG Limits (sa Bot's DM):</b>
<blockquote>•🗑 Magulong basura mula sa lahat ng files na hindi naka-sort 👎
• Max 1 file size: <b>8 GB </b>
• Max 1 file quality: <b>WALANG LIMIT</b>
• Max 1 file duration: <b>WALANG LIMIT</b>
• Max number ng downloads: <b>WALANG LIMIT</b>
• Max URLs sa isang mensahe: <b>10</b> (lamang sa quality selection mode)
• Max playlist items bawat 1 beses: <b>50</b>
• Max TikTok videos bawat 1 beses: <b>500</b>
• Max images bawat 1 beses: <b>1000</b>
• URL rate limits: <b>5/min, 60/hour, 1000/day</b>
• Command limit: <b>20/min</b>
• 1 Download max time: <b>2 oras</b>
• 🔞 NSFW content ay may bayad! 1⭐️ = $0.02
• 🆓 LAHAT NG IBA PANG MEDIA AY TOTALLY LIBRE
• 📝 Lahat ng content logs & caching sa aking log-channels para sa instant repost kapag muling nag-download</blockquote>

💬<b>Ang limits na ito ay para lamang sa video na may subtitles:</b>
<blockquote>• Max video+subs duration: <b>1.5 oras</b>
• Max video+subs file size: <b>500 MB</b>
• Max video+subs quality: <b>720p</b></blockquote>
————————————
🚀 <b>Mga Benepisyo ng Bayad na Grupo (2️⃣x Limits):</b>
<blockquote>•  🗂 Maayos na structured media vault na naka-sort ayon sa topics 👍
•  📁 Ang mga bot ay tumutugon sa topic kung saan mo sila tinawag
•  📌 Auto pin status message na may download progress
•  🖼 Ang /img command ay nagda-download ng media bilang 10-item albums
• Max 1 file size: <b>16 GB</b> ⬆️
• Max URLs sa isang mensahe: <b>20</b> ⬆️ (lamang sa quality selection mode)
• Max playlist items bawat 1 beses: <b>100</b> ⬆️
• Max TikTok videos bawat 1 beses: 1000 ⬆️
• Max images bawat 1 beses: 2000 ⬆️
• URL rate limits: <b>10/min, 120/hour, 2000/day</b> ⬆️
• Command limit: <b>40/min</b> ⬆️
• 1 Download max time: <b>4 oras</b> ⬆️
• 🔞 NSFW content: Libre na may full metadata 🆓
• 📢 Hindi na kailangan mag-subscribe sa aking channel para sa mga grupo
• 👥 Lahat ng miyembro ng grupo ay magkakaroon ng access sa paid functions!
• 🗒 Walang logs / walang cache sa aking log-channels! Maaari mong tanggihan ang copy/repost sa group settings</blockquote>

💬 <b>2️⃣x limits para sa video na may subtitles:</b>
<blockquote>• Max video+subs duration: <b>3 oras</b> ⬆️
• Max video+subs file size: <b>1000 MB</b> ⬆️
• Max video+subs quality: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Presyo at Setup:</b>
<blockquote>• Presyo: <b>$5/buwan</b> bawat 1 bot sa grupo
• Setup: Makipag-ugnayan sa @iilililiiillliiliililliilliliiil
• Pagbabayad: 💎TON o iba pang paraan💲
• Suporta: Kasama ang full technical support</blockquote>
————————————
Maaari mong idagdag ang aking mga bot sa inyong grupo upang i-unblock ang libreng 🔞<b>NSFW</b> at i-double (x2️⃣) ang lahat ng limits.
Makipag-ugnayan sa akin kung nais mong payagan ko ang inyong grupo na gamitin ang aking mga bot @iilililiiillliiliililliilliliiil
————————————
💡<b>TIP:</b> <blockquote>Maaari kayong mag-ambag ng pera kasama ang anumang dami ng inyong mga kaibigan (halimbawa 100 tao) at gumawa ng 1 purchase para sa buong grupo - LAHAT NG MIYEMBRO NG GRUPO AY MAGKAKAROON NG FULL UNLIMITED ACCESS sa lahat ng bot functions sa grupo na iyon para lamang sa <b>$0.05</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW Mode: ON✅</b>

• Ang NSFW content ay ipapakita nang walang blurring.
• Ang mga spoiler ay hindi ilalapat sa NSFW media.
• Ang content ay makikita agad

<i>Gamitin ang /nsfw off upang i-enable ang blur</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW Mode: OFF</b>

⚠️ <b>Naka-enable ang Blur</b>
• Ang NSFW content ay itatago sa ilalim ng spoiler   
• Upang makita, kailangan mong i-click ang media
• Ang mga spoiler ay ilalapat sa NSFW media.

<i>Gamitin ang /nsfw on upang i-disable ang blur</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Hindi wasto ang parameter</b>

Gamitin:
• <code>/nsfw on</code> - i-disable ang blur
• <code>/nsfw off</code> - i-enable ang blur
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Sinusuri ang cache...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Pinoproseso..."
    DOWNLOADING_MSG = "📥 <b>Nagda-download ng media...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Nagda-download ng larawan...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Tapos na ang download</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Na-download:"
    SENT_STATUS_MSG = "Naipadala:"
    PENDING_TO_SEND_STATUS_MSG = "Naghihintay na ipadala:"
    TITLE_LABEL_MSG = "Pamagat:"
    MEDIA_COUNT_LABEL_MSG = "Bilang ng media:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Tapos na ang download, pinoproseso ang audio..."
    VIDEO_PROCESSING_MSG = "📽 Pinoproseso ang video..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Naipadala mula sa cache</b>\n\nNaipadalang albums: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Matagumpay na naipadala ang video mula sa cache."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Naipadala ang mga video ng playlist mula sa cache ({cached}/{total} files)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} videos naipadala mula sa cache, nagda-download ng mga nawawala..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Naipadala mula sa cache: {cached}\n🔄 Nagpapatuloy ang download..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Hindi ma-analyze ang media, nagpapatuloy sa maximum na pinapayagang range (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Hindi matukoy ang bilang ng media, nagpapatuloy sa maximum na pinapayagang range (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Hindi matukoy ang kabuuang bilang ng media, nagpapatuloy sa tinukoy na range {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>Hindi wasto ang URL</b>\n\nMangyaring magbigay ng wastong URL na nagsisimula sa http:// o https://"

    ERROR_OCCURRED_MSG = "❌ <b>May naganap na error</b>\n\n<code>{url}</code>\n\nError: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Error sa pagpapadala ng video: {error}"
    ERROR_UNKNOWN_MSG = "❌ Hindi kilalang error: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Walang sapat na disk space upang mag-download ng mga video."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Ang file size ay lumampas sa limit na {limit} GB. Mangyaring pumili ng mas maliit na file sa loob ng pinapayagang size."

    ERROR_GETTING_LINK_MSG = "❌ <b>Error sa pagkuha ng link:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Nilimitahan ng Telegram ang pagpapadala ng mensahe.\n⏳ Mangyaring maghintay: {time}\nUpang i-update ang timer, ipadala ulit ang URL ng 2 beses."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Nilimitahan ng Telegram ang pagpapadala ng mensahe.\n⏳ Mangyaring maghintay: \nUpang i-update ang timer, ipadala ulit ang URL ng 2 beses."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Nabigo sa pag-download ng subtitles"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Direktang Stream Links</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Pamagat:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Tagal:</b> {duration} sec\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Error: Hindi nahanap ang orihinal na mensahe."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Ang Tag #{tag} ay naglalaman ng mga ipinagbabawal na character. Tanging mga titik, numero at _ lamang ang pinapayagan.\nMangyaring gamitin: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Naipadala ang mga video ng playlist: {sent}/{total} files."
    PLAYLIST_CACHE_SENT_MSG = "✅ Naipadala mula sa cache: {cached}/{total} files."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Nabigo sa pagkuha ng stream links"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Pumili ng browser para mag-download ng cookies:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Walang nahanap na browser sa sistemang ito. Maaari kang mag-download ng cookies mula sa remote URL o subaybayan ang status ng browser:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Buksan ang Browser</b> - upang subaybayan ang status ng browser sa mini-app"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Buksan ang Browser"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Mag-download mula sa Remote URL"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Na-download ang YouTube cookie file sa pamamagitan ng fallback at na-save bilang cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Walang nahanap na suportadong browser at walang naka-configure na COOKIE_URL. Gamitin ang /cookie o mag-upload ng cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Ang fallback COOKIE_URL ay dapat tumuro sa isang .txt file."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Masyadong malaki ang fallback cookie file (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Hindi available ang fallback cookie source (status {status}). Subukan ang /cookie o mag-upload ng cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Error sa pag-download ng fallback cookie. Subukan ang /cookie o mag-upload ng cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Hindi malamang error habang nagda-download ng fallback cookie."
    BTN_CLOSE = "🔚Isara"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Di-wastong boolean value"
    ARGS_CLOSED_MSG = "Nakasara"
    ARGS_ALL_RESET_MSG = "✅ Na-reset ang lahat ng arguments"
    ARGS_RESET_ERROR_MSG = "❌ Error sa pag-reset ng arguments"
    ARGS_INVALID_PARAM_MSG = "❌ Hindi wasto ang parameter"
    ARGS_BOOL_SET_MSG = "Nakatakda sa {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "Nakatakda na sa {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Hindi wasto ang napiling value"
    ARGS_VALUE_SET_MSG = "Nakatakda sa {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "Nakatakda na sa {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Kasalukuyang value:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Mga Halimbawa:</b>\n• <code>default</code> - Gamitin ang default XFF strategy\n• <code>never</code> - Huwag kailanman gamitin ang XFF header\n• <code>US</code> - United States country code\n• <code>GB</code> - United Kingdom country code\n• <code>DE</code> - Germany country code\n• <code>FR</code> - France country code\n• <code>JP</code> - Japan country code\n• <code>192.168.1.0/24</code> - IP block (CIDR)\n• <code>10.0.0.0/8</code> - Private IP range\n• <code>203.0.113.0/24</code> - Public IP block\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Tandaan:</b> Pinapalitan nito ang --geo-bypass options. Gamitin ang anumang 2-letter country code o IP block sa CIDR notation.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Halimbawa:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Mangyaring ipadala ang iyong bagong value."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Saklaw:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Mangyaring ipadala ang isang numero."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Mga Halimbawa:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Tandaan:</b> Ang mga headers na ito ay idaragdag sa umiiral na Referer at User-Agent headers.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Kasalukuyang yt-dlp Arguments:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - True/False switches\n• 📋 <b>Select</b> - Pumili mula sa options\n• 🔢 <b>Numeric</b> - Number input\n• 📝🔧 <b>Text</b> - Text/JSON input</blockquote>\n\nAng mga setting na ito ay ilalapat sa lahat ng inyong downloads."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "Pilitin ang IPv6 connections",
        "force_ipv4": "Pilitin ang IPv4 connections", 
        "no_live_from_start": "Huwag mag-download ng live streams mula sa simula",
        "live_from_start": "Mag-download ng live streams mula sa simula",
        "no_check_certificates": "Pigilan ang HTTPS certificate validation",
        "check_certificate": "Tingnan ang SSL certificate",
        "no_playlist": "Mag-download lamang ng isang video, hindi playlist",
        "embed_metadata": "I-embed ang metadata sa video file",
        "embed_thumbnail": "I-embed ang thumbnail sa video file",
        "write_thumbnail": "Isulat ang thumbnail sa file",
        "ignore_errors": "Balewalain ang download errors at magpatuloy",
        "legacy_server_connect": "Payagan ang legacy server connections",
        "concurrent_fragments": "Bilang ng concurrent fragments na i-download",
        "xff": "X-Forwarded-For header strategy",
        "user_agent": "User-Agent header",
        "impersonate": "Browser impersonation",
        "referer": "Referer header",
        "geo_bypass": "Bypass geographic restrictions",
        "hls_use_mpegts": "Gamitin ang MPEG-TS para sa HLS",
        "no_part": "Huwag gamitin ang .part files",
        "no_continue": "Huwag ipagpatuloy ang partial downloads",
        "audio_format": "Audio format",
        "video_format": "Video format",
        "merge_output_format": "Merge output format",
        "send_as_file": "Ipadala bilang file",
        "username": "Username",
        "password": "Password",
        "twofactor": "Two-factor authentication code",
        "min_filesize": "Minimum file size (MB)",
        "max_filesize": "Maximum file size (MB)",
        "playlist_items": "Playlist items",
        "date": "Petsa",
        "datebefore": "Petsa bago",
        "dateafter": "Petsa pagkatapos",
        "http_headers": "HTTP headers",
        "sleep_interval": "Sleep interval",
        "max_sleep_interval": "Maximum sleep interval",
        "retries": "Bilang ng retries",
        "http_chunk_size": "HTTP chunk size",
        "sleep_subtitles": "Sleep para sa subtitles"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ Configuration ng yt-dlp Arguments</b>\n\n<blockquote>📋 <b>Mga Grupo:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ Configuration ng yt-dlp Arguments</b>\n\n"
        "<blockquote>📋 <b>Mga Grupo:</b>\n"
        "• ✅/❌ <b>Boolean</b> - True/False switches\n"
        "• 📋 <b>Select</b> - Pumili mula sa options\n"
        "• 🔢 <b>Numeric</b> - Number input\n"
        "• 📝🔧 <b>Text</b> - Text/JSON input</blockquote>\n\n"
        "Ang mga setting na ito ay ilalapat sa lahat ng inyong downloads."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Mangyaring maghintay..."
    ERROR_OCCURRED_SHORT_MSG = "❌ May naganap na error"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Awtomatikong nagsara ang input mode dahil sa kawalan ng aktibidad (5 minuto)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Ang input ay naglalaman ng potensyal na mapanganib na content: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Masyadong mahaba ang input (max 1000 characters)"
    ARGS_INVALID_URL_MSG = "❌ Hindi wasto ang URL format. Dapat magsimula sa http:// o https://"
    ARGS_INVALID_JSON_MSG = "❌ Hindi wasto ang JSON format"
    ARGS_NUMBER_RANGE_MSG = "❌ Ang numero ay dapat nasa pagitan ng {min_val} at {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Hindi wasto ang number format"
    ARGS_DATE_FORMAT_MSG = "❌ Ang petsa ay dapat nasa YYYYMMDD format (hal., 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Ang taon ay dapat nasa pagitan ng 1900 at 2100"
    ARGS_MONTH_RANGE_MSG = "❌ Ang buwan ay dapat nasa pagitan ng 01 at 12"
    ARGS_DAY_RANGE_MSG = "❌ Ang araw ay dapat nasa pagitan ng 01 at 31"
    ARGS_INVALID_DATE_MSG = "❌ Hindi wasto ang date format"
    ARGS_INVALID_XFF_MSG = "❌ Ang XFF ay dapat 'default', 'never', country code (hal., US), o IP block (hal., 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "Walang nakatakdang custom arguments. Lahat ng parameters ay gumagamit ng default values."
    ARGS_RESET_SUCCESS_MSG = "✅ Na-reset ang lahat ng arguments sa defaults."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Masyadong mahaba ang text. Maximum 500 characters."
    ARGS_ERROR_PROCESSING_MSG = "❌ Error sa pagproseso ng input. Pakisubukang muli."
    ARGS_BOOL_INPUT_MSG = "❌ Pakilagay ang 'True' o 'False' para sa opsyon na Ipadala Bilang File."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Mangyaring magbigay ng wastong numero."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Mangyaring ipadala ang <code>True</code> o <code>False</code> upang paganahin/i-disable ang opsyong ito."
    ARGS_JSON_VALUE_REQUEST_MSG = "Mangyaring magpadala ng wastong JSON."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Wala ka pang tag."
    TAGS_MESSAGE_CLOSED_MSG = "Nakasara ang tags message."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Naka-disable ang mga subtitle at naka-off ang Always Ask mode."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ Naka-enable ang SUBS Always Ask."
    SUBS_LANGUAGE_SET_MSG = "✅ Itinakda ang wika ng subtitle sa: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️WARNING: due to high CPU impact this function is very slow (near real-time) and limited to:\n"
        "- 720p max quality\n"
        "- 1.5 hour max duration\n"
        "- 500mb max video size</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Mabilisang mga utos:</b>\n"
        "• <code>/subs off</code> - i-disable ang subtitles\n"
        "• <code>/subs on</code> - i-enable ang Always Ask mode\n"
        "• <code>/subs ru</code> - itakda ang wika\n"
        "• <code>/subs ru auto</code> - itakda ang wika gamit ang AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Naka-disable ang Subtitles"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Napiling wika: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Nagda-download ng subtitles..."
    SUBS_DISABLED_ERROR_MSG = "❌ Naka-disable ang subtitles. Gamitin ang /subs upang i-configure."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Ang pag-download ng subtitle ay suportado lamang para sa YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Mga Subtitle</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Wika:</b> {lang}\n"
        "<b>Uri:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Naipadala ang Subtitles SRT-file sa user."
    SUBS_ERROR_PROCESSING_MSG = "❌ Error sa pagproseso ng subtitle file."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Nabigo sa pag-download ng subtitles."
    SUBS_ERROR_MSG = "❌ Error sa pag-download ng subtitles: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Hatiin ang laki ng bahagi na nakatakda sa: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **Invalid size!**\n\n"
        "**Valid range:** 100MB to 2GB\n\n"
        "**Valid formats:**\n"
        "• `100mb` to `2000mb` (megabytes)\n"
        "• `0.1gb` to `2gb` (gigabytes)\n\n"
        "**Examples:**\n"
        "• `/split 100mb` - 100 megabytes\n"
        "• `/split 500mb` - 500 megabytes\n"
        "• `/split 1.5gb` - 1.5 gigabytes\n"
        "• `/split 2gb` - 2 gigabytes\n"
        "• `/split 2000mb` - 2000 megabytes (2GB)\n\n"
        "**Presets:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Pumili ng maximum na laki ng bahagi para sa paghahati ng video:**\n\n"
        "**Saklaw:** 100MB hanggang 2GB\n\n"
        "**Mabilisang mga utos:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Mga halimbawa:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Sarado ang menu."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Mga Setting ng Bot</b>\n\nPumili ng kategorya:"
    SETTINGS_MENU_CLOSED_MSG = "Sarado ang menu."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Mga Opsyon sa Paglilinis</b>\n\nPumili kung ano ang lilinisin:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nPumili ng aksyon:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIA</b>\n\nPumili ng aksyon:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nPumili ng aksyon:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ KARAGDAGANG MGA UTOS</b>\n\nPumili ng aksyon:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Naisakatuparan ang utos."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Limitasyon sa baha. Subukan mamaya."
    SETTINGS_HINT_SENT_MSG = "Ipinadala ang pahiwatig."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Binuksan ang search helper."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Hindi kilalang utos."
    SETTINGS_HINT_CLOSED_MSG = "Sarado ang pahiwatig."
    SETTINGS_HELP_SENT_MSG = "Nagpadala ng help txt sa user"
    SETTINGS_MENU_OPENED_MSG = "Binuksan ang /settings menu"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Nakasara ang search helper"
    SEARCH_CLOSED_MSG = "Nakasara"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proxy {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Error sa pag-save ng mga setting ng proxy."
    PROXY_MENU_TEXT_MSG = "Paganahin o huwag paganahin ang paggamit ng proxy server para sa lahat ng pagpapatakbo ng yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Paganahin o huwag paganahin ang paggamit ng proxy servers ({count} available) para sa lahat ng yt-dlp operations?\n\nKapag pinagana, pipiliin ang mga proxy gamit ang {method} method."
    PROXY_MENU_CLOSED_MSG = "Sarado ang menu."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Naka-enable ang proxy. Lahat ng yt-dlp operation ay gagamit ng proxy."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Naka-enable ang proxy. Lahat ng yt-dlp operation ay gagamit ng {count} proxy server na may {method} paraan ng pagpili."
    PROXY_DISABLED_MSG = "❌ Naka-disable ang proxy."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Error sa pag-save ng mga setting ng proxy."
    PROXY_ENABLED_CALLBACK_MSG = "Pinagana ang proxy."
    PROXY_DISABLED_CALLBACK_MSG = "Naka-disable ang proxy."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ MAGHINTAY HANGGANG MATAPOS ANG IYONG DATING DOWNLOAD"
    AUDIO_HELP_MSG = (
        "<b>🎧 Audio Download Command</b>\n\n"
        "Paggamit: <code>/audio URL</code>\n\n"
        "<b>Mga halimbawa:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Tingnan din: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Nakasara ang audio hint."
    PLAYLIST_HELP_CLOSED_MSG = "Nakasara ang playlist help."
    USERLOGS_CLOSED_MSG = "Isinara ang mensahe ng mga log."
    HELP_CLOSED_MSG = "Isinara ang tulong."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>Mga Setting ng NSFW Blur</b>\n\nAng nilalaman ng NSFW ay <b>{status}</b>.\n\nPumili kung i-blur ang nilalaman ng NSFW:"
    NSFW_MENU_CLOSED_MSG = "Sarado ang menu."
    NSFW_BLUR_DISABLED_MSG = "Na-disable ang NSFW blur."
    NSFW_BLUR_ENABLED_MSG = "Naka-enable ang NSFW blur."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Na-disable ang NSFW blur."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Naka-enable ang NSFW blur."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "I-enable o i-disable ang pagpapadala ng MediaInfo para sa na-download na files?"
    MEDIAINFO_MENU_CLOSED_MSG = "Nakasara ang menu."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ Naka-enable ang MediaInfo. Pagkatapos mag-download, ipapadala ang file info."
    MEDIAINFO_DISABLED_MSG = "❌ Naka-disable ang MediaInfo."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "Naka-enable ang MediaInfo."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "Naka-disable ang MediaInfo."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Listahan ng Available na Formats</b>\n\n"
        "Kunin ang available na video/audio formats para sa isang URL.\n\n"
        "<b>Paggamit:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Mga halimbawa:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Paano gamitin ang format IDs:</b>\n"
        "Pagkatapos makuha ang listahan, gamitin ang specific format ID:\n"
        "• <code>/format id 401</code> - i-download ang format 401\n"
        "• <code>/format id401</code> - pareho sa itaas\n"
        "• <code>/format id140 audio</code> - i-download ang format 140 bilang MP3 audio\n\n"
        "Ang command na ito ay magpapakita ng lahat ng available na formats na maaaring i-download."
    )
    LIST_PROCESSING_MSG = "🔄 Kinukuha ang available na formats..."
    LIST_INVALID_URL_MSG = "❌ Mangyaring magbigay ng wastong URL na nagsisimula sa http:// o https://"
    LIST_CAPTION_MSG = (
        "📃 Available na formats para sa:\n<code>{url}</code>\n\n"
        "💡 <b>Paano itakda ang format:</b>\n"
        "• <code>/format id 134</code> - I-download ang specific format ID\n"
        "• <code>/format 720p</code> - I-download ayon sa quality\n"
        "• <code>/format best</code> - I-download ang best quality\n"
        "• <code>/format ask</code> - Laging magtanong para sa quality\n\n"
        "{audio_note}\n"
        "📋 Gamitin ang format ID mula sa listahan sa itaas"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Audio-only formats:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - I-download ang format 140 bilang MP3 audio\n"
        "• <code>/format id140 audio</code> - pareho sa itaas\n"
        "Ang mga ito ay maa-download bilang MP3 audio files.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Error sa pagpapadala ng mga format ng file: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Nabigong makakuha ng mga format:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Nagkaroon ng error habang pinoproseso ang command"
    LIST_ERROR_CALLBACK_MSG = "May naganap na error"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Paano gamitin ang format IDs:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Pagkatapos makuha ang listahan, gamitin ang partikular na format ID:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - i-download ang format 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - pareho sa itaas\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - i-download ang format 140 bilang MP3 audio\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - pareho sa itaas\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Natuklasan ang audio-only formats: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Ang mga format na ito ay maa-download bilang MP3 audio files.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Mga format na video lamang:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Gamitin ang format ID mula sa listahan sa itaas"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Paggamit:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>Mga halimbawa:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - pinakamahusay na kalidad\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p o mas mababa\n"
        "• /link 720p https://youtube.com/watch?v=... - pareho sa itaas\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K o mas mababa\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K o mas mababa"
        "</blockquote>\n\n"
        "<b>Kalidad:</b> mula 1 hanggang 10000 (hal., 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Mangyaring magbigay ng wastong URL"
    LINK_PROCESSING_MSG = "🔗 Kumukuha ng direktang link..."
    LINK_DURATION_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Na-update ang keyboard setting!**\n\nBagong setting: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Invalid argument!**\n\n"
        "Valid options: `off`, `1x3`, `2x3`, `full`\n\n"
        "Example: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Keyboard Settings**\n\n"
        "Current: **{current}**\n\n"
        "Choose an option:\n\n"
        "Or use: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 na-activate ang keyboard!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Nakatago ang keyboard"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 Na-activate ang 1x3 na keyboard!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 Na-activate ang 2x3 na keyboard!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Na-activate ang Emoji keyboard!"
    KEYBOARD_ERROR_APPLYING_MSG = "Error sa pag-apply ng keyboard setting {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Nakatakda ang format sa: Always Ask. Tatanungin ka para sa kalidad sa bawat pagpapadala ng URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format set to: Always Ask. Now you will be prompted for quality each time you send a URL."
    FORMAT_BEST_UPDATED_MSG = "✅ Na-update ang format sa pinakamahusay na kalidad (AVC+MP4 priority):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Na-update ang format sa ID {id}:\n{format}\n\n💡 <b>Paalala:</b> Kung ito ay audio-only format, ito ay ma-download bilang MP3 audio file."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Na-update ang format sa ID {id} (audio-only):\n{format}\n\n💡 Ito ay ma-download bilang MP3 audio file."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Na-update ang format sa kalidad {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Na-update ang format sa:\n{format}"
    FORMAT_MENU_MSG = (
        "Pumili ng format option o magpadala ng custom gamit ang:\n"
        "• <code>/format &lt;format_string&gt;</code> - custom format\n"
        "• <code>/format 720</code> - 720p quality\n"
        "• <code>/format 4k</code> - 4K quality\n"
        "• <code>/format 8k</code> - 8K quality\n"
        "• <code>/format id 401</code> - specific format ID\n"
        "• <code>/format ask</code> - laging ipakita ang menu\n"
        "• <code>/format best</code> - bv+ba/best quality"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Upang gumamit ng custom format, ipadala ang command sa sumusunod na form:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Palitan ang <code>bestvideo+bestaudio/best</code> ng iyong nais na format string."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Pumili ng iyong nais na resolution at codec:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Nakatakda ang format sa: Always Ask. Ngayon ay tatanungin ka para sa kalidad sa bawat pagpapadala ng URL."
    FORMAT_UPDATED_MSG = "✅ Na-update ang format sa:\n{format}"
    FORMAT_SAVED_MSG = "✅ Na-save ang format."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Na-update ang pagpipilian ng format."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Sarado ang custom format menu"
    FORMAT_CODEC_SET_MSG = "✅ Nakatakda ang codec sa {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Na-update ang pagpipilian ng browser."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Tinanggihan ang pag-access. Admin lang."
    ACCESS_DENIED_ADMIN = "❌ Tinanggihan ang pag-access. Admin lang."
    WELCOME_MASTER = "Maligayang pagdating Master 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Paumanhin... May naganap na error habang nagda-download."
    SIZE_LIMIT_EXCEEDED = "❌ Ang laki ng file ay lumampas sa {max_size_gb} GB na limitasyon. Mangyaring pumili ng mas maliit na file sa loob ng pinapayagang laki."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Hindi nahanap ang script: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Nagda-download ng bagong Firebase dump gamit ang {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Matagumpay na na-reload ang cache ng Firebase!"
    ADMIN_CACHE_FAILED_MSG = "❌ Nabigong i-reload ang cache ng Firebase. Suriin kung may {cache_file}."
    ADMIN_ERROR_RELOADING_MSG = "❌ Error sa pag-reload ng cache: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Error sa pagpapatakbo ng {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Ipinadala ang mensahe ng promo sa lahat ng iba pang user</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Hindi maipadala ang mensahe ng promo. Subukan na mag-reply sa isang mensahe\nO may naganap na error</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ Hindi pa nagda-download ang user ng anumang nilalaman...</b> Wala pa sa mga log"
    ADMIN_INVALID_COMMAND_MSG = "❌ Di-wastong utos"
    ADMIN_NO_DATA_FOUND_MSG = "❌ Walang nakitang data sa cache para sa <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Walang laman ang pila — wala pang umalis sa channel."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Pila ng ban</b>\nKabuuang nakabinbin: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (kaliwa: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… at {extra} higit pang mga user."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Gamitin ang /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Mga naka-block na user mula sa pila: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Naka-enable ang auto-blocking: ang mga bagong aalis ay ipagbabawal kaagad."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Na-disable ang awtomatikong pag-block."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Naka-iskedyul na window ng auto-block na nakatakda sa bawat {interval}."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Log ng aktibidad ng channel para sa huling {hours} oras (2 araw)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 Huling {hours} oras (2 araw): sumali sa {joined}, umalis {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Walang aktibidad sa huling {hours} oras (2 araw)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Kabuuan: 🟢 {joined} sumali, 🔴 {left} naiwan."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Walang access sa log ng aktibidad ng channel. Hindi mabasa ng mga bot ang mga log ng admin. Magbigay ng CHANNEL_GUARD_SESSION_STRING sa config na may session ng user para paganahin ang feature na ito."
    BAN_TIME_USAGE_MSG = "❌ Paggamit: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Gumamit ng mga format tulad ng 10s, 6m, 5h, 4d, 3w, 2M o 1y."
    BAN_TIME_SET_MSG = "🕒 Ang pagitan ng pag-scan ng log ng channel ay nakatakda sa {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Ulat ng pag-scan ng channel\n"
        "Na-run sa: {run_ts}\n"
        "Interval: {interval}\n"
        "Mga bagong umalis: {new_leavers}\n"
        "Auto bans: {auto_banned}\n"
        "Nakabinbin: {pending}\n"
        "Huling event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Paggamit: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Hindi makakapagtanggal ng admin ang admin"
    ADMIN_USER_BLOCKED_MSG = "Naka-block ang user 🔒❌\n \nID: <code>{user_id}</code>\nPetsa ng pag-block: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "Naka-block na ang <code>{user_id}</code> ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Sorry! Hindi ka admin"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Paggamit: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Na-unblock ang user 🔓✅\n \nID: <code>{user_id}</code>\nPetsa ng pag-unblock: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "Ang <code>{user_id}</code> ay na-unblock na ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Na-unblock na mga user: {count}\n⏱ Timestamp: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Paggamit: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Binabalewala ang user 👁️❌\n \nID: <code>{user_id}</code>\nPetsa ng pagbalewala: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> ay binabalewala na ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Paggamit: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Hindi na binabalewala ang user 👁️✅\n \nID: <code>{user_id}</code>\nPetsa ng hindi pagbalewala: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> ay hindi binabalewala ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Tagal ng pagtakbo ng bot -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Mangyaring magbigay ng URL upang i-clear ang cache.\nPaggamit: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Mangyaring magbigay ng wastong URL.\nPaggamit: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Matagumpay na na-clear ang cache para sa URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Walang nakitang cache para sa link na ito."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Error sa pag-clear ng cache: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Tinanggihan ang pag-access. Admin lang."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Pagpapatakbo ng script ng pag-update ng listahan ng porno: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Matagumpay na nakumpleto ang script!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Matagumpay na nakumpleto ang script!\n\nOutput:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Nabigo ang script na may return code {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Error sa pagpapatakbo ng script: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Nire-reload ang porn at mga cache na nauugnay sa domain..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Matagumpay na na-reload ang porn caches!\n\n"
        "📊 Kasalukuyang status ng cache:\n"
        "• Porn domains: {porn_domains}\n"
        "• Porn keywords: {porn_keywords}\n"
        "• Supported sites: {supported_sites}\n"
        "• WHITELIST: {whitelist}\n"
        "• GREYLIST: {greylist}\n"
        "• BLACK_LIST: {black_list}\n"
        "• WHITE_KEYWORDS: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Error sa pag-reload ng porn cache: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Mangyaring magbigay ng URL para suriin.\nPaggamit: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Mangyaring magbigay ng wastong URL.\nPaggamit: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Sinusuri ang URL para sa NSFW na nilalaman...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Resulta ng Porn Check</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Status:</b> <b>{status_text}</b>\n\n"
        "<b>Explanation:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Error sa pagsuri sa URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Nilinis ang cookies."
    CLEAN_LOGS_CLEANED_MSG = "nililinis ang mga log."
    CLEAN_TAGS_CLEANED_MSG = "nilinis ang mga tag."
    CLEAN_FORMAT_CLEANED_MSG = "nalinis ang format."
    CLEAN_SPLIT_CLEANED_MSG = "nilinis ang split."
    CLEAN_MEDIAINFO_CLEANED_MSG = "nilinis ang mediainfo."
    CLEAN_SUBS_CLEANED_MSG = "Nilinis ang mga setting ng subtitle."
    CLEAN_KEYBOARD_CLEANED_MSG = "Nalinis ang mga setting ng keyboard."
    CLEAN_ARGS_CLEANED_MSG = "Nalinis ang mga setting ng Args."
    CLEAN_NSFW_CLEANED_MSG = "Nilinis ang mga setting ng NSFW."
    CLEAN_PROXY_CLEANED_MSG = "Nalinis ang mga setting ng proxy."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Nilinis ang mga setting ng paghihintay sa baha."
    CLEAN_ALL_CLEANED_MSG = "Lahat ng mga file ay nalinis."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nPumili ng aksyon:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Na-save ang cookie file"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Nilaktawan ang pagpapatunay para sa cookies na hindi YouTube"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Umiiral ang cookie file ngunit may maling format"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Hindi nahanap ang cookie file."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Sinisimulan ang pagsubok sa YouTube cookies...\n\nMangyaring maghintay habang sinusuri at pinapatunay ko ang iyong cookies."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Ang iyong umiiral na YouTube cookies ay gumagana nang maayos!\n\nHindi na kailangan na mag-download ng bago."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Ang iyong umiiral na YouTube cookies ay nag-expire o hindi wasto.\n\n🔄 Nagda-download ng bagong cookies..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} cookie source ay hindi naka-configure!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} cookie source ay dapat na isang .txt file!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Range limit exceeded: {range_count} files requested (maximum {max_img_files}).\n\nUse one of these commands to download maximum available files:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Isara"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Na-exceed ang limitasyon ng media: {count} file ang hiniling (maximum {max_count}).\n\nGamitin ang isa sa mga utos na ito upang i-download ang maximum na available na file:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Nakahanap ng <b>{count}</b> media item mula sa link"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Piliin ang hanay ng pag-download:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Pagpapanggap ng browser"
    ARGS_REFERER_DESC_MSG = "Header ng referer"
    ARGS_USER_AGENT_DESC_MSG = "Header ng User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "I-bypass ang mga paghihigpit sa heograpiya"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Suriin ang SSL certificate"
    ARGS_LIVE_FROM_START_DESC_MSG = "Mag-download ng mga live stream mula sa simula"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Huwag mag-download ng mga live stream sa simula"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Gumamit ng lalagyan ng MPEG-TS para sa mga HLS na video"
    ARGS_NO_PLAYLIST_DESC_MSG = "Mag-download lamang ng isang video, hindi playlist"
    ARGS_NO_PART_DESC_MSG = "Huwag gumamit ng .part file"
    ARGS_NO_CONTINUE_DESC_MSG = "Huwag ipagpatuloy ang mga bahagyang pag-download"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Format ng audio para sa pagkuha"
    ARGS_EMBED_METADATA_DESC_MSG = "I-embed ang metadata sa video file"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "I-embed ang thumbnail sa video file"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Sumulat ng thumbnail sa file"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Bilang ng mga kasabay na fragment na ida-download"
    ARGS_FORCE_IPV4_DESC_MSG = "Pilitin ang mga koneksyon sa IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "Pilitin ang mga koneksyon sa IPv6"
    ARGS_XFF_DESC_MSG = "X-Forwarded-Para sa diskarte sa header"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "Laki ng HTTP chunk (bytes)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Matulog bago mag-download ng subtitle (segundo)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Payagan ang mga legacy na koneksyon sa server"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Pigilan ang pagpapatunay ng sertipiko ng HTTPS"
    ARGS_USERNAME_DESC_MSG = "username ng account"
    ARGS_PASSWORD_DESC_MSG = "Password ng account"
    ARGS_TWOFACTOR_DESC_MSG = "Dalawang-factor na authentication code"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Huwag pansinin ang mga error sa pag-download at magpatuloy"
    ARGS_MIN_FILESIZE_DESC_MSG = "Minimum na laki ng file (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Pinakamataas na laki ng file (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Mga item sa playlist na ida-download (hal., 1,3,5 o 1-5)"
    ARGS_DATE_DESC_MSG = "Mag-download ng mga video na na-upload sa petsang ito (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Mag-download ng mga video na na-upload bago ang petsang ito (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Mag-download ng mga video na na-upload pagkatapos ng petsang ito (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Mga custom na HTTP header (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Sleep interval sa pagitan ng mga kahilingan (segundo)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Pinakamataas na agwat ng pagtulog (segundo)"
    ARGS_RETRIES_DESC_MSG = "Bilang ng mga muling pagsubok"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Format ng lalagyan ng video"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Output na format ng lalagyan para sa pagsasama"
    ARGS_SEND_AS_FILE_DESC_MSG = "Ipadala ang lahat ng media bilang dokumento sa halip na media"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "magpanggap"
    ARGS_REFERER_SHORT_MSG = "Referer"
    ARGS_GEO_BYPASS_SHORT_MSG = "Geo Bypass"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Suriin ang Cert"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Live na Simula"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Walang Live Start"
    ARGS_USER_AGENT_SHORT_MSG = "Ahente ng Gumagamit"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Walang Playlist"
    ARGS_NO_PART_SHORT_MSG = "Walang Bahagi"
    ARGS_NO_CONTINUE_SHORT_MSG = "Walang Ituloy"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Format ng Audio"
    ARGS_EMBED_METADATA_SHORT_MSG = "I-embed ang Meta"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "I-embed ang Thumb"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Sumulat ng Thumb"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Kasabay"
    ARGS_FORCE_IPV4_SHORT_MSG = "Pilitin ang IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Pilitin ang IPv6"
    ARGS_XFF_SHORT_MSG = "XFF Header"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Laki ng Tipak"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Mga Sleep Sub"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Legacy Connect"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Walang Check Cert"
    ARGS_USERNAME_SHORT_MSG = "Username"
    ARGS_PASSWORD_SHORT_MSG = "Password"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Huwag pansinin ang mga Error"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Min Laki"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Pinakamataas na Sukat"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Mga Item ng Playlist"
    ARGS_DATE_SHORT_MSG = "Petsa"
    ARGS_DATEBEFORE_SHORT_MSG = "Date Bago"
    ARGS_DATEAFTER_SHORT_MSG = "Petsa Pagkatapos"
    ARGS_HTTP_HEADERS_SHORT_MSG = "Mga Header ng HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Sleep Interval"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Max Sleep"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Format ng Video"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Pagsamahin ang Format"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Ipadala Bilang File"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ Masyadong malaki ang file. Ang maximum na laki ay 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Tanging mga file na may sumusunod na format ang pinapayagang .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ Ang file ay hindi mukhang cookie.txt (walang linyang '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ Error sa pagbabasa ng file: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Umiiral ang cookie file at may tamang format"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} masyadong malaki ang cookie file! Max 100KB, nakakuha ng {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} na-download at na-save ang cookie file bilang cookie.txt sa iyong folder.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ Ang pinagmulan ng cookie ng {service} ay hindi available (status {status}). Mangyaring subukan muli mamaya."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Error sa pag-download ng {service} cookie file. Pakisubukang muli mamaya."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Nagbigay ang user ng bagong cookie file.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Matagumpay na na-update ang cookie:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Hindi wastong cookie.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ Hindi naka-configure ang mga source ng cookie sa YouTube!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Nagda-download at sinusuri ang YouTube cookies...\n\nPagtatangka {attempt} ng {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Tinanggihan ang pag-access. Admin lang."
    ADMIN_USER_LOGS_TOTAL_MSG = "Kabuuan: <b>{total}</b>\n<b>{user_id}</b> - logs (Huling 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 na-activate ang keyboard!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Itinakda ang wika ng subtitle sa: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Itinakda ang wika ng subtitle sa: {flag} {name} na may naka-enable na AUTO/TRANS."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Isinara ang menu ng wika ng subtitle."
    SUBS_DOWNLOADING_MSG = "💬 Nagda-download ng mga subtitle..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Nire-reload ang cache ng Firebase sa memorya..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Walang COOKIE_URL na na-configure. Gamitin ang /cookie o mag-upload ng cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Nagda-download ng cookies mula sa malayong URL..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Ang Fallback COOKIE_URL ay dapat tumuro sa isang .txt file."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Masyadong malaki ang Fallback cookie file (>100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Na-download ang cookie file sa YouTube sa pamamagitan ng fallback at na-save bilang cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Ang fallback na pinagmulan ng cookie ay hindi available (status {status}). Subukan ang /cookie o mag-upload ng cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Error sa pag-download ng fallback cookie. Subukan ang /cookie o mag-upload ng cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Hindi inaasahang error sa pag-download ng fallback na cookie."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} hindi naka-install ang browser."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Na-save ang cookies gamit ang browser: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Nabigong i-save ang cookies: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ Gumagana nang maayos ang cookies sa YouTube"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ Ang YouTube cookies ay nag-expire o hindi wasto\n\nGamitin ang /cookie upang makakuha ng bagong cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - custom format\n• <code>/format 720</code> - Kalidad na 720p\n• <code>/format 4k</code> - Kalidad na 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Naipadala ang hint."
    FORMAT_MKV_TOGGLE_MSG = "Ang MKV ay {status} na"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Walang naka-configure na remote na URL"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Di-wastong format ng file"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Masyadong malaki ang file"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Matagumpay na na-download ang cookies"
    COOKIES_SERVER_ERROR_MSG = "❌ Error sa server {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Nabigo ang pag-download"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Hindi inaasahang error"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Hindi naka-install ang browser."
    COOKIES_MENU_CLOSED_MSG = "Sarado ang menu."
    COOKIES_HINT_CLOSED_MSG = "Isinara ang pahiwatig ng cookie."
    IMG_HELP_CLOSED_MSG = "Isinara ang tulong."
    SUBS_LANGUAGE_UPDATED_MSG = "Na-update ang mga setting ng wika ng subtitle."
    SUBS_MENU_CLOSED_MSG = "Isinara ang menu ng wika ng subtitle."
    KEYBOARD_SET_TO_MSG = "Itinakda ang keyboard sa {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Error sa pagpoproseso ng setting"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "Pinagana ang MediaInfo."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "Hindi pinagana ang MediaInfo."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Na-disable ang NSFW blur."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Naka-enable ang NSFW blur."
    SETTINGS_MENU_CLOSED_MSG = "Sarado ang menu."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Aktibo ang paghihintay sa baha. Subukan mamaya."
    OTHER_HELP_CLOSED_MSG = "Isinara ang tulong."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Isinara ang mensahe ng mga log."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Sarado ang menu."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Di-wastong laki."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Error sa pagpapadala ng MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Nagkaroon ng error: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - lahat ng log"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - lahat {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 I-download mula sa Remote URL"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Buksan ang Browser"
    SELECT_BROWSER_MSG = "Pumili ng browser kung saan magda-download ng cookies:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Walang nakitang mga browser sa system na ito. Maaari kang mag-download ng cookies mula sa malayong URL o subaybayan ang status ng browser:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Buksan ang Browser</b> - upang subaybayan ang status ng browser sa mini-app"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Nabigong patakbuhin ang /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Limitasyon sa baha. Subukan mamaya."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Nabigong buksan ang menu ng cookie ng browser"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "I-save habang isinara ang pahiwatig ng cookie."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Paggamit:</b>\n<code>/link [quality] URL</code>\n\n<b>Mga halimbawa:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - pinakamahusay na kalidad\n• /link 720 https://youtube.com/watch?v=... - 720p o mas mababa\n• /link 720p https://youtube.com/watch?v=... - pareho sa itaas\n• /link 4k https://youtube.com/watch?v=... - 4K o mas mababa\n• /link 8k https://youtube.com/watch?v=... - 8K o mas mababa</blockquote>\n\n<b>Kalidad:</b> mula 1 hanggang 10000 (hal., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - Kalidad na 8K"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Nakuha ang direktang link</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Nabigong makakuha ng mga link ng stream"
    LINK_ERROR_GETTING_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Di-wastong index ng cookie ng YouTube: {selected_index}. Ang available na hanay ay 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Nagda-download at sinusuri ang YouTube cookies...\n\nPagtatangka {attempt} ng {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Nagda-download at sinusuri ang YouTube cookies...\n\nPagtatangka {attempt} ng {total}\n🔍 Sinusubukan ang cookies..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ Matagumpay na na-download at na-validate ang YouTube cookies!\n\nGinamit na pinagmulan {source} ng {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Lahat ng YouTube cookies ay nag-expire o hindi available!\n\nMakipag-ugnayan sa administrator ng bot upang palitan ang mga ito."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ Na-exceed ang limitasyon ng pagsubok sa YouTube cookie!\n\n🔢 Maximum: {limit} pagtatangka bawat oras\n⏰ Mangyaring subukan muli mamaya"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Ang tag #{wrong} ay naglalaman ng mga ipinagbabawal na character. Tanging mga titik, numero at _ lamang ang pinapayagan.\nMangyaring gamitin: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Di-wastong argumento!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Nakatakdang wika ng subtitle: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Halimbawa: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Napiling wika: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Palaging Ask mode {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Ang mga subtitle ay hindi pinagana"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Mga setting ng subtitle</b>\n\n{status_text}\n\nPumili ng wika ng subtitle:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - huwag paganahin ang mga subtitle\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Mga setting ng subtitle</b>\n\n{status_text}\n\nPumili ng wika ng subtitle:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Pamagat:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Tagal:</b> {duration} seg\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 720p maximum na kalidad\n- 1.5 oras maximum na tagal\n- 500mb maximum na laki ng video</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️BABALA: dahil sa mataas na epekto sa CPU, ang function na ito ay napakabagal (malapit sa real-time) at limitado sa:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Mabilisang mga utos:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - huwag paganahin ang mga subtitle\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - paganahin ang Always Ask mode\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - set language\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - set language with AUTO/TRANS enabled\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - paganahin ang Always Ask mode\n"
    SUBS_AUTO_SUBS_TEXT = "(auto-subs)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Auto-subs mode {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "Na-disable ang SUBS sa pamamagitan ng command: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "Naka-enable ang SUBS Always Ask sa pamamagitan ng command: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "Itinakda ang wika ng SUBS sa pamamagitan ng command: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "Itinakda ang SUBS language + auto mode sa pamamagitan ng command: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Binuksan ng user ang /subs na menu."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Itinakda ng user ang subtitle na wika sa: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Na-toggle ng user ang AUTO/TRANS mode sa: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Na-toggle ng user ang Always Ask mode sa: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Humiling ng cookies ang user mula sa browser."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Ang keyboard ng pagpili ng browser ay ipinadala gamit ang mga naka-install na browser lamang."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Isinara ang pagpili ng browser."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "Matagumpay na nagamit ang Fallback COOKIE_URL (nakatago ang pinagmulan)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "Nabigo ang Fallback COOKIE_URL: status={status} (nakatago)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Fallback COOKIE_URL hindi inaasahang error: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Browser {browser} hindi naka-install."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Na-save ang cookies gamit ang browser: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "Na-save ang cookie file para sa user na si {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "Umiiral ang cookie file, may tamang format, at gumagana ang cookies sa YouTube."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Umiiral ang cookie file at may tamang format, ngunit ang cookies sa YouTube ay nag-expire na."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Umiiral ang cookie file at may tamang format."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Umiiral ang cookie file ngunit may maling format."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Hindi nahanap ang cookie file."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{service} ang URL ng cookie ay walang laman para sa user na {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} cookie URL ay hindi .txt (nakatago)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} masyadong malaki ang cookie file: {size} bytes (nakatago ang pinagmulan)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{service} cookie file na na-download para sa user na {user_id} (nakatago ang source)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Hindi nakita ang script: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Nabigong magpadala ng paunang status message"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Error sa pagpapatakbo ng {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Na-reload ang cache ng Firebase sa pamamagitan ng awtomatikong gawain."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Na-reload ng admin ang cache ng Firebase."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Error sa pag-reload ng Firebase cache: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Sinimulan ang broadcast. Teksto:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Ipinadala ang mensahe sa broadcast sa lahat ng user."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Nabigong i-broadcast ang mensahe: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Na-clear ng Admin {user_id} ang cache para sa URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Sinimulan ni Admin {user_id} ang script ng pag-update ng listahan ng porno: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Matagumpay na nakumpleto ng admin ang script ng pag-update ng listahan ng porno {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Nabigo ang script ng pag-update ng listahan ng porno ng admin {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Sinubukan ng Admin {user_id} na patakbuhin ang hindi umiiral na script: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Error sa pagpapatakbo ng porn update script ng admin {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Sinimulan ni Admin {user_id} ang pag-reload ng cache ng porn"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Error sa pag-reload ng porn cache ng admin {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Sinuri ng Admin {user_id} ang URL para sa NSFW: {url} - Resulta: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "Hiniling ng user ang pagbabago ng format."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "Nakatakda ang format sa ALWAYS_ASK."
    FORMAT_UPDATED_BEST_LOG_MSG = "Na-update ang format sa best: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "Na-update ang format sa ID {format_id}: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "Na-update ang format sa ID {format_id} (audio-only): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "Na-update ang format sa quality {quality}: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "Na-update ang format sa: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "Naipadala ang format menu."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "Sarado ang pagpili ng format."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "Naipadala ang custom format hint."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "Naipadala ang format resolution menu."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "Bumalik sa main format menu."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "Na-update ang format sa: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "Nakatakda ang format sa ALWAYS_ASK."
    FORMAT_CODEC_SET_LOG_MSG = "Nakatakda ang codec preference sa {codec}"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Sarado ang custom format menu"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "Na-extract ang direktang link para sa user na si {url} mula sa {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Nabigong i-extract ang direktang link para sa user na {user_id} mula sa {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Error sa utos ng link para sa user na {error}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Itinakda ng user na si {setting} ang keyboard sa {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Itinakda ng user na si {setting} ang keyboard sa {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "Itinakda ang MediaInfo sa pamamagitan ng command: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Binuksan ng user ang /mediainfo menu."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: sarado."
    MEDIAINFO_ENABLED_LOG_MSG = "Pinagana ang MediaInfo."
    MEDIAINFO_DISABLED_LOG_MSG = "Hindi pinagana ang MediaInfo."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Itinakda ang hating laki sa {size} byte sa pamamagitan ng argumento."
    SPLIT_MENU_OPENED_LOG_MSG = "Binuksan ng user ang /split na menu."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Isinara ang hating pagpili."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Itinakda ang hating laki sa {size} byte."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Itinakda ang proxy sa pamamagitan ng command: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Binuksan ng user ang /proxy na menu."
    PROXY_MENU_CLOSED_LOG_MSG = "Proxy: sarado."
    PROXY_ENABLED_LOG_MSG = "Pinagana ang proxy."
    PROXY_DISABLED_LOG_MSG = "Naka-disable ang proxy."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Isinara ang mensahe ng tulong."
    AUDIO_HELP_SHOWN_LOG_MSG = "Nagpakita ng /audio help"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Hiniling ng user ang tulong sa playlist."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Isinara ang tulong sa playlist."
    AUDIO_HINT_CLOSED_LOG_MSG = "Isinara ang pahiwatig ng audio."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Direktang menu ng link na ginawa sa pamamagitan ng LINK button para sa user na si {url} mula sa {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Nabigong i-extract ang direktang link sa pamamagitan ng LINK button para sa user na si {error} mula sa {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "LIST command na naisakatuparan para sa user na {url}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Mabilis na I-embed: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Palaging Ask menu na ipinadala para sa {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Gumawa ng naka-cache na menu ng mga katangian para sa user na si {error} pagkatapos ng error: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Laging Magtanong ng error sa menu para sa {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Naayos ang format sa pamamagitan ng mga setting ng /args"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Audio"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Video"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Video"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Susunod ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Nakaraan"
    SUBTITLES_NEXT_BUTTON_MSG = "Susunod ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Walang laman ang lahat ng field ng text"
    SENDER_VIDEO_DURATION_MSG = "Tagal ng video:"
    SENDER_UPLOADING_FILE_MSG = "📤 Ina-upload ang file..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Nag-a-upload ng Video..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Tagal ng video:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 file ang na-upload."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Impormasyon sa Video"
    DOWN_UP_NUMBER_MSG = "Numero"
    DOWN_UP_TITLE_MSG = "Pamagat"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Na-download na video."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Pinoproseso para sa pag-upload..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Na-upload ang split part {part} file"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Kumpleto na ang pag-upload"
    DOWN_UP_FILES_UPLOADED_MSG = "na-upload na mga file"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Isara"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBS"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 SUBS"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Browser"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Pagkuha ng direktang link..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Pagkuha ng mga available na format..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Kinukuha ang paglalarawan ng video..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Error sa pagkuha ng paglalarawan: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Hindi available ang paglalarawan ng video"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Error sa pagpapadala ng paglalarawan: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Ipinadala ang paglalarawan ng video sa user {user_id} para sa {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Sinisimulan ang gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Tagal:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Browser:</b> Buksan sa web browser"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Magagamit na mga format para sa"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Paano gamitin ang mga format ID:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Pagkatapos makuha ang listahan, gumamit ng partikular na format ID:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - format ng pag-download 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - katulad ng nasa itaas"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - i-download ang format 140 bilang MP3 audio"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Natukoy ang mga format na audio lamang"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Ang mga format na ito ay mada-download bilang mga MP3 audio file."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Paano magtakda ng format:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Mag-download ng partikular na format ID"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - I-download ayon sa kalidad"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/pinakamahusay na format</code> - I-download ang pinakamahusay na kalidad"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Palaging humingi ng kalidad"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Mga audio-only na format:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - I-download ang format 140 bilang MP3 audio"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Ida-download ang mga ito bilang mga MP3 audio file."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Gumamit ng format ID mula sa listahan sa itaas"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Error: Hindi nakita ang orihinal na mensahe."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Pahina ng mga format"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Error sa pagpapakita ng menu ng mga format"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Error sa pagkuha ng mga format"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Error sa pagkuha ng mga available na format."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Pakisubukang muli mamaya."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>Hindi maproseso ng yt-dlp ang nilalamang ito"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Inirerekomenda ng system ang paggamit ng gallery-dl sa halip."
    ALWAYS_ASK_OPTIONS_MSG = "**Mga Pagpipilian:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Para sa mga gallery ng larawan: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Para sa mga iisang larawan: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Ang Gallery-dl ay madalas na gumagana nang mas mahusay para sa Instagram, Twitter, at iba pang nilalaman ng social media."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Subukan ang Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Naayos ang format sa pamamagitan ng /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Mga subtitle"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Naka-dub na audio"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Available ang mga subtitle"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Pumili ng subtitle na wika"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Hindi mahanap at hindi mag-e-embed ang mga sub"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Instant repost mula sa cache"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Pumili ng wikang audio"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞Bayaran ang NSFW (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Piliin ang kalidad ng pag-download"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Mag-download ng larawan (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Kumuha ng direktang link sa video"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Ipakita ang listahan ng mga available na format"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Baguhin ang ext/codec ng video"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀I-embed"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — I-extract lang ang audio"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞Bayaran ang NSFW (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Instant repost mula sa cache"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Pumili ng wikang audio"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Pinakamahusay"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Iba pa"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝sub lang"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Matalinong pagpapangkat"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Idinagdag ang row ng action button (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Nagdagdag ng mga row ng action button (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Nagdagdag ng mga button sa ibaba sa umiiral na row"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Gumawa ng bagong hilera sa ibaba"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Walang nakitang mga video sa playlist"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "Hindi sinusuportahang URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Walang mahanap na video"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Walang nakitang video"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Walang nakitang media"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Walang laman ang tweet na ito"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Error sa pagkuha ng impormasyon ng video:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Error sa pagkuha ng impormasyon ng video"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Subukan ang command na <code>/clean</code> at subukang muli. Kung magpapatuloy ang error, nangangailangan ng pahintulot ang YouTube. I-update ang cookies.txt sa pamamagitan ng <code>/cookie</code> o <code>/cookies_from_browser</code> at subukang muli."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Sarado ang menu."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Manu-manong Pagpili ng Kalidad"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Manu-manong piliin ang kalidad dahil nabigo ang awtomatikong pagtuklas:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Lahat ng Available na Format"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Mga Magagamit na Kalidad (mula sa cache)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Paggamit ng mga naka-cache na katangian - maaaring hindi available ang mga bagong format"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Format ng pag-download"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Nagda-download"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Nagda-download gamit ang pagsubaybay sa pag-unlad..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Nagda-download gamit ang format:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Nagda-download ng audio gamit ang format:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Dina-download ang pinakamahusay na kalidad..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Dina-download ang database dump..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Nagda-download"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Pahina ng mga format"
    ALWAYS_ASK_FROM_CACHE_MSG = "(mula sa cache)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Error: Hindi nakita ang orihinal na mensahe. Maaaring natanggal ito. Mangyaring ipadala muli ang link."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Error: Hindi nakita ang orihinal na URL. Mangyaring ipadala muli ang link."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Nakuha ang direktang link</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Pamagat:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Tagal:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Nabigong makakuha ng mga link ng stream"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Direktang link na kinuha sa pamamagitan ng Always Ask menu para sa user na si {url} mula sa {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Nabigong i-extract ang direktang link sa pamamagitan ng Always Ask menu para sa user na {user_id} mula sa {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Direktang link na nakuha sa pamamagitan ng down_and_up_with_format para sa user na {url} mula sa {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Nabigong i-extract ang direktang link sa pamamagitan ng down_and_up_with_format para sa user {user_id} mula sa {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Kinukuha ang direktang link sa pamamagitan ng down_and_audio para sa user {user_id} mula sa {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Nabigong i-extract ang direktang link sa pamamagitan ng down_and_audio para sa user na {user_id} mula sa {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Ipinadala ang audio mula sa cache."
    AUDIO_PROCESSING_MSG = "🎙️ Pinoproseso ang audio..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Nagda-download ng audio:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Nagkaroon ng error habang nagda-download ng audio."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Nabigong i-extract ang impormasyon ng audio"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Nilaktawan ang hindi sinusuportahang uri ng file sa playlist sa index {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "Hindi nahanap ang audio file pagkatapos ng pag-download."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Nag-u-upload ng audio file...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Nabigong magpadala ng audio: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Ipinadala ang audio ng playlist: {sent}/{total} mga file (kalidad={quality}) sa user{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Nabigong mag-download ng audio: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Kinansela ang pag-download dahil sa timeout (2 oras)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Hindi nahanap ang video file: {filename}"
    VIDEO_PROCESSING_ERROR_MSG = "❌ Error sa pagproseso ng video: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Error sa pagpapadala ng file ng paglalarawan: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 kung gusto mong baguhin ang caption ng video - tumugon sa video gamit ang bagong text</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Walang nakitang mga subtitle"
    VIDEO_PROGRESS_MSG = "<b>Video:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Audio:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ Lumampas sa limitasyon ng URL: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Nakumpleto ang pagproseso"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Hindi pinapayagan ang mga hanay ng playlist sa maraming URL mode. Magpadala lamang ng mga solong URL na walang mga saklaw (*1*5, /vid 1-10, atbp.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Tingnan <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>dito</a> kung sinusuportahan ng iyong site"
    ERROR_COOKIE_NEEDED_MSG = "Maaaring kailanganin mo ng <code>cookie</code> para sa pag-download ng video na ito. Una, linisin ang iyong workspace sa pamamagitan ng command na <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Para sa Youtube - kumuha ng <code>cookie</code> sa pamamagitan ng command na <b>/cookie</b>. Para sa anumang iba pang sinusuportahang site - ipadala ang iyong sariling cookie (<a href='https://t.me/tg_ytdlp/203'>guide1</a>) (<a href='https://t.me/tg_ytdlp/214'>guide2</a>) at pagkatapos nito ipadala muli ang link ng iyong video."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Pumili ng subtitle na wika"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Walang mga alternatibong wika ng audio"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Pumili ng wikang audio"
    PAGE_NUMBER_MSG = "Pahina {page}"
    TOTAL_PROGRESS_MSG = "Kabuuang Pag-unlad"
    SUBTITLE_MENU_CLOSED_MSG = "Isinara ang subtitle menu."
    SUBTITLE_LANGUAGE_SET_MSG = "Nakatakdang wika ng subtitle: {value}"
    AUDIO_SET_MSG = "Audio set: {value}"
    FILTERS_UPDATED_MSG = "Na-update ang mga filter"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Bumalik"
    CLOSE_BUTTON_TEXT = "🔚Isara"
    LIST_BUTTON_TEXT = "📃Listahan"
    IMAGE_BUTTON_TEXT = "🖼Larawan"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Hindi awtomatikong natukoy ang mga kalidad\nGamitin ang button na 'Iba pa' para makita ang lahat ng available na format.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Natuklasan ang Live Stream**\n\nHindi pinapayagan ang pag-download ng patuloy o walang hanggang live stream.\n\nMangyaring maghintay hanggang matapos ang stream at subukan muli ang pag-download kapag:\n• Alam na ang tagal ng stream\n• Natapos na ang stream\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Pag-download ng Live Stream</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Tipak {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Pinakamataas na laki: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Kabuuang tagal: {duration} seg"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Live Stream - Tipak {chunk}</b>\n⏱ Tagal: {duration} seg\n📦 Laki: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Tipak {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Kumpleto na ang Pag-download ng Live Stream</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "Na-download {chunks} (mga) tipak"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Kabuuang tagal: {duration} seg"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Nahinto ang Pag-download ng Live Stream</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Ang direktoryo ng user ay tinanggal (marahil sa pamamagitan ng /clean command)"
    LIVE_STREAM_FILE_DELETED_MSG = "Ang chunk file ay tinanggal (marahil sa pamamagitan ng /clean command)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Natapos na ang stream"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Mangyaring pumili ng ibang format gamit ang command na `/format`."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Nakuha ang direktang link</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Pamagat:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Tagal:</b> {duration} seg\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Error sa Pagproseso ng File**\n\nNa-download ang video ngunit hindi ma-proseso dahil sa di-wastong character sa filename.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Error sa Pagproseso ng File**\n\nNa-download ang video ngunit hindi ma-proseso dahil sa error ng di-wastong argumento.\n\n"
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Format Hindi Available**\n\nAng hiniling na format ng video ay hindi available para sa video na ito.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Hindi natagpuan ang Format ID {format_id} para sa video na ito.\n\nAvailable na Format IDs: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **Ang AV1 format ay hindi available para sa video na ito.**\n\n**Available na format:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Error sa Pagproseso ng File**\n\nNa-download ang audio ngunit hindi ma-proseso dahil sa di-wastong character sa filename.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Error sa Pagproseso ng File**\n\nNa-download ang audio ngunit hindi ma-proseso dahil sa error ng di-wastong argumento.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Ipinasok ng user ang ipinagbabawal na nilalaman. Hindi ma-download."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "NSFW blur set sa pamamagitan ng command: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Binuksan ng user ang /nsfw menu."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: sarado."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Nabigong i-download ang {service} cookie: status={status} (nakatago ang url)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Error sa pag-download ng {service} cookie: {error} (nakatago ang url)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Hindi inaasahang error habang dina-download ang {service} cookie (nakatago ang url): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Na-update ang cookie file para sa user na si {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Di-wastong nilalaman ng cookie na ibinigay ng user {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "Walang laman ang mga URL ng cookie ng YouTube para sa user na {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "Na-download at na-validate ang cookies ng YouTube para sa user na si {source} mula sa source {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Nabigo ang lahat ng pinagmumulan ng cookie sa YouTube para sa user na {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Error sa check_porn command ng admin {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Ang laki ng hating bahagi ay nakatakda sa {size} byte."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Nakumpleto ang pag-upload ng video sa paghahati ng file."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Ipinadala ang mga video sa playlist: {sent}/{total} mga file (kalidad={quality}) sa user {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Hindi kilalang error: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Nilaktawan ang hindi sinusuportahang uri ng file sa playlist sa index {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg not found. Please install FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Nabigo ang pag-convert sa MP4: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Ang pag-embed ng subtitles ay maaaring tumagal ng mahabang panahon (hanggang 1 min bawat 1 min ng video)!\n🔥 Sinisimulan ang pag-burn ng subtitles..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Hindi maaaring i-embed ang mga subtitle dahil sa mga limitasyon (kalidad/tagal/laki)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Hindi available ang mga subtitle para sa napiling wika"
    ERROR_SENDING_VIDEO_MSG = "❌ Error sa pagpapadala ng video: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Ipinadala ang mga video sa playlist: {sent}/{total} mga file."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Kinansela ang pag-download dahil sa timeout (2 oras)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Nabigong i-download ang video: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Error: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ Ang JSON ay dapat na isang object (diksyonaryo)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Di-wastong format ng JSON. Mangyaring magbigay ng wastong JSON."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Ang halaga ay dapat nasa pagitan ng {min_val} at {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} itinakda sa: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Totoo"
    ARGS_FALSE_BUTTON_MSG = "❌ Mali"
    ARGS_BACK_BUTTON_MSG = "🔙 Back"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Isara"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Totoo"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Mali"
    ARGS_NOT_SET_MSG = "Hindi nakatakda"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ Ang AV1 format ay hindi available para sa video na ito.\n\nAvailable na format:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Error sa pag-download: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ Walang nakitang mga video sa playlist sa index {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Nabigo ang Video Conversion**\n\nHindi ma-convert ang video sa MP4 dahil sa error ng di-wastong argumento.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Nabigo ang Video Conversion**\n\nHindi ma-convert ang video sa MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Nabigong makakuha ng mga link ng stream"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Error sa pagkuha ng link:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ Walang nakitang content sa index {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Error: Hindi nakita ang orihinal na mensahe."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Error: Hindi nakita ang URL."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Hindi maaaring i-embed ang URL na ito."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} codec ay hindi available para sa video na ito"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} format ay hindi available para sa video na ito"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Limitasyon sa baha. Subukan mamaya."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Suriin ang Cookie"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ NAKA-ON"
    PROXY_OFF_BUTTON_MSG = "❌ NAKA-OFF"
    PROXY_CLOSE_BUTTON_MSG = "🔚Isara"
    
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ NAKA-ON"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ NAKA-OFF"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Isara"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ NAKA-ON (Walang Malabo)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ON (Walang Blur)"
    NSFW_OFF_BLUR_MSG = "✅ OFF (Blur)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ OFF (Blur)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Malinis"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Error sa pagproseso ng mensahe ng tugon para sa user {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Error sa pagpapadala ng broadcast sa user {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Logs ng {bot_name}\nUser: {user_id}\nKabuuang logs: {total}\nKasalukuyang oras: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nKabuuan {path}: {count}\nKasalukuyang oras: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Kabuuang Users: {count}</i>\nHuling 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Mga porn cache na na-reload ng admin {admin_id}. Mga Domain: {domains}, Mga Keyword: {keywords}, Mga Site: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS_: __VARX4_DOM: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Error sa pagpapadala ng timeout message: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Pumili ng wika</b>"
    LANG_CHANGED_MSG = "✅ Napalitan ang wika sa {lang_name}"
    LANG_ERROR_MSG = "❌ Error sa pagpapalit ng wika"
    LANG_CLOSED_MSG = "Nakasara ang pagpili ng wika"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] callback: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Pagdaragdag ng button ng pagsubaybay sa browser na may URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "Hindi na-configure ang URL ng pagsubaybay sa browser: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Keyboard setting updated!**\n\nNew setting: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Nabigong itago ang keyboard: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Paggamit ng gumaganang cookies sa YouTube para sa pagkuha ng link para sa user na si {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Walang gumaganang cookies sa YouTube na available para sa pagkuha ng link para sa user na si {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Paggamit ng umiiral nang cookies sa YouTube para sa pagkuha ng link para sa user na si {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Walang nakitang cookies sa YouTube para sa pagkuha ng link para sa user na si {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Kinopya ang global cookie file sa user {user_id} folder para sa pagkuha ng link"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Ang user na si {user_id} ay humiling ng mediainfo command"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] User {user_id} ay admin: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] User {user_id} ay nasa channel: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Tinanggihan ang access ng user na {user_id} - hindi admin at wala sa channel"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] User {user_id} nabigyan ng access"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Available lang ang command na ito para sa mga administrator."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Tapos na ang pag-download gamit ang suporta sa PO token"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Limitasyon sa baha. Subukan mamaya."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST token refresh error: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Error sa pagsasara ng session ng Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Error sa pagsisimula ng base db structure: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Hindi lahat ng parameter ay nakatakda sa config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL ay hindi nakatakda"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey ay hindi nakatakda para sa pagkuha ng idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Error sa pag-download ng Firebase dump: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Nabigong i-download ang Firebase dump sa pamamagitan ng REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Error sa _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Error sa pagpapatakbo ng auto reload_cache (attempt {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Nabigo ang lahat ng muling pagsubok"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Sinisimulan ang pag-download ng dump ng Firebase sa {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Hindi available ang dependency: mga kahilingan o Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ Walang laman ang database"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Error sa pagsasara ng logger: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Error habang naglilinis: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Error sa pag-clone: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ I-clone ang timeout"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Pagbubukod ng clone: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Kinansela ng user ang update"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Matagumpay na na-clone ang repository"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Inilipat ang mga backup sa _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Ang lahat ng mga module ay na-load"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Nakumpleto ang paglilinis sa labasan"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Natanggap ang signal {signal}, isinasara nang maayos..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Mangyaring maghintay..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Nagda-download ng HLS stream:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "naghihintay ng mga fragment"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Ang backup {ts} ay hindi nakita sa _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Nabigong i-restore ang {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Na-restore: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Mga detalye:</b> {error_details}\n\nNahinto ang pag-download dahil sa kritikal na error.\n\n💡 <b>Tip:</b> Kung nakakakuha ka ng 401 Unauthorized error, subukan ang paggamit ng <code>/cookie instagram</code> command o magpadala ng iyong sariling cookies upang ma-authenticate sa Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domain sa porn blacklist: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Nakahanap ng mga keyword na porn: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domain sa whitelist: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Nakakita ng mga keyword sa whitelist: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Walang nakitang mga keyword na porn"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API error sa index {index}, lumalaktaw sa susunod na audio..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API error sa index {index}, lumalaktaw sa susunod na video..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "Nagpasok ang user ng <b>url</b>\n <b>pangalan ng user:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>Nagpasok ang user ng ganito:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Sumali sa Channel"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Handler sa pagrerehistro: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - I-download ang aking 5 cookies"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Kunin ang YT-cookie ng browser"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Patunayan ang iyong cookie file"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Mag-upload ng custom na cookie"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Isara"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Mga available na format para sa: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Isara"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Isara"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Isara"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Isara"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Isinara ang tulong."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "sarado"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "May naganap na error"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "Hindi natagpuan ang ffmpeg sa PATH o direktoryo ng proyekto. Mangyaring i-install ang FFmpeg."
    YTDLP_NOT_FOUND_MSG = "Ang yt-dlp binary ay hindi nakita sa PATH o direktoryo ng proyekto. Mangyaring i-install ang yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Hahatiin ang video sa {rounds} na bahagi, na maaaring labis"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Hinahati ang bahagi ng video {current}/{total}: {start_time:.2f}s hanggang {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Nabigong lumikha ng split part {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Matagumpay na nalikha ang split part {part}: {target_name} ({size} bytes)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Error sa paghahati ng bahagi ng video {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Matagumpay na nahati ang video sa {count} na bahagi"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Error sa proseso ng paghahati ng video: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Error habang pinoproseso ang video {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Hindi umiiral ang video file: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Error sa pag-parse ng dimensions '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Hindi matukoy ang video dimensions mula sa '{size_result}', gumagamit ng default: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Error sa paglikha ng thumbnail: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Error sa pag-parse ng video duration: {error}, ang resulta ay: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Hindi nalikha ang thumbnail sa {thumb_dir}, gumagamit ng default"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Error sa pagpapatupad ng command: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Error sa paglikha ng thumbnail gamit ang FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Nilaktawan ang seksyong hindi dict na config: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Nakatakda ang {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Gumagamit ng cookies ng user: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Paggamit ng cookies sa YouTube para sa user na si {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Kinopya ang pandaigdigang file ng cookie sa folder na {user_id} ng user"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Gumagamit ng kinopyang pandaigdigang cookies bilang cookies ng user: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Nabigong kopyahin ang pandaigdigang cookie file para sa user na {user_id}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Gumagamit ng --no-cookies para sa domain: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Humiling ng proxy ngunit nabigong mag-import/makakuha ng config: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Pilitin ang paggamit ng proxy para sa gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Hiniling ang proxy ngunit hindi kumpleto ang configuration ng proxy"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Nabigo ang proxy helper: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Pinag-parse ang mga item ng extractor..."
    GALLERY_DL_ITEM_COUNT_MSG = "Item {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Natagpuan ang metadata (tag 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "Nahanap na URL (tag 3): {url}, metadata: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Natagpuan ang metadata (legacy): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "Nahanap na URL (legacy): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Natagpuan ang filename: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Natagpuan ang direktoryo: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Natagpuan ang extension: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Na-parse {count} item, impormasyon: {info}, fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Pagtatakda ng gallery-dl config: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Pagsubok sa Diskarte A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor module ay hindi nahanap"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() hindi available sa build na ito"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Tinatawagan ang extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Walang extractor ang tumugma sa URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Pagtatakda ng cookies sa extractor: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Nabigong itakda ang cookies sa extractor: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Nakita ang extractor, tumatawag ng mga item()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Nagtagumpay ang Diskarte A, nakakuha ng impormasyon: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Diskarte A: extractor.items() ay hindi nagbalik ng wastong impormasyon"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Nabigo ang Strategy A (extractor.find): {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Fallback metadata mula sa --get-urls: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Nabigo ang lahat ng diskarte upang makakuha ng metadata"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Nabigong i-extract ang impormasyon ng larawan: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job module ay hindi nahanap (sirang pag-install?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob hindi available sa build na ito"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Naghahanap ng mga na-download na file sa direktoryo ng gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Sinusubukang maghanap ng mga file sa pamamagitan ng mga pangalan mula sa extractor"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Error sa pagbabasa ng mga argumento ng user para sa {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Error habang pinoproseso ang video{video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Ang user {user_id} ay pinagana ang send_as_file, na ipinapadala bilang dokumento"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "paulit-ulit na nag-time out ang send_video; bumabalik sa send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Masyadong mahaba ang caption, sinusubukan na may kaunting caption"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "nag-time out ang send_video (minimal caption); fallback sa send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Error sa pagpapadala ng video na may kaunting caption: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Error sa pagpapadala ng buong file ng paglalarawan: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Error sa pag-alis ng pansamantalang file ng paglalarawan: {error}"
    
    # YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Nilaktawan ang match_filter para sa domain sa NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Sinusuri ang umiiral nang cookies sa YouTube sa URL ng user para sa pagtukoy ng format para sa user na {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Gumagana ang kasalukuyang cookies ng YouTube sa URL ng user para sa pagtukoy ng format para sa user {user_id} - gamit ang mga ito"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Nabigo ang kasalukuyang cookies ng YouTube sa URL ng user, sinusubukang kumuha ng mga bago para sa pagtukoy ng format para sa user na {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Sinusubukan ang pinagmulan ng cookie sa YouTube na {i} para sa pagtukoy ng format para sa user na {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "Ang cookies sa YouTube mula sa pinagmulan {i} ay gumagana sa URL ng user para sa pagtukoy ng format para sa user {user_id} - na-save sa folder ng user"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "Ang cookies ng YouTube mula sa pinagmulan {i} ay hindi gumagana sa URL ng user para sa pagtukoy ng format para sa user na {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Nabigong i-download ang cookies ng YouTube mula sa pinagmulan {i} para sa pagtukoy ng format para sa user na {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Nabigo ang lahat ng pinagmumulan ng cookie ng YouTube para sa pagtukoy ng format para sa user na {user_id}, ay susubukan nang walang cookies"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Walang pinagmumulan ng cookie ng YouTube na na-configure para sa pagtukoy ng format para sa user na si {user_id}, ang susubukan nang walang cookies"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Walang nakitang cookies sa YouTube para sa pagtukoy ng format para sa user na si {user_id}, na sumusubok na kumuha ng mga bago"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Paggamit ng cookies sa YouTube para sa pagtukoy ng format para sa user na {user_id} (na-validate na sa menu na Laging Magtanong)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Walang nakitang cookies sa YouTube para sa pagtukoy ng format para sa user na si {user_id}, sinusubukang i-restore..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Kinopya ang pandaigdigang cookie file sa user {user_id} folder para sa pagtukoy ng format"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Nabigong kopyahin ang pandaigdigang cookie file para sa user na {user_id}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Gumagamit ng --no-cookies para sa domain sa get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "Hindi pa nasimulan ang app. Hindi ma-access ang {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Caption:</b> <code>{caption}</code>\n<b>ID ng user:</b> <code>{user_id}</code>\n<b>Unang pangalan ng user:</b> <code>{users_name}</code>\n<b>ID ng file ng video:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Error sa caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Hindi inaasahang error sa caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL ng Video</a>{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL отсутствует sa конфигурации"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ nasimulan ang firebase_admin"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 Na-refresh ang REST idToken"
    DB_LOG_FOR_USER_ADDED_MSG = "Idinagdag ang log para sa user"
    DB_DATABASE_CREATED_MSG = "nilikha ang db"
    DB_BOT_STARTED_MSG = "Nagsimula ang bot"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "Ang RELOAD_CACHE_EVERY ay nagpatuloy sa config.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Naka-cache na ang bahagi ng playlist: {path_parts}, lumalaktaw"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: walang nahanap na cache para sa anumang variant ng URL/kalidad, nagbabalik ng walang laman na dict"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: mabilis na bilang para sa malaking hanay: {cached_count} naka-cache na mga video"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: walang nakitang cache para sa hash {url_hash}, kalidad {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: walang nahanap na cache para sa anumang variant ng URL, nagbabalik ng Wala"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Tinanggihan ang pag-access. Admin lang."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Auto Firebase cache reloading updated!\n\n📊 Status: {status}\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Di-wastong argumento. Gamitin ang /auto_cache sa | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Ang pagitan ay dapat nasa pagitan ng 1 at 168 na oras"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Nabigong itakda ang pagitan"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Auto Firebase cache interval updated!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Auto Firebase cache reloading started!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Naka-enable ang auto reload; susunod sa {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Na-disable ng admin ang auto reload."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Itinakda sa {interval}h; susunod sa {interval}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Nagsimula ang auto reload; susunod sa {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Itinigil ng admin ang auto reload."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Na-load ang cache ng Firebase: {count} root node"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Hindi nakita ang file ng cache ng Firebase, simula sa walang laman na cache: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Nabigong i-load ang cache ng firebase: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Na-reload ang cache ng Firebase: {count} root node"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Hindi nakita ang file ng cache ng Firebase: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Nabigong i-reload ang firebase cache: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 Ikaw ay pinagbawalan mula sa bot! Para ma-unban, makipag-ugnayan sa {Config.ADMIN_USERNAME}\n<blockquote>P.S. Huwag umalis sa channel - awtomatikong mapagbabawalan ka ⛔️</blockquote>\n🌍Palitan ang wika /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Walang nakitang mga format ng video. Sinusubukang mag-download ng larawan..."
    AA_FLOOD_WAIT_MSG = "⚠️ Nilimitahan ng Telegram ang pagpapadala ng mensahe.\n⏳ Mangyaring maghintay: {time_str}\nUpang i-update ang timer, ipadala muli ang URL ng 2 beses."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>I-click ang button upang kopyahin ang stream URL, pagkatapos ay i-paste ito sa VLC app</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>I-click ang button upang kopyahin ang stream URL, pagkatapos ay i-paste ito sa VLC app</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Error sa pagkuha ng link:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Error sa pagpapadala ng mga format ng file: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Nabigong makakuha ng mga format:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Pagsusuri... (maghintay ng 6 na segundo)"
    AA_PROCESSING_MSG = "🔎 Pagsusuri..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Ang tag #{wrong} ay naglalaman ng mga ipinagbabawal na character. Tanging mga titik, numero at _ lamang ang pinapayagan.\nMangyaring gamitin: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Para sa pagtatrabaho sa grupo, kailangan ng bot ang mga karapatan ng administrator. Mangyaring gawing admin ang bot sa grupong ito."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Kamusta {first_name},\n \n<i>Ang bot na ito🤖 ay maaaring mag-download ng anumang video sa telegram nang direkta.😊 Para sa karagdagang impormasyon pindutin ang <b>/help</b></i> 👈\n\n<blockquote>P.S. Ang pag-download ng 🔞NSFW na nilalaman at mga file mula sa ☁️Cloud Storage ay may bayad! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Huwag umalis sa channel - ma-ba-ban ka sa paggamit ng bot ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Walang mga file na aalisin."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 Matagumpay na naalis ang lahat ng file!\n\nMga naalis na file:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ MAGHINTAY HANGGANG MATAPOS ANG IYONG DATING DOWNLOAD"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "Ang instance ng app ay Wala sa check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict is None, na nagpapahintulot sa pag-download"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict is None, na nagpapahintulot sa pag-embed ng subtitle"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: checking limits - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: info_dict keys: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Nilaktawan ang pag-embed ng subtitle: ang tagal {duration}s ay lumampas sa limitasyon {max_duration}s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Nilaktawan ang pag-embed ng subtitle: laki {size_mb:.2f}MB ay lumampas sa limitasyon {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Nilaktawan ang pag-embed ng subtitle: kalidad {width}x{height} (min side {min_side}p) lumampas sa limitasyon {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "playlist"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Na-exceed ang range limit para sa {service}: {count} (maximum {max_count}).\n\nGamitin ang isa sa mga utos na ito upang i-download ang maximum na available na file:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Na-exceed ang range limit para sa {service}: {count} (maximum {max_count})\nUser ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "Hindi pinagana ang provider ng token ng PO sa config"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "Ang URL {url} ay hindi isang YouTube domain, na nilalaktawan ang PO token"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "Hindi available ang PO token provider sa {base_url}, na bumabalik sa karaniwang pagkuha ng YouTube"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "Na-clear ang cache ng provider ng PO token, titingnan ang availability sa susunod na kahilingan"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Hindi pa available ang instance ng app"
    HELPER_USER_NAME_MSG = "Gumagamit"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "May nakitang paghihintay sa baha, natutulog nang {wait_seconds} segundo"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Natukoy ang paghihintay sa baha ngunit hindi ma-extract ang oras, natutulog nang {retry_delay} segundo"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "May nakitang error sa msg_seqno, natutulog nang {retry_delay} segundo"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Hindi kumpleto ang configuration ng proxy, gamit ang direktang koneksyon"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Isara"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Isara"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Isara"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Inalis ang file ng mga log."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Inalis ang file ng mga tag."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Inalis ang format ng file."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Inalis ang split file."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Inalis ang file ng Mediainfo."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Inalis ang mga setting ng subtitle."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Inalis ang mga setting ng keyboard."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Inalis ang mga setting ng args."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 Inalis ang mga setting ng NSFW."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Inalis ang mga setting ng proxy."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Inalis ang mga setting ng paghihintay sa baha."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Isara"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Utos sa Pag-download ng Video"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Paggamit: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Mga halimbawa:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (direktang pagkakasunod-sunod)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (baligtad na pagkakasunod-sunod)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Tingnan din: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Isinara ng user na {user_id} ang add_bot_to_group na utos"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Nabigong i-extract ang YouTube ID"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Nabigong i-download ang thumbnail o ito ay masyadong malaki"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Pumili ng wikang audio"
    AA_NO_SUBTITLES_DETECTED_MSG = "Walang nakitang mga subtitle"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Pumili ng subtitle na wika"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Error sa Pagpapatunay"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Hindi Nahanap ang Account"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Account Hindi Available"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Lumampas sa Limit ng Rate"
    GALLERY_DL_NETWORK_ERROR_MSG = "Error sa Network"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Content Hindi Available"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Mga Paghihigpit sa Heograpiya"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Kinakailangan ang Pagpapatunay"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Paglabag sa Patakaran"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Hindi Alam na Error"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Nagsimula ang pag-download</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Isara"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Utos sa Pag-download ng Video</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Paggamit: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Mga halimbawa:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Tingnan din: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Limitasyon sa baha. Subukan mamaya."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Cookie Command Usage</b>

<code>/cookie</code> - Ipakita ang cookie menu
<code>/cookie youtube</code> - I-download ang YouTube cookies
<code>/cookie instagram</code> - I-download ang Instagram cookies
<code>/cookie tiktok</code> - I-download ang TikTok cookies
<code>/cookie x</code> o <code>/cookie twitter</code> - I-download ang Twitter/X cookies
<code>/cookie facebook</code> - I-download ang Facebook cookies
<code>/cookie custom</code> - Ipakita ang custom cookie instructions

<i>Ang available na serbisyo ay depende sa bot configuration.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Natanggal ang cookie file at na-clear ang cache."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Nakaraan"
    SUBS_BACK_BUTTON_MSG = "🔙Bumalik"
    SUBS_OFF_BUTTON_MSG = "🚫 NAKA-OFF"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - itakda ang wika"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - itakda ang wika gamit ang AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Wastong opsyon:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 WIKA"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 MALINIS"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIES"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MEDIA"
    SETTINGS_INFO_BUTTON_MSG = "📖 IMPORMASYON"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ HIGIT PA"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Cookies lang"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Mga log"
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Mga tag"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Format"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Hatiin"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 MediaInfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Mga subtitle"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Keyboard"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Args"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Proxy"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Paghihintay sa baha"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Lahat ng files"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - I-download ang aking 5 cookies"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Kunin ang browser's YT-cookie"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - I-validate ang iyong cookie file"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - I-upload ang custom cookie"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Baguhin ang kalidad at format"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - I-ON / I-OFF ang MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Baguhin ang split video part size"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - I-download ang video bilang audio"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Mga setting ng wika ng mga subtitle"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Paano i-download ang playlists"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - I-download ang images via gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Ipadala ang iyong #tags"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Kumuha ng instructions"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Ipadala ang iyong logs"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Tulong ng playlist"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - paano"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Kumuha ng direct video links"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - I-enable/disable ang proxy"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Layout ng keyboard"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Inline na katulong sa paghahanap"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - mga argumento ng yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - Mga setting ng blur ng NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Clean Options</b>\n\nPumili kung ano ang lilinisin:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: I-activate ang @vid search"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: I-activate ang @vid search"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 NAKA-OFF"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 PUNO"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL ng Mga Larawan]({url})"
    IMAGE_ERROR_MSG = "❌ Error: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Bumalik"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - custom format"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p kalidad"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K kalidad"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K kalidad"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - partikular na format ID"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - laging ipakita ang menu"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/pinakamahusay na kalidad"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Laging Magtanong (menu + buttons)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Iba pa (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (pinakamahusay para sa PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (pinakamahusay para sa mobile Telegram)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (MAX kalidad)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Custom (ilagay ang iyong sarili)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Mula sa Browser"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Sarili mo"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Awtomatik na nagsara ang input mode dahil sa kawalan ng aktibidad (5 minuto)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 I-reset Lahat"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Tingnan ang Kasalukuyan"
    ARGS_BACK_BUTTON_MSG = "🔙 Bumalik"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>I-forward ang mensaheng ito sa iyong favorites upang i-save ang mga settings na ito bilang template.</i> \n\n<i>I-forward ang mensaheng ito pabalik dito upang i-apply ang mga settings na ito.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Kasalukuyang yt-dlp Arguments:\n\nWalang naka-configure na custom settings.\n\n---\n\n<i>I-forward ang mensaheng ito sa iyong favorites upang i-save ang mga settings na ito bilang template.</i> \n\n<i>I-forward ang mensaheng ito pabalik dito upang i-apply ang mga settings na ito.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Kasalukuyang yt-dlp Arguments:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 I-export ang Settings"
    ARGS_SETTINGS_READY_MSG = "Handa na ang settings para sa export! I-forward ang mensaheng ito sa favorites upang i-save."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Kasalukuyang yt-dlp Arguments:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Nabigo na makilala ang settings sa mensahe. Siguraduhing nagpadala ka ng tamang settings template."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Matagumpay na na-import ang settings!\n\nIn-apply na parameters: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Mga pangunahing setting:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Error sa pag-save ng imported settings."
    ARGS_ERROR_IMPORTING_MSG = "❌ May naganap na error habang nag-i-import ng settings."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>I-download ang Cookie Files</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Pumili ng serbisyo upang i-download ang cookie file."
    COOKIE_MENU_SAVE_INFO_MSG = "Ang cookie files ay ma-save bilang cookie.txt sa iyong folder."
    COOKIE_MENU_TIP_HEADER_MSG = "Tip: Maaari mo ring gamitin ang direct command:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – i-download at i-validate ang cookies"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – gumamit ng partikular na source ayon sa index (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Pagkatapos ay i-verify gamit ang <code>/check_cookie</code> (nagte-test sa RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Laging Magtanong"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Link"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Panoorin"  # PANSAMANTALANG NAKA-DISABLE: down ang poketube service
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Caption"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ TRIM"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Video Trim</b>\n\nVideo duration: <b>{start_time} - {end_time}</b>\n\nMangyaring ipadala ang nais na time range sa format:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nHalimbawa: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Hindi wastong format. Mangyaring gamitin: <code>HH:MM:SS-HH:MM:SS</code>\n\nHalimbawa: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Hindi wastong range. Ang start time ay dapat na mas mababa kaysa sa end time."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ Ang time range ay nasa labas ng mga hangganan ng video.\n\nVideo duration: <b>{start_time} - {end_time}</b>\n\nAng iyong range ay dapat na nasa loob ng mga limitasyong ito."

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Bahagyang nakumpleto - {successful_uploads}/{total_files} audio files na na-upload."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Matagumpay na na-download at naipadala ang audio - {total_files} files na na-upload."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Pribadong TikTok Account</b>\n\n"
        "Ang TikTok account na ito ay pribado o lahat ng videos ay pribado.\n\n"
        "<b>💡 Solusyon:</b>\n"
        "1. Sundin ang account @{username}\n"
        "2. Ipadala ang iyong cookies sa bot gamit ang <code>/cookie</code> command\n"
        "3. Subukan muli\n\n"
        "<b>Pagkatapos i-update ang cookies, subukan muli!</b>"
    )

    #######################################################
