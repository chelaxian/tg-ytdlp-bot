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
    CREDITS_MSG = "<blockquote><i>يديره</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 تغيير اللغة: /lang</b>"
    TO_USE_MSG = "<i>لاستخدام هذا البوت تحتاج إلى الاشتراك في قناة تليجرام @tg_ytdlp.</i>\nبعد انضمامك إلى القناة، <b>أعد إرسال رابط الفيديو مرة أخرى وسيقوم البوت بتحميله لك</b> ❤️\n\n<blockquote>P.S. بسبب المحتوى 🔞NSFW المحتمل - التحميل من ☁️<b>التخزين السحابي</b> و📁<b>مشاركة الملفات</b> و🔗<b>مختصري الروابط</b> و🔞<b>مواقع إباحية</b> مدفوع! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ لا 🗑<b>تحذف/تلغي الاشتراك في قناة @tg_ytdlp</b> ولا 🤖<b>ترسل روابط/أوامر بشكل مفرط للبوت</b> - سيتم حظرك تلقائياً من استخدام البوت ⛔️</blockquote>"

    ERROR1 = "لم يتم العثور على رابط URL. يرجى إدخال رابط يحتوي على <b>https://</b> أو <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>قوائم التشغيل (yt-dlp)</b>

لتحميل قوائم التشغيل أرسل رابطها مع نطاقات <code>*البداية*النهاية</code> في النهاية. على سبيل المثال: <code>URL*1*5</code> (أول 5 مقاطع فيديو من 1 إلى 5 شاملاً). <code>URL*-1*-5</code> (آخر 5 مقاطع فيديو من 1 إلى 5 شاملاً).
أو يمكنك استخدام <code>/vid من-إلى URL</code>. على سبيل المثال: <code>/vid 3-7 URL</code> (يحمل مقاطع الفيديو من 3 إلى 7 شاملاً من البداية). <code>/vid -3-7 URL</code> (يحمل مقاطع الفيديو من 3 إلى 7 شاملاً من النهاية). يعمل أيضًا مع أمر <code>/audio</code>.

<b>أمثلة:</b>

