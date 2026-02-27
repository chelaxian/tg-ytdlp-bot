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
    CREDITS_MSG = "<blockquote><i>Zarządzane przez</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Zmień język: /lang</b>"
    TO_USE_MSG = "<i>Aby użyć tego bota, musisz zasubskrybować kanał Telegram @tg_ytdlp.</i>\nPo dołączeniu do kanału <b>wyślij ponownie link do filmu, a bot pobierze go dla Ciebie</b> ❤️\n\n<blockquote>P.S. Ze względu na potencjalną treść 🔞NSFW - pobieranie z ☁️<b>chmury</b>, 📁<b>udostępniania plików</b>, 🔗<b>skracaczy URL</b> i 🔞<b>stron dla dorosłych</b> jest płatne! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ NIE 🗑<b>usuwaj/nie rezygnuj z kanału @tg_ytdlp</b> i NIE 🤖<b>spamuj bota zbyt dużą ilością URL/poleceń</b> - zostaniesz automatycznie zbanowany ⛔️</blockquote>"

    ERROR1 = "Nie znaleziono linku URL. Proszę wprowadzić URL z <b>https://</b> lub <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Playlisty (yt-dlp)</b>

Aby pobrać playlisty, wyślij ich URL z zakresami <code>*start*end</code> na końcu. Na przykład: <code>URL*1*5</code> (pierwsze 5 filmów od 1 do 5 włącznie).<code>URL*-1*-5</code> (ostatnie 5 filmów od 1 do 5 włącznie).
Możesz też użyć <code>/vid OD-DO URL</code>. Na przykład: <code>/vid 3-7 URL</code> (pobiera filmy od 3 do 7 włącznie od początku). <code>/vid -3-7 URL</code> (pobiera filmy od 3 do 7 włącznie od końca). Działa również dla polecenia <code>/audio</code>.

<b>Przykłady:</b>

