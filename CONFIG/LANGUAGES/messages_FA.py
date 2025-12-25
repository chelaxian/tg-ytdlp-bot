# Messages Configuration
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# Removed circular import

class Messages(object):
    #######################################################
    # Messages and errors
    #######################################################
    CREDITS_MSG = "<blockquote><i>مدیریت شده توسط</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 تغییر زبان: /lang</b>"
    TO_USE_MSG = "<i>برای استفاده از این ربات باید به کانال تلگرام @tg_ytdlp مشترک شوید.</i>\nپس از پیوستن به کانال، <b>لینک ویدیوی خود را دوباره ارسال کنید و ربات آن را برای شما دانلود می‌کند</b> ❤️\n\n<blockquote>P.S. دانلود محتوای 🔞NSFW و فایل‌ها از ☁️Cloud Storage پولی است! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ کانال را ترک نکنید - از استفاده از ربات محروم خواهید شد ⛔️</blockquote>"

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
    ARGS_INVALID_BOOL_MSG = "❌ Invalid boolean value"
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
        "<b>💬 Subtitles</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Language:</b> {lang}\n"
        "<b>Type:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 فایل SRT زیرنویس برای کاربر ارسال شد."
    SUBS_ERROR_PROCESSING_MSG = "❌ خطا در پردازش فایل زیرنویس."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ دانلود زیرنویس‌ها ناموفق بود."
    SUBS_ERROR_MSG = "❌ خطا در دانلود زیرنویس‌ها: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Split part size set to: {size}"
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
        "🎬 **Choose max part size for video splitting:**\n\n"
        "**Range:** 100MB to 2GB\n\n"
        "**Quick commands:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Examples:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "منو بسته شد."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>تنظیمات ربات</b>\n\nیک دسته انتخاب کنید:"
    SETTINGS_MENU_CLOSED_MSG = "منو بسته شد."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Clean Options</b>\n\nChoose what to clean:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nChoose an action:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIA</b>\n\nChoose an action:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nChoose an action:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ MORE COMMANDS</b>\n\nChoose an action:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Command executed."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Flood limit. Try later."
    SETTINGS_HINT_SENT_MSG = "Hint sent."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Search helper opened."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Unknown command."
    SETTINGS_HINT_CLOSED_MSG = "Hint closed."
    SETTINGS_HELP_SENT_MSG = "ارسال فایل راهنمای txt به کاربر"
    SETTINGS_MENU_OPENED_MSG = "منوی /settings باز شد"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Search helper closed"
    SEARCH_CLOSED_MSG = "Closed"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proxy {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Error saving proxy settings."
    PROXY_MENU_TEXT_MSG = "فعال یا غیرفعال کردن استفاده از سرور پروکسی برای تمام عملیات yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "فعال یا غیرفعال کردن استفاده از سرورهای پروکسی ({count} موجود) برای تمام عملیات yt-dlp?\n\nوقتی فعال باشد، پروکسی‌ها با استفاده از روش {method} انتخاب می‌شوند."
    PROXY_MENU_CLOSED_MSG = "منو بسته شد."
    PROXY_ENABLED_CONFIRM_MSG = "✅ پروکسی فعال شد. تمام عملیات yt-dlp از پروکسی استفاده خواهند کرد."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ پروکسی فعال شد. تمام عملیات yt-dlp از {count} سرور پروکسی با روش انتخاب {method} استفاده خواهند کرد."
    PROXY_DISABLED_MSG = "❌ Proxy disabled."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Error saving proxy settings."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy enabled."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy disabled."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ WAIT UNTIL YOUR PREVIOUS DOWNLOAD IS FINISHED"
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
    AUDIO_HELP_CLOSED_MSG = "راهنمای صوتی بسته شد."
    PLAYLIST_HELP_CLOSED_MSG = "راهنمای لیست پخش بسته شد."
    USERLOGS_CLOSED_MSG = "Logs message closed."
    HELP_CLOSED_MSG = "Help closed."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW Blur Settings</b>\n\nNSFW content is <b>{status}</b>.\n\nChoose whether to blur NSFW content:"
    NSFW_MENU_CLOSED_MSG = "منو بسته شد."
    NSFW_BLUR_DISABLED_MSG = "NSFW blur disabled."
    NSFW_BLUR_ENABLED_MSG = "NSFW blur enabled."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW blur disabled."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW blur enabled."
    
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
    LINK_INVALID_URL_MSG = "❌ لطفاً یک URL معتبر وارد کنید"
    LINK_PROCESSING_MSG = "🔗 در حال دریافت لینک مستقیم..."
    LINK_DURATION_MSG = "⏱ <b>مدت زمان:</b> {duration} ثانیه\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>جریان ویدیو:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>جریان صوتی:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Keyboard setting updated!**\n\nNew setting: **{setting}**"
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
    KEYBOARD_ACTIVATED_MSG = "🎹 keyboard activated!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Keyboard hidden"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3 keyboard activated!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3 keyboard activated!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Emoji keyboard activated!"
    KEYBOARD_ERROR_APPLYING_MSG = "Error applying keyboard setting {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ فرمت به این تنظیم شد: Always Ask. هر بار که URL ارسال می‌کنید از شما کیفیت پرسیده می‌شود."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ فرمت به این تنظیم شد: Always Ask. اکنون هر بار که URL ارسال می‌کنید از شما کیفیت پرسیده می‌شود."
    FORMAT_BEST_UPDATED_MSG = "✅ Format updated to best quality (AVC+MP4 priority):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Format updated to ID {id}:\n{format}\n\n💡 <b>Note:</b> If this is an audio-only format, it will be downloaded as MP3 audio file."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Format updated to ID {id} (audio-only):\n{format}\n\n💡 This will be downloaded as MP3 audio file."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Format updated to quality {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Format updated to:\n{format}"
    FORMAT_MENU_MSG = (
        "Select a format option or send a custom one using:\n"
        "• <code>/format &lt;format_string&gt;</code> - custom format\n"
        "• <code>/format 720</code> - 720p quality\n"
        "• <code>/format 4k</code> - 4K quality\n"
        "• <code>/format 8k</code> - 8K quality\n"
        "• <code>/format id 401</code> - specific format ID\n"
        "• <code>/format ask</code> - always show menu\n"
        "• <code>/format best</code> - bv+ba/best quality"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "To use a custom format, send the command in the following form:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Replace <code>bestvideo+bestaudio/best</code> with your desired format string."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Select your desired resolution and codec:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format set to: Always Ask. Now you will be prompted for quality each time you send a URL."
    FORMAT_UPDATED_MSG = "✅ Format updated to:\n{format}"
    FORMAT_SAVED_MSG = "✅ Format saved."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Format choice updated."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "منوی فرمت سفارشی بسته شد"
    FORMAT_CODEC_SET_MSG = "✅ Codec set to {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Browser choice updated."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Access denied. Admin only."
    ACCESS_DENIED_ADMIN = "❌ Access denied. Admin only."
    WELCOME_MASTER = "Welcome Master 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Sorry... Some error occurred during download."
    SIZE_LIMIT_EXCEEDED = "❌ The file size exceeds the {max_size_gb} GB limit. Please select a smaller file within the allowed size."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Script not found: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Downloading fresh Firebase dump using {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase cache reloaded successfully!"
    ADMIN_CACHE_FAILED_MSG = "❌ Failed to reload Firebase cache. Check if {cache_file} exists."
    ADMIN_ERROR_RELOADING_MSG = "❌ Error reloading cache: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Error running {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Promo message sent to all other users</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Cannot send the promo message. Try replying to a message\nOr some error occurred</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ User did not download any content yet...</b> Not exist in logs"
    ADMIN_INVALID_COMMAND_MSG = "❌ Invalid command"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ No data found in cache for <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Queue is empty — nobody left the channel yet."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Ban queue</b>\nPending total: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (left: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… and {extra} more users."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Use /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Blocked users from queue: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Auto-blocking enabled: new leavers will be banned immediately."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Auto-blocking disabled."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Scheduled auto-block window set to every {interval}."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Channel activity log for the last {hours} hours (2 days)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 Last {hours} hours (2 days): joined {joined}, left {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ No activity for the last {hours} hours (2 days)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Total: 🟢 {joined} joined, 🔴 {left} left."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ No access to channel activity log. Bots cannot read admin logs. Provide CHANNEL_GUARD_SESSION_STRING in config with a user session to enable this feature."
    BAN_TIME_USAGE_MSG = "❌ Usage: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Use formats like 10s, 6m, 5h, 4d, 3w, 2M or 1y."
    BAN_TIME_SET_MSG = "🕒 Channel log scan interval set to {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Channel scan report\n"
        "Run at: {run_ts}\n"
        "Interval: {interval}\n"
        "New leavers: {new_leavers}\n"
        "Auto bans: {auto_banned}\n"
        "Pending: {pending}\n"
        "Last event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Usage: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Admin cannot delete an admin"
    ADMIN_USER_BLOCKED_MSG = "User blocked 🔒❌\n \nID: <code>{user_id}</code>\nBlocked Date: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> is already blocked ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Sorry! You are not an admin"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Usage: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "User unblocked 🔓✅\n \nID: <code>{user_id}</code>\nUnblocked Date: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> is already unblocked ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Unblocked users: {count}\n⏱ Timestamp: {date}"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Bot running time -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Please provide a URL to clear cache for.\nUsage: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Please provide a valid URL.\nUsage: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Cache cleared successfully for URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ No cache found for this link."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Error clearing cache: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Access denied. Admin only."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Running porn list update script: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Script completed successfully!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Script completed successfully!\n\nOutput:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Script failed with return code {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Error running script: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Reloading porn and domain-related caches..."
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
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Error reloading porn cache: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Please provide a URL to check.\nUsage: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Please provide a valid URL.\nUsage: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Checking URL for NSFW content...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Porn Check Result</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Status:</b> <b>{status_text}</b>\n\n"
        "<b>Explanation:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Error checking URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Cookies cleaned."
    CLEAN_LOGS_CLEANED_MSG = "logs cleaned."
    CLEAN_TAGS_CLEANED_MSG = "tags cleaned."
    CLEAN_FORMAT_CLEANED_MSG = "format cleaned."
    CLEAN_SPLIT_CLEANED_MSG = "split cleaned."
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfo cleaned."
    CLEAN_SUBS_CLEANED_MSG = "Subtitle settings cleaned."
    CLEAN_KEYBOARD_CLEANED_MSG = "Keyboard settings cleaned."
    CLEAN_ARGS_CLEANED_MSG = "Args settings cleaned."
    CLEAN_NSFW_CLEANED_MSG = "NSFW settings cleaned."
    CLEAN_PROXY_CLEANED_MSG = "Proxy settings cleaned."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Flood wait settings cleaned."
    CLEAN_ALL_CLEANED_MSG = "All files cleaned."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nChoose an action:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Cookie file saved"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Skipped validation for non-YouTube cookies"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Cookie file exists but has incorrect format"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Cookie file is not found."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Starting YouTube cookies test...\n\nPlease wait while I check and validate your cookies."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Your existing YouTube cookies are working properly!\n\nNo need to download new ones."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Your existing YouTube cookies are expired or invalid.\n\n🔄 Downloading new cookies..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} cookie source is not configured!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} cookie source must be a .txt file!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Range limit exceeded: {range_count} files requested (maximum {max_img_files}).\n\nUse one of these commands to download maximum available files:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Close"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Media limit exceeded: {count} files requested (maximum {max_count}).\n\nUse one of these commands to download maximum available files:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Found <b>{count}</b> media items from the link"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Select download range:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Browser impersonation"
    ARGS_REFERER_DESC_MSG = "Referer header"
    ARGS_USER_AGENT_DESC_MSG = "User-Agent header"
    ARGS_GEO_BYPASS_DESC_MSG = "Bypass geographic restrictions"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Check SSL certificate"
    ARGS_LIVE_FROM_START_DESC_MSG = "Download live streams from start"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Do not download live streams from start"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Use MPEG-TS container for HLS videos"
    ARGS_NO_PLAYLIST_DESC_MSG = "Download only single video, not playlist"
    ARGS_NO_PART_DESC_MSG = "Do not use .part files"
    ARGS_NO_CONTINUE_DESC_MSG = "Do not resume partial downloads"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Audio format for extraction"
    ARGS_EMBED_METADATA_DESC_MSG = "Embed metadata in video file"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Embed thumbnail in video file"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Write thumbnail to file"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Number of concurrent fragments to download"
    ARGS_FORCE_IPV4_DESC_MSG = "Force IPv4 connections"
    ARGS_FORCE_IPV6_DESC_MSG = "Force IPv6 connections"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For header strategy"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP chunk size (bytes)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Sleep before subtitle download (seconds)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Allow legacy server connections"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Suppress HTTPS certificate validation"
    ARGS_USERNAME_DESC_MSG = "Account username"
    ARGS_PASSWORD_DESC_MSG = "Account password"
    ARGS_TWOFACTOR_DESC_MSG = "Two-factor authentication code"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Ignore download errors and continue"
    ARGS_MIN_FILESIZE_DESC_MSG = "Minimum file size (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Maximum file size (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Playlist items to download (e.g., 1,3,5 or 1-5)"
    ARGS_DATE_DESC_MSG = "Download videos uploaded on this date (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Download videos uploaded before this date (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Download videos uploaded after this date (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Custom HTTP headers (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Sleep interval between requests (seconds)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Maximum sleep interval (seconds)"
    ARGS_RETRIES_DESC_MSG = "Number of retries"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Video container format"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Output container format for merging"
    ARGS_SEND_AS_FILE_DESC_MSG = "Send all media as document instead of media"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Impersonate"
    ARGS_REFERER_SHORT_MSG = "Referer"
    ARGS_GEO_BYPASS_SHORT_MSG = "Geo Bypass"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Check Cert"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Live Start"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "No Live Start"
    ARGS_USER_AGENT_SHORT_MSG = "User Agent"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "بدون پلی‌لیست"
    ARGS_NO_PART_SHORT_MSG = "No Part"
    ARGS_NO_CONTINUE_SHORT_MSG = "No Continue"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Audio Format"
    ARGS_EMBED_METADATA_SHORT_MSG = "Embed Meta"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Embed Thumb"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Write Thumb"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Concurrent"
    ARGS_FORCE_IPV4_SHORT_MSG = "Force IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Force IPv6"
    ARGS_XFF_SHORT_MSG = "XFF Header"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Chunk Size"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Sleep Subs"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Legacy Connect"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "No Check Cert"
    ARGS_USERNAME_SHORT_MSG = "Username"
    ARGS_PASSWORD_SHORT_MSG = "Password"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Ignore Errors"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Min Size"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Max Size"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "آیتم‌های پلی‌لیست"
    ARGS_DATE_SHORT_MSG = "Date"
    ARGS_DATEBEFORE_SHORT_MSG = "Date Before"
    ARGS_DATEAFTER_SHORT_MSG = "Date After"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP Headers"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Sleep Interval"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Max Sleep"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Video Format"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Merge Format"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Send As File"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ The file is too large. Maximum size is 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Only files of the following format are allowed .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ The file does not look like cookie.txt (there is no line '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ Error reading file: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Cookie file exists and has correct format"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} cookie file is too large! Max 100KB, got {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} cookie file downloaded and saved as cookie.txt in your folder.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} cookie source is unavailable (status {status}). Please try again later."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Error downloading {service} cookie file. Please try again later."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ User provided a new cookie file.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie successfully updated:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Not a valid cookie.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube cookie sources are not configured!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Access denied. Admin only."
    ADMIN_USER_LOGS_TOTAL_MSG = "Total: <b>{total}</b>\n<b>{user_id}</b> - logs (Last 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 keyboard activated!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Subtitle language set to: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Subtitle language set to: {flag} {name} with AUTO/TRANS enabled."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Subtitle language menu closed."
    SUBS_DOWNLOADING_MSG = "💬 Downloading subtitles..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Reloading Firebase cache into memory..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ No COOKIE_URL configured. Use /cookie or upload cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Downloading cookies from remote URL..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL must point to a .txt file."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fallback cookie file is too large (>100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie file downloaded via fallback and saved as cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fallback cookie source unavailable (status {status}). Try /cookie or upload cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Error downloading fallback cookie. Try /cookie or upload cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Unexpected error during fallback cookie download."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} browser not installed."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookies saved using browser: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Failed to save cookies: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube cookies are working properly"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube cookies are expired or invalid\n\nUse /cookie to get new cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - custom format\n• <code>/format 720</code> - 720p quality\n• <code>/format 4k</code> - 4K quality"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Hint sent."
    FORMAT_MKV_TOGGLE_MSG = "MKV is now {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ No remote URL configured"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Invalid file format"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ File too large"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookies downloaded successfully"
    COOKIES_SERVER_ERROR_MSG = "❌ Server error {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Download failed"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Unexpected error"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Browser not installed."
    COOKIES_MENU_CLOSED_MSG = "Menu closed."
    COOKIES_HINT_CLOSED_MSG = "Cookie hint closed."
    IMG_HELP_CLOSED_MSG = "Help closed."
    SUBS_LANGUAGE_UPDATED_MSG = "Subtitle language settings updated."
    SUBS_MENU_CLOSED_MSG = "Subtitle language menu closed."
    KEYBOARD_SET_TO_MSG = "Keyboard set to {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Error processing setting"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo enabled."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo disabled."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW blur disabled."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW blur enabled."
    SETTINGS_MENU_CLOSED_MSG = "Menu closed."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Flood wait active. Try later."
    OTHER_HELP_CLOSED_MSG = "Help closed."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Logs message closed."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menu closed."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Invalid size."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Error sending MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ An error occurred: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - all logs"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - all {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Download from Remote URL"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Open Browser"
    SELECT_BROWSER_MSG = "Select a browser to download cookies from:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "No browsers found on this system. You can download cookies from remote URL or monitor browser status:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Open Browser</b> - to monitor browser status in mini-app"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Failed to run /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Flood limit. Try later."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Failed to open browser cookie menu"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Save as cookie hint closed."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Usage:</b>\n<code>/link [quality] URL</code>\n\n<b>Examples:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - best quality\n• /link 720 https://youtube.com/watch?v=... - 720p or lower\n• /link 720p https://youtube.com/watch?v=... - same as above\n• /link 4k https://youtube.com/watch?v=... - 4K or lower\n• /link 8k https://youtube.com/watch?v=... - 8K or lower</blockquote>\n\n<b>Quality:</b> from 1 to 10000 (e.g., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K quality"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Failed to get stream links"
    LINK_ERROR_GETTING_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Invalid YouTube cookie index: {selected_index}. Available range is 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}\n🔍 Testing cookies..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube cookies successfully downloaded and validated!\n\nUsed source {source} of {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ All YouTube cookies are expired or unavailable!\n\nContact the bot administrator to replace them."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube cookie retry limit exceeded!\n\n🔢 Maximum: {limit} attempts per hour\n⏰ Please try again later"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Tag #{wrong} contains forbidden characters. Only letters, digits and _ are allowed.\nPlease use: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Invalid argument!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Subtitle language set: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Example: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} زبان انتخاب شده: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ حالت Always Ask {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Subtitles are disabled"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Subtitle settings</b>\n\n{status_text}\n\nSelect subtitle language:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - disable subtitles\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Subtitle settings</b>\n\n{status_text}\n\nSelect subtitle language:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Title:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 720p max quality\n- 1.5 hour max duration\n- 500mb max video size</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️WARNING: due to high CPU impact this function is very slow (near real-time) and limited to:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Quick commands:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - disable subtitles\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - enable Always Ask mode\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - set language\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - set language with AUTO/TRANS enabled\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - enable Always Ask mode\n"
    SUBS_AUTO_SUBS_TEXT = " (auto-subs)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Auto-subs mode {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS disabled via command: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Always Ask enabled via command: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "SUBS language set via command: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "SUBS language + auto mode set via command: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "User opened /subs menu."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "User set subtitle language to: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "User toggled AUTO/TRANS mode to: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "User toggled Always Ask mode to: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "User requested cookies from browser."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Browser selection keyboard sent with installed browsers only."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Browser selection closed."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "Fallback COOKIE_URL used successfully (source hidden)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "Fallback COOKIE_URL failed: status={status} (hidden)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Fallback COOKIE_URL unexpected error: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Browser {browser} not installed."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Cookies saved using browser: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "Cookie file saved for user {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "Cookie file exists, has correct format, and YouTube cookies are working."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Cookie file exists and has correct format, but YouTube cookies are expired."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Cookie file exists and has correct format."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Cookie file exists but has incorrect format."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Cookie file not found."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{service} cookie URL is empty for user {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} cookie URL is not .txt (hidden)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} cookie file too large: {size} bytes (source hidden)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{service} cookie file downloaded for user {user_id} (source hidden)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Script not found: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Failed to send initial status message"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Error running {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Firebase cache reloaded by auto task."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Firebase cache reloaded by admin."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Error reloading Firebase cache: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Broadcast initiated. Text:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Broadcast message sent to all users."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Failed to broadcast message: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Admin {user_id} cleared cache for URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Admin {user_id} started porn list update script: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Porn list update script completed successfully by admin {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Porn list update script failed by admin {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Admin {user_id} tried to run non-existent script: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Error running porn update script by admin {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Admin {user_id} started porn cache reload"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Error reloading porn cache by admin {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Admin {user_id} checked URL for NSFW: {url} - Result: {status}"
    
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
    LINK_EXTRACTED_LOG_MSG = "Direct link extracted for user {user_id} from {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Failed to extract direct link for user {user_id} from {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Error in link command for user {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "User {user_id} set keyboard to {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "User {user_id} set keyboard to {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo set via command: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "User opened /mediainfo menu."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: closed."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo enabled."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo disabled."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Split size set to {size} bytes via argument."
    SPLIT_MENU_OPENED_LOG_MSG = "User opened /split menu."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Split selection closed."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Split size set to {size} bytes."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Proxy set via command: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "User opened /proxy menu."
    PROXY_MENU_CLOSED_LOG_MSG = "Proxy: closed."
    PROXY_ENABLED_LOG_MSG = "Proxy enabled."
    PROXY_DISABLED_LOG_MSG = "Proxy disabled."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Help message closed."
    AUDIO_HELP_SHOWN_LOG_MSG = "Showed /audio help"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "User requested playlist help."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Playlist help closed."
    AUDIO_HINT_CLOSED_LOG_MSG = "Audio hint closed."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Direct link menu created via LINK button for user {user_id} from {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Failed to extract direct link via LINK button for user {user_id} from {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "LIST command executed for user {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Quick Embed: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Always Ask menu sent for {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Created cached qualities menu for user {user_id} after error: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Always Ask menu error for {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Format is fixed via /args settings"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Audio"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Video"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Video"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Next ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Prev"
    SUBTITLES_NEXT_BUTTON_MSG = "Next ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ All text fields are empty"
    SENDER_VIDEO_DURATION_MSG = "Video duration:"
    SENDER_UPLOADING_FILE_MSG = "📤 Uploading file..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Uploading Video..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Video duration:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 file uploaded."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Video Info"
    DOWN_UP_NUMBER_MSG = "Number"
    DOWN_UP_TITLE_MSG = "Title"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Downloaded video."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Processing for upload..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Splitted part {part} file uploaded"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Upload complete"
    DOWN_UP_FILES_UPLOADED_MSG = "files uploaded"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Close"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBS"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 SUBS"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Browser"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Getting direct link..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Getting available formats..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Getting video description..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Error getting description: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Video description is not available"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Error sending description: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Video description sent to user {user_id} for {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Starting gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Duration:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Browser:</b> Open in web browser"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Available formats for"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 How to use format IDs:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "After getting the list, use specific format ID:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - download format 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - same as above"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - download format 140 as MP3 audio"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Audio-only formats detected"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "These formats will be downloaded as MP3 audio files."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>How to set format:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Download specific format ID"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Download by quality"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Download best quality"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Always ask for quality"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Audio-only formats:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Download format 140 as MP3 audio"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "These will be downloaded as MP3 audio files."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Use format ID from the list above"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Error: Original message not found."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Formats page"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Error showing formats menu"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Error getting formats"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Error getting available formats."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Please try again later."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp cannot process this content"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "The system recommends using gallery-dl instead."
    ALWAYS_ASK_OPTIONS_MSG = "**Options:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• For image galleries: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• For single images: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl often works better for Instagram, Twitter, and other social media content."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Try Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Format fixed via /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Subtitles"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Dubbed audio"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Subtitles are available"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Choose subtitle language"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Subs not found & won't embed"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Instant repost from cache"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Choose audio language"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW is paid (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Choose download quality"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Download image (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Get direct link to video"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Show available formats list"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Change video ext/codec"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Embed"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Extract only audio"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW is paid (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Instant repost from cache"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Choose audio language"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Best"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Other"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝sub only"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Smart grouping"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Added action button row (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Added action button rows (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Added bottom buttons to existing row"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Created new bottom row"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "No videos found in playlist"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "Unsupported URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "No video could be found"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "No video found"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "No media found"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "This tweet does not contain"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Error retrieving video information:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Error retrieving video information"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Try the <code>/clean</code> command and try again. If the error persists, YouTube requires authorization. Update cookies.txt via <code>/cookie</code> or <code>/cookies_from_browser</code> and try again."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Menu closed."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Manual Quality Selection"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Choose quality manually since automatic detection failed:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 All Available Formats"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Available Qualities (from cache)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Using cached qualities - new formats may not be available"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Downloading format"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Downloading"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Downloading with progress tracking..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Downloading using format:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Downloading audio using format:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Downloading best quality..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Downloading database dump..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Downloading"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Formats page"
    ALWAYS_ASK_FROM_CACHE_MSG = "(from cache)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Error: Original message not found. It might have been deleted. Please send the link again."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Error: Original URL not found. Please send the link again."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Title:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Duration:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Failed to get stream links"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Direct link extracted via Always Ask menu for user {user_id} from {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Failed to extract direct link via Always Ask menu for user {user_id} from {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Direct link extracted via down_and_up_with_format for user {user_id} from {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Failed to extract direct link via down_and_up_with_format for user {user_id} from {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Direct link extracted via down_and_audio for user {user_id} from {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Failed to extract direct link via down_and_audio for user {user_id} from {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Audio sent from cache."
    AUDIO_PROCESSING_MSG = "🎙️ Audio is processing..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Downloading audio:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Error occurred during audio download."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Failed to extract audio information"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Skipping unsupported file type in playlist at index {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "Audio file not found after download."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Uploading audio file...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Failed to send audio: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Playlist audio sent: {sent}/{total} files (quality={quality}) to user{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Failed to download audio: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Download cancelled due to timeout (2 hours)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Video file not found: {filename}"
    VIDEO_PROCESSING_ERROR_MSG = "❌ Error processing video: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Error sending description file: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 if you want to change video caption - reply to video with new text</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "No subtitles detected"
    VIDEO_PROGRESS_MSG = "<b>Video:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Audio:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL limit exceeded: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Processing completed"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Playlist ranges are not allowed in multiple URL mode. Send only single URLs without ranges (*1*5, /vid 1-10, etc.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Check <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>here</a> if your site supported"
    ERROR_COOKIE_NEEDED_MSG = "You may need <code>cookie</code> for downloading this video. First, clean your workspace via <b>/clean</b> command"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "For Youtube - get <code>cookie</code> via <b>/cookie</b> command. For any other supported site - send your own cookie (<a href='https://t.me/tg_ytdlp/203'>guide1</a>) (<a href='https://t.me/tg_ytdlp/214'>guide2</a>) and after that send your video link again."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Choose subtitle language"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "No alternative audio languages"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Choose audio language"
    PAGE_NUMBER_MSG = "Page {page}"
    TOTAL_PROGRESS_MSG = "Total Progress"
    SUBTITLE_MENU_CLOSED_MSG = "Subtitle menu closed."
    SUBTITLE_LANGUAGE_SET_MSG = "Subtitle language set: {value}"
    AUDIO_SET_MSG = "Audio set: {value}"
    FILTERS_UPDATED_MSG = "Filters updated"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Back"
    CLOSE_BUTTON_TEXT = "🔚Close"
    LIST_BUTTON_TEXT = "📃List"
    IMAGE_BUTTON_TEXT = "🖼Image"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Qualities not auto-detected\nUse 'Other' button to see all available formats.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Live Stream Detected**\n\nDownloading of ongoing or infinite live streams is not allowed.\n\nPlease wait for the stream to end and try downloading again when:\n• The stream duration is known\n• The stream has finished\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Live Stream Download</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Chunk {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Max size: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Total duration: {duration} sec"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Live Stream - Chunk {chunk}</b>\n⏱ Duration: {duration} sec\n📦 Size: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Chunk {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Live Stream Download Complete</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "Downloaded {chunks} chunk(s)"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Total duration: {duration} sec"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Live Stream Download Stopped</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "User directory was deleted (probably by /clean command)"
    LIVE_STREAM_FILE_DELETED_MSG = "Chunk file was deleted (probably by /clean command)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Stream has ended"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Please select a different format using `/format` command."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Title:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **File Processing Error**\n\nThe video was downloaded but couldn't be processed due to invalid characters in the filename.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **File Processing Error**\n\nThe video was downloaded but couldn't be processed due to an invalid argument error.\n\n"
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Format Not Available**\n\nThe requested video format is not available for this video.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Format ID {format_id} not found for this video.\n\nAvailable format IDs: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **AV1 format is not available for this video.**\n\n**Available formats:**\n{formats_text}\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "User entered forbidden content. Cannot be downloaded."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "NSFW blur set via command: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "User opened /nsfw menu."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: closed."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Failed to download {service} cookie: status={status} (url hidden)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Error downloading {service} cookie: {error} (url hidden)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Unexpected error while downloading {service} cookie (url hidden): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Cookie file updated for user {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Invalid cookie content provided by user {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "YouTube cookie URLs are empty for user {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "YouTube cookies downloaded and validated for user {user_id} from source {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "All YouTube cookie sources failed for user {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Error in check_porn command by admin {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Split part size set to {size} bytes."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Video upload completed with file splitting."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Playlist videos sent: {sent}/{total} files (quality={quality}) to user {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Unknown error: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Skipping unsupported file type in playlist at index {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg not found. Please install FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Conversion to MP4 failed: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Embedding subtitles may take a long time (up to 1 min per 1 min of video)!\n🔥 Starting to burn subtitles..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Subtitles cannot be embedded due to limits (quality/duration/size)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Subtitles are not available for the selected language"
    ERROR_SENDING_VIDEO_MSG = "❌ Error sending video: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Playlist videos sent: {sent}/{total} files."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Download cancelled due to timeout (2 hours)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Failed to download video: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Error: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON must be an object (dictionary)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Invalid JSON format. Please provide valid JSON."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Value must be between {min_val} and {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} set to: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ True"
    ARGS_FALSE_BUTTON_MSG = "❌ False"
    ARGS_BACK_BUTTON_MSG = "🔙 Back"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Close"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ True"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ False"
    ARGS_NOT_SET_MSG = "Not set"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ AV1 format is not available for this video.\n\nAvailable formats:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Error downloading: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ No videos found in playlist at index {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Video Conversion Failed**\n\nThe video couldn't be converted to MP4 due to an invalid argument error.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Video Conversion Failed**\n\nThe video couldn't be converted to MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Failed to get stream links"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ No content found at index {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Error: Original message not found."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Error: URL not found."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ This URL cannot be embedded."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} codec not available for this video"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} format not available for this video"
    
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
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Check Cookie"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ ON"
    PROXY_OFF_BUTTON_MSG = "❌ OFF"
    PROXY_CLOSE_BUTTON_MSG = "🔚Close"
    
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ ON"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ OFF"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Close"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ ON (No Blur)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ON (No Blur)"
    NSFW_OFF_BLUR_MSG = "✅ OFF (Blur)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ OFF (Blur)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Clean"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Error processing reply message for user {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Error sending broadcast to user {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Logs of {bot_name}\nUser: {user_id}\nTotal logs: {total}\nCurrent time: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nTotal {path}: {count}\nCurrent time: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Total Users: {count}</i>\nLast 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Porn caches reloaded by admin {admin_id}. Domains: {domains}, Keywords: {keywords}, Sites: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Error sending timeout message: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>انتخاب زبان</b>"
    LANG_CHANGED_MSG = "✅ زبان به {lang_name} تغییر یافت"
    LANG_ERROR_MSG = "❌ خطا در تغییر زبان"
    LANG_CLOSED_MSG = "انتخاب زبان بسته شد"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] callback: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Adding browser monitoring button with URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "Browser monitoring URL not configured: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Keyboard setting updated!**\n\nNew setting: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Failed to hide keyboard: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Using working YouTube cookies for link extraction for user {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "No working YouTube cookies available for link extraction for user {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Using existing YouTube cookies for link extraction for user {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "No YouTube cookies found for link extraction for user {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Copied global cookie file to user {user_id} folder for link extraction"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] User {user_id} requested mediainfo command"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] User {user_id} is admin: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] User {user_id} is in channel: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] User {user_id} access denied - not admin and not in channel"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] User {user_id} access granted"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ This command is only available for administrators."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Download finished with PO token support"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood limit. Try later."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST token refresh error: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Error closing Firebase session: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Error initializing base db structure: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Not all parameters are set in config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL is not set"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey is not set for getting idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Error downloading Firebase dump: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Failed to download Firebase dump via REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Error in _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Error running auto reload_cache (attempt {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ All retry attempts failed"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Starting Firebase dump download at {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Dependency not available: requests or Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ Database is empty"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Error closing logger: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Error during cleanup: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Clone error: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Clone timeout"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Clone exception: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Update canceled by user"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Repository cloned successfully"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Backups moved to _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ All modules are loaded"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Cleanup completed on exit"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Received signal {signal}, shutting down gracefully..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Please wait..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Downloading HLS stream:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "waiting for fragments"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Backup {ts} not found in _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Failed to restore {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Restored: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Details:</b> {error_details}\n\nDownload stopped due to critical error.\n\n💡 <b>Tip:</b> If you're getting 401 Unauthorized error, try using <code>/cookie instagram</code> command or send your own cookies to authenticate with Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domain in porn blacklist: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Found porn keywords: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domain in whitelist: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Found whitelist keywords: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ No porn keywords found"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API error at index {index}, skipping to next audio..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API error at index {index}, skipping to next video..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "User entered a <b>url</b>\n <b>user's name:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>User entered like this:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Join Channel"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Registering handler: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Download my 5 cookies"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Get browser's YT-cookie"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Validate your cookie file"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Upload custom cookie"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Close"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Available formats for: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Close"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Close"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Close"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Close"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Help closed."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Closed"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "خطا رخ داد"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg not found in PATH or project directory. Please install FFmpeg."
    YTDLP_NOT_FOUND_MSG = "yt-dlp binary not found in PATH or project directory. Please install yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Video will be split into {rounds} parts, which may be excessive"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Splitting video part {current}/{total}: {start_time:.2f}s to {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Failed to create split part {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Successfully created split part {part}: {target_name} ({size} bytes)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Error splitting video part {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Video split into {count} parts successfully"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Error in video splitting process: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Error while processing video {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Video file does not exist: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Error parsing dimensions '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Could not determine video dimensions from '{size_result}', using default: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Error creating thumbnail: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Error parsing video duration: {error}, result was: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Thumbnail not created at {thumb_dir}, using default"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Command execution error: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Error creating thumbnail with FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Skipping non-dict config section: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Setting {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Using user cookies: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Using YouTube cookies for user {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Copied global cookie file to user {user_id} folder"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Using copied global cookies as user cookies: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Failed to copy global cookie file for user {user_id}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Using --no-cookies for domain: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy requested but failed to import/get config: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Force using proxy for gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy requested but proxy configuration is incomplete"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Proxy helper failed: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Parsing extractor items..."
    GALLERY_DL_ITEM_COUNT_MSG = "Item {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Found metadata (tag 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "Found URL (tag 3): {url}, metadata: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Found metadata (legacy): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "Found URL (legacy): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Found filename: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Found directory: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Found extension: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Parsed {count} items, info: {info}, fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Setting gallery-dl config: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Trying Strategy A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor module not found"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() not available in this build"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Calling extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "No extractor matched the URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Setting cookies on extractor: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Failed to set cookies on extractor: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Extractor found, calling items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Strategy A succeeded, got info: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Strategy A: extractor.items() returned no valid info"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Strategy A (extractor.find) failed: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Fallback metadata from --get-urls: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "All strategies failed to obtain metadata"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Failed to extract image info: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job module not found (broken install?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob not available in this build"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Searching for downloaded files in gallery-dl directory"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Trying to find files by names from extractor"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Error reading user args for {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Error while processing video{video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "User {user_id} has send_as_file enabled, sending as document"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video timed out repeatedly; falling back to send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Caption too long, trying with minimal caption"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (minimal caption) timed out; fallback to send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Error sending video with minimal caption: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Error sending full description file: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Error removing temporary description file: {error}"
    
    # YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Skipping match_filter for domain in NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Checking existing YouTube cookies on user's URL for format detection for user {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Existing YouTube cookies work on user's URL for format detection for user {user_id} - using them"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Existing YouTube cookies failed on user's URL, trying to get new ones for format detection for user {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Trying YouTube cookie source {i} for format detection for user {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "YouTube cookies from source {i} work on user's URL for format detection for user {user_id} - saved to user folder"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "YouTube cookies from source {i} don't work on user's URL for format detection for user {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Failed to download YouTube cookies from source {i} for format detection for user {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "All YouTube cookie sources failed for format detection for user {user_id}, will try without cookies"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "No YouTube cookie sources configured for format detection for user {user_id}, will try without cookies"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "No YouTube cookies found for format detection for user {user_id}, attempting to get new ones"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Using YouTube cookies for format detection for user {user_id} (already validated in Always Ask menu)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "No YouTube cookies found for format detection for user {user_id}, attempting to restore..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Copied global cookie file to user {user_id} folder for format detection"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Failed to copy global cookie file for user {user_id}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Using --no-cookies for domain in get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "App not initialized yet. Cannot access {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Caption:</b> <code>{caption}</code>\n<b>User id:</b> <code>{user_id}</code>\n<b>User first name:</b> <code>{users_name}</code>\n<b>Video file id:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Error in caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Unexpected error in caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 Video URL</a>{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL отсутствует в конфигурации"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin initialized"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken refreshed"
    DB_LOG_FOR_USER_ADDED_MSG = "Log for user added"
    DB_DATABASE_CREATED_MSG = "db created"
    DB_BOT_STARTED_MSG = "Bot started"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY persisted to config.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Playlist part already cached: {path_parts}, skipping"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: no cache found for any URL/quality variant, returning empty dict"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: fast count for large range: {cached_count} cached videos"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: no cache found for hash {url_hash}, quality {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: no cache found for any URL variant, returning None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Access denied. Admin only."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Auto Firebase cache reloading updated!\n\n📊 Status: {status}\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Invalid argument. Use /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Interval must be between 1 and 168 hours"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Failed to set interval"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Auto Firebase cache interval updated!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Auto Firebase cache reloading started!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Auto reload ENABLED; next at {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Auto reload DISABLED by admin."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Auto reload interval set to {interval}h; next at {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Auto reload started; next at {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Auto reload stopped by admin."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase cache loaded: {count} root nodes"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Firebase cache file not found, starting with empty cache: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Failed to load firebase cache: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase cache reloaded: {count} root nodes"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Firebase cache file not found: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Failed to reload firebase cache: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = "🚫 You are banned from the bot!"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ No video formats found. Trying image downloader…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram has limited message sending.\n⏳ Please wait: {time_str}\nTo update timer send URL again 2 times."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Click button to copy stream URL, then paste it in VLC app</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Click button to copy stream URL, then paste it in VLC app</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Error sending formats file: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Failed to get formats:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Analyzing... (wait 6 sec)"
    AA_PROCESSING_MSG = "🔎 Analyzing..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{wrong} contains forbidden characters. Only letters, digits and _ are allowed.\nPlease use: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Для работы в группе боту нужны права администратора. Пожалуйста, сделайте бота админом этой группы."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Hello {first_name},\n \n<i>This bot🤖 can download any videos into telegram directly.😊 For more information press <b>/help</b></i> 👈\n\n<blockquote>P.S. Downloading 🔞NSFW content and files from ☁️Cloud Storage is paid! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Do not leave the channel - you will be banned from using the bot ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 No files to remove."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 All files removed successfully!\n\nRemoved files:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ WAIT UNTIL YOUR PREVIOUS DOWNLOAD IS FINISHED"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "App instance is None in check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict is None, allowing download"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict is None, allowing subtitle embedding"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: checking limits - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: info_dict keys: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Subtitle embedding skipped: duration {duration}s exceeds limit {max_duration}s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Subtitle embedding skipped: size {size_mb:.2f}MB exceeds limit {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Subtitle embedding skipped: quality {width}x{height} (min side {min_side}p) exceeds limit {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "playlist"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Range limit exceeded for {service}: {count} (maximum {max_count}).\n\nUse one of these commands to download maximum available files:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Range limit exceeded for {service}: {count} (maximum {max_count})\nUser ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "PO token provider disabled in config"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} is not a YouTube domain, skipping PO token"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO token provider is not available at {base_url}, falling back to standard YouTube extraction"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO token provider cache cleared, will check availability on next request"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "App instance not available yet"
    HELPER_USER_NAME_MSG = "User"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood wait detected, sleeping for {wait_seconds} seconds"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood wait detected but couldn't extract time, sleeping for {retry_delay} seconds"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno error detected, sleeping for {retry_delay} seconds"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy configuration incomplete, using direct connection"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Close"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Close"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Close"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Logs file removed."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Tags file removed."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Format file removed."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Split file removed."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Mediainfo file removed."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Subtitle settings removed."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Keyboard settings removed."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Args settings removed."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 NSFW settings removed."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Proxy settings removed."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Flood wait settings removed."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Close"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Video Download Command"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Usage: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "مثال‌ها:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (direct order)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (reverse order)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "همچنین ببینید: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "User {user_id} closed add_bot_to_group command"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Failed to extract YouTube ID"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Failed to download thumbnail or it is too big"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Choose audio language"
    AA_NO_SUBTITLES_DETECTED_MSG = "No subtitles detected"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Choose subtitle language"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Authentication Error"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Account Not Found"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Account Unavailable"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Rate Limit Exceeded"
    GALLERY_DL_NETWORK_ERROR_MSG = "Network Error"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Content Unavailable"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Geographic Restrictions"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Verification Required"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Policy Violation"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Unknown Error"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Download started</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Close"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Video Download Command</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Usage: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Examples:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Also see: /audio, /img, /help, /playlist, /settings"
    
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
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Cookie file removed and cache cleared."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Prev"
    SUBS_BACK_BUTTON_MSG = "🔙Back"
    SUBS_OFF_BUTTON_MSG = "🚫 OFF"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - set language"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - set language with AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Valid options:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 LANGUAGE"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 CLEAN"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIES"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MEDIA"
    SETTINGS_INFO_BUTTON_MSG = "📖 INFO"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ MORE"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Cookies only"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Logs "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Tags"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Format"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Split"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Subtitles"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Keyboard"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Args"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Proxy"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Flood wait"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  All files"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Download my 5 cookies"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Get browser's YT-cookie"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Validate your cookie file"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Upload custom cookie"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Change quality & format"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Turn ON / OFF MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Change split video part size"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Download video as audio"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Subtitles language settings"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - How to download playlists"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Download images via gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Send your #tags"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Get instructions"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage -Send your logs"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Playlist's help"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - howto"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Get direct video links"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Enable/disable proxy"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Keyboard layout"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Inline search helper"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp arguments"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - NSFW blur settings"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Clean Options</b>\n\nChoose what to clean:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: Activate @vid search"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: Activate @vid search"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 OFF"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 FULL"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[Images URL]({url})"
    IMAGE_ERROR_MSG = "❌ Error: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Back"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - custom format"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p quality"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K quality"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K quality"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - specific format ID"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - always show menu"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/best quality"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Always Ask (menu + buttons)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Others (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (best for PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (best for mobile Telegram)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (MAX quality)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Custom (enter your own)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 From Browser"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Your Own"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Input mode automatically closed due to inactivity (5 minutes)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Reset All"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 View Current"
    ARGS_BACK_BUTTON_MSG = "🔙 Back"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Forward this message to your favorites to save these settings as a template.</i> \n\n<i>Forward this message back here to apply these settings.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Current yt-dlp Arguments:\n\nNo custom settings configured.\n\n---\n\n<i>Forward this message to your favorites to save these settings as a template.</i> \n\n<i>Forward this message back here to apply these settings.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Current yt-dlp Arguments:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Export Settings"
    ARGS_SETTINGS_READY_MSG = "Settings ready for export! Forward this message to favorites to save."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Current yt-dlp Arguments:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Failed to recognize settings in message. Make sure you sent a correct settings template."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Settings successfully imported!\n\nApplied parameters: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Key settings:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Error saving imported settings."
    ARGS_ERROR_IMPORTING_MSG = "❌ An error occurred while importing settings."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Download Cookie Files</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Choose a service to download the cookie file."
    COOKIE_MENU_SAVE_INFO_MSG = "Cookie files will be saved as cookie.txt in your folder."
    COOKIE_MENU_TIP_HEADER_MSG = "Tip: You can also use direct command:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – download and validate cookies"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – use a specific source by index (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Then verify with <code>/check_cookie</code> (tests on RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Always Ask"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Link"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Watch"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Caption"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Partially completed - {successful_uploads}/{total_files} audio files uploaded."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Audio successfully downloaded and sent - {total_files} files uploaded."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Private TikTok Account</b>\n\n"
        "This TikTok account is private or all videos are private.\n\n"
        "<b>💡 Solution:</b>\n"
        "1. Follow the account @{username}\n"
        "2. Send your cookies to the bot using <code>/cookie</code> command\n"
        "3. Try again\n\n"
        "<b>After updating cookies, try again!</b>"
    )

    #######################################################
