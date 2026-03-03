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
    CREDITS_MSG = "<blockquote><i>Gerenciado por</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Alterar idioma: /lang</b>"
    TO_USE_MSG = "<i>Para usar este bot você precisa se inscrever no canal Telegram @tg_ytdlp.</i>\nDepois de ingressar no canal, <b>reenvie seu link de vídeo e o bot fará o download para você</b> ❤️\n\n<blockquote>P.S. Devido a possível conteúdo 🔞NSFW - download de ☁️<b>Armazenamento em nuvem</b>, 📁<b>Compartilhamento de arquivos</b>, 🔗<b>Encurtadores de URL</b> e 🔞<b>Sites adultos</b> é pago! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ NÃO 🗑<b>exclua/cancele a inscrição do canal @tg_ytdlp</b> e NÃO 🤖<b>envie spam de URL/comandos em excesso ao bot</b> - você será banido automaticamente ⛔️</blockquote>"

    ERROR1 = "Link URL não encontrado. Por favor, insira uma URL com <b>https://</b> ou <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Playlists (yt-dlp)</b>

Para baixar playlists, envie sua URL com intervalos <code>*start*end</code> no final. Por exemplo: <code>URL*1*5</code> (primeiros 5 vídeos de 1 a 5 inclusive).<code>URL*-1*-5</code> (últimos 5 vídeos de 1 a 5 inclusive).
Ou você pode usar <code>/vid FROM-TO URL</code>. Por exemplo: <code>/vid 3-7 URL</code> (baixa vídeos de 3 a 7 inclusive do início). <code>/vid -3-7 URL</code> (baixa vídeos de 3 a 7 inclusive do final). Também funciona para o comando <code>/audio</code>.

<b>Exemplos:</b>

