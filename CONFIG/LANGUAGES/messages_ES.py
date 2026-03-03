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
    CREDITS_MSG = "<blockquote><i>Administrado por</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Cambiar idioma: /lang</b>"
    TO_USE_MSG = "<i>Para usar este bot necesitas suscribirte al canal de Telegram @tg_ytdlp.</i>\nDespués de unirte al canal, <b>reenvía tu enlace de video y el bot lo descargará para ti</b> ❤️\n\n<blockquote>P.S. Por el posible contenido 🔞NSFW - descargar de ☁️<b>Almacenamiento en la nube</b>, 📁<b>Compartir archivos</b>, 🔗<b>Acortadores de URL</b> y 🔞<b>Sitios para adultos</b> es de pago! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ NO 🗑<b>elimines/canceles la suscripción al canal @tg_ytdlp</b> y NO 🤖<b>hagas spam de URL/comandos al bot</b> - serás baneado automáticamente ⛔️</blockquote>"

    ERROR1 = "No se encontró un enlace URL. Por favor ingrese una URL con <b>https://</b> o <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Listas de reproducción (yt-dlp)</b>

Para descargar listas de reproducción envía su URL con rangos <code>*start*end</code> al final. Por ejemplo: <code>URL*1*5</code> (primeros 5 videos del 1 al 5 inclusive).<code>URL*-1*-5</code> (últimos 5 videos del 1 al 5 inclusive).
O puedes usar <code>/vid FROM-TO URL</code>. Por ejemplo: <code>/vid 3-7 URL</code> (descarga videos del 3 al 7 inclusive desde el inicio). <code>/vid -3-7 URL</code> (descarga videos del 3 al 7 inclusive desde el final). También funciona para el comando <code>/audio</code>.

<b>Ejemplos:</b>

