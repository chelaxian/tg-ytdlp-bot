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
    CREDITS_MSG = "<blockquote><i>Boshqaruvchi</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Tilni o'zgartirish: /lang</b>"
    TO_USE_MSG = "<i>Ushbu botdan foydalanish uchun @tg_ytdlp Telegram kanaliga obuna bo'lishingiz kerak.</i>\nKanalga qo'shilgandan so'ng <b>video havolangizni qayta yuboring, bot uni siz uchun yuklab oladi</b> ❤️\n\n<blockquote>P.S. 🔞NSFW kontent ehtimoli tufayli - ☁️<b>Bulutli saqlash</b>, 📁<b>Fayl ulashish</b>, 🔗<b>URL qisqartirgichlar</b> va 🔞<b>Porno saytlardan</b> yuklab olish pullik! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ @tg_ytdlp kanalini 🗑<b>o'chirmang/obunani bekor qilmang</b> va botga 🤖<b>URL/buyruqlarni ortiqcha spam qilmang</b> - botdan foydalanishdan avtomatik chetlashtirilasiz ⛔️</blockquote>"

    ERROR1 = "URL havolasi topilmadi. Iltimos, <b>https://</b> yoki <b>http://</b> bilan URL kiriting"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Pleylistlar (yt-dlp)</b>

Pleylistlarni yuklab olish uchun uning URL manzilini oxirida <code>*start*end</code> diapazonlari bilan yuboring. Masalan: <code>URL*1*5</code> (1 dan 5 gacha birinchi 5 ta video).<code>URL*-1*-5</code> (1 dan 5 gacha oxirgi 5 ta video).
Yoki <code>/vid DAN-GACHA URL</code> dan foydalanishingiz mumkin. Masalan: <code>/vid 3-7 URL</code> (boshidan 3 dan 7 gacha videolarni yuklaydi). <code>/vid -3-7 URL</code> (oxiridan 3 dan 7 gacha videolarni yuklaydi). <code>/audio</code> buyrug'i uchun ham ishlaydi.

<b>Misollar:</b>

🟥 <b>YouTube pleylistidan video diapazoni:</b> (🍪 kerak)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(1 dan 5 gacha birinchi 5 ta videoni yuklaydi)
🟥 <b>YouTube pleylistidan bitta video:</b> (🍪 kerak)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(faqat 3-videoni yuklaydi)

⬛️ <b>TikTok profil:</b> (sizning 🍪 kerak)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(foydalanuvchi profilidan birinchi 10 ta videoni yuklaydi)

🟪 <b>Instagram hikoyalari:</b> (sizning 🍪 kerak)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(birinchi 3 ta hikoyani yuklaydi)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(albomdan birinchi 10 ta hikoyani yuklaydi)

🟦 <b>VK videolari:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(foydalanuvchi/guruh profilidan birinchi 3 ta videoni yuklaydi)

⬛️<b>Rutube kanallari:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(kanaldan 2 dan 4 gacha videolarni yuklaydi)

🟪 <b>Twitch klip'lari:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(kanaldan birinchi 3 ta klipni yuklaydi)

🟦 <b>Vimeo guruhlari:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(guruhdan birinchi 2 ta videoni yuklaydi)

🟧 <b>Pornhub modellari:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(model profilidan birinchi 2 ta videoni yuklaydi)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(sizning so'rovingiz bo'yicha qidiruv natijalaridan birinchi 3 ta videoni yuklaydi)

va hokazo...
<a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">qo'llab-quvvatlanadigan saytlar ro'yxati</a>ni ko'ring
</blockquote>

<blockquote expandable>🖼 <b>Rasmlar (gallery-dl)</b>

Ko'plab platformalardan rasmlar/fotolar/albomlarni yuklab olish uchun <code>/img URL</code> dan foydalaning.

<b>Misollar:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Diapazonlar:</b>
<code>/img 11-20 https://example.com/album</code> — elementlar 11..20
<code>/img 11- https://example.com/album</code> — 11 dan oxirigacha (yoki bot limiti)

<i>Qo'llab-quvvatlanadigan platformalar vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor va boshqalarni o'z ichiga oladi. To'liq ro'yxat:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">gallery-dl tomonidan qo'llab-quvvatlanadigan saytlar</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Video Yuklab Olish Boti - Yordam</b>

📥 <b>Asosiy Foydalanish:</b>
• Har qanday havolani yuboring → bot uni yuklab oladi
  <i>bot avtomatik ravishda yt-dlp orqali videolarni va gallery-dl orqali rasmlarni yuklab olishga harakat qiladi.</i>
• <b>Bir nechta URL:</b> Sifat tanlash rejimida (<code>/format</code>) bir xabarda <b>10 tagacha URL</b> yuborishingiz mumkin. Har bir URL yangi qatorda yoki bo'shliqlar bilan ajratilgan.
• <code>/audio URL</code> → audioni ajratib olish
• <code>/link [quality] URL</code> → to'g'ridan-to'g'ri havolalarni olish
• <code>/proxy</code> → barcha yuklab olishlar uchun proksini yoqish/o'chirish
• Videoga matn bilan javob bering → sarlavhani o'zgartirish

📋 <b>Pleylistlar va Diapazonlar:</b>
• <code>URL*1*5</code> → birinchi 5 ta videoni yuklab olish
• <code>URL*-1*-5</code> → oxirgi 5 ta videoni yuklab olish
• <code>/vid 3-7 URL</code> → <code>URL*3*7</code> bo'ladi
• <code>/vid -3-7 URL</code> → <code>URL*-3*-7</code> bo'ladi

🍪 <b>Cookie va Maxfiy:</b>
• Maxfiy videolar uchun *.txt cookie yuklash
• <code>/cookie [service]</code> → cookie'larni yuklab olish (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → indeks bo'yicha manbani tanlash (1–N)
• <code>/cookies_from_browser</code> → brauzerdan ajratib olish
• <code>/check_cookie</code> → cookie'ni tekshirish
• <code>/save_as_cookie</code> → matnni cookie sifatida saqlash

🧹 <b>Tozalash:</b>
• <code>/clean</code> → faqat media fayllar
• <code>/clean all</code> → hamma narsa
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Sozlamalar:</b>
• <code>/settings</code> → sozlamalar menyusi
• <code>/format</code> → sifat va format
• <code>/split</code> → videoni qismlarga bo'lish
• <code>/mediainfo on/off</code> → media ma'lumotlari
• <code>/nsfw on/off</code> → NSFW xiralash
• <code>/tags</code> → saqlangan teglarni ko'rish
• <code>/sub on/off</code> → subtitrlar
• <code>/keyboard</code> → klaviatura (OFF/1x3/2x3)

🏷️ <b>Teglar:</b>
• URL dan keyin <code>#tag1#tag2</code> qo'shing
• Teglar sarlavhalarda ko'rinadi
• <code>/tags</code> → barcha teglarni ko'rish

🔗 <b>To'g'ridan-to'g'ri Havolalar:</b>
• <code>/link URL</code> → eng yaxshi sifat
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → ma'lum sifat

⚙️ <b>Tezkor Buyruqlar:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → sifatni o'rnatish
• <code>/keyboard off/1x3/2x3/full</code> → klaviatura tartibi
• <code>/split 100mb-2000mb</code> → qism hajmini o'zgartirish
• <code>/subs off/ru/en auto</code> → subtitr tili
• <code>/list URL</code> → mavjud formatlar ro'yxati
• <code>/mediainfo on/off</code> → media ma'lumotlarini yoqish/o'chirish
• <code>/proxy on/off</code> → barcha yuklab olishlar uchun proksini yoqish/o'chirish

📊 <b>Ma'lumot:</b>
• <code>/usage</code> → yuklab olish tarixi
• <code>/search</code> → @vid orqali ichki qidiruv

🖼 <b>Rasmlar:</b>
• <code>URL</code> → rasm URL'larini yuklab olish
• <code>/img URL</code> → URL dan rasmlarni yuklab olish
• <code>/img 11-20 URL</code> → ma'lum diapazonni yuklab olish
• <code>/img 11- URL</code> → 11-dan oxirigacha yuklab olish

👨‍💻 <i>Dasturchi:</i> @upekshaip
🤝 <i>Hissa qo'shuvchi:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Cookie'ni <b><u>cookie.txt</u></b> sifatida saqlang va botga hujjat sifatida yuboring.\n\n"
        "Shuningdek, cookie'larni <b><u>/save_as_cookie</u></b> buyrug'i bilan oddiy matn sifatida yuborishingiz mumkin.\n"
        "<b><u>/save_as_cookie</u></b> dan foydalanish:</b>\n\n"
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
        "<b><u>Ko'rsatmalar:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>Video qidiruv</b>

@vid orqali inline qidiruvni faollashtirish uchun quyidagi tugmani bosing.

