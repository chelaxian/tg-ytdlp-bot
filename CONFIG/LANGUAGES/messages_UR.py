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
    CREDITS_MSG = "<blockquote><i>منتظم</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 زبان تبدیل کریں: /lang</b>"
    TO_USE_MSG = "<i>اس بوٹ کو استعمال کرنے کے لیے آپ کو @tg_ytdlp Telegram چینل میں سبسکرائب کرنا ہوگا۔</i>\nچینل میں شامل ہونے کے بعد، <b>اپنا ویڈیو لنک دوبارہ بھیجیں اور بوٹ اسے آپ کے لیے ڈاؤن لوڈ کرے گا</b> ❤️\n\n<blockquote>P.S. 🔞NSFW مواد اور ☁️کلاؤڈ اسٹوریج سے فائلیں ڈاؤن لوڈ کرنا ادائیگی شدہ ہے! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ چینل نہ چھوڑیں - آپ کو بوٹ استعمال کرنے سے پابندی لگائی جائے گی ⛔️</blockquote>"

    ERROR1 = "URL لنک نہیں ملا۔ براہ کرم <b>https://</b> یا <b>http://</b> کے ساتھ ایک URL درج کریں"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>پلے لسٹیں (yt-dlp)</b>

پلے لسٹیں ڈاؤن لوڈ کرنے کے لیے اس کا URL <code>*start*end</code> رینجز کے ساتھ آخر میں بھیجیں۔ مثال کے طور پر: <code>URL*1*5</code> (1 سے 5 تک شامل پہلے 5 ویڈیوز)۔ <code>URL*-1*-5</code> (1 سے 5 تک شامل آخری 5 ویڈیوز)۔
یا آپ <code>/vid FROM-TO URL</code> استعمال کر سکتے ہیں۔ مثال کے طور پر: <code>/vid 3-7 URL</code> (شروع سے 3 سے 7 تک شامل ویڈیوز ڈاؤن لوڈ کرتا ہے)۔ <code>/vid -3-7 URL</code> (آخر سے 3 سے 7 تک شامل ویڈیوز ڈاؤن لوڈ کرتا ہے)۔ <code>/audio</code> کمانڈ کے لیے بھی کام کرتا ہے۔

<b>مثالیں:</b>

🟥 <b>YouTube پلے لسٹ سے ویڈیو رینج:</b> (🍪 درکار)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(1 سے 5 تک شامل پہلے 5 ویڈیوز ڈاؤن لوڈ کرتا ہے)
🟥 <b>YouTube پلے لسٹ سے ایک ویڈیو:</b> (🍪 درکار)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(صرف تیسرا ویڈیو ڈاؤن لوڈ کرتا ہے)

⬛️ <b>TikTok پروفائل:</b> (آپ کا 🍪 درکار)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(صارف پروفائل سے پہلے 10 ویڈیوز ڈاؤن لوڈ کرتا ہے)

🟪 <b>Instagram کہانیاں:</b> (آپ کا 🍪 درکار)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(پہلی 3 کہانیاں ڈاؤن لوڈ کرتا ہے)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(البم سے پہلی 10 کہانیاں ڈاؤن لوڈ کرتا ہے)

🟦 <b>VK ویڈیوز:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(صارف/گروپ پروفائل سے پہلے 3 ویڈیوز ڈاؤن لوڈ کرتا ہے)

⬛️<b>Rutube چینلز:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(چینل سے 2 سے 4 تک شامل ویڈیوز ڈاؤن لوڈ کرتا ہے)

🟪 <b>Twitch کلپس:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(چینل سے پہلے 3 کلپس ڈاؤن لوڈ کرتا ہے)

🟦 <b>Vimeo گروپس:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(گروپ سے پہلے 2 ویڈیوز ڈاؤن لوڈ کرتا ہے)

🟧 <b>Pornhub ماڈلز:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(ماڈل پروفائل سے پہلے 2 ویڈیوز ڈاؤن لوڈ کرتا ہے)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(آپ کے پرامپٹ کے ذریعے سرچ نتائج سے پہلے 3 ویڈیوز ڈاؤن لوڈ کرتا ہے)

اور اسی طرح...
<a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">سپورٹ شدہ سائٹس کی فہرست</a> دیکھیں
</blockquote>

<blockquote expandable>🖼 <b>تصاویر (gallery-dl)</b>

بہت سے پلیٹ فارمز سے تصاویر/فوٹوز/البمز ڈاؤن لوڈ کرنے کے لیے <code>/img URL</code> استعمال کریں۔

<b>مثالیں:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>رینجز:</b>
<code>/img 11-20 https://example.com/album</code> — آئٹمز 11..20
<code>/img 11- https://example.com/album</code> — 11 سے آخر تک (یا بوٹ کی حد)

<i>سپورٹ شدہ پلیٹ فارمز میں vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor وغیرہ شامل ہیں۔ مکمل فہرست:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">gallery-dl سپورٹ شدہ سائٹس</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>ویڈیو ڈاؤن لوڈ بوٹ - مدد</b>

📥 <b>بنیادی استعمال:</b>
• کوئی بھی لنک بھیجیں → بوٹ اسے ڈاؤن لوڈ کرے گا
  <i>بوٹ خودکار طور پر yt-dlp کے ذریعے ویڈیوز اور gallery-dl کے ذریعے تصاویر ڈاؤن لوڈ کرنے کی کوشش کرتا ہے۔</i>
• <b>متعدد URLs:</b> کوالٹی سلیکشن موڈ میں (<code>/format</code>) آپ ایک پیغام میں <b>10 URLs</b> تک بھیج سکتے ہیں۔ ہر URL ایک نئی لائن پر یا خالی جگہوں سے الگ۔
• <code>/audio URL</code> → آڈیو نکالیں
• <code>/link [quality] URL</code> → براہ راست لنکس حاصل کریں
• <code>/proxy</code> → تمام ڈاؤن لوڈز کے لیے پروکسی فعال/غیر فعال کریں
• ویڈیو پر متن کے ساتھ جواب دیں → کیپشن تبدیل کریں

📋 <b>پلے لسٹیں اور رینجز:</b>
• <code>URL*1*5</code> → پہلے 5 ویڈیوز ڈاؤن لوڈ کریں
• <code>URL*-1*-5</code> → آخری 5 ویڈیوز ڈاؤن لوڈ کریں
• <code>/vid 3-7 URL</code> → <code>URL*3*7</code> بن جاتا ہے
• <code>/vid -3-7 URL</code> → <code>URL*-3*-7</code> بن جاتا ہے

