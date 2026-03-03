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
    CREDITS_MSG = "<blockquote><i>Tarafından yönetiliyor</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Dili değiştir: /lang</b>"
    TO_USE_MSG = "<i>Bu botu kullanmak için @tg_ytdlp Telegram kanalına abone olmanız gerekir.</i>\nKanala katıldıktan sonra <b>video bağlantınızı tekrar gönderin, bot sizin için indirecektir</b> ❤️\n\n<blockquote>P.S. Olası 🔞NSFW içeriği nedeniyle - ☁️<b>Bulut Depolama</b>, 📁<b>Dosya Paylaşımları</b>, 🔗<b>URL kısaltıcılar</b> ve 🔞<b>Porno sitelerinden</b> indirme ücretlidir! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ @tg_ytdlp kanalını 🗑<b>silme/abonelikten çıkma</b> ve bota 🤖<b>aşırı URL/komut SPAM’i yapma</b> - bot kullanımından otomatik yasaklanırsınız ⛔️</blockquote>"

    ERROR1 = "URL bağlantısı bulunamadı. Lütfen <b>https://</b> veya <b>http://</b> ile bir URL girin"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Çalma Listeleri (yt-dlp)</b>

Çalma listelerini indirmek için URL'sini sonunda <code>*start*end</code> aralıklarıyla gönderin. Örneğin: <code>URL*1*5</code> (1'den 5'e kadar ilk 5 video dahil).<code>URL*-1*-5</code> (1'den 5'e kadar son 5 video dahil).
Veya <code>/vid BAŞLANGIÇ-BİTİŞ URL</code> kullanabilirsiniz. Örneğin: <code>/vid 3-7 URL</code> (baştan 3'ten 7'ye kadar videoları indirir). <code>/vid -3-7 URL</code> (sondan 3'ten 7'ye kadar videoları indirir). <code>/audio</code> komutu için de çalışır.

<b>Örnekler:</b>

🟥 <b>YouTube çalma listesinden video aralığı:</b> (🍪 gerekli)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(1'den 5'e kadar ilk 5 videoyu indirir)
🟥 <b>YouTube çalma listesinden tek video:</b> (🍪 gerekli)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(sadece 3. videoyu indirir)

⬛️ <b>TikTok profili:</b> (🍪 gerekli)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(kullanıcı profilinden ilk 10 videoyu indirir)

🟪 <b>Instagram hikayeleri:</b> (🍪 gerekli)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(ilk 3 hikayeyi indirir)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(albümden ilk 10 hikayeyi indirir)

🟦 <b>VK videoları:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(kullanıcı/grup profilinden ilk 3 videoyu indirir)

⬛️<b>Rutube kanalları:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(kanaldan 2'den 4'e kadar videoları indirir)

🟪 <b>Twitch klipleri:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(kanaldan ilk 3 klibi indirir)

🟦 <b>Vimeo grupları:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(gruptan ilk 2 videoyu indirir)