<blockquote>PC'da har qanday chatda <b>"@vid Sizning_Qidiruv_Savolingiz"</b> deb yozing.</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Rasm yuklab olish buyrug'i</b>\n\n"
        "Ishlatish: <code>/img URL</code>\n\n"
        "<b>Misollar:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Qo'llab-quvvatlanadigan platformalar (misollar):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor va boshqalar — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">to'liq ro'yxat</a></blockquote>"
        "Shuningdek qarang: "
    )
    
    LINK_HINT_MSG = (
        "Sifat tanlash bilan to'g'ridan-to'g'ri video havolalarini olish.\n\n"
        "Ishlatish: /link + URL \n\n"
        "(mas. /link https://youtu.be/abc123)\n"
        "(mas. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Guruhga bot qo'shish</b>

Kengaytirilgan funksiyalar va yuqori chegaralarni olish uchun botlarimni guruhlaringizga qo'shing!
————————————
📊 <b>Joriy BEPUL chegaralar (Bot'ning DM'ida):</b>
<blockquote>•🗑 Barcha fayllardan tartibsiz axlat 👎
• Maksimal 1 fayl hajmi: <b>8 GB</b>
• Maksimal 1 fayl sifat: <b>CHEKSIZ</b>
• Maksimal 1 fayl davomiyligi: <b>CHEKSIZ</b>
• Maksimal yuklab olishlar soni: <b>CHEKSIZ</b>
• Bir xabarda maksimal URL: <b>10</b> (faqat sifat tanlash rejimida)
• 1 marta maksimal ro'yxat elementlari: <b>50</b>
• 1 marta maksimal TikTok videolari: <b>500</b>
• 1 marta maksimal rasmlar: <b>1000</b>
• URL tezlik chegaralari: <b>5/min, 60/soat, 1000/kun</b>
• Buyruq chegarasi: <b>20/min</b>
• 1 Yuklab olish maksimal vaqti: <b>2 soat</b>
• 🔞 NSFW kontenti pullik! 1⭐️ = $0.02
• 🆓 BOSHQA BARCHA MEDIA TO'LIQ BEPUL
• 📝 Barcha kontent loglari va kesh log-kanallarimga qayta yuklab olishda darhol qayta post qilish uchun</blockquote>

💬<b>Bu chegaralar faqat subtitrli video uchun:</b>
<blockquote>• Maksimal video+subs davomiyligi: <b>1.5 soat</b>
• Maksimal video+subs fayl hajmi: <b>500 MB</b>
• Maksimal video+subs sifat: <b>720p</b></blockquote>
————————————
🚀 <b>Pullik guruh imtiyozlari (2️⃣x chegaralar):</b>
<blockquote>•  🗂 Mavzular bo'yicha tartiblangan tartibli media ombori 👍
•  📁 Botlar siz chaqirgan mavzuda javob beradi
•  📌 Yuklab olish jarayoni bilan avtomatik pin status xabari
•  🖼 /img buyrug'i mediani 10 elementli albomlar sifatida yuklab oladi
• Maksimal 1 fayl hajmi: <b>16 GB</b> ⬆️
• Bir xabarda maksimal URL: <b>20</b> ⬆️ (faqat sifat tanlash rejimida)
• 1 marta maksimal ro'yxat elementlari: <b>100</b> ⬆️
• 1 marta maksimal TikTok videolari: 1000 ⬆️
• 1 marta maksimal rasmlar: 2000 ⬆️
• URL tezlik chegaralari: <b>10/min, 120/soat, 2000/kun</b> ⬆️
• Buyruq chegarasi: <b>40/min</b> ⬆️
• 1 Yuklab olish maksimal vaqti: <b>4 soat</b> ⬆️
• 🔞 NSFW kontenti: To'liq metadata bilan bepul 🆓
• 📢 Guruhlar uchun kanalimga obuna bo'lish shart emas
• 👥 Barcha guruh a'zolari pullik funksiyalarga ega bo'ladi!
• 🗒 Log-kanallarimga log/kesh yo'q! Guruh sozlamalarida nusxa/qayta post qilishni rad etishingiz mumkin</blockquote>

💬 <b>Subtitrli video uchun 2️⃣x chegaralar:</b>
<blockquote>• Maksimal video+subs davomiyligi: <b>3 soat</b> ⬆️
• Maksimal video+subs fayl hajmi: <b>1000 MB</b> ⬆️
• Maksimal video+subs sifat: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Narx va sozlash:</b>
<blockquote>• Narx: guruhdagi 1 bot uchun <b>$5/oy</b>
• Sozlash: @iilililiiillliiliililliilliliiil bilan bog'laning
• To'lov: 💎TON yoki boshqa usullar💲
• Yordam: To'liq texnik yordam kiritilgan</blockquote>
————————————
Bepul 🔞<b>NSFW</b> blokini ochish va barcha chegaralarni ikki baravar (x2️⃣) qilish uchun botlarimni guruhingizga qo'shishingiz mumkin.
Guruhingiz botlarimdan foydalanishga ruxsat berishni xohlasangiz, @iilililiiillliiliililliilliliiil bilan bog'laning
————————————
💡<b>MASLAHAT:</b> <blockquote>Do'stlaringiz bilan har qanday miqdorda pul to'plashingiz mumkin (masalan, 100 kishi) va butun guruh uchun 1 xarid qiling - BARCHA GURUH A'ZOLARI shunchaki <b>0.05$</b> evaziga o'sha guruhdagi barcha bot funksiyalariga TO'LIQ CHEKSIZ KIRISH imkoniyatiga ega bo'ladi</blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW rejimi: YOQILDI✅</b>

• NSFW kontenti bulanishsiz ko'rsatiladi.
• Spoiler'lar NSFW media'ga qo'llanmaydi.
• Kontent darhol ko'rinadi

<i>Bulanishni yoqish uchun /nsfw off ishlating</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW rejimi: O'CHIRILDI</b>

⚠️ <b>Bulanish yoqilgan</b>
• NSFW kontenti spoiler ostida yashiriladi   
• Ko'rish uchun media'ga bosishingiz kerak bo'ladi
• Spoiler'lar NSFW media'ga qo'llanadi.

<i>Bulanishni o'chirish uchun /nsfw on ishlating</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Noto'g'ri parametr</b>

Ishlating:
• <code>/nsfw on</code> - bulanishni o'chirish
• <code>/nsfw off</code> - bulanishni yoqish
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Kesh tekshirilmoqda...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Qayta ishlanmoqda..."
    DOWNLOADING_MSG = "📥 <b>Media yuklanmoqda...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Rasm yuklanmoqda...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Yuklab olish yakunlandi</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Yuklab olindi:"
    SENT_STATUS_MSG = "Yuborildi:"
    PENDING_TO_SEND_STATUS_MSG = "Yuborish kutilmoqda:"
    TITLE_LABEL_MSG = "Sarlavha:"
    MEDIA_COUNT_LABEL_MSG = "Media soni:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Yuklab olish yakunlandi, audio qayta ishlanmoqda..."
    VIDEO_PROCESSING_MSG = "📽 Video qayta ishlanmoqda..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Keshdan yuborildi</b>\n\nYuborilgan albomlar: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Video muvaffaqiyatli keshdan yuborildi."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Ro'yxat videolari keshdan yuborildi ({cached}/{total} fayl)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} video keshdan yuborildi, yetishmayotganlar yuklanmoqda..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Keshdan yuborildi: {cached}\n🔄 Yuklab olish davom etmoqda..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Mediani tahlil qila olmadi, maksimal ruxsat etilgan diapazon (1-{fallback_limit}) bilan davom etmoqda..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Media sonini aniqlab bo'lmadi, maksimal ruxsat etilgan diapazon (1-{total_limit}) bilan davom etmoqda..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Umumiy media sonini aniqlab bo'lmadi, belgilangan diapazon {start}-{end} bilan davom etmoqda..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>Noto'g'ri URL</b>\n\nIltimos, http:// yoki https:// bilan boshlanadigan to'g'ri URL kiriting"

    ERROR_OCCURRED_MSG = "❌ <b>Xatolik yuz berdi</b>\n\n<code>{url}</code>\n\nXatolik: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Videoni yuborishda xatolik: {error}"
    ERROR_UNKNOWN_MSG = "❌ Noma'lum xatolik: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Videolarni yuklab olish uchun disk maydoni yetarli emas."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Fayl hajmi {limit} GB chegarasidan oshib ketdi. Iltimos, ruxsat etilgan hajm ichida kichikroq faylni tanlang."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>Barcha mavjud proksi-lar bilan video yuklab olish muvaffaqiyatsiz tugadi</b>\n\nProksi-lar orqali barcha yuklab olish urinishlari muvaffaqiyatsiz tugadi.\nUrinib ko'ring:\n• Proksi-lar ishlashini tekshiring\n• Ro'yxatdan boshqa proksi-larni sinab ko'ring\n• Proksi-larsiz yuklab oling (agar mumkin bo'lsa)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Havolani olishda xatolik:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram xabar yuborishni chekladi.\n⏳ Iltimos, kuting: {time}\nTaymerni yangilash uchun URLni yana 2 marta yuboring."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram xabar yuborishni chekladi.\n⏳ Iltimos, kuting: \nTaymerni yangilash uchun URLni yana 2 marta yuboring."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Subtitrlar yuklab olinmadi"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>To'g'ridan-to'g'ri oqim havolalari</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Sarlavha:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Davomiyligi:</b> {duration} sek\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Xatolik: Asl xabar topilmadi."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ #{tag} tegi taqiqlangan belgilarni o'z ichiga oladi. Faqat harflar, raqamlar va _ ruxsat etiladi.\nIltimos, ishlating: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Ro'yxat videolari yuborildi: {sent}/{total} fayl."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>Ro'yxat bo'yicha maslahat</b>

Siz diapazonni ko'rsatmasdan ro'yxat havolasini yubordingiz. Bot avtomatik ravishda birinchi videoni yuklab oldi (<code>*1*1</code>).

<b>Ro'yxatdan bir nechta videoni yuklab olish uchun diapazonni ko'rsating:</b>
• <code>URL*1*5</code> — birinchi 5 ta video (1 dan 5 gacha, shu jumladan)
• <code>URL*3*3</code> — faqat 3-video
• <code>/vid 1-10 URL</code> — muqobil format

Ko'proq ma'lumot: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ Keshdan yuborildi: {cached}/{total} fayl."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Oqim havolalarini olishda muvaffaqiyatsizlik"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Cookie'larni yuklab olish uchun brauzerni tanlang:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Ushbu tizimda brauzer topilmadi. Siz cookie'larni masofaviy URL'dan yuklab olishingiz yoki brauzer holatini kuzatishingiz mumkin:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Brauzerni ochish</b> - mini-ilovada brauzer holatini kuzatish uchun"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Brauzerni ochish"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Masofaviy URL'dan yuklab olish"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie fayli zaxira orqali yuklab olindi va cookie.txt sifatida saqlandi"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Qo'llab-quvvatlanadigan brauzerlar topilmadi va COOKIE_URL sozlanmagan. /cookie ishlating yoki cookie.txt yuklang."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Zaxira COOKIE_URL .txt faylga ishora qilishi kerak."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Zaxira cookie fayli juda katta (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Zaxira cookie manbasi mavjud emas (holat {status}). /cookie sinab ko'ring yoki cookie.txt yuklang."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Zaxira cookie'ni yuklab olishda xatolik. /cookie sinab ko'ring yoki cookie.txt yuklang."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Zaxira cookie yuklab olish paytida kutilmagan xatolik."
    BTN_CLOSE = "🔚Yopish"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Noto'g'ri boolean qiymat"
    ARGS_CLOSED_MSG = "Yopildi"
    ARGS_ALL_RESET_MSG = "✅ Barcha argumentlar qayta tiklandi"
    ARGS_RESET_ERROR_MSG = "❌ Argumentlarni qayta tiklashda xatolik"
    ARGS_INVALID_PARAM_MSG = "❌ Noto'g'ri parametr"
    ARGS_BOOL_SET_MSG = "{value} ga o'rnatildi"
    ARGS_BOOL_ALREADY_SET_MSG = "Allaqachon {value} ga o'rnatilgan"
    ARGS_INVALID_SELECT_MSG = "❌ Noto'g'ri tanlov qiymati"
    ARGS_VALUE_SET_MSG = "{value} ga o'rnatildi"
    ARGS_VALUE_ALREADY_SET_MSG = "Allaqachon {value} ga o'rnatilgan"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Joriy qiymat:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Misollar:</b>\n• <code>default</code> - Standart XFF strategiyasidan foydalanish\n• <code>never</code> - XFF header'ni hech qachon ishlatmaslik\n• <code>US</code> - AQSh mamlakat kodi\n• <code>GB</code> - Buyuk Britaniya mamlakat kodi\n• <code>DE</code> - Germaniya mamlakat kodi\n• <code>FR</code> - Frantsiya mamlakat kodi\n• <code>JP</code> - Yaponiya mamlakat kodi\n• <code>192.168.1.0/24</code> - IP blok (CIDR)\n• <code>10.0.0.0/8</code> - Shaxsiy IP diapazoni\n• <code>203.0.113.0/24</code> - Ommaviy IP blok\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Eslatma:</b> Bu --geo-bypass variantlarini almashtiradi. Har qanday 2 harfli mamlakat kodi yoki CIDR belgisi bilan IP blokidan foydalaning.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Misol:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Iltimos, yangi qiymatingizni yuboring."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Diapazon:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Iltimos, raqam yuboring."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Misollar:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Eslatma:</b> Bu header'lar mavjud Referer va User-Agent header'lariga qo'shiladi.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Joriy yt-dlp argumentlari:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - True/False kalitlar\n• 📋 <b>Tanlash</b> - Variantlardan tanlash\n• 🔢 <b>Raqamli</b> - Raqam kiritish\n• 📝🔧 <b>Matn</b> - Matn/JSON kiritish</blockquote>\n\nBu sozlamalar barcha yuklab olishlaringizga qo'llanadi."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "IPv6 ulanishlarni majburlash",
        "force_ipv4": "IPv4 ulanishlarni majburlash", 
        "no_live_from_start": "Jonli oqimlarni boshidan yuklab olmaslik",
        "live_from_start": "Jonli oqimlarni boshidan yuklab olish",
        "no_check_certificates": "HTTPS sertifikat tekshiruvini bostirish",
        "check_certificate": "SSL sertifikatni tekshirish",
        "no_playlist": "Faqat bitta videoni yuklab olish, ro'yxat emas",
        "embed_metadata": "Video faylga metadata kiritish",
        "embed_thumbnail": "Video faylga thumbnail kiritish",
        "write_thumbnail": "Thumbnail'ni faylga yozish",
        "ignore_errors": "Yuklab olish xatolarini e'tiborsiz qoldirish va davom etish",
        "legacy_server_connect": "Eski server ulanishlariga ruxsat berish",
        "concurrent_fragments": "Bir vaqtning o'zida yuklab olinadigan fragmentlar soni",
        "xff": "X-Forwarded-For header strategiyasi",
        "user_agent": "User-Agent header",
        "impersonate": "Brauzer taklif qilish",
        "referer": "Referer header",
        "geo_bypass": "Geografik cheklovlarni aylanib o'tish",
        "hls_use_mpegts": "HLS uchun MPEG-TS ishlatish",
        "no_part": ".part fayllardan foydalanmaslik",
        "no_continue": "Qisman yuklab olishlarni davom ettirmaslik",
        "audio_format": "Audio formati",
        "video_format": "Video formati",
        "merge_output_format": "Birlashtirish uchun chiqish formati",
        "send_as_file": "Fayl sifatida yuborish",
        "username": "Foydalanuvchi nomi",
        "password": "Parol",
        "twofactor": "Ikki bosqichli autentifikatsiya kodi",
        "min_filesize": "Minimal fayl hajmi (MB)",
        "max_filesize": "Maksimal fayl hajmi (MB)",
        "playlist_items": "Ro'yxat elementlari",
        "date": "Sana",
        "datebefore": "Sana oldin",
        "dateafter": "Sana keyin",
        "http_headers": "HTTP header'lar",
        "sleep_interval": "Kutilish intervali",
        "max_sleep_interval": "Maksimal kutilish intervali",
        "retries": "Qayta urinishlar soni",
        "http_chunk_size": "HTTP chunk hajmi",
        "sleep_subtitles": "Subtitlar uchun kutilish"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp argumentlari sozlash</b>\n\n<blockquote>📋 <b>Guruhlar:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp argumentlari sozlash</b>\n\n"
        "<blockquote>📋 <b>Guruhlar:</b>\n"
        "• ✅/❌ <b>Boolean</b> - True/False kalitlar\n"
        "• 📋 <b>Tanlash</b> - Variantlardan tanlash\n"
        "• 🔢 <b>Raqamli</b> - Raqam kiritish\n"
        "• 📝🔧 <b>Matn</b> - Matn/JSON kiritish</blockquote>\n\n"
        "Bu sozlamalar barcha yuklab olishlaringizga qo'llanadi."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Iltimos, kuting..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Xatolik yuz berdi"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Faollik yo'qligi sababli kiritish rejimi avtomatik yopildi (5 daqiqa)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Kiritilgan ma'lumot potentsial xavfli kontentni o'z ichiga oladi: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Kiritilgan ma'lumot juda uzun (maksimal 1000 belgi)"
    ARGS_INVALID_URL_MSG = "❌ Noto'g'ri URL formati. http:// yoki https:// bilan boshlanishi kerak"
    ARGS_INVALID_JSON_MSG = "❌ Noto'g'ri JSON formati"
    ARGS_NUMBER_RANGE_MSG = "❌ Raqam {min_val} va {max_val} orasida bo'lishi kerak"
    ARGS_INVALID_NUMBER_MSG = "❌ Noto'g'ri raqam formati"
    ARGS_DATE_FORMAT_MSG = "❌ Sana YYYYMMDD formatida bo'lishi kerak (mas., 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Yil 1900 va 2100 orasida bo'lishi kerak"
    ARGS_MONTH_RANGE_MSG = "❌ Oy 01 va 12 orasida bo'lishi kerak"
    ARGS_DAY_RANGE_MSG = "❌ Kun 01 va 31 orasida bo'lishi kerak"
    ARGS_INVALID_DATE_MSG = "❌ Noto'g'ri sana formati"
    ARGS_INVALID_XFF_MSG = "❌ XFF 'default', 'never', mamlakat kodi (mas., US) yoki IP blok (mas., 192.168.1.0/24) bo'lishi kerak"
    ARGS_NO_CUSTOM_MSG = "Maxsus argumentlar o'rnatilmagan. Barcha parametrlar standart qiymatlardan foydalanadi."
    ARGS_RESET_SUCCESS_MSG = "✅ Barcha argumentlar standartga qaytarildi."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Matn juda uzun. Maksimal 500 belgi."
    ARGS_ERROR_PROCESSING_MSG = "❌ Kiritilgan ma'lumotni qayta ishlashda xatolik. Iltimos, qayta urinib ko'ring."
    ARGS_BOOL_INPUT_MSG = "❌ Fayl sifatida yuborish variantini uchun 'True' yoki 'False' kiriting."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Iltimos, to'g'ri raqam kiriting."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Bu variantni yoqish/o'chirish uchun <code>True</code> yoki <code>False</code> yuboring."
    ARGS_JSON_VALUE_REQUEST_MSG = "Iltimos, to'g'ri JSON yuboring."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Sizda hali teg'lar yo'q."
    TAGS_MESSAGE_CLOSED_MSG = "Teg xabari yopildi."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Subtitrlar o'chirildi va Har doim so'rash rejimi o'chirildi."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBTITR Har doim so'rash yoqildi."
    SUBS_LANGUAGE_SET_MSG = "✅ Subtitr tili o'rnatildi: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️OGOHLANTIRISH: yuqori CPU ta'siri tufayli bu funksiya juda sekin (deyarli real-time) va quyidagilarga cheklangan:\n"
        "- 720p maksimal sifat\n"
        "- 1.5 soat maksimal davomiylik\n"
        "- 500mb maksimal video hajmi</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Tezkor buyruqlar:</b>\n"
        "• <code>/subs off</code> - subtitrlarni o'chirish\n"
        "• <code>/subs on</code> - Har doim so'rash rejimini yoqish\n"
        "• <code>/subs ru</code> - tilni o'rnatish\n"
        "• <code>/subs ru auto</code> - AUTO/TRANS bilan tilni o'rnatish"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Subtitrlar o'chirilgan"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Tanlangan til: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Subtitrlar yuklanmoqda..."
    SUBS_DISABLED_ERROR_MSG = "❌ Subtitrlar o'chirilgan. Sozlash uchun /subs ishlating."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Subtitrlar yuklab olish faqat YouTube uchun qo'llab-quvvatlanadi."
    SUBS_CAPTION_MSG = (
        "<b>💬 Subtitrlar</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Til:</b> {lang}\n"
        "<b>Tur:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Subtitrlar SRT-fayli foydalanuvchiga yuborildi."
    SUBS_ERROR_PROCESSING_MSG = "❌ Subtitr faylini qayta ishlashda xatolik."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Subtitrlarni yuklab olishda muvaffaqiyatsizlik."
    SUBS_ERROR_MSG = "❌ Subtitrlarni yuklab olishda xatolik: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Bo'linish qismi hajmi o'rnatildi: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **Noto'g'ri hajm!**\n\n"
        "**To'g'ri diapazon:** 100MB dan 2GB gacha\n\n"
        "**To'g'ri formatlar:**\n"
        "• `100mb` dan `2000mb` gacha (megabayt)\n"
        "• `0.1gb` dan `2gb` gacha (gigabayt)\n\n"
        "**Misollar:**\n"
        "• `/split 100mb` - 100 megabayt\n"
        "• `/split 500mb` - 500 megabayt\n"
        "• `/split 1.5gb` - 1.5 gigabayt\n"
        "• `/split 2gb` - 2 gigabayt\n"
        "• `/split 2000mb` - 2000 megabayt (2GB)\n\n"
        "**Oldindan sozlangan:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Video bo'linishi uchun maksimal qism hajmini tanlang:**\n\n"
        "**Diapazon:** 100MB dan 2GB gacha\n\n"
        "**Tezkor buyruqlar:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Misollar:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Menyu yopildi."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Bot sozlamalari</b>\n\nKategoriyani tanlang:"
    SETTINGS_MENU_CLOSED_MSG = "Menyu yopildi."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Tozalash variantlari</b>\n\nNimani tozalashni tanlang:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIE'LAR</b>\n\nHarakatni tanlang:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIA</b>\n\nHarakatni tanlang:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 MA'LUMOT</b>\n\nHarakatni tanlang:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ QO'SHIMCHA BUYRUQLAR</b>\n\nHarakatni tanlang:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Buyruq bajarildi."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ To'ldirish chegarasi. Keyinroq urinib ko'ring."
    SETTINGS_HINT_SENT_MSG = "Maslahat yuborildi."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Qidiruv yordamchisi ochildi."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Noma'lum buyruq."
    SETTINGS_HINT_CLOSED_MSG = "Maslahat yopildi."
    SETTINGS_HELP_SENT_MSG = "Foydalanuvchiga yordam matni yuborildi"
    SETTINGS_MENU_OPENED_MSG = "/settings menyusi ochildi"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Qidiruv yordamchisi yopildi"
    SEARCH_CLOSED_MSG = "Yopildi"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proxy {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Proxy sozlamalarini saqlashda xatolik."
    PROXY_MENU_TEXT_MSG = "Barcha yt-dlp operatsiyalari uchun proxy serverni yoqish yoki o'chirish?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Barcha yt-dlp operatsiyalari uchun proksi-serverlar ({config_count} + {file_count} mavjud) yordamida yoqilsin yoki oʻchirilsinmi?\n\nALL (AVTO) yoqilganda proksi-serverlar ruxsat etilgan mamlakatlar boʻyicha (YouTube xatosida koʻrsatilgan) avtomatik tanlanadi."
    PROXY_MENU_CLOSED_MSG = "Menyu yopildi."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy yoqildi. Barcha yt-dlp operatsiyalari proxy'dan foydalanadi."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy yoqildi. Barcha yt-dlp operatsiyalari {count} proxy server va {method} tanlash usuli bilan ishlaydi."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Proksi yoqilgan (YouTube xatosi bo'yicha AVTO).\n\nYouTube geo-blok xatosi qaytarganda bot faqat shu xatoda ko'rsatilgan mamlakatlar proksilaridan foydalanadi (barcha proksilarni ketma-ket sinash yo'q)."
    PROXY_DISABLED_MSG = "❌ Proxy o'chirildi."
    PROXY_TRYING_COUNTRY_MSG = "🔄 Proksi sinanmoqda: {country} ({current}/{total})"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Proxy sozlamalarini saqlashda xatolik."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy yoqildi."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy o'chirildi."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ OLDINGI YUKLAB OLISH TUGAGUNIGACHA KUTING"
    AUDIO_HELP_MSG = (
        "<b>🎧 Audio yuklab olish buyrug'i</b>\n\n"
        "Ishlatish: <code>/audio URL</code>\n\n"
        "<b>Misollar:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Shuningdek qarang: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Audio maslahati yopildi."
    PLAYLIST_HELP_CLOSED_MSG = "Ro'yxat yordami yopildi."
    USERLOGS_CLOSED_MSG = "Log xabari yopildi."
    HELP_CLOSED_MSG = "Yordam yopildi."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW Bulanish sozlamalari</b>\n\nNSFW kontenti <b>{status}</b>.\n\nNSFW kontentni bulanishini tanlang:"
    NSFW_MENU_CLOSED_MSG = "Menyu yopildi."
    NSFW_BLUR_DISABLED_MSG = "NSFW bulanish o'chirildi."
    NSFW_BLUR_ENABLED_MSG = "NSFW bulanish yoqildi."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW bulanish o'chirildi."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW bulanish yoqildi."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Yuklab olingan fayllar uchun MediaInfo yuborishni yoqish yoki o'chirish?"
    MEDIAINFO_MENU_CLOSED_MSG = "Menyu yopildi."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo yoqildi. Yuklab olgandan keyin, fayl ma'lumotlari yuboriladi."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo o'chirildi."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo yoqildi."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo o'chirildi."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Mavjud formatlarni ro'yxatga olish</b>\n\n"
        "URL uchun mavjud video/audio formatlarini olish.\n\n"
        "<b>Ishlatish:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Misollar:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Format ID'lardan qanday foydalanish:</b>\n"
        "Ro'yxatni olgandan keyin, aniq format ID'dan foydalaning:\n"
        "• <code>/format id 401</code> - 401 formatini yuklab olish\n"
        "• <code>/format id401</code> - yuqoridagi bilan bir xil\n"
        "• <code>/format id140 audio</code> - 140 formatini MP3 audio sifatida yuklab olish\n\n"
        "Bu buyruq yuklab olinishi mumkin bo'lgan barcha mavjud formatlarni ko'rsatadi."
    )
    LIST_PROCESSING_MSG = "🔄 Mavjud formatlar olinmoqda..."
    LIST_INVALID_URL_MSG = "❌ Iltimos, http:// yoki https:// bilan boshlanadigan to'g'ri URL kiriting"
    LIST_CAPTION_MSG = (
        "📃 Mavjud formatlar:\n<code>{url}</code>\n\n"
        "💡 <b>Formatni qanday o'rnatish:</b>\n"
        "• <code>/format id 134</code> - Aniq format ID'ni yuklab olish\n"
        "• <code>/format 720p</code> - Sifat bo'yicha yuklab olish\n"
        "• <code>/format best</code> - Eng yaxshi sifatni yuklab olish\n"
        "• <code>/format ask</code> - Har doim sifatni so'rash\n\n"
        "{audio_note}\n"
        "📋 Yuqoridagi ro'yxatdan format ID'dan foydalaning"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Faqat audio formatlar:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - 140 formatini MP3 audio sifatida yuklab olish\n"
        "• <code>/format id140 audio</code> - yuqoridagi bilan bir xil\n"
        "Bular MP3 audio fayllari sifatida yuklab olinadi.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Format faylini yuborishda xatolik: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Formatlarni olishda muvaffaqiyatsizlik:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Buyruqni qayta ishlashda xatolik yuz berdi"
    LIST_ERROR_CALLBACK_MSG = "Xatolik yuz berdi"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Format ID'lardan qanday foydalanish:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Ro'yxatni olgandan keyin, aniq format ID'dan foydalaning:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - 401 formatini yuklab olish\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - yuqoridagi bilan bir xil\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - 140 formatini MP3 audio sifatida yuklab olish\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - yuqoridagi bilan bir xil\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Faqat audio formatlar aniqlandi: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Bular MP3 audio fayllari sifatida yuklab olinadi.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Faqat video formatlar:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Yuqoridagi ro'yxatdan format ID'dan foydalaning"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Ishlatish:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>Misollar:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - eng yaxshi sifat\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p yoki pastroq\n"
        "• /link 720p https://youtube.com/watch?v=... - yuqoridagi bilan bir xil\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K yoki pastroq\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K yoki pastroq"
        "</blockquote>\n\n"
        "<b>Sifat:</b> 1 dan 10000 gacha (masalan, 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Iltimos, to'g'ri URL kiriting"
    LINK_PROCESSING_MSG = "🔗 To'g'ridan-to'g'ri havola olinmoqda..."
    LINK_DURATION_MSG = "⏱ <b>Davomiyligi:</b> {duration} sek\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video oqimi:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio oqimi:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Klaviatura sozlamasi yangilandi!**\n\nYangi sozlama: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Noto'g'ri argument!**\n\n"
        "To'g'ri variantlar: `off`, `1x3`, `2x3`, `full`\n\n"
        "Misol: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Klaviatura sozlamalari**\n\n"
        "Joriy: **{current}**\n\n"
        "Variantni tanlang:\n\n"
        "Yoki ishlating: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 klaviatura faollashtirildi!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Klaviatura yashirildi"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3 klaviatura faollashtirildi!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3 klaviatura faollashtirildi!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Emoji klaviatura faollashtirildi!"
    KEYBOARD_ERROR_APPLYING_MSG = "Klaviatura sozlamasini qo'llashda xatolik {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Format o'rnatildi: Har doim so'rash. Har safar URL yuborganingizda sifat so'raladi."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format o'rnatildi: Har doim so'rash. Endi har safar URL yuborganingizda sifat so'raladi."
    FORMAT_BEST_UPDATED_MSG = "✅ Format eng yaxshi sifatga yangilandi (AVC+MP4 ustuvorligi):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Format ID {id} ga yangilandi:\n{format}\n\n💡 <b>Eslatma:</b> Agar bu faqat audio format bo'lsa, MP3 audio fayli sifatida yuklab olinadi."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Format ID {id} ga yangilandi (faqat audio):\n{format}\n\n💡 Bu MP3 audio fayli sifatida yuklab olinadi."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Format {quality} sifatiga yangilandi:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Format yangilandi:\n{format}"
    FORMAT_MENU_MSG = (
        "Format variantini tanlang yoki maxsus formatni yuboring:\n"
        "• <code>/format &lt;format_string&gt;</code> - maxsus format\n"
        "• <code>/format 720</code> - 720p sifat\n"
        "• <code>/format 4k</code> - 4K sifat\n"
        "• <code>/format 8k</code> - 8K sifat\n"
        "• <code>/format id 401</code> - aniq format ID\n"
        "• <code>/format ask</code> - har doim menyuni ko'rsatish\n"
        "• <code>/format best</code> - bv+ba/eng yaxshi sifat"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Maxsus formatdan foydalanish uchun, buyruqni quyidagi shaklda yuboring:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "<code>bestvideo+bestaudio/best</code> ni o'zingiz xohlagan format qatori bilan almashtiring."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Xohlagan piksellar soni va codec'ni tanlang:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format o'rnatildi: Har doim so'rash. Endi har safar URL yuborganingizda sifat so'raladi."
    FORMAT_UPDATED_MSG = "✅ Format yangilandi:\n{format}"
    FORMAT_SAVED_MSG = "✅ Format saqlandi."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Format tanlovi yangilandi."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Maxsus format menyusi yopildi"
    FORMAT_CODEC_SET_MSG = "✅ Codec {codec} ga o'rnatildi"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Brauzer tanlovi yangilandi."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Kirish rad etildi. Faqat admin."
    ACCESS_DENIED_ADMIN = "❌ Kirish rad etildi. Faqat admin."
    WELCOME_MASTER = "Xush kelibsiz, Usta 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Kechirasiz... Yuklab olish paytida xatolik yuz berdi."
    SIZE_LIMIT_EXCEEDED = "❌ Fayl hajmi {max_size_gb} GB chegarasidan oshib ketdi. Iltimos, ruxsat etilgan hajm ichida kichikroq faylni tanlang."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Skript topilmadi: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ {script_path} ishlatib yangi Firebase dump yuklanmoqda..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase kesh muvaffaqiyatli qayta yuklandi!"
    ADMIN_CACHE_FAILED_MSG = "❌ Firebase keshni qayta yuklashda muvaffaqiyatsizlik. {cache_file} mavjudligini tekshiring."
    ADMIN_ERROR_RELOADING_MSG = "❌ Keshni qayta yuklashda xatolik: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ {script_path} ishga tushirishda xatolik:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Promo xabari boshqa barcha foydalanuvchilarga yuborildi</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Promo xabarni yuborib bo'lmadi. Xabarga javob berib ko'ring\nYoki xatolik yuz berdi</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ Foydalanuvchi hali hech qanday kontentni yuklab olmagan...</b> Log'larda mavjud emas"
    ADMIN_INVALID_COMMAND_MSG = "❌ Noto'g'ri buyruq"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ <code>{{path}}</code> uchun keshda ma'lumot topilmadi"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Navbat bo'sh — hali hech kim kanaldan chiqmagan."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Bloklash navbati</b>\nKutilmoqda jami: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (chiqdi: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… va yana {extra} foydalanuvchi."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "/block_user show • all • auto • 10s ishlating"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Navbatdan bloklangan foydalanuvchilar: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Avtomatik bloklash yoqildi: yangi chiqib ketuvchilar darhol bloklanadi."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Avtomatik bloklash o'chirildi."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Rejalashtirilgan avtomatik bloklash oynasi har {interval} ga o'rnatildi."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Oxirgi {hours} soat (2 kun) uchun kanal faollik log'i."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 Oxirgi {hours} soat (2 kun): qo'shildi {joined}, chiqdi {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Oxirgi {hours} soat (2 kun) uchun faollik yo'q."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Jami: 🟢 {joined} qo'shildi, 🔴 {left} chiqdi."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Kanal faollik log'iga kirish yo'q. Botlar admin log'larini o'qiy olmaydi. Ushbu funksiyani yoqish uchun config'da CHANNEL_GUARD_SESSION_STRING'ga foydalanuvchi sessiyasini ta'minlang."
    BAN_TIME_USAGE_MSG = "❌ Ishlatish: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ 10s, 6m, 5h, 4d, 3w, 2M yoki 1y kabi formatlardan foydalaning."
    BAN_TIME_SET_MSG = "🕒 Kanal log skanlash intervali {interval} ga o'rnatildi."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Kanal skanlash hisoboti\n"
        "Ishga tushirilgan vaqt: {run_ts}\n"
        "Interval: {interval}\n"
        "Yangi chiqib ketuvchilar: {new_leavers}\n"
        "Avtomatik bloklashlar: {auto_banned}\n"
        "Kutilmoqda: {pending}\n"
        "Oxirgi event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Ishlatish: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Admin admin'ni o'chira olmaydi"
    ADMIN_USER_BLOCKED_MSG = "Foydalanuvchi bloklandi 🔒❌\n \nID: <code>{user_id}</code>\nBloklangan sana: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> allaqachon bloklangan ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Kechirasiz! Siz admin emassiz"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Ishlatish: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Foydalanuvchi blokdan olindi 🔓✅\n \nID: <code>{user_id}</code>\nBlokdan olingan sana: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> allaqachon blokdan olingan ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Blokdan olingan foydalanuvchilar: {count}\n⏱ Vaqt belgisi: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Ishlatish: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Foydalanuvchi e'tiborsiz qoldirildi 👁️❌\n \nID: <code>{user_id}</code>\nE'tiborsiz qoldirilgan sana: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> allaqachon e'tiborsiz qoldirilgan ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Ishlatish: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Foydalanuvchi endi e'tiborsiz qoldirilmaydi 👁️✅\n \nID: <code>{user_id}</code>\nE'tiborsiz qoldirilmaslik sanasi: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> e'tiborsiz qoldirilmaydi ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Bot ish vaqti -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Keshni tozalash uchun URL kiriting.\nIshlatish: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Iltimos, to'g'ri URL kiriting.\nIshlatish: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ URL uchun kesh muvaffaqiyatli tozalandi:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Ushbu havola uchun kesh topilmadi."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Keshni tozalashda xatolik: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Kirish rad etildi. Faqat admin."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Porn ro'yxatini yangilash skripti ishga tushirilmoqda: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Skript muvaffaqiyatli yakunlandi!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Skript muvaffaqiyatli yakunlandi!\n\nChiqish:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Skript {returncode} qaytish kodi bilan muvaffaqiyatsiz:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Skriptni ishga tushirishda xatolik: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Porn va domen bilan bog'liq keshlar qayta yuklanmoqda..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Porn keshlar muvaffaqiyatli qayta yuklandi!\n\n"
        "📊 Joriy kesh holati:\n"
        "• Porn domenlar: {porn_domains}\n"
        "• Porn kalit so'zlar: {porn_keywords}\n"
        "• Qo'llab-quvvatlanadigan saytlar: {supported_sites}\n"
        "• OQ RO'YXAT: {whitelist}\n"
        "• KULRANG RO'YXAT: {greylist}\n"
        "• QORA RO'YXAT: {black_list}\n"
        "• OQ KALIT SO'ZLAR: {white_keywords}\n"
        "• PROXY DOMENLARI: {proxy_domains}\n"
        "• PROXY_2 DOMENLARI: {proxy_2_domains}\n"
        "• TOZA SAVOL: {clean_query}\n"
        "• COOKIE'SIZ DOMENLAR: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Porn keshni qayta yuklashda xatolik: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Tekshirish uchun URL kiriting.\nIshlatish: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Iltimos, to'g'ri URL kiriting.\nIshlatish: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 NSFW kontent uchun URL tekshirilmoqda...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Porn tekshiruv natijasi</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Holat:</b> <b>{status_text}</b>\n\n"
        "<b>Izoh:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ URL'ni tekshirishda xatolik: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Cookie'lar tozalandi."
    CLEAN_LOGS_CLEANED_MSG = "log'lar tozalandi."
    CLEAN_TAGS_CLEANED_MSG = "teg'lar tozalandi."
    CLEAN_FORMAT_CLEANED_MSG = "format tozalandi."
    CLEAN_SPLIT_CLEANED_MSG = "bo'linish tozalandi."
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfo tozalandi."
    CLEAN_SUBS_CLEANED_MSG = "Subtitr sozlamalari tozalandi."
    CLEAN_KEYBOARD_CLEANED_MSG = "Klaviatura sozlamalari tozalandi."
    CLEAN_ARGS_CLEANED_MSG = "Argument sozlamalari tozalandi."
    CLEAN_NSFW_CLEANED_MSG = "NSFW sozlamalari tozalandi."
    CLEAN_PROXY_CLEANED_MSG = "Proxy sozlamalari tozalandi."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "To'ldirish kutilish sozlamalari tozalandi."
    CLEAN_ALL_CLEANED_MSG = "Barcha fayllar tozalandi."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIE'LAR</b>\n\nHarakatni tanlang:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Cookie fayli saqlandi"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ YouTube bo'lmagan cookie'lar uchun tekshiruv o'tkazib yuborildi"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Cookie fayli mavjud, lekin noto'g'ri formatda"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Cookie fayli topilmadi."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 YouTube cookie'larini test qilish boshlandi...\n\nCookie'laringizni tekshirib tasdiqlashimni kutib turing."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Mavjud YouTube cookie'laringiz to'g'ri ishlayapti!\n\nYangi cookie'larni yuklab olish shart emas."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Mavjud YouTube cookie'laringiz muddati o'tgan yoki noto'g'ri.\n\n🔄 Yangi cookie'lar yuklanmoqda..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} cookie manbasi sozlanmagan!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} cookie manbasi .txt fayl bo'lishi kerak!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Diapazon chegarasi oshib ketdi: {range_count} fayl so'ralgan (maksimal {max_img_files}).\n\nMaksimal mavjud fayllarni yuklab olish uchun quyidagi buyruqlardan birini ishlating:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Yopish"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Media chegarasi oshib ketdi: {count} fayl so'ralgan (maksimal {max_count}).\n\nMaksimal mavjud fayllarni yuklab olish uchun quyidagi buyruqlardan birini ishlating:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Havoladan <b>{count}</b> media element topildi"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Yuklab olish diapazonini tanlang:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Brauzer taklif qilish"
    ARGS_REFERER_DESC_MSG = "Referer header"
    ARGS_USER_AGENT_DESC_MSG = "User-Agent header"
    ARGS_GEO_BYPASS_DESC_MSG = "Geografik cheklovlarni aylanib o'tish"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "SSL sertifikatni tekshirish"
    ARGS_LIVE_FROM_START_DESC_MSG = "Jonli oqimlarni boshidan yuklab olish"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Jonli oqimlarni boshidan yuklab olmaslik"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "HLS videolar uchun MPEG-TS konteyner ishlatish"
    ARGS_NO_PLAYLIST_DESC_MSG = "Faqat bitta videoni yuklab olish, ro'yxat emas"
    ARGS_NO_PART_DESC_MSG = ".part fayllardan foydalanmaslik"
    ARGS_NO_CONTINUE_DESC_MSG = "Qisman yuklab olishlarni davom ettirmaslik"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Ajratish uchun audio formati"
    ARGS_EMBED_METADATA_DESC_MSG = "Video faylga metadata kiritish"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Video faylga thumbnail kiritish"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Thumbnail'ni faylga yozish"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Bir vaqtning o'zida yuklab olinadigan fragmentlar soni"
    ARGS_FORCE_IPV4_DESC_MSG = "IPv4 ulanishlarni majburlash"
    ARGS_FORCE_IPV6_DESC_MSG = "IPv6 ulanishlarni majburlash"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For header strategiyasi"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP chunk hajmi (bayt)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Subtitr yuklab olishdan oldin kutilish (soniya)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Eski server ulanishlariga ruxsat berish"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "HTTPS sertifikat tekshiruvini bostirish"
    ARGS_USERNAME_DESC_MSG = "Hisob foydalanuvchi nomi"
    ARGS_PASSWORD_DESC_MSG = "Hisob paroli"
    ARGS_TWOFACTOR_DESC_MSG = "Ikki bosqichli autentifikatsiya kodi"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Yuklab olish xatolarini e'tiborsiz qoldirish va davom etish"
    ARGS_MIN_FILESIZE_DESC_MSG = "Minimal fayl hajmi (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Maksimal fayl hajmi (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Yuklab olinadigan ro'yxat elementlari (mas., 1,3,5 yoki 1-5)"
    ARGS_DATE_DESC_MSG = "Ushbu sanada yuklangan videolarni yuklab olish (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Ushbu sanadan oldin yuklangan videolarni yuklab olish (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Ushbu sanadan keyin yuklangan videolarni yuklab olish (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Maxsus HTTP header'lar (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "So'rovlar orasidagi kutilish intervali (soniya)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Maksimal kutilish intervali (soniya)"
    ARGS_RETRIES_DESC_MSG = "Qayta urinishlar soni"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Video konteyner formati"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Birlashtirish uchun chiqish konteyner formati"
    ARGS_SEND_AS_FILE_DESC_MSG = "Barcha mediani media o'rniga hujjat sifatida yuborish"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Taklif qilish"
    ARGS_REFERER_SHORT_MSG = "Referer"
    ARGS_GEO_BYPASS_SHORT_MSG = "Geo Aylanib o'tish"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Sertifikatni tekshirish"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Jonli boshidan"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Jonli boshidan yo'q"
    ARGS_USER_AGENT_SHORT_MSG = "User-Agent"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Ro'yxat yo'q"
    ARGS_NO_PART_SHORT_MSG = "Qism yo'q"
    ARGS_NO_CONTINUE_SHORT_MSG = "Davom yo'q"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Audio formati"
    ARGS_EMBED_METADATA_SHORT_MSG = "Meta kiritish"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Thumbnail kiritish"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Thumbnail yozish"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Bir vaqtda"
    ARGS_FORCE_IPV4_SHORT_MSG = "IPv4 majburlash"
    ARGS_FORCE_IPV6_SHORT_MSG = "IPv6 majburlash"
    ARGS_XFF_SHORT_MSG = "XFF Header"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Chunk hajmi"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Subtitr kutilishi"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Eski ulanish"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Sertifikat tekshirish yo'q"
    ARGS_USERNAME_SHORT_MSG = "Foydalanuvchi nomi"
    ARGS_PASSWORD_SHORT_MSG = "Parol"
    ARGS_TWOFACTOR_SHORT_MSG = "2 faktorli autentifikatsiya"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Xatolarni e'tiborsiz qoldirish"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Min hajm"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Max hajm"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Ro'yxat elementlari"
    ARGS_DATE_SHORT_MSG = "Sana"
    ARGS_DATEBEFORE_SHORT_MSG = "Sana oldin"
    ARGS_DATEAFTER_SHORT_MSG = "Sana keyin"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP Header'lar"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Kutilish intervali"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Max kutilish"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Video formati"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Birlashtirish formati"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Fayl sifatida yuborish"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ Fayl juda katta. Maksimal hajmi 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Faqat .txt formatidagi fayllar ruxsat etiladi."
    COOKIES_INVALID_COOKIE_MSG = "❌ Fayl cookie.txt'ga o'xshamaydi ('# Netscape HTTP Cookie File' qatori yo'q)."
    COOKIES_ERROR_READING_MSG = "❌ Faylni o'qishda xatolik: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Cookie fayli mavjud va to'g'ri formatda"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} cookie fayli juda katta! Maksimal 100KB, olingan {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} cookie fayli yuklab olindi va papkangizda cookie.txt sifatida saqlandi.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} cookie manbasi mavjud emas (holat {status}). Iltimos, keyinroq qayta urinib ko'ring."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ {service} cookie faylini yuklab olishda xatolik. Iltimos, keyinroq qayta urinib ko'ring."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Foydalanuvchi yangi cookie faylini taqdim etdi.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie muvaffaqiyatli yangilandi:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ To'g'ri cookie emas.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube cookie manbalari sozlanmagan!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 YouTube cookie'larini yuklab olish va tekshirish...\n\nUrinish {attempt}/{total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Kirish rad etildi. Faqat admin."
    ADMIN_USER_LOGS_TOTAL_MSG = "Jami: <b>{total}</b>\n<b>{user_id}</b> - loglar (Oxirgi 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 keyboard activated!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Subtitr tili o'rnatildi: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Subtitr tili o'rnatildi: {flag} {name} (AUTO/TRANS yoqilgan)."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Subtitr tili menyusi yopildi."
    SUBS_DOWNLOADING_MSG = "💬 Subtitrlar yuklanmoqda..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Firebase kesh xotiraga qayta yuklanmoqda..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ COOKIE_URL sozlanmagan. /cookie ishlating yoki cookie.txt yuklang."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Masofaviy URL'dan cookie'lar yuklanmoqda..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Zaxira COOKIE_URL .txt faylga ishora qilishi kerak."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Zaxira cookie fayli juda katta (>100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie fayli zaxira orqali yuklab olindi va cookie.txt sifatida saqlandi"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Zaxira cookie manbasi mavjud emas (holat {status}). /cookie sinab ko'ring yoki cookie.txt yuklang."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Zaxira cookie'ni yuklab olishda xatolik. /cookie sinab ko'ring yoki cookie.txt yuklang."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Zaxira cookie yuklab olish paytida kutilmagan xatolik."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} brauzer o'rnatilmagan."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookie'lar brauzer yordamida saqlandi: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Cookie'larni saqlashda muvaffaqiyatsizlik: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube cookie'lari to'g'ri ishlayapti"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube cookie'lari muddati o'tgan yoki noto'g'ri\n\nYangi cookie'larni olish uchun /cookie ishlating"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - maxsus format\n• <code>/format 720</code> - 720p sifat\n• <code>/format 4k</code> - 4K sifat"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Maslahat yuborildi."
    FORMAT_MKV_TOGGLE_MSG = "MKV endi {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Masofaviy URL sozlanmagan"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Noto'g'ri fayl formati"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Fayl juda katta"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookie'lar muvaffaqiyatli yuklab olindi"
    COOKIES_SERVER_ERROR_MSG = "❌ Server xatoligi {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Yuklab olish muvaffaqiyatsiz"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Kutilmagan xatolik"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Brauzer o'rnatilmagan."
    COOKIES_MENU_CLOSED_MSG = "Menyu yopildi."
    COOKIES_HINT_CLOSED_MSG = "Cookie maslahati yopildi."
    IMG_HELP_CLOSED_MSG = "Yordam yopildi."
    SUBS_LANGUAGE_UPDATED_MSG = "Subtitr tili sozlamalari yangilandi."
    SUBS_MENU_CLOSED_MSG = "Subtitr tili menyusi yopildi."
    KEYBOARD_SET_TO_MSG = "Klaviatura {setting} ga o'rnatildi"
    KEYBOARD_ERROR_PROCESSING_MSG = "Sozlamani qayta ishlashda xatolik"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo yoqildi."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo o'chirildi."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW bulanish o'chirildi."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW bulanish yoqildi."
    SETTINGS_MENU_CLOSED_MSG = "Menyu yopildi."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "To'ldirish kutilishi faol. Keyinroq urinib ko'ring."
    OTHER_HELP_CLOSED_MSG = "Yordam yopildi."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Log xabari yopildi."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menyu yopildi."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Noto'g'ri hajm."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ MediaInfo yuborishda xatolik: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Xatolik yuz berdi: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - barcha log'lar"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - barcha {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Masofaviy URL'dan yuklab olish"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Brauzerni ochish"
    SELECT_BROWSER_MSG = "Cookie'larni yuklab olish uchun brauzerni tanlang:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Ushbu tizimda brauzer topilmadi. Siz cookie'larni masofaviy URL'dan yuklab olishingiz yoki brauzer holatini kuzatishingiz mumkin:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Brauzerni ochish</b> - mini-ilovada brauzer holatini kuzatish uchun"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ /check_cookie ishga tushirishda muvaffaqiyatsizlik"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ To'ldirish chegarasi. Keyinroq urinib ko'ring."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Brauzer cookie menyusini ochishda muvaffaqiyatsizlik"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Cookie sifatida saqlash maslahati yopildi."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Ishlatish:</b>\n<code>/link [quality] URL</code>\n\n<b>Misollar:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - eng yaxshi sifat\n• /link 720 https://youtube.com/watch?v=... - 720p yoki pastroq\n• /link 720p https://youtube.com/watch?v=... - yuqoridagi bilan bir xil\n• /link 4k https://youtube.com/watch?v=... - 4K yoki pastroq\n• /link 8k https://youtube.com/watch?v=... - 8K yoki pastroq</blockquote>\n\n<b>Sifat:</b> 1 dan 10000 gacha (mas., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K sifat"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>To'g'ridan-to'g'ri havola olingan</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio oqimi:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Oqim havolalarini olishda muvaffaqiyatsizlik"
    LINK_ERROR_GETTING_MSG = "❌ <b>Havolani olishda xatolik:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Noto'g'ri YouTube cookie indeksi: {selected_index}. Mavjud diapazon 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 YouTube cookie'larini yuklab olish va tekshirish...\n\nUrinish {attempt}/{total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 YouTube cookie'larini yuklab olish va tekshirish...\n\nUrinish {attempt}/{total}\n🔍 Cookie'lar tekshirilmoqda..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube cookie'lar muvaffaqiyatli yuklab olindi va tasdiqlandi!\n\nIshlatilgan manba {source}/{total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Barcha YouTube cookie'lar muddati o'tgan yoki mavjud emas!\n\nUlarni almashtirish uchun bot administratori bilan bog'laning."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube cookie qayta urinish chegarasi oshib ketdi!\n\n🔢 Maksimal: soatiga {limit} urinish\n⏰ Iltimos, keyinroq qayta urinib ko'ring"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ #{wrong} tegi taqiqlangan belgilarni o'z ichiga oladi. Faqat harflar, raqamlar va _ ruxsat etiladi.\nIltimos, ishlating: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Noto'g'ri argument!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Subtitr tili o'rnatildi: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Misol: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Tanlangan til: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Har doim so'rash rejimi {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Subtitrlar o'chirilgan"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Subtitr sozlamalari</b>\n\n{status_text}\n\nSubtitr tilini tanlang:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - subtitrlarni o'chirish\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Subtitr sozlamalari</b>\n\n{status_text}\n\nSubtitr tilini tanlang:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Sarlavha:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Davomiyligi:</b> {duration} sek\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video oqimi:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 720p maksimal sifat\n- 1.5 soat maksimal davomiylik\n- 500mb maksimal video hajmi</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️OGOHLANTIRISH: yuqori CPU ta'siri tufayli bu funksiya juda sekin (deyarli real-time) va quyidagilarga cheklangan:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Tezkor buyruqlar:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - subtitrlarni o'chirish\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - Har doim so'rash rejimini yoqish\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - tilni o'rnatish\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - AUTO/TRANS yoqilgan holda tilni o'rnatish\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - Har doim so'rash rejimini yoqish\n"
    SUBS_AUTO_SUBS_TEXT = " (avto-subtitrlar)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Avto-subtitrlar rejimi {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS disabled via command: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Always Ask enabled via command: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "SUBS language set via command: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "SUBS language + auto mode set via command: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "User opened /subs menu."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "User set subtitle language to: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "User toggled AUTO/TRANS mode to: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Foydalanuvchi Har doim so'rash rejimini o'zgartirdi: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Foydalanuvchi brauzerdan cookie so'radi."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Brauzer tanlash klaviaturasi faqat o'rnatilgan brauzerlar bilan yuborildi."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Brauzer tanlash yopildi."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "Zaxira COOKIE_URL muvaffaqiyatli ishlatildi (manba yashirilgan)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "Zaxira COOKIE_URL muvaffaqiyatsiz: status={status} (yashirilgan)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Zaxira COOKIE_URL kutilmagan xato: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Brauzer {browser} o'rnatilmagan."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Cookie brauzer yordamida saqlandi: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "Cookie fayli foydalanuvchi {user_id} uchun saqlandi."
    COOKIES_FILE_WORKING_LOG_MSG = "Cookie fayli mavjud, to'g'ri formatga ega va YouTube cookie'lari ishlayapti."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Cookie fayli mavjud va to'g'ri formatga ega, lekin YouTube cookie'lari muddati o'tgan."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Cookie fayli mavjud va to'g'ri formatga ega."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Cookie fayli mavjud, lekin noto'g'ri formatga ega."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Cookie fayli topilmadi."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{service} cookie URL foydalanuvchi {user_id} uchun bo'sh."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} cookie URL is not .txt (hidden)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} cookie file too large: {size} bytes (source hidden)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{service} cookie file downloaded for user {user_id} (source hidden)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Script not found: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Dastlabki holat xabari yuborilmadi"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "{script_path} ishga tushirishda xato: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Firebase cache avtomatik vazifa tomonidan qayta yuklandi."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Firebase cache admin tomonidan qayta yuklandi."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Firebase cache qayta yuklashda xato: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Translyatsiya boshlandi. Matn:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Translyatsiya xabari barcha foydalanuvchilarga yuborildi."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Translyatsiya xabari yuborilmadi: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Admin {user_id} URL uchun cache tozaladi: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Admin {user_id} porn ro'yxatini yangilash skriptini boshladi: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Porn ro'yxatini yangilash skripti admin {user_id} tomonidan muvaffaqiyatli yakunlandi"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Porn ro'yxatini yangilash skripti admin {user_id} tomonidan muvaffaqiyatsiz: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Admin {user_id} mavjud bo'lmagan skriptni ishga tushirishga harakat qildi: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Admin {user_id} tomonidan porn yangilash skriptini ishga tushirishda xato: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Admin {user_id} porn cache qayta yuklashni boshladi"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Admin {user_id} tomonidan porn cache qayta yuklashda xato: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Admin {user_id} NSFW uchun URL tekshirdi: {url} - Natija: {status}"
    
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
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Maxsus format menyusi yopildi"
    
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
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo yoqildi."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo o'chirildi."
    
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
    AUDIO_HELP_SHOWN_LOG_MSG = "/audio yordam ko'rsatildi"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "User requested playlist help."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Ro'yxat yordami yopildi."
    AUDIO_HINT_CLOSED_LOG_MSG = "Audio maslahati yopildi."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Direct link menu created via LINK button for user {user_id} from {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Failed to extract direct link via LINK button for user {user_id} from {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "LIST command executed for user {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Tezkor Embed: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Har doim so'rash menyusi {url} uchun yuborildi"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Xato keyin foydalanuvchi {user_id} uchun keshlangan sifatlar menyusi yaratildi: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Har doim so'rash menyusi xatosi {url} uchun: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Format is fixed via /args settings"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Audio"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Video"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Video"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Keyingi ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Oldingi"
    SUBTITLES_NEXT_BUTTON_MSG = "Next ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Barcha matn maydonlari bo'sh"
    SENDER_VIDEO_DURATION_MSG = "Video davomiyligi:"
    SENDER_UPLOADING_FILE_MSG = "📤 Fayl yuklanmoqda..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Video yuklanmoqda..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Video davomiyligi:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 fayl yuklandi."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Video ma'lumotlari"
    DOWN_UP_NUMBER_MSG = "Raqam"
    DOWN_UP_TITLE_MSG = "Sarlavha"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Video yuklab olindi."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Yuklash uchun qayta ishlanmoqda..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Bo'lingan {part} qism fayli yuklandi"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Yuklash yakunlandi"
    DOWN_UP_FILES_UPLOADED_MSG = "fayl yuklandi"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Yopish"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼KODEK"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBLYAJ"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 SUBTITRLAR"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Brauzer"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 To'g'ridan-to'g'ri havola olinmoqda..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Mavjud formatlar olinmoqda..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Video tavsifi olinmoqda..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Tavsifni olishda xatolik: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Video tavsifi mavjud emas"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Tavsifni yuborishda xatolik: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Video tavsifi foydalanuvchi {user_id} ga {url} ({title}) uchun yuborildi"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 gallery-dl ishga tushirilmoqda…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Davomiyligi:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Brauzer:</b> Veb-brauzerda ochish"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Mavjud formatlar"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Format ID'lardan qanday foydalanish:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Ro'yxatni olgandan keyin, aniq format ID'dan foydalaning:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - 401 formatini yuklab olish"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - yuqoridagi bilan bir xil"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - 140 formatini MP3 audio sifatida yuklab olish"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Faqat audio formatlar aniqlandi"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Bular MP3 audio fayllari sifatida yuklab olinadi."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Formatni qanday o'rnatish:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Aniq format ID'ni yuklab olish"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Sifat bo'yicha yuklab olish"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Eng yaxshi sifatni yuklab olish"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Har doim sifatni so'rash"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Faqat audio formatlar:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - 140 formatini MP3 audio sifatida yuklab olish"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Bular MP3 audio fayllari sifatida yuklab olinadi."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Yuqoridagi ro'yxatdan format ID'dan foydalaning"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Xatolik: Asl xabar topilmadi."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Formatlar sahifasi"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Formatlar menyusini ko'rsatishda xatolik"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Formatlarni olishda xatolik"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Mavjud formatlarni olishda xatolik."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Iltimos, keyinroq qayta urinib ko'ring."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp bu kontentni qayta ishlay olmaydi"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Tizim o'rniga gallery-dl ishlatishni tavsiya qiladi."
    ALWAYS_ASK_OPTIONS_MSG = "**Variantlar:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Rasm galereyalari uchun: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Bitta rasmlar uchun: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl ko'pincha Instagram, Twitter va boshqa ijtimoiy media kontenti uchun yaxshiroq ishlaydi."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Gallery-dl sinab ko'ring"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Format /args orqali belgilangan"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Subtitrlar"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Dublyaj qilingan audio"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Subtitrlar mavjud"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Subtitr tilini tanlang"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Subtitrlar topilmadi va kiritilmaydi"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Keshdan darhol qayta post qilish"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Audio tilini tanlang"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW pullik (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Yuklab olish sifatini tanlang"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Rasmni yuklab olish (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Videoni poketube'da tomosha qilish"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Videoga to'g'ridan-to'g'ri havola olish"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Mavjud formatlar ro'yxatini ko'rsatish"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Video kengaytmasini/codec'ni o'zgartirish"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Kiritish"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Faqat audioni ajratish"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW pullik (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Keshdan darhol qayta post qilish"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Videoni poketube'da tomosha qilish"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Audio tilini tanlang"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Eng yaxshi"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Boshqa"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝faqat subtitr"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Aqlli guruhlash"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Harakat tugmalari qatori qo'shildi (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Harakat tugmalari qatorlari qo'shildi (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Mavjud qatorga pastki tugmalar qo'shildi"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Yangi pastki qator yaratildi"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Ro'yxatda video topilmadi"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "Qo'llab-quvvatlanmaydigan URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Video topilmadi"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Video topilmadi"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Media topilmadi"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Bu tweet o'z ichiga olmaydi"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Video ma'lumotlarini olishda xatolik:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Video ma'lumotlarini olishda xatolik"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "<code>/clean</code> buyrug'ini bajarib, qayta urinib ko'ring. Agar xatolik davom etsa, YouTube autentifikatsiya talab qiladi. <code>/cookie</code> yoki <code>/cookies_from_browser</code> orqali cookies.txt'ni yangilang va qayta urinib ko'ring."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Menyu yopildi."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Qo'lda sifat tanlash"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Avtomatik aniqlash muvaffaqiyatsiz bo'lgani uchun sifatni qo'lda tanlang:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Barcha mavjud formatlar"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Mavjud sifatlar (keshdan)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Keshdan olingan sifatlar ishlatilmoqda - yangi formatlar mavjud bo'lmasligi mumkin"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Format yuklanmoqda"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Yuklanmoqda"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Progress kuzatuv bilan yuklanmoqda..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Format yordamida yuklanmoqda:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Audio format yordamida yuklanmoqda:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Eng yaxshi sifat yuklanmoqda..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Ma'lumotlar bazasi dump'i yuklanmoqda..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Yuklanmoqda"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Formatlar sahifasi"
    ALWAYS_ASK_FROM_CACHE_MSG = "(keshdan)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Xatolik: Asl xabar topilmadi. O'chirilgan bo'lishi mumkin. Iltimos, havolani qayta yuboring."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Xatolik: Asl URL topilmadi. Iltimos, havolani qayta yuboring."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>To'g'ridan-to'g'ri havola olindi</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Sarlavha:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Davomiyligi:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Video oqimi:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Audio oqimi:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Oqim havolalarini olishda muvaffaqiyatsizlik"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Foydalanuvchi {user_id} uchun {url} dan Always Ask menyusi orqali to'g'ridan-to'g'ri havola ajratildi"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Foydalanuvchi {user_id} uchun {url} dan Always Ask menyusi orqali to'g'ridan-to'g'ri havolani ajratishda muvaffaqiyatsizlik: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Foydalanuvchi {user_id} uchun {url} dan down_and_up_with_format orqali to'g'ridan-to'g'ri havola ajratildi"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Foydalanuvchi {user_id} uchun {url} dan down_and_up_with_format orqali to'g'ridan-to'g'ri havolani ajratishda muvaffaqiyatsizlik: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Foydalanuvchi {user_id} uchun {url} dan down_and_audio orqali to'g'ridan-to'g'ri havola ajratildi"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Foydalanuvchi {user_id} uchun {url} dan down_and_audio orqali to'g'ridan-to'g'ri havolani ajratishda muvaffaqiyatsizlik: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Audio keshdan yuborildi."
    AUDIO_PROCESSING_MSG = "🎙️ Audio qayta ishlanmoqda..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Audio yuklanmoqda:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Audio yuklab olish paytida xatolik yuz berdi."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Audio ma'lumotlarini ajratishda muvaffaqiyatsizlik"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Ro'yxatdagi {index} indeksida qo'llab-quvvatlanmaydigan fayl turi o'tkazib yuborilmoqda"
    AUDIO_FILE_NOT_FOUND_MSG = "Yuklab olingandan keyin audio fayl topilmadi."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ Audio yuborish muvaffaqiyatsiz: Fayl hajmi 0 B ga teng (pleylist indeksi {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ Audio fayli hali yuklanmoqda, iltimos kuting..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Audio fayl yuklanmoqda...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Audioni yuborishda muvaffaqiyatsizlik: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Ro'yxat audio yuborildi: {sent}/{total} fayl (sifat={quality}) foydalanuvchi{user_id} ga"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Audioni yuklab olishda muvaffaqiyatsizlik: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Yuklab olish timeout tufayli bekor qilindi (2 soat)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Video fayl topilmadi: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ Video yuborish muvaffaqiyatsiz: Fayl hajmi 0 B ga teng (pleylist indeksi {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ Video fayli hali yuklanmoqda, iltimos kuting..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Videoni qayta ishlashda xatolik: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Tavsif faylini yuborishda xatolik: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 agar video sarlavhasini o'zgartirmoqchi bo'lsangiz - videoga yangi matn bilan javob bering</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Subtitrlar aniqlanmadi"
    VIDEO_PROGRESS_MSG = "<b>Video:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Audio:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL chegarasi oshib ketdi: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Qayta ishlash yakunlandi"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Ko'p URL rejimida ro'yxat diapazonlari ruxsat etilmaydi. Faqat diapazonsiz bitta URL'larni yuboring (*1*5, /vid 1-10 va hokazo)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Sizning saytingiz qo'llab-quvvatlanganligini <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>bu yerda</a> tekshiring"
    ERROR_COOKIE_NEEDED_MSG = "Bu videoni yuklab olish uchun <code>cookie</code> kerak bo'lishi mumkin. Avval ish maydoningizni <b>/clean</b> buyrug'i orqali tozalang"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Youtube uchun - <b>/cookie</b> buyrug'i orqali <code>cookie</code> oling. Boshqa qo'llab-quvvatlanadigan sayt uchun - o'z cookie'ingizni yuboring (<a href='https://t.me/tg_ytdlp/203'>qo'llanma1</a>) (<a href='https://t.me/tg_ytdlp/214'>qo'llanma2</a>) va shundan keyin video havolangizni qayta yuboring."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Subtitr tilini tanlang"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Muqobil audio tillar yo'q"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Audio tilini tanlang"
    PAGE_NUMBER_MSG = "Sahifa {page}"
    TOTAL_PROGRESS_MSG = "Umumiy progress"
    SUBTITLE_MENU_CLOSED_MSG = "Subtitr menyusi yopildi."
    SUBTITLE_LANGUAGE_SET_MSG = "Subtitr tili o'rnatildi: {value}"
    AUDIO_SET_MSG = "Audio o'rnatildi: {value}"
    FILTERS_UPDATED_MSG = "Filterlar yangilandi"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Orqaga"
    CLOSE_BUTTON_TEXT = "🔚Yopish"
    LIST_BUTTON_TEXT = "📃Ro'yxat"
    IMAGE_BUTTON_TEXT = "🖼Rasm"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Sifatlar avtomatik aniqlanmadi\nBarcha mavjud formatlarni ko'rish uchun 'Boshqa' tugmasidan foydalaning.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Jonli oqim aniqlandi**\n\nDavom etayotgan yoki cheksiz jonli oqimlarni yuklab olish ruxsat etilmaydi.\n\nIltimos, oqim tugaguncha kuting va quyidagi holatlarda qayta yuklab olishga harakat qiling:\n• Oqim davomiyligi ma'lum\n• Oqim tugagan\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Jonli oqim yuklab olinmoqda</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Qism {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Maksimal hajm: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Jami davomiylik: {duration} sek"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Jonli oqim - Qism {chunk}</b>\n⏱ Davomiyligi: {duration} sek\n📦 Hajmi: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Qism {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Jonli oqim yuklab olish yakunlandi</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "{chunks} qism yuklab olindi"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Jami davomiylik: {duration} sek"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Jonli oqim yuklab olish to'xtatildi</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Foydalanuvchi papkasi o'chirildi (ehtimol /clean buyrug'i orqali)"
    LIVE_STREAM_FILE_DELETED_MSG = "Qism fayli o'chirildi (ehtimol /clean buyrug'i orqali)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Oqim tugadi"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Iltimos, `/format` buyrug'i yordamida boshqa formatni tanlang."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>To'g'ridan-to'g'ri havola olindi</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Sarlavha:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Davomiyligi:</b> {duration} sek\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Video oqimi:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Audio oqimi:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Fayl qayta ishlash xatosi**\n\nVideo yuklab olindi, lekin fayl nomidagi noto'g'ri belgilar tufayli qayta ishlash mumkin emas.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Fayl qayta ishlash xatosi**\n\nVideo yuklab olindi, lekin noto'g'ri argument xatosi tufayli qayta ishlash mumkin emas.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Sabab:**\n"
        "• Yuklangan fayl video fayl emas\n"
        "• Bu hujjat (PDF, DOC va boshqalar) yoki arxiv bo'lishi mumkin\n\n"
        "**Yechim:**\n"
        "• Havolani tekshiring - u videoga emas, hujjatga olib borishi mumkin\n"
        "• Boshqa havola yoki manbani sinab ko'ring\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Sabab:**\n"
        "• Fayl video sifatida qayta ishlanmaydi\n"
        "• Bu video fayl bo'lmasligi yoki fayl buzilgan bo'lishi mumkin\n\n"
        "**Yechim:**\n"
        "• Havolani tekshiring - u videoga emas, hujjatga olib borishi mumkin\n"
        "• Boshqa havola yoki manbani sinab ko'ring\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Format mavjud emas**\n\nSo'ralgan video formati bu video uchun mavjud emas.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Format ID {format_id} bu video uchun topilmadi.\n\nMavjud format ID'lar: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **AV1 formati bu video uchun mavjud emas.**\n\n**Mavjud formatlar:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Fayl qayta ishlash xatosi**\n\nAudio yuklab olindi, lekin fayl nomidagi noto'g'ri belgilar tufayli qayta ishlash mumkin emas.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Fayl qayta ishlash xatosi**\n\nAudio yuklab olindi, lekin noto'g'ri argument xatosi tufayli qayta ishlash mumkin emas.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Foydalanuvchi taqiqlangan kontentni kiritdi. Yuklab bo'lmaydi."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "NSFW blur buyruq orqali o'rnatildi: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Foydalanuvchi /nsfw menyusini ochdi."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: yopildi."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "{service} cookie yuklab olishda muvaffaqiyatsizlik: status={status} (url yashirilgan)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "{service} cookie yuklab olishda xatolik: {error} (url yashirilgan)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "{service} cookie yuklab olish paytida kutilmagan xatolik (url yashirilgan): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Foydalanuvchi {user_id} uchun cookie fayli yangilandi."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Foydalanuvchi {user_id} tomonidan noto'g'ri cookie kontenti taqdim etildi."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "Foydalanuvchi {user_id} uchun YouTube cookie URL'lari bo'sh."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "Foydalanuvchi {user_id} uchun {source} manbasidan YouTube cookie'lari yuklab olindi va tekshirildi."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Foydalanuvchi {user_id} uchun barcha YouTube cookie manbalari muvaffaqiyatsiz bo'ldi."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Admin {admin_id} tomonidan check_porn buyrug'ida xatolik: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Bo'linadigan qism hajmi {size} baytga o'rnatildi."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Video fayl bo'linishi bilan yuklash yakunlandi."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Ro'yxat videolari yuborildi: {sent}/{total} fayl (sifat={quality}) foydalanuvchi {user_id} ga"
    UNKNOWN_ERROR_MSG = "❌ Noma'lum xatolik: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Ro'yxatdagi {index} indeksida qo'llab-quvvatlanmaydigan fayl turi o'tkazib yuborilmoqda"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg topilmadi. Iltimos, FFmpeg'ni o'rnating."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ MP4'ga konvertatsiya qilishda muvaffaqiyatsizlik: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Subtitrlarni kiritish uzoq vaqt olishi mumkin (1 daqiqa video uchun 1 daqiqagacha)!\n🔥 Subtitrlarni yondirish boshlandi..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Subtitrlar cheklovlar tufayli kiritilmaydi (sifat/davomiylik/hajm)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Tanlangan til uchun subtitrlar mavjud emas"
    ERROR_SENDING_VIDEO_MSG = "❌ Videoni yuborishda xatolik: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Ro'yxat videolari yuborildi: {sent}/{total} fayl."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Yuklab olish timeout tufayli bekor qilindi (2 soat)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Videoni yuklab olishda muvaffaqiyatsizlik: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Xatolik: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON obyekt (lug'at) bo'lishi kerak."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Noto'g'ri JSON formati. Iltimos, to'g'ri JSON taqdim eting."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Qiymat {min_val} va {max_val} orasida bo'lishi kerak."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} o'rnatildi: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Haqiqiy"
    ARGS_FALSE_BUTTON_MSG = "❌ Yolg'on"
    ARGS_BACK_BUTTON_MSG = "🔙 Orqaga"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Yopish"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Haqiqiy"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Yolg'on"
    ARGS_NOT_SET_MSG = "O'rnatilmagan"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ AV1 formati bu video uchun mavjud emas.\n\nMavjud formatlar:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Yuklab olishda xatolik: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ Ro'yxatdagi {index} indeksida videolar topilmadi."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Video konvertatsiyasi muvaffaqiyatsiz**\n\nVideo noto'g'ri argument xatosi tufayli MP4'ga konvertatsiya qilinmadi.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Video konvertatsiyasi muvaffaqiyatsiz**\n\nVideo MP4'ga konvertatsiya qilinmadi.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Oqim havolalarini olishda muvaffaqiyatsizlik"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Havolani olishda xatolik:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ {index} indeksida kontent topilmadi"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Xatolik: Asl xabar topilmadi."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Xatolik: URL topilmadi."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Bu URL kiritilmaydi."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} codec bu video uchun mavjud emas"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} formati bu video uchun mavjud emas"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood limit. Keyinroq urinib ko'ring."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Cookie'ni tekshirish"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ AVTO (YouTube xatosi bo'yicha)"
    PROXY_OFF_BUTTON_MSG = "❌ O'CHIRILGAN"
    PROXY_CLOSE_BUTTON_MSG = "🔚Yopish"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Davlatni tanlang:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Mamlakat tanlashni tozalash"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Tanlangan mamlakat: {country} (kod: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Mavjud proksi-serverlar: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Bot avval HTTP, keyin SOCKS5 ni sinab ko'radi"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Tanlangan mamlakat uchun proksi avtomatik ravishda yoqiladi"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Mamlakat tanlovi tozalandi"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Mamlakat tanlovi tozalandi"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Tanlangan davlat: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Fayldagi mamlakatdan foydalanish: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Fayldagi mavjud mamlakatlar: {count}"

    PROXY_COUNTRY_NOT_AVAILABLE_MSG = "❌ Bu mamlakat uchun proxy mavjud emas. Boshqa mamlakatni sinab ko'ring."
    PROXY_COUNTRY_SET_BY_COMMAND_MSG = "✅ Proxy o'rnatildi: {country} (kod: {country_code})"
    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 Tanlangan mamlakat: {mamlakat} (kod: {mamlakat_kodi})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ Bu mamlakat uchun proksi yoqilgan"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ Proksi oʻchirilgan (yoqish uchun ALL (AVTO) tugmasini bosing)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ YOQILGAN"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ O'CHIRILGAN"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Yopish"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV: YOQILGAN"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV: O'CHIRILGAN"
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ YOQILGAN (Blur yo'q)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ YOQILGAN (Blur yo'q)"
    NSFW_OFF_BLUR_MSG = "✅ O'CHIRILGAN (Blur)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ O'CHIRILGAN (Blur)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Toza"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Foydalanuvchi {user} uchun javob xabarini qayta ishlashda xatolik: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Foydalanuvchi {user} ga broadcast yuborishda xatolik: {error}"
    ADMIN_LOGS_FORMAT_MSG = "{bot_name} loglari\nFoydalanuvchi: {user_id}\nJami loglar: {total}\nJoriy vaqt: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nJami {path}: {count}\nJoriy vaqt: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Jami foydalanuvchilar: {count}</i>\nOxirgi 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Porn keshlari admin {admin_id} tomonidan qayta yuklandi. Domenlar: {domains}, Kalit so'zlar: {keywords}, Saytlar: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Timeout xabarini yuborishda xatolik: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Tilni tanlang</b>"
    LANG_CHANGED_MSG = "✅ Til {lang_name} ga o'zgartirildi"
    LANG_ERROR_MSG = "❌ Tilni o'zgartirishda xatolik"
    LANG_CLOSED_MSG = "Til tanlash yopildi"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] callback: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Brauzer monitoring tugmasi URL bilan qo'shilmoqda: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "Brauzer monitoring URL sozlanmagan: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Klaviatura sozlamasi yangilandi!**\n\nYangi sozlama: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Klaviatura yashirishda muvaffaqiyatsizlik: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Foydalanuvchi {user_id} uchun havola ajratishda ishlaydigan YouTube cookie'lari ishlatilmoqda"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Foydalanuvchi {user_id} uchun havola ajratishda ishlaydigan YouTube cookie'lari mavjud emas"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Foydalanuvchi {user_id} uchun havola ajratishda mavjud YouTube cookie'lari ishlatilmoqda"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Foydalanuvchi {user_id} uchun havola ajratishda YouTube cookie'lari topilmadi"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Foydalanuvchi {user_id} papkasiga havola ajratish uchun global cookie fayli nusxalandi"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Foydalanuvchi {user_id} mediainfo buyrug'ini so'radi"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Foydalanuvchi {user_id} admin: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Foydalanuvchi {user_id} kanalda: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Foydalanuvchi {user_id} kirish rad etildi - admin emas va kanalda emas"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Foydalanuvchi {user_id} kirish ruxsati berildi"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Bu buyruq faqat administratorlar uchun mavjud."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ PO token qo'llab-quvvatlash bilan yuklab olish yakunlandi"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood limit. Keyinroq urinib ko'ring."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST token yangilash xatosi: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Firebase sessiyasini yopishda xatolik: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Asosiy db strukturasini ishga tushirishda xatolik: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ config.py'da barcha parametrlar o'rnatilmagan (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL o'rnatilmagan"
    DB_API_KEY_NOT_SET_MSG = "❌ idToken olish uchun FIREBASE_CONF.apiKey o'rnatilmagan"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Firebase dump yuklab olishda xatolik: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ REST orqali Firebase dump yuklab olishda muvaffaqiyatsizlik"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ _download_and_reload_cache'da xatolik: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Avtomatik reload_cache ishga tushirishda xatolik (urinish {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Barcha qayta urinishlar muvaffaqiyatsiz bo'ldi"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Firebase dump yuklab olish {datetime} da boshlandi"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Bog'liqlik mavjud emas: requests yoki Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ Ma'lumotlar bazasi bo'sh"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Logger yopishda xatolik: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Tozalash paytida xatolik: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Clone xatosi: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Clone timeout"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Clone istisnosi: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Foydalanuvchi tomonidan yangilanish bekor qilindi"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Repository muvaffaqiyatli klonlandi"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Backup'lar _backup/ papkasiga ko'chirildi"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Barcha modullar yuklandi"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Chiqishda tozalash yakunlandi"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Signal {signal} qabul qilindi, xushmuomala bilan o'chirilmoqda..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Iltimos, kuting..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 HLS oqimi yuklanmoqda:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "fragmentlar kutilmoqda"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Backup {ts} _backup/ papkasida topilmadi"
    RESTORE_FAILED_RESTORE_MSG = "❌ {src} -> {dest_path} tiklashda muvaffaqiyatsizlik: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Tiklandi: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Tafsilotlar:</b> {error_details}\n\nKritik xatolik tufayli yuklab olish to'xtatildi.\n\n💡 <b>Maslahat:</b> Agar 401 Unauthorized xatosi olsangiz, <code>/cookie instagram</code> buyrug'ini ishlatib ko'ring yoki Instagram bilan autentifikatsiya qilish uchun o'z cookie'laringizni yuboring."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domen porn qora ro'yxatida: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Porn kalit so'zlari topildi: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domen oq ro'yxatda: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Oq ro'yxat kalit so'zlari topildi: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Porn kalit so'zlari topilmadi"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API xatosi {index} indeksida, keyingi audio'ga o'tilmoqda..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API xatosi {index} indeksida, keyingi video'ga o'tilmoqda..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "Foydalanuvchi <b>url</b> kiritdi\n <b>foydalanuvchi nomi:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>Foydalanuvchi shunday kiritdi:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Kanalga qo'shilish"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Handler ro'yxatga olinmoqda: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Mening 5 cookie'larimni yuklab olish"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Brauzerning YT-cookie'sini olish"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Cookie faylingizni tekshirish"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Maxsus cookie yuklash"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Yopish"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Mavjud formatlar: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Yopish"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Yopish"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Yopish"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Yopish"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Yordam yopildi."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Yopildi"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Xatolik yuz berdi"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg PATH yoki loyiha papkasida topilmadi. Iltimos, FFmpeg'ni o'rnating."
    YTDLP_NOT_FOUND_MSG = "yt-dlp binar fayli PATH yoki loyiha papkasida topilmadi. Iltimos, yt-dlp'ni o'rnating."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Video {rounds} qismga bo'linadi, bu haddan tashqari bo'lishi mumkin"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Video qismi bo'linmoqda {current}/{total}: {start_time:.2f}s dan {end_time:.2f}s gacha"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Bo'linadigan qism {part} yaratishda muvaffaqiyatsizlik: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Bo'linadigan qism {part} muvaffaqiyatli yaratildi: {target_name} ({size} bayt)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Video qismini {part} bo'lishda xatolik: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Video {count} qismga muvaffaqiyatli bo'lindi"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Video bo'lish jarayonida xatolik: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Video {video_path} ni qayta ishlashda xatolik: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Video fayl mavjud emas: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "O'lchamlarni tahlil qilishda xatolik '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "'{size_result}' dan video o'lchamlarini aniqlab bo'lmadi, standart ishlatilmoqda: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Kichik rasm yaratishda xatolik: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Video davomiyligini tahlil qilishda xatolik: {error}, natija: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Kichik rasm {thumb_dir} da yaratilmadi, standart ishlatilmoqda"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Buyruqni bajarishda xatolik: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "FFmpeg yordamida kichik rasm yaratishda xatolik: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Lug'at bo'lmagan config bo'limi o'tkazib yuborilmoqda: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Sozlash {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Foydalanuvchi cookie'lari ishlatilmoqda: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Foydalanuvchi {user_id} uchun YouTube cookie'lari ishlatilmoqda"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Global cookie fayli foydalanuvchi {user_id} papkasiga nusxalandi"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Nusxalangan global cookie'lar foydalanuvchi cookie'lari sifatida ishlatilmoqda: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Foydalanuvchi {user_id} uchun global cookie faylini nusxalashda muvaffaqiyatsizlik: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Domen uchun --no-cookies ishlatilmoqda: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy so'ralgan, lekin import/get config muvaffaqiyatsiz: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "gallery-dl uchun proxy majburiy ishlatilmoqda: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy so'ralgan, lekin proxy konfiguratsiyasi to'liq emas"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Proxy helper muvaffaqiyatsiz: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Extractor elementlarini tahlil qilish..."
    GALLERY_DL_ITEM_COUNT_MSG = "Element {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Metadata topildi (tag 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL topildi (tag 3): {url}, metadata: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Metadata topildi (legacy): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL topildi (legacy): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Fayl nomi topildi: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Papka topildi: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Kengaytma topildi: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "{count} element tahlil qilindi, info: {info}, fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "gallery-dl config sozlanmoqda: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "A strategiyasi sinanmoqda: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor moduli topilmadi"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() bu build'da mavjud emas"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "extractor.find({url}) chaqirilmoqda"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Hech qanday extractor URL'ga mos kelmadi"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Extractor'da cookie'lar o'rnatilmoqda: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Extractor'da cookie'larni o'rnatishda muvaffaqiyatsizlik: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Extractor topildi, items() chaqirilmoqda"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "A strategiyasi muvaffaqiyatli, info olindi: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "A strategiyasi: extractor.items() hech qanday to'g'ri info qaytarmadi"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "A strategiyasi (extractor.find) muvaffaqiyatsiz: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "--get-urls dan fallback metadata: jami={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Barcha strategiyalar metadata olishda muvaffaqiyatsiz bo'ldi"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Rasm ma'lumotlarini ajratishda muvaffaqiyatsizlik: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job moduli topilmadi (buzilgan o'rnatish?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob bu build'da mavjud emas"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "gallery-dl papkasida yuklab olingan fayllarni qidirish"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Extractor'dan fayl nomlari bo'yicha fayllarni topishga harakat qilish"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Foydalanuvchi {user_id} uchun args o'qishda xatolik: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Video{video_path} ni qayta ishlashda xatolik: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Foydalanuvchi {user_id} da send_as_file yoqilgan, hujjat sifatida yuborilmoqda"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video takroriy timeout; send_document'ga o'tilmoqda"
    SENDER_CAPTION_TOO_LONG_MSG = "Sarlavha juda uzun, minimal sarlavha bilan sinab ko'rilmoqda"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (minimal sarlavha) timeout; send_document'ga o'tilmoqda"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Minimal sarlavha bilan videoni yuborishda xatolik: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "To'liq tavsif faylini yuborishda xatolik: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Vaqtinchalik tavsif faylini olib tashlashda xatolik: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "NO_FILTER_DOMAINS'dagi domen uchun match_filter o'tkazib yuborilmoqda: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Foydalanuvchi {user_id} uchun format aniqlash uchun foydalanuvchi URL'idagi mavjud YouTube cookie'lari tekshirilmoqda"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Mavjud YouTube cookie'lari foydalanuvchi {user_id} uchun format aniqlash uchun foydalanuvchi URL'ida ishlaydi - ular ishlatilmoqda"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Mavjud YouTube cookie'lari foydalanuvchi URL'ida muvaffaqiyatsiz bo'ldi, foydalanuvchi {user_id} uchun format aniqlash uchun yangilarini olishga harakat qilinmoqda"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Foydalanuvchi {user_id} uchun format aniqlash uchun YouTube cookie manbasi {i} sinanmoqda"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "{i} manbasidan YouTube cookie'lari foydalanuvchi {user_id} uchun format aniqlash uchun foydalanuvchi URL'ida ishlaydi - foydalanuvchi papkasiga saqlandi"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "{i} manbasidan YouTube cookie'lari foydalanuvchi {user_id} uchun format aniqlash uchun foydalanuvchi URL'ida ishlamaydi"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Foydalanuvchi {user_id} uchun format aniqlash uchun {i} manbasidan YouTube cookie'larni yuklab olishda muvaffaqiyatsizlik"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Foydalanuvchi {user_id} uchun format aniqlash uchun barcha YouTube cookie manbalari muvaffaqiyatsiz bo'ldi, cookie'siz sinab ko'riladi"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Foydalanuvchi {user_id} uchun format aniqlash uchun YouTube cookie manbalari sozlanmagan, cookie'siz sinab ko'riladi"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Foydalanuvchi {user_id} uchun format aniqlash uchun YouTube cookie'lari topilmadi, yangilarini olishga harakat qilinmoqda"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Foydalanuvchi {user_id} uchun format aniqlash uchun YouTube cookie'lari ishlatilmoqda (Always Ask menyusida allaqachon tekshirilgan)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Foydalanuvchi {user_id} uchun format aniqlash uchun YouTube cookie'lari topilmadi, tiklashga harakat qilinmoqda..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Foydalanuvchi {user_id} papkasiga format aniqlash uchun global cookie fayli nusxalandi"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Foydalanuvchi {user_id} uchun global cookie faylini nusxalashda muvaffaqiyatsizlik: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "get_video_formats'da domen uchun --no-cookies ishlatilmoqda: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "Ilova hali ishga tushirilmagan. {name} ga kirish mumkin emas"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Sarlavha:</b> <code>{caption}</code>\n<b>Foydalanuvchi id:</b> <code>{user_id}</code>\n<b>Foydalanuvchi ismi:</b> <code>{users_name}</code>\n<b>Video fayl id:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor'da xatolik: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor'da kutilmagan xatolik: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 Video havolasi</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL konfiguratsiyada mavjud emas"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin ishga tushirildi"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken yangilandi"
    DB_LOG_FOR_USER_ADDED_MSG = "Foydalanuvchi uchun log qo'shildi"
    DB_DATABASE_CREATED_MSG = "db yaratildi"
    DB_BOT_STARTED_MSG = "Bot ishga tushdi"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY config.py'ga saqlandi: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Ro'yxat qismi allaqachon keshlangan: {path_parts}, o'tkazib yuborilmoqda"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: hech qanday URL/sifat variantlari uchun kesh topilmadi, bo'sh lug'at qaytarilmoqda"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: katta diapazon uchun tez hisoblash: {cached_count} keshlangan videolar"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: hash {url_hash}, sifat {quality_key} uchun kesh topilmadi"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: hech qanday URL variantlari uchun kesh topilmadi, None qaytarilmoqda"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Kirish rad etildi. Faqat admin."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Avtomatik Firebase kesh qayta yuklash yangilandi!\n\n📊 Holat: {status}\n⏰ Jadval: har {interval} soatda 00:00 dan\n🕒 Keyingi qayta yuklash: {next_exec} ({delta_min} daqiqada)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Avtomatik Firebase kesh qayta yuklash to'xtatildi!\n\n📊 Holat: ❌ O'CHIRILGAN\n💡 Qayta yoqish uchun /auto_cache on ishlating"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Noto'g'ri argument. /auto_cache on | off | N (1..168) ishlating"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Interval 1 va 168 soat orasida bo'lishi kerak"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Interval o'rnatishda muvaffaqiyatsizlik"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Avtomatik Firebase kesh interval yangilandi!\n\n📊 Holat: ✅ YOQILGAN\n⏰ Jadval: har {interval} soatda 00:00 dan\n🕒 Keyingi qayta yuklash: {next_exec} ({delta_min} daqiqada)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Avtomatik Firebase kesh qayta yuklash boshlandi!\n\n📊 Holat: ✅ YOQILGAN\n⏰ Jadval: har {interval} soatda 00:00 dan\n🕒 Keyingi qayta yuklash: {next_exec} ({delta_min} daqiqada)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Avtomatik Firebase kesh qayta yuklash to'xtatildi!\n\n📊 Holat: ❌ O'CHIRILGAN\n💡 Qayta yoqish uchun /auto_cache on ishlating"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Avtomatik qayta yuklash YOQILGAN; keyingisi {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Avtomatik qayta yuklash admin tomonidan O'CHIRILGAN."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Avtomatik qayta yuklash interval {interval}h ga o'rnatildi; keyingisi {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Avtomatik qayta yuklash boshlandi; keyingisi {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Avtomatik qayta yuklash admin tomonidan to'xtatildi."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase kesh yuklandi: {count} asosiy tugun"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Firebase kesh fayli topilmadi, bo'sh kesh bilan boshlanmoqda: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Firebase kesh yuklashda muvaffaqiyatsizlik: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase kesh qayta yuklandi: {count} asosiy tugun"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Firebase kesh fayli topilmadi: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Firebase kesh qayta yuklashda muvaffaqiyatsizlik: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 Siz botdan bloklangansiz! Blokdan chiqish uchun {Config.ADMIN_USERNAME} bilan bog'laning\n<blockquote>P.S. Kanalni tark etmang - siz avtomatik ravishda bloklanasiz ⛔️</blockquote>\n🌍Tilni o'zgartirish /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Video formatlari topilmadi. Rasm yuklovchisini sinab ko'rilmoqda…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram xabar yuborishni chekladi.\n⏳ Iltimos, kuting: {time_str}\nTaymerni yangilash uchun URL'ni yana 2 marta yuboring."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Oqim URL'ini nusxalash uchun tugmani bosing, keyin VLC ilovasiga yopishtiring</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Oqim URL'ini nusxalash uchun tugmani bosing, keyin VLC ilovasiga yopishtiring</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Havolani olishda xatolik:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Formatlar faylini yuborishda xatolik: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Formatlarni olishda muvaffaqiyatsizlik:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Tahlil qilinmoqda... (6 sek kutish)"
    AA_PROCESSING_MSG = "🔎 Tahlil qilinmoqda..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ #{wrong} tegi taqiqlangan belgilarni o'z ichiga oladi. Faqat harflar, raqamlar va _ ruxsat etiladi.\nIltimos, ishlating: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Guruhda ishlash uchun botga admin huquqlari kerak. Iltimos, botni bu guruhning admini qiling."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Salom {first_name},\n \n<i>Bu bot🤖 har qanday videolarni to'g'ridan-to'g'ri telegramga yuklab olishi mumkin.😊 Ko'proq ma'lumot uchun <b>/help</b> ni bosing</i> 👈\n\n<blockquote>P.S. 🔞NSFW kontent ehtimoli tufayli - ☁️<b>Bulutli saqlash</b>, 📁<b>Fayl ulashish</b>, 🔗<b>URL qisqartirgichlar</b> va 🔞<b>Porno saytlardan</b> yuklab olish pullik! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ @tg_ytdlp kanalini 🗑<b>o'chirmang/obunani bekor qilmang</b> va botga 🤖<b>URL/buyruqlarni ortiqcha spam qilmang</b> - botdan foydalanishdan avtomatik chetlashtirilasiz ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Olib tashlash uchun fayllar yo'q."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 Barcha fayllar muvaffaqiyatli olib tashlandi!\n\nOlib tashlangan fayllar:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ OLDINGI YUKLAB OLISH TUGAGUNCHA KUTING"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "check_user'da App instance None"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict None, yuklab olishga ruxsat berilmoqda"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict None, subtitr kiritishga ruxsat berilmoqda"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: cheklovlar tekshirilmoqda - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: info_dict kalitlari: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Subtitr kiritish o'tkazib yuborildi: davomiylik {duration}s chegaradan {max_duration}s oshib ketdi"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Subtitr kiritish o'tkazib yuborildi: hajm {size_mb:.2f}MB chegaradan {max_size}MB oshib ketdi"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Subtitr kiritish o'tkazib yuborildi: sifat {width}x{height} (minimal tomon {min_side}p) chegaradan {max_quality}p oshib ketdi"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "ro'yxat"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ {service} uchun diapazon chegarasi oshib ketdi: {count} (maksimal {max_count}).\n\nMaksimal mavjud fayllarni yuklab olish uchun quyidagi buyruqlardan birini ishlating:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ {service} uchun diapazon chegarasi oshib ketdi: {count} (maksimal {max_count})\nFoydalanuvchi ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "PO token provider config'da o'chirilgan"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} YouTube domeni emas, PO token o'tkazib yuborilmoqda"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO token provider {base_url} da mavjud emas, standart YouTube ajratishga o'tilmoqda"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO token provider kesh tozalandi, keyingi so'rovda mavjudligi tekshiriladi"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Ilova instance hali mavjud emas"
    HELPER_USER_NAME_MSG = "Foydalanuvchi"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood wait aniqlandi, {wait_seconds} soniya kutish"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood wait aniqlandi, lekin vaqtni ajratib bo'lmadi, {retry_delay} soniya kutish"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno xatosi aniqlandi, {retry_delay} soniya kutish"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy konfiguratsiyasi to'liq emas, to'g'ridan-to'g'ri ulanish ishlatilmoqda"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Yopish"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Yopish"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Yopish"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Log fayli olib tashlandi."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Tag fayli olib tashlandi."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Format fayli olib tashlandi."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Split fayli olib tashlandi."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Mediainfo fayli olib tashlandi."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Subtitr sozlamalari olib tashlandi."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Klaviatura sozlamalari olib tashlandi."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Args sozlamalari olib tashlandi."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 NSFW sozlamalari olib tashlandi."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Proxy sozlamalari olib tashlandi."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Flood wait sozlamalari olib tashlandi."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Yopish"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Video yuklab olish buyrug'i"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Ishlatish: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Misollar:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (to'g'ri tartib)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (teskari tartib)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Shuningdek qarang: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Foydalanuvchi {user_id} add_bot_to_group buyrug'ini yopdi"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "YouTube ID'ni ajratishda muvaffaqiyatsizlik"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Kichik rasmni yuklab olishda muvaffaqiyatsizlik yoki juda katta"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Audio tilini tanlang"
    AA_NO_SUBTITLES_DETECTED_MSG = "Subtitrlar aniqlanmadi"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Subtitr tilini tanlang"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Autentifikatsiya xatosi"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Hisob topilmadi"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Hisob mavjud emas"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Tezlik chegarasi oshib ketdi"
    GALLERY_DL_NETWORK_ERROR_MSG = "Tarmoq xatosi"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Kontent mavjud emas"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Geografik cheklovlar"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Tasdiqlash talab qilinadi"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Qoida buzilishi"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Noma'lum xatolik"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Yuklab olish boshlandi</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Yopish"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Video yuklab olish buyrug'i</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Ishlatish: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Misollar:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Shuningdek qarang: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Flood limit. Keyinroq urinib ko'ring."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Cookie buyrug'i ishlatilishi</b>

<code>/cookie</code> - Cookie menyusini ko'rsatish
<code>/cookie youtube</code> - YouTube cookie'larini yuklab olish
<code>/cookie instagram</code> - Instagram cookie'larini yuklab olish
<code>/cookie tiktok</code> - TikTok cookie'larini yuklab olish
<code>/cookie x</code> yoki <code>/cookie twitter</code> - Twitter/X cookie'larini yuklab olish
<code>/cookie facebook</code> - Facebook cookie'larini yuklab olish
<code>/cookie custom</code> - Maxsus cookie ko'rsatmalarini ko'rsatish

<i>Mavjud xizmatlar bot konfiguratsiyasiga bog'liq.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Cookie fayli olib tashlandi va kesh tozalandi."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Oldingi"
    SUBS_BACK_BUTTON_MSG = "🔙Orqaga"
    SUBS_OFF_BUTTON_MSG = "🚫 O'CHIRILGAN"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - tilni o'rnatish"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - AUTO/TRANS bilan tilni o'rnatish"
    SUBS_VALID_OPTIONS_MSG = "To'g'ri variantlar:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 TIL"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 TOZALASH"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIE'LAR"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MEDIA"
    SETTINGS_INFO_BUTTON_MSG = "📖 MA'LUMOT"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ BOSHQA"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Faqat cookie'lar"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Loglar "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Taglar"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Format"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Bo'lish"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Subtitrlar"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Klaviatura"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Args"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Proxy"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Flood wait"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Barcha fayllar"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Mening 5 cookie'larimni yuklab olish"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Brauzerning YT-cookie'sini olish"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Cookie faylingizni tekshirish"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Maxsus cookie yuklash"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Sifat va formatni o'zgartirish"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - MediaInfo'ni YOQISH / O'CHIRISH"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Video qism hajmini o'zgartirish"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Videoni audio sifatida yuklab olish"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Subtitr til sozlamalari"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Ro'yxatlarni qanday yuklab olish"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - gallery-dl orqali rasmlarni yuklab olish"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - #tag'laringizni yuborish"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Ko'rsatmalarni olish"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Loglaringizni yuborish"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Ro'yxat yordami"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - qanday qilish"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - To'g'ridan-to'g'ri video havolalarini olish"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Proxy'ni yoqish/o'chirish"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Klaviatura tartibi"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Inline qidiruv yordamchisi"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp argumentlari"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - NSFW blur sozlamalari"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Tozalash variantlari</b>\n\nNimani tozalashni tanlang:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobil: @vid qidiruvni faollashtirish"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobil: @vid qidiruvni faollashtirish"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 O'CHIRILGAN"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 TO'LIQ"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[Rasmlar URL]({url})"
    IMAGE_ERROR_MSG = "❌ Xatolik: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Orqaga"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - maxsus format"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p sifat"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K sifat"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K sifat"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - aniq format ID"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - har doim menyuni ko'rsatish"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/eng yaxshi sifat"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Har doim so'rash (menyu + tugmalar)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Boshqalar (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (PC/Mac Telegram uchun eng yaxshi)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (mobil Telegram uchun eng yaxshi)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (MAKSIMAL sifat)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Maxsus (o'zingiz kiritasiz)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Brauzerdan"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 O'zingizniki"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Faollik yo'qligi tufayli kiritish rejimi avtomatik yopildi (5 daqiqa)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Hammasini qayta tiklash"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Joriy holatni ko'rish"
    ARGS_BACK_BUTTON_MSG = "🔙 Orqaga"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Bu sozlamalarni shablon sifatida saqlash uchun bu xabarni sevimlilaringizga yuboring.</i> \n\n<i>Bu sozlamalarni qo'llash uchun bu xabarni qayta bu yerga yuboring.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Joriy yt-dlp argumentlari:\n\nMaxsus sozlamalar sozlanmagan.\n\n---\n\n<i>Bu sozlamalarni shablon sifatida saqlash uchun bu xabarni sevimlilaringizga yuboring.</i> \n\n<i>Bu sozlamalarni qo'llash uchun bu xabarni qayta bu yerga yuboring.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Joriy yt-dlp argumentlari:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Sozlamalarni eksport qilish"
    ARGS_SETTINGS_READY_MSG = "Sozlamalar eksport qilishga tayyor! Saqlash uchun bu xabarni sevimlilaringizga yuboring."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Joriy yt-dlp argumentlari:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Xabardagi sozlamalarni tanib bo'lmadi. To'g'ri sozlamalar shablonini yuborganingizga ishonch hosil qiling."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Sozlamalar muvaffaqiyatli import qilindi!\n\nQo'llangan parametrlar: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Asosiy sozlamalar:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Import qilingan sozlamalarni saqlashda xatolik."
    ARGS_ERROR_IMPORTING_MSG = "❌ Sozlamalarni import qilish paytida xatolik yuz berdi."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Cookie fayllarini yuklab olish</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Cookie faylini yuklab olish uchun xizmatni tanlang."
    COOKIE_MENU_SAVE_INFO_MSG = "Cookie fayllari sizning papkangizda cookie.txt sifatida saqlanadi."
    COOKIE_MENU_TIP_HEADER_MSG = "Maslahat: Shuningdek, to'g'ridan-to'g'ri buyruqdan foydalanishingiz mumkin:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – cookie'larni yuklab olish va tekshirish"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – indeks bo'yicha aniq manbadan foydalanish (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Keyin <code>/check_cookie</code> bilan tekshiring (RickRoll'da sinaydi)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Har doim so'rash"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Havola"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Tomosha qilish"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Sarlavha"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ KESISH"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Video Kesish</b>\n\nVideo davomiyligi: <b>{start_time} - {end_time}</b>\n\nIltimos, kerakli vaqt oralig'ini formatda yuboring:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nMisol: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Noto'g'ri format. Iltimos, ishlating: <code>HH:MM:SS-HH:MM:SS</code>\n\nMisol: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Noto'g'ri oraliq. Boshlanish vaqti tugash vaqtidan kichik bo'lishi kerak."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ Vaqt oralig'i video chegaralaridan tashqarida.\n\nVideo davomiyligi: <b>{start_time} - {end_time}</b>\n\nSizning oralig'ingiz bu chegaralar ichida bo'lishi kerak."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>Video kesiladi:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Qisman yakunlandi - {successful_uploads}/{total_files} audio fayl yuklandi."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Audio muvaffaqiyatli yuklab olindi va yuborildi - {total_files} fayl yuklandi."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Maxfiy TikTok hisobi</b>\n\n"
        "Bu TikTok hisobi maxfiy yoki barcha videolar maxfiydir.\n\n"
        "<b>💡 Yechim:</b>\n"
        "1. @{username} hisobiga obuna bo'ling\n"
        "2. <code>/cookie</code> buyrug'i yordamida cookie'laringizni botga yuboring\n"
        "3. Qayta urinib ko'ring\n\n"
        "<b>Cookie'larni yangilagandan keyin, qayta urinib ko'ring!</b>"
    )

    #######################################################
