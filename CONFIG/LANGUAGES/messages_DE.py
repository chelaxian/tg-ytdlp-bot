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
    CREDITS_MSG = "<blockquote><i>Verwaltet von</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Sprache ändern: /lang</b>"
    TO_USE_MSG = "<i>Um diesen Bot zu verwenden, müssen Sie dem Telegram-Kanal @tg_ytdlp beitreten.</i>\nNachdem Sie dem Kanal beigetreten sind, <b>senden Sie Ihren Video-Link erneut und der Bot wird ihn für Sie herunterladen</b> ❤️\n\n<blockquote>P.S. Das Herunterladen von 🔞NSFW-Inhalten und Dateien von ☁️Cloud Storage ist kostenpflichtig! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Verlassen Sie den Kanal nicht - Sie werden vom Bot-Nutzung gesperrt ⛔️</blockquote>"

    ERROR1 = "URL-Link nicht gefunden. Bitte geben Sie eine URL mit <b>https://</b> oder <b>http://</b> ein"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Wiedergabelisten (yt-dlp)</b>

Um Wiedergabelisten herunterzuladen, senden Sie die URL mit <code>*start*end</code> Bereichen am Ende. Zum Beispiel: <code>URL*1*5</code> (erste 5 Videos von 1 bis 5 einschließlich).<code>URL*-1*-5</code> (letzte 5 Videos von 1 bis 5 einschließlich).
Oder Sie können <code>/vid VON-BIS URL</code> verwenden. Zum Beispiel: <code>/vid 3-7 URL</code> (lädt Videos von 3 bis 7 einschließlich vom Anfang herunter). <code>/vid -3-7 URL</code> (lädt Videos von 3 bis 7 einschließlich vom Ende herunter). Funktioniert auch für den Befehl <code>/audio</code>.

<b>Beispiele:</b>

