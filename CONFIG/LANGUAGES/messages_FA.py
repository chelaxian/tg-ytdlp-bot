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
    CREDITS_MSG = "<blockquote><i>مدیریت شده توسط</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 تغییر زبان: /lang</b>"
    TO_USE_MSG = "<i>برای استفاده از این ربات باید به کانال تلگرام @tg_ytdlp مشترک شوید.</i>\nپس از پیوستن به کانال، <b>لینک ویدیوی خود را دوباره ارسال کنید و ربات آن را برای شما دانلود می‌کند</b> ❤️\n\n<blockquote>P.S. به دلیل محتوای احتمالی 🔞NSFW - دانلود از ☁️<b>ذخیره‌سازی ابری</b>، 📁<b>اشتراک‌گذاری فایل</b>، 🔗<b>کوتاه‌کننده‌های URL</b> و 🔞<b>سایت‌های مستهجن</b> پولی است! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ کانال @tg_ytdlp را 🗑<b>حذف/لغو اشتراک نکنید</b> و به ربات 🤖<b>URL/دستورات را بیش از حد اسپم نکنید</b> - به‌طور خودکار از استفاده ربات محروم می‌شوید ⛔️</blockquote>"

    ERROR1 = "لینک URL یافت نشد. لطفاً یک URL با <b>https://</b> یا <b>http://</b> وارد کنید"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>لیست‌های پخش (yt-dlp)</b>

برای دانلود لیست‌های پخش، URL آن را با محدوده‌های <code>*start*end</code> در انتها ارسال کنید. به عنوان مثال: <code>URL*1*5</code> (5 ویدیوی اول از 1 تا 5 شامل).<code>URL*-1*-5</code> (5 ویدیوی آخر از 1 تا 5 شامل).
یا می‌توانید از <code>/vid از-تا URL</code> استفاده کنید. به عنوان مثال: <code>/vid 3-7 URL</code> (ویدیوها را از 3 تا 7 شامل از ابتدا دانلود می‌کند). <code>/vid -3-7 URL</code> (ویدیوها را از 3 تا 7 شامل از انتها دانلود می‌کند). برای دستور <code>/audio</code> نیز کار می‌کند.

<b>مثال‌ها:</b>