🟥 <b>نطاق فيديو من قائمة تشغيل يوتيوب:</b> (يحتاج 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(يحمل مقاطع الفيديو من 1 إلى 5 شاملاً)
🟥 <b>فيديو واحد من قائمة تشغيل يوتيوب:</b> (يحتاج 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(يحمل الفيديو الثالث فقط)

⬛️ <b>ملف TikTok الشخصي:</b> (يحتاج 🍪 الخاص بك)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(يحمل أول 10 مقاطع فيديو من الملف الشخصي)

🟪 <b>قصص Instagram:</b> (يحتاج 🍪 الخاص بك)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(يحمل أول 3 قصص)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(يحمل أول 10 قصص من الألبوم)

🟦 <b>مقاطع فيديو VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(يحمل أول 3 مقاطع فيديو من الملف الشخصي/المجموعة)

⬛️<b>قنوات Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(يحمل مقاطع الفيديو من 2 إلى 4 شاملاً من القناة)

🟪 <b>مقاطع Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(يحمل أول 3 مقاطع من القناة)

🟦 <b>مجموعات Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(يحمل أول مقطعي فيديو من المجموعة)

🟧 <b>نماذج Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(يحمل أول مقطعي فيديو من ملف النموذج)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(يحمل أول 3 مقاطع فيديو من نتائج البحث بكلماتك)

وهكذا...
انظر <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">قائمة المواقع المدعومة</a>
</blockquote>

<blockquote expandable>🖼 <b>الصور (gallery-dl)</b>

استخدم <code>/img URL</code> لتحميل الصور/الألبومات من العديد من المنصات.

<b>أمثلة:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>النطاقات:</b>
<code>/img 11-20 https://example.com/album</code> — العناصر 11..20
<code>/img 11- https://example.com/album</code> — من 11 إلى النهاية (أو حد البوت)

<i>المنصات المدعومة تشمل vk، 2ch، 35photo، 4chan، 500px، ArtStation، Boosty، Civitai، Cyberdrop، DeviantArt، Discord، Facebook، Fansly، Instagram، Pinterest، Reddit، TikTok، Tumblr، Twitter/X، JoyReactor، إلخ. القائمة الكاملة:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">مواقع gallery-dl المدعومة</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>بوت تحميل الفيديو - المساعدة</b>

📥 <b>الاستخدام الأساسي:</b>
• أرسل أي رابط → البوت يحمله
  <i>البوت يحاول تلقائياً تحميل مقاطع الفيديو عبر yt-dlp والصور عبر gallery-dl.</i>
• <b>روابط متعددة:</b> في وضع اختيار الجودة (<code>/format</code>) يمكنك إرسال حتى <b>10 روابط</b> في رسالة واحدة . كل رابط في سطر جديد أو مفصول بمسافات.
• <code>/audio URL</code> → استخراج الصوت
• <code>/link [جودة] URL</code> → الحصول على روابط مباشرة
• <code>/proxy</code> → تفعيل/إلغاء البروكسي لجميع التحميلات
• أجب على الفيديو بنص → تغيير التسمية التوضيحية

📋 <b>قوائم التشغيل والنطاقات:</b>
• <code>URL*1*5</code> → تحميل أول 5 مقاطع فيديو
• <code>URL*-1*-5</code> → تحميل آخر 5 مقاطع فيديو
• <code>/vid 3-7 URL</code> → يصبح <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → يصبح <code>URL*-3*-7</code>

🍪 <b>ملفات تعريف الارتباط والخاص:</b>
• ارفع ملف تعريف الارتباط *.txt للفيديوهات الخاصة
• <code>/cookie [خدمة]</code> → تحميل ملفات تعريف الارتباط (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → اختر المصدر بالرقم (1–N)
• <code>/cookies_from_browser</code> → استخراج من المتصفح
• <code>/check_cookie</code> → التحقق من ملف تعريف الارتباط
• <code>/save_as_cookie</code> → حفظ النص كملف تعريف ارتباط

🧹 <b>التنظيف:</b>
• <code>/clean</code> → ملفات الوسائط فقط
• <code>/clean all</code> → كل شيء
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>الإعدادات:</b>
• <code>/settings</code> → قائمة الإعدادات
• <code>/format</code> → الجودة والتنسيق
• <code>/split</code> → تقسيم الفيديو إلى أجزاء
• <code>/mediainfo on/off</code> → معلومات الوسائط
• <code>/nsfw on/off</code> → ضبابية المحتوى غير المناسب
• <code>/tags</code> → عرض العلامات المحفوظة
• <code>/sub on/off</code> → الترجمات
• <code>/keyboard</code> → لوحة المفاتيح (OFF/1x3/2x3)

🏷️ <b>العلامات:</b>
• أضف <code>#tag1#tag2</code> بعد الرابط
• تظهر العلامات في التسميات التوضيحية
• <code>/tags</code> → عرض جميع العلامات

🔗 <b>الروابط المباشرة:</b>
• <code>/link URL</code> → أفضل جودة
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → جودة محددة

⚙️ <b>الأوامر السريعة:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → تعيين الجودة
• <code>/keyboard off/1x3/2x3/full</code> → تخطيط لوحة المفاتيح
• <code>/split 100mb-2000mb</code> → تغيير حجم الجزء
• <code>/subs off/ru/en auto</code> → لغة الترجمات
• <code>/list URL</code> → قائمة التنسيقات المتاحة
• <code>/mediainfo on/off</code> → تشغيل/إيقاف معلومات الوسائط
• <code>/proxy on/off</code> → تفعيل/إلغاء البروكسي لجميع التحميلات

📊 <b>المعلومات:</b>
• <code>/usage</code> → تاريخ التحميل
• <code>/search</code> → البحث المضمن عبر @vid

🖼 <b>الصور:</b>
• <code>URL</code> → تحميل صور من الرابط
• <code>/img URL</code> → تحميل صور من الرابط
• <code>/img 11-20 URL</code> → تحميل نطاق محدد
• <code>/img 11- URL</code> → تحميل من 11 إلى النهاية

👨‍💻 <i>Developer:</i> @upekshaip
🤝 <i>Contributor:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "فقط احفظ ملف تعريف الارتباط كـ <b><u>cookie.txt</u></b> وأرسله للبوت كوثيقة.\n\n"
        "يمكنك أيضًا إرسال ملفات تعريف الارتباط كنص عادي باستخدام أمر <b><u>/save_as_cookie</u></b>.\n"
        "<b>استخدام <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>التعليمات:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (Arabic)
    SEARCH_MSG = """
🔍 <b>البحث عن الفيديو</b>

اضغط على الزر أدناه لتفعيل البحث المضمن عبر @vid.

<blockquote>على الكمبيوتر فقط اكتب <b>"@vid استعلام_البحث_الخاص_بك"</b> في أي محادثة.</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 أمر تحميل الصور</b>\n\n"
        "الاستخدام: <code>/img URL</code>\n\n"
        "<b>أمثلة:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>المنصات المدعومة (أمثلة):</b>\n"
        "<blockquote>vk، 2ch، 35photo، 4chan، 500px، ArtStation، Boosty، Civitai، Cyberdrop، DeviantArt، Discord، Facebook، Fansly، Instagram، Patreon، Pinterest، Reddit، TikTok، Tumblr، Twitter/X، JoyReactor، إلخ. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">القائمة الكاملة</a></blockquote>"
        "انظر أيضًا: "
    )
    
    LINK_HINT_MSG = (
        "الحصول على روابط فيديو مباشرة مع اختيار الجودة.\n\n"
        "الاستخدام: /link + URL \n\n"
        "(مثال: /link https://youtu.be/abc123)\n"
        "(مثال: /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>إضافة البوت إلى المجموعة</b>

أضف بوتاتي إلى مجموعاتك للحصول على ميزات محسنة وحدود أعلى!
————————————
📊 <b>الحدود المجانية الحالية (في رسائل البوت المباشرة):</b>
<blockquote>•🗑 فوضى من جميع الملفات غير المرتبة 👎
• الحد الأقصى لحجم ملف واحد: <b>8 جيجابايت</b>
• الحد الأقصى لجودة ملف واحد: <b>غير محدود</b>
• الحد الأقصى لمدة ملف واحد: <b>غير محدود</b>
• الحد الأقصى لعدد التحميلات: <b>غير محدود</b>
• الحد الأقصى للروابط في رسالة واحدة: <b>10</b> (فقط في وضع اختيار الجودة)
• الحد الأقصى لعناصر قائمة التشغيل في المرة الواحدة: <b>50</b>
• الحد الأقصى لمقاطع TikTok في المرة الواحدة: <b>500</b>
• الحد الأقصى للصور في المرة الواحدة: <b>1000</b>
• حدود معدل الروابط: <b>5/دقيقة، 60/ساعة، 1000/يوم</b>
• حد الأوامر: <b>20/دقيقة</b>
• الحد الأقصى لوقت التحميل الواحد: <b>ساعتان</b>
• 🔞 المحتوى غير المناسب مدفوع! 1⭐️ = $0.02
• 🆓 جميع الوسائط الأخرى مجانية تمامًا
• 📝 جميع سجلات المحتوى والتخزين المؤقت في قنوات السجل الخاصة بي لإعادة النشر الفوري عند إعادة التحميل</blockquote>

💬<b>هذه الحدود فقط للفيديو مع الترجمات:</b>
<blockquote>• الحد الأقصى لمدة الفيديو+الترجمات: <b>1.5 ساعة</b>
• الحد الأقصى لحجم ملف الفيديو+الترجمات: <b>500 ميجابايت</b>
• الحد الأقصى لجودة الفيديو+الترجمات: <b>720p</b></blockquote>
————————————
🚀 <b>مزايا المجموعة المدفوعة (2️⃣x الحدود):</b>
<blockquote>•  🗂 خزنة وسائط منظمة مرتبة حسب المواضيع 👍
•  📁 البوتات ترد في الموضوع الذي تستدعيهم فيه
•  📌 تثبيت تلقائي لرسالة الحالة مع تقدم التحميل
•  🖼 أمر /img يحمل الوسائط كألبومات من 10 عناصر
• الحد الأقصى لحجم ملف واحد: <b>16 جيجابايت</b> ⬆️
• الحد الأقصى للروابط في رسالة واحدة: <b>20</b> ⬆️ (فقط في وضع اختيار الجودة)
• الحد الأقصى لعناصر قائمة التشغيل في المرة الواحدة: <b>100</b> ⬆️
• الحد الأقصى لمقاطع TikTok في المرة الواحدة: 1000 ⬆️
• الحد الأقصى للصور في المرة الواحدة: 2000 ⬆️
• حدود معدل الروابط: <b>10/دقيقة، 120/ساعة، 2000/يوم</b> ⬆️
• حد الأوامر: <b>40/دقيقة</b> ⬆️
• الحد الأقصى لوقت التحميل الواحد: <b>4 ساعات</b> ⬆️
• 🔞 المحتوى غير المناسب: مجاني مع البيانات الوصفية الكاملة 🆓
• 📢 لا حاجة للاشتراك في قناتي للمجموعات
• 👥 جميع أعضاء المجموعة سيكون لديهم إمكانية الوصول إلى الوظائف المدفوعة!
• 🗒 لا سجلات / لا تخزين مؤقت في قنوات السجل الخاصة بي! يمكنك رفض النسخ/إعادة النشر في إعدادات المجموعة</blockquote>

💬 <b>2️⃣x الحدود للفيديو مع الترجمات:</b>
<blockquote>• الحد الأقصى لمدة الفيديو+الترجمات: <b>3 ساعات</b> ⬆️
• الحد الأقصى لحجم ملف الفيديو+الترجمات: <b>1000 ميجابايت</b> ⬆️
• الحد الأقصى لجودة الفيديو+الترجمات: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>التسعير والإعداد:</b>
<blockquote>• السعر: <b>$5/شهر</b> لكل بوت واحد في المجموعة
• الإعداد: اتصل بـ @iilililiiillliiliililliilliliiil
• الدفع: 💎TON أو طرق أخرى💲
• الدعم: دعم فني كامل مشمول</blockquote>
————————————
يمكنك إضافة بوتاتي إلى مجموعتك لإلغاء حظر 🔞<b>المحتوى غير المناسب</b> المجاني ومضاعفة (x2️⃣) جميع الحدود.
اتصل بي إذا كنت تريد مني السماح لمجموعتك باستخدام بوتاتي @iilililiiillliiliililliilliliiil
————————————
💡<b>نصيحة:</b> <blockquote>يمكنك المساهمة بالمال مع أي عدد من أصدقائك (على سبيل المثال 100 شخص) وإجراء عملية شراء واحدة للمجموعة بأكملها - جميع أعضاء المجموعة سيكون لديهم وصول غير محدود كامل لجميع وظائف البوتات في تلك المجموعة مقابل <b>0.05$</b> فقط</blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>وضع المحتوى غير المناسب: مفعل✅</b>

• سيتم عرض المحتوى غير المناسب بدون ضبابية.
• لن تنطبق العوائق على وسائط المحتوى غير المناسب.
• سيكون المحتوى مرئيًا فورًا

<i>استخدم /nsfw off لتفعيل الضبابية</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>وضع المحتوى غير المناسب: معطل</b>

⚠️ <b>الضبابية مفعلة</b>
• سيتم إخفاء المحتوى غير المناسب تحت العوائق   
• للعرض، ستحتاج إلى النقر على الوسائط
• ستطبق العوائق على وسائط المحتوى غير المناسب.

<i>استخدم /nsfw on لإلغاء الضبابية</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>معامل غير صحيح</b>

استخدم:
• <code>/nsfw on</code> - إلغاء الضبابية
• <code>/nsfw off</code> - تفعيل الضبابية
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>فحص التخزين المؤقت...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 معالجة..."
    DOWNLOADING_MSG = "📥 <b>تحميل الوسائط...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>تحميل الصورة...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>اكتمل التحميل</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "تم التحميل:"
    SENT_STATUS_MSG = "تم الإرسال:"
    PENDING_TO_SEND_STATUS_MSG = "في انتظار الإرسال:"
    TITLE_LABEL_MSG = "العنوان:"
    MEDIA_COUNT_LABEL_MSG = "عدد الوسائط:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "اكتمل التنزيل، جاري معالجة الصوت..."
    VIDEO_PROCESSING_MSG = "📽 معالجة الفيديو..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>تم الإرسال من التخزين المؤقت</b>\n\nالألبومات المرسلة: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ تم إرسال الفيديو بنجاح من التخزين المؤقت."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ تم إرسال فيديوهات قائمة التشغيل من التخزين المؤقت ({cached}/{total} ملف)."
    CACHE_PARTIAL_MSG = "📥 تم إرسال {cached}/{total} فيديو من التخزين المؤقت، تحميل المفقود منها..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ تم الإرسال من التخزين المؤقت: {cached}\n🔄 متابعة التحميل..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 لا يمكن تحليل الوسائط، المتابعة بالنطاق المسموح الأقصى (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 لا يمكن تحديد عدد الوسائط، المتابعة بالنطاق المسموح الأقصى (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 لا يمكن تحديد العدد الإجمالي للوسائط، المتابعة بالنطاق المحدد {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>رابط غير صحيح</b>\n\nيرجى تقديم رابط صحيح يبدأ بـ http:// أو https://"

    ERROR_OCCURRED_MSG = "❌ <b>حدث خطأ</b>\n\n<code>{url}</code>\n\nالخطأ: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ خطأ في إرسال الفيديو: {error}"
    ERROR_UNKNOWN_MSG = "❌ خطأ غير معروف: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ مساحة القرص غير كافية لتحميل مقاطع الفيديو."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ حجم الملف يتجاوز الحد الأقصى {limit} جيجابايت. يرجى اختيار ملف أصغر ضمن الحجم المسموح."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>فشل تحميل الفيديو مع جميع البروكسيات المتاحة</b>\n\nفشلت جميع محاولات التحميل عبر البروكسيات.\nجرب:\n• التحقق من عمل البروكسي\n• تجربة بروكسي آخر من القائمة\n• التحميل بدون بروكسي (إن أمكن)"

    ERROR_GETTING_LINK_MSG = "❌ <b>خطأ في الحصول على الرابط:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ قام تليجرام بتقييد إرسال الرسائل.\n⏳ يرجى الانتظار: {time}\nلتحديث المؤقت أرسل الرابط مرة أخرى مرتين."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ قام تليجرام بتقييد إرسال الرسائل.\n⏳ يرجى الانتظار: \nلتحديث المؤقت أرسل الرابط مرة أخرى مرتين."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ فشل في تحميل الترجمات"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>روابط البث المباشر</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>العنوان:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>المدة:</b> {duration} ثانية\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ خطأ: لم يتم العثور على الرسالة الأصلية."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ العلامة #{tag} تحتوي على أحرف محظورة. يُسمح فقط بالأحرف والأرقام و _.\nيرجى استخدام: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ تم إرسال فيديوهات قائمة التشغيل: {sent}/{total} ملف."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>نصيحة حول قوائم التشغيل</b>

أرسلت رابط قائمة تشغيل دون تحديد نطاق. قام البوت تلقائياً بتنزيل الفيديو الأول (<code>*1*1</code>).

<b>لتنزيل عدة فيديوهات من قائمة التشغيل، حدد نطاقاً:</b>
• <code>URL*1*5</code> — أول 5 فيديوهات (من 1 إلى 5 شاملة)
• <code>URL*3*3</code> — الفيديو الثالث فقط
• <code>/vid 1-10 URL</code> — تنسيق بديل

اعرف المزيد: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ تم الإرسال من التخزين المؤقت: {cached}/{total} ملف."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ فشل في الحصول على روابط البث"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "اختر متصفحًا لتحميل ملفات تعريف الارتباط منه:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "لم يتم العثور على متصفحات في هذا النظام. يمكنك تحميل ملفات تعريف الارتباط من رابط بعيد أو مراقبة حالة المتصفح:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>فتح المتصفح</b> - لمراقبة حالة المتصفح في التطبيق المصغر"
    BROWSER_OPEN_BUTTON_MSG = "🌐 فتح المتصفح"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 تحميل من رابط بعيد"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ تم تحميل ملف تعريف ارتباط يوتيوب عبر الاحتياطي وحفظه كـ cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ لم يتم العثور على متصفحات مدعومة ولم يتم تكوين COOKIE_URL. استخدم /cookie أو ارفع cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ يجب أن يشير COOKIE_URL الاحتياطي إلى ملف .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ ملف تعريف الارتباط الاحتياطي كبير جدًا (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ مصدر ملف تعريف الارتباط الاحتياطي غير متاح (الحالة {status}). جرب /cookie أو ارفع cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ خطأ في تحميل ملف تعريف الارتباط الاحتياطي. جرب /cookie أو ارفع cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ خطأ غير متوقع أثناء تحميل ملف تعريف الارتباط الاحتياطي."
    BTN_CLOSE = "🔚إغلاق"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ قيمة منطقية غير صحيحة"
    ARGS_CLOSED_MSG = "مغلق"
    ARGS_ALL_RESET_MSG = "✅ تم إعادة تعيين جميع المعاملات"
    ARGS_RESET_ERROR_MSG = "❌ خطأ في إعادة تعيين المعاملات"
    ARGS_INVALID_PARAM_MSG = "❌ معامل غير صحيح"
    ARGS_BOOL_SET_MSG = "تم تعيينه إلى {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "مُعيّن بالفعل إلى {value}"
    ARGS_INVALID_SELECT_MSG = "❌ قيمة اختيار غير صحيحة"
    ARGS_VALUE_SET_MSG = "تم تعيينه إلى {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "مُعيّن بالفعل إلى {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>القيمة الحالية:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>أمثلة:</b>\n• <code>default</code> - استخدام استراتيجية XFF الافتراضية\n• <code>never</code> - عدم استخدام رأس XFF أبدًا\n• <code>US</code> - رمز دولة الولايات المتحدة\n• <code>GB</code> - رمز دولة المملكة المتحدة\n• <code>DE</code> - رمز دولة ألمانيا\n• <code>FR</code> - رمز دولة فرنسا\n• <code>JP</code> - رمز دولة اليابان\n• <code>192.168.1.0/24</code> - كتلة IP (CIDR)\n• <code>10.0.0.0/8</code> - نطاق IP خاص\n• <code>203.0.113.0/24</code> - كتلة IP عامة\n\n"
    ARGS_XFF_NOTE_MSG = "<b>ملاحظة:</b> هذا يحل محل خيارات --geo-bypass. استخدم أي رمز دولة من حرفين أو كتلة IP في تدوين CIDR.\n\n"
    ARGS_EXAMPLE_MSG = "<b>مثال:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "يرجى إرسال قيمتك الجديدة."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>النطاق:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "يرجى إرسال رقم."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>أمثلة:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>ملاحظة:</b> ستتم إضافة هذه الرؤوس إلى رؤوس Referer و User-Agent الموجودة.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 معاملات yt-dlp الحالية:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>منطقي</b> - مفاتيح صحيح/خطأ\n• 📋 <b>اختيار</b> - اختر من الخيارات\n• 🔢 <b>رقمي</b> - إدخال رقم\n• 📝🔧 <b>نص</b> - إدخال نص/JSON</blockquote>\n\nستتم تطبيق هذه الإعدادات على جميع تحميلاتك."
    
    # أسماء المعاملات المترجمة للعرض
    ARGS_PARAM_NAMES = {
        "force_ipv6": "فرض اتصالات IPv6",
        "force_ipv4": "فرض اتصالات IPv4", 
        "no_live_from_start": "عدم تحميل البث المباشر من البداية",
        "live_from_start": "تحميل البث المباشر من البداية",
        "no_check_certificates": "قمع التحقق من شهادة HTTPS",
        "check_certificate": "فحص شهادة SSL",
        "no_playlist": "تحميل فيديو واحد فقط، وليس قائمة التشغيل",
        "embed_metadata": "تضمين البيانات الوصفية في ملف الفيديو",
        "embed_thumbnail": "تضمين الصورة المصغرة في ملف الفيديو",
        "write_thumbnail": "كتابة الصورة المصغرة في ملف",
        "ignore_errors": "تجاهل أخطاء التحميل والمتابعة",
        "legacy_server_connect": "السماح باتصالات الخادم القديمة",
        "concurrent_fragments": "عدد الأجزاء المتزامنة للتحميل",
        "xff": "استراتيجية رأس X-Forwarded-For",
        "user_agent": "رأس User-Agent",
        "impersonate": "تقليد المتصفح",
        "referer": "رأس Referer",
        "geo_bypass": "تجاوز القيود الجغرافية",
        "hls_use_mpegts": "استخدام MPEG-TS لـ HLS",
        "no_part": "عدم استخدام ملفات .part",
        "no_continue": "عدم استئناف التحميلات الجزئية",
        "audio_format": "تنسيق الصوت",
        "video_format": "تنسيق الفيديو",
        "merge_output_format": "تنسيق دمج الإخراج",
        "send_as_file": "إرسال كملف",
        "username": "اسم المستخدم",
        "password": "كلمة المرور",
        "twofactor": "رمز المصادقة الثنائية",
        "min_filesize": "الحد الأدنى لحجم الملف (ميجابايت)",
        "max_filesize": "الحد الأقصى لحجم الملف (ميجابايت)",
        "playlist_items": "عناصر قائمة التشغيل",
        "date": "التاريخ",
        "datebefore": "التاريخ قبل",
        "dateafter": "التاريخ بعد",
        "http_headers": "رؤوس HTTP",
        "sleep_interval": "فاصل النوم",
        "max_sleep_interval": "الحد الأقصى لفاصل النوم",
        "retries": "عدد المحاولات",
        "http_chunk_size": "حجم جزء HTTP",
        "sleep_subtitles": "النوم للترجمات"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ تكوين معاملات yt-dlp</b>\n\n<blockquote>📋 <b>المجموعات:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ تكوين معاملات yt-dlp</b>\n\n"
        "<blockquote>📋 <b>المجموعات:</b>\n"
        "• ✅/❌ <b>منطقي</b> - مفاتيح صحيح/خطأ\n"
        "• 📋 <b>اختيار</b> - اختر من الخيارات\n"
        "• 🔢 <b>رقمي</b> - إدخال رقم\n"
        "• 📝🔧 <b>نص</b> - إدخال نص/JSON</blockquote>\n\n"
        "ستتم تطبيق هذه الإعدادات على جميع تحميلاتك."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ يرجى الانتظار..."
    ERROR_OCCURRED_SHORT_MSG = "❌ حدث خطأ"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ تم إغلاق وضع الإدخال تلقائياً بسبب عدم النشاط (5 دقائق)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ الإدخال يحتوي على محتوى قد يكون خطيراً: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ الإدخال طويل جداً (الحد الأقصى 1000 حرف)"
    ARGS_INVALID_URL_MSG = "❌ تنسيق URL غير صحيح. يجب أن يبدأ بـ http:// أو https://"
    ARGS_INVALID_JSON_MSG = "❌ تنسيق JSON غير صحيح"
    ARGS_NUMBER_RANGE_MSG = "❌ يجب أن يكون الرقم بين {min_val} و {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ تنسيق رقم غير صحيح"
    ARGS_DATE_FORMAT_MSG = "❌ يجب أن يكون التاريخ بتنسيق YYYYMMDD (مثال: 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ يجب أن تكون السنة بين 1900 و 2100"
    ARGS_MONTH_RANGE_MSG = "❌ يجب أن يكون الشهر بين 01 و 12"
    ARGS_DAY_RANGE_MSG = "❌ يجب أن يكون اليوم بين 01 و 31"
    ARGS_INVALID_DATE_MSG = "❌ تنسيق تاريخ غير صحيح"
    ARGS_INVALID_XFF_MSG = "❌ يجب أن يكون XFF 'default' أو 'never' أو رمز دولة (مثال: US) أو كتلة IP (مثال: 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "لم يتم تعيين معاملات مخصصة. جميع المعاملات تستخدم القيم الافتراضية."
    ARGS_RESET_SUCCESS_MSG = "✅ تم إعادة تعيين جميع المعاملات إلى الافتراضية."
    ARGS_TEXT_TOO_LONG_MSG = "❌ النص طويل جداً. الحد الأقصى 500 حرف."
    ARGS_ERROR_PROCESSING_MSG = "❌ خطأ في معالجة الإدخال. يرجى المحاولة مرة أخرى."
    ARGS_BOOL_INPUT_MSG = "❌ يرجى إدخال 'True' أو 'False' لخيار إرسال كملف."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ يرجى تقديم رقم صحيح."
    ARGS_BOOL_VALUE_REQUEST_MSG = "يرجى إرسال <code>True</code> أو <code>False</code> لتفعيل/إلغاء هذا الخيار."
    ARGS_JSON_VALUE_REQUEST_MSG = "يرجى إرسال JSON صحيح."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "ليس لديك علامات بعد."
    TAGS_MESSAGE_CLOSED_MSG = "تم إغلاق رسالة العلامات."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ تم إلغاء الترجمات ووضع السؤال دائماً."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ تم تفعيل وضع السؤال دائماً للترجمات."
    SUBS_LANGUAGE_SET_MSG = "✅ تم تعيين لغة الترجمات إلى: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️تحذير: بسبب التأثير العالي على المعالج، هذه الوظيفة بطيئة جداً (قريب من الوقت الفعلي) ومحدودة إلى:\n"
        "- جودة قصوى 720p\n"
        "- مدة قصوى 1.5 ساعة\n"
        "- حجم فيديو قصوى 500 ميجابايت</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>الأوامر السريعة:</b>\n"
        "• <code>/subs off</code> - إلغاء الترجمات\n"
        "• <code>/subs on</code> - تفعيل وضع السؤال دائماً\n"
        "• <code>/subs ru</code> - تعيين اللغة\n"
        "• <code>/subs ru auto</code> - تعيين اللغة مع AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 الترجمات معطلة"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} اللغة المختارة: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 تحميل الترجمات..."
    SUBS_DISABLED_ERROR_MSG = "❌ الترجمات معطلة. استخدم /subs للتكوين."
    SUBS_YOUTUBE_ONLY_MSG = "❌ تحميل الترجمات مدعوم فقط لـ YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 الترجمات</b>\n\n"
        "<b>الفيديو:</b> {title}\n"
        "<b>اللغة:</b> {lang}\n"
        "<b>النوع:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 تم إرسال ملف ترجمات SRT للمستخدم."
    SUBS_ERROR_PROCESSING_MSG = "❌ خطأ في معالجة ملف الترجمات."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ فشل في تحميل الترجمات."
    SUBS_ERROR_MSG = "❌ خطأ في تحميل الترجمات: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ تم تعيين حجم جزء التقسيم إلى: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **حجم غير صحيح!**\n\n"
        "**النطاق الصحيح:** 100 ميجابايت إلى 2 جيجابايت\n\n"
        "**التنسيقات الصحيحة:**\n"
        "• `100mb` إلى `2000mb` (ميجابايت)\n"
        "• `0.1gb` إلى `2gb` (جيجابايت)\n\n"
        "**أمثلة:**\n"
        "• `/split 100mb` - 100 ميجابايت\n"
        "• `/split 500mb` - 500 ميجابايت\n"
        "• `/split 1.5gb` - 1.5 جيجابايت\n"
        "• `/split 2gb` - 2 جيجابايت\n"
        "• `/split 2000mb` - 2000 ميجابايت (2 جيجابايت)\n\n"
        "**الإعدادات المسبقة:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **اختر الحد الأقصى لحجم الجزء لتقسيم الفيديو:**\n\n"
        "**النطاق:** 100 ميجابايت إلى 2 جيجابايت\n\n"
        "**الأوامر السريعة:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**أمثلة:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "تم إغلاق القائمة."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>إعدادات البوت</b>\n\nاختر فئة:"
    SETTINGS_MENU_CLOSED_MSG = "تم إغلاق القائمة."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 خيارات التنظيف</b>\n\nاختر ما تريد تنظيفه:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 ملفات تعريف الارتباط</b>\n\nاختر إجراء:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 الوسائط</b>\n\nاختر إجراء:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 المعلومات</b>\n\nاختر إجراء:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ المزيد من الأوامر</b>\n\nاختر إجراء:"
    SETTINGS_COMMAND_EXECUTED_MSG = "تم تنفيذ الأمر."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ حد الفيضان. جرب لاحقاً."
    SETTINGS_HINT_SENT_MSG = "تم إرسال التلميح."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "تم فتح مساعد البحث."
    SETTINGS_UNKNOWN_COMMAND_MSG = "أمر غير معروف."
    SETTINGS_HINT_CLOSED_MSG = "تم إغلاق التلميح."
    SETTINGS_HELP_SENT_MSG = "إرسال نص المساعدة للمستخدم"
    SETTINGS_MENU_OPENED_MSG = "تم فتح قائمة /settings"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 تم إغلاق مساعد البحث"
    SEARCH_CLOSED_MSG = "مغلق"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ البروكسي {status}."
    PROXY_ERROR_SAVING_MSG = "❌ خطأ في حفظ إعدادات البروكسي."
    PROXY_MENU_TEXT_MSG = "تفعيل أو إلغاء استخدام خادم البروكسي لجميع عمليات yt-dlp؟"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "هل تريد تمكين أو تعطيل استخدام الخوادم الوكيلة (يتوفر {config_count} + {file_count}) لجميع عمليات yt-dlp؟\n\nعند تمكين الكل (AUTO)، سيتم اختيار الوكلاء باستخدام طريقة عشوائية."
    PROXY_MENU_CLOSED_MSG = "تم إغلاق القائمة."
    PROXY_ENABLED_CONFIRM_MSG = "✅ تم تفعيل البروكسي. جميع عمليات yt-dlp ستستخدم البروكسي."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ تم تفعيل البروكسي. جميع عمليات yt-dlp ستستخدم {count} خادم بروكسي مع طريقة اختيار {method}."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ تم تمكين الوكيل (الوضع التلقائي بالكامل).\n\n📊 سيحاول الروبوت استخدام الوكلاء بهذا الترتيب:\n1️⃣ {config_count} وكلاء من Config.py\n2️⃣ {file_count} وكيل من ملف TXT/proxy.txt\n\n🔄 سيتم تجربة جميع البروكسيات بشكل تسلسلي حتى يتم الاتصال بنجاح."
    PROXY_DISABLED_MSG = "❌ تم إلغاء البروكسي."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ خطأ في حفظ إعدادات البروكسي."
    PROXY_ENABLED_CALLBACK_MSG = "تم تفعيل البروكسي."
    PROXY_DISABLED_CALLBACK_MSG = "تم إلغاء البروكسي."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ انتظر حتى ينتهي التحميل السابق"
    AUDIO_HELP_MSG = (
        "<b>🎧 أمر تحميل الصوت</b>\n\n"
        "الاستخدام: <code>/audio URL</code>\n\n"
        "<b>أمثلة:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "انظر أيضاً: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "تم إغلاق تلميح الصوت."
    PLAYLIST_HELP_CLOSED_MSG = "تم إغلاق مساعدة قائمة التشغيل."
    USERLOGS_CLOSED_MSG = "تم إغلاق رسالة السجلات."
    HELP_CLOSED_MSG = "تم إغلاق المساعدة."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>إعدادات ضبابية المحتوى غير المناسب</b>\n\nالمحتوى غير المناسب <b>{status}</b>.\n\nاختر ما إذا كنت تريد ضبابية المحتوى غير المناسب:"
    NSFW_MENU_CLOSED_MSG = "تم إغلاق القائمة."
    NSFW_BLUR_DISABLED_MSG = "تم إلغاء ضبابية المحتوى غير المناسب."
    NSFW_BLUR_ENABLED_MSG = "تم تفعيل ضبابية المحتوى غير المناسب."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "تم إلغاء ضبابية المحتوى غير المناسب."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "تم تفعيل ضبابية المحتوى غير المناسب."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ معلومات الوسائط {status}."
    MEDIAINFO_MENU_TITLE_MSG = "تفعيل أو إلغاء إرسال معلومات الوسائط للملفات المحملة؟"
    MEDIAINFO_MENU_CLOSED_MSG = "تم إغلاق القائمة."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ تم تفعيل معلومات الوسائط. بعد التحميل، سيتم إرسال معلومات الملف."
    MEDIAINFO_DISABLED_MSG = "❌ تم إلغاء معلومات الوسائط."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "تم تفعيل معلومات الوسائط."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "تم إلغاء معلومات الوسائط."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 قائمة التنسيقات المتاحة</b>\n\n"
        "احصل على تنسيقات الفيديو/الصوت المتاحة لرابط.\n\n"
        "<b>الاستخدام:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>أمثلة:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 كيفية استخدام معرفات التنسيق:</b>\n"
        "بعد الحصول على القائمة، استخدم معرف تنسيق محدد:\n"
        "• <code>/format id 401</code> - تحميل التنسيق 401\n"
        "• <code>/format id401</code> - نفس ما سبق\n"
        "• <code>/format id140 audio</code> - تحميل التنسيق 140 كصوت MP3\n\n"
        "سيظهر هذا الأمر جميع التنسيقات المتاحة التي يمكن تحميلها."
    )
    LIST_PROCESSING_MSG = "🔄 جاري الحصول على التنسيقات المتاحة..."
    LIST_INVALID_URL_MSG = "❌ يرجى تقديم رابط صحيح يبدأ بـ http:// أو https://"
    LIST_CAPTION_MSG = (
        "📃 التنسيقات المتاحة لـ:\n<code>{url}</code>\n\n"
        "💡 <b>كيفية تعيين التنسيق:</b>\n"
        "• <code>/format id 134</code> - تحميل معرف تنسيق محدد\n"
        "• <code>/format 720p</code> - تحميل حسب الجودة\n"
        "• <code>/format best</code> - تحميل أفضل جودة\n"
        "• <code>/format ask</code> - السؤال دائماً عن الجودة\n\n"
        "{audio_note}\n"
        "📋 استخدم معرف التنسيق من القائمة أعلاه"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>تنسيقات الصوت فقط:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - تحميل التنسيق 140 كصوت MP3\n"
        "• <code>/format id140 audio</code> - نفس ما سبق\n"
        "سيتم تحميلها كملفات صوت MP3.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ خطأ في إرسال ملف التنسيقات: {error}"
    LIST_ERROR_GETTING_MSG = "❌ فشل في الحصول على التنسيقات:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ حدث خطأ أثناء معالجة الأمر"
    LIST_ERROR_CALLBACK_MSG = "حدث خطأ"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 كيفية استخدام معرفات التنسيق:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "بعد الحصول على القائمة، استخدم معرف تنسيق محدد:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - تحميل التنسيق 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - نفس ما سبق\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - تحميل التنسيق 140 كصوت MP3\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - نفس ما سبق\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 تم اكتشاف تنسيقات الصوت فقط: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "سيتم تحميل هذه التنسيقات كملفات صوت MP3.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>تنسيقات الفيديو فقط:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 استخدم معرف التنسيق من القائمة أعلاه"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>الاستخدام:</b>\n"
        "<code>/link [جودة] URL</code>\n\n"
        "<b>أمثلة:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - أفضل جودة\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p أو أقل\n"
        "• /link 720p https://youtube.com/watch?v=... - نفس ما سبق\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K أو أقل\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K أو أقل"
        "</blockquote>\n\n"
        "<b>الجودة:</b> من 1 إلى 10000 (مثال: 144، 240، 720، 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ يرجى تقديم رابط صحيح"
    LINK_PROCESSING_MSG = "🔗 جاري الحصول على الرابط المباشر..."
    LINK_DURATION_MSG = "⏱ <b>المدة:</b> {duration} ثانية\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>بث الفيديو:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>بث الصوت:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **تم تحديث إعداد لوحة المفاتيح!**\n\nالإعداد الجديد: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **معامل غير صحيح!**\n\n"
        "الخيارات الصحيحة: `off`, `1x3`, `2x3`, `full`\n\n"
        "مثال: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **إعدادات لوحة المفاتيح**\n\n"
        "الحالي: **{current}**\n\n"
        "اختر خياراً:\n\n"
        "أو استخدم: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 تم تفعيل لوحة المفاتيح!"
    KEYBOARD_HIDDEN_MSG = "⌨️ تم إخفاء لوحة المفاتيح"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 تم تفعيل لوحة المفاتيح 1x3!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 تم تفعيل لوحة المفاتيح 2x3!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 تم تفعيل لوحة المفاتيح الرموز التعبيرية!"
    KEYBOARD_ERROR_APPLYING_MSG = "خطأ في تطبيق إعداد لوحة المفاتيح {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ تم تعيين التنسيق إلى: السؤال دائماً. سيتم سؤالك عن الجودة في كل مرة ترسل رابط."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ تم تعيين التنسيق إلى: السؤال دائماً. الآن سيتم سؤالك عن الجودة في كل مرة ترسل رابط."
    FORMAT_BEST_UPDATED_MSG = "✅ تم تحديث التنسيق إلى أفضل جودة (أولوية AVC+MP4):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ تم تحديث التنسيق إلى المعرف {id}:\n{format}\n\n💡 <b>ملاحظة:</b> إذا كان هذا تنسيق صوت فقط، سيتم تحميله كملف صوت MP3."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ تم تحديث التنسيق إلى المعرف {id} (صوت فقط):\n{format}\n\n💡 سيتم تحميله كملف صوت MP3."
    FORMAT_QUALITY_UPDATED_MSG = "✅ تم تحديث التنسيق إلى الجودة {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ تم تحديث التنسيق إلى:\n{format}"
    FORMAT_MENU_MSG = (
        "اختر خيار تنسيق أو أرسل مخصص باستخدام:\n"
        "• <code>/format &lt;format_string&gt;</code> - تنسيق مخصص\n"
        "• <code>/format 720</code> - جودة 720p\n"
        "• <code>/format 4k</code> - جودة 4K\n"
        "• <code>/format 8k</code> - جودة 8K\n"
        "• <code>/format id 401</code> - معرف تنسيق محدد\n"
        "• <code>/format ask</code> - إظهار القائمة دائماً\n"
        "• <code>/format best</code> - bv+ba/أفضل جودة"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "لاستخدام تنسيق مخصص، أرسل الأمر بالشكل التالي:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "استبدل <code>bestvideo+bestaudio/best</code> بسلسلة التنسيق المطلوبة."
    )
    FORMAT_RESOLUTION_MENU_MSG = "اختر الدقة وترميز الفيديو المطلوبين:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ تم تعيين التنسيق إلى: السؤال دائماً. الآن سيتم سؤالك عن الجودة في كل مرة ترسل رابط."
    FORMAT_UPDATED_MSG = "✅ تم تحديث التنسيق إلى:\n{format}"
    FORMAT_SAVED_MSG = "✅ تم حفظ التنسيق."
    FORMAT_CHOICE_UPDATED_MSG = "✅ تم تحديث اختيار التنسيق."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "تم إغلاق قائمة التنسيق المخصص"
    FORMAT_CODEC_SET_MSG = "✅ تم تعيين الترميز إلى {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ تم تحديث اختيار المتصفح."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ تم رفض الوصول. للمدير فقط."
    ACCESS_DENIED_ADMIN = "❌ تم رفض الوصول. للمدير فقط."
    WELCOME_MASTER = "مرحباً أيها السيد 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ عذراً... حدث خطأ أثناء التحميل."
    SIZE_LIMIT_EXCEEDED = "❌ حجم الملف يتجاوز الحد الأقصى {max_size_gb} جيجابايت. يرجى اختيار ملف أصغر ضمن الحجم المسموح."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ لم يتم العثور على السكريبت: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ جاري تحميل نسخة Firebase جديدة باستخدام {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ تم إعادة تحميل تخزين Firebase المؤقت بنجاح!"
    ADMIN_CACHE_FAILED_MSG = "❌ فشل في إعادة تحميل تخزين Firebase المؤقت. تحقق من وجود {cache_file}."
    ADMIN_ERROR_RELOADING_MSG = "❌ خطأ في إعادة تحميل التخزين المؤقت: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ خطأ في تشغيل {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ تم إرسال رسالة الترويج لجميع المستخدمين الآخرين</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ لا يمكن إرسال رسالة الترويج. جرب الرد على رسالة\nأو حدث خطأ ما</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ المستخدم لم يحمل أي محتوى بعد...</b> غير موجود في السجلات"
    ADMIN_INVALID_COMMAND_MSG = "❌ أمر غير صحيح"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ لم يتم العثور على بيانات في التخزين المؤقت لـ <code>{{path}}</code>"
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ الاستخدام: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 لا يمكن للمدير حذف مدير آخر"
    ADMIN_USER_BLOCKED_MSG = "تم حظر المستخدم 🔒❌\n \nالمعرف: <code>{user_id}</code>\nتاريخ الحظر: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> محظور بالفعل ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 عذراً! أنت لست مديراً"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ الاستخدام: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "تم إلغاء حظر المستخدم 🔓✅\n \nالمعرف: <code>{user_id}</code>\nتاريخ إلغاء الحظر: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> غير محظور بالفعل ✅😐"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ الاستخدام: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "تم تجاهل المستخدم 👁️❌\n \nالمعرف: <code>{user_id}</code>\nتاريخ التجاهل: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> متجاهل بالفعل ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ الاستخدام: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "لم يعد المستخدم متجاهلاً 👁️✅\n \nالمعرف: <code>{user_id}</code>\nتاريخ إلغاء التجاهل: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> غير متجاهل ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>وقت تشغيل البوت -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ يرجى تقديم رابط لمسح التخزين المؤقت.\nالاستخدام: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ يرجى تقديم رابط صحيح.\nالاستخدام: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ تم مسح التخزين المؤقت بنجاح للرابط:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ لم يتم العثور على تخزين مؤقت لهذا الرابط."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ خطأ في مسح التخزين المؤقت: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ تم رفض الوصول. للمدير فقط."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ جاري تشغيل سكريبت تحديث قائمة المحتوى غير المناسب: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ تم إكمال السكريبت بنجاح!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ تم إكمال السكريبت بنجاح!\n\nالمخرجات:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ فشل السكريبت مع رمز الإرجاع {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ خطأ في تشغيل السكريبت: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ جاري إعادة تحميل تخزين المحتوى غير المناسب والمواقع ذات الصلة..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ تم إعادة تحميل تخزين المحتوى غير المناسب بنجاح!\n\n"
        "📊 حالة التخزين المؤقت الحالية:\n"
        "• مواقع المحتوى غير المناسب: {porn_domains}\n"
        "• كلمات المحتوى غير المناسب: {porn_keywords}\n"
        "• المواقع المدعومة: {supported_sites}\n"
        "• القائمة البيضاء: {whitelist}\n"
        "• القائمة الرمادية: {greylist}\n"
        "• القائمة السوداء: {black_list}\n"
        "• الكلمات البيضاء: {white_keywords}\n"
        "• مواقع البروكسي: {proxy_domains}\n"
        "• مواقع البروكسي 2: {proxy_2_domains}\n"
        "• استعلام نظيف: {clean_query}\n"
        "• مواقع بدون ملفات تعريف ارتباط: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ خطأ في إعادة تحميل تخزين المحتوى غير المناسب: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ يرجى تقديم رابط للفحص.\nالاستخدام: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ يرجى تقديم رابط صحيح.\nالاستخدام: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 جاري فحص الرابط للمحتوى غير المناسب...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>نتيجة فحص المحتوى غير المناسب</b>\n\n"
        "<b>الرابط:</b> <code>{url}</code>\n"
        "<b>الحالة:</b> <b>{status_text}</b>\n\n"
        "<b>التفسير:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ خطأ في فحص الرابط: {error}"
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 سجل نشاط القناة لآخر {hours} ساعة (يومان)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 خلال آخر {hours} ساعة (يومان): انضم {joined}، غادر {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ لا يوجد نشاط خلال آخر {hours} ساعة (يومان)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "الإجمالي: 🟢 انضم {joined}، 🔴 غادر {left}."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ لا يوجد وصول إلى سجل نشاط القناة. لا يمكن للبوتات قراءة سجلات المسؤول. قم بتوفير CHANNEL_GUARD_SESSION_STRING في الإعدادات مع جلسة مستخدم لتمكين هذه الميزة."
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ قائمة الانتظار فارغة — لم يغادر أحد القناة بعد."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>قائمة انتظار الحظر</b>\nالمعلقون الإجمالي: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (غادر: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… و {extra} مستخدمين آخرين."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "استخدم /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ تم حظر المستخدمين من قائمة الانتظار: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ تم تفعيل الحظر التلقائي: سيتم حظر المغادرين الجدد فوراً."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ تم إلغاء تفعيل الحظر التلقائي."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ تم تعيين نافذة الحظر التلقائي المجدولة إلى كل {interval}."
    BAN_TIME_USAGE_MSG = "❌ الاستخدام: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ استخدم التنسيقات مثل 10s، 6m، 5h، 4d، 3w، 2M أو 1y."
    BAN_TIME_SET_MSG = "🕒 تم تعيين فاصل فحص سجل القناة إلى {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ تقرير فحص القناة\n"
        "تم التشغيل في: {run_ts}\n"
        "الفاصل: {interval}\n"
        "المغادرون الجدد: {new_leavers}\n"
        "الحظر التلقائي: {auto_banned}\n"
        "المعلقون: {pending}\n"
        "آخر event_id: {last_event_id}"
    )
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ تم إلغاء حظر المستخدمين: {count}\n⏱ الطابع الزمني: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ الاستخدام: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "تم تجاهل المستخدم 👁️❌\n \nالمعرف: <code>{user_id}</code>\nتاريخ التجاهل: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> متجاهل بالفعل ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ الاستخدام: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "لم يعد المستخدم متجاهلاً 👁️✅\n \nالمعرف: <code>{user_id}</code>\nتاريخ إلغاء التجاهل: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> غير متجاهل ✅😐"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "تم تنظيف ملفات تعريف الارتباط."
    CLEAN_LOGS_CLEANED_MSG = "تم تنظيف السجلات."
    CLEAN_TAGS_CLEANED_MSG = "تم تنظيف العلامات."
    CLEAN_FORMAT_CLEANED_MSG = "تم تنظيف التنسيق."
    CLEAN_SPLIT_CLEANED_MSG = "تم تنظيف التقسيم."
    CLEAN_MEDIAINFO_CLEANED_MSG = "تم تنظيف معلومات الوسائط."
    CLEAN_SUBS_CLEANED_MSG = "تم تنظيف إعدادات الترجمات."
    CLEAN_KEYBOARD_CLEANED_MSG = "تم تنظيف إعدادات لوحة المفاتيح."
    CLEAN_ARGS_CLEANED_MSG = "تم تنظيف إعدادات المعاملات."
    CLEAN_NSFW_CLEANED_MSG = "تم تنظيف إعدادات المحتوى غير المناسب."
    CLEAN_PROXY_CLEANED_MSG = "تم تنظيف إعدادات البروكسي."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "تم تنظيف إعدادات انتظار الفيضان."
    CLEAN_ALL_CLEANED_MSG = "تم تنظيف جميع الملفات."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 ملفات تعريف الارتباط</b>\n\nاختر إجراء:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ تم حفظ ملف تعريف الارتباط"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ تم تخطي التحقق من ملفات تعريف الارتباط غير الخاصة بـ YouTube"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ ملف تعريف الارتباط موجود ولكن بتنسيق غير صحيح"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ لم يتم العثور على ملف تعريف الارتباط."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 بدء اختبار ملفات تعريف ارتباط YouTube...\n\nيرجى الانتظار بينما أتحقق من ملفات تعريف الارتباط وأتحقق من صحتها."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ ملفات تعريف ارتباط YouTube الموجودة تعمل بشكل صحيح!\n\nلا حاجة لتحميل ملفات جديدة."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ ملفات تعريف ارتباط YouTube الموجودة منتهية الصلاحية أو غير صحيحة.\n\n🔄 جاري تحميل ملفات جديدة..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ مصدر ملفات تعريف الارتباط {service} غير مُكوّن!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ مصدر ملفات تعريف الارتباط {service} يجب أن يكون ملف .txt!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ تم تجاوز حد النطاق: تم طلب {range_count} ملف (الحد الأقصى {max_img_files}).\n\nاستخدم أحد هذه الأوامر لتحميل الحد الأقصى من الملفات المتاحة:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚إغلاق"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ تم تجاوز حد الوسائط: تم طلب {count} ملف (الحد الأقصى {max_count}).\n\nاستخدم أحد هذه الأوامر لتحميل الحد الأقصى من الملفات المتاحة:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 تم العثور على <b>{count}</b> عنصر وسائط من الرابط"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "اختر نطاق التحميل:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "انتحال شخصية المتصفح"
    ARGS_REFERER_DESC_MSG = "رأس Referer"
    ARGS_USER_AGENT_DESC_MSG = "رأس User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "تجاوز القيود الجغرافية"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "فحص شهادة SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "تحميل البث المباشر من البداية"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "عدم تحميل البث المباشر من البداية"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "استخدام حاوية MPEG-TS لمقاطع HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "تحميل فيديو واحد فقط، وليس قائمة التشغيل"
    ARGS_NO_PART_DESC_MSG = "عدم استخدام ملفات .part"
    ARGS_NO_CONTINUE_DESC_MSG = "عدم استكمال التحميلات الجزئية"
    ARGS_AUDIO_FORMAT_DESC_MSG = "تنسيق الصوت للاستخراج"
    ARGS_EMBED_METADATA_DESC_MSG = "تضمين البيانات الوصفية في ملف الفيديو"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "تضمين الصورة المصغرة في ملف الفيديو"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "كتابة الصورة المصغرة إلى ملف"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "عدد الأجزاء المتزامنة للتحميل"
    ARGS_FORCE_IPV4_DESC_MSG = "فرض اتصالات IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "فرض اتصالات IPv6"
    ARGS_XFF_DESC_MSG = "استراتيجية رأس X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "حجم قطعة HTTP (بايت)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "انتظار قبل تحميل الترجمات (ثواني)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "السماح باتصالات الخادم القديمة"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "قمع التحقق من شهادة HTTPS"
    ARGS_USERNAME_DESC_MSG = "اسم مستخدم الحساب"
    ARGS_PASSWORD_DESC_MSG = "كلمة مرور الحساب"
    ARGS_TWOFACTOR_DESC_MSG = "رمز المصادقة الثنائية"
    ARGS_IGNORE_ERRORS_DESC_MSG = "تجاهل أخطاء التحميل والمتابعة"
    ARGS_MIN_FILESIZE_DESC_MSG = "الحد الأدنى لحجم الملف (ميجابايت)"
    ARGS_MAX_FILESIZE_DESC_MSG = "الحد الأقصى لحجم الملف (ميجابايت)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "عناصر قائمة التشغيل للتحميل (مثال: 1,3,5 أو 1-5)"
    ARGS_DATE_DESC_MSG = "تحميل الفيديوهات المرفوعة في هذا التاريخ (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "تحميل الفيديوهات المرفوعة قبل هذا التاريخ (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "تحميل الفيديوهات المرفوعة بعد هذا التاريخ (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "رؤوس HTTP مخصصة (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "فترة الانتظار بين الطلبات (ثواني)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "الحد الأقصى لفترة الانتظار (ثواني)"
    ARGS_RETRIES_DESC_MSG = "عدد المحاولات"
    ARGS_VIDEO_FORMAT_DESC_MSG = "تنسيق حاوية الفيديو"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "تنسيق حاوية الإخراج للدمج"
    ARGS_SEND_AS_FILE_DESC_MSG = "إرسال جميع الوسائط كوثيقة بدلاً من وسائط"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "انتحال"
    ARGS_REFERER_SHORT_MSG = "المُحيل"
    ARGS_GEO_BYPASS_SHORT_MSG = "تجاوز جغرافي"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "فحص الشهادة"
    ARGS_LIVE_FROM_START_SHORT_MSG = "بداية مباشرة"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "لا بداية مباشرة"
    ARGS_USER_AGENT_SHORT_MSG = "وكيل المستخدم"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "لا قائمة تشغيل"
    ARGS_NO_PART_SHORT_MSG = "لا جزء"
    ARGS_NO_CONTINUE_SHORT_MSG = "لا استكمال"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "تنسيق الصوت"
    ARGS_EMBED_METADATA_SHORT_MSG = "تضمين البيانات"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "تضمين الصورة"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "كتابة الصورة"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "متزامن"
    ARGS_FORCE_IPV4_SHORT_MSG = "فرض IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "فرض IPv6"
    ARGS_XFF_SHORT_MSG = "رأس XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "حجم القطعة"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "انتظار الترجمات"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "اتصال قديم"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "لا فحص شهادة"
    ARGS_USERNAME_SHORT_MSG = "اسم المستخدم"
    ARGS_PASSWORD_SHORT_MSG = "كلمة المرور"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "تجاهل الأخطاء"
    ARGS_MIN_FILESIZE_SHORT_MSG = "الحد الأدنى"
    ARGS_MAX_FILESIZE_SHORT_MSG = "الحد الأقصى"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "عناصر القائمة"
    ARGS_DATE_SHORT_MSG = "التاريخ"
    ARGS_DATEBEFORE_SHORT_MSG = "تاريخ قبل"
    ARGS_DATEAFTER_SHORT_MSG = "تاريخ بعد"
    ARGS_HTTP_HEADERS_SHORT_MSG = "رؤوس HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "فترة الانتظار"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "الحد الأقصى للانتظار"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "تنسيق الفيديو"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "تنسيق الدمج"
    ARGS_SEND_AS_FILE_SHORT_MSG = "إرسال كملف"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ الملف كبير جداً. الحد الأقصى للحجم هو 100 كيلوبايت."
    COOKIES_INVALID_FORMAT_MSG = "❌ يُسمح فقط بملفات التنسيق التالي .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ الملف لا يبدو كملف cookie.txt (لا يوجد سطر '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ خطأ في قراءة الملف: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ ملف تعريف الارتباط موجود وله تنسيق صحيح"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ ملف تعريف ارتباط {service} كبير جداً! الحد الأقصى 100 كيلوبايت، تم الحصول على {size} كيلوبايت."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ تم تحميل ملف تعريف ارتباط {service} وحفظه كـ cookie.txt في مجلدك.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ مصدر ملف تعريف ارتباط {service} غير متاح (الحالة {status}). يرجى المحاولة مرة أخرى لاحقاً."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ خطأ في تحميل ملف تعريف ارتباط {service}. يرجى المحاولة مرة أخرى لاحقاً."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ قدم المستخدم ملف تعريف ارتباط جديد.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ تم تحديث ملف تعريف الارتباط بنجاح:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ ليس ملف تعريف ارتباط صحيح.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ مصادر ملفات تعريف ارتباط YouTube غير مُكوّنة!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 جاري تحميل وفحص ملفات تعريف ارتباط YouTube...\n\nالمحاولة {attempt} من {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ تم رفض الوصول. للمدير فقط."
    ADMIN_USER_LOGS_TOTAL_MSG = "المجموع: <b>{total}</b>\n<b>{user_id}</b> - السجلات (آخر 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 تم تفعيل لوحة المفاتيح!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ تم تعيين لغة الترجمة إلى: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ تم تعيين لغة الترجمة إلى: {flag} {name} مع تفعيل AUTO/TRANS."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "تم إغلاق قائمة لغة الترجمة."
    SUBS_DOWNLOADING_MSG = "💬 جاري تحميل الترجمات..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 جاري إعادة تحميل تخزين Firebase المؤقت في الذاكرة..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ لم يتم تكوين COOKIE_URL. استخدم /cookie أو ارفع cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 جاري تحميل ملفات تعريف الارتباط من الرابط البعيد..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ يجب أن يشير COOKIE_URL الاحتياطي إلى ملف .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ ملف تعريف الارتباط الاحتياطي كبير جداً (>100 كيلوبايت)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ تم تحميل ملف تعريف ارتباط YouTube عبر الاحتياطي وحفظه كـ cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ مصدر ملف تعريف الارتباط الاحتياطي غير متاح (الحالة {status}). جرب /cookie أو ارفع cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ خطأ في تحميل ملف تعريف الارتباط الاحتياطي. جرب /cookie أو ارفع cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ خطأ غير متوقع أثناء تحميل ملف تعريف الارتباط الاحتياطي."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ متصفح {browser} غير مثبت."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ تم حفظ ملفات تعريف الارتباط باستخدام المتصفح: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ فشل في حفظ ملفات تعريف الارتباط: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ ملفات تعريف ارتباط YouTube تعمل بشكل صحيح"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ ملفات تعريف ارتباط YouTube منتهية الصلاحية أو غير صحيحة\n\nاستخدم /cookie للحصول على ملفات جديدة"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - تنسيق مخصص\n• <code>/format 720</code> - جودة 720p\n• <code>/format 4k</code> - جودة 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "تم إرسال التلميح."
    FORMAT_MKV_TOGGLE_MSG = "MKV الآن {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ لم يتم تكوين رابط بعيد"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ تنسيق ملف غير صحيح"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ الملف كبير جداً"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ تم تحميل ملفات تعريف الارتباط بنجاح"
    COOKIES_SERVER_ERROR_MSG = "❌ خطأ في الخادم {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ فشل التحميل"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ خطأ غير متوقع"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ المتصفح غير مثبت."
    COOKIES_MENU_CLOSED_MSG = "تم إغلاق القائمة."
    COOKIES_HINT_CLOSED_MSG = "تم إغلاق تلميح ملف تعريف الارتباط."
    IMG_HELP_CLOSED_MSG = "تم إغلاق المساعدة."
    SUBS_LANGUAGE_UPDATED_MSG = "تم تحديث إعدادات لغة الترجمة."
    SUBS_MENU_CLOSED_MSG = "تم إغلاق قائمة لغة الترجمة."
    KEYBOARD_SET_TO_MSG = "تم تعيين لوحة المفاتيح إلى {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "خطأ في معالجة الإعداد"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "تم تفعيل MediaInfo."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "تم إلغاء تفعيل MediaInfo."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "تم إلغاء تفعيل ضبابية المحتوى غير المناسب."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "تم تفعيل ضبابية المحتوى غير المناسب."
    SETTINGS_MENU_CLOSED_MSG = "تم إغلاق القائمة."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "انتظار الفيضان نشط. جرب لاحقاً."
    OTHER_HELP_CLOSED_MSG = "تم إغلاق المساعدة."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "تم إغلاق رسالة السجلات."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "تم إغلاق القائمة."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "حجم غير صحيح."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ خطأ في إرسال معلومات الوسائط: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ حدث خطأ: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 معلومات الوسائط</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - جميع السجلات"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - جميع {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 تحميل من الرابط البعيد"
    BROWSER_OPEN_BUTTON_MSG = "🌐 فتح المتصفح"
    SELECT_BROWSER_MSG = "اختر متصفحاً لتحميل ملفات تعريف الارتباط منه:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "لم يتم العثور على متصفحات في هذا النظام. يمكنك تحميل ملفات تعريف الارتباط من رابط بعيد أو مراقبة حالة المتصفح:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>فتح المتصفح</b> - لمراقبة حالة المتصفح في التطبيق المصغر"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ فشل في تشغيل /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ حد الفيضان. جرب لاحقاً."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ فشل في فتح قائمة ملفات تعريف ارتباط المتصفح"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "تم إغلاق تلميح حفظ كملف تعريف ارتباط."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>الاستخدام:</b>\n<code>/link [quality] URL</code>\n\n<b>أمثلة:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - أفضل جودة\n• /link 720 https://youtube.com/watch?v=... - 720p أو أقل\n• /link 720p https://youtube.com/watch?v=... - نفس ما سبق\n• /link 4k https://youtube.com/watch?v=... - 4K أو أقل\n• /link 8k https://youtube.com/watch?v=... - 8K أو أقل</blockquote>\n\n<b>الجودة:</b> من 1 إلى 10000 (مثال: 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - جودة 8K"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>تم الحصول على الرابط المباشر</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>التنسيق:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>تيار الصوت:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ فشل في الحصول على روابط التيار"
    LINK_ERROR_GETTING_MSG = "❌ <b>خطأ في الحصول على الرابط:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ فهرس ملف تعريف ارتباط YouTube غير صحيح: {selected_index}. النطاق المتاح هو 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 جاري تحميل وفحص ملفات تعريف ارتباط YouTube...\n\nالمحاولة {attempt} من {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 جاري تحميل وفحص ملفات تعريف ارتباط YouTube...\n\nالمحاولة {attempt} من {total}\n🔍 جاري اختبار ملفات تعريف الارتباط..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ تم تحميل ملفات تعريف ارتباط YouTube والتحقق منها بنجاح!\n\nتم استخدام المصدر {source} من {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ جميع ملفات تعريف ارتباط YouTube منتهية الصلاحية أو غير متاحة!\n\nاتصل بمدير البوت لاستبدالها."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ تم تجاوز الحد الأقصى لمحاولات إعادة تجربة ملفات تعريف ارتباط YouTube!\n\n🔢 الحد الأقصى: {limit} محاولات في الساعة\n⏰ حاول مرة أخرى لاحقاً"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ العلامة #{wrong} تحتوي على أحرف محظورة. يُسمح فقط بالأحرف والأرقام و _.\nيرجى استخدام: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **وسيطة غير صحيحة!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ تم تعيين لغة الترجمة: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "مثال: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} اللغة المحددة: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ وضع السؤال دائماً {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 الترجمات معطلة"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 إعدادات الترجمة</b>\n\n{status_text}\n\nاختر لغة الترجمة:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - تعطيل الترجمات\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 إعدادات الترجمة</b>\n\n{status_text}\n\nاختر لغة الترجمة:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>العنوان:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>المدة:</b> {duration} ثانية\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>تيار الفيديو:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- جودة 720p كحد أقصى\n- مدة 1.5 ساعة كحد أقصى\n- حجم فيديو 500 ميجابايت كحد أقصى</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️تحذير: بسبب التأثير العالي على المعالج، هذه الوظيفة بطيئة جداً (قريب من الوقت الفعلي) ومحدودة إلى:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>أوامر سريعة:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - تعطيل الترجمات\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - تفعيل وضع السؤال دائماً\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - تعيين اللغة\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - تعيين اللغة مع تفعيل AUTO/TRANS\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - تفعيل وضع السؤال دائماً\n"
    SUBS_AUTO_SUBS_TEXT = " (ترجمات تلقائية)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ وضع الترجمات التلقائية {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "تم تعطيل الترجمات عبر الأمر: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "تم تفعيل وضع السؤال دائماً للترجمات عبر الأمر: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "تم تعيين لغة الترجمات عبر الأمر: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "تم تعيين لغة الترجمات + الوضع التلقائي عبر الأمر: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "فتح المستخدم قائمة /subs."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "عين المستخدم لغة الترجمة إلى: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "غير المستخدم وضع AUTO/TRANS إلى: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "غير المستخدم وضع السؤال دائماً إلى: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "طلب المستخدم ملفات تعريف الارتباط من المتصفح."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "تم إرسال لوحة مفاتيح اختيار المتصفح مع المتصفحات المثبتة فقط."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "تم إغلاق اختيار المتصفح."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "تم استخدام COOKIE_URL الاحتياطي بنجاح (المصدر مخفي)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "فشل COOKIE_URL الاحتياطي: الحالة={status} (مخفي)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "خطأ غير متوقع في COOKIE_URL الاحتياطي: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "المتصفح {browser} غير مثبت."
    COOKIES_SAVED_BROWSER_LOG_MSG = "تم حفظ ملفات تعريف الارتباط باستخدام المتصفح: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "تم حفظ ملف تعريف الارتباط للمستخدم {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "ملف تعريف الارتباط موجود، له تنسيق صحيح، وملفات تعريف ارتباط YouTube تعمل."
    COOKIES_FILE_EXPIRED_LOG_MSG = "ملف تعريف الارتباط موجود وله تنسيق صحيح، ولكن ملفات تعريف ارتباط YouTube منتهية الصلاحية."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "ملف تعريف الارتباط موجود وله تنسيق صحيح."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "ملف تعريف الارتباط موجود ولكن له تنسيق غير صحيح."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "لم يتم العثور على ملف تعريف الارتباط."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "رابط ملف تعريف ارتباط {service} فارغ للمستخدم {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "رابط ملف تعريف ارتباط {service} ليس .txt (مخفي)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "ملف تعريف ارتباط {service} كبير جداً: {size} بايت (المصدر مخفي)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "تم تحميل ملف تعريف ارتباط {service} للمستخدم {user_id} (المصدر مخفي)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "لم يتم العثور على السكريبت: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "فشل في إرسال رسالة الحالة الأولية"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "خطأ في تشغيل {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "تم إعادة تحميل تخزين Firebase المؤقت بواسطة المهمة التلقائية."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "تم إعادة تحميل تخزين Firebase المؤقت بواسطة المدير."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "خطأ في إعادة تحميل تخزين Firebase المؤقت: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "تم بدء البث. النص:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "تم إرسال رسالة البث إلى جميع المستخدمين."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "فشل في بث الرسالة: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "المدير {user_id} مسح التخزين المؤقت للرابط: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "بدأ المدير {user_id} سكريبت تحديث قائمة المحتوى غير المناسب: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "اكتمل سكريبت تحديث قائمة المحتوى غير المناسب بنجاح بواسطة المدير {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "فشل سكريبت تحديث قائمة المحتوى غير المناسب بواسطة المدير {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "حاول المدير {user_id} تشغيل سكريبت غير موجود: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "خطأ في تشغيل سكريبت تحديث المحتوى غير المناسب بواسطة المدير {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "بدأ المدير {user_id} إعادة تحميل تخزين المحتوى غير المناسب المؤقت"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "خطأ في إعادة تحميل تخزين المحتوى غير المناسب المؤقت بواسطة المدير {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "فحص المدير {user_id} الرابط للمحتوى غير المناسب: {url} - النتيجة: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "طلب المستخدم تغيير التنسيق."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "تم تعيين التنسيق إلى ALWAYS_ASK."
    FORMAT_UPDATED_BEST_LOG_MSG = "تم تحديث التنسيق إلى الأفضل: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "تم تحديث التنسيق إلى المعرف {format_id}: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "تم تحديث التنسيق إلى المعرف {format_id} (صوت فقط): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "تم تحديث التنسيق إلى الجودة {quality}: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "تم تحديث التنسيق إلى: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "تم إرسال قائمة التنسيق."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "تم إغلاق اختيار التنسيق."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "تم إرسال تلميح التنسيق المخصص."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "تم إرسال قائمة دقة التنسيق."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "عاد إلى قائمة التنسيق الرئيسية."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "تم تحديث التنسيق إلى: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "تم تعيين التنسيق إلى ALWAYS_ASK."
    FORMAT_CODEC_SET_LOG_MSG = "تم تعيين تفضيل الترميز إلى {codec}"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "تم إغلاق قائمة التنسيق المخصص"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "تم استخراج الرابط المباشر للمستخدم {user_id} من {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "فشل استخراج الرابط المباشر للمستخدم {user_id} من {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "خطأ في أمر الرابط للمستخدم {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "عين المستخدم {user_id} لوحة المفاتيح إلى {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "عين المستخدم {user_id} لوحة المفاتيح إلى {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "تم تعيين MediaInfo عبر الأمر: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "فتح المستخدم قائمة /mediainfo."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: تم الإغلاق."
    MEDIAINFO_ENABLED_LOG_MSG = "تم تفعيل MediaInfo."
    MEDIAINFO_DISABLED_LOG_MSG = "تم إلغاء تفعيل MediaInfo."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "تم تعيين حجم التقسيم إلى {size} بايت عبر الوسيطة."
    SPLIT_MENU_OPENED_LOG_MSG = "فتح المستخدم قائمة /split."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "تم إغلاق اختيار التقسيم."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "تم تعيين حجم التقسيم إلى {size} بايت."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "تم تعيين البروكسي عبر الأمر: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "فتح المستخدم قائمة /proxy."
    PROXY_MENU_CLOSED_LOG_MSG = "البروكسي: تم الإغلاق."
    PROXY_ENABLED_LOG_MSG = "تم تفعيل البروكسي."
    PROXY_DISABLED_LOG_MSG = "تم إلغاء تفعيل البروكسي."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "تم إغلاق رسالة المساعدة."
    AUDIO_HELP_SHOWN_LOG_MSG = "تم عرض مساعدة /audio"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "طلب المستخدم مساعدة قائمة التشغيل."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "تم إغلاق مساعدة قائمة التشغيل."
    AUDIO_HINT_CLOSED_LOG_MSG = "تم إغلاق تلميح الصوت."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "تم إنشاء قائمة الرابط المباشر عبر زر LINK للمستخدم {user_id} من {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "فشل في استخراج الرابط المباشر عبر زر LINK للمستخدم {user_id} من {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "تم تنفيذ أمر LIST للمستخدم {user_id}، الرابط: {url}"
    QUICK_EMBED_LOG_MSG = "التضمين السريع: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "تم إرسال قائمة السؤال دائماً لـ {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "تم إنشاء قائمة الجودات المخزنة للمستخدم {user_id} بعد الخطأ: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "خطأ في قائمة السؤال دائماً لـ {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "التنسيق ثابت عبر إعدادات /args"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "صوت"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "فيديو"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "فيديو"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "التالي ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ السابق"
    SUBTITLES_NEXT_BUTTON_MSG = "التالي ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ جميع حقول النص فارغة"
    SENDER_VIDEO_DURATION_MSG = "مدة الفيديو:"
    SENDER_UPLOADING_FILE_MSG = "📤 جاري رفع الملف..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 جاري رفع الفيديو..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 مدة الفيديو:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "تم رفع ملف واحد."
    DOWN_UP_VIDEO_INFO_MSG = "📋 معلومات الفيديو"
    DOWN_UP_NUMBER_MSG = "الرقم"
    DOWN_UP_TITLE_MSG = "العنوان"
    DOWN_UP_ID_MSG = "المعرف"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ تم تحميل الفيديو."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 جاري المعالجة للرفع..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 تم رفع الجزء المقسم {part}"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ اكتمل الرفع"
    DOWN_UP_FILES_UPLOADED_MSG = "تم رفع الملفات"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 إغلاق"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼ترميز"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 دبلجة"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 ترجمات"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 المتصفح"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 جاري الحصول على الرابط المباشر..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 جاري الحصول على التنسيقات المتاحة..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 جاري الحصول على وصف الفيديو..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ خطأ في الحصول على الوصف: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ وصف الفيديو غير متاح"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ خطأ في إرسال الوصف: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 تم إرسال وصف الفيديو للمستخدم {user_id} لـ {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 بدء gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>المدة:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>التنسيق:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>المتصفح:</b> فتح في متصفح الويب"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "التنسيقات المتاحة لـ"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 كيفية استخدام معرفات التنسيق:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "بعد الحصول على القائمة، استخدم معرف التنسيق المحدد:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - تحميل التنسيق 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - نفس ما سبق"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - تحميل التنسيق 140 كصوت MP3"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 تم اكتشاف تنسيقات صوت فقط"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "ستتم تحميل هذه التنسيقات كملفات صوت MP3."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>كيفية تعيين التنسيق:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - تحميل معرف التنسيق المحدد"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - تحميل حسب الجودة"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - تحميل أفضل جودة"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - السؤال دائماً عن الجودة"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>تنسيقات صوت فقط:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - تحميل التنسيق 140 كصوت MP3"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "ستتم تحميل هذه كملفات صوت MP3."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 استخدم معرف التنسيق من القائمة أعلاه"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ خطأ: لم يتم العثور على الرسالة الأصلية."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "صفحة التنسيقات"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ خطأ في عرض قائمة التنسيقات"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ خطأ في الحصول على التنسيقات"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ خطأ في الحصول على التنسيقات المتاحة."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "يرجى المحاولة مرة أخرى لاحقاً."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp لا يمكنه معالجة هذا المحتوى"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "يوصي النظام باستخدام gallery-dl بدلاً من ذلك."
    ALWAYS_ASK_OPTIONS_MSG = "**الخيارات:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• للمعرض الصور: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• للصور المفردة: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "gallery-dl يعمل غالباً بشكل أفضل مع Instagram و Twitter ومحتوى وسائل التواصل الاجتماعي الأخرى."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 جرب Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 التنسيق ثابت عبر /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 الترجمات"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 الصوت المدبلج"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — الترجمات متاحة"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — اختر لغة الترجمة"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ لم يتم العثور على الترجمات ولن يتم تضمينها"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — إعادة نشر فورية من التخزين المؤقت"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — اختر لغة الصوت"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞المحتوى غير المناسب مدفوع (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — اختر جودة التحميل"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — تحميل الصورة (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — مشاهدة الفيديو في poketube"  # معطل مؤقتًا: خدمة poketube معطلة
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — الحصول على رابط مباشر للفيديو"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — عرض قائمة التنسيقات المتاحة"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — تغيير امتداد/ترميز الفيديو"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀تضمين"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — استخراج الصوت فقط"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞المحتوى للبالغين مدفوع (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — إعادة نشر فورية من التخزين المؤقت"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — مشاهدة الفيديو في poketube"  # معطل مؤقتًا: خدمة poketube معطلة
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — اختيار لغة الصوت"
    ALWAYS_ASK_BEST_BUTTON_MSG = "الأفضل"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛أخرى"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝ترجمات فقط"
    ALWAYS_ASK_SMART_GROUPING_MSG = "التجميع الذكي"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "تم إضافة صف أزرار الإجراء (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "تم إضافة صفوف أزرار الإجراء (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "تم إضافة الأزرار السفلية إلى الصف الموجود"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "تم إنشاء صف سفلي جديد"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "لم يتم العثور على مقاطع فيديو في قائمة التشغيل"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "رابط غير مدعوم"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "لم يتم العثور على فيديو"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "لم يتم العثور على فيديو"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "لم يتم العثور على وسائط"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "هذه التغريدة لا تحتوي على"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>خطأ في استرجاع معلومات الفيديو:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "خطأ في استرجاع معلومات الفيديو"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "جرب أمر <code>/clean</code> وحاول مرة أخرى. إذا استمر الخطأ، يتطلب YouTube تفويضاً. حدث ملف cookies.txt عبر <code>/cookie</code> أو <code>/cookies_from_browser</code> وحاول مرة أخرى."
    ALWAYS_ASK_MENU_CLOSED_MSG = "تم إغلاق القائمة."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 اختيار الجودة اليدوي"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "اختر الجودة يدوياً لأن الكشف التلقائي فشل:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 جميع التنسيقات المتاحة"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 الجودات المتاحة (من التخزين المؤقت)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ استخدام الجودات المخزنة - قد لا تكون التنسيقات الجديدة متاحة"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 جاري تحميل التنسيق"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 جاري التحميل"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 جاري التحميل مع تتبع التقدم..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 جاري التحميل باستخدام التنسيق:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 جاري تحميل الصوت باستخدام التنسيق:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 جاري تحميل أفضل جودة..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 جاري تحميل نسخة احتياطية من قاعدة البيانات..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 جاري التحميل"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "صفحة التنسيقات"
    ALWAYS_ASK_FROM_CACHE_MSG = "(من التخزين المؤقت)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ خطأ: لم يتم العثور على الرسالة الأصلية. ربما تم حذفها. يرجى إرسال الرابط مرة أخرى."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ خطأ: لم يتم العثور على الرابط الأصلي. يرجى إرسال الرابط مرة أخرى."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>تم الحصول على الرابط المباشر</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>العنوان:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>المدة:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>التنسيق:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>تيار الفيديو:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>تيار الصوت:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ فشل في الحصول على روابط التيار"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "تم استخراج الرابط المباشر عبر قائمة السؤال دائماً للمستخدم {user_id} من {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "فشل في استخراج الرابط المباشر عبر قائمة السؤال دائماً للمستخدم {user_id} من {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "تم استخراج الرابط المباشر عبر down_and_up_with_format للمستخدم {user_id} من {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "فشل في استخراج الرابط المباشر عبر down_and_up_with_format للمستخدم {user_id} من {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "تم استخراج الرابط المباشر عبر down_and_audio للمستخدم {user_id} من {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "فشل في استخراج الرابط المباشر عبر down_and_audio للمستخدم {user_id} من {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ تم إرسال الصوت من التخزين المؤقت."
    AUDIO_PROCESSING_MSG = "🎙️ جاري معالجة الصوت..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 جاري تحميل الصوت:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "حدث خطأ أثناء تحميل الصوت."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ فشل في استخراج معلومات الصوت"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "تخطي نوع الملف غير المدعوم في قائمة التشغيل في الفهرس {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "لم يتم العثور على ملف الصوت بعد التحميل."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ فشل إرسال الصوت: حجم الملف يساوي 0 بايت (فهرس قائمة التشغيل {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ ملف الصوت لا يزال قيد التنزيل، يرجى الانتظار..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 جاري رفع ملف الصوت...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ فشل في إرسال الصوت: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "تم إرسال صوت قائمة التشغيل: {sent}/{total} ملف (الجودة={quality}) للمستخدم{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ فشل في تحميل الصوت: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ تم إلغاء التحميل بسبب انتهاء الوقت (ساعتان)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ لم يتم العثور على ملف الفيديو: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ فشل إرسال الفيديو: حجم الملف يساوي 0 بايت (فهرس قائمة التشغيل {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ ملف الفيديو لا يزال قيد التنزيل، يرجى الانتظار..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ خطأ في معالجة الفيديو: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ خطأ في إرسال ملف الوصف: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 إذا كنت تريد تغيير تسمية الفيديو - أجب على الفيديو بنص جديد</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "لم يتم اكتشاف ترجمات"
    VIDEO_PROGRESS_MSG = "<b>فيديو:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>صوت:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>رابط:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ تم تجاوز حد الروابط: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "اكتملت المعالجة"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ نطاقات قوائم التشغيل غير مسموحة في وضع الروابط المتعددة. أرسل روابط فردية فقط بدون نطاقات (*1*5، /vid 1-10، إلخ)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "تحقق <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>هنا</a> إذا كان موقعك مدعوماً"
    ERROR_COOKIE_NEEDED_MSG = "قد تحتاج <code>cookie</code> لتحميل هذا الفيديو. أولاً، نظف مساحة العمل عبر أمر <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "لـ YouTube - احصل على <code>cookie</code> عبر أمر <b>/cookie</b>. لأي موقع مدعوم آخر - أرسل ملف cookie الخاص بك (<a href='https://t.me/tg_ytdlp/203'>دليل1</a>) (<a href='https://t.me/tg_ytdlp/214'>دليل2</a>) وبعد ذلك أرسل رابط الفيديو مرة أخرى."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "اختر لغة الترجمة"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "لا توجد لغات صوت بديلة"
    CHOOSE_AUDIO_LANGUAGE_MSG = "اختر لغة الصوت"
    PAGE_NUMBER_MSG = "صفحة {page}"
    TOTAL_PROGRESS_MSG = "التقدم الإجمالي"
    SUBTITLE_MENU_CLOSED_MSG = "تم إغلاق قائمة الترجمة."
    SUBTITLE_LANGUAGE_SET_MSG = "تم تعيين لغة الترجمة: {value}"
    AUDIO_SET_MSG = "تم تعيين الصوت: {value}"
    FILTERS_UPDATED_MSG = "تم تحديث المرشحات"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙عودة"
    CLOSE_BUTTON_TEXT = "🔚إغلاق"
    LIST_BUTTON_TEXT = "📃قائمة"
    IMAGE_BUTTON_TEXT = "🖼صورة"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ لم يتم الكشف التلقائي عن الجودات\nاستخدم زر 'أخرى' لرؤية جميع التنسيقات المتاحة.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **تم اكتشاف بث مباشر**\n\nتحميل البث المباشر الجاري أو اللامحدود غير مسموح.\n\nيرجى انتظار انتهاء البث والمحاولة مرة أخرى عندما:\n• تصبح مدة البث معروفة\n• ينتهي البث\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>تحميل البث المباشر</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "الجزء {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "الحجم الأقصى: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "المدة الإجمالية: {duration} ثانية"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>البث المباشر - الجزء {chunk}</b>\n⏱ المدة: {duration} ثانية\n📦 الحجم: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "الجزء {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>اكتمل تحميل البث المباشر</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "تم تحميل {chunks} جزء(أجزاء)"
    LIVE_STREAM_TOTAL_DURATION_MSG = "المدة الإجمالية: {duration} ثانية"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>توقف تحميل البث المباشر</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "تم حذف مجلد المستخدم (على الأرجح بواسطة أمر /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "تم حذف ملف الجزء (على الأرجح بواسطة أمر /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ انتهى البث"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "يرجى اختيار تنسيق مختلف باستخدام أمر `/format`."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>تم الحصول على الرابط المباشر</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>العنوان:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>المدة:</b> {duration} ثانية\n"
    FORMAT_FIELD_MSG = "🎛 <b>التنسيق:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>تيار الفيديو:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>تيار الصوت:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **خطأ في معالجة الملف**\n\nتم تحميل الفيديو ولكن لا يمكن معالجته بسبب أحرف غير صحيحة في اسم الملف.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **خطأ في معالجة الملف**\n\nتم تحميل الفيديو ولكن لا يمكن معالجته بسبب خطأ في الوسيطة.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**السبب:**\n"
        "• الملف الذي تم تنزيله ليس ملف فيديو\n"
        "• قد يكون مستندًا (PDF، DOC، إلخ) أو أرشيفًا\n\n"
        "**الحل:**\n"
        "• تحقق من الرابط - قد يؤدي إلى مستند وليس فيديو\n"
        "• جرب رابطًا أو مصدرًا مختلفًا\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**السبب:**\n"
        "• لا يمكن معالجة الملف كفيديو\n"
        "• قد لا يكون ملف فيديو أو أن الملف تالف\n\n"
        "**الحل:**\n"
        "• تحقق من الرابط - قد يؤدي إلى مستند وليس فيديو\n"
        "• جرب رابطًا أو مصدرًا مختلفًا\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **التنسيق غير متاح**\n\nتنسيق الفيديو المطلوب غير متاح لهذا الفيديو.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ لم يتم العثور على معرف التنسيق {format_id} لهذا الفيديو.\n\nمعرفات التنسيق المتاحة: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **تنسيق AV1 غير متاح لهذا الفيديو.**\n\n**التنسيقات المتاحة:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **خطأ في معالجة الملف**\n\nتم تحميل الصوت ولكن لا يمكن معالجته بسبب أحرف غير صحيحة في اسم الملف.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **خطأ في معالجة الملف**\n\nتم تحميل الصوت ولكن لا يمكن معالجته بسبب خطأ في الوسيطة.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "دخل المستخدم محتوى محظور. لا يمكن تحميله."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "تم تعيين ضبابية المحتوى غير المناسب عبر الأمر: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "فتح المستخدم قائمة /nsfw."
    NSFW_MENU_CLOSED_LOG_MSG = "المحتوى غير المناسب: مغلق."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "فشل في تحميل ملف تعريف الارتباط {service}: status={status} (الرابط مخفي)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "خطأ في تحميل ملف تعريف الارتباط {service}: {error} (الرابط مخفي)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "خطأ غير متوقع أثناء تحميل ملف تعريف الارتباط {service} (الرابط مخفي): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "تم تحديث ملف تعريف الارتباط للمستخدم {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "محتوى ملف تعريف الارتباط غير صالح قدمه المستخدم {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "روابط ملفات تعريف الارتباط لـ YouTube فارغة للمستخدم {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "تم تحميل وتحقق ملفات تعريف الارتباط لـ YouTube للمستخدم {user_id} من المصدر {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "فشلت جميع مصادر ملفات تعريف الارتباط لـ YouTube للمستخدم {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "خطأ في أمر check_porn بواسطة المسؤول {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "تم تعيين حجم الجزء المقسم إلى {size} بايت."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "اكتمل رفع الفيديو مع تقسيم الملف."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "تم إرسال فيديوهات قائمة التشغيل: {sent}/{total} ملف (الجودة={quality}) للمستخدم {user_id}"
    UNKNOWN_ERROR_MSG = "❌ خطأ غير معروف: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "تخطي نوع الملف غير المدعوم في قائمة التشغيل في الفهرس {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ لم يتم العثور على FFmpeg. يرجى تثبيت FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ فشل التحويل إلى MP4: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ قد يستغرق تضمين الترجمات وقتاً طويلاً (حتى دقيقة واحدة لكل دقيقة من الفيديو)!\n🔥 بدء حرق الترجمات..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ لا يمكن تضمين الترجمات بسبب الحدود (الجودة/المدة/الحجم)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ الترجمات غير متاحة للغة المحددة"
    ERROR_SENDING_VIDEO_MSG = "❌ خطأ في إرسال الفيديو: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ تم إرسال فيديوهات قائمة التشغيل: {sent}/{total} ملف."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ تم إلغاء التحميل بسبب انتهاء الوقت (ساعتان)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ فشل في تحميل الفيديو: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ خطأ: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ يجب أن يكون JSON كائناً (قاموس)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ تنسيق JSON غير صالح. يرجى تقديم JSON صالح."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ يجب أن تكون القيمة بين {min_val} و {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ تم تعيين {description} إلى: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ صحيح"
    ARGS_FALSE_BUTTON_MSG = "❌ خطأ"
    ARGS_BACK_BUTTON_MSG = "🔙 عودة"
    ARGS_CLOSE_BUTTON_MSG = "🔚 إغلاق"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ صحيح"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ خطأ"
    ARGS_NOT_SET_MSG = "غير محدد"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["صحيح", "نعم", "أجل", "True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["خطأ", "لا", "ليس", "False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ تنسيق AV1 غير متاح لهذا الفيديو.\n\nالتنسيقات المتاحة:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ خطأ في التحميل: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ لم يتم العثور على فيديوهات في قائمة التشغيل في الفهرس {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **فشل تحويل الفيديو**\n\nلا يمكن تحويل الفيديو إلى MP4 بسبب خطأ في الوسيطة.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **فشل تحويل الفيديو**\n\nلا يمكن تحويل الفيديو إلى MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ فشل في الحصول على روابط التيار"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>خطأ في الحصول على الرابط:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ لم يتم العثور على محتوى في الفهرس {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ خطأ: لم يتم العثور على الرسالة الأصلية."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ خطأ: لم يتم العثور على الرابط."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ لا يمكن تضمين هذا الرابط."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ ترميز {codec} غير متاح لهذا الفيديو"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ تنسيق {format} غير متاح لهذا الفيديو"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ حد الفيضان. جرب لاحقاً."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ فحص ملف تعريف الارتباط"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ الكل (تلقائي)"
    PROXY_OFF_BUTTON_MSG = "❌ إيقاف"
    PROXY_CLOSE_BUTTON_MSG = "🔚إغلاق"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 اختر الدولة:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ مسح اختيار البلد"
    PROXY_COUNTRY_SELECTED_MSG = "✅ الدولة المحددة: {country} (الرمز: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 الوكلاء المتاحون: {proxy_count} (HTTP: {http_count}، SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 سيحاول البوت استخدام HTTP أولاً، ثم SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 تم تمكين الوكيل تلقائيًا للبلد المحدد"
    PROXY_COUNTRY_CLEARED_MSG = "✅ تم مسح اختيار البلد"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ تم مسح اختيار البلد"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ البلد المحدد: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 استخدام البلد من الملف: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 الدول المتاحة من الملف: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 الدولة المختارة: {country} (الرمز: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ تمكين الوكيل لهذا البلد"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ تم تعطيل الوكيل (اضغط الكل (AUTO) للتمكين)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ تشغيل"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ إيقاف"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚إغلاق"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV: تشغيل"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV: إيقاف"
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ تشغيل (بدون ضبابية)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ تشغيل (بدون ضبابية)"
    NSFW_OFF_BLUR_MSG = "✅ إيقاف (ضبابية)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ إيقاف (ضبابية)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "نظيف"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "خطأ في معالجة رسالة الرد للمستخدم {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "خطأ في إرسال البث للمستخدم {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "سجلات {bot_name}\nالمستخدم: {user_id}\nإجمالي السجلات: {total}\nالوقت الحالي: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nإجمالي {path}: {count}\nالوقت الحالي: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>إجمالي المستخدمين: {count}</i>\nآخر 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "تم إعادة تحميل ذاكرة التخزين المؤقت للمحتوى الإباحي بواسطة المسؤول {admin_id}. النطاقات: {domains}، الكلمات المفتاحية: {keywords}، المواقع: {sites}، القائمة البيضاء: {whitelist}، القائمة الرمادية: {greylist}، القائمة السوداء: {black_list}، الكلمات المفتاحية البيضاء: {white_keywords}، نطاقات البروكسي: {proxy_domains}، نطاقات البروكسي 2: {proxy_2_domains}، الاستعلام النظيف: {clean_query}، نطاقات بدون ملفات تعريف الارتباط: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "خطأ في إرسال رسالة انتهاء الوقت: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>اختر اللغة</b>"
    LANG_CHANGED_MSG = "✅ تم تغيير اللغة إلى {lang_name}"
    LANG_ERROR_MSG = "❌ خطأ في تغيير اللغة"
    LANG_CLOSED_MSG = "تم إغلاق اختيار اللغة"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[المتصفح] استدعاء: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "إضافة زر مراقبة المتصفح مع الرابط: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "رابط مراقبة المتصفح غير مُكوَّن: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **تم تحديث إعداد لوحة المفاتيح!**\n\nالإعداد الجديد: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "فشل في إخفاء لوحة المفاتيح: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "استخدام ملفات تعريف الارتباط العاملة لـ YouTube لاستخراج الرابط للمستخدم {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "لا توجد ملفات تعريف ارتباط عاملة لـ YouTube متاحة لاستخراج الرابط للمستخدم {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "استخدام ملفات تعريف الارتباط الموجودة لـ YouTube لاستخراج الرابط للمستخدم {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "لم يتم العثور على ملفات تعريف ارتباط لـ YouTube لاستخراج الرابط للمستخدم {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "تم نسخ ملف تعريف الارتباط العام إلى مجلد المستخدم {user_id} لاستخراج الرابط"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[معلومات الوسائط] طلب المستخدم {user_id} أمر معلومات الوسائط"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[معلومات الوسائط] المستخدم {user_id} مسؤول: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[معلومات الوسائط] المستخدم {user_id} في القناة: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[معلومات الوسائط] تم رفض الوصول للمستخدم {user_id} - ليس مسؤولاً وليس في القناة"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[معلومات الوسائط] تم منح الوصول للمستخدم {user_id}"
    MEDIAINFO_CALLBACK_MSG = "[معلومات الوسائط] استدعاء: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ هذا الأمر متاح للمسؤولين فقط."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ اكتمل التحميل مع دعم رمز PO"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ حد الفيضان. جرب لاحقاً."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ خطأ في تحديث رمز REST: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ خطأ في إغلاق جلسة Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ خطأ في تهيئة هيكل قاعدة البيانات الأساسية: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ لم يتم تعيين جميع المعاملات في config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL غير مُعيّن"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey غير مُعيّن للحصول على idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ خطأ في تحميل نسخة Firebase: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ فشل في تحميل نسخة Firebase عبر REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ خطأ في _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ خطأ في تشغيل إعادة تحميل التخزين المؤقت التلقائي (محاولة {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ فشلت جميع محاولات إعادة المحاولة"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 بدء تحميل نسخة Firebase في {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ التبعية غير متاحة: requests أو Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ قاعدة البيانات فارغة"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ خطأ في إغلاق المسجل: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ خطأ أثناء التنظيف: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ خطأ في الاستنساخ: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ انتهت مهلة الاستنساخ"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ استثناء الاستنساخ: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ تم إلغاء التحديث بواسطة المستخدم"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ تم استنساخ المستودع بنجاح"
    UPDATE_BACKUPS_MOVED_MSG = "✅ تم نقل النسخ الاحتياطية إلى _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ تم تحميل جميع الوحدات"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ اكتمل التنظيف عند الخروج"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 تم استلام الإشارة {signal}، إغلاق بأمان..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "يرجى الانتظار..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 جاري تحميل تيار HLS:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "انتظار الأجزاء"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ لم يتم العثور على النسخة الاحتياطية {ts} في _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ فشل في استعادة {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ تم الاستعادة: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>الرابط:</b> <code>{url}</code>\n\n<b>التفاصيل:</b> {error_details}\n\nتم إيقاف التحميل بسبب خطأ حرج.\n\n💡 <b>نصيحة:</b> إذا كنت تحصل على خطأ 401 غير مصرح، جرب استخدام أمر <code>/cookie instagram</code> أو أرسل ملفات تعريف الارتباط الخاصة بك للمصادقة مع Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ النطاق في القائمة السوداء للمحتوى الإباحي: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ تم العثور على كلمات مفتاحية إباحية: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ النطاق في القائمة البيضاء: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ تم العثور على كلمات مفتاحية في القائمة البيضاء: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ لم يتم العثور على كلمات مفتاحية إباحية"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ خطأ في TikTok API في الفهرس {index}، تخطي إلى الصوت التالي..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ خطأ في TikTok API في الفهرس {index}، تخطي إلى الفيديو التالي..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "دخل المستخدم <b>رابط</b>\n <b>اسم المستخدم:</b> {user_name}\nالرابط: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>دخل المستخدم هكذا:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "انضم إلى القناة"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 تسجيل المعالج: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - تحميل ملفات تعريف الارتباط الخمسة الخاصة بي"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - الحصول على ملف تعريف ارتباط YouTube من المتصفح"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - التحقق من صحة ملف تعريف الارتباط الخاص بك"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - رفع ملف تعريف ارتباط مخصص"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 إغلاق"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "التنسيقات المتاحة لـ: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚إغلاق"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚إغلاق"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚إغلاق"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚إغلاق"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "تم إغلاق المساعدة."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "تم الإغلاق"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "حدث خطأ"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "لم يتم العثور على ffmpeg في PATH أو مجلد المشروع. يرجى تثبيت FFmpeg."
    YTDLP_NOT_FOUND_MSG = "لم يتم العثور على yt-dlp binary في PATH أو مجلد المشروع. يرجى تثبيت yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "سيتم تقسيم الفيديو إلى {rounds} جزء، مما قد يكون مفرطاً"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "تقسيم جزء الفيديو {current}/{total}: من {start_time:.2f}ث إلى {end_time:.2f}ث"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "فشل في إنشاء الجزء المقسم {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "تم إنشاء الجزء المقسم {part} بنجاح: {target_name} ({size} بايت)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "خطأ في تقسيم جزء الفيديو {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "تم تقسيم الفيديو إلى {count} جزء بنجاح"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "خطأ في عملية تقسيم الفيديو: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] خطأ أثناء معالجة الفيديو {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "ملف الفيديو غير موجود: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "خطأ في تحليل الأبعاد '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "لا يمكن تحديد أبعاد الفيديو من '{size_result}'، استخدام الافتراضي: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "خطأ في إنشاء الصورة المصغرة: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "خطأ في تحليل مدة الفيديو: {error}، النتيجة كانت: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "لم يتم إنشاء الصورة المصغرة في {thumb_dir}، استخدام الافتراضي"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "خطأ في تنفيذ الأمر: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "خطأ في إنشاء الصورة المصغرة مع FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "تخطي قسم التكوين غير القاموسي: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "تعيين {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] استخدام ملفات تعريف الارتباط للمستخدم: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "استخدام ملفات تعريف الارتباط لـ YouTube للمستخدم {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "تم نسخ ملف تعريف الارتباط العام إلى مجلد المستخدم {user_id}"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] استخدام ملفات تعريف الارتباط العامة المنسوخة كملفات تعريف ارتباط للمستخدم: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "فشل نسخ ملف تعريف الارتباط العام للمستخدم {user_id}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "استخدام --no-cookies للنطاق: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "تم طلب وكيل ولكن فشل استيراد/الحصول على التكوين: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "فرض استخدام الوكيل لـ gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "تم طلب البروكسي ولكن تكوين البروكسي غير مكتمل"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "فشل مساعد الوكيل: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "جاري تحليل عناصر المستخرج..."
    GALLERY_DL_ITEM_COUNT_MSG = "العنصر {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "تم العثور على بيانات وصفية (علامة 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "تم العثور على رابط (علامة 3): {url}، بيانات وصفية: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "تم العثور على بيانات وصفية (قديمة): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "تم العثور على رابط (قديم): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "تم العثور على اسم الملف: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "تم العثور على الدليل: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "تم العثور على الامتداد: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "تم تحليل {count} عنصر، معلومات: {info}، احتياطي: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "تعيين تكوين gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "محاولة الاستراتيجية أ: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "وحدة gallery_dl.extractor غير موجودة"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() غير متاح في هذا البناء"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "استدعاء extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "لا يوجد مستخرج يطابق الرابط"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "تعيين ملفات تعريف الارتباط على المستخرج: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "فشل في تعيين ملفات تعريف الارتباط على المستخرج: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "تم العثور على المستخرج، استدعاء items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "نجحت الاستراتيجية أ، حصلت على معلومات: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "الاستراتيجية أ: extractor.items() لم تُرجع معلومات صحيحة"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "فشلت الاستراتيجية أ (extractor.find): {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "بيانات وصفية احتياطية من --get-urls: إجمالي={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "فشلت جميع الاستراتيجيات في الحصول على البيانات الوصفية"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "فشل في استخراج معلومات الصورة: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "وحدة gallery_dl.job غير موجودة (تثبيت معطل؟)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob غير متاح في هذا البناء"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "البحث عن الملفات المحملة في مجلد gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "محاولة العثور على الملفات بالأسماء من المستخرج"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "خطأ في قراءة معاملات المستخدم {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] خطأ أثناء معالجة الفيديو {video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "المستخدم {user_id} لديه send_as_file مفعل، إرسال كوثيقة"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "انتهت مهلة send_video بشكل متكرر؛ العودة إلى send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "التسمية طويلة جداً، محاولة مع تسمية مختصرة"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "انتهت مهلة send_video (تسمية مختصرة)؛ العودة إلى send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "خطأ في إرسال الفيديو مع تسمية مختصرة: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "خطأ في إرسال ملف الوصف الكامل: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "خطأ في إزالة ملف الوصف المؤقت: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "تخطي match_filter للنطاق في NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "فحص ملفات تعريف الارتباط الموجودة لـ YouTube على رابط المستخدم لكشف التنسيق للمستخدم {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "ملفات تعريف الارتباط الموجودة لـ YouTube تعمل على رابط المستخدم لكشف التنسيق للمستخدم {user_id} - استخدامها"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "فشلت ملفات تعريف الارتباط الموجودة لـ YouTube على رابط المستخدم، محاولة الحصول على ملفات جديدة لكشف التنسيق للمستخدم {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "محاولة مصدر ملف تعريف الارتباط لـ YouTube {i} لكشف التنسيق للمستخدم {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "ملفات تعريف الارتباط لـ YouTube من المصدر {i} تعمل على رابط المستخدم لكشف التنسيق للمستخدم {user_id} - محفوظة في مجلد المستخدم"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "ملفات تعريف الارتباط لـ YouTube من المصدر {i} لا تعمل على رابط المستخدم لكشف التنسيق للمستخدم {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "فشل في تحميل ملفات تعريف الارتباط لـ YouTube من المصدر {i} لكشف التنسيق للمستخدم {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "فشلت جميع مصادر ملفات تعريف الارتباط لـ YouTube لكشف التنسيق للمستخدم {user_id}، سيتم المحاولة بدون ملفات تعريف الارتباط"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "لا توجد مصادر ملفات تعريف ارتباط لـ YouTube مُكوَّنة لكشف التنسيق للمستخدم {user_id}، سيتم المحاولة بدون ملفات تعريف الارتباط"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "لم يتم العثور على ملفات تعريف ارتباط لـ YouTube لكشف التنسيق للمستخدم {user_id}، محاولة الحصول على ملفات جديدة"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "استخدام ملفات تعريف الارتباط لـ YouTube لكشف التنسيق للمستخدم {user_id} (تم التحقق منها بالفعل في قائمة Always Ask)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "لم يتم العثور على ملفات تعريف ارتباط لـ YouTube لكشف التنسيق للمستخدم {user_id}، محاولة الاستعادة..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "تم نسخ ملف تعريف الارتباط العام إلى مجلد المستخدم {user_id} لكشف التنسيق"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "فشل في نسخ ملف تعريف الارتباط العام للمستخدم {user_id}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "استخدام --no-cookies للنطاق في get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "التطبيق لم يتم تهيئته بعد. لا يمكن الوصول إلى {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>التسمية:</b> <code>{caption}</code>\n<b>معرف المستخدم:</b> <code>{user_id}</code>\n<b>الاسم الأول للمستخدم:</b> <code>{users_name}</code>\n<b>معرف ملف الفيديو:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "خطأ في محرر التسمية: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "خطأ غير متوقع في محرر التسمية: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 رابط الفيديو</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL غير موجود في التكوين"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ تم تهيئة firebase_admin"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 تم تحديث REST idToken"
    DB_LOG_FOR_USER_ADDED_MSG = "تم إضافة سجل للمستخدم"
    DB_DATABASE_CREATED_MSG = "تم إنشاء قاعدة البيانات"
    DB_BOT_STARTED_MSG = "تم بدء البوت"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "تم حفظ RELOAD_CACHE_EVERY في config.py: {hours}ساعة"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "جزء قائمة التشغيل مُخزن مؤقتاً بالفعل: {path_parts}، تخطي"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: لم يتم العثور على تخزين مؤقت لأي متغير URL/جودة، إرجاع قاموس فارغ"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: عدد سريع للمدى الكبير: {cached_count} فيديو مخزن مؤقتاً"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: لم يتم العثور على تخزين مؤقت للهاش {url_hash}، الجودة {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: لم يتم العثور على تخزين مؤقت لأي متغير URL، إرجاع None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ تم رفض الوصول. للمدير فقط."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 تم تحديث إعادة تحميل تخزين Firebase المؤقت التلقائي!\n\n📊 الحالة: {status}\n⏰ الجدولة: كل {interval} ساعة من 00:00\n🕒 إعادة التحميل التالية: {next_exec} (خلال {delta_min} دقيقة)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 تم إيقاف إعادة تحميل تخزين Firebase المؤقت التلقائي!\n\n📊 الحالة: ❌ معطل\n💡 استخدم /auto_cache on لإعادة التفعيل"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ وسيطة غير صحيحة. استخدم /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ يجب أن يكون الفاصل بين 1 و 168 ساعة"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ فشل في تعيين الفاصل"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ تم تحديث فاصل تخزين Firebase المؤقت التلقائي!\n\n📊 الحالة: ✅ مفعل\n⏰ الجدولة: كل {interval} ساعة من 00:00\n🕒 إعادة التحميل التالية: {next_exec} (خلال {delta_min} دقيقة)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 بدأت إعادة تحميل تخزين Firebase المؤقت التلقائي!\n\n📊 الحالة: ✅ مفعل\n⏰ الجدولة: كل {interval} ساعة من 00:00\n🕒 إعادة التحميل التالية: {next_exec} (خلال {delta_min} دقيقة)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 تم إيقاف إعادة تحميل تخزين Firebase المؤقت التلقائي!\n\n📊 الحالة: ❌ معطل\n💡 استخدم /auto_cache on لإعادة التفعيل"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "إعادة التحميل التلقائي مفعل؛ التالية في {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "تم تعطيل إعادة التحميل التلقائي بواسطة المدير."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "تم تعيين فاصل إعادة التحميل التلقائي إلى {interval}ساعة؛ التالية في {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "بدأت إعادة التحميل التلقائي؛ التالية في {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "تم إيقاف إعادة التحميل التلقائي بواسطة المدير."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ تم تحميل تخزين Firebase المؤقت: {count} عقدة جذر"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ لم يتم العثور على ملف تخزين Firebase المؤقت، البدء بتخزين مؤقت فارغ: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ فشل في تحميل تخزين Firebase المؤقت: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ تم إعادة تحميل تخزين Firebase المؤقت: {count} عقدة جذر"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ لم يتم العثور على ملف تخزين Firebase المؤقت: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ فشل في إعادة تحميل تخزين Firebase المؤقت: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 أنت محظور من البوت! لإلغاء الحظر، اتصل بـ {Config.ADMIN_USERNAME}\n<blockquote>P.S. لا تغادر القناة - سيتم حظرك تلقائياً ⛔️</blockquote>\n🌍تغيير اللغة /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ لم يتم العثور على تنسيقات فيديو. جاري تجربة محمل الصور…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram حد من إرسال الرسائل.\n⏳ يرجى الانتظار: {time_str}\nلتحديث المؤقت أرسل الرابط مرة أخرى مرتين."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>انقر على الزر لنسخ رابط التيار، ثم الصقه في تطبيق VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>انقر على الزر لنسخ رابط التيار، ثم الصقه في تطبيق VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>خطأ في الحصول على الرابط:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ خطأ في إرسال ملف التنسيقات: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ فشل في الحصول على التنسيقات:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 جاري التحليل... (انتظر 6 ثوان)"
    AA_PROCESSING_MSG = "🔎 جاري التحليل..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ العلامة #{wrong} تحتوي على أحرف محظورة. فقط الحروف والأرقام و _ مسموحة.\nيرجى استخدام: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ للعمل في المجموعة يحتاج البوت إلى صلاحيات المدير. يرجى جعل البوت مديراً لهذه المجموعة."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "مرحباً {first_name}،\n \n<i>هذا البوت🤖 يمكنه تحميل أي فيديوهات إلى Telegram مباشرة.😊 لمزيد من المعلومات اضغط <b>/help</b></i> 👈\n\n<blockquote>P.S. تحميل 🔞المحتوى السميح والملفات من ☁️Cloud Storage هو مدفوع! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ لا تغادر القناة - سيتم حظرك من استخدام البوت ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 لا توجد ملفات للحذف."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 تم حذف جميع الملفات بنجاح!\n\nالملفات المحذوفة:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ انتظر حتى ينتهي التحميل السابق"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "مثيل التطبيق هو None في check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict هو None، السماح بالتحميل"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict هو None، السماح بتضمين الترجمة"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: فحص الحدود - أقصى جودة={max_quality}p، أقصى مدة={max_duration}s، أقصى حجم={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: مفاتيح info_dict: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "تم تخطي تضمين الترجمة: المدة {duration}ثانية تتجاوز الحد {max_duration}ثانية"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "تم تخطي تضمين الترجمة: الحجم {size_mb:.2f}MB يتجاوز الحد {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "تم تخطي تضمين الترجمة: الجودة {width}x{height} (الضلع الأدنى {min_side}p) تتجاوز الحد {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "قائمة تشغيل"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ تم تجاوز حد النطاق لـ {service}: {count} (الحد الأقصى {max_count}).\n\nاستخدم أحد هذه الأوامر لتحميل أقصى عدد من الملفات المتاحة:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ تم تجاوز حد النطاق لـ {service}: {count} (الحد الأقصى {max_count})\nمعرف المستخدم: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "مزود رمز PO معطل في التكوين"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "الرابط {url} ليس نطاق YouTube، تخطي رمز PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "مزود رمز PO غير متاح في {base_url}، العودة إلى استخراج YouTube القياسي"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "تم مسح تخزين مزود رمز PO المؤقت، سيتم فحص التوفر في الطلب التالي"
    HELPER_POT_GENERIC_ARGS_MSG = "عام:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "مثيل التطبيق غير متاح بعد"
    HELPER_USER_NAME_MSG = "المستخدم"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "تم اكتشاف انتظار الفيضان، النوم لمدة {wait_seconds} ثانية"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "تم اكتشاف انتظار الفيضان ولكن لا يمكن استخراج الوقت، النوم لمدة {retry_delay} ثانية"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "تم اكتشاف خطأ msg_seqno، النوم لمدة {retry_delay} ثانية"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "تكوين البروكسي غير مكتمل، استخدام الاتصال المباشر"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚إغلاق"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚إغلاق"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "مخصص"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚إغلاق"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 تم حذف ملف السجلات."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 تم حذف ملف العلامات."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 تم حذف ملف التنسيق."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 تم حذف ملف التقسيم."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 تم حذف ملف معلومات الوسائط."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 تم حذف إعدادات الترجمة."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 تم حذف إعدادات لوحة المفاتيح."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 تم حذف إعدادات الوسائط."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 تم حذف إعدادات NSFW."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 تم حذف إعدادات البروكسي."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 تم حذف إعدادات انتظار الفيضان."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚إغلاق"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 أمر تحميل الفيديو"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "الاستخدام: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "أمثلة:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (ترتيب مباشر)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (ترتيب عكسي)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "انظر أيضاً: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "المستخدم {user_id} أغلق أمر add_bot_to_group"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "فشل في استخراج معرف YouTube"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "فشل في تحميل الصورة المصغرة أو أنها كبيرة جداً"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "اختر لغة الصوت"
    AA_NO_SUBTITLES_DETECTED_MSG = "لم يتم اكتشاف ترجمات"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "اختر لغة الترجمة"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "خطأ في المصادقة"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "الحساب غير موجود"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "الحساب غير متاح"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "تم تجاوز حد المعدل"
    GALLERY_DL_NETWORK_ERROR_MSG = "خطأ في الشبكة"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "المحتوى غير متاح"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "قيود جغرافية"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "مطلوب التحقق"
    GALLERY_DL_POLICY_VIOLATION_MSG = "انتهاك السياسة"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "خطأ غير معروف"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ بدأ التحميل</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚إغلاق"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 أمر تحميل الفيديو</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "الاستخدام: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>أمثلة:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "انظر أيضاً: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ حد الفيضان. جرب لاحقاً."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 استخدام أمر ملفات تعريف الارتباط</b>

<code>/cookie</code> - إظهار قائمة ملفات تعريف الارتباط
<code>/cookie youtube</code> - تحميل ملفات تعريف ارتباط YouTube
<code>/cookie instagram</code> - تحميل ملفات تعريف ارتباط Instagram
<code>/cookie tiktok</code> - تحميل ملفات تعريف ارتباط TikTok
<code>/cookie x</code> أو <code>/cookie twitter</code> - تحميل ملفات تعريف ارتباط Twitter/X
<code>/cookie facebook</code> - تحميل ملفات تعريف ارتباط Facebook
<code>/cookie custom</code> - إظهار تعليمات ملفات تعريف الارتباط المخصصة

<i>الخدمات المتاحة تعتمد على تكوين البوت.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 تم إزالة ملف تعريف الارتباط ومسح التخزين المؤقت."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ السابق"
    SUBS_BACK_BUTTON_MSG = "🔙عودة"
    SUBS_OFF_BUTTON_MSG = "🚫 إيقاف"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - تعيين اللغة"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - تعيين اللغة مع تفعيل AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "الخيارات الصحيحة:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 اللغة"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 GitHub المطور"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 GitHub المساهم"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 تنظيف"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 ملفات تعريف الارتباط"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 الوسائط"
    SETTINGS_INFO_BUTTON_MSG = "📖 معلومات"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ المزيد"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 ملفات تعريف الارتباط فقط"
    SETTINGS_LOGS_BUTTON_MSG = "📃 السجلات "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ العلامات"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 التنسيق"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ التقسيم"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 معلومات الوسائط"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 الترجمات"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 لوحة المفاتيح"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ الوسائط"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 محتوى غير مناسب"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 البروكسي"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 انتظار الفيضان"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  جميع الملفات"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - تحميل ملفات تعريف الارتباط الخمسة الخاصة بي"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - الحصول على ملف تعريف ارتباط YT من المتصفح"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - التحقق من ملف تعريف الارتباط"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - رفع ملف تعريف ارتباط مخصص"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - تغيير الجودة والتنسيق"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - تشغيل / إيقاف MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - تغيير حجم جزء الفيديو المقسم"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - تحميل الفيديو كصوت"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - إعدادات لغة الترجمات"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - كيفية تحميل قوائم التشغيل"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - تحميل الصور عبر gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - إرسال علاماتك #"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - الحصول على التعليمات"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - إرسال سجلاتك"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - مساعدة قائمة التشغيل"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - كيفية الإضافة"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - الحصول على روابط الفيديو المباشرة"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - تفعيل/إيقاف البروكسي"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - تخطيط لوحة المفاتيح"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - مساعد البحث المضمن"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - وسائط yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - إعدادات ضبابية المحتوى غير المناسب"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 خيارات التنظيف</b>\n\nاختر ما تريد تنظيفه:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 الهاتف المحمول: تفعيل بحث @vid"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 الهاتف المحمول: تفعيل بحث @vid"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 إيقاف"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 كامل"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[رابط الصور]({url})"
    IMAGE_ERROR_MSG = "❌ خطأ: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙عودة"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - تنسيق مخصص"
    FORMAT_720P_MSG = "• <code>/format 720</code> - جودة 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - جودة 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - جودة 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - معرف تنسيق محدد"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - عرض القائمة دائماً"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/أفضل جودة"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ اسأل دائماً (قائمة + أزرار)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 أخرى (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (الأفضل لـ PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (الأفضل للهاتف Telegram)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (أقصى جودة)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 مخصص (أدخل الخاص بك)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 من المتصفح"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 الخاص بك"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ تم إغلاق وضع الإدخال تلقائياً بسبب عدم النشاط (5 دقائق)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 إعادة تعيين الكل"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 عرض الحالي"
    ARGS_BACK_BUTTON_MSG = "🔙 عودة"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>أعد توجيه هذه الرسالة إلى مفضلاتك لحفظ هذه الإعدادات كقالب.</i> \n\n<i>أعد توجيه هذه الرسالة هنا لتطبيق هذه الإعدادات.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 وسائط yt-dlp الحالية:\n\nلم يتم تكوين إعدادات مخصصة.\n\n---\n\n<i>أعد توجيه هذه الرسالة إلى مفضلاتك لحفظ هذه الإعدادات كقالب.</i> \n\n<i>أعد توجيه هذه الرسالة هنا لتطبيق هذه الإعدادات.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 وسائط yt-dlp الحالية:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 تصدير الإعدادات"
    ARGS_SETTINGS_READY_MSG = "الإعدادات جاهزة للتصدير! أعد توجيه هذه الرسالة إلى المفضلة للحفظ."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 وسائط yt-dlp الحالية:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ فشل في التعرف على الإعدادات في الرسالة. تأكد من إرسال قالب إعدادات صحيح."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ تم استيراد الإعدادات بنجاح!\n\nالمعاملات المطبقة: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "الإعدادات الرئيسية:\n"
    ARGS_ERROR_SAVING_MSG = "❌ خطأ في حفظ الإعدادات المستوردة."
    ARGS_ERROR_IMPORTING_MSG = "❌ حدث خطأ أثناء استيراد الإعدادات."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>تحميل ملفات Cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "اختر خدمة لتحميل ملف cookie."
    COOKIE_MENU_SAVE_INFO_MSG = "سيتم حفظ ملفات cookie كـ cookie.txt في مجلدك."
    COOKIE_MENU_TIP_HEADER_MSG = "نصيحة: يمكنك أيضاً استخدام الأمر المباشر:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – تحميل والتحقق من cookies"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – استخدام مصدر محدد بالفهرس (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "ثم تحقق باستخدام <code>/check_cookie</code> (يختبر على RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "اسأل دائماً"
    SUBS_AUTO_TRANS_BUTTON_MSG = "تلقائي/ترجمة"

    # Always Ask menu button messages
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ قص"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>قص الفيديو</b>\n\nمدة الفيديو: <b>{start_time} - {end_time}</b>\n\nيرجى إرسال النطاق الزمني المطلوب بالتنسيق:\n<code>س:د:ث-س:د:ث</code>\n\nمثال: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ تنسيق غير صحيح. يرجى استخدام: <code>س:د:ث-س:د:ث</code>\n\nمثال: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ نطاق غير صحيح. يجب أن يكون وقت البداية أقل من وقت النهاية."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ النطاق الزمني خارج حدود الفيديو.\n\nمدة الفيديو: <b>{start_time} - {end_time}</b>\n\nيجب أن يكون النطاق الخاص بك ضمن هذه الحدود."
    AA_ERROR_VIDEO_DURATION_UNKNOWN_MSG = "❌ لم يتم تحديد مدة الفيديو. يرجى المحاولة مرة أخرى أو استخدام فيديو آخر."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>سيتم قص الفيديو:</b> {start_time} - {end_time}"
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗رابط"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁مشاهدة"  # معطل مؤقتًا: خدمة poketube معطلة
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝الوصف"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ مكتمل جزئياً - {successful_uploads}/{total_files} ملف صوتي تم رفعه."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ تم تحميل وإرسال الصوت بنجاح - {total_files} ملف تم رفعه."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>حساب TikTok خاص</b>\n\n"
        "هذا الحساب في TikTok خاص أو جميع الفيديوهات خاصة.\n\n"
        "<b>💡 الحل:</b>\n"
        "1. تابع الحساب @{username}\n"
        "2. أرسل ملفات cookie الخاصة بك للبوت باستخدام أمر <code>/cookie</code>\n"
        "3. جرب مرة أخرى\n\n"
        "<b>بعد تحديث cookies، جرب مرة أخرى!</b>"
    )

    #######################################################