🟥 <b>Zakres filmów z playlisty YouTube:</b> (wymaga 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(pobiera pierwsze 5 filmów od 1 do 5 włącznie)
🟥 <b>Pojedynczy film z playlisty YouTube:</b> (wymaga 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(pobiera tylko 3. film)

⬛️ <b>Profil TikTok:</b> (wymaga 🍪)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(pobiera pierwsze 10 filmów z profilu użytkownika)

🟪 <b>Stories Instagram:</b> (wymaga 🍪)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(pobiera pierwsze 3 historie)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(pobiera pierwsze 10 historii z albumu)

🟦 <b>Filmy VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(pobiera pierwsze 3 filmy z profilu użytkownika/grupy)

⬛️<b>Kanały Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(pobiera filmy od 2 do 4 włącznie z kanału)

🟪 <b>Klipy Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(pobiera pierwsze 3 klipy z kanału)

🟦 <b>Grupy Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(pobiera pierwsze 2 filmy z grupy)

🟧 <b>Modele Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(pobiera pierwsze 2 filmy z profilu modelu)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(pobiera pierwsze 3 filmy z wyników wyszukiwania według twojego promptu)

i tak dalej...
zobacz <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">listę obsługiwanych stron</a>
</blockquote>

<blockquote expandable>🖼 <b>Obrazy (gallery-dl)</b>

Użyj <code>/img URL</code>, aby pobrać obrazy/zdjęcia/albumy z wielu platform.

<b>Przykłady:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Zakresy:</b>
<code>/img 11-20 https://example.com/album</code> — elementy 11..20
<code>/img 11- https://example.com/album</code> — od 11 do końca (lub limit bota)

<i>Obsługiwane platformy obejmują vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor itp. Pełna lista:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">strony obsługiwane przez gallery-dl</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Bot Pobierania Video - Pomoc</b>

📥 <b>Podstawowe Użycie:</b>
• Wyślij dowolny link → bot go pobierze
  <i>bot automatycznie próbuje pobrać filmy przez yt-dlp i obrazy przez gallery-dl.</i>
• <b>Wiele URL:</b> W trybie wyboru jakości (<code>/format</code>) możesz wysłać do <b>10 URL</b> w jednej wiadomości. Każdy URL w nowej linii lub oddzielony spacjami.
• <code>/audio URL</code> → wyodrębnij audio
• <code>/link [quality] URL</code> → uzyskaj bezpośrednie linki
• <code>/proxy</code> → włącz/wyłącz proxy dla wszystkich pobrań
• Odpowiedz na film tekstem → zmień podpis

📋 <b>Playlisty i Zakresy:</b>
• <code>URL*1*5</code> → pobierz pierwsze 5 filmów
• <code>URL*-1*-5</code> → pobierz ostatnie 5 filmów
• <code>/vid 3-7 URL</code> → staje się <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → staje się <code>URL*-3*-7</code>

🍪 <b>Ciastka i Prywatne:</b>
• Prześlij *.txt cookie dla prywatnych filmów
• <code>/cookie [service]</code> → pobierz ciasteczka (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → wybierz źródło według indeksu (1–N)
• <code>/cookies_from_browser</code> → wyodrębnij z przeglądarki
• <code>/check_cookie</code> → zweryfikuj ciasteczko
• <code>/save_as_cookie</code> → zapisz tekst jako ciasteczko

🧹 <b>Czyszczenie:</b>
• <code>/clean</code> → tylko pliki multimedialne
• <code>/clean all</code> → wszystko
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Ustawienia:</b>
• <code>/settings</code> → menu ustawień
• <code>/format</code> → jakość i format
• <code>/split</code> → podziel film na części
• <code>/mediainfo on/off</code> → informacje o mediach
• <code>/nsfw on/off</code> → rozmycie NSFW
• <code>/tags</code> → wyświetl zapisane tagi
• <code>/sub on/off</code> → napisy
• <code>/keyboard</code> → klawiatura (OFF/1x3/2x3)

🏷️ <b>Tagi:</b>
• Dodaj <code>#tag1#tag2</code> po URL
• Tagi pojawiają się w podpisach
• <code>/tags</code> → wyświetl wszystkie tagi

🔗 <b>Bezpośrednie Linki:</b>
• <code>/link URL</code> → najlepsza jakość
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → określona jakość

⚙️ <b>Szybkie Polecenia:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → ustaw jakość
• <code>/keyboard off/1x3/2x3/full</code> → układ klawiatury
• <code>/split 100mb-2000mb</code> → zmień rozmiar części
• <code>/subs off/ru/en auto</code> → język napisów
• <code>/list URL</code> → lista dostępnych formatów
• <code>/mediainfo on/off</code> → włącz/wyłącz informacje o mediach
• <code>/proxy on/off</code> → włącz/wyłącz proxy dla wszystkich pobrań

📊 <b>Informacje:</b>
• <code>/usage</code> → historia pobierania
• <code>/search</code> → wyszukiwanie wbudowane przez @vid

🖼 <b>Obrazy:</b>
• <code>URL</code> → pobierz URL obrazów
• <code>/img URL</code> → pobierz obrazy z URL
• <code>/img 11-20 URL</code> → pobierz określony zakres
• <code>/img 11- URL</code> → pobierz od 11. do końca

👨‍💻 <i>Deweloper:</i> @upekshaip
🤝 <i>Współautor:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Po prostu zapisz swoje ciasteczko jako <b><u>cookie.txt</u></b> i wyślij je do bota jako dokument.\n\n"
        "Możesz również wysłać ciasteczka jako zwykły tekst za pomocą polecenia <b><u>/save_as_cookie</u></b>.\n"
        "<b>Użycie <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>Instrukcje:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message
    SEARCH_MSG = """
🔍 <b>Wyszukiwanie wideo</b>

Naciśnij przycisk poniżej, aby aktywować wyszukiwanie wbudowane przez @vid.

<blockquote>Na PC po prostu wpisz <b>"@vid Your_Search_Query"</b> w dowolnym czacie.</blockquote>
    """
    
    # Settings and Hints
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Polecenie Pobierania Obrazów</b>\n\n"
        "Użycie: <code>/img URL</code>\n\n"
        "<b>Przykłady:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Obsługiwane platformy (przykłady):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor itp. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">pełna lista</a></blockquote>"
        "Zobacz także: "
    )
    
    LINK_HINT_MSG = (
        "Uzyskaj bezpośrednie linki do wideo z wyborem jakości.\n\n"
        "Użycie: /link + URL \n\n"
        "(np. /link https://youtu.be/abc123)\n"
        "(np. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Dodaj Bota do Grupy</b>

Dodaj moje boty do swoich grup, aby uzyskać ulepszone funkcje i wyższe limity!
————————————
📊 <b>Obecne DARMOWE Limity (w DM Bota):</b>
<blockquote>•🗑 Bałagan z wszystkich plików nieposortowanych 👎
• Maksymalny rozmiar 1 pliku: <b>8 GB </b>
• Maksymalna jakość 1 pliku: <b>NIELIMITOWANA</b>
• Maksymalny czas trwania 1 pliku: <b>NIELIMITOWANY</b>
• Maksymalna liczba pobrań: <b>NIELIMITOWANA</b>
• Maksymalna liczba URL w jednej wiadomości: <b>10</b> (tylko w trybie wyboru jakości)
• Maksymalna liczba elementów playlisty na 1 raz: <b>50</b>
• Maksymalna liczba filmów TikTok na 1 raz: <b>500</b>
• Maksymalna liczba obrazów na 1 raz: <b>1000</b>
• Limity szybkości URL: <b>5/min, 60/godz, 1000/dzień</b>
• Limit poleceń: <b>20/min</b>
• Maksymalny czas 1 pobrania: <b>2 godziny</b>
• 🔞 Treść NSFW jest płatna! 1⭐️ = $0.02
• 🆓 WSZYSTKIE INNE MEDIA SĄ CAŁKOWICIE DARMOWE
• 📝 Wszystkie logi treści i buforowanie do moich kanałów logów dla natychmiastowego ponownego udostępnienia przy ponownym pobieraniu</blockquote>

💬<b>Te limity dotyczą tylko wideo z napisami:</b>
<blockquote>• Maksymalny czas trwania wideo+napisy: <b>1.5 godziny</b>
• Maksymalny rozmiar pliku wideo+napisy: <b>500 MB</b>
• Maksymalna jakość wideo+napisy: <b>720p</b></blockquote>
————————————
🚀 <b>Korzyści Płatnej Grupy (2️⃣x Limity):</b>
<blockquote>•  🗂 Uporządkowane schowki mediów posortowane według tematów 👍
•  📁 Boty odpowiadają w temacie, w którym je wywołasz
•  📌 Automatyczne przypięcie wiadomości statusu z postępem pobierania
•  🖼 Polecenie /img pobiera media jako albumy 10-elementowe
• Maksymalny rozmiar 1 pliku: <b>16 GB</b> ⬆️
• Maksymalna liczba URL w jednej wiadomości: <b>20</b> ⬆️ (tylko w trybie wyboru jakości)
• Maksymalna liczba elementów playlisty na 1 raz: <b>100</b> ⬆️
• Maksymalna liczba filmów TikTok na 1 raz: 1000 ⬆️
• Maksymalna liczba obrazów na 1 raz: 2000 ⬆️
• Limity szybkości URL: <b>10/min, 120/godz, 2000/dzień</b> ⬆️
• Limit poleceń: <b>40/min</b> ⬆️
• Maksymalny czas 1 pobrania: <b>4 godziny</b> ⬆️
• 🔞 Treść NSFW: Darmowa z pełnymi metadanymi 🆓
• 📢 Nie trzeba subskrybować mojego kanału dla grup
• 👥 Wszyscy członkowie grupy będą mieli dostęp do płatnych funkcji!
• 🗒 Brak logów / brak cache do moich kanałów logów! Możesz odrzucić kopię/ponowne udostępnienie w ustawieniach grupy</blockquote>

💬 <b>2️⃣x limity dla wideo z napisami:</b>
<blockquote>• Maksymalny czas trwania wideo+napisy: <b>3 godziny</b> ⬆️
• Maksymalny rozmiar pliku wideo+napisy: <b>1000 MB</b> ⬆️
• Maksymalna jakość wideo+napisy: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Cennik i Konfiguracja:</b>
<blockquote>• Cena: <b>$5/miesiąc</b> za 1 bota w grupie
• Konfiguracja: Skontaktuj się z @iilililiiillliiliililliilliliiil
• Płatność: 💎TON lub inne metody💲
• Wsparcie: Pełne wsparcie techniczne wliczone</blockquote>
————————————
Możesz dodać moje boty do swojej grupy, aby odblokować darmowe 🔞<b>NSFW</b> i podwoić (x2️⃣) wszystkie limity.
Skontaktuj się ze mną, jeśli chcesz, abym zezwolił twojej grupie na używanie moich botów @iilililiiillliiliililliilliliiil
————————————
💡<b>WSKAZÓWKA:</b> <blockquote>Możesz złożyć się z dowolną liczbą przyjaciół (na przykład 100 osób) i zrobić 1 zakup dla całej grupy - WSZYSCY CZŁONKOWIE GRUPY BĘDĄ MIEĆ PEŁNY NIELIMITOWANY DOSTĘP do wszystkich funkcji botów w tej grupie za tylko <b>0.05$</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>Tryb NSFW: WŁĄCZONY✅</b>

• Treść NSFW będzie wyświetlana bez rozmycia.
• Spoilery nie będą stosowane do mediów NSFW.
• Treść będzie widoczna natychmiast

<i>Użyj /nsfw off, aby włączyć rozmycie</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>Tryb NSFW: WYŁĄCZONY</b>

⚠️ <b>Rozmycie włączone</b>
• Treść NSFW będzie ukryta pod spoilerm   
• Aby zobaczyć, będziesz musiał kliknąć na media
• Spoilery będą stosowane do mediów NSFW.

<i>Użyj /nsfw on, aby wyłączyć rozmycie</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Nieprawidłowy parametr</b>

Użyj:
• <code>/nsfw on</code> - wyłącz rozmycie
• <code>/nsfw off</code> - włącz rozmycie
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Sprawdzanie cache...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Przetwarzanie..."
    DOWNLOADING_MSG = "📥 <b>Pobieranie mediów...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Pobieranie obrazu...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Pobieranie zakończone</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Pobrano:"
    SENT_STATUS_MSG = "Wysłano:"
    PENDING_TO_SEND_STATUS_MSG = "Oczekuje na wysłanie:"
    TITLE_LABEL_MSG = "Tytuł:"
    MEDIA_COUNT_LABEL_MSG = "Liczba mediów:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Pobieranie zakończone, przetwarzanie audio..."
    VIDEO_PROCESSING_MSG = "📽 Wideo jest przetwarzane..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Wysłano z cache</b>\n\nWysłane albumy: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Wideo pomyślnie wysłane z cache."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Filmy z playlisty wysłane z cache ({cached}/{total} plików)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} filmów wysłanych z cache, pobieranie brakujących..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Wysłano z cache: {cached}\n🔄 Kontynuowanie pobierania..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Nie można przeanalizować mediów, kontynuowanie z maksymalnym dozwolonym zakresem (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Nie można określić liczby mediów, kontynuowanie z maksymalnym dozwolonym zakresem (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Nie można określić całkowitej liczby mediów, kontynuowanie z określonym zakresem {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>Nieprawidłowy URL</b>\n\nProszę podać prawidłowy URL zaczynający się od http:// lub https://"

    ERROR_OCCURRED_MSG = "❌ <b>Wystąpił błąd</b>\n\n<code>{url}</code>\n\nBłąd: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Błąd wysyłania wideo: {error}"
    ERROR_UNKNOWN_MSG = "❌ Nieznany błąd: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Za mało miejsca na dysku, aby pobrać filmy."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Rozmiar pliku przekracza limit {limit} GB. Proszę wybrać mniejszy plik w dozwolonym rozmiarze."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>Nie udało się pobrać wideo ze wszystkimi dostępnymi proxy</b>\n\nWszystkie próby pobrania przez proxy zakończyły się niepowodzeniem.\nSpróbuj:\n• Sprawdzić funkcjonalność proxy\n• Wypróbować inne proxy z listy\n• Pobrać bez proxy (jeśli to możliwe)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Błąd pobierania linku:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram ograniczył wysyłanie wiadomości.\n⏳ Proszę czekać: {time}\nAby zaktualizować timer, wyślij URL ponownie 2 razy."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram ograniczył wysyłanie wiadomości.\n⏳ Proszę czekać: \nAby zaktualizować timer, wyślij URL ponownie 2 razy."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Nie udało się pobrać napisów"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Bezpośrednie Linki Strumieniowe</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Tytuł:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Czas trwania:</b> {duration} sek\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Błąd: Nie znaleziono oryginalnej wiadomości."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{tag} zawiera niedozwolone znaki. Dozwolone są tylko litery, cyfry i _.\nProszę użyć: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Filmy z playlisty wysłane: {sent}/{total} plików."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>Wskazówka dotycząca playlist</b>

Wysłałeś link do playlisty bez określenia zakresu. Bot automatycznie pobrał pierwszy film (<code>*1*1</code>).

<b>Aby pobrać kilka filmów z playlisty, określ zakres:</b>
• <code>URL*1*5</code> — pierwsze 5 filmów (od 1 do 5 włącznie)
• <code>URL*3*3</code> — tylko 3. film
• <code>/vid 1-10 URL</code> — format alternatywny

Dowiedz się więcej: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ Wysłano z cache: {cached}/{total} plików."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Nie udało się pobrać linków strumieniowych"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Wybierz przeglądarkę, z której pobrać ciasteczka:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Nie znaleziono przeglądarek w tym systemie. Możesz pobrać ciasteczka z zdalnego URL lub monitorować status przeglądarki:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Otwórz Przeglądarkę</b> - aby monitorować status przeglądarki w mini-aplikacji"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Otwórz Przeglądarkę"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Pobierz ze Zdalnego URL"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Plik ciasteczka YouTube pobrany przez fallback i zapisany jako cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Nie znaleziono obsługiwanych przeglądarek i nie skonfigurowano COOKIE_URL. Użyj /cookie lub prześlij cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL musi wskazywać na plik .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Plik ciasteczka fallback jest zbyt duży (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Źródło ciasteczka fallback niedostępne (status {status}). Spróbuj /cookie lub prześlij cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Błąd pobierania ciasteczka fallback. Spróbuj /cookie lub prześlij cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Nieoczekiwany błąd podczas pobierania ciasteczka fallback."
    BTN_CLOSE = "🔚Zamknij"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Nieprawidłowa wartość logiczna"
    ARGS_CLOSED_MSG = "Zamknięte"
    ARGS_ALL_RESET_MSG = "✅ Wszystkie argumenty zresetowane"
    ARGS_RESET_ERROR_MSG = "❌ Błąd podczas resetowania argumentów"
    ARGS_INVALID_PARAM_MSG = "❌ Nieprawidłowy parametr"
    ARGS_BOOL_SET_MSG = "Ustawiono na {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "Już ustawiono na {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Nieprawidłowa wartość wyboru"
    ARGS_VALUE_SET_MSG = "Ustawiono na {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "Już ustawiono na {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Bieżąca wartość:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Przykłady:</b>\n• <code>default</code> - Użyj domyślnej strategii XFF\n• <code>never</code> - Nigdy nie używaj nagłówka XFF\n• <code>US</code> - Kod kraju Stany Zjednoczone\n• <code>GB</code> - Kod kraju Wielka Brytania\n• <code>DE</code> - Kod kraju Niemcy\n• <code>FR</code> - Kod kraju Francja\n• <code>JP</code> - Kod kraju Japonia\n• <code>192.168.1.0/24</code> - Blok IP (CIDR)\n• <code>10.0.0.0/8</code> - Zakres IP prywatnych\n• <code>203.0.113.0/24</code> - Blok IP publicznych\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Uwaga:</b> To zastępuje opcje --geo-bypass. Użyj dowolnego 2-literowego kodu kraju lub bloku IP w notacji CIDR.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Przykład:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Proszę wysłać nową wartość."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Zakres:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Proszę wysłać liczbę."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Przykłady:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Uwaga:</b> Te nagłówki zostaną dodane do istniejących nagłówków Referer i User-Agent.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Bieżące Argumenty yt-dlp:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - Przełączniki True/False\n• 📋 <b>Select</b> - Wybierz z opcji\n• 🔢 <b>Numeric</b> - Wprowadź liczbę\n• 📝🔧 <b>Text</b> - Wprowadź tekst/JSON</blockquote>\n\nTe ustawienia zostaną zastosowane do wszystkich pobrań."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "Wymuś połączenia IPv6",
        "force_ipv4": "Wymuś połączenia IPv4", 
        "no_live_from_start": "Nie pobieraj strumieni na żywo od początku",
        "live_from_start": "Pobieraj strumienie na żywo od początku",
        "no_check_certificates": "Pomiń walidację certyfikatów HTTPS",
        "check_certificate": "Sprawdź certyfikat SSL",
        "no_playlist": "Pobierz tylko pojedyncze wideo, nie playlistę",
        "embed_metadata": "Osadź metadane w pliku wideo",
        "embed_thumbnail": "Osadź miniaturę w pliku wideo",
        "write_thumbnail": "Zapisz miniaturę do pliku",
        "ignore_errors": "Ignoruj błędy pobierania i kontynuuj",
        "legacy_server_connect": "Zezwól na połączenia z serwerami legacy",
        "concurrent_fragments": "Liczba jednoczesnych fragmentów do pobrania",
        "xff": "Strategia nagłówka X-Forwarded-For",
        "user_agent": "Nagłówek User-Agent",
        "impersonate": "Personifikacja przeglądarki",
        "referer": "Nagłówek Referer",
        "geo_bypass": "Omijaj ograniczenia geograficzne",
        "hls_use_mpegts": "Użyj MPEG-TS dla HLS",
        "no_part": "Nie używaj plików .part",
        "no_continue": "Nie wznawiaj częściowych pobrań",
        "audio_format": "Format audio",
        "video_format": "Format wideo",
        "merge_output_format": "Format wyjściowy scalania",
        "send_as_file": "Wyślij jako plik",
        "username": "Nazwa użytkownika",
        "password": "Hasło",
        "twofactor": "Kod uwierzytelniania dwuskładnikowego",
        "min_filesize": "Minimalny rozmiar pliku (MB)",
        "max_filesize": "Maksymalny rozmiar pliku (MB)",
        "playlist_items": "Elementy playlisty",
        "date": "Data",
        "datebefore": "Data przed",
        "dateafter": "Data po",
        "http_headers": "Nagłówki HTTP",
        "sleep_interval": "Interwał uśpienia",
        "max_sleep_interval": "Maksymalny interwał uśpienia",
        "retries": "Liczba ponownych prób",
        "http_chunk_size": "Rozmiar fragmentu HTTP",
        "sleep_subtitles": "Uśpienie dla napisów"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ Konfiguracja Argumentów yt-dlp</b>\n\n<blockquote>📋 <b>Grupy:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ Konfiguracja Argumentów yt-dlp</b>\n\n"
        "<blockquote>📋 <b>Grupy:</b>\n"
        "• ✅/❌ <b>Boolean</b> - Przełączniki True/False\n"
        "• 📋 <b>Select</b> - Wybierz z opcji\n"
        "• 🔢 <b>Numeric</b> - Wprowadź liczbę\n"
        "• 📝🔧 <b>Text</b> - Wprowadź tekst/JSON</blockquote>\n\n"
        "Te ustawienia zostaną zastosowane do wszystkich pobrań."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Proszę czekać..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Wystąpił błąd"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Tryb wprowadzania automatycznie zamknięty z powodu braku aktywności (5 minut)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Wprowadzenie zawiera potencjalnie niebezpieczną zawartość: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Wprowadzenie zbyt długie (maksymalnie 1000 znaków)"
    ARGS_INVALID_URL_MSG = "❌ Nieprawidłowy format URL. Musi zaczynać się od http:// lub https://"
    ARGS_INVALID_JSON_MSG = "❌ Nieprawidłowy format JSON"
    ARGS_NUMBER_RANGE_MSG = "❌ Liczba musi być między {min_val} a {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Nieprawidłowy format liczby"
    ARGS_DATE_FORMAT_MSG = "❌ Data musi być w formacie YYYYMMDD (np. 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Rok musi być między 1900 a 2100"
    ARGS_MONTH_RANGE_MSG = "❌ Miesiąc musi być między 01 a 12"
    ARGS_DAY_RANGE_MSG = "❌ Dzień musi być między 01 a 31"
    ARGS_INVALID_DATE_MSG = "❌ Nieprawidłowy format daty"
    ARGS_INVALID_XFF_MSG = "❌ XFF musi być 'default', 'never', kod kraju (np. US) lub blok IP (np. 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "Nie ustawiono niestandardowych argumentów. Wszystkie parametry używają wartości domyślnych."
    ARGS_RESET_SUCCESS_MSG = "✅ Wszystkie argumenty zresetowane do domyślnych."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Tekst zbyt długi. Maksymalnie 500 znaków."
    ARGS_ERROR_PROCESSING_MSG = "❌ Błąd przetwarzania danych wejściowych. Spróbuj ponownie."
    ARGS_BOOL_INPUT_MSG = "❌ Wprowadź 'True' lub 'False' dla opcji Wyślij jako plik."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Podaj prawidłową liczbę."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Wyślij <code>True</code> lub <code>False</code> aby włączyć/wyłączyć tę opcję."
    ARGS_JSON_VALUE_REQUEST_MSG = "Wyślij prawidłowy JSON."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Nie masz jeszcze tagów."
    TAGS_MESSAGE_CLOSED_MSG = "Wiadomość tagów zamknięta."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Napisy wyłączone i tryb Always Ask wyłączony."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Always Ask włączony."
    SUBS_LANGUAGE_SET_MSG = "✅ Język napisów ustawiony na: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️OSTRZEŻENIE: z powodu wysokiego obciążenia CPU ta funkcja jest bardzo wolna (blisko czasu rzeczywistego) i ograniczona do:\n"
        "- maksymalna jakość 720p\n"
        "- maksymalny czas trwania 1.5 godziny\n"
        "- maksymalny rozmiar wideo 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Szybkie polecenia:</b>\n"
        "• <code>/subs off</code> - wyłącz napisy\n"
        "• <code>/subs on</code> - włącz tryb Always Ask\n"
        "• <code>/subs ru</code> - ustaw język\n"
        "• <code>/subs ru auto</code> - ustaw język z AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Napisy są wyłączone"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Wybrany język: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Pobieranie napisów..."
    SUBS_DISABLED_ERROR_MSG = "❌ Napisy są wyłączone. Użyj /subs aby skonfigurować."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Pobieranie napisów jest obsługiwane tylko dla YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Subtitles</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Language:</b> {lang}\n"
        "<b>Type:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Plik napisów SRT wysłany do użytkownika."
    SUBS_ERROR_PROCESSING_MSG = "❌ Błąd przetwarzania pliku napisów."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Nie udało się pobrać napisów."
    SUBS_ERROR_MSG = "❌ Błąd pobierania napisów: {error}"
    
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
    SPLIT_MENU_CLOSED_MSG = "Menu zamknięte."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Ustawienia bota</b>\n\nWybierz kategorię:"
    SETTINGS_MENU_CLOSED_MSG = "Menu zamknięte."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Opcje czyszczenia</b>\n\nWybierz, co wyczyścić:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIE</b>\n\nWybierz akcję:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIA</b>\n\nWybierz akcję:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nWybierz akcję:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ WIĘCEJ POLECEŃ</b>\n\nWybierz akcję:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Polecenie wykonane."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Limit powodziowy. Spróbuj później."
    SETTINGS_HINT_SENT_MSG = "Podpowiedź wysłana."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Pomocnik wyszukiwania otwarty."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Nieznane polecenie."
    SETTINGS_HINT_CLOSED_MSG = "Podpowiedź zamknięta."
    SETTINGS_HELP_SENT_MSG = "Wysłano plik pomocy txt do użytkownika"
    SETTINGS_MENU_OPENED_MSG = "Otworzono menu /settings"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Pomocnik wyszukiwania zamknięty"
    SEARCH_CLOSED_MSG = "Zamknięte"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proxy {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Błąd podczas zapisywania ustawień proxy."
    PROXY_MENU_TEXT_MSG = "Włączyć czy wyłączyć używanie serwera proxy dla wszystkich operacji yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Włączyć lub wyłączyć korzystanie z serwerów proxy (dostępne {config_count} + {file_count}) dla wszystkich operacji yt-dlp?\n\nPo włączeniu WSZYSTKIE (AUTO) proxy będą wybierane metodą losową."
    PROXY_MENU_CLOSED_MSG = "Menu zamknięte."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy włączone. Wszystkie operacje yt-dlp będą używać proxy."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy włączone. Wszystkie operacje yt-dlp będą używać {count} serwerów proxy z metodą wyboru {method}."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Włączono serwer proxy (tryb ALL AUTO).\n\n📊 Bot będzie próbował proxy w następującej kolejności:\n1️⃣ {config_count} serwerów proxy z Config.py\n2️⃣ {file_count} proxy z pliku TXT/proxy.txt\n\n🔄 Wszystkie serwery proxy będą wypróbowywane sekwencyjnie, aż do pomyślnego połączenia."
    PROXY_DISABLED_MSG = "❌ Proxy wyłączone."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Błąd podczas zapisywania ustawień proxy."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy włączone."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy wyłączone."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ POCZEKAJ, AŻ TWOJE POPRZEDNIE POBRANIE SIĘ ZAKOŃCZY"
    AUDIO_HELP_MSG = (
        "<b>🎧 Polecenie pobierania audio</b>\n\n"
        "Użycie: <code>/audio URL</code>\n\n"
        "<b>Przykłady:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Zobacz także: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Podpowiedź audio zamknięta."
    PLAYLIST_HELP_CLOSED_MSG = "Pomoc playlisty zamknięta."
    USERLOGS_CLOSED_MSG = "Wiadomość logów zamknięta."
    HELP_CLOSED_MSG = "Pomoc zamknięta."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>Ustawienia rozmycia NSFW</b>\n\nTreść NSFW jest <b>{status}</b>.\n\nWybierz, czy rozmyć treść NSFW:"
    NSFW_MENU_CLOSED_MSG = "Menu zamknięte."
    NSFW_BLUR_DISABLED_MSG = "Rozmycie NSFW wyłączone."
    NSFW_BLUR_ENABLED_MSG = "Rozmycie NSFW włączone."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Rozmycie NSFW wyłączone."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Rozmycie NSFW włączone."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Włączyć czy wyłączyć wysyłanie MediaInfo dla pobranych plików?"
    MEDIAINFO_MENU_CLOSED_MSG = "Menu zamknięte."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo włączone. Po pobraniu informacje o pliku zostaną wysłane."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo wyłączone."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo włączone."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo wyłączone."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Lista dostępnych formatów</b>\n\n"
        "Pobierz dostępne formaty wideo/audio dla URL.\n\n"
        "<b>Użycie:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Przykłady:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Jak używać ID formatów:</b>\n"
        "Po otrzymaniu listy użyj konkretnego ID formatu:\n"
        "• <code>/format id 401</code> - pobierz format 401\n"
        "• <code>/format id401</code> - to samo co powyżej\n"
        "• <code>/format id140 audio</code> - pobierz format 140 jako audio MP3\n\n"
        "To polecenie pokaże wszystkie dostępne formaty, które można pobrać."
    )
    LIST_PROCESSING_MSG = "🔄 Pobieranie dostępnych formatów..."
    LIST_INVALID_URL_MSG = "❌ Podaj prawidłowy URL zaczynający się od http:// lub https://"
    LIST_CAPTION_MSG = (
        "📃 Dostępne formaty dla:\n<code>{url}</code>\n\n"
        "💡 <b>Jak ustawić format:</b>\n"
        "• <code>/format id 134</code> - Pobierz konkretny ID formatu\n"
        "• <code>/format 720p</code> - Pobierz według jakości\n"
        "• <code>/format best</code> - Pobierz najlepszą jakość\n"
        "• <code>/format ask</code> - Zawsze pytaj o jakość\n\n"
        "{audio_note}\n"
        "📋 Użyj ID formatu z listy powyżej"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Formaty tylko audio:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Pobierz format 140 jako audio MP3\n"
        "• <code>/format id140 audio</code> - to samo co powyżej\n"
        "Te będą pobrane jako pliki audio MP3.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Błąd wysyłania pliku formatów: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Nie udało się pobrać formatów:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Wystąpił błąd podczas przetwarzania polecenia"
    LIST_ERROR_CALLBACK_MSG = "Wystąpił błąd"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Jak używać ID formatów:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Po otrzymaniu listy użyj konkretnego ID formatu:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - pobierz format 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - to samo co powyżej\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - pobierz format 140 jako audio MP3\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - to samo co powyżej\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Wykryto formaty tylko audio: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Te formaty będą pobrane jako pliki audio MP3.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Formaty tylko wideo:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Użyj ID formatu z listy powyżej"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Użycie:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>Przykłady:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - najlepsza jakość\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p lub niższa\n"
        "• /link 720p https://youtube.com/watch?v=... - to samo co powyżej\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K lub niższa\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K lub niższa"
        "</blockquote>\n\n"
        "<b>Jakość:</b> od 1 do 10000 (np. 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Podaj prawidłowy URL"
    LINK_PROCESSING_MSG = "🔗 Pobieranie bezpośredniego linku..."
    LINK_DURATION_MSG = "⏱ <b>Czas trwania:</b> {duration} sek\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Strumień wideo:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Strumień audio:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Ustawienie klawiatury zaktualizowane!**\n\nNowe ustawienie: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Nieprawidłowy argument!**\n\n"
        "Prawidłowe opcje: `off`, `1x3`, `2x3`, `full`\n\n"
        "Przykład: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Ustawienia klawiatury**\n\n"
        "Aktualne: **{current}**\n\n"
        "Wybierz opcję:\n\n"
        "Lub użyj: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 klawiatura aktywowana!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Klawiatura ukryta"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 Klawiatura 1x3 aktywowana!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 Klawiatura 2x3 aktywowana!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Klawiatura emoji aktywowana!"
    KEYBOARD_ERROR_APPLYING_MSG = "Błąd podczas stosowania ustawienia klawiatury {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Format ustawiony na: Always Ask. Będziesz pytany o jakość za każdym razem gdy wyślesz URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format ustawiony na: Always Ask. Teraz będziesz pytany o jakość za każdym razem gdy wyślesz URL."
    FORMAT_BEST_UPDATED_MSG = "✅ Format zaktualizowany do najlepszej jakości (priorytet AVC+MP4):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Format zaktualizowany do ID {id}:\n{format}\n\n💡 <b>Uwaga:</b> Jeśli to jest format tylko audio, zostanie pobrany jako plik audio MP3."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Format zaktualizowany do ID {id} (tylko audio):\n{format}\n\n💡 To zostanie pobrane jako plik audio MP3."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Format zaktualizowany do jakości {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Format zaktualizowany do:\n{format}"
    FORMAT_MENU_MSG = (
        "Wybierz opcję formatu lub wyślij niestandardową używając:\n"
        "• <code>/format &lt;format_string&gt;</code> - niestandardowy format\n"
        "• <code>/format 720</code> - jakość 720p\n"
        "• <code>/format 4k</code> - jakość 4K\n"
        "• <code>/format 8k</code> - jakość 8K\n"
        "• <code>/format id 401</code> - konkretne ID formatu\n"
        "• <code>/format ask</code> - zawsze pokazuj menu\n"
        "• <code>/format best</code> - bv+ba/najlepsza jakość"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Aby użyć niestandardowego formatu, wyślij polecenie w następującej formie:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Zastąp <code>bestvideo+bestaudio/best</code> własnym ciągiem formatu."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Wybierz żądaną rozdzielczość i kodek:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format ustawiony na: Always Ask. Teraz będziesz pytany o jakość za każdym razem gdy wyślesz URL."
    FORMAT_UPDATED_MSG = "✅ Format zaktualizowany do:\n{format}"
    FORMAT_SAVED_MSG = "✅ Format zapisany."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Wybór formatu zaktualizowany."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Menu niestandardowego formatu zamknięte"
    FORMAT_CODEC_SET_MSG = "✅ Kodek ustawiony na {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Wybór przeglądarki zaktualizowany."
    
    # Clean command messages
    
    # Admin command messages
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format ustawiony na: Always Ask. Teraz będziesz pytany o jakość za każdym razem gdy wyślesz URL."
    FORMAT_UPDATED_MSG = "✅ Format zaktualizowany do:\n{format}"
    FORMAT_SAVED_MSG = "✅ Format zapisany."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Wybór formatu zaktualizowany."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Menu niestandardowego formatu zamknięte"
    FORMAT_CODEC_SET_MSG = "✅ Kodek ustawiony na {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Wybór przeglądarki zaktualizowany."
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Błąd podczas przeładowywania pamięci podręcznej NSFW: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Podaj URL do sprawdzenia.\nUżycie: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Podaj prawidłowy URL.\nUżycie: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Sprawdzanie URL pod kątem treści NSFW...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Wynik sprawdzenia NSFW</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Status:</b> <b>{status_text}</b>\n\n"
        "<b>Wyjaśnienie:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Błąd podczas sprawdzania URL: {error}"
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Użycie: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Administrator nie może usunąć administratora"
    ADMIN_USER_BLOCKED_MSG = "Użytkownik zablokowany 🔒❌\n \nID: <code>{user_id}</code>\nData blokady: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> jest już zablokowany ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Przepraszam! Nie jesteś administratorem"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Użycie: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Użytkownik odblokowany 🔓✅\n \nID: <code>{user_id}</code>\nData odblokowania: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> jest już odblokowany ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Odblokowani użytkownicy: {count}\n⏱ Znacznik czasu: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Użycie: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Użytkownik zignorowany 👁️❌\n \nID: <code>{user_id}</code>\nData ignorowania: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> jest już ignorowany ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Użycie: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Użytkownik nie jest już ignorowany 👁️✅\n \nID: <code>{user_id}</code>\nData zaprzestania ignorowania: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> nie jest ignorowany ✅😐"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Ciasteczka wyczyszczone."
    CLEAN_LOGS_CLEANED_MSG = "Logi wyczyszczone."
    CLEAN_TAGS_CLEANED_MSG = "Tagi wyczyszczone."
    CLEAN_FORMAT_CLEANED_MSG = "Format wyczyszczony."
    CLEAN_SPLIT_CLEANED_MSG = "Podział wyczyszczony."
    CLEAN_MEDIAINFO_CLEANED_MSG = "Mediainfo wyczyszczone."
    CLEAN_SUBS_CLEANED_MSG = "Ustawienia napisów wyczyszczone."
    CLEAN_KEYBOARD_CLEANED_MSG = "Ustawienia klawiatury wyczyszczone."
    CLEAN_ARGS_CLEANED_MSG = "Ustawienia argumentów wyczyszczone."
    CLEAN_NSFW_CLEANED_MSG = "Ustawienia NSFW wyczyszczone."
    CLEAN_PROXY_CLEANED_MSG = "Ustawienia proxy wyczyszczone."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Ustawienia limitów wyczyszczone."
    CLEAN_ALL_CLEANED_MSG = "Wszystkie pliki wyczyszczone."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 CIASTECZKA</b>\n\nWybierz akcję:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Plik cookie zapisany"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Pominięto walidację dla plików cookie innych niż YouTube"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Plik cookie istnieje, ale ma nieprawidłowy format"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Plik cookie nie został znaleziony."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Rozpoczynam test plików cookie YouTube...\n\nProszę czekać, sprawdzam i walidację Twoje pliki cookie."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Twoje istniejące pliki cookie YouTube działają prawidłowo!\n\nNie ma potrzeby pobierania nowych."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Twoje istniejące pliki cookie YouTube są wygasłe lub nieprawidłowe.\n\n🔄 Pobieranie nowych plików cookie..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ Źródło cookie {service} nie jest skonfigurowane!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ Źródło cookie {service} musi być plikiem .txt!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Przekroczono limit zakresu: żądano {range_count} plików (maksymalnie {max_img_files}).\n\nUżyj jednego z tych poleceń, aby pobrać maksymalną liczbę dostępnych plików:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Zamknij"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Przekroczono limit mediów: żądano {count} plików (maksymalnie {max_count}).\n\nUżyj jednego z tych poleceń, aby pobrać maksymalną liczbę dostępnych plików:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Znaleziono <b>{count}</b> elementów multimedialnych z linku"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Wybierz zakres pobierania:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Podszywanie się pod przeglądarkę"
    ARGS_REFERER_DESC_MSG = "Nagłówek Referer"
    ARGS_USER_AGENT_DESC_MSG = "Nagłówek User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "Obejście ograniczeń geograficznych"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Sprawdź certyfikat SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "Pobierz transmisje na żywo od początku"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Nie pobieraj transmisji na żywo od początku"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Użyj kontenera MPEG-TS dla filmów HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "Pobierz tylko pojedynczy film, nie listę odtwarzania"
    ARGS_NO_PART_DESC_MSG = "Nie używaj plików .part"
    ARGS_NO_CONTINUE_DESC_MSG = "Nie wznawiaj częściowych pobrań"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Format audio do ekstrakcji"
    ARGS_EMBED_METADATA_DESC_MSG = "Osadź metadane w pliku wideo"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Osadź miniaturę w pliku wideo"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Zapisz miniaturę do pliku"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Liczba równoczesnych fragmentów do pobrania"
    ARGS_FORCE_IPV4_DESC_MSG = "Wymuś połączenia IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "Wymuś połączenia IPv6"
    ARGS_XFF_DESC_MSG = "Strategia nagłówka X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "Rozmiar fragmentu HTTP (bajty)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Opóźnienie przed pobraniem napisów (sekundy)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Zezwól na starsze połączenia serwerowe"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Wyłącz walidację certyfikatu HTTPS"
    ARGS_USERNAME_DESC_MSG = "Nazwa użytkownika konta"
    ARGS_PASSWORD_DESC_MSG = "Hasło konta"
    ARGS_TWOFACTOR_DESC_MSG = "Kod uwierzytelniania dwuskładnikowego"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Ignoruj błędy pobierania i kontynuuj"
    ARGS_MIN_FILESIZE_DESC_MSG = "Minimalny rozmiar pliku (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Maksymalny rozmiar pliku (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Elementy listy odtwarzania do pobrania (np. 1,3,5 lub 1-5)"
    ARGS_DATE_DESC_MSG = "Pobierz filmy przesłane w tej dacie (RRRRMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Pobierz filmy przesłane przed tą datą (RRRRMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Pobierz filmy przesłane po tej dacie (RRRRMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Niestandardowe nagłówki HTTP (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Interwał opóźnienia między żądaniami (sekundy)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Maksymalny interwał opóźnienia (sekundy)"
    ARGS_RETRIES_DESC_MSG = "Liczba ponownych prób"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Format kontenera wideo"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Format kontenera wyjściowego do scalania"
    ARGS_SEND_AS_FILE_DESC_MSG = "Wyślij wszystkie multimedia jako dokument zamiast multimediów"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Podszywanie"
    ARGS_REFERER_SHORT_MSG = "Referer"
    ARGS_GEO_BYPASS_SHORT_MSG = "Obejście Geo"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Sprawdź Cert"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Start na żywo"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Brak startu na żywo"
    ARGS_USER_AGENT_SHORT_MSG = "User Agent"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Brak listy odtwarzania"
    ARGS_NO_PART_SHORT_MSG = "Bez Part"
    ARGS_NO_CONTINUE_SHORT_MSG = "Bez kontynuacji"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Format audio"
    ARGS_EMBED_METADATA_SHORT_MSG = "Osadź meta"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Osadź miniaturę"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Zapisz miniaturę"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Równoczesne"
    ARGS_FORCE_IPV4_SHORT_MSG = "Wymuś IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Wymuś IPv6"
    ARGS_XFF_SHORT_MSG = "Nagłówek XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Rozmiar fragmentu"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Opóźnienie napisów"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Starsze połączenie"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Bez sprawdzania Cert"
    ARGS_USERNAME_SHORT_MSG = "Nazwa użytkownika"
    ARGS_PASSWORD_SHORT_MSG = "Hasło"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Ignoruj błędy"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Min rozmiar"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Max rozmiar"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Elementy listy odtwarzania"
    ARGS_DATE_SHORT_MSG = "Data"
    ARGS_DATEBEFORE_SHORT_MSG = "Data przed"
    ARGS_DATEAFTER_SHORT_MSG = "Data po"
    ARGS_HTTP_HEADERS_SHORT_MSG = "Nagłówki HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Interwał opóźnienia"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Max opóźnienie"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Format wideo"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Format scalania"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Wyślij jako plik"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ Plik jest za duży. Maksymalny rozmiar to 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Dozwolone są tylko pliki w formacie .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ Plik nie wygląda jak cookie.txt (brak linii '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ Błąd odczytu pliku: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Plik cookie istnieje i ma prawidłowy format"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ Plik cookie {service} jest za duży! Maksymalnie 100KB, otrzymano {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ Plik cookie {service} został pobrany i zapisany jako cookie.txt w Twoim folderze.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ Źródło cookie {service} jest niedostępne (status {status}). Spróbuj ponownie później."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Błąd pobierania pliku cookie {service}. Spróbuj ponownie później."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Użytkownik dostarczył nowy plik cookie.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie pomyślnie zaktualizowane:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Nieprawidłowe cookie.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ Źródła cookie YouTube nie są skonfigurowane!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Pobieranie i sprawdzanie cookie YouTube...\n\nPróba {attempt} z {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Brak dostępu. Tylko administrator."
    ADMIN_USER_LOGS_TOTAL_MSG = "Łącznie: <b>{total}</b>\n<b>{user_id}</b> - logi (Ostatnie 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 keyboard activated!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Język napisów ustawiony na: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Język napisów ustawiony na: {flag} {name} z włączonym AUTO/TRANS."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Menu języka napisów zamknięte."
    SUBS_DOWNLOADING_MSG = "💬 Pobieranie napisów..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Przeładowywanie cache Firebase do pamięci..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Nie skonfigurowano COOKIE_URL. Użyj /cookie lub prześlij cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Pobieranie cookies z zdalnego URL..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Zapasowy COOKIE_URL musi wskazywać na plik .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Zapasowy plik cookie jest zbyt duży (>100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Plik cookie YouTube pobrany przez zapasowe źródło i zapisany jako cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Zapasowe źródło cookie niedostępne (status {status}). Spróbuj /cookie lub prześlij cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Błąd podczas pobierania zapasowego cookie. Spróbuj /cookie lub prześlij cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Nieoczekiwany błąd podczas pobierania zapasowego cookie."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ Przeglądarka {browser} nie jest zainstalowana."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookies zapisane przy użyciu przeglądarki: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Nie udało się zapisać cookies: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ Cookies YouTube działają poprawnie"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ Cookies YouTube wygasły lub są nieprawidłowe\n\nUżyj /cookie, aby uzyskać nowe cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - format niestandardowy\n• <code>/format 720</code> - jakość 720p\n• <code>/format 4k</code> - jakość 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Wysłano podpowiedź."
    FORMAT_MKV_TOGGLE_MSG = "MKV jest teraz {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Nie skonfigurowano zdalnego URL"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Nieprawidłowy format pliku"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Plik zbyt duży"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookies pobrane pomyślnie"
    COOKIES_SERVER_ERROR_MSG = "❌ Błąd serwera {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Pobieranie nie powiodło się"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Nieoczekiwany błąd"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Przeglądarka nie jest zainstalowana."
    COOKIES_MENU_CLOSED_MSG = "Menu zamknięte."
    COOKIES_HINT_CLOSED_MSG = "Podpowiedź cookie zamknięta."
    IMG_HELP_CLOSED_MSG = "Pomoc zamknięta."
    SUBS_LANGUAGE_UPDATED_MSG = "Ustawienia języka napisów zaktualizowane."
    SUBS_MENU_CLOSED_MSG = "Menu języka napisów zamknięte."
    KEYBOARD_SET_TO_MSG = "Klawiatura ustawiona na {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Błąd podczas przetwarzania ustawienia"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo włączone."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo wyłączone."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Rozmycie NSFW wyłączone."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Rozmycie NSFW włączone."
    SETTINGS_MENU_CLOSED_MSG = "Menu zamknięte."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Flood wait aktywny. Spróbuj później."
    OTHER_HELP_CLOSED_MSG = "Pomoc zamknięta."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Wiadomość z logami zamknięta."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menu zamknięte."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Nieprawidłowy rozmiar."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Błąd podczas wysyłania MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Wystąpił błąd: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - wszystkie logi"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - wszystkie {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Pobierz ze zdalnego URL"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Otwórz przeglądarkę"
    SELECT_BROWSER_MSG = "Wybierz przeglądarkę, z której pobrać cookies:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Nie znaleziono przeglądarek w tym systemie. Możesz pobrać cookies ze zdalnego URL lub monitorować status przeglądarki:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Otwórz przeglądarkę</b> - aby monitorować status przeglądarki w mini-aplikacji"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Nie udało się uruchomić /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Limit flood. Spróbuj później."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Nie udało się otworzyć menu cookie przeglądarki"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Podpowiedź 'Zapisz jako cookie' zamknięta."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Użycie:</b>\n<code>/link [jakość] URL</code>\n\n<b>Przykłady:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - najlepsza jakość\n• /link 720 https://youtube.com/watch?v=... - 720p lub niższa\n• /link 720p https://youtube.com/watch?v=... - jak powyżej\n• /link 4k https://youtube.com/watch?v=... - 4K lub niższa\n• /link 8k https://youtube.com/watch?v=... - 8K lub niższa</blockquote>\n\n<b>Jakość:</b> od 1 do 10000 (np. 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - jakość 8K"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Uzyskano bezpośredni link</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Strumień audio:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Nie udało się pobrać linków do strumieni"
    LINK_ERROR_GETTING_MSG = "❌ <b>Błąd pobierania linku:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Nieprawidłowy indeks cookie YouTube: {selected_index}. Dostępny zakres to 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Pobieranie i sprawdzanie cookies YouTube...\n\nPróba {attempt} z {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Pobieranie i sprawdzanie cookies YouTube...\n\nPróba {attempt} z {total}\n🔍 Testowanie cookies..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ Cookies YouTube pomyślnie pobrane i zweryfikowane!\n\nUżyto źródła {source} z {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Wszystkie cookies YouTube wygasły lub są niedostępne!\n\nSkontaktuj się z administratorem bota, aby je zastąpić."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ Przekroczono limit ponownych prób cookie YouTube!\n\n🔢 Maksimum: {limit} prób na godzinę\n⏰ Spróbuj ponownie później"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Tag #{wrong} zawiera niedozwolone znaki. Dozwolone są tylko litery, cyfry i _.\nUżyj: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Nieprawidłowy argument!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Ustawiono język napisów: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Przykład: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Wybrany język: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Tryb Always Ask {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Napisy są wyłączone"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Ustawienia napisów</b>\n\n{status_text}\n\nWybierz język napisów:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - wyłącz napisy\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Ustawienia napisów</b>\n\n{status_text}\n\nWybierz język napisów:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Tytuł:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Czas trwania:</b> {duration} sek\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Strumień wideo:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- maksymalna jakość 720p\n- maksymalny czas trwania 1,5 godziny\n- maksymalny rozmiar wideo 500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️OSTRZEŻENIE: ze względu na duże obciążenie CPU ta funkcja jest bardzo wolna (blisko czasu rzeczywistego) i ograniczona do:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Szybkie polecenia:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - wyłącz napisy\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - włącz tryb Always Ask\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - ustaw język\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - ustaw język z włączonym AUTO/TRANS\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - włącz tryb Always Ask\n"
    SUBS_AUTO_SUBS_TEXT = " (auto-napisy)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Tryb auto-napisów {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "NAPISY wyłączone przez polecenie: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "NAPISY Always Ask włączone przez polecenie: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "Język NAPISÓW ustawiony przez polecenie: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "Język NAPISÓW + tryb auto ustawiony przez polecenie: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Użytkownik otworzył menu /subs."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Użytkownik ustawił język napisów na: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Użytkownik przełączył tryb AUTO/TRANS na: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Użytkownik przełączył tryb Always Ask na: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Użytkownik poprosił o cookies z przeglądarki."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Wysłano klawiaturę wyboru przeglądarki tylko z zainstalowanymi przeglądarkami."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Wybór przeglądarki zamknięty."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "Zapasowy COOKIE_URL użyty pomyślnie (źródło ukryte)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "Zapasowy COOKIE_URL nie powiódł się: status={status} (ukryte)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Zapasowy COOKIE_URL nieoczekiwany błąd: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Przeglądarka {browser} nie jest zainstalowana."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Cookies zapisane przy użyciu przeglądarki: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "Plik cookie zapisany dla użytkownika {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "Plik cookie istnieje, ma poprawny format i cookies YouTube działają."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Plik cookie istnieje i ma poprawny format, ale cookies YouTube wygasły."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Plik cookie istnieje i ma poprawny format."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Plik cookie istnieje, ale ma niepoprawny format."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Plik cookie nie znaleziony."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "URL cookie {service} jest pusty dla użytkownika {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "URL cookie {service} nie jest .txt (ukryte)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "Plik cookie {service} zbyt duży: {size} bajtów (źródło ukryte)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "Plik cookie {service} pobrany dla użytkownika {user_id} (źródło ukryte)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Skrypt nie znaleziony: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Nie udało się wysłać początkowego komunikatu o statusie"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Błąd podczas uruchamiania {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Cache Firebase przeładowany przez zadanie automatyczne."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Cache Firebase przeładowany przez administratora."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Błąd podczas przeładowywania cache Firebase: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Rozpoczęto transmisję. Tekst:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Wiadomość transmisji wysłana do wszystkich użytkowników."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Nie udało się wysłać wiadomości transmisji: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Administrator {user_id} wyczyścił cache dla URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Administrator {user_id} rozpoczął skrypt aktualizacji listy pornograficznej: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Skrypt aktualizacji listy pornograficznej zakończony pomyślnie przez administratora {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Skrypt aktualizacji listy pornograficznej nie powiódł się przez administratora {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Administrator {user_id} próbował uruchomić nieistniejący skrypt: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Błąd podczas uruchamiania skryptu aktualizacji pornograficznej przez administratora {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Administrator {user_id} rozpoczął przeładowywanie cache pornograficznego"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Błąd podczas przeładowywania cache pornograficznego przez administratora {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Administrator {user_id} sprawdził URL pod kątem NSFW: {url} - Wynik: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "Użytkownik poprosił o zmianę formatu."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "Format ustawiony na ALWAYS_ASK."
    FORMAT_UPDATED_BEST_LOG_MSG = "Format zaktualizowany na najlepszy: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "Format zaktualizowany na ID {format_id}: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "Format zaktualizowany na ID {format_id} (tylko audio): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "Format zaktualizowany na jakość {quality}: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "Format zaktualizowany na: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "Menu formatu wysłane."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "Wybór formatu zamknięty."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "Podpowiedź formatu niestandardowego wysłana."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "Menu rozdzielczości formatu wysłane."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "Powrót do głównego menu formatu."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "Format zaktualizowany na: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "Format ustawiony na ALWAYS_ASK."
    FORMAT_CODEC_SET_LOG_MSG = "Preferencja kodeka ustawiona na {codec}"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Menu formatu niestandardowego zamknięte"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "Bezpośredni link wyodrębniony dla użytkownika {user_id} z {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Nie udało się wyodrębnić bezpośredniego linku dla użytkownika {user_id} z {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Błąd w poleceniu linku dla użytkownika {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Użytkownik {user_id} ustawił klawiaturę na {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Użytkownik {user_id} ustawił klawiaturę na {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo ustawione przez polecenie: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Użytkownik otworzył menu /mediainfo."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: zamknięte."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo włączone."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo wyłączone."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Rozmiar podziału ustawiony na {size} bajtów przez argument."
    SPLIT_MENU_OPENED_LOG_MSG = "Użytkownik otworzył menu /split."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Wybór podziału zamknięty."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Rozmiar podziału ustawiony na {size} bajtów."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Proxy ustawione przez polecenie: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Użytkownik otworzył menu /proxy."
    PROXY_MENU_CLOSED_LOG_MSG = "Proxy: zamknięte."
    PROXY_ENABLED_LOG_MSG = "Proxy włączone."
    PROXY_DISABLED_LOG_MSG = "Proxy wyłączone."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Wiadomość pomocy zamknięta."
    AUDIO_HELP_SHOWN_LOG_MSG = "Pokazano pomoc /audio"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Użytkownik poprosił o pomoc dotyczącą listy odtwarzania."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Pomoc dotycząca listy odtwarzania zamknięta."
    AUDIO_HINT_CLOSED_LOG_MSG = "Podpowiedź audio zamknięta."
    
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
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Zamknij"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼KODEK"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBBING"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 NAPISY"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Przeglądarka"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Uzyskiwanie bezpośredniego linku..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Uzyskiwanie dostępnych formatów..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Uzyskiwanie opisu wideo..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Błąd podczas uzyskiwania opisu: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Opis wideo nie jest dostępny"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Błąd podczas wysyłania opisu: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Opis wideo wysłany do użytkownika {user_id} dla {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Uruchamianie gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Czas trwania:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Przeglądarka:</b> Otwórz w przeglądarce internetowej"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Dostępne formaty dla"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Jak używać ID formatów:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Po otrzymaniu listy użyj konkretnego ID formatu:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - pobierz format 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - to samo co powyżej"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - pobierz format 140 jako audio MP3"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Wykryto formaty tylko audio"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Te formaty będą pobrane jako pliki audio MP3."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Jak ustawić format:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Pobierz konkretne ID formatu"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Pobierz według jakości"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Pobierz najlepszą jakość"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Zawsze pytaj o jakość"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Formaty tylko audio:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Pobierz format 140 jako audio MP3"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Te będą pobrane jako pliki audio MP3."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Użyj ID formatu z listy powyżej"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Błąd: Oryginalna wiadomość nie znaleziona."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Strona formatów"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Błąd podczas wyświetlania menu formatów"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Błąd podczas uzyskiwania formatów"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Błąd podczas uzyskiwania dostępnych formatów."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Spróbuj ponownie później."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp nie może przetworzyć tej zawartości"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "System zaleca użycie gallery-dl zamiast tego."
    ALWAYS_ASK_OPTIONS_MSG = "**Opcje:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Dla galerii obrazów: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Dla pojedynczych obrazów: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl często działa lepiej dla Instagram, Twitter i innych treści z mediów społecznościowych."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Spróbuj Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Format ustalony przez /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Napisy"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Zdubbingowane audio"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Napisy są dostępne"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Wybierz język napisów"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Napisy nie znalezione i nie zostaną osadzone"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Natychmiastowy repost z cache"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Wybierz język audio"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW jest płatne (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Wybierz jakość pobierania"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Pobierz obraz (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Obejrzyj wideo w poketube"  # TYMCZASOWO WYŁĄCZONE: usługa poketube nie działa
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Uzyskaj bezpośredni link do wideo"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Pokaż listę dostępnych formatów"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Zmień rozszerzenie/kodek wideo"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Osadź"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Wyodrębnij tylko audio"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW jest płatne (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Natychmiastowy repost z cache"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Obejrzyj wideo w poketube"  # TYMCZASOWO WYŁĄCZONE: usługa poketube nie działa
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Wybierz język audio"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Najlepsze"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Inne"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝tylko napisy"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Inteligentne grupowanie"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Dodano wiersz przycisków akcji (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Dodano wiersze przycisków akcji (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Dodano dolne przyciski do istniejącego wiersza"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Utworzono nowy dolny wiersz"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Nie znaleziono wideo w liście odtwarzania"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "Nieobsługiwany URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Nie można znaleźć wideo"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Nie znaleziono wideo"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Nie znaleziono mediów"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Ten tweet nie zawiera"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Błąd podczas pobierania informacji o wideo:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Błąd podczas pobierania informacji o wideo"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Spróbuj polecenia <code>/clean</code> i spróbuj ponownie. Jeśli błąd się utrzymuje, YouTube wymaga autoryzacji. Zaktualizuj cookies.txt przez <code>/cookie</code> lub <code>/cookies_from_browser</code> i spróbuj ponownie."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Menu zamknięte."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Ręczny wybór jakości"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Wybierz jakość ręcznie, ponieważ automatyczne wykrywanie nie powiodło się:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Wszystkie dostępne formaty"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Dostępne jakości (z cache)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Używanie jakości z cache - nowe formaty mogą nie być dostępne"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Pobieranie formatu"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Pobieranie"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Pobieranie ze śledzeniem postępu..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Pobieranie przy użyciu formatu:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Pobieranie audio przy użyciu formatu:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Pobieranie najlepszej jakości..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Pobieranie zrzutu bazy danych..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Pobieranie"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Strona formatów"
    ALWAYS_ASK_FROM_CACHE_MSG = "(z cache)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Błąd: Oryginalna wiadomość nie znaleziona. Może zostać usunięta. Wyślij link ponownie."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Błąd: Oryginalny URL nie znaleziony. Wyślij link ponownie."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Uzyskano bezpośredni link</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Tytuł:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Czas trwania:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Strumień wideo:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Strumień audio:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Nie udało się uzyskać linków do strumieni"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Bezpośredni link wyodrębniony przez menu Always Ask dla użytkownika {user_id} z {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Nie udało się wyodrębnić bezpośredniego linku przez menu Always Ask dla użytkownika {user_id} z {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Bezpośredni link wyodrębniony przez down_and_up_with_format dla użytkownika {user_id} z {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Nie udało się wyodrębnić bezpośredniego linku przez down_and_up_with_format dla użytkownika {user_id} z {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Bezpośredni link wyodrębniony przez down_and_audio dla użytkownika {user_id} z {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Nie udało się wyodrębnić bezpośredniego linku przez down_and_audio dla użytkownika {user_id} z {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Audio wysłane z cache."
    AUDIO_PROCESSING_MSG = "🎙️ Audio jest przetwarzane..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Pobieranie audio:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Wystąpił błąd podczas pobierania audio."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Nie udało się wyodrębnić informacji o audio"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Pomijanie nieobsługiwanego typu pliku w liście odtwarzania pod indeksem {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "Plik audio nie znaleziony po pobraniu."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ Nie udało się wysłać audio: Rozmiar pliku wynosi 0 B (indeks listy odtwarzania {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ Plik audio jest nadal pobierany, proszę czekać..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Wysyłanie pliku audio...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Nie udało się wysłać audio: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Audio z listy odtwarzania wysłane: {sent}/{total} plików (jakość={quality}) do użytkownika {user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Nie udało się pobrać audio: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Pobieranie anulowane z powodu przekroczenia czasu (2 godziny)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Plik wideo nie znaleziony: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ Nie udało się wysłać wideo: Rozmiar pliku wynosi 0 B (indeks listy odtwarzania {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ Plik wideo jest nadal pobierany, proszę czekać..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Błąd podczas przetwarzania wideo: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Błąd podczas wysyłania pliku opisu: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 jeśli chcesz zmienić podpis wideo - odpowiedz na wideo z nowym tekstem</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Nie wykryto napisów"
    VIDEO_PROGRESS_MSG = "<b>Wideo:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Audio:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ Przekroczono limit URL: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Przetwarzanie zakończone"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Zakresy list odtwarzania nie są dozwolone w trybie wielu URL. Wysyłaj tylko pojedyncze URL bez zakresów (*1*5, /vid 1-10, itp.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Sprawdź <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>tutaj</a>, czy Twoja strona jest obsługiwana"
    ERROR_COOKIE_NEEDED_MSG = "Możesz potrzebować <code>cookie</code> do pobrania tego wideo. Najpierw wyczyść swoją przestrzeń roboczą przez polecenie <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Dla YouTube - uzyskaj <code>cookie</code> przez polecenie <b>/cookie</b>. Dla każdej innej obsługiwanej strony - wyślij własne cookie (<a href='https://t.me/tg_ytdlp/203'>przewodnik1</a>) (<a href='https://t.me/tg_ytdlp/214'>przewodnik2</a>) i następnie wyślij ponownie link do wideo."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Wybierz język napisów"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Brak alternatywnych języków audio"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Wybierz język audio"
    PAGE_NUMBER_MSG = "Strona {page}"
    TOTAL_PROGRESS_MSG = "Całkowity postęp"
    SUBTITLE_MENU_CLOSED_MSG = "Menu napisów zamknięte."
    SUBTITLE_LANGUAGE_SET_MSG = "Język napisów ustawiony: {value}"
    AUDIO_SET_MSG = "Audio ustawione: {value}"
    FILTERS_UPDATED_MSG = "Filtry zaktualizowane"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Wstecz"
    CLOSE_BUTTON_TEXT = "🔚Zamknij"
    LIST_BUTTON_TEXT = "📃Lista"
    IMAGE_BUTTON_TEXT = "🖼Obraz"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Jakości nie wykryte automatycznie\nUżyj przycisku 'Inne', aby zobaczyć wszystkie dostępne formaty.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Wykryto transmisję na żywo**\n\nPobieranie trwających lub nieskończonych transmisji na żywo nie jest dozwolone.\n\nPoczekaj, aż transmisja się zakończy i spróbuj pobrać ponownie, gdy:\n• Czas trwania transmisji jest znany\n• Transmisja się zakończyła\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Pobieranie transmisji na żywo</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Fragment {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Maksymalny rozmiar: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Całkowity czas trwania: {duration} sek"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Transmisja na żywo - Fragment {chunk}</b>\n⏱ Czas trwania: {duration} sek\n📦 Rozmiar: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Fragment {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Pobieranie transmisji na żywo zakończone</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "Pobrano {chunks} fragment(ów)"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Całkowity czas trwania: {duration} sek"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Pobieranie transmisji na żywo zatrzymane</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Katalog użytkownika został usunięty (prawdopodobnie przez polecenie /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "Plik fragmentu został usunięty (prawdopodobnie przez polecenie /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Transmisja się zakończyła"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Wybierz inny format używając polecenia `/format`."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Uzyskano bezpośredni link</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Tytuł:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Czas trwania:</b> {duration} sek\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Strumień wideo:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Strumień audio:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Błąd przetwarzania pliku**\n\nWideo zostało pobrane, ale nie mogło zostać przetworzone z powodu nieprawidłowych znaków w nazwie pliku.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Błąd przetwarzania pliku**\n\nWideo zostało pobrane, ale nie mogło zostać przetworzone z powodu błędu nieprawidłowego argumentu.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Powód:**\n"
        "• Pobrany plik nie jest plikiem wideo\n"
        "• Może to być dokument (PDF, DOC itp.) lub archiwum\n\n"
        "**Rozwiązanie:**\n"
        "• Sprawdź link - może prowadzić do dokumentu, a nie do wideo\n"
        "• Spróbuj innego linku lub źródła\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Powód:**\n"
        "• Plik nie może być przetworzony jako wideo\n"
        "• Może nie być plikiem wideo lub plik jest uszkodzony\n\n"
        "**Rozwiązanie:**\n"
        "• Sprawdź link - może prowadzić do dokumentu, a nie do wideo\n"
        "• Spróbuj innego linku lub źródła\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Format niedostępny**\n\nŻądany format wideo nie jest dostępny dla tego wideo.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ ID formatu {format_id} nie znaleziono dla tego wideo.\n\nDostępne ID formatów: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **Format AV1 nie jest dostępny dla tego wideo.**\n\n**Dostępne formaty:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Błąd przetwarzania pliku**\n\nAudio zostało pobrane, ale nie mogło zostać przetworzone z powodu nieprawidłowych znaków w nazwie pliku.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Błąd przetwarzania pliku**\n\nAudio zostało pobrane, ale nie mogło zostać przetworzone z powodu błędu nieprawidłowego argumentu.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Użytkownik wprowadził zabronioną zawartość. Nie można pobrać."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "Rozmycie NSFW ustawione przez polecenie: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Użytkownik otworzył menu /nsfw."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: zamknięte."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Nie udało się pobrać cookie {service}: status={status} (url ukryty)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Błąd podczas pobierania cookie {service}: {error} (url ukryty)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Nieoczekiwany błąd podczas pobierania cookie {service} (url ukryty): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Plik cookie zaktualizowany dla użytkownika {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Nieprawidłowa zawartość cookie dostarczona przez użytkownika {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "URL-e cookie YouTube są puste dla użytkownika {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "Cookie YouTube pobrane i zweryfikowane dla użytkownika {user_id} ze źródła {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Wszystkie źródła cookie YouTube nie powiodły się dla użytkownika {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Błąd w poleceniu check_porn przez administratora {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Rozmiar części podziału ustawiony na {size} bajtów."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Wysyłanie wideo zakończone z podziałem pliku."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Wideo z listy odtwarzania wysłane: {sent}/{total} plików (jakość={quality}) do użytkownika {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Nieznany błąd: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Pomijanie nieobsługiwanego typu pliku w liście odtwarzania pod indeksem {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg nie znaleziony. Zainstaluj FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Konwersja do MP4 nie powiodła się: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Osadzanie napisów może zająć dużo czasu (do 1 min na 1 min wideo)!\n🔥 Rozpoczynanie wypalania napisów..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Napisy nie mogą być osadzone z powodu limitów (jakość/czas trwania/rozmiar)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Napisy nie są dostępne dla wybranego języka"
    ERROR_SENDING_VIDEO_MSG = "❌ Błąd podczas wysyłania wideo: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Wideo z listy odtwarzania wysłane: {sent}/{total} plików."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Pobieranie anulowane z powodu przekroczenia czasu (2 godziny)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Nie udało się pobrać wideo: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Błąd: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON musi być obiektem (słownikiem)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Nieprawidłowy format JSON. Podaj prawidłowy JSON."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Wartość musi być między {min_val} a {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} ustawione na: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Prawda"
    ARGS_FALSE_BUTTON_MSG = "❌ Fałsz"
    ARGS_BACK_BUTTON_MSG = "🔙 Wstecz"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Zamknij"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Prawda"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Fałsz"
    ARGS_NOT_SET_MSG = "Nie ustawiono"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ Format AV1 nie jest dostępny dla tego wideo.\n\nDostępne formaty:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Błąd podczas pobierania: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ Nie znaleziono wideo w liście odtwarzania pod indeksem {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Konwersja wideo nie powiodła się**\n\nWideo nie mogło zostać przekonwertowane do MP4 z powodu błędu nieprawidłowego argumentu.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Konwersja wideo nie powiodła się**\n\nWideo nie mogło zostać przekonwertowane do MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Nie udało się uzyskać linków do strumieni"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Błąd podczas uzyskiwania linku:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ Nie znaleziono zawartości pod indeksem {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Błąd: Oryginalna wiadomość nie znaleziona."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Błąd: URL nie znaleziony."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Ten URL nie może być osadzony."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ Kodek {codec} nie jest dostępny dla tego wideo"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ Format {format} nie jest dostępny dla tego wideo"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Limit powodziowy. Spróbuj później."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Sprawdź Cookie"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ WSZYSTKO (AUTO)"
    PROXY_OFF_BUTTON_MSG = "❌ WYŁ."
    PROXY_CLOSE_BUTTON_MSG = "🔚Zamknij"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Wybierz kraj:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Wyczyść wybór kraju"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Wybrany kraj: {country} (kod: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Dostępne proxy: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Bot najpierw spróbuje HTTP, potem SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Serwer proxy automatycznie włączony dla wybranego kraju"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Wybór kraju został wyczyszczony"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Wybór kraju został wyczyszczony"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Wybrany kraj: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Używanie kraju z pliku: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Dostępne kraje z pliku: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 Wybrany kraj: {country} (kod: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ Serwer proxy włączony dla tego kraju"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ Serwer proxy wyłączony (naciśnij WSZYSTKIE (AUTO), aby włączyć)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ WŁ."
    MEDIAINFO_OFF_BUTTON_MSG = "❌ WYŁ."
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Zamknij"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV: WŁ."
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV: WYŁ."
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ WŁ. (Bez rozmycia)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ WŁ. (Bez rozmycia)"
    NSFW_OFF_BLUR_MSG = "✅ WYŁ. (Rozmycie)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ WYŁ. (Rozmycie)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Czyszczenie"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Błąd podczas przetwarzania wiadomości odpowiedzi dla użytkownika {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Błąd podczas wysyłania wiadomości rozgłoszeniowej do użytkownika {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Logi {bot_name}\nUżytkownik: {user_id}\nCałkowite logi: {total}\nAktualny czas: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nCałkowite {path}: {count}\nAktualny czas: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Całkowici użytkownicy: {count}</i>\nOstatnie 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Cache pornograficzne przeładowane przez administratora {admin_id}. Domeny: {domains}, Słowa kluczowe: {keywords}, Strony: {sites}, BIAŁA LISTA: {whitelist}, SZARA LISTA: {greylist}, CZARNA LISTA: {black_list}, BIAŁE SŁOWA KLUCZOWE: {white_keywords}, PROXY_DOMAINY: {proxy_domains}, PROXY_2_DOMAINY: {proxy_2_domains}, CZYSTE_ZAPYTANIE: {clean_query}, DOMENY_BEZ_COOKIE: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Błąd podczas wysyłania wiadomości o przekroczeniu czasu: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Wybierz język</b>"
    LANG_CHANGED_MSG = "✅ Język zmieniony na {lang_name}"
    LANG_ERROR_MSG = "❌ Błąd podczas zmiany języka"
    LANG_CLOSED_MSG = "Wybór języka zamknięty"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] callback: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Dodawanie przycisku monitorowania przeglądarki z URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "URL monitorowania przeglądarki nie skonfigurowany: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Ustawienie klawiatury zaktualizowane!**\n\nNowe ustawienie: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Nie udało się ukryć klawiatury: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Używanie działających cookie YouTube do wyodrębniania linków dla użytkownika {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Brak działających cookie YouTube dostępnych do wyodrębniania linków dla użytkownika {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Używanie istniejących cookie YouTube do wyodrębniania linków dla użytkownika {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Nie znaleziono cookie YouTube do wyodrębniania linków dla użytkownika {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Skopiowano globalny plik cookie do folderu użytkownika {user_id} do wyodrębniania linków"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Użytkownik {user_id} zażądał polecenia mediainfo"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Użytkownik {user_id} jest administratorem: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Użytkownik {user_id} jest w kanale: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Użytkownik {user_id} odmowa dostępu - nie administrator i nie w kanale"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Użytkownik {user_id} dostęp przyznany"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ To polecenie jest dostępne tylko dla administratorów."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Pobieranie zakończone z obsługą tokenu PO"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Limit powodziowy. Spróbuj później."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ Błąd odświeżania tokenu REST: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Błąd podczas zamykania sesji Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Błąd podczas inicjalizacji podstawowej struktury bazy danych: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Nie wszystkie parametry są ustawione w config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL nie jest ustawiony"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey nie jest ustawiony do uzyskania idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Błąd podczas pobierania zrzutu Firebase: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Nie udało się pobrać zrzutu Firebase przez REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Błąd w _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Błąd podczas uruchamiania automatycznego reload_cache (próba {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Wszystkie próby ponowienia nie powiodły się"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Rozpoczynanie pobierania zrzutu Firebase o {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Zależność niedostępna: requests lub Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ Baza danych jest pusta"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Błąd podczas zamykania loggera: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Błąd podczas czyszczenia: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Błąd klonowania: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Przekroczenie czasu klonowania"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Wyjątek podczas klonowania: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Aktualizacja anulowana przez użytkownika"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Repozytorium sklonowane pomyślnie"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Kopie zapasowe przeniesione do _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Wszystkie moduły są załadowane"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Czyszczenie zakończone przy wyjściu"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Otrzymano sygnał {signal}, zamykanie elegancko..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Proszę czekać..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Pobieranie strumienia HLS:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "oczekiwanie na fragmenty"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Kopia zapasowa {ts} nie znaleziona w _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Nie udało się przywrócić {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Przywrócono: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Szczegóły:</b> {error_details}\n\nPobieranie zatrzymane z powodu krytycznego błędu.\n\n💡 <b>Wskazówka:</b> Jeśli otrzymujesz błąd 401 Unauthorized, spróbuj użyć polecenia <code>/cookie instagram</code> lub wyślij własne cookie do uwierzytelnienia z Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domena na czarnej liście pornograficznej: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Znaleziono słowa kluczowe pornograficzne: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domena na białej liście: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Znaleziono słowa kluczowe z białej listy: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Nie znaleziono słów kluczowych pornograficznych"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Błąd API TikTok pod indeksem {index}, pomijanie do następnego audio..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Błąd API TikTok pod indeksem {index}, pomijanie do następnego wideo..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "Użytkownik wprowadził <b>url</b>\n <b>imię użytkownika:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>Użytkownik wprowadził tak:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Dołącz do kanału"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Rejestrowanie handlera: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Pobierz moje 5 cookie"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Uzyskaj cookie YT z przeglądarki"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Zweryfikuj swój plik cookie"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Prześlij niestandardowe cookie"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Zamknij"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Dostępne formaty dla: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Zamknij"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Zamknij"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Zamknij"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Zamknij"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Pomoc zamknięta."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Zamknięte"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Wystąpił błąd"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg nie znaleziony w PATH lub katalogu projektu. Zainstaluj FFmpeg."
    YTDLP_NOT_FOUND_MSG = "binarny yt-dlp nie znaleziony w PATH lub katalogu projektu. Zainstaluj yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Wideo zostanie podzielone na {rounds} części, co może być nadmierne"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Dzielenie części wideo {current}/{total}: {start_time:.2f}s do {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Nie udało się utworzyć części podziału {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Pomyślnie utworzono część podziału {part}: {target_name} ({size} bajtów)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Błąd podczas dzielenia części wideo {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Wideo podzielone na {count} części pomyślnie"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Błąd w procesie dzielenia wideo: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Błąd podczas przetwarzania wideo {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Plik wideo nie istnieje: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Błąd podczas parsowania wymiarów '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Nie można określić wymiarów wideo z '{size_result}', używanie domyślnych: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Błąd podczas tworzenia miniatury: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Błąd podczas parsowania czasu trwania wideo: {error}, wynik to: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Miniatura nie utworzona w {thumb_dir}, używanie domyślnej"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Błąd wykonania polecenia: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Błąd podczas tworzenia miniatury z FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Pomijanie sekcji konfiguracji nie będącej słownikiem: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Ustawianie {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Używanie cookie użytkownika: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Używanie cookie YouTube dla użytkownika {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Skopiowano globalny plik cookie do folderu użytkownika {user_id}"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Używanie skopiowanych globalnych cookie jako cookie użytkownika: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Nie udało się skopiować globalnego pliku cookie dla użytkownika {user_id}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Używanie --no-cookies dla domeny: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy żądane, ale nie udało się zaimportować/pobrać konfiguracji: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Wymuszanie użycia proxy dla gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy żądane, ale konfiguracja proxy jest niekompletna"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Pomocnik proxy nie powiódł się: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Parsowanie elementów ekstraktora..."
    GALLERY_DL_ITEM_COUNT_MSG = "Element {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Znaleziono metadane (tag 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "Znaleziono URL (tag 3): {url}, metadane: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Znaleziono metadane (legacy): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "Znaleziono URL (legacy): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Znaleziono nazwę pliku: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Znaleziono katalog: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Znaleziono rozszerzenie: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Sparsowano {count} elementów, info: {info}, fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Ustawianie konfiguracji gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Próba Strategii A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "moduł gallery_dl.extractor nie znaleziony"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() niedostępne w tej wersji"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Wywoływanie extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Żaden ekstraktor nie pasuje do URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Ustawianie cookie na ekstraktorze: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Nie udało się ustawić cookie na ekstraktorze: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Ekstraktor znaleziony, wywoływanie items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Strategia A powiodła się, otrzymano info: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Strategia A: extractor.items() zwróciło brak prawidłowych informacji"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Strategia A (extractor.find) nie powiodła się: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Metadane fallback z --get-urls: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Wszystkie strategie nie powiodły się w uzyskaniu metadanych"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Nie udało się wyodrębnić informacji o obrazie: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "moduł gallery_dl.job nie znaleziony (uszkodzona instalacja?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob niedostępne w tej wersji"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Wyszukiwanie pobranych plików w katalogu gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Próba znalezienia plików według nazw z ekstraktora"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Błąd podczas odczytywania argumentów użytkownika dla {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Błąd podczas przetwarzania wideo {video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Użytkownik {user_id} ma włączone send_as_file, wysyłanie jako dokument"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video przekroczyło limit czasu wielokrotnie; powrót do send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Podpis zbyt długi, próba z minimalnym podpisem"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (minimalny podpis) przekroczyło limit czasu; powrót do send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Błąd podczas wysyłania wideo z minimalnym podpisem: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Błąd podczas wysyłania pełnego pliku opisu: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Błąd podczas usuwania tymczasowego pliku opisu: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Pomijanie match_filter dla domeny w NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Sprawdzanie istniejących cookie YouTube na URL użytkownika do wykrywania formatu dla użytkownika {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Istniejące cookie YouTube działają na URL użytkownika do wykrywania formatu dla użytkownika {user_id} - używanie ich"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Istniejące cookie YouTube nie powiodły się na URL użytkownika, próba uzyskania nowych do wykrywania formatu dla użytkownika {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Próba źródła cookie YouTube {i} do wykrywania formatu dla użytkownika {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "Cookie YouTube ze źródła {i} działają na URL użytkownika do wykrywania formatu dla użytkownika {user_id} - zapisane do folderu użytkownika"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "Cookie YouTube ze źródła {i} nie działają na URL użytkownika do wykrywania formatu dla użytkownika {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Nie udało się pobrać cookie YouTube ze źródła {i} do wykrywania formatu dla użytkownika {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Wszystkie źródła cookie YouTube nie powiodły się do wykrywania formatu dla użytkownika {user_id}, próba bez cookie"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Brak skonfigurowanych źródeł cookie YouTube do wykrywania formatu dla użytkownika {user_id}, próba bez cookie"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Nie znaleziono cookie YouTube do wykrywania formatu dla użytkownika {user_id}, próba uzyskania nowych"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Używanie cookie YouTube do wykrywania formatu dla użytkownika {user_id} (już zweryfikowane w menu Always Ask)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Nie znaleziono cookie YouTube do wykrywania formatu dla użytkownika {user_id}, próba przywrócenia..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Skopiowano globalny plik cookie do folderu użytkownika {user_id} do wykrywania formatu"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Nie udało się skopiować globalnego pliku cookie dla użytkownika {user_id}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Używanie --no-cookies dla domeny w get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "Aplikacja jeszcze nie zainicjalizowana. Nie można uzyskać dostępu do {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Podpis:</b> <code>{caption}</code>\n<b>ID użytkownika:</b> <code>{user_id}</code>\n<b>Imię użytkownika:</b> <code>{users_name}</code>\n<b>ID pliku wideo:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Błąd w caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Nieoczekiwany błąd w caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL wideo</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL brakuje w konfiguracji"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin zainicjalizowany"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken odświeżony"
    DB_LOG_FOR_USER_ADDED_MSG = "Log dla użytkownika dodany"
    DB_DATABASE_CREATED_MSG = "baza danych utworzona"
    DB_BOT_STARTED_MSG = "Bot uruchomiony"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY zapisany do config.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Część listy odtwarzania już w cache: {path_parts}, pomijanie"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: brak cache dla żadnego wariantu URL/jakości, zwracanie pustego słownika"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: szybkie liczenie dla dużego zakresu: {cached_count} wideo w cache"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: brak cache dla hash {url_hash}, jakość {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: brak cache dla żadnego wariantu URL, zwracanie None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Dostęp odmówiony. Tylko administrator."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Automatyczne przeładowywanie cache Firebase zaktualizowane!\n\n📊 Status: {status}\n⏰ Harmonogram: co {interval} godzin od 00:00\n🕒 Następne przeładowanie: {next_exec} (za {delta_min} minut)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Automatyczne przeładowywanie cache Firebase zatrzymane!\n\n📊 Status: ❌ WYŁĄCZONE\n💡 Użyj /auto_cache on, aby ponownie włączyć"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Nieprawidłowy argument. Użyj /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Interwał musi być między 1 a 168 godzinami"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Nie udało się ustawić interwału"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Interwał automatycznego przeładowywania cache Firebase zaktualizowany!\n\n📊 Status: ✅ WŁĄCZONE\n⏰ Harmonogram: co {interval} godzin od 00:00\n🕒 Następne przeładowanie: {next_exec} (za {delta_min} minut)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Automatyczne przeładowywanie cache Firebase uruchomione!\n\n📊 Status: ✅ WŁĄCZONE\n⏰ Harmonogram: co {interval} godzin od 00:00\n🕒 Następne przeładowanie: {next_exec} (za {delta_min} minut)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Automatyczne przeładowywanie cache Firebase zatrzymane!\n\n📊 Status: ❌ WYŁĄCZONE\n💡 Użyj /auto_cache on, aby ponownie włączyć"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Automatyczne przeładowywanie WŁĄCZONE; następne o {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Automatyczne przeładowywanie WYŁĄCZONE przez administratora."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Interwał automatycznego przeładowywania ustawiony na {interval}h; następne o {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Automatyczne przeładowywanie uruchomione; następne o {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Automatyczne przeładowywanie zatrzymane przez administratora."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Cache Firebase załadowany: {count} węzłów głównych"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Plik cache Firebase nie znaleziony, rozpoczynanie z pustym cache: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Nie udało się załadować cache Firebase: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Cache Firebase przeładowany: {count} węzłów głównych"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Plik cache Firebase nie znaleziony: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Nie udało się przeładować cache Firebase: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 Zostałeś zbanowany z bota! Aby odbanować, skontaktuj się z {Config.ADMIN_USERNAME}\n<blockquote>P.S. Nie opuszczaj kanału - zostaniesz automatycznie zbanowany ⛔️</blockquote>\n🌍Zmień język /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Nie znaleziono formatów wideo. Próba pobrania obrazów…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram ograniczył wysyłanie wiadomości.\n⏳ Proszę czekać: {time_str}\nAby zaktualizować timer wyślij URL ponownie 2 razy."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Kliknij przycisk, aby skopiować URL strumienia, a następnie wklej go w aplikacji VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Kliknij przycisk, aby skopiować URL strumienia, a następnie wklej go w aplikacji VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Błąd podczas uzyskiwania linku:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Błąd podczas wysyłania pliku formatów: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Nie udało się uzyskać formatów:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Analizowanie... (poczekaj 6 sek)"
    AA_PROCESSING_MSG = "🔎 Analizowanie..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{wrong} zawiera niedozwolone znaki. Dozwolone są tylko litery, cyfry i _.\nProszę użyć: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Do pracy w grupie bot potrzebuje uprawnień administratora. Proszę ustawić bota jako administratora tej grupy."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Witaj {first_name},\n \n<i>Ten bot🤖 może pobierać dowolne wideo bezpośrednio do telegramu.😊 Aby uzyskać więcej informacji, naciśnij <b>/help</b></i> 👈\n\n<blockquote>P.S. Pobieranie treści 🔞NSFW i plików z ☁️Cloud Storage jest płatne! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Nie opuszczaj kanału - zostaniesz zbanowany z używania bota ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Brak plików do usunięcia."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 Wszystkie pliki usunięte pomyślnie!\n\nUsunięte pliki:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ POCZEKAJ, AŻ TWOJE POPRZEDNIE POBRANIE SIĘ ZAKOŃCZY"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "Instancja aplikacji jest None w check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict jest None, zezwalanie na pobieranie"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict jest None, zezwalanie na osadzanie napisów"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: sprawdzanie limitów - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: klucze info_dict: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Osadzanie napisów pominięte: czas trwania {duration}s przekracza limit {max_duration}s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Osadzanie napisów pominięte: rozmiar {size_mb:.2f}MB przekracza limit {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Osadzanie napisów pominięte: jakość {width}x{height} (minimalna strona {min_side}p) przekracza limit {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "lista odtwarzania"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Przekroczono limit zakresu dla {service}: {count} (maksimum {max_count}).\n\nUżyj jednego z tych poleceń, aby pobrać maksymalną dostępną liczbę plików:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Przekroczono limit zakresu dla {service}: {count} (maksimum {max_count})\nID użytkownika: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "Dostawca tokenu PO wyłączony w konfiguracji"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} nie jest domeną YouTube, pomijanie tokenu PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "Dostawca tokenu PO nie jest dostępny pod {base_url}, powrót do standardowego wyodrębniania YouTube"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "Cache dostawcy tokenu PO wyczyszczony, sprawdzanie dostępności przy następnym żądaniu"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Instancja aplikacji jeszcze niedostępna"
    HELPER_USER_NAME_MSG = "Użytkownik"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Wykryto limit powodziowy, oczekiwanie przez {wait_seconds} sekund"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Wykryto limit powodziowy, ale nie można było wyodrębnić czasu, oczekiwanie przez {retry_delay} sekund"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "Wykryto błąd msg_seqno, oczekiwanie przez {retry_delay} sekund"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Konfiguracja proxy niekompletna, używanie bezpośredniego połączenia"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Zamknij"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Zamknij"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Zamknij"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Plik logów usunięty."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Plik tagów usunięty."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Plik formatu usunięty."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Plik podziału usunięty."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Plik mediainfo usunięty."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Ustawienia napisów usunięte."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Ustawienia klawiatury usunięte."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Ustawienia args usunięte."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 Ustawienia NSFW usunięte."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Ustawienia proxy usunięte."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Ustawienia flood wait usunięte."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Zamknij"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Polecenie pobierania wideo"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Użycie: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Przykłady:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (kolejność bezpośrednia)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (kolejność odwrotna)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Zobacz także: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Użytkownik {user_id} zamknął polecenie add_bot_to_group"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Nie udało się wyodrębnić ID YouTube"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Nie udało się pobrać miniatury lub jest zbyt duża"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Wybierz język audio"
    AA_NO_SUBTITLES_DETECTED_MSG = "Nie wykryto napisów"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Wybierz język napisów"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Błąd uwierzytelniania"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Konto nie znalezione"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Konto niedostępne"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Przekroczono limit szybkości"
    GALLERY_DL_NETWORK_ERROR_MSG = "Błąd sieci"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Zawartość niedostępna"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Ograniczenia geograficzne"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Wymagana weryfikacja"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Naruszenie zasad"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Nieznany błąd"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Pobieranie rozpoczęte</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Zamknij"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Polecenie pobierania wideo</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Użycie: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Przykłady:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Zobacz także: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Limit powodziowy. Spróbuj później."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Użycie polecenia Cookie</b>

<code>/cookie</code> - Pokaż menu cookie
<code>/cookie youtube</code> - Pobierz cookie YouTube
<code>/cookie instagram</code> - Pobierz cookie Instagram
<code>/cookie tiktok</code> - Pobierz cookie TikTok
<code>/cookie x</code> lub <code>/cookie twitter</code> - Pobierz cookie Twitter/X
<code>/cookie facebook</code> - Pobierz cookie Facebook
<code>/cookie custom</code> - Pokaż instrukcje niestandardowego cookie

<i>Dostępne usługi zależą od konfiguracji bota.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Plik cookie usunięty i cache wyczyszczony."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Poprz."
    SUBS_BACK_BUTTON_MSG = "🔙Wstecz"
    SUBS_OFF_BUTTON_MSG = "🚫 WYŁ."
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - ustaw język"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - ustaw język z AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Prawidłowe opcje:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 JĘZYK"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 CZYŚĆ"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIE"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MEDIA"
    SETTINGS_INFO_BUTTON_MSG = "📖 INFO"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ WIĘCEJ"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Tylko cookie"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Logi "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Tagi"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Format"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Podział"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Napisy"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Klawiatura"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Args"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Proxy"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Flood wait"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Wszystkie pliki"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Pobierz moje 5 cookie"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Uzyskaj cookie YT z przeglądarki"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Zweryfikuj swój plik cookie"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Prześlij niestandardowe cookie"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Zmień jakość i format"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Włącz/Wyłącz MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Zmień rozmiar części podziału wideo"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Pobierz wideo jako audio"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Ustawienia języka napisów"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Jak pobierać listy odtwarzania"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Pobierz obrazy przez gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Wyślij swoje #tagi"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Uzyskaj instrukcje"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Wyślij swoje logi"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Pomoc dotycząca list odtwarzania"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - jak to zrobić"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Uzyskaj bezpośrednie linki do wideo"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Włącz/Wyłącz proxy"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Układ klawiatury"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Pomocnik wyszukiwania inline"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - argumenty yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - Ustawienia rozmycia NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Opcje czyszczenia</b>\n\nWybierz, co wyczyścić:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobilne: Aktywuj wyszukiwanie @vid"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobilne: Aktywuj wyszukiwanie @vid"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 WYŁ."
    KEYBOARD_FULL_BUTTON_MSG = "🔣 PEŁNE"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL obrazów]({url})"
    IMAGE_ERROR_MSG = "❌ Błąd: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Wstecz"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - niestandardowy format"
    FORMAT_720P_MSG = "• <code>/format 720</code> - jakość 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - jakość 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - jakość 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - konkretne ID formatu"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - zawsze pokazuj menu"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/najlepsza jakość"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Zawsze pytaj (menu + przyciski)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Inne (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (najlepsze dla PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (najlepsze dla mobilnego Telegram)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (MAKSYMALNA jakość)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Niestandardowe (wprowadź własne)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Z przeglądarki"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Własne"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Tryb wprowadzania automatycznie zamknięty z powodu braku aktywności (5 minut)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Resetuj wszystko"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Zobacz aktualne"
    ARGS_BACK_BUTTON_MSG = "🔙 Wstecz"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Przekaż tę wiadomość do ulubionych, aby zapisać te ustawienia jako szablon.</i> \n\n<i>Przekaż tę wiadomość z powrotem tutaj, aby zastosować te ustawienia.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Aktualne argumenty yt-dlp:\n\nBrak skonfigurowanych niestandardowych ustawień.\n\n---\n\n<i>Przekaż tę wiadomość do ulubionych, aby zapisać te ustawienia jako szablon.</i> \n\n<i>Przekaż tę wiadomość z powrotem tutaj, aby zastosować te ustawienia.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Aktualne argumenty yt-dlp:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Eksportuj ustawienia"
    ARGS_SETTINGS_READY_MSG = "Ustawienia gotowe do eksportu! Przekaż tę wiadomość do ulubionych, aby zapisać."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Aktualne argumenty yt-dlp:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Nie udało się rozpoznać ustawień w wiadomości. Upewnij się, że wysłałeś poprawny szablon ustawień."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Ustawienia pomyślnie zaimportowane!\n\nZastosowane parametry: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Kluczowe ustawienia:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Błąd podczas zapisywania zaimportowanych ustawień."
    ARGS_ERROR_IMPORTING_MSG = "❌ Wystąpił błąd podczas importowania ustawień."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Pobierz pliki cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Wybierz usługę, aby pobrać plik cookie."
    COOKIE_MENU_SAVE_INFO_MSG = "Pliki cookie będą zapisane jako cookie.txt w Twoim folderze."
    COOKIE_MENU_TIP_HEADER_MSG = "Wskazówka: Możesz również użyć bezpośredniego polecenia:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – pobierz i zweryfikuj cookie"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – użyj konkretnego źródła według indeksu (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Następnie zweryfikuj za pomocą <code>/check_cookie</code> (testy na RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Zawsze pytaj"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Link"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Obejrzyj"  # TYMCZASOWO WYŁĄCZONE: usługa poketube nie działa
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Podpis"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ PRZYTNIJ"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Przycinanie wideo</b>\n\nCzas trwania wideo: <b>{start_time} - {end_time}</b>\n\nProszę wysłać żądany zakres czasu w formacie:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nPrzykład: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Nieprawidłowy format. Proszę użyć: <code>HH:MM:SS-HH:MM:SS</code>\n\nPrzykład: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Nieprawidłowy zakres. Czas rozpoczęcia musi być mniejszy niż czas zakończenia."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ Zakres czasu jest poza granicami wideo.\n\nCzas trwania wideo: <b>{start_time} - {end_time}</b>\n\nTwój zakres musi być w tych granicach."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>Wideo zostanie przycięte:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Częściowo ukończone - {successful_uploads}/{total_files} plików audio przesłanych."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Audio pomyślnie pobrane i wysłane - {total_files} plików przesłanych."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Prywatne konto TikTok</b>\n\n"
        "To konto TikTok jest prywatne lub wszystkie wideo są prywatne.\n\n"
        "<b>💡 Rozwiązanie:</b>\n"
        "1. Obserwuj konto @{username}\n"
        "2. Wyślij swoje cookie do bota używając polecenia <code>/cookie</code>\n"
        "3. Spróbuj ponownie\n\n"
        "<b>Po zaktualizowaniu cookie, spróbuj ponownie!</b>"
    )

    #######################################################