🟥 <b>محدوده ویدیو از لیست پخش YouTube:</b> (نیاز به 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(5 ویدیوی اول از 1 تا 5 شامل را دانلود می‌کند)
🟥 <b>ویدیوی تکی از لیست پخش YouTube:</b> (نیاز به 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(فقط ویدیوی سوم را دانلود می‌کند)

⬛️ <b>پروفایل TikTok:</b> (نیاز به 🍪 شما)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(10 ویدیوی اول از پروفایل کاربر را دانلود می‌کند)

🟪 <b>استوری‌های Instagram:</b> (نیاز به 🍪 شما)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(3 استوری اول را دانلود می‌کند)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(10 استوری اول از آلبوم را دانلود می‌کند)

🟦 <b>ویدیوهای VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(3 ویدیوی اول از پروفایل کاربر/گروه را دانلود می‌کند)

⬛️<b>کانال‌های Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(ویدیوها را از 2 تا 4 شامل از کانال دانلود می‌کند)

🟪 <b>کلیپ‌های Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(3 کلیپ اول از کانال را دانلود می‌کند)

🟦 <b>گروه‌های Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(2 ویدیوی اول از گروه را دانلود می‌کند)

🟧 <b>مدل‌های Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(2 ویدیوی اول از پروفایل مدل را دانلود می‌کند)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(3 ویدیوی اول از نتایج جستجو بر اساس درخواست شما را دانلود می‌کند)

و غیره...
<a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">لیست سایت‌های پشتیبانی شده</a> را ببینید
</blockquote>

<blockquote expandable>🖼 <b>تصاویر (gallery-dl)</b>

از <code>/img URL</code> برای دانلود تصاویر/عکس‌ها/آلبوم‌ها از پلتفرم‌های مختلف استفاده کنید.

<b>مثال‌ها:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>محدوده‌ها:</b>
<code>/img 11-20 https://example.com/album</code> — موارد 11..20
<code>/img 11- https://example.com/album</code> — از 11 تا انتها (یا محدودیت ربات)

<i>پلتفرم‌های پشتیبانی شده شامل vk، 2ch، 35photo، 4chan، 500px، ArtStation، Boosty، Civitai، Cyberdrop، DeviantArt، Discord، Facebook، Fansly، Instagram، Pinterest، Reddit، TikTok، Tumblr، Twitter/X، JoyReactor و غیره است. لیست کامل:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">سایت‌های پشتیبانی شده توسط gallery-dl</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>ربات دانلود ویدیو - راهنما</b>

📥 <b>استفاده پایه:</b>
• ارسال هر لینکی → ربات آن را دانلود می‌کند
  <i>ربات به طور خودکار سعی می‌کند ویدیوها را از طریق yt-dlp و تصاویر را از طریق gallery-dl دانلود کند.</i>
• <b>چندین URL:</b> در حالت انتخاب کیفیت (<code>/format</code>) می‌توانید تا <b>10 URL</b> را در یک پیام ارسال کنید. هر URL در یک خط جدید یا با فاصله جدا شده است.
• <code>/audio URL</code> → استخراج صدا
• <code>/link [quality] URL</code> → دریافت لینک‌های مستقیم
• <code>/proxy</code> → فعال/غیرفعال کردن پروکسی برای همه دانلودها
• پاسخ به ویدیو با متن → تغییر عنوان

📋 <b>لیست‌های پخش و محدوده‌ها:</b>
• <code>URL*1*5</code> → دانلود 5 ویدیوی اول
• <code>URL*-1*-5</code> → دانلود 5 ویدیوی آخر
• <code>/vid 3-7 URL</code> → تبدیل به <code>URL*3*7</code> می‌شود
• <code>/vid -3-7 URL</code> → تبدیل به <code>URL*-3*-7</code> می‌شود

🍪 <b>کوکی‌ها و خصوصی:</b>
• آپلود *.txt کوکی برای ویدیوهای خصوصی
• <code>/cookie [service]</code> → دانلود کوکی‌ها (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → انتخاب منبع بر اساس فهرست (1–N)
• <code>/cookies_from_browser</code> → استخراج از مرورگر
• <code>/check_cookie</code> → تأیید کوکی
• <code>/save_as_cookie</code> → ذخیره متن به عنوان کوکی

🧹 <b>پاکسازی:</b>
• <code>/clean</code> → فقط فایل‌های رسانه
• <code>/clean all</code> → همه چیز
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>تنظیمات:</b>
• <code>/settings</code> → منوی تنظیمات
• <code>/format</code> → کیفیت و فرمت
• <code>/split</code> → تقسیم ویدیو به بخش‌ها
• <code>/mediainfo on/off</code> → اطلاعات رسانه
• <code>/nsfw on/off</code> → تار کردن NSFW
• <code>/tags</code> → مشاهده تگ‌های ذخیره شده
• <code>/sub on/off</code> → زیرنویس‌ها
• <code>/keyboard</code> → صفحه کلید (OFF/1x3/2x3)

🏷️ <b>تگ‌ها:</b>
• افزودن <code>#tag1#tag2</code> بعد از URL
• تگ‌ها در عنوان‌ها ظاهر می‌شوند
• <code>/tags</code> → مشاهده همه تگ‌ها

🔗 <b>لینک‌های مستقیم:</b>
• <code>/link URL</code> → بهترین کیفیت
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → کیفیت خاص

⚙️ <b>دستورات سریع:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → تنظیم کیفیت
• <code>/keyboard off/1x3/2x3/full</code> → چیدمان صفحه کلید
• <code>/split 100mb-2000mb</code> → تغییر اندازه بخش
• <code>/subs off/ru/en auto</code> → زبان زیرنویس
• <code>/list URL</code> → فهرست فرمت‌های موجود
• <code>/mediainfo on/off</code> → روشن/خاموش کردن اطلاعات رسانه
• <code>/proxy on/off</code> → فعال/غیرفعال کردن پروکسی برای همه دانلودها

📊 <b>اطلاعات:</b>
• <code>/usage</code> → تاریخچه دانلود
• <code>/search</code> → جستجوی درون خطی از طریق @vid

🖼 <b>تصاویر:</b>
• <code>URL</code> → دانلود URL تصاویر
• <code>/img URL</code> → دانلود تصاویر از URL
• <code>/img 11-20 URL</code> → دانلود محدوده خاص
• <code>/img 11- URL</code> → دانلود از 11ام تا آخر

👨‍💻 <i>توسعه‌دهنده:</i> @upekshaip
🤝 <i>مشارکت‌کننده:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "فقط کوکی خود را به عنوان <b><u>cookie.txt</u></b> ذخیره کنید و آن را به عنوان سند به ربات ارسال کنید.\n\n"
        "همچنین می‌توانید کوکی‌ها را به صورت متن ساده با دستور <b><u>/save_as_cookie</u></b> ارسال کنید.\n"
        "<b>استفاده از <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>دستورالعمل‌ها:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message
    SEARCH_MSG = """
🔍 <b>جستجوی ویدیو</b>

دکمه زیر را فشار دهید تا جستجوی درون خطی از طریق @vid فعال شود.

<blockquote>در رایانه فقط <b>"@vid Your_Search_Query"</b> را در هر چتی تایپ کنید.</blockquote>
    """
    
    # Settings and Hints
    
    
    IMG_HELP_MSG = (
        "<b>🖼 دستور دانلود تصویر</b>\n\n"
        "استفاده: <code>/img URL</code>\n\n"
        "<b>مثال‌ها:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>پلتفرم‌های پشتیبانی شده (مثال‌ها):</b>\n"
        "<blockquote>vk، 2ch، 35photo، 4chan، 500px، ArtStation، Boosty، Civitai، Cyberdrop، DeviantArt، Discord، Facebook، Fansly، Instagram، Patreon، Pinterest، Reddit، TikTok، Tumblr، Twitter/X، JoyReactor و غیره — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">لیست کامل</a></blockquote>"
        "همچنین ببینید: "
    )
    
    LINK_HINT_MSG = (
        "دریافت لینک‌های مستقیم ویدیو با انتخاب کیفیت.\n\n"
        "استفاده: /link + URL \n\n"
        "(مثلاً /link https://youtu.be/abc123)\n"
        "(مثلاً /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>افزودن ربات به گروه</b>

ربات‌های من را به گروه‌های خود اضافه کنید تا ویژگی‌های پیشرفته و محدودیت‌های بالاتر دریافت کنید!
————————————
📊 <b>محدودیت‌های رایگان فعلی (در DM ربات):</b>
<blockquote>•🗑 آشفتگی از همه فایل‌های مرتب نشده 👎
• حداکثر اندازه 1 فایل: <b>8 GB </b>
• حداکثر کیفیت 1 فایل: <b>نامحدود</b>
• حداکثر مدت زمان 1 فایل: <b>نامحدود</b>
• حداکثر تعداد دانلود: <b>نامحدود</b>
• حداکثر URL در یک پیام: <b>10</b> (فقط در حالت انتخاب کیفیت)
• حداکثر موارد لیست پخش در 1 بار: <b>50</b>
• حداکثر ویدیوهای TikTok در 1 بار: <b>500</b>
• حداکثر تصاویر در 1 بار: <b>1000</b>
• محدودیت‌های نرخ URL: <b>5/دقیقه، 60/ساعت، 1000/روز</b>
• محدودیت دستور: <b>20/دقیقه</b>
• حداکثر زمان 1 دانلود: <b>2 ساعت</b>
• 🔞 محتوای NSFW پولی است! 1⭐️ = $0.02
• 🆓 همه رسانه‌های دیگر کاملاً رایگان هستند
• 📝 همه لاگ‌های محتوا و کش به کانال‌های لاگ من برای بازنشر فوری هنگام دانلود مجدد</blockquote>

💬<b>این محدودیت‌ها فقط برای ویدیو با زیرنویس:</b>
<blockquote>• حداکثر مدت زمان ویدیو+زیرنویس: <b>1.5 ساعت</b>
• حداکثر اندازه فایل ویدیو+زیرنویس: <b>500 MB</b>
• حداکثر کیفیت ویدیو+زیرنویس: <b>720p</b></blockquote>
————————————
🚀 <b>مزایای گروه پولی (2️⃣x محدودیت‌ها):</b>
<blockquote>•  🗂 مخزن رسانه منظم ساختاریافته مرتب شده بر اساس موضوعات 👍
•  📁 ربات‌ها در موضوعی که آنها را فراخوانی می‌کنید پاسخ می‌دهند
•  📌 پیام وضعیت خودکار با پیشرفت دانلود
•  🖼 دستور /img رسانه را به عنوان آلبوم‌های 10 موردی دانلود می‌کند
• حداکثر اندازه 1 فایل: <b>16 GB</b> ⬆️
• حداکثر URL در یک پیام: <b>20</b> ⬆️ (فقط در حالت انتخاب کیفیت)
• حداکثر موارد لیست پخش در 1 بار: <b>100</b> ⬆️
• حداکثر ویدیوهای TikTok در 1 بار: 1000 ⬆️
• حداکثر تصاویر در 1 بار: 2000 ⬆️
• محدودیت‌های نرخ URL: <b>10/دقیقه، 120/ساعت، 2000/روز</b> ⬆️
• محدودیت دستور: <b>40/دقیقه</b> ⬆️
• حداکثر زمان 1 دانلود: <b>4 ساعت</b> ⬆️
• 🔞 محتوای NSFW: رایگان با متادیتای کامل 🆓
• 📢 نیازی به اشتراک در کانال من برای گروه‌ها نیست
• 👥 همه اعضای گروه به عملکردهای پولی دسترسی خواهند داشت!
• 🗒 بدون لاگ / بدون کش به کانال‌های لاگ من! می‌توانید کپی/بازنشر را در تنظیمات گروه رد کنید</blockquote>

💬 <b>2️⃣x محدودیت‌ها برای ویدیو با زیرنویس:</b>
<blockquote>• حداکثر مدت زمان ویدیو+زیرنویس: <b>3 ساعت</b> ⬆️
• حداکثر اندازه فایل ویدیو+زیرنویس: <b>1000 MB</b> ⬆️
• حداکثر کیفیت ویدیو+زیرنویس: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>قیمت‌گذاری و راه‌اندازی:</b>
<blockquote>• قیمت: <b>$5/ماه</b> برای 1 ربات در گروه
• راه‌اندازی: تماس با @iilililiiillliiliililliilliliiil
• پرداخت: 💎TON یا روش‌های دیگر💲
• پشتیبانی: پشتیبانی فنی کامل شامل می‌شود</blockquote>
————————————
می‌توانید ربات‌های من را به گروه خود اضافه کنید تا 🔞<b>NSFW</b> رایگان را باز کنید و همه محدودیت‌ها را دو برابر (x2️⃣) کنید.
اگر می‌خواهید من اجازه دهم گروه شما از ربات‌های من استفاده کند با من تماس بگیرید @iilililiiillliiliililliilliliiil
————————————
💡<b>نکته:</b> <blockquote>می‌توانید با هر تعداد از دوستان خود (مثلاً 100 نفر) پول جمع کنید و 1 خرید برای کل گروه انجام دهید - همه اعضای گروه دسترسی کامل نامحدود به همه عملکردهای ربات در آن گروه را فقط با <b>0.05$</b> خواهند داشت</blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>حالت NSFW: روشن✅</b>

• محتوای NSFW بدون تار شدن نمایش داده می‌شود.
• اسپویلرها به رسانه NSFW اعمال نمی‌شوند.
• محتوا فوراً قابل مشاهده خواهد بود

<i>از /nsfw off برای فعال کردن تار استفاده کنید</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>حالت NSFW: خاموش</b>

⚠️ <b>تار فعال شده</b>
• محتوای NSFW زیر اسپویلر پنهان خواهد شد   
• برای مشاهده، باید روی رسانه کلیک کنید
• اسپویلرها به رسانه NSFW اعمال می‌شوند.

<i>از /nsfw on برای غیرفعال کردن تار استفاده کنید</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>پارامتر نامعتبر</b>

استفاده کنید:
• <code>/nsfw on</code> - غیرفعال کردن تار
• <code>/nsfw off</code> - فعال کردن تار
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>بررسی کش...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 در حال پردازش..."
    DOWNLOADING_MSG = "📥 <b>در حال دانلود رسانه...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>در حال دانلود تصویر...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>دانلود کامل شد</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "دانلود شده:"
    SENT_STATUS_MSG = "ارسال شده:"
    PENDING_TO_SEND_STATUS_MSG = "در انتظار ارسال:"
    TITLE_LABEL_MSG = "عنوان:"
    MEDIA_COUNT_LABEL_MSG = "تعداد رسانه:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "دانلود تمام شد، در حال پردازش صدا..."
    VIDEO_PROCESSING_MSG = "📽 ویدیو در حال پردازش است..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>از کش ارسال شد</b>\n\nآلبوم‌های ارسال شده: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ ویدیو با موفقیت از کش ارسال شد."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ ویدیوهای لیست پخش از کش ارسال شدند ({cached}/{total} فایل)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} ویدیو از کش ارسال شد، در حال دانلود موارد گمشده..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ از کش ارسال شد: {cached}\n🔄 ادامه دانلود..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 نتوانست رسانه را تجزیه و تحلیل کند، با حداکثر محدوده مجاز ادامه می‌دهد (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 نتوانست تعداد رسانه را تعیین کند، با حداکثر محدوده مجاز ادامه می‌دهد (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 نتوانست تعداد کل رسانه را تعیین کند، با محدوده مشخص شده ادامه می‌دهد {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>URL نامعتبر</b>\n\nلطفاً یک URL معتبر که با http:// یا https:// شروع می‌شود ارائه دهید"

    ERROR_OCCURRED_MSG = "❌ <b>خطا رخ داد</b>\n\n<code>{url}</code>\n\nخطا: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ خطا در ارسال ویدیو: {error}"
    ERROR_UNKNOWN_MSG = "❌ خطای ناشناخته: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ فضای دیسک کافی برای دانلود ویدیوها نیست."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ اندازه فایل از محدودیت {limit} GB تجاوز می‌کند. لطفاً یک فایل کوچکتر در اندازه مجاز انتخاب کنید."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>دانلود ویدیو با تمام پروکسی‌های موجود ناموفق بود</b>\n\nهمه تلاش‌های دانلود از طریق پروکسی ناموفق بوده است.\nامتحان کنید:\n• بررسی عملکرد پروکسی\n• امتحان پروکسی دیگری از لیست\n• دانلود بدون پروکسی (در صورت امکان)"

    ERROR_GETTING_LINK_MSG = "❌ <b>خطا در دریافت لینک:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ تلگرام ارسال پیام را محدود کرده است.\n⏳ لطفاً صبر کنید: {time}\nبرای به‌روزرسانی تایمر، URL را دوباره 2 بار ارسال کنید."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ تلگرام ارسال پیام را محدود کرده است.\n⏳ لطفاً صبر کنید: \nبرای به‌روزرسانی تایمر، URL را دوباره 2 بار ارسال کنید."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ دانلود زیرنویس‌ها ناموفق بود"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>لینک‌های استریم مستقیم</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>عنوان:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>مدت زمان:</b> {duration} ثانیه\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ خطا: پیام اصلی یافت نشد."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ تگ #{tag} شامل کاراکترهای ممنوع است. فقط حروف، اعداد و _ مجاز است.\nلطفاً استفاده کنید: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ ویدیوهای لیست پخش ارسال شدند: {sent}/{total} فایل."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>نکته درباره لیست پخش</b>

شما لینک لیست پخش را بدون مشخص کردن محدوده ارسال کردید. ربات به طور خودکار اولین ویدیو را دانلود کرد (<code>*1*1</code>).

<b>برای دانلود چندین ویدیو از لیست پخش، محدوده را مشخص کنید:</b>
• <code>URL*1*5</code> — 5 ویدیوی اول (از 1 تا 5 شامل)
• <code>URL*3*3</code> — فقط ویدیوی سوم
• <code>/vid 1-10 URL</code> — فرمت جایگزین

بیشتر بدانید: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ از کش ارسال شد: {cached}/{total} فایل."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ دریافت لینک‌های استریم ناموفق بود"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "مرورگری را برای دانلود کوکی‌ها انتخاب کنید:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "هیچ مرورگری در این سیستم یافت نشد. می‌توانید کوکی‌ها را از URL از راه دور دانلود کنید یا وضعیت مرورگر را نظارت کنید:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>باز کردن مرورگر</b> - برای نظارت بر وضعیت مرورگر در مینی‌اپ"
    BROWSER_OPEN_BUTTON_MSG = "🌐 باز کردن مرورگر"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 دانلود از URL از راه دور"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ فایل کوکی YouTube از طریق fallback دانلود شد و به عنوان cookie.txt ذخیره شد"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ هیچ مرورگر پشتیبانی شده‌ای یافت نشد و COOKIE_URL پیکربندی نشده است. از /cookie استفاده کنید یا cookie.txt را آپلود کنید."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL باید به یک فایل .txt اشاره کند."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ فایل کوکی fallback خیلی بزرگ است (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ منبع کوکی fallback در دسترس نیست (وضعیت {status}). /cookie را امتحان کنید یا cookie.txt را آپلود کنید."
    COOKIE_FALLBACK_ERROR_MSG = "❌ خطا در دانلود کوکی fallback. /cookie را امتحان کنید یا cookie.txt را آپلود کنید."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ خطای غیرمنتظره در حین دانلود کوکی fallback."
    BTN_CLOSE = "🔚بستن"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ مقدار بولی نامعتبر"
    ARGS_CLOSED_MSG = "بسته شد"
    ARGS_ALL_RESET_MSG = "✅ همه آرگومان‌ها بازنشانی شدند"
    ARGS_RESET_ERROR_MSG = "❌ خطا در بازنشانی آرگومان‌ها"
    ARGS_INVALID_PARAM_MSG = "❌ پارامتر نامعتبر"
    ARGS_BOOL_SET_MSG = "تنظیم شده به {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "قبلاً به {value} تنظیم شده"
    ARGS_INVALID_SELECT_MSG = "❌ مقدار انتخاب نامعتبر"
    ARGS_VALUE_SET_MSG = "تنظیم شده به {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "قبلاً به {value} تنظیم شده"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>مقدار فعلی:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>مثال‌ها:</b>\n• <code>default</code> - استفاده از استراتژی XFF پیش‌فرض\n• <code>never</code> - هرگز از هدر XFF استفاده نکن\n• <code>US</code> - کد کشور ایالات متحده\n• <code>GB</code> - کد کشور بریتانیا\n• <code>DE</code> - کد کشور آلمان\n• <code>FR</code> - کد کشور فرانسه\n• <code>JP</code> - کد کشور ژاپن\n• <code>192.168.1.0/24</code> - بلوک IP (CIDR)\n• <code>10.0.0.0/8</code> - محدوده IP خصوصی\n• <code>203.0.113.0/24</code> - بلوک IP عمومی\n\n"
    ARGS_XFF_NOTE_MSG = "<b>یادداشت:</b> این جایگزین گزینه‌های --geo-bypass می‌شود. از هر کد کشور 2 حرفی یا بلوک IP در نماد CIDR استفاده کنید.\n\n"
    ARGS_EXAMPLE_MSG = "<b>مثال:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "لطفاً مقدار جدید خود را ارسال کنید."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>محدوده:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "لطفاً یک عدد ارسال کنید."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>مثال‌ها:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>یادداشت:</b> این هدرها به هدرهای Referer و User-Agent موجود اضافه می‌شوند.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 آرگومان‌های فعلی yt-dlp:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - سوئیچ‌های True/False\n• 📋 <b>Select</b> - انتخاب از گزینه‌ها\n• 🔢 <b>Numeric</b> - ورودی عدد\n• 📝🔧 <b>Text</b> - ورودی متن/JSON</blockquote>\n\nاین تنظیمات به همه دانلودهای شما اعمال می‌شود."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "اجبار اتصالات IPv6",
        "force_ipv4": "اجبار اتصالات IPv4", 
        "no_live_from_start": "استریم‌های زنده را از ابتدا دانلود نکن",
        "live_from_start": "استریم‌های زنده را از ابتدا دانلود کن",
        "no_check_certificates": "سرکوب اعتبارسنجی گواهی HTTPS",
        "check_certificate": "بررسی گواهی SSL",
        "no_playlist": "فقط یک ویدیو دانلود کن، نه لیست پخش",
        "embed_metadata": "جاسازی متادیتا در فایل ویدیو",
        "embed_thumbnail": "جاسازی بندانگشتی در فایل ویدیو",
        "write_thumbnail": "نوشتن بندانگشتی به فایل",
        "ignore_errors": "نادیده گرفتن خطاهای دانلود و ادامه",
        "legacy_server_connect": "اجازه اتصال به سرورهای قدیمی",
        "concurrent_fragments": "تعداد قطعات همزمان برای دانلود",
        "xff": "استراتژی هدر X-Forwarded-For",
        "user_agent": "هدر User-Agent",
        "impersonate": "تقلید مرورگر",
        "referer": "هدر Referer",
        "geo_bypass": "دور زدن محدودیت‌های جغرافیایی",
        "hls_use_mpegts": "استفاده از MPEG-TS برای HLS",
        "no_part": "استفاده نکردن از فایل‌های .part",
        "no_continue": "از سرگیری دانلودهای جزئی نکن",
        "audio_format": "فرمت صدا",
        "video_format": "فرمت ویدیو",
        "merge_output_format": "فرمت خروجی ادغام",
        "send_as_file": "ارسال به عنوان فایل",
        "username": "نام کاربری",
        "password": "رمز عبور",
        "twofactor": "کد احراز هویت دو عاملی",
        "min_filesize": "حداقل اندازه فایل (MB)",
        "max_filesize": "حداکثر اندازه فایل (MB)",
        "playlist_items": "موارد لیست پخش",
        "date": "تاریخ",
        "datebefore": "تاریخ قبل از",
        "dateafter": "تاریخ بعد از",
        "http_headers": "هدرهای HTTP",
        "sleep_interval": "فاصله خواب",
        "max_sleep_interval": "حداکثر فاصله خواب",
        "retries": "تعداد تلاش‌های مجدد",
        "http_chunk_size": "اندازه قطعه HTTP",
        "sleep_subtitles": "خواب برای زیرنویس‌ها"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ پیکربندی آرگومان‌های yt-dlp</b>\n\n<blockquote>📋 <b>گروه‌ها:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ پیکربندی آرگومان‌های yt-dlp</b>\n\n"
        "<blockquote>📋 <b>گروه‌ها:</b>\n"
        "• ✅/❌ <b>Boolean</b> - سوئیچ‌های True/False\n"
        "• 📋 <b>Select</b> - انتخاب از گزینه‌ها\n"
        "• 🔢 <b>Numeric</b> - ورودی عدد\n"
        "• 📝🔧 <b>Text</b> - ورودی متن/JSON</blockquote>\n\n"
        "این تنظیمات به همه دانلودهای شما اعمال می‌شود."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ لطفاً صبر کنید..."
    ERROR_OCCURRED_SHORT_MSG = "❌ خطا رخ داد"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ حالت ورودی به دلیل عدم فعالیت به طور خودکار بسته شد (5 دقیقه)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ ورودی شامل محتوای بالقوه خطرناک است: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ ورودی خیلی طولانی است (حداکثر 1000 کاراکتر)"
    ARGS_INVALID_URL_MSG = "❌ فرمت URL نامعتبر است. باید با http:// یا https:// شروع شود"
    ARGS_INVALID_JSON_MSG = "❌ فرمت JSON نامعتبر است"
    ARGS_NUMBER_RANGE_MSG = "❌ عدد باید بین {min_val} و {max_val} باشد"
    ARGS_INVALID_NUMBER_MSG = "❌ فرمت عدد نامعتبر است"
    ARGS_DATE_FORMAT_MSG = "❌ تاریخ باید به فرمت YYYYMMDD باشد (مثلاً 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ سال باید بین 1900 و 2100 باشد"
    ARGS_MONTH_RANGE_MSG = "❌ ماه باید بین 01 و 12 باشد"
    ARGS_DAY_RANGE_MSG = "❌ روز باید بین 01 و 31 باشد"
    ARGS_INVALID_DATE_MSG = "❌ فرمت تاریخ نامعتبر است"
    ARGS_INVALID_XFF_MSG = "❌ XFF باید 'default'، 'never'، کد کشور (مثلاً US) یا بلوک IP (مثلاً 192.168.1.0/24) باشد"
    ARGS_NO_CUSTOM_MSG = "هیچ آرگومان سفارشی تنظیم نشده است. همه پارامترها از مقادیر پیش‌فرض استفاده می‌کنند."
    ARGS_RESET_SUCCESS_MSG = "✅ همه آرگومان‌ها به پیش‌فرض بازنشانی شدند."
    ARGS_TEXT_TOO_LONG_MSG = "❌ متن خیلی طولانی است. حداکثر 500 کاراکتر."
    ARGS_ERROR_PROCESSING_MSG = "❌ خطا در پردازش ورودی. لطفاً دوباره تلاش کنید."
    ARGS_BOOL_INPUT_MSG = "❌ لطفاً 'True' یا 'False' را برای گزینه ارسال به عنوان فایل وارد کنید."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ لطفاً یک عدد معتبر وارد کنید."
    ARGS_BOOL_VALUE_REQUEST_MSG = "لطفاً <code>True</code> یا <code>False</code> را برای فعال/غیرفعال کردن این گزینه ارسال کنید."
    ARGS_JSON_VALUE_REQUEST_MSG = "لطفاً JSON معتبر ارسال کنید."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "شما هنوز تگ ندارید."
    TAGS_MESSAGE_CLOSED_MSG = "پیام تگ بسته شد."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ زیرنویس‌ها غیرفعال شد و حالت Always Ask خاموش شد."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Always Ask فعال شد."
    SUBS_LANGUAGE_SET_MSG = "✅ زبان زیرنویس به این تنظیم شد: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️هشدار: به دلیل تأثیر زیاد CPU این عملکرد بسیار کند است (نزدیک به زمان واقعی) و محدود به:\n"
        "- کیفیت حداکثر 720p\n"
        "- مدت زمان حداکثر 1.5 ساعت\n"
        "- اندازه ویدیو حداکثر 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>دستورات سریع:</b>\n"
        "• <code>/subs off</code> - غیرفعال کردن زیرنویس‌ها\n"
        "• <code>/subs on</code> - فعال کردن حالت Always Ask\n"
        "• <code>/subs ru</code> - تنظیم زبان\n"
        "• <code>/subs ru auto</code> - تنظیم زبان با AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 زیرنویس‌ها غیرفعال هستند"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} زبان انتخاب شده: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 در حال دانلود زیرنویس‌ها..."
    SUBS_DISABLED_ERROR_MSG = "❌ زیرنویس‌ها غیرفعال هستند. از /subs برای پیکربندی استفاده کنید."
    SUBS_YOUTUBE_ONLY_MSG = "❌ دانلود زیرنویس فقط برای YouTube پشتیبانی می‌شود."
    SUBS_CAPTION_MSG = (
        "<b>💬 زیرنویس‌ها</b>\n\n"
        "<b>ویدیو:</b> {title}\n"
        "<b>زبان:</b> {lang}\n"
        "<b>Type:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 فایل SRT زیرنویس برای کاربر ارسال شد."
    SUBS_ERROR_PROCESSING_MSG = "❌ خطا در پردازش فایل زیرنویس."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ دانلود زیرنویس‌ها ناموفق بود."
    SUBS_ERROR_MSG = "❌ خطا در دانلود زیرنویس‌ها: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ اندازه بخش تقسیم به این تنظیم شد: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **اندازه نامعتبر!**\n\n"
        "**محدوده معتبر:** 100MB تا 2GB\n\n"
        "**فرمت‌های معتبر:**\n"
        "• `100mb` تا `2000mb` (مگابایت)\n"
        "• `0.1gb` تا `2gb` (گیگابایت)\n\n"
        "**مثال‌ها:**\n"
        "• `/split 100mb` - 100 مگابایت\n"
        "• `/split 500mb` - 500 مگابایت\n"
        "• `/split 1.5gb` - 1.5 گیگابایت\n"
        "• `/split 2gb` - 2 گیگابایت\n"
        "• `/split 2000mb` - 2000 مگابایت (2GB)\n\n"
        "**پیش‌تنظیمات:**\n"
        "• `/split 250mb`، `/split 500mb`، `/split 1gb`، `/split 1.5gb`، `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **حداکثر اندازه بخش برای تقسیم ویدیو را انتخاب کنید:**\n\n"
        "**محدوده:** 100MB تا 2GB\n\n"
        "**دستورات سریع:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**مثال‌ها:** `/split 300mb`، `/split 1.2gb`، `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "منو بسته شد."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>تنظیمات ربات</b>\n\nیک دسته انتخاب کنید:"
    SETTINGS_MENU_CLOSED_MSG = "منو بسته شد."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 گزینه‌های پاکسازی</b>\n\nانتخاب کنید چه چیزی را پاک کنید:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 کوکی‌ها</b>\n\nیک عمل انتخاب کنید:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 رسانه</b>\n\nیک عمل انتخاب کنید:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 اطلاعات</b>\n\nیک عمل انتخاب کنید:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ دستورات بیشتر</b>\n\nیک عمل انتخاب کنید:"
    SETTINGS_COMMAND_EXECUTED_MSG = "دستور اجرا شد."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ محدودیت سیل. بعداً تلاش کنید."
    SETTINGS_HINT_SENT_MSG = "راهنما ارسال شد."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "کمک‌کننده جستجو باز شد."
    SETTINGS_UNKNOWN_COMMAND_MSG = "دستور ناشناخته."
    SETTINGS_HINT_CLOSED_MSG = "راهنما بسته شد."
    SETTINGS_HELP_SENT_MSG = "ارسال فایل راهنمای txt به کاربر"
    SETTINGS_MENU_OPENED_MSG = "منوی /settings باز شد"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 کمک‌کننده جستجو بسته شد"
    SEARCH_CLOSED_MSG = "بسته شد"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ پروکسی {status}."
    PROXY_ERROR_SAVING_MSG = "❌ خطا در ذخیره تنظیمات پروکسی."
    PROXY_MENU_TEXT_MSG = "فعال یا غیرفعال کردن استفاده از سرور پروکسی برای تمام عملیات yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "با استفاده از سرورهای پراکسی ({config_count} + {file_count} موجود) برای همه عملیات yt-dlp فعال یا غیرفعال شود؟\n\nوقتی ALL (AUTO) فعال باشد، پراکسی‌ها بر اساس کشورهای مجاز (درج شده در خطای YouTube) به‌طور خودکار انتخاب می‌شوند."
    PROXY_MENU_CLOSED_MSG = "منو بسته شد."
    PROXY_ENABLED_CONFIRM_MSG = "✅ پروکسی فعال شد. تمام عملیات yt-dlp از پروکسی استفاده خواهند کرد."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ پروکسی فعال شد. تمام عملیات yt-dlp از {count} سرور پروکسی با روش انتخاب {method} استفاده خواهند کرد."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ پروکسی فعال است (خودکار هنگام خطای YouTube).\n\nوقتی YouTube خطای محدودیت جغرافیایی برگرداند، ربات فقط از پروکسی کشورهای ذکر شده در آن خطا استفاده می‌کند (بدون امتحان متوالی همه پروکسی‌ها)."
    PROXY_DISABLED_MSG = "❌ پروکسی غیرفعال شد."
    PROXY_TRYING_COUNTRY_MSG = "🔄 در حال امتحان پروکسی: {country} ({current}/{total})"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ خطا در ذخیره تنظیمات پروکسی."
    PROXY_ENABLED_CALLBACK_MSG = "پروکسی فعال شد."
    PROXY_DISABLED_CALLBACK_MSG = "پروکسی غیرفعال شد."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ تا پایان دانلود قبلی صبر کنید"
    AUDIO_HELP_MSG = (
        "<b>🎧 دستور دانلود صدا</b>\n\n"
        "استفاده: <code>/audio URL</code>\n\n"
        "<b>مثال‌ها:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "همچنین ببینید: /vid، /img، /help، /playlist، /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "راهنمای صوتی بسته شد."
    PLAYLIST_HELP_CLOSED_MSG = "راهنمای لیست پخش بسته شد."
    USERLOGS_CLOSED_MSG = "پیام لاگ‌ها بسته شد."
    HELP_CLOSED_MSG = "راهنما بسته شد."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>تنظیمات تار NSFW</b>\n\nمحتوای NSFW <b>{status}</b> است.\n\nانتخاب کنید که آیا محتوای NSFW تار شود:"
    NSFW_MENU_CLOSED_MSG = "منو بسته شد."
    NSFW_BLUR_DISABLED_MSG = "تار NSFW غیرفعال شد."
    NSFW_BLUR_ENABLED_MSG = "تار NSFW فعال شد."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "تار NSFW غیرفعال شد."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "تار NSFW فعال شد."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "فعال یا غیرفعال کردن ارسال MediaInfo برای فایل‌های دانلود شده?"
    MEDIAINFO_MENU_CLOSED_MSG = "منو بسته شد."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo فعال شد. پس از دانلود، اطلاعات فایل ارسال خواهد شد."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo غیرفعال شد."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo فعال شد."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo غیرفعال شد."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 فهرست فرمت‌های موجود</b>\n\n"
        "دریافت فرمت‌های ویدیو/صوتی موجود برای یک URL.\n\n"
        "<b>نحوه استفاده:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>مثال‌ها:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 نحوه استفاده از شناسه‌های فرمت:</b>\n"
        "پس از دریافت لیست، از شناسه فرمت خاص استفاده کنید:\n"
        "• <code>/format id 401</code> - دانلود فرمت 401\n"
        "• <code>/format id401</code> - همانند بالا\n"
        "• <code>/format id140 audio</code> - دانلود فرمت 140 به عنوان صوتی MP3\n\n"
        "این دستور تمام فرمت‌های موجودی که می‌توانند دانلود شوند را نمایش می‌دهد."
    )
    LIST_PROCESSING_MSG = "🔄 در حال دریافت فرمت‌های موجود..."
    LIST_INVALID_URL_MSG = "❌ لطفاً یک URL معتبر که با http:// یا https:// شروع می‌شود وارد کنید"
    LIST_CAPTION_MSG = (
        "📃 فرمت‌های موجود برای:\n<code>{url}</code>\n\n"
        "💡 <b>نحوه تنظیم فرمت:</b>\n"
        "• <code>/format id 134</code> - دانلود شناسه فرمت خاص\n"
        "• <code>/format 720p</code> - دانلود بر اساس کیفیت\n"
        "• <code>/format best</code> - دانلود بهترین کیفیت\n"
        "• <code>/format ask</code> - همیشه کیفیت را بپرس\n\n"
        "{audio_note}\n"
        "📋 از شناسه فرمت از لیست بالا استفاده کنید"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>فرمت‌های فقط صوتی:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - دانلود فرمت 140 به عنوان صوتی MP3\n"
        "• <code>/format id140 audio</code> - همانند بالا\n"
        "این‌ها به عنوان فایل‌های صوتی MP3 دانلود خواهند شد.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ خطا در ارسال فایل فرمت‌ها: {error}"
    LIST_ERROR_GETTING_MSG = "❌ دریافت فرمت‌ها ناموفق بود:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ در حین پردازش دستور خطایی رخ داد"
    LIST_ERROR_CALLBACK_MSG = "خطا رخ داد"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 نحوه استفاده از شناسه‌های فرمت:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "پس از دریافت لیست، از شناسه فرمت خاص استفاده کنید:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - دانلود فرمت 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - همانند بالا\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - دانلود فرمت 140 به عنوان صوتی MP3\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - همانند بالا\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 فرمت‌های فقط صوتی شناسایی شد: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "این فرمت‌ها به عنوان فایل‌های صوتی MP3 دانلود خواهند شد.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>فرمت‌های فقط ویدیویی:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 از شناسه فرمت از لیست بالا استفاده کنید"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>استفاده:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>مثال‌ها:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - بهترین کیفیت\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p یا پایین‌تر\n"
        "• /link 720p https://youtube.com/watch?v=... - همانند بالا\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K یا پایین‌تر\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K یا پایین‌تر"
        "</blockquote>\n\n"
        "<b>کیفیت:</b> از 1 تا 10000 (مثلاً 144، 240، 720، 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ لطفاً یک URL معتبر وارد کنید"
    LINK_PROCESSING_MSG = "🔗 در حال دریافت لینک مستقیم..."
    LINK_DURATION_MSG = "⏱ <b>مدت زمان:</b> {duration} ثانیه\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>جریان ویدیو:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>جریان صوتی:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **تنظیم صفحه کلید به‌روزرسانی شد!**\n\nتنظیم جدید: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **آرگومان نامعتبر!**\n\n"
        "گزینه‌های معتبر: `off`، `1x3`، `2x3`، `full`\n\n"
        "مثال: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **تنظیمات صفحه کلید**\n\n"
        "فعلی: **{current}**\n\n"
        "یک گزینه انتخاب کنید:\n\n"
        "یا استفاده کنید: `/keyboard off`، `/keyboard 1x3`، `/keyboard 2x3`، `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 صفحه کلید فعال شد!"
    KEYBOARD_HIDDEN_MSG = "⌨️ صفحه کلید مخفی شد"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 صفحه کلید 1x3 فعال شد!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 صفحه کلید 2x3 فعال شد!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 صفحه کلید ایموجی فعال شد!"
    KEYBOARD_ERROR_APPLYING_MSG = "خطا در اعمال تنظیم صفحه کلید {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ فرمت به این تنظیم شد: Always Ask. هر بار که URL ارسال می‌کنید از شما کیفیت پرسیده می‌شود."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ فرمت به این تنظیم شد: Always Ask. اکنون هر بار که URL ارسال می‌کنید از شما کیفیت پرسیده می‌شود."
    FORMAT_BEST_UPDATED_MSG = "✅ فرمت به بهترین کیفیت (اولویت AVC+MP4) به‌روزرسانی شد:\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ فرمت به شناسه {id} به‌روزرسانی شد:\n{format}\n\n💡 <b>نکته:</b> اگر این یک فرمت فقط صوتی است، به عنوان فایل صوتی MP3 دانلود خواهد شد."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ فرمت به شناسه {id} (فقط صوتی) به‌روزرسانی شد:\n{format}\n\n💡 این به عنوان فایل صوتی MP3 دانلود خواهد شد."
    FORMAT_QUALITY_UPDATED_MSG = "✅ فرمت به کیفیت {quality} به‌روزرسانی شد:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ فرمت به این به‌روزرسانی شد:\n{format}"
    FORMAT_MENU_MSG = (
        "یک گزینه فرمت انتخاب کنید یا یک مورد سفارشی با استفاده از ارسال کنید:\n"
        "• <code>/format &lt;format_string&gt;</code> - فرمت سفارشی\n"
        "• <code>/format 720</code> - کیفیت 720p\n"
        "• <code>/format 4k</code> - کیفیت 4K\n"
        "• <code>/format 8k</code> - کیفیت 8K\n"
        "• <code>/format id 401</code> - شناسه فرمت خاص\n"
        "• <code>/format ask</code> - همیشه منو را نمایش بده\n"
        "• <code>/format best</code> - bv+ba/بهترین کیفیت"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "برای استفاده از فرمت سفارشی، دستور را به این صورت ارسال کنید:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "<code>bestvideo+bestaudio/best</code> را با رشته فرمت مورد نظر خود جایگزین کنید."
    )
    FORMAT_RESOLUTION_MENU_MSG = "رزولوشن و کدک مورد نظر خود را انتخاب کنید:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ فرمت به این تنظیم شد: Always Ask. اکنون هر بار که URL ارسال می‌کنید از شما کیفیت پرسیده می‌شود."
    FORMAT_UPDATED_MSG = "✅ فرمت به این به‌روزرسانی شد:\n{format}"
    FORMAT_SAVED_MSG = "✅ فرمت ذخیره شد."
    FORMAT_CHOICE_UPDATED_MSG = "✅ انتخاب فرمت به‌روزرسانی شد."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "منوی فرمت سفارشی بسته شد"
    FORMAT_CODEC_SET_MSG = "✅ کدک به {codec} تنظیم شد"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ انتخاب مرورگر به‌روزرسانی شد."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ دسترسی رد شد. فقط مدیر."
    ACCESS_DENIED_ADMIN = "❌ دسترسی رد شد. فقط مدیر."
    WELCOME_MASTER = "خوش آمدید ارباب 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ متأسفم... خطایی در حین دانلود رخ داد."
    SIZE_LIMIT_EXCEEDED = "❌ اندازه فایل از محدودیت {max_size_gb} GB تجاوز می‌کند. لطفاً فایلی کوچکتر در اندازه مجاز انتخاب کنید."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ اسکریپت یافت نشد: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ در حال دانلود دامپ Firebase تازه با استفاده از {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ کش Firebase با موفقیت بارگذاری مجدد شد!"
    ADMIN_CACHE_FAILED_MSG = "❌ بارگذاری مجدد کش Firebase ناموفق بود. بررسی کنید که {cache_file} وجود دارد."
    ADMIN_ERROR_RELOADING_MSG = "❌ خطا در بارگذاری مجدد کش: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ خطا در اجرای {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ پیام تبلیغاتی به همه کاربران دیگر ارسال شد</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ نمی‌توان پیام تبلیغاتی را ارسال کرد. سعی کنید به یک پیام پاسخ دهید\nیا خطایی رخ داد</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ کاربر هنوز محتوایی دانلود نکرده است...</b> در لاگ‌ها وجود ندارد"
    ADMIN_INVALID_COMMAND_MSG = "❌ دستور نامعتبر"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ داده‌ای در کش برای <code>{{path}}</code> یافت نشد"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ صف خالی است — هنوز کسی کانال را ترک نکرده است."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>صف بن</b>\nکل در انتظار: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (ترک کرد: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… و {extra} کاربر دیگر."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "استفاده کنید /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ کاربران از صف مسدود شدند: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ مسدودسازی خودکار فعال شد: ترک‌کنندگان جدید فوراً بن می‌شوند."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ مسدودسازی خودکار غیرفعال شد."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ پنجره مسدودسازی خودکار برنامه‌ریزی شده به هر {interval} تنظیم شد."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 لاگ فعالیت کانال برای آخرین {hours} ساعت (2 روز)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 آخرین {hours} ساعت (2 روز): {joined} پیوست، {left} ترک کرد."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ هیچ فعالیتی برای آخرین {hours} ساعت (2 روز) وجود ندارد."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "کل: 🟢 {joined} پیوست، 🔴 {left} ترک کرد."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ دسترسی به لاگ فعالیت کانال وجود ندارد. ربات‌ها نمی‌توانند لاگ‌های مدیر را بخوانند. CHANNEL_GUARD_SESSION_STRING را در config با یک نشست کاربری برای فعال‌سازی این ویژگی ارائه دهید."
    BAN_TIME_USAGE_MSG = "❌ استفاده: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ از فرمت‌هایی مانند 10s، 6m، 5h، 4d، 3w، 2M یا 1y استفاده کنید."
    BAN_TIME_SET_MSG = "🕒 فاصله اسکن لاگ کانال به {interval} تنظیم شد."
    BAN_TIME_REPORT_MSG = (
        "🛡️ گزارش اسکن کانال\n"
        "اجرا در: {run_ts}\n"
        "فاصله: {interval}\n"
        "ترک‌کنندگان جدید: {new_leavers}\n"
        "بن‌های خودکار: {auto_banned}\n"
        "در انتظار: {pending}\n"
        "آخرین event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ استفاده: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 مدیر نمی‌تواند یک مدیر را حذف کند"
    ADMIN_USER_BLOCKED_MSG = "کاربر مسدود شد 🔒❌\n \nID: <code>{user_id}</code>\nتاریخ مسدودسازی: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> قبلاً مسدود شده است ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 متأسفم! شما مدیر نیستید"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ استفاده: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "کاربر از مسدودیت خارج شد 🔓✅\n \nID: <code>{user_id}</code>\nتاریخ خارج شدن از مسدودیت: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> قبلاً از مسدودیت خارج شده است ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ کاربران از مسدودیت خارج شدند: {count}\n⏱ مهر زمانی: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ استفاده: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "کاربر نادیده گرفته شد 👁️❌\n \nشناسه: <code>{user_id}</code>\nتاریخ نادیده گرفته شده: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> قبلاً نادیده گرفته شده است ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ استفاده: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "کاربر دیگر نادیده گرفته نمی‌شود 👁️✅\n \nشناسه: <code>{user_id}</code>\nتاریخ عدم نادیده گرفتن: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> نادیده گرفته نمی‌شود ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>زمان اجرای ربات -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ لطفاً یک URL برای پاک کردن کش ارائه دهید.\nاستفاده: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ لطفاً یک URL معتبر ارائه دهید.\nاستفاده: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ کش با موفقیت برای URL پاک شد:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ هیچ کشی برای این لینک یافت نشد."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ خطا در پاک کردن کش: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ دسترسی رد شد. فقط مدیر."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ در حال اجرای اسکریپت به‌روزرسانی لیست پورن: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ اسکریپت با موفقیت تکمیل شد!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ اسکریپت با موفقیت تکمیل شد!\n\nخروجی:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ اسکریپت با کد بازگشت {returncode} ناموفق بود:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ خطا در اجرای اسکریپت: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ در حال بارگذاری مجدد کش‌های پورن و دامنه‌های مرتبط..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ کش‌های پورن با موفقیت بارگذاری مجدد شدند!\n\n"
        "📊 وضعیت فعلی کش:\n"
        "• دامنه‌های پورن: {porn_domains}\n"
        "• کلمات کلیدی پورن: {porn_keywords}\n"
        "• سایت‌های پشتیبانی شده: {supported_sites}\n"
        "• WHITELIST: {whitelist}\n"
        "• GREYLIST: {greylist}\n"
        "• BLACK_LIST: {black_list}\n"
        "• WHITE_KEYWORDS: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ خطا در بارگذاری مجدد کش پورن: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ لطفاً یک URL برای بررسی ارائه دهید.\nاستفاده: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ لطفاً یک URL معتبر ارائه دهید.\nاستفاده: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 در حال بررسی URL برای محتوای NSFW...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>نتیجه بررسی پورن</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>وضعیت:</b> <b>{status_text}</b>\n\n"
        "<b>توضیح:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ خطا در بررسی URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "کوکی‌ها پاک شدند."
    CLEAN_LOGS_CLEANED_MSG = "لاگ‌ها پاک شدند."
    CLEAN_TAGS_CLEANED_MSG = "تگ‌ها پاک شدند."
    CLEAN_FORMAT_CLEANED_MSG = "فرمت پاک شد."
    CLEAN_SPLIT_CLEANED_MSG = "تقسیم پاک شد."
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfo پاک شد."
    CLEAN_SUBS_CLEANED_MSG = "تنظیمات زیرنویس پاک شدند."
    CLEAN_KEYBOARD_CLEANED_MSG = "تنظیمات صفحه کلید پاک شدند."
    CLEAN_ARGS_CLEANED_MSG = "تنظیمات Args پاک شدند."
    CLEAN_NSFW_CLEANED_MSG = "تنظیمات NSFW پاک شدند."
    CLEAN_PROXY_CLEANED_MSG = "تنظیمات پروکسی پاک شدند."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "تنظیمات Flood wait پاک شدند."
    CLEAN_ALL_CLEANED_MSG = "همه فایل‌ها پاک شدند."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 کوکی‌ها</b>\n\nیک عمل انتخاب کنید:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ فایل کوکی ذخیره شد"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ اعتبارسنجی برای کوکی‌های غیر-YouTube رد شد"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ فایل کوکی وجود دارد اما فرمت نادرست است"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ فایل کوکی یافت نشد."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 در حال شروع تست کوکی‌های YouTube...\n\nلطفاً صبر کنید در حالی که کوکی‌های شما را بررسی و اعتبارسنجی می‌کنم."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ کوکی‌های YouTube موجود شما به درستی کار می‌کنند!\n\nنیازی به دانلود جدید نیست."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ کوکی‌های YouTube موجود شما منقضی شده یا نامعتبر هستند.\n\n🔄 در حال دانلود کوکی‌های جدید..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ منبع کوکی {service} پیکربندی نشده است!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ منبع کوکی {service} باید یک فایل .txt باشد!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ محدودیت محدوده تجاوز شد: {range_count} فایل درخواست شده (حداکثر {max_img_files}).\n\nاز یکی از این دستورات برای دانلود حداکثر فایل‌های موجود استفاده کنید:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚بستن"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ محدودیت رسانه تجاوز شد: {count} فایل درخواست شده (حداکثر {max_count}).\n\nاز یکی از این دستورات برای دانلود حداکثر فایل‌های موجود استفاده کنید:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 <b>{count}</b> مورد رسانه از لینک یافت شد"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "محدوده دانلود را انتخاب کنید:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "تقلید مرورگر"
    ARGS_REFERER_DESC_MSG = "هدر Referer"
    ARGS_USER_AGENT_DESC_MSG = "هدر User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "دور زدن محدودیت‌های جغرافیایی"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "بررسی گواهی SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "دانلود استریم‌های زنده از ابتدا"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "استریم‌های زنده را از ابتدا دانلود نکن"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "استفاده از کانتینر MPEG-TS برای ویدیوهای HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "فقط یک ویدیو دانلود کن، نه لیست پخش"
    ARGS_NO_PART_DESC_MSG = "استفاده نکردن از فایل‌های .part"
    ARGS_NO_CONTINUE_DESC_MSG = "از سرگیری دانلودهای جزئی نکن"
    ARGS_AUDIO_FORMAT_DESC_MSG = "فرمت صدا برای استخراج"
    ARGS_EMBED_METADATA_DESC_MSG = "جاسازی متادیتا در فایل ویدیو"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "جاسازی بندانگشتی در فایل ویدیو"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "نوشتن بندانگشتی به فایل"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "تعداد قطعات همزمان برای دانلود"
    ARGS_FORCE_IPV4_DESC_MSG = "اجبار اتصالات IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "اجبار اتصالات IPv6"
    ARGS_XFF_DESC_MSG = "استراتژی هدر X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "اندازه قطعه HTTP (بایت)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "خواب قبل از دانلود زیرنویس (ثانیه)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "اجازه اتصال به سرورهای قدیمی"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "سرکوب اعتبارسنجی گواهی HTTPS"
    ARGS_USERNAME_DESC_MSG = "نام کاربری حساب"
    ARGS_PASSWORD_DESC_MSG = "رمز عبور حساب"
    ARGS_TWOFACTOR_DESC_MSG = "کد احراز هویت دو عاملی"
    ARGS_IGNORE_ERRORS_DESC_MSG = "نادیده گرفتن خطاهای دانلود و ادامه"
    ARGS_MIN_FILESIZE_DESC_MSG = "حداقل اندازه فایل (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "حداکثر اندازه فایل (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "موارد لیست پخش برای دانلود (مثلاً 1,3,5 یا 1-5)"
    ARGS_DATE_DESC_MSG = "دانلود ویدیوهای آپلود شده در این تاریخ (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "دانلود ویدیوهای آپلود شده قبل از این تاریخ (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "دانلود ویدیوهای آپلود شده بعد از این تاریخ (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "هدرهای HTTP سفارشی (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "فاصله خواب بین درخواست‌ها (ثانیه)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "حداکثر فاصله خواب (ثانیه)"
    ARGS_RETRIES_DESC_MSG = "تعداد تلاش‌های مجدد"
    ARGS_VIDEO_FORMAT_DESC_MSG = "فرمت کانتینر ویدیو"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "فرمت کانتینر خروجی برای ادغام"
    ARGS_SEND_AS_FILE_DESC_MSG = "ارسال همه رسانه به عنوان سند به جای رسانه"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "تقلید"
    ARGS_REFERER_SHORT_MSG = "ارجاع‌دهنده"
    ARGS_GEO_BYPASS_SHORT_MSG = "دور زدن جغرافیایی"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "بررسی گواهی"
    ARGS_LIVE_FROM_START_SHORT_MSG = "شروع زنده"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "بدون شروع زنده"
    ARGS_USER_AGENT_SHORT_MSG = "کاربر عامل"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "بدون پلی‌لیست"
    ARGS_NO_PART_SHORT_MSG = "بدون Part"
    ARGS_NO_CONTINUE_SHORT_MSG = "بدون Continue"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "فرمت صدا"
    ARGS_EMBED_METADATA_SHORT_MSG = "جاسازی متا"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "جاسازی بندانگشتی"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "نوشتن بندانگشتی"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "همزمان"
    ARGS_FORCE_IPV4_SHORT_MSG = "اجبار IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "اجبار IPv6"
    ARGS_XFF_SHORT_MSG = "هدر XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "اندازه قطعه"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "خواب زیرنویس"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "اتصال قدیمی"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "بدون بررسی گواهی"
    ARGS_USERNAME_SHORT_MSG = "نام کاربری"
    ARGS_PASSWORD_SHORT_MSG = "رمز عبور"
    ARGS_TWOFACTOR_SHORT_MSG = "احراز هویت دو مرحله‌ای"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "نادیده گرفتن خطاها"
    ARGS_MIN_FILESIZE_SHORT_MSG = "حداقل اندازه"
    ARGS_MAX_FILESIZE_SHORT_MSG = "حداکثر اندازه"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "آیتم‌های پلی‌لیست"
    ARGS_DATE_SHORT_MSG = "تاریخ"
    ARGS_DATEBEFORE_SHORT_MSG = "قبل از تاریخ"
    ARGS_DATEAFTER_SHORT_MSG = "بعد از تاریخ"
    ARGS_HTTP_HEADERS_SHORT_MSG = "هدرهای HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "فاصله خواب"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "حداکثر خواب"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "فرمت ویدیو"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "فرمت ادغام"
    ARGS_SEND_AS_FILE_SHORT_MSG = "ارسال به عنوان فایل"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ فایل خیلی بزرگ است. حداکثر اندازه 100 KB است."
    COOKIES_INVALID_FORMAT_MSG = "❌ فقط فایل‌های با فرمت .txt مجاز هستند."
    COOKIES_INVALID_COOKIE_MSG = "❌ فایل شبیه cookie.txt نیست (خط '# Netscape HTTP Cookie File' وجود ندارد)."
    COOKIES_ERROR_READING_MSG = "❌ خطا در خواندن فایل: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ فایل کوکی وجود دارد و فرمت صحیح دارد"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ فایل کوکی {service} خیلی بزرگ است! حداکثر 100KB، دریافت شده {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ فایل کوکی {service} دانلود و به عنوان cookie.txt در پوشه شما ذخیره شد.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ منبع کوکی {service} در دسترس نیست (وضعیت {status}). لطفاً بعداً دوباره تلاش کنید."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ خطا در دانلود فایل کوکی {service}. لطفاً بعداً دوباره تلاش کنید."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ کاربر یک فایل کوکی جدید ارائه داد.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ کوکی با موفقیت به‌روزرسانی شد:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ کوکی معتبر نیست.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ منابع کوکی YouTube پیکربندی نشده‌اند!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 در حال دانلود و بررسی کوکی‌های YouTube...\n\nتلاش {attempt} از {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ دسترسی رد شد. فقط مدیر."
    ADMIN_USER_LOGS_TOTAL_MSG = "کل: <b>{total}</b>\n<b>{user_id}</b> - لاگ‌ها (آخرین 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 صفحه کلید فعال شد!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ زبان زیرنویس به این تنظیم شد: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ زبان زیرنویس به این تنظیم شد: {flag} {name} با فعال بودن AUTO/TRANS."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "منوی زبان زیرنویس بسته شد."
    SUBS_DOWNLOADING_MSG = "💬 در حال دانلود زیرنویس‌ها..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 در حال بارگذاری مجدد کش Firebase در حافظه..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ COOKIE_URL پیکربندی نشده است. از /cookie استفاده کنید یا cookie.txt را آپلود کنید."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 در حال دانلود کوکی‌ها از URL از راه دور..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL باید به یک فایل .txt اشاره کند."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ فایل کوکی fallback خیلی بزرگ است (>100KB)"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ فایل کوکی YouTube از طریق fallback دانلود شد و به عنوان cookie.txt ذخیره شد"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ منبع کوکی fallback در دسترس نیست (وضعیت {status}). /cookie را امتحان کنید یا cookie.txt را آپلود کنید."
    COOKIE_FALLBACK_ERROR_MSG = "❌ خطا در دانلود کوکی fallback. /cookie را امتحان کنید یا cookie.txt را آپلود کنید."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ خطای غیرمنتظره در حین دانلود کوکی fallback."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ مرورگر {browser} نصب نشده است."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ کوکی‌ها با استفاده از مرورگر ذخیره شدند: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ ذخیره کوکی‌ها ناموفق بود: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ کوکی‌های YouTube به درستی کار می‌کنند"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ کوکی‌های YouTube منقضی شده یا نامعتبر هستند\n\nاز /cookie برای دریافت کوکی‌های جدید استفاده کنید"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - فرمت سفارشی\n• <code>/format 720</code> - کیفیت 720p\n• <code>/format 4k</code> - کیفیت 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "راهنما ارسال شد."
    FORMAT_MKV_TOGGLE_MSG = "MKV اکنون {status} است"
    COOKIES_NO_REMOTE_URL_MSG = "❌ هیچ URL از راه دور پیکربندی نشده است"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ فرمت فایل نامعتبر است"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ فایل خیلی بزرگ است"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ کوکی‌ها با موفقیت دانلود شدند"
    COOKIES_SERVER_ERROR_MSG = "❌ خطای سرور {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ دانلود ناموفق بود"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ خطای غیرمنتظره"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ مرورگر نصب نشده است."
    COOKIES_MENU_CLOSED_MSG = "منو بسته شد."
    COOKIES_HINT_CLOSED_MSG = "راهنمای کوکی بسته شد."
    IMG_HELP_CLOSED_MSG = "راهنما بسته شد."
    SUBS_LANGUAGE_UPDATED_MSG = "تنظیمات زبان زیرنویس به‌روزرسانی شد."
    SUBS_MENU_CLOSED_MSG = "منوی زبان زیرنویس بسته شد."
    KEYBOARD_SET_TO_MSG = "صفحه کلید به {setting} تنظیم شد"
    KEYBOARD_ERROR_PROCESSING_MSG = "خطا در پردازش تنظیم"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo فعال شد."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo غیرفعال شد."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "تار NSFW غیرفعال شد."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "تار NSFW فعال شد."
    SETTINGS_MENU_CLOSED_MSG = "منو بسته شد."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Flood wait فعال است. بعداً تلاش کنید."
    OTHER_HELP_CLOSED_MSG = "راهنما بسته شد."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "پیام لاگ‌ها بسته شد."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "منو بسته شد."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "اندازه نامعتبر."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ خطا در ارسال MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ خطایی رخ داد: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - همه لاگ‌ها"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - همه {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 دانلود از URL از راه دور"
    BROWSER_OPEN_BUTTON_MSG = "🌐 باز کردن مرورگر"
    SELECT_BROWSER_MSG = "مرورگری را برای دانلود کوکی‌ها انتخاب کنید:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "هیچ مرورگری در این سیستم یافت نشد. می‌توانید کوکی‌ها را از URL از راه دور دانلود کنید یا وضعیت مرورگر را نظارت کنید:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>باز کردن مرورگر</b> - برای نظارت بر وضعیت مرورگر در مینی‌اپ"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ اجرای /check_cookie ناموفق بود"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ محدودیت سیل. بعداً تلاش کنید."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ باز کردن منوی کوکی مرورگر ناموفق بود"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "راهنمای ذخیره به عنوان کوکی بسته شد."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>استفاده:</b>\n<code>/link [quality] URL</code>\n\n<b>مثال‌ها:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - بهترین کیفیت\n• /link 720 https://youtube.com/watch?v=... - 720p یا پایین‌تر\n• /link 720p https://youtube.com/watch?v=... - همانند بالا\n• /link 4k https://youtube.com/watch?v=... - 4K یا پایین‌تر\n• /link 8k https://youtube.com/watch?v=... - 8K یا پایین‌تر</blockquote>\n\n<b>کیفیت:</b> از 1 تا 10000 (مثلاً 144، 240، 720، 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - کیفیت 8K"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>لینک مستقیم به دست آمد</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>فرمت:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>جریان صوتی:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ دریافت لینک‌های استریم ناموفق بود"
    LINK_ERROR_GETTING_MSG = "❌ <b>خطا در دریافت لینک:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ شاخص کوکی YouTube نامعتبر: {selected_index}. محدوده موجود 1-{total_urls} است"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 در حال دانلود و بررسی کوکی‌های YouTube...\n\nتلاش {attempt} از {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 در حال دانلود و بررسی کوکی‌های YouTube...\n\nتلاش {attempt} از {total}\n🔍 در حال تست کوکی‌ها..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ کوکی‌های YouTube با موفقیت دانلود و اعتبارسنجی شدند!\n\nمنبع استفاده شده {source} از {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ همه کوکی‌های YouTube منقضی شده یا در دسترس نیستند!\n\nبرای جایگزینی با مدیر ربات تماس بگیرید."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ محدودیت تلاش مجدد کوکی YouTube تجاوز شد!\n\n🔢 حداکثر: {limit} تلاش در ساعت\n⏰ لطفاً بعداً دوباره تلاش کنید"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ تگ #{wrong} شامل کاراکترهای ممنوع است. فقط حروف، اعداد و _ مجاز است.\nلطفاً استفاده کنید: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **آرگومان نامعتبر!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ زبان زیرنویس تنظیم شد: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "مثال: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} زبان انتخاب شده: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ حالت Always Ask {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 زیرنویس‌ها غیرفعال هستند"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 تنظیمات زیرنویس</b>\n\n{status_text}\n\nزبان زیرنویس را انتخاب کنید:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - غیرفعال کردن زیرنویس‌ها\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 تنظیمات زیرنویس</b>\n\n{status_text}\n\nزبان زیرنویس را انتخاب کنید:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>عنوان:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>مدت زمان:</b> {duration} ثانیه\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>جریان ویدیو:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- کیفیت حداکثر 720p\n- مدت زمان حداکثر 1.5 ساعت\n- اندازه ویدیو حداکثر 500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️هشدار: به دلیل تأثیر زیاد CPU این عملکرد بسیار کند است (نزدیک به زمان واقعی) و محدود به:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>دستورات سریع:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - غیرفعال کردن زیرنویس‌ها\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - فعال کردن حالت Always Ask\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - set language\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - تنظیم زبان با فعال بودن AUTO/TRANS\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - فعال کردن حالت Always Ask\n"
    SUBS_AUTO_SUBS_TEXT = " (زیرنویس خودکار)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ حالت زیرنویس خودکار {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS از طریق دستور غیرفعال شد: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Always Ask از طریق دستور فعال شد: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "زبان SUBS از طریق دستور تنظیم شد: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "زبان SUBS + حالت auto از طریق دستور تنظیم شد: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "کاربر منوی /subs را باز کرد."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "کاربر زبان زیرنویس را به این تنظیم کرد: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "کاربر حالت AUTO/TRANS را به این تغییر داد: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "کاربر حالت Always Ask را به این تغییر داد: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "کاربر کوکی‌ها را از مرورگر درخواست کرد."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "صفحه کلید انتخاب مرورگر فقط با مرورگرهای نصب شده ارسال شد."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "انتخاب مرورگر بسته شد."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "COOKIE_URL fallback با موفقیت استفاده شد (منبع مخفی)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "COOKIE_URL fallback ناموفق بود: وضعیت={status} (مخفی)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "خطای غیرمنتظره COOKIE_URL fallback: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "مرورگر {browser} نصب نشده است."
    COOKIES_SAVED_BROWSER_LOG_MSG = "کوکی‌ها با استفاده از مرورگر ذخیره شدند: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "فایل کوکی برای کاربر {user_id} ذخیره شد."
    COOKIES_FILE_WORKING_LOG_MSG = "فایل کوکی وجود دارد، فرمت صحیح دارد و کوکی‌های YouTube کار می‌کنند."
    COOKIES_FILE_EXPIRED_LOG_MSG = "فایل کوکی وجود دارد و فرمت صحیح دارد، اما کوکی‌های YouTube منقضی شده‌اند."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "فایل کوکی وجود دارد و فرمت صحیح دارد."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "فایل کوکی وجود دارد اما فرمت نادرست دارد."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "فایل کوکی یافت نشد."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "URL کوکی {service} برای کاربر {user_id} خالی است."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "URL کوکی {service} .txt نیست (مخفی)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "فایل کوکی {service} خیلی بزرگ است: {size} بایت (منبع مخفی)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "فایل کوکی {service} برای کاربر {user_id} دانلود شد (منبع مخفی)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "اسکریپت یافت نشد: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "ارسال پیام وضعیت اولیه ناموفق بود"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "خطا در اجرای {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "کش Firebase توسط کار خودکار بارگذاری مجدد شد."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "کش Firebase توسط مدیر بارگذاری مجدد شد."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "خطا در بارگذاری مجدد کش Firebase: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "پخش آغاز شد. متن:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "پیام پخش به همه کاربران ارسال شد."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "پخش پیام ناموفق بود: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "مدیر {user_id} کش را برای URL پاک کرد: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "مدیر {user_id} اسکریپت به‌روزرسانی لیست پورن را شروع کرد: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "اسکریپت به‌روزرسانی لیست پورن با موفقیت توسط مدیر {user_id} تکمیل شد"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "اسکریپت به‌روزرسانی لیست پورن توسط مدیر {user_id} ناموفق بود: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "مدیر {user_id} سعی کرد اسکریپت غیرموجود را اجرا کند: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "خطا در اجرای اسکریپت به‌روزرسانی پورن توسط مدیر {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "مدیر {user_id} بارگذاری مجدد کش پورن را شروع کرد"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "خطا در بارگذاری مجدد کش پورن توسط مدیر {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "مدیر {user_id} URL را برای NSFW بررسی کرد: {url} - نتیجه: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "کاربر تغییر فرمت را درخواست کرد."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "فرمت به ALWAYS_ASK تنظیم شد."
    FORMAT_UPDATED_BEST_LOG_MSG = "فرمت به بهترین به‌روزرسانی شد: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "فرمت به شناسه {format_id} به‌روزرسانی شد: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "فرمت به شناسه {format_id} (فقط صوتی) به‌روزرسانی شد: {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "فرمت به کیفیت {quality} به‌روزرسانی شد: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "فرمت به این به‌روزرسانی شد: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "منوی فرمت ارسال شد."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "انتخاب فرمت بسته شد."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "راهنمای فرمت سفارشی ارسال شد."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "منوی رزولوشن فرمت ارسال شد."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "بازگشت به منوی اصلی فرمت."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "فرمت به این به‌روزرسانی شد: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "فرمت به ALWAYS_ASK تنظیم شد."
    FORMAT_CODEC_SET_LOG_MSG = "ترجیح کدک به {codec} تنظیم شد"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "منوی فرمت سفارشی بسته شد"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "لینک مستقیم برای کاربر {user_id} از {url} استخراج شد"
    LINK_EXTRACTION_FAILED_LOG_MSG = "استخراج لینک مستقیم برای کاربر {user_id} از {url} ناموفق بود: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "خطا در دستور link برای کاربر {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "کاربر {user_id} صفحه کلید را به {setting} تنظیم کرد"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "کاربر {user_id} صفحه کلید را به {setting} تنظیم کرد"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo از طریق دستور تنظیم شد: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "کاربر منوی /mediainfo را باز کرد."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: بسته شد."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo فعال شد."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo غیرفعال شد."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "اندازه تقسیم از طریق آرگومان به {size} بایت تنظیم شد."
    SPLIT_MENU_OPENED_LOG_MSG = "کاربر منوی /split را باز کرد."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "انتخاب تقسیم بسته شد."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "اندازه تقسیم به {size} بایت تنظیم شد."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "پروکسی از طریق دستور تنظیم شد: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "کاربر منوی /proxy را باز کرد."
    PROXY_MENU_CLOSED_LOG_MSG = "پروکسی: بسته شد."
    PROXY_ENABLED_LOG_MSG = "پروکسی فعال شد."
    PROXY_DISABLED_LOG_MSG = "پروکسی غیرفعال شد."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "پیام راهنما بسته شد."
    AUDIO_HELP_SHOWN_LOG_MSG = "راهنمای /audio نمایش داده شد"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "کاربر راهنمای لیست پخش را درخواست کرد."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "راهنمای لیست پخش بسته شد."
    AUDIO_HINT_CLOSED_LOG_MSG = "راهنمای صوتی بسته شد."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "منوی لینک مستقیم از طریق دکمه LINK برای کاربر {user_id} از {url} ایجاد شد"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "استخراج لینک مستقیم از طریق دکمه LINK برای کاربر {user_id} از {url} ناموفق بود: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "دستور LIST برای کاربر {user_id}، url: {url} اجرا شد"
    QUICK_EMBED_LOG_MSG = "جاسازی سریع: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "منوی Always Ask برای {url} ارسال شد"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "منوی کیفیت‌های کش شده برای کاربر {user_id} پس از خطا ایجاد شد: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "خطای منوی Always Ask برای {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "فرمت از طریق تنظیمات /args ثابت شده است"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "صدا"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "ویدیو"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "ویدیو"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "بعدی ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ قبلی"
    SUBTITLES_NEXT_BUTTON_MSG = "بعدی ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ همه فیلدهای متنی خالی هستند"
    SENDER_VIDEO_DURATION_MSG = "مدت زمان ویدیو:"
    SENDER_UPLOADING_FILE_MSG = "📤 در حال آپلود فایل..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 در حال آپلود ویدیو..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 مدت زمان ویدیو:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 فایل آپلود شد."
    DOWN_UP_VIDEO_INFO_MSG = "📋 اطلاعات ویدیو"
    DOWN_UP_NUMBER_MSG = "شماره"
    DOWN_UP_TITLE_MSG = "عنوان"
    DOWN_UP_ID_MSG = "شناسه"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ ویدیو دانلود شد."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 در حال پردازش برای آپلود..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 فایل بخش تقسیم شده {part} آپلود شد"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ آپلود تکمیل شد"
    DOWN_UP_FILES_UPLOADED_MSG = "فایل‌ها آپلود شدند"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Close"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBS"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 SUBS"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Browser"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 در حال دریافت لینک مستقیم..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 در حال دریافت فرمت‌های موجود..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 در حال دریافت توضیحات ویدیو..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ خطا در دریافت توضیحات: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ توضیحات ویدیو در دسترس نیست"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ خطا در ارسال توضیحات: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 توضیحات ویدیو برای کاربر {user_id} برای {url} ({title}) ارسال شد"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 در حال شروع gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>مدت زمان:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>فرمت:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>مرورگر:</b> باز کردن در مرورگر وب"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "فرمت‌های موجود برای"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 نحوه استفاده از شناسه‌های فرمت:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "پس از دریافت لیست، از شناسه فرمت خاص استفاده کنید:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - دانلود فرمت 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - همانند بالا"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - دانلود فرمت 140 به عنوان صوتی MP3"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 فرمت‌های فقط صوتی شناسایی شدند"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "این فرمت‌ها به عنوان فایل‌های صوتی MP3 دانلود خواهند شد."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>نحوه تنظیم فرمت:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - دانلود شناسه فرمت خاص"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - دانلود بر اساس کیفیت"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - دانلود بهترین کیفیت"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - همیشه کیفیت را بپرس"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>فرمت‌های فقط صوتی:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - دانلود فرمت 140 به عنوان صوتی MP3"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "این‌ها به عنوان فایل‌های صوتی MP3 دانلود خواهند شد."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 از شناسه فرمت از لیست بالا استفاده کنید"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ خطا: پیام اصلی یافت نشد."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "صفحه فرمت‌ها"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ خطا در نمایش منوی فرمت‌ها"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ خطا در دریافت فرمت‌ها"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ خطا در دریافت فرمت‌های موجود."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "لطفاً بعداً دوباره تلاش کنید."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp نمی‌تواند این محتوا را پردازش کند"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "سیستم استفاده از gallery-dl را توصیه می‌کند."
    ALWAYS_ASK_OPTIONS_MSG = "**گزینه‌ها:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• برای گالری تصاویر: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• برای تصاویر تکی: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl اغلب برای Instagram، Twitter و سایر محتوای رسانه‌های اجتماعی بهتر کار می‌کند."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 امتحان Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 فرمت از طریق /args ثابت شده است"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 زیرنویس‌ها"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 صدا دوبله شده"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — زیرنویس‌ها در دسترس هستند"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — زبان زیرنویس را انتخاب کنید"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ زیرنویس‌ها یافت نشدند و جاسازی نمی‌شوند"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — بازنشر فوری از کش"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — زبان صوتی را انتخاب کنید"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW پولی است (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — کیفیت دانلود را انتخاب کنید"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — دانلود تصویر (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — دریافت لینک مستقیم به ویدیو"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — نمایش لیست فرمت‌های موجود"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — تغییر پسوند/کدک ویدیو"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀جاسازی"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — استخراج فقط صدا"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW پولی است (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — بازنشر فوری از کش"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — تماشای ویدیو در poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — زبان صوتی را انتخاب کنید"
    ALWAYS_ASK_BEST_BUTTON_MSG = "بهترین"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛سایر"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝فقط زیرنویس"
    ALWAYS_ASK_SMART_GROUPING_MSG = "گروه‌بندی هوشمند"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "ردیف دکمه عمل اضافه شد (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "ردیف‌های دکمه عمل اضافه شدند (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "دکمه‌های پایین به ردیف موجود اضافه شدند"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "ردیف پایین جدید ایجاد شد"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "هیچ ویدیویی در لیست پخش یافت نشد"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "URL پشتیبانی نشده"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "هیچ ویدیویی یافت نشد"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "هیچ ویدیویی یافت نشد"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "هیچ رسانه‌ای یافت نشد"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "این توییت شامل"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>خطا در دریافت اطلاعات ویدیو:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "خطا در دریافت اطلاعات ویدیو"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "دستور <code>/clean</code> را امتحان کنید و دوباره تلاش کنید. اگر خطا ادامه داشت، YouTube نیاز به مجوز دارد. cookies.txt را از طریق <code>/cookie</code> یا <code>/cookies_from_browser</code> به‌روزرسانی کنید و دوباره تلاش کنید."
    ALWAYS_ASK_MENU_CLOSED_MSG = "منو بسته شد."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 انتخاب دستی کیفیت"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "کیفیت را به صورت دستی انتخاب کنید زیرا شناسایی خودکار ناموفق بود:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 همه فرمت‌های موجود"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 کیفیت‌های موجود (از کش)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ استفاده از کیفیت‌های کش شده - فرمت‌های جدید ممکن است در دسترس نباشند"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 در حال دانلود فرمت"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 در حال دانلود"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 در حال دانلود با ردیابی پیشرفت..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 در حال دانلود با استفاده از فرمت:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 در حال دانلود صدا با استفاده از فرمت:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 در حال دانلود بهترین کیفیت..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 در حال دانلود دامپ پایگاه داده..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 در حال دانلود"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "صفحه فرمت‌ها"
    ALWAYS_ASK_FROM_CACHE_MSG = "(از کش)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ خطا: پیام اصلی یافت نشد. ممکن است حذف شده باشد. لطفاً لینک را دوباره ارسال کنید."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ خطا: URL اصلی یافت نشد. لطفاً لینک را دوباره ارسال کنید."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>لینک مستقیم به دست آمد</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>عنوان:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>مدت زمان:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>فرمت:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>جریان ویدیو:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>جریان صوتی:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ دریافت لینک‌های استریم ناموفق بود"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "لینک مستقیم از طریق منوی Always Ask برای کاربر {user_id} از {url} استخراج شد"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "استخراج لینک مستقیم از طریق منوی Always Ask برای کاربر {user_id} از {url} ناموفق بود: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "لینک مستقیم از طریق down_and_up_with_format برای کاربر {user_id} از {url} استخراج شد"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "استخراج لینک مستقیم از طریق down_and_up_with_format برای کاربر {user_id} از {url} ناموفق بود: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "لینک مستقیم از طریق down_and_audio برای کاربر {user_id} از {url} استخراج شد"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "استخراج لینک مستقیم از طریق down_and_audio برای کاربر {user_id} از {url} ناموفق بود: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ صدا از کش ارسال شد."
    AUDIO_PROCESSING_MSG = "🎙️ صدا در حال پردازش است..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 در حال دانلود صدا:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "خطا در حین دانلود صدا رخ داد."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ استخراج اطلاعات صدا ناموفق بود"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "رد کردن نوع فایل پشتیبانی نشده در لیست پخش در شاخص {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "فایل صوتی پس از دانلود یافت نشد."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ ارسال صدا ناموفق بود: اندازه فایل برابر 0 بایت است (شاخص لیست پخش {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ فایل صدا هنوز در حال دانلود است، لطفا صبر کنید..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 در حال آپلود فایل صوتی...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ ارسال صدا ناموفق بود: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "صداهای لیست پخش ارسال شد: {sent}/{total} فایل (کیفیت={quality}) به کاربر {user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ دانلود صدا ناموفق بود: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ دانلود به دلیل زمان‌بندی لغو شد (2 ساعت)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ فایل ویدیو یافت نشد: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ ارسال ویدیو ناموفق بود: اندازه فایل برابر 0 بایت است (شاخص لیست پخش {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ فایل ویدیو هنوز در حال دانلود است، لطفا صبر کنید..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ خطا در پردازش ویدیو: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ خطا در ارسال فایل توضیحات: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 اگر می‌خواهید عنوان ویدیو را تغییر دهید - به ویدیو با متن جدید پاسخ دهید</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "هیچ زیرنویسی شناسایی نشد"
    VIDEO_PROGRESS_MSG = "<b>ویدیو:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>صدا:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ محدودیت URL تجاوز شد: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "پردازش تکمیل شد"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ محدوده‌های لیست پخش در حالت چند URL مجاز نیست. فقط URLهای تکی بدون محدوده ارسال کنید (*1*5، /vid 1-10 و غیره)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "بررسی کنید <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>اینجا</a> اگر سایت شما پشتیبانی می‌شود"
    ERROR_COOKIE_NEEDED_MSG = "ممکن است برای دانلود این ویدیو به <code>cookie</code> نیاز داشته باشید. ابتدا فضای کاری خود را از طریق دستور <b>/clean</b> پاک کنید"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "برای YouTube - <code>cookie</code> را از طریق دستور <b>/cookie</b> دریافت کنید. برای هر سایت پشتیبانی شده دیگر - کوکی خود را ارسال کنید (<a href='https://t.me/tg_ytdlp/203'>راهنما1</a>) (<a href='https://t.me/tg_ytdlp/214'>راهنما2</a>) و پس از آن لینک ویدیوی خود را دوباره ارسال کنید."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "زبان زیرنویس را انتخاب کنید"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "هیچ زبان صوتی جایگزینی وجود ندارد"
    CHOOSE_AUDIO_LANGUAGE_MSG = "زبان صوتی را انتخاب کنید"
    PAGE_NUMBER_MSG = "صفحه {page}"
    TOTAL_PROGRESS_MSG = "پیشرفت کل"
    SUBTITLE_MENU_CLOSED_MSG = "منوی زیرنویس بسته شد."
    SUBTITLE_LANGUAGE_SET_MSG = "زبان زیرنویس تنظیم شد: {value}"
    AUDIO_SET_MSG = "صدا تنظیم شد: {value}"
    FILTERS_UPDATED_MSG = "فیلترها به‌روزرسانی شدند"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙بازگشت"
    CLOSE_BUTTON_TEXT = "🔚بستن"
    LIST_BUTTON_TEXT = "📃لیست"
    IMAGE_BUTTON_TEXT = "🖼تصویر"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ کیفیت‌ها به طور خودکار شناسایی نشدند\nاز دکمه 'Other' برای دیدن همه فرمت‌های موجود استفاده کنید.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **استریم زنده شناسایی شد**\n\nدانلود استریم‌های زنده در حال اجرا یا نامحدود مجاز نیست.\n\nلطفاً تا پایان استریم صبر کنید و دوباره دانلود را امتحان کنید وقتی:\n• مدت زمان استریم مشخص است\n• استریم به پایان رسیده است\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>دانلود استریم زنده</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "قطعه {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "حداکثر اندازه: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "مدت زمان کل: {duration} ثانیه"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>استریم زنده - قطعه {chunk}</b>\n⏱ مدت زمان: {duration} ثانیه\n📦 اندازه: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "قطعه {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>دانلود استریم زنده تکمیل شد</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "{chunks} قطعه دانلود شد"
    LIVE_STREAM_TOTAL_DURATION_MSG = "مدت زمان کل: {duration} ثانیه"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>دانلود استریم زنده متوقف شد</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "پوشه کاربر حذف شد (احتمالاً با دستور /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "فایل قطعه حذف شد (احتمالاً با دستور /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ استریم به پایان رسیده است"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "لطفاً فرمت دیگری را با استفاده از دستور `/format` انتخاب کنید."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>لینک مستقیم به دست آمد</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>عنوان:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>مدت زمان:</b> {duration} ثانیه\n"
    FORMAT_FIELD_MSG = "🎛 <b>فرمت:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>جریان ویدیو:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>جریان صوتی:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **خطا در پردازش فایل**\n\nویدیو دانلود شد اما به دلیل کاراکترهای نامعتبر در نام فایل نمی‌تواند پردازش شود.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **خطا در پردازش فایل**\n\nویدیو دانلود شد اما به دلیل خطای آرگومان نامعتبر نمی‌تواند پردازش شود.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**دلیل:**\n"
        "• فایل دانلود شده یک فایل ویدیو نیست\n"
        "• ممکن است یک سند (PDF، DOC و غیره) یا بایگانی باشد\n\n"
        "**راه حل:**\n"
        "• لینک را بررسی کنید - ممکن است به یک سند منجر شود، نه ویدیو\n"
        "• لینک یا منبع دیگری را امتحان کنید\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**دلیل:**\n"
        "• فایل نمی‌تواند به عنوان ویدیو پردازش شود\n"
        "• ممکن است فایل ویدیو نباشد یا فایل خراب باشد\n\n"
        "**راه حل:**\n"
        "• لینک را بررسی کنید - ممکن است به یک سند منجر شود، نه ویدیو\n"
        "• لینک یا منبع دیگری را امتحان کنید\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **فرمت در دسترس نیست**\n\nفرمت ویدیوی درخواستی برای این ویدیو در دسترس نیست.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ شناسه فرمت {format_id} برای این ویدیو یافت نشد.\n\nشناسه‌های فرمت موجود: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **فرمت AV1 برای این ویدیو در دسترس نیست.**\n\n**فرمت‌های موجود:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **خطا در پردازش فایل**\n\nصدا دانلود شد اما به دلیل کاراکترهای نامعتبر در نام فایل نمی‌تواند پردازش شود.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **خطا در پردازش فایل**\n\nصدا دانلود شد اما به دلیل خطای آرگومان نامعتبر نمی‌تواند پردازش شود.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "کاربر محتوای ممنوعه وارد کرده است. نمی‌تواند دانلود شود."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "تار NSFW از طریق دستور تنظیم شد: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "کاربر منوی /nsfw را باز کرد."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: بسته شد."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "دانلود کوکی {service} ناموفق بود: وضعیت={status} (url مخفی)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "خطا در دانلود کوکی {service}: {error} (url مخفی)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "خطای غیرمنتظره در حین دانلود کوکی {service} (url مخفی): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "فایل کوکی برای کاربر {user_id} به‌روزرسانی شد."
    COOKIES_INVALID_CONTENT_LOG_MSG = "محتوای کوکی نامعتبر توسط کاربر {user_id} ارائه شد."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "URLهای کوکی YouTube برای کاربر {user_id} خالی هستند."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "کوکی‌های YouTube برای کاربر {user_id} از منبع {source} دانلود و اعتبارسنجی شدند."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "همه منابع کوکی YouTube برای کاربر {user_id} ناموفق بودند."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "خطا در دستور check_porn توسط مدیر {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "اندازه بخش تقسیم به {size} بایت تنظیم شد."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "آپلود ویدیو با تقسیم فایل تکمیل شد."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "ویدیوهای لیست پخش ارسال شدند: {sent}/{total} فایل (کیفیت={quality}) به کاربر {user_id}"
    UNKNOWN_ERROR_MSG = "❌ خطای ناشناخته: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "رد کردن نوع فایل پشتیبانی نشده در لیست پخش در شاخص {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg یافت نشد. لطفاً FFmpeg را نصب کنید."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ تبدیل به MP4 ناموفق بود: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ جاسازی زیرنویس‌ها ممکن است زمان زیادی ببرد (تا 1 دقیقه به ازای هر 1 دقیقه ویدیو)!\n🔥 شروع به سوزاندن زیرنویس‌ها..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ زیرنویس‌ها به دلیل محدودیت‌ها (کیفیت/مدت زمان/اندازه) نمی‌توانند جاسازی شوند"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ زیرنویس‌ها برای زبان انتخاب شده در دسترس نیستند"
    ERROR_SENDING_VIDEO_MSG = "❌ خطا در ارسال ویدیو: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ ویدیوهای لیست پخش ارسال شدند: {sent}/{total} فایل."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ دانلود به دلیل زمان‌بندی لغو شد (2 ساعت)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ دانلود ویدیو ناموفق بود: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ خطا: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON باید یک شیء (دیکشنری) باشد."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ فرمت JSON نامعتبر است. لطفاً JSON معتبر ارائه دهید."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ مقدار باید بین {min_val} و {max_val} باشد."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} به این تنظیم شد: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ درست"
    ARGS_FALSE_BUTTON_MSG = "❌ نادرست"
    ARGS_BACK_BUTTON_MSG = "🔙 بازگشت"
    ARGS_CLOSE_BUTTON_MSG = "🔚 بستن"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ درست"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ نادرست"
    ARGS_NOT_SET_MSG = "تنظیم نشده"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ فرمت AV1 برای این ویدیو در دسترس نیست.\n\nفرمت‌های موجود:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ خطا در دانلود: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ هیچ ویدیویی در لیست پخش در شاخص {index} یافت نشد."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **تبدیل ویدیو ناموفق بود**\n\nویدیو به دلیل خطای آرگومان نامعتبر نمی‌تواند به MP4 تبدیل شود.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **تبدیل ویدیو ناموفق بود**\n\nویدیو نمی‌تواند به MP4 تبدیل شود.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ دریافت لینک‌های استریم ناموفق بود"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>خطا در دریافت لینک:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ هیچ محتوایی در شاخص {index} یافت نشد"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ خطا: پیام اصلی یافت نشد."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ خطا: URL یافت نشد."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ این URL نمی‌تواند جاسازی شود."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ کدک {codec} برای این ویدیو در دسترس نیست"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ فرمت {format} برای این ویدیو در دسترس نیست"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ محدودیت سیل. بعداً تلاش کنید."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ بررسی کوکی"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ خودکار (هنگام خطای YouTube)"
    PROXY_OFF_BUTTON_MSG = "❌ خاموش"
    PROXY_CLOSE_BUTTON_MSG = "🔚بستن"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 کشور را انتخاب کنید:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ پاک کردن انتخاب کشور"
    PROXY_COUNTRY_SELECTED_MSG = "✅ کشور انتخاب شده: {country} (کد: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 پراکسی های موجود: {proxy_count} (HTTP: {http_count}، SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 ربات ابتدا HTTP و سپس SOCKS5 را امتحان می کند"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 پروکسی به طور خودکار برای کشور انتخاب شده فعال می شود"
    PROXY_COUNTRY_CLEARED_MSG = "✅ انتخاب کشور پاک شد"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ انتخاب کشور پاک شد"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ کشور انتخاب شده: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 استفاده از کشور از فایل: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 کشورهای موجود از فایل: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 کشور انتخابی: {country} (کد: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ پروکسی برای این کشور فعال است"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ پروکسی غیرفعال است (برای فعال کردن ALL (AUTO) را فشار دهید)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ روشن"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ خاموش"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚بستن"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV: روشن"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV: خاموش"
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ روشن (بدون تار)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ روشن (بدون تار)"
    NSFW_OFF_BLUR_MSG = "✅ خاموش (تار)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ خاموش (تار)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "محتوای غیرمجاز"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "پاک"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "خطا در پردازش پیام پاسخ برای کاربر {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "خطا در ارسال پخش برای کاربر {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "لاگ‌های {bot_name}\nکاربر: {user_id}\nکل لاگ‌ها: {total}\nزمان فعلی: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nکل {path}: {count}\nزمان فعلی: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>کل کاربران: {count}</i>\nآخرین 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "کش‌های پورن توسط مدیر {admin_id} بارگذاری مجدد شدند. دامنه‌ها: {domains}، کلمات کلیدی: {keywords}، سایت‌ها: {sites}، WHITELIST: {whitelist}، GREYLIST: {greylist}، BLACK_LIST: {black_list}، WHITE_KEYWORDS: {white_keywords}، PROXY_DOMAINS: {proxy_domains}، PROXY_2_DOMAINS: {proxy_2_domains}، CLEAN_QUERY: {clean_query}، NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "خطا در ارسال پیام زمان‌بندی: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>انتخاب زبان</b>"
    LANG_CHANGED_MSG = "✅ زبان به {lang_name} تغییر یافت"
    LANG_ERROR_MSG = "❌ خطا در تغییر زبان"
    LANG_CLOSED_MSG = "انتخاب زبان بسته شد"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] callback: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "افزودن دکمه نظارت مرورگر با URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "URL نظارت مرورگر پیکربندی نشده است: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **تنظیم صفحه کلید به‌روزرسانی شد!**\n\nتنظیم جدید: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "مخفی کردن صفحه کلید ناموفق بود: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "استفاده از کوکی‌های YouTube کارآمد برای استخراج لینک برای کاربر {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "هیچ کوکی YouTube کارآمدی برای استخراج لینک برای کاربر {user_id} در دسترس نیست"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "استفاده از کوکی‌های YouTube موجود برای استخراج لینک برای کاربر {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "هیچ کوکی YouTube برای استخراج لینک برای کاربر {user_id} یافت نشد"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "فایل کوکی سراسری به پوشه کاربر {user_id} برای استخراج لینک کپی شد"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] کاربر {user_id} دستور mediainfo را درخواست کرد"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] کاربر {user_id} مدیر است: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] کاربر {user_id} در کانال است: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] دسترسی کاربر {user_id} رد شد - نه مدیر و نه در کانال"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] دسترسی کاربر {user_id} اعطا شد"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ این دستور فقط برای مدیران در دسترس است."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ دانلود با پشتیبانی توکن PO تکمیل شد"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ محدودیت سیل. بعداً تلاش کنید."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ خطا در به‌روزرسانی توکن REST: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ خطا در بستن جلسه Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ خطا در راه‌اندازی ساختار پایه db: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ همه پارامترها در config.py تنظیم نشده‌اند (FIREBASE_CONF، FIREBASE_USER، FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL تنظیم نشده است"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey برای دریافت idToken تنظیم نشده است"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ خطا در دانلود دامپ Firebase: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ دانلود دامپ Firebase از طریق REST ناموفق بود"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ خطا در _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ خطا در اجرای بارگذاری مجدد خودکار cache (تلاش {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ همه تلاش‌های مجدد ناموفق بودند"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 شروع دانلود دامپ Firebase در {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ وابستگی در دسترس نیست: requests یا Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ پایگاه داده خالی است"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ خطا در بستن logger: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ خطا در حین پاکسازی: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ خطای Clone: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ زمان‌بندی Clone"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ استثنای Clone: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ به‌روزرسانی توسط کاربر لغو شد"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ مخزن با موفقیت کلون شد"
    UPDATE_BACKUPS_MOVED_MSG = "✅ پشتیبان‌گیری‌ها به _backup/ منتقل شدند"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ همه ماژول‌ها بارگذاری شدند"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ پاکسازی در خروجی تکمیل شد"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 سیگنال {signal} دریافت شد، خاموش شدن به صورت منظم..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "لطفاً صبر کنید..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 در حال دانلود استریم HLS:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "در انتظار قطعات"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ پشتیبان‌گیری {ts} در _backup/ یافت نشد"
    RESTORE_FAILED_RESTORE_MSG = "❌ بازیابی {src} -> {dest_path} ناموفق بود: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ بازیابی شد: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>جزئیات:</b> {error_details}\n\nدانلود به دلیل خطای بحرانی متوقف شد.\n\n💡 <b>نکته:</b> اگر خطای 401 Unauthorized دریافت می‌کنید، از دستور <code>/cookie instagram</code> استفاده کنید یا کوکی‌های خود را برای احراز هویت با Instagram ارسال کنید."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ دامنه در لیست سیاه پورن: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ کلمات کلیدی پورن یافت شد: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ دامنه در لیست سفید: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ کلمات کلیدی لیست سفید یافت شد: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ هیچ کلمه کلیدی پورن یافت نشد"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ خطای TikTok API در شاخص {index}، رد کردن به صدا بعدی..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ خطای TikTok API در شاخص {index}، رد کردن به ویدیو بعدی..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "کاربر یک <b>url</b> وارد کرد\n <b>نام کاربر:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>کاربر به این صورت وارد کرد:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "عضویت در کانال"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 ثبت handler: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - دانلود 5 کوکی من"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - دریافت کوکی YT مرورگر"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - اعتبارسنجی فایل کوکی شما"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - آپلود کوکی سفارشی"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 بستن"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "فرمت‌های موجود برای: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚بستن"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚بستن"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚بستن"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Close"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "راهنما بسته شد."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "بسته شد"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "خطا رخ داد"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg در PATH یا دایرکتوری پروژه یافت نشد. لطفاً FFmpeg را نصب کنید."
    YTDLP_NOT_FOUND_MSG = "باینری yt-dlp در PATH یا دایرکتوری پروژه یافت نشد. لطفاً yt-dlp را نصب کنید."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "ویدیو به {rounds} بخش تقسیم خواهد شد که ممکن است بیش از حد باشد"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "تقسیم بخش ویدیو {current}/{total}: {start_time:.2f} ثانیه تا {end_time:.2f} ثانیه"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "ایجاد بخش تقسیم {part} ناموفق بود: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "بخش تقسیم {part} با موفقیت ایجاد شد: {target_name} ({size} بایت)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "خطا در تقسیم بخش ویدیو {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "ویدیو با موفقیت به {count} بخش تقسیم شد"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "خطا در فرآیند تقسیم ویدیو: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] خطا در حین پردازش ویدیو {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "فایل ویدیو وجود ندارد: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "خطا در تجزیه ابعاد '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "نمی‌توان ابعاد ویدیو را از '{size_result}' تعیین کرد، استفاده از پیش‌فرض: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "خطا در ایجاد بندانگشتی: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "خطا در تجزیه مدت زمان ویدیو: {error}، نتیجه: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "بندانگشتی در {thumb_dir} ایجاد نشد، استفاده از پیش‌فرض"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "خطا در اجرای دستور: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "خطا در ایجاد بندانگشتی با FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "رد کردن بخش پیکربندی غیر-dict: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "تنظیم {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] استفاده از کوکی‌های کاربر: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "استفاده از کوکی‌های YouTube برای کاربر {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "فایل کوکی سراسری به پوشه کاربر {user_id} کپی شد"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] استفاده از کوکی‌های سراسری کپی شده به عنوان کوکی‌های کاربر: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "کپی فایل کوکی سراسری برای کاربر {user_id} ناموفق بود: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "استفاده از --no-cookies برای دامنه: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "پروکسی درخواست شد اما وارد کردن/دریافت پیکربندی ناموفق بود: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "اجبار استفاده از پروکسی برای gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "پروکسی درخواست شد اما پیکربندی پروکسی ناقص است"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "کمک‌کننده پروکسی ناموفق بود: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "تجزیه موارد extractor..."
    GALLERY_DL_ITEM_COUNT_MSG = "مورد {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "متادیتا یافت شد (تگ 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL یافت شد (تگ 3): {url}، متادیتا: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "متادیتا یافت شد (legacy): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL یافت شد (legacy): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "نام فایل یافت شد: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "دایرکتوری یافت شد: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "پسوند یافت شد: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "{count} مورد تجزیه شد، اطلاعات: {info}، fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "تنظیم پیکربندی gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "تلاش استراتژی A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "ماژول gallery_dl.extractor یافت نشد"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() در این بیلد در دسترس نیست"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "فراخوانی extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "هیچ extractor با URL مطابقت نداشت"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "تنظیم کوکی‌ها روی extractor: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "تنظیم کوکی‌ها روی extractor ناموفق بود: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Extractor یافت شد، فراخوانی items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "استراتژی A موفق بود، اطلاعات دریافت شد: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "استراتژی A: extractor.items() هیچ اطلاعات معتبری برنگرداند"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "استراتژی A (extractor.find) ناموفق بود: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "متادیتای fallback از --get-urls: کل={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "همه استراتژی‌ها برای دریافت متادیتا ناموفق بودند"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "استخراج اطلاعات تصویر ناموفق بود: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "ماژول gallery_dl.job یافت نشد (نصب خراب؟)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob در این بیلد در دسترس نیست"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "جستجوی فایل‌های دانلود شده در دایرکتوری gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "تلاش برای یافتن فایل‌ها بر اساس نام‌ها از extractor"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "خطا در خواندن آرگومان‌های کاربر برای {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] خطا در حین پردازش ویدیو {video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "کاربر {user_id} send_as_file را فعال کرده است، ارسال به عنوان سند"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video به طور مکرر زمان‌بندی شد؛ بازگشت به send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "عنوان خیلی طولانی است، تلاش با عنوان حداقلی"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (عنوان حداقلی) زمان‌بندی شد؛ بازگشت به send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "خطا در ارسال ویدیو با عنوان حداقلی: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "خطا در ارسال فایل توضیحات کامل: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "خطا در حذف فایل توضیحات موقت: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "رد کردن match_filter برای دامنه در NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "بررسی کوکی‌های YouTube موجود در URL کاربر برای شناسایی فرمت برای کاربر {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "کوکی‌های YouTube موجود در URL کاربر برای شناسایی فرمت برای کاربر {user_id} کار می‌کنند - استفاده از آنها"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "کوکی‌های YouTube موجود در URL کاربر برای شناسایی فرمت برای کاربر {user_id} ناموفق بودند، تلاش برای دریافت جدید"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "تلاش منبع کوکی YouTube {i} برای شناسایی فرمت برای کاربر {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "کوکی‌های YouTube از منبع {i} در URL کاربر برای شناسایی فرمت برای کاربر {user_id} کار می‌کنند - ذخیره در پوشه کاربر"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "کوکی‌های YouTube از منبع {i} در URL کاربر برای شناسایی فرمت برای کاربر {user_id} کار نمی‌کنند"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "دانلود کوکی‌های YouTube از منبع {i} برای شناسایی فرمت برای کاربر {user_id} ناموفق بود"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "همه منابع کوکی YouTube برای شناسایی فرمت برای کاربر {user_id} ناموفق بودند، بدون کوکی تلاش خواهد شد"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "هیچ منبع کوکی YouTube برای شناسایی فرمت برای کاربر {user_id} پیکربندی نشده است، بدون کوکی تلاش خواهد شد"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "هیچ کوکی YouTube برای شناسایی فرمت برای کاربر {user_id} یافت نشد، تلاش برای دریافت جدید"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "استفاده از کوکی‌های YouTube برای شناسایی فرمت برای کاربر {user_id} (قبلاً در منوی Always Ask اعتبارسنجی شده است)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "هیچ کوکی YouTube برای شناسایی فرمت برای کاربر {user_id} یافت نشد، تلاش برای بازیابی..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "فایل کوکی سراسری به پوشه کاربر {user_id} برای شناسایی فرمت کپی شد"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "کپی فایل کوکی سراسری برای کاربر {user_id} ناموفق بود: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "استفاده از --no-cookies برای دامنه در get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "برنامه هنوز راه‌اندازی نشده است. نمی‌توان به {name} دسترسی داشت"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>عنوان:</b> <code>{caption}</code>\n<b>شناسه کاربر:</b> <code>{user_id}</code>\n<b>نام کاربر:</b> <code>{users_name}</code>\n<b>شناسه فایل ویدیو:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "خطا در caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "خطای غیرمنتظره در caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL ویدیو</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL در پیکربندی وجود ندارد"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin راه‌اندازی شد"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken به‌روزرسانی شد"
    DB_LOG_FOR_USER_ADDED_MSG = "لاگ برای کاربر اضافه شد"
    DB_DATABASE_CREATED_MSG = "پایگاه داده ایجاد شد"
    DB_BOT_STARTED_MSG = "ربات شروع شد"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY در config.py ذخیره شد: {hours} ساعت"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "بخش لیست پخش قبلاً کش شده است: {path_parts}، رد کردن"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: هیچ کشی برای هیچ نوع URL/کیفیت یافت نشد، بازگرداندن دیکشنری خالی"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: شمارش سریع برای محدوده بزرگ: {cached_count} ویدیوی کش شده"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: هیچ کشی برای هش {url_hash}، کیفیت {quality_key} یافت نشد"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: هیچ کشی برای هیچ نوع URL یافت نشد، بازگرداندن None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ دسترسی رد شد. فقط مدیر."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 بارگذاری مجدد خودکار کش Firebase به‌روزرسانی شد!\n\n📊 وضعیت: {status}\n⏰ برنامه: هر {interval} ساعت از 00:00\n🕒 بارگذاری مجدد بعدی: {next_exec} (در {delta_min} دقیقه)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 بارگذاری مجدد خودکار کش Firebase متوقف شد!\n\n📊 وضعیت: ❌ غیرفعال\n💡 از /auto_cache on برای فعال‌سازی مجدد استفاده کنید"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ آرگومان نامعتبر. از /auto_cache on | off | N (1..168) استفاده کنید"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ فاصله باید بین 1 تا 168 ساعت باشد"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ تنظیم فاصله ناموفق بود"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ فاصله بارگذاری مجدد خودکار کش Firebase به‌روزرسانی شد!\n\n📊 وضعیت: ✅ فعال\n⏰ برنامه: هر {interval} ساعت از 00:00\n🕒 بارگذاری مجدد بعدی: {next_exec} (در {delta_min} دقیقه)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 بارگذاری مجدد خودکار کش Firebase شروع شد!\n\n📊 وضعیت: ✅ فعال\n⏰ برنامه: هر {interval} ساعت از 00:00\n🕒 بارگذاری مجدد بعدی: {next_exec} (در {delta_min} دقیقه)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 بارگذاری مجدد خودکار کش Firebase متوقف شد!\n\n📊 وضعیت: ❌ غیرفعال\n💡 از /auto_cache on برای فعال‌سازی مجدد استفاده کنید"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "بارگذاری مجدد خودکار فعال شد؛ بعدی در {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "بارگذاری مجدد خودکار توسط مدیر غیرفعال شد."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "فاصله بارگذاری مجدد خودکار به {interval} ساعت تنظیم شد؛ بعدی در {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "بارگذاری مجدد خودکار شروع شد؛ بعدی در {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "بارگذاری مجدد خودکار توسط مدیر متوقف شد."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ کش Firebase بارگذاری شد: {count} گره ریشه"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ فایل کش Firebase یافت نشد، شروع با کش خالی: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ بارگذاری کش firebase ناموفق بود: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ کش Firebase بارگذاری مجدد شد: {count} گره ریشه"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ فایل کش Firebase یافت نشد: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ بارگذاری مجدد کش firebase ناموفق بود: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 شما از ربات مسدود شده‌اید! برای رفع مسدودیت با {Config.ADMIN_USERNAME} تماس بگیرید\n<blockquote>P.S. کانال را ترک نکنید - به طور خودکار مسدود خواهید شد ⛔️</blockquote>\n🌍تغییر زبان /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ هیچ فرمت ویدیویی یافت نشد. در حال امتحان دانلودگر تصویر…"
    AA_FLOOD_WAIT_MSG = "⚠️ تلگرام ارسال پیام را محدود کرده است.\n⏳ لطفاً صبر کنید: {time_str}\nبرای به‌روزرسانی تایمر، URL را دوباره 2 بار ارسال کنید."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>برای کپی URL استریم روی دکمه کلیک کنید، سپس آن را در برنامه VLC جایگذاری کنید</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>برای کپی URL استریم روی دکمه کلیک کنید، سپس آن را در برنامه VLC جایگذاری کنید</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>خطا در دریافت لینک:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ خطا در ارسال فایل فرمت‌ها: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ دریافت فرمت‌ها ناموفق بود:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 در حال تجزیه و تحلیل... (6 ثانیه صبر کنید)"
    AA_PROCESSING_MSG = "🔎 در حال تجزیه و تحلیل..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ تگ #{wrong} شامل کاراکترهای ممنوع است. فقط حروف، اعداد و _ مجاز است.\nلطفاً استفاده کنید: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ برای کار در گروه، ربات به حقوق مدیر نیاز دارد. لطفاً ربات را مدیر این گروه کنید."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "سلام {first_name}،\n \n<i>این ربات🤖 می‌تواند هر ویدیویی را مستقیماً به تلگرام دانلود کند.😊 برای اطلاعات بیشتر <b>/help</b> را فشار دهید</i> 👈\n\n<blockquote>P.S. به دلیل محتوای احتمالی 🔞NSFW - دانلود از ☁️<b>ذخیره‌سازی ابری</b>، 📁<b>اشتراک‌گذاری فایل</b>، 🔗<b>کوتاه‌کننده‌های URL</b> و 🔞<b>سایت‌های مستهجن</b> پولی است! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ کانال @tg_ytdlp را 🗑<b>حذف/لغو اشتراک نکنید</b> و به ربات 🤖<b>URL/دستورات را بیش از حد اسپم نکنید</b> - به‌طور خودکار از استفاده ربات محروم می‌شوید ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 هیچ فایلی برای حذف وجود ندارد."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 همه فایل‌ها با موفقیت حذف شدند!\n\nفایل‌های حذف شده:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ تا پایان دانلود قبلی صبر کنید"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "نمونه برنامه در check_user None است"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict None است، اجازه دانلود"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict None است، اجازه جاسازی زیرنویس"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: بررسی محدودیت‌ها - حداکثر کیفیت={max_quality}p، حداکثر مدت زمان={max_duration} ثانیه، حداکثر اندازه={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: کلیدهای info_dict: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "جاسازی زیرنویس رد شد: مدت زمان {duration} ثانیه از محدودیت {max_duration} ثانیه تجاوز می‌کند"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "جاسازی زیرنویس رد شد: اندازه {size_mb:.2f}MB از محدودیت {max_size}MB تجاوز می‌کند"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "جاسازی زیرنویس رد شد: کیفیت {width}x{height} (حداقل ضلع {min_side}p) از محدودیت {max_quality}p تجاوز می‌کند"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "لیست پخش"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ محدودیت محدوده برای {service} تجاوز شد: {count} (حداکثر {max_count}).\n\nاز یکی از این دستورات برای دانلود حداکثر فایل‌های موجود استفاده کنید:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ محدودیت محدوده برای {service} تجاوز شد: {count} (حداکثر {max_count})\nشناسه کاربر: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "ارائه‌دهنده توکن PO در پیکربندی غیرفعال است"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} دامنه YouTube نیست، رد کردن توکن PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "ارائه‌دهنده توکن PO در {base_url} در دسترس نیست، بازگشت به استخراج استاندارد YouTube"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "کش ارائه‌دهنده توکن PO پاک شد، در درخواست بعدی در دسترس بودن بررسی خواهد شد"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "نمونه برنامه هنوز در دسترس نیست"
    HELPER_USER_NAME_MSG = "کاربر"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood wait شناسایی شد، خوابیدن برای {wait_seconds} ثانیه"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood wait شناسایی شد اما نمی‌توان زمان را استخراج کرد، خوابیدن برای {retry_delay} ثانیه"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "خطای msg_seqno شناسایی شد، خوابیدن برای {retry_delay} ثانیه"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "پیکربندی پروکسی ناقص است، استفاده از اتصال مستقیم"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚بستن"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚بستن"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚بستن"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 فایل لاگ‌ها حذف شد."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 فایل تگ‌ها حذف شد."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 فایل فرمت حذف شد."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 فایل تقسیم حذف شد."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 فایل Mediainfo حذف شد."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 تنظیمات زیرنویس حذف شدند."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 تنظیمات صفحه کلید حذف شدند."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 تنظیمات Args حذف شدند."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 تنظیمات NSFW حذف شدند."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 تنظیمات پروکسی حذف شدند."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 تنظیمات Flood wait حذف شدند."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚بستن"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 دستور دانلود ویدیو"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "استفاده: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "مثال‌ها:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (ترتیب مستقیم)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (ترتیب معکوس)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "همچنین ببینید: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "کاربر {user_id} دستور add_bot_to_group را بست"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "استخراج شناسه YouTube ناموفق بود"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "دانلود بندانگشتی ناموفق بود یا خیلی بزرگ است"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "زبان صوتی را انتخاب کنید"
    AA_NO_SUBTITLES_DETECTED_MSG = "هیچ زیرنویسی شناسایی نشد"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "زبان زیرنویس را انتخاب کنید"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "خطای احراز هویت"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "حساب یافت نشد"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "حساب در دسترس نیست"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "محدودیت نرخ تجاوز شد"
    GALLERY_DL_NETWORK_ERROR_MSG = "خطای شبکه"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "محتوا در دسترس نیست"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "محدودیت‌های جغرافیایی"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "تأیید لازم است"
    GALLERY_DL_POLICY_VIOLATION_MSG = "نقض سیاست"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "خطای ناشناخته"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ دانلود شروع شد</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚بستن"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 دستور دانلود ویدیو</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "استفاده: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>مثال‌ها:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "همچنین ببینید: /audio، /img، /help، /playlist، /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ محدودیت سیل. بعداً تلاش کنید."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 استفاده از دستور کوکی</b>

<code>/cookie</code> - نمایش منوی کوکی
<code>/cookie youtube</code> - دانلود کوکی‌های YouTube
<code>/cookie instagram</code> - دانلود کوکی‌های Instagram
<code>/cookie tiktok</code> - دانلود کوکی‌های TikTok
<code>/cookie x</code> یا <code>/cookie twitter</code> - دانلود کوکی‌های Twitter/X
<code>/cookie facebook</code> - دانلود کوکی‌های Facebook
<code>/cookie custom</code> - نمایش دستورالعمل‌های کوکی سفارشی

<i>سرویس‌های موجود بستگی به پیکربندی ربات دارد.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 فایل کوکی حذف شد و کش پاک شد."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ قبلی"
    SUBS_BACK_BUTTON_MSG = "🔙بازگشت"
    SUBS_OFF_BUTTON_MSG = "🚫 خاموش"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - تنظیم زبان"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - تنظیم زبان با AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "گزینه‌های معتبر:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 LANGUAGE"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 CLEAN"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIES"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MEDIA"
    SETTINGS_INFO_BUTTON_MSG = "📖 INFO"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ MORE"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 فقط کوکی‌ها"
    SETTINGS_LOGS_BUTTON_MSG = "📃 لاگ‌ها "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ تگ‌ها"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 فرمت"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ تقسیم"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 زیرنویس‌ها"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 صفحه کلید"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Args"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 پروکسی"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Flood wait"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  همه فایل‌ها"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - دانلود 5 کوکی من"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - دریافت کوکی YT مرورگر"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - اعتبارسنجی فایل کوکی شما"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - آپلود کوکی سفارشی"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - تغییر کیفیت و فرمت"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - روشن/خاموش کردن MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - تغییر اندازه بخش تقسیم ویدیو"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - دانلود ویدیو به عنوان صدا"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - تنظیمات زبان زیرنویس"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - نحوه دانلود لیست‌های پخش"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - دانلود تصاویر از طریق gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - ارسال #تگ‌های شما"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - دریافت دستورالعمل‌ها"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - ارسال لاگ‌های شما"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - راهنمای لیست پخش"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - نحوه"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - دریافت لینک‌های مستقیم ویدیو"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - فعال/غیرفعال کردن پروکسی"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - چیدمان صفحه کلید"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - کمک‌کننده جستجوی درون خطی"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - آرگومان‌های yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - تنظیمات تار NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 گزینه‌های پاکسازی</b>\n\nانتخاب کنید چه چیزی را پاک کنید:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 موبایل: فعال کردن جستجوی @vid"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 موبایل: فعال کردن جستجوی @vid"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 خاموش"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 کامل"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL تصاویر]({url})"
    IMAGE_ERROR_MSG = "❌ خطا: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙بازگشت"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - فرمت سفارشی"
    FORMAT_720P_MSG = "• <code>/format 720</code> - کیفیت 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - کیفیت 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - کیفیت 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - شناسه فرمت خاص"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - همیشه منو را نمایش بده"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/بهترین کیفیت"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Always Ask (منو + دکمه‌ها)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 سایر (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (بهترین برای PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (بهترین برای موبایل Telegram)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (حداکثر کیفیت)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 سفارشی (خودتان وارد کنید)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 از مرورگر"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 خودتان"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ حالت ورودی به دلیل عدم فعالیت به طور خودکار بسته شد (5 دقیقه)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 بازنشانی همه"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 مشاهده فعلی"
    ARGS_BACK_BUTTON_MSG = "🔙 بازگشت"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>این پیام را به علاقه‌مندی‌های خود ارسال کنید تا این تنظیمات را به عنوان الگو ذخیره کنید.</i> \n\n<i>این پیام را دوباره اینجا ارسال کنید تا این تنظیمات اعمال شوند.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 آرگومان‌های فعلی yt-dlp:\n\nهیچ تنظیم سفارشی پیکربندی نشده است.\n\n---\n\n<i>این پیام را به علاقه‌مندی‌های خود ارسال کنید تا این تنظیمات را به عنوان الگو ذخیره کنید.</i> \n\n<i>این پیام را دوباره اینجا ارسال کنید تا این تنظیمات اعمال شوند.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 آرگومان‌های فعلی yt-dlp:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 صادرات تنظیمات"
    ARGS_SETTINGS_READY_MSG = "تنظیمات برای صادرات آماده است! این پیام را به علاقه‌مندی‌ها ارسال کنید تا ذخیره شود."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 آرگومان‌های فعلی yt-dlp:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ شناسایی تنظیمات در پیام ناموفق بود. مطمئن شوید که یک الگوی تنظیمات صحیح ارسال کرده‌اید."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ تنظیمات با موفقیت وارد شد!\n\nپارامترهای اعمال شده: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "تنظیمات کلیدی:\n"
    ARGS_ERROR_SAVING_MSG = "❌ خطا در ذخیره تنظیمات وارد شده."
    ARGS_ERROR_IMPORTING_MSG = "❌ خطایی در حین وارد کردن تنظیمات رخ داد."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>دانلود فایل‌های کوکی</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "یک سرویس برای دانلود فایل کوکی انتخاب کنید."
    COOKIE_MENU_SAVE_INFO_MSG = "فایل‌های کوکی به عنوان cookie.txt در پوشه شما ذخیره خواهند شد."
    COOKIE_MENU_TIP_HEADER_MSG = "نکته: همچنین می‌توانید از دستور مستقیم استفاده کنید:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – دانلود و اعتبارسنجی کوکی‌ها"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – استفاده از یک منبع خاص بر اساس شاخص (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "سپس با <code>/check_cookie</code> تأیید کنید (تست روی RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "همیشه بپرس"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗لینک"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁تماشا"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝عنوان"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ برش"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>برش ویدیو</b>\n\nمدت زمان ویدیو: <b>{start_time} - {end_time}</b>\n\nلطفاً محدوده زمانی مورد نظر را در قالب ارسال کنید:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nمثال: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ فرمت نامعتبر. لطفاً استفاده کنید: <code>HH:MM:SS-HH:MM:SS</code>\n\nمثال: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ محدوده نامعتبر. زمان شروع باید کمتر از زمان پایان باشد."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ محدوده زمانی خارج از مرزهای ویدیو است.\n\nمدت زمان ویدیو: <b>{start_time} - {end_time}</b>\n\nمحدوده شما باید در این محدودیت‌ها باشد."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>ویدیو برش داده می‌شود:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ به طور جزئی تکمیل شد - {successful_uploads}/{total_files} فایل صوتی آپلود شد."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ صدا با موفقیت دانلود و ارسال شد - {total_files} فایل آپلود شد."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>حساب TikTok خصوصی</b>\n\n"
        "این حساب TikTok خصوصی است یا همه ویدیوها خصوصی هستند.\n\n"
        "<b>💡 راه حل:</b>\n"
        "1. حساب @{username} را دنبال کنید\n"
        "2. کوکی‌های خود را با استفاده از دستور <code>/cookie</code> به ربات ارسال کنید\n"
        "3. دوباره تلاش کنید\n\n"
        "<b>پس از به‌روزرسانی کوکی‌ها، دوباره تلاش کنید!</b>"
    )

    #######################################################