🟧 <b>Pornhub modelleri:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(model profilinden ilk 2 videoyu indirir)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(prompt'unuza göre arama sonuçlarından ilk 3 videoyu indirir)

ve böyle devam eder...
bakın <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">desteklenen siteler listesi</a>
</blockquote>

<blockquote expandable>🖼 <b>Görseller (gallery-dl)</b>

Birçok platformdan görsel/fotoğraf/albüm indirmek için <code>/img URL</code> kullanın.

<b>Örnekler:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Aralıklar:</b>
<code>/img 11-20 https://example.com/album</code> — öğeler 11..20
<code>/img 11- https://example.com/album</code> — 11'den sona kadar (veya bot limiti)

<i>Desteklenen platformlar vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor vb. içerir. Tam liste:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">gallery-dl desteklenen siteler</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Video İndirme Botu - Yardım</b>

📥 <b>Temel Kullanım:</b>
• Herhangi bir bağlantı gönder → bot indirir
  <i>bot otomatik olarak yt-dlp ile videoları ve gallery-dl ile görselleri indirmeye çalışır.</i>
• <b>Birden fazla URL:</b> Kalite seçim modunda (<code>/format</code>) bir mesajda <b>10 URL</b>'ye kadar gönderebilirsiniz. Her URL yeni bir satırda veya boşluklarla ayrılmış.
• <code>/audio URL</code> → ses çıkar
• <code>/link [quality] URL</code> → doğrudan bağlantılar al
• <code>/proxy</code> → tüm indirmeler için proxy'yi etkinleştir/devre dışı bırak
• Videoya metinle yanıt ver → başlığı değiştir

📋 <b>Çalma Listeleri ve Aralıklar:</b>
• <code>URL*1*5</code> → ilk 5 videoyu indir
• <code>URL*-1*-5</code> → son 5 videoyu indir
• <code>/vid 3-7 URL</code> → <code>URL*3*7</code> olur
• <code>/vid -3-7 URL</code> → <code>URL*-3*-7</code> olur

🍪 <b>Çerezler ve Özel:</b>
• Özel videolar için *.txt çerez yükle
• <code>/cookie [service]</code> → çerezleri indir (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → dizine göre kaynak seç (1–N)
• <code>/cookies_from_browser</code> → tarayıcıdan çıkar
• <code>/check_cookie</code> → çerezi doğrula
• <code>/save_as_cookie</code> → metni çerez olarak kaydet

🧹 <b>Temizleme:</b>
• <code>/clean</code> → yalnızca medya dosyaları
• <code>/clean all</code> → her şey
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Ayarlar:</b>
• <code>/settings</code> → ayarlar menüsü
• <code>/format</code> → kalite ve format
• <code>/split</code> → videoyu parçalara böl
• <code>/mediainfo on/off</code> → medya bilgisi
• <code>/nsfw on/off</code> → NSFW bulanıklık
• <code>/tags</code> → kaydedilmiş etiketleri görüntüle
• <code>/sub on/off</code> → altyazılar
• <code>/keyboard</code> → klavye (OFF/1x3/2x3)

🏷️ <b>Etiketler:</b>
• URL'den sonra <code>#tag1#tag2</code> ekle
• Etiketler başlıklarda görünür
• <code>/tags</code> → tüm etiketleri görüntüle

🔗 <b>Doğrudan Bağlantılar:</b>
• <code>/link URL</code> → en iyi kalite
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → belirli kalite

⚙️ <b>Hızlı Komutlar:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → kalite ayarla
• <code>/keyboard off/1x3/2x3/full</code> → klavye düzeni
• <code>/split 100mb-2000mb</code> → parça boyutunu değiştir
• <code>/subs off/ru/en auto</code> → altyazı dili
• <code>/list URL</code> → mevcut formatların listesi
• <code>/mediainfo on/off</code> → medya bilgisini aç/kapat
• <code>/proxy on/off</code> → tüm indirmeler için proxy'yi etkinleştir/devre dışı bırak

📊 <b>Bilgi:</b>
• <code>/usage</code> → indirme geçmişi
• <code>/search</code> → @vid üzerinden satır içi arama

🖼 <b>Görseller:</b>
• <code>URL</code> → görsel URL'lerini indir
• <code>/img URL</code> → URL'den görselleri indir
• <code>/img 11-20 URL</code> → belirli aralığı indir
• <code>/img 11- URL</code> → 11'den sona kadar indir

👨‍💻 <i>Geliştirici:</i> @upekshaip
🤝 <i>Katkıda Bulunan:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Çerezinizi <b><u>cookie.txt</u></b> olarak kaydedin ve bot'a bir belge olarak gönderin.\n\n"
        "Ayrıca çerezleri <b><u>/save_as_cookie</u></b> komutuyla düz metin olarak da gönderebilirsiniz.\n"
        "<b><b><u>/save_as_cookie</u></b> Kullanımı:</b>\n\n"
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
        "<b><u>Talimatlar:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message
    SEARCH_MSG = """
🔍 <b>Video arama</b>

Satır içi aramayı @vid üzerinden etkinleştirmek için aşağıdaki düğmeye basın.

<blockquote>PC'de herhangi bir sohbette <b>"@vid Your_Search_Query"</b> yazmanız yeterlidir.</blockquote>
    """
    
    # Settings and Hints
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Görsel İndirme Komutu</b>\n\n"
        "Kullanım: <code>/img URL</code>\n\n"
        "<b>Örnekler:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Desteklenen platformlar (örnekler):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, vb. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">tam liste</a></blockquote>"
        "Ayrıca bakın: "
    )
    
    LINK_HINT_MSG = (
        "Kalite seçimiyle doğrudan video bağlantıları alın.\n\n"
        "Kullanım: /link + URL \n\n"
        "(örn. /link https://youtu.be/abc123)\n"
        "(örn. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Gruba Bot Ekle</b>

Gelişmiş özellikler ve daha yüksek limitler için botlarımı gruplarınıza ekleyin!
————————————
📊 <b>Mevcut ÜCRETSİZ Limitler (Bot'un DM'inde):</b>
<blockquote>•🗑 Sıralanmamış tüm dosyalardan dağınık çöp 👎
• Maks 1 dosya boyutu: <b>8 GB </b>
• Maks 1 dosya kalitesi: <b>SINIRSIZ</b>
• Maks 1 dosya süresi: <b>SINIRSIZ</b>
• Maks indirme sayısı: <b>SINIRSIZ</b>
• Bir mesajda maks URL: <b>10</b> (yalnızca kalite seçim modunda)
• 1 seferde maks çalma listesi öğesi: <b>50</b>
• 1 seferde maks TikTok videosu: <b>500</b>
• 1 seferde maks görsel: <b>1000</b>
• URL hız limitleri: <b>5/dak, 60/saat, 1000/gün</b>
• Komut limiti: <b>20/dak</b>
• 1 İndirme maks süre: <b>2 saat</b>
• 🔞 NSFW içeriği ücretlidir! 1⭐️ = $0.02
• 🆓 DİĞER TÜM MEDYA TAMAMEN ÜCRETSİZDİR
• 📝 Tüm içerik logları ve önbellekleme, yeniden indirirken anında yeniden gönderim için log kanallarıma</blockquote>

💬<b>Bu limitler yalnızca altyazılı video için:</b>
<blockquote>• Maks video+altyazı süresi: <b>1.5 saat</b>
• Maks video+altyazı dosya boyutu: <b>500 MB</b>
• Maks video+altyazı kalitesi: <b>720p</b></blockquote>
————————————
🚀 <b>Ücretli Grup Avantajları (2️⃣x Limitler):</b>
<blockquote>•  🗂 Konulara göre sıralanmış yapılandırılmış düzenli medya kasası 👍
•  📁 Botlar onları çağırdığınız konuda yanıt verir
•  📌 İndirme ilerlemesiyle otomatik sabitleme durum mesajı
•  🖼 /img komutu medyayı 10 öğeli albümler olarak indirir
• Maks 1 dosya boyutu: <b>16 GB</b> ⬆️
• Bir mesajda maks URL: <b>20</b> ⬆️ (yalnızca kalite seçim modunda)
• 1 seferde maks çalma listesi öğesi: <b>100</b> ⬆️
• 1 seferde maks TikTok videosu: 1000 ⬆️
• 1 seferde maks görsel: 2000 ⬆️
• URL hız limitleri: <b>10/dak, 120/saat, 2000/gün</b> ⬆️
• Komut limiti: <b>40/dak</b> ⬆️
• 1 İndirme maks süre: <b>4 saat</b> ⬆️
• 🔞 NSFW içeriği: Tam metadata ile ücretsiz 🆓
• 📢 Gruplar için kanalıma abone olmanıza gerek yok
• 👥 Tüm grup üyeleri ücretli işlevlere erişecek!
• 🗒 Log kanallarıma log yok / önbellek yok! Grup ayarlarında kopya/yeniden gönderimi reddedebilirsiniz</blockquote>

💬 <b>Altyazılı video için 2️⃣x limitler:</b>
<blockquote>• Maks video+altyazı süresi: <b>3 saat</b> ⬆️
• Maks video+altyazı dosya boyutu: <b>1000 MB</b> ⬆️
• Maks video+altyazı kalitesi: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Fiyatlandırma ve Kurulum:</b>
<blockquote>• Fiyat: <b>$5/ay</b> grupta 1 bot başına
• Kurulum: @iilililiiillliiliililliilliliiil ile iletişime geçin
• Ödeme: 💎TON veya diğer yöntemler💲
• Destek: Tam teknik destek dahil</blockquote>
————————————
Ücretsiz 🔞<b>NSFW</b>'yi açmak ve tüm limitleri ikiye katlamak (x2️⃣) için botlarımı grubunuza ekleyebilirsiniz.
Grubunuzun botlarımı kullanmasına izin vermemi istiyorsanız benimle iletişime geçin @iilililiiillliiliililliilliliiil
————————————
💡<b>İPUCU:</b> <blockquote>Arkadaşlarınızla herhangi bir miktarda para toplayabilirsiniz (örneğin 100 kişi) ve tüm grup için 1 satın alma yapabilirsiniz - TÜM GRUP ÜYELERİ O GRUPTAKİ TÜM BOT İŞLEVLERİNE TAM SINIRSIZ ERİŞİME SAHİP OLACAKTIR sadece <b>$0.05</b> karşılığında</blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW Modu: AÇIK✅</b>

• NSFW içeriği bulanıklaştırma olmadan gösterilecektir.
• Spoiler'lar NSFW medyaya uygulanmayacaktır.
• İçerik hemen görünür olacaktır

<i>Bulanıklığı etkinleştirmek için /nsfw off kullanın</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW Modu: KAPALI</b>

⚠️ <b>Bulanıklık etkin</b>
• NSFW içeriği spoiler altında gizlenecektir   
• Görüntülemek için medyaya tıklamanız gerekecektir
• Spoiler'lar NSFW medyaya uygulanacaktır.

<i>Bulanıklığı devre dışı bırakmak için /nsfw on kullanın</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Geçersiz parametre</b>

Kullanın:
• <code>/nsfw on</code> - bulanıklığı devre dışı bırak
• <code>/nsfw off</code> - bulanıklığı etkinleştir
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Önbellek kontrol ediliyor...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 İşleniyor..."
    DOWNLOADING_MSG = "📥 <b>Medya indiriliyor...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Görsel indiriliyor...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>İndirme tamamlandı</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "İndirildi:"
    SENT_STATUS_MSG = "Gönderildi:"
    PENDING_TO_SEND_STATUS_MSG = "Gönderilmeyi bekliyor:"
    TITLE_LABEL_MSG = "Başlık:"
    MEDIA_COUNT_LABEL_MSG = "Medya sayısı:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "İndirme tamamlandı, ses işleniyor..."
    VIDEO_PROCESSING_MSG = "📽 Video işleniyor..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Önbellekten gönderildi</b>\n\nGönderilen albümler: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Video önbellekten başarıyla gönderildi."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Çalma listesi videoları önbellekten gönderildi ({cached}/{total} dosya)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} video önbellekten gönderildi, eksik olanlar indiriliyor..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Önbellekten gönderildi: {cached}\n🔄 İndirme devam ediyor..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Medya analiz edilemedi, izin verilen maksimum aralıkla devam ediliyor (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Medya sayısı belirlenemedi, izin verilen maksimum aralıkla devam ediliyor (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Toplam medya sayısı belirlenemedi, belirtilen aralıkla devam ediliyor {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>Geçersiz URL</b>\n\nLütfen http:// veya https:// ile başlayan geçerli bir URL sağlayın"

    ERROR_OCCURRED_MSG = "❌ <b>Hata oluştu</b>\n\n<code>{url}</code>\n\nHata: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Video gönderme hatası: {error}"
    ERROR_UNKNOWN_MSG = "❌ Bilinmeyen hata: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Video indirmek için yeterli disk alanı yok."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Dosya boyutu {limit} GB limitini aşıyor. Lütfen izin verilen boyut içinde daha küçük bir dosya seçin."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>Tüm mevcut proxy'lerle video indirilemedi</b>\n\nProxy üzerinden yapılan tüm indirme denemeleri başarısız oldu.\nDeneyin:\n• Proxy işlevselliğini kontrol edin\n• Listeden başka bir proxy deneyin\n• Proxy olmadan indirin (mümkünse)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Bağlantı alma hatası:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram mesaj göndermeyi sınırladı.\n⏳ Lütfen bekleyin: {time}\nZamanlayıcıyı güncellemek için URL'yi tekrar 2 kez gönderin."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram mesaj göndermeyi sınırladı.\n⏳ Lütfen bekleyin: \nZamanlayıcıyı güncellemek için URL'yi tekrar 2 kez gönderin."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Altyazılar indirilemedi"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Doğrudan Stream Bağlantıları</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Başlık:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Süre:</b> {duration} sn\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Hata: Orijinal mesaj bulunamadı."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Etiket #{tag} yasak karakterler içeriyor. Yalnızca harfler, rakamlar ve _ izin verilir.\nLütfen kullanın: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Çalma listesi videoları gönderildi: {sent}/{total} dosya."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>Çalma Listesi İpucu</b>

Bir aralık belirtmeden çalma listesi bağlantısı gönderdiniz. Bot otomatik olarak ilk videoyu indirdi (<code>*1*1</code>).

<b>Bir çalma listesinden birden fazla video indirmek için bir aralık belirtin:</b>
• <code>URL*1*5</code> — ilk 5 video (1'den 5'e dahil)
• <code>URL*3*3</code> — yalnızca 3. video
• <code>/vid 1-10 URL</code> — alternatif format

Daha fazla bilgi: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ Önbellekten gönderildi: {cached}/{total} dosya."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Stream bağlantıları alınamadı"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Çerezleri indirmek için bir tarayıcı seçin:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Bu sistemde tarayıcı hatası oluştu. Çerezleri uzak URL'den indirilebilir veya tarayıcı kayıtlarını izleyebilirsiniz:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Tarayıcıyı Aç</b> - mini-uygulamada tarayıcıyı izlemek için"
    BROWSER_OPEN_BUTTON_MSG = "🌐Tarayıcıyı Aç"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Uzak URL'den İndir"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube çerez dosyası geri dönüş üzerinden indirildi ve cookie.txt olarak kaydedildi"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Desteklenen tarayıcı hatası oluştu ve COOKIE_URL yapılandırılmadı. /cookie kullanın veya cookie.txt dosyasını yükleyin."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL bir .txt dosyasına işaret eder."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Geri dönüş çerez dosyası çok büyük (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fallback çerez kaynağı kullanılamıyor (durum {status}). /cookie deneyin veya cookie.txt yükleyin."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Fallback çerez indirme hatası. /cookie hatası veya cookie.txt dosyasını yükleyin."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Fallback çerez indirme sırasında beklenmeyen hata."
    BTN_CLOSE = "🔚Kapat"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Geçersiz boole değeri"
    ARGS_CLOSED_MSG = "Kapatıldı"
    ARGS_ALL_RESET_MSG = "✅ Tüm argümanlar sıfırlandı"
    ARGS_RESET_ERROR_MSG = "❌ Argümanları sıfırlarken hata"
    ARGS_INVALID_PARAM_MSG = "❌ Geçersiz parametre"
    ARGS_BOOL_SET_MSG = "{value} olarak ayarlandı"
    ARGS_BOOL_ALREADY_SET_MSG = "Zaten {value} olarak ayarlanmış"
    ARGS_INVALID_SELECT_MSG = "❌ Geçersiz seçim değeri"
    ARGS_VALUE_SET_MSG = "{value} olarak ayarlandı"
    ARGS_VALUE_ALREADY_SET_MSG = "Zaten {value} olarak ayarlanmış"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Mevcut değer:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Örnekler:</b>\n• <code>default</code> - Varsayılan XFF stratejisini kullan\n• <code>never</code> - XFF başlığını asla kullanma\n• <code>US</code> - Amerika Birleşik Devletleri ülke kodu\n• <code>GB</code> - Birleşik Krallık ülke kodu\n• <code>DE</code> - Almanya ülke kodu\n• <code>FR</code> - Fransa ülke kodu\n• <code>JP</code> - Japonya ülke kodu\n• <code>192.168.1.0/24</code> - IP bloğu (CIDR)\n• <code>10.0.0.0/8</code> - Özel IP aralığı\n• <code>203.0.113.0/24</code> - Genel IP bloğu\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Not:</b> Bu --geo-bypass seçeneklerinin yerini alır. CIDR notasyonunda herhangi bir 2 harfli ülke kodu veya IP bloğu kullanın.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Örnek:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Lütfen yeni değerinizi gönderin."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Aralık:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Lütfen bir sayı gönderin."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Örnekler:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Not:</b> Bu başlıklar mevcut Referer ve User-Agent başlıklarına eklenecektir.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Mevcut yt-dlp Argümanları:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - True/False anahtarları\n• 📋 <b>Select</b> - Seçeneklerden seç\n• 🔢 <b>Numeric</b> - Sayı girişi\n• 📝🔧 <b>Text</b> - Metin/JSON girişi</blockquote>\n\nBu ayarlar tüm indirmelerinize uygulanacaktır."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "IPv6 bağlantılarını zorla",
        "force_ipv4": "IPv4 bağlantılarını zorla", 
        "no_live_from_start": "Canlı yayınları baştan indirme",
        "live_from_start": "Canlı yayınları baştan indir",
        "no_check_certificates": "HTTPS sertifika doğrulamasını bastır",
        "check_certificate": "SSL sertifikasını kontrol et",
        "no_playlist": "Yalnızca tek video indir, çalma listesi değil",
        "embed_metadata": "Video dosyasına metadata ekle",
        "embed_thumbnail": "Video dosyasına küçük resim ekle",
        "write_thumbnail": "Küçük resmi dosyaya yaz",
        "ignore_errors": "İndirme hatalarını yoksay ve devam et",
        "legacy_server_connect": "Eski sunucu bağlantılarına izin ver",
        "concurrent_fragments": "İndirilecek eşzamanlı parça sayısı",
        "xff": "X-Forwarded-For başlık stratejisi",
        "user_agent": "User-Agent başlığı",
        "impersonate": "Tarayıcı taklidi",
        "referer": "Referer başlığı",
        "geo_bypass": "Coğrafi kısıtlamaları atla",
        "hls_use_mpegts": "HLS için MPEG-TS kullan",
        "no_part": ".part dosyalarını kullanma",
        "no_continue": "Kısmi indirmeleri sürdürme",
        "audio_format": "Ses formatı",
        "video_format": "Video formatı",
        "merge_output_format": "Birleştirme çıktı formatı",
        "send_as_file": "Dosya olarak gönder",
        "username": "Kullanıcı adı",
        "password": "Şifre",
        "twofactor": "İki faktörlü kimlik doğrulama kodu",
        "min_filesize": "Minimum dosya boyutu (MB)",
        "max_filesize": "Maksimum dosya boyutu (MB)",
        "playlist_items": "Çalma listesi öğeleri",
        "date": "Tarih",
        "datebefore": "Tarihten önce",
        "dateafter": "Tarihten sonra",
        "http_headers": "HTTP başlıkları",
        "sleep_interval": "Bekleme aralığı",
        "max_sleep_interval": "Maksimum bekleme aralığı",
        "retries": "Yeniden deneme sayısı",
        "http_chunk_size": "HTTP parça boyutu",
        "sleep_subtitles": "Altyazılar için bekle"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp Argümanları Yapılandırması</b>\n\n<blockquote>📋 <b>Gruplar:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp Argümanları Yapılandırması</b>\n\n"
        "<blockquote>📋 <b>Gruplar:</b>\n"
        "• ✅/❌ <b>Boolean</b> - True/False anahtarları\n"
        "• 📋 <b>Select</b> - Seçeneklerden seç\n"
        "• 🔢 <b>Numeric</b> - Sayı girişi\n"
        "• 📝🔧 <b>Text</b> - Metin/JSON girişi</blockquote>\n\n"
        "Bu ayarlar tüm indirmelerinize uygulanacaktır."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Lütfen bekleyin..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Hata oluştu"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Girdi modu hareketsizlik nedeniyle otomatik olarak kapatıldı (5 dakika)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Girdi potansiyel olarak tehlikeli içerik içeriyor: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Girdi çok uzun (maks 1000 karakter)"
    ARGS_INVALID_URL_MSG = "❌ Geçersiz URL formatı. http:// veya https:// ile başlamalıdır"
    ARGS_INVALID_JSON_MSG = "❌ Geçersiz JSON formatı"
    ARGS_NUMBER_RANGE_MSG = "❌ Sayı {min_val} ile {max_val} arasında olmalıdır"
    ARGS_INVALID_NUMBER_MSG = "❌ Geçersiz sayı formatı"
    ARGS_DATE_FORMAT_MSG = "❌ Tarih YYYYMMDD formatında olmalıdır (örn., 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Yıl 1900 ile 2100 arasında olmalıdır"
    ARGS_MONTH_RANGE_MSG = "❌ Ay 01 ile 12 arasında olmalıdır"
    ARGS_DAY_RANGE_MSG = "❌ Gün 01 ile 31 arasında olmalıdır"
    ARGS_INVALID_DATE_MSG = "❌ Geçersiz tarih formatı"
    ARGS_INVALID_XFF_MSG = "❌ XFF 'default', 'never', ülke kodu (örn., US) veya IP bloğu (örn., 192.168.1.0/24) olmalıdır"
    ARGS_NO_CUSTOM_MSG = "Özel argüman ayarlanmadı. Tüm parametreler varsayılan değerleri kullanıyor."
    ARGS_RESET_SUCCESS_MSG = "✅ Tüm argümanlar varsayılanlara sıfırlandı."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Metin çok uzun. Maksimum 500 karakter."
    ARGS_ERROR_PROCESSING_MSG = "❌ Girdi işlenirken hata. Lütfen tekrar deneyin."
    ARGS_BOOL_INPUT_MSG = "❌ Dosya Olarak Gönder seçeneği için lütfen 'True' veya 'False' girin."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Lütfen geçerli bir sayı girin."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Bu seçeneği etkinleştirmek/devre dışı bırakmak için lütfen <code>True</code> veya <code>False</code> gönderin."
    ARGS_JSON_VALUE_REQUEST_MSG = "Lütfen geçerli JSON gönderin."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Henüz etiketiniz yok."
    TAGS_MESSAGE_CLOSED_MSG = "Etiket mesajı kapatıldı."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Altyazılar devre dışı bırakıldı ve Always Ask modu kapatıldı."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Always Ask etkinleştirildi."
    SUBS_LANGUAGE_SET_MSG = "✅ Altyazı dili şu şekilde ayarlandı: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️UYARI: yüksek CPU etkisi nedeniyle bu işlev çok yavaştır (neredeyse gerçek zamanlı) ve şunlarla sınırlıdır:\n"
        "- 720p maksimum kalite\n"
        "- 1.5 saat maksimum süre\n"
        "- 500mb maksimum video boyutu</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Hızlı komutlar:</b>\n"
        "• <code>/subs off</code> - altyazıları devre dışı bırak\n"
        "• <code>/subs on</code> - Always Ask modunu etkinleştir\n"
        "• <code>/subs ru</code> - dili ayarla\n"
        "• <code>/subs ru auto</code> - AUTO/TRANS ile dili ayarla"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Altyazılar devre dışı"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Seçilen dil: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Altyazılar indiriliyor..."
    SUBS_DISABLED_ERROR_MSG = "❌ Altyazılar devre dışı. Yapılandırmak için /subs kullanın."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Altyazı indirme yalnızca YouTube için desteklenir."
    SUBS_CAPTION_MSG = (
        "<b>💬 Subtitles</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Language:</b> {lang}\n"
        "<b>Type:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Altyazı SRT dosyası kullanıcıya gönderildi."
    SUBS_ERROR_PROCESSING_MSG = "❌ Altyazı dosyası işlenirken hata."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Altyazılar indirilemedi."
    SUBS_ERROR_MSG = "❌ Altyazılar indirilirken hata: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Bölünmüş parça boyutu şu şekilde ayarlandı: {size}"
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
    SPLIT_MENU_CLOSED_MSG = "Menüler."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Bot Ayarları</b>\n\nBir kategori seçin:"
    SETTINGS_MENU_CLOSED_MSG = "Menü kapatıldı."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Clean Options</b>\n\nChoose what to clean:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nChoose an action:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIA</b>\n\nChoose an action:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nChoose an action:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ MORE COMMANDS</b>\n\nChoose an action:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Komut yürütüldü."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Taşkın sınırı. Daha sonra deneyin."
    SETTINGS_HINT_SENT_MSG = "İpucu gönderildi."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Arama yardımcısı açıldı."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Bilinmeyen komut."
    SETTINGS_HINT_CLOSED_MSG = "İpucu kapatıldı."
    SETTINGS_HELP_SENT_MSG = "Kullanıcıya yardım metni gönderildi"
    SETTINGS_MENU_OPENED_MSG = "/settings menüsü açıldı"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Arama yardımcısı kapatıldı"
    SEARCH_CLOSED_MSG = "Kapatıldı"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Vekil {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Proxy ayarları kaydedilirken hata oluştu."
    PROXY_MENU_TEXT_MSG = "Tüm yt-dlp işlemleri için proxy sunucusu kullanmayı etkinleştir veya devre dışı bırak?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Tüm yt-dlp işlemleri için proxy sunucuların ({config_count} + {file_count} mevcut) kullanılması etkinleştirilsin mi devre dışı mı bırakılsın?\n\nALL (AUTO) etkinleştirildiğinde, proxy'ler izin verilen ülkelere (YouTube hata mesajında belirtilen) göre otomatik seçilir."
    PROXY_MENU_CLOSED_MSG = "Menü kapatıldı."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy etkin. Tüm yt-dlp işlemlerinde proxy kullanılacaktır."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy etkin. Tüm yt-dlp işlemleri {count} proxy sunucularını {method} seçim yöntemiyle kullanacaktır."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Proxy etkin (YouTube hatasında OTOMATİK).\n\nYouTube coğrafi kısıtlama hatası verdiğinde bot yalnızca hata mesajında belirtilen ülkelerin proxy'lerini kullanır (tüm proxy'ler sırayla denenmez)."
    PROXY_DISABLED_MSG = "❌ Proxy devre dışı bırakıldı."
    PROXY_TRYING_COUNTRY_MSG = "🔄 Proxy deneniyor: {country} ({current}/{total})"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Proxy ayarları kaydedilirken hata oluştu."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy etkinleştirildi."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy devre dışı bırakıldı."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ ÖNCEKİ İNDİRMENİZ TAMAMLANANA KADAR BEKLEYİN"
    AUDIO_HELP_MSG = (
        "<b>🎧 Ses İndirme Komutu</b>\n\n"
        "Kullanım: <code>/audio URL</code>\n\n"
        "<b>Örnekler:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Ayrıca bakın: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Ses ipucu kapatıldı."
    PLAYLIST_HELP_CLOSED_MSG = "Çalma listesi yardımı kapatıldı."
    USERLOGS_CLOSED_MSG = "Günlük mesajı kapatıldı."
    HELP_CLOSED_MSG = "Yardım kapatıldı."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW Blur Settings</b>\n\nNSFW content is <b>{status}</b>.\n\nChoose whether to blur NSFW content:"
    NSFW_MENU_CLOSED_MSG = "Menü kapatıldı."
    NSFW_BLUR_DISABLED_MSG = "NSFW bulanıklığı devre dışı bırakıldı."
    NSFW_BLUR_ENABLED_MSG = "NSFW bulanıklığı etkin."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW blur disabled."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW blur enabled."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "İndirilen dosyalar için MediaInfo göndermeyi etkinleştir veya devre dışı bırak?"
    MEDIAINFO_MENU_CLOSED_MSG = "Menü kapatıldı."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo etkinleştirildi. İndirmeden sonra dosya bilgisi gönderilecektir."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo devre dışı."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo etkinleştirildi."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo devre dışı."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Mevcut Formatları Listele</b>\n\n"
        "Bir URL için mevcut video/ses formatlarını al.\n\n"
        "<b>Kullanım:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Örnekler:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Format ID'leri nasıl kullanılır:</b>\n"
        "Listeyi aldıktan sonra, belirli format ID kullanın:\n"
        "• <code>/format id 401</code> - format 401'i indir\n"
        "• <code>/format id401</code> - yukarıdakiyle aynı\n"
        "• <code>/format id140 audio</code> - format 140'ı MP3 ses olarak indir\n\n"
        "Bu komut indirilebilecek tüm mevcut formatları gösterecektir."
    )
    LIST_PROCESSING_MSG = "🔄 Mevcut formatlar alınıyor..."
    LIST_INVALID_URL_MSG = "❌ Lütfen http:// veya https:// ile başlayan geçerli bir URL sağlayın"
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
    LIST_ERROR_SENDING_MSG = "❌ Format dosyası gönderilirken hata oluştu: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Failed to get formats:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Komut işlenirken bir hata oluştu"
    LIST_ERROR_CALLBACK_MSG = "Hata oluştu"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Format ID'lerini nasıl kullanılır:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Listeyi aldıktan sonra, belirli format ID kullanın:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - format 401'i indir\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - yukarıdakiyle aynı\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - format 140'ı MP3 ses olarak indir\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - yukarıdakiyle aynı\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Sadece ses formatları tespit edildi: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Bu formatlar MP3 ses dosyaları olarak indirilecektir.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Video-only formats:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Yukarıdaki listeden format kimliğini kullanın"
    
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
    LINK_INVALID_URL_MSG = "❌ Lütfen geçerli bir URL girin"
    LINK_PROCESSING_MSG = "🔗 Doğrudan bağlantı alınıyor..."
    LINK_DURATION_MSG = "⏱ <b>Süre:</b> {duration} sn\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video akışı:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Ses akışı:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
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
    KEYBOARD_ACTIVATED_MSG = "🎹 klavye etkinleştirildi!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Klavye gizlendi"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3 klavye etkinleştirildi!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3 klavye etkinleştirildi!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Emoji klavyesi etkinleştirildi!"
    KEYBOARD_ERROR_APPLYING_MSG = "Klavye ayarı uygulanırken hata {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Format şu şekilde ayarlandı: Always Ask. Her URL gönderdiğinizde kalite sorulacaktır."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format şu şekilde ayarlandı: Always Ask. Artık her URL gönderdiğinizde kalite sorulacaktır."
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
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Özel format menüsü kapatıldı"
    FORMAT_CODEC_SET_MSG = "✅ Codec set to {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Tarayıcı seçimi güncellendi."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Erişim reddedildi. Yalnızca yönetici."
    ACCESS_DENIED_ADMIN = "❌ Erişim reddedildi. Yalnızca yönetici."
    WELCOME_MASTER = "Hoş geldiniz Usta 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Üzgünüm... İndirme sırasında bir hata oluştu."
    SIZE_LIMIT_EXCEEDED = "❌ Dosya boyutu {max_size_gb} GB sınırını aşıyor. Lütfen izin verilen boyut dahilinde daha küçük bir dosya seçin."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Komut dosyası bulunamadı: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ {script_path} kullanarak yeni Firebase dökümü indiriliyor ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase önbelleği başarıyla yeniden yüklendi!"
    ADMIN_CACHE_FAILED_MSG = "❌ Firebase önbelleği yeniden yüklenemedi. {cache_file} olup olmadığını kontrol edin."
    ADMIN_ERROR_RELOADING_MSG = "❌ Önbellek yeniden yüklenirken hata oluştu: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ {script_path} çalıştırılırken hata:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Diğer tüm kullanıcılara tanıtım mesajı gönderildi</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Tanıtım mesajı gönderilemiyor. Bir mesaja yanıt vermeyi deneyin\nVeya bir hata oluştu</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ Kullanıcı henüz herhangi bir içerik indirmedi...</b> Günlüklerde mevcut değil"
    ADMIN_INVALID_COMMAND_MSG = "❌ Geçersiz komut"
    ADMIN_NO_DATA_FOUND_MSG = "❌ <code>{{path}</code> için önbellekte veri bulunamadı"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Sıra boş — henüz kimse kanaldan ayrılmadı."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Yasaklama kuyruğu</b>\nBekleyen toplam: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (sol: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… ve {extra} daha fazla kullanıcı."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "/block_user show • all • auto • 10s kullanın"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Sıradaki kullanıcılar engellendi: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Otomatik engelleme etkinleştirildi: yeni ayrılanlar hemen yasaklanacak."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Otomatik engelleme devre dışı bırakıldı."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Zamanlanmış otomatik engelleme penceresi her {interval} olarak ayarlandı."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Son {hours} saate (2 gün) ait kanal etkinliği günlüğü."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 Son {hours} saat (2 gün): {joined} katıldı, {hours} kaldı."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Son {hours} saatte (2 gün) etkinlik yok."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Toplam: 🟢 {joined} katıldı, 🔴 {left} ayrıldı."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Kanal etkinlik günlüğüne erişim yok. Botlar yönetici günlüklerini okuyamaz. Bu özelliği etkinleştirmek için yapılandırmada CHANNEL_GUARD_SESSION_STRING'e bir kullanıcı oturumu sağlayın."
    BAN_TIME_USAGE_MSG = "❌ Kullanım: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ 10s, 6m, 5h, 4d, 3w, 2M veya 1y gibi formatları kullanın."
    BAN_TIME_SET_MSG = "🕒 Kanal günlüğü tarama aralığı {interval} olarak ayarlandı."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Kanal tarama raporu\n"
        "Çalıştırma zamanı: {run_ts}\n"
        "Aralık: {interval}\n"
        "Yeni ayrılanlar: {new_leavers}\n"
        "Otomatik yasaklamalar: {auto_banned}\n"
        "Beklemede: {pending}\n"
        "Son event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Kullanım: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Yönetici bir yöneticiyi silemez"
    ADMIN_USER_BLOCKED_MSG = "Kullanıcı engellendi 🔒❌\n \nID: <code>{user_id}</code>\nEngellenme Tarihi: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> zaten engellendi ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Üzgünüm! Yönetici değilsiniz"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Kullanım: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Kullanıcı engeli kaldırıldı 🔓✅\n \nID: <code>{user_id}</code>\nEngel Kaldırma Tarihi: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code>'in engellemesi zaten kaldırıldı ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Engeli kaldırılan kullanıcılar: {count}\n⏱ Zaman damgası: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Kullanım: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Kullanıcı yok sayıldı 👁️❌\n \nID: <code>{user_id}</code>\nYok sayılma tarihi: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> zaten yok sayılıyor ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Kullanım: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Kullanıcı artık yok sayılmıyor 👁️✅\n \nID: <code>{user_id}</code>\nYok sayılmama tarihi: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> yok sayılmıyor ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Bot çalışma süresi -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Lütfen önbelleği temizlemek için bir URL girin.\nKullanım: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Lütfen geçerli bir URL girin.\nKullanım: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ URL için önbellek başarıyla temizlendi:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Bu bağlantı için önbellek bulunamadı."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Önbellek temizlenirken hata oluştu: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Erişim reddedildi. Yalnızca yönetici."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Porno listesi güncelleme komut dosyası çalıştırılıyor: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Komut dosyası başarıyla tamamlandı!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Betik başarıyla tamamlandı!\n\nÇıktı:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Betik {returncode} dönüş kodu ile başarısız oldu:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Komut dosyası çalıştırılırken hata oluştu: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Porno ve alanla ilgili önbellekler yeniden yükleniyor..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Porno önbellekleri başarıyla yeniden yüklendi!\n\n"
        "📊 Mevcut önbellek durumu:\n"
        "• Porno alan adları: {porn_domains}\n"
        "• Porno anahtar kelimeler: {porn_keywords}\n"
        "• Desteklenen siteler: {supported_sites}\n"
        "• BEYAZ LİSTE: {whitelist}\n"
        "• GRİ LİSTE: {greylist}\n"
        "• SİYAH LİSTE: {black_list}\n"
        "• BEYAZ ANAHTAR KELİMELER: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Porno önbelleği yeniden yüklenirken hata oluştu: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Lütfen kontrol etmek için bir URL girin.\nKullanım: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Lütfen geçerli bir URL girin.\nKullanım: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 URL NSFW içeriği için kontrol ediliyor...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Porno Kontrol Sonucu</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Durum:</b> <b>{status_text}</b>\n\n"
        "<b>Açıklama:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ URL kontrol edilirken hata oluştu: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Çerezler temizlendi."
    CLEAN_LOGS_CLEANED_MSG = "günlükler temizlendi."
    CLEAN_TAGS_CLEANED_MSG = "Etiketler temizlendi."
    CLEAN_FORMAT_CLEANED_MSG = "biçimi temizlendi."
    CLEAN_SPLIT_CLEANED_MSG = "bölünmüş temizlendi."
    CLEAN_MEDIAINFO_CLEANED_MSG = "medya bilgileri temizlendi."
    CLEAN_SUBS_CLEANED_MSG = "Altyazı ayarları temizlendi."
    CLEAN_KEYBOARD_CLEANED_MSG = "Klavye ayarları temizlendi."
    CLEAN_ARGS_CLEANED_MSG = "Args ayarları temizlendi."
    CLEAN_NSFW_CLEANED_MSG = "NSFW ayarları temizlendi."
    CLEAN_PROXY_CLEANED_MSG = "Proxy ayarları temizlendi."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Flood bekleme ayarları temizlendi."
    CLEAN_ALL_CLEANED_MSG = "Tüm dosyalar temizlendi."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 ÇEREZLER</b>\n\nBir işlem seçin:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Çerez dosyası kaydedildi"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ YouTube dışı çerezler için doğrulama atlandı"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Çerez dosyası mevcut ancak formatı yanlış"
    COOKIES_FILE_NOT_FOUND_MSG = "❌Çerez dosyası bulunamadı."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 YouTube çerezleri testi başlatılıyor...\n\nLütfen çerezlerinizi kontrol edip doğrularken bekleyin."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Mevcut YouTube çerezleriniz düzgün çalışıyor!\n\nYeni çerez indirmenize gerek yok."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Mevcut YouTube çerezleriniz süresi dolmuş veya geçersiz.\n\n🔄 Yeni çerezler indiriliyor..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} çerez kaynağı yapılandırılmamış!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} çerez kaynağı .txt dosyası olmalıdır!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Range limit exceeded: {range_count} files requested (maximum {max_img_files}).\n\nUse one of these commands to download maximum available files:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Kapat"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Medya limiti aşıldı: {count} dosya istendi (maksimum {max_count}).\n\nMaksimum mevcut dosyaları indirmek için bu komutlardan birini kullanın:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Bağlantıdan <b>{count}</b> medya öğesi bulundu"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "İndirme aralığını seçin:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Tarayıcı taklidi"
    ARGS_REFERER_DESC_MSG = "Referer başlığı"
    ARGS_USER_AGENT_DESC_MSG = "User-Agent başlığı"
    ARGS_GEO_BYPASS_DESC_MSG = "Coğrafi kısıtlamaları atla"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "SSL sertifikasını kontrol et"
    ARGS_LIVE_FROM_START_DESC_MSG = "Canlı yayınları baştan indir"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Canlı yayınları baştan indirme"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "HLS videoları için MPEG-TS konteyner kullan"
    ARGS_NO_PLAYLIST_DESC_MSG = "Sadece tek video indir, playlist değil"
    ARGS_NO_PART_DESC_MSG = ".part dosyalarını kullanma"
    ARGS_NO_CONTINUE_DESC_MSG = "Kısmi indirmeleri devam ettirme"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Çıkarma için ses formatı"
    ARGS_EMBED_METADATA_DESC_MSG = "Video dosyasına metadata göm"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Video dosyasına küçük resim göm"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Küçük resmi dosyaya yaz"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "İndirilecek eşzamanlı parça sayısı"
    ARGS_FORCE_IPV4_DESC_MSG = "IPv4 bağlantılarını zorla"
    ARGS_FORCE_IPV6_DESC_MSG = "IPv6 bağlantılarını zorla"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For başlık stratejisi"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP parça boyutu (bayt)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Altyazı indirmeden önce bekleme (saniye)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Eski sunucu bağlantılarına izin ver"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "HTTPS sertifika doğrulamasını bastır"
    ARGS_USERNAME_DESC_MSG = "Hesap kullanıcı adı"
    ARGS_PASSWORD_DESC_MSG = "Hesap şifresi"
    ARGS_TWOFACTOR_DESC_MSG = "İki faktörlü kimlik doğrulama kodu"
    ARGS_IGNORE_ERRORS_DESC_MSG = "İndirme hatalarını yoksay ve devam et"
    ARGS_MIN_FILESIZE_DESC_MSG = "Minimum dosya boyutu (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Maksimum dosya boyutu (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "İndirilecek playlist öğeleri (örn., 1,3,5 veya 1-5)"
    ARGS_DATE_DESC_MSG = "Bu tarihte yüklenen videoları indir (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Bu tarihten önce yüklenen videoları indir (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Bu tarihten sonra yüklenen videoları indir (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Özel HTTP başlıkları (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "İstekler arası bekleme süresi (saniye)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Maksimum bekleme süresi (saniye)"
    ARGS_RETRIES_DESC_MSG = "Yeniden deneme sayısı"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Video konteyner formatı"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Birleştirme için çıktı konteyner formatı"
    ARGS_SEND_AS_FILE_DESC_MSG = "Tüm medyayı medya yerine belge olarak gönder"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Taklit"
    ARGS_REFERER_SHORT_MSG = "Yönlendiren"
    ARGS_GEO_BYPASS_SHORT_MSG = "Geo Atla"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Sertifika Kontrol"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Canlı Başlangıç"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Canlı Başlangıç Yok"
    ARGS_USER_AGENT_SHORT_MSG = "User-Agent"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Playlist Yok"
    ARGS_NO_PART_SHORT_MSG = "Parça Yok"
    ARGS_NO_CONTINUE_SHORT_MSG = "Devam Yok"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Ses Formatı"
    ARGS_EMBED_METADATA_SHORT_MSG = "Meta Göm"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Küçük Resim Göm"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Küçük Resim Yaz"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Eşzamanlı"
    ARGS_FORCE_IPV4_SHORT_MSG = "IPv4 Zorla"
    ARGS_FORCE_IPV6_SHORT_MSG = "IPv6 Zorla"
    ARGS_XFF_SHORT_MSG = "XFF Başlık"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Parça Boyutu"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Altyazı Bekleme"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Eski Bağlantı"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Sertifika Kontrol Yok"
    ARGS_USERNAME_SHORT_MSG = "Kullanıcı Adı"
    ARGS_PASSWORD_SHORT_MSG = "Şifre"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Hataları Yoksay"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Min Boyut"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Max Boyut"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Playlist Öğeleri"
    ARGS_DATE_SHORT_MSG = "Tarih"
    ARGS_DATEBEFORE_SHORT_MSG = "Tarih Öncesi"
    ARGS_DATEAFTER_SHORT_MSG = "Tarih Sonrası"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP Başlıkları"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Bekleme Aralığı"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Max Bekleme"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Video Formatı"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Birleştirme Formatı"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Dosya Olarak Gönder"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ Dosya çok büyük. Maksimum boyut 100 KB'dir."
    COOKIES_INVALID_FORMAT_MSG = "❌ Yalnızca aşağıdaki formattaki .txt dosyalarına izin verilir."
    COOKIES_INVALID_COOKIE_MSG = "❌ Dosya cookie.txt dosyasına benzemiyor ('# Netscape HTTP Çerez Dosyası' satırı yok)."
    COOKIES_ERROR_READING_MSG = "❌ Dosya okunurken hata oluştu: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Çerez dosyası mevcut ve doğru formatta"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} çerez dosyası çok büyük! Maksimum 100KB, {size}KB aldı."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} çerez dosyası indirildi ve klasörünüze cookie.txt olarak kaydedildi.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} çerez kaynağı mevcut değil (durum {status}). Lütfen daha sonra tekrar deneyin."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ {service} çerez dosyası indirilirken hata oluştu. Lütfen daha sonra tekrar deneyin."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Kullanıcı yeni bir çerez dosyası sağladı.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Çerez başarıyla güncellendi:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Geçerli bir çerez değil.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube çerez kaynakları yapılandırılmamış!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Erişim reddedildi. Yalnızca yönetici."
    ADMIN_USER_LOGS_TOTAL_MSG = "Toplam: <b>{total}</b>\n<b>{user_id}</b> - loglar (Son 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 klavye etkinleştirildi!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Altyazı dili şu şekilde ayarlandı: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Altyazı dili şu şekilde ayarlandı: {flag} {name}, AUTO/TRANS etkin."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Altyazı dili menüsü kapatıldı."
    SUBS_DOWNLOADING_MSG = "💬 Altyazılar indiriliyor..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Firebase önbelleği belleğe yeniden yükleniyor..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ COOKIE_URL yapılandırılmamış. /cookie kullanın veya cookie.txt dosyasını yükleyin."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Uzak URL'den çerezler indiriliyor..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Yedek COOKIE_URL bir .txt dosyasına işaret etmelidir."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Yedek çerez dosyası çok büyük (>100 KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Yedek yoluyla indirilen ve cookie.txt olarak kaydedilen YouTube çerez dosyası"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Yedek çerez kaynağı mevcut değil (durum {status}). /cookie komutunu deneyin veya cookie.txt yükleyin."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Yedek çerez indirilirken hata oluştu. /cookie'yi deneyin veya cookie.txt dosyasını yükleyin."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Yedek çerez indirilirken beklenmeyen hata."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} tarayıcı yüklü değil."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Tarayıcı kullanılarak kaydedilen çerezler: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Çerezler kaydedilemedi: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube çerezleri düzgün çalışıyor"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube cookies are expired or invalid\n\nUse /cookie to get new cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - custom format\n• <code>/format 720</code> - 720p quality\n• <code>/format 4k</code> - 4K quality"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Hint sent."
    FORMAT_MKV_TOGGLE_MSG = "MKV is now {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Yapılandırılan uzak URL yok"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Geçersiz dosya formatı"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Dosya çok büyük"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Çerezler başarıyla indirildi"
    COOKIES_SERVER_ERROR_MSG = "❌ Sunucu hatası {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ İndirme başarısız oldu"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Beklenmeyen hata"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Tarayıcı yüklü değil."
    COOKIES_MENU_CLOSED_MSG = "Menü kapatıldı."
    COOKIES_HINT_CLOSED_MSG = "Çerez ipucu kapatıldı."
    IMG_HELP_CLOSED_MSG = "Yardım kapatıldı."
    SUBS_LANGUAGE_UPDATED_MSG = "Altyazı dili ayarları güncellendi."
    SUBS_MENU_CLOSED_MSG = "Altyazı dili menüsü kapatıldı."
    KEYBOARD_SET_TO_MSG = "Klavye {setting} olarak ayarlandı"
    KEYBOARD_ERROR_PROCESSING_MSG = "Ayar işlenirken hata"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo etkinleştirildi."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo devre dışı bırakıldı."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW bulanıklık devre dışı."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW bulanıklık etkin."
    SETTINGS_MENU_CLOSED_MSG = "Menü kapatıldı."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Flood wait aktif. Daha sonra deneyin."
    OTHER_HELP_CLOSED_MSG = "Yardım kapatıldı."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Log mesajı kapatıldı."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menü kapatıldı."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Geçersiz boyut."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ MediaInfo gönderilirken hata oluştu: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Bir hata oluştu: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - tüm günlükler"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - tümü {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Uzak URL'den indirin"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Tarayıcıyı aç"
    SELECT_BROWSER_MSG = "Çerezleri indirmek için bir tarayıcı seçin:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Bu sistemde tarayıcı bulunamadı. Çerezleri uzak URL'den indirebilir veya tarayıcı durumunu izleyebilirsiniz:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Tarayıcıyı Aç</b> - mini uygulamada tarayıcı durumunu izlemek için"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ /check_cookie çalıştırılamadı"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Taşkın sınırı. Daha sonra deneyin."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Tarayıcı çerez menüsü açılamadı"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Çerez ipucu olarak kaydet kapalı."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Usage:</b>\n<code>/link [quality] URL</code>\n\n<b>Examples:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - best quality\n• /link 720 https://youtube.com/watch?v=... - 720p or lower\n• /link 720p https://youtube.com/watch?v=... - same as above\n• /link 4k https://youtube.com/watch?v=... - 4K or lower\n• /link 8k https://youtube.com/watch?v=... - 8K or lower</blockquote>\n\n<b>Quality:</b> from 1 to 10000 (e.g., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K quality"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Yayın bağlantıları alınamadı"
    LINK_ERROR_GETTING_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Geçersiz YouTube çerez dizini: {selected_index}. Kullanılabilir aralık: 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 YouTube çerezleri indiriliyor ve kontrol ediliyor...\n\nDeneme {attempt} / {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 YouTube çerezleri indiriliyor ve kontrol ediliyor...\n\nDeneme {attempt} / {total}\n🔍 Çerezler test ediliyor..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube çerezleri başarıyla indirildi ve doğrulandı!\n\nKullanılan kaynak {source} / {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Tüm YouTube çerezleri süresi dolmuş veya mevcut değil!\n\nDeğiştirmeleri için bot yöneticisine başvurun."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube çerez yeniden deneme limiti aşıldı!\n\n🔢 Maksimum: saatte {limit} deneme\n⏰ Lütfen daha sonra tekrar deneyin"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Tag #{wrong} contains forbidden characters. Only letters, digits and _ are allowed.\nPlease use: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Invalid argument!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Altyazı dili seti: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Örnek: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Seçilen dil: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Always Ask modu {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Altyazılar devre dışı"
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
    SUBS_AUTO_SUBS_TEXT = "(otomatik abonelikler)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Otomatik abone modu {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS şu komutla devre dışı bırakıldı: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Her Zaman Sor şu komutla etkinleştirilir: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "SUBS dili şu komutla ayarlanır: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "SUBS dili + otomatik mod komutla ayarlanır: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Kullanıcı /subs menüsünü açtı."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Kullanıcı altyazı dilini şu şekilde ayarladı: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Kullanıcı AUTO/TRANS modunu şu şekilde değiştirdi: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Kullanıcı Her Zaman Sor modunu şu şekilde değiştirdi: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Kullanıcı tarayıcıdan çerez istedi."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Tarayıcı seçim klavyesi yalnızca yüklü tarayıcılarla birlikte gönderilir."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Tarayıcı seçimi kapatıldı."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "Geri dönüş COOKIE_URL başarıyla kullanıldı (kaynak gizlendi)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "Geri dönüş COOKIE_URL başarısız oldu: durum={status} (gizli)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Geri dönüş COOKIE_URL beklenmeyen hatası: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Tarayıcı {browser} yüklü değil."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Tarayıcı kullanılarak kaydedilen çerezler: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "{user_id} kullanıcısı için çerez dosyası kaydedildi."
    COOKIES_FILE_WORKING_LOG_MSG = "Çerez dosyası mevcut, doğru formatta ve YouTube çerezleri çalışıyor."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Çerez dosyası mevcut ve doğru formatta ancak YouTube çerezlerinin süresi dolmuş."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Çerez dosyası mevcut ve doğru formatta."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Çerez dosyası mevcut ancak formatı yanlış."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Çerez dosyası bulunamadı."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{service} çerez URL'si {user_id} kullanıcısı için boş."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} çerez URL'si .txt değil (gizli)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} çerez dosyası çok büyük: {size} bayt (kaynak gizli)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{service} kullanıcısı için indirilen çerez dosyası {user_id} (kaynak gizli)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Script not found: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "İlk durum mesajı gönderilemedi"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "{script_path} çalıştırılırken hata: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Firebase önbelleği otomatik görev tarafından yeniden yüklendi."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Firebase önbelleği yönetici tarafından yeniden yüklendi."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Firebase önbelleği yeniden yüklenirken hata: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Yayın başlatıldı. Metin:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Yayın mesajı tüm kullanıcılara gönderildi."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Mesaj yayınlanamadı: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Yönetici {user_id} URL için önbelleği temizledi: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Yönetici {user_id} yasaklı içerik listesi güncelleme scriptini başlattı: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Yasaklı içerik listesi güncelleme scripti yönetici {user_id} tarafından başarıyla tamamlandı"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Yasaklı içerik listesi güncelleme scripti yönetici {user_id} tarafından başarısız oldu: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Yönetici {user_id} var olmayan scripti çalıştırmaya çalıştı: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Yönetici {user_id} tarafından yasaklı içerik güncelleme scripti çalıştırılırken hata: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Yönetici {user_id} yasaklı içerik önbelleği yeniden yüklemeyi başlattı"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Yönetici {user_id} tarafından yasaklı içerik önbelleği yeniden yüklenirken hata: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Yönetici {user_id} URL'yi NSFW için kontrol etti: {url} - Sonuç: {status}"
    
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
    LINK_EXTRACTED_LOG_MSG = "{user_id} kullanıcısı için {url} kaynağından doğrudan bağlantı çıkarıldı"
    LINK_EXTRACTION_FAILED_LOG_MSG = "{user_id} kullanıcısı için {url}'den doğrudan bağlantı çıkarılamadı: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "{user_id} kullanıcısı için bağlantı komutunda hata: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Kullanıcı {user_id} klavyeyi {setting} olarak ayarladı"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Kullanıcı {user_id} klavyeyi {setting} olarak ayarladı"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo şu komutla ayarlandı: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Kullanıcı /mediainfo menüsünü açtı."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: kapalı."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo etkinleştirildi."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo devre dışı bırakıldı."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Bölme boyutu bağımsız değişken aracılığıyla {size} bayta ayarlandı."
    SPLIT_MENU_OPENED_LOG_MSG = "Kullanıcı menüyü açtı/böldü."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Bölünmüş seçim kapatıldı."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Bölme boyutu {size} bayt olarak ayarlandı."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Komut aracılığıyla proxy ayarı: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Kullanıcı /proxy menüsünü açtı."
    PROXY_MENU_CLOSED_LOG_MSG = "Proxy: kapalı."
    PROXY_ENABLED_LOG_MSG = "Proxy etkinleştirildi."
    PROXY_DISABLED_LOG_MSG = "Proxy devre dışı bırakıldı."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Yardım mesajı kapatıldı."
    AUDIO_HELP_SHOWN_LOG_MSG = "/audio yardımı gösterildi"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Kullanıcı oynatma listesi yardımını istedi."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Oynatma listesi yardımı kapatıldı."
    AUDIO_HINT_CLOSED_LOG_MSG = "Ses ipucu kapatıldı."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "{url} adresinden {user_id} kullanıcısı için LINK düğmesi aracılığıyla oluşturulan doğrudan bağlantı menüsü"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "{user_id} kullanıcısı için {url}: {error} kullanıcısı için BAĞLANTI düğmesi aracılığıyla doğrudan bağlantı çıkarılamadı"
    LIST_COMMAND_EXECUTED_LOG_MSG = "{user_id} kullanıcısı için LIST komutu yürütüldü, url: {url}"
    QUICK_EMBED_LOG_MSG = "Hızlı Gömme: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Her Zaman Sor menüsü {url} için gönderildi"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Hata sonrası kullanıcı {user_id} için önbelleğe alınmış kaliteler menüsü oluşturuldu: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Her Zaman Sor menüsü hatası {url} için: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Format /args ayarları ile sabitlendi"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Ses"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Video"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Video"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Sonraki ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Önceki"
    SUBTITLES_NEXT_BUTTON_MSG = "Sonraki ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Tüm metin alanları boş"
    SENDER_VIDEO_DURATION_MSG = "Video süresi:"
    SENDER_UPLOADING_FILE_MSG = "📤 Dosya yükleniyor..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Video yükleniyor..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Video süresi:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 dosya yüklendi."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Video Bilgisi"
    DOWN_UP_NUMBER_MSG = "Numara"
    DOWN_UP_TITLE_MSG = "Başlık"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Video indirildi."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Yükleme için işleniyor..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Bölünmüş {part} parça dosyası yüklendi"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Yükleme tamamlandı"
    DOWN_UP_FILES_UPLOADED_MSG = "dosyalar yüklendi"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Kapat"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼KODEK"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBLAJ"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 ABONE OL"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Tarayıcı"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Doğrudan bağlantı alınıyor..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Mevcut formatlar alınıyor..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Video açıklaması alınıyor..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Açıklama alınırken hata oluştu: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Video açıklaması mevcut değil"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Açıklama gönderilirken hata oluştu: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 {url} ({title}) için {user_id} kullanıcısına video açıklaması gönderildi"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Galeri-dl başlatılıyor…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Süre:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Biçim:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Tarayıcı:</b> Web tarayıcısında aç"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "İçin mevcut formatlar"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Format ID'lerini nasıl kullanılır:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Listeyi aldıktan sonra, belirli format ID kullanın:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - format 401'i indir"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - yukarıdakiyle aynı"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - format 140'ı MP3 ses olarak indir"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Sadece ses formatları tespit edildi"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Bu formatlar MP3 ses dosyaları olarak indirilecektir."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Format nasıl ayarlanır:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Belirli format ID'sini indir"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Kaliteye göre indir"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - En iyi kaliteyi indir"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Her zaman kalite sor"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Sadece ses formatları:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Format 140'ı MP3 ses olarak indir"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Bunlar MP3 ses dosyaları olarak indirilecektir."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Yukarıdaki listeden format ID kullanın"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Hata: Orijinal mesaj bulunamadı."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Formatlar sayfası"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Formatlar menüsü gösterilirken hata"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Formatlar alınırken hata oluştu"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Kullanılabilir formatlar alınırken hata oluştu."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Lütfen daha sonra tekrar deneyin."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp bu içeriği işleyemiyor"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Sistem bunun yerine gallery-dl kullanılmasını önerir."
    ALWAYS_ASK_OPTIONS_MSG = "**Seçenekler:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Resim galerileri için: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Tek görseller için: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl genellikle Instagram, Twitter ve diğer sosyal medya içerikleri için daha iyi çalışır."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Galeri-dl'yi deneyin"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Format /args ile düzeltildi"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Altyazılar"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Dublajlı ses"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Altyazılar mevcut"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Altyazı dilini seçin"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Abonelikler bulunamadı ve yerleştirilmiyor"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Önbellekten anında yeniden gönderme"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Ses dilini seçin"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW ödenir (⭐️$0,02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — İndirme kalitesini seçin"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Resmi indir (galeri-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Videoya doğrudan bağlantı alın"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Mevcut formatların listesini göster"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Video dahili/codec'ini değiştirin"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Göm"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Yalnızca sesi çıkart"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW ödenir (⭐️$0,02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Önbellekten anında yeniden gönderme"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Ses dilini seçin"
    ALWAYS_ASK_BEST_BUTTON_MSG = "En iyi"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Diğer"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝yalnızca abone olun"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Akıllı gruplama"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Eylem düğmesi satırı eklendi (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Eylem düğmesi satırları eklendi (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Mevcut satıra alt düğmeler eklendi"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Yeni alt satır oluşturuldu"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Oynatma listesinde video bulunamadı"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "Desteklenmeyen URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Hiçbir video bulunamadı"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Video bulunamadı"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Medya bulunamadı"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Bu tweet şunları içermiyor"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Video bilgileri alınırken hata oluştu:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Video bilgileri alınırken hata oluştu"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "<code>/clean</code> komutunu deneyin ve tekrar deneyin. Hata devam ederse YouTube'un yetkilendirilmesi gerekir. Cookies.txt dosyasını <code>/cookie</code> veya <code>/cookies_from_browser</code> aracılığıyla güncelleyin ve tekrar deneyin."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Menü kapatıldı."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Manuel Kalite Seçimi"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Otomatik algılama başarısız olduğundan kaliteyi manuel olarak seçin:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Mevcut Tüm Formatlar"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Mevcut Kaliteler (önbellekten)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Önbelleğe alınmış kaliteler kullanılıyor - yeni formatlar mevcut olmayabilir"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Format indiriliyor"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 İndiriliyor"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 İlerleme takibi ile indiriliyor..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Format kullanılarak indiriliyor:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Format kullanılarak ses indiriliyor:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 En iyi kalite indiriliyor..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Veritabanı dökümü indiriliyor..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 İndiriliyor"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Formatlar sayfası"
    ALWAYS_ASK_FROM_CACHE_MSG = "(önbellekten)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Hata: Orijinal mesaj bulunamadı. Silinmiş olabilir. Lütfen bağlantıyı tekrar gönderin."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Hata: Orijinal URL bulunamadı. Lütfen bağlantıyı tekrar gönderin."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Doğrudan bağlantı alındı</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Başlık:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Süre:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Biçim:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Video akışı:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Ses akışı:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Yayın bağlantıları alınamadı"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "{user_id} kullanıcısı için {url} adresinden Her Zaman Sor menüsü aracılığıyla alınan doğrudan bağlantı"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "{user_id} kullanıcısı için {url}: {error} kullanıcısı için Her Zaman Sor menüsü aracılığıyla doğrudan bağlantı çıkarılamadı"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "{user_id} kullanıcısı için {url}'dan down_and_up_with_format aracılığıyla doğrudan bağlantı çıkarıldı"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "{user_id} kullanıcısı için {url}: {error} için down_and_up_with_format aracılığıyla doğrudan bağlantı çıkarılamadı"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "{url} adresinden {user_id} kullanıcısı için down_and_audio aracılığıyla doğrudan bağlantı çıkarıldı"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "{url}'den {user_id} kullanıcısı için down_and_audio aracılığıyla doğrudan bağlantı çıkarılamadı: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Ses önbellekten gönderildi."
    AUDIO_PROCESSING_MSG = "🎙️ Ses işleniyor..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Ses indiriliyor:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Ses indirme sırasında hata oluştu."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Ses bilgileri çıkarılamadı"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "{index} dizinindeki oynatma listesinde desteklenmeyen dosya türü atlanıyor"
    AUDIO_FILE_NOT_FOUND_MSG = "İndirdikten sonra ses dosyası bulunamadı."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ Ses gönderme başarısız: Dosya boyutu 0 B'ye eşit (çalma listesi dizini {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ Ses dosyası hala indiriliyor, lütfen bekleyin..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Ses dosyası yükleniyor...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Ses gönderilemedi: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Çalma listesi sesi gönderildi: {sent}/{total} dosyalar (kalite={quality}){user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Ses indirilemedi: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Zaman aşımı nedeniyle indirme işlemi iptal edildi (2 saat)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Video dosyası bulunamadı: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ Video gönderme başarısız: Dosya boyutu 0 B'ye eşit (çalma listesi dizini {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ Video dosyası hala indiriliyor, lütfen bekleyin..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Video işlenirken hata oluştu: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Açıklama dosyası gönderilirken hata oluştu: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 video başlığını değiştirmek istiyorsanız - videoya yeni metinle yanıt verin</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Altyazı tespit edilmedi"
    VIDEO_PROGRESS_MSG = "<b>Video:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Ses:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL limiti aşıldı: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "İşleme tamamlandı"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Çoklu URL modunda playlist aralıklarına izin verilmez. Sadece aralıksız tek URL'ler gönderin (*1*5, /vid 1-10, vb.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Sitenizin desteklenip desteklenmediğini <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>buradan</a> kontrol edin"
    ERROR_COOKIE_NEEDED_MSG = "Bu videoyu indirmek için <code>cookie</code> gerekebilir. Önce <b>/clean</b> komutu ile çalışma alanınızı temizleyin"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Youtube için - <b>/cookie</b> komutu ile <code>cookie</code> alın. Diğer desteklenen siteler için - kendi cookie'nizi gönderin (<a href='https://t.me/tg_ytdlp/203'>kılavuz1</a>) (<a href='https://t.me/tg_ytdlp/214'>kılavuz2</a>) ve ardından video bağlantınızı tekrar gönderin."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Altyazı dili seçin"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Alternatif ses dilleri yok"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Ses dili seçin"
    PAGE_NUMBER_MSG = "Sayfa {page}"
    TOTAL_PROGRESS_MSG = "Toplam İlerleme"
    SUBTITLE_MENU_CLOSED_MSG = "Altyazı menüsü kapatıldı."
    SUBTITLE_LANGUAGE_SET_MSG = "Altyazı dili ayarlandı: {value}"
    AUDIO_SET_MSG = "Ses ayarlandı: {value}"
    FILTERS_UPDATED_MSG = "Filtreler güncellendi"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Geri"
    CLOSE_BUTTON_TEXT = "🔚Kapat"
    LIST_BUTTON_TEXT = "📃Liste"
    IMAGE_BUTTON_TEXT = "🖼Resim"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Qualities not auto-detected\nUse 'Other' button to see all available formats.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Live Stream Detected**\n\nDownloading of ongoing or infinite live streams is not allowed.\n\nPlease wait for the stream to end and try downloading again when:\n• The stream duration is known\n• The stream has finished\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Canlı Yayın İndirme</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Parça {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Maksimum boyut: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Toplam süre: {duration} sn"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Canlı Yayın - Parça {chunk}</b>\n⏱ Süre: {duration} sn\n📦 Boyut: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Parça {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Canlı Yayın İndirme Tamamlandı</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "{chunks} parça indirildi"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Toplam süre: {duration} sn"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Canlı Yayın İndirme Durduruldu</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Kullanıcı dizini silindi (muhtemelen /clean komutu ile)"
    LIVE_STREAM_FILE_DELETED_MSG = "Parça dosyası silindi (muhtemelen /clean komutu ile)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Yayın sona erdi"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Lütfen `/format` komutunu kullanarak farklı bir format seçin."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Title:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Ses akışı:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **File Processing Error**\n\nThe video was downloaded but couldn't be processed due to invalid characters in the filename.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **File Processing Error**\n\nThe video was downloaded but couldn't be processed due to an invalid argument error.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Neden:**\n"
        "• İndirilen dosya bir video dosyası değil\n"
        "• Bir belge (PDF, DOC, vb.) veya arşiv olabilir\n\n"
        "**Çözüm:**\n"
        "• Bağlantıyı kontrol edin - bir belgeye, videoya değil, götürebilir\n"
        "• Farklı bir bağlantı veya kaynak deneyin\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Neden:**\n"
        "• Dosya video olarak işlenemez\n"
        "• Video dosyası olmayabilir veya dosya bozuk olabilir\n\n"
        "**Çözüm:**\n"
        "• Bağlantıyı kontrol edin - bir belgeye, videoya değil, götürebilir\n"
        "• Farklı bir bağlantı veya kaynak deneyin\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Format Not Available**\n\nThe requested video format is not available for this video.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Format ID {format_id} not found for this video.\n\nAvailable format IDs: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **Bu video için AV1 formatı mevcut değil.**\n\n**Mevcut formatlar:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Dosya İşleme Hatası**\n\nSes indirildi ancak dosya adındaki geçersiz karakterler nedeniyle işlenemedi.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Dosya İşleme Hatası**\n\nSes indirildi ancak geçersiz argüman hatası nedeniyle işlenemedi.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Kullanıcı yasak içerik girdi. İndirilemiyor."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "NSFW bulanıklığı şu komutla ayarlandı: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Kullanıcı /nsfw menüsünü açtı."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: kapalı."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "{service} çerezi indirilemedi: durum={status} (url gizlendi)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "{service} çerezi indirilirken hata oluştu: {error} (url gizlendi)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "{service} çerezi indirilirken beklenmeyen hata (URL gizli): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "{user_id} kullanıcısı için çerez dosyası güncellendi."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Kullanıcı tarafından sağlanan geçersiz çerez içeriği {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "YouTube çerez URL'leri {user_id} kullanıcısı için boş."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "{user_id} kullanıcısı için {source} kaynağından indirilen ve doğrulanan YouTube çerezleri."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Kullanıcı {user_id} için tüm YouTube cookie kaynakları başarısız oldu."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Admin tarafından check_porn komutunda hata {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Bölünmüş parça boyutu {size} bayt olarak ayarlandı."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Video yükleme, dosya bölme işlemiyle tamamlandı."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Kullanıcıya gönderilen oynatma listesi videoları: {sent}/{total} dosyalar (kalite={quality}) {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Bilinmeyen hata: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Playlist'te {index} indeksindeki desteklenmeyen dosya türü atlanıyor"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg bulunamadı. Lütfen FFmpeg'i yükleyin."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ MP4'e dönüştürme başarısız: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Altyazı gömme uzun sürebilir (video süresinin 1 dakikası başına 1 dakikaya kadar)!\n🔥 Altyazı yakma başlatılıyor..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Altyazılar limitler nedeniyle gömülemez (kalite/süre/boyut)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Seçilen dil için altyazı mevcut değil"
    ERROR_SENDING_VIDEO_MSG = "❌ Video gönderme hatası: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Playlist videoları gönderildi: {sent}/{total} dosya."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ İndirme zaman aşımı nedeniyle iptal edildi (2 saat)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Video indirme başarısız: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Hata: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON bir nesne (sözlük) olmalıdır."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Geçersiz JSON formatı. Lütfen geçerli JSON sağlayın."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Değer {min_val} ile {max_val} arasında olmalıdır."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} şu şekilde ayarlandı: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Doğru"
    ARGS_FALSE_BUTTON_MSG = "❌ Yanlış"
    ARGS_BACK_BUTTON_MSG = "🔙 Geri"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Kapat"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Doğru"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Yanlış"
    ARGS_NOT_SET_MSG = "Ayarlanmadı"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ AV1 format is not available for this video.\n\nAvailable formats:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ İndirme hatası: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ {index} dizinindeki oynatma listesinde video bulunamadı."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Video Conversion Failed**\n\nThe video couldn't be converted to MP4 due to an invalid argument error.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Video Conversion Failed**\n\nThe video couldn't be converted to MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Yayın bağlantıları alınamadı"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ {index} dizininde içerik bulunamadı"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Hata: Orijinal mesaj bulunamadı."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Hata: URL bulunamadı."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Bu URL eklenemez."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} codec bu video için mevcut değil"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} biçimi bu video için mevcut değil"
    
    # Always Ask Menu button texts
    AA_AVC_BUTTON_MSG = "✅AVC"
    AA_AVC_BUTTON_INACTIVE_MSG = "☑️ AVC"
    AA_AVC_BUTTON_UNAVAILABLE_MSG = "❌ AVC"
    AA_AV1_BUTTON_MSG = "✅AV1"
    AA_AV1_BUTTON_INACTIVE_MSG = "☑️ AV1"
    AA_AV1_BUTTON_UNAVAILABLE_MSG = "❌ AV1"
    AA_VP9_BUTTON_MSG = "✅VP9"
    AA_VP9_BUTTON_INACTIVE_MSG = "☑️ VP9"
    AA_VP9_BUTTON_UNAVAILABLE_MSG = "❌ VP9"
    AA_MP4_BUTTON_MSG = "✅ MP4"
    AA_MP4_BUTTON_INACTIVE_MSG = "☑️ MP4"
    AA_MP4_BUTTON_UNAVAILABLE_MSG = "❌ MP4"
    AA_MKV_BUTTON_MSG = "✅MKV"
    AA_MKV_BUTTON_INACTIVE_MSG = "☑️ MKV"
    AA_MKV_BUTTON_UNAVAILABLE_MSG = "❌ MKV"

    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood limit. Try later."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Çerezleri Kontrol Et"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ OTOMATİK (YouTube hatasında)"
    PROXY_OFF_BUTTON_MSG = "❌ KAPALI"
    PROXY_CLOSE_BUTTON_MSG = "🔚Kapat"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Ülke Seçin:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Ülke Seçimini Temizle"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Seçilen ülke: {country} (kod: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Kullanılabilir proxy'ler: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Bot önce HTTP'yi deneyecek, sonra SOCKS5'i deneyecek"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Seçilen ülke için proxy otomatik olarak etkinleştirilir"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Ülke seçimi temizlendi"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Ülke seçimi temizlendi"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Seçilen ülke: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Ülkeyi dosyadan kullanma: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Dosyadaki mevcut ülkeler: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 Seçilen ülke: {country} (kod: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ Bu ülke için proxy etkin"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ Proxy devre dışı (etkinleştirmek için ALL (AUTO) tuşuna basın)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ AÇIK"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ KAPALI"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Kapat"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ AÇIK (Bulanıklık Yok)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ON (No Blur)"
    NSFW_OFF_BLUR_MSG = "✅ KAPALI (Bulanıklaştırma)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ OFF (Blur)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Temiz"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Kullanıcı {user} için yanıt mesajı işlenirken hata: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Kullanıcı {user} için yayın gönderilirken hata: {error}"
    ADMIN_LOGS_FORMAT_MSG = "{bot_name} logları\nKullanıcı: {user_id}\nToplam loglar: {total}\nMevcut zaman: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nToplam {path}: {count}\nMevcut zaman: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Toplam Kullanıcılar: {count}</i>\nSon 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Porno önbellekleri admin {admin_id} tarafından yeniden yüklendi. Alan Adları: {domains}, Anahtar Kelimeler: {keywords}, Siteler: {sites}, BEYAZ LİSTE: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Zaman aşımı mesajı gönderilirken hata oluştu: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Dil seç</b>"
    LANG_CHANGED_MSG = "✅ Dil {lang_name} olarak değiştirildi"
    LANG_ERROR_MSG = "❌ Dil değiştirilirken hata"
    LANG_CLOSED_MSG = "Dil seçimi kapatıldı"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] geri arama: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "URL'li tarayıcı izleme düğmesi ekleniyor: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "Tarayıcı izleme URL'si yapılandırılmadı: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Keyboard setting updated!**\n\nNew setting: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Klavye gizlenemedi: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "{user_id} kullanıcısı için bağlantı çıkarmak amacıyla çalışan YouTube çerezlerini kullanma"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "{user_id} kullanıcısı için bağlantı çıkarma için çalışan YouTube çerezi yok"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "{user_id} kullanıcısı için bağlantı çıkarmak amacıyla mevcut YouTube çerezleri kullanılıyor"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Kullanıcı {user_id} için bağlantı çıkarma için YouTube cookie bulunamadı"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Bağlantı çıkarma için global cookie dosyası kullanıcı {user_id} klasörüne kopyalandı"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Kullanıcı {user_id} mediainfo komutu istedi"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Kullanıcı {user_id} yönetici: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Kullanıcı {user_id} kanalda: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Kullanıcı {user_id} erişimi reddedildi - yönetici değil ve kanalda değil"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Kullanıcı {user_id} erişimi verildi"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] geri arama: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Bu komut yalnızca yöneticiler tarafından kullanılabilir."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ PO belirteci desteğiyle indirme işlemi tamamlandı"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Taşkın sınırı. Daha sonra deneyin."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST belirteci yenileme hatası: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Firebase oturumu kapatılırken hata oluştu: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Temel veritabanı yapısı başlatılırken hata oluştu: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Config.py'de tüm parametreler ayarlanmamıştır (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL ayarlanmamış"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey, idToken almak için ayarlanmadı"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Firebase dökümü indirilirken hata oluştu: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Firebase dökümü REST aracılığıyla indirilemedi"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ _download_and_reload_cache hatası: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Auto reload_cache çalıştırılırken hata oluştu ({error}/{max_retries}enemesi): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Tüm yeniden deneme girişimleri başarısız oldu"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 {datetime} adresinden Firebase dökümü indirme işlemi başlatılıyor"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Bağımlılık mevcut değil: istekler veya Oturum"
    DB_DATABASE_EMPTY_MSG = "⚠️ Veritabanı boş"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Günlükçüyü kapatırken hata oluştu: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Temizleme sırasında hata: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Klonlama hatası: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Klonlama zaman aşımı"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Klon istisnası: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Güncelleme kullanıcı tarafından iptal edildi"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Depo başarıyla klonlandı"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Yedeklemeler _backup/ konumuna taşındı"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Tüm modüller yüklendi"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Çıkışta temizlik tamamlandı"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Received signal {signal}, shutting down gracefully..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Lütfen bekleyin..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 HLS akışını indirme:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "parçaları bekliyorum"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Yedekleme {ts} _backup/ dosyasında bulunamadı"
    RESTORE_FAILED_RESTORE_MSG = "❌ Geri yükleme başarısız oldu {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Geri yüklendi: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Details:</b> {error_details}\n\nDownload stopped due to critical error.\n\n💡 <b>Tip:</b> If you're getting 401 Unauthorized error, try using <code>/cookie instagram</code> command or send your own cookies to authenticate with Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Porno kara listesindeki alan adı: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Porno anahtar kelimeleri bulundu: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Beyaz listedeki alan adı: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Beyaz liste anahtar kelimeleri bulundu: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Porno anahtar kelimesi bulunamadı"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ {index} dizininde TikTok API hatası, sonraki sese geçiliyor..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ {index} dizininde TikTok API hatası, sonraki videoya geçiliyor..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "User entered a <b>url</b>\n <b>user's name:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>User entered like this:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Kanala Katıl"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 İşleyici kaydediliyor: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - 5 çerezimi indir"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Tarayıcının YT çerezini alır"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Çerez dosyanızı doğrulayın"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Özel çerez yükle"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Kapat"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Kullanılabilir formatlar: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Kapat"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Kapat"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Kapat"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Kapat"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Yardım kapatıldı."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Kapatıldı"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Hata oluştu"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "PATH veya proje dizininde ffmpeg bulunamadı. Lütfen FFmpeg'i yükleyin."
    YTDLP_NOT_FOUND_MSG = "PATH veya proje dizininde yt-dlp binary bulunamadı. Lütfen yt-dlp'yi yükleyin."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Video {rounds} parçaya bölünecek, bu aşırı olabilir"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Video parçası {current}/{total} bölünüyor: {start_time:.2f}s'den {end_time:.2f}s'ye"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Bölünmüş parça {part} oluşturulamadı: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Bölünmüş parça {part} başarıyla oluşturuldu: {target_name} ({size} bayt)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Video parçası {part} bölünürken hata: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Video başarıyla {count} parçaya bölündü"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Video bölme işleminde hata: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Video {video_path} işlenirken hata: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Video dosyası mevcut değil: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Boyutlar '{size_result}' ayrıştırılırken hata: {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "'{size_result}'den video boyutları belirlenemedi, varsayılan kullanılıyor: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Küçük resim oluşturulurken hata: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Video süresi ayrıştırılırken hata: {error}, sonuç: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "{thumb_dir} konumunda küçük resim oluşturulmadı, varsayılan kullanılıyor"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Komut yürütme hatası: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "FFmpeg ile küçük resim oluşturulurken hata: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Dict olmayan yapılandırma bölümü atlanıyor: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "{section}.{key} = {value} ayarlanıyor"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Kullanıcı cookie'leri kullanılıyor: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Kullanıcı {user_id} için YouTube cookie'leri kullanılıyor"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Global cookie dosyası kullanıcı {user_id} klasörüne kopyalandı"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Kopyalanan global cookie'ler kullanıcı cookie'leri olarak kullanılıyor: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Kullanıcı {user_id} için global cookie dosyası kopyalanamadı: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Domain için --no-cookies kullanılıyor: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy istendi ancak yapılandırma içe aktarılamadı/alınamadı: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "gallery-dl için proxy kullanımı zorlanıyor: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy istendi ancak proxy yapılandırması eksik"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Proxy yardımcısı başarısız: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Çıkarıcı öğeleri ayrıştırılıyor..."
    GALLERY_DL_ITEM_COUNT_MSG = "Öğe {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Metadata bulundu (etiket 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL bulundu (etiket 3): {url}, metadata: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Metadata bulundu (eski): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL bulundu (eski): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Dosya adı bulundu: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Bulunan dizin: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Bulunan uzantı: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Ayrıştırılmış {count} öğeler, bilgi: {info}, geri dönüş: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Gallery-dl yapılandırmasını ayarlama: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "A Stratejisi deneniyor: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "Gallery_dl.extractor modülü bulunamadı"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "Gallery_dl.extractor.find() bu yapıda mevcut değil"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "extractor.find({url}) çağrılıyor"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "URL'yle eşleşen çıkarıcı yok"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Çıkarıcıda çerezlerin ayarlanması: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Çıkarıcıda çerezler ayarlanamadı: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Çıkarıcı bulundu, items() çağrılıyor"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Strateji A başarılı oldu, bilgi alındı: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Strateji A: extractor.items() geçerli bilgi döndürmedi"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Strateji A (extractor.find) başarısız: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "--get-urls'den yedek metadata: toplam={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Tüm stratejiler metadata almayı başaramadı"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Görüntü bilgisi çıkarılamadı: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job modülü bulunamadı (bozuk kurulum?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob bu derlemede mevcut değil"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "gallery-dl dizininde indirilen dosyalar aranıyor"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Çıkarıcıdan isimlerle dosyalar bulunmaya çalışılıyor"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Kullanıcı {user_id} için argümanlar okunurken hata: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Video{video_path} işlenirken hata: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Kullanıcı {user_id} send_as_file etkin, belge olarak gönderiliyor"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video tekrar tekrar zaman aşımına uğradı; send_document'e geri dönülüyor"
    SENDER_CAPTION_TOO_LONG_MSG = "Başlık çok uzun, minimal başlıkla deneniyor"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (minimal başlık) zaman aşımına uğradı; send_document'e geri dönülüyor"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Minimal başlıklı video gönderilirken hata: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Tam açıklama dosyası gönderilirken hata: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Geçici açıklama dosyası kaldırılırken hata: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "NO_FILTER_DOMAINS içindeki domain için match_filter atlanıyor: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Kullanıcı {user_id} için format tespiti için kullanıcının URL'sinde mevcut YouTube cookie'leri kontrol ediliyor"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Mevcut YouTube cookie'leri kullanıcı {user_id} için format tespiti için kullanıcının URL'sinde çalışıyor - kullanılıyor"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Mevcut YouTube cookie'leri kullanıcının URL'sinde başarısız oldu, kullanıcı {user_id} için format tespiti için yenilerini almaya çalışılıyor"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Kullanıcı {user_id} için format tespiti için YouTube cookie kaynağı {i} deneniyor"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "Kaynak {i}'den gelen YouTube cookie'leri kullanıcı {user_id} için format tespiti için kullanıcının URL'sinde çalışıyor - kullanıcı klasörüne kaydedildi"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "Kaynak {i}'den gelen YouTube cookie'leri kullanıcı {user_id} için format tespiti için kullanıcının URL'sinde çalışmıyor"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Kullanıcı {user_id} için format tespiti için kaynak {i}'den YouTube cookie'leri indirilemedi"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Kullanıcı {user_id} için format tespiti için tüm YouTube cookie kaynakları başarısız oldu, cookie olmadan denenilecek"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Kullanıcı {user_id} için format tespiti için YouTube cookie kaynağı yapılandırılmadı, cookie olmadan denenilecek"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Kullanıcı {user_id} için format tespiti için YouTube cookie bulunamadı, yenilerini almaya çalışılıyor"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Kullanıcı {user_id} için format tespiti için YouTube cookie'leri kullanılıyor (Always Ask menüsünde zaten doğrulandı)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Kullanıcı {user_id} için format tespiti için YouTube cookie bulunamadı, geri yüklenmeye çalışılıyor..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Format tespiti için global cookie dosyası kullanıcı {user_id} klasörüne kopyalandı"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Kullanıcı {user_id} için global cookie dosyası kopyalanamadı: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "get_video_formats içinde domain için --no-cookies kullanılıyor: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "Uygulama henüz başlatılmadı. {name} erişilemiyor"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Başlık:</b> <code>{caption}</code>\n<b>Kullanıcı id:</b> <code>{user_id}</code>\n<b>Kullanıcı adı:</b> <code>{users_name}</code>\n<b>Video dosya id:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor'da hata: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Caption_editor'da beklenmeyen hata: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 Video URL\'si</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL, konsollarda отсутствует"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin başlatıldı"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken yenilendi"
    DB_LOG_FOR_USER_ADDED_MSG = "Kullanıcı için log eklendi"
    DB_DATABASE_CREATED_MSG = "veritabanı oluşturuldu"
    DB_BOT_STARTED_MSG = "Bot başlatıldı"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY config.py'ye kaydedildi: {hours}sa"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Playlist parçası zaten önbellekte: {path_parts}, atlanıyor"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: herhangi bir URL/kalite varyantı için önbellek bulunamadı, boş dict döndürülüyor"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: büyük aralık için hızlı sayım: {cached_count} önbelleğe alınmış video"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: hash {url_hash}, kalite {quality_key} için önbellek bulunamadı"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: herhangi bir URL varyantı için önbellek bulunamadı, None döndürülüyor"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Erişim reddedildi. Yalnızca yönetici."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Otomatik Firebase önbellek yenileme güncellendi!\n\n📊 Durum: {status}\n⏰ Zamanlama: 00:00'dan itibaren her {interval} saatte bir\n🕒 Sonraki yenileme: {next_exec} ({delta_min} dakika içinde)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Geçersiz argüman. /auto_cache'i kullanın | kapalı | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Aralık 1 ila 168 saat arasında olmalıdır"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Aralık ayarlanamadı"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Auto Firebase cache interval updated!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Auto Firebase cache reloading started!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Otomatik yeniden yükleme ETKİN; sonraki {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Otomatik yeniden yükleme yönetici tarafından DEVRE DIŞI BIRAKILDI."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Otomatik yeniden yükleme aralığı {interval}sa olarak ayarlandı; sonraki {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Otomatik yeniden yükleme başlatıldı; sonraki {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Otomatik yeniden yükleme yönetici tarafından durduruldu."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase önbelleği yüklendi: {count} kök düğümler"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Firebase önbellek dosyası bulunamadı, boş önbellekle başlıyor: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Firebase önbelleği yüklenemedi: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase önbelleği yeniden yüklendi: {count} kök düğümler"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Firebase önbellek dosyası bulunamadı: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Firebase önbelleği yeniden yüklenemedi: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 Bottan yasaklandınız! Yasak kaldırmak için {Config.ADMIN_USERNAME} ile iletişime geçin\n<blockquote>P.S. Kanaldan ayrılmayın - otomatik olarak yasaklanacaksınız ⛔️</blockquote>\n🌍Dili değiştir /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Hiçbir video formatı bulunamadı. Resim indirici deneniyor…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram mesaj göndermeyi sınırladı.\n⏳ Lütfen bekleyin: {time_str}\nZamanlayıcıyı güncellemek için URL'yi tekrar 2 kez gönderin."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Akış URL'sini kopyalamak için düğmeye tıklayın, ardından VLC uygulamasına yapıştırın</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Akış URL'sini kopyalamak için düğmeye tıklayın, ardından VLC uygulamasına yapıştırın</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Bağlantı alınırken hata:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Format dosyası gönderilirken hata oluştu: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Formatlar alınamadı:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Analiz ediliyor... (6 saniye bekleyin)"
    AA_PROCESSING_MSG = "🔎 Analiz ediliyor..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Etiket #{wrong} yasak karakterler içeriyor. Sadece harfler, rakamlar ve _ kullanılabilir.\nLütfen kullanın: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Yönetim kuruluna yeni bir yönetici olarak katıldım. Lütfen, yönetici grubunuzla iletişime geçin."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Merhaba {first_name},\n \n<i>Bu bot🤖 her türlü videoyu doğrudan telegram'a indirebilir.😊 Daha fazla bilgi için <b>/help</b> tuşuna basın</i> 👈\n\n<blockquote>P.S. Olası 🔞NSFW içeriği nedeniyle - ☁️<b>Bulut Depolama</b>, 📁<b>Dosya Paylaşımları</b>, 🔗<b>URL kısaltıcılar</b> ve 🔞<b>Porno sitelerinden</b> indirme ücretlidir! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ @tg_ytdlp kanalını 🗑<b>silme/abonelikten çıkma</b> ve bota 🤖<b>aşırı URL/komut SPAM'i yapma</b> - bot kullanımından otomatik yasaklanırsınız ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Kaldırılacak dosya yok."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 All files removed successfully!\n\nRemoved files:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ ÖNCEKİ İNDİRMENİZ TAMAMLANANA KADAR BEKLEYİN"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "check_user içinde App instance None"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict None, indirmeye izin veriliyor"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict None, altyazı gömülmesine izin veriliyor"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: limitler kontrol ediliyor - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: info_dict anahtarları: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Altyazı gömme atlandı: süre {duration}s limit {max_duration}s'yi aşıyor"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Altyazı gömme atlandı: boyut {size_mb:.2f}MB limit {max_size}MB'yi aşıyor"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Altyazı gömme atlandı: kalite {width}x{height} (min kenar {min_side}p) limit {max_quality}p'yi aşıyor"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "Tiktok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "çalma listesi"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ {service} için aralık limiti aşıldı: {count} (maksimum {max_count}).\n\nMaksimum mevcut dosyaları indirmek için şu komutlardan birini kullanın:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ {service} için aralık limiti aşıldı: {count} (maksimum {max_count})\nKullanıcı ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "PO belirteci sağlayıcısı yapılandırmada devre dışı bırakıldı"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} bir YouTube alanı değil; PO jetonu atlanıyor"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO belirteci sağlayıcısı {base_url} adresinde mevcut değil, standart YouTube çıkarma yöntemine geri dönüyoruz"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO belirteci sağlayıcı önbelleği temizlendi, bir sonraki istekte kullanılabilirlik kontrol edilecek"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "App instance henüz mevcut değil"
    HELPER_USER_NAME_MSG = "Kullanıcı"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood wait tespit edildi, {wait_seconds} saniye bekleniyor"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood wait tespit edildi ancak süre çıkarılamadı, {retry_delay} saniye bekleniyor"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno hatası tespit edildi, {retry_delay} saniye bekleniyor"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy yapılandırması eksik, doğrudan bağlantı kullanılıyor"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Kapat"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Kapat"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Kapat"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Günlük dosyası kaldırıldı."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Etiketler dosyası kaldırıldı."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Format dosyası kaldırıldı."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Bölünmüş dosya kaldırıldı."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Mediainfo dosyası kaldırıldı."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Altyazı ayarları kaldırıldı."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Klavye ayarları kaldırıldı."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Args ayarları kaldırıldı."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 NSFW ayarları kaldırıldı."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Proxy ayarları kaldırıldı."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Flood bekleme ayarları kaldırıldı."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Kapat"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Video İndirme Komutu"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Kullanım: <code>/vid URL'si</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Örnekler:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (direct order)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (reverse order)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Ayrıca bakın: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Kullanıcı {user_id} add_bot_to_group komutunu kapattı"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "YouTube ID çıkarılamadı"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Küçük resim indirilemedi veya çok büyük"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Ses dilini seçin"
    AA_NO_SUBTITLES_DETECTED_MSG = "Altyazı algılanmadı"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Altyazı dilini seçin"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Kimlik Doğrulama Hatası"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Hesap Bulunamadı"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Hesap Kullanılamıyor"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Oran Limiti Aşıldı"
    GALLERY_DL_NETWORK_ERROR_MSG = "Ağ Hatası"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "İçerik Kullanılamıyor"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Coğrafi Kısıtlamalar"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Doğrulama Gerekli"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Politika İhlali"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Bilinmeyen Hata"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ İndirme başlatıldı</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Kapat"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Video İndirme Komutu</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Kullanım: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Örnekler:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Ayrıca bakın: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Flood limiti. Daha sonra deneyin."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Cookie Komutu Kullanımı</b>

<code>/cookie</code> - Cookie menüsünü göster
<code>/cookie youtube</code> - YouTube cookie'lerini indir
<code>/cookie instagram</code> - Instagram cookie'lerini indir
<code>/cookie tiktok</code> - TikTok cookie'lerini indir
<code>/cookie x</code> veya <code>/cookie twitter</code> - Twitter/X cookie'lerini indir
<code>/cookie facebook</code> - Facebook cookie'lerini indir
<code>/cookie custom</code> - Özel cookie talimatlarını göster

<i>Mevcut hizmetler bot yapılandırmasına bağlıdır.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Cookie dosyası kaldırıldı ve önbellek temizlendi."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Önceki"
    SUBS_BACK_BUTTON_MSG = "🔙Geri"
    SUBS_OFF_BUTTON_MSG = "🚫 KAPALI"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - dili ayarla"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - AUTO/TRANS ile dili ayarla"
    SUBS_VALID_OPTIONS_MSG = "Geçerli seçenekler:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 DİL"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Geliştirici GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 GitHub'ı Kontrol Et"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 TEMİZ"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪ÇEREZLER"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MEDYA"
    SETTINGS_INFO_BUTTON_MSG = "📖 BİLGİ"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ DAHA FAZLA"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Sadece cookie'ler"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Loglar "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Etiketler"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Biçim"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Böl"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 MediaInfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Altyazılar"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Klavye"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Argümanlar"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Vekil"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Flood bekleme"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Tüm dosyalar"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - 5 cookie'imi indir"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Tarayıcının YT-cookie'sini al"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Cookie dosyanızı doğrula"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Özel cookie yükle"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Kalite ve formatı değiştir"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - MediaInfo'yu AÇ / KAPAT"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Video parça boyutunu değiştir"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Videoyu ses olarak indir"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Altyazı dil ayarları"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Çalma listelerini nasıl indirilir"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - gallery-dl ile resimleri indir"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - #etiketlerinizi gönder"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Talimatları al"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Loglarınızı gönder"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Çalma listesi yardımı"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - nasıl yapılır"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Doğrudan video bağlantılarını al"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Proxy'yi etkinleştir/devre dışı bırak"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Klavye düzeni"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Satır içi arama yardımcısı"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp argümanları"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - NSFW bulanıklık ayarları"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Temizleme Seçenekleri</b>\n\nNe temizleneceğini seçin:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobil: @vid aramayı etkinleştir"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobil: @vid aramasını etkinleştirin"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 KAPALI"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 TAM"
    KEYBOARD_1X3_BUTTON_MSG = "📱1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[Resimlerin URL'si]({url})"
    IMAGE_ERROR_MSG = "❌ Hata: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Geri"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - özel format"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p kalite"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K kalite"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K kalite"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - belirli format ID"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - her zaman menüyü göster"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/en iyi kalite"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Her Zaman Sor (menü + düğmeler)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Diğerleri (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (PC/Mac Telegram için en iyi)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (mobil Telegram için en iyi)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (MAKS kalite)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Özel (kendiniz girin)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Tarayıcıdan"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷İnstagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Kendi"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Girdi modu hareketsizlik nedeniyle otomatik olarak kapatıldı (5 dakika)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Tümünü Sıfırla"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Mevcutu Görüntüle"
    ARGS_BACK_BUTTON_MSG = "🔙 Geri"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Bu ayarları şablon olarak kaydetmek için bu mesajı favorilerinize iletin.</i> \n\n<i>Bu ayarları uygulamak için bu mesajı buraya geri iletin.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Mevcut yt-dlp Argümanları:\n\nÖzel ayar yapılandırılmamış.\n\n---\n\n<i>Bu ayarları şablon olarak kaydetmek için bu mesajı favorilerinize iletin.</i> \n\n<i>Bu ayarları uygulamak için bu mesajı buraya geri iletin.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Mevcut yt-dlp Argümanları:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Ayarları Dışa Aktar"
    ARGS_SETTINGS_READY_MSG = "Ayarlar dışa aktarım için hazır! Kaydetmek için bu mesajı favorilerinize iletin."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Mevcut yt-dlp Argümanları:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Mesajdaki ayarlar tanınamadı. Doğru bir ayar şablonu gönderdiğinizden emin olun."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Ayarlar başarıyla içe aktarıldı!\n\nUygulanan parametreler: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Ana ayarlar:\n"
    ARGS_ERROR_SAVING_MSG = "❌ İçe aktarılan ayarlar kaydedilirken hata oluştu."
    ARGS_ERROR_IMPORTING_MSG = "❌ Ayarlar içe aktarılırken bir hata oluştu."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Cookie Dosyalarını İndir</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Cookie dosyasını indirmek için bir hizmet seçin."
    COOKIE_MENU_SAVE_INFO_MSG = "Cookie dosyaları klasörünüzde cookie.txt olarak kaydedilecektir."
    COOKIE_MENU_TIP_HEADER_MSG = "İpucu: Doğrudan komutu da kullanabilirsiniz:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – cookie'leri indir ve doğrula"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – indekse göre belirli bir kaynak kullan (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Ardından <code>/check_cookie</code> ile doğrulayın (RickRoll'de test eder)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Her Zaman Sor"
    SUBS_AUTO_TRANS_BUTTON_MSG = "OTOMATİK/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Bağlantı"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁İzle"  # GEÇİCİ OLARAK DEVRE DIŞI: poketube hizmeti kapalı
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Açıklama"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ KES"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Video Kesme</b>\n\nVideo süresi: <b>{start_time} - {end_time}</b>\n\nLütfen istenen zaman aralığını formatında gönderin:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nÖrnek: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Geçersiz format. Lütfen kullanın: <code>HH:MM:SS-HH:MM:SS</code>\n\nÖrnek: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Geçersiz aralık. Başlangıç zamanı bitiş zamanından küçük olmalıdır."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ Zaman aralığı video sınırlarının dışında.\n\nVideo süresi: <b>{start_time} - {end_time}</b>\n\nAralığınız bu sınırlar içinde olmalıdır."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>Video kırpılacak:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Kısmen tamamlandı - {successful_uploads}/{total_files} ses dosyası yüklendi."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Ses başarıyla indirildi ve gönderildi - {total_files} dosya yüklendi."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Özel TikTok Hesabı</b>\n\n"
        "Bu TikTok hesabı özeldir veya tüm videolar özeldir.\n\n"
        "<b>💡 Çözüm:</b>\n"
        "1. @{username} hesabını takip edin\n"
        "2. <code>/cookie</code> komutunu kullanarak cookie'lerinizi bot'a gönderin\n"
        "3. Tekrar deneyin\n\n"
        "<b>Cookie'leri güncelledikten sonra tekrar deneyin!</b>"
    )

    #######################################################