🟥 <b>Videobereich aus YouTube-Wiedergabeliste:</b> (benötigt 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(lädt die ersten 5 Videos von 1 bis 5 einschließlich herunter)
🟥 <b>Einzelnes Video aus YouTube-Wiedergabeliste:</b> (benötigt 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(lädt nur das 3. Video herunter)

⬛️ <b>TikTok-Profil:</b> (benötigt Ihr 🍪)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(lädt die ersten 10 Videos aus dem Benutzerprofil herunter)

🟪 <b>Instagram-Stories:</b> (benötigt Ihr 🍪)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(lädt die ersten 3 Stories herunter)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(lädt die ersten 10 Stories aus dem Album herunter)

🟦 <b>VK-Videos:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(lädt die ersten 3 Videos aus dem Benutzer-/Gruppenprofil herunter)

⬛️<b>Rutube-Kanäle:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(lädt Videos von 2 bis 4 einschließlich aus dem Kanal herunter)

🟪 <b>Twitch-Clips:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(lädt die ersten 3 Clips aus dem Kanal herunter)

🟦 <b>Vimeo-Gruppen:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(lädt die ersten 2 Videos aus der Gruppe herunter)

🟧 <b>Pornhub-Modelle:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(lädt die ersten 2 Videos aus dem Modellprofil herunter)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(lädt die ersten 3 Videos aus den Suchergebnissen nach Ihrem Prompt herunter)

und so weiter...
siehe <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">Liste der unterstützten Seiten</a>
</blockquote>

<blockquote expandable>🖼 <b>Bilder (gallery-dl)</b>

Verwenden Sie <code>/img URL</code>, um Bilder/Fotos/Alben von vielen Plattformen herunterzuladen.

<b>Beispiele:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Bereiche:</b>
<code>/img 11-20 https://example.com/album</code> — Elemente 11..20
<code>/img 11- https://example.com/album</code> — von 11 bis zum Ende (oder Bot-Limit)

<i>Unterstützte Plattformen umfassen vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor usw. Vollständige Liste:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">von gallery-dl unterstützte Seiten</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Video-Download-Bot - Hilfe</b>

📥 <b>Grundlegende Verwendung:</b>
• Senden Sie einen beliebigen Link → Bot lädt ihn herunter
  <i>der Bot versucht automatisch, Videos über yt-dlp und Bilder über gallery-dl herunterzuladen.</i>
• <b>Mehrere URLs:</b> Im Qualitätsauswahlmodus (<code>/format</code>) können Sie bis zu <b>10 URLs</b> in einer Nachricht senden. Jede URL in einer neuen Zeile oder durch Leerzeichen getrennt.
• <code>/audio URL</code> → Audio extrahieren
• <code>/link [Qualität] URL</code> → direkte Links erhalten
• <code>/proxy</code> → Proxy für alle Downloads aktivieren/deaktivieren
• Antworten Sie auf Video mit Text → Beschriftung ändern

📋 <b>Wiedergabelisten & Bereiche:</b>
• <code>URL*1*5</code> → erste 5 Videos herunterladen
• <code>URL*-1*-5</code> → letzte 5 Videos herunterladen
• <code>/vid 3-7 URL</code> → wird zu <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → wird zu <code>URL*-3*-7</code>

🍪 <b>Cookies & Privat:</b>
• Laden Sie *.txt Cookie für private Videos hoch
• <code>/cookie [Service]</code> → Cookies herunterladen (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → Quelle nach Index auswählen (1–N)
• <code>/cookies_from_browser</code> → aus Browser extrahieren
• <code>/check_cookie</code> → Cookie überprüfen
• <code>/save_as_cookie</code> → Text als Cookie speichern

🧹 <b>Bereinigung:</b>
• <code>/clean</code> → nur Mediendateien
• <code>/clean all</code> → alles
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Einstellungen:</b>
• <code>/settings</code> → Einstellungsmenü
• <code>/format</code> → Qualität & Format
• <code>/split</code> → Video in Teile aufteilen
• <code>/mediainfo on/off</code> → Medieninfo
• <code>/nsfw on/off</code> → NSFW-Unschärfe
• <code>/tags</code> → gespeicherte Tags anzeigen
• <code>/sub on/off</code> → Untertitel
• <code>/keyboard</code> → Tastatur (OFF/1x3/2x3)

🏷️ <b>Tags:</b>
• <code>#tag1#tag2</code> nach URL hinzufügen
• Tags erscheinen in Beschriftungen
• <code>/tags</code> → alle Tags anzeigen

🔗 <b>Direkte Links:</b>
• <code>/link URL</code> → beste Qualität
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → spezifische Qualität

⚙️ <b>Schnellbefehle:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → Qualität setzen
• <code>/keyboard off/1x3/2x3/full</code> → Tastaturlayout
• <code>/split 100mb-2000mb</code> → Teilgröße ändern
• <code>/subs off/ru/en auto</code> → Untertitelsprache
• <code>/list URL</code> → Liste verfügbarer Formate
• <code>/mediainfo on/off</code> → Medieninfo ein/aus
• <code>/proxy on/off</code> → Proxy für alle Downloads aktivieren/deaktivieren

📊 <b>Info:</b>
• <code>/usage</code> → Download-Verlauf
• <code>/search</code> → Inline-Suche über @vid

🖼 <b>Bilder:</b>
• <code>URL</code> → Bild-URLs herunterladen
• <code>/img URL</code> → Bilder von URL herunterladen
• <code>/img 11-20 URL</code> → spezifischen Bereich herunterladen
• <code>/img 11- URL</code> → von 11. bis zum Ende herunterladen

👨‍💻 <i>Developer:</i> @upekshaip
🤝 <i>Contributor:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Speichern Sie einfach Ihr Cookie als <b><u>cookie.txt</u></b> und senden Sie es dem Bot als Dokument.\n\n"
        "Sie können Cookies auch als Klartext mit dem Befehl <b><u>/save_as_cookie</u></b> senden.\n"
        "<b>Verwendung von <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>Anweisungen:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>Videosuche</b>

Drücken Sie die Schaltfläche unten, um die Inline-Suche über @vid zu aktivieren.

<blockquote>Auf dem PC geben Sie einfach <b>"@vid Ihre_Suchanfrage"</b> in einem beliebigen Chat ein.</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Bild-Download-Befehl</b>\n\n"
        "Verwendung: <code>/img URL</code>\n\n"
        "<b>Beispiele:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Unterstützte Plattformen (Beispiele):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, etc. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">vollständige Liste</a></blockquote>"
        "Siehe auch: "
    )
    
    LINK_HINT_MSG = (
        "Erhalten Sie direkte Video-Links mit Qualitätsauswahl.\n\n"
        "Verwendung: /link + URL \n\n"
        "(z.B. /link https://youtu.be/abc123)\n"
        "(z.B. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Bot zu Gruppe hinzufügen</b>

Fügen Sie meine Bots zu Ihren Gruppen hinzu, um erweiterte Funktionen und höhere Limits zu erhalten!
————————————
📊 <b>Aktuelle KOSTENLOSE Limits (in Bot's DM):</b>
<blockquote>•🗑 Unordentlicher Müll von allen unsortierten Dateien 👎
• Max. 1 Dateigröße: <b>8 GB </b>
• Max. 1 Dateiqualität: <b>UNLIM</b>
• Max. 1 Dateidauer: <b>UNLIM</b>
• Max. Anzahl Downloads: <b>UNLIM</b>
• Max. URLs in einer Nachricht: <b>10</b> (nur im Qualitätsauswahlmodus)
• Max. Wiedergabelisten-Items pro 1 Mal: <b>50</b>
• Max. TikTok-Videos pro 1 Mal: <b>500</b>
• Max. Bilder pro 1 Mal: <b>1000</b>
• URL-Ratenlimits: <b>5/min, 60/Stunde, 1000/Tag</b>
• Befehlslimit: <b>20/min</b>
• 1 Download max. Zeit: <b>2 Stunden</b>
• 🔞 NSFW-Inhalt ist kostenpflichtig! 1⭐️ = $0.02
• 🆓 ALLE ANDEREN MEDIEN SIND VOLLSTÄNDIG KOSTENLOS
• 📝 Alle Inhalts-Logs & Caching zu meinen Log-Kanälen für sofortiges Repost beim erneuten Herunterladen</blockquote>

💬<b>Diese Limits nur für Video mit Untertiteln:</b>
<blockquote>• Max. Video+Untertitel-Dauer: <b>1.5 Stunden</b>
• Max. Video+Untertitel-Dateigröße: <b>500 MB</b>
• Max. Video+Untertitel-Qualität: <b>720p</b></blockquote>
————————————
🚀 <b>Bezahlte Gruppen-Vorteile (2️⃣x Limits):</b>
<blockquote>•  🗂 Strukturiertes, ordentliches Medienarchiv nach Themen sortiert 👍
•  📁 Bots antworten im Thema, in dem Sie sie aufrufen
•  📌 Automatisches Anheften von Statusnachrichten mit Download-Fortschritt
•  🖼 /img-Befehl lädt Medien als 10-Item-Alben herunter
• Max. 1 Dateigröße: <b>16 GB</b> ⬆️
• Max. URLs in einer Nachricht: <b>20</b> ⬆️ (nur im Qualitätsauswahlmodus)
• Max. Wiedergabelisten-Items pro 1 Mal: <b>100</b> ⬆️
• Max. TikTok-Videos pro 1 Mal: 1000 ⬆️
• Max. Bilder pro 1 Mal: 2000 ⬆️
• URL-Ratenlimits: <b>10/min, 120/Stunde, 2000/Tag</b> ⬆️
• Befehlslimit: <b>40/min</b> ⬆️
• 1 Download max. Zeit: <b>4 Stunden</b> ⬆️
• 🔞 NSFW-Inhalt: Kostenlos mit vollständigen Metadaten 🆓
• 📢 Keine Notwendigkeit, meinem Kanal für Gruppen beizutreten
• 👥 Alle Gruppenmitglieder haben Zugang zu bezahlten Funktionen!
• 🗒 Keine Logs / kein Cache zu meinen Log-Kanälen! Sie können Kopie/Repost in Gruppeneinstellungen ablehnen</blockquote>

💬 <b>2️⃣x Limits für Video mit Untertiteln:</b>
<blockquote>• Max. Video+Untertitel-Dauer: <b>3 Stunden</b> ⬆️
• Max. Video+Untertitel-Dateigröße: <b>1000 MB</b> ⬆️
• Max. Video+Untertitel-Qualität: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Preise & Einrichtung:</b>
<blockquote>• Preis: <b>$5/Monat</b> pro 1 Bot in Gruppe
• Einrichtung: Kontaktieren Sie @iilililiiillliiliililliilliliiil
• Zahlung: 💎TON oder andere Methoden💲
• Support: Vollständiger technischer Support inklusive</blockquote>
————————————
Sie können meine Bots zu Ihrer Gruppe hinzufügen, um kostenloses 🔞<b>NSFW</b> freizuschalten und alle Limits zu verdoppeln (x2️⃣).
Kontaktieren Sie mich, wenn Sie möchten, dass ich Ihrer Gruppe erlaube, meine Bots zu verwenden @iilililiiillliiliililliilliliiil
————————————
💡<b>TIPP:</b> <blockquote>Sie können Geld mit beliebig vielen Ihrer Freunde zusammenlegen (z.B. 100 Personen) und 1 Kauf für die ganze Gruppe tätigen - ALLE GRUPPENMITGLIEDER HABEN VOLLSTÄNDIGEN UNLIMITIERTEN ZUGANG zu allen Bot-Funktionen in dieser Gruppe für nur <b>0.05$</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW-Modus: EIN✅</b>

• NSFW-Inhalt wird ohne Unschärfe angezeigt.
• Spoiler gelten nicht für NSFW-Medien.
• Der Inhalt ist sofort sichtbar

<i>Verwenden Sie /nsfw off, um Unschärfe zu aktivieren</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW-Modus: AUS</b>

⚠️ <b>Unschärfe aktiviert</b>
• NSFW-Inhalt wird unter Spoiler verborgen   
• Zum Anzeigen müssen Sie auf das Medium klicken
• Spoiler gelten für NSFW-Medien.

<i>Verwenden Sie /nsfw on, um Unschärfe zu deaktivieren</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Ungültiger Parameter</b>

Verwenden Sie:
• <code>/nsfw on</code> - Unschärfe deaktivieren
• <code>/nsfw off</code> - Unschärfe aktivieren
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Cache wird überprüft...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Verarbeitung läuft..."
    DOWNLOADING_MSG = "📥 <b>Medien werden heruntergeladen...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Bild wird heruntergeladen...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Download abgeschlossen</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Heruntergeladen:"
    SENT_STATUS_MSG = "Gesendet:"
    PENDING_TO_SEND_STATUS_MSG = "Ausstehend zum Senden:"
    TITLE_LABEL_MSG = "Titel:"
    MEDIA_COUNT_LABEL_MSG = "Medienanzahl:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Download abgeschlossen, Audio wird verarbeitet..."
    VIDEO_PROCESSING_MSG = "📽 Video wird verarbeitet..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Aus Cache gesendet</b>\n\nGesendete Alben: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Video erfolgreich aus Cache gesendet."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Wiedergabelisten-Videos aus Cache gesendet ({cached}/{total} Dateien)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} Videos aus Cache gesendet, fehlende werden heruntergeladen..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Aus Cache gesendet: {cached}\n🔄 Download wird fortgesetzt..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Medien konnten nicht analysiert werden, fortfahren mit maximal erlaubtem Bereich (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Medienanzahl konnte nicht bestimmt werden, fortfahren mit maximal erlaubtem Bereich (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Gesamte Medienanzahl konnte nicht bestimmt werden, fortfahren mit angegebenem Bereich {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>Ungültige URL</b>\n\nBitte geben Sie eine gültige URL ein, die mit http:// oder https:// beginnt"

    ERROR_OCCURRED_MSG = "❌ <b>Fehler aufgetreten</b>\n\n<code>{url}</code>\n\nFehler: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Fehler beim Senden des Videos: {error}"
    ERROR_UNKNOWN_MSG = "❌ Unbekannter Fehler: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Nicht genug Speicherplatz zum Herunterladen von Videos."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Die Dateigröße überschreitet das Limit von {limit} GB. Bitte wählen Sie eine kleinere Datei innerhalb der erlaubten Größe."

    ERROR_GETTING_LINK_MSG = "❌ <b>Fehler beim Abrufen des Links:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram hat das Senden von Nachrichten eingeschränkt.\n⏳ Bitte warten Sie: {time}\nUm den Timer zu aktualisieren, senden Sie die URL erneut 2 Mal."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram hat das Senden von Nachrichten eingeschränkt.\n⏳ Bitte warten Sie: \nUm den Timer zu aktualisieren, senden Sie die URL erneut 2 Mal."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Untertitel konnten nicht heruntergeladen werden"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Direkte Stream-Links</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Titel:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Dauer:</b> {duration} Sek\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Fehler: Ursprüngliche Nachricht nicht gefunden."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{tag} enthält verbotene Zeichen. Nur Buchstaben, Ziffern und _ sind erlaubt.\nBitte verwenden Sie: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Wiedergabelisten-Videos gesendet: {sent}/{total} Dateien."
    PLAYLIST_CACHE_SENT_MSG = "✅ Aus Cache gesendet: {cached}/{total} Dateien."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Stream-Links konnten nicht abgerufen werden"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Wählen Sie einen Browser aus, von dem Cookies heruntergeladen werden sollen:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Keine Browser auf diesem System gefunden. Sie können Cookies von einer Remote-URL herunterladen oder den Browser-Status überwachen:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Browser öffnen</b> - um Browser-Status in Mini-App zu überwachen"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Browser öffnen"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Von Remote-URL herunterladen"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube-Cookie-Datei über Fallback heruntergeladen und als cookie.txt gespeichert"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Keine unterstützten Browser gefunden und keine COOKIE_URL konfiguriert. Verwenden Sie /cookie oder laden Sie cookie.txt hoch."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL muss auf eine .txt-Datei zeigen."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fallback-Cookie-Datei ist zu groß (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fallback-Cookie-Quelle nicht verfügbar (Status {status}). Versuchen Sie /cookie oder laden Sie cookie.txt hoch."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Fehler beim Herunterladen des Fallback-Cookies. Versuchen Sie /cookie oder laden Sie cookie.txt hoch."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Unerwarteter Fehler beim Herunterladen des Fallback-Cookies."
    BTN_CLOSE = "🔚Schließen"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Ungültiger Boolean-Wert"
    ARGS_CLOSED_MSG = "Geschlossen"
    ARGS_ALL_RESET_MSG = "✅ Alle Argumente zurückgesetzt"
    ARGS_RESET_ERROR_MSG = "❌ Fehler beim Zurücksetzen der Argumente"
    ARGS_INVALID_PARAM_MSG = "❌ Ungültiger Parameter"
    ARGS_BOOL_SET_MSG = "Auf {value} gesetzt"
    ARGS_BOOL_ALREADY_SET_MSG = "Bereits auf {value} gesetzt"
    ARGS_INVALID_SELECT_MSG = "❌ Ungültiger Auswahlwert"
    ARGS_VALUE_SET_MSG = "Auf {value} gesetzt"
    ARGS_VALUE_ALREADY_SET_MSG = "Bereits auf {value} gesetzt"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Aktueller Wert:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Beispiele:</b>\n• <code>default</code> - Standard-XFF-Strategie verwenden\n• <code>never</code> - XFF-Header niemals verwenden\n• <code>US</code> - Ländercode Vereinigte Staaten\n• <code>GB</code> - Ländercode Vereinigtes Königreich\n• <code>DE</code> - Ländercode Deutschland\n• <code>FR</code> - Ländercode Frankreich\n• <code>JP</code> - Ländercode Japan\n• <code>192.168.1.0/24</code> - IP-Block (CIDR)\n• <code>10.0.0.0/8</code> - Private IP-Bereich\n• <code>203.0.113.0/24</code> - Öffentlicher IP-Block\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Hinweis:</b> Dies ersetzt --geo-bypass-Optionen. Verwenden Sie einen beliebigen 2-Buchstaben-Ländercode oder IP-Block in CIDR-Notation.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Beispiel:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Bitte senden Sie Ihren neuen Wert."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Bereich:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Bitte senden Sie eine Zahl."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Beispiele:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Hinweis:</b> Diese Header werden zu den vorhandenen Referer- und User-Agent-Headern hinzugefügt.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Aktuelle yt-dlp-Argumente:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - True/False-Schalter\n• 📋 <b>Auswahl</b> - Aus Optionen wählen\n• 🔢 <b>Numerisch</b> - Zahleneingabe\n• 📝🔧 <b>Text</b> - Text/JSON-Eingabe</blockquote>\n\nDiese Einstellungen werden auf alle Ihre Downloads angewendet."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "IPv6-Verbindungen erzwingen",
        "force_ipv4": "IPv4-Verbindungen erzwingen", 
        "no_live_from_start": "Live-Streams nicht von Anfang herunterladen",
        "live_from_start": "Live-Streams von Anfang herunterladen",
        "no_check_certificates": "HTTPS-Zertifikatsvalidierung unterdrücken",
        "check_certificate": "SSL-Zertifikat überprüfen",
        "no_playlist": "Nur einzelnes Video herunterladen, nicht Wiedergabeliste",
        "embed_metadata": "Metadaten in Videodatei einbetten",
        "embed_thumbnail": "Miniaturansicht in Videodatei einbetten",
        "write_thumbnail": "Miniaturansicht in Datei schreiben",
        "ignore_errors": "Download-Fehler ignorieren und fortfahren",
        "legacy_server_connect": "Legacy-Server-Verbindungen erlauben",
        "concurrent_fragments": "Anzahl gleichzeitiger zu downloadender Fragmente",
        "xff": "X-Forwarded-For-Header-Strategie",
        "user_agent": "User-Agent-Header",
        "impersonate": "Browser-Impersonation",
        "referer": "Referer-Header",
        "geo_bypass": "Geografische Beschränkungen umgehen",
        "hls_use_mpegts": "MPEG-TS für HLS verwenden",
        "no_part": ".part-Dateien nicht verwenden",
        "no_continue": "Teilweise Downloads nicht fortsetzen",
        "audio_format": "Audioformat",
        "video_format": "Videoformat",
        "merge_output_format": "Ausgabeformat für Zusammenführung",
        "send_as_file": "Als Datei senden",
        "username": "Benutzername",
        "password": "Passwort",
        "twofactor": "Zwei-Faktor-Authentifizierungscode",
        "min_filesize": "Mindestdateigröße (MB)",
        "max_filesize": "Maximaldateigröße (MB)",
        "playlist_items": "Wiedergabelisten-Items",
        "date": "Datum",
        "datebefore": "Datum vor",
        "dateafter": "Datum nach",
        "http_headers": "HTTP-Header",
        "sleep_interval": "Warteintervall",
        "max_sleep_interval": "Maximales Warteintervall",
        "retries": "Anzahl Wiederholungen",
        "http_chunk_size": "HTTP-Chunk-Größe",
        "sleep_subtitles": "Wartezeit für Untertitel"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp-Argumente-Konfiguration</b>\n\n<blockquote>📋 <b>Gruppen:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp-Argumente-Konfiguration</b>\n\n"
        "<blockquote>📋 <b>Gruppen:</b>\n"
        "• ✅/❌ <b>Boolean</b> - True/False-Schalter\n"
        "• 📋 <b>Auswahl</b> - Aus Optionen wählen\n"
        "• 🔢 <b>Numerisch</b> - Zahleneingabe\n"
        "• 📝🔧 <b>Text</b> - Text/JSON-Eingabe</blockquote>\n\n"
        "Diese Einstellungen werden auf alle Ihre Downloads angewendet."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Bitte warten..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Fehler aufgetreten"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Eingabemodus wurde automatisch aufgrund von Inaktivität geschlossen (5 Minuten)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Eingabe enthält potenziell gefährliche Inhalte: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Eingabe zu lang (max. 1000 Zeichen)"
    ARGS_INVALID_URL_MSG = "❌ Ungültiges URL-Format. Muss mit http:// oder https:// beginnen"
    ARGS_INVALID_JSON_MSG = "❌ Ungültiges JSON-Format"
    ARGS_NUMBER_RANGE_MSG = "❌ Zahl muss zwischen {min_val} und {max_val} liegen"
    ARGS_INVALID_NUMBER_MSG = "❌ Ungültiges Zahlenformat"
    ARGS_DATE_FORMAT_MSG = "❌ Datum muss im Format YYYYMMDD sein (z.B. 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Jahr muss zwischen 1900 und 2100 liegen"
    ARGS_MONTH_RANGE_MSG = "❌ Monat muss zwischen 01 und 12 liegen"
    ARGS_DAY_RANGE_MSG = "❌ Tag muss zwischen 01 und 31 liegen"
    ARGS_INVALID_DATE_MSG = "❌ Ungültiges Datumsformat"
    ARGS_INVALID_XFF_MSG = "❌ XFF muss 'default', 'never', Ländercode (z.B. US) oder IP-Block (z.B. 192.168.1.0/24) sein"
    ARGS_NO_CUSTOM_MSG = "Keine benutzerdefinierten Argumente gesetzt. Alle Parameter verwenden Standardwerte."
    ARGS_RESET_SUCCESS_MSG = "✅ Alle Argumente auf Standardwerte zurückgesetzt."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Text zu lang. Maximum 500 Zeichen."
    ARGS_ERROR_PROCESSING_MSG = "❌ Fehler bei der Verarbeitung der Eingabe. Bitte versuchen Sie es erneut."
    ARGS_BOOL_INPUT_MSG = "❌ Bitte geben Sie 'True' oder 'False' für die Option Als Datei senden ein."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Bitte geben Sie eine gültige Zahl ein."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Bitte senden Sie <code>True</code> oder <code>False</code>, um diese Option zu aktivieren/deaktivieren."
    ARGS_JSON_VALUE_REQUEST_MSG = "Bitte senden Sie gültiges JSON."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Sie haben noch keine Tags."
    TAGS_MESSAGE_CLOSED_MSG = "Tags-Nachricht geschlossen."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Untertitel deaktiviert und Immer Fragen-Modus ausgeschaltet."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ UNTERTITEL Immer Fragen aktiviert."
    SUBS_LANGUAGE_SET_MSG = "✅ Untertitelsprache gesetzt auf: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️WARNUNG: Aufgrund hoher CPU-Belastung ist diese Funktion sehr langsam (nahezu Echtzeit) und begrenzt auf:\n"
        "- Max. Qualität 720p\n"
        "- Max. Dauer 1.5 Stunden\n"
        "- Max. Videogröße 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Schnellbefehle:</b>\n"
        "• <code>/subs off</code> - Untertitel deaktivieren\n"
        "• <code>/subs on</code> - Immer Fragen-Modus aktivieren\n"
        "• <code>/subs ru</code> - Sprache setzen\n"
        "• <code>/subs ru auto</code> - Sprache mit AUTO/TRANS setzen"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Untertitel sind deaktiviert"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Ausgewählte Sprache: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Untertitel werden heruntergeladen..."
    SUBS_DISABLED_ERROR_MSG = "❌ Untertitel sind deaktiviert. Verwenden Sie /subs zum Konfigurieren."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Untertitel-Download wird nur für YouTube unterstützt."
    SUBS_CAPTION_MSG = (
        "<b>💬 Untertitel</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Sprache:</b> {lang}\n"
        "<b>Typ:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Untertitel-SRT-Datei an Benutzer gesendet."
    SUBS_ERROR_PROCESSING_MSG = "❌ Fehler beim Verarbeiten der Untertiteldatei."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Untertitel konnten nicht heruntergeladen werden."
    SUBS_ERROR_MSG = "❌ Fehler beim Herunterladen der Untertitel: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Teilgröße für Aufteilung gesetzt auf: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **Ungültige Größe!**\n\n"
        "**Gültiger Bereich:** 100MB bis 2GB\n\n"
        "**Gültige Formate:**\n"
        "• `100mb` bis `2000mb` (Megabyte)\n"
        "• `0.1gb` bis `2gb` (Gigabyte)\n\n"
        "**Beispiele:**\n"
        "• `/split 100mb` - 100 Megabyte\n"
        "• `/split 500mb` - 500 Megabyte\n"
        "• `/split 1.5gb` - 1.5 Gigabyte\n"
        "• `/split 2gb` - 2 Gigabyte\n"
        "• `/split 2000mb` - 2000 Megabyte (2GB)\n\n"
        "**Voreinstellungen:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Maximale Teilgröße für Video-Aufteilung wählen:**\n\n"
        "**Bereich:** 100MB bis 2GB\n\n"
        "**Schnellbefehle:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Beispiele:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Menü geschlossen."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Bot-Einstellungen</b>\n\nKategorie wählen:"
    SETTINGS_MENU_CLOSED_MSG = "Menü geschlossen."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Bereinigungsoptionen</b>\n\nWählen Sie, was bereinigt werden soll:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nAktion wählen:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIEN</b>\n\nAktion wählen:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nAktion wählen:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ WEITERE BEFEHLE</b>\n\nAktion wählen:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Befehl ausgeführt."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Flood-Limit. Versuchen Sie es später erneut."
    SETTINGS_HINT_SENT_MSG = "Hinweis gesendet."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Suchassistent geöffnet."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Unbekannter Befehl."
    SETTINGS_HINT_CLOSED_MSG = "Hinweis geschlossen."
    SETTINGS_HELP_SENT_MSG = "Hilfetext an Benutzer gesendet"
    SETTINGS_MENU_OPENED_MSG = "/settings-Menü geöffnet"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Suchassistent geschlossen"
    SEARCH_CLOSED_MSG = "Geschlossen"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proxy {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Fehler beim Speichern der Proxy-Einstellungen."
    PROXY_MENU_TEXT_MSG = "Proxy-Server für alle yt-dlp-Operationen aktivieren oder deaktivieren?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Proxy-Server ({count} verfügbar) für alle yt-dlp-Operationen aktivieren oder deaktivieren?\n\nWenn aktiviert, werden Proxies mit der Methode {method} ausgewählt."
    PROXY_MENU_CLOSED_MSG = "Menü geschlossen."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy aktiviert. Alle yt-dlp-Operationen verwenden den Proxy."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy aktiviert. Alle yt-dlp-Operationen verwenden {count} Proxy-Server mit {method} Auswahlmethode."
    PROXY_DISABLED_MSG = "❌ Proxy deaktiviert."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Fehler beim Speichern der Proxy-Einstellungen."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy aktiviert."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy deaktiviert."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ WARTEN SIE, BIS IHR VORHERIGER DOWNLOAD ABGESCHLOSSEN IST"
    AUDIO_HELP_MSG = (
        "<b>🎧 Audio-Download-Befehl</b>\n\n"
        "Verwendung: <code>/audio URL</code>\n\n"
        "<b>Beispiele:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Siehe auch: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Audio-Hinweis geschlossen."
    PLAYLIST_HELP_CLOSED_MSG = "Wiedergabelisten-Hilfe geschlossen."
    USERLOGS_CLOSED_MSG = "Logs-Nachricht geschlossen."
    HELP_CLOSED_MSG = "Hilfe geschlossen."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW-Unschärfe-Einstellungen</b>\n\nNSFW-Inhalt ist <b>{status}</b>.\n\nWählen Sie, ob NSFW-Inhalt unscharf gemacht werden soll:"
    NSFW_MENU_CLOSED_MSG = "Menü geschlossen."
    NSFW_BLUR_DISABLED_MSG = "NSFW-Unschärfe deaktiviert."
    NSFW_BLUR_ENABLED_MSG = "NSFW-Unschärfe aktiviert."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW-Unschärfe deaktiviert."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW-Unschärfe aktiviert."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "MediaInfo für heruntergeladene Dateien senden aktivieren oder deaktivieren?"
    MEDIAINFO_MENU_CLOSED_MSG = "Menü geschlossen."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo aktiviert. Nach dem Herunterladen werden Dateiinformationen gesendet."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo deaktiviert."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo aktiviert."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo deaktiviert."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Verfügbare Formate auflisten</b>\n\n"
        "Verfügbare Video/Audio-Formate für eine URL abrufen.\n\n"
        "<b>Verwendung:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Beispiele:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 So verwenden Sie Format-IDs:</b>\n"
        "Nach dem Abrufen der Liste verwenden Sie eine spezifische Format-ID:\n"
        "• <code>/format id 401</code> - Format 401 herunterladen\n"
        "• <code>/format id401</code> - dasselbe wie oben\n"
        "• <code>/format id140 audio</code> - Format 140 als MP3-Audio herunterladen\n\n"
        "Dieser Befehl zeigt alle verfügbaren Formate an, die heruntergeladen werden können."
    )
    LIST_PROCESSING_MSG = "🔄 Verfügbare Formate werden abgerufen..."
    LIST_INVALID_URL_MSG = "❌ Bitte geben Sie eine gültige URL ein, die mit http:// oder https:// beginnt"
    LIST_CAPTION_MSG = (
        "📃 Verfügbare Formate für:\n<code>{url}</code>\n\n"
        "💡 <b>So setzen Sie das Format:</b>\n"
        "• <code>/format id 134</code> - Spezifische Format-ID herunterladen\n"
        "• <code>/format 720p</code> - Nach Qualität herunterladen\n"
        "• <code>/format best</code> - Beste Qualität herunterladen\n"
        "• <code>/format ask</code> - Immer nach Qualität fragen\n\n"
        "{audio_note}\n"
        "📋 Verwenden Sie Format-ID aus der Liste oben"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Nur Audio-Formate:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Format 140 als MP3-Audio herunterladen\n"
        "• <code>/format id140 audio</code> - dasselbe wie oben\n"
        "Diese werden als MP3-Audiodateien heruntergeladen.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Fehler beim Senden der Formate-Datei: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Formate konnten nicht abgerufen werden:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Beim Verarbeiten des Befehls ist ein Fehler aufgetreten"
    LIST_ERROR_CALLBACK_MSG = "Fehler aufgetreten"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 So verwenden Sie Format-IDs:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Nach dem Abrufen der Liste verwenden Sie eine spezifische Format-ID:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - Format 401 herunterladen\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - dasselbe wie oben\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - Format 140 als MP3-Audio herunterladen\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - dasselbe wie oben\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Nur Audio-Formate erkannt: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Diese Formate werden als MP3-Audiodateien heruntergeladen.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Nur Video-Formate:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Verwenden Sie Format-ID aus der Liste oben"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Verwendung:</b>\n"
        "<code>/link [Qualität] URL</code>\n\n"
        "<b>Beispiele:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - beste Qualität\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p oder niedriger\n"
        "• /link 720p https://youtube.com/watch?v=... - dasselbe wie oben\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K oder niedriger\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K oder niedriger"
        "</blockquote>\n\n"
        "<b>Qualität:</b> von 1 bis 10000 (z.B. 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Bitte geben Sie eine gültige URL ein"
    LINK_PROCESSING_MSG = "🔗 Direkter Link wird abgerufen..."
    LINK_DURATION_MSG = "⏱ <b>Dauer:</b> {duration} Sek\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video-Stream:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio-Stream:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Tastatur-Einstellung aktualisiert!**\n\nNeue Einstellung: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Ungültiges Argument!**\n\n"
        "Gültige Optionen: `off`, `1x3`, `2x3`, `full`\n\n"
        "Beispiel: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Tastatur-Einstellungen**\n\n"
        "Aktuell: **{current}**\n\n"
        "Wählen Sie eine Option:\n\n"
        "Oder verwenden Sie: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 Tastatur aktiviert!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Tastatur ausgeblendet"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3-Tastatur aktiviert!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3-Tastatur aktiviert!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Emoji-Tastatur aktiviert!"
    KEYBOARD_ERROR_APPLYING_MSG = "Fehler beim Anwenden der Tastatur-Einstellung {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Format auf gesetzt: Always Ask. Sie werden jedes Mal nach der Qualität gefragt, wenn Sie eine URL senden."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format auf gesetzt: Always Ask. Jetzt werden Sie jedes Mal nach der Qualität gefragt, wenn Sie eine URL senden."
    FORMAT_BEST_UPDATED_MSG = "✅ Format auf beste Qualität aktualisiert (AVC+MP4 Priorität):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Format auf ID {id} aktualisiert:\n{format}\n\n💡 <b>Hinweis:</b> Wenn dies ein Nur-Audio-Format ist, wird es als MP3-Audiodatei heruntergeladen."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Format auf ID {id} aktualisiert (Nur-Audio):\n{format}\n\n💡 Dies wird als MP3-Audiodatei heruntergeladen."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Format auf Qualität {quality} aktualisiert:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Format aktualisiert auf:\n{format}"
    FORMAT_MENU_MSG = (
        "Wählen Sie eine Format-Option oder senden Sie eine benutzerdefinierte mit:\n"
        "• <code>/format &lt;format_string&gt;</code> - benutzerdefiniertes Format\n"
        "• <code>/format 720</code> - 720p Qualität\n"
        "• <code>/format 4k</code> - 4K Qualität\n"
        "• <code>/format 8k</code> - 8K Qualität\n"
        "• <code>/format id 401</code> - spezifische Format-ID\n"
        "• <code>/format ask</code> - Menü immer anzeigen\n"
        "• <code>/format best</code> - bv+ba/beste Qualität"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Um ein benutzerdefiniertes Format zu verwenden, senden Sie den Befehl in folgender Form:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Ersetzen Sie <code>bestvideo+bestaudio/best</code> mit Ihrer gewünschten Format-Zeichenkette."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Wählen Sie Ihre gewünschte Auflösung und Codec:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format auf gesetzt: Always Ask. Jetzt werden Sie jedes Mal nach der Qualität gefragt, wenn Sie eine URL senden."
    FORMAT_UPDATED_MSG = "✅ Format aktualisiert auf:\n{format}"
    FORMAT_SAVED_MSG = "✅ Format gespeichert."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Format-Auswahl aktualisiert."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Benutzerdefiniertes Format-Menü geschlossen"
    FORMAT_CODEC_SET_MSG = "✅ Codec set to {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Browser-Auswahl aktualisiert."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Zugriff verweigert. Nur für Administratoren."
    ACCESS_DENIED_ADMIN = "❌ Zugriff verweigert. Nur für Administratoren."
    WELCOME_MASTER = "Willkommen Meister 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Entschuldigung... Beim Download ist ein Fehler aufgetreten."
    SIZE_LIMIT_EXCEEDED = "❌ Die Dateigröße überschreitet das Limit von {max_size_gb} GB. Bitte wählen Sie eine kleinere Datei innerhalb der erlaubten Größe."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Script nicht gefunden: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Lade frischen Firebase-Dump mit {script_path} herunter ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase-Cache erfolgreich neu geladen!"
    ADMIN_CACHE_FAILED_MSG = "❌ Firebase-Cache konnte nicht neu geladen werden. Überprüfen Sie, ob {cache_file} existiert."
    ADMIN_ERROR_RELOADING_MSG = "❌ Fehler beim Neuladen des Caches: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Fehler beim Ausführen von {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Promo-Nachricht an alle anderen Benutzer gesendet</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Promo-Nachricht kann nicht gesendet werden. Versuchen Sie, auf eine Nachricht zu antworten\nOder es ist ein Fehler aufgetreten</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ Benutzer hat noch keinen Inhalt heruntergeladen...</b> Existiert nicht in den Logs"
    ADMIN_INVALID_COMMAND_MSG = "❌ Ungültiger Befehl"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ Keine Daten im Cache für <code>{{path}}</code> gefunden"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Warteschlange ist leer — niemand hat den Kanal noch verlassen."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Sperr-Warteschlange</b>\nAusstehend gesamt: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (verlassen: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… und {extra} weitere Benutzer."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Verwenden Sie /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Benutzer aus Warteschlange gesperrt: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Auto-Sperrung aktiviert: neue Verlasser werden sofort gesperrt."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Auto-Sperrung deaktiviert."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Geplantes Auto-Sperr-Fenster auf alle {interval} gesetzt."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Kanal-Aktivitätsprotokoll für die letzten {hours} Stunden (2 Tage)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 Letzte {hours} Stunden (2 Tage): {joined} beigetreten, {left} verlassen."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Keine Aktivität für die letzten {hours} Stunden (2 Tage)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Gesamt: 🟢 {joined} beigetreten, 🔴 {left} verlassen."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Kein Zugriff auf Kanal-Aktivitätsprotokoll. Bots können Admin-Logs nicht lesen. Geben Sie CHANNEL_GUARD_SESSION_STRING in der Konfiguration mit einer Benutzersitzung an, um diese Funktion zu aktivieren."
    BAN_TIME_USAGE_MSG = "❌ Verwendung: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Verwenden Sie Formate wie 10s, 6m, 5h, 4d, 3w, 2M oder 1y."
    BAN_TIME_SET_MSG = "🕒 Kanal-Log-Scan-Intervall auf {interval} gesetzt."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Kanal-Scan-Bericht\n"
        "Ausgeführt um: {run_ts}\n"
        "Intervall: {interval}\n"
        "Neue Verlasser: {new_leavers}\n"
        "Auto-Sperrungen: {auto_banned}\n"
        "Ausstehend: {pending}\n"
        "Letzte event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Verwendung: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Administrator kann keinen Administrator löschen"
    ADMIN_USER_BLOCKED_MSG = "Benutzer gesperrt 🔒❌\n \nID: <code>{user_id}</code>\nSperrdatum: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> ist bereits gesperrt ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Entschuldigung! Sie sind kein Administrator"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Verwendung: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Benutzer entsperrt 🔓✅\n \nID: <code>{user_id}</code>\nEntsperrdatum: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> ist bereits entsperrt ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Entsperrte Benutzer: {count}\n⏱ Zeitstempel: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Verwendung: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Benutzer ignoriert 👁️❌\n \nID: <code>{user_id}</code>\nIgnoriert am: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> wird bereits ignoriert ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Verwendung: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Benutzer wird nicht mehr ignoriert 👁️✅\n \nID: <code>{user_id}</code>\nNicht mehr ignoriert am: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> wird nicht ignoriert ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Bot-Laufzeit -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Bitte geben Sie eine URL zum Cache-Löschen an.\nVerwendung: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Bitte geben Sie eine gültige URL ein.\nVerwendung: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Cache erfolgreich für URL gelöscht:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Kein Cache für diesen Link gefunden."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Fehler beim Löschen des Caches: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Zugriff verweigert. Nur für Administratoren."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Führe Porn-Liste-Update-Script aus: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Script erfolgreich abgeschlossen!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Script erfolgreich abgeschlossen!\n\nAusgabe:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Script fehlgeschlagen mit Rückgabecode {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Fehler beim Ausführen des Scripts: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Lade Porn- und Domain-bezogene Caches neu..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Porn-Caches erfolgreich neu geladen!\n\n"
        "📊 Aktueller Cache-Status:\n"
        "• Porn-Domains: {porn_domains}\n"
        "• Porn-Schlüsselwörter: {porn_keywords}\n"
        "• Unterstützte Seiten: {supported_sites}\n"
        "• WHITELIST: {whitelist}\n"
        "• GREYLIST: {greylist}\n"
        "• BLACK_LIST: {black_list}\n"
        "• WHITE_KEYWORDS: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Fehler beim Neuladen des Porn-Caches: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Bitte geben Sie eine URL zum Überprüfen an.\nVerwendung: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Bitte geben Sie eine gültige URL ein.\nVerwendung: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Überprüfe URL auf NSFW-Inhalt...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Porn-Überprüfungsergebnis</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Status:</b> <b>{status_text}</b>\n\n"
        "<b>Erklärung:</b>\n{explanation}"
        "<b>Erklärung:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Fehler beim Überprüfen der URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Cookies bereinigt."
    CLEAN_LOGS_CLEANED_MSG = "Logs bereinigt."
    CLEAN_TAGS_CLEANED_MSG = "Tags bereinigt."
    CLEAN_FORMAT_CLEANED_MSG = "Format bereinigt."
    CLEAN_SPLIT_CLEANED_MSG = "Split bereinigt."
    CLEAN_MEDIAINFO_CLEANED_MSG = "MediaInfo bereinigt."
    CLEAN_SUBS_CLEANED_MSG = "Untertitel-Einstellungen bereinigt."
    CLEAN_KEYBOARD_CLEANED_MSG = "Tastatur-Einstellungen bereinigt."
    CLEAN_ARGS_CLEANED_MSG = "Argumente-Einstellungen bereinigt."
    CLEAN_NSFW_CLEANED_MSG = "NSFW-Einstellungen bereinigt."
    CLEAN_PROXY_CLEANED_MSG = "Proxy-Einstellungen bereinigt."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Flood-Warte-Einstellungen bereinigt."
    CLEAN_ALL_CLEANED_MSG = "Alle Dateien bereinigt."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nAktion wählen:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Cookie-Datei gespeichert"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Validierung für Nicht-YouTube-Cookies übersprungen"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Cookie-Datei existiert, hat aber falsches Format"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Cookie-Datei wurde nicht gefunden."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Starte YouTube-Cookies-Test...\n\nBitte warten Sie, während ich Ihre Cookies überprüfe und validiere."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Ihre vorhandenen YouTube-Cookies funktionieren ordnungsgemäß!\n\nKeine Notwendigkeit, neue herunterzuladen."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Ihre vorhandenen YouTube-Cookies sind abgelaufen oder ungültig.\n\n🔄 Lade neue Cookies herunter..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} Cookie-Quelle ist nicht konfiguriert!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} Cookie-Quelle muss eine .txt-Datei sein!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Bereichslimit überschritten: {range_count} Dateien angefordert (Maximum {max_img_files}).\n\nVerwenden Sie einen dieser Befehle, um die maximale Anzahl verfügbarer Dateien herunterzuladen:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Schließen"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Medienlimit überschritten: {count} Dateien angefordert (Maximum {max_count}).\n\nVerwenden Sie einen dieser Befehle, um die maximale Anzahl verfügbarer Dateien herunterzuladen:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 <b>{count}</b> Medienelemente vom Link gefunden"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Download-Bereich auswählen:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Browser-Impersonation"
    ARGS_REFERER_DESC_MSG = "Referer-Header"
    ARGS_USER_AGENT_DESC_MSG = "User-Agent-Header"
    ARGS_GEO_BYPASS_DESC_MSG = "Geografische Beschränkungen umgehen"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "SSL-Zertifikat überprüfen"
    ARGS_LIVE_FROM_START_DESC_MSG = "Live-Streams von Anfang herunterladen"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Live-Streams nicht von Anfang herunterladen"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "MPEG-TS-Container für HLS-Videos verwenden"
    ARGS_NO_PLAYLIST_DESC_MSG = "Nur einzelnes Video herunterladen, nicht Wiedergabeliste"
    ARGS_NO_PART_DESC_MSG = ".part-Dateien nicht verwenden"
    ARGS_NO_CONTINUE_DESC_MSG = "Teilweise Downloads nicht fortsetzen"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Audioformat für Extraktion"
    ARGS_EMBED_METADATA_DESC_MSG = "Metadaten in Videodatei einbetten"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Miniaturansicht in Videodatei einbetten"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Miniaturansicht in Datei schreiben"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Anzahl gleichzeitiger zu downloadender Fragmente"
    ARGS_FORCE_IPV4_DESC_MSG = "IPv4-Verbindungen erzwingen"
    ARGS_FORCE_IPV6_DESC_MSG = "IPv6-Verbindungen erzwingen"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For-Header-Strategie"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP-Chunk-Größe (Bytes)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Wartezeit vor Untertitel-Download (Sekunden)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Legacy-Server-Verbindungen erlauben"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "HTTPS-Zertifikatsvalidierung unterdrücken"
    ARGS_USERNAME_DESC_MSG = "Konto-Benutzername"
    ARGS_PASSWORD_DESC_MSG = "Konto-Passwort"
    ARGS_TWOFACTOR_DESC_MSG = "Zwei-Faktor-Authentifizierungscode"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Download-Fehler ignorieren und fortfahren"
    ARGS_MIN_FILESIZE_DESC_MSG = "Mindestdateigröße (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Maximaldateigröße (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Wiedergabelisten-Items zum Herunterladen (z.B. 1,3,5 oder 1-5)"
    ARGS_DATE_DESC_MSG = "Videos herunterladen, die an diesem Datum hochgeladen wurden (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Videos herunterladen, die vor diesem Datum hochgeladen wurden (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Videos herunterladen, die nach diesem Datum hochgeladen wurden (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Benutzerdefinierte HTTP-Header (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Warteintervall zwischen Anfragen (Sekunden)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Maximales Warteintervall (Sekunden)"
    ARGS_RETRIES_DESC_MSG = "Anzahl Wiederholungen"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Video-Container-Format"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Ausgabe-Container-Format für Zusammenführung"
    ARGS_SEND_AS_FILE_DESC_MSG = "Alle Medien als Dokument statt als Medium senden"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Impersonieren"
    ARGS_REFERER_SHORT_MSG = "Referer"
    ARGS_GEO_BYPASS_SHORT_MSG = "Geo-Umgehung"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Zertifikat prüfen"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Live Start"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Kein Live Start"
    ARGS_USER_AGENT_SHORT_MSG = "User-Agent"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Keine Wiedergabeliste"
    ARGS_NO_PART_SHORT_MSG = "Kein Part"
    ARGS_NO_CONTINUE_SHORT_MSG = "Nicht fortsetzen"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Audio-Format"
    ARGS_EMBED_METADATA_SHORT_MSG = "Meta einbetten"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Miniatur einbetten"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Miniatur schreiben"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Gleichzeitig"
    ARGS_FORCE_IPV4_SHORT_MSG = "IPv4 erzwingen"
    ARGS_FORCE_IPV6_SHORT_MSG = "IPv6 erzwingen"
    ARGS_XFF_SHORT_MSG = "XFF-Header"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Chunk-Größe"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Wartezeit Subs"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Legacy Connect"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Kein Zertifikat prüfen"
    ARGS_USERNAME_SHORT_MSG = "Benutzername"
    ARGS_PASSWORD_SHORT_MSG = "Passwort"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Fehler ignorieren"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Min. Größe"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Max. Größe"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Wiedergabelisten-Items"
    ARGS_DATE_SHORT_MSG = "Datum"
    ARGS_DATEBEFORE_SHORT_MSG = "Datum vor"
    ARGS_DATEAFTER_SHORT_MSG = "Datum nach"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP-Header"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Warteintervall"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Max. Wartezeit"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Video-Format"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Zusammenführungs-Format"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Als Datei senden"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ The file is too large. Maximum size is 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Nur Dateien im folgenden Format sind erlaubt .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ Die Datei sieht nicht wie cookie.txt aus (es gibt keine Zeile '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ Fehler beim Lesen der Datei: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Cookie-Datei existiert und hat das richtige Format"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} Cookie-Datei ist zu groß! Max. 100KB, erhalten {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} Cookie-Datei heruntergeladen und als cookie.txt in Ihrem Ordner gespeichert.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} Cookie-Quelle ist nicht verfügbar (Status {status}). Bitte versuchen Sie es später erneut."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Fehler beim Herunterladen der {service} Cookie-Datei. Bitte versuchen Sie es später erneut."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Benutzer hat eine neue Cookie-Datei bereitgestellt.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie erfolgreich aktualisiert:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Kein gültiges Cookie.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube Cookie-Quellen sind nicht konfiguriert!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 YouTube-Cookies werden heruntergeladen und überprüft...\n\nVersuch {attempt} von {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Zugriff verweigert. Nur für Administratoren."
    ADMIN_USER_LOGS_TOTAL_MSG = "Gesamt: <b>{total}</b>\n<b>{user_id}</b> - Protokolle (Letzte 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 Tastatur aktiviert!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Untertitel-Sprache auf gesetzt: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Untertitel-Sprache auf gesetzt: {flag} {name} mit AUTO/TRANS aktiviert."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Untertitel-Sprachen-Menü geschlossen."
    SUBS_DOWNLOADING_MSG = "💬 Untertitel werden heruntergeladen..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Firebase-Cache wird in den Speicher neu geladen..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Keine COOKIE_URL konfiguriert. Verwenden Sie /cookie oder laden Sie cookie.txt hoch."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Cookies werden von Remote-URL heruntergeladen..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL muss auf eine .txt-Datei zeigen."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fallback-Cookie-Datei ist zu groß (>100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube-Cookie-Datei über Fallback heruntergeladen und als cookie.txt gespeichert"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fallback-Cookie-Quelle nicht verfügbar (Status {status}). Versuchen Sie /cookie oder laden Sie cookie.txt hoch."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Fehler beim Herunterladen des Fallback-Cookies. Versuchen Sie /cookie oder laden Sie cookie.txt hoch."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Unerwarteter Fehler beim Herunterladen des Fallback-Cookies."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ Browser {browser} ist nicht installiert."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookies mit Browser gespeichert: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Fehler beim Speichern der Cookies: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube-Cookies funktionieren ordnungsgemäß"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube-Cookies sind abgelaufen oder ungültig\n\nVerwenden Sie /cookie, um neue Cookies zu erhalten"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - benutzerdefiniertes Format\n• <code>/format 720</code> - 720p Qualität\n• <code>/format 4k</code> - 4K Qualität"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Hinweis gesendet."
    FORMAT_MKV_TOGGLE_MSG = "MKV ist jetzt {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Keine Remote-URL konfiguriert"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Ungültiges Dateiformat"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Datei zu groß"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookies erfolgreich heruntergeladen"
    COOKIES_SERVER_ERROR_MSG = "❌ Serverfehler {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Download fehlgeschlagen"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Unerwarteter Fehler"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Browser nicht installiert."
    COOKIES_MENU_CLOSED_MSG = "Menü geschlossen."
    COOKIES_HINT_CLOSED_MSG = "Cookie-Hinweis geschlossen."
    IMG_HELP_CLOSED_MSG = "Hilfe geschlossen."
    SUBS_LANGUAGE_UPDATED_MSG = "Untertitel-Spracheinstellungen aktualisiert."
    SUBS_MENU_CLOSED_MSG = "Untertitel-Sprachen-Menü geschlossen."
    KEYBOARD_SET_TO_MSG = "Tastatur auf {setting} gesetzt"
    KEYBOARD_ERROR_PROCESSING_MSG = "Fehler beim Verarbeiten der Einstellung"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo aktiviert."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo deaktiviert."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW-Unschärfe deaktiviert."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW-Unschärfe aktiviert."
    SETTINGS_MENU_CLOSED_MSG = "Menü geschlossen."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Flood-Wartezeit aktiv. Versuchen Sie es später."
    OTHER_HELP_CLOSED_MSG = "Hilfe geschlossen."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Protokoll-Nachricht geschlossen."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menü geschlossen."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Ungültige Größe."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Error sending MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ An error occurred: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - alle Protokolle"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - alle {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Download from Remote URL"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Browser öffnen"
    SELECT_BROWSER_MSG = "Select a browser to download cookies from:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "No browsers found on this system. You can download cookies from remote URL or monitor browser status:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Browser öffnen</b> - um den Browser-Status in der Mini-App zu überwachen"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ /check_cookie konnte nicht ausgeführt werden"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Flood-Limit. Versuchen Sie es später."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Fehler beim Öffnen des Browser-Cookie-Menüs"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Als Cookie-Hinweis speichern geschlossen."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Verwendung:</b>\n<code>/link [Qualität] URL</code>\n\n<b>Beispiele:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - beste Qualität\n• /link 720 https://youtube.com/watch?v=... - 720p oder niedriger\n• /link 720p https://youtube.com/watch?v=... - wie oben\n• /link 4k https://youtube.com/watch?v=... - 4K oder niedriger\n• /link 8k https://youtube.com/watch?v=... - 8K oder niedriger</blockquote>\n\n<b>Qualität:</b> von 1 bis 10000 (z.B. 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K Qualität"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direkter Link erhalten</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio-Stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Stream-Links konnten nicht abgerufen werden"
    LINK_ERROR_GETTING_MSG = "❌ <b>Fehler beim Abrufen des Links:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Ungültiger YouTube-Cookie-Index: {selected_index}. Verfügbarer Bereich ist 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 YouTube-Cookies werden heruntergeladen und überprüft...\n\nVersuch {attempt} von {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 YouTube-Cookies werden heruntergeladen und überprüft...\n\nVersuch {attempt} von {total}\n🔍 Cookies werden getestet..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube-Cookies erfolgreich heruntergeladen und validiert!\n\nVerwendete Quelle {source} von {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Alle YouTube-Cookies sind abgelaufen oder nicht verfügbar!\n\nKontaktieren Sie den Bot-Administrator, um sie zu ersetzen."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube Cookie-Wiederholungslimit überschritten!\n\n🔢 Maximum: {limit} Versuche pro Stunde\n⏰ Bitte versuchen Sie es später erneut"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Tag #{wrong} enthält verbotene Zeichen. Nur Buchstaben, Ziffern und _ sind erlaubt.\nBitte verwenden Sie: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Ungültiges Argument!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Untertitel-Sprache gesetzt: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Beispiel: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Ausgewählte Sprache: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Always Ask Modus {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Untertitel sind deaktiviert"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Untertitel-Einstellungen</b>\n\n{status_text}\n\nUntertitel-Sprache auswählen:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - Untertitel deaktivieren\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Untertitel-Einstellungen</b>\n\n{status_text}\n\nUntertitel-Sprache auswählen:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Titel:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Dauer:</b> {duration} Sek\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video-Stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 720p maximale Qualität\n- 1.5 Stunden maximale Dauer\n- 500mb maximale Videogröße</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️WARNUNG: Aufgrund hoher CPU-Belastung ist diese Funktion sehr langsam (nahezu Echtzeit) und beschränkt auf:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Schnellbefehle:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - Untertitel deaktivieren\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - Always Ask Modus aktivieren\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - Sprache festlegen\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - Sprache mit AUTO/TRANS aktiviert festlegen\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - Always Ask Modus aktivieren\n"
    SUBS_AUTO_SUBS_TEXT = " (Auto-Untertitel)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Auto-Untertitel Modus {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS disabled via command: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Always Ask über Befehl aktiviert: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "SUBS Sprache über Befehl gesetzt: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "SUBS Sprache + Auto-Modus über Befehl gesetzt: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Benutzer hat /subs Menü geöffnet."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Benutzer hat Untertitel-Sprache gesetzt auf: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Benutzer hat AUTO/TRANS Modus umgeschaltet auf: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Benutzer hat Always Ask Modus umgeschaltet auf: {new_always_ask}"
    
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
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Fehler beim Senden der ersten Statusnachricht"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Fehler beim Ausführen von {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Firebase-Cache von automatischer Aufgabe neu geladen."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Firebase-Cache von Administrator neu geladen."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Fehler beim Neuladen des Firebase-Cache: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Übertragung initiiert. Text:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Broadcast-Nachricht an alle Benutzer gesendet."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Broadcast-Nachricht konnte nicht gesendet werden: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Admin {user_id} hat Cache für URL gelöscht: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Admin {user_id} hat Porn-Liste-Update-Skript gestartet: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Porn-Liste-Update-Skript erfolgreich abgeschlossen von Admin {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Porn-Liste-Update-Skript fehlgeschlagen von Admin {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Admin {user_id} hat versucht, nicht existierendes Skript auszuführen: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Fehler beim Ausführen des Porn-Update-Skripts von Admin {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Admin {user_id} hat Porn-Cache-Neuladen gestartet"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Fehler beim Neuladen des Porn-Cache von Admin {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Admin {user_id} hat URL auf NSFW überprüft: {url} - Ergebnis: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "Benutzer hat Format-Änderung angefordert."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "Format auf ALWAYS_ASK gesetzt."
    FORMAT_UPDATED_BEST_LOG_MSG = "Format auf beste aktualisiert: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "Format auf ID {format_id} aktualisiert: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "Format auf ID {format_id} aktualisiert (Nur-Audio): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "Format auf Qualität {quality} aktualisiert: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "Format aktualisiert auf: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "Format-Menü gesendet."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "Format-Auswahl geschlossen."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "Benutzerdefinierter Format-Hinweis gesendet."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "Format resolution menu sent."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "Returned to main format menu."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "Format updated to: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "Format set to ALWAYS_ASK."
    FORMAT_CODEC_SET_LOG_MSG = "Codec preference set to {codec}"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Benutzerdefiniertes Format-Menü geschlossen"
    
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
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo aktiviert."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo deaktiviert."
    
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
    AUDIO_HELP_SHOWN_LOG_MSG = "/audio Hilfe angezeigt"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "User requested playlist help."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Wiedergabeliste-Hilfe geschlossen."
    AUDIO_HINT_CLOSED_LOG_MSG = "Audio-Hinweis geschlossen."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Direct link menu created via LINK button for user {user_id} from {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Failed to extract direct link via LINK button for user {user_id} from {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "LIST command executed for user {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Quick Embed: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Always Ask Menü gesendet für {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Gecachte Qualitäten-Menü für Benutzer {user_id} nach Fehler erstellt: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Always Ask Menü-Fehler für {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Format ist über /args Einstellungen festgelegt"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Audio"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Video"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Video"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Weiter ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Zurück"
    SUBTITLES_NEXT_BUTTON_MSG = "Next ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ All text fields are empty"
    SENDER_VIDEO_DURATION_MSG = "Video-Dauer:"
    SENDER_UPLOADING_FILE_MSG = "📤 Datei wird hochgeladen..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Video wird hochgeladen..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Video-Dauer:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 Datei hochgeladen."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Video-Info"
    DOWN_UP_NUMBER_MSG = "Nummer"
    DOWN_UP_TITLE_MSG = "Titel"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Video heruntergeladen."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Processing for upload..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Splitted part {part} file uploaded"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Upload complete"
    DOWN_UP_FILES_UPLOADED_MSG = "files uploaded"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Schließen"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 SYNCHRONISIERT"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 UNTERTITEL"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Browser"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Direkten Link abrufen..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Verfügbare Formate werden abgerufen..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Videobeschreibung wird abgerufen..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Fehler beim Abrufen der Beschreibung: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Videobeschreibung ist nicht verfügbar"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Fehler beim Senden der Beschreibung: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Videobeschreibung an Benutzer {user_id} für {url} ({title}) gesendet"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 gallery-dl wird gestartet…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Dauer:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Browser:</b> Im Webbrowser öffnen"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Verfügbare Formate für"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 So verwenden Sie Format-IDs:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Nach Erhalt der Liste verwenden Sie eine spezifische Format-ID:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - Format 401 herunterladen"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - wie oben"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - Format 140 als MP3-Audio herunterladen"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Nur-Audio-Formate erkannt"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Diese Formate werden als MP3-Audiodateien heruntergeladen."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>So legen Sie das Format fest:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Spezifische Format-ID herunterladen"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Nach Qualität herunterladen"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Beste Qualität herunterladen"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Immer nach Qualität fragen"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Nur-Audio-Formate:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Format 140 als MP3-Audio herunterladen"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Diese werden als MP3-Audiodateien heruntergeladen."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Verwenden Sie Format-ID aus der Liste oben"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Fehler: Ursprüngliche Nachricht nicht gefunden."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Formate-Seite"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Fehler beim Anzeigen des Formate-Menüs"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Fehler beim Abrufen der Formate"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Fehler beim Abrufen verfügbarer Formate."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Bitte versuchen Sie es später erneut."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp kann diesen Inhalt nicht verarbeiten"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Das System empfiehlt stattdessen die Verwendung von gallery-dl."
    ALWAYS_ASK_OPTIONS_MSG = "**Optionen:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Für Bildergalerien: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Für einzelne Bilder: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl funktioniert oft besser für Instagram, Twitter und andere Social-Media-Inhalte."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Gallery-dl versuchen"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Format über /args festgelegt"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Untertitel"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Synchronisierte Audio"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Untertitel sind verfügbar"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Untertitel-Sprache auswählen"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Untertitel nicht gefunden & werden nicht eingebettet"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Sofortiger Repost aus Cache"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Audio-Sprache auswählen"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW ist kostenpflichtig (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Download-Qualität auswählen"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Bild herunterladen (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Video in poketube ansehen"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Direkten Link zum Video erhalten"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Liste verfügbarer Formate anzeigen"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Video-Erweiterung/Codec ändern"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Einbetten"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Nur Audio extrahieren"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW ist kostenpflichtig (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Sofortiger Repost aus Cache"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Video in poketube ansehen"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Audio-Sprache auswählen"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Beste"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Andere"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝nur Untertitel"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Intelligente Gruppierung"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Aktions-Button-Zeile hinzugefügt (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Aktions-Button-Zeilen hinzugefügt (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Untere Buttons zur bestehenden Zeile hinzugefügt"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Neue untere Zeile erstellt"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Keine Videos in Wiedergabeliste gefunden"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "Nicht unterstützte URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Kein Video gefunden"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Kein Video gefunden"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Keine Medien gefunden"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Dieser Tweet enthält nicht"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Fehler beim Abrufen der Videoinformationen:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Fehler beim Abrufen der Videoinformationen"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Versuchen Sie den Befehl <code>/clean</code> und versuchen Sie es erneut. Wenn der Fehler weiterhin besteht, erfordert YouTube eine Autorisierung. Aktualisieren Sie cookies.txt über <code>/cookie</code> oder <code>/cookies_from_browser</code> und versuchen Sie es erneut."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Menü geschlossen."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Manuelle Qualitätsauswahl"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Qualität manuell auswählen, da automatische Erkennung fehlgeschlagen ist:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Alle verfügbaren Formate"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Verfügbare Qualitäten (aus Cache)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Verwende gecachte Qualitäten - neue Formate sind möglicherweise nicht verfügbar"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Format wird heruntergeladen"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Wird heruntergeladen"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Wird mit Fortschrittsverfolgung heruntergeladen..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Wird mit Format heruntergeladen:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Audio wird mit Format heruntergeladen:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Beste Qualität wird heruntergeladen..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Datenbank-Dump wird heruntergeladen..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Wird heruntergeladen"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Formate-Seite"
    ALWAYS_ASK_FROM_CACHE_MSG = "(aus Cache)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Fehler: Ursprüngliche Nachricht nicht gefunden. Sie wurde möglicherweise gelöscht. Bitte senden Sie den Link erneut."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Fehler: Ursprüngliche URL nicht gefunden. Bitte senden Sie den Link erneut."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direkter Link erhalten</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Titel:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Dauer:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Video-Stream:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Audio-Stream:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Stream-Links konnten nicht abgerufen werden"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Direkter Link über Always Ask Menü für Benutzer {user_id} von {url} extrahiert"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Direkter Link konnte nicht über Always Ask Menü für Benutzer {user_id} von {url} extrahiert werden: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Direkter Link über down_and_up_with_format für Benutzer {user_id} von {url} extrahiert"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Direkter Link konnte nicht über down_and_up_with_format für Benutzer {user_id} von {url} extrahiert werden: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Direkter Link über down_and_audio für Benutzer {user_id} von {url} extrahiert"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Direkter Link konnte nicht über down_and_audio für Benutzer {user_id} von {url} extrahiert werden: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Audio aus Cache gesendet."
    AUDIO_PROCESSING_MSG = "🎙️ Audio wird verarbeitet..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Audio wird heruntergeladen:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Fehler beim Herunterladen des Audios aufgetreten."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Audio-Informationen konnten nicht extrahiert werden"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Nicht unterstützter Dateityp in Wiedergabeliste bei Index {index} wird übersprungen"
    AUDIO_FILE_NOT_FOUND_MSG = "Audio-Datei nach dem Download nicht gefunden."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Audio-Datei wird hochgeladen...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Audio konnte nicht gesendet werden: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Wiedergabeliste-Audio gesendet: {sent}/{total} Dateien (Qualität={quality}) an Benutzer{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Audio konnte nicht heruntergeladen werden: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Download aufgrund von Timeout abgebrochen (2 Stunden)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Video-Datei nicht gefunden: {filename}"
    VIDEO_PROCESSING_ERROR_MSG = "❌ Fehler beim Verarbeiten des Videos: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Fehler beim Senden der Beschreibungsdatei: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 Wenn Sie die Video-Beschriftung ändern möchten - antworten Sie auf das Video mit neuem Text</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Keine Untertitel erkannt"
    VIDEO_PROGRESS_MSG = "<b>Video:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Audio:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL-Limit überschritten: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Verarbeitung abgeschlossen"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Wiedergabelisten-Bereiche sind im Mehrfach-URL-Modus nicht erlaubt. Senden Sie nur einzelne URLs ohne Bereiche (*1*5, /vid 1-10, etc.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Überprüfen Sie <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>hier</a>, ob Ihre Seite unterstützt wird"
    ERROR_COOKIE_NEEDED_MSG = "Möglicherweise benötigen Sie <code>cookie</code> zum Herunterladen dieses Videos. Bereinigen Sie zuerst Ihren Arbeitsbereich über den Befehl <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Für YouTube - erhalten Sie <code>cookie</code> über den Befehl <b>/cookie</b>. Für jede andere unterstützte Seite - senden Sie Ihr eigenes Cookie (<a href='https://t.me/tg_ytdlp/203'>Anleitung1</a>) (<a href='https://t.me/tg_ytdlp/214'>Anleitung2</a>) und senden Sie danach Ihren Video-Link erneut."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Untertitel-Sprache auswählen"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Keine alternativen Audio-Sprachen"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Audio-Sprache auswählen"
    PAGE_NUMBER_MSG = "Seite {page}"
    TOTAL_PROGRESS_MSG = "Gesamtfortschritt"
    SUBTITLE_MENU_CLOSED_MSG = "Untertitel-Menü geschlossen."
    SUBTITLE_LANGUAGE_SET_MSG = "Untertitel-Sprache gesetzt: {value}"
    AUDIO_SET_MSG = "Audio gesetzt: {value}"
    FILTERS_UPDATED_MSG = "Filter aktualisiert"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Zurück"
    CLOSE_BUTTON_TEXT = "🔚Schließen"
    LIST_BUTTON_TEXT = "📃Liste"
    IMAGE_BUTTON_TEXT = "🖼Bild"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Qualitäten nicht automatisch erkannt\nVerwenden Sie die 'Andere' Schaltfläche, um alle verfügbaren Formate zu sehen.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Live-Stream erkannt**\n\nDas Herunterladen von laufenden oder unendlichen Live-Streams ist nicht erlaubt.\n\nBitte warten Sie, bis der Stream endet, und versuchen Sie erneut herunterzuladen, wenn:\n• Die Stream-Dauer bekannt ist\n• Der Stream beendet wurde\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Live-Stream-Download</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Chunk {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Max. Größe: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Gesamtdauer: {duration} Sek"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Live-Stream - Chunk {chunk}</b>\n⏱ Dauer: {duration} Sek\n📦 Größe: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Chunk {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Live-Stream-Download abgeschlossen</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "{chunks} Chunk(s) heruntergeladen"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Gesamtdauer: {duration} Sek"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Live-Stream-Download gestoppt</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Benutzerverzeichnis wurde gelöscht (wahrscheinlich durch /clean Befehl)"
    LIVE_STREAM_FILE_DELETED_MSG = "Chunk-Datei wurde gelöscht (wahrscheinlich durch /clean Befehl)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Stream ist beendet"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Bitte wählen Sie ein anderes Format mit dem Befehl `/format`."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direkter Link erhalten</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Titel:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Dauer:</b> {duration} Sek\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Video-Stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Audio-Stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Dateiverarbeitungsfehler**\n\nDas Video wurde heruntergeladen, konnte aber aufgrund ungültiger Zeichen im Dateinamen nicht verarbeitet werden.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Dateiverarbeitungsfehler**\n\nDas Video wurde heruntergeladen, konnte aber aufgrund eines ungültigen Argumentfehlers nicht verarbeitet werden.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Grund:**\n"
        "• Die heruntergeladene Datei ist keine Videodatei\n"
        "• Es könnte ein Dokument (PDF, DOC usw.) oder ein Archiv sein\n\n"
        "**Lösung:**\n"
        "• Überprüfen Sie den Link - er könnte zu einem Dokument führen, nicht zu einem Video\n"
        "• Versuchen Sie einen anderen Link oder eine andere Quelle\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Grund:**\n"
        "• Die Datei kann nicht als Video verarbeitet werden\n"
        "• Es ist möglicherweise keine Videodatei oder die Datei ist beschädigt\n\n"
        "**Lösung:**\n"
        "• Überprüfen Sie den Link - er könnte zu einem Dokument führen, nicht zu einem Video\n"
        "• Versuchen Sie einen anderen Link oder eine andere Quelle\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Format nicht verfügbar**\n\nDas angeforderte Videoformat ist für dieses Video nicht verfügbar.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Format-ID {format_id} für dieses Video nicht gefunden.\n\nVerfügbare Format-IDs: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **AV1-Format ist für dieses Video nicht verfügbar.**\n\n**Verfügbare Formate:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Dateiverarbeitungsfehler**\n\nDas Audio wurde heruntergeladen, konnte aber aufgrund ungültiger Zeichen im Dateinamen nicht verarbeitet werden.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Dateiverarbeitungsfehler**\n\nDas Audio wurde heruntergeladen, konnte aber aufgrund eines ungültigen Argumentfehlers nicht verarbeitet werden.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Benutzer hat verbotenen Inhalt eingegeben. Kann nicht heruntergeladen werden."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "NSFW-Unschärfe über Befehl gesetzt: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Benutzer hat /nsfw Menü geöffnet."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: geschlossen."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "{service} Cookie konnte nicht heruntergeladen werden: status={status} (URL verborgen)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Fehler beim Herunterladen des {service} Cookies: {error} (URL verborgen)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Unerwarteter Fehler beim Herunterladen des {service} Cookies (URL verborgen): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Cookie-Datei für Benutzer {user_id} aktualisiert."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Ungültiger Cookie-Inhalt von Benutzer {user_id} bereitgestellt."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "YouTube Cookie-URLs sind leer für Benutzer {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "YouTube-Cookies für Benutzer {user_id} von Quelle {source} heruntergeladen und validiert."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Alle YouTube Cookie-Quellen sind für Benutzer {user_id} fehlgeschlagen."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Fehler im check_porn Befehl von Admin {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Split-Teilgröße auf {size} Bytes gesetzt."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Video-Upload mit Dateiaufteilung abgeschlossen."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Wiedergabelisten-Videos gesendet: {sent}/{total} Dateien (Qualität={quality}) an Benutzer {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Unbekannter Fehler: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Nicht unterstützter Dateityp in Wiedergabeliste bei Index {index} wird übersprungen"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg nicht gefunden. Bitte installieren Sie FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Konvertierung zu MP4 fehlgeschlagen: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Das Einbetten von Untertiteln kann lange dauern (bis zu 1 Min. pro 1 Min. Video)!\n🔥 Beginne mit dem Einbrennen von Untertiteln..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Untertitel können aufgrund von Limits nicht eingebettet werden (Qualität/Dauer/Größe)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Untertitel sind für die ausgewählte Sprache nicht verfügbar"
    ERROR_SENDING_VIDEO_MSG = "❌ Fehler beim Senden des Videos: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Wiedergabelisten-Videos gesendet: {sent}/{total} Dateien."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Download aufgrund von Timeout abgebrochen (2 Stunden)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Video konnte nicht heruntergeladen werden: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Fehler: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON muss ein Objekt (Wörterbuch) sein."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Ungültiges JSON-Format. Bitte geben Sie gültiges JSON an."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Wert muss zwischen {min_val} und {max_val} liegen."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} auf gesetzt: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Wahr"
    ARGS_FALSE_BUTTON_MSG = "❌ Falsch"
    ARGS_BACK_BUTTON_MSG = "🔙 Zurück"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Schließen"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Wahr"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Falsch"
    ARGS_NOT_SET_MSG = "Nicht gesetzt"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ AV1-Format ist für dieses Video nicht verfügbar.\n\nVerfügbare Formate:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Fehler beim Herunterladen: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ Keine Videos in Wiedergabeliste bei Index {index} gefunden."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Video-Konvertierung fehlgeschlagen**\n\nDas Video konnte aufgrund eines ungültigen Argumentfehlers nicht zu MP4 konvertiert werden.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Video-Konvertierung fehlgeschlagen**\n\nDas Video konnte nicht zu MP4 konvertiert werden.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Stream-Links konnten nicht abgerufen werden"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Fehler beim Abrufen des Links:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ Kein Inhalt bei Index {index} gefunden"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Fehler: Ursprüngliche Nachricht nicht gefunden."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Fehler: URL nicht gefunden."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Diese URL kann nicht eingebettet werden."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} Codec ist für dieses Video nicht verfügbar"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} Format ist für dieses Video nicht verfügbar"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood-Limit. Versuchen Sie es später."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Cookie prüfen"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ ALLE (AUTO)"
    PROXY_OFF_BUTTON_MSG = "❌ AUS"
    PROXY_CLOSE_BUTTON_MSG = "🔚Schließen"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Land auswählen:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Länderauswahl löschen"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Ausgewähltes Land: {country} (Code: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Verfügbare Proxys: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Bot wird es zuerst mit HTTP versuchen, dann mit SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Proxy wird für das ausgewählte Land automatisch aktiviert"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Länderauswahl gelöscht"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Länderauswahl gelöscht"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Ausgewähltes Land: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Land aus Datei verwenden: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Verfügbare Länder aus der Datei: {count}"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ EIN"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ AUS"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Schließen"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV: EIN"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV: AUS"
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ EIN (Keine Unschärfe)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ EIN (Keine Unschärfe)"
    NSFW_OFF_BLUR_MSG = "✅ AUS (Unschärfe)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ AUS (Unschärfe)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Sauber"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Fehler beim Verarbeiten der Antwortnachricht für Benutzer {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Fehler beim Senden der Broadcast-Nachricht an Benutzer {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Protokolle von {bot_name}\nBenutzer: {user_id}\nGesamtprotokolle: {total}\nAktuelle Zeit: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nGesamt {path}: {count}\nAktuelle Zeit: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Gesamtbenutzer: {count}</i>\nLetzte 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Porn-Caches von Admin {admin_id} neu geladen. Domains: {domains}, Keywords: {keywords}, Sites: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Fehler beim Senden der Timeout-Nachricht: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Sprache wählen</b>"
    LANG_CHANGED_MSG = "✅ Sprache geändert zu {lang_name}"
    LANG_ERROR_MSG = "❌ Fehler beim Ändern der Sprache"
    LANG_CLOSED_MSG = "Sprachauswahl geschlossen"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] Rückruf: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Browser-Überwachungs-Button mit URL hinzufügen: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "Browser-Überwachungs-URL nicht konfiguriert: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Tastatur-Einstellung aktualisiert!**\n\nNeue Einstellung: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Tastatur konnte nicht ausgeblendet werden: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Funktionierende YouTube-Cookies für Link-Extraktion für Benutzer {user_id} verwenden"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Keine funktionierenden YouTube-Cookies für Link-Extraktion für Benutzer {user_id} verfügbar"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Vorhandene YouTube-Cookies für Link-Extraktion für Benutzer {user_id} verwenden"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Keine YouTube-Cookies für Link-Extraktion für Benutzer {user_id} gefunden"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Globale Cookie-Datei in Benutzer {user_id} Ordner für Link-Extraktion kopiert"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Benutzer {user_id} hat mediainfo Befehl angefordert"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Benutzer {user_id} ist Admin: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Benutzer {user_id} ist im Kanal: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Benutzer {user_id} Zugriff verweigert - nicht Admin und nicht im Kanal"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Benutzer {user_id} Zugriff gewährt"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] Rückruf: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Dieser Befehl ist nur für Administratoren verfügbar."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Download mit PO-Token-Unterstützung abgeschlossen"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood-Limit. Versuchen Sie es später."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST-Token-Aktualisierungsfehler: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Fehler beim Schließen der Firebase-Sitzung: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Fehler beim Initialisieren der Basis-DB-Struktur: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Nicht alle Parameter sind in config.py gesetzt (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL ist nicht gesetzt"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey ist nicht gesetzt für das Abrufen von idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Fehler beim Herunterladen des Firebase-Dumps: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Firebase-Dump konnte nicht über REST heruntergeladen werden"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Fehler in _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Fehler beim Ausführen von auto reload_cache (Versuch {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Alle Wiederholungsversuche fehlgeschlagen"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Firebase-Dump-Download wird gestartet um {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Abhängigkeit nicht verfügbar: requests oder Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ Datenbank ist leer"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Fehler beim Schließen des Loggers: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Fehler während der Bereinigung: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Klon-Fehler: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Klon-Timeout"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Klon-Ausnahme: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Update vom Benutzer abgebrochen"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Repository erfolgreich geklont"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Backups nach _backup/ verschoben"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Alle Module sind geladen"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Bereinigung beim Beenden abgeschlossen"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Signal {signal} empfangen, wird ordnungsgemäß heruntergefahren..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Bitte warten..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 HLS-Stream wird heruntergeladen:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "Warten auf Fragmente"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Backup {ts} nicht in _backup/ gefunden"
    RESTORE_FAILED_RESTORE_MSG = "❌ Wiederherstellung fehlgeschlagen {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Wiederhergestellt: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Details:</b> {error_details}\n\nDownload aufgrund eines kritischen Fehlers gestoppt.\n\n💡 <b>Tipp:</b> Wenn Sie einen 401 Unauthorized Fehler erhalten, versuchen Sie den Befehl <code>/cookie instagram</code> zu verwenden oder senden Sie Ihre eigenen Cookies zur Authentifizierung mit Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domain in Porn-Blacklist: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Porn-Schlüsselwörter gefunden: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domain in Whitelist: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Whitelist-Schlüsselwörter gefunden: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Keine Porn-Schlüsselwörter gefunden"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API-Fehler bei Index {index}, überspringe zum nächsten Audio..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API-Fehler bei Index {index}, überspringe zum nächsten Video..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "Benutzer hat eine <b>URL</b> eingegeben\n <b>Benutzername:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>Benutzer hat folgendes eingegeben:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Kanal beitreten"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Handler wird registriert: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Meine 5 Cookies herunterladen"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Browser YT-Cookie abrufen"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Cookie-Datei validieren"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Benutzerdefiniertes Cookie hochladen"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Schließen"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Verfügbare Formate für: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Schließen"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Schließen"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Schließen"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Schließen"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Hilfe geschlossen."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Geschlossen"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Fehler aufgetreten"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg nicht in PATH oder Projektverzeichnis gefunden. Bitte installieren Sie FFmpeg."
    YTDLP_NOT_FOUND_MSG = "yt-dlp Binary nicht in PATH oder Projektverzeichnis gefunden. Bitte installieren Sie yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Video wird in {rounds} Teile aufgeteilt, was möglicherweise übermäßig ist"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Video-Teil {current}/{total} wird aufgeteilt: {start_time:.2f}s bis {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Split-Teil {part} konnte nicht erstellt werden: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Split-Teil {part} erfolgreich erstellt: {target_name} ({size} Bytes)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Fehler beim Aufteilen des Video-Teils {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Video erfolgreich in {count} Teile aufgeteilt"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Fehler im Video-Aufteilungsprozess: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Fehler beim Verarbeiten des Videos {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Video-Datei existiert nicht: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Fehler beim Parsen der Abmessungen '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Video-Abmessungen konnten nicht aus '{size_result}' bestimmt werden, verwende Standard: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Fehler beim Erstellen des Thumbnails: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Fehler beim Parsen der Video-Dauer: {error}, Ergebnis war: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Thumbnail wurde nicht bei {thumb_dir} erstellt, verwende Standard"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Befehlsausführungsfehler: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Fehler beim Erstellen des Thumbnails mit FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Nicht-Dict-Konfigurationsabschnitt wird übersprungen: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Setze {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Verwende Benutzer-Cookies: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Verwende YouTube-Cookies für Benutzer {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Globale Cookie-Datei in Benutzer {user_id} Ordner kopiert"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Verwende kopierte globale Cookies als Benutzer-Cookies: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Globale Cookie-Datei für Benutzer {user_id} konnte nicht kopiert werden: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Verwende --no-cookies für Domain: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy angefordert, aber Import/Abruf der Konfiguration fehlgeschlagen: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Erzwinge Proxy-Verwendung für gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy angefordert, aber Proxy-Konfiguration ist unvollständig"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Proxy-Helper fehlgeschlagen: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Extractor-Elemente werden geparst..."
    GALLERY_DL_ITEM_COUNT_MSG = "Element {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Metadaten gefunden (Tag 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL gefunden (Tag 3): {url}, Metadaten: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Metadaten gefunden (Legacy): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL gefunden (Legacy): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Dateiname gefunden: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Verzeichnis gefunden: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Erweiterung gefunden: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "{count} Elemente geparst, Info: {info}, Fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Setze gallery-dl Konfiguration: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Versuche Strategie A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor Modul nicht gefunden"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() in dieser Version nicht verfügbar"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Rufe extractor.find({url}) auf"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Kein Extractor hat die URL gematcht"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Setze Cookies auf Extractor: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Cookies auf Extractor setzen fehlgeschlagen: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Extractor gefunden, rufe items() auf"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Strategie A erfolgreich, Info erhalten: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Strategie A: extractor.items() hat keine gültigen Informationen zurückgegeben"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Strategie A (extractor.find) fehlgeschlagen: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Fallback-Metadaten von --get-urls: gesamt={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Alle Strategien konnten keine Metadaten erhalten"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Bild-Informationen extrahieren fehlgeschlagen: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job Modul nicht gefunden (defekte Installation?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob in dieser Version nicht verfügbar"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Suche nach heruntergeladenen Dateien im gallery-dl Verzeichnis"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Versuche Dateien anhand von Namen vom Extractor zu finden"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Fehler beim Lesen der Benutzer-Argumente für {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Fehler beim Verarbeiten des Videos{video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Benutzer {user_id} hat send_as_file aktiviert, sende als Dokument"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video hat wiederholt ein Timeout; wechsle zu send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Beschriftung zu lang, versuche mit minimaler Beschriftung"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (minimale Beschriftung) hat ein Timeout; wechsle zu send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Fehler beim Senden des Videos mit minimaler Beschriftung: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Fehler beim Senden der vollständigen Beschreibungsdatei: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Fehler beim Entfernen der temporären Beschreibungsdatei: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Überspringe match_filter für Domain in NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Überprüfe vorhandene YouTube-Cookies auf Benutzer-URL für Format-Erkennung für Benutzer {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Vorhandene YouTube-Cookies funktionieren auf Benutzer-URL für Format-Erkennung für Benutzer {user_id} - verwende sie"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Vorhandene YouTube-Cookies funktionieren nicht auf Benutzer-URL, versuche neue zu erhalten für Format-Erkennung für Benutzer {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Versuche YouTube-Cookie-Quelle {i} für Format-Erkennung für Benutzer {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "YouTube-Cookies von Quelle {i} funktionieren auf Benutzer-URL für Format-Erkennung für Benutzer {user_id} - in Benutzer-Ordner gespeichert"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "YouTube-Cookies von Quelle {i} funktionieren nicht auf Benutzer-URL für Format-Erkennung für Benutzer {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "YouTube-Cookies von Quelle {i} konnten nicht heruntergeladen werden für Format-Erkennung für Benutzer {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Alle YouTube-Cookie-Quellen sind für Format-Erkennung für Benutzer {user_id} fehlgeschlagen, versuche ohne Cookies"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Keine YouTube-Cookie-Quellen konfiguriert für Format-Erkennung für Benutzer {user_id}, versuche ohne Cookies"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Keine YouTube-Cookies gefunden für Format-Erkennung für Benutzer {user_id}, versuche neue zu erhalten"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Verwende YouTube-Cookies für Format-Erkennung für Benutzer {user_id} (bereits im Always Ask Menü validiert)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Keine YouTube-Cookies gefunden für Format-Erkennung für Benutzer {user_id}, versuche wiederherzustellen..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Globale Cookie-Datei in Benutzer {user_id} Ordner für Format-Erkennung kopiert"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Globale Cookie-Datei für Benutzer {user_id} konnte nicht kopiert werden: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Verwende --no-cookies für Domain in get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "App noch nicht initialisiert. Kann nicht auf {name} zugreifen"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Beschriftung:</b> <code>{caption}</code>\n<b>Benutzer-ID:</b> <code>{user_id}</code>\n<b>Benutzer Vorname:</b> <code>{users_name}</code>\n<b>Video-Datei-ID:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Fehler im caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Unerwarteter Fehler im caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 Video-URL</a>{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL fehlt in der Konfiguration"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin initialisiert"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken aktualisiert"
    DB_LOG_FOR_USER_ADDED_MSG = "Protokoll für Benutzer hinzugefügt"
    DB_DATABASE_CREATED_MSG = "Datenbank erstellt"
    DB_BOT_STARTED_MSG = "Bot gestartet"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY in config.py gespeichert: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Wiedergabelisten-Teil bereits gecacht: {path_parts}, überspringe"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: kein Cache für URL/Qualitäts-Variante gefunden, gebe leeres Dict zurück"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: schnelle Zählung für großen Bereich: {cached_count} gecachte Videos"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: kein Cache für Hash {url_hash}, Qualität {quality_key} gefunden"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: kein Cache für URL-Variante gefunden, gebe None zurück"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Zugriff verweigert. Nur für Administratoren."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Automatisches Firebase-Cache-Neuladen aktualisiert!\n\n📊 Status: {status}\n⏰ Zeitplan: alle {interval} Stunden ab 00:00\n🕒 Nächstes Neuladen: {next_exec} (in {delta_min} Minuten)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Automatisches Firebase-Cache-Neuladen gestoppt!\n\n📊 Status: ❌ DEAKTIVIERT\n💡 Verwenden Sie /auto_cache on zum erneuten Aktivieren"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Ungültiges Argument. Verwenden Sie /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Intervall muss zwischen 1 und 168 Stunden liegen"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Intervall konnte nicht gesetzt werden"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Automatisches Firebase-Cache-Intervall aktualisiert!\n\n📊 Status: ✅ AKTIVIERT\n⏰ Zeitplan: alle {interval} Stunden ab 00:00\n🕒 Nächstes Neuladen: {next_exec} (in {delta_min} Minuten)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Automatisches Firebase-Cache-Neuladen gestartet!\n\n📊 Status: ✅ AKTIVIERT\n⏰ Zeitplan: alle {interval} Stunden ab 00:00\n🕒 Nächstes Neuladen: {next_exec} (in {delta_min} Minuten)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Automatisches Firebase-Cache-Neuladen gestoppt!\n\n📊 Status: ❌ DEAKTIVIERT\n💡 Verwenden Sie /auto_cache on zum erneuten Aktivieren"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Automatisches Neuladen AKTIVIERT; nächstes Mal um {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Automatisches Neuladen von Admin DEAKTIVIERT."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Automatisches Neuladen-Intervall auf {interval}h gesetzt; nächstes Mal um {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Automatisches Neuladen gestartet; nächstes Mal um {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Automatisches Neuladen von Admin gestoppt."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase-Cache geladen: {count} Root-Knoten"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Firebase-Cache-Datei nicht gefunden, starte mit leerem Cache: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Firebase-Cache konnte nicht geladen werden: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase-Cache neu geladen: {count} Root-Knoten"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Firebase-Cache-Datei nicht gefunden: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Firebase-Cache konnte nicht neu geladen werden: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 Sie sind vom Bot gesperrt! Zum Entsperren kontaktieren Sie {Config.ADMIN_USERNAME}\n<blockquote>P.S. Verlassen Sie den Kanal nicht - Sie werden automatisch gesperrt ⛔️</blockquote>\n🌍Sprache ändern /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Keine Videoformate gefunden. Versuche Bild-Downloader…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram hat das Senden von Nachrichten eingeschränkt.\n⏳ Bitte warten Sie: {time_str}\nUm den Timer zu aktualisieren, senden Sie die URL erneut 2 Mal."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Klicken Sie auf die Schaltfläche, um die Stream-URL zu kopieren, und fügen Sie sie dann in die VLC-App ein</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Klicken Sie auf die Schaltfläche, um die Stream-URL zu kopieren, und fügen Sie sie dann in die VLC-App ein</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Fehler beim Abrufen des Links:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Fehler beim Senden der Formate-Datei: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Formate konnten nicht abgerufen werden:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Analysiere... (6 Sek. warten)"
    AA_PROCESSING_MSG = "🔎 Analysiere..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{wrong} enthält verbotene Zeichen. Nur Buchstaben, Ziffern und _ sind erlaubt.\nBitte verwenden Sie: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Für die Arbeit in der Gruppe benötigt der Bot Administratorrechte. Bitte machen Sie den Bot zum Administrator dieser Gruppe."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Hallo {first_name},\n \n<i>Dieser Bot🤖 kann Videos direkt in Telegram herunterladen.😊 Für weitere Informationen drücken Sie <b>/help</b></i> 👈\n\n<blockquote>P.S. Das Herunterladen von 🔞NSFW-Inhalten und Dateien von ☁️Cloud Storage ist kostenpflichtig! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Verlassen Sie den Kanal nicht - Sie werden von der Bot-Nutzung gesperrt ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Keine Dateien zum Entfernen."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 Alle Dateien erfolgreich entfernt!\n\nEntfernte Dateien:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ WARTEN SIE, BIS IHR VORHERIGER DOWNLOAD ABGESCHLOSSEN IST"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "App-Instanz ist None in check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict ist None, erlaube Download"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict ist None, erlaube Untertitel-Einbettung"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: überprüfe Limits - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: info_dict Schlüssel: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Untertitel-Einbettung übersprungen: Dauer {duration}s überschreitet Limit {max_duration}s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Untertitel-Einbettung übersprungen: Größe {size_mb:.2f}MB überschreitet Limit {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Untertitel-Einbettung übersprungen: Qualität {width}x{height} (min. Seite {min_side}p) überschreitet Limit {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "Wiedergabeliste"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Bereichslimit überschritten für {service}: {count} (Maximum {max_count}).\n\nVerwenden Sie einen dieser Befehle, um die maximal verfügbaren Dateien herunterzuladen:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Bereichslimit überschritten für {service}: {count} (Maximum {max_count})\nBenutzer-ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "PO-Token-Provider in Konfiguration deaktiviert"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} ist keine YouTube-Domain, überspringe PO-Token"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO-Token-Provider ist nicht verfügbar bei {base_url}, wechsle zu Standard-YouTube-Extraktion"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO-Token-Provider-Cache geleert, wird Verfügbarkeit bei nächster Anfrage überprüfen"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "App-Instanz noch nicht verfügbar"
    HELPER_USER_NAME_MSG = "Benutzer"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood-Wartezeit erkannt, warte {wait_seconds} Sekunden"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood-Wartezeit erkannt, aber Zeit konnte nicht extrahiert werden, warte {retry_delay} Sekunden"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno Fehler erkannt, warte {retry_delay} Sekunden"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy-Konfiguration unvollständig, verwende direkte Verbindung"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Schließen"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Schließen"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Schließen"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Protokolldatei entfernt."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Tags-Datei entfernt."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Format-Datei entfernt."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Split-Datei entfernt."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Mediainfo-Datei entfernt."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Untertitel-Einstellungen entfernt."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Tastatur-Einstellungen entfernt."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Args-Einstellungen entfernt."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 NSFW-Einstellungen entfernt."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Proxy-Einstellungen entfernt."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Flood-Wait-Einstellungen entfernt."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Schließen"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Video-Download-Befehl"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Verwendung: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Beispiele:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (direkte Reihenfolge)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (umgekehrte Reihenfolge)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Siehe auch: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Benutzer {user_id} hat add_bot_to_group-Befehl geschlossen"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "YouTube-ID konnte nicht extrahiert werden"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Thumbnail konnte nicht heruntergeladen werden oder ist zu groß"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Audio-Sprache auswählen"
    AA_NO_SUBTITLES_DETECTED_MSG = "Keine Untertitel erkannt"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Untertitel-Sprache auswählen"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Authentifizierungsfehler"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Konto nicht gefunden"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Konto nicht verfügbar"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Rate-Limit überschritten"
    GALLERY_DL_NETWORK_ERROR_MSG = "Netzwerkfehler"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Inhalt nicht verfügbar"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Geografische Beschränkungen"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Verifizierung erforderlich"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Richtlinienverletzung"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Unbekannter Fehler"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Download gestartet</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Schließen"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Video-Download-Befehl</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Verwendung: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Beispiele:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Siehe auch: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Flood-Limit. Versuchen Sie es später."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Cookie-Befehl Verwendung</b>

<code>/cookie</code> - Cookie-Menü anzeigen
<code>/cookie youtube</code> - YouTube-Cookies herunterladen
<code>/cookie instagram</code> - Instagram-Cookies herunterladen
<code>/cookie tiktok</code> - TikTok-Cookies herunterladen
<code>/cookie x</code> oder <code>/cookie twitter</code> - Twitter/X-Cookies herunterladen
<code>/cookie facebook</code> - Facebook-Cookies herunterladen
<code>/cookie custom</code> - Benutzerdefinierte Cookie-Anweisungen anzeigen

<i>Verfügbare Dienste hängen von der Bot-Konfiguration ab.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Cookie-Datei entfernt und Cache geleert."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Zurück"
    SUBS_BACK_BUTTON_MSG = "🔙Zurück"
    SUBS_OFF_BUTTON_MSG = "🚫 AUS"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - Sprache festlegen"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - Sprache mit AUTO/TRANS festlegen"
    SUBS_VALID_OPTIONS_MSG = "Gültige Optionen:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 SPRACHE"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 BEREINIGEN"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIES"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MEDIEN"
    SETTINGS_INFO_BUTTON_MSG = "📖 INFO"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ MEHR"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Nur Cookies"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Protokolle "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Tags"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Format"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Aufteilen"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Untertitel"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Tastatur"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Argumente"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Proxy"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Flood-Wartezeit"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Alle Dateien"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Meine 5 Cookies herunterladen"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Browser YT-Cookie abrufen"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Cookie-Datei validieren"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Benutzerdefiniertes Cookie hochladen"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Qualität & Format ändern"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - MediaInfo EIN / AUS"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Split-Video-Teilgröße ändern"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Video als Audio herunterladen"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Untertitel-Spracheinstellungen"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Wie man Wiedergabelisten herunterlädt"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Bilder über gallery-dl herunterladen"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Ihre #tags senden"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Anweisungen erhalten"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Ihre Protokolle senden"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Wiedergabelisten-Hilfe"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - Anleitung"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Direkte Video-Links erhalten"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Proxy aktivieren/deaktivieren"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Tastatur-Layout"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Inline-Such-Helfer"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp-Argumente"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - NSFW-Unschärfe-Einstellungen"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Bereinigungsoptionen</b>\n\nWählen Sie, was bereinigt werden soll:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobil: @vid Suche aktivieren"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobil: @vid Suche aktivieren"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 AUS"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 VOLLSTÄNDIG"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[Bilder-URL]({url})"
    IMAGE_ERROR_MSG = "❌ Fehler: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Zurück"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - benutzerdefiniertes Format"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p Qualität"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K Qualität"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K Qualität"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - spezifische Format-ID"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - Menü immer anzeigen"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/beste Qualität"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Immer Fragen (Menü + Schaltflächen)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Andere (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (am besten für PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (am besten für mobiles Telegram)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (MAX Qualität)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Benutzerdefiniert (eigene Eingabe)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Vom Browser"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Eigene"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Eingabemodus wurde automatisch aufgrund von Inaktivität geschlossen (5 Minuten)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Alle zurücksetzen"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Aktuelles anzeigen"
    ARGS_BACK_BUTTON_MSG = "🔙 Zurück"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Leiten Sie diese Nachricht an Ihre Favoriten weiter, um diese Einstellungen als Vorlage zu speichern.</i> \n\n<i>Leiten Sie diese Nachricht hierher zurück, um diese Einstellungen anzuwenden.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Aktuelle yt-dlp-Argumente:\n\nKeine benutzerdefinierten Einstellungen konfiguriert.\n\n---\n\n<i>Leiten Sie diese Nachricht an Ihre Favoriten weiter, um diese Einstellungen als Vorlage zu speichern.</i> \n\n<i>Leiten Sie diese Nachricht hierher zurück, um diese Einstellungen anzuwenden.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Aktuelle yt-dlp-Argumente:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Einstellungen exportieren"
    ARGS_SETTINGS_READY_MSG = "Einstellungen bereit zum Exportieren! Leiten Sie diese Nachricht an Favoriten weiter, um zu speichern."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Aktuelle yt-dlp-Argumente:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Einstellungen in Nachricht konnten nicht erkannt werden. Stellen Sie sicher, dass Sie eine korrekte Einstellungsvorlage gesendet haben."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Einstellungen erfolgreich importiert!\n\nAngewendete Parameter: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Haupteinstellungen:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Fehler beim Speichern der importierten Einstellungen."
    ARGS_ERROR_IMPORTING_MSG = "❌ Fehler beim Importieren der Einstellungen."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Cookie-Dateien herunterladen</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Wählen Sie einen Dienst aus, um die Cookie-Datei herunterzuladen."
    COOKIE_MENU_SAVE_INFO_MSG = "Cookie-Dateien werden als cookie.txt in Ihrem Ordner gespeichert."
    COOKIE_MENU_TIP_HEADER_MSG = "Tipp: Sie können auch den direkten Befehl verwenden:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – Cookies herunterladen und validieren"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – verwenden Sie eine spezifische Quelle nach Index (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Dann mit <code>/check_cookie</code> verifizieren (testet auf RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Immer Fragen"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Link"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Ansehen"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Beschriftung"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ SCHNEIDEN"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Video Schneiden</b>\n\nVideodauer: <b>{start_time} - {end_time}</b>\n\nBitte senden Sie den gewünschten Zeitbereich im Format:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nBeispiel: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Ungültiges Format. Bitte verwenden Sie: <code>HH:MM:SS-HH:MM:SS</code>\n\nBeispiel: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Ungültiger Bereich. Die Startzeit muss kleiner als die Endzeit sein."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ Der Zeitbereich liegt außerhalb der Videogrenzen.\n\nVideodauer: <b>{start_time} - {end_time}</b>\n\nIhr Bereich muss innerhalb dieser Grenzen liegen."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>Video wird zugeschnitten:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Teilweise abgeschlossen - {successful_uploads}/{total_files} Audio-Dateien hochgeladen."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Audio erfolgreich heruntergeladen und gesendet - {total_files} Dateien hochgeladen."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Privates TikTok-Konto</b>\n\n"
        "Dieses TikTok-Konto ist privat oder alle Videos sind privat.\n\n"
        "<b>💡 Lösung:</b>\n"
        "1. Folgen Sie dem Konto @{username}\n"
        "2. Senden Sie Ihre Cookies an den Bot mit dem Befehl <code>/cookie</code>\n"
        "3. Versuchen Sie es erneut\n\n"
        "<b>Nach dem Aktualisieren der Cookies, versuchen Sie es erneut!</b>"
    )

    #######################################################