🍪 <b>کوکیز اور پرائیویٹ:</b>
• پرائیویٹ ویڈیوز کے لیے *.txt کوکی اپ لوڈ کریں
• <code>/cookie [service]</code> → کوکیز ڈاؤن لوڈ کریں (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → انڈیکس کے ذریعے ماخذ منتخب کریں (1–N)
• <code>/cookies_from_browser</code> → براؤزر سے نکالیں
• <code>/check_cookie</code> → کوکی کی تصدیق کریں
• <code>/save_as_cookie</code> → متن کو کوکی کے طور پر محفوظ کریں

🧹 <b>صاف کرنا:</b>
• <code>/clean</code> → صرف میڈیا فائلیں
• <code>/clean all</code> → سب کچھ
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>ترتیبات:</b>
• <code>/settings</code> → ترتیبات کا مینو
• <code>/format</code> → کوالٹی اور فارمیٹ
• <code>/split</code> → ویڈیو کو حصوں میں تقسیم کریں
• <code>/mediainfo on/off</code> → میڈیا معلومات
• <code>/nsfw on/off</code> → NSFW بلر
• <code>/tags</code> → محفوظ شدہ ٹیگز دیکھیں
• <code>/sub on/off</code> → سب ٹائٹلز
• <code>/keyboard</code> → کی بورڈ (OFF/1x3/2x3)

🏷️ <b>ٹیگز:</b>
• URL کے بعد <code>#tag1#tag2</code> شامل کریں
• ٹیگز کیپشنز میں ظاہر ہوتے ہیں
• <code>/tags</code> → تمام ٹیگز دیکھیں

🔗 <b>براہ راست لنکس:</b>
• <code>/link URL</code> → بہترین کوالٹی
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → مخصوص کوالٹی

⚙️ <b>فوری کمانڈز:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → کوالٹی سیٹ کریں
• <code>/keyboard off/1x3/2x3/full</code> → کی بورڈ لے آؤٹ
• <code>/split 100mb-2000mb</code> → حصے کا سائز تبدیل کریں
• <code>/subs off/ur/en auto</code> → سب ٹائٹل زبان
• <code>/list URL</code> → دستیاب فارمیٹس کی فہرست
• <code>/mediainfo on/off</code> → میڈیا معلومات آن/آف
• <code>/proxy on/off</code> → تمام ڈاؤن لوڈز کے لیے پروکسی فعال/غیر فعال کریں

📊 <b>معلومات:</b>
• <code>/usage</code> → ڈاؤن لوڈ ہسٹری
• <code>/search</code> → @vid کے ذریعے ان لائن سرچ

🖼 <b>تصاویر:</b>
• <code>URL</code> → تصاویر URL ڈاؤن لوڈ کریں
• <code>/img URL</code> → URL سے تصاویر ڈاؤن لوڈ کریں
• <code>/img 11-20 URL</code> → مخصوص رینج ڈاؤن لوڈ کریں
• <code>/img 11- URL</code> → 11ویں سے آخر تک ڈاؤن لوڈ کریں

👨‍💻 <i>ڈویلپر:</i> @upekshaip
🤝 <i>تعاون کنندہ:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
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
    PROCESSING_MSG = "🔄 پروسیسنگ ..."
    DOWNLOADING_MSG = "📥 <b>Downloading media...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Downloading image...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Download complete</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "ڈاؤن لوڈ:"
    SENT_STATUS_MSG = "بھیجا:"
    PENDING_TO_SEND_STATUS_MSG = "بھیجنے کے لئے زیر التواء:"
    TITLE_LABEL_MSG = "عنوان:"
    MEDIA_COUNT_LABEL_MSG = "میڈیا گنتی:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "ڈاؤن لوڈ ختم ، پروسیسنگ آڈیو ..."
    VIDEO_PROCESSING_MSG = "📽 ویڈیو پروسیسنگ کر رہی ہے ..."
    WAITING_HOURGLASS_MSG = "⌛"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Sent from cache</b>\n\nSent albums: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ ویڈیو کامیابی کے ساتھ کیشے سے بھیجی گئی۔"
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ کیشے ({cached}/{total} فائلوں) سے بھیجی گئی پلے لسٹ ویڈیوز۔"
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} ویڈیوز کیشے سے بھیجے گئے، گمشدہ افراد کو ڈاؤن لوڈ کرتے ہوئے ..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Sent from cache: {cached}\n🔄 Continuing download..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Could not analyze media, proceeding with maximum allowed range (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Could not determine media count, proceeding with maximum allowed range (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Could not determine total media count, proceeding with specified range {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>Invalid URL</b>\n\nPlease provide a valid URL starting with http:// or https://"

    ERROR_OCCURRED_MSG = "❌ <b>Error occurred</b>\n\n<code>{url}</code>\n\nError: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Error sending video: {error}"
    ERROR_UNKNOWN_MSG = "❌ نامعلوم غلطی: {error}"
    ERROR_NO_DISK_SPACE_MSG = "videos ویڈیوز ڈاؤن لوڈ کرنے کے لئے کافی ڈسک کی جگہ نہیں ہے۔"
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ فائل کا سائز {limit} GB حد سے تجاوز کرتا ہے۔ براہ کرم اجازت شدہ سائز میں ایک چھوٹی فائل منتخب کریں۔"

    ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram has limited message sending.\n⏳ Please wait: {time}\nTo update timer send URL again 2 times."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram has limited message sending.\n⏳ Please wait: \nTo update timer send URL again 2 times."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "sub سب ٹائٹلز ڈاؤن لوڈ کرنے میں ناکام"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Direct Stream Links</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Title:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Duration:</b> {duration} sec\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ غلطی: اصل پیغام نہیں ملا۔"

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{tag} contains forbidden characters. Only letters, digits and _ are allowed.\nPlease use: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ پلے لسٹ ویڈیوز بھیجی گئیں: {sent}/{total} فائلیں۔"
    PLAYLIST_CACHE_SENT_MSG = "cache کیشے سے بھیجا گیا: {cached}/{total} فائلیں۔"
    
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
    BTN_CLOSE = "🔚 کلوز"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ باطل بولین قدر"
    ARGS_CLOSED_MSG = "بند"
    ARGS_ALL_RESET_MSG = "✅ تمام دلائل ری سیٹ ہو گئے"
    ARGS_RESET_ERROR_MSG = "❌ دلائل ری سیٹ کرنے میں خرابی"
    ARGS_INVALID_PARAM_MSG = "❌ غلط پیرامیٹر"
    ARGS_BOOL_SET_MSG = "{value} پر سیٹ کیا گیا"
    ARGS_BOOL_ALREADY_SET_MSG = "پہلے سے {value} پر سیٹ ہے"
    ARGS_INVALID_SELECT_MSG = "❌ غلط انتخاب کی قیمت"
    ARGS_VALUE_SET_MSG = "{value} پر سیٹ کیا گیا"
    ARGS_VALUE_ALREADY_SET_MSG = "پہلے سے {value} پر سیٹ ہے"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Current value:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Examples:</b>\n• <code>default</code> - Use default XFF strategy\n• <code>never</code> - Never use XFF header\n• <code>US</code> - United States country code\n• <code>GB</code> - United Kingdom country code\n• <code>DE</code> - Germany country code\n• <code>FR</code> - France country code\n• <code>JP</code> - Japan country code\n• <code>192.168.1.0/24</code> - IP block (CIDR)\n• <code>10.0.0.0/8</code> - Private IP range\n• <code>203.0.113.0/24</code> - Public IP block\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Note:</b> This replaces --geo-bypass options. Use any 2-letter country code or IP block in CIDR notation.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Example:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "براہ کرم اپنی نئی قیمت بھیجیں۔"
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Range:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "براہ کرم ایک نمبر بھیجیں۔"
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
    PLEASE_WAIT_MSG = "⏳ براہ کرم انتظار کریں ..."
    ERROR_OCCURRED_SHORT_MSG = "❌ غلطی ہوئی"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Input mode automatically closed due to inactivity (5 minutes)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ ان پٹ میں ممکنہ طور پر خطرناک مواد شامل ہے: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ ان پٹ بہت لمبا (زیادہ سے زیادہ 1000 حروف)"
    ARGS_INVALID_URL_MSG = "ulal غلط URL فارمیٹ۔ http: // یا https: // کے ساتھ شروع ہونا چاہئے"
    ARGS_INVALID_JSON_MSG = "J JSON کی غلط شکل"
    ARGS_NUMBER_RANGE_MSG = "❌ نمبر {max_val} اور {min_val} کے درمیان ہونا چاہئے"
    ARGS_INVALID_NUMBER_MSG = "number غلط نمبر کی شکل"
    ARGS_DATE_FORMAT_MSG = "❌ تاریخ YYYYMMDD فارمیٹ میں ہونی چاہئے (جیسے ، 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ سال 1900 سے 2100 کے درمیان ہونا چاہئے"
    ARGS_MONTH_RANGE_MSG = "❌ مہینہ 01 اور 12 کے درمیان ہونا چاہئے"
    ARGS_DAY_RANGE_MSG = "❌ دن 01 اور 31 کے درمیان ہونا چاہئے"
    ARGS_INVALID_DATE_MSG = "❌ تاریخ کی غلط شکل"
    ARGS_INVALID_XFF_MSG = "❌ XFF لازمی طور پر 'ڈیفالٹ' ، 'کبھی نہیں' ، کنٹری کوڈ (جیسے ، US) ، یا IP بلاک (جیسے ، 192.168.1.0/24) ہونا چاہئے۔"
    ARGS_NO_CUSTOM_MSG = "کوئی کسٹم دلائل سیٹ نہیں ہیں۔ تمام پیرامیٹرز پہلے سے طے شدہ اقدار کا استعمال کرتے ہیں۔"
    ARGS_RESET_SUCCESS_MSG = "✅ تمام دلائل ڈیفالٹس کو دوبارہ ترتیب دیتے ہیں۔"
    ARGS_TEXT_TOO_LONG_MSG = "❌ متن بہت لمبا ہے۔ زیادہ سے زیادہ 500 حروف۔"
    ARGS_ERROR_PROCESSING_MSG = "procession ان پٹ پروسیسنگ میں خرابی۔ براہ کرم دوبارہ کوشش کریں۔"
    ARGS_BOOL_INPUT_MSG = "❌ براہ کرم 'True' یا 'False' درج کریں Send As File آپشن کے لیے۔"
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ براہ کرم ایک درست نمبر فراہم کریں۔"
    ARGS_BOOL_VALUE_REQUEST_MSG = "براہ کرم <code>True</code> یا <code>False</code> بھیجیں اس آپشن کو فعال/غیر فعال کرنے کے لیے۔"
    ARGS_JSON_VALUE_REQUEST_MSG = "براہ کرم درست JSON بھیجیں۔"
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "آپ کے پاس ابھی تک کوئی ٹیگز نہیں ہیں۔"
    TAGS_MESSAGE_CLOSED_MSG = "ٹیگز پیغام بند۔"
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ سب ٹائٹلز غیر فعال اور Always Ask موڈ بند کر دیا گیا۔"
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Always Ask فعال ہے۔"
    SUBS_LANGUAGE_SET_MSG = "✅ سب ٹائٹل زبان سیٹ کی گئی: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️انتباہ: اعلی CPU اثر کی وجہ سے یہ فنکشن بہت سست ہے (تقریباً real-time) اور محدود ہے:\n"
        "- زیادہ سے زیادہ کوالٹی 720p\n"
        "- زیادہ سے زیادہ دورانیہ 1.5 گھنٹہ\n"
        "- زیادہ سے زیادہ ویڈیو سائز 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>فوری کمانڈز:</b>\n"
        "• <code>/subs off</code> - سب ٹائٹلز غیر فعال کریں\n"
        "• <code>/subs on</code> - Always Ask موڈ فعال کریں\n"
        "• <code>/subs ur</code> - زبان سیٹ کریں\n"
        "• <code>/subs ur auto</code> - AUTO/TRANS کے ساتھ زبان سیٹ کریں"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 سب ٹائٹلز غیر فعال ہیں"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} منتخب شدہ زبان: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 سب ٹائٹلز ڈاؤن لوڈ ہو رہے ہیں..."
    SUBS_DISABLED_ERROR_MSG = "❌ سب ٹائٹلز غیر فعال ہیں۔ ترتیب دینے کے لیے /subs استعمال کریں۔"
    SUBS_YOUTUBE_ONLY_MSG = "❌ سب ٹائٹل ڈاؤن لوڈ صرف YouTube کے لیے سپورٹ کیا جاتا ہے۔"
    SUBS_CAPTION_MSG = (
        "<b>💬 سب ٹائٹلز</b>\n\n"
        "<b>ویڈیو:</b> {title}\n"
        "<b>زبان:</b> {lang}\n"
        "<b>قسم:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 سب ٹائٹلز SRT-فائل صارف کو بھیج دی گئی۔"
    SUBS_ERROR_PROCESSING_MSG = "❌ سب ٹائٹل فائل پراسیس کرنے میں خرابی۔"
    SUBS_ERROR_DOWNLOAD_MSG = "❌ سب ٹائٹلز ڈاؤن لوڈ کرنے میں ناکام۔"
    SUBS_ERROR_MSG = "❌ سب ٹائٹلز ڈاؤن لوڈ کرنے میں خرابی: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ تقسیم حصے کا سائز سیٹ کیا گیا: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **غلط سائز!**\n\n"
        "**درست رینج:** 100MB سے 2GB\n\n"
        "**درست فارمیٹس:**\n"
        "• `100mb` سے `2000mb` (میگا بائٹس)\n"
        "• `0.1gb` سے `2gb` (گیگا بائٹس)\n\n"
        "**مثالیں:**\n"
        "• `/split 100mb` - 100 میگا بائٹس\n"
        "• `/split 500mb` - 500 میگا بائٹس\n"
        "• `/split 1.5gb` - 1.5 گیگا بائٹس\n"
        "• `/split 2gb` - 2 گیگا بائٹس\n"
        "• `/split 2000mb` - 2000 میگا بائٹس (2GB)\n\n"
        "**پری سیٹس:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **ویڈیو تقسیم کے لیے زیادہ سے زیادہ حصے کا سائز منتخب کریں:**\n\n"
        "**رینج:** 100MB سے 2GB\n\n"
        "**فوری کمانڈز:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**مثالیں:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "مینو بند۔"
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>بوٹ کی ترتیبات</b>\n\nایک زمرہ منتخب کریں:"
    SETTINGS_MENU_CLOSED_MSG = "مینو بند۔"
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 صاف کرنے کے اختیارات</b>\n\nصاف کرنے کے لیے منتخب کریں:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nایک عمل منتخب کریں:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 میڈیا</b>\n\nایک عمل منتخب کریں:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 معلومات</b>\n\nایک عمل منتخب کریں:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ مزید کمانڈز</b>\n\nایک عمل منتخب کریں:"
    SETTINGS_COMMAND_EXECUTED_MSG = "کمانڈ چلائی گئی۔"
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Flood کی حد۔ بعد میں کوشش کریں۔"
    SETTINGS_HINT_SENT_MSG = "اشارہ بھیجا گیا۔"
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "سرچ ہیلپر کھولا گیا۔"
    SETTINGS_UNKNOWN_COMMAND_MSG = "نامعلوم کمانڈ۔"
    SETTINGS_HINT_CLOSED_MSG = "اشارہ بند۔"
    SETTINGS_HELP_SENT_MSG = "صارف کو مدد کا متن بھیجا گیا"
    SETTINGS_MENU_OPENED_MSG = "/settings مینو کھولا گیا"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 سرچ ہیلپر بند"
    SEARCH_CLOSED_MSG = "بند"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ پراکسی {status}."
    PROXY_ERROR_SAVING_MSG = "❌ پروکسی ترتیبات محفوظ کرنے میں خرابی۔"
    PROXY_MENU_TEXT_MSG = "تمام yt-dlp آپریشنز کے لیے پروکسی سرور استعمال کرنے کو فعال/غیر فعال کریں؟"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "تمام yt-dlp آپریشنز کے لیے پروکسی سرورز ({count} دستیاب) استعمال کرنے کو فعال/غیر فعال کریں؟\n\nجب فعال ہو تو، پروکسیز {method} طریقہ استعمال کرتے ہوئے منتخب کیے جائیں گے۔"
    PROXY_MENU_CLOSED_MSG = "مینو بند۔"
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy فعال ہے۔ تمام yt-dlp آپریشنز proxy استعمال کریں گے۔"
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy فعال ہے۔ تمام yt-dlp آپریشنز {count} proxy سرورز {method} انتخاب کے طریقہ کے ساتھ استعمال کریں گے۔"
    PROXY_DISABLED_MSG = "❌ Proxy غیر فعال ہے۔"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ پروکسی ترتیبات محفوظ کرنے میں خرابی۔"
    PROXY_ENABLED_CALLBACK_MSG = "Proxy فعال ہے۔"
    PROXY_DISABLED_CALLBACK_MSG = "Proxy غیر فعال ہے۔"
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ اپنے پچھلے ڈاؤن لوڈ کے ختم ہونے تک انتظار کریں"
    AUDIO_HELP_MSG = (
        "<b>🎧 آڈیو ڈاؤن لوڈ کمانڈ</b>\n\n"
        "استعمال: <code>/audio URL</code>\n\n"
        "<b>مثالیں:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "یہ بھی دیکھیں: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "آڈیو اشارہ بند۔"
    PLAYLIST_HELP_CLOSED_MSG = "پلے لسٹ مدد بند۔"
    USERLOGS_CLOSED_MSG = "لاگز پیغام بند۔"
    HELP_CLOSED_MSG = "مدد بند۔"
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW Blur ترتیبات</b>\n\nNSFW مواد <b>{status}</b> ہے۔\n\nمنتخب کریں کہ NSFW مواد کو دھندلا کرنا ہے:"
    NSFW_MENU_CLOSED_MSG = "مینو بند۔"
    NSFW_BLUR_DISABLED_MSG = "NSFW blur غیر فعال ہے۔"
    NSFW_BLUR_ENABLED_MSG = "NSFW blur فعال ہے۔"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW blur غیر فعال ہے۔"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW blur فعال ہے۔"
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ میڈیا انفو {status}."
    MEDIAINFO_MENU_TITLE_MSG = "ڈاؤن لوڈ شدہ فائلوں کے لیے MediaInfo بھیجنے کو فعال/غیر فعال کریں؟"
    MEDIAINFO_MENU_CLOSED_MSG = "مینو بند۔"
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo فعال ہے۔ ڈاؤن لوڈ کے بعد، فائل کی معلومات بھیجی جائے گی۔"
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo غیر فعال ہے۔"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo فعال ہے۔"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo غیر فعال ہے۔"
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 List Available Formats</b>\n\n"
        "Get available video/audio formats for a URL.\n\n"
        "<b>Usage:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Examples:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 How to use format IDs:</b>\n"
        "After getting the list, use specific format ID:\n"
        "• <code>/format id 401</code> - download format 401\n"
        "• <code>/format id401</code> - same as above\n"
        "• <code>/format id140 audio</code> - download format 140 as MP3 audio\n\n"
        "This command will show all available formats that can be downloaded."
    )
    LIST_PROCESSING_MSG = "available دستیاب فارمیٹس حاصل کرنا ..."
    LIST_INVALID_URL_MSG = "❌ براہ کرم HTTP: // یا HTTPS: // کے ساتھ شروع ہونے والا ایک درست URL فراہم کریں"
    LIST_CAPTION_MSG = (
        "📃 Available formats for:\n<code>{url}</code>\n\n"
        "💡 <b>How to set format:</b>\n"
        "• <code>/format id 134</code> - Download specific format ID\n"
        "• <code>/format 720p</code> - Download by quality\n"
        "• <code>/format best</code> - Download best quality\n"
        "• <code>/format ask</code> - Always ask for quality\n\n"
        "{audio_note}\n"
        "📋 Use format ID from the list above"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Audio-only formats:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Download format 140 as MP3 audio\n"
        "• <code>/format id140 audio</code> - same as above\n"
        "These will be downloaded as MP3 audio files.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "form فارمیٹس فائل بھیجنے میں غلطی: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Failed to get formats:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ کمانڈ پر کارروائی کرتے وقت ایک خرابی پیش آگئی"
    LIST_ERROR_CALLBACK_MSG = "خرابی پیش آئی"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 How to use format IDs:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "فہرست حاصل کرنے کے بعد، مخصوص فارمیٹ ID استعمال کریں:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - فارمیٹ 401 ڈاؤن لوڈ کریں\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - اوپر کی طرح\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - فارمیٹ 140 کو MP3 آڈیو کے طور پر ڈاؤن لوڈ کریں\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - اوپر کی طرح\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 صرف آڈیو فارمیٹس کا پتہ چلا: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "یہ فارمیٹس MP3 آڈیو فائلوں کے طور پر ڈاؤن لوڈ کیے جائیں گے۔\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>صرف ویڈیو فارمیٹس:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 اوپر کی فہرست سے فارمیٹ ID استعمال کریں"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>استعمال:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>مثالیں:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - بہترین کوالٹی\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p یا کم\n"
        "• /link 720p https://youtube.com/watch?v=... - اوپر کی طرح\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K یا کم\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K یا کم"
        "</blockquote>\n\n"
        "<b>کوالٹی:</b> 1 سے 10000 تک (مثلاً، 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ براہ کرم درست URL فراہم کریں"
    LINK_PROCESSING_MSG = "🔗 براہ راست لنک حاصل کیا جا رہا ہے..."
    LINK_DURATION_MSG = "⏱ <b>دورانیہ:</b> {duration} سیکنڈ\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>ویڈیو سٹریم:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>آڈیو سٹریم:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **کی بورڈ کی ترتیب اپ ڈیٹ ہو گئی!**\n\nنئی ترتیب: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **غلط دلیل!**\n\n"
        "درست اختیارات: `off`, `1x3`, `2x3`, `full`\n\n"
        "مثال: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **کی بورڈ کی ترتیبات**\n\n"
        "موجودہ: **{current}**\n\n"
        "ایک اختیار منتخب کریں:\n\n"
        "یا استعمال کریں: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 کی بورڈ فعال ہے!"
    KEYBOARD_HIDDEN_MSG = "⌨️ کی بورڈ چھپا ہوا ہے"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3 کی بورڈ فعال ہے!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3 کی بورڈ فعال ہے!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 ایموجی کی بورڈ فعال ہے!"
    KEYBOARD_ERROR_APPLYING_MSG = "کی بورڈ کی ترتیب {setting} لاگو کرنے میں خرابی: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ فارمیٹ سیٹ کیا گیا: ہمیشہ پوچھیں۔ آپ کو ہر بار URL بھیجنے پر کوالٹی کے لیے پوچھا جائے گا۔"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ فارمیٹ سیٹ کیا گیا: ہمیشہ پوچھیں۔ اب آپ کو ہر بار URL بھیجنے پر کوالٹی کے لیے پوچھا جائے گا۔"
    FORMAT_BEST_UPDATED_MSG = "✅ فارمیٹ بہترین کوالٹی (AVC+MP4 ترجیح) پر اپ ڈیٹ کیا گیا:\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ فارمیٹ ID {id} پر اپ ڈیٹ کیا گیا:\n{format}\n\n💡 <b>نوٹ:</b> اگر یہ صرف آڈیو فارمیٹ ہے، تو یہ MP3 آڈیو فائل کے طور پر ڈاؤن لوڈ ہوگا۔"
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ فارمیٹ ID {id} (صرف آڈیو) پر اپ ڈیٹ کیا گیا:\n{format}\n\n💡 یہ MP3 آڈیو فائل کے طور پر ڈاؤن لوڈ ہوگا۔"
    FORMAT_QUALITY_UPDATED_MSG = "✅ فارمیٹ کوالٹی {quality} پر اپ ڈیٹ کیا گیا:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ فارمیٹ اپ ڈیٹ کیا گیا:\n{format}"
    FORMAT_MENU_MSG = (
        "ایک فارمیٹ آپشن منتخب کریں یا کسٹم بھیجیں:\n"
        "• <code>/format &lt;format_string&gt;</code> - کسٹم فارمیٹ\n"
        "• <code>/format 720</code> - 720p کوالٹی\n"
        "• <code>/format 4k</code> - 4K کوالٹی\n"
        "• <code>/format 8k</code> - 8K کوالٹی\n"
        "• <code>/format id 401</code> - مخصوص فارمیٹ ID\n"
        "• <code>/format ask</code> - ہمیشہ مینو دکھائیں\n"
        "• <code>/format best</code> - bv+ba/best کوالٹی"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "کسٹم فارمیٹ استعمال کرنے کے لیے، کمانڈ اس شکل میں بھیجیں:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "<code>bestvideo+bestaudio/best</code> کو اپنی مطلوبہ فارمیٹ سٹرنگ سے تبدیل کریں۔"
    )
    FORMAT_RESOLUTION_MENU_MSG = "اپنی مطلوبہ ریزولوشن اور کوڈیک منتخب کریں:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ فارمیٹ سیٹ کیا گیا: ہمیشہ پوچھیں۔ اب آپ کو ہر بار URL بھیجنے پر کوالٹی کے لیے پوچھا جائے گا۔"
    FORMAT_UPDATED_MSG = "✅ فارمیٹ اپ ڈیٹ کیا گیا:\n{format}"
    FORMAT_SAVED_MSG = "✅ فارمیٹ محفوظ کیا گیا۔"
    FORMAT_CHOICE_UPDATED_MSG = "✅ فارمیٹ کا انتخاب اپ ڈیٹ کیا گیا۔"
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "کسٹم فارمیٹ مینو بند"
    FORMAT_CODEC_SET_MSG = "✅ کوڈیک {codec} پر سیٹ کیا گیا"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ براؤزر کا انتخاب اپ ڈیٹ کیا گیا۔"
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Access denied. Admin only."
    ACCESS_DENIED_ADMIN = "❌ رسائی سے انکار. صرف ایڈمن۔"
    WELCOME_MASTER = "خوش آمدید ماسٹر 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ معذرت ... ڈاؤن لوڈ کے دوران کچھ خرابی پیش آگئی۔"
    SIZE_LIMIT_EXCEEDED = "❌ فائل کا سائز {max_size_gb} GB حد سے تجاوز کرتا ہے۔ براہ کرم اجازت شدہ سائز میں ایک چھوٹی فائل منتخب کریں۔"
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ اسکرپٹ نہیں ملا: {script_path}"
    ADMIN_DOWNLOADING_MSG = "{script_path} کا استعمال کرتے ہوئے تازہ فائر بیس ڈمپ ڈاؤن لوڈ کرنا ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ فائربیس کیشے کو کامیابی کے ساتھ دوبارہ لوڈ کیا گیا!"
    ADMIN_CACHE_FAILED_MSG = "fire فائر بیس کیشے کو دوبارہ لوڈ کرنے میں ناکام۔ چیک کریں کہ آیا {cache_file} موجود ہے۔"
    ADMIN_ERROR_RELOADING_MSG = "❌ کیشے کو دوبارہ لوڈ کرنے میں غلطی: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Error running {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b> ✅ پرومو پیغام دوسرے تمام صارفین کو بھیجا گیا </b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Cannot send the promo message. Try replying to a message\nOr some error occurred</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b> ❌ صارف نے ابھی تک کوئی مواد ڈاؤن لوڈ نہیں کیا ... </b> لاگوں میں موجود نہیں ہے"
    ADMIN_INVALID_COMMAND_MSG = "❌ غلط کمانڈ"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ No data found in cache for <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡 قطار خالی ہے - ابھی تک کسی نے چینل نہیں چھوڑا۔"
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Ban queue</b>\nPending total: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <کوڈ> {last_left} </code> {username}_{name}1__ (بائیں: {user_id})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… اور {extra} مزید صارفین۔"
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "/block_user show • all • auto • 10s استعمال کریں"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "cessers صارفین کو قطار سے مسدود: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙ آٹو بلاکنگ فعال: نئے لیورز پر فوری طور پر پابندی عائد کردی جائے گی۔"
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ آٹو بلاکنگ غیر فعال۔"
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "__ ہر {interval} پر طے شدہ آٹو بلاک ونڈو سیٹ کریں۔"
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 آخری {hours} گھنٹے (2 دن) کے لئے چینل کی سرگرمی لاگ ان۔"
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 آخری {left} گھنٹے (2 دن): __v{joined}ں شامل ہوئے ، بائیں __va{hours}"
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "__ آخری {hours} گھنٹے (2 دن) کے لئے کوئی سرگرمی نہیں ہے۔"
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "کل: __ {left} شامل ہوا ، __ __v{joined}ئیں۔"
    CHANNEL_GUARD_NO_ACCESS_MSG = "channel چینل کی سرگرمی لاگ تک رسائی نہیں۔ بوٹس ایڈمن لاگز نہیں پڑھ سکتے ہیں۔ اس خصوصیت کو قابل بنانے کے لئے صارف سیشن کے ساتھ تشکیل میں چینل_گارڈ_سیشن_سٹرنگ فراہم کریں۔"
    BAN_TIME_USAGE_MSG = "❌ استعمال: {command} <10s | 6m | 5h | 4d | 3W | 2m | 1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "10 10s ، 6m ، 5h ، 4d ، 3W ، 2M یا 1y جیسے فارمیٹس کا استعمال کریں۔"
    BAN_TIME_SET_MSG = "🕒 چینل لاگ اسکین وقفہ {interval} پر سیٹ کریں۔"
    BAN_TIME_REPORT_MSG = (
        "🛡️ Channel scan report\n"
        "Run at: {run_ts}\n"
        "Interval: {interval}\n"
        "New leavers: {new_leavers}\n"
        "Auto bans: {auto_banned}\n"
        "Pending: {pending}\n"
        "Last event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ استعمال: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 ایڈمن ایڈمن کو حذف نہیں کر سکتا"
    ADMIN_USER_BLOCKED_MSG = "صارف بلاک 🔒❌\n \nID: <code>{user_id}</code>\nبلاک کی تاریخ: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> پہلے سے بلاک ہے ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 معذرت! آپ ایڈمن نہیں ہیں"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ استعمال: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "صارف ان بلاک 🔓✅\n \nID: <code>{user_id}</code>\nان بلاک کی تاریخ: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> پہلے سے ان بلاک ہے ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ ان بلاک شدہ صارفین: {count}\n⏱ ٹائم اسٹیمپ: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ استعمال: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "صارف کو نظر انداز کیا گیا 👁️❌\n \nشناخت: <code>{user_id}</code>\nنظر انداز کی تاریخ: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> پہلے سے نظر انداز کیا جا رہا ہے ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ استعمال: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "صارف اب نظر انداز نہیں کیا جا رہا 👁️✅\n \nشناخت: <code>{user_id}</code>\nنظر انداز نہ کرنے کی تاریخ: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> نظر انداز نہیں کیا جا رہا ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>بوٹ چلنے کا وقت -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ براہ کرم cache صاف کرنے کے لیے URL فراہم کریں۔\nاستعمال: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ براہ کرم درست URL فراہم کریں۔\nاستعمال: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ URL کے لیے cache کامیابی سے صاف کیا گیا:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ اس لنک کے لیے کوئی cache نہیں ملا۔"
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ cache صاف کرنے میں خرابی: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ رسائی مسترد۔ صرف ایڈمن۔"
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ پورن فہرست اپ ڈیٹ اسکرپٹ چل رہی ہے: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ اسکرپٹ کامیابی سے مکمل ہوئی!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ اسکرپٹ کامیابی سے مکمل ہوئی!\n\nآؤٹ پٹ:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ اسکرپٹ ریٹرن کوڈ {returncode} کے ساتھ ناکام:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ اسکرپٹ چلانے میں خرابی: {error}"
    ADMIN_RELOADING_PORN_MSG = "porn فحش اور ڈومین سے متعلق کیشوں کو دوبارہ لوڈ کرنا ..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Porn caches reloaded successfully!\n\n"
        "📊 Current cache status:\n"
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
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ فحش کیشے کو دوبارہ لوڈ کرنے میں غلطی: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Please provide a URL to check.\nUsage: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Please provide a valid URL.\nUsage: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Checking URL for NSFW content...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Porn Check Result</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Status:</b> <b>{status_text}</b>\n\n"
        "<b>Explanation:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ URL کی جانچ پڑتال میں غلطی: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "کوکیز صاف کی گئیں۔"
    CLEAN_LOGS_CLEANED_MSG = "لاگز صاف کیے گئے۔"
    CLEAN_TAGS_CLEANED_MSG = "ٹیگز صاف کیے گئے۔"
    CLEAN_FORMAT_CLEANED_MSG = "فارمیٹ صاف کیا گیا۔"
    CLEAN_SPLIT_CLEANED_MSG = "تقسیم صاف کی گئی۔"
    CLEAN_MEDIAINFO_CLEANED_MSG = "میڈیا انفو صاف کیا گیا۔"
    CLEAN_SUBS_CLEANED_MSG = "سب ٹائٹل کی ترتیبات صاف کی گئیں۔"
    CLEAN_KEYBOARD_CLEANED_MSG = "کی بورڈ کی ترتیبات صاف کی گئیں۔"
    CLEAN_ARGS_CLEANED_MSG = "دلائل کی ترتیبات صاف کی گئیں۔"
    CLEAN_NSFW_CLEANED_MSG = "NSFW کی ترتیبات صاف کی گئیں۔"
    CLEAN_PROXY_CLEANED_MSG = "پروکسی کی ترتیبات صاف کی گئیں۔"
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Flood wait کی ترتیبات صاف کی گئیں۔"
    CLEAN_ALL_CLEANED_MSG = "تمام فائلیں صاف کی گئیں۔"
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nایک عمل منتخب کریں:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ کوکی فائل محفوظ کی گئی"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ غیر-YouTube کوکیز کے لیے تصدیق چھوڑ دی گئی"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ کوکی فائل موجود ہے لیکن غلط فارمیٹ میں ہے"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ کوکی فائل نہیں ملی۔"
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 YouTube کوکیز کا ٹیسٹ شروع ہو رہا ہے...\n\nبراہ کرم انتظار کریں جب میں آپ کی کوکیز چیک اور تصدیق کر رہا ہوں۔"
    COOKIES_YOUTUBE_WORKING_MSG = "✅ آپ کی موجودہ YouTube کوکیز صحیح طریقے سے کام کر رہی ہیں!\n\nنئی ڈاؤن لوڈ کرنے کی ضرورت نہیں ہے۔"
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ آپ کی موجودہ YouTube کوکیز ختم ہو گئیں یا غلط ہیں۔\n\n🔄 نئی کوکیز ڈاؤن لوڈ کی جا رہی ہیں..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} کوکی ماخذ ترتیب نہیں دیا گیا!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} کوکی ماخذ .txt فائل ہونا چاہیے!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ رینج کی حد سے تجاوز: {range_count} فائلیں درخواست کی گئیں (زیادہ سے زیادہ {max_img_files})۔\n\nزیادہ سے زیادہ دستیاب فائلیں ڈاؤن لوڈ کرنے کے لیے ان کمانڈز میں سے ایک استعمال کریں:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚بند"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ میڈیا کی حد سے تجاوز: {count} فائلیں درخواست کی گئیں (زیادہ سے زیادہ {max_count})۔\n\nزیادہ سے زیادہ دستیاب فائلیں ڈاؤن لوڈ کرنے کے لیے ان کمانڈز میں سے ایک استعمال کریں:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 لنک سے <b>{count}</b> میڈیا آئٹمز ملے"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "ڈاؤن لوڈ رینج منتخب کریں:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "براؤزر کی نقل"
    ARGS_REFERER_DESC_MSG = "Referer ہیڈر"
    ARGS_USER_AGENT_DESC_MSG = "User-Agent ہیڈر"
    ARGS_GEO_BYPASS_DESC_MSG = "جغرافیائی پابندیوں کو بائی پاس کریں"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "SSL سرٹیفکیٹ چیک کریں"
    ARGS_LIVE_FROM_START_DESC_MSG = "شروع سے لائیو سٹریمز ڈاؤن لوڈ کریں"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "شروع سے لائیو سٹریمز ڈاؤن لوڈ نہ کریں"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "HLS ویڈیوز کے لیے MPEG-TS کنٹینر استعمال کریں"
    ARGS_NO_PLAYLIST_DESC_MSG = "صرف ایک ویڈیو ڈاؤن لوڈ کریں، پلے لسٹ نہیں"
    ARGS_NO_PART_DESC_MSG = ".part فائلیں استعمال نہ کریں"
    ARGS_NO_CONTINUE_DESC_MSG = "جزوی ڈاؤن لوڈز دوبارہ شروع نہ کریں"
    ARGS_AUDIO_FORMAT_DESC_MSG = "ایکسٹریکشن کے لیے آڈیو فارمیٹ"
    ARGS_EMBED_METADATA_DESC_MSG = "ویڈیو فائل میں میٹا ڈیٹا ایمبیڈ کریں"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "ویڈیو فائل میں تھمب نیل ایمبیڈ کریں"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "تھمب نیل فائل میں لکھیں"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "ڈاؤن لوڈ کرنے کے لیے بیک وقت fragments کی تعداد"
    ARGS_FORCE_IPV4_DESC_MSG = "IPv4 کنکشنز پر مجبور کریں"
    ARGS_FORCE_IPV6_DESC_MSG = "IPv6 کنکشنز پر مجبور کریں"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For ہیڈر کی حکمت عملی"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP chunk سائز (بائٹس)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "سب ٹائٹل ڈاؤن لوڈ سے پہلے سلیپ (سیکنڈ)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "پرانی سرور کنکشنز کی اجازت دیں"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "HTTPS سرٹیفکیٹ کی توثیق کو دبائیں"
    ARGS_USERNAME_DESC_MSG = "اکاؤنٹ کا صارف نام"
    ARGS_PASSWORD_DESC_MSG = "اکاؤنٹ کا پاس ورڈ"
    ARGS_TWOFACTOR_DESC_MSG = "دو فیکٹر تصدیق کا کوڈ"
    ARGS_IGNORE_ERRORS_DESC_MSG = "ڈاؤن لوڈ کی خرابیوں کو نظر انداز کریں اور جاری رکھیں"
    ARGS_MIN_FILESIZE_DESC_MSG = "کم سے کم فائل سائز (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "زیادہ سے زیادہ فائل سائز (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "ڈاؤن لوڈ کرنے کے لیے پلے لسٹ آئٹمز (مثلاً، 1,3,5 یا 1-5)"
    ARGS_DATE_DESC_MSG = "اس تاریخ پر اپ لوڈ کیے گئے ویڈیوز ڈاؤن لوڈ کریں (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "اس تاریخ سے پہلے اپ لوڈ کیے گئے ویڈیوز ڈاؤن لوڈ کریں (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "اس تاریخ کے بعد اپ لوڈ کیے گئے ویڈیوز ڈاؤن لوڈ کریں (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "کسٹم HTTP ہیڈرز (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "درخواستوں کے درمیان سلیپ انٹرویل (سیکنڈ)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "زیادہ سے زیادہ سلیپ انٹرویل (سیکنڈ)"
    ARGS_RETRIES_DESC_MSG = "دوبارہ کوششوں کی تعداد"
    ARGS_VIDEO_FORMAT_DESC_MSG = "ویڈیو کنٹینر فارمیٹ"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "مرجنگ کے لیے آؤٹ پٹ کنٹینر فارمیٹ"
    ARGS_SEND_AS_FILE_DESC_MSG = "تمام میڈیا کو میڈیا کے بجائے دستاویز کے طور پر بھیجیں"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "نقل"
    ARGS_REFERER_SHORT_MSG = "ریفرر"
    ARGS_GEO_BYPASS_SHORT_MSG = "جیو بائی پاس"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "سرٹیفکیٹ چیک"
    ARGS_LIVE_FROM_START_SHORT_MSG = "لائیو شروع"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "لائیو شروع نہیں"
    ARGS_USER_AGENT_SHORT_MSG = "یوزر ایجنٹ"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "پلے لسٹ نہیں"
    ARGS_NO_PART_SHORT_MSG = "Part نہیں"
    ARGS_NO_CONTINUE_SHORT_MSG = "Continue نہیں"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "آڈیو فارمیٹ"
    ARGS_EMBED_METADATA_SHORT_MSG = "Meta ایمبیڈ"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Thumb ایمبیڈ"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Thumb لکھیں"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "بیک وقت"
    ARGS_FORCE_IPV4_SHORT_MSG = "IPv4 پر مجبور"
    ARGS_FORCE_IPV6_SHORT_MSG = "IPv6 پر مجبور"
    ARGS_XFF_SHORT_MSG = "XFF ہیڈر"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Chunk سائز"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Subs سلیپ"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "پرانا کنکشن"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "سرٹیفکیٹ چیک نہیں"
    ARGS_USERNAME_SHORT_MSG = "صارف نام"
    ARGS_PASSWORD_SHORT_MSG = "پاس ورڈ"
    ARGS_TWOFACTOR_SHORT_MSG = "2 ایف اے"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "خرابیوں کو نظر انداز"
    ARGS_MIN_FILESIZE_SHORT_MSG = "کم سائز"
    ARGS_MAX_FILESIZE_SHORT_MSG = "زیادہ سائز"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "پلے لسٹ آئٹمز"
    ARGS_DATE_SHORT_MSG = "تاریخ"
    ARGS_DATEBEFORE_SHORT_MSG = "تاریخ سے پہلے"
    ARGS_DATEAFTER_SHORT_MSG = "تاریخ کے بعد"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP ہیڈرز"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "سلیپ انٹرویل"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "زیادہ سلیپ"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "ویڈیو فارمیٹ"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "مرج فارمیٹ"
    ARGS_SEND_AS_FILE_SHORT_MSG = "فائل کے طور پر بھیجیں"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ فائل بہت بڑی ہے۔ زیادہ سے زیادہ سائز 100 KB ہے۔"
    COOKIES_INVALID_FORMAT_MSG = "❌ صرف .txt فارمیٹ کی فائلیں اجازت یافتہ ہیں۔"
    COOKIES_INVALID_COOKIE_MSG = "❌ فائل cookie.txt کی طرح نہیں لگتی (کوئی لائن '# Netscape HTTP Cookie File' نہیں ہے)۔"
    COOKIES_ERROR_READING_MSG = "❌ فائل پڑھنے میں خرابی: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ کوکی فائل موجود ہے اور درست فارمیٹ میں ہے"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} کوکی فائل بہت بڑی ہے! زیادہ سے زیادہ 100KB، ملا {size}KB۔"
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} کوکی فائل ڈاؤن لوڈ کی گئی اور آپ کے فولڈر میں cookie.txt کے طور پر محفوظ کی گئی۔</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} کوکی ماخذ دستیاب نہیں ہے (حالت {status})۔ براہ کرم بعد میں دوبارہ کوشش کریں۔"
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ {service} کوکی فائل ڈاؤن لوڈ کرنے میں خرابی۔ براہ کرم بعد میں دوبارہ کوشش کریں۔"
    COOKIES_USER_PROVIDED_MSG = "<b>✅ صارف نے ایک نئی کوکی فائل فراہم کی۔</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ کوکی کامیابی سے اپ ڈیٹ کی گئی:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ درست کوکی نہیں ہے۔</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube کوکی ماخذ ترتیب نہیں دیے گئے!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 YouTube کوکیز ڈاؤن لوڈ اور چیک کی جا رہی ہیں...\n\nکوشش {attempt} از {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ رسائی مسترد۔ صرف ایڈمن۔"
    ADMIN_USER_LOGS_TOTAL_MSG = "کل: <b>{total}</b>\n<b>{user_id}</b> - لاگز (آخری 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 کی بورڈ فعال ہے!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ سب ٹائٹل زبان سیٹ کی گئی: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ سب ٹائٹل زبان سیٹ کی گئی: {flag} {name} AUTO/TRANS کے ساتھ فعال۔"
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "سب ٹائٹل زبان مینو بند۔"
    SUBS_DOWNLOADING_MSG = "💬 سب ٹائٹلز ڈاؤن لوڈ ہو رہے ہیں..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Firebase cache میموری میں دوبارہ لوڈ ہو رہی ہے..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ کوئی COOKIE_URL ترتیب نہیں دیا گیا۔ /cookie استعمال کریں یا cookie.txt اپ لوڈ کریں۔"
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 ریموٹ URL سے کوکیز ڈاؤن لوڈ کی جا رہی ہیں..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL .txt فائل کی طرف اشارہ کرنا چاہیے۔"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fallback کوکی فائل بہت بڑی ہے (>100KB)۔"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube کوکی فائل fallback کے ذریعے ڈاؤن لوڈ کی گئی اور cookie.txt کے طور پر محفوظ کی گئی"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fallback کوکی ماخذ دستیاب نہیں ہے (حالت {status})۔ /cookie استعمال کریں یا cookie.txt اپ لوڈ کریں۔"
    COOKIE_FALLBACK_ERROR_MSG = "❌ Fallback کوکی ڈاؤن لوڈ کرنے میں خرابی۔ /cookie استعمال کریں یا cookie.txt اپ لوڈ کریں۔"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Fallback کوکی ڈاؤن لوڈ کے دوران غیر متوقع خرابی۔"
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} براؤزر انسٹال نہیں ہے۔"
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ کوکیز براؤزر استعمال کرتے ہوئے محفوظ کی گئیں: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ کوکیز محفوظ کرنے میں ناکام: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube کوکیز صحیح طریقے سے کام کر رہی ہیں"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube کوکیز ختم ہو گئیں یا غلط ہیں\n\nنئی کوکیز حاصل کرنے کے لیے /cookie استعمال کریں"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - کسٹم فارمیٹ\n• <code>/format 720</code> - 720p کوالٹی\n• <code>/format 4k</code> - 4K کوالٹی"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "اشارہ بھیجا گیا۔"
    FORMAT_MKV_TOGGLE_MSG = "MKV اب {status} ہے"
    COOKIES_NO_REMOTE_URL_MSG = "❌ کوئی ریموٹ URL ترتیب نہیں دیا گیا"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ غلط فائل فارمیٹ"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ فائل بہت بڑی ہے"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ کوکیز کامیابی سے ڈاؤن لوڈ کی گئیں"
    COOKIES_SERVER_ERROR_MSG = "❌ سرور خرابی {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ ڈاؤن لوڈ ناکام"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ غیر متوقع خرابی"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ براؤزر انسٹال نہیں ہے۔"
    COOKIES_MENU_CLOSED_MSG = "مینو بند۔"
    COOKIES_HINT_CLOSED_MSG = "کوکی اشارہ بند۔"
    IMG_HELP_CLOSED_MSG = "مدد بند۔"
    SUBS_LANGUAGE_UPDATED_MSG = "سب ٹائٹل زبان کی ترتیبات اپ ڈیٹ کی گئیں۔"
    SUBS_MENU_CLOSED_MSG = "سب ٹائٹل زبان مینو بند۔"
    KEYBOARD_SET_TO_MSG = "کی بورڈ {setting} پر سیٹ کیا گیا"
    KEYBOARD_ERROR_PROCESSING_MSG = "ترتیب پراسیس کرنے میں خرابی"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo فعال ہے۔"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo غیر فعال ہے۔"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW blur غیر فعال ہے۔"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW blur فعال ہے۔"
    SETTINGS_MENU_CLOSED_MSG = "مینو بند۔"
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Flood wait فعال ہے۔ بعد میں کوشش کریں۔"
    OTHER_HELP_CLOSED_MSG = "مدد بند۔"
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "لاگز پیغام بند۔"
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "مینو بند۔"
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "غلط سائز۔"
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ MediaInfo بھیجنے میں خرابی: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ خرابی پیش آئی: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote> 📊 mediainfo </blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - تمام لاگز"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - تمام {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 ریموٹ URL سے ڈاؤن لوڈ کریں"
    BROWSER_OPEN_BUTTON_MSG = "🌐 براؤزر کھولیں"
    SELECT_BROWSER_MSG = "کوکیز ڈاؤن لوڈ کرنے کے لیے ایک براؤزر منتخب کریں:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "اس سسٹم پر کوئی براؤزر نہیں ملا۔ آپ ریموٹ URL سے کوکیز ڈاؤن لوڈ کر سکتے ہیں یا براؤزر کی حالت مانیٹر کر سکتے ہیں:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>براؤزر کھولیں</b> - منی-ایپ میں براؤزر کی حالت مانیٹر کرنے کے لیے"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ /check_cookie چلانے میں ناکام"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Flood کی حد۔ بعد میں کوشش کریں۔"
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ براؤزر کوکی مینو کھولنے میں ناکام"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "کوکی کے طور پر محفوظ کریں اشارہ بند۔"
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>استعمال:</b>\n<code>/link [quality] URL</code>\n\n<b>مثالیں:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - بہترین کوالٹی\n• /link 720 https://youtube.com/watch?v=... - 720p یا کم\n• /link 720p https://youtube.com/watch?v=... - اوپر کی طرح\n• /link 4k https://youtube.com/watch?v=... - 4K یا کم\n• /link 8k https://youtube.com/watch?v=... - 8K یا کم</blockquote>\n\n<b>کوالٹی:</b> 1 سے 10000 تک (مثلاً، 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K کوالٹی"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>براہ راست لنک حاصل کیا گیا</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>فارمیٹ:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>آڈیو سٹریم:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ سٹریم لنکس حاصل کرنے میں ناکام"
    LINK_ERROR_GETTING_MSG = "❌ <b>لنک حاصل کرنے میں خرابی:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ غلط YouTube کوکی انڈیکس: {selected_index}۔ دستیاب رینج 1-{total_urls} ہے"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 YouTube کوکیز ڈاؤن لوڈ اور چیک کی جا رہی ہیں...\n\nکوشش {attempt} از {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 YouTube کوکیز ڈاؤن لوڈ اور چیک کی جا رہی ہیں...\n\nکوشش {attempt} از {total}\n🔍 کوکیز ٹیسٹ کی جا رہی ہیں..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube کوکیز کامیابی سے ڈاؤن لوڈ اور تصدیق کی گئیں!\n\nاستعمال شدہ ماخذ {source} از {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ تمام YouTube کوکیز ختم ہو گئیں یا دستیاب نہیں ہیں!\n\nانہیں تبدیل کرنے کے لیے بوٹ ایڈمنسٹریٹر سے رابطہ کریں۔"
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube کوکی retry کی حد سے تجاوز!\n\n🔢 زیادہ سے زیادہ: {limit} فی گھنٹہ کوششیں\n⏰ براہ کرم بعد میں دوبارہ کوشش کریں"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ ٹیگ #{wrong} میں ممنوعہ حروف شامل ہیں۔ صرف حروف، ہندسے اور _ کی اجازت ہے۔\nبراہ کرم استعمال کریں: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **غلط دلیل!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ سب ٹائٹل زبان سیٹ کی گئی: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "مثال: `/subs ur auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} منتخب شدہ زبان: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Always Ask موڈ {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 سب ٹائٹلز غیر فعال ہیں"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 سب ٹائٹل کی ترتیبات</b>\n\n{status_text}\n\nسب ٹائٹل زبان منتخب کریں:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - سب ٹائٹلز غیر فعال کریں\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 سب ٹائٹل کی ترتیبات</b>\n\n{status_text}\n\nسب ٹائٹل زبان منتخب کریں:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>عنوان:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>دورانیہ:</b> {duration} سیکنڈ\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>ویڈیو سٹریم:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- زیادہ سے زیادہ کوالٹی 720p\n- زیادہ سے زیادہ دورانیہ 1.5 گھنٹہ\n- زیادہ سے زیادہ ویڈیو سائز 500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️انتباہ: اعلی CPU اثر کی وجہ سے یہ فنکشن بہت سست ہے (تقریباً real-time) اور محدود ہے:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>فوری کمانڈز:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - سب ٹائٹلز غیر فعال کریں\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - Always Ask موڈ فعال کریں\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ur` - زبان سیٹ کریں\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ur auto` - AUTO/TRANS کے ساتھ زبان سیٹ کریں\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - Always Ask موڈ فعال کریں\n"
    SUBS_AUTO_SUBS_TEXT = " (خودکار-سب ٹائٹلز)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ خودکار-سب ٹائٹلز موڈ {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "کمانڈ کے ذریعے غیر فعال: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "سبس ہمیشہ کمانڈ کے ذریعے فعال پوچھیں: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "کمانڈ کے ذریعے سبس لینگویج سیٹ کریں: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "سبس لینگویج + آٹو موڈ کمانڈ کے ذریعے سیٹ کریں: {arg} آٹو"
    SUBS_MENU_OPENED_LOG_MSG = "صارف کھولا /سبس مینو۔"
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "صارف نے سب ٹائٹل کی زبان مرتب کی: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "صارف نے آٹو/ٹرانس موڈ کو ٹوگل کیا: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "صارف ٹوگل ہمیشہ موڈ سے پوچھیں: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "صارف نے براؤزر سے کوکیز کی درخواست کی۔"
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "براؤزر سلیکشن کی بورڈ صرف انسٹال براؤزرز کے ساتھ بھیجا گیا ہے۔"
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "براؤزر کا انتخاب بند۔"
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "فال بیک بیک کوکی_ورل کامیابی کے ساتھ استعمال ہوا (ماخذ پوشیدہ)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "فال بیک بیک کوکی_ورل ناکام: حیثیت = {status} (پوشیدہ)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "فال بیک کوکی_ورل غیر متوقع غلطی: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "براؤزر {browser} انسٹال نہیں ہوا۔"
    COOKIES_SAVED_BROWSER_LOG_MSG = "براؤزر کا استعمال کرتے ہوئے کوکیز کو محفوظ کیا گیا: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "صارف {user_id} کے لئے کوکی فائل محفوظ کی گئی ہے۔"
    COOKIES_FILE_WORKING_LOG_MSG = "کوکی فائل موجود ہے ، اس کی درست شکل ہے ، اور یوٹیوب کوکیز کام کر رہی ہیں۔"
    COOKIES_FILE_EXPIRED_LOG_MSG = "کوکی فائل موجود ہے اور اس کی درست شکل ہے ، لیکن یوٹیوب کوکیز کی میعاد ختم ہوگئی ہے۔"
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "کوکی فائل موجود ہے اور اس کی درست شکل ہے۔"
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "کوکی فائل موجود ہے لیکن اس کی غلط شکل ہے۔"
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "کوکی فائل نہیں ملی۔"
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{user_id} کوکی یو آر ایل صارف کے لئے خالی ہے {service}۔"
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} کوکی یو آر ایل نہیں ہے .Txt (پوشیدہ)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{size} کوکی فائل بہت بڑی: __v{service}ئٹس (ماخذ پوشیدہ)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{user_id} کوکی فائل صارف کے لئے ڈاؤن لوڈ کی گئی {service} (ماخذ پوشیدہ)۔"
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "اسکرپٹ نہیں ملا: {user_id}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "ابتدائی سٹیٹس پیغام بھیجنے میں ناکام"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Error running {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "آٹو ٹاسک کے ذریعہ فائربیس کیشے کو دوبارہ لوڈ کیا گیا۔"
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "فائر بیس کیشے ایڈمن کے ذریعہ دوبارہ لوڈ۔"
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "فائر بیس کیشے کو دوبارہ لوڈ کرنے میں غلطی: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Broadcast initiated. Text:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "نشریاتی پیغام تمام صارفین کو بھیجا گیا۔"
    ADMIN_BROADCAST_FAILED_LOG_MSG = "پیغام نشر کرنے میں ناکام: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "ایڈمن {url} url کے لئے صاف کیشے: __va{user_id}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "ایڈمن {script_path} شروع شدہ فحش فہرست کی تازہ کاری اسکر{user_id}_0__"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "فحش فہرست کی تازہ کاری اسکرپٹ ایڈمن {user_id} کے ذریعہ کامیابی کے ساتھ مکمل ہوئی"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "فحش فہرست کی تازہ کاری اسکرپٹ ایڈمن کے ذریعہ ناکام ہوگئی {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "ایڈمن {script_path} غیر موجود اسکرپٹ چلانے کی کوشش {user_id}_0__"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "ایڈمن {user_id} کے ذریعہ فحش اپ ڈیٹ اسکرپٹ چلانے میں غلطی: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "ایڈمن {user_id} نے پورن cache دوبارہ لوڈ شروع کیا"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "ایڈمن {user_id} کے ذریعہ فحش کیشے کو دوبارہ لوڈ کرنے میں غلطی: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "ایڈمن {status} NSFW کے لئے URL چیک کیا: _{url}- نتیجہ: __var{user_id}"
    
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
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "کسٹم فارمیٹ مینو بند"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "{user_id} سے صارف {url} کے لئے براہ راست لنک نکالا گیا"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Failed to extract direct link for user {user_id} from {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Error in link command for user {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "صارف {setting} {user_id} پر کی بورڈ مرتب کریں"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "صارف {setting} {user_id} پر کی بورڈ مرتب کریں"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "میڈیا انفو کمانڈ کے ذریعے سیٹ کریں: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "صارف کھولا /میڈیا انفو مینو۔"
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "میڈیا انفو: بند۔"
    MEDIAINFO_ENABLED_LOG_MSG = "میڈیا انفو فعال."
    MEDIAINFO_DISABLED_LOG_MSG = "میڈیا انفو غیر فعال۔"
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "اسپلٹ سائز {size} بائٹس پر دلیل کے ذریعے سیٹ کیا گیا ہے۔"
    SPLIT_MENU_OPENED_LOG_MSG = "صارف کھولا /تقسیم مینو۔"
    SPLIT_SELECTION_CLOSED_LOG_MSG = "تقسیم کا انتخاب بند ہے۔"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Split size set to {size} bytes."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "پراکسی سیٹ کے ذریعے کمانڈ: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "صارف کھولا /پراکسی مینو۔"
    PROXY_MENU_CLOSED_LOG_MSG = "پراکسی: بند۔"
    PROXY_ENABLED_LOG_MSG = "پراکسی فعال."
    PROXY_DISABLED_LOG_MSG = "پراکسی غیر فعال."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "مدد پیغام بند کریں۔"
    AUDIO_HELP_SHOWN_LOG_MSG = "/audio مدد دکھائی گئی"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "صارف نے پلے لسٹ مدد کی درخواست کی۔"
    PLAYLIST_HELP_CLOSED_LOG_MSG = "پلے لسٹ میں مدد بند۔"
    AUDIO_HINT_CLOSED_LOG_MSG = "آڈیو اشارہ بند۔"
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "براہ راست لنک مینو {user_id} سے صارف {url} کے ل link لنک بٹن کے ذریعے تیار کیا گیا ہے"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Failed to extract direct link via LINK button for user {user_id} from {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "صارف {url} ، url کے لئے پھانسی دیئے گئے کمانڈ: __va{user_id}"
    QUICK_EMBED_LOG_MSG = "فوری سرایت: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "{url} کے لئے بھیجے گئے مینو سے ہمیشہ پوچھیں"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Created cached qualities menu for user {user_id} after error: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Always ask menu error for {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "فارمیٹ /args ترتیبات کے ذریعے فکس کیا گیا ہے"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "آڈیو"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "ویڈیو"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "ویڈیو"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "اگلا ▶ ️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀ ️ prep"
    SUBTITLES_NEXT_BUTTON_MSG = "اگلا ➡"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "text تمام ٹیکسٹ فیلڈ خالی ہیں"
    SENDER_VIDEO_DURATION_MSG = "ویڈیو دورانیہ:"
    SENDER_UPLOADING_FILE_MSG = "file فائل اپ لوڈ کرنا ..."
    SENDER_UPLOADING_VIDEO_MSG = "video ویڈیو اپ لوڈ کرنا ..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 ویڈیو دورانیہ:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 فائل اپ لوڈ۔"
    DOWN_UP_VIDEO_INFO_MSG = "📋 ویڈیو کی معلومات"
    DOWN_UP_NUMBER_MSG = "نمبر"
    DOWN_UP_TITLE_MSG = "عنوان"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑ ڈاؤن لوڈ ویڈیو۔"
    DOWN_UP_PROCESSING_UPLOAD_MSG = "apload اپ لوڈ کے لئے پروسیسنگ ..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "spt تقسیم شدہ حصہ {part} فائل اپ لوڈ کی گئی"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ اپ لوڈ مکمل کریں"
    DOWN_UP_FILES_UPLOADED_MSG = "فائلیں اپ لوڈ کی گئیں"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 قریب"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼 کوڈیک"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 ڈبس"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 سب"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 براؤزر"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "direct براہ راست لنک حاصل کرنا ..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "available دستیاب فارمیٹس حاصل کرنا ..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 ویڈیو کی تفصیل حاصل کی جا رہی ہے..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ تفصیل حاصل کرنے میں خرابی: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ ویڈیو کی تفصیل دستیاب نہیں ہے"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ تفصیل بھیجنے میں خرابی: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 ویڈیو کی تفصیل صارف {user_id} کو {url} ({title}) کے لیے بھیجی گئی"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "G گیلری ، DL شروع کرنا…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>دورانیہ:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>فارمیٹ:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>براؤزر:</b> ویب براؤزر میں کھولیں"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "دستیاب فارمیٹس"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 فارمیٹ IDs کا استعمال کیسے کریں:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "فہرست حاصل کرنے کے بعد، مخصوص فارمیٹ ID استعمال کریں:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - فارمیٹ 401 ڈاؤن لوڈ کریں"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - اوپر کی طرح"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - فارمیٹ 140 کو MP3 آڈیو کے طور پر ڈاؤن لوڈ کریں"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 صرف آڈیو فارمیٹس کا پتہ چلا"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "یہ فارمیٹس MP3 آڈیو فائلوں کے طور پر ڈاؤن لوڈ کیے جائیں گے۔"
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>فارمیٹ کیسے سیٹ کریں:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - مخصوص فارمیٹ ID ڈاؤن لوڈ کریں"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - کوالٹی کے لحاظ سے ڈاؤن لوڈ کریں"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - بہترین کوالٹی ڈاؤن لوڈ کریں"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - ہمیشہ کوالٹی پوچھیں"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>صرف آڈیو فارمیٹس:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - فارمیٹ 140 کو MP3 آڈیو کے طور پر ڈاؤن لوڈ کریں"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "یہ MP3 آڈیو فائلوں کے طور پر ڈاؤن لوڈ کیے جائیں گے۔"
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 اوپر کی فہرست سے فارمیٹ ID استعمال کریں"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ خرابی: اصل پیغام نہیں ملا۔"
    ALWAYS_ASK_FORMATS_PAGE_MSG = "فارمیٹس صفحہ"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ فارمیٹس مینو دکھانے میں خرابی"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ فارمیٹس حاصل کرنے میں خرابی"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ دستیاب فارمیٹس حاصل کرنے میں خرابی۔"
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "براہ کرم بعد میں دوبارہ کوشش کریں۔"
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp اس مواد کو پراسیس نہیں کر سکتا"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "سسٹم gallery-dl استعمال کرنے کی سفارش کرتا ہے۔"
    ALWAYS_ASK_OPTIONS_MSG = "**اختیارات:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• تصویر گیلریوں کے لیے: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• ایک تصویر کے لیے: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl اکثر Instagram، Twitter اور دیگر سوشل میڈیا مواد کے لیے بہتر کام کرتا ہے۔"
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Gallery-dl آزمائیں"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 فارمیٹ /args کے ذریعے فکس کیا گیا"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 سب ٹائٹلز"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 ڈب شدہ آڈیو"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — سب ٹائٹلز دستیاب ہیں"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — سب ٹائٹل زبان منتخب کریں"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ سب ٹائٹلز نہیں ملیں اور ایمبیڈ نہیں ہوں گی"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — cache سے فوری ری پوسٹ"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — آڈیو زبان منتخب کریں"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW ادائیگی شدہ ہے (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — ڈاؤن لوڈ کوالٹی منتخب کریں"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — تصویر ڈاؤن لوڈ کریں (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — poketube میں ویڈیو دیکھیں"  # عارضی طور پر غیر فعال: poketube سروس ڈاؤن ہے
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — ویڈیو کا براہ راست لنک حاصل کریں"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — دستیاب فارمیٹس کی فہرست دکھائیں"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — ویڈیو ext/codec تبدیل کریں"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "membed"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — صرف آڈیو نکالیں"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW ادائیگی شدہ ہے (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — cache سے فوری ری پوسٹ"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — poketube میں ویڈیو دیکھیں"  # عارضی طور پر غیر فعال: poketube سروس ڈاؤن ہے
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — آڈیو زبان منتخب کریں"
    ALWAYS_ASK_BEST_BUTTON_MSG = "بہترین"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛دیگر"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝صرف سب"
    ALWAYS_ASK_SMART_GROUPING_MSG = "ذہین گروپ بندی"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "ایکشن بٹن کی قطار شامل کی گئی (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "ایکشن بٹن کی قطاریں شامل کی گئیں (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "موجودہ قطار میں نیچے کے بٹن شامل کیے گئے"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "نیا نیچے کی قطار بنائی گئی"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "پلے لسٹ میں کوئی ویڈیوز نہیں ملیں"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "غیر معاون URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "کوئی ویڈیو نہیں مل سکی"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "کوئی ویڈیو نہیں ملی"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "کوئی میڈیا نہیں ملا"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "یہ ٹویٹ میں شامل نہیں ہے"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>ویڈیو کی معلومات حاصل کرنے میں خرابی:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "ویڈیو کی معلومات حاصل کرنے میں خرابی"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "<code>/clean</code> کمانڈ آزمائیں اور دوبارہ کوشش کریں۔ اگر خرابی برقرار رہے، تو YouTube کو تصدیق درکار ہے۔ <code>/cookie</code> یا <code>/cookies_from_browser</code> کے ذریعے cookies.txt اپ ڈیٹ کریں اور دوبارہ کوشش کریں۔"
    ALWAYS_ASK_MENU_CLOSED_MSG = "مینو بند۔"
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 دستی کوالٹی انتخاب"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "خودکار پتہ لگانے میں ناکامی کی وجہ سے دستی طور پر کوالٹی منتخب کریں:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 تمام دستیاب فارمیٹس"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 دستیاب کوالٹیز (cache سے)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ cache شدہ کوالٹیز استعمال کر رہے ہیں - نئے فارمیٹس دستیاب نہیں ہو سکتے"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 فارمیٹ ڈاؤن لوڈ ہو رہا ہے"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 ڈاؤن لوڈ ہو رہا ہے"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 پیش رفت ٹریکنگ کے ساتھ ڈاؤن لوڈ ہو رہا ہے..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 فارمیٹ استعمال کرتے ہوئے ڈاؤن لوڈ ہو رہا ہے:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 فارمیٹ استعمال کرتے ہوئے آڈیو ڈاؤن لوڈ ہو رہا ہے:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 بہترین کوالٹی ڈاؤن لوڈ ہو رہی ہے..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 ڈیٹا بیس dump ڈاؤن لوڈ ہو رہا ہے..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 ڈاؤن لوڈ ہو رہا ہے"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "فارمیٹس صفحہ"
    ALWAYS_ASK_FROM_CACHE_MSG = "(cache سے)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ خرابی: اصل پیغام نہیں ملا۔ یہ حذف ہو گیا ہو سکتا ہے۔ براہ کرم لنک دوبارہ بھیجیں۔"
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ خرابی: اصل URL نہیں ملا۔ براہ کرم لنک دوبارہ بھیجیں۔"
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>براہ راست لنک حاصل کیا گیا</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>عنوان:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>دورانیہ:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>فارمیٹ:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>ویڈیو سٹریم:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>آڈیو سٹریم:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ سٹریم لنکس حاصل کرنے میں ناکام"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "براہ راست لنک {user_id} سے صارف {url} کے لئے ہمیشہ پوچھو مینو کے ذریعے نکالا جاتا ہے"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Failed to extract direct link via Always Ask menu for user {user_id} from {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "براہ راست لنک {user_id} سے {url} کے لئے down_and_up_with_format کے ذریعے نکالا گیا"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Failed to extract direct link via down_and_up_with_format for user {user_id} from {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "براہ راست لنک {user_id} سے صارف {url} کے لئے ڈاون_ینڈ_اڈیو کے ذریعے نکالا گیا"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Failed to extract direct link via down_and_audio for user {user_id} from {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ آڈیو cache سے بھیجی گئی۔"
    AUDIO_PROCESSING_MSG = "🎙️ آڈیو پراسیس ہو رہی ہے..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 آڈیو ڈاؤن لوڈ ہو رہی ہے:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "آڈیو ڈاؤن لوڈ کے دوران خرابی پیش آئی۔"
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ آڈیو کی معلومات نکالنے میں ناکام"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "پلے لسٹ میں انڈیکس {index} پر غیر معاون فائل کی قسم کو چھوڑ رہے ہیں"
    AUDIO_FILE_NOT_FOUND_MSG = "ڈاؤن لوڈ کے بعد آڈیو فائل نہیں ملی۔"
    AUDIO_UPLOADING_MSG = "{process}\n📤 آڈیو فائل اپ لوڈ ہو رہی ہے...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ آڈیو بھیجنے میں ناکام: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "پلے لسٹ آڈیو بھیجی گئی: {sent}/{total} فائلیں (کوالٹی={quality}) صارف{user_id} کو"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ آڈیو ڈاؤن لوڈ کرنے میں ناکام: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ ٹائم آؤٹ کی وجہ سے ڈاؤن لوڈ منسوخ (2 گھنٹے)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ ویڈیو فائل نہیں ملی: {filename}"
    VIDEO_PROCESSING_ERROR_MSG = "❌ ویڈیو پراسیس کرنے میں خرابی: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ تفصیل فائل بھیجنے میں خرابی: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 اگر آپ ویڈیو کیپشن تبدیل کرنا چاہتے ہیں - نئے متن کے ساتھ ویڈیو پر جواب دیں</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "کوئی سب ٹائٹلز نہیں ملیں"
    VIDEO_PROGRESS_MSG = "<b>ویڈیو:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>آڈیو:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current}/{total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL کی حد سے تجاوز: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "پراسیسنگ مکمل"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ متعدد URL موڈ میں پلے لسٹ رینجز کی اجازت نہیں ہے۔ صرف ایک URLs بھیجیں بغیر رینجز کے (*1*5, /vid 1-10, وغیرہ)۔"
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "اگر آپ کی سائٹ سپورٹ شدہ ہے تو <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>یہاں</a> چیک کریں"
    ERROR_COOKIE_NEEDED_MSG = "اس ویڈیو کو ڈاؤن لوڈ کرنے کے لیے آپ کو <code>cookie</code> کی ضرورت ہو سکتی ہے۔ پہلے، <b>/clean</b> کمانڈ کے ذریعے اپنا ورک اسپیس صاف کریں"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "YouTube کے لیے - <b>/cookie</b> کمانڈ کے ذریعے <code>cookie</code> حاصل کریں۔ کسی بھی دوسری سپورٹ شدہ سائٹ کے لیے - اپنی کوکی بھیجیں (<a href='https://t.me/tg_ytdlp/203'>گائیڈ1</a>) (<a href='https://t.me/tg_ytdlp/214'>گائیڈ2</a>) اور اس کے بعد اپنا ویڈیو لنک دوبارہ بھیجیں۔"
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "سب ٹائٹل زبان منتخب کریں"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "کوئی متبادل آڈیو زبانیں نہیں"
    CHOOSE_AUDIO_LANGUAGE_MSG = "آڈیو زبان منتخب کریں"
    PAGE_NUMBER_MSG = "صفحہ {page}"
    TOTAL_PROGRESS_MSG = "کل پیش رفت"
    SUBTITLE_MENU_CLOSED_MSG = "سب ٹائٹل مینو بند۔"
    SUBTITLE_LANGUAGE_SET_MSG = "سب ٹائٹل زبان سیٹ کی گئی: {value}"
    AUDIO_SET_MSG = "آڈیو سیٹ کی گئی: {value}"
    FILTERS_UPDATED_MSG = "فلٹرز اپ ڈیٹ کیے گئے"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙واپس"
    CLOSE_BUTTON_TEXT = "🔚بند"
    LIST_BUTTON_TEXT = "📃فہرست"
    IMAGE_BUTTON_TEXT = "🖼تصویر"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ کوالٹیز خودکار طور پر پتہ نہیں چلیں\nتمام دستیاب فارمیٹس دیکھنے کے لیے 'دیگر' بٹن استعمال کریں۔</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **لائیو سٹریم کا پتہ چلا**\n\nجاری یا لامحدود لائیو سٹریمز ڈاؤن لوڈ کرنے کی اجازت نہیں ہے۔\n\nبراہ کرم سٹریم کے ختم ہونے کا انتظار کریں اور دوبارہ ڈاؤن لوڈ کرنے کی کوشش کریں جب:\n• سٹریم کا دورانیہ معلوم ہے\n• سٹریم ختم ہو گئی ہے\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>لائیو سٹریم ڈاؤن لوڈ</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "chunk {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "زیادہ سے زیادہ سائز: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "کل دورانیہ: {duration} سیکنڈ"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>لائیو سٹریم - Chunk {chunk}</b>\n⏱ دورانیہ: {duration} سیکنڈ\n📦 سائز: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "chunk {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>لائیو سٹریم ڈاؤن لوڈ مکمل</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "{chunks} chunk(s) ڈاؤن لوڈ کیے گئے"
    LIVE_STREAM_TOTAL_DURATION_MSG = "کل دورانیہ: {duration} سیکنڈ"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>لائیو سٹریم ڈاؤن لوڈ روک دیا گیا</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "صارف ڈائریکٹری حذف کی گئی (شاید /clean کمانڈ کے ذریعے)"
    LIVE_STREAM_FILE_DELETED_MSG = "Chunk فائل حذف کی گئی (شاید /clean کمانڈ کے ذریعے)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ سٹریم ختم ہو گئی ہے"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "براہ کرم <code>/format</code> کمانڈ استعمال کرتے ہوئے ایک مختلف فارمیٹ منتخب کریں۔"
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>براہ راست لنک حاصل کیا گیا</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>عنوان:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>دورانیہ:</b> {duration} سیکنڈ\n"
    FORMAT_FIELD_MSG = "🎛 <b>فارمیٹ:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>ویڈیو سٹریم:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>آڈیو سٹریم:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **فائل پراسیسنگ خرابی**\n\nویڈیو ڈاؤن لوڈ ہو گئی لیکن فائل نام میں غلط حروف کی وجہ سے پراسیس نہیں کی جا سکی۔\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **فائل پراسیسنگ خرابی**\n\nویڈیو ڈاؤن لوڈ ہو گئی لیکن غلط دلیل کی خرابی کی وجہ سے پراسیس نہیں کی جا سکی۔\n\n"
    FORMAT_NOT_AVAILABLE_MSG = "❌ **فارمیٹ دستیاب نہیں**\n\nدرخواست کردہ ویڈیو فارمیٹ اس ویڈیو کے لیے دستیاب نہیں ہے۔\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ فارمیٹ ID {format_id} اس ویڈیو کے لیے نہیں ملا۔\n\nدستیاب فارمیٹ IDs: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **AV1 فارمیٹ اس ویڈیو کے لیے دستیاب نہیں ہے۔**\n\n**دستیاب فارمیٹس:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **فائل پراسیسنگ خرابی**\n\nآڈیو ڈاؤن لوڈ ہو گئی لیکن فائل نام میں غلط حروف کی وجہ سے پراسیس نہیں کی جا سکی۔\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **فائل پراسیسنگ خرابی**\n\nآڈیو ڈاؤن لوڈ ہو گئی لیکن غلط دلیل کی خرابی کی وجہ سے پراسیس نہیں کی جا سکی۔\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "صارف نے ممنوعہ مواد داخل کیا۔ ڈاؤن لوڈ نہیں کیا جا سکتا۔"
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "NSFW blur کمانڈ کے ذریعے سیٹ کیا گیا: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "صارف نے /nsfw مینو کھولا۔"
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: بند۔"
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "{service} کوکی ڈاؤن لوڈ کرنے میں ناکام: status={status} (url چھپا ہوا)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "{service} کوکی ڈاؤن لوڈ کرنے میں خرابی: {error} (url چھپا ہوا)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "{service} کوکی ڈاؤن لوڈ کرتے وقت غیر متوقع خرابی (url چھپا ہوا): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "صارف {user_id} کے لیے کوکی فائل اپ ڈیٹ کی گئی۔"
    COOKIES_INVALID_CONTENT_LOG_MSG = "صارف {user_id} کی طرف سے فراہم کردہ غلط کوکی مواد۔"
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "صارف {user_id} کے لیے YouTube کوکی URLs خالی ہیں۔"
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "صارف {user_id} کے لیے ماخذ {source} سے YouTube کوکیز ڈاؤن لوڈ اور تصدیق کی گئیں۔"
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "صارف {user_id} کے لیے تمام YouTube کوکی ماخذ ناکام ہو گئے۔"
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "ایڈمن {admin_id} کی طرف سے check_porn کمانڈ میں خرابی: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "تقسیم حصے کا سائز {size} بائٹس پر سیٹ کیا گیا۔"
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "فائل تقسیم کے ساتھ ویڈیو اپ لوڈ مکمل۔"
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "پلے لسٹ ویڈیوز بھیجی گئیں: {sent}/{total} فائلیں (کوالٹی={quality}) صارف {user_id} کو"
    UNKNOWN_ERROR_MSG = "❌ نامعلوم خرابی: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "پلے لسٹ میں انڈیکس {index} پر غیر معاون فائل کی قسم کو چھوڑ رہے ہیں"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg نہیں ملا۔ براہ کرم FFmpeg انسٹال کریں۔"
    CONVERSION_TO_MP4_FAILED_MSG = "❌ MP4 میں تبدیلی ناکام: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ سب ٹائٹلز ایمبیڈ کرنا زیادہ وقت لے سکتا ہے (ویڈیو کے 1 منٹ فی 1 منٹ تک)!\n🔥 سب ٹائٹلز جلانا شروع کر رہے ہیں..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ سب ٹائٹلز حدوں (کوالٹی/دورانیہ/سائز) کی وجہ سے ایمبیڈ نہیں کی جا سکتیں"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ منتخب شدہ زبان کے لیے سب ٹائٹلز دستیاب نہیں ہیں"
    ERROR_SENDING_VIDEO_MSG = "❌ ویڈیو بھیجنے میں خرابی: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ پلے لسٹ ویڈیوز بھیجی گئیں: {sent}/{total} فائلیں۔"
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ ٹائم آؤٹ کی وجہ سے ڈاؤن لوڈ منسوخ (2 گھنٹے)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ ویڈیو ڈاؤن لوڈ کرنے میں ناکام: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ خرابی: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON ایک آبجیکٹ (ڈکشنری) ہونا چاہیے۔"
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ غلط JSON فارمیٹ۔ براہ کرم درست JSON فراہم کریں۔"
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ قیمت {min_val} اور {max_val} کے درمیان ہونی چاہیے۔"
    ARGS_PARAM_SET_TO_MSG = "✅ {description} سیٹ کیا گیا: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ سچ ہے"
    ARGS_FALSE_BUTTON_MSG = "❌ غلط"
    ARGS_BACK_BUTTON_MSG = "🔙 واپس"
    ARGS_CLOSE_BUTTON_MSG = "🔚 بند"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ سچ ہے"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ غلط"
    ARGS_NOT_SET_MSG = "سیٹ نہیں کیا گیا"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ AV1 فارمیٹ اس ویڈیو کے لیے دستیاب نہیں ہے۔\n\nدستیاب فارمیٹس:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ ڈاؤن لوڈ کرنے میں خرابی: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ انڈیکس {index} پر پلے لسٹ میں کوئی ویڈیوز نہیں ملیں۔"
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **ویڈیو تبدیلی ناکام**\n\nغلط دلیل کی خرابی کی وجہ سے ویڈیو MP4 میں تبدیل نہیں کی جا سکی۔\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **ویڈیو تبدیلی ناکام**\n\nویڈیو MP4 میں تبدیل نہیں کی جا سکی۔\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ سٹریم لنکس حاصل کرنے میں ناکام"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>لنک حاصل کرنے میں خرابی:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ انڈیکس {index} پر کوئی مواد نہیں ملا"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ خرابی: اصل پیغام نہیں ملا۔"
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ خرابی: URL نہیں ملا۔"
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ یہ URL ایمبیڈ نہیں کیا جا سکتا۔"
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} کوڈیک اس ویڈیو کے لیے دستیاب نہیں ہے"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} فارمیٹ اس ویڈیو کے لیے دستیاب نہیں ہے"
    
    # Always Ask Menu button texts
    AA_AVC_BUTTON_MSG = "✅ AVC"
    AA_AVC_BUTTON_INACTIVE_MSG = "☑️ AVC"
    AA_AVC_BUTTON_UNAVAILABLE_MSG = "❌ AVC"
    AA_AV1_BUTTON_MSG = "✅ av1"
    AA_AV1_BUTTON_INACTIVE_MSG = "☑️ AV1"
    AA_AV1_BUTTON_UNAVAILABLE_MSG = "❌ AV1"
    AA_VP9_BUTTON_MSG = "✅ vp9"
    AA_VP9_BUTTON_INACTIVE_MSG = "☑️ VP9"
    AA_VP9_BUTTON_UNAVAILABLE_MSG = "❌ VP9"
    AA_MP4_BUTTON_MSG = "M MP4"
    AA_MP4_BUTTON_INACTIVE_MSG = "☑️ MP4"
    AA_MP4_BUTTON_UNAVAILABLE_MSG = "❌ MP4"
    AA_MKV_BUTTON_MSG = "✅ ایم کے وی"
    AA_MKV_BUTTON_INACTIVE_MSG = "☑️ MKV"
    AA_MKV_BUTTON_UNAVAILABLE_MSG = "❌ MKV"

    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood کی حد۔ بعد میں کوشش کریں۔"
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "__ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ کوکی چیک کریں"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ on"
    PROXY_OFF_BUTTON_MSG = "❌ آف"
    PROXY_CLOSE_BUTTON_MSG = "🔚بند"
    
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ on"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ آف"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚بند"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ ON (بلر نہیں)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ON (بلر نہیں)"
    NSFW_OFF_BLUR_MSG = "✅ OFF (بلر)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ OFF (بلر)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "صاف"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "صارف {user} کے لیے جوابی پیغام پراسیس کرنے میں خرابی: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "صارف {user} کو براڈکاسٹ بھیجنے میں خرابی: {error}"
    ADMIN_LOGS_FORMAT_MSG = "{bot_name} کے لاگز\nصارف: {user_id}\nکل لاگز: {total}\nموجودہ وقت: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nکل {path}: {count}\nموجودہ وقت: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>کل صارفین: {count}</i>\nآخری 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "ایڈمن {admin_id} کی طرف سے پورن cache دوبارہ لوڈ کی گئیں۔ Domains: {domains}, Keywords: {keywords}, Sites: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "ٹائم آؤٹ پیغام بھیجنے میں خرابی: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>زبان منتخب کریں</b>"
    LANG_CHANGED_MSG = "✅ زبان تبدیل کی گئی {lang_name}"
    LANG_ERROR_MSG = "❌ زبان تبدیل کرنے میں خرابی"
    LANG_CLOSED_MSG = "زبان کا انتخاب بند"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[براؤزر] کال بیک: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "URL کے ساتھ براؤزر مانیٹرنگ بٹن شامل کر رہے ہیں: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "براؤزر مانیٹرنگ URL ترتیب نہیں دیا گیا: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **کی بورڈ کی ترتیب اپ ڈیٹ کی گئی!**\n\nنئی ترتیب: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "کی بورڈ چھپانے میں ناکام: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "صارف {user_id} کے لیے لنک ایکسٹریکشن کے لیے کام کرنے والی YouTube کوکیز استعمال کر رہے ہیں"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "صارف {user_id} کے لیے لنک ایکسٹریکشن کے لیے کوئی کام کرنے والی YouTube کوکیز دستیاب نہیں ہیں"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "صارف {user_id} کے لیے لنک ایکسٹریکشن کے لیے موجودہ YouTube کوکیز استعمال کر رہے ہیں"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "صارف {user_id} کے لیے لنک ایکسٹریکشن کے لیے کوئی YouTube کوکیز نہیں ملیں"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "صارف {user_id} کے فولڈر میں لنک ایکسٹریکشن کے لیے global کوکی فائل کاپی کی گئی"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] صارف {user_id} نے mediainfo کمانڈ درخواست کی"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] صارف {user_id} ایڈمن ہے: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] صارف {user_id} چینل میں ہے: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] صارف {user_id} کی رسائی مسترد - ایڈمن نہیں ہے اور چینل میں نہیں ہے"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] صارف {user_id} کی رسائی منظور"
    MEDIAINFO_CALLBACK_MSG = "[میڈیا انفو] کال بیک: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ یہ کمانڈ صرف ایڈمنسٹریٹرز کے لیے دستیاب ہے۔"
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ PO token سپورٹ کے ساتھ ڈاؤن لوڈ مکمل"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood کی حد۔ بعد میں کوشش کریں۔"
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ باقی ٹوکن ریفریش غلطی: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "fire فائر بیس سیشن کو بند کرنے میں غلطی: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "base بیس ڈی بی ڈھانچے کو شروع کرنے میں غلطی: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "config config.py (فائر بیس_کونف ، فائر بیس_سر ، فائر بیس_ پاس ورڈ) میں تمام پیرامیٹرز مرتب نہیں کیے گئے ہیں۔"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ فائر بیس_کونف.ڈیٹا بیسورل سیٹ نہیں ہے"
    DB_API_KEY_NOT_SET_MSG = "❌ فائر بیس_کونف.ایپکی کو آئی ڈی ٹوکین حاصل کرنے کے لئے سیٹ نہیں کیا گیا ہے"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "fire فائر بیس ڈمپ ڈاؤن لوڈ کرنے میں غلطی: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "rest آرام کے ذریعہ فائر بیس ڈمپ ڈاؤن لوڈ کرنے میں ناکام"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "_ ڈاونلوڈ_ینڈ_رلوڈ_کیچ میں غلطی: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Error running auto reload_cache (attempt {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "re دوبارہ کوشش کرنے کی تمام کوششیں ناکام ہوگئیں"
    DB_STARTING_FIREBASE_DUMP_MSG = "{datetime} پر فائر بیس ڈمپ ڈاؤن لوڈ کرنا شروع کریں"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠ انحصار دستیاب نہیں: درخواستیں یا سیشن"
    DB_DATABASE_EMPTY_MSG = "⚠ ڈیٹا بیس خالی ہے"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ بند کرنے میں غلطی: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "clean صفائی کے دوران غلطی: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ کلون کی خرابی: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ کلون ٹائم آؤٹ"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ کلون استثناء: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ صارف کے ذریعہ منسوخ شدہ اپ ڈیٹ"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ ذخیرہ نے کامیابی کے ساتھ کلون کیا"
    UPDATE_BACKUPS_MOVED_MSG = "✅ بیک اپ _ بیک اپ/ میں منتقل ہوگئے"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ تمام ماڈیول بھری ہوئی ہیں"
    MAGIC_CLEANUP_COMPLETED_MSG = "out باہر نکلنے پر صفائی مکمل"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Received signal {signal}, shutting down gracefully..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "براہ کرم انتظار کریں ..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "H HLS اسٹریم ڈاؤن لوڈ کرنا:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "ٹکڑوں کا انتظار ہے"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ بیک اپ {ts} _ بیک اپ/ میں نہیں ملا"
    RESTORE_FAILED_RESTORE_MSG = "❌ Failed to restore {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ بحال: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Details:</b> {error_details}\n\nDownload stopped due to critical error.\n\n💡 <b>Tip:</b> If you're getting 401 Unauthorized error, try using <code>/cookie instagram</code> command or send your own cookies to authenticate with Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "porn فحش بلیک لسٹ میں ڈومین: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "for فحش مطلوبہ الفاظ ملا: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "list وائٹ لسٹ میں ڈومین: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "whit وائٹ لسٹ کے مطلوبہ الفاظ مل گئے: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ کوئی فحش کلیدی الفاظ نہیں ملے"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "ing انڈیکس {index} میں ٹکٹوک API کی غلطی ، اگلے آڈیو کو چھوڑیں ..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "ing انڈیکس {index} میں ٹکٹوک API کی خرابی ، اگلی ویڈیو میں اچھ .ا ..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "User entered a <b>url</b>\n <b>user's name:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>User entered like this:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "چینل میں شامل ہوں"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "heand ہینڈلر کو رجسٹر کرنا: {func_name} {handler_type}__"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /کوکی - میری 5 کوکیز ڈاؤن لوڈ کریں"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /کوکیز_فرم_بروزر - براؤزر کا YT کوکی حاصل کریں"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /چیک_ کوکی - اپنی کوکی فائل کو درست کریں"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - کسٹم کوکی اپ لوڈ کریں"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 قریب"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "دستیاب فارمیٹس: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚 کلوز"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚 کلوز"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚 کلوز"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚 کلوز"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "مدد بند"
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "بند"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "خرابی پیش آئی"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg not found in PATH or project directory. Please install FFmpeg."
    YTDLP_NOT_FOUND_MSG = "YT-DLP بائنری پاتھ یا پروجیکٹ ڈائرکٹری میں نہیں ملا۔ براہ کرم YT-DLP انسٹال کریں۔"
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "ویڈیو {rounds} حصوں میں تقسیم ہو جائے گی، جو زیادہ ہو سکتا ہے"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "ویڈیو کا حصہ تقسیم ہو رہا ہے {current}/{total}: {start_time:.2f}s سے {end_time:.2f}s تک"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "تقسیم کا حصہ {part} بنانے میں ناکام: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "تقسیم کا حصہ {part} کامیابی سے بنایا گیا: {target_name} ({size} بائٹس)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "ویڈیو کے حصے {part} کو تقسیم کرنے میں خرابی: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "ویڈیو {count} حصوں میں کامیابی سے تقسیم ہو گئی"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "ویڈیو تقسیم کرنے کے عمل میں خرابی: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] ویڈیو {video_path} پر کارروائی کرتے وقت خرابی: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "ویڈیو فائل موجود نہیں: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "ابعاد '{size_result}' کو پارس کرنے میں خرابی: {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "'{size_result}' سے ویڈیو کے ابعاد کا تعین نہیں کر سکا، ڈیفالٹ استعمال کر رہے ہیں: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "تھمب نیل بنانے میں خرابی: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "ویڈیو کی مدت کو پارس کرنے میں خرابی: {error}, نتیجہ تھا: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "{thumb_dir} پر تھمب نیل نہیں بنایا گیا، ڈیفالٹ استعمال کر رہے ہیں"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Command execution error: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Error creating thumbnail with FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "غیر-ڈکشنری کنفیگ سیکشن چھوڑ رہے ہیں: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "سیٹ کر رہے ہیں {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] صارف کی کوکیز استعمال کر رہے ہیں: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "صارف {user_id} کے لیے YouTube کی کوکیز استعمال کر رہے ہیں"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "عالمی کوکی فائل صارف {user_id} کے فولڈر میں کاپی کی گئی"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] کاپی شدہ عالمی کوکیز کو صارف کی کوکیز کے طور پر استعمال کر رہے ہیں: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "صارف {user_id} کے لیے عالمی کوکی فائل کاپی کرنے میں ناکام: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "ڈومین کے لیے --no-cookies استعمال کر رہے ہیں: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "پراکسی درخواست کی گئی لیکن کنفیگ درآمد/حاصل کرنے میں ناکام: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "gallery-dl کے لیے پراکسی استعمال کرنے پر مجبور کر رہے ہیں: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "پروکسی درخواست کی گئی لیکن پروکسی کنفیگریشن نامکمل ہے"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "پراکسی ہیلپر ناکام: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "ایکسٹریکٹر آئٹمز کو پارس کر رہے ہیں..."
    GALLERY_DL_ITEM_COUNT_MSG = "آئٹم {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "میٹا ڈیٹا ملا (ٹیگ 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL ملا (ٹیگ 3): {url}, میٹا ڈیٹا: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "میٹا ڈیٹا ملا (لیگیسی): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL ملا (لیگیسی): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "فائل کا نام ملا: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "ڈائریکٹری ملا: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "ایکسٹینشن ملا: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Parsed {count} items, info: {info}, fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "گیلری ، DL کنفیگ ترتیب دینا: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "استراتیجی A آزما رہے ہیں: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor ماڈیول نہیں ملا"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() اس بلڈ میں دستیاب نہیں"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "extractor.find({url}) کو کال کر رہے ہیں"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "کوئی ایکسٹریکٹر URL سے میل نہیں کھایا"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "ایکسٹریکٹر پر کوکیز سیٹ کر رہے ہیں: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "ایکسٹریکٹر پر کوکیز سیٹ کرنے میں ناکام: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "ایکسٹریکٹر ملا، items() کو کال کر رہے ہیں"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "استراتیجی A کامیاب، معلومات ملی: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "استراتیجی A: extractor.items() نے کوئی درست معلومات واپس نہیں کی"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "استراتیجی A (extractor.find) ناکام: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "--get-urls سے فال بیک میٹا ڈیٹا: کل={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "تمام استراتیجیاں میٹا ڈیٹا حاصل کرنے میں ناکام"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "تصویر کی معلومات نکالنے میں ناکام: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job ماڈیول نہیں ملا (خراب انسٹال؟)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob اس بلڈ میں دستیاب نہیں"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "gallery-dl ڈائریکٹری میں ڈاؤن لوڈ شدہ فائلوں کی تلاش"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "ایکسٹریکٹر سے ناموں کے ذریعے فائلیں تلاش کرنے کی کوشش"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "صارف {user_id} کے لیے صارف کے دلائل پڑھنے میں خرابی: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] ویڈیو {video_path} پر کارروائی کرتے وقت خرابی: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "صارف {user_id} کے پاس send_as_file فعال ہے، دستاویز کے طور پر بھیج رہے ہیں"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video بار بار ٹائم آؤٹ ہوا؛ send_document پر واپس جا رہے ہیں"
    SENDER_CAPTION_TOO_LONG_MSG = "کیپشن بہت لمبی ہے، کم سے کم کیپشن کے ساتھ کوشش کر رہے ہیں"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (کم سے کم کیپشن) ٹائم آؤٹ؛ send_document پر فال بیک"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "کم سے کم کیپشن کے ساتھ ویڈیو بھیجنے میں خرابی: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "مکمل تفصیل فائل بھیجنے میں خرابی: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "عارضی تفصیل فائل ہٹانے میں خرابی: {error}"
    
    # YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "NO_FILTER_DOMAINS میں ڈومین کے لیے match_filter چھوڑ رہے ہیں: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے صارف کے URL پر موجودہ YouTube کوکیز چیک کر رہے ہیں"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے صارف کے URL پر موجودہ YouTube کوکیز کام کر رہی ہیں - انہیں استعمال کر رہے ہیں"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "صارف کے URL پر موجودہ YouTube کوکیز ناکام ہو گئیں، صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے نئی حاصل کرنے کی کوشش کر رہے ہیں"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے YouTube کوکی ماخذ {i} آزمائیں"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "ماخذ {i} سے YouTube کوکیز صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے صارف کے URL پر کام کر رہی ہیں - صارف فولڈر میں محفوظ کی گئیں"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "ماخذ {i} سے YouTube کوکیز صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے صارف کے URL پر کام نہیں کر رہیں"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے ماخذ {i} سے YouTube کوکیز ڈاؤن لوڈ کرنے میں ناکام"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے تمام YouTube کوکی ماخذ ناکام ہو گئے، کوکیز کے بغیر کوشش کریں گے"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے کوئی YouTube کوکی ماخذ ترتیب نہیں دیے گئے، کوکیز کے بغیر کوشش کریں گے"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے کوئی YouTube کوکیز نہیں ملیں، نئی حاصل کرنے کی کوشش کر رہے ہیں"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے YouTube کوکیز استعمال کر رہے ہیں (Always Ask مینو میں پہلے سے تصدیق شدہ)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "صارف {user_id} کے لیے فارمیٹ ڈیٹیکشن کے لیے کوئی YouTube کوکیز نہیں ملیں، بحال کرنے کی کوشش کر رہے ہیں..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "صارف {user_id} کے فولڈر میں فارمیٹ ڈیٹیکشن کے لیے global کوکی فائل کاپی کی گئی"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "صارف {user_id} کے لیے global کوکی فائل کاپی کرنے میں ناکام: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "get_video_formats میں ڈومین کے لیے --no-cookies استعمال کر رہے ہیں: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "ایپ ابھی تک شروع نہیں ہوئی۔ {name} تک رسائی نہیں ہو سکتی"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>کیپشن:</b> <code>{caption}</code>\n<b>صارف ID:</b> <code>{user_id}</code>\n<b>صارف کا پہلا نام:</b> <code>{users_name}</code>\n<b>ویڈیو فائل ID:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor میں خرابی: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor میں غیر متوقع خرابی: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 ویڈیو URL</a>{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL کنفیگریشن میں موجود نہیں"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin شروع کیا گیا"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken اپ ڈیٹ کیا گیا"
    DB_LOG_FOR_USER_ADDED_MSG = "صارف کے لیے لاگ شامل کیا گیا"
    DB_DATABASE_CREATED_MSG = "db بنایا گیا"
    DB_BOT_STARTED_MSG = "بوٹ شروع ہوا"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY config.py میں محفوظ کیا گیا: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "پلے لسٹ کا حصہ پہلے سے cache میں ہے: {path_parts}، چھوڑ رہے ہیں"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: کسی URL/کوالٹی متغیر کے لیے کیش نہیں ملا، خالی ڈکشنری واپس کر رہے ہیں"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: بڑی رینج کے لیے تیز گنتی: {cached_count} کیش شدہ ویڈیوز"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: ہیش {url_hash}، کوالٹی {quality_key} کے لیے کیش نہیں ملا"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: کسی URL متغیر کے لیے کیش نہیں ملا، None واپس کر رہے ہیں"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ رسائی مسترد۔ صرف ایڈمن۔"
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Firebase کیش خودکار ری لوڈنگ اپ ڈیٹ!\n\n📊 حالت: {status}\n⏰ شیڈول: 00:00 سے ہر {interval} گھنٹے\n🕒 اگلا ری لوڈ: {next_exec} ({delta_min} منٹ میں)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Firebase کیش خودکار ری لوڈنگ بند!\n\n📊 حالت: ❌ غیر فعال\n💡 دوبارہ فعال کرنے کے لیے /auto_cache on استعمال کریں"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ غلط دلیل۔ /auto_cache on | off | N (1..168) استعمال کریں"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ وقفہ 1 اور 168 گھنٹوں کے درمیان ہونا چاہیے"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ وقفہ سیٹ کرنے میں ناکام"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Firebase کیش خودکار وقفہ اپ ڈیٹ!\n\n📊 حالت: ✅ فعال\n⏰ شیڈول: 00:00 سے ہر {interval} گھنٹے\n🕒 اگلا ری لوڈ: {next_exec} ({delta_min} منٹ میں)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Firebase کیش خودکار ری لوڈنگ شروع!\n\n📊 حالت: ✅ فعال\n⏰ شیڈول: 00:00 سے ہر {interval} گھنٹے\n🕒 اگلا ری لوڈ: {next_exec} ({delta_min} منٹ میں)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Firebase کیش خودکار ری لوڈنگ بند!\n\n📊 حالت: ❌ غیر فعال\n💡 دوبارہ فعال کرنے کے لیے /auto_cache on استعمال کریں"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "خودکار ری لوڈ فعال؛ اگلا {next_exec} پر"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "خودکار ری لوڈ ایڈمن کی طرف سے غیر فعال۔"
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "خودکار ری لوڈ وقفہ {interval}گھنٹے پر سیٹ؛ اگلا {next_exec} پر"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "خودکار ری لوڈ شروع؛ اگلا {next_exec} پر"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "خودکار ری لوڈ ایڈمن کی طرف سے بند۔"
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase کیش لوڈ: {count} روٹ نوڈز"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Firebase کیش فائل نہیں ملی، خالی کیش کے ساتھ شروع کر رہے ہیں: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Firebase کیش لوڈ کرنے میں ناکام: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase کیش ری لوڈ: {count} روٹ نوڈز"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Firebase کیش فائل نہیں ملی: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Firebase کیش ری لوڈ کرنے میں ناکام: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 آپ کو بوٹ سے پابندی لگا دی گئی ہے! پابندی ختم کرنے کے لیے {Config.ADMIN_USERNAME} سے رابطہ کریں\n<blockquote>P.S. چینل نہ چھوڑیں - آپ کو خودکار طور پر پابند کر دیا جائے گا ⛔️</blockquote>\n🌍زبان تبدیل کریں /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ کوئی ویڈیو فارمیٹ نہیں ملا۔ تصویر ڈاؤن لوڈر آزما رہے ہیں…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram نے پیغام بھیجنے کو محدود کر دیا ہے۔\n⏳ براہ کرم انتظار کریں: {time_str}\nٹائمر اپ ڈیٹ کرنے کے لیے URL دوبارہ 2 بار بھیجیں۔"
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>اسٹریم URL کاپی کرنے کے لیے بٹن پر کلک کریں، پھر VLC ایپ میں پیسٹ کریں</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>اسٹریم URL کاپی کرنے کے لیے بٹن پر کلک کریں، پھر VLC ایپ میں پیسٹ کریں</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>لنک حاصل کرنے میں خرابی:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ فارمیٹ فائل بھیجنے میں خرابی: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ فارمیٹ حاصل کرنے میں ناکام:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 تجزیہ کر رہے ہیں... (6 سیکنڈ انتظار کریں)"
    AA_PROCESSING_MSG = "🔎 تجزیہ کر رہے ہیں..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ ٹیگ #{wrong} میں ممنوعہ حروف ہیں۔ صرف حروف، ہندسے اور _ کی اجازت ہے۔\nبراہ کرم استعمال کریں: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ گروپ میں کام کرنے کے لیے بوٹ کو ایڈمنسٹریٹر کی اجازت درکار ہے۔ براہ کرم اس گروپ میں بوٹ کو ایڈمن بنائیں۔"
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "ہیلو {first_name},\n \n<i>یہ بوٹ🤖 کسی بھی ویڈیو کو براہ راست telegram میں ڈاؤن لوڈ کر سکتا ہے۔😊 مزید معلومات کے لیے <b>/help</b> دبائیں</i> 👈\n\n<blockquote>P.S. 🔞NSFW مواد اور ☁️کلاؤڈ اسٹوریج سے فائلوں کو ڈاؤن لوڈ کرنا ادائیگی ہے! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ چینل مت چھوڑیں - آپ کو بوٹ استعمال کرنے سے پابند کر دیا جائے گا ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 ہٹانے کے لیے کوئی فائل نہیں۔"
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 تمام فائلیں کامیابی سے ہٹا دی گئیں!\n\nہٹائی گئی فائلیں:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ اپنے پچھلے ڈاؤن لوڈ کے ختم ہونے تک انتظار کریں"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "check_user میں App instance None ہے"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict None ہے، ڈاؤن لوڈ کی اجازت دے رہے ہیں"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict None ہے، سب ٹائٹل ایمبیڈنگ کی اجازت دے رہے ہیں"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: حدیں چیک کر رہے ہیں - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "چیک_سبس_ لیمٹس: انفارمیشن_ڈکٹ کیز: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "سب ٹائٹل ایمبیڈنگ چھوڑ دی گئی: دورانیہ {duration}s حد {max_duration}s سے تجاوز کرتا ہے"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "سب ٹائٹل ایمبیڈنگ چھوڑ دی گئی: سائز {size_mb:.2f}MB حد {max_size}MB سے تجاوز کرتا ہے"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "سب ٹائٹل ایمبیڈنگ چھوڑ دی گئی: کوالٹی {width}x{height} (کم سائیڈ {min_side}p) حد {max_quality}p سے تجاوز کرتی ہے"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "ٹیکٹوک"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "انسٹاگرام"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "پلے لسٹ"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ {service} کے لیے رینج کی حد سے تجاوز: {count} (زیادہ سے زیادہ {max_count})۔\n\nزیادہ سے زیادہ دستیاب فائلیں ڈاؤن لوڈ کرنے کے لیے ان کمانڈز میں سے ایک استعمال کریں:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ {service} کے لیے رینج کی حد سے تجاوز: {count} (زیادہ سے زیادہ {max_count})\nصارف ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "PO token provider کنفیگ میں غیر فعال ہے"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} YouTube ڈومین نہیں ہے، PO token چھوڑ رہے ہیں"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO token provider {base_url} پر دستیاب نہیں ہے، معیاری YouTube extraction پر واپس جا رہے ہیں"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO token provider کیش صاف کیا گیا، اگلے درخواست پر دستیابی چیک کریں گے"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "App instance ابھی دستیاب نہیں ہے"
    HELPER_USER_NAME_MSG = "صارف"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood wait کا پتہ چلا، {wait_seconds} سیکنڈ کے لیے سلا رہے ہیں"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood wait کا پتہ چلا لیکن وقت نکال نہیں سکے، {retry_delay} سیکنڈ کے لیے سلا رہے ہیں"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno خرابی کا پتہ چلا، {retry_delay} سیکنڈ کے لیے سلا رہے ہیں"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "پروکسی کنفیگریشن نامکمل ہے، براہ راست کنکشن استعمال کر رہے ہیں"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚بند کریں"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚بند کریں"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚بند کریں"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 لاگز فائل ہٹا دی گئی۔"
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 ٹیگز فائل ہٹا دی گئی۔"
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 فارمیٹ فائل ہٹا دی گئی۔"
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 اسپلٹ فائل ہٹا دی گئی۔"
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 میڈیا انفو فائل ہٹا دی گئی۔"
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 سب ٹائٹل کی ترتیبات ہٹا دی گئیں۔"
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 کی بورڈ کی ترتیبات ہٹا دی گئیں۔"
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 آرگس کی ترتیبات ہٹا دی گئیں۔"
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 NSFW کی ترتیبات ہٹا دی گئیں۔"
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 پروکسی کی ترتیبات ہٹا دی گئیں۔"
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 فلڈ ویٹ کی ترتیبات ہٹا دی گئیں۔"
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚بند کریں"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 ویڈیو ڈاؤن لوڈ کمانڈ"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "استعمال: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "مثالیں:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (سیدھا ترتیب)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (الٹا ترتیب)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "یہ بھی دیکھیں: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "صارف {user_id} نے add_bot_to_group کمانڈ بند کی"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "YouTube ID نکالنے میں ناکام"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "تھمب نیل ڈاؤن لوڈ کرنے میں ناکام یا یہ بہت بڑا ہے"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "آڈیو زبان منتخب کریں"
    AA_NO_SUBTITLES_DETECTED_MSG = "کوئی سب ٹائٹلز نہیں ملیں"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "سب ٹائٹل زبان منتخب کریں"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "تصدیق کی خرابی"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "اکاؤنٹ نہیں ملا"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "اکاؤنٹ دستیاب نہیں"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "ریٹ کی حد سے تجاوز"
    GALLERY_DL_NETWORK_ERROR_MSG = "نیٹ ورک خرابی"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "مواد دستیاب نہیں"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "جغرافیائی پابندیاں"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "تصدیق درکار"
    GALLERY_DL_POLICY_VIOLATION_MSG = "پالیسی کی خلاف ورزی"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "نامعلوم خرابی"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ ڈاؤن لوڈ شروع ہو گیا</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚بند کریں"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 ویڈیو ڈاؤن لوڈ کمانڈ</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "استعمال: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>مثالیں:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "یہ بھی دیکھیں: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Flood limit. بعد میں کوشش کریں۔"
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 کوکی کمانڈ کا استعمال</b>

<code>/cookie</code> - کوکی مینو دکھائیں
<code>/cookie youtube</code> - YouTube کوکیز ڈاؤن لوڈ کریں
<code>/cookie instagram</code> - Instagram کوکیز ڈاؤن لوڈ کریں
<code>/cookie tiktok</code> - TikTok کوکیز ڈاؤن لوڈ کریں
<code>/cookie x</code> یا <code>/cookie twitter</code> - Twitter/X کوکیز ڈاؤن لوڈ کریں
<code>/cookie facebook</code> - Facebook کوکیز ڈاؤن لوڈ کریں
<code>/cookie custom</code> - اپنی کوکی کی ہدایات دکھائیں

<i>دستیاب خدمات بوٹ کی ترتیب پر منحصر ہیں۔</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 کوکی فائل ہٹا دی گئی اور کیش صاف کر دی گئی۔"
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ پچھلا"
    SUBS_BACK_BUTTON_MSG = "🔙واپس"
    SUBS_OFF_BUTTON_MSG = "🚫 بند"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - زبان سیٹ کریں"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - AUTO/TRANS کے ساتھ زبان سیٹ کریں"
    SUBS_VALID_OPTIONS_MSG = "درست اختیارات:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 زبان"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 دیو گٹ ہب"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 contr Github"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 صاف"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 کوکیز"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 میڈیا"
    SETTINGS_INFO_BUTTON_MSG = "📖 معلومات"
    SETTINGS_MORE_BUTTON_MSG = "⚙ مزید"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 صرف کوکیز"
    SETTINGS_LOGS_BUTTON_MSG = "📃 لاگز "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ ٹیگز"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 فارمیٹ"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ تقسیم"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 میڈیا انفو"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 سب ٹائٹلز"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 کی بورڈ"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ آرگس"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 پروکسی"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 فلڈ ویٹ"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  تمام فائلیں"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - میری 5 کوکیز ڈاؤن لوڈ کریں"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - براؤزر کی YT-کوکی حاصل کریں"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - اپنی کوکی فائل کی تصدیق کریں"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - اپنی کوکی اپ لوڈ کریں"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - کوالٹی اور فارمیٹ تبدیل کریں"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - MediaInfo آن/آف کریں"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - ویڈیو پارٹ سائز تبدیل کریں"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - ویڈیو کو آڈیو کے طور پر ڈاؤن لوڈ کریں"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - سب ٹائٹل زبان کی ترتیبات"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - پلے لسٹ کیسے ڈاؤن لوڈ کریں"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - gallery-dl کے ذریعے تصاویر ڈاؤن لوڈ کریں"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - اپنے #tags بھیجیں"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - ہدایات حاصل کریں"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - اپنے لاگز بھیجیں"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - پلے لسٹ کی مدد"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - کیسے"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - براہ راست ویڈیو لنکس حاصل کریں"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - پروکسی فعال/غیر فعال کریں"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - کی بورڈ لی آؤٹ"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - ان لائن سرچ ہیلپر"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp آرگومنٹس"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - NSFW بلر کی ترتیبات"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 صفائی کے اختیارات</b>\n\nمنتخب کریں کہ کیا صاف کرنا ہے:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 موبائل: @vid سرچ چالو کریں"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 موبائل: @ویڈ تلاش کو چالو کریں"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 آف"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 مکمل"
    KEYBOARD_1X3_BUTTON_MSG = "x 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "x 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗 [تصاویر url] ({url})"
    IMAGE_ERROR_MSG = "❌ غلطی: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙واپس"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - اپنا فارمیٹ"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p کوالٹی"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K کوالٹی"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K کوالٹی"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - مخصوص فارمیٹ ID"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - ہمیشہ مینو دکھائیں"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/best کوالٹی"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ ہمیشہ پوچھیں (مینو + بٹن)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 دوسرے (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (PC/Mac Telegram کے لیے بہترین)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (موبائل Telegram کے لیے بہترین)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (زیادہ سے زیادہ کوالٹی)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 اپنا (اپنا داخل کریں)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1- {max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 براؤزر سے"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 ٹویٹر/ایکس"
    COOKIES_TIKTOK_BUTTON_MSG = "ik ٹیکٹوک"
    COOKIES_VK_BUTTON_MSG = "📘 vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 انسٹاگرام"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 اپنی"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ غیر فعالی کی وجہ سے ان پٹ موڈ خود بخود بند ہو گیا (5 منٹ)۔"
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 سب ری سیٹ کریں"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 موجودہ دیکھیں"
    ARGS_BACK_BUTTON_MSG = "🔙 واپس"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>ان ترتیبات کو ٹیمپلیٹ کے طور پر محفوظ کرنے کے لیے اس پیغام کو اپنے پسندیدہ میں فارورڈ کریں۔</i> \n\n<i>ان ترتیبات کو لاگو کرنے کے لیے اس پیغام کو یہاں واپس فارورڈ کریں۔</i>"
    ARGS_NO_SETTINGS_MSG = "📋 موجودہ yt-dlp آرگومنٹس:\n\nکوئی اپنی ترتیبات ترتیب نہیں دی گئیں۔\n\n---\n\n<i>ان ترتیبات کو ٹیمپلیٹ کے طور پر محفوظ کرنے کے لیے اس پیغام کو اپنے پسندیدہ میں فارورڈ کریں۔</i> \n\n<i>ان ترتیبات کو لاگو کرنے کے لیے اس پیغام کو یہاں واپس فارورڈ کریں۔</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 موجودہ yt-dlp آرگومنٹس:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 ترتیبات برآمد کریں"
    ARGS_SETTINGS_READY_MSG = "ترتیبات برآمد کے لیے تیار ہیں! اس پیغام کو پسندیدہ میں فارورڈ کریں تاکہ محفوظ کریں۔"
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 موجودہ yt-dlp آرگومنٹس:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ پیغام میں ترتیبات پہچاننے میں ناکام۔ یقینی بنائیں کہ آپ نے صحیح ترتیبات کا ٹیمپلیٹ بھیجا ہے۔"
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ ترتیبات کامیابی سے درآمد کی گئیں!\n\nلاگو کردہ پیرامیٹرز: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "کلیدی ترتیبات:\n"
    ARGS_ERROR_SAVING_MSG = "❌ درآمد شدہ ترتیبات محفوظ کرنے میں خرابی۔"
    ARGS_ERROR_IMPORTING_MSG = "❌ ترتیبات درآمد کرتے وقت ایک خرابی پیش آئی۔"

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>کوکی فائلیں ڈاؤن لوڈ کریں</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "کوکی فائل ڈاؤن لوڈ کرنے کے لیے ایک سروس منتخب کریں۔"
    COOKIE_MENU_SAVE_INFO_MSG = "کوکی فائلیں آپ کے فولڈر میں cookie.txt کے طور پر محفوظ کی جائیں گی۔"
    COOKIE_MENU_TIP_HEADER_MSG = "نصیحت: آپ براہ راست کمانڈ بھی استعمال کر سکتے ہیں:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – کوکیز ڈاؤن لوڈ اور تصدیق کریں"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – انڈیکس کے ذریعے مخصوص ماخذ استعمال کریں (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "پھر <code>/check_cookie</code> کے ساتھ تصدیق کریں (RickRoll پر ٹیسٹ کرتا ہے)۔"

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "ہمیشہ پوچھیں"
    SUBS_AUTO_TRANS_BUTTON_MSG = "خودکار/ترجمہ"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗لنک"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Watch"  # عارضی طور پر غیر فعال: poketube سروس ڈاؤن ہے
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝تفصیل"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ کاٹنا"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>ویڈیو کاٹنا</b>\n\nویڈیو کی مدت: <b>{start_time} - {end_time}</b>\n\nبراہ کرم مطلوبہ وقت کی حد فارمیٹ میں بھیجیں:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nمثال: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ غلط فارمیٹ۔ براہ کرم استعمال کریں: <code>HH:MM:SS-HH:MM:SS</code>\n\nمثال: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ غلط حد۔ شروع کا وقت اختتام کے وقت سے کم ہونا چاہیے۔"
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ وقت کی حد ویڈیو کی حدود سے باہر ہے۔\n\nویڈیو کی مدت: <b>{start_time} - {end_time}</b>\n\nآپ کی حد ان حدود کے اندر ہونی چاہیے۔"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ جزوی طور پر مکمل - {successful_uploads}/{total_files} آڈیو فائلیں اپ لوڈ کی گئیں۔"
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ آڈیو کامیابی سے ڈاؤن لوڈ اور بھیج دی گئی - {total_files} فائلیں اپ لوڈ کی گئیں۔"

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>نجی TikTok اکاؤنٹ</b>\n\n"
        "یہ TikTok اکاؤنٹ نجی ہے یا تمام ویڈیوز نجی ہیں۔\n\n"
        "<b>💡 حل:</b>\n"
        "1. اکاؤنٹ @{username} کو فالو کریں\n"
        "2. <code>/cookie</code> کمانڈ کا استعمال کرتے ہوئے اپنی کوکیز بوٹ کو بھیجیں\n"
        "3. دوبارہ کوشش کریں\n\n"
        "<b>کوکیز اپ ڈیٹ کرنے کے بعد، دوبارہ کوشش کریں!</b>"
    )

    #######################################################