🟥 <b>Intervalo de vídeo da playlist do YouTube:</b> (precisa 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(baixa os primeiros 5 vídeos de 1 a 5 inclusive)
🟥 <b>Vídeo único da playlist do YouTube:</b> (precisa 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(baixa apenas o 3º vídeo)

⬛️ <b>Perfil do TikTok:</b> (precisa do seu 🍪)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(baixa os primeiros 10 vídeos do perfil do usuário)

🟪 <b>Stories do Instagram:</b> (precisa do seu 🍪)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(baixa as primeiras 3 stories)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(baixa as primeiras 10 stories do álbum)

🟦 <b>Vídeos do VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(baixa os primeiros 3 vídeos do perfil do usuário/grupo)

⬛️<b>Canais do Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(baixa vídeos de 2 a 4 inclusive do canal)

🟪 <b>Clipes do Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(baixa os primeiros 3 clipes do canal)

🟦 <b>Grupos do Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(baixa os primeiros 2 vídeos do grupo)

🟧 <b>Modelos do Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(baixa os primeiros 2 vídeos do perfil do modelo)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(baixa os primeiros 3 vídeos dos resultados da pesquisa pelo seu prompt)

e assim por diante...
veja <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">lista de sites suportados</a>
</blockquote>

<blockquote expandable>🖼 <b>Imagens (gallery-dl)</b>

Use <code>/img URL</code> para baixar imagens/fotos/álbuns de muitas plataformas.

<b>Exemplos:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Intervalos:</b>
<code>/img 11-20 https://example.com/album</code> — itens 11..20
<code>/img 11- https://example.com/album</code> — de 11 até o final (ou limite do bot)

<i>Plataformas suportadas incluem vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, etc. Lista completa:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">sites suportados pelo gallery-dl</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Bot de Download de Vídeo - Ajuda</b>

📥 <b>Uso Básico:</b>
• Envie qualquer link → bot baixa
  <i>o bot tenta automaticamente baixar vídeos via yt-dlp e imagens via gallery-dl.</i>
• <b>Múltiplas URLs:</b> No modo de seleção de qualidade (<code>/format</code>) você pode enviar até <b>10 URLs</b> em uma mensagem. Cada URL em uma nova linha ou separada por espaços.
• <code>/audio URL</code> → extrair áudio
• <code>/link [quality] URL</code> → obter links diretos
• <code>/proxy</code> → ativar/desativar proxy para todos os downloads
• Responda ao vídeo com texto → alterar legenda

📋 <b>Playlists e Intervalos:</b>
• <code>URL*1*5</code> → baixar primeiros 5 vídeos
• <code>URL*-1*-5</code> → baixar últimos 5 vídeos
• <code>/vid 3-7 URL</code> → torna-se <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → torna-se <code>URL*-3*-7</code>

🍪 <b>Cookies e Privado:</b>
• Envie cookie *.txt para vídeos privados
• <code>/cookie [service]</code> → baixar cookies (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → escolher fonte por índice (1–N)
• <code>/cookies_from_browser</code> → extrair do navegador
• <code>/check_cookie</code> → verificar cookie
• <code>/save_as_cookie</code> → salvar texto como cookie

🧹 <b>Limpeza:</b>
• <code>/clean</code> → apenas arquivos de mídia
• <code>/clean all</code> → tudo
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Configurações:</b>
• <code>/settings</code> → menu de configurações
• <code>/format</code> → qualidade e formato
• <code>/split</code> → dividir vídeo em partes
• <code>/mediainfo on/off</code> → informações de mídia
• <code>/nsfw on/off</code> → desfoque NSFW
• <code>/tags</code> → visualizar tags salvas
• <code>/sub on/off</code> → legendas
• <code>/keyboard</code> → teclado (OFF/1x3/2x3)

🏷️ <b>Tags:</b>
• Adicione <code>#tag1#tag2</code> após a URL
• Tags aparecem nas legendas
• <code>/tags</code> → visualizar todas as tags

🔗 <b>Links Diretos:</b>
• <code>/link URL</code> → melhor qualidade
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → qualidade específica

⚙️ <b>Comandos Rápidos:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → definir qualidade
• <code>/keyboard off/1x3/2x3/full</code> → layout do teclado
• <code>/split 100mb-2000mb</code> → alterar tamanho da parte
• <code>/subs off/ru/en auto</code> → idioma das legendas
• <code>/list URL</code> → lista de formatos disponíveis
• <code>/mediainfo on/off</code> → ativar/desativar informações de mídia
• <code>/proxy on/off</code> → ativar/desativar proxy para todos os downloads

📊 <b>Informações:</b>
• <code>/usage</code> → histórico de downloads
• <code>/search</code> → busca inline via @vid

🖼 <b>Imagens:</b>
• <code>URL</code> → baixar URL de imagens
• <code>/img URL</code> → baixar imagens da URL
• <code>/img 11-20 URL</code> → baixar intervalo específico
• <code>/img 11- URL</code> → baixar do 11º até o final

👨‍💻 <i>Desenvolvedor:</i> @upekshaip
🤝 <i>Contribuidor:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Basta salvar seu cookie como <b><u>cookie.txt</u></b> e enviá-lo ao bot como um documento.\n\n"
        "Você também pode enviar cookies como texto simples com o comando <b><u>/save_as_cookie</u></b>.\n"
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
        "<b><u>Instruções:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>Busca de vídeo</b>

Pressione o botão abaixo para ativar a busca inline via @vid.

<blockquote>No PC, basta digitar <b>"@vid Sua_Consulta_de_Busca"</b> em qualquer chat.</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Comando de Download de Imagem</b>\n\n"
        "Uso: <code>/img URL</code>\n\n"
        "<b>Exemplos:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Plataformas suportadas (exemplos):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, etc. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">lista completa</a></blockquote>"
        "Veja também: "
    )
    
    LINK_HINT_MSG = (
        "Obtenha links diretos de vídeo com seleção de qualidade.\n\n"
        "Uso: /link + URL \n\n"
        "(ex. /link https://youtu.be/abc123)\n"
        "(ex. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Adicionar Bot ao Grupo</b>

Adicione meus bots aos seus grupos para obter recursos aprimorados e limites maiores!
————————————
📊 <b>Limites GRATUITOS Atuais (no DM do Bot):</b>
<blockquote>•🗑 Bagunça desorganizada de todos os arquivos 👎
• Tamanho máximo de 1 arquivo: <b>8 GB </b>
• Qualidade máxima de 1 arquivo: <b>ILIMITADO</b>
• Duração máxima de 1 arquivo: <b>ILIMITADO</b>
• Número máximo de downloads: <b>ILIMITADO</b>
• Máximo de URLs em uma mensagem: <b>10</b> (apenas no modo de seleção de qualidade)
• Máximo de itens de playlist por vez: <b>50</b>
• Máximo de vídeos do TikTok por vez: <b>500</b>
• Máximo de imagens por vez: <b>1000</b>
• Limites de taxa de URL: <b>5/min, 60/hora, 1000/dia</b>
• Limite de comandos: <b>20/min</b>
• Tempo máximo de 1 download: <b>2 horas</b>
• 🔞 Conteúdo NSFW é pago! 1⭐️ = $0.02
• 🆓 TODAS AS OUTRAS MÍDIAS SÃO TOTALMENTE GRATUITAS
• 📝 Todos os logs de conteúdo e cache para meus canais de log para repost instantâneo ao rebaixar</blockquote>

💬<b>Estes limites apenas para vídeo com legendas:</b>
<blockquote>• Duração máxima de vídeo+legendas: <b>1.5 horas</b>
• Tamanho máximo de arquivo de vídeo+legendas: <b>500 MB</b>
• Qualidade máxima de vídeo+legendas: <b>720p</b></blockquote>
————————————
🚀 <b>Benefícios de Grupo Pago (2️⃣x Limites):</b>
<blockquote>•  🗂 Cofre de mídia organizado e estruturado ordenado por tópicos 👍
•  📁 Bots respondem no tópico em que você os chama
•  📌 Fixar automaticamente mensagem de status com progresso do download
•  🖼 Comando /img baixa mídia como álbuns de 10 itens
• Tamanho máximo de 1 arquivo: <b>16 GB</b> ⬆️
• Máximo de URLs em uma mensagem: <b>20</b> ⬆️ (apenas no modo de seleção de qualidade)
• Máximo de itens de playlist por vez: <b>100</b> ⬆️
• Máximo de vídeos do TikTok por vez: 1000 ⬆️
• Máximo de imagens por vez: 2000 ⬆️
• Limites de taxa de URL: <b>10/min, 120/hora, 2000/dia</b> ⬆️
• Limite de comandos: <b>40/min</b> ⬆️
• Tempo máximo de 1 download: <b>4 horas</b> ⬆️
• 🔞 Conteúdo NSFW: Grátis com metadados completos 🆓
• 📢 Não precisa se inscrever no meu canal para grupos
• 👥 Todos os membros do grupo terão acesso às funções pagas!
• 🗒 Sem logs / sem cache para meus canais de log! Você pode rejeitar cópia/repost nas configurações do grupo</blockquote>

💬 <b>Limites 2️⃣x para vídeo com legendas:</b>
<blockquote>• Duração máxima de vídeo+legendas: <b>3 horas</b> ⬆️
• Tamanho máximo de arquivo de vídeo+legendas: <b>1000 MB</b> ⬆️
• Qualidade máxima de vídeo+legendas: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Preços e Configuração:</b>
<blockquote>• Preço: <b>$5/mês</b> por 1 bot no grupo
• Configuração: Entre em contato com @iilililiiillliiliililliilliliiil
• Pagamento: 💎TON ou outros métodos💲
• Suporte: Suporte técnico completo incluído</blockquote>
————————————
Você pode adicionar meus bots ao seu grupo para desbloquear 🔞<b>NSFW</b> gratuito e dobrar (x2️⃣) todos os limites.
Entre em contato comigo se quiser que eu permita que seu grupo use meus bots @iilililiiillliiliililliilliliiil
————————————
💡<b>DICA:</b> <blockquote>Você pode juntar dinheiro com qualquer quantidade de seus amigos (por exemplo, 100 pessoas) e fazer 1 compra para todo o grupo - TODOS OS MEMBROS DO GRUPO TERÃO ACESSO TOTAL ILIMITADO a todas as funções dos bots nesse grupo por apenas <b>0.05$</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>Modo NSFW: LIGADO✅</b>

• O conteúdo NSFW será exibido sem desfoque.
• Spoilers não se aplicarão à mídia NSFW.
• O conteúdo será visível imediatamente

<i>Use /nsfw off para ativar o desfoque</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>Modo NSFW: DESLIGADO</b>

⚠️ <b>Desfoque ativado</b>
• O conteúdo NSFW será ocultado sob spoiler   
• Para visualizar, você precisará clicar na mídia
• Spoilers se aplicarão à mídia NSFW.

<i>Use /nsfw on para desativar o desfoque</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Parâmetro inválido</b>

Use:
• <code>/nsfw on</code> - desativar desfoque
• <code>/nsfw off</code> - ativar desfoque
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Verificando cache...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Processando..."
    DOWNLOADING_MSG = "📥 <b>Baixando mídia...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Baixando imagem...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Download completo</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Baixado:"
    SENT_STATUS_MSG = "Enviado:"
    PENDING_TO_SEND_STATUS_MSG = "Pendente para enviar:"
    TITLE_LABEL_MSG = "Título:"
    MEDIA_COUNT_LABEL_MSG = "Contagem de mídia:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Download concluído, processando áudio..."
    VIDEO_PROCESSING_MSG = "📽 Vídeo está processando..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Enviado do cache</b>\n\nÁlbuns enviados: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Vídeo enviado com sucesso do cache."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Vídeos da playlist enviados do cache ({cached}/{total} arquivos)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} vídeos enviados do cache, baixando os que faltam..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Enviado do cache: {cached}\n🔄 Continuando download..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Não foi possível analisar mídia, prosseguindo com o intervalo máximo permitido (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Não foi possível determinar contagem de mídia, prosseguindo com o intervalo máximo permitido (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Não foi possível determinar contagem total de mídia, prosseguindo com o intervalo especificado {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>URL inválida</b>\n\nPor favor, forneça uma URL válida começando com http:// ou https://"

    ERROR_OCCURRED_MSG = "❌ <b>Erro ocorreu</b>\n\n<code>{url}</code>\n\nErro: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Erro ao enviar vídeo: {error}"
    ERROR_UNKNOWN_MSG = "❌ Erro desconhecido: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Espaço em disco insuficiente para baixar vídeos."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ O tamanho do arquivo excede o limite de {limit} GB. Por favor, selecione um arquivo menor dentro do tamanho permitido."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>Falha ao baixar vídeo com todos os proxies disponíveis</b>\n\nTodas as tentativas de download através de proxies falharam.\nTente:\n• Verificar a funcionalidade do proxy\n• Tentar outro proxy da lista\n• Baixar sem proxy (se possível)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Erro ao obter link:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ O Telegram limitou o envio de mensagens.\n⏳ Por favor, aguarde: {time}\nPara atualizar o temporizador, envie a URL novamente 2 vezes."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ O Telegram limitou o envio de mensagens.\n⏳ Por favor, aguarde: \nPara atualizar o temporizador, envie a URL novamente 2 vezes."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Falha ao baixar legendas"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Links de Stream Diretos</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Título:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Duração:</b> {duration} seg\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Erro: Mensagem original não encontrada."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ A tag #{tag} contém caracteres proibidos. Apenas letras, dígitos e _ são permitidos.\nPor favor, use: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Vídeos da playlist enviados: {sent}/{total} arquivos."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>Dica sobre playlists</b>

Você enviou um link de playlist sem especificar um intervalo. O bot baixou automaticamente o primeiro vídeo (<code>*1*1</code>).

<b>Para baixar vários vídeos de uma playlist, especifique um intervalo:</b>
• <code>URL*1*5</code> — primeiros 5 vídeos (de 1 a 5 inclusive)
• <code>URL*3*3</code> — apenas o 3º vídeo
• <code>/vid 1-10 URL</code> — formato alternativo

Saiba mais: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ Enviado do cache: {cached}/{total} arquivos."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Falha ao obter links de stream"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Selecione um navegador para baixar cookies:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Nenhum navegador encontrado neste sistema. Você pode baixar cookies de URL remota ou monitorar o status do navegador:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Abrir Navegador</b> - para monitorar o status do navegador no mini-app"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Abrir Navegador"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Baixar de URL Remota"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Arquivo de cookie do YouTube baixado via fallback e salvo como cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Nenhum navegador suportado encontrado e nenhum COOKIE_URL configurado. Use /cookie ou envie cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ O COOKIE_URL de fallback deve apontar para um arquivo .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ O arquivo de cookie de fallback é muito grande (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fonte de cookie de fallback indisponível (status {status}). Tente /cookie ou envie cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Erro ao baixar cookie de fallback. Tente /cookie ou envie cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Erro inesperado durante o download do cookie de fallback."
    BTN_CLOSE = "🔚Fechar"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Valor booleano inválido"
    ARGS_CLOSED_MSG = "Fechado"
    ARGS_ALL_RESET_MSG = "✅ Todos os argumentos redefinidos"
    ARGS_RESET_ERROR_MSG = "❌ Erro ao redefinir argumentos"
    ARGS_INVALID_PARAM_MSG = "❌ Parâmetro inválido"
    ARGS_BOOL_SET_MSG = "Definido como {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "Já definido como {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Valor de seleção inválido"
    ARGS_VALUE_SET_MSG = "Definido como {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "Já definido como {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Valor atual:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Exemplos:</b>\n• <code>default</code> - Usar estratégia XFF padrão\n• <code>never</code> - Nunca usar cabeçalho XFF\n• <code>US</code> - Código do país Estados Unidos\n• <code>GB</code> - Código do país Reino Unido\n• <code>DE</code> - Código do país Alemanha\n• <code>FR</code> - Código do país França\n• <code>JP</code> - Código do país Japão\n• <code>192.168.1.0/24</code> - Bloco IP (CIDR)\n• <code>10.0.0.0/8</code> - Intervalo IP privado\n• <code>203.0.113.0/24</code> - Bloco IP público\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Nota:</b> Isso substitui as opções --geo-bypass. Use qualquer código de país de 2 letras ou bloco IP em notação CIDR.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Exemplo:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Por favor, envie seu novo valor."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Intervalo:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Por favor, envie um número."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Exemplos:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Nota:</b> Estes cabeçalhos serão adicionados aos cabeçalhos Referer e User-Agent existentes.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Argumentos atuais do yt-dlp:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Booleano</b> - Interruptores True/False\n• 📋 <b>Seleção</b> - Escolha entre opções\n• 🔢 <b>Numérico</b> - Entrada de número\n• 📝🔧 <b>Texto</b> - Entrada de texto/JSON</blockquote>\n\nEstas configurações serão aplicadas a todos os seus downloads."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "Forçar conexões IPv6",
        "force_ipv4": "Forçar conexões IPv4", 
        "no_live_from_start": "Não baixar streams ao vivo desde o início",
        "live_from_start": "Baixar streams ao vivo desde o início",
        "no_check_certificates": "Suprimir validação de certificado HTTPS",
        "check_certificate": "Verificar certificado SSL",
        "no_playlist": "Baixar apenas vídeo único, não playlist",
        "embed_metadata": "Incorporar metadados no arquivo de vídeo",
        "embed_thumbnail": "Incorporar miniatura no arquivo de vídeo",
        "write_thumbnail": "Escrever miniatura em arquivo",
        "ignore_errors": "Ignorar erros de download e continuar",
        "legacy_server_connect": "Permitir conexões de servidor legadas",
        "concurrent_fragments": "Número de fragmentos simultâneos para baixar",
        "xff": "Estratégia de cabeçalho X-Forwarded-For",
        "user_agent": "Cabeçalho User-Agent",
        "impersonate": "Personificação de navegador",
        "referer": "Cabeçalho Referer",
        "geo_bypass": "Bypass de restrições geográficas",
        "hls_use_mpegts": "Usar MPEG-TS para HLS",
        "no_part": "Não usar arquivos .part",
        "no_continue": "Não retomar downloads parciais",
        "audio_format": "Formato de áudio",
        "video_format": "Formato de vídeo",
        "merge_output_format": "Formato de saída de mesclagem",
        "send_as_file": "Enviar como arquivo",
        "username": "Nome de usuário",
        "password": "Senha",
        "twofactor": "Código de autenticação de dois fatores",
        "min_filesize": "Tamanho mínimo de arquivo (MB)",
        "max_filesize": "Tamanho máximo de arquivo (MB)",
        "playlist_items": "Itens de playlist",
        "date": "Data",
        "datebefore": "Data antes",
        "dateafter": "Data depois",
        "http_headers": "Cabeçalhos HTTP",
        "sleep_interval": "Intervalo de espera",
        "max_sleep_interval": "Intervalo máximo de espera",
        "retries": "Número de tentativas",
        "http_chunk_size": "Tamanho de chunk HTTP",
        "sleep_subtitles": "Espera para legendas"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ Configuração de Argumentos do yt-dlp</b>\n\n<blockquote>📋 <b>Grupos:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ Configuração de Argumentos do yt-dlp</b>\n\n"
        "<blockquote>📋 <b>Grupos:</b>\n"
        "• ✅/❌ <b>Booleano</b> - Interruptores True/False\n"
        "• 📋 <b>Seleção</b> - Escolha entre opções\n"
        "• 🔢 <b>Numérico</b> - Entrada de número\n"
        "• 📝🔧 <b>Texto</b> - Entrada de texto/JSON</blockquote>\n\n"
        "Estas configurações serão aplicadas a todos os seus downloads."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Por favor, aguarde..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Erro ocorreu"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Modo de entrada fechado automaticamente devido à inatividade (5 minutos)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Entrada contém conteúdo potencialmente perigoso: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Entrada muito longa (máx. 1000 caracteres)"
    ARGS_INVALID_URL_MSG = "❌ Formato de URL inválido. Deve começar com http:// ou https://"
    ARGS_INVALID_JSON_MSG = "❌ Formato JSON inválido"
    ARGS_NUMBER_RANGE_MSG = "❌ Número deve estar entre {min_val} e {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Formato de número inválido"
    ARGS_DATE_FORMAT_MSG = "❌ Data deve estar no formato YYYYMMDD (ex.: 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Ano deve estar entre 1900 e 2100"
    ARGS_MONTH_RANGE_MSG = "❌ Mês deve estar entre 01 e 12"
    ARGS_DAY_RANGE_MSG = "❌ Dia deve estar entre 01 e 31"
    ARGS_INVALID_DATE_MSG = "❌ Formato de data inválido"
    ARGS_INVALID_XFF_MSG = "❌ XFF deve ser 'default', 'never', código de país (ex.: US) ou bloco IP (ex.: 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "Nenhum argumento personalizado definido. Todos os parâmetros usam valores padrão."
    ARGS_RESET_SUCCESS_MSG = "✅ Todos os argumentos redefinidos para padrões."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Texto muito longo. Máximo de 500 caracteres."
    ARGS_ERROR_PROCESSING_MSG = "❌ Erro ao processar entrada. Por favor, tente novamente."
    ARGS_BOOL_INPUT_MSG = "❌ Por favor, insira 'True' ou 'False' para a opção Enviar Como Arquivo."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Por favor, forneça um número válido."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Por favor, envie <code>True</code> ou <code>False</code> para ativar/desativar esta opção."
    ARGS_JSON_VALUE_REQUEST_MSG = "Por favor, envie JSON válido."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Você ainda não tem tags."
    TAGS_MESSAGE_CLOSED_MSG = "Mensagem de tags fechada."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Legendas desativadas e modo Sempre Perguntar desligado."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Sempre Perguntar ativado."
    SUBS_LANGUAGE_SET_MSG = "✅ Idioma das legendas definido para: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️AVISO: devido ao alto impacto na CPU, esta função é muito lenta (quase em tempo real) e limitada a:\n"
        "- Qualidade máxima de 720p\n"
        "- Duração máxima de 1,5 hora\n"
        "- Tamanho máximo de vídeo de 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Comandos rápidos:</b>\n"
        "• <code>/subs off</code> - desativar legendas\n"
        "• <code>/subs on</code> - ativar modo Sempre Perguntar\n"
        "• <code>/subs pt</code> - definir idioma\n"
        "• <code>/subs pt auto</code> - definir idioma com AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Legendas estão desativadas"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Idioma selecionado: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Baixando legendas..."
    SUBS_DISABLED_ERROR_MSG = "❌ Legendas estão desativadas. Use /subs para configurar."
    SUBS_YOUTUBE_ONLY_MSG = "❌ O download de legendas é suportado apenas para YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Legendas</b>\n\n"
        "<b>Vídeo:</b> {title}\n"
        "<b>Idioma:</b> {lang}\n"
        "<b>Tipo:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Arquivo SRT de legendas enviado ao usuário."
    SUBS_ERROR_PROCESSING_MSG = "❌ Erro ao processar arquivo de legendas."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Falha ao baixar legendas."
    SUBS_ERROR_MSG = "❌ Erro ao baixar legendas: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Tamanho da parte de divisão definido para: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **Tamanho inválido!**\n\n"
        "**Intervalo válido:** 100MB a 2GB\n\n"
        "**Formatos válidos:**\n"
        "• `100mb` a `2000mb` (megabytes)\n"
        "• `0.1gb` a `2gb` (gigabytes)\n\n"
        "**Exemplos:**\n"
        "• `/split 100mb` - 100 megabytes\n"
        "• `/split 500mb` - 500 megabytes\n"
        "• `/split 1.5gb` - 1,5 gigabytes\n"
        "• `/split 2gb` - 2 gigabytes\n"
        "• `/split 2000mb` - 2000 megabytes (2GB)\n\n"
        "**Predefinições:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Escolha o tamanho máximo da parte para divisão de vídeo:**\n\n"
        "**Intervalo:** 100MB a 2GB\n\n"
        "**Comandos rápidos:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Exemplos:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Menu fechado."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Configurações do Bot</b>\n\nEscolha uma categoria:"
    SETTINGS_MENU_CLOSED_MSG = "Menu fechado."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Opções de Limpeza</b>\n\nEscolha o que limpar:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nEscolha uma ação:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MÍDIA</b>\n\nEscolha uma ação:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFORMAÇÕES</b>\n\nEscolha uma ação:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ MAIS COMANDOS</b>\n\nEscolha uma ação:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Comando executado."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Limite de flood. Tente mais tarde."
    SETTINGS_HINT_SENT_MSG = "Dica enviada."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Ajudante de pesquisa aberto."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Comando desconhecido."
    SETTINGS_HINT_CLOSED_MSG = "Dica fechada."
    SETTINGS_HELP_SENT_MSG = "Enviar texto de ajuda ao usuário"
    SETTINGS_MENU_OPENED_MSG = "Menu /settings aberto"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Ajudante de pesquisa fechado"
    SEARCH_CLOSED_MSG = "Fechado"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proxy {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Erro ao salvar configurações de proxy."
    PROXY_MENU_TEXT_MSG = "Ativar ou desativar o uso de servidor proxy para todas as operações yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Ativar ou desativar o uso de servidores proxy ({config_count} + {file_count} disponíveis) para todas as operações yt-dlp?\n\nQuando ativado ALL (AUTO), os proxies são selecionados automaticamente conforme os países permitidos (indicados no erro do YouTube)."
    PROXY_MENU_CLOSED_MSG = "Menu fechado."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy ativado. Todas as operações yt-dlp usarão proxy."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy ativado. Todas as operações yt-dlp usarão {count} servidores proxy com método de seleção {method}."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Proxy habilitado (AUTO por erro do YouTube).\n\nQuando o YouTube devolver erro de geo-bloqueio, o bot usará apenas proxies dos países indicados nesse erro (sem tentar todos em sequência)."
    PROXY_DISABLED_MSG = "❌ Proxy desativado."
    PROXY_TRYING_COUNTRY_MSG = "🔄 A tentar proxy: {country} ({current}/{total})"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Erro ao salvar configurações de proxy."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy ativado."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy desativado."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ AGUARDE ATÉ QUE SEU DOWNLOAD ANTERIOR TERMINE"
    AUDIO_HELP_MSG = (
        "<b>🎧 Comando de Download de Áudio</b>\n\n"
        "Uso: <code>/audio URL</code>\n\n"
        "<b>Exemplos:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Veja também: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Dica de áudio fechada."
    PLAYLIST_HELP_CLOSED_MSG = "Ajuda de playlist fechada."
    USERLOGS_CLOSED_MSG = "Mensagem de logs fechada."
    HELP_CLOSED_MSG = "Ajuda fechada."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>Configurações de Desfoque NSFW</b>\n\nConteúdo NSFW está <b>{status}</b>.\n\nEscolha se deseja desfocar conteúdo NSFW:"
    NSFW_MENU_CLOSED_MSG = "Menu fechado."
    NSFW_BLUR_DISABLED_MSG = "Desfoque NSFW desativado."
    NSFW_BLUR_ENABLED_MSG = "Desfoque NSFW ativado."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Desfoque NSFW desativado."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Desfoque NSFW ativado."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Ativar ou desativar o envio de MediaInfo para arquivos baixados?"
    MEDIAINFO_MENU_CLOSED_MSG = "Menu fechado."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo ativado. Após o download, as informações do arquivo serão enviadas."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo desativado."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo ativado."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo desativado."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Listar Formatos Disponíveis</b>\n\n"
        "Obter formatos de vídeo/áudio disponíveis para uma URL.\n\n"
        "<b>Uso:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Exemplos:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Como usar IDs de formato:</b>\n"
        "Após obter a lista, use o ID de formato específico:\n"
        "• <code>/format id 401</code> - baixar formato 401\n"
        "• <code>/format id401</code> - mesmo que acima\n"
        "• <code>/format id140 audio</code> - baixar formato 140 como áudio MP3\n\n"
        "Este comando mostrará todos os formatos disponíveis que podem ser baixados."
    )
    LIST_PROCESSING_MSG = "🔄 Obtendo formatos disponíveis..."
    LIST_INVALID_URL_MSG = "❌ Por favor, forneça uma URL válida começando com http:// ou https://"
    LIST_CAPTION_MSG = (
        "📃 Formatos disponíveis para:\n<code>{url}</code>\n\n"
        "💡 <b>Como definir formato:</b>\n"
        "• <code>/format id 134</code> - Baixar ID de formato específico\n"
        "• <code>/format 720p</code> - Baixar por qualidade\n"
        "• <code>/format best</code> - Baixar melhor qualidade\n"
        "• <code>/format ask</code> - Sempre perguntar pela qualidade\n\n"
        "{audio_note}\n"
        "📋 Use o ID de formato da lista acima"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Formatos apenas de áudio:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Baixar formato 140 como áudio MP3\n"
        "• <code>/format id140 audio</code> - mesmo que acima\n"
        "Estes serão baixados como arquivos de áudio MP3.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Erro ao enviar arquivo de formatos: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Falha ao obter formatos:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Ocorreu um erro ao processar o comando"
    LIST_ERROR_CALLBACK_MSG = "Erro ocorrido"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Como usar IDs de formato:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Após obter a lista, use o ID de formato específico:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - baixar formato 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - mesmo que acima\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - baixar formato 140 como áudio MP3\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - mesmo que acima\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Formatos apenas de áudio detectados: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Estes formatos serão baixados como arquivos de áudio MP3.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Formatos apenas de vídeo:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Use o ID de formato da lista acima"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Uso:</b>\n"
        "<code>/link [qualidade] URL</code>\n\n"
        "<b>Exemplos:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - melhor qualidade\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p ou inferior\n"
        "• /link 720p https://youtube.com/watch?v=... - mesmo que acima\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K ou inferior\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K ou inferior"
        "</blockquote>\n\n"
        "<b>Qualidade:</b> de 1 a 10000 (ex.: 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Por favor, forneça uma URL válida"
    LINK_PROCESSING_MSG = "🔗 Obtendo link direto..."
    LINK_DURATION_MSG = "⏱ <b>Duração:</b> {duration} seg\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Stream de vídeo:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Stream de áudio:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Configuração do teclado atualizada!**\n\nNova configuração: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Argumento inválido!**\n\n"
        "Opções válidas: `off`, `1x3`, `2x3`, `full`\n\n"
        "Exemplo: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Configurações do Teclado**\n\n"
        "Atual: **{current}**\n\n"
        "Escolha uma opção:\n\n"
        "Ou use: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 teclado ativado!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Teclado oculto"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 Teclado 1x3 ativado!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 Teclado 2x3 ativado!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Teclado de emoji ativado!"
    KEYBOARD_ERROR_APPLYING_MSG = "Erro ao aplicar configuração do teclado {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Formato definido para: Sempre Perguntar. Você será solicitado pela qualidade cada vez que enviar uma URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Formato definido para: Sempre Perguntar. Agora você será solicitado pela qualidade cada vez que enviar uma URL."
    FORMAT_BEST_UPDATED_MSG = "✅ Formato atualizado para melhor qualidade (prioridade AVC+MP4):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Formato atualizado para ID {id}:\n{format}\n\n💡 <b>Nota:</b> Se este for um formato apenas de áudio, será baixado como arquivo de áudio MP3."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Formato atualizado para ID {id} (apenas áudio):\n{format}\n\n💡 Este será baixado como arquivo de áudio MP3."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Formato atualizado para qualidade {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Formato atualizado para:\n{format}"
    FORMAT_MENU_MSG = (
        "Selecione uma opção de formato ou envie uma personalizada usando:\n"
        "• <code>/format &lt;format_string&gt;</code> - formato personalizado\n"
        "• <code>/format 720</code> - qualidade 720p\n"
        "• <code>/format 4k</code> - qualidade 4K\n"
        "• <code>/format 8k</code> - qualidade 8K\n"
        "• <code>/format id 401</code> - ID de formato específico\n"
        "• <code>/format ask</code> - sempre mostrar menu\n"
        "• <code>/format best</code> - bv+ba/melhor qualidade"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Para usar um formato personalizado, envie o comando no seguinte formato:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Substitua <code>bestvideo+bestaudio/best</code> pela sua string de formato desejada."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Selecione sua resolução e codec desejados:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Formato definido para: Sempre Perguntar. Agora você será solicitado pela qualidade cada vez que enviar uma URL."
    FORMAT_UPDATED_MSG = "✅ Formato atualizado para:\n{format}"
    FORMAT_SAVED_MSG = "✅ Formato salvo."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Escolha de formato atualizada."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Menu de formato personalizado fechado"
    FORMAT_CODEC_SET_MSG = "✅ Codec definido para {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Escolha do navegador atualizada."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Acesso negado. Apenas administrador."
    ACCESS_DENIED_ADMIN = "❌ Acesso negado. Apenas administrador."
    WELCOME_MASTER = "Bem-vindo Mestre 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Desculpe... Ocorreu algum erro durante o download."
    SIZE_LIMIT_EXCEEDED = "❌ O tamanho do arquivo excede o limite de {max_size_gb} GB. Por favor, selecione um arquivo menor dentro do tamanho permitido."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Script não encontrado: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Baixando dump fresco do Firebase usando {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Cache do Firebase recarregado com sucesso!"
    ADMIN_CACHE_FAILED_MSG = "❌ Falha ao recarregar cache do Firebase. Verifique se {cache_file} existe."
    ADMIN_ERROR_RELOADING_MSG = "❌ Erro ao recarregar cache: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Erro ao executar {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Mensagem promocional enviada para todos os outros usuários</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Não é possível enviar a mensagem promocional. Tente responder a uma mensagem\nOu algum erro ocorreu</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ O usuário ainda não baixou nenhum conteúdo...</b> Não existe nos logs"
    ADMIN_INVALID_COMMAND_MSG = "❌ Comando inválido"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ Nenhum dado encontrado no cache para <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Fila está vazia — ninguém saiu do canal ainda."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Fila de banimento</b>\nTotal pendente: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (saiu: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… e {extra} usuários a mais."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Use /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Usuários bloqueados da fila: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Auto-bloqueio ativado: novos que saírem serão banidos imediatamente."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Auto-bloqueio desativado."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Janela de auto-bloqueio agendada definida para cada {interval}."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Log de atividade do canal das últimas {hours} horas (2 dias)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 Últimas {hours} horas (2 dias): entraram {joined}, saíram {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Nenhuma atividade nas últimas {hours} horas (2 dias)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Total: 🟢 {joined} entraram, 🔴 {left} saíram."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Sem acesso ao log de atividade do canal. Bots não podem ler logs de administrador. Forneça CHANNEL_GUARD_SESSION_STRING na configuração com uma sessão de usuário para habilitar este recurso."
    BAN_TIME_USAGE_MSG = "❌ Uso: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Use formatos como 10s, 6m, 5h, 4d, 3w, 2M ou 1y."
    BAN_TIME_SET_MSG = "🕒 Intervalo de varredura do log do canal definido para {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Relatório de varredura do canal\n"
        "Executado em: {run_ts}\n"
        "Intervalo: {interval}\n"
        "Novos que saíram: {new_leavers}\n"
        "Banimentos automáticos: {auto_banned}\n"
        "Pendentes: {pending}\n"
        "Último event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Uso: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Administrador não pode excluir um administrador"
    ADMIN_USER_BLOCKED_MSG = "Usuário bloqueado 🔒❌\n \nID: <code>{user_id}</code>\nData de bloqueio: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> já está bloqueado ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Desculpe! Você não é um administrador"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Uso: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Usuário desbloqueado 🔓✅\n \nID: <code>{user_id}</code>\nData de desbloqueio: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> já está desbloqueado ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Usuários desbloqueados: {count}\n⏱ Timestamp: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Uso: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Usuário ignorado 👁️❌\n \nID: <code>{user_id}</code>\nData de ignorado: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> já está sendo ignorado ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Uso: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Usuário não é mais ignorado 👁️✅\n \nID: <code>{user_id}</code>\nData de não mais ignorado: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> não está sendo ignorado ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Tempo de execução do bot -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Por favor, forneça uma URL para limpar o cache.\nUso: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Por favor, forneça uma URL válida.\nUso: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Cache limpo com sucesso para URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Nenhum cache encontrado para este link."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Erro ao limpar cache: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Acesso negado. Apenas administrador."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Executando script de atualização da lista de pornografia: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Script concluído com sucesso!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Script concluído com sucesso!\n\nSaída:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Script falhou com código de retorno {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Erro ao executar script: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Recarregando caches de pornografia e domínios relacionados..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Caches de pornografia recarregados com sucesso!\n\n"
        "📊 Status atual do cache:\n"
        "• Domínios de pornografia: {porn_domains}\n"
        "• Palavras-chave de pornografia: {porn_keywords}\n"
        "• Sites suportados: {supported_sites}\n"
        "• LISTA BRANCA: {whitelist}\n"
        "• LISTA CINZA: {greylist}\n"
        "• LISTA PRETA: {black_list}\n"
        "• PALAVRAS-CHAVE BRANCAS: {white_keywords}\n"
        "• DOMÍNIOS DE PROXY: {proxy_domains}\n"
        "• DOMÍNIOS DE PROXY_2: {proxy_2_domains}\n"
        "• CONSULTA LIMPA: {clean_query}\n"
        "• DOMÍNIOS SEM COOKIE: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Erro ao recarregar cache de pornografia: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Por favor, forneça uma URL para verificar.\nUso: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Por favor, forneça uma URL válida.\nUso: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Verificando URL para conteúdo NSFW...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Resultado da Verificação de Pornografia</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Status:</b> <b>{status_text}</b>\n\n"
        "<b>Explicação:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Erro ao verificar URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Cookies limpos."
    CLEAN_LOGS_CLEANED_MSG = "logs limpos."
    CLEAN_TAGS_CLEANED_MSG = "tags limpas."
    CLEAN_FORMAT_CLEANED_MSG = "formato limpo."
    CLEAN_SPLIT_CLEANED_MSG = "divisão limpa."
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfo limpo."
    CLEAN_SUBS_CLEANED_MSG = "Configurações de legendas limpas."
    CLEAN_KEYBOARD_CLEANED_MSG = "Configurações do teclado limpas."
    CLEAN_ARGS_CLEANED_MSG = "Configurações de argumentos limpas."
    CLEAN_NSFW_CLEANED_MSG = "Configurações NSFW limpas."
    CLEAN_PROXY_CLEANED_MSG = "Configurações de proxy limpas."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Configurações de espera de flood limpas."
    CLEAN_ALL_CLEANED_MSG = "Todos os arquivos limpos."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nEscolha uma ação:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Arquivo de cookie salvo"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Validação ignorada para cookies não-YouTube"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Arquivo de cookie existe mas tem formato incorreto"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Arquivo de cookie não encontrado."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Iniciando teste de cookies do YouTube...\n\nPor favor, aguarde enquanto verifico e valido seus cookies."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Seus cookies do YouTube existentes estão funcionando corretamente!\n\nNão é necessário baixar novos."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Seus cookies do YouTube existentes estão expirados ou inválidos.\n\n🔄 Baixando novos cookies..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ Fonte de cookies {service} não está configurada!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ Fonte de cookies {service} deve ser um arquivo .txt!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Limite de intervalo excedido: {range_count} arquivos solicitados (máximo {max_img_files}).\n\nUse um destes comandos para baixar o máximo de arquivos disponíveis:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Fechar"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Limite de mídia excedido: {count} arquivos solicitados (máximo {max_count}).\n\nUse um destes comandos para baixar o máximo de arquivos disponíveis:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Encontrados <b>{count}</b> itens de mídia do link"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Selecione o intervalo de download:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Personificação do navegador"
    ARGS_REFERER_DESC_MSG = "Cabeçalho Referer"
    ARGS_USER_AGENT_DESC_MSG = "Cabeçalho User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "Bypass de restrições geográficas"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Verificar certificado SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "Baixar transmissões ao vivo desde o início"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Não baixar transmissões ao vivo desde o início"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Usar contêiner MPEG-TS para vídeos HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "Baixar apenas vídeo único, não playlist"
    ARGS_NO_PART_DESC_MSG = "Não usar arquivos .part"
    ARGS_NO_CONTINUE_DESC_MSG = "Não retomar downloads parciais"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Formato de áudio para extração"
    ARGS_EMBED_METADATA_DESC_MSG = "Incorporar metadados no arquivo de vídeo"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Incorporar miniatura no arquivo de vídeo"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Escrever miniatura em arquivo"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Número de fragmentos simultâneos para baixar"
    ARGS_FORCE_IPV4_DESC_MSG = "Forçar conexões IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "Forçar conexões IPv6"
    ARGS_XFF_DESC_MSG = "Estratégia de cabeçalho X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "Tamanho do chunk HTTP (bytes)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Aguardar antes de baixar legendas (segundos)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Permitir conexões de servidor legadas"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Suprimir validação de certificado HTTPS"
    ARGS_USERNAME_DESC_MSG = "Nome de usuário da conta"
    ARGS_PASSWORD_DESC_MSG = "Senha da conta"
    ARGS_TWOFACTOR_DESC_MSG = "Código de autenticação de dois fatores"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Ignorar erros de download e continuar"
    ARGS_MIN_FILESIZE_DESC_MSG = "Tamanho mínimo do arquivo (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Tamanho máximo do arquivo (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Itens da playlist para baixar (ex.: 1,3,5 ou 1-5)"
    ARGS_DATE_DESC_MSG = "Baixar vídeos enviados nesta data (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Baixar vídeos enviados antes desta data (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Baixar vídeos enviados após esta data (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Cabeçalhos HTTP personalizados (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Intervalo de espera entre solicitações (segundos)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Intervalo de espera máximo (segundos)"
    ARGS_RETRIES_DESC_MSG = "Número de tentativas"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Formato de contêiner de vídeo"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Formato de contêiner de saída para mesclagem"
    ARGS_SEND_AS_FILE_DESC_MSG = "Enviar toda a mídia como documento em vez de mídia"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Personificar"
    ARGS_REFERER_SHORT_MSG = "Referer"
    ARGS_GEO_BYPASS_SHORT_MSG = "Contornar Geo"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Verificar Cert"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Início ao Vivo"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Sem Início ao Vivo"
    ARGS_USER_AGENT_SHORT_MSG = "Agente do Usuário"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Sem Playlist"
    ARGS_NO_PART_SHORT_MSG = "Sem Parte"
    ARGS_NO_CONTINUE_SHORT_MSG = "Sem Continuar"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Formato de Áudio"
    ARGS_EMBED_METADATA_SHORT_MSG = "Incorporar Meta"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Incorporar Miniatura"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Escrever Miniatura"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Simultâneo"
    ARGS_FORCE_IPV4_SHORT_MSG = "Forçar IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Forçar IPv6"
    ARGS_XFF_SHORT_MSG = "Cabeçalho XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Tamanho do Chunk"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Aguardar Legendas"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Conexão Legada"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Sem Verificar Cert"
    ARGS_USERNAME_SHORT_MSG = "Nome de Usuário"
    ARGS_PASSWORD_SHORT_MSG = "Senha"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Ignorar Erros"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Tamanho Mín"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Tamanho Máx"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Itens da Playlist"
    ARGS_DATE_SHORT_MSG = "Data"
    ARGS_DATEBEFORE_SHORT_MSG = "Data Antes"
    ARGS_DATEAFTER_SHORT_MSG = "Data Depois"
    ARGS_HTTP_HEADERS_SHORT_MSG = "Cabeçalhos HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Intervalo de Espera"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Espera Máx"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Formato de Vídeo"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Formato de Mesclagem"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Enviar Como Arquivo"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ O arquivo é muito grande. O tamanho máximo é 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Apenas arquivos no formato .txt são permitidos."
    COOKIES_INVALID_COOKIE_MSG = "❌ O arquivo não parece ser cookie.txt (não há a linha '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ Erro ao ler arquivo: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Arquivo de cookie existe e tem formato correto"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ Arquivo de cookie {service} é muito grande! Máximo 100KB, obtido {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ Arquivo de cookie {service} baixado e salvo como cookie.txt na sua pasta.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ Fonte de cookies {service} está indisponível (status {status}). Por favor, tente novamente mais tarde."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Erro ao baixar arquivo de cookie {service}. Por favor, tente novamente mais tarde."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Usuário forneceu um novo arquivo de cookie.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie atualizado com sucesso:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Não é um cookie válido.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ Fontes de cookies do YouTube não estão configuradas!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Baixando e verificando cookies do YouTube...\n\nTentativa {attempt} de {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Acesso negado. Apenas administrador."
    ADMIN_USER_LOGS_TOTAL_MSG = "Total: <b>{total}</b>\n<b>{user_id}</b> - logs (Últimos 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 teclado ativado!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Idioma das legendas definido para: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Idioma das legendas definido para: {flag} {name} com AUTO/TRANS ativado."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Menu de idioma de legendas fechado."
    SUBS_DOWNLOADING_MSG = "💬 Baixando legendas..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Recarregando cache do Firebase na memória..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Nenhum COOKIE_URL configurado. Use /cookie ou envie cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Baixando cookies de URL remota..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ COOKIE_URL de fallback deve apontar para um arquivo .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Arquivo de cookie de fallback é muito grande (>100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Arquivo de cookie do YouTube baixado via fallback e salvo como cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fonte de cookie de fallback indisponível (status {status}). Tente /cookie ou envie cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Erro ao baixar cookie de fallback. Tente /cookie ou envie cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Erro inesperado durante o download do cookie de fallback."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ Navegador {browser} não instalado."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookies salvos usando navegador: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Falha ao salvar cookies: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ Cookies do YouTube estão funcionando corretamente"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ Cookies do YouTube estão expirados ou inválidos\n\nUse /cookie para obter novos cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - formato personalizado\n• <code>/format 720</code> - qualidade 720p\n• <code>/format 4k</code> - qualidade 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Dica enviada."
    FORMAT_MKV_TOGGLE_MSG = "MKV agora está {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Nenhuma URL remota configurada"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Formato de arquivo inválido"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Arquivo muito grande"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookies baixados com sucesso"
    COOKIES_SERVER_ERROR_MSG = "❌ Erro do servidor {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Download falhou"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Erro inesperado"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Navegador não instalado."
    COOKIES_MENU_CLOSED_MSG = "Menu fechado."
    COOKIES_HINT_CLOSED_MSG = "Dica de cookie fechada."
    IMG_HELP_CLOSED_MSG = "Ajuda fechada."
    SUBS_LANGUAGE_UPDATED_MSG = "Configurações de idioma de legendas atualizadas."
    SUBS_MENU_CLOSED_MSG = "Menu de idioma de legendas fechado."
    KEYBOARD_SET_TO_MSG = "Teclado definido para {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Erro ao processar configuração"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo ativado."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo desativado."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Desfoque NSFW desativado."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Desfoque NSFW ativado."
    SETTINGS_MENU_CLOSED_MSG = "Menu fechado."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Espera de flood ativa. Tente mais tarde."
    OTHER_HELP_CLOSED_MSG = "Ajuda fechada."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Mensagem de logs fechada."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menu fechado."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Tamanho inválido."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Erro ao enviar MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Ocorreu um erro: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - todos os logs"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - todos {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Baixar de URL Remota"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Abrir Navegador"
    SELECT_BROWSER_MSG = "Selecione um navegador para baixar cookies:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Nenhum navegador encontrado neste sistema. Você pode baixar cookies de URL remota ou monitorar o status do navegador:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Abrir Navegador</b> - para monitorar o status do navegador no mini-app"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Falha ao executar /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Limite de flood. Tente mais tarde."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Falha ao abrir menu de cookies do navegador"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Dica de salvar como cookie fechada."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Uso:</b>\n<code>/link [qualidade] URL</code>\n\n<b>Exemplos:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - melhor qualidade\n• /link 720 https://youtube.com/watch?v=... - 720p ou inferior\n• /link 720p https://youtube.com/watch?v=... - mesmo que acima\n• /link 4k https://youtube.com/watch?v=... - 4K ou inferior\n• /link 8k https://youtube.com/watch?v=... - 8K ou inferior</blockquote>\n\n<b>Qualidade:</b> de 1 a 10000 (ex.: 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - qualidade 8K"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Link direto obtido</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Formato:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Stream de áudio:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Falha ao obter links de stream"
    LINK_ERROR_GETTING_MSG = "❌ <b>Erro ao obter link:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Índice de cookie do YouTube inválido: {selected_index}. Intervalo disponível é 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Baixando e verificando cookies do YouTube...\n\nTentativa {attempt} de {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Baixando e verificando cookies do YouTube...\n\nTentativa {attempt} de {total}\n🔍 Testando cookies..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ Cookies do YouTube baixados e validados com sucesso!\n\nFonte usada {source} de {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Todos os cookies do YouTube estão expirados ou indisponíveis!\n\nEntre em contato com o administrador do bot para substituí-los."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ Limite de tentativas de cookie do YouTube excedido!\n\n🔢 Máximo: {limit} tentativas por hora\n⏰ Por favor, tente novamente mais tarde"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Tag #{wrong} contém caracteres proibidos. Apenas letras, dígitos e _ são permitidos.\nPor favor, use: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Argumento inválido!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Idioma das legendas definido: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Exemplo: `/subs pt auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Idioma selecionado: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Modo Sempre Perguntar {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Legendas estão desativadas"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Configurações de legendas</b>\n\n{status_text}\n\nSelecione o idioma das legendas:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - desativar legendas\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Configurações de legendas</b>\n\n{status_text}\n\nSelecione o idioma das legendas:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Título:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Duração:</b> {duration} seg\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Stream de vídeo:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- Qualidade máxima de 720p\n- Duração máxima de 1,5 hora\n- Tamanho máximo de vídeo de 500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️AVISO: devido ao alto impacto na CPU, esta função é muito lenta (quase em tempo real) e limitada a:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Comandos rápidos:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - desativar legendas\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - ativar modo Sempre Perguntar\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs pt` - definir idioma\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs pt auto` - definir idioma com AUTO/TRANS ativado\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - ativar modo Sempre Perguntar\n"
    SUBS_AUTO_SUBS_TEXT = " (legendas automáticas)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Modo de legendas automáticas {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS desabilitado via comando: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Sempre Perguntar habilitado via comando: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "Idioma de SUBS definido via comando: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "Idioma de SUBS + modo automático definido via comando: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Usuário abriu o menu /subs."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Usuário definiu idioma de legenda para: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Usuário alternou modo AUTO/TRANS para: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Usuário alternou modo Sempre Perguntar para: {new_always_ask}"
    
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
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Falha ao enviar mensagem de status inicial"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Erro ao executar {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Cache do Firebase recarregado por tarefa automática."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Cache do Firebase recarregado por administrador."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Erro ao recarregar cache do Firebase: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Transmissão iniciada. Texto:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Mensagem de transmissão enviada para todos os usuários."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Falha ao transmitir mensagem: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Admin {user_id} limpou o cache para URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Admin {user_id} iniciou o script de atualização da lista de pornografia: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Script de atualização da lista de pornografia concluído com sucesso pelo admin {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Script de atualização da lista de pornografia falhou pelo admin {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Admin {user_id} tentou executar script inexistente: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Erro ao executar script de atualização de pornografia pelo admin {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Administrador {user_id} iniciou recarregamento de cache porn"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Erro ao recarregar cache de pornografia pelo admin {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Admin {user_id} verificou URL para NSFW: {url} - Resultado: {status}"
    
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
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Menu de formato personalizado fechado"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "Link direto extraído para o usuário {user_id} de {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Falha ao extrair link direto para o usuário {user_id} de {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Erro no comando link para o usuário {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Usuário {user_id} definiu teclado para {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Usuário {user_id} definiu teclado para {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo definido via comando: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Usuário abriu o menu /mediainfo."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: fechado."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo habilitado."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo desabilitado."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Tamanho de divisão definido para {size} bytes via argumento."
    SPLIT_MENU_OPENED_LOG_MSG = "Usuário abriu o menu /split."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Seleção de divisão fechada."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Split size set to {size} bytes."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Proxy definido via comando: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Usuário abriu o menu /proxy."
    PROXY_MENU_CLOSED_LOG_MSG = "Proxy: fechado."
    PROXY_ENABLED_LOG_MSG = "Proxy habilitado."
    PROXY_DISABLED_LOG_MSG = "Proxy desabilitado."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Mensagem de ajuda fechada."
    AUDIO_HELP_SHOWN_LOG_MSG = "Mostrou ajuda /audio"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Usuário solicitou ajuda de playlist."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Ajuda de playlist fechada."
    AUDIO_HINT_CLOSED_LOG_MSG = "Dica de áudio fechada."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Menu de link direto criado via botão LINK para usuário {user_id} de {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Falha ao extrair link direto via botão LINK para usuário {user_id} de {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "Comando LIST executado para usuário {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Incorporação Rápida: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Menu Sempre Perguntar enviado para {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Menu de qualidades em cache criado para usuário {user_id} após erro: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Erro no menu Sempre Perguntar para {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Formato está fixo via configurações /args"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Áudio"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Vídeo"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Vídeo"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Próximo ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Anterior"
    SUBTITLES_NEXT_BUTTON_MSG = "Próximo ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Todos os campos de texto estão vazios"
    SENDER_VIDEO_DURATION_MSG = "Duração do vídeo:"
    SENDER_UPLOADING_FILE_MSG = "📤 Enviando arquivo..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Enviando Vídeo..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Duração do vídeo:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 arquivo enviado."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Informações do Vídeo"
    DOWN_UP_NUMBER_MSG = "Número"
    DOWN_UP_TITLE_MSG = "Título"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Vídeo baixado."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Processando para envio..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Parte dividida {part} arquivo enviado"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Envio completo"
    DOWN_UP_FILES_UPLOADED_MSG = "arquivos enviados"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Fechar"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBLAGENS"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 LEGENDAS"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Navegador"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Obtendo link direto..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Obtendo formatos disponíveis..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Obtendo descrição do vídeo..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Erro ao obter descrição: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ A descrição do vídeo não está disponível"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Erro ao enviar descrição: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Descrição do vídeo enviada ao usuário {user_id} para {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Iniciando gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Duração:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Formato:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Navegador:</b> Abrir no navegador web"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Formatos disponíveis para"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Como usar IDs de formato:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Após obter a lista, use o ID de formato específico:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - baixar formato 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - mesmo que acima"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - baixar formato 140 como áudio MP3"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Formatos apenas de áudio detectados"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Estes formatos serão baixados como arquivos de áudio MP3."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Como definir formato:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Baixar ID de formato específico"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Baixar por qualidade"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Baixar melhor qualidade"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Sempre perguntar pela qualidade"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Formatos apenas de áudio:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Baixar formato 140 como áudio MP3"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Estes serão baixados como arquivos de áudio MP3."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Use o ID de formato da lista acima"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Erro: Mensagem original não encontrada."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Página de formatos"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Erro ao mostrar menu de formatos"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Erro ao obter formatos"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Erro ao obter formatos disponíveis."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Por favor, tente novamente mais tarde."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp não pode processar este conteúdo"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "O sistema recomenda usar gallery-dl em vez disso."
    ALWAYS_ASK_OPTIONS_MSG = "**Opções:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Para galerias de imagens: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Para imagens únicas: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl geralmente funciona melhor para Instagram, Twitter e outro conteúdo de mídia social."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Tentar Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Formato fixo via /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Legendas"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Áudio dublado"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Legendas estão disponíveis"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Escolher idioma das legendas"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Legendas não encontradas e não serão incorporadas"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Repostagem instantânea do cache"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Escolher idioma do áudio"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW é pago (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Escolher qualidade de download"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Baixar imagem (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Assistir vídeo no poketube"  # TEMPORARIAMENTE DESABILITADO: o serviço poketube está fora do ar
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Obter link direto para o vídeo"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Mostrar lista de formatos disponíveis"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Alterar extensão/codec do vídeo"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Incorporar"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Extrair apenas áudio"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW é pago (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Repostagem instantânea do cache"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Assistir vídeo no poketube"  # TEMPORARIAMENTE DESABILITADO: o serviço poketube está fora do ar
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Escolher idioma do áudio"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Melhor"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Outro"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝apenas leg"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Agrupamento inteligente"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Linha de botão de ação adicionada (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Linhas de botão de ação adicionadas (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Botões inferiores adicionados à linha existente"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Nova linha inferior criada"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Nenhum vídeo encontrado na playlist"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "URL não suportada"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Nenhum vídeo pôde ser encontrado"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Nenhum vídeo encontrado"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Nenhuma mídia encontrada"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Este tweet não contém"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Erro ao recuperar informações do vídeo:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Erro ao recuperar informações do vídeo"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Tente o comando <code>/clean</code> e tente novamente. Se o erro persistir, o YouTube requer autorização. Atualize cookies.txt via <code>/cookie</code> ou <code>/cookies_from_browser</code> e tente novamente."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Menu fechado."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Seleção Manual de Qualidade"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Escolha a qualidade manualmente, pois a detecção automática falhou:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Todos os Formatos Disponíveis"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Qualidades Disponíveis (do cache)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Usando qualidades em cache - novos formatos podem não estar disponíveis"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Baixando formato"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Baixando"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Baixando com rastreamento de progresso..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Baixando usando formato:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Baixando áudio usando formato:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Baixando melhor qualidade..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Baixando dump do banco de dados..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Baixando"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Página de formatos"
    ALWAYS_ASK_FROM_CACHE_MSG = "(do cache)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Erro: Mensagem original não encontrada. Ela pode ter sido excluída. Por favor, envie o link novamente."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Erro: URL original não encontrada. Por favor, envie o link novamente."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Link direto obtido</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Título:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Duração:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Formato:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Stream de vídeo:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Stream de áudio:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Falha ao obter links de stream"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Link direto extraído via menu Sempre Perguntar para usuário {user_id} de {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Falha ao extrair link direto via menu Sempre Perguntar para usuário {user_id} de {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Link direto extraído via down_and_up_with_format para usuário {user_id} de {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Falha ao extrair link direto via down_and_up_with_format para usuário {user_id} de {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Link direto extraído via down_and_audio para usuário {user_id} de {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Falha ao extrair link direto via down_and_audio para usuário {user_id} de {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Áudio enviado do cache."
    AUDIO_PROCESSING_MSG = "🎙️ Áudio está processando..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Baixando áudio:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Erro ocorrido durante o download do áudio."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Falha ao extrair informações do áudio"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Ignorando tipo de arquivo não suportado na playlist no índice {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "Arquivo de áudio não encontrado após o download."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ Erro ao enviar áudio: O tamanho do arquivo é igual a 0 B (índice da playlist {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ O arquivo de áudio ainda está sendo baixado, aguarde..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Enviando arquivo de áudio...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Falha ao enviar áudio: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Áudio da playlist enviado: {sent}/{total} arquivos (qualidade={quality}) para usuário{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Falha ao baixar áudio: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Download cancelado devido ao tempo limite (2 horas)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Arquivo de vídeo não encontrado: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ Erro ao enviar vídeo: O tamanho do arquivo é igual a 0 B (índice da playlist {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ O arquivo de vídeo ainda está sendo baixado, aguarde..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Erro ao processar vídeo: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Erro ao enviar arquivo de descrição: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 se você quiser alterar a legenda do vídeo - responda ao vídeo com novo texto</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Nenhuma legenda detectada"
    VIDEO_PROGRESS_MSG = "<b>Vídeo:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Áudio:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ Limite de URL excedido: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Processamento concluído"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Intervalos de playlist não são permitidos no modo de múltiplas URLs. Envie apenas URLs únicas sem intervalos (*1*5, /vid 1-10, etc.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Verifique <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>aqui</a> se seu site é suportado"
    ERROR_COOKIE_NEEDED_MSG = "Você pode precisar de <code>cookie</code> para baixar este vídeo. Primeiro, limpe seu workspace via comando <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Para Youtube - obtenha <code>cookie</code> via comando <b>/cookie</b>. Para qualquer outro site suportado - envie seu próprio cookie (<a href='https://t.me/tg_ytdlp/203'>guia1</a>) (<a href='https://t.me/tg_ytdlp/214'>guia2</a>) e depois envie seu link de vídeo novamente."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Escolher idioma das legendas"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Nenhum idioma de áudio alternativo"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Escolher idioma do áudio"
    PAGE_NUMBER_MSG = "Página {page}"
    TOTAL_PROGRESS_MSG = "Progresso Total"
    SUBTITLE_MENU_CLOSED_MSG = "Menu de legendas fechado."
    SUBTITLE_LANGUAGE_SET_MSG = "Idioma das legendas definido: {value}"
    AUDIO_SET_MSG = "Áudio definido: {value}"
    FILTERS_UPDATED_MSG = "Filtros atualizados"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Voltar"
    CLOSE_BUTTON_TEXT = "🔚Fechar"
    LIST_BUTTON_TEXT = "📃Lista"
    IMAGE_BUTTON_TEXT = "🖼Imagem"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Qualidades não detectadas automaticamente\nUse o botão 'Outro' para ver todos os formatos disponíveis.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Transmissão ao Vivo Detectada**\n\nO download de transmissões ao vivo em andamento ou infinitas não é permitido.\n\nPor favor, aguarde a transmissão terminar e tente baixar novamente quando:\n• A duração da transmissão for conhecida\n• A transmissão tiver terminado\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Download de Transmissão ao Vivo</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Chunk {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Tamanho máx: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Duração total: {duration} seg"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Transmissão ao Vivo - Chunk {chunk}</b>\n⏱ Duração: {duration} seg\n📦 Tamanho: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Chunk {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Download de Transmissão ao Vivo Concluído</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "Baixados {chunks} chunk(s)"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Duração total: {duration} seg"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Download de Transmissão ao Vivo Parado</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Diretório do usuário foi excluído (provavelmente pelo comando /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "Arquivo chunk foi excluído (provavelmente pelo comando /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Transmissão terminou"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Por favor, selecione um formato diferente usando o comando <code>/format</code>."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Link direto obtido</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Título:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Duração:</b> {duration} seg\n"
    FORMAT_FIELD_MSG = "🎛 <b>Formato:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Stream de vídeo:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Stream de áudio:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Erro de Processamento de Arquivo**\n\nO vídeo foi baixado mas não pôde ser processado devido a caracteres inválidos no nome do arquivo.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Erro de Processamento de Arquivo**\n\nO vídeo foi baixado mas não pôde ser processado devido a um erro de argumento inválido.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Motivo:**\n"
        "• O arquivo baixado não é um arquivo de vídeo\n"
        "• Pode ser um documento (PDF, DOC, etc.) ou arquivo\n\n"
        "**Solução:**\n"
        "• Verifique o link - pode levar a um documento, não a um vídeo\n"
        "• Tente um link ou fonte diferente\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Motivo:**\n"
        "• O arquivo não pode ser processado como vídeo\n"
        "• Pode não ser um arquivo de vídeo ou o arquivo está corrompido\n\n"
        "**Solução:**\n"
        "• Verifique o link - pode levar a um documento, não a um vídeo\n"
        "• Tente um link ou fonte diferente\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Formato Não Disponível**\n\nO formato de vídeo solicitado não está disponível para este vídeo.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ ID de formato {format_id} não encontrado para este vídeo.\n\nIDs de formato disponíveis: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **Formato AV1 não está disponível para este vídeo.**\n\n**Formatos disponíveis:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Erro de Processamento de Arquivo**\n\nO áudio foi baixado mas não pôde ser processado devido a caracteres inválidos no nome do arquivo.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Erro de Processamento de Arquivo**\n\nO áudio foi baixado mas não pôde ser processado devido a um erro de argumento inválido.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Usuário inseriu conteúdo proibido. Não pode ser baixado."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "Desfoque NSFW definido via comando: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Usuário abriu menu /nsfw."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: fechado."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Falha ao baixar cookie {service}: status={status} (url oculto)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Erro ao baixar cookie {service}: {error} (url oculto)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Erro inesperado ao baixar cookie {service} (url oculto): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Arquivo de cookie atualizado para usuário {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Conteúdo de cookie inválido fornecido por usuário {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "URLs de cookie do YouTube estão vazias para usuário {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "Cookies do YouTube baixados e validados para usuário {user_id} da fonte {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Todas as fontes de cookie do YouTube falharam para usuário {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Erro no comando check_porn por administrador {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Tamanho da parte dividida definido para {size} bytes."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Envio de vídeo concluído com divisão de arquivo."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Vídeos da playlist enviados: {sent}/{total} arquivos (qualidade={quality}) para usuário {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Erro desconhecido: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Ignorando tipo de arquivo não suportado na playlist no índice {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg não encontrado. Por favor, instale FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Conversão para MP4 falhou: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Incorporar legendas pode levar muito tempo (até 1 min por 1 min de vídeo)!\n🔥 Iniciando queima de legendas..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Legendas não podem ser incorporadas devido a limites (qualidade/duração/tamanho)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Legendas não estão disponíveis para o idioma selecionado"
    ERROR_SENDING_VIDEO_MSG = "❌ Erro ao enviar vídeo: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Vídeos da playlist enviados: {sent}/{total} arquivos."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Download cancelado devido ao tempo limite (2 horas)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Falha ao baixar vídeo: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Erro: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON deve ser um objeto (dicionário)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Formato JSON inválido. Por favor, forneça JSON válido."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Valor deve estar entre {min_val} e {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} definido para: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Verdadeiro"
    ARGS_FALSE_BUTTON_MSG = "❌ Falso"
    ARGS_BACK_BUTTON_MSG = "🔙 Voltar"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Fechar"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Verdadeiro"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Falso"
    ARGS_NOT_SET_MSG = "Não definido"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ Formato AV1 não está disponível para este vídeo.\n\nFormatos disponíveis:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Erro ao baixar: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ Nenhum vídeo encontrado na playlist no índice {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Conversão de Vídeo Falhou**\n\nO vídeo não pôde ser convertido para MP4 devido a um erro de argumento inválido.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Conversão de Vídeo Falhou**\n\nO vídeo não pôde ser convertido para MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Falha ao obter links de stream"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Erro ao obter link:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ Nenhum conteúdo encontrado no índice {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Erro: Mensagem original não encontrada."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Erro: URL não encontrada."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Esta URL não pode ser incorporada."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ Codec {codec} não está disponível para este vídeo"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ Formato {format} não está disponível para este vídeo"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Limite de flood. Tente mais tarde."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Verificar Cookie"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ AUTO (por erro YouTube)"
    PROXY_OFF_BUTTON_MSG = "❌ OFF"
    PROXY_CLOSE_BUTTON_MSG = "🔚Fechar"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Selecione o país:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Limpar seleção de país"
    PROXY_COUNTRY_SELECTED_MSG = "✅ País selecionado: {country} (código: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Proxies disponíveis: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 O bot tentará primeiro o HTTP, depois o SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Proxy ativado automaticamente para o país selecionado"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Seleção de país desmarcada"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Seleção de país desmarcada"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ País selecionado: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Usando o país do arquivo: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Países disponíveis no arquivo: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 País selecionado: {country} (código: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ Proxy habilitado para este país"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ Proxy desativado (pressione ALL (AUTO) para ativar)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ ON"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ OFF"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Fechar"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ ON (Sem Desfoque)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ON (Sem Desfoque)"
    NSFW_OFF_BLUR_MSG = "✅ OFF (Desfoque)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ OFF (Desfoque)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Limpar"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Erro ao processar mensagem de resposta para usuário {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Erro ao enviar transmissão para usuário {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Logs de {bot_name}\nUsuário: {user_id}\nTotal de logs: {total}\nHora atual: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nTotal {path}: {count}\nHora atual: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Total de Usuários: {count}</i>\nÚltimos 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Caches porn recarregados por administrador {admin_id}. Domains: {domains}, Keywords: {keywords}, Sites: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Erro ao enviar mensagem de tempo limite: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Escolher idioma</b>"
    LANG_CHANGED_MSG = "✅ Idioma alterado para {lang_name}"
    LANG_ERROR_MSG = "❌ Erro ao alterar idioma"
    LANG_CLOSED_MSG = "Seleção de idioma fechada"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] callback: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Adicionando botão de monitoramento do navegador com URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "URL de monitoramento do navegador não configurada: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Configuração do teclado atualizada!**\n\nNova configuração: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Falha ao ocultar teclado: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Usando cookies do YouTube funcionais para extração de link para usuário {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Nenhum cookie do YouTube funcionando disponível para extração de link para usuário {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Usando cookies do YouTube existentes para extração de link para usuário {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Nenhum cookie do YouTube encontrado para extração de link para usuário {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Arquivo de cookie global copiado para pasta do usuário {user_id} para extração de link"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Usuário {user_id} solicitou comando mediainfo"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Usuário {user_id} é administrador: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Usuário {user_id} está no canal: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Acesso negado ao usuário {user_id} - não é administrador e não está no canal"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Acesso concedido ao usuário {user_id}"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Este comando está disponível apenas para administradores."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Download concluído com suporte a token PO"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Limite de flood. Tente mais tarde."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ Erro ao atualizar token REST: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Erro ao fechar sessão Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Erro ao inicializar estrutura base do banco de dados: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Nem todos os parâmetros estão definidos em config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL não está definido"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey não está definido para obter idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Erro ao baixar dump do Firebase: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Falha ao baixar dump do Firebase via REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Erro em _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Erro ao executar auto reload_cache (tentativa {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Todas as tentativas de repetição falharam"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Iniciando download do dump do Firebase em {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Dependência não disponível: requests ou Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ Banco de dados está vazio"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Erro ao fechar logger: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Erro durante limpeza: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Erro ao clonar: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Timeout ao clonar"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Exceção ao clonar: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Atualização cancelada pelo usuário"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Repositório clonado com sucesso"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Backups movidos para _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Todos os módulos foram carregados"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Limpeza concluída na saída"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Sinal {signal} recebido, encerrando graciosamente..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Por favor, aguarde..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Baixando stream HLS:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "aguardando fragmentos"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Backup {ts} não encontrado em _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Falha ao restaurar {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Restaurado: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Detalhes:</b> {error_details}\n\nDownload interrompido devido a erro crítico.\n\n💡 <b>Dica:</b> Se você estiver recebendo erro 401 Não autorizado, tente usar o comando <code>/cookie instagram</code> ou envie seus próprios cookies para autenticar com o Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domínio na lista negra de pornografia: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Palavras-chave de pornografia encontradas: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domínio na lista branca: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Palavras-chave da lista branca encontradas: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Nenhuma palavra-chave de pornografia encontrada"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Erro na API do TikTok no índice {index}, pulando para o próximo áudio..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Erro na API do TikTok no índice {index}, pulando para o próximo vídeo..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "Usuário inseriu uma <b>url</b>\n <b>nome do usuário:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>Usuário inseriu assim:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Entrar no Canal"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Registrando manipulador: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Baixar meus 5 cookies"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Obter cookie YT do navegador"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Validar seu arquivo de cookie"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Enviar cookie personalizado"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Fechar"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Formatos disponíveis para: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Fechar"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Fechar"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Fechar"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Fechar"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Ajuda fechada."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Fechado"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Erro ocorrido"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg não encontrado em PATH ou diretório do projeto. Por favor, instale FFmpeg."
    YTDLP_NOT_FOUND_MSG = "Binário yt-dlp não encontrado em PATH ou diretório do projeto. Por favor, instale yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "O vídeo será dividido em {rounds} partes, o que pode ser excessivo"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Dividindo parte do vídeo {current}/{total}: {start_time:.2f}s até {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Falha ao criar parte dividida {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Parte dividida {part} criada com sucesso: {target_name} ({size} bytes)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Erro ao dividir parte do vídeo {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Vídeo dividido em {count} partes com sucesso"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Erro no processo de divisão de vídeo: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Erro ao processar vídeo {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Arquivo de vídeo não existe: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Erro ao analisar dimensões '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Não foi possível determinar dimensões do vídeo de '{size_result}', usando padrão: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Erro ao criar miniatura: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Erro ao analisar duração do vídeo: {error}, resultado foi: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Miniatura não criada em {thumb_dir}, usando padrão"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Erro na execução do comando: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Erro ao criar miniatura com FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Pulando seção de configuração não-dict: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Definindo {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Usando cookies do usuário: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Usando cookies do YouTube para o usuário {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Arquivo de cookie global copiado para a pasta do usuário {user_id}"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Usando cookies globais copiados como cookies do usuário: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Falha ao copiar arquivo de cookie global para usuário {user_id}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Usando --no-cookies para domínio: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy solicitado mas falhou ao importar/obter config: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Forçando uso de proxy para gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy solicitado mas configuração de proxy está incompleta"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Auxiliar de proxy falhou: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Analisando itens do extrator..."
    GALLERY_DL_ITEM_COUNT_MSG = "Item {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Metadados encontrados (tag 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL encontrada (tag 3): {url}, metadados: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Metadados encontrados (legado): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL encontrada (legado): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Nome do arquivo encontrado: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Diretório encontrado: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Extensão encontrada: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "{count} itens analisados, info: {info}, fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Definindo configuração do gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Tentando Estratégia A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "módulo gallery_dl.extractor não encontrado"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() não disponível nesta compilação"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Chamando extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Nenhum extrator correspondeu à URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Definindo cookies no extrator: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Falha ao definir cookies no extrator: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Extrator encontrado, chamando items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Estratégia A bem-sucedida, obteve info: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Estratégia A: extractor.items() não retornou informações válidas"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Estratégia A (extractor.find) falhou: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Metadados de fallback de --get-urls: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Todas as estratégias falharam ao obter metadados"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Falha ao extrair informações da imagem: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "Módulo gallery_dl.job não encontrado (instalação quebrada?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob não disponível nesta compilação"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Procurando arquivos baixados no diretório gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Tentando encontrar arquivos por nomes do extrator"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Erro ao ler argumentos do usuário para {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Erro ao processar vídeo{video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Usuário {user_id} tem send_as_file habilitado, enviando como documento"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video expirou repetidamente; voltando para send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Legenda muito longa, tentando com legenda mínima"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (legenda mínima) expirou; voltando para send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Erro ao enviar vídeo com legenda mínima: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Erro ao enviar arquivo de descrição completo: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Erro ao remover arquivo de descrição temporário: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Ignorando match_filter para domínio em NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Verificando cookies do YouTube existentes na URL do usuário para detecção de formato para usuário {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Cookies do YouTube existentes funcionam na URL do usuário para detecção de formato para usuário {user_id} - usando-os"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Cookies do YouTube existentes falharam na URL do usuário, tentando obter novos para detecção de formato para usuário {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Tentando fonte de cookie do YouTube {i} para detecção de formato para usuário {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "Cookies do YouTube da fonte {i} funcionam na URL do usuário para detecção de formato para usuário {user_id} - salvos na pasta do usuário"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "Cookies do YouTube da fonte {i} não funcionam na URL do usuário para detecção de formato para usuário {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Falha ao baixar cookies do YouTube da fonte {i} para detecção de formato para usuário {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Todas as fontes de cookie do YouTube falharam para detecção de formato para usuário {user_id}, tentará sem cookies"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Nenhuma fonte de cookie do YouTube configurada para detecção de formato para usuário {user_id}, tentará sem cookies"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Nenhum cookie do YouTube encontrado para detecção de formato para usuário {user_id}, tentando obter novos"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Usando cookies do YouTube para detecção de formato para usuário {user_id} (já validados no menu Sempre Perguntar)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Nenhum cookie do YouTube encontrado para detecção de formato para usuário {user_id}, tentando restaurar..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Arquivo de cookie global copiado para pasta do usuário {user_id} para detecção de formato"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Falha ao copiar arquivo de cookie global para usuário {user_id}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Usando --no-cookies para domínio em get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "App ainda não inicializado. Não é possível acessar {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Legenda:</b> <code>{caption}</code>\n<b>ID do usuário:</b> <code>{user_id}</code>\n<b>Primeiro nome do usuário:</b> <code>{users_name}</code>\n<b>ID do arquivo de vídeo:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Erro em caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Erro inesperado em caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL do Vídeo</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL ausente na configuração"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin inicializado"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken atualizado"
    DB_LOG_FOR_USER_ADDED_MSG = "Log para usuário adicionado"
    DB_DATABASE_CREATED_MSG = "banco de dados criado"
    DB_BOT_STARTED_MSG = "Bot iniciado"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY persistido em config.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Parte da playlist já em cache: {path_parts}, pulando"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: nenhum cache encontrado para qualquer variante de URL/qualidade, retornando dict vazio"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: contagem rápida para intervalo grande: {cached_count} vídeos em cache"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: nenhum cache encontrado para hash {url_hash}, qualidade {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: nenhum cache encontrado para qualquer variante de URL, retornando None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Access denied. Admin only."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Recarregamento automático do cache Firebase atualizado!\n\n📊 Status: {status}\n⏰ Agendamento: a cada {interval} horas a partir das 00:00\n🕒 Próximo recarregamento: {next_exec} (em {delta_min} minutos)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Recarregamento automático do cache Firebase parado!\n\n📊 Status: ❌ DESABILITADO\n💡 Use /auto_cache on para reativar"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Argumento inválido. Use /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ O intervalo deve estar entre 1 e 168 horas"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Falha ao definir intervalo"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Intervalo do cache Firebase automático atualizado!\n\n📊 Status: ✅ HABILITADO\n⏰ Agendamento: a cada {interval} horas a partir das 00:00\n🕒 Próximo recarregamento: {next_exec} (em {delta_min} minutos)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Recarregamento automático do cache Firebase iniciado!\n\n📊 Status: ✅ HABILITADO\n⏰ Agendamento: a cada {interval} horas a partir das 00:00\n🕒 Próximo recarregamento: {next_exec} (em {delta_min} minutos)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Recarregamento automático do cache Firebase parado!\n\n📊 Status: ❌ DESABILITADO\n💡 Use /auto_cache on para reativar"
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
    DB_USER_BANNED_MSG = f"🚫 Você está banido do bot! Para ser desbanido, entre em contato com {Config.ADMIN_USERNAME}\n<blockquote>P.S. Não saia do canal - você será automaticamente banido ⛔️</blockquote>\n🌍Mudar idioma /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Nenhum formato de vídeo encontrado. Tentando downloader de imagens…"
    AA_FLOOD_WAIT_MSG = "⚠️ O Telegram limitou o envio de mensagens.\n⏳ Por favor, aguarde: {time_str}\nPara atualizar o temporizador, envie a URL novamente 2 vezes."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Clique no botão para copiar a URL do stream, depois cole no app VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Clique no botão para copiar a URL do stream, depois cole no app VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Erro ao obter link:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Erro ao enviar arquivo de formatos: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Falha ao obter formatos:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Analisando... (aguarde 6 seg)"
    AA_PROCESSING_MSG = "🔎 Analisando..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{wrong} contém caracteres proibidos. Apenas letras, dígitos e _ são permitidos.\nPor favor, use: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Para trabalhar em grupo, o bot precisa de direitos de administrador. Por favor, torne o bot administrador deste grupo."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Olá {first_name},\n \n<i>Este bot🤖 pode baixar qualquer vídeo diretamente no telegram.😊 Para mais informações pressione <b>/help</b></i> 👈\n\n<blockquote>P.S. Devido a possível conteúdo 🔞NSFW - download de ☁️<b>Armazenamento em nuvem</b>, 📁<b>Compartilhamento de arquivos</b>, 🔗<b>Encurtadores de URL</b> e 🔞<b>Sites adultos</b> é pago! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ NÃO 🗑<b>exclua/cancele a inscrição do canal @tg_ytdlp</b> e NÃO 🤖<b>envie spam de URL/comandos em excesso ao bot</b> - você será banido automaticamente ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Nenhum arquivo para remover."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 Todos os arquivos removidos com sucesso!\n\nArquivos removidos:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ AGUARDE ATÉ SEU DOWNLOAD ANTERIOR TERMINAR"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "Instância do app é None em check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict é None, permitindo download"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict é None, permitindo incorporação de legendas"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: verificando limites - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: chaves info_dict: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Incorporação de legendas pulada: duração {duration}s excede limite {max_duration}s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Incorporação de legendas pulada: tamanho {size_mb:.2f}MB excede limite {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Incorporação de legendas pulada: qualidade {width}x{height} (lado mínimo {min_side}p) excede limite {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "playlist"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Limite de intervalo excedido para {service}: {count} (máximo {max_count}).\n\nUse um destes comandos para baixar o máximo de arquivos disponíveis:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Limite de intervalo excedido para {service}: {count} (máximo {max_count})\nID do Usuário: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "Provedor de token PO desabilitado na configuração"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} não é um domínio do YouTube, pulando token PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "Provedor de token PO não está disponível em {base_url}, voltando para extração padrão do YouTube"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "Cache do provedor de token PO limpo, verificará disponibilidade na próxima solicitação"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Instância do app ainda não disponível"
    HELPER_USER_NAME_MSG = "Usuário"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood wait detectado, aguardando {wait_seconds} segundos"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood wait detectado mas não foi possível extrair tempo, aguardando {retry_delay} segundos"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "erro msg_seqno detectado, aguardando {retry_delay} segundos"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Configuração de proxy incompleta, usando conexão direta"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Fechar"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Fechar"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Fechar"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Arquivo de logs removido."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Arquivo de tags removido."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Arquivo de formato removido."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Arquivo de divisão removido."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Arquivo de mediainfo removido."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Configurações de legendas removidas."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Configurações do teclado removidas."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Configurações de argumentos removidas."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 Configurações NSFW removidas."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Configurações de proxy removidas."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Configurações de espera de flood removidas."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Fechar"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Comando de Download de Vídeo"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Uso: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Exemplos:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (ordem direta)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (ordem reversa)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Veja também: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Usuário {user_id} fechou comando add_bot_to_group"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Falha ao extrair ID do YouTube"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Falha ao baixar miniatura ou ela é muito grande"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Escolher idioma do áudio"
    AA_NO_SUBTITLES_DETECTED_MSG = "Nenhuma legenda detectada"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Escolher idioma das legendas"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Erro de Autenticação"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Conta Não Encontrada"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Conta Indisponível"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Limite de Taxa Excedido"
    GALLERY_DL_NETWORK_ERROR_MSG = "Erro de Rede"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Conteúdo Indisponível"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Restrições Geográficas"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Verificação Necessária"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Violação de Política"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Erro Desconhecido"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Download iniciado</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Fechar"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Comando de Download de Vídeo</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Uso: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Exemplos:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Veja também: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Limite de flood. Tente mais tarde."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Uso do Comando Cookie</b>

<code>/cookie</code> - Mostrar menu de cookies
<code>/cookie youtube</code> - Baixar cookies do YouTube
<code>/cookie instagram</code> - Baixar cookies do Instagram
<code>/cookie tiktok</code> - Baixar cookies do TikTok
<code>/cookie x</code> ou <code>/cookie twitter</code> - Baixar cookies do Twitter/X
<code>/cookie facebook</code> - Baixar cookies do Facebook
<code>/cookie custom</code> - Mostrar instruções de cookie personalizado

<i>Serviços disponíveis dependem da configuração do bot.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Arquivo de cookie removido e cache limpo."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Anterior"
    SUBS_BACK_BUTTON_MSG = "🔙Voltar"
    SUBS_OFF_BUTTON_MSG = "🚫 DESLIGADO"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs pt</code> - definir idioma"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs pt auto</code> - definir idioma com AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Opções válidas:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 IDIOMA"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 LIMPAR"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIES"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MÍDIA"
    SETTINGS_INFO_BUTTON_MSG = "📖 INFO"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ MAIS"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Apenas cookies"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Logs "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Tags"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Formato"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Dividir"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Legendas"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Teclado"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Argumentos"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Proxy"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Espera de flood"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Todos os arquivos"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Baixar meus 5 cookies"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Obter cookie YT do navegador"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Validar seu arquivo de cookie"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Enviar cookie personalizado"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Alterar qualidade e formato"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Ativar / Desativar MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Alterar tamanho da parte de vídeo dividida"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Baixar vídeo como áudio"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Configurações de idioma das legendas"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Como baixar playlists"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Baixar imagens via gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Enviar suas #tags"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Obter instruções"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Enviar seus logs"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Ajuda de playlist"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - como fazer"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Obter links diretos de vídeo"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Ativar/desativar proxy"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Layout do teclado"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Ajudante de pesquisa inline"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - Argumentos yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - Configurações de desfoque NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Opções de Limpeza</b>\n\nEscolha o que limpar:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: Ativar pesquisa @vid"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: Ativar pesquisa @vid"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 DESLIGADO"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 COMPLETO"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL das Imagens]({url})"
    IMAGE_ERROR_MSG = "❌ Erro: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Voltar"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - formato personalizado"
    FORMAT_720P_MSG = "• <code>/format 720</code> - qualidade 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - qualidade 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - qualidade 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - ID de formato específico"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - sempre mostrar menu"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/melhor qualidade"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Sempre Perguntar (menu + botões)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Outros (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (melhor para Telegram PC/Mac)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (melhor para Telegram mobile)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (qualidade MÁXIMA)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Personalizado (insira o seu próprio)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Do Navegador"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Seu Próprio"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Modo de entrada fechado automaticamente devido à inatividade (5 minutos)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Redefinir Tudo"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Ver Atual"
    ARGS_BACK_BUTTON_MSG = "🔙 Voltar"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Encaminhe esta mensagem para seus favoritos para salvar essas configurações como um modelo.</i> \n\n<i>Encaminhe esta mensagem de volta aqui para aplicar essas configurações.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Argumentos atuais do yt-dlp:\n\nNenhuma configuração personalizada configurada.\n\n---\n\n<i>Encaminhe esta mensagem para seus favoritos para salvar essas configurações como um modelo.</i> \n\n<i>Encaminhe esta mensagem de volta aqui para aplicar essas configurações.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Argumentos atuais do yt-dlp:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Exportar Configurações"
    ARGS_SETTINGS_READY_MSG = "Configurações prontas para exportação! Encaminhe esta mensagem para favoritos para salvar."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Argumentos atuais do yt-dlp:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Falha ao reconhecer configurações na mensagem. Certifique-se de enviar um modelo de configurações correto."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Configurações importadas com sucesso!\n\nParâmetros aplicados: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Configurações principais:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Erro ao salvar configurações importadas."
    ARGS_ERROR_IMPORTING_MSG = "❌ Ocorreu um erro ao importar configurações."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Baixar Arquivos de Cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Escolha um serviço para baixar o arquivo de cookie."
    COOKIE_MENU_SAVE_INFO_MSG = "Arquivos de cookie serão salvos como cookie.txt na sua pasta."
    COOKIE_MENU_TIP_HEADER_MSG = "Dica: Você também pode usar comando direto:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – baixar e validar cookies"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – usar uma fonte específica por índice (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Depois verifique com <code>/check_cookie</code> (testa em RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Sempre Perguntar"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Link"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Assistir"  # TEMPORARIAMENTE DESABILITADO: o serviço poketube está fora do ar
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Descrição"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ CORTAR"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Cortar Vídeo</b>\n\nDuração do vídeo: <b>{start_time} - {end_time}</b>\n\nPor favor, envie o intervalo de tempo desejado no formato:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nExemplo: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Formato inválido. Por favor use: <code>HH:MM:SS-HH:MM:SS</code>\n\nExemplo: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Intervalo inválido. O tempo de início deve ser menor que o tempo de término."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ O intervalo de tempo está fora dos limites do vídeo.\n\nDuração do vídeo: <b>{start_time} - {end_time}</b>\n\nSeu intervalo deve estar dentro desses limites."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>O vídeo será cortado:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Parcialmente concluído - {successful_uploads}/{total_files} arquivos de áudio enviados."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Áudio baixado e enviado com sucesso - {total_files} arquivos enviados."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Conta Privada do TikTok</b>\n\n"
        "Esta conta do TikTok é privada ou todos os vídeos são privados.\n\n"
        "<b>💡 Solução:</b>\n"
        "1. Siga a conta @{username}\n"
        "2. Envie seus cookies para o bot usando o comando <code>/cookie</code>\n"
        "3. Tente novamente\n\n"
        "<b>Após atualizar os cookies, tente novamente!</b>"
    )

    #######################################################