🟥 <b>Rango de videos de lista de reproducción de YouTube:</b> (necesita 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(descarga los primeros 5 videos del 1 al 5 inclusive)
🟥 <b>Video único de lista de reproducción de YouTube:</b> (necesita 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(descarga solo el 3er video)

⬛️ <b>Perfil de TikTok:</b> (necesita tu 🍪)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(descarga los primeros 10 videos del perfil de usuario)

🟪 <b>Historias de Instagram:</b> (necesita tu 🍪)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(descarga las primeras 3 historias)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(descarga las primeras 10 historias del álbum)

🟦 <b>Videos de VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(descarga los primeros 3 videos del perfil de usuario/grupo)

⬛️<b>Canales de Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(descarga videos del 2 al 4 inclusive del canal)

🟪 <b>Clips de Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(descarga los primeros 3 clips del canal)

🟦 <b>Grupos de Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(descarga los primeros 2 videos del grupo)

🟧 <b>Modelos de Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(descarga los primeros 2 videos del perfil del modelo)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(descarga los primeros 3 videos de los resultados de búsqueda por tu prompt)

y así sucesivamente...
ver <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">lista de sitios soportados</a>
</blockquote>

<blockquote expandable>🖼 <b>Imágenes (gallery-dl)</b>

Usa <code>/img URL</code> para descargar imágenes/fotos/álbumes de muchas plataformas.

<b>Ejemplos:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Rangos:</b>
<code>/img 11-20 https://example.com/album</code> — elementos 11..20
<code>/img 11- https://example.com/album</code> — del 11 al final (o límite del bot)

<i>Las plataformas soportadas incluyen vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, etc. Lista completa:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">sitios soportados de gallery-dl</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Bot de Descarga de Videos - Ayuda</b>

📥 <b>Uso Básico:</b>
• Envía cualquier enlace → el bot lo descarga
  <i>el bot intenta automáticamente descargar videos vía yt-dlp e imágenes vía gallery-dl.</i>
• <b>Múltiples URLs:</b> En modo de selección de calidad (<code>/format</code>) puedes enviar hasta <b>10 URLs</b> en un mensaje. Cada URL en una nueva línea o separadas por espacios.
• <code>/audio URL</code> → extraer audio
• <code>/link [quality] URL</code> → obtener enlaces directos
• <code>/proxy</code> → habilitar/deshabilitar proxy para todas las descargas
• Responde al video con texto → cambiar subtítulo

📋 <b>Listas de Reproducción y Rangos:</b>
• <code>URL*1*5</code> → descargar primeros 5 videos
• <code>URL*-1*-5</code> → descargar últimos 5 videos
• <code>/vid 3-7 URL</code> → se convierte en <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → se convierte en <code>URL*-3*-7</code>

🍪 <b>Cookies y Privado:</b>
• Sube cookie *.txt para videos privados
• <code>/cookie [service]</code> → descargar cookies (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → elegir fuente por índice (1–N)
• <code>/cookies_from_browser</code> → extraer del navegador
• <code>/check_cookie</code> → verificar cookie
• <code>/save_as_cookie</code> → guardar texto como cookie

🧹 <b>Limpieza:</b>
• <code>/clean</code> → solo archivos multimedia
• <code>/clean all</code> → todo
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Configuración:</b>
• <code>/settings</code> → menú de configuración
• <code>/format</code> → calidad y formato
• <code>/split</code> → dividir video en partes
• <code>/mediainfo on/off</code> → información multimedia
• <code>/nsfw on/off</code> → desenfoque NSFW
• <code>/tags</code> → ver etiquetas guardadas
• <code>/sub on/off</code> → subtítulos
• <code>/keyboard</code> → teclado (OFF/1x3/2x3)

🏷️ <b>Etiquetas:</b>
• Agrega <code>#tag1#tag2</code> después de la URL
• Las etiquetas aparecen en los subtítulos
• <code>/tags</code> → ver todas las etiquetas

🔗 <b>Enlaces Directos:</b>
• <code>/link URL</code> → mejor calidad
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → calidad específica

⚙️ <b>Comandos Rápidos:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → establecer calidad
• <code>/keyboard off/1x3/2x3/full</code> → diseño de teclado
• <code>/split 100mb-2000mb</code> → cambiar tamaño de parte
• <code>/subs off/ru/en auto</code> → idioma de subtítulos
• <code>/list URL</code> → lista de formatos disponibles
• <code>/mediainfo on/off</code> → activar/desactivar información multimedia
• <code>/proxy on/off</code> → habilitar/deshabilitar proxy para todas las descargas

📊 <b>Información:</b>
• <code>/usage</code> → historial de descargas
• <code>/search</code> → búsqueda en línea vía @vid

🖼 <b>Imágenes:</b>
• <code>URL</code> → descargar URL de imágenes
• <code>/img URL</code> → descargar imágenes de URL
• <code>/img 11-20 URL</code> → descargar rango específico
• <code>/img 11- URL</code> → descargar desde el 11º hasta el final

👨‍💻 <i>Desarrollador:</i> @upekshaip
🤝 <i>Contribuidor:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Simplemente guarda tu cookie como <b><u>cookie.txt</u></b> y envíalo al bot como documento.\n\n"
        "También puedes enviar cookies como texto plano con el comando <b><u>/save_as_cookie</u></b>.\n"
        "<b>Uso de <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>Instrucciones:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>Búsqueda de videos</b>

Presiona el botón de abajo para activar la búsqueda en línea vía @vid.

<blockquote>En PC simplemente escribe <b>"@vid Tu_Consulta_de_Búsqueda"</b> en cualquier chat.</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Comando de Descarga de Imágenes</b>\n\n"
        "Uso: <code>/img URL</code>\n\n"
        "<b>Ejemplos:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Plataformas soportadas (ejemplos):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, etc. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">lista completa</a></blockquote>"
        "También ver: "
    )
    
    LINK_HINT_MSG = (
        "Obtén enlaces directos de video con selección de calidad.\n\n"
        "Uso: /link + URL \n\n"
        "(ej. /link https://youtu.be/abc123)\n"
        "(ej. /link 720 https://youtu.be/abc123)"
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
🔞 <b>Modo NSFW: ACTIVADO✅</b>

• El contenido NSFW se mostrará sin desenfoque.
• Los spoilers no se aplicarán a los medios NSFW.
• El contenido será visible inmediatamente

<i>Usa /nsfw off para habilitar el desenfoque</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>Modo NSFW: DESACTIVADO</b>

⚠️ <b>Desenfoque habilitado</b>
• El contenido NSFW estará oculto bajo spoiler   
• Para ver, necesitarás hacer clic en el medio
• Los spoilers se aplicarán a los medios NSFW.

<i>Usa /nsfw on para deshabilitar el desenfoque</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Parámetro inválido</b>

Usa:
• <code>/nsfw on</code> - deshabilitar desenfoque
• <code>/nsfw off</code> - habilitar desenfoque
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Verificando caché...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Procesando..."
    DOWNLOADING_MSG = "📥 <b>Descargando medios...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Descargando imagen...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Descarga completa</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Descargado:"
    SENT_STATUS_MSG = "Enviado:"
    PENDING_TO_SEND_STATUS_MSG = "Pendiente de enviar:"
    TITLE_LABEL_MSG = "Título:"
    MEDIA_COUNT_LABEL_MSG = "Recuento de medios:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Descarga finalizada, procesando audio..."
    VIDEO_PROCESSING_MSG = "📽 El video se está procesando..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Enviado desde caché</b>\n\nÁlbumes enviados: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Video enviado exitosamente desde caché."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Videos de lista de reproducción enviados desde caché ({cached}/{total} archivos)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} videos enviados desde caché, descargando los faltantes..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Enviado desde caché: {cached}\n🔄 Continuando descarga..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 No se pudo analizar los medios, procediendo con el rango máximo permitido (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 No se pudo determinar el recuento de medios, procediendo con el rango máximo permitido (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 No se pudo determinar el recuento total de medios, procediendo con el rango especificado {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>URL inválida</b>\n\nPor favor proporciona una URL válida que comience con http:// o https://"

    ERROR_OCCURRED_MSG = "❌ <b>Ocurrió un error</b>\n\n<code>{url}</code>\n\nError: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Error al enviar video: {error}"
    ERROR_UNKNOWN_MSG = "❌ Error desconocido: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ No hay suficiente espacio en disco para descargar videos."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ El tamaño del archivo excede el límite de {limit} GB. Por favor selecciona un archivo más pequeño dentro del tamaño permitido."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>Error al descargar video con todos los proxies disponibles</b>\n\nTodos los intentos de descarga a través de proxies han fallado.\nIntenta:\n• Verificar la funcionalidad del proxy\n• Probar otro proxy de la lista\n• Descargar sin proxy (si es posible)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Error al obtener enlace:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram ha limitado el envío de mensajes.\n⏳ Por favor espera: {time}\nPara actualizar el temporizador envía la URL nuevamente 2 veces."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram ha limitado el envío de mensajes.\n⏳ Por favor espera: \nPara actualizar el temporizador envía la URL nuevamente 2 veces."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Error al descargar subtítulos"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Enlaces de Transmisión Directa</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Título:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Duración:</b> {duration} seg\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Error: Mensaje original no encontrado."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ La etiqueta #{tag} contiene caracteres prohibidos. Solo se permiten letras, dígitos y _.\nPor favor usa: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Videos de lista de reproducción enviados: {sent}/{total} archivos."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>Consejo sobre listas de reproducción</b>

Enviaste un enlace de lista de reproducción sin especificar un rango. El bot descargó automáticamente el primer video (<code>*1*1</code>).

<b>Para descargar varios videos de una lista de reproducción, especifica un rango:</b>
• <code>URL*1*5</code> — primeros 5 videos (del 1 al 5 inclusive)
• <code>URL*3*3</code> — solo el 3er video
• <code>/vid 1-10 URL</code> — formato alternativo

Más información: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ Enviado desde caché: {cached}/{total} archivos."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Error al obtener enlaces de transmisión"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Selecciona un navegador para descargar cookies:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "No se encontraron navegadores en este sistema. Puedes descargar cookies desde URL remota o monitorear el estado del navegador:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Abrir Navegador</b> - para monitorear el estado del navegador en mini-app"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Abrir Navegador"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Descargar desde URL Remota"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Archivo de cookie de YouTube descargado vía respaldo y guardado como cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ No se encontraron navegadores soportados y no hay COOKIE_URL configurado. Usa /cookie o sube cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ La URL de respaldo COOKIE_URL debe apuntar a un archivo .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ El archivo de cookie de respaldo es demasiado grande (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fuente de cookie de respaldo no disponible (estado {status}). Prueba /cookie o sube cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Error al descargar cookie de respaldo. Prueba /cookie o sube cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Error inesperado durante la descarga de cookie de respaldo."
    BTN_CLOSE = "🔚Cerrar"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Valor booleano inválido"
    ARGS_CLOSED_MSG = "Cerrado"
    ARGS_ALL_RESET_MSG = "✅ Todos los argumentos restablecidos"
    ARGS_RESET_ERROR_MSG = "❌ Error al restablecer argumentos"
    ARGS_INVALID_PARAM_MSG = "❌ Parámetro inválido"
    ARGS_BOOL_SET_MSG = "Establecido en {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "Ya establecido en {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Valor de selección inválido"
    ARGS_VALUE_SET_MSG = "Establecido en {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "Ya establecido en {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Valor actual:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Ejemplos:</b>\n• <code>default</code> - Usar estrategia XFF predeterminada\n• <code>never</code> - Nunca usar encabezado XFF\n• <code>US</code> - Código de país Estados Unidos\n• <code>GB</code> - Código de país Reino Unido\n• <code>DE</code> - Código de país Alemania\n• <code>FR</code> - Código de país Francia\n• <code>JP</code> - Código de país Japón\n• <code>192.168.1.0/24</code> - Bloque IP (CIDR)\n• <code>10.0.0.0/8</code> - Rango IP privado\n• <code>203.0.113.0/24</code> - Bloque IP público\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Nota:</b> Esto reemplaza las opciones --geo-bypass. Usa cualquier código de país de 2 letras o bloque IP en notación CIDR.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Ejemplo:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Por favor envía tu nuevo valor."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Rango:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Por favor envía un número."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Ejemplos:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Nota:</b> Estos encabezados se agregarán a los encabezados Referer y User-Agent existentes.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Argumentos actuales de yt-dlp:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Booleano</b> - Interruptores Verdadero/Falso\n• 📋 <b>Selección</b> - Elige entre opciones\n• 🔢 <b>Numérico</b> - Entrada de número\n• 📝🔧 <b>Texto</b> - Entrada de texto/JSON</blockquote>\n\nEstas configuraciones se aplicarán a todas tus descargas."
    
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
    PLEASE_WAIT_MSG = "⏳ Por favor espera..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Ocurrió un error"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Modo de entrada cerrado automáticamente por inactividad (5 minutos)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ La entrada contiene contenido potencialmente peligroso: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Entrada demasiado larga (máximo 1000 caracteres)"
    ARGS_INVALID_URL_MSG = "❌ Formato de URL inválido. Debe comenzar con http:// o https://"
    ARGS_INVALID_JSON_MSG = "❌ Formato JSON inválido"
    ARGS_NUMBER_RANGE_MSG = "❌ El número debe estar entre {min_val} y {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Formato de número inválido"
    ARGS_DATE_FORMAT_MSG = "❌ La fecha debe estar en formato YYYYMMDD (ej., 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ El año debe estar entre 1900 y 2100"
    ARGS_MONTH_RANGE_MSG = "❌ El mes debe estar entre 01 y 12"
    ARGS_DAY_RANGE_MSG = "❌ El día debe estar entre 01 y 31"
    ARGS_INVALID_DATE_MSG = "❌ Formato de fecha inválido"
    ARGS_INVALID_XFF_MSG = "❌ XFF debe ser 'default', 'never', código de país (ej., US), o bloque IP (ej., 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "No se establecieron argumentos personalizados. Todos los parámetros usan valores predeterminados."
    ARGS_RESET_SUCCESS_MSG = "✅ Todos los argumentos restablecidos a los predeterminados."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Texto demasiado largo. Máximo 500 caracteres."
    ARGS_ERROR_PROCESSING_MSG = "❌ Error al procesar la entrada. Por favor intenta de nuevo."
    ARGS_BOOL_INPUT_MSG = "❌ Por favor ingresa 'True' o 'False' para la opción Enviar Como Archivo."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Por favor proporciona un número válido."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Por favor envía <code>True</code> o <code>False</code> para habilitar/deshabilitar esta opción."
    ARGS_JSON_VALUE_REQUEST_MSG = "Por favor envía JSON válido."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Aún no tienes etiquetas."
    TAGS_MESSAGE_CLOSED_MSG = "Mensaje de etiquetas cerrado."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Subtítulos deshabilitados y modo Siempre Preguntar desactivado."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Siempre Preguntar habilitado."
    SUBS_LANGUAGE_SET_MSG = "✅ Idioma de subtítulos establecido en: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️ADVERTENCIA: debido al alto impacto en CPU esta función es muy lenta (casi en tiempo real) y limitada a:\n"
        "- calidad máxima 720p\n"
        "- duración máxima 1.5 horas\n"
        "- tamaño máximo de video 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Comandos rápidos:</b>\n"
        "• <code>/subs off</code> - deshabilitar subtítulos\n"
        "• <code>/subs on</code> - habilitar modo Siempre Preguntar\n"
        "• <code>/subs ru</code> - establecer idioma\n"
        "• <code>/subs ru auto</code> - establecer idioma con AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Los subtítulos están deshabilitados"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Idioma seleccionado: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Descargando subtítulos..."
    SUBS_DISABLED_ERROR_MSG = "❌ Los subtítulos están deshabilitados. Usa /subs para configurar."
    SUBS_YOUTUBE_ONLY_MSG = "❌ La descarga de subtítulos solo está soportada para YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Subtítulos</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Idioma:</b> {lang}\n"
        "<b>Tipo:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Archivo SRT de subtítulos enviado al usuario."
    SUBS_ERROR_PROCESSING_MSG = "❌ Error al procesar archivo de subtítulos."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Error al descargar subtítulos."
    SUBS_ERROR_MSG = "❌ Error al descargar subtítulos: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Tamaño de parte dividida establecido en: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **¡Tamaño inválido!**\n\n"
        "**Rango válido:** 100MB a 2GB\n\n"
        "**Formatos válidos:**\n"
        "• `100mb` a `2000mb` (megabytes)\n"
        "• `0.1gb` a `2gb` (gigabytes)\n\n"
        "**Ejemplos:**\n"
        "• `/split 100mb` - 100 megabytes\n"
        "• `/split 500mb` - 500 megabytes\n"
        "• `/split 1.5gb` - 1.5 gigabytes\n"
        "• `/split 2gb` - 2 gigabytes\n"
        "• `/split 2000mb` - 2000 megabytes (2GB)\n\n"
        "**Preajustes:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Elige el tamaño máximo de parte para dividir video:**\n\n"
        "**Rango:** 100MB a 2GB\n\n"
        "**Comandos rápidos:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Ejemplos:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Menú cerrado."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Configuración del Bot</b>\n\nElige una categoría:"
    SETTINGS_MENU_CLOSED_MSG = "Menú cerrado."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Opciones de Limpieza</b>\n\nElige qué limpiar:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nElige una acción:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIOS</b>\n\nElige una acción:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFORMACIÓN</b>\n\nElige una acción:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ MÁS COMANDOS</b>\n\nElige una acción:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Comando ejecutado."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Límite de inundación. Intenta más tarde."
    SETTINGS_HINT_SENT_MSG = "Pista enviada."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Ayudante de búsqueda abierto."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Comando desconocido."
    SETTINGS_HINT_CLOSED_MSG = "Pista cerrada."
    SETTINGS_HELP_SENT_MSG = "Enviar texto de ayuda al usuario"
    SETTINGS_MENU_OPENED_MSG = "Abierto menú /settings"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Ayudante de búsqueda cerrado"
    SEARCH_CLOSED_MSG = "Cerrado"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proxy {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Error al guardar configuración de proxy."
    PROXY_MENU_TEXT_MSG = "¿Habilitar o deshabilitar el uso de servidor proxy para todas las operaciones de yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "¿Habilitar o deshabilitar el uso de servidores proxy ({config_count} + {file_count} disponibles) para todas las operaciones de yt-dlp?\n\nCuando se habilita TODO (AUTO), los proxies se seleccionan automáticamente según los países permitidos (indicados en el error de YouTube)."
    PROXY_MENU_CLOSED_MSG = "Menú cerrado."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy habilitado. Todas las operaciones de yt-dlp usarán proxy."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy habilitado. Todas las operaciones de yt-dlp usarán {count} servidores proxy con método de selección {method}."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Proxy habilitado (AUTO por error de YouTube).\n\nCuando YouTube devuelva un error de geo-bloqueo, el bot usará solo proxies de los países indicados en ese error (sin probar todos los proxies en secuencia)."
    PROXY_DISABLED_MSG = "❌ Proxy deshabilitado."
    PROXY_TRYING_COUNTRY_MSG = "🔄 Probando proxy: {country} ({current}/{total})"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Error al guardar configuración de proxy."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy habilitado."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy deshabilitado."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ ESPERA HASTA QUE TU DESCARGA ANTERIOR TERMINE"
    AUDIO_HELP_MSG = (
        "<b>🎧 Comando de Descarga de Audio</b>\n\n"
        "Uso: <code>/audio URL</code>\n\n"
        "<b>Ejemplos:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "También ver: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Pista de audio cerrada."
    PLAYLIST_HELP_CLOSED_MSG = "Ayuda de lista de reproducción cerrada."
    USERLOGS_CLOSED_MSG = "Mensaje de logs cerrado."
    HELP_CLOSED_MSG = "Ayuda cerrada."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>Configuración de Desenfoque NSFW</b>\n\nEl contenido NSFW está <b>{status}</b>.\n\nElige si desenfocar el contenido NSFW:"
    NSFW_MENU_CLOSED_MSG = "Menú cerrado."
    NSFW_BLUR_DISABLED_MSG = "Desenfoque NSFW deshabilitado."
    NSFW_BLUR_ENABLED_MSG = "Desenfoque NSFW habilitado."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Desenfoque NSFW deshabilitado."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Desenfoque NSFW habilitado."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "¿Habilitar o deshabilitar el envío de MediaInfo para archivos descargados?"
    MEDIAINFO_MENU_CLOSED_MSG = "Menú cerrado."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo habilitado. Después de descargar, se enviará la información del archivo."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo deshabilitado."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo habilitado."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo deshabilitado."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Listar Formatos Disponibles</b>\n\n"
        "Obtén formatos de video/audio disponibles para una URL.\n\n"
        "<b>Uso:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Ejemplos:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Cómo usar IDs de formato:</b>\n"
        "Después de obtener la lista, usa un ID de formato específico:\n"
        "• <code>/format id 401</code> - descargar formato 401\n"
        "• <code>/format id401</code> - igual que arriba\n"
        "• <code>/format id140 audio</code> - descargar formato 140 como audio MP3\n\n"
        "Este comando mostrará todos los formatos disponibles que se pueden descargar."
    )
    LIST_PROCESSING_MSG = "🔄 Obteniendo formatos disponibles..."
    LIST_INVALID_URL_MSG = "❌ Por favor proporciona una URL válida que comience con http:// o https://"
    LIST_CAPTION_MSG = (
        "📃 Formatos disponibles para:\n<code>{url}</code>\n\n"
        "💡 <b>Cómo establecer formato:</b>\n"
        "• <code>/format id 134</code> - Descargar ID de formato específico\n"
        "• <code>/format 720p</code> - Descargar por calidad\n"
        "• <code>/format best</code> - Descargar mejor calidad\n"
        "• <code>/format ask</code> - Siempre preguntar por calidad\n\n"
        "{audio_note}\n"
        "📋 Usa ID de formato de la lista de arriba"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Formatos solo de audio:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Descargar formato 140 como audio MP3\n"
        "• <code>/format id140 audio</code> - igual que arriba\n"
        "Estos se descargarán como archivos de audio MP3.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Error al enviar archivo de formatos: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Error al obtener formatos:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Ocurrió un error al procesar el comando"
    LIST_ERROR_CALLBACK_MSG = "Ocurrió un error"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Cómo usar IDs de formato:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Después de obtener la lista, usa un ID de formato específico:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - descargar formato 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - igual que arriba\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - descargar formato 140 como audio MP3\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - igual que arriba\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Formatos solo de audio detectados: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Estos formatos se descargarán como archivos de audio MP3.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Formatos solo de video:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Usa ID de formato de la lista de arriba"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Uso:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>Ejemplos:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - mejor calidad\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p o inferior\n"
        "• /link 720p https://youtube.com/watch?v=... - igual que arriba\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K o inferior\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K o inferior"
        "</blockquote>\n\n"
        "<b>Calidad:</b> del 1 al 10000 (ej., 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Por favor proporciona una URL válida"
    LINK_PROCESSING_MSG = "🔗 Obteniendo enlace directo..."
    LINK_DURATION_MSG = "⏱ <b>Duración:</b> {duration} seg\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Transmisión de video:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Transmisión de audio:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **¡Configuración de teclado actualizada!**\n\nNueva configuración: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **¡Argumento inválido!**\n\n"
        "Opciones válidas: `off`, `1x3`, `2x3`, `full`\n\n"
        "Ejemplo: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Configuración de Teclado**\n\n"
        "Actual: **{current}**\n\n"
        "Elige una opción:\n\n"
        "O usa: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 ¡teclado activado!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Teclado oculto"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 ¡teclado 1x3 activado!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 ¡teclado 2x3 activado!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 ¡teclado de emojis activado!"
    KEYBOARD_ERROR_APPLYING_MSG = "Error al aplicar configuración de teclado {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Formato establecido en: Siempre Preguntar. Se te pedirá la calidad cada vez que envíes una URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Formato establecido en: Siempre Preguntar. Ahora se te pedirá la calidad cada vez que envíes una URL."
    FORMAT_BEST_UPDATED_MSG = "✅ Formato actualizado a mejor calidad (prioridad AVC+MP4):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Formato actualizado a ID {id}:\n{format}\n\n💡 <b>Nota:</b> Si este es un formato solo de audio, se descargará como archivo de audio MP3."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Formato actualizado a ID {id} (solo audio):\n{format}\n\n💡 Esto se descargará como archivo de audio MP3."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Formato actualizado a calidad {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Formato actualizado a:\n{format}"
    FORMAT_MENU_MSG = (
        "Selecciona una opción de formato o envía una personalizada usando:\n"
        "• <code>/format &lt;format_string&gt;</code> - formato personalizado\n"
        "• <code>/format 720</code> - calidad 720p\n"
        "• <code>/format 4k</code> - calidad 4K\n"
        "• <code>/format 8k</code> - calidad 8K\n"
        "• <code>/format id 401</code> - ID de formato específico\n"
        "• <code>/format ask</code> - siempre mostrar menú\n"
        "• <code>/format best</code> - bv+ba/mejor calidad"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Para usar un formato personalizado, envía el comando en la siguiente forma:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Reemplaza <code>bestvideo+bestaudio/best</code> con tu cadena de formato deseada."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Selecciona tu resolución y códec deseado:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Formato establecido en: Siempre Preguntar. Ahora se te pedirá la calidad cada vez que envíes una URL."
    FORMAT_UPDATED_MSG = "✅ Formato actualizado a:\n{format}"
    FORMAT_SAVED_MSG = "✅ Formato guardado."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Opción de formato actualizada."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Menú de formato personalizado cerrado"
    FORMAT_CODEC_SET_MSG = "✅ Códec establecido en {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Opción de navegador actualizada."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Acceso denegado. Solo administradores."
    ACCESS_DENIED_ADMIN = "❌ Acceso denegado. Solo administradores."
    WELCOME_MASTER = "Bienvenido Maestro 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Lo siento... Ocurrió algún error durante la descarga."
    SIZE_LIMIT_EXCEEDED = "❌ El tamaño del archivo excede el límite de {max_size_gb} GB. Por favor selecciona un archivo más pequeño dentro del tamaño permitido."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Script no encontrado: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Descargando volcado fresco de Firebase usando {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ ¡Caché de Firebase recargado exitosamente!"
    ADMIN_CACHE_FAILED_MSG = "❌ Error al recargar caché de Firebase. Verifica si {cache_file} existe."
    ADMIN_ERROR_RELOADING_MSG = "❌ Error al recargar caché: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Error al ejecutar {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Mensaje promocional enviado a todos los demás usuarios</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ No se puede enviar el mensaje promocional. Intenta responder a un mensaje\nO ocurrió algún error</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ El usuario aún no ha descargado ningún contenido...</b> No existe en los logs"
    ADMIN_INVALID_COMMAND_MSG = "❌ Comando inválido"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ No se encontraron datos en caché para <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ La cola está vacía — nadie ha dejado el canal aún."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Cola de bloqueo</b>\nTotal pendiente: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (salió: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… y {extra} usuarios más."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Usa /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Usuarios bloqueados de la cola: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Auto-bloqueo habilitado: los nuevos que salgan serán baneados inmediatamente."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Auto-bloqueo deshabilitado."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Ventana de auto-bloqueo programada establecida en cada {interval}."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Registro de actividad del canal de las últimas {hours} horas (2 días)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 Últimas {hours} horas (2 días): se unieron {joined}, salieron {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Sin actividad en las últimas {hours} horas (2 días)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Total: 🟢 {joined} se unieron, 🔴 {left} salieron."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Sin acceso al registro de actividad del canal. Los bots no pueden leer los logs de administrador. Proporciona CHANNEL_GUARD_SESSION_STRING en config con una sesión de usuario para habilitar esta función."
    BAN_TIME_USAGE_MSG = "❌ Uso: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Usa formatos como 10s, 6m, 5h, 4d, 3w, 2M o 1y."
    BAN_TIME_SET_MSG = "🕒 Intervalo de escaneo de log del canal establecido en {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Reporte de escaneo del canal\n"
        "Ejecutado en: {run_ts}\n"
        "Intervalo: {interval}\n"
        "Nuevos que salieron: {new_leavers}\n"
        "Baneos automáticos: {auto_banned}\n"
        "Pendiente: {pending}\n"
        "Último event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Uso: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Un administrador no puede eliminar a otro administrador"
    ADMIN_USER_BLOCKED_MSG = "Usuario bloqueado 🔒❌\n \nID: <code>{user_id}</code>\nFecha de bloqueo: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> ya está bloqueado ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 ¡Lo siento! No eres un administrador"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Uso: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Usuario desbloqueado 🔓✅\n \nID: <code>{user_id}</code>\nFecha de desbloqueo: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> ya está desbloqueado ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Usuarios desbloqueados: {count}\n⏱ Marca de tiempo: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Uso: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Usuario ignorado 👁️❌\n \nID: <code>{user_id}</code>\nFecha de ignorado: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> ya está siendo ignorado ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Uso: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Usuario ya no ignorado 👁️✅\n \nID: <code>{user_id}</code>\nFecha de dejar de ignorar: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> no está siendo ignorado ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Tiempo de ejecución del bot -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Por favor proporciona una URL para limpiar la caché.\nUso: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Por favor proporciona una URL válida.\nUso: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Caché limpiada exitosamente para URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ No se encontró caché para este enlace."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Error al limpiar caché: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Acceso denegado. Solo administradores."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Ejecutando script de actualización de lista de pornografía: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ ¡Script completado exitosamente!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ ¡Script completado exitosamente!\n\nSalida:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Script falló con código de retorno {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Error al ejecutar script: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Recargando cachés de pornografía y dominios relacionados..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ ¡Cachés de pornografía recargados exitosamente!\n\n"
        "📊 Estado actual de caché:\n"
        "• Dominios de pornografía: {porn_domains}\n"
        "• Palabras clave de pornografía: {porn_keywords}\n"
        "• Sitios soportados: {supported_sites}\n"
        "• LISTA BLANCA: {whitelist}\n"
        "• LISTA GRIS: {greylist}\n"
        "• LISTA NEGRA: {black_list}\n"
        "• PALABRAS CLAVE BLANCAS: {white_keywords}\n"
        "• DOMINIOS PROXY: {proxy_domains}\n"
        "• DOMINIOS PROXY_2: {proxy_2_domains}\n"
        "• CONSULTA LIMPIA: {clean_query}\n"
        "• DOMINIOS SIN COOKIE: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Error al recargar caché de pornografía: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Por favor proporciona una URL para verificar.\nUso: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Por favor proporciona una URL válida.\nUso: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Verificando URL para contenido NSFW...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Resultado de Verificación de Pornografía</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Estado:</b> <b>{status_text}</b>\n\n"
        "<b>Explicación:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Error al verificar URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Cookies limpiados."
    CLEAN_LOGS_CLEANED_MSG = "logs limpiados."
    CLEAN_TAGS_CLEANED_MSG = "etiquetas limpiadas."
    CLEAN_FORMAT_CLEANED_MSG = "formato limpiado."
    CLEAN_SPLIT_CLEANED_MSG = "división limpiada."
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfo limpiado."
    CLEAN_SUBS_CLEANED_MSG = "Configuración de subtítulos limpiada."
    CLEAN_KEYBOARD_CLEANED_MSG = "Configuración de teclado limpiada."
    CLEAN_ARGS_CLEANED_MSG = "Configuración de argumentos limpiada."
    CLEAN_NSFW_CLEANED_MSG = "Configuración NSFW limpiada."
    CLEAN_PROXY_CLEANED_MSG = "Configuración de proxy limpiada."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Configuración de espera de inundación limpiada."
    CLEAN_ALL_CLEANED_MSG = "Todos los archivos limpiados."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nElige una acción:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Archivo de cookie guardado"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Validación omitida para cookies que no son de YouTube"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ El archivo de cookie existe pero tiene formato incorrecto"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ No se encontró el archivo de cookie."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Iniciando prueba de cookies de YouTube...\n\nPor favor espera mientras verifico y valido tus cookies."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ ¡Tus cookies de YouTube existentes están funcionando correctamente!\n\nNo necesitas descargar nuevas."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Tus cookies de YouTube existentes están expiradas o son inválidas.\n\n🔄 Descargando nuevas cookies..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ ¡La fuente de cookies de {service} no está configurada!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ ¡La fuente de cookies de {service} debe ser un archivo .txt!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Límite de rango excedido: {range_count} archivos solicitados (máximo {max_img_files}).\n\nUsa uno de estos comandos para descargar el máximo de archivos disponibles:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Cerrar"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Límite de medios excedido: {count} archivos solicitados (máximo {max_count}).\n\nUsa uno de estos comandos para descargar el máximo de archivos disponibles:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Se encontraron <b>{count}</b> elementos multimedia del enlace"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Selecciona rango de descarga:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Suplantación de navegador"
    ARGS_REFERER_DESC_MSG = "Encabezado Referer"
    ARGS_USER_AGENT_DESC_MSG = "Encabezado User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "Bypass de restricciones geográficas"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Verificar certificado SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "Descargar transmisiones en vivo desde el inicio"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "No descargar transmisiones en vivo desde el inicio"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Usar contenedor MPEG-TS para videos HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "Descargar solo un video, no lista de reproducción"
    ARGS_NO_PART_DESC_MSG = "No usar archivos .part"
    ARGS_NO_CONTINUE_DESC_MSG = "No reanudar descargas parciales"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Formato de audio para extracción"
    ARGS_EMBED_METADATA_DESC_MSG = "Insertar metadatos en archivo de video"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Insertar miniatura en archivo de video"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Escribir miniatura en archivo"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Número de fragmentos concurrentes para descargar"
    ARGS_FORCE_IPV4_DESC_MSG = "Forzar conexiones IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "Forzar conexiones IPv6"
    ARGS_XFF_DESC_MSG = "Estrategia de encabezado X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "Tamaño de fragmento HTTP (bytes)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Esperar antes de descargar subtítulos (segundos)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Permitir conexiones de servidor heredadas"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Suprimir validación de certificado HTTPS"
    ARGS_USERNAME_DESC_MSG = "Nombre de usuario de la cuenta"
    ARGS_PASSWORD_DESC_MSG = "Contraseña de la cuenta"
    ARGS_TWOFACTOR_DESC_MSG = "Código de autenticación de dos factores"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Ignorar errores de descarga y continuar"
    ARGS_MIN_FILESIZE_DESC_MSG = "Tamaño mínimo de archivo (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Tamaño máximo de archivo (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Elementos de lista de reproducción para descargar (ej., 1,3,5 o 1-5)"
    ARGS_DATE_DESC_MSG = "Descargar videos subidos en esta fecha (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Descargar videos subidos antes de esta fecha (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Descargar videos subidos después de esta fecha (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Encabezados HTTP personalizados (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Intervalo de espera entre solicitudes (segundos)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Intervalo de espera máximo (segundos)"
    ARGS_RETRIES_DESC_MSG = "Número de reintentos"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Formato de contenedor de video"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Formato de contenedor de salida para fusionar"
    ARGS_SEND_AS_FILE_DESC_MSG = "Enviar todos los medios como documento en lugar de medios"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Suplantar"
    ARGS_REFERER_SHORT_MSG = "Referer"
    ARGS_GEO_BYPASS_SHORT_MSG = "Omitir Geo"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Verificar Cert"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Inicio en Vivo"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Sin Inicio en Vivo"
    ARGS_USER_AGENT_SHORT_MSG = "Agente de Usuario"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Sin Lista"
    ARGS_NO_PART_SHORT_MSG = "Sin Parte"
    ARGS_NO_CONTINUE_SHORT_MSG = "Sin Continuar"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Formato de Audio"
    ARGS_EMBED_METADATA_SHORT_MSG = "Insertar Meta"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Insertar Min"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Escribir Min"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Concurrente"
    ARGS_FORCE_IPV4_SHORT_MSG = "Forzar IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Forzar IPv6"
    ARGS_XFF_SHORT_MSG = "Encabezado XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Tamaño Fragmento"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Esperar Subs"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Conexión Heredada"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Sin Verificar Cert"
    ARGS_USERNAME_SHORT_MSG = "Usuario"
    ARGS_PASSWORD_SHORT_MSG = "Contraseña"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Ignorar Errores"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Tamaño Mín"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Tamaño Máx"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Elementos Lista"
    ARGS_DATE_SHORT_MSG = "Fecha"
    ARGS_DATEBEFORE_SHORT_MSG = "Fecha Antes"
    ARGS_DATEAFTER_SHORT_MSG = "Fecha Después"
    ARGS_HTTP_HEADERS_SHORT_MSG = "Encabezados HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Intervalo Espera"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Espera Máx"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Formato Video"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Formato Fusionar"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Enviar Como Archivo"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ El archivo es demasiado grande. El tamaño máximo es 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Solo se permiten archivos del siguiente formato .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ El archivo no parece cookie.txt (no hay línea '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ Error al leer archivo: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ El archivo de cookie existe y tiene formato correcto"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ ¡El archivo de cookie de {service} es demasiado grande! Máx 100KB, obtuvo {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ Archivo de cookie de {service} descargado y guardado como cookie.txt en tu carpeta.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ La fuente de cookies de {service} no está disponible (estado {status}). Por favor intenta más tarde."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Error al descargar archivo de cookie de {service}. Por favor intenta más tarde."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ El usuario proporcionó un nuevo archivo de cookie.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie actualizado exitosamente:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ No es un cookie válido.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ ¡Las fuentes de cookies de YouTube no están configuradas!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Descargando y verificando cookies de YouTube...\n\nIntento {attempt} de {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Acceso denegado. Solo administradores."
    ADMIN_USER_LOGS_TOTAL_MSG = "Total: <b>{total}</b>\n<b>{user_id}</b> - logs (Últimos 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 ¡teclado activado!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Idioma de subtítulos establecido en: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Idioma de subtítulos establecido en: {flag} {name} con AUTO/TRANS habilitado."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Menú de idioma de subtítulos cerrado."
    SUBS_DOWNLOADING_MSG = "💬 Descargando subtítulos..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Recargando caché de Firebase en memoria..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ No hay COOKIE_URL configurado. Usa /cookie o sube cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Descargando cookies desde URL remota..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ La URL de respaldo COOKIE_URL debe apuntar a un archivo .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ El archivo de cookie de respaldo es demasiado grande (>100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Archivo de cookie de YouTube descargado vía respaldo y guardado como cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fuente de cookie de respaldo no disponible (estado {status}). Prueba /cookie o sube cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Error al descargar cookie de respaldo. Prueba /cookie o sube cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Error inesperado durante la descarga de cookie de respaldo."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ Navegador {browser} no instalado."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookies guardados usando navegador: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Error al guardar cookies: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ Las cookies de YouTube están funcionando correctamente"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ Las cookies de YouTube están expiradas o son inválidas\n\nUsa /cookie para obtener nuevas cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - formato personalizado\n• <code>/format 720</code> - calidad 720p\n• <code>/format 4k</code> - calidad 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Pista enviada."
    FORMAT_MKV_TOGGLE_MSG = "MKV ahora está {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ No hay URL remota configurada"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Formato de archivo inválido"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Archivo demasiado grande"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookies descargados exitosamente"
    COOKIES_SERVER_ERROR_MSG = "❌ Error del servidor {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Descarga fallida"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Error inesperado"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Navegador no instalado."
    COOKIES_MENU_CLOSED_MSG = "Menú cerrado."
    COOKIES_HINT_CLOSED_MSG = "Pista de cookie cerrada."
    IMG_HELP_CLOSED_MSG = "Ayuda cerrada."
    SUBS_LANGUAGE_UPDATED_MSG = "Configuración de idioma de subtítulos actualizada."
    SUBS_MENU_CLOSED_MSG = "Menú de idioma de subtítulos cerrado."
    KEYBOARD_SET_TO_MSG = "Teclado establecido en {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Error al procesar configuración"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo habilitado."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo deshabilitado."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Desenfoque NSFW deshabilitado."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Desenfoque NSFW habilitado."
    SETTINGS_MENU_CLOSED_MSG = "Menú cerrado."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Espera de inundación activa. Intenta más tarde."
    OTHER_HELP_CLOSED_MSG = "Ayuda cerrada."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Mensaje de logs cerrado."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menú cerrado."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Tamaño inválido."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Error al enviar MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Ocurrió un error: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - todos los logs"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - todos {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Descargar desde URL Remota"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Abrir Navegador"
    SELECT_BROWSER_MSG = "Selecciona un navegador para descargar cookies:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "No se encontraron navegadores en este sistema. Puedes descargar cookies desde URL remota o monitorear el estado del navegador:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Abrir Navegador</b> - para monitorear el estado del navegador en mini-app"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Error al ejecutar /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Límite de inundación. Intenta más tarde."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Error al abrir menú de cookies del navegador"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Pista de guardar como cookie cerrada."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Uso:</b>\n<code>/link [quality] URL</code>\n\n<b>Ejemplos:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - mejor calidad\n• /link 720 https://youtube.com/watch?v=... - 720p o inferior\n• /link 720p https://youtube.com/watch?v=... - igual que arriba\n• /link 4k https://youtube.com/watch?v=... - 4K o inferior\n• /link 8k https://youtube.com/watch?v=... - 8K o inferior</blockquote>\n\n<b>Calidad:</b> del 1 al 10000 (ej., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - calidad 8K"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Enlace directo obtenido</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Formato:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Transmisión de audio:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Error al obtener enlaces de transmisión"
    LINK_ERROR_GETTING_MSG = "❌ <b>Error al obtener enlace:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Índice de cookie de YouTube inválido: {selected_index}. El rango disponible es 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Descargando y verificando cookies de YouTube...\n\nIntento {attempt} de {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Descargando y verificando cookies de YouTube...\n\nIntento {attempt} de {total}\n🔍 Probando cookies..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ ¡Cookies de YouTube descargados y validados exitosamente!\n\nFuente usada {source} de {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ ¡Todas las cookies de YouTube están expiradas o no disponibles!\n\nContacta al administrador del bot para reemplazarlas."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ ¡Límite de reintentos de cookies de YouTube excedido!\n\n🔢 Máximo: {limit} intentos por hora\n⏰ Por favor intenta más tarde"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ La etiqueta #{wrong} contiene caracteres prohibidos. Solo se permiten letras, dígitos y _.\nPor favor usa: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **¡Argumento inválido!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Idioma de subtítulos establecido: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Ejemplo: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Idioma seleccionado: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Modo Siempre Preguntar {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Los subtítulos están deshabilitados"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Configuración de subtítulos</b>\n\n{status_text}\n\nSelecciona idioma de subtítulos:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - deshabilitar subtítulos\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Configuración de subtítulos</b>\n\n{status_text}\n\nSelecciona idioma de subtítulos:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Título:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Duración:</b> {duration} seg\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Transmisión de video:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- calidad máxima 720p\n- duración máxima 1.5 horas\n- tamaño máximo de video 500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️ADVERTENCIA: debido al alto impacto en CPU esta función es muy lenta (casi en tiempo real) y limitada a:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Comandos rápidos:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - deshabilitar subtítulos\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - habilitar modo Siempre Preguntar\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - establecer idioma\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - establecer idioma con AUTO/TRANS habilitado\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - habilitar modo Siempre Preguntar\n"
    SUBS_AUTO_SUBS_TEXT = " (auto-subs)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Modo auto-subs {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS deshabilitado vía comando: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Siempre Preguntar habilitado vía comando: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "Idioma SUBS establecido vía comando: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "Idioma SUBS + modo auto establecido vía comando: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Usuario abrió menú /subs."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Usuario estableció idioma de subtítulos en: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Usuario cambió modo AUTO/TRANS a: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Usuario cambió modo Siempre Preguntar a: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Usuario solicitó cookies del navegador."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Teclado de selección de navegador enviado solo con navegadores instalados."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Selección de navegador cerrada."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "COOKIE_URL de respaldo usado exitosamente (fuente oculta)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "COOKIE_URL de respaldo falló: estado={status} (oculto)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "COOKIE_URL de respaldo error inesperado: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Navegador {browser} no instalado."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Cookies guardados usando navegador: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "Archivo de cookie guardado para usuario {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "Archivo de cookie existe, tiene formato correcto, y las cookies de YouTube están funcionando."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Archivo de cookie existe y tiene formato correcto, pero las cookies de YouTube están expiradas."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Archivo de cookie existe y tiene formato correcto."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Archivo de cookie existe pero tiene formato incorrecto."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Archivo de cookie no encontrado."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "URL de cookie de {service} está vacía para usuario {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "URL de cookie de {service} no es .txt (oculto)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "Archivo de cookie de {service} demasiado grande: {size} bytes (fuente oculta)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "Archivo de cookie de {service} descargado para usuario {user_id} (fuente oculta)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Script no encontrado: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Error al enviar mensaje de estado inicial"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Error al ejecutar {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Caché de Firebase recargado por tarea automática."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Caché de Firebase recargado por administrador."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Error al recargar caché de Firebase: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Transmisión iniciada. Texto:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Mensaje de transmisión enviado a todos los usuarios."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Error al transmitir mensaje: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Administrador {user_id} limpió caché para URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Administrador {user_id} inició script de actualización de lista de pornografía: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Script de actualización de lista de pornografía completado exitosamente por administrador {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Script de actualización de lista de pornografía falló por administrador {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Administrador {user_id} intentó ejecutar script inexistente: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Error al ejecutar script de actualización de pornografía por administrador {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Administrador {user_id} inició recarga de caché de pornografía"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Error al recargar caché de pornografía por administrador {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Administrador {user_id} verificó URL para NSFW: {url} - Resultado: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "Usuario solicitó cambio de formato."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "Formato establecido en SIEMPRE_PREGUNTAR."
    FORMAT_UPDATED_BEST_LOG_MSG = "Formato actualizado a mejor: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "Formato actualizado a ID {format_id}: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "Formato actualizado a ID {format_id} (solo audio): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "Formato actualizado a calidad {quality}: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "Formato actualizado a: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "Menú de formato enviado."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "Selección de formato cerrada."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "Pista de formato personalizado enviada."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "Menú de resolución de formato enviado."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "Regresado al menú principal de formato."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "Formato actualizado a: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "Formato establecido en SIEMPRE_PREGUNTAR."
    FORMAT_CODEC_SET_LOG_MSG = "Preferencia de códec establecida en {codec}"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Menú de formato personalizado cerrado"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "Enlace directo extraído para usuario {user_id} desde {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Error al extraer enlace directo para usuario {user_id} desde {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Error en comando link para usuario {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Usuario {user_id} estableció teclado en {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Usuario {user_id} estableció teclado en {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo establecido vía comando: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Usuario abrió menú /mediainfo."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: cerrado."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo habilitado."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo deshabilitado."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Tamaño de división establecido en {size} bytes vía argumento."
    SPLIT_MENU_OPENED_LOG_MSG = "Usuario abrió menú /split."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Selección de división cerrada."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Tamaño de división establecido en {size} bytes."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Proxy establecido vía comando: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Usuario abrió menú /proxy."
    PROXY_MENU_CLOSED_LOG_MSG = "Proxy: cerrado."
    PROXY_ENABLED_LOG_MSG = "Proxy habilitado."
    PROXY_DISABLED_LOG_MSG = "Proxy deshabilitado."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Mensaje de ayuda cerrado."
    AUDIO_HELP_SHOWN_LOG_MSG = "Mostró ayuda /audio"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Usuario solicitó ayuda de lista de reproducción."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Ayuda de lista de reproducción cerrada."
    AUDIO_HINT_CLOSED_LOG_MSG = "Pista de audio cerrada."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Menú de enlace directo creado vía botón LINK para usuario {user_id} desde {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Error al extraer enlace directo vía botón LINK para usuario {user_id} desde {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "Comando LIST ejecutado para usuario {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Incrustación Rápida: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Menú Siempre Preguntar enviado para {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Menú de calidades en caché creado para usuario {user_id} después de error: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Error de menú Siempre Preguntar para {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "El formato está fijado vía configuración /args"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Audio"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Video"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Video"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Siguiente ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Anterior"
    SUBTITLES_NEXT_BUTTON_MSG = "Siguiente ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Todos los campos de texto están vacíos"
    SENDER_VIDEO_DURATION_MSG = "Duración del video:"
    SENDER_UPLOADING_FILE_MSG = "📤 Subiendo archivo..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Subiendo Video..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Duración del video:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 archivo subido."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Información del Video"
    DOWN_UP_NUMBER_MSG = "Número"
    DOWN_UP_TITLE_MSG = "Título"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Video descargado."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Procesando para subir..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Parte dividida {part} archivo subido"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Subida completada"
    DOWN_UP_FILES_UPLOADED_MSG = "archivos subidos"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Cerrar"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CÓDEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DOBLAJES"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 SUBS"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Navegador"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Obteniendo enlace directo..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Obteniendo formatos disponibles..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Obteniendo descripción del video..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Error al obtener descripción: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ La descripción del video no está disponible"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Error al enviar descripción: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Descripción del video enviada al usuario {user_id} para {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Iniciando gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Duración:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Formato:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Navegador:</b> Abrir en navegador web"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Formatos disponibles para"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Cómo usar IDs de formato:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Después de obtener la lista, usa un ID de formato específico:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - descargar formato 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - igual que arriba"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - descargar formato 140 como audio MP3"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Formatos solo de audio detectados"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Estos formatos se descargarán como archivos de audio MP3."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Cómo establecer formato:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Descargar ID de formato específico"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Descargar por calidad"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Descargar mejor calidad"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Siempre preguntar por calidad"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Formatos solo de audio:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Descargar formato 140 como audio MP3"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Estos se descargarán como archivos de audio MP3."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Usa ID de formato de la lista de arriba"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Error: Mensaje original no encontrado."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Página de formatos"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Error al mostrar menú de formatos"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Error al obtener formatos"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Error al obtener formatos disponibles."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Por favor intenta más tarde."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp no puede procesar este contenido"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "El sistema recomienda usar gallery-dl en su lugar."
    ALWAYS_ASK_OPTIONS_MSG = "**Opciones:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Para galerías de imágenes: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Para imágenes individuales: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl a menudo funciona mejor para Instagram, Twitter y otro contenido de redes sociales."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Probar Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Formato fijado vía /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Subtítulos"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Audio doblado"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Los subtítulos están disponibles"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Elige idioma de subtítulos"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Subs no encontrados y no se insertarán"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Repost instantáneo desde caché"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Elige idioma de audio"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW es de pago (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Elige calidad de descarga"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Descargar imagen (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Ver video en poketube"  # TEMPORALMENTE DESHABILITADO: el servicio poketube está caído
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Obtener enlace directo al video"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Mostrar lista de formatos disponibles"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Cambiar ext/códec de video"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Incrustar"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Extraer solo audio"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW es de pago (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Repost instantáneo desde caché"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Ver video en poketube"  # TEMPORALMENTE DESHABILITADO: el servicio poketube está caído
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Elige idioma de audio"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Mejor"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Otros"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝solo subs"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Agrupación inteligente"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Fila de botones de acción agregada (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Filas de botones de acción agregadas (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Botones inferiores agregados a fila existente"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Nueva fila inferior creada"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "No se encontraron videos en la lista de reproducción"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "URL no soportada"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "No se pudo encontrar video"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "No se encontró video"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "No se encontraron medios"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Este tweet no contiene"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Error al obtener información del video:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Error al obtener información del video"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Prueba el comando <code>/clean</code> e intenta de nuevo. Si el error persiste, YouTube requiere autorización. Actualiza cookies.txt vía <code>/cookie</code> o <code>/cookies_from_browser</code> e intenta de nuevo."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Menú cerrado."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Selección Manual de Calidad"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Elige calidad manualmente ya que la detección automática falló:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Todos los Formatos Disponibles"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Calidades Disponibles (desde caché)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Usando calidades en caché - los nuevos formatos pueden no estar disponibles"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Descargando formato"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Descargando"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Descargando con seguimiento de progreso..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Descargando usando formato:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Descargando audio usando formato:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Descargando mejor calidad..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Descargando volcado de base de datos..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Descargando"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Página de formatos"
    ALWAYS_ASK_FROM_CACHE_MSG = "(desde caché)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Error: Mensaje original no encontrado. Puede haber sido eliminado. Por favor envía el enlace nuevamente."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Error: URL original no encontrada. Por favor envía el enlace nuevamente."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Enlace directo obtenido</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Título:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Duración:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Formato:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Transmisión de video:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Transmisión de audio:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Error al obtener enlaces de transmisión"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Enlace directo extraído vía menú Siempre Preguntar para usuario {user_id} desde {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Error al extraer enlace directo vía menú Siempre Preguntar para usuario {user_id} desde {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Enlace directo extraído vía down_and_up_with_format para usuario {user_id} desde {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Error al extraer enlace directo vía down_and_up_with_format para usuario {user_id} desde {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Enlace directo extraído vía down_and_audio para usuario {user_id} desde {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Error al extraer enlace directo vía down_and_audio para usuario {user_id} desde {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Audio enviado desde caché."
    AUDIO_PROCESSING_MSG = "🎙️ El audio se está procesando..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Descargando audio:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Ocurrió un error durante la descarga de audio."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Error al extraer información de audio"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Omitiendo tipo de archivo no soportado en lista de reproducción en índice {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "Archivo de audio no encontrado después de la descarga."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ Error al enviar audio: El tamaño del archivo es igual a 0 B (índice de lista de reproducción {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ El archivo de audio aún se está descargando, por favor espere..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Subiendo archivo de audio...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Error al enviar audio: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Audio de lista de reproducción enviado: {sent}/{total} archivos (calidad={quality}) al usuario{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Error al descargar audio: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Descarga cancelada debido a tiempo de espera (2 horas)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Archivo de video no encontrado: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ Error al enviar video: El tamaño del archivo es igual a 0 B (índice de lista de reproducción {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ El archivo de video aún se está descargando, por favor espere..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Error al procesar video: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Error al enviar archivo de descripción: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 si quieres cambiar el subtítulo del video - responde al video con nuevo texto</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "No se detectaron subtítulos"
    VIDEO_PROGRESS_MSG = "<b>Video:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Audio:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ Límite de URL excedido: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Procesamiento completado"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Los rangos de lista de reproducción no están permitidos en modo de múltiples URLs. Envía solo URLs individuales sin rangos (*1*5, /vid 1-10, etc.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Verifica <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>aquí</a> si tu sitio está soportado"
    ERROR_COOKIE_NEEDED_MSG = "Puedes necesitar <code>cookie</code> para descargar este video. Primero, limpia tu espacio de trabajo vía comando <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Para Youtube - obtén <code>cookie</code> vía comando <b>/cookie</b>. Para cualquier otro sitio soportado - envía tu propio cookie (<a href='https://t.me/tg_ytdlp/203'>guía1</a>) (<a href='https://t.me/tg_ytdlp/214'>guía2</a>) y después envía tu enlace de video nuevamente."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Elige idioma de subtítulos"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "No hay idiomas de audio alternativos"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Elige idioma de audio"
    PAGE_NUMBER_MSG = "Página {page}"
    TOTAL_PROGRESS_MSG = "Progreso Total"
    SUBTITLE_MENU_CLOSED_MSG = "Menú de subtítulos cerrado."
    SUBTITLE_LANGUAGE_SET_MSG = "Idioma de subtítulos establecido: {value}"
    AUDIO_SET_MSG = "Audio establecido: {value}"
    FILTERS_UPDATED_MSG = "Filtros actualizados"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Atrás"
    CLOSE_BUTTON_TEXT = "🔚Cerrar"
    LIST_BUTTON_TEXT = "📃Lista"
    IMAGE_BUTTON_TEXT = "🖼Imagen"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Calidades no detectadas automáticamente\nUsa el botón 'Otros' para ver todos los formatos disponibles.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Transmisión en Vivo Detectada**\n\nLa descarga de transmisiones en vivo en curso o infinitas no está permitida.\n\nPor favor espera a que termine la transmisión e intenta descargar nuevamente cuando:\n• La duración de la transmisión sea conocida\n• La transmisión haya terminado\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Descarga de Transmisión en Vivo</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Fragmento {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Tamaño máx: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Duración total: {duration} seg"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Transmisión en Vivo - Fragmento {chunk}</b>\n⏱ Duración: {duration} seg\n📦 Tamaño: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Fragmento {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Descarga de Transmisión en Vivo Completada</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "Descargados {chunks} fragmento(s)"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Duración total: {duration} seg"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Descarga de Transmisión en Vivo Detenida</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "El directorio del usuario fue eliminado (probablemente por comando /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "El archivo de fragmento fue eliminado (probablemente por comando /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ La transmisión ha terminado"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Por favor selecciona un formato diferente usando el comando `/format`."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Enlace directo obtenido</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Título:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Duración:</b> {duration} seg\n"
    FORMAT_FIELD_MSG = "🎛 <b>Formato:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Transmisión de video:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Transmisión de audio:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Error de Procesamiento de Archivo**\n\nEl video fue descargado pero no pudo ser procesado debido a caracteres inválidos en el nombre del archivo.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Error de Procesamiento de Archivo**\n\nEl video fue descargado pero no pudo ser procesado debido a un error de argumento inválido.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Razón:**\n"
        "• El archivo descargado no es un archivo de video\n"
        "• Podría ser un documento (PDF, DOC, etc.) o un archivo\n\n"
        "**Solución:**\n"
        "• Verifique el enlace - podría llevar a un documento, no a un video\n"
        "• Pruebe con un enlace o fuente diferente\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Razón:**\n"
        "• El archivo no puede ser procesado como video\n"
        "• Puede que no sea un archivo de video o el archivo está dañado\n\n"
        "**Solución:**\n"
        "• Verifique el enlace - podría llevar a un documento, no a un video\n"
        "• Pruebe con un enlace o fuente diferente\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Formato No Disponible**\n\nEl formato de video solicitado no está disponible para este video.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ ID de formato {format_id} no encontrado para este video.\n\nIDs de formato disponibles: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **El formato AV1 no está disponible para este video.**\n\n**Formatos disponibles:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Error de Procesamiento de Archivo**\n\nEl audio fue descargado pero no pudo ser procesado debido a caracteres inválidos en el nombre del archivo.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Error de Procesamiento de Archivo**\n\nEl audio fue descargado pero no pudo ser procesado debido a un error de argumento inválido.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "El usuario ingresó contenido prohibido. No se puede descargar."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "Desenfoque NSFW establecido vía comando: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Usuario abrió menú /nsfw."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: cerrado."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Error al descargar cookie de {service}: estado={status} (url oculta)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Error al descargar cookie de {service}: {error} (url oculta)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Error inesperado al descargar cookie de {service} (url oculta): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Archivo de cookie actualizado para usuario {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Contenido de cookie inválido proporcionado por usuario {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "Las URLs de cookies de YouTube están vacías para usuario {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "Cookies de YouTube descargadas y validadas para usuario {user_id} desde fuente {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Todas las fuentes de cookies de YouTube fallaron para usuario {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Error en comando check_porn por administrador {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Tamaño de parte dividida establecido en {size} bytes."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Subida de video completada con división de archivo."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Videos de lista de reproducción enviados: {sent}/{total} archivos (calidad={quality}) al usuario {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Error desconocido: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Omitiendo tipo de archivo no soportado en lista de reproducción en índice {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg no encontrado. Por favor instala FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Conversión a MP4 fallida: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ ¡Insertar subtítulos puede tomar mucho tiempo (hasta 1 min por 1 min de video)!\n🔥 Comenzando a quemar subtítulos..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Los subtítulos no se pueden insertar debido a límites (calidad/duración/tamaño)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Los subtítulos no están disponibles para el idioma seleccionado"
    ERROR_SENDING_VIDEO_MSG = "❌ Error al enviar video: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Videos de lista de reproducción enviados: {sent}/{total} archivos."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Descarga cancelada debido a tiempo de espera (2 horas)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Error al descargar video: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Error: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON debe ser un objeto (diccionario)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Formato JSON inválido. Por favor proporciona JSON válido."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ El valor debe estar entre {min_val} y {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} establecido en: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Verdadero"
    ARGS_FALSE_BUTTON_MSG = "❌ Falso"
    ARGS_BACK_BUTTON_MSG = "🔙 Atrás"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Cerrar"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Verdadero"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Falso"
    ARGS_NOT_SET_MSG = "No establecido"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ El formato AV1 no está disponible para este video.\n\nFormatos disponibles:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Error al descargar: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ No se encontraron videos en la lista de reproducción en índice {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Conversión de Video Fallida**\n\nEl video no pudo ser convertido a MP4 debido a un error de argumento inválido.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Conversión de Video Fallida**\n\nEl video no pudo ser convertido a MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Error al obtener enlaces de transmisión"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Error al obtener enlace:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ No se encontró contenido en índice {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Error: Mensaje original no encontrado."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Error: URL no encontrada."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Esta URL no se puede incrustar."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ Códec {codec} no disponible para este video"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ Formato {format} no disponible para este video"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Límite de inundación. Intenta más tarde."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Verificar Cookie"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ AUTO (por error YouTube)"
    PROXY_OFF_BUTTON_MSG = "❌ DESACTIVADO"
    PROXY_CLOSE_BUTTON_MSG = "🔚Cerrar"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Seleccionar país:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Borrar selección de país"
    PROXY_COUNTRY_SELECTED_MSG = "✅ País seleccionado: {país} (código: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Proxies disponibles: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 El bot probará HTTP primero y luego SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Proxy habilitado automáticamente para el país seleccionado"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Selección de país borrada"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Selección de país borrada"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ País seleccionado: {país}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Usando país del archivo: {país}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Países disponibles desde el archivo: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 País seleccionado: {país} (código: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ Proxy habilitado para este país"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ Proxy deshabilitado (presione TODO (AUTO) para habilitar)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ ACTIVADO"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ DESACTIVADO"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Cerrar"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV: ACTIVADO"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV: DESACTIVADO"
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ ACTIVADO (Sin Desenfoque)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ACTIVADO (Sin Desenfoque)"
    NSFW_OFF_BLUR_MSG = "✅ DESACTIVADO (Desenfoque)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ DESACTIVADO (Desenfoque)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Limpio"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Error al procesar mensaje de respuesta para usuario {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Error al enviar transmisión al usuario {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Logs de {bot_name}\nUsuario: {user_id}\nTotal de logs: {total}\nHora actual: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nTotal {path}: {count}\nHora actual: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Total de Usuarios: {count}</i>\nÚltimos 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Cachés de pornografía recargados por administrador {admin_id}. Dominios: {domains}, Palabras clave: {keywords}, Sitios: {sites}, LISTA BLANCA: {whitelist}, LISTA GRIS: {greylist}, LISTA NEGRA: {black_list}, PALABRAS CLAVE BLANCAS: {white_keywords}, DOMINIOS PROXY: {proxy_domains}, DOMINIOS PROXY_2: {proxy_2_domains}, CONSULTA LIMPIA: {clean_query}, DOMINIOS SIN COOKIE: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Error al enviar mensaje de tiempo de espera: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Elige idioma</b>"
    LANG_CHANGED_MSG = "✅ Idioma cambiado a {lang_name}"
    LANG_ERROR_MSG = "❌ Error al cambiar idioma"
    LANG_CLOSED_MSG = "Selección de idioma cerrada"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] callback: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Agregando botón de monitoreo de navegador con URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "URL de monitoreo de navegador no configurada: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **¡Configuración de teclado actualizada!**\n\nNueva configuración: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Error al ocultar teclado: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Usando cookies de YouTube funcionando para extracción de enlace para usuario {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "No hay cookies de YouTube funcionando disponibles para extracción de enlace para usuario {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Usando cookies de YouTube existentes para extracción de enlace para usuario {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "No se encontraron cookies de YouTube para extracción de enlace para usuario {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Archivo de cookie global copiado a carpeta del usuario {user_id} para extracción de enlace"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Usuario {user_id} solicitó comando mediainfo"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Usuario {user_id} es administrador: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Usuario {user_id} está en canal: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Acceso denegado para usuario {user_id} - no es administrador y no está en canal"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Acceso concedido para usuario {user_id}"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Este comando solo está disponible para administradores."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Descarga finalizada con soporte de token PO"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Límite de inundación. Intenta más tarde."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ Error de actualización de token REST: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Error al cerrar sesión de Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Error al inicializar estructura de base de datos base: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ No todos los parámetros están establecidos en config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL no está establecido"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey no está establecido para obtener idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Error al descargar volcado de Firebase: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Error al descargar volcado de Firebase vía REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Error en _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Error al ejecutar recarga automática de caché (intento {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Todos los intentos de reintento fallaron"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Iniciando descarga de volcado de Firebase en {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Dependencia no disponible: requests o Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ La base de datos está vacía"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Error al cerrar logger: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Error durante limpieza: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Error de clonación: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Tiempo de espera de clonación agotado"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Excepción de clonación: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Actualización cancelada por usuario"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Repositorio clonado exitosamente"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Respaldos movidos a _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Todos los módulos están cargados"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Limpieza completada al salir"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Señal {signal} recibida, cerrando correctamente..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Por favor espera..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Descargando transmisión HLS:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "esperando fragmentos"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Respaldo {ts} no encontrado en _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Error al restaurar {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Restaurado: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Detalles:</b> {error_details}\n\nDescarga detenida debido a error crítico.\n\n💡 <b>Consejo:</b> Si estás obteniendo error 401 No Autorizado, intenta usar el comando <code>/cookie instagram</code> o envía tus propias cookies para autenticarte con Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Dominio en lista negra de pornografía: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Palabras clave de pornografía encontradas: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Dominio en lista blanca: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Palabras clave de lista blanca encontradas: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ No se encontraron palabras clave de pornografía"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Error de API de TikTok en índice {index}, omitiendo al siguiente audio..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Error de API de TikTok en índice {index}, omitiendo al siguiente video..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "Usuario ingresó una <b>url</b>\n <b>nombre del usuario:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>El usuario ingresó así:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Unirse al Canal"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Registrando manejador: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Descargar mis 5 cookies"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Obtener cookie YT del navegador"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Validar tu archivo de cookie"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Subir cookie personalizada"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Cerrar"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Formatos disponibles para: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Cerrar"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Cerrar"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Cerrar"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Cerrar"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Ayuda cerrada."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Cerrado"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Ocurrió un error"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg no encontrado en PATH o directorio del proyecto. Por favor instala FFmpeg."
    YTDLP_NOT_FOUND_MSG = "Binario yt-dlp no encontrado en PATH o directorio del proyecto. Por favor instala yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "El video se dividirá en {rounds} partes, lo cual puede ser excesivo"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Dividiendo parte de video {current}/{total}: {start_time:.2f}s a {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Error al crear parte dividida {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Parte dividida {part} creada exitosamente: {target_name} ({size} bytes)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Error al dividir parte de video {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Video dividido en {count} partes exitosamente"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Error en el proceso de división de video: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Error al procesar video {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "El archivo de video no existe: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Error al analizar dimensiones '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "No se pudieron determinar las dimensiones del video desde '{size_result}', usando predeterminado: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Error al crear miniatura: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Error al analizar duración del video: {error}, el resultado fue: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Miniatura no creada en {thumb_dir}, usando predeterminado"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Error de ejecución de comando: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Error al crear miniatura con FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Omitiendo sección de configuración no-dict: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Estableciendo {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Usando cookies del usuario: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Usando cookies de YouTube para usuario {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Archivo de cookie global copiado a carpeta del usuario {user_id}"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Usando cookies globales copiadas como cookies del usuario: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Error al copiar archivo de cookie global para usuario {user_id}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Usando --no-cookies para dominio: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy solicitado pero falló al importar/obtener configuración: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Forzando uso de proxy para gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy solicitado pero la configuración de proxy está incompleta"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Ayudante de proxy falló: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Analizando elementos del extractor..."
    GALLERY_DL_ITEM_COUNT_MSG = "Elemento {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Metadatos encontrados (etiqueta 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL encontrada (etiqueta 3): {url}, metadatos: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Metadatos encontrados (heredado): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL encontrada (heredado): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Nombre de archivo encontrado: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Directorio encontrado: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Extensión encontrada: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Analizados {count} elementos, información: {info}, respaldo: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Estableciendo configuración de gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Intentando Estrategia A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "Módulo gallery_dl.extractor no encontrado"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() no disponible en esta compilación"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Llamando extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Ningún extractor coincidió con la URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Estableciendo cookies en extractor: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Error al establecer cookies en extractor: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Extractor encontrado, llamando items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Estrategia A exitosa, obtuvo información: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Estrategia A: extractor.items() no devolvió información válida"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Estrategia A (extractor.find) falló: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Metadatos de respaldo de --get-urls: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Todas las estrategias fallaron al obtener metadatos"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Error al extraer información de imagen: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "Módulo gallery_dl.job no encontrado (¿instalación rota?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob no disponible en esta compilación"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Buscando archivos descargados en directorio gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Intentando encontrar archivos por nombres del extractor"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Error al leer argumentos del usuario para {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Error al procesar video{video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Usuario {user_id} tiene send_as_file habilitado, enviando como documento"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video agotó el tiempo repetidamente; recurriendo a send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Subtítulo demasiado largo, intentando con subtítulo mínimo"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (subtítulo mínimo) agotó el tiempo; recurriendo a send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Error al enviar video con subtítulo mínimo: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Error al enviar archivo de descripción completo: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Error al eliminar archivo de descripción temporal: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Omitiendo match_filter para dominio en NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Verificando cookies de YouTube existentes en URL del usuario para detección de formato para usuario {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Las cookies de YouTube existentes funcionan en URL del usuario para detección de formato para usuario {user_id} - usándolas"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Las cookies de YouTube existentes fallaron en URL del usuario, intentando obtener nuevas para detección de formato para usuario {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Intentando fuente de cookie de YouTube {i} para detección de formato para usuario {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "Las cookies de YouTube de la fuente {i} funcionan en URL del usuario para detección de formato para usuario {user_id} - guardadas en carpeta del usuario"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "Las cookies de YouTube de la fuente {i} no funcionan en URL del usuario para detección de formato para usuario {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Error al descargar cookies de YouTube de la fuente {i} para detección de formato para usuario {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Todas las fuentes de cookies de YouTube fallaron para detección de formato para usuario {user_id}, intentará sin cookies"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "No hay fuentes de cookies de YouTube configuradas para detección de formato para usuario {user_id}, intentará sin cookies"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "No se encontraron cookies de YouTube para detección de formato para usuario {user_id}, intentando obtener nuevas"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Usando cookies de YouTube para detección de formato para usuario {user_id} (ya validadas en menú Always Ask)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "No se encontraron cookies de YouTube para detección de formato para usuario {user_id}, intentando restaurar..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Archivo de cookie global copiado a carpeta del usuario {user_id} para detección de formato"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Error al copiar archivo de cookie global para usuario {user_id}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Usando --no-cookies para dominio en get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "La aplicación aún no está inicializada. No se puede acceder a {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Subtítulo:</b> <code>{caption}</code>\n<b>ID de usuario:</b> <code>{user_id}</code>\n<b>Nombre del usuario:</b> <code>{users_name}</code>\n<b>ID de archivo de video:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Error en caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Error inesperado en caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL del Video</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL falta en la configuración"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin inicializado"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken actualizado"
    DB_LOG_FOR_USER_ADDED_MSG = "Log para usuario agregado"
    DB_DATABASE_CREATED_MSG = "base de datos creada"
    DB_BOT_STARTED_MSG = "Bot iniciado"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY persistido en config.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Parte de lista de reproducción ya en caché: {path_parts}, omitiendo"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: no se encontró caché para ninguna variante de URL/calidad, devolviendo dict vacío"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: conteo rápido para rango grande: {cached_count} videos en caché"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: no se encontró caché para hash {url_hash}, calidad {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: no se encontró caché para ninguna variante de URL, devolviendo None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Acceso denegado. Solo administradores."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 ¡Recarga automática de caché de Firebase actualizada!\n\n📊 Estado: {status}\n⏰ Programación: cada {interval} horas desde las 00:00\n🕒 Próxima recarga: {next_exec} (en {delta_min} minutos)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 ¡Recarga automática de caché de Firebase detenida!\n\n📊 Estado: ❌ DESHABILITADO\n💡 Usa /auto_cache on para volver a habilitar"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Argumento inválido. Usa /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ El intervalo debe estar entre 1 y 168 horas"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Error al establecer intervalo"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ ¡Intervalo de recarga automática de caché de Firebase actualizado!\n\n📊 Estado: ✅ HABILITADO\n⏰ Programación: cada {interval} horas desde las 00:00\n🕒 Próxima recarga: {next_exec} (en {delta_min} minutos)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 ¡Recarga automática de caché de Firebase iniciada!\n\n📊 Estado: ✅ HABILITADO\n⏰ Programación: cada {interval} horas desde las 00:00\n🕒 Próxima recarga: {next_exec} (en {delta_min} minutos)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 ¡Recarga automática de caché de Firebase detenida!\n\n📊 Estado: ❌ DESHABILITADO\n💡 Usa /auto_cache on para volver a habilitar"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Recarga automática HABILITADA; próxima en {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Recarga automática DESHABILITADA por administrador."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Intervalo de recarga automática establecido en {interval}h; próxima en {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Recarga automática iniciada; próxima en {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Recarga automática detenida por administrador."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Caché de Firebase cargado: {count} nodos raíz"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Archivo de caché de Firebase no encontrado, comenzando con caché vacío: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Error al cargar caché de firebase: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Caché de Firebase recargado: {count} nodos raíz"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Archivo de caché de Firebase no encontrado: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Error al recargar caché de firebase: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 ¡Estás baneado del bot! Para desbanear, contacta con {Config.ADMIN_USERNAME}\n<blockquote>P.S. No abandones el canal - serás baneado automáticamente ⛔️</blockquote>\n🌍Cambiar idioma /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ No se encontraron formatos de video. Intentando descargador de imágenes…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram ha limitado el envío de mensajes.\n⏳ Por favor espera: {time_str}\nPara actualizar el temporizador envía la URL nuevamente 2 veces."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">Reproductor VLC (iOS)</a></b>\n\n<i>Haz clic en el botón para copiar la URL de transmisión, luego pégala en la aplicación VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">Reproductor VLC (Android)</a></b>\n\n<i>Haz clic en el botón para copiar la URL de transmisión, luego pégala en la aplicación VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Error al obtener enlace:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Error al enviar archivo de formatos: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Error al obtener formatos:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Analizando... (espera 6 seg)"
    AA_PROCESSING_MSG = "🔎 Analizando..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ La etiqueta #{wrong} contiene caracteres prohibidos. Solo se permiten letras, dígitos y _.\nPor favor usa: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ El bot necesita derechos de administrador para trabajar en el grupo. Por favor, haz que el bot sea administrador de este grupo."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Hola {first_name},\n \n<i>Este bot🤖 puede descargar cualquier video directamente a telegram.😊 Para más información presiona <b>/help</b></i> 👈\n\n<blockquote>P.S. Por el posible contenido 🔞NSFW - descargar de ☁️<b>Almacenamiento en la nube</b>, 📁<b>Compartir archivos</b>, 🔗<b>Acortadores de URL</b> y 🔞<b>Sitios para adultos</b> es de pago! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ NO 🗑<b>elimines/canceles la suscripción al canal @tg_ytdlp</b> y NO 🤖<b>hagas spam de URL/comandos al bot</b> - serás baneado automáticamente ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 No hay archivos para eliminar."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 ¡Todos los archivos eliminados exitosamente!\n\nArchivos eliminados:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ ESPERA HASTA QUE TU DESCARGA ANTERIOR TERMINE"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "La instancia de la aplicación es None en check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict es None, permitiendo descarga"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict es None, permitiendo inserción de subtítulos"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: verificando límites - calidad_máx={max_quality}p, duración_máx={max_duration}s, tamaño_máx={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: claves de info_dict: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Inserción de subtítulos omitida: duración {duration}s excede límite {max_duration}s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Inserción de subtítulos omitida: tamaño {size_mb:.2f}MB excede límite {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Inserción de subtítulos omitida: calidad {width}x{height} (lado mínimo {min_side}p) excede límite {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "lista de reproducción"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Límite de rango excedido para {service}: {count} (máximo {max_count}).\n\nUsa uno de estos comandos para descargar el máximo de archivos disponibles:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Límite de rango excedido para {service}: {count} (máximo {max_count})\nID de usuario: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "Proveedor de token PO deshabilitado en configuración"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} no es un dominio de YouTube, omitiendo token PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "Proveedor de token PO no está disponible en {base_url}, volviendo a extracción estándar de YouTube"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "Caché del proveedor de token PO limpiado, verificará disponibilidad en la próxima solicitud"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Instancia de aplicación aún no disponible"
    HELPER_USER_NAME_MSG = "Usuario"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood wait detectado, esperando {wait_seconds} segundos"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood wait detectado pero no se pudo extraer tiempo, esperando {retry_delay} segundos"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "Error msg_seqno detectado, esperando {retry_delay} segundos"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Configuración de proxy incompleta, usando conexión directa"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Cerrar"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Cerrar"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Cerrar"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Archivo de logs eliminado."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Archivo de etiquetas eliminado."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Archivo de formato eliminado."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Archivo de división eliminado."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Archivo de mediainfo eliminado."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Configuraciones de subtítulos eliminadas."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Configuraciones de teclado eliminadas."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Configuraciones de argumentos eliminadas."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 Configuraciones NSFW eliminadas."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Configuraciones de proxy eliminadas."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Configuraciones de flood wait eliminadas."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Cerrar"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Comando de Descarga de Video"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Uso: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Ejemplos:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (orden directo)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (orden inverso)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "También ver: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Usuario {user_id} cerró comando add_bot_to_group"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Error al extraer ID de YouTube"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Error al descargar miniatura o es demasiado grande"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Elige idioma de audio"
    AA_NO_SUBTITLES_DETECTED_MSG = "No se detectaron subtítulos"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Elige idioma de subtítulos"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Error de Autenticación"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Cuenta No Encontrada"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Cuenta No Disponible"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Límite de Velocidad Excedido"
    GALLERY_DL_NETWORK_ERROR_MSG = "Error de Red"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Contenido No Disponible"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Restricciones Geográficas"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Verificación Requerida"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Violación de Política"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Error Desconocido"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Descarga iniciada</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Cerrar"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Comando de Descarga de Video</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Uso: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Ejemplos:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "También ver: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Límite de inundación. Intenta más tarde."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Uso del Comando Cookie</b>

<code>/cookie</code> - Mostrar menú de cookies
<code>/cookie youtube</code> - Descargar cookies de YouTube
<code>/cookie instagram</code> - Descargar cookies de Instagram
<code>/cookie tiktok</code> - Descargar cookies de TikTok
<code>/cookie x</code> o <code>/cookie twitter</code> - Descargar cookies de Twitter/X
<code>/cookie facebook</code> - Descargar cookies de Facebook
<code>/cookie custom</code> - Mostrar instrucciones de cookie personalizada

<i>Los servicios disponibles dependen de la configuración del bot.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Archivo de cookie eliminado y caché limpiada."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Anterior"
    SUBS_BACK_BUTTON_MSG = "🔙Atrás"
    SUBS_OFF_BUTTON_MSG = "🚫 DESACTIVADO"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs es</code> - establecer idioma"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs es auto</code> - establecer idioma con AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Opciones válidas:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 IDIOMA"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 LIMPIAR"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIES"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MEDIOS"
    SETTINGS_INFO_BUTTON_MSG = "📖 INFORMACIÓN"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ MÁS"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Solo cookies"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Logs "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Etiquetas"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Formato"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Dividir"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Subtítulos"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Teclado"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Argumentos"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Proxy"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Espera de inundación"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Todos los archivos"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Descargar mis 5 cookies"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Obtener cookie YT del navegador"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Validar tu archivo de cookie"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Subir cookie personalizada"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Cambiar calidad y formato"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Activar/Desactivar MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Cambiar tamaño de parte de video dividido"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Descargar video como audio"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Configuración de idioma de subtítulos"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Cómo descargar listas de reproducción"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Descargar imágenes vía gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Enviar tus #etiquetas"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Obtener instrucciones"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Enviar tus logs"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Ayuda de lista de reproducción"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - cómo hacerlo"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Obtener enlaces directos de video"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Habilitar/deshabilitar proxy"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Diseño de teclado"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Ayudante de búsqueda en línea"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - argumentos de yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - Configuración de desenfoque NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Opciones de Limpieza</b>\n\nElige qué limpiar:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Móvil: Activar búsqueda @vid"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Móvil: Activar búsqueda @vid"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 DESACTIVADO"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 COMPLETO"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL de Imágenes]({url})"
    IMAGE_ERROR_MSG = "❌ Error: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Atrás"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - formato personalizado"
    FORMAT_720P_MSG = "• <code>/format 720</code> - calidad 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - calidad 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - calidad 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - ID de formato específico"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - siempre mostrar menú"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/mejor calidad"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Siempre Preguntar (menú + botones)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Otros (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (mejor para PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (mejor para Telegram móvil)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Mejorvideo+Mejoraudio (calidad MÁX)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Personalizado (ingresa el tuyo)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Desde Navegador"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 El Tuyo"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Modo de entrada cerrado automáticamente por inactividad (5 minutos)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Restablecer Todo"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Ver Actual"
    ARGS_BACK_BUTTON_MSG = "🔙 Atrás"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Reenvía este mensaje a tus favoritos para guardar estas configuraciones como plantilla.</i> \n\n<i>Reenvía este mensaje de vuelta aquí para aplicar estas configuraciones.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Argumentos actuales de yt-dlp:\n\nNo hay configuraciones personalizadas configuradas.\n\n---\n\n<i>Reenvía este mensaje a tus favoritos para guardar estas configuraciones como plantilla.</i> \n\n<i>Reenvía este mensaje de vuelta aquí para aplicar estas configuraciones.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Argumentos actuales de yt-dlp:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Exportar Configuraciones"
    ARGS_SETTINGS_READY_MSG = "¡Configuraciones listas para exportar! Reenvía este mensaje a favoritos para guardar."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Argumentos actuales de yt-dlp:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Error al reconocer configuraciones en el mensaje. Asegúrate de enviar una plantilla de configuraciones correcta."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ ¡Configuraciones importadas exitosamente!\n\nParámetros aplicados: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Configuraciones clave:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Error al guardar configuraciones importadas."
    ARGS_ERROR_IMPORTING_MSG = "❌ Ocurrió un error al importar configuraciones."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Descargar Archivos de Cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Elige un servicio para descargar el archivo de cookie."
    COOKIE_MENU_SAVE_INFO_MSG = "Los archivos de cookie se guardarán como cookie.txt en tu carpeta."
    COOKIE_MENU_TIP_HEADER_MSG = "Consejo: También puedes usar comando directo:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – descargar y validar cookies"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – usar una fuente específica por índice (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Luego verifica con <code>/check_cookie</code> (pruebas en RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Siempre Preguntar"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Enlace"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Ver"  # TEMPORALMENTE DESHABILITADO: el servicio poketube está caído
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Descripción"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ RECORTAR"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Recortar Video</b>\n\nDuración del video: <b>{start_time} - {end_time}</b>\n\nPor favor, envía el rango de tiempo deseado en formato:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nEjemplo: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Formato inválido. Por favor usa: <code>HH:MM:SS-HH:MM:SS</code>\n\nEjemplo: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Rango inválido. El tiempo de inicio debe ser menor que el tiempo de finalización."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ El rango de tiempo está fuera de los límites del video.\n\nDuración del video: <b>{start_time} - {end_time}</b>\n\nTu rango debe estar dentro de estos límites."
    AA_ERROR_VIDEO_DURATION_UNKNOWN_MSG = "❌ No se pudo determinar la duración del video. Por favor, inténtalo de nuevo o usa otro video."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>El video será recortado:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Completado parcialmente - {successful_uploads}/{total_files} archivos de audio subidos."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Audio descargado y enviado exitosamente - {total_files} archivos subidos."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Cuenta Privada de TikTok</b>\n\n"
        "Esta cuenta de TikTok es privada o todos los videos son privados.\n\n"
        "<b>💡 Solución:</b>\n"
        "1. Sigue la cuenta @{username}\n"
        "2. Envía tus cookies al bot usando el comando <code>/cookie</code>\n"
        "3. Intenta de nuevo\n\n"
        "<b>¡Después de actualizar las cookies, intenta de nuevo!</b>"
    )

    #######################################################
