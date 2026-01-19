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
    CREDITS_MSG = "<blockquote><i>Gestito da</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Cambia lingua: /lang</b>"
    TO_USE_MSG = "<i>Per usare questo bot devi iscriverti al canale Telegram @tg_ytdlp.</i>\nDopo esserti unito al canale, <b>reinvia il tuo link video e il bot lo scaricherà per te</b> ❤️\n\n<blockquote>P.S. Il download di contenuti 🔞NSFW e file da ☁️Cloud Storage è a pagamento! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Non lasciare il canale - sarai bannato dall'uso del bot ⛔️</blockquote>"

    ERROR1 = "Link URL non trovato. Inserisci un URL con <b>https://</b> o <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Playlist (yt-dlp)</b>

Per scaricare le playlist invia il loro URL con intervalli <code>*start*end</code> alla fine. Ad esempio: <code>URL*1*5</code> (primi 5 video da 1 a 5 inclusi).<code>URL*-1*-5</code> (ultimi 5 video da 1 a 5 inclusi).
Oppure puoi usare <code>/vid DA-A URL</code>. Ad esempio: <code>/vid 3-7 URL</code> (scarica video da 3 a 7 inclusi dall'inizio). <code>/vid -3-7 URL</code> (scarica video da 3 a 7 inclusi dalla fine). Funziona anche per il comando <code>/audio</code>.

<b>Esempi:</b>

🟥 <b>Intervallo video da playlist YouTube:</b> (serve 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(scarica i primi 5 video da 1 a 5 inclusi)
🟥 <b>Video singolo da playlist YouTube:</b> (serve 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(scarica solo il 3° video)

⬛️ <b>Profilo TikTok:</b> (serve il tuo 🍪)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(scarica i primi 10 video dal profilo utente)

🟪 <b>Storie Instagram:</b> (serve il tuo 🍪)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(scarica le prime 3 storie)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(scarica le prime 10 storie dall'album)

🟦 <b>Video VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(scarica i primi 3 video dal profilo utente/gruppo)

⬛️<b>Canali Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(scarica video da 2 a 4 inclusi dal canale)

🟪 <b>Clip Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(scarica i primi 3 clip dal canale)

🟦 <b>Gruppi Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(scarica i primi 2 video dal gruppo)

🟧 <b>Modelli Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(scarica i primi 2 video dal profilo modello)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(scarica i primi 3 video dai risultati di ricerca in base al tuo prompt)

e così via...
vedi <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">elenco dei siti supportati</a>
</blockquote>

<blockquote expandable>🖼 <b>Immagini (gallery-dl)</b>

Usa <code>/img URL</code> per scaricare immagini/foto/album da molte piattaforme.

<b>Esempi:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Intervalli:</b>
<code>/img 11-20 https://example.com/album</code> — elementi 11..20
<code>/img 11- https://example.com/album</code> — da 11 alla fine (o limite bot)

<i>Le piattaforme supportate includono vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, ecc. Elenco completo:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">siti supportati da gallery-dl</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Bot Download Video - Aiuto</b>

📥 <b>Utilizzo Base:</b>
• Invia qualsiasi link → il bot lo scarica
  <i>il bot prova automaticamente a scaricare video tramite yt-dlp e immagini tramite gallery-dl.</i>
• <b>URL multipli:</b> In modalità selezione qualità (<code>/format</code>) puoi inviare fino a <b>10 URL</b> in un messaggio. Ogni URL su una nuova riga o separati da spazi.
• <code>/audio URL</code> → estrai audio
• <code>/link [quality] URL</code> → ottieni link diretti
• <code>/proxy</code> → abilita/disabilita proxy per tutti i download
• Rispondi al video con testo → cambia didascalia

📋 <b>Playlist e Intervalli:</b>
• <code>URL*1*5</code> → scarica i primi 5 video
• <code>URL*-1*-5</code> → scarica gli ultimi 5 video
• <code>/vid 3-7 URL</code> → diventa <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → diventa <code>URL*-3*-7</code>

🍪 <b>Cookie e Privati:</b>
• Carica *.txt cookie per video privati
• <code>/cookie [service]</code> → scarica cookie (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → scegli sorgente per indice (1–N)
• <code>/cookies_from_browser</code> → estrai dal browser
• <code>/check_cookie</code> → verifica cookie
• <code>/save_as_cookie</code> → salva testo come cookie

🧹 <b>Pulizia:</b>
• <code>/clean</code> → solo file multimediali
• <code>/clean all</code> → tutto
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Impostazioni:</b>
• <code>/settings</code> → menu impostazioni
• <code>/format</code> → qualità e formato
• <code>/split</code> → dividi video in parti
• <code>/mediainfo on/off</code> → informazioni multimediali
• <code>/nsfw on/off</code> → sfocatura NSFW
• <code>/tags</code> → visualizza tag salvati
• <code>/sub on/off</code> → sottotitoli
• <code>/keyboard</code> → tastiera (OFF/1x3/2x3)

🏷️ <b>Tag:</b>
• Aggiungi <code>#tag1#tag2</code> dopo URL
• I tag appaiono nelle didascalie
• <code>/tags</code> → visualizza tutti i tag

🔗 <b>Link Diretti:</b>
• <code>/link URL</code> → migliore qualità
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → qualità specifica

⚙️ <b>Comandi Rapidi:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → imposta qualità
• <code>/keyboard off/1x3/2x3/full</code> → layout tastiera
• <code>/split 100mb-2000mb</code> → cambia dimensione parte
• <code>/subs off/ru/en auto</code> → lingua sottotitoli
• <code>/list URL</code> → elenco formati disponibili
• <code>/mediainfo on/off</code> → attiva/disattiva informazioni multimediali
• <code>/proxy on/off</code> → abilita/disabilita proxy per tutti i download

📊 <b>Info:</b>
• <code>/usage</code> → cronologia download
• <code>/search</code> → ricerca inline tramite @vid

🖼 <b>Immagini:</b>
• <code>URL</code> → scarica URL immagini
• <code>/img URL</code> → scarica immagini da URL
• <code>/img 11-20 URL</code> → scarica intervallo specifico
• <code>/img 11- URL</code> → scarica dall'11° alla fine

👨‍💻 <i>Sviluppatore:</i> @upekshaip
🤝 <i>Collaboratore:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Salva semplicemente il tuo cookie come <b><u>cookie.txt</u></b> e invialo al bot come documento.\n\n"
        "Puoi anche inviare i cookie come testo normale con il comando <b><u>/save_as_cookie</u></b>.\n"
        "<b>Utilizzo di <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>Istruzioni:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message
    SEARCH_MSG = """
🔍 <b>Ricerca video</b>

Premi il pulsante qui sotto per attivare la ricerca inline tramite @vid.

<blockquote>Sul PC digita semplicemente <b>"@vid Your_Search_Query"</b> in qualsiasi chat.</blockquote>
    """
    
    # Settings and Hints
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Comando Download Immagini</b>\n\n"
        "Utilizzo: <code>/img URL</code>\n\n"
        "<b>Esempi:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Piattaforme supportate (esempi):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, ecc. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">elenco completo</a></blockquote>"
        "Vedi anche: "
    )
    
    LINK_HINT_MSG = (
        "Ottieni link video diretti con selezione qualità.\n\n"
        "Utilizzo: /link + URL \n\n"
        "(es. /link https://youtu.be/abc123)\n"
        "(es. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Aggiungi Bot al Gruppo</b>

Aggiungi i miei bot ai tuoi gruppi per ottenere funzionalità avanzate e limiti più alti!
————————————
📊 <b>Limiti GRATUITI Attuali (nella DM del Bot):</b>
<blockquote>•🗑 Disordine da tutti i file non ordinati 👎
• Dimensione max 1 file: <b>8 GB </b>
• Qualità max 1 file: <b>ILLIMITATA</b>
• Durata max 1 file: <b>ILLIMITATA</b>
• Numero max di download: <b>ILLIMITATO</b>
• Max URL in un messaggio: <b>10</b> (solo in modalità selezione qualità)
• Max elementi playlist per 1 volta: <b>50</b>
• Max video TikTok per 1 volta: <b>500</b>
• Max immagini per 1 volta: <b>1000</b>
• Limiti rate URL: <b>5/min, 60/ora, 1000/giorno</b>
• Limite comandi: <b>20/min</b>
• 1 Download tempo max: <b>2 ore</b>
• 🔞 I contenuti NSFW sono a pagamento! 1⭐️ = $0.02
• 🆓 TUTTI GLI ALTRI MEDIA SONO TOTALMENTE GRATUITI
• 📝 Tutti i log dei contenuti e cache ai miei log-channels per repost istantaneo quando si ri-scarica</blockquote>

💬<b>Questi limiti solo per video con sottotitoli:</b>
<blockquote>• Durata max video+sottotitoli: <b>1.5 ore</b>
• Dimensione max file video+sottotitoli: <b>500 MB</b>
• Qualità max video+sottotitoli: <b>720p</b></blockquote>
————————————
🚀 <b>Vantaggi Gruppo a Pagamento (2️⃣x Limiti):</b>
<blockquote>•  🗂 Vault media strutturato ordinato per argomenti 👍
•  📁 I bot rispondono nell'argomento in cui li chiami
•  📌 Auto pin messaggio di stato con progresso download
•  🖼 Il comando /img scarica i media come album da 10 elementi
• Dimensione max 1 file: <b>16 GB</b> ⬆️
• Max URL in un messaggio: <b>20</b> ⬆️ (solo in modalità selezione qualità)
• Max elementi playlist per 1 volta: <b>100</b> ⬆️
• Max video TikTok per 1 volta: 1000 ⬆️
• Max immagini per 1 volta: 2000 ⬆️
• Limiti rate URL: <b>10/min, 120/ora, 2000/giorno</b> ⬆️
• Limite comandi: <b>40/min</b> ⬆️
• 1 Download tempo max: <b>4 ore</b> ⬆️
• 🔞 Contenuti NSFW: Gratuiti con metadati completi 🆓
• 📢 Non serve iscriversi al mio canale per i gruppi
• 👥 Tutti i membri del gruppo avranno accesso alle funzioni a pagamento!
• 🗒 Nessun log / nessuna cache ai miei log-channels! Puoi rifiutare copia/repost nelle impostazioni del gruppo</blockquote>

💬 <b>Limiti 2️⃣x per video con sottotitoli:</b>
<blockquote>• Durata max video+sottotitoli: <b>3 ore</b> ⬆️
• Dimensione max file video+sottotitoli: <b>1000 MB</b> ⬆️
• Qualità max video+sottotitoli: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Prezzi e Configurazione:</b>
<blockquote>• Prezzo: <b>$5/mese</b> per 1 bot nel gruppo
• Configurazione: Contatta @iilililiiillliiliililliilliliiil
• Pagamento: 💎TON o altri metodi💲
• Supporto: Supporto tecnico completo incluso</blockquote>
————————————
Puoi aggiungere i miei bot al tuo gruppo per sbloccare gratuitamente 🔞<b>NSFW</b> e raddoppiare (x2️⃣) tutti i limiti.
Contattami se vuoi che permetta al tuo gruppo di usare i miei bot @iilililiiillliiliililliilliliiil
————————————
💡<b>SUGGERIMENTO:</b> <blockquote>Puoi mettere insieme i soldi con qualsiasi numero di tuoi amici (ad esempio 100 persone) e fare 1 acquisto per tutto il gruppo - TUTTI I MEMBRI DEL GRUPPO AVRANNO ACCESSO ILLIMITATO COMPLETO a tutte le funzioni dei bot in quel gruppo per soli <b>$0.05</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>Modalità NSFW: ON✅</b>

• I contenuti NSFW verranno visualizzati senza sfocatura.
• Gli spoiler non si applicheranno ai media NSFW.
• Il contenuto sarà visibile immediatamente

<i>Usa /nsfw off per abilitare la sfocatura</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>Modalità NSFW: OFF</b>

⚠️ <b>Sfocatura abilitata</b>
• I contenuti NSFW saranno nascosti sotto spoiler   
• Per visualizzare, dovrai cliccare sul media
• Gli spoiler si applicheranno ai media NSFW.

<i>Usa /nsfw on per disabilitare la sfocatura</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Parametro non valido</b>

Usa:
• <code>/nsfw on</code> - disabilita sfocatura
• <code>/nsfw off</code> - abilita sfocatura
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Controllo cache...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Elaborazione..."
    DOWNLOADING_MSG = "📥 <b>Download media...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Download immagine...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Download completato</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Scaricato:"
    SENT_STATUS_MSG = "Inviato:"
    PENDING_TO_SEND_STATUS_MSG = "In attesa di invio:"
    TITLE_LABEL_MSG = "Titolo:"
    MEDIA_COUNT_LABEL_MSG = "Conteggio media:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Download completato, elaborazione audio..."
    VIDEO_PROCESSING_MSG = "📽 Il video è in elaborazione..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Inviato dalla cache</b>\n\nAlbum inviati: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Video inviato con successo dalla cache."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Video playlist inviati dalla cache ({cached}/{total} file)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} video inviati dalla cache, download di quelli mancanti..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Inviato dalla cache: {cached}\n🔄 Continuazione download..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Impossibile analizzare i media, procedendo con l'intervallo massimo consentito (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Impossibile determinare il conteggio media, procedendo con l'intervallo massimo consentito (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Impossibile determinare il conteggio totale media, procedendo con l'intervallo specificato {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>URL non valido</b>\n\nFornisci un URL valido che inizi con http:// o https://"

    ERROR_OCCURRED_MSG = "❌ <b>Si è verificato un errore</b>\n\n<code>{url}</code>\n\nErrore: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Errore nell'invio del video: {error}"
    ERROR_UNKNOWN_MSG = "❌ Errore sconosciuto: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Spazio su disco insufficiente per scaricare i video."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ La dimensione del file supera il limite di {limit} GB. Seleziona un file più piccolo entro la dimensione consentita."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>Impossibile scaricare il video con tutti i proxy disponibili</b>\n\nTutti i tentativi di download tramite proxy sono falliti.\nProva:\n• Verificare la funzionalità del proxy\n• Provare un altro proxy dall'elenco\n• Scaricare senza proxy (se possibile)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Errore nell'ottenere il link:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram ha limitato l'invio di messaggi.\n⏳ Attendi: {time}\nPer aggiornare il timer invia di nuovo l'URL 2 volte."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram ha limitato l'invio di messaggi.\n⏳ Attendi: \nPer aggiornare il timer invia di nuovo l'URL 2 volte."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Impossibile scaricare i sottotitoli"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Link Stream Diretti</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Titolo:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Durata:</b> {duration} sec\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Errore: Messaggio originale non trovato."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Il Tag #{tag} contiene caratteri vietati. Sono consentiti solo lettere, cifre e _.\nUsa: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Video playlist inviati: {sent}/{total} file."
    PLAYLIST_CACHE_SENT_MSG = "✅ Inviato dalla cache: {cached}/{total} file."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Impossibile ottenere i link stream"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Seleziona un browser per scaricare i cookie:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Nessun browser trovato su questo sistema. Puoi scaricare i cookie dall'URL remoto o monitorare lo stato del browser:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Apri Browser</b> - per monitorare lo stato del browser nella mini-app"
    BROWSER_OPEN_BUTTON_MSG = "🌐 ApriBrowser"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Scarica da URL Remoto"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ File cookie YouTube scaricato tramite fallback e salvato come cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Nessun browser supportato trovato e nessun COOKIE_URL configurato. Usa /cookie o carica cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Il fallback COOKIE_URL deve puntare a un file .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Il file cookie fallback è troppo grande (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Sorgente cookie fallback non disponibile (stato {status}). Prova /cookie o carica cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Errore nello scaricare il cookie fallback. Prova /cookie o carica cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Errore imprevisto durante il download del cookie fallback."
    BTN_CLOSE = "🔚Chiudi"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Valore booleano non valido"
    ARGS_CLOSED_MSG = "Chiuso"
    ARGS_ALL_RESET_MSG = "✅ Tutti gli argomenti reimpostati"
    ARGS_RESET_ERROR_MSG = "❌ Errore nel reimpostare gli argomenti"
    ARGS_INVALID_PARAM_MSG = "❌ Parametro non valido"
    ARGS_BOOL_SET_MSG = "Impostato su {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "Già impostato su {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Valore di selezione non valido"
    ARGS_VALUE_SET_MSG = "Impostato su {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "Già impostato su {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Valore attuale:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Esempi:</b>\n• <code>default</code> - Usa strategia XFF predefinita\n• <code>never</code> - Non usare mai l'header XFF\n• <code>US</code> - Codice paese Stati Uniti\n• <code>GB</code> - Codice paese Regno Unito\n• <code>DE</code> - Codice paese Germania\n• <code>FR</code> - Codice paese Francia\n• <code>JP</code> - Codice paese Giappone\n• <code>192.168.1.0/24</code> - Blocco IP (CIDR)\n• <code>10.0.0.0/8</code> - Intervallo IP privato\n• <code>203.0.113.0/24</code> - Blocco IP pubblico\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Nota:</b> Questo sostituisce le opzioni --geo-bypass. Usa qualsiasi codice paese a 2 lettere o blocco IP in notazione CIDR.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Esempio:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Invia il tuo nuovo valore."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Intervallo:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Invia un numero."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Esempi:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Nota:</b> Questi header saranno aggiunti agli header Referer e User-Agent esistenti.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Argomenti yt-dlp Attuali:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - Interruttori True/False\n• 📋 <b>Select</b> - Scegli dalle opzioni\n• 🔢 <b>Numeric</b> - Input numerico\n• 📝🔧 <b>Text</b> - Input testo/JSON</blockquote>\n\nQueste impostazioni saranno applicate a tutti i tuoi download."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "Forza connessioni IPv6",
        "force_ipv4": "Forza connessioni IPv4", 
        "no_live_from_start": "Non scaricare stream live dall'inizio",
        "live_from_start": "Scarica stream live dall'inizio",
        "no_check_certificates": "Sopprimi validazione certificato HTTPS",
        "check_certificate": "Controlla certificato SSL",
        "no_playlist": "Scarica solo video singolo, non playlist",
        "embed_metadata": "Incorpora metadati nel file video",
        "embed_thumbnail": "Incorpora miniatura nel file video",
        "write_thumbnail": "Scrivi miniatura su file",
        "ignore_errors": "Ignora errori download e continua",
        "legacy_server_connect": "Consenti connessioni server legacy",
        "concurrent_fragments": "Numero di frammenti concorrenti da scaricare",
        "xff": "Strategia header X-Forwarded-For",
        "user_agent": "Header User-Agent",
        "impersonate": "Impersonazione browser",
        "referer": "Header Referer",
        "geo_bypass": "Bypassa restrizioni geografiche",
        "hls_use_mpegts": "Usa MPEG-TS per HLS",
        "no_part": "Non usare file .part",
        "no_continue": "Non riprendere download parziali",
        "audio_format": "Formato audio",
        "video_format": "Formato video",
        "merge_output_format": "Formato output merge",
        "send_as_file": "Invia come file",
        "username": "Nome utente",
        "password": "Password",
        "twofactor": "Codice autenticazione a due fattori",
        "min_filesize": "Dimensione file minima (MB)",
        "max_filesize": "Dimensione file massima (MB)",
        "playlist_items": "Elementi playlist",
        "date": "Data",
        "datebefore": "Data prima",
        "dateafter": "Data dopo",
        "http_headers": "Header HTTP",
        "sleep_interval": "Intervallo sleep",
        "max_sleep_interval": "Intervallo sleep massimo",
        "retries": "Numero di tentativi",
        "http_chunk_size": "Dimensione chunk HTTP",
        "sleep_subtitles": "Sleep per sottotitoli"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ Configurazione Argomenti yt-dlp</b>\n\n<blockquote>📋 <b>Gruppi:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ Configurazione Argomenti yt-dlp</b>\n\n"
        "<blockquote>📋 <b>Gruppi:</b>\n"
        "• ✅/❌ <b>Boolean</b> - Interruttori True/False\n"
        "• 📋 <b>Select</b> - Scegli dalle opzioni\n"
        "• 🔢 <b>Numeric</b> - Input numerico\n"
        "• 📝🔧 <b>Text</b> - Input testo/JSON</blockquote>\n\n"
        "Queste impostazioni saranno applicate a tutti i tuoi download."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Attendi..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Si è verificato un errore"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Modalità input chiusa automaticamente per inattività (5 minuti)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ L'input contiene contenuto potenzialmente pericoloso: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Input troppo lungo (max 1000 caratteri)"
    ARGS_INVALID_URL_MSG = "❌ Formato URL non valido. Deve iniziare con http:// o https://"
    ARGS_INVALID_JSON_MSG = "❌ Formato JSON non valido"
    ARGS_NUMBER_RANGE_MSG = "❌ Il numero deve essere tra {min_val} e {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Formato numero non valido"
    ARGS_DATE_FORMAT_MSG = "❌ La data deve essere in formato YYYYMMDD (es., 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ L'anno deve essere tra 1900 e 2100"
    ARGS_MONTH_RANGE_MSG = "❌ Il mese deve essere tra 01 e 12"
    ARGS_DAY_RANGE_MSG = "❌ Il giorno deve essere tra 01 e 31"
    ARGS_INVALID_DATE_MSG = "❌ Formato data non valido"
    ARGS_INVALID_XFF_MSG = "❌ XFF deve essere 'default', 'never', codice paese (es., US), o blocco IP (es., 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "Nessun argomento personalizzato impostato. Tutti i parametri usano valori predefiniti."
    ARGS_RESET_SUCCESS_MSG = "✅ Tutti gli argomenti reimpostati ai valori predefiniti."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Testo troppo lungo. Massimo 500 caratteri."
    ARGS_ERROR_PROCESSING_MSG = "❌ Errore nell'elaborazione dell'input. Per favore riprova."
    ARGS_BOOL_INPUT_MSG = "❌ Inserisci \"Vero\" o \"Falso\" per l'opzione Invia come file."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Si prega di fornire un numero valido."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Invia <code>True</code> o <code>False</code> per abilitare/disabilitare questa opzione."
    ARGS_JSON_VALUE_REQUEST_MSG = "Invia un JSON valido."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Non hai ancora tag."
    TAGS_MESSAGE_CLOSED_MSG = "Messaggio di tag chiuso."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Sottotitoli disabilitati e modalità Chiedi sempre disattivata."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUB Chiedi sempre abilitato."
    SUBS_LANGUAGE_SET_MSG = "✅ Lingua dei sottotitoli impostata su: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️WARNING: due to high CPU impact this function is very slow (near real-time) and limited to:\n"
        "- 720p max quality\n"
        "- 1.5 hour max duration\n"
        "- 500mb max video size</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Comandi rapidi:</b>\n"
        "• <code>/subs off</code> - disabilita sottotitoli\n"
        "• <code>/subs on</code> - abilita modalità Always Ask\n"
        "• <code>/subs ru</code> - imposta lingua\n"
        "• <code>/subs ru auto</code> - imposta lingua con AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 I sottotitoli sono disabilitati"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Lingua selezionata: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Scarica sottotitoli in corso..."
    SUBS_DISABLED_ERROR_MSG = "❌ I sottotitoli sono disabilitati. Usa /subs per configurare."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Il download dei sottotitoli è supportato solo per YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Subtitles</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Language:</b> {lang}\n"
        "<b>Type:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 File SRT sottotitoli inviato all'utente."
    SUBS_ERROR_PROCESSING_MSG = "❌ Errore nell'elaborazione del file sottotitoli."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Impossibile scaricare i sottotitoli."
    SUBS_ERROR_MSG = "❌ Errore nel download dei sottotitoli: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Dimensione parte divisa impostata su: {size}"
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
        "**Comandi rapidi:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Esempi:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Menu chiuso."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Impostazioni Bot</b>\n\nScegli una categoria:"
    SETTINGS_MENU_CLOSED_MSG = "Menu chiuso."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Clean Options</b>\n\nChoose what to clean:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nChoose an action:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIA</b>\n\nChoose an action:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nChoose an action:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ MORE COMMANDS</b>\n\nChoose an action:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Comando eseguito."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Limite alluvioni. Riprova più tardi."
    SETTINGS_HINT_SENT_MSG = "Suggerimento inviato."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Assistente di ricerca aperto."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Comando sconosciuto."
    SETTINGS_HINT_CLOSED_MSG = "Suggerimento chiuso."
    SETTINGS_HELP_SENT_MSG = "Inviato help txt all'utente"
    SETTINGS_MENU_OPENED_MSG = "Menu /settings aperto"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍Assistente di ricerca chiuso"
    SEARCH_CLOSED_MSG = "Chiuso"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Procura {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Errore durante il salvataggio delle impostazioni del proxy."
    PROXY_MENU_TEXT_MSG = "Abilitare o disabilitare l'utilizzo del server proxy per tutte le operazioni yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Abilitare o disabilitare l'utilizzo dei server proxy ({config_count} + {file_count} disponibili) per tutte le operazioni yt-dlp?\n\nQuando è abilitato TUTTO (AUTO), i proxy verranno selezionati utilizzando il metodo casuale."
    PROXY_MENU_CLOSED_MSG = "Menù chiuso."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy abilitato. Tutte le operazioni yt-dlp utilizzeranno il proxy."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy abilitato. Tutte le operazioni yt-dlp utilizzeranno server proxy {count} con metodo di selezione {method}."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Proxy abilitato (modalità ALL AUTO).\n\n📊 Il bot proverà i proxy in questo ordine:\n1️⃣ {config_count} proxy da Config.py\n2️⃣ {file_count} proxy dal file TXT/proxy.txt\n\n🔄 Tutti i proxy verranno provati in sequenza fino alla connessione riuscita."
    PROXY_DISABLED_MSG = "❌Proxy disabilitato."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Errore durante il salvataggio delle impostazioni del proxy."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy abilitato."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy disabilitato."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ ATTENDERE FINO AL TERMINE DEL DOWNLOAD PRECEDENTE"
    AUDIO_HELP_MSG = (
        "<b>🎧 Audio Download Command</b>\n\n"
        "Utilizzo: <code>/audio URL</code>\n\n"
        "<b>Esempi:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Vedi anche: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Suggerimento audio chiuso."
    PLAYLIST_HELP_CLOSED_MSG = "Aiuto playlist chiuso."
    USERLOGS_CLOSED_MSG = "Messaggio di registro chiuso."
    HELP_CLOSED_MSG = "Aiuto chiuso."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW Blur Settings</b>\n\nNSFW content is <b>{status}</b>.\n\nChoose whether to blur NSFW content:"
    NSFW_MENU_CLOSED_MSG = "Menù chiuso."
    NSFW_BLUR_DISABLED_MSG = "Sfocatura NSFW disabilitata."
    NSFW_BLUR_ENABLED_MSG = "Sfocatura NSFW abilitata."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW blur disabled."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW blur enabled."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Abilitare o disabilitare l'invio di MediaInfo per i file scaricati?"
    MEDIAINFO_MENU_CLOSED_MSG = "Menù chiuso."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo abilitato. Dopo il download, verranno inviate le informazioni sul file."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo disabilitato."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo abilitato."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo disabilitato."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Elenco Formati Disponibili</b>\n\n"
        "Ottieni i formati video/audio disponibili per un URL.\n\n"
        "<b>Utilizzo:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Esempi:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Come usare gli ID formato:</b>\n"
        "Dopo aver ottenuto l'elenco, usa l'ID formato specifico:\n"
        "• <code>/format id 401</code> - scarica formato 401\n"
        "• <code>/format id401</code> - stesso di sopra\n"
        "• <code>/format id140 audio</code> - scarica formato 140 come audio MP3\n\n"
        "Questo comando mostrerà tutti i formati disponibili che possono essere scaricati."
    )
    LIST_PROCESSING_MSG = "🔄 Recupero formati disponibili..."
    LIST_INVALID_URL_MSG = "❌ Fornisci un URL valido che inizi con http:// o https://"
    LIST_CAPTION_MSG = (
        "📃 Formati disponibili per:\n<code>{url}</code>\n\n"
        "💡 <b>Come impostare il formato:</b>\n"
        "• <code>/format id 134</code> - Scarica ID formato specifico\n"
        "• <code>/format 720p</code> - Scarica per qualità\n"
        "• <code>/format best</code> - Scarica migliore qualità\n"
        "• <code>/format ask</code> - Chiedi sempre la qualità\n\n"
        "{audio_note}\n"
        "📋 Usa ID formato dall'elenco sopra"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Formati solo audio:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Scarica formato 140 come audio MP3\n"
        "• <code>/format id140 audio</code> - stesso di sopra\n"
        "Questi verranno scaricati come file audio MP3.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Errore durante l'invio del file dei formati: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Failed to get formats:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Si è verificato un errore durante l'elaborazione del comando"
    LIST_ERROR_CALLBACK_MSG = "Si è verificato un errore"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 How to use format IDs:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "After getting the list, use specific format ID:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - download format 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - same as above\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - download format 140 as MP3 audio\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - same as above\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Audio-only formats detected: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "These formats will be downloaded as MP3 audio files.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Video-only formats:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Utilizza l'ID formato dall'elenco sopra"
    
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
    LINK_INVALID_URL_MSG = "❌ Fornisci un URL valido"
    LINK_PROCESSING_MSG = "🔗 Ottenere il collegamento diretto..."
    LINK_DURATION_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
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
    KEYBOARD_ACTIVATED_MSG = "🎹 tastiera attivata!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Tastiera nascosta"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 Tastiera 1x3 attivata!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 Tastiera 2x3 attivata!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Tastiera Emoji attivata!"
    KEYBOARD_ERROR_APPLYING_MSG = "Errore durante l'applicazione dell'impostazione della tastiera {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Format set to: Always Ask. You will be prompted for quality each time you send a URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format set to: Always Ask. Now you will be prompted for quality each time you send a URL."
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
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Custom format menu closed"
    FORMAT_CODEC_SET_MSG = "✅ Codec set to {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Scelta del browser aggiornata."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Accesso negato. Solo amministratore."
    ACCESS_DENIED_ADMIN = "❌ Accesso negato. Solo amministratore."
    WELCOME_MASTER = "Benvenuto Maestro 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Spiacenti... Si è verificato un errore durante il download."
    SIZE_LIMIT_EXCEEDED = "❌ La dimensione del file supera il limite di {max_size_gb} GB. Seleziona un file più piccolo entro le dimensioni consentite."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Script non trovato: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Download del nuovo dump Firebase utilizzando {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Cache Firebase ricaricata con successo!"
    ADMIN_CACHE_FAILED_MSG = "❌ Impossibile ricaricare la cache di Firebase. Controlla se {cache_file} esiste."
    ADMIN_ERROR_RELOADING_MSG = "❌ Errore durante il ricaricamento della cache: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Errore durante l'esecuzione di {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Messaggio promozionale inviato a tutti gli altri utenti</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Impossibile inviare il messaggio promozionale. Prova a rispondere a un messaggio\nO si è verificato un errore</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ L'utente non ha ancora scaricato alcun contenuto...</b> Non esiste nei log"
    ADMIN_INVALID_COMMAND_MSG = "❌ Comando non valido"
    ADMIN_NO_DATA_FOUND_MSG = "❌ Nessun dato trovato nella cache per <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ La coda è vuota: nessuno ha ancora lasciato il canale."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Coda ban</b>\nTotale in attesa: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (a sinistra: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… e {extra} altri utenti."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Usa /block_user mostra • tutto • automatico • 10 secondi"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Utenti bloccati dalla coda: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Blocco automatico abilitato: i nuovi usciti verranno bannati immediatamente."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Blocco automatico disabilitato."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Finestra di blocco automatico programmata impostata su ogni {interval}."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Registro delle attività del canale per le ultime {hours} ore (2 giorni)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 Ultime {hours} ore (2 giorni): entrato {joined}, lasciato {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Nessuna attività nelle ultime {hours} ore (2 giorni)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Totale: 🟢 {joined} iscritti, 🔴 {left} rimasti."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Nessun accesso al registro delle attività del canale. I bot non possono leggere i log di amministrazione. Fornisci CHANNEL_GUARD_SESSION_STRING nella configurazione con una sessione utente per abilitare questa funzione."
    BAN_TIME_USAGE_MSG = "❌ Utilizzo: {command} <10s|6m|5h|4g|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Utilizza formati come 10s, 6m, 5h, 4d, 3w, 2M o 1y."
    BAN_TIME_SET_MSG = "🕒 Intervallo di scansione del registro del canale impostato su {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Rapporto di scansione canale\n"
        "Eseguito alle: {run_ts}\n"
        "Intervallo: {interval}\n"
        "Nuovi abbandoni: {new_leavers}\n"
        "Ban automatici: {auto_banned}\n"
        "In attesa: {pending}\n"
        "Ultimo event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Utilizzo: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 L'amministratore non può eliminare un amministratore"
    ADMIN_USER_BLOCKED_MSG = "Utente bloccato 🔒❌\n \nID: <code>{user_id}</code>\nData di blocco: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> è già bloccato ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Scusate! Non sei un amministratore"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Utilizzo: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Utente sbloccato 🔓✅\n \nID: <code>{user_id}</code>\nData di sblocco: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> è già sbloccato ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Utenti sbloccati: {count}\n⏱ Timestamp: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Uso: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Utente ignorato 👁️❌\n \nID: <code>{user_id}</code>\nData di ignorato: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> è già ignorato ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Uso: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Utente non più ignorato 👁️✅\n \nID: <code>{user_id}</code>\nData di non più ignorato: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> non è ignorato ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Tempo di esecuzione del bot -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Fornisci un URL per cui cancellare la cache.\nUso: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Fornisci un URL valido.\nUso: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Cache cancellata con successo per URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Nessuna cache trovata per questo collegamento."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Errore durante lo svuotamento della cache: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Accesso negato. Solo amministratore."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Esecuzione dello script di aggiornamento dell'elenco porno: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Script completato con successo!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Script completato con successo!\n\nOutput:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Script fallito con codice di ritorno {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Errore durante l'esecuzione dello script: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Ricaricamento delle cache relative al porno e al dominio..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Cache porno ricaricati con successo!\n\n"
        "📊 Stato cache corrente:\n"
        "• Domini porno: {porn_domains}\n"
        "• Parole chiave porno: {porn_keywords}\n"
        "• Siti supportati: {supported_sites}\n"
        "• LISTA BIANCA: {whitelist}\n"
        "• LISTA GRIGIA: {greylist}\n"
        "• LISTA NERA: {black_list}\n"
        "• PAROLE CHIAVE BIANCHE: {white_keywords}\n"
        "• DOMINI PROXY: {proxy_domains}\n"
        "• DOMINI PROXY_2: {proxy_2_domains}\n"
        "• QUERY PULITA: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Errore durante il ricaricamento della cache del porno: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Fornisci un URL da controllare.\nUso: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Fornisci un URL valido.\nUso: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Controllo URL per contenuti NSFW...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Risultato Controllo Porn</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Stato:</b> <b>{status_text}</b>\n\n"
        "<b>Explanation:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Errore durante il controllo dell'URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Biscotti puliti."
    CLEAN_LOGS_CLEANED_MSG = "tronchi puliti."
    CLEAN_TAGS_CLEANED_MSG = "tag puliti."
    CLEAN_FORMAT_CLEANED_MSG = "formato pulito."
    CLEAN_SPLIT_CLEANED_MSG = "diviso pulito."
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfo pulito."
    CLEAN_SUBS_CLEANED_MSG = "Impostazioni dei sottotitoli pulite."
    CLEAN_KEYBOARD_CLEANED_MSG = "Impostazioni della tastiera pulite."
    CLEAN_ARGS_CLEANED_MSG = "Impostazioni degli argomenti pulite."
    CLEAN_NSFW_CLEANED_MSG = "Impostazioni NSFW pulite."
    CLEAN_PROXY_CLEANED_MSG = "Impostazioni proxy pulite."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Impostazioni di attesa del diluvio pulite."
    CLEAN_ALL_CLEANED_MSG = "Tutti i file puliti."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nScegli un'azione:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅File cookie salvato"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Convalida saltata per i cookie non YouTube"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Il file cookie esiste ma ha un formato errato"
    COOKIES_FILE_NOT_FOUND_MSG = "❌File cookie non trovato."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Avvio test cookie YouTube...\n\nAttendi mentre controllo e valido i tuoi cookie."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ I tuoi cookie YouTube esistenti funzionano correttamente!\n\nNon è necessario scaricare nuovi cookie."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ I tuoi cookie YouTube esistenti sono scaduti o non validi.\n\n🔄 Download di nuovi cookie in corso..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} la fonte dei cookie non è configurata!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} la fonte del cookie deve essere un file .txt!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Range limit exceeded: {range_count} files requested (maximum {max_img_files}).\n\nUse one of these commands to download maximum available files:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Chiudi"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Limite media superato: {count} file richiesti (massimo {max_count}).\n\nUsa uno di questi comandi per scaricare il massimo di file disponibili:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Trovato <b>{count}</b> elementi multimediali dal collegamento"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Seleziona l'intervallo di download:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Rappresentazione del browser"
    ARGS_REFERER_DESC_MSG = "Intestazione del referente"
    ARGS_USER_AGENT_DESC_MSG = "Intestazione agente utente"
    ARGS_GEO_BYPASS_DESC_MSG = "Bypassare le restrizioni geografiche"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Controlla il certificato SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "Scarica streaming live dall'inizio"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Non scaricare streaming live dall'inizio"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Utilizza il contenitore MPEG-TS per i video HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "Scarica solo un singolo video, non una playlist"
    ARGS_NO_PART_DESC_MSG = "Non utilizzare file .part"
    ARGS_NO_CONTINUE_DESC_MSG = "Non riprendere i download parziali"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Formato audio per l'estrazione"
    ARGS_EMBED_METADATA_DESC_MSG = "Incorpora metadati nel file video"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Incorpora la miniatura nel file video"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Scrivi la miniatura nel file"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Numero di frammenti simultanei da scaricare"
    ARGS_FORCE_IPV4_DESC_MSG = "Forza le connessioni IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "Forza le connessioni IPv6"
    ARGS_XFF_DESC_MSG = "Strategia di intestazione X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "Dimensione blocco HTTP (byte)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Dormi prima del download dei sottotitoli (secondi)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Consenti connessioni server legacy"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Sopprimi la convalida del certificato HTTPS"
    ARGS_USERNAME_DESC_MSG = "Nome utente dell'account"
    ARGS_PASSWORD_DESC_MSG = "Password dell'account"
    ARGS_TWOFACTOR_DESC_MSG = "Codice di autenticazione a due fattori"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Ignora gli errori di download e continua"
    ARGS_MIN_FILESIZE_DESC_MSG = "Dimensione minima del file (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Dimensione massima del file (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Elementi della playlist da scaricare (ad esempio, 1,3,5 o 1-5)"
    ARGS_DATE_DESC_MSG = "Scarica i video caricati in questa data (AAAAMMGG)"
    ARGS_DATEBEFORE_DESC_MSG = "Scarica i video caricati prima di questa data (AAAAMMGG)"
    ARGS_DATEAFTER_DESC_MSG = "Scarica i video caricati dopo questa data (AAAAMMGG)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Intestazioni HTTP personalizzate (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Intervallo di sospensione tra le richieste (secondi)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Intervallo massimo di sonno (secondi)"
    ARGS_RETRIES_DESC_MSG = "Numero di tentativi"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Formato contenitore video"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Formato del contenitore di output per l'unione"
    ARGS_SEND_AS_FILE_DESC_MSG = "Invia tutti i media come documento invece che come media"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Impersonare"
    ARGS_REFERER_SHORT_MSG = "Referente"
    ARGS_GEO_BYPASS_SHORT_MSG = "Bypass geografico"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Controlla il certificato"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Inizio dal vivo"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Nessun inizio dal vivo"
    ARGS_USER_AGENT_SHORT_MSG = "Agente utente"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Nessuna playlist"
    ARGS_NO_PART_SHORT_MSG = "Nessun Part"
    ARGS_NO_CONTINUE_SHORT_MSG = "Nessun Continue"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Formato Audio"
    ARGS_EMBED_METADATA_SHORT_MSG = "Incorpora Meta"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Incorpora Thumb"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Scrivi Thumb"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Concorrenti"
    ARGS_FORCE_IPV4_SHORT_MSG = "Forza IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Forza IPv6"
    ARGS_XFF_SHORT_MSG = "Intestazione XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Dimensione Chunk"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Sleep Sottotitoli"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Connessione Legacy"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Nessun Controllo Cert"
    ARGS_USERNAME_SHORT_MSG = "Nome Utente"
    ARGS_PASSWORD_SHORT_MSG = "Password"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Ignora Errori"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Dimensione Min"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Dimensione Max"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Elementi playlist"
    ARGS_DATE_SHORT_MSG = "Data"
    ARGS_DATEBEFORE_SHORT_MSG = "Data Prima"
    ARGS_DATEAFTER_SHORT_MSG = "Data Dopo"
    ARGS_HTTP_HEADERS_SHORT_MSG = "Header HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Intervallo Sleep"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Sleep Max"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Formato Video"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Formato Merge"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Invia Come File"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ Il file è troppo grande. La dimensione massima è 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Sono ammessi solo file del seguente formato .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ Il file non assomiglia a cookie.txt (non c'è la riga '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ Errore durante la lettura del file: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Il file cookie esiste e ha il formato corretto"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ Il file cookie {service} è troppo grande! Massimo 100KB, ottenuto {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} file cookie scaricato e salvato come cookie.txt nella tua cartella.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ La fonte cookie {service} non è disponibile (stato {status}). Riprova più tardi."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Errore durante il download del file cookie {service}. Per favore riprova più tardi."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ L'utente ha fornito un nuovo file cookie.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie aggiornato con successo:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌Cookie non valido.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ Le origini dei cookie di YouTube non sono configurate!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Accesso negato. Solo amministratore."
    ADMIN_USER_LOGS_TOTAL_MSG = "Totale: <b>{total}</b>\n<b>{user_id}</b> - log (Ultimi 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 tastiera attivata!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Lingua dei sottotitoli impostata su: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Lingua dei sottotitoli impostata su: {flag} {name} con AUTO/TRANS abilitato."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Menu della lingua dei sottotitoli chiuso."
    SUBS_DOWNLOADING_MSG = "💬 Download dei sottotitoli..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Ricaricamento della cache di Firebase in memoria..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Nessun COOKIE_URL configurato. Utilizza /cookie o carica cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Scaricamento di cookie da URL remoto..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ COOKIE_URL fallback deve puntare a un file .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Il file dei cookie di fallback è troppo grande (>100 KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ File cookie di YouTube scaricato tramite fallback e salvato come cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fonte cookie di riserva non disponibile (stato {status}). Prova /cookie o carica cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Errore durante il download del cookie di fallback. Prova /cookie o carica cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Errore imprevisto durante il download dei cookie di fallback."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} browser non installato."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookie salvati utilizzando il browser: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Impossibile salvare i cookie: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ I cookie di YouTube funzionano correttamente"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube cookies are expired or invalid\n\nUse /cookie to get new cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - formato personalizzato\n• <code>/format 720</code> - qualità 720p\n• <code>/format 4k</code> - qualità 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Suggerimento inviato."
    FORMAT_MKV_TOGGLE_MSG = "MKV è ora {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Nessun URL remoto configurato"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Formato file non valido"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ File troppo grande"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookie scaricati correttamente"
    COOKIES_SERVER_ERROR_MSG = "❌ Errore del server {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Download non riuscito"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Errore imprevisto"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Browser non installato."
    COOKIES_MENU_CLOSED_MSG = "Menù chiuso."
    COOKIES_HINT_CLOSED_MSG = "Suggerimento sui cookie chiuso."
    IMG_HELP_CLOSED_MSG = "Aiuto chiuso."
    SUBS_LANGUAGE_UPDATED_MSG = "Impostazioni della lingua dei sottotitoli aggiornate."
    SUBS_MENU_CLOSED_MSG = "Menu della lingua dei sottotitoli chiuso."
    KEYBOARD_SET_TO_MSG = "Tastiera impostata su {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Impostazione dell'elaborazione dell'errore"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo abilitato."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo disabilitato."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Sfocatura NSFW disabilitata."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Sfocatura NSFW abilitata."
    SETTINGS_MENU_CLOSED_MSG = "Menu chiuso."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Attesa flood attiva. Riprova più tardi."
    OTHER_HELP_CLOSED_MSG = "Aiuto chiuso."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Messaggio log chiuso."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menu chiuso."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Dimensione non valida."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Errore durante l'invio di MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Si è verificato un errore: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - tutti i registri"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - tutti {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Scarica dall'URL remoto"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Apri il browser"
    SELECT_BROWSER_MSG = "Selezionare un browser da cui scaricare i cookie:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Nessun browser trovato su questo sistema. Puoi scaricare cookie da URL remoti o monitorare lo stato del browser:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Apri browser</b>: per monitorare lo stato del browser nella mini-app"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Impossibile eseguire /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Limite alluvioni. Riprova più tardi."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Impossibile aprire il menu dei cookie del browser"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Salva come suggerimento sui cookie chiuso."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Usage:</b>\n<code>/link [quality] URL</code>\n\n<b>Examples:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - best quality\n• /link 720 https://youtube.com/watch?v=... - 720p or lower\n• /link 720p https://youtube.com/watch?v=... - same as above\n• /link 4k https://youtube.com/watch?v=... - 4K or lower\n• /link 8k https://youtube.com/watch?v=... - 8K or lower</blockquote>\n\n<b>Quality:</b> from 1 to 10000 (e.g., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K quality"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Impossibile ottenere i collegamenti agli streaming"
    LINK_ERROR_GETTING_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Indice cookie YouTube non valido: {selected_index}. L'intervallo disponibile è 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Download e verifica cookie YouTube in corso...\n\nTentativo {attempt} di {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Download e verifica cookie YouTube in corso...\n\nTentativo {attempt} di {total}\n🔍 Test cookie in corso..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ Cookie YouTube scaricati e validati con successo!\n\nFonte utilizzata {source} di {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Tutti i cookie YouTube sono scaduti o non disponibili!\n\nContatta l'amministratore del bot per sostituirli."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ Limite di tentativi cookie YouTube superato!\n\n🔢 Massimo: {limit} tentativi all'ora\n⏰ Riprova più tardi"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Il tag #{wrong} contiene caratteri non consentiti. Sono consentiti solo lettere, cifre e _.\nUsa: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Argomento non valido!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Lingua dei sottotitoli impostata: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Esempio: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Lingua selezionata: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Modalità Always Ask {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 I sottotitoli sono disabilitati"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Impostazioni Sottotitoli</b>\n\n{status_text}\n\nSeleziona lingua sottotitoli:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - disabilita sottotitoli\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Impostazioni Sottotitoli</b>\n\n{status_text}\n\nSeleziona lingua sottotitoli:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Title:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- qualità massima 720p\n- durata massima 1.5 ore\n- dimensione video massima 500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️ATTENZIONE: a causa dell'elevato impatto sulla CPU questa funzione è molto lenta (quasi in tempo reale) e limitata a:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Quick commands:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - disable subtitles\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - enable Always Ask mode\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - set language\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - set language with AUTO/TRANS enabled\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - enable Always Ask mode\n"
    SUBS_AUTO_SUBS_TEXT = "(sostituzioni automatiche)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Modalità abbonamenti automatici {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS disabilitato tramite comando: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Chiedi sempre abilitato tramite comando: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "Lingua SUBS impostata tramite comando: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "Lingua SUBS + modalità automatica impostata tramite comando: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "L'utente ha aperto il menu /subs."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "L'utente ha impostato la lingua dei sottotitoli su: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "L'utente ha attivato la modalità AUTO/TRANS su: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "L'utente ha attivato la modalità Chiedi sempre su: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "L'utente ha richiesto i cookie dal browser."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Tastiera di selezione del browser inviata solo con i browser installati."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Selezione del browser chiusa."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "COOKIE_URL di riserva utilizzato correttamente (origine nascosta)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "COOKIE_URL fallback non riuscito: status={status} (nascosto)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Errore imprevisto COOKIE_URL di fallback: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Browser {browser} non installato."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Cookie salvati utilizzando il browser: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "File cookie salvato per l'utente {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "Il file cookie esiste, ha il formato corretto e i cookie di YouTube funzionano."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Il file cookie esiste e ha il formato corretto, ma i cookie di YouTube sono scaduti."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Il file cookie esiste e ha il formato corretto."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Il file cookie esiste ma ha un formato errato."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "File cookie non trovato."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{service} L'URL del cookie è vuoto per l'utente {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} L'URL del cookie non è .txt (nascosto)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} file cookie troppo grande: {size} byte (origine nascosta)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{service} file cookie scaricato per l'utente {user_id} (fonte nascosta)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Script non trovato: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Impossibile inviare il messaggio di stato iniziale"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Errore durante l'esecuzione di {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Cache Firebase ricaricata dall'attività automatica."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Cache Firebase ricaricata dall'amministratore."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Errore durante il ricaricamento della cache Firebase: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Broadcast avviato. Testo:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Messaggio broadcast inviato a tutti gli utenti."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Impossibile trasmettere il messaggio: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "L'amministratore {user_id} ha cancellato la cache per l'URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "L'amministratore {user_id} ha avviato lo script di aggiornamento dell'elenco porno: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Script di aggiornamento dell'elenco porno completato con successo dall'amministratore {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Script di aggiornamento dell'elenco porno non riuscito dall'amministratore {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "L'amministratore {user_id} ha provato a eseguire uno script inesistente: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Errore durante l'esecuzione dello script di aggiornamento porno da parte dell'amministratore {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "L'amministratore {user_id} ha avviato la ricarica della cache del porno"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Errore durante il ricaricamento della cache porno da parte dell'amministratore {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "L'amministratore {user_id} ha controllato l'URL per NSFW: {url} - Risultato: {status}"
    
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
    LINK_EXTRACTED_LOG_MSG = "Link diretto estratto per l'utente {user_id} da {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Impossibile estrarre il collegamento diretto per l'utente {user_id} da {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Errore nel comando di collegamento per l'utente {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "L'utente {user_id} ha impostato la tastiera su {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "L'utente {user_id} ha impostato la tastiera su {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo impostato tramite comando: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "L'utente ha aperto il menu /mediainfo."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: chiuso."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo abilitato."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo disabilitato."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Dimensione divisa impostata su {size} byte tramite argomento."
    SPLIT_MENU_OPENED_LOG_MSG = "Menu aperto/diviso dall'utente."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Selezione divisa chiusa."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Dimensione divisa impostata su {size} byte."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Proxy impostato tramite comando: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "L'utente ha aperto il menu /proxy."
    PROXY_MENU_CLOSED_LOG_MSG = "Procura: chiusa."
    PROXY_ENABLED_LOG_MSG = "Proxy abilitato."
    PROXY_DISABLED_LOG_MSG = "Proxy disabilitato."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Messaggio di aiuto chiuso."
    AUDIO_HELP_SHOWN_LOG_MSG = "Mostrato l'aiuto /audio"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "L'utente ha richiesto aiuto per la playlist."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Guida alla playlist chiusa."
    AUDIO_HINT_CLOSED_LOG_MSG = "Suggerimento audio chiuso."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Menu di collegamento diretto creato tramite il pulsante LINK per l'utente {user_id} da {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Impossibile estrarre il collegamento diretto tramite il pulsante LINK per l'utente {user_id} da {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "Comando LIST eseguito per l'utente {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Incorpora Rapido: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Menu Chiedi Sempre inviato per {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Creato menu qualità in cache per utente {user_id} dopo errore: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Errore menu Chiedi Sempre per {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Il formato viene corretto tramite le impostazioni di /args"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Audio"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Video"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Video"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Avanti ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Precedente"
    SUBTITLES_NEXT_BUTTON_MSG = "Avanti ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Tutti i campi di testo sono vuoti"
    SENDER_VIDEO_DURATION_MSG = "Durata del video:"
    SENDER_UPLOADING_FILE_MSG = "📤 Caricamento file..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Caricamento video..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Durata del video:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 file caricato."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Informazioni video"
    DOWN_UP_NUMBER_MSG = "Numero"
    DOWN_UP_TITLE_MSG = "Titolo"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Video scaricato."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Elaborazione per il caricamento..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 File della parte divisa {part} caricato"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Caricamento completato"
    DOWN_UP_FILES_UPLOADED_MSG = "file caricati"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚Chiudi"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CODICE"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBBI"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬SOTTOS"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐Browser"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Ottenere il collegamento diretto..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Ottenere i formati disponibili..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Ottenere la descrizione del video..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Errore durante il recupero della descrizione: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ La descrizione del video non è disponibile"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Errore durante l'invio della descrizione: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Descrizione del video inviata all'utente {user_id} per {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Inizio gallery-dl..."
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Durata:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Formato:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Browser:</b> aprire nel browser web"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Formati disponibili per"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Come utilizzare gli ID formato:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Dopo aver ottenuto l'elenco, utilizza l'ID formato specifico:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - scarica il formato 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - come sopra"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - scarica il formato 140 come audio MP3"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Formati solo audio rilevati"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Questi formati verranno scaricati come file audio MP3."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Come impostare il formato:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Scarica l'ID del formato specifico"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Scarica in base alla qualità"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Scarica la migliore qualità"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Richiedi sempre la qualità"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Formati solo audio:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Scarica il formato 140 come audio MP3"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Questi verranno scaricati come file audio MP3."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Utilizza l'ID formato dall'elenco sopra"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Errore: messaggio originale non trovato."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Pagina dei formati"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Errore durante la visualizzazione del menu formati"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Errore durante il recupero dei formati"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Errore nel reperire i formati disponibili."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Per favore riprova più tardi."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp non può elaborare questo contenuto"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Il sistema consiglia invece di utilizzare gallery-dl."
    ALWAYS_ASK_OPTIONS_MSG = "**Opzioni:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Per le gallerie di immagini: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Per immagini singole: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl spesso funziona meglio per Instagram, Twitter e altri contenuti dei social media."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Prova Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Formato corretto tramite /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Sottotitoli"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Audio doppiato"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — I sottotitoli sono disponibili"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Scegli la lingua dei sottotitoli"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Iscrizione non trovata e non verrà incorporata"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Repost istantaneo dalla cache"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Scegli la lingua dell'audio"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW viene pagato (⭐️$0,02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Scegli la qualità del download"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Scarica immagine (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Ottieni il collegamento diretto al video"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃: mostra l'elenco dei formati disponibili"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Modifica estensione/codec video"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Incorpora"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Estrai solo l'audio"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW viene pagato (⭐️$0,02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Repost istantaneo dalla cache"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Scegli la lingua dell'audio"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Migliore"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Altro"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝solo iscritti"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Raggruppamento intelligente"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Aggiunta riga di pulsanti di azione (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Aggiunte righe di pulsanti di azione (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Aggiunti pulsanti in basso alla riga esistente"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Creata nuova riga inferiore"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Nessun video trovato nella playlist"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "URL non supportato"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Non è stato trovato alcun video"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Nessun video trovato"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Nessun supporto trovato"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Questo tweet non contiene"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Errore nel recupero delle informazioni sul video:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Errore durante il recupero delle informazioni sul video"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Prova il comando <code>/clean</code> e riprova. Se l'errore persiste, YouTube richiede l'autorizzazione. Aggiorna cookies.txt tramite <code>/cookie</code> o <code>/cookies_from_browser</code> e riprova."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Menù chiuso."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛Selezione manuale della qualità"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Scegli la qualità manualmente poiché il rilevamento automatico non è riuscito:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Tutti i formati disponibili"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Qualità disponibili (dalla cache)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Utilizzo delle qualità memorizzate nella cache: i nuovi formati potrebbero non essere disponibili"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Download del formato"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Download"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Download con monitoraggio dello stato di avanzamento..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Download utilizzando il formato:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Scaricare l'audio utilizzando il formato:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Download della migliore qualità..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Download del dump del database..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Download"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Pagina dei formati"
    ALWAYS_ASK_FROM_CACHE_MSG = "(dalla cache)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Errore: messaggio originale non trovato. Potrebbe essere stato cancellato. Si prega di inviare nuovamente il collegamento."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Errore: URL originale non trovato. Si prega di inviare nuovamente il collegamento."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Link diretto ottenuto</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Titolo:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Durata:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Formato:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Streaming video:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Streaming audio:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Impossibile ottenere i collegamenti agli streaming"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Collegamento diretto estratto tramite il menu Chiedi sempre per l'utente {user_id} da {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Impossibile estrarre il collegamento diretto tramite il menu Chiedi sempre per l'utente {user_id} da {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Collegamento diretto estratto tramite down_and_up_with_format per l'utente {user_id} da {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Impossibile estrarre il collegamento diretto tramite down_and_up_with_format per l'utente {user_id} da {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Collegamento diretto estratto tramite down_and_audio per l'utente {user_id} da {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Impossibile estrarre il collegamento diretto tramite down_and_audio per l'utente {user_id} da {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Audio inviato dalla cache."
    AUDIO_PROCESSING_MSG = "🎙️L'audio è in elaborazione..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Download audio in corso:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Si è verificato un errore durante il download dell'audio."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Impossibile estrarre le informazioni audio"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Tipo di file non supportato nella playlist all'indice {index} saltato"
    AUDIO_FILE_NOT_FOUND_MSG = "File audio non trovato dopo il download."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ Impossibile inviare l'audio: La dimensione del file è uguale a 0 B (indice playlist {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ Il file audio è ancora in download, attendere prego..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Caricamento file audio in corso...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Impossibile inviare l'audio: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Audio della playlist inviato: {sent}/{total} file (qualità={quality}) all'utente{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Impossibile scaricare l'audio: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Download annullato per timeout (2 ore)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ File video non trovato: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ Impossibile inviare il video: La dimensione del file è uguale a 0 B (indice playlist {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ Il file video è ancora in download, attendere prego..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Errore durante l'elaborazione del video: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Errore durante l'invio del file di descrizione: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 se vuoi cambiare la didascalia del video, rispondi al video con il nuovo testo</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Nessun sottotitolo rilevato"
    VIDEO_PROGRESS_MSG = "<b>Video:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Audio:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ Limite URL superato: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Elaborazione completata"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Gli intervalli di playlist non sono consentiti in modalità URL multipli. Invia solo URL singoli senza intervalli (*1*5, /vid 1-10, ecc.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Controlla <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>qui</a> se il tuo sito è supportato"
    ERROR_COOKIE_NEEDED_MSG = "Potrebbe essere necessario <code>cookie</code> per scaricare questo video. Innanzitutto, pulisci il tuo spazio di lavoro tramite il comando <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Per Youtube - ottieni <code>cookie</code> tramite il comando <b>/cookie</b>. Per qualsiasi altro sito supportato - invia il tuo cookie (<a href='https://t.me/tg_ytdlp/203'>guida1</a>) (<a href='https://t.me/tg_ytdlp/214'>guida2</a>) e dopo invia di nuovo il link del video."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Scegli la lingua dei sottotitoli"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Nessuna lingua audio alternativa"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Scegli la lingua audio"
    PAGE_NUMBER_MSG = "Pagina {page}"
    TOTAL_PROGRESS_MSG = "Progresso Totale"
    SUBTITLE_MENU_CLOSED_MSG = "Menu sottotitoli chiuso."
    SUBTITLE_LANGUAGE_SET_MSG = "Lingua dei sottotitoli impostata: {value}"
    AUDIO_SET_MSG = "Set audio: {value}"
    FILTERS_UPDATED_MSG = "Filtri aggiornati"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Indietro"
    CLOSE_BUTTON_TEXT = "🔚Chiudi"
    LIST_BUTTON_TEXT = "📃Elenco"
    IMAGE_BUTTON_TEXT = "🖼Immagine"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Qualità non rilevate automaticamente\nUsa il pulsante 'Altro' per vedere tutti i formati disponibili.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Stream Live Rilevato**\n\nIl download di stream live in corso o infiniti non è consentito.\n\nAttendi che lo stream finisca e riprova il download quando:\n• La durata dello stream è nota\n• Lo stream è terminato\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Download live streaming</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Pezzo {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Dimensione massima: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Durata totale: {duration} sec"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Stream Live - Chunk {chunk}</b>\n⏱ Durata: {duration} sec\n📦 Dimensione: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Pezzo {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Download del live streaming completato</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "Pezzi scaricati {chunks}"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Durata totale: {duration} sec"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Download del live streaming interrotto</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "La directory utente è stata eliminata (probabilmente tramite il comando /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "Il file del blocco è stato eliminato (probabilmente tramite il comando /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Lo streaming è terminato"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Seleziona un formato diverso utilizzando il comando \"/format\"."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Link diretto ottenuto</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Title:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Durata:</b> {duration} sec\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Flusso audio:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Errore nell'Elaborazione del File**\n\nIl video è stato scaricato ma non è stato possibile elaborarlo a causa di caratteri non validi nel nome del file.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Errore nell'Elaborazione del File**\n\nIl video è stato scaricato ma non è stato possibile elaborarlo a causa di un errore di argomento non valido.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Motivo:**\n"
        "• Il file scaricato non è un file video\n"
        "• Potrebbe essere un documento (PDF, DOC, ecc.) o un archivio\n\n"
        "**Soluzione:**\n"
        "• Controlla il link - potrebbe portare a un documento, non a un video\n"
        "• Prova un link o una fonte diversa\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Motivo:**\n"
        "• Il file non può essere elaborato come video\n"
        "• Potrebbe non essere un file video o il file è danneggiato\n\n"
        "**Soluzione:**\n"
        "• Controlla il link - potrebbe portare a un documento, non a un video\n"
        "• Prova un link o una fonte diversa\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Formato Non Disponibile**\n\nIl formato video richiesto non è disponibile per questo video.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Format ID {format_id} non trovato per questo video.\n\nFormat ID disponibili: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **Il formato AV1 non è disponibile per questo video.**\n\n**Formati disponibili:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Errore nell'elaborazione del file**\n\nL'audio è stato scaricato ma non è stato possibile elaborarlo a causa di caratteri non validi nel nome del file.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Errore nell'elaborazione del file**\n\nL'audio è stato scaricato ma non è stato possibile elaborarlo a causa di un errore di argomento non valido.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "L'utente ha inserito contenuti vietati. Non può essere scaricato."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "Sfocatura NSFW impostata tramite comando: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "L'utente ha aperto il menu /nsfw."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: chiuso."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Impossibile scaricare il cookie {service}: status={status} (URL nascosto)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Errore durante il download del cookie {service}: {error} (URL nascosto)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Errore imprevisto durante il download del cookie {service} (URL nascosto): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "File cookie aggiornato per l'utente {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Contenuto del cookie non valido fornito dall'utente {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "Gli URL dei cookie di YouTube sono vuoti per l'utente {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "Cookie di YouTube scaricati e convalidati per l'utente {user_id} dalla fonte {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Tutte le origini dei cookie di YouTube non sono riuscite per l'utente {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Errore nel comando check_porn dell'amministratore {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Dimensione parte divisa impostata su {size} byte."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Caricamento del video completato con la suddivisione del file."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Video della playlist inviati: {sent}/{total} file (qualità={quality}) all'utente {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Errore sconosciuto: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Tipo di file non supportato nella playlist all'indice {index} saltato"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg not found. Please install FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Conversione in MP4 non riuscita: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ L'inserimento dei sottotitoli può richiedere molto tempo (fino a 1 min per 1 min di video)!\n🔥 Inizio masterizzazione sottotitoli..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ I sottotitoli non possono essere incorporati a causa dei limiti (qualità/durata/dimensione)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ I sottotitoli non sono disponibili per la lingua selezionata"
    ERROR_SENDING_VIDEO_MSG = "❌ Errore durante l'invio del video: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Video della playlist inviati: {sent}/{total} file."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Download annullato per timeout (2 ore)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Impossibile scaricare il video: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Errore: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON deve essere un oggetto (dizionario)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Formato JSON non valido. Fornisci un JSON valido."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Il valore deve essere compreso tra {min_val} e {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} impostato su: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅Vero"
    ARGS_FALSE_BUTTON_MSG = "❌ Falso"
    ARGS_BACK_BUTTON_MSG = "🔙 Indietro"
    ARGS_CLOSE_BUTTON_MSG = "🔚Chiudi"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅Vero"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Falso"
    ARGS_NOT_SET_MSG = "Non impostato"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ Il formato AV1 non è disponibile per questo video.\n\nFormati disponibili:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Errore durante il download: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ Nessun video trovato nella playlist all'indice {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Conversione video fallita**\n\nIl video non è stato convertito in MP4 a causa di un errore di argomento non valido.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Conversione video fallita**\n\nIl video non è stato convertito in MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Impossibile ottenere i collegamenti agli streaming"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Errore nell'ottenere il link:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ Nessun contenuto trovato nell'indice {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Errore: messaggio originale non trovato."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Errore: URL non trovato."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Questo URL non può essere incorporato."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ Codec {codec} non disponibile per questo video"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ Formato {format} non disponibile per questo video"
    
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
    AA_MP4_BUTTON_MSG = "✅MP4"
    AA_MP4_BUTTON_INACTIVE_MSG = "☑️ MP4"
    AA_MP4_BUTTON_UNAVAILABLE_MSG = "❌ MP4"
    AA_MKV_BUTTON_MSG = "✅MKV"
    AA_MKV_BUTTON_INACTIVE_MSG = "☑️ MKV"
    AA_MKV_BUTTON_UNAVAILABLE_MSG = "❌ MKV"

    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Limite flood. Riprova più tardi."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Controlla Biscotto"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ TUTTO (AUTOMATICO)"
    PROXY_OFF_BUTTON_MSG = "❌ SPENTO"
    PROXY_CLOSE_BUTTON_MSG = "🔚Chiudi"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Seleziona il Paese:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Cancella la selezione del paese"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Paese selezionato: {country} (codice: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Proxy disponibili: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Il bot proverà prima HTTP, poi SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Proxy abilitato automaticamente per il paese selezionato"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Selezione del paese cancellata"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Selezione del paese cancellata"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Paese selezionato: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Utilizzo del paese dal file: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Paesi disponibili dal file: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 Paese selezionato: {country} (codice: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ Proxy abilitato per questo Paese"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ Proxy disabilitato (premi TUTTO (AUTO) per abilitarlo)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ON"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ SPENTO"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Chiudi"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ ON (nessuna sfocatura)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ON (No Blur)"
    NSFW_OFF_BLUR_MSG = "✅ DISATTIVATO (Sfocatura)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ OFF (Blur)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Pulito"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Errore nell'elaborazione del messaggio di risposta per l'utente {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Errore durante l'invio della trasmissione all'utente {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Log di {bot_name}\nUtente: {user_id}\nLog totali: {total}\nOra corrente: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nTotale {path}: {count}\nOra corrente: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Utenti totali: {count}</i>\nUltimi 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Cache porno ricaricate dall'amministratore {admin_id}. Domini: {domains}, Parole chiave: {keywords}, Siti: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Errore durante l'invio del messaggio di timeout: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Scegli lingua</b>"
    LANG_CHANGED_MSG = "✅ Lingua cambiata in {lang_name}"
    LANG_ERROR_MSG = "❌ Errore nel cambiare lingua"
    LANG_CLOSED_MSG = "Selezione lingua chiusa"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "Richiamata [BROWSER]: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Aggiunta del pulsante di monitoraggio del browser con URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "URL di monitoraggio del browser non configurato: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Impostazione tastiera aggiornata!**\n\nNuova impostazione: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Impossibile nascondere la tastiera: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Utilizzo dei cookie YouTube funzionanti per l'estrazione dei collegamenti per l'utente {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Nessun cookie YouTube funzionante disponibile per l'estrazione dei collegamenti per l'utente {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Utilizzo dei cookie di YouTube esistenti per l'estrazione dei collegamenti per l'utente {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Nessun cookie YouTube trovato per l'estrazione dei link per l'utente {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "File cookie globale copiato nella cartella {user_id} dell'utente per l'estrazione del collegamento"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] L'utente {user_id} ha richiesto il comando mediainfo"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] L'utente {user_id} è amministratore: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] L'utente {user_id} è nel canale: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Accesso utente {user_id} negato - non amministratore e non nel canale"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Accesso utente {user_id} concesso"
    MEDIAINFO_CALLBACK_MSG = "Richiamata [MEDIAINFO]: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Questo comando è disponibile solo per gli amministratori."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Download terminato con supporto token PO"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Limite alluvioni. Riprova più tardi."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ Errore di aggiornamento del token REST: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Errore durante la chiusura della sessione Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Errore durante l'inizializzazione della struttura del database di base: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Non tutti i parametri sono impostati in config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL non è impostato"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey non è impostato per ottenere idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Errore durante il download del dump Firebase: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Impossibile scaricare il dump Firebase tramite REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Errore in _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Errore durante l'esecuzione di auto reload_cache (tentativo {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Tutti i tentativi sono falliti"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Avvio del download del dump di Firebase alle {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Dipendenza non disponibile: richieste o Sessione"
    DB_DATABASE_EMPTY_MSG = "⚠️ Il database è vuoto"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Errore durante la chiusura del logger: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Errore durante la pulizia: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Errore di clonazione: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Timeout della clonazione"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Eccezione clone: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Aggiornamento annullato dall'utente"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Repository clonato con successo"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Backup spostati in _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Tutti i moduli sono caricati"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Pulizia completata all'uscita"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Segnale {signal} ricevuto, spegnimento in corso..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Attendere prego..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Download dello streaming HLS:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "in attesa di frammenti"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Backup {ts} non trovato in _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Impossibile ripristinare {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Restaurato: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Dettagli:</b> {error_details}\n\nDownload interrotto a causa di un errore critico.\n\n💡 <b>Suggerimento:</b> Se ricevi l'errore 401 Non autorizzato, prova a usare il comando <code>/cookie instagram</code> o invia i tuoi cookie per autenticarti con Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Dominio nella lista nera del porno: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Parole chiave porno trovate: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Dominio nella whitelist: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Trovate parole chiave nella whitelist: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Nessuna parola chiave porno trovata"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Errore API TikTok all'indice {index}, passaggio all'audio successivo..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Errore API TikTok all'indice {index}, passaggio al video successivo..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "L'utente ha inserito un <b>url</b>\n <b>nome utente:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>L'utente ha inserito così:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Unisciti al canale"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Gestore di registrazione: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Scarica i miei 5 cookie"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Ottieni il cookie YT del browser"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Convalida il tuo file cookie"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Carica cookie personalizzato"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚Chiudi"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Formati disponibili per: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Chiudi"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Chiudi"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Chiudi"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Chiudi"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Aiuto chiuso."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Chiuso"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Si è verificato un errore"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg non trovato nel PATH o nella directory del progetto. Per favore installa FFmpeg."
    YTDLP_NOT_FOUND_MSG = "Binario yt-dlp non trovato nel PERCORSO o nella directory del progetto. Per favore installa yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Il video sarà diviso in {rounds} parti, il che potrebbe essere eccessivo"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Divisione parte video {current}/{total}: {start_time:.2f}s a {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Impossibile creare parte divisa {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Parte divisa {part} creata con successo: {target_name} ({size} byte)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Errore nella divisione parte video {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Video diviso in {count} parti con successo"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Errore nel processo di divisione video: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Errore durante l'elaborazione video {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Il file video non esiste: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Errore nell'analisi delle dimensioni '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Impossibile determinare le dimensioni video da '{size_result}', uso predefinito: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Errore nella creazione della miniatura: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Errore nell'analisi della durata video: {error}, risultato: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Miniatura non creata in {thumb_dir}, uso predefinito"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Errore nell'esecuzione del comando: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Errore nella creazione della miniatura con FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Saltare la sezione di configurazione non dict: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Impostazione {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Utilizzo dei cookie utente: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Utilizzo dei cookie di YouTube per l'utente {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "File cookie globale copiato nella cartella {user_id} dell'utente"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Utilizzo di cookie globali copiati come cookie utente: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Impossibile copiare il file cookie globale per l'utente {user_id}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Utilizzo di --no-cookies per il dominio: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Il proxy ha richiesto ma non è riuscito a importare/ottenere la configurazione: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Forza l'uso del proxy per gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy richiesto ma la configurazione del proxy è incompleta"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Assistente proxy non riuscito: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Analisi degli elementi dell'estrattore in corso..."
    GALLERY_DL_ITEM_COUNT_MSG = "Articolo {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Metadati trovati (tag 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL trovato (tag 3): {url}, metadati: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Metadati trovati (legacy): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL trovato (legacy): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Nome file trovato: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Directory trovata: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Estensione trovata: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Elementi {count} analizzati, informazioni: {info}, fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Impostazione della configurazione gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Provando la strategia A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "Modulo gallery_dl.extractor non trovato"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() non disponibile in questa build"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Chiamata a extract.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Nessun estrattore corrispondeva all'URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Impostazione dei cookie sull'estrattore: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Impossibile impostare i cookie sull'estrattore: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Estrattore trovato, chiamata items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "La strategia A ha avuto successo, ho ottenuto informazioni: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Strategia A: extractor.items() non ha restituito informazioni valide"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Strategia A (extractor.find) fallita: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Metadati di fallback da --get-urls: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Tutte le strategie non sono riuscite a ottenere i metadati"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Impossibile estrarre le informazioni sull'immagine: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "Modulo gallery_dl.job non trovato (installazione interrotta?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob non disponibile in questa build"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Ricerca dei file scaricati nella directory gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Cercando di trovare i file per nome dall'estrattore"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Errore durante la lettura degli argomenti utente per {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Errore durante l'elaborazione del video{video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "L'utente {user_id} ha abilitato send_as_file, inviando come documento"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video è scaduto ripetutamente; tornando a send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Didascalia troppo lunga, prova con una didascalia minima"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (didascalia minima) è scaduto; fallback su send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Errore durante l'invio del video con didascalia minima: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Errore durante l'invio del file di descrizione completo: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Errore durante la rimozione del file di descrizione temporaneo: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Saltare match_filter per il dominio in NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Controllo dei cookie di YouTube esistenti sull'URL dell'utente per il rilevamento del formato per l'utente {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "I cookie di YouTube esistenti funzionano sull'URL dell'utente per il rilevamento del formato per l'utente {user_id} - utilizzandoli"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "I cookie di YouTube esistenti non hanno funzionato sull'URL dell'utente, tentativo di ottenerne di nuovi per il rilevamento del formato per l'utente {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Prova dell'origine cookie di YouTube {i} per il rilevamento del formato per l'utente {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "I cookie di YouTube dalla fonte {i} funzionano sull'URL dell'utente per il rilevamento del formato per l'utente {user_id} - salvato nella cartella dell'utente"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "I cookie di YouTube provenienti dalla fonte {i} non funzionano sull'URL dell'utente per il rilevamento del formato per l'utente {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Impossibile scaricare i cookie di YouTube dalla fonte {i} per il rilevamento del formato per l'utente {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Tutte le origini cookie di YouTube non sono riuscite a rilevare il formato per l'utente {user_id}, proveranno senza cookie"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Nessuna fonte di cookie di YouTube configurata per il rilevamento del formato per l'utente {user_id} proverà senza cookie"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Nessun cookie di YouTube trovato per il rilevamento del formato per l'utente {user_id}, tentativo di ottenerne di nuovi"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Utilizzo dei cookie di YouTube per il rilevamento del formato per l'utente {user_id} (già convalidato nel menu Chiedi sempre)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Nessun cookie di YouTube trovato per il rilevamento del formato per l'utente {user_id}, tentativo di ripristino..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "File cookie globale copiato nella cartella {user_id} dell'utente per il rilevamento del formato"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Impossibile copiare il file cookie globale per l'utente {user_id}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Utilizzo di --no-cookies per il dominio in get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "App non ancora inizializzata. Impossibile accedere a {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Didascalia:</b> <code>{caption}</code>\n<b>ID utente:</b> <code>{user_id}</code>\n<b>Nome utente:</b> <code>{users_name}</code>\n<b>ID file video:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Errore nell'editor_didascalia: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Errore imprevisto in caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗URL del video</a>{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL mancante nella configurazione"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin inizializzato"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken aggiornato"
    DB_LOG_FOR_USER_ADDED_MSG = "Accedi per l'utente aggiunto"
    DB_DATABASE_CREATED_MSG = "db creato"
    DB_BOT_STARTED_MSG = "Il bot è iniziato"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY persiste in config.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Parte della playlist già memorizzata nella cache: {path_parts}, saltata"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: nessuna cache trovata per nessuna variante URL/qualità, restituendo dict vuoto"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: conteggio veloce per un ampio intervallo: {cached_count} video memorizzati nella cache"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: nessuna cache trovata per l'hash {url_hash}, qualità {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: nessuna cache trovata per nessuna variante URL, restituendo None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Accesso negato. Solo amministratore."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Ricaricamento automatico cache Firebase aggiornato!\n\n📊 Stato: {status}\n⏰ Programma: ogni {interval} ore dalle 00:00\n🕒 Prossimo ricaricamento: {next_exec} (tra {delta_min} minuti)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Ricaricamento automatico cache Firebase interrotto!\n\n📊 Stato: ❌ DISABILITATO\n💡 Usa /auto_cache on per riabilitare"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Argomento non valido. Usa /auto_cache su | spento | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ L'intervallo deve essere compreso tra 1 e 168 ore"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Impossibile impostare l'intervallo"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Intervallo cache Firebase automatica aggiornato!\n\n📊 Stato: ✅ ABILITATO\n⏰ Programma: ogni {interval} ore dalle 00:00\n🕒 Prossimo ricaricamento: {next_exec} (tra {delta_min} minuti)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Ricaricamento automatico cache Firebase avviato!\n\n📊 Stato: ✅ ABILITATO\n⏰ Programma: ogni {interval} ore dalle 00:00\n🕒 Prossimo ricaricamento: {next_exec} (tra {delta_min} minuti)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Ricaricamento automatico cache Firebase interrotto!\n\n📊 Stato: ❌ DISABILITATO\n💡 Usa /auto_cache on per riabilitare"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Ricarica automatica ABILITATA; successivo alle {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Ricarica automatica DISABILITATA dall'amministratore."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Intervallo di ricarica automatica impostato su {interval}h; successivo alle {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Ricarica automatica avviata; successivo alle {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Ricarica automatica interrotta dall'amministratore."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Cache Firebase caricata: {count} nodi root"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ File cache Firebase non trovato, che inizia con cache vuota: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Impossibile caricare la cache di Firebase: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Cache Firebase ricaricata: {count} nodi root"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ File cache Firebase non trovato: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Impossibile ricaricare la cache di Firebase: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 Sei stato bannato dal bot! Per essere sbannato, contatta {Config.ADMIN_USERNAME}\n<blockquote>P.S. Non lasciare il canale - sarai automaticamente bannato ⛔️</blockquote>\n🌍Cambia lingua /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Nessun formato video trovato. Sto provando il downloader di immagini..."
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram ha limitato l'invio di messaggi.\n⏳ Attendi: {time_str}\nPer aggiornare il timer invia di nuovo l'URL 2 volte."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Clicca il pulsante per copiare l'URL dello stream, poi incollalo nell'app VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Clicca il pulsante per copiare l'URL dello stream, poi incollalo nell'app VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Errore nell'ottenere il link:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Errore durante l'invio del file dei formati: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Impossibile ottenere i formati:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Analisi in corso... (attendere 6 secondi)"
    AA_PROCESSING_MSG = "🔎 Analizzando..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Il tag #{wrong} contiene caratteri non consentiti. Sono consentiti solo lettere, cifre e _.\nUsa: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Per il lavoro di gruppo, è necessario un lavoro da parte dell'amministratore. Quindi, seleziona l'amministratore di questo gruppo."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Ciao {first_name},\n \n<i>Questo bot🤖 può scaricare qualsiasi video direttamente in telegram.😊 Per maggiori informazioni premi <b>/help</b></i> 👈\n\n<blockquote>P.S. Il download di contenuti 🔞NSFW e file da ☁️Cloud Storage è a pagamento! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Non lasciare il canale - sarai bannato dall'uso del bot ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Nessun file da rimuovere."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 All files removed successfully!\n\nRemoved files:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ ATTENDERE FINO AL TERMINE DEL DOWNLOAD PRECEDENTE"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "L'istanza dell'app è Nessuna in check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict è Nessuno, consentendo il download"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict è None, consentendo l'incorporamento dei sottotitoli"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: verifica dei limiti - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: chiavi info_dict: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Incorporamento dei sottotitoli saltato: la durata {duration}s supera il limite {max_duration}s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Incorporamento dei sottotitoli saltato: la dimensione {size_mb:.2f}MB supera il limite {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Incorporamento sottotitoli saltato: la qualità {width}x{height} (lato minimo {min_side}p) supera il limite {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "playlist"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Limite intervallo superato per {service}: {count} (massimo {max_count}).\n\nUsa uno di questi comandi per scaricare il massimo di file disponibili:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Limite intervallo superato per {service}: {count} (massimo {max_count})\nID Utente: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "Provider di token PO disabilitato nella configurazione"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "L'URL {url} non è un dominio YouTube, verrà ignorato il token PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "Il fornitore di token PO non è disponibile presso {base_url}, ricorrendo all'estrazione standard da YouTube"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "Cache del fornitore di token PO cancellata, verificherà la disponibilità alla prossima richiesta"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Istanza dell'app non ancora disponibile"
    HELPER_USER_NAME_MSG = "Utente"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Rilevata attesa diluvio, in pausa per {wait_seconds} secondi"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Rilevata attesa Flood ma impossibile estrarre il tempo, in pausa per {retry_delay} secondi"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "Rilevato errore msg_seqno, inattivo per {retry_delay} secondi"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Configurazione proxy incompleta, utilizzo della connessione diretta"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Chiudi"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Chiudi"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Chiudi"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 File di registro rimosso."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 File dei tag rimosso."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 File di formato rimosso."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 File diviso rimosso."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑File Mediainfo rimosso."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Impostazioni dei sottotitoli rimosse."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Impostazioni della tastiera rimosse."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Impostazioni degli argomenti rimosse."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 Impostazioni NSFW rimosse."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Impostazioni proxy rimosse."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Impostazioni di attesa del diluvio rimosse."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Chiudi"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Comando di download video"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Utilizzo: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Esempi:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (ordine diretto)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (ordine inverso)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Vedi anche: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "L'utente {user_id} ha chiuso il comando add_bot_to_group"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Impossibile estrarre l'ID YouTube"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Impossibile scaricare la miniatura oppure è troppo grande"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Scegli la lingua dell'audio"
    AA_NO_SUBTITLES_DETECTED_MSG = "Nessun sottotitolo rilevato"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Scegli la lingua dei sottotitoli"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Errore di autenticazione"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Conto non trovato"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Account Unavailable"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Limite di velocità superato"
    GALLERY_DL_NETWORK_ERROR_MSG = "Errore di rete"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Content Unavailable"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Restrizioni geografiche"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Verifica richiesta"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Violazione delle norme"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Errore sconosciuto"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>♥️ Download avviato</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Chiudi"
    
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
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Vedi anche: /audio, /img, /help, /playlist, /settings"
    
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
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 File cookie rimosso e cache cancellata."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Prec"
    SUBS_BACK_BUTTON_MSG = "🔙Indietro"
    SUBS_OFF_BUTTON_MSG = "🚫 SPENTO"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - imposta la lingua"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - imposta la lingua con AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Opzioni valide:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍LINGUA"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Sviluppatore GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contro GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 PULITO"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪BISCOTTI"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞MEDIA"
    SETTINGS_INFO_BUTTON_MSG = "📖INFO"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ ALTRO"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Solo biscotti"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Registri"
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Tag"
    SETTINGS_FORMAT_BUTTON_MSG = "📼Formato"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Spalato"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Sottotitoli"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Tastiera"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Arg"
    SETTINGS_NSFW_BUTTON_MSG = "🔞NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎Delega"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄Attesa alluvione"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑 Tutti i file"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Scarica i miei 5 cookie"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Ottieni il cookie YT del browser"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Convalida il tuo file cookie"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Carica cookie personalizzato"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Cambia qualità e formato"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Attiva/disattiva MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Modifica le dimensioni della parte video divisa"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Scarica il video come audio"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Impostazioni della lingua dei sottotitoli"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Come scaricare le playlist"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Scarica le immagini tramite gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Invia i tuoi #tag"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Ottieni istruzioni"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage -Invia i tuoi log"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Aiuto per la playlist"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - istruzioni"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Ottieni collegamenti video diretti"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Abilita/disabilita proxy"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Layout della tastiera"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Assistente per la ricerca in linea"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - argomenti yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - Impostazioni di sfocatura NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Clean Options</b>\n\nChoose what to clean:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱Mobile: attiva la ricerca @vid"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱Mobile: attiva la ricerca @vid"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 SPENTO"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 COMPLETO"
    KEYBOARD_1X3_BUTTON_MSG = "📱1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL immagini]({url})"
    IMAGE_ERROR_MSG = "❌ Errore: {str(e)}"
    
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
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Dal browser"
    COOKIES_TWITTER_BUTTON_MSG = "🐦Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵TikTok"
    COOKIES_VK_BUTTON_MSG = "📘Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Il tuo"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Modalità di ingresso chiusa automaticamente per inattività (5 minuti)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Reimposta tutto"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Visualizza corrente"
    ARGS_BACK_BUTTON_MSG = "🔙 Indietro"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Inoltra questo messaggio ai tuoi preferiti per salvare queste impostazioni come modello.</i> \n\n<i>Inoltra questo messaggio qui per applicare queste impostazioni.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Argomenti yt-dlp correnti:\n\nNessuna impostazione personalizzata configurata.\n\n---\n\n<i>Inoltra questo messaggio ai tuoi preferiti per salvare queste impostazioni come modello.</i> \n\n<i>Inoltra questo messaggio qui per applicare queste impostazioni.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Argomenti yt-dlp correnti:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Impostazioni di esportazione"
    ARGS_SETTINGS_READY_MSG = "Impostazioni pronte per l'esportazione! Inoltra questo messaggio ai preferiti per salvarlo."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Argomenti attuali di yt-dlp:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Impossibile riconoscere le impostazioni nel messaggio. Assicurati di aver inviato un modello di impostazioni corretto."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Impostazioni importate con successo!\n\nParametri applicati: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Impostazioni chiave:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Errore durante il salvataggio delle impostazioni importate."
    ARGS_ERROR_IMPORTING_MSG = "❌ Si è verificato un errore durante l'importazione delle impostazioni."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Scarica file cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Scegli un servizio per scaricare il file cookie."
    COOKIE_MENU_SAVE_INFO_MSG = "I file cookie verranno salvati come cookie.txt nella tua cartella."
    COOKIE_MENU_TIP_HEADER_MSG = "Suggerimento: puoi anche utilizzare il comando diretto:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – scarica e convalida i cookie"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – utilizza una fonte specifica per indice (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Quindi verifica con <code>/check_cookie</code> (test su RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Chiedi sempre"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Link"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Watch"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Didascalia"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ TAGLIA"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Taglia Video</b>\n\nDurata video: <b>{start_time} - {end_time}</b>\n\nSi prega di inviare l'intervallo di tempo desiderato nel formato:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nEsempio: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Formato non valido. Si prega di utilizzare: <code>HH:MM:SS-HH:MM:SS</code>\n\nEsempio: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Intervallo non valido. L'ora di inizio deve essere inferiore all'ora di fine."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ L'intervallo di tempo è fuori dai limiti del video.\n\nDurata video: <b>{start_time} - {end_time}</b>\n\nIl tuo intervallo deve essere entro questi limiti."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>Il video sarà tagliato:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Parzialmente completato - {successful_uploads}/{total_files} file audio caricati."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Audio scaricato e inviato con successo - {total_files} file caricati."

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
