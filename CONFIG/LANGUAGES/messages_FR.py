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
    CREDITS_MSG = "<blockquote><i>Géré par</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Changer la langue: /lang</b>"
    TO_USE_MSG = "<i>Pour utiliser ce bot, vous devez vous abonner à la chaîne Telegram @tg_ytdlp.</i>\nAprès avoir rejoint la chaîne, <b>renvoyez votre lien vidéo et le bot le téléchargera pour vous</b> ❤️\n\n<blockquote>P.S. Le téléchargement de contenu 🔞NSFW et de fichiers depuis ☁️Stockage Cloud est payant ! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Ne quittez pas la chaîne - vous serez banni de l'utilisation du bot ⛔️</blockquote>"

    ERROR1 = "Aucun lien URL trouvé. Veuillez entrer une URL avec <b>https://</b> ou <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Listes de lecture (yt-dlp)</b>

Pour télécharger des listes de lecture, envoyez leur URL avec des plages <code>*start*end</code> à la fin. Par exemple : <code>URL*1*5</code> (5 premières vidéos de 1 à 5 inclus).<code>URL*-1*-5</code> (5 dernières vidéos de 1 à 5 inclus).
Ou vous pouvez utiliser <code>/vid FROM-TO URL</code>. Par exemple : <code>/vid 3-7 URL</code> (télécharge les vidéos de 3 à 7 inclus depuis le début). <code>/vid -3-7 URL</code> (télécharge les vidéos de 3 à 7 inclus depuis la fin). Fonctionne aussi pour la commande <code>/audio</code>.

<b>Exemples :</b>

🟥 <b>Plage de vidéos depuis une liste de lecture YouTube :</b> (nécessite 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(télécharge les 5 premières vidéos de 1 à 5 inclus)
🟥 <b>Vidéo unique depuis une liste de lecture YouTube :</b> (nécessite 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(télécharge uniquement la 3e vidéo)

⬛️ <b>Profil TikTok :</b> (nécessite votre 🍪)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(télécharge les 10 premières vidéos du profil utilisateur)

🟪 <b>Stories Instagram :</b> (nécessite votre 🍪)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(télécharge les 3 premières stories)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(télécharge les 10 premières stories de l'album)

🟦 <b>Vidéos VK :</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(télécharge les 3 premières vidéos du profil utilisateur/groupe)

⬛️<b>Chaînes Rutube :</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(télécharge les vidéos de 2 à 4 inclus de la chaîne)

🟪 <b>Clips Twitch :</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(télécharge les 3 premiers clips de la chaîne)

🟦 <b>Groupes Vimeo :</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(télécharge les 2 premières vidéos du groupe)

🟧 <b>Modèles Pornhub :</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(télécharge les 2 premières vidéos du profil modèle)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(télécharge les 3 premières vidéos des résultats de recherche par votre prompt)

et ainsi de suite...
voir <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">liste des sites supportés</a>
</blockquote>

<blockquote expandable>🖼 <b>Images (gallery-dl)</b>

Utilisez <code>/img URL</code> pour télécharger des images/photos/albums depuis de nombreuses plateformes.

<b>Exemples :</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Plages :</b>
<code>/img 11-20 https://example.com/album</code> — éléments 11..20
<code>/img 11- https://example.com/album</code> — de 11 à la fin (ou limite du bot)

<i>Les plateformes supportées incluent vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, etc. Liste complète :</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">sites supportés par gallery-dl</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Bot de Téléchargement Vidéo - Aide</b>

📥 <b>Utilisation de Base :</b>
• Envoyez n'importe quel lien → le bot le télécharge
  <i>le bot essaie automatiquement de télécharger les vidéos via yt-dlp et les images via gallery-dl.</i>
• <b>URLs multiples :</b> En mode sélection de qualité (<code>/format</code>) vous pouvez envoyer jusqu'à <b>10 URLs</b> dans un message. Chaque URL sur une nouvelle ligne ou séparée par des espaces.
• <code>/audio URL</code> → extraire l'audio
• <code>/link [quality] URL</code> → obtenir des liens directs
• <code>/proxy</code> → activer/désactiver le proxy pour tous les téléchargements
• Répondez à la vidéo avec du texte → changer la légende

📋 <b>Listes de Lecture & Plages :</b>
• <code>URL*1*5</code> → télécharger les 5 premières vidéos
• <code>URL*-1*-5</code> → télécharger les 5 dernières vidéos
• <code>/vid 3-7 URL</code> → devient <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → devient <code>URL*-3*-7</code>

🍪 <b>Cookies & Privé :</b>
• Téléversez un cookie *.txt pour les vidéos privées
• <code>/cookie [service]</code> → télécharger les cookies (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → choisir la source par index (1–N)
• <code>/cookies_from_browser</code> → extraire du navigateur
• <code>/check_cookie</code> → vérifier le cookie
• <code>/save_as_cookie</code> → sauvegarder le texte comme cookie

🧹 <b>Nettoyage :</b>
• <code>/clean</code> → fichiers multimédias uniquement
• <code>/clean all</code> → tout
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Paramètres :</b>
• <code>/settings</code> → menu des paramètres
• <code>/format</code> → qualité & format
• <code>/split</code> → diviser la vidéo en parties
• <code>/mediainfo on/off</code> → informations multimédias
• <code>/nsfw on/off</code> → flou NSFW
• <code>/tags</code> → voir les tags sauvegardés
• <code>/sub on/off</code> → sous-titres
• <code>/keyboard</code> → clavier (OFF/1x3/2x3)

🏷️ <b>Tags :</b>
• Ajoutez <code>#tag1#tag2</code> après l'URL
• Les tags apparaissent dans les légendes
• <code>/tags</code> → voir tous les tags

🔗 <b>Liens Directs :</b>
• <code>/link URL</code> → meilleure qualité
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → qualité spécifique

⚙️ <b>Commandes Rapides :</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → définir la qualité
• <code>/keyboard off/1x3/2x3/full</code> → disposition du clavier
• <code>/split 100mb-2000mb</code> → changer la taille des parties
• <code>/subs off/ru/en auto</code> → langue des sous-titres
• <code>/list URL</code> → liste des formats disponibles
• <code>/mediainfo on/off</code> → activer/désactiver les informations multimédias
• <code>/proxy on/off</code> → activer/désactiver le proxy pour tous les téléchargements

📊 <b>Info :</b>
• <code>/usage</code> → historique des téléchargements
• <code>/search</code> → recherche inline via @vid

🖼 <b>Images :</b>
• <code>URL</code> → télécharger l'URL des images
• <code>/img URL</code> → télécharger les images depuis l'URL
• <code>/img 11-20 URL</code> → télécharger une plage spécifique
• <code>/img 11- URL</code> → télécharger du 11e à la fin

👨‍💻 <i>Développeur :</i> @upekshaip
🤝 <i>Contributeur :</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Enregistrez simplement votre cookie sous <b><u>cookie.txt</u></b> et envoyez-le au bot comme document.\n\n"
        "Vous pouvez également envoyer les cookies en texte brut avec la commande <b><u>/save_as_cookie</u></b>.\n"
        "<b>Utilisation de <b><u>/save_as_cookie</u></b> :</b>\n\n"
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
        "<b><u>Instructions :</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>Recherche vidéo</b>

Appuyez sur le bouton ci-dessous pour activer la recherche inline via @vid.

<blockquote>Sur PC, tapez simplement <b>"@vid Votre_Requête_Recherche"</b> dans n'importe quel chat.</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Commande de Téléchargement d'Images</b>\n\n"
        "Utilisation : <code>/img URL</code>\n\n"
        "<b>Exemples :</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Plateformes supportées (exemples) :</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, etc. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">liste complète</a></blockquote>"
        "Voir aussi : "
    )
    
    LINK_HINT_MSG = (
        "Obtenez des liens vidéo directs avec sélection de qualité.\n\n"
        "Utilisation : /link + URL \n\n"
        "(ex. /link https://youtu.be/abc123)\n"
        "(ex. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Ajouter le Bot au Groupe</b>

Ajoutez mes bots à vos groupes pour obtenir des fonctionnalités améliorées et des limites plus élevées !
————————————
📊 <b>Limites GRATUITES Actuelles (dans les MP du Bot) :</b>
<blockquote>•🗑 Désordre de tous les fichiers non triés 👎
• Taille max 1 fichier : <b>8 Go </b>
• Qualité max 1 fichier : <b>ILLIM</b>
• Durée max 1 fichier : <b>ILLIM</b>
• Nombre max de téléchargements : <b>ILLIM</b>
• URLs max dans un message : <b>10</b> (seulement en mode sélection de qualité)
• Éléments de liste max par fois : <b>50</b>
• Vidéos TikTok max par fois : <b>500</b>
• Images max par fois : <b>1000</b>
• Limites de débit URL : <b>5/min, 60/heure, 1000/jour</b>
• Limite de commandes : <b>20/min</b>
• Temps max 1 téléchargement : <b>2 heures</b>
• 🔞 Le contenu NSFW est payant ! 1⭐️ = $0.02
• 🆓 TOUS LES AUTRES MÉDIAS SONT TOTALEMENT GRATUITS
• 📝 Tous les logs de contenu et mise en cache vers mes canaux de logs pour repost instantané lors du re-téléchargement</blockquote>

💬<b>Ces limites uniquement pour vidéo avec sous-titres :</b>
<blockquote>• Durée max vidéo+sous-titres : <b>1.5 heures</b>
• Taille max fichier vidéo+sous-titres : <b>500 Mo</b>
• Qualité max vidéo+sous-titres : <b>720p</b></blockquote>
————————————
🚀 <b>Avantages Groupe Payant (Limites 2️⃣x) :</b>
<blockquote>•  🗂 Coffre-fort multimédia structuré et propre trié par sujets 👍
•  📁 Les bots répondent dans le sujet où vous les appelez
•  📌 Épinglage automatique du message de statut avec progression du téléchargement
•  🖼 La commande /img télécharge les médias en albums de 10 éléments
• Taille max 1 fichier : <b>16 Go</b> ⬆️
• URLs max dans un message : <b>20</b> ⬆️ (seulement en mode sélection de qualité)
• Éléments de liste max par fois : <b>100</b> ⬆️
• Vidéos TikTok max par fois : 1000 ⬆️
• Images max par fois : 2000 ⬆️
• Limites de débit URL : <b>10/min, 120/heure, 2000/jour</b> ⬆️
• Limite de commandes : <b>40/min</b> ⬆️
• Temps max 1 téléchargement : <b>4 heures</b> ⬆️
• 🔞 Contenu NSFW : Gratuit avec métadonnées complètes 🆓
• 📢 Pas besoin de s'abonner à ma chaîne pour les groupes
• 👥 Tous les membres du groupe auront accès aux fonctions payantes !
• 🗒 Pas de logs / pas de cache vers mes canaux de logs ! Vous pouvez refuser la copie/repost dans les paramètres du groupe</blockquote>

💬 <b>Limites 2️⃣x pour vidéo avec sous-titres :</b>
<blockquote>• Durée max vidéo+sous-titres : <b>3 heures</b> ⬆️
• Taille max fichier vidéo+sous-titres : <b>1000 Mo</b> ⬆️
• Qualité max vidéo+sous-titres : <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Tarifs & Configuration :</b>
<blockquote>• Prix : <b>$5/mois</b> par 1 bot dans le groupe
• Configuration : Contactez @iilililiiillliiliililliilliliiil
• Paiement : 💎TON ou autres méthodes💲
• Support : Support technique complet inclus</blockquote>
————————————
Vous pouvez ajouter mes bots à votre groupe pour débloquer gratuitement 🔞<b>NSFW</b> et doubler (x2️⃣) toutes les limites.
Contactez-moi si vous voulez que j'autorise votre groupe à utiliser mes bots @iilililiiillliiliililliilliliiil
————————————
💡<b>ASTUCE :</b> <blockquote>Vous pouvez mettre de l'argent avec n'importe quel nombre de vos amis (par exemple 100 personnes) et faire 1 achat pour tout le groupe - TOUS LES MEMBRES DU GROUPE AURONT UN ACCÈS COMPLET ET ILLIMITÉ à toutes les fonctions des bots dans ce groupe pour seulement <b>0.05$</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>Mode NSFW : ACTIVÉ✅</b>

• Le contenu NSFW sera affiché sans flou.
• Les spoilers ne s'appliqueront pas aux médias NSFW.
• Le contenu sera visible immédiatement

<i>Utilisez /nsfw off pour activer le flou</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>Mode NSFW : DÉSACTIVÉ</b>

⚠️ <b>Flou activé</b>
• Le contenu NSFW sera masqué sous spoiler   
• Pour voir, vous devrez cliquer sur le média
• Les spoilers s'appliqueront aux médias NSFW.

<i>Utilisez /nsfw on pour désactiver le flou</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Paramètre invalide</b>

Utilisez :
• <code>/nsfw on</code> - désactiver le flou
• <code>/nsfw off</code> - activer le flou
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Vérification du cache...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Traitement en cours..."
    DOWNLOADING_MSG = "📥 <b>Téléchargement des médias...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Téléchargement de l'image...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Téléchargement terminé</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Téléchargé :"
    SENT_STATUS_MSG = "Envoyé :"
    PENDING_TO_SEND_STATUS_MSG = "En attente d'envoi :"
    TITLE_LABEL_MSG = "Titre :"
    MEDIA_COUNT_LABEL_MSG = "Nombre de médias :"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Téléchargement terminé, traitement de l'audio..."
    VIDEO_PROCESSING_MSG = "📽 La vidéo est en cours de traitement..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Envoyé depuis le cache</b>\n\nAlbums envoyés : <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Vidéo envoyée avec succès depuis le cache."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Vidéos de liste de lecture envoyées depuis le cache ({cached}/{total} fichiers)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} vidéos envoyées depuis le cache, téléchargement des manquantes..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Envoyé depuis le cache : {cached}\n🔄 Poursuite du téléchargement..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Impossible d'analyser les médias, poursuite avec la plage maximale autorisée (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Impossible de déterminer le nombre de médias, poursuite avec la plage maximale autorisée (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Impossible de déterminer le nombre total de médias, poursuite avec la plage spécifiée {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>URL invalide</b>\n\nVeuillez fournir une URL valide commençant par http:// ou https://"

    ERROR_OCCURRED_MSG = "❌ <b>Erreur survenue</b>\n\n<code>{url}</code>\n\nErreur : {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Erreur lors de l'envoi de la vidéo : {error}"
    ERROR_UNKNOWN_MSG = "❌ Erreur inconnue : {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Pas assez d'espace disque pour télécharger les vidéos."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ La taille du fichier dépasse la limite de {limit} Go. Veuillez sélectionner un fichier plus petit dans la taille autorisée."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>Échec du téléchargement de la vidéo avec tous les proxies disponibles</b>\n\nToutes les tentatives de téléchargement via proxies ont échoué.\nEssayez:\n• Vérifier le fonctionnement du proxy\n• Essayer un autre proxy de la liste\n• Télécharger sans proxy (si possible)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Erreur lors de l'obtention du lien :</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram a limité l'envoi de messages.\n⏳ Veuillez attendre : {time}\nPour mettre à jour le minuteur, envoyez l'URL à nouveau 2 fois."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram a limité l'envoi de messages.\n⏳ Veuillez attendre : \nPour mettre à jour le minuteur, envoyez l'URL à nouveau 2 fois."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Échec du téléchargement des sous-titres"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Liens de Flux Directs</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Titre :</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Durée :</b> {duration} sec\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Erreur : Message original introuvable."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Le tag #{tag} contient des caractères interdits. Seules les lettres, chiffres et _ sont autorisés.\nVeuillez utiliser : {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Vidéos de liste de lecture envoyées : {sent}/{total} fichiers."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>Astuce pour les listes de lecture</b>

Vous avez envoyé un lien de liste de lecture sans spécifier de plage. Le bot a automatiquement téléchargé la première vidéo (<code>*1*1</code>).

<b>Pour télécharger plusieurs vidéos d'une liste de lecture, spécifiez une plage :</b>
• <code>URL*1*5</code> — les 5 premières vidéos (de 1 à 5 inclus)
• <code>URL*3*3</code> — uniquement la 3e vidéo
• <code>/vid 1-10 URL</code> — format alternatif

En savoir plus : <code>/playlist</code>"""
    PLAYLIST_CACHE_SENT_MSG = "✅ Envoyé depuis le cache : {cached}/{total} fichiers."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Échec de l'obtention des liens de flux"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Sélectionnez un navigateur pour télécharger les cookies :"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Aucun navigateur trouvé sur ce système. Vous pouvez télécharger les cookies depuis une URL distante ou surveiller le statut du navigateur :"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Ouvrir le Navigateur</b> - pour surveiller le statut du navigateur dans la mini-app"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Ouvrir le Navigateur"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Télécharger depuis l'URL Distante"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Fichier de cookie YouTube téléchargé via repli et enregistré sous cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Aucun navigateur supporté trouvé et aucune COOKIE_URL configurée. Utilisez /cookie ou téléversez cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ La COOKIE_URL de repli doit pointer vers un fichier .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Le fichier de cookie de repli est trop volumineux (>100 Ko)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Source de cookie de repli indisponible (statut {status}). Essayez /cookie ou téléversez cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Erreur lors du téléchargement du cookie de repli. Essayez /cookie ou téléversez cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Erreur inattendue lors du téléchargement du cookie de repli."
    BTN_CLOSE = "🔚Fermer"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Valeur booléenne invalide"
    ARGS_CLOSED_MSG = "Fermé"
    ARGS_ALL_RESET_MSG = "✅ Tous les arguments réinitialisés"
    ARGS_RESET_ERROR_MSG = "❌ Erreur lors de la réinitialisation des arguments"
    ARGS_INVALID_PARAM_MSG = "❌ Paramètre invalide"
    ARGS_BOOL_SET_MSG = "Défini sur {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "Déjà défini sur {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Valeur de sélection invalide"
    ARGS_VALUE_SET_MSG = "Défini sur {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "Déjà défini sur {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Valeur actuelle :</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Exemples :</b>\n• <code>default</code> - Utiliser la stratégie XFF par défaut\n• <code>never</code> - Ne jamais utiliser l'en-tête XFF\n• <code>US</code> - Code pays États-Unis\n• <code>GB</code> - Code pays Royaume-Uni\n• <code>DE</code> - Code pays Allemagne\n• <code>FR</code> - Code pays France\n• <code>JP</code> - Code pays Japon\n• <code>192.168.1.0/24</code> - Bloc IP (CIDR)\n• <code>10.0.0.0/8</code> - Plage IP privée\n• <code>203.0.113.0/24</code> - Bloc IP public\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Note :</b> Cela remplace les options --geo-bypass. Utilisez n'importe quel code pays à 2 lettres ou bloc IP en notation CIDR.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Exemple :</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Veuillez envoyer votre nouvelle valeur."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Plage :</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Veuillez envoyer un nombre."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Exemples :</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Note :</b> Ces en-têtes seront ajoutés aux en-têtes Referer et User-Agent existants.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Arguments yt-dlp Actuels :</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Booléen</b> - Interrupteurs True/False\n• 📋 <b>Sélection</b> - Choisir parmi les options\n• 🔢 <b>Numérique</b> - Saisie de nombre\n• 📝🔧 <b>Texte</b> - Saisie Texte/JSON</blockquote>\n\nCes paramètres seront appliqués à tous vos téléchargements."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "Forcer les connexions IPv6",
        "force_ipv4": "Forcer les connexions IPv4", 
        "no_live_from_start": "Ne pas télécharger les flux en direct depuis le début",
        "live_from_start": "Télécharger les flux en direct depuis le début",
        "no_check_certificates": "Supprimer la validation du certificat HTTPS",
        "check_certificate": "Vérifier le certificat SSL",
        "no_playlist": "Télécharger uniquement une vidéo, pas la liste de lecture",
        "embed_metadata": "Intégrer les métadonnées dans le fichier vidéo",
        "embed_thumbnail": "Intégrer la miniature dans le fichier vidéo",
        "write_thumbnail": "Écrire la miniature dans un fichier",
        "ignore_errors": "Ignorer les erreurs de téléchargement et continuer",
        "legacy_server_connect": "Autoriser les connexions serveur héritées",
        "concurrent_fragments": "Nombre de fragments simultanés à télécharger",
        "xff": "Stratégie d'en-tête X-Forwarded-For",
        "user_agent": "En-tête User-Agent",
        "impersonate": "Usurpation de navigateur",
        "referer": "En-tête Referer",
        "geo_bypass": "Contourner les restrictions géographiques",
        "hls_use_mpegts": "Utiliser MPEG-TS pour HLS",
        "no_part": "Ne pas utiliser les fichiers .part",
        "no_continue": "Ne pas reprendre les téléchargements partiels",
        "audio_format": "Format audio",
        "video_format": "Format vidéo",
        "merge_output_format": "Format de sortie de fusion",
        "send_as_file": "Envoyer comme fichier",
        "username": "Nom d'utilisateur",
        "password": "Mot de passe",
        "twofactor": "Code d'authentification à deux facteurs",
        "min_filesize": "Taille minimale de fichier (Mo)",
        "max_filesize": "Taille maximale de fichier (Mo)",
        "playlist_items": "Éléments de liste de lecture",
        "date": "Date",
        "datebefore": "Date avant",
        "dateafter": "Date après",
        "http_headers": "En-têtes HTTP",
        "sleep_interval": "Intervalle de veille",
        "max_sleep_interval": "Intervalle de veille maximum",
        "retries": "Nombre de tentatives",
        "http_chunk_size": "Taille de fragment HTTP",
        "sleep_subtitles": "Veille pour les sous-titres"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ Configuration des Arguments yt-dlp</b>\n\n<blockquote>📋 <b>Groupes :</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ Configuration des Arguments yt-dlp</b>\n\n"
        "<blockquote>📋 <b>Groupes :</b>\n"
        "• ✅/❌ <b>Booléen</b> - Interrupteurs True/False\n"
        "• 📋 <b>Sélection</b> - Choisir parmi les options\n"
        "• 🔢 <b>Numérique</b> - Saisie de nombre\n"
        "• 📝🔧 <b>Texte</b> - Saisie Texte/JSON</blockquote>\n\n"
        "Ces paramètres seront appliqués à tous vos téléchargements."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Veuillez patienter..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Erreur survenue"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Mode de saisie fermé automatiquement en raison de l'inactivité (5 minutes)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ La saisie contient du contenu potentiellement dangereux : {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Saisie trop longue (max 1000 caractères)"
    ARGS_INVALID_URL_MSG = "❌ Format d'URL invalide. Doit commencer par http:// ou https://"
    ARGS_INVALID_JSON_MSG = "❌ Format JSON invalide"
    ARGS_NUMBER_RANGE_MSG = "❌ Le nombre doit être entre {min_val} et {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Format de nombre invalide"
    ARGS_DATE_FORMAT_MSG = "❌ La date doit être au format YYYYMMDD (ex. : 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ L'année doit être entre 1900 et 2100"
    ARGS_MONTH_RANGE_MSG = "❌ Le mois doit être entre 01 et 12"
    ARGS_DAY_RANGE_MSG = "❌ Le jour doit être entre 01 et 31"
    ARGS_INVALID_DATE_MSG = "❌ Format de date invalide"
    ARGS_INVALID_XFF_MSG = "❌ XFF doit être 'default', 'never', code pays (ex. : US), ou bloc IP (ex. : 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "Aucun argument personnalisé défini. Tous les paramètres utilisent les valeurs par défaut."
    ARGS_RESET_SUCCESS_MSG = "✅ Tous les arguments réinitialisés aux valeurs par défaut."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Texte trop long. Maximum 500 caractères."
    ARGS_ERROR_PROCESSING_MSG = "❌ Erreur lors du traitement de la saisie. Veuillez réessayer."
    ARGS_BOOL_INPUT_MSG = "❌ Veuillez entrer 'True' ou 'False' pour l'option Envoyer Comme Fichier."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Veuillez fournir un nombre valide."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Veuillez envoyer <code>True</code> ou <code>False</code> pour activer/désactiver cette option."
    ARGS_JSON_VALUE_REQUEST_MSG = "Veuillez envoyer un JSON valide."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Vous n'avez pas encore de tags."
    TAGS_MESSAGE_CLOSED_MSG = "Message de tags fermé."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Sous-titres désactivés et mode Toujours Demander désactivé."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SOUS-TITRES Toujours Demander activé."
    SUBS_LANGUAGE_SET_MSG = "✅ Langue des sous-titres définie sur : {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️AVERTISSEMENT : en raison de l'impact élevé sur le CPU, cette fonction est très lente (quasi temps réel) et limitée à :\n"
        "- qualité max 720p\n"
        "- durée max 1.5 heures\n"
        "- taille max vidéo 500mo</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Commandes rapides :</b>\n"
        "• <code>/subs off</code> - désactiver les sous-titres\n"
        "• <code>/subs on</code> - activer le mode Toujours Demander\n"
        "• <code>/subs ru</code> - définir la langue\n"
        "• <code>/subs ru auto</code> - définir la langue avec AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Les sous-titres sont désactivés"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Langue sélectionnée : {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Téléchargement des sous-titres..."
    SUBS_DISABLED_ERROR_MSG = "❌ Les sous-titres sont désactivés. Utilisez /subs pour configurer."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Le téléchargement de sous-titres n'est pris en charge que pour YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Sous-titres</b>\n\n"
        "<b>Vidéo :</b> {title}\n"
        "<b>Langue :</b> {lang}\n"
        "<b>Type :</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Fichier SRT de sous-titres envoyé à l'utilisateur."
    SUBS_ERROR_PROCESSING_MSG = "❌ Erreur lors du traitement du fichier de sous-titres."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Échec du téléchargement des sous-titres."
    SUBS_ERROR_MSG = "❌ Erreur lors du téléchargement des sous-titres : {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Taille de partie divisée définie sur : {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **Taille invalide !**\n\n"
        "**Plage valide :** 100 Mo à 2 Go\n\n"
        "**Formats valides :**\n"
        "• `100mb` à `2000mb` (mégaoctets)\n"
        "• `0.1gb` à `2gb` (gigaoctets)\n\n"
        "**Exemples :**\n"
        "• `/split 100mb` - 100 mégaoctets\n"
        "• `/split 500mb` - 500 mégaoctets\n"
        "• `/split 1.5gb` - 1.5 gigaoctets\n"
        "• `/split 2gb` - 2 gigaoctets\n"
        "• `/split 2000mb` - 2000 mégaoctets (2 Go)\n\n"
        "**Préréglages :**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Choisissez la taille max de partie pour la division vidéo :**\n\n"
        "**Plage :** 100 Mo à 2 Go\n\n"
        "**Commandes rapides :**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Exemples :** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Menu fermé."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Paramètres du Bot</b>\n\nChoisissez une catégorie :"
    SETTINGS_MENU_CLOSED_MSG = "Menu fermé."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Options de Nettoyage</b>\n\nChoisissez ce qu'il faut nettoyer :"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nChoisissez une action :"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MÉDIAS</b>\n\nChoisissez une action :"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nChoisissez une action :"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ PLUS DE COMMANDES</b>\n\nChoisissez une action :"
    SETTINGS_COMMAND_EXECUTED_MSG = "Commande exécutée."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Limite de flood. Réessayez plus tard."
    SETTINGS_HINT_SENT_MSG = "Indice envoyé."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Assistant de recherche ouvert."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Commande inconnue."
    SETTINGS_HINT_CLOSED_MSG = "Indice fermé."
    SETTINGS_HELP_SENT_MSG = "Envoyer le texte d'aide à l'utilisateur"
    SETTINGS_MENU_OPENED_MSG = "Menu /settings ouvert"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Assistant de recherche fermé"
    SEARCH_CLOSED_MSG = "Fermé"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proxy {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Erreur lors de l'enregistrement des paramètres de proxy."
    PROXY_MENU_TEXT_MSG = "Activer ou désactiver l'utilisation du serveur proxy pour toutes les opérations yt-dlp ?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Activer ou désactiver l'utilisation de serveurs proxy ({config_count} + {file_count} disponibles) pour toutes les opérations yt-dlp ?\n\nLorsqu'il est activé TOUT (AUTO), les proxys seront sélectionnés en utilisant une méthode aléatoire."
    PROXY_MENU_CLOSED_MSG = "Menu fermé."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy activé. Toutes les opérations yt-dlp utiliseront le proxy."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy activé. Toutes les opérations yt-dlp utiliseront {count} serveurs proxy avec la méthode de sélection {method}."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Proxy activé (mode ALL AUTO).\n\n📊 Le robot essaiera les proxys dans cet ordre :\n1️⃣ {config_count} proxys de Config.py\n2️⃣ {file_count} proxys du fichier TXT/proxy.txt\n\n🔄 Tous les proxys seront essayés séquentiellement jusqu'à ce que la connexion soit réussie."
    PROXY_DISABLED_MSG = "❌ Proxy désactivé."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Erreur lors de l'enregistrement des paramètres de proxy."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy activé."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy désactivé."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ ATTENDEZ QUE VOTRE TÉLÉCHARGEMENT PRÉCÉDENT SOIT TERMINÉ"
    AUDIO_HELP_MSG = (
        "<b>🎧 Commande de Téléchargement Audio</b>\n\n"
        "Utilisation : <code>/audio URL</code>\n\n"
        "<b>Exemples :</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Voir aussi : /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Indice audio fermé."
    PLAYLIST_HELP_CLOSED_MSG = "Aide de liste de lecture fermée."
    USERLOGS_CLOSED_MSG = "Message de logs fermé."
    HELP_CLOSED_MSG = "Aide fermée."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>Paramètres de Flou NSFW</b>\n\nLe contenu NSFW est <b>{status}</b>.\n\nChoisissez s'il faut flouter le contenu NSFW :"
    NSFW_MENU_CLOSED_MSG = "Menu fermé."
    NSFW_BLUR_DISABLED_MSG = "Flou NSFW désactivé."
    NSFW_BLUR_ENABLED_MSG = "Flou NSFW activé."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Flou NSFW désactivé."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Flou NSFW activé."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Activer ou désactiver l'envoi de MediaInfo pour les fichiers téléchargés ?"
    MEDIAINFO_MENU_CLOSED_MSG = "Menu fermé."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo activé. Après le téléchargement, les informations du fichier seront envoyées."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo désactivé."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo activé."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo désactivé."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Lister les Formats Disponibles</b>\n\n"
        "Obtenez les formats vidéo/audio disponibles pour une URL.\n\n"
        "<b>Utilisation :</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Exemples :</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Comment utiliser les IDs de format :</b>\n"
        "Après avoir obtenu la liste, utilisez un ID de format spécifique :\n"
        "• <code>/format id 401</code> - télécharger le format 401\n"
        "• <code>/format id401</code> - identique à ci-dessus\n"
        "• <code>/format id140 audio</code> - télécharger le format 140 comme audio MP3\n\n"
        "Cette commande affichera tous les formats disponibles qui peuvent être téléchargés."
    )
    LIST_PROCESSING_MSG = "🔄 Obtention des formats disponibles..."
    LIST_INVALID_URL_MSG = "❌ Veuillez fournir une URL valide commençant par http:// ou https://"
    LIST_CAPTION_MSG = (
        "📃 Formats disponibles pour :\n<code>{url}</code>\n\n"
        "💡 <b>Comment définir le format :</b>\n"
        "• <code>/format id 134</code> - Télécharger un ID de format spécifique\n"
        "• <code>/format 720p</code> - Télécharger par qualité\n"
        "• <code>/format best</code> - Télécharger la meilleure qualité\n"
        "• <code>/format ask</code> - Toujours demander la qualité\n\n"
        "{audio_note}\n"
        "📋 Utilisez l'ID de format de la liste ci-dessus"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Formats audio uniquement :</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Télécharger le format 140 comme audio MP3\n"
        "• <code>/format id140 audio</code> - identique à ci-dessus\n"
        "Ceux-ci seront téléchargés comme fichiers audio MP3.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Erreur lors de l'envoi du fichier de formats : {error}"
    LIST_ERROR_GETTING_MSG = "❌ Échec de l'obtention des formats :\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Une erreur s'est produite lors du traitement de la commande"
    LIST_ERROR_CALLBACK_MSG = "Erreur survenue"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Comment utiliser les IDs de format :\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Après avoir obtenu la liste, utilisez un ID de format spécifique :\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - télécharger le format 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - identique à ci-dessus\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - télécharger le format 140 comme audio MP3\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - identique à ci-dessus\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Formats audio uniquement détectés : {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Ces formats seront téléchargés comme fichiers audio MP3.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Formats vidéo uniquement :</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Utilisez l'ID de format de la liste ci-dessus"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Utilisation :</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>Exemples :</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - meilleure qualité\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p ou inférieur\n"
        "• /link 720p https://youtube.com/watch?v=... - identique à ci-dessus\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K ou inférieur\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K ou inférieur"
        "</blockquote>\n\n"
        "<b>Qualité :</b> de 1 à 10000 (ex. : 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Veuillez fournir une URL valide"
    LINK_PROCESSING_MSG = "🔗 Obtention du lien direct..."
    LINK_DURATION_MSG = "⏱ <b>Durée :</b> {duration} sec\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Flux vidéo :</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Flux audio :</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Paramètre de clavier mis à jour !**\n\nNouveau paramètre : **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Argument invalide !**\n\n"
        "Options valides : `off`, `1x3`, `2x3`, `full`\n\n"
        "Exemple : `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Paramètres du Clavier**\n\n"
        "Actuel : **{current}**\n\n"
        "Choisissez une option :\n\n"
        "Ou utilisez : `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 clavier activé !"
    KEYBOARD_HIDDEN_MSG = "⌨️ Clavier masqué"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 Clavier 1x3 activé !"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 Clavier 2x3 activé !"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Clavier emoji activé !"
    KEYBOARD_ERROR_APPLYING_MSG = "Erreur lors de l'application du paramètre de clavier {setting} : {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Format défini sur : Toujours Demander. Vous serez invité à choisir la qualité à chaque fois que vous enverrez une URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format défini sur : Toujours Demander. Maintenant vous serez invité à choisir la qualité à chaque fois que vous enverrez une URL."
    FORMAT_BEST_UPDATED_MSG = "✅ Format mis à jour vers la meilleure qualité (priorité AVC+MP4) :\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Format mis à jour vers l'ID {id} :\n{format}\n\n💡 <b>Note :</b> Si c'est un format audio uniquement, il sera téléchargé comme fichier audio MP3."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Format mis à jour vers l'ID {id} (audio uniquement) :\n{format}\n\n💡 Ceci sera téléchargé comme fichier audio MP3."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Format mis à jour vers la qualité {quality} :\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Format mis à jour vers :\n{format}"
    FORMAT_MENU_MSG = (
        "Sélectionnez une option de format ou envoyez-en une personnalisée en utilisant :\n"
        "• <code>/format &lt;format_string&gt;</code> - format personnalisé\n"
        "• <code>/format 720</code> - qualité 720p\n"
        "• <code>/format 4k</code> - qualité 4K\n"
        "• <code>/format 8k</code> - qualité 8K\n"
        "• <code>/format id 401</code> - ID de format spécifique\n"
        "• <code>/format ask</code> - toujours afficher le menu\n"
        "• <code>/format best</code> - bv+ba/meilleure qualité"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Pour utiliser un format personnalisé, envoyez la commande sous la forme suivante :\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Remplacez <code>bestvideo+bestaudio/best</code> par votre chaîne de format souhaitée."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Sélectionnez votre résolution et codec souhaités :"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Format défini sur : Toujours Demander. Maintenant vous serez invité à choisir la qualité à chaque fois que vous enverrez une URL."
    FORMAT_UPDATED_MSG = "✅ Format mis à jour vers :\n{format}"
    FORMAT_SAVED_MSG = "✅ Format sauvegardé."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Choix de format mis à jour."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Menu de format personnalisé fermé"
    FORMAT_CODEC_SET_MSG = "✅ Codec défini sur {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Choix de navigateur mis à jour."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Accès refusé. Administrateurs uniquement."
    ACCESS_DENIED_ADMIN = "❌ Accès refusé. Administrateurs uniquement."
    WELCOME_MASTER = "Bienvenue Maître 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Désolé... Une erreur s'est produite lors du téléchargement."
    SIZE_LIMIT_EXCEEDED = "❌ La taille du fichier dépasse la limite de {max_size_gb} Go. Veuillez sélectionner un fichier plus petit dans la taille autorisée."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Script introuvable : {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Téléchargement du dump Firebase frais en utilisant {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Cache Firebase rechargé avec succès !"
    ADMIN_CACHE_FAILED_MSG = "❌ Échec du rechargement du cache Firebase. Vérifiez si {cache_file} existe."
    ADMIN_ERROR_RELOADING_MSG = "❌ Erreur lors du rechargement du cache : {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Erreur lors de l'exécution de {script_path} :\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Message promo envoyé à tous les autres utilisateurs</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Impossible d'envoyer le message promo. Essayez de répondre à un message\nOu une erreur s'est produite</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ L'utilisateur n'a pas encore téléchargé de contenu...</b> N'existe pas dans les logs"
    ADMIN_INVALID_COMMAND_MSG = "❌ Commande invalide"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ Aucune donnée trouvée dans le cache pour <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ La file d'attente est vide — personne n'a quitté le canal pour l'instant."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>File d'attente de bannissement</b>\nTotal en attente : {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (quitté : {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… et {extra} utilisateurs de plus."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Utilisez /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Utilisateurs bloqués de la file d'attente : {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Auto-bannissement activé : les nouveaux partants seront bannis immédiatement."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Auto-bannissement désactivé."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Fenêtre d'auto-bannissement programmée définie sur chaque {interval}."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Journal d'activité du canal pour les {hours} dernières heures (2 jours)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 {hours} dernières heures (2 jours) : {joined} rejoints, {left} quittés."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Aucune activité pour les {hours} dernières heures (2 jours)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Total : 🟢 {joined} rejoints, 🔴 {left} quittés."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Aucun accès au journal d'activité du canal. Les bots ne peuvent pas lire les logs d'administrateur. Fournissez CHANNEL_GUARD_SESSION_STRING dans config avec une session utilisateur pour activer cette fonctionnalité."
    BAN_TIME_USAGE_MSG = "❌ Utilisation : {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Utilisez des formats comme 10s, 6m, 5h, 4d, 3w, 2M ou 1y."
    BAN_TIME_SET_MSG = "🕒 Intervalle de scan du journal du canal défini sur {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Rapport de scan du canal\n"
        "Exécuté à : {run_ts}\n"
        "Intervalle : {interval}\n"
        "Nouveaux partants : {new_leavers}\n"
        "Bannissements auto : {auto_banned}\n"
        "En attente : {pending}\n"
        "Dernier event_id : {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Utilisation : /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Un administrateur ne peut pas supprimer un administrateur"
    ADMIN_USER_BLOCKED_MSG = "Utilisateur bloqué 🔒❌\n \nID : <code>{user_id}</code>\nDate de blocage : {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> est déjà bloqué ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Désolé ! Vous n'êtes pas un administrateur"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Utilisation : /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Utilisateur débloqué 🔓✅\n \nID : <code>{user_id}</code>\nDate de déblocage : {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> est déjà débloqué ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Utilisateurs débloqués : {count}\n⏱ Horodatage : {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Utilisation : /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Utilisateur ignoré 👁️❌\n \nID : <code>{user_id}</code>\nDate d'ignoré : {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> est déjà ignoré ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Utilisation : /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Utilisateur n'est plus ignoré 👁️✅\n \nID : <code>{user_id}</code>\nDate de ne plus ignorer : {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> n'est pas ignoré ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Temps d'exécution du bot -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Veuillez fournir une URL pour effacer le cache.\nUtilisation : <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Veuillez fournir une URL valide.\nUtilisation : <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Cache effacé avec succès pour l'URL :\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Aucun cache trouvé pour ce lien."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Erreur lors de l'effacement du cache : {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Accès refusé. Administrateurs uniquement."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Exécution du script de mise à jour de la liste pornographique : {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Script terminé avec succès !"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Script terminé avec succès !\n\nSortie :\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Script échoué avec le code de retour {returncode} :\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Erreur lors de l'exécution du script : {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Rechargement des caches pornographiques et liés aux domaines..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Caches pornographiques rechargés avec succès !\n\n"
        "📊 État actuel du cache :\n"
        "• Domaines pornographiques : {porn_domains}\n"
        "• Mots-clés pornographiques : {porn_keywords}\n"
        "• Sites supportés : {supported_sites}\n"
        "• LISTE BLANCHE : {whitelist}\n"
        "• LISTE GRISE : {greylist}\n"
        "• LISTE NOIRE : {black_list}\n"
        "• MOTS-CLÉS BLANCS : {white_keywords}\n"
        "• DOMAINES PROXY : {proxy_domains}\n"
        "• DOMAINES PROXY_2 : {proxy_2_domains}\n"
        "• REQUÊTE PROPRE : {clean_query}\n"
        "• DOMAINES SANS COOKIE : {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Erreur lors du rechargement du cache pornographique : {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Veuillez fournir une URL à vérifier.\nUtilisation : <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Veuillez fournir une URL valide.\nUtilisation : <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Vérification de l'URL pour le contenu NSFW...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Résultat de Vérification Pornographique</b>\n\n"
        "<b>URL :</b> <code>{url}</code>\n"
        "<b>Statut :</b> <b>{status_text}</b>\n\n"
        "<b>Explication :</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Erreur lors de la vérification de l'URL : {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Cookies nettoyés."
    CLEAN_LOGS_CLEANED_MSG = "logs nettoyés."
    CLEAN_TAGS_CLEANED_MSG = "tags nettoyés."
    CLEAN_FORMAT_CLEANED_MSG = "format nettoyé."
    CLEAN_SPLIT_CLEANED_MSG = "split nettoyé."
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfo nettoyé."
    CLEAN_SUBS_CLEANED_MSG = "Paramètres de sous-titres nettoyés."
    CLEAN_KEYBOARD_CLEANED_MSG = "Paramètres de clavier nettoyés."
    CLEAN_ARGS_CLEANED_MSG = "Paramètres d'arguments nettoyés."
    CLEAN_NSFW_CLEANED_MSG = "Paramètres NSFW nettoyés."
    CLEAN_PROXY_CLEANED_MSG = "Paramètres de proxy nettoyés."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Paramètres d'attente de flood nettoyés."
    CLEAN_ALL_CLEANED_MSG = "Tous les fichiers nettoyés."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nChoisissez une action :"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Fichier de cookie sauvegardé"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Validation ignorée pour les cookies non-YouTube"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Le fichier de cookie existe mais a un format incorrect"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Le fichier de cookie est introuvable."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Démarrage du test des cookies YouTube...\n\nVeuillez patienter pendant que je vérifie et valide vos cookies."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Vos cookies YouTube existants fonctionnent correctement !\n\nPas besoin de télécharger de nouveaux."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Vos cookies YouTube existants sont expirés ou invalides.\n\n🔄 Téléchargement de nouveaux cookies..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ La source de cookies {service} n'est pas configurée !"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ La source de cookies {service} doit être un fichier .txt !"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Limite de plage dépassée : {range_count} fichiers demandés (maximum {max_img_files}).\n\nUtilisez l'une de ces commandes pour télécharger le maximum de fichiers disponibles :\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Fermer"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Limite de médias dépassée : {count} fichiers demandés (maximum {max_count}).\n\nUtilisez l'une de ces commandes pour télécharger le maximum de fichiers disponibles :\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 <b>{count}</b> éléments multimédias trouvés depuis le lien"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Sélectionnez la plage de téléchargement :"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Usurpation de navigateur"
    ARGS_REFERER_DESC_MSG = "En-tête Referer"
    ARGS_USER_AGENT_DESC_MSG = "En-tête User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "Contourner les restrictions géographiques"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Vérifier le certificat SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "Télécharger les flux en direct depuis le début"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Ne pas télécharger les flux en direct depuis le début"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Utiliser le conteneur MPEG-TS pour les vidéos HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "Télécharger uniquement une vidéo, pas la liste de lecture"
    ARGS_NO_PART_DESC_MSG = "Ne pas utiliser les fichiers .part"
    ARGS_NO_CONTINUE_DESC_MSG = "Ne pas reprendre les téléchargements partiels"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Format audio pour extraction"
    ARGS_EMBED_METADATA_DESC_MSG = "Intégrer les métadonnées dans le fichier vidéo"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Intégrer la miniature dans le fichier vidéo"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Écrire la miniature dans un fichier"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Nombre de fragments simultanés à télécharger"
    ARGS_FORCE_IPV4_DESC_MSG = "Forcer les connexions IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "Forcer les connexions IPv6"
    ARGS_XFF_DESC_MSG = "Stratégie d'en-tête X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "Taille de fragment HTTP (octets)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Veille avant téléchargement de sous-titres (secondes)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Autoriser les connexions serveur héritées"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Supprimer la validation du certificat HTTPS"
    ARGS_USERNAME_DESC_MSG = "Nom d'utilisateur du compte"
    ARGS_PASSWORD_DESC_MSG = "Mot de passe du compte"
    ARGS_TWOFACTOR_DESC_MSG = "Code d'authentification à deux facteurs"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Ignorer les erreurs de téléchargement et continuer"
    ARGS_MIN_FILESIZE_DESC_MSG = "Taille minimale de fichier (Mo)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Taille maximale de fichier (Mo)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Éléments de liste de lecture à télécharger (ex. : 1,3,5 ou 1-5)"
    ARGS_DATE_DESC_MSG = "Télécharger les vidéos téléversées à cette date (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Télécharger les vidéos téléversées avant cette date (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Télécharger les vidéos téléversées après cette date (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "En-têtes HTTP personnalisés (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Intervalle de veille entre les requêtes (secondes)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Intervalle de veille maximum (secondes)"
    ARGS_RETRIES_DESC_MSG = "Nombre de tentatives"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Format de conteneur vidéo"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Format de conteneur de sortie pour fusion"
    ARGS_SEND_AS_FILE_DESC_MSG = "Envoyer tous les médias comme document au lieu de médias"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Usurper"
    ARGS_REFERER_SHORT_MSG = "Referer"
    ARGS_GEO_BYPASS_SHORT_MSG = "Contourner Geo"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Vérifier Cert"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Début en Direct"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Pas de Début en Direct"
    ARGS_USER_AGENT_SHORT_MSG = "Agent Utilisateur"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Pas de Liste"
    ARGS_NO_PART_SHORT_MSG = "Pas de Partie"
    ARGS_NO_CONTINUE_SHORT_MSG = "Pas de Continuer"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Format Audio"
    ARGS_EMBED_METADATA_SHORT_MSG = "Intégrer Meta"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Intégrer Mini"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Écrire Mini"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Simultané"
    ARGS_FORCE_IPV4_SHORT_MSG = "Forcer IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Forcer IPv6"
    ARGS_XFF_SHORT_MSG = "En-tête XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Taille Fragment"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Veille Subs"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Connexion Héritée"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Pas de Vérif Cert"
    ARGS_USERNAME_SHORT_MSG = "Nom d'utilisateur"
    ARGS_PASSWORD_SHORT_MSG = "Mot de passe"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Ignorer Erreurs"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Taille Min"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Taille Max"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Éléments Liste"
    ARGS_DATE_SHORT_MSG = "Date"
    ARGS_DATEBEFORE_SHORT_MSG = "Date Avant"
    ARGS_DATEAFTER_SHORT_MSG = "Date Après"
    ARGS_HTTP_HEADERS_SHORT_MSG = "En-têtes HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Intervalle Veille"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Veille Max"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Format Vidéo"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Format Fusion"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Envoyer Fichier"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ Le fichier est trop volumineux. La taille maximale est de 100 Ko."
    COOKIES_INVALID_FORMAT_MSG = "❌ Seuls les fichiers au format .txt sont autorisés."
    COOKIES_INVALID_COOKIE_MSG = "❌ Le fichier ne ressemble pas à cookie.txt (il n'y a pas de ligne '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ Erreur lors de la lecture du fichier : {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Le fichier de cookie existe et a un format correct"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ Le fichier de cookie {service} est trop volumineux ! Max 100 Ko, obtenu {size} Ko."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ Fichier de cookie {service} téléchargé et sauvegardé sous cookie.txt dans votre dossier.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ La source de cookies {service} est indisponible (statut {status}). Veuillez réessayer plus tard."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Erreur lors du téléchargement du fichier de cookie {service}. Veuillez réessayer plus tard."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ L'utilisateur a fourni un nouveau fichier de cookie.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie mis à jour avec succès :</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Ce n'est pas un cookie valide.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ Les sources de cookies YouTube ne sont pas configurées !"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Téléchargement et vérification des cookies YouTube...\n\nTentative {attempt} sur {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Accès refusé. Administrateurs uniquement."
    ADMIN_USER_LOGS_TOTAL_MSG = "Total : <b>{total}</b>\n<b>{user_id}</b> - logs (10 derniers) :\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 clavier activé !"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Langue des sous-titres définie sur : {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Langue des sous-titres définie sur : {flag} {name} avec AUTO/TRANS activé."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Menu de langue des sous-titres fermé."
    SUBS_DOWNLOADING_MSG = "💬 Téléchargement des sous-titres..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Rechargement du cache Firebase en mémoire..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Aucune COOKIE_URL configurée. Utilisez /cookie ou téléversez cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Téléchargement des cookies depuis l'URL distante..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ La COOKIE_URL de repli doit pointer vers un fichier .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Le fichier de cookie de repli est trop volumineux (>100 Ko)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Fichier de cookie YouTube téléchargé via repli et enregistré sous cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Source de cookie de repli indisponible (statut {status}). Essayez /cookie ou téléversez cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Erreur lors du téléchargement du cookie de repli. Essayez /cookie ou téléversez cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Erreur inattendue lors du téléchargement du cookie de repli."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ Le navigateur {browser} n'est pas installé."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookies sauvegardés en utilisant le navigateur : {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Échec de la sauvegarde des cookies : {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ Les cookies YouTube fonctionnent correctement"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ Les cookies YouTube sont expirés ou invalides\n\nUtilisez /cookie pour obtenir de nouveaux cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - format personnalisé\n• <code>/format 720</code> - qualité 720p\n• <code>/format 4k</code> - qualité 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Indice envoyé."
    FORMAT_MKV_TOGGLE_MSG = "MKV est maintenant {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Aucune URL distante configurée"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Format de fichier invalide"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Fichier trop volumineux"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookies téléchargés avec succès"
    COOKIES_SERVER_ERROR_MSG = "❌ Erreur serveur {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Échec du téléchargement"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Erreur inattendue"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Navigateur non installé."
    COOKIES_MENU_CLOSED_MSG = "Menu fermé."
    COOKIES_HINT_CLOSED_MSG = "Indice de cookie fermé."
    IMG_HELP_CLOSED_MSG = "Aide fermée."
    SUBS_LANGUAGE_UPDATED_MSG = "Paramètres de langue des sous-titres mis à jour."
    SUBS_MENU_CLOSED_MSG = "Menu de langue des sous-titres fermé."
    KEYBOARD_SET_TO_MSG = "Clavier défini sur {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Erreur lors du traitement du paramètre"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo activé."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo désactivé."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Flou NSFW désactivé."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Flou NSFW activé."
    SETTINGS_MENU_CLOSED_MSG = "Menu fermé."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Attente de flood active. Réessayez plus tard."
    OTHER_HELP_CLOSED_MSG = "Aide fermée."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Message de logs fermé."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menu fermé."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Taille invalide."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Erreur lors de l'envoi de MediaInfo : {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Une erreur s'est produite : {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - tous les logs"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - tous {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Télécharger depuis l'URL Distante"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Ouvrir le Navigateur"
    SELECT_BROWSER_MSG = "Sélectionnez un navigateur pour télécharger les cookies :"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Aucun navigateur trouvé sur ce système. Vous pouvez télécharger les cookies depuis une URL distante ou surveiller le statut du navigateur :"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Ouvrir le Navigateur</b> - pour surveiller le statut du navigateur dans la mini-app"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Échec de l'exécution de /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Limite de flood. Réessayez plus tard."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Échec de l'ouverture du menu de cookies du navigateur"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Indice 'Enregistrer comme cookie' fermé."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Utilisation :</b>\n<code>/link [quality] URL</code>\n\n<b>Exemples :</b>\n<blockquote>• /link https://youtube.com/watch?v=... - meilleure qualité\n• /link 720 https://youtube.com/watch?v=... - 720p ou inférieur\n• /link 720p https://youtube.com/watch?v=... - identique à ci-dessus\n• /link 4k https://youtube.com/watch?v=... - 4K ou inférieur\n• /link 8k https://youtube.com/watch?v=... - 8K ou inférieur</blockquote>\n\n<b>Qualité :</b> de 1 à 10000 (ex. : 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - qualité 8K"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Lien direct obtenu</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format :</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Flux audio :</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Échec de l'obtention des liens de flux"
    LINK_ERROR_GETTING_MSG = "❌ <b>Erreur lors de l'obtention du lien :</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Index de cookie YouTube invalide : {selected_index}. La plage disponible est 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Téléchargement et vérification des cookies YouTube...\n\nTentative {attempt} sur {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Téléchargement et vérification des cookies YouTube...\n\nTentative {attempt} sur {total}\n🔍 Test des cookies..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ Cookies YouTube téléchargés et validés avec succès !\n\nSource utilisée {source} sur {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Tous les cookies YouTube sont expirés ou indisponibles !\n\nContactez l'administrateur du bot pour les remplacer."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ Limite de nouvelle tentative de cookie YouTube dépassée !\n\n🔢 Maximum : {limit} tentatives par heure\n⏰ Veuillez réessayer plus tard"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Le tag #{wrong} contient des caractères interdits. Seules les lettres, chiffres et _ sont autorisés.\nVeuillez utiliser : {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Argument invalide !**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Langue des sous-titres définie : {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Exemple : `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Langue sélectionnée : {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Mode Toujours Demander {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Les sous-titres sont désactivés"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Paramètres de sous-titres</b>\n\n{status_text}\n\nSélectionnez la langue des sous-titres :\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - désactiver les sous-titres\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Paramètres de sous-titres</b>\n\n{status_text}\n\nSélectionnez la langue des sous-titres :"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Titre :</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Durée :</b> {duration} sec\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Flux vidéo :</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- qualité max 720p\n- durée max 1.5 heures\n- taille max vidéo 500mo</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️AVERTISSEMENT : en raison de l'impact élevé sur le CPU, cette fonction est très lente (quasi temps réel) et limitée à :\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Commandes rapides :</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - désactiver les sous-titres\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - activer le mode Toujours Demander\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - définir la langue\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - définir la langue avec AUTO/TRANS activé\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - activer le mode Toujours Demander\n"
    SUBS_AUTO_SUBS_TEXT = " (sous-titres auto)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Mode sous-titres auto {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SOUS-TITRES désactivés via commande : {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SOUS-TITRES Toujours Demander activé via commande : {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "Langue SOUS-TITRES définie via commande : {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "Langue SOUS-TITRES + mode auto défini via commande : {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Utilisateur a ouvert le menu /subs."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Utilisateur a défini la langue des sous-titres sur : {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Utilisateur a basculé le mode AUTO/TRANS sur : {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Utilisateur a basculé le mode Toujours Demander sur : {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Utilisateur a demandé des cookies depuis le navigateur."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Clavier de sélection de navigateur envoyé avec uniquement les navigateurs installés."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Sélection de navigateur fermée."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "COOKIE_URL de repli utilisée avec succès (source masquée)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "COOKIE_URL de repli échouée : statut={status} (masquée)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Erreur inattendue COOKIE_URL de repli : {error_type} : {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Navigateur {browser} non installé."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Cookies sauvegardés en utilisant le navigateur : {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "Fichier de cookie sauvegardé pour l'utilisateur {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "Fichier de cookie existe, a un format correct, et les cookies YouTube fonctionnent."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Fichier de cookie existe et a un format correct, mais les cookies YouTube sont expirés."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Fichier de cookie existe et a un format correct."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Fichier de cookie existe mais a un format incorrect."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Fichier de cookie introuvable."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "URL de cookie {service} vide pour l'utilisateur {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "URL de cookie {service} n'est pas .txt (masquée)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "Fichier de cookie {service} trop volumineux : {size} octets (source masquée)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "Fichier de cookie {service} téléchargé pour l'utilisateur {user_id} (source masquée)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Script introuvable : {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Échec de l'envoi du message de statut initial"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Erreur lors de l'exécution de {script_path} : {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Cache Firebase rechargé par tâche automatique."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Cache Firebase rechargé par administrateur."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Erreur lors du rechargement du cache Firebase : {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Diffusion initiée. Texte :\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Message de diffusion envoyé à tous les utilisateurs."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Échec de la diffusion du message : {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Administrateur {user_id} a effacé le cache pour l'URL : {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Administrateur {user_id} a démarré le script de mise à jour de la liste pornographique : {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Script de mise à jour de la liste pornographique terminé avec succès par l'administrateur {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Script de mise à jour de la liste pornographique échoué par l'administrateur {user_id} : {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Administrateur {user_id} a essayé d'exécuter un script inexistant : {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Erreur lors de l'exécution du script de mise à jour pornographique par l'administrateur {user_id} : {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Administrateur {user_id} a démarré le rechargement du cache pornographique"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Erreur lors du rechargement du cache pornographique par l'administrateur {user_id} : {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Administrateur {user_id} a vérifié l'URL pour NSFW : {url} - Résultat : {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "Utilisateur a demandé un changement de format."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "Format défini sur TOUJOURS_DEMANDER."
    FORMAT_UPDATED_BEST_LOG_MSG = "Format mis à jour vers meilleur : {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "Format mis à jour vers ID {format_id} : {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "Format mis à jour vers ID {format_id} (audio uniquement) : {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "Format mis à jour vers qualité {quality} : {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "Format mis à jour vers : {format}"
    FORMAT_MENU_SENT_LOG_MSG = "Menu de format envoyé."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "Sélection de format fermée."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "Indice de format personnalisé envoyé."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "Menu de résolution de format envoyé."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "Retour au menu de format principal."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "Format mis à jour vers : {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "Format défini sur TOUJOURS_DEMANDER."
    FORMAT_CODEC_SET_LOG_MSG = "Préférence de codec définie sur {codec}"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Menu de format personnalisé fermé"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "Lien direct extrait pour l'utilisateur {user_id} depuis {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Échec de l'extraction du lien direct pour l'utilisateur {user_id} depuis {url} : {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Erreur dans la commande link pour l'utilisateur {user_id} : {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Utilisateur {user_id} a défini le clavier sur {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Utilisateur {user_id} a défini le clavier sur {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo défini via commande : {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Utilisateur a ouvert le menu /mediainfo."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo : fermé."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo activé."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo désactivé."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Taille de division définie sur {size} octets via argument."
    SPLIT_MENU_OPENED_LOG_MSG = "Utilisateur a ouvert le menu /split."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Sélection de division fermée."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Taille de division définie sur {size} octets."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Proxy défini via commande : {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Utilisateur a ouvert le menu /proxy."
    PROXY_MENU_CLOSED_LOG_MSG = "Proxy : fermé."
    PROXY_ENABLED_LOG_MSG = "Proxy activé."
    PROXY_DISABLED_LOG_MSG = "Proxy désactivé."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Message d'aide fermé."
    AUDIO_HELP_SHOWN_LOG_MSG = "Aide /audio affichée"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Utilisateur a demandé l'aide de liste de lecture."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Aide de liste de lecture fermée."
    AUDIO_HINT_CLOSED_LOG_MSG = "Indice audio fermé."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Menu de lien direct créé via bouton LINK pour l'utilisateur {user_id} depuis {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Échec de l'extraction du lien direct via bouton LINK pour l'utilisateur {user_id} depuis {url} : {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "Commande LIST exécutée pour l'utilisateur {user_id}, url : {url}"
    QUICK_EMBED_LOG_MSG = "Intégration rapide : {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Menu Toujours Demander envoyé pour {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Menu de qualités en cache créé pour l'utilisateur {user_id} après erreur : {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Erreur du menu Toujours Demander pour {url} : {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Le format est fixé via les paramètres /args"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Audio"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Vidéo"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Vidéo"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Suivant ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Précédent"
    SUBTITLES_NEXT_BUTTON_MSG = "Suivant ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Tous les champs texte sont vides"
    SENDER_VIDEO_DURATION_MSG = "Durée de la vidéo :"
    SENDER_UPLOADING_FILE_MSG = "📤 Téléversement du fichier..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Téléversement de la Vidéo..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Durée de la vidéo :"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 fichier téléversé."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Infos Vidéo"
    DOWN_UP_NUMBER_MSG = "Numéro"
    DOWN_UP_TITLE_MSG = "Titre"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Vidéo téléchargée."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Traitement pour téléversement..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Fichier partie divisée {part} téléversé"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Téléversement terminé"
    DOWN_UP_FILES_UPLOADED_MSG = "fichiers téléversés"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Fermer"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DOUBLAGES"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 SOUS-TITRES"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Navigateur"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Obtention du lien direct..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Obtention des formats disponibles..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Obtention de la description de la vidéo..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Erreur lors de l'obtention de la description: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ La description de la vidéo n'est pas disponible"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Erreur lors de l'envoi de la description: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Description de la vidéo envoyée à l'utilisateur {user_id} pour {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Démarrage de gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Durée :</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Format :</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Navigateur :</b> Ouvrir dans le navigateur web"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Formats disponibles pour"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Comment utiliser les IDs de format :"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Après avoir obtenu la liste, utilisez un ID de format spécifique :"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - télécharger le format 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - identique à ci-dessus"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - télécharger le format 140 comme audio MP3"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Formats audio uniquement détectés"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Ces formats seront téléchargés comme fichiers audio MP3."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Comment définir le format :</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Télécharger un ID de format spécifique"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Télécharger par qualité"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Télécharger la meilleure qualité"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Toujours demander la qualité"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Formats audio uniquement :</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Télécharger le format 140 comme audio MP3"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Ceux-ci seront téléchargés comme fichiers audio MP3."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Utilisez l'ID de format de la liste ci-dessus"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Erreur : Message original introuvable."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Page de formats"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Erreur lors de l'affichage du menu de formats"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Erreur lors de l'obtention des formats"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Erreur lors de l'obtention des formats disponibles."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Veuillez réessayer plus tard."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp ne peut pas traiter ce contenu"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Le système recommande d'utiliser gallery-dl à la place."
    ALWAYS_ASK_OPTIONS_MSG = "**Options :**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Pour les galeries d'images : <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Pour les images individuelles : <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl fonctionne souvent mieux pour Instagram, Twitter et autres contenus de réseaux sociaux."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Essayer Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Format fixé via /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Sous-titres"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Audio doublé"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Les sous-titres sont disponibles"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Choisir la langue des sous-titres"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Sous-titres introuvables et ne seront pas intégrés"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Repost instantané depuis le cache"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Choisir la langue audio"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW est payant (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Choisir la qualité de téléchargement"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Télécharger l'image (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Regarder la vidéo dans poketube"  # TEMPORAIREMENT DÉSACTIVÉ: le service poketube est en panne
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Obtenir le lien direct vers la vidéo"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Afficher la liste des formats disponibles"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Changer l'extension/codec vidéo"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Intégrer"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Extraire uniquement l'audio"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW est payant (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Repost instantané depuis le cache"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Regarder la vidéo dans poketube"  # TEMPORAIREMENT DÉSACTIVÉ: le service poketube est en panne
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Choisir la langue audio"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Meilleur"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Autre"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝sous-titres uniquement"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Regroupement intelligent"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Ligne de boutons d'action ajoutée (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Lignes de boutons d'action ajoutées (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Boutons du bas ajoutés à la ligne existante"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Nouvelle ligne du bas créée"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Aucune vidéo trouvée dans la liste de lecture"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "URL non supportée"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Aucune vidéo n'a pu être trouvée"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Aucune vidéo trouvée"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Aucun média trouvé"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Ce tweet ne contient pas"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Erreur lors de la récupération des informations vidéo :</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Erreur lors de la récupération des informations vidéo"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Essayez la commande <code>/clean</code> et réessayez. Si l'erreur persiste, YouTube nécessite une autorisation. Mettez à jour cookies.txt via <code>/cookie</code> ou <code>/cookies_from_browser</code> et réessayez."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Menu fermé."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Sélection Manuelle de Qualité"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Choisissez la qualité manuellement car la détection automatique a échoué :"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Tous les Formats Disponibles"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Qualités Disponibles (depuis le cache)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Utilisation des qualités en cache - les nouveaux formats peuvent ne pas être disponibles"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Téléchargement du format"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Téléchargement"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Téléchargement avec suivi de progression..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Téléchargement en utilisant le format :"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Téléchargement audio en utilisant le format :"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Téléchargement de la meilleure qualité..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Téléchargement du dump de base de données..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Téléchargement"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Page de formats"
    ALWAYS_ASK_FROM_CACHE_MSG = "(depuis le cache)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Erreur : Message original introuvable. Il a peut-être été supprimé. Veuillez renvoyer le lien."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Erreur : URL originale introuvable. Veuillez renvoyer le lien."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Lien direct obtenu</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Titre :</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Durée :</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Format :</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Flux vidéo :</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Flux audio :</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Échec de l'obtention des liens de flux"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Lien direct extrait via menu Toujours Demander pour l'utilisateur {user_id} depuis {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Échec de l'extraction du lien direct via menu Toujours Demander pour l'utilisateur {user_id} depuis {url} : {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Lien direct extrait via down_and_up_with_format pour l'utilisateur {user_id} depuis {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Échec de l'extraction du lien direct via down_and_up_with_format pour l'utilisateur {user_id} depuis {url} : {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Lien direct extrait via down_and_audio pour l'utilisateur {user_id} depuis {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Échec de l'extraction du lien direct via down_and_audio pour l'utilisateur {user_id} depuis {url} : {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Audio envoyé depuis le cache."
    AUDIO_PROCESSING_MSG = "🎙️ L'audio est en cours de traitement..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Téléchargement de l'audio :\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Erreur survenue lors du téléchargement de l'audio."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Échec de l'extraction des informations audio"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Ignorant le type de fichier non supporté dans la liste de lecture à l'index {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "Fichier audio introuvable après téléchargement."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ Échec de l'envoi de l'audio : La taille du fichier est égale à 0 B (index de la liste de lecture {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ Le fichier audio est encore en cours de téléchargement, veuillez patienter..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Téléversement du fichier audio...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Échec de l'envoi de l'audio : {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Audio de liste de lecture envoyé : {sent}/{total} fichiers (qualité={quality}) à l'utilisateur{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Échec du téléchargement de l'audio : {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Téléchargement annulé en raison du délai d'attente (2 heures)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Fichier vidéo introuvable : {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ Échec de l'envoi de la vidéo : La taille du fichier est égale à 0 B (index de la liste de lecture {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ Le fichier vidéo est encore en cours de téléchargement, veuillez patienter..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Erreur lors du traitement de la vidéo : {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Erreur lors de l'envoi du fichier de description : {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 si vous voulez changer la légende de la vidéo - répondez à la vidéo avec le nouveau texte</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Aucun sous-titre détecté"
    VIDEO_PROGRESS_MSG = "<b>Vidéo :</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Audio :</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL :</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ Limite d'URL dépassée : {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Traitement terminé"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Les plages de liste de lecture ne sont pas autorisées en mode URL multiple. Envoyez uniquement des URLs individuelles sans plages (*1*5, /vid 1-10, etc.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Vérifiez <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>ici</a> si votre site est supporté"
    ERROR_COOKIE_NEEDED_MSG = "Vous pourriez avoir besoin d'un <code>cookie</code> pour télécharger cette vidéo. D'abord, nettoyez votre espace de travail via la commande <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Pour Youtube - obtenez un <code>cookie</code> via la commande <b>/cookie</b>. Pour tout autre site supporté - envoyez votre propre cookie (<a href='https://t.me/tg_ytdlp/203'>guide1</a>) (<a href='https://t.me/tg_ytdlp/214'>guide2</a>) et après cela renvoyez votre lien vidéo."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Choisir la langue des sous-titres"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Aucune langue audio alternative"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Choisir la langue audio"
    PAGE_NUMBER_MSG = "Page {page}"
    TOTAL_PROGRESS_MSG = "Progression Totale"
    SUBTITLE_MENU_CLOSED_MSG = "Menu de sous-titres fermé."
    SUBTITLE_LANGUAGE_SET_MSG = "Langue des sous-titres définie : {value}"
    AUDIO_SET_MSG = "Audio défini : {value}"
    FILTERS_UPDATED_MSG = "Filtres mis à jour"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Retour"
    CLOSE_BUTTON_TEXT = "🔚Fermer"
    LIST_BUTTON_TEXT = "📃Liste"
    IMAGE_BUTTON_TEXT = "🖼Image"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Qualités non détectées automatiquement\nUtilisez le bouton 'Autre' pour voir tous les formats disponibles.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Flux en Direct Détecté**\n\nLe téléchargement de flux en direct en cours ou infinis n'est pas autorisé.\n\nVeuillez attendre la fin du flux et réessayer le téléchargement lorsque :\n• La durée du flux est connue\n• Le flux est terminé\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Téléchargement de Flux en Direct</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Fragment {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Taille max : {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Durée totale : {duration} sec"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Flux en Direct - Fragment {chunk}</b>\n⏱ Durée : {duration} sec\n📦 Taille : {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Fragment {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Téléchargement de Flux en Direct Terminé</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "{chunks} fragment(s) téléchargé(s)"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Durée totale : {duration} sec"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Téléchargement de Flux en Direct Arrêté</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Le répertoire utilisateur a été supprimé (probablement par la commande /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "Le fichier fragment a été supprimé (probablement par la commande /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Le flux est terminé"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Veuillez sélectionner un format différent en utilisant la commande `/format`."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Lien direct obtenu</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Titre :</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Durée :</b> {duration} sec\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format :</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Flux vidéo :</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Flux audio :</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Erreur de Traitement de Fichier**\n\nLa vidéo a été téléchargée mais n'a pas pu être traitée en raison de caractères invalides dans le nom de fichier.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Erreur de Traitement de Fichier**\n\nLa vidéo a été téléchargée mais n'a pas pu être traitée en raison d'une erreur d'argument invalide.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Raison:**\n"
        "• Le fichier téléchargé n'est pas un fichier vidéo\n"
        "• Il pourrait s'agir d'un document (PDF, DOC, etc.) ou d'une archive\n\n"
        "**Solution:**\n"
        "• Vérifiez le lien - il pourrait mener à un document, pas à une vidéo\n"
        "• Essayez un lien ou une source différente\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Raison:**\n"
        "• Le fichier ne peut pas être traité comme une vidéo\n"
        "• Ce n'est peut-être pas un fichier vidéo ou le fichier est corrompu\n\n"
        "**Solution:**\n"
        "• Vérifiez le lien - il pourrait mener à un document, pas à une vidéo\n"
        "• Essayez un lien ou une source différente\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Format Non Disponible**\n\nLe format vidéo demandé n'est pas disponible pour cette vidéo.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ ID de format {format_id} introuvable pour cette vidéo.\n\nIDs de format disponibles : {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **Le format AV1 n'est pas disponible pour cette vidéo.**\n\n**Formats disponibles :**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Erreur de Traitement de Fichier**\n\nL'audio a été téléchargé mais n'a pas pu être traité en raison de caractères invalides dans le nom de fichier.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Erreur de Traitement de Fichier**\n\nL'audio a été téléchargé mais n'a pas pu être traité en raison d'une erreur d'argument invalide.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "L'utilisateur a entré un contenu interdit. Ne peut pas être téléchargé."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "Flou NSFW défini via commande : {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Utilisateur a ouvert le menu /nsfw."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW : fermé."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Échec du téléchargement du cookie {service} : statut={status} (url masquée)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Erreur lors du téléchargement du cookie {service} : {error} (url masquée)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Erreur inattendue lors du téléchargement du cookie {service} (url masquée) : {error_type} : {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Fichier de cookie mis à jour pour l'utilisateur {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Contenu de cookie invalide fourni par l'utilisateur {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "Les URLs de cookies YouTube sont vides pour l'utilisateur {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "Cookies YouTube téléchargés et validés pour l'utilisateur {user_id} depuis la source {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Toutes les sources de cookies YouTube ont échoué pour l'utilisateur {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Erreur dans la commande check_porn par l'administrateur {admin_id} : {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Taille de partie divisée définie sur {size} octets."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Téléversement vidéo terminé avec division de fichier."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Vidéos de liste de lecture envoyées : {sent}/{total} fichiers (qualité={quality}) à l'utilisateur {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Erreur inconnue : {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Ignorant le type de fichier non supporté dans la liste de lecture à l'index {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg introuvable. Veuillez installer FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Échec de la conversion en MP4 : {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ L'intégration des sous-titres peut prendre beaucoup de temps (jusqu'à 1 min par 1 min de vidéo) !\n🔥 Démarrage de la gravure des sous-titres..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Les sous-titres ne peuvent pas être intégrés en raison des limites (qualité/durée/taille)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Les sous-titres ne sont pas disponibles pour la langue sélectionnée"
    ERROR_SENDING_VIDEO_MSG = "❌ Erreur lors de l'envoi de la vidéo : {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Vidéos de liste de lecture envoyées : {sent}/{total} fichiers."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Téléchargement annulé en raison du délai d'attente (2 heures)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Échec du téléchargement de la vidéo : {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Erreur : {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ Le JSON doit être un objet (dictionnaire)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Format JSON invalide. Veuillez fournir un JSON valide."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ La valeur doit être entre {min_val} et {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} défini sur : <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Vrai"
    ARGS_FALSE_BUTTON_MSG = "❌ Faux"
    ARGS_BACK_BUTTON_MSG = "🔙 Retour"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Fermer"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Vrai"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Faux"
    ARGS_NOT_SET_MSG = "Non défini"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ Le format AV1 n'est pas disponible pour cette vidéo.\n\nFormats disponibles :\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Erreur lors du téléchargement : {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ Aucune vidéo trouvée dans la liste de lecture à l'index {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Échec de la Conversion Vidéo**\n\nLa vidéo n'a pas pu être convertie en MP4 en raison d'une erreur d'argument invalide.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Échec de la Conversion Vidéo**\n\nLa vidéo n'a pas pu être convertie en MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Échec de l'obtention des liens de flux"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Erreur lors de l'obtention du lien :</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ Aucun contenu trouvé à l'index {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Erreur : Message original introuvable."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Erreur : URL introuvable."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ Cette URL ne peut pas être intégrée."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ Le codec {codec} n'est pas disponible pour cette vidéo"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ Le format {format} n'est pas disponible pour cette vidéo"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Limite de flood. Réessayez plus tard."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Vérifier Cookie"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ TOUT (AUTO)"
    PROXY_OFF_BUTTON_MSG = "❌ DÉSACTIVÉ"
    PROXY_CLOSE_BUTTON_MSG = "🔚Fermer"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Sélectionnez le pays :"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Effacer la sélection du pays"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Pays sélectionné : {country} (code : {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Proxy disponibles : {proxy_count} (HTTP : {http_count}, SOCKS5 : {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Le robot essaiera d'abord HTTP, puis SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Proxy automatiquement activé pour le pays sélectionné"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Sélection du pays effacée"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Sélection du pays effacée"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Pays sélectionné : {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Utilisation du pays à partir du fichier : {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Pays disponibles à partir du fichier : {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 Pays sélectionné : {country} (code : {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ Proxy activé pour ce pays"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ Proxy désactivé (appuyez sur ALL (AUTO) pour activer)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ ACTIVÉ"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ DÉSACTIVÉ"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Fermer"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV : ACTIVÉ"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV : DÉSACTIVÉ"
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ ACTIVÉ (Pas de Flou)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ACTIVÉ (Pas de Flou)"
    NSFW_OFF_BLUR_MSG = "✅ DÉSACTIVÉ (Flou)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ DÉSACTIVÉ (Flou)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Propre"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Erreur lors du traitement du message de réponse pour l'utilisateur {user} : {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Erreur lors de l'envoi de la diffusion à l'utilisateur {user} : {error}"
    ADMIN_LOGS_FORMAT_MSG = "Logs de {bot_name}\nUtilisateur : {user_id}\nTotal logs : {total}\nHeure actuelle : {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nTotal {path} : {count}\nHeure actuelle : {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Total Utilisateurs : {count}</i>\n20 derniers {path} :\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Caches pornographiques rechargés par l'administrateur {admin_id}. Domaines : {domains}, Mots-clés : {keywords}, Sites : {sites}, LISTE BLANCHE : {whitelist}, LISTE GRISE : {greylist}, LISTE NOIRE : {black_list}, MOTS-CLÉS BLANCS : {white_keywords}, DOMAINES PROXY : {proxy_domains}, DOMAINES PROXY_2 : {proxy_2_domains}, REQUÊTE PROPRE : {clean_query}, DOMAINES SANS COOKIE : {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Erreur lors de l'envoi du message de délai d'attente : {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Choisir la langue</b>"
    LANG_CHANGED_MSG = "✅ Langue changée en {lang_name}"
    LANG_ERROR_MSG = "❌ Erreur lors du changement de langue"
    LANG_CLOSED_MSG = "Sélection de langue fermée"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[NAVIGATEUR] callback : {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Ajout du bouton de surveillance du navigateur avec URL : {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "URL de surveillance du navigateur non configurée : {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Paramètre de clavier mis à jour !**\n\nNouveau paramètre : **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Échec du masquage du clavier : {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Utilisation des cookies YouTube fonctionnels pour l'extraction de lien pour l'utilisateur {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Aucun cookie YouTube fonctionnel disponible pour l'extraction de lien pour l'utilisateur {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Utilisation des cookies YouTube existants pour l'extraction de lien pour l'utilisateur {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Aucun cookie YouTube trouvé pour l'extraction de lien pour l'utilisateur {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Fichier de cookie global copié vers le dossier de l'utilisateur {user_id} pour l'extraction de lien"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Utilisateur {user_id} a demandé la commande mediainfo"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Utilisateur {user_id} est administrateur : {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Utilisateur {user_id} est dans le canal : {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Accès refusé à l'utilisateur {user_id} - n'est pas administrateur et n'est pas dans le canal"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Accès accordé à l'utilisateur {user_id}"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback : {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Cette commande n'est disponible que pour les administrateurs."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Téléchargement terminé avec support du token PO"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Limite de flood. Réessayez plus tard."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ Erreur de rafraîchissement du token REST : {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Erreur lors de la fermeture de la session Firebase : {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Erreur lors de l'initialisation de la structure de base de données : {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Tous les paramètres ne sont pas définis dans config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL n'est pas défini"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey n'est pas défini pour obtenir idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Erreur lors du téléchargement du dump Firebase : {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Échec du téléchargement du dump Firebase via REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Erreur dans _download_and_reload_cache : {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Erreur lors de l'exécution de auto reload_cache (tentative {attempt}/{max_retries}) : {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Toutes les tentatives de nouvelle tentative ont échoué"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Démarrage du téléchargement du dump Firebase à {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Dépendance non disponible : requests ou Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ La base de données est vide"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Erreur lors de la fermeture du logger : {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Erreur lors du nettoyage : {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Erreur de clonage : {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Délai d'attente de clonage"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Exception de clonage : {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Mise à jour annulée par l'utilisateur"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Dépôt cloné avec succès"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Sauvegardes déplacées vers _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Tous les modules sont chargés"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Nettoyage terminé à la sortie"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Signal {signal} reçu, arrêt gracieux..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Veuillez patienter..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Téléchargement du flux HLS :"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "en attente des fragments"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Sauvegarde {ts} introuvable dans _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Échec de la restauration {src} -> {dest_path} : {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Restauré : {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL :</b> <code>{url}</code>\n\n<b>Détails :</b> {error_details}\n\nTéléchargement arrêté en raison d'une erreur critique.\n\n💡 <b>Astuce :</b> Si vous obtenez une erreur 401 Non autorisé, essayez d'utiliser la commande <code>/cookie instagram</code> ou envoyez vos propres cookies pour vous authentifier avec Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domaine dans la liste noire pornographique : {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Mots-clés pornographiques trouvés : {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domaine dans la liste blanche : {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Mots-clés de liste blanche trouvés : {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Aucun mot-clé pornographique trouvé"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Erreur API TikTok à l'index {index}, passage à l'audio suivant..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Erreur API TikTok à l'index {index}, passage à la vidéo suivante..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "Utilisateur a entré une <b>url</b>\n <b>nom de l'utilisateur :</b> {user_name}\nURL : {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>Utilisateur a entré comme ceci :</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Rejoindre le Canal"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Enregistrement du gestionnaire : {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Télécharger mes 5 cookies"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Obtenir le cookie YT du navigateur"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Valider votre fichier de cookie"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Téléverser un cookie personnalisé"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Fermer"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Formats disponibles pour : {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Fermer"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Fermer"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Fermer"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Fermer"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Aide fermée."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Fermé"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Une erreur s'est produite"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg introuvable dans PATH ou le répertoire du projet. Veuillez installer FFmpeg."
    YTDLP_NOT_FOUND_MSG = "Binaire yt-dlp introuvable dans PATH ou le répertoire du projet. Veuillez installer yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "La vidéo sera divisée en {rounds} parties, ce qui peut être excessif"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Division de la partie vidéo {current}/{total} : {start_time:.2f}s à {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Échec de la création de la partie divisée {part} : {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Partie divisée {part} créée avec succès : {target_name} ({size} octets)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Erreur lors de la division de la partie vidéo {part} : {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Vidéo divisée en {count} parties avec succès"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Erreur dans le processus de division vidéo : {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Erreur lors du traitement de la vidéo {video_path} : {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Le fichier vidéo n'existe pas : {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Erreur lors de l'analyse des dimensions '{size_result}' : {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Impossible de déterminer les dimensions de la vidéo à partir de '{size_result}', utilisation par défaut : {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Erreur lors de la création de la miniature : {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Erreur lors de l'analyse de la durée de la vidéo : {error}, résultat était : {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Miniature non créée à {thumb_dir}, utilisation par défaut"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Erreur d'exécution de commande : {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Erreur lors de la création de la miniature avec FFmpeg : {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Ignorant la section de configuration non-dict : {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Définition {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Utilisation des cookies utilisateur : {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Utilisation des cookies YouTube pour l'utilisateur {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Fichier de cookie global copié vers le dossier de l'utilisateur {user_id}"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Utilisation des cookies globaux copiés comme cookies utilisateur : {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Échec de la copie du fichier de cookie global pour l'utilisateur {user_id} : {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Utilisation de --no-cookies pour le domaine : {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy demandé mais échec de l'import/obtention de la configuration : {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Forcer l'utilisation du proxy pour gallery-dl : {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy demandé mais la configuration du proxy est incomplète"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Échec de l'assistant proxy : {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Analyse des éléments de l'extracteur..."
    GALLERY_DL_ITEM_COUNT_MSG = "Élément {count} : {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Métadonnées trouvées (tag 2) : {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL trouvée (tag 3) : {url}, métadonnées : {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Métadonnées trouvées (héritage) : {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL trouvée (héritage) : {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Nom de fichier trouvé : {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Répertoire trouvé : {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Extension trouvée : {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "{count} éléments analysés, info : {info}, repli : {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Définition de la configuration gallery-dl : {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Tentative de la Stratégie A : extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "Module gallery_dl.extractor introuvable"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() non disponible dans cette version"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Appel de extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Aucun extracteur ne correspond à l'URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Définition des cookies sur l'extracteur : {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Échec de la définition des cookies sur l'extracteur : {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Extracteur trouvé, appel de items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Stratégie A réussie, info obtenue : {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Stratégie A : extractor.items() n'a renvoyé aucune info valide"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Stratégie A (extractor.find) a échoué : {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Métadonnées de repli depuis --get-urls : total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Toutes les stratégies ont échoué à obtenir les métadonnées"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Échec de l'extraction des informations d'image : {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "Module gallery_dl.job introuvable (installation cassée ?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob non disponible dans cette version"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Recherche des fichiers téléchargés dans le répertoire gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Tentative de trouver les fichiers par noms depuis l'extracteur"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Erreur lors de la lecture des arguments utilisateur pour {user_id} : {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Erreur lors du traitement de la vidéo{video_path} : {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "L'utilisateur {user_id} a send_as_file activé, envoi en tant que document"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video a expiré à plusieurs reprises ; repli sur send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Légende trop longue, tentative avec légende minimale"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (légende minimale) a expiré ; repli sur send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Erreur lors de l'envoi de la vidéo avec légende minimale : {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Erreur lors de l'envoi du fichier de description complet : {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Erreur lors de la suppression du fichier de description temporaire : {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
    
    # YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Ignorant match_filter pour le domaine dans NO_FILTER_DOMAINS : {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Vérification des cookies YouTube existants sur l'URL de l'utilisateur pour la détection de format pour l'utilisateur {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Les cookies YouTube existants fonctionnent sur l'URL de l'utilisateur pour la détection de format pour l'utilisateur {user_id} - utilisation de ceux-ci"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Les cookies YouTube existants ont échoué sur l'URL de l'utilisateur, tentative d'obtenir de nouveaux pour la détection de format pour l'utilisateur {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Tentative de la source de cookie YouTube {i} pour la détection de format pour l'utilisateur {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "Les cookies YouTube de la source {i} fonctionnent sur l'URL de l'utilisateur pour la détection de format pour l'utilisateur {user_id} - sauvegardés dans le dossier utilisateur"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "Les cookies YouTube de la source {i} ne fonctionnent pas sur l'URL de l'utilisateur pour la détection de format pour l'utilisateur {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Échec du téléchargement des cookies YouTube de la source {i} pour la détection de format pour l'utilisateur {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Toutes les sources de cookies YouTube ont échoué pour la détection de format pour l'utilisateur {user_id}, tentative sans cookies"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Aucune source de cookie YouTube configurée pour la détection de format pour l'utilisateur {user_id}, tentative sans cookies"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Aucun cookie YouTube trouvé pour la détection de format pour l'utilisateur {user_id}, tentative d'obtenir de nouveaux"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Utilisation des cookies YouTube pour la détection de format pour l'utilisateur {user_id} (déjà validés dans le menu Always Ask)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Aucun cookie YouTube trouvé pour la détection de format pour l'utilisateur {user_id}, tentative de restauration..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Fichier de cookie global copié vers le dossier de l'utilisateur {user_id} pour la détection de format"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Échec de la copie du fichier de cookie global pour l'utilisateur {user_id} : {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Utilisation de --no-cookies pour le domaine dans get_video_formats : {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "Application non initialisée. Impossible d'accéder à {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Légende :</b> <code>{caption}</code>\n<b>ID utilisateur :</b> <code>{user_id}</code>\n<b>Prénom utilisateur :</b> <code>{users_name}</code>\n<b>ID fichier vidéo :</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Erreur dans caption_editor : {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Erreur inattendue dans caption_editor : {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL Vidéo</a>{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL manquant dans la configuration"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin initialisé"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken rafraîchi"
    DB_LOG_FOR_USER_ADDED_MSG = "Log pour utilisateur ajouté"
    DB_DATABASE_CREATED_MSG = "base de données créée"
    DB_BOT_STARTED_MSG = "Bot démarré"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY persisté dans config.py : {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Partie de liste de lecture déjà en cache : {path_parts}, ignorée"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos : aucun cache trouvé pour aucune variante URL/qualité, renvoi d'un dict vide"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count : comptage rapide pour grande plage : {cached_count} vidéos en cache"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids : aucun cache trouvé pour hash {url_hash}, qualité {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids : aucun cache trouvé pour aucune variante URL, renvoi None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Accès refusé. Administrateur uniquement."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Rechargement automatique du cache Firebase mis à jour !\n\n📊 Statut : {status}\n⏰ Planification : toutes les {interval} heures à partir de 00:00\n🕒 Prochain rechargement : {next_exec} (dans {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Rechargement automatique du cache Firebase arrêté !\n\n📊 Statut : ❌ DÉSACTIVÉ\n💡 Utilisez /auto_cache on pour réactiver"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Argument invalide. Utilisez /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ L'intervalle doit être entre 1 et 168 heures"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Échec de la définition de l'intervalle"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Intervalle de rechargement automatique du cache Firebase mis à jour !\n\n📊 Statut : ✅ ACTIVÉ\n⏰ Planification : toutes les {interval} heures à partir de 00:00\n🕒 Prochain rechargement : {next_exec} (dans {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Rechargement automatique du cache Firebase démarré !\n\n📊 Statut : ✅ ACTIVÉ\n⏰ Planification : toutes les {interval} heures à partir de 00:00\n🕒 Prochain rechargement : {next_exec} (dans {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Rechargement automatique du cache Firebase arrêté !\n\n📊 Statut : ❌ DÉSACTIVÉ\n💡 Utilisez /auto_cache on pour réactiver"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Rechargement automatique ACTIVÉ ; prochain à {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Rechargement automatique DÉSACTIVÉ par l'administrateur."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Intervalle de rechargement automatique défini sur {interval}h ; prochain à {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Rechargement automatique démarré ; prochain à {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Rechargement automatique arrêté par l'administrateur."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Cache Firebase chargé : {count} nœuds racine"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Fichier de cache Firebase introuvable, démarrage avec cache vide : {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Échec du chargement du cache Firebase : {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Cache Firebase rechargé : {count} nœuds racine"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Fichier de cache Firebase introuvable : {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Échec du rechargement du cache Firebase : {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 Vous êtes banni du bot ! Pour être débanni, contactez {Config.ADMIN_USERNAME}\n<blockquote>P.S. Ne quittez pas le canal - vous serez automatiquement banni ⛔️</blockquote>\n🌍Changer la langue /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Aucun format vidéo trouvé. Tentative avec le téléchargeur d'images…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram a limité l'envoi de messages.\n⏳ Veuillez patienter : {time_str}\nPour mettre à jour le minuteur, envoyez l'URL à nouveau 2 fois."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Cliquez sur le bouton pour copier l'URL du flux, puis collez-la dans l'application VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Cliquez sur le bouton pour copier l'URL du flux, puis collez-la dans l'application VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Erreur lors de l'obtention du lien :</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Erreur lors de l'envoi du fichier de formats : {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Échec de l'obtention des formats :\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Analyse en cours... (attendre 6 sec)"
    AA_PROCESSING_MSG = "🔎 Analyse en cours..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Le tag #{wrong} contient des caractères interdits. Seules les lettres, chiffres et _ sont autorisés.\nVeuillez utiliser : {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Pour fonctionner dans le groupe, le bot a besoin des droits d'administrateur. Veuillez faire du bot un administrateur de ce groupe."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Bonjour {first_name},\n \n<i>Ce bot🤖 peut télécharger n'importe quelle vidéo directement dans Telegram.😊 Pour plus d'informations, appuyez sur <b>/help</b></i> 👈\n\n<blockquote>P.S. Le téléchargement de contenu 🔞NSFW et de fichiers depuis ☁️Stockage Cloud est payant ! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Ne quittez pas le canal - vous serez banni de l'utilisation du bot ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Aucun fichier à supprimer."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 Tous les fichiers supprimés avec succès !\n\nFichiers supprimés :\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ ATTENDEZ QUE VOTRE TÉLÉCHARGEMENT PRÉCÉDENT SOIT TERMINÉ"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "Instance d'application est None dans check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit : info_dict est None, autorisation du téléchargement"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits : info_dict est None, autorisation de l'intégration de sous-titres"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits : vérification des limites - qualité_max={max_quality}p, durée_max={max_duration}s, taille_max={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits : clés info_dict : {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Intégration de sous-titres ignorée : durée {duration}s dépasse la limite {max_duration}s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Intégration de sous-titres ignorée : taille {size_mb:.2f}MB dépasse la limite {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Intégration de sous-titres ignorée : qualité {width}x{height} (côté min {min_side}p) dépasse la limite {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "liste de lecture"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Limite de plage dépassée pour {service} : {count} (maximum {max_count}).\n\nUtilisez l'une de ces commandes pour télécharger le maximum de fichiers disponibles :\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Limite de plage dépassée pour {service} : {count} (maximum {max_count})\nID Utilisateur : {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "Fournisseur de token PO désactivé dans la configuration"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "L'URL {url} n'est pas un domaine YouTube, ignoré le token PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "Le fournisseur de token PO n'est pas disponible à {base_url}, repli sur l'extraction YouTube standard"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "Cache du fournisseur de token PO effacé, vérification de la disponibilité à la prochaine requête"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Instance d'application non disponible encore"
    HELPER_USER_NAME_MSG = "Utilisateur"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood wait détecté, attente de {wait_seconds} secondes"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood wait détecté mais impossible d'extraire le temps, attente de {retry_delay} secondes"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "Erreur msg_seqno détectée, attente de {retry_delay} secondes"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Configuration proxy incomplète, utilisation de la connexion directe"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Fermer"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Fermer"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Fermer"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Fichier de logs supprimé."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Fichier de tags supprimé."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Fichier de format supprimé."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Fichier de division supprimé."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Fichier Mediainfo supprimé."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Paramètres de sous-titres supprimés."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Paramètres de clavier supprimés."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Paramètres Args supprimés."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 Paramètres NSFW supprimés."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Paramètres Proxy supprimés."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Paramètres Flood wait supprimés."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Fermer"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Commande de Téléchargement Vidéo"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Utilisation : <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Exemples :"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (ordre direct)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (ordre inverse)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Voir aussi : /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Utilisateur {user_id} a fermé la commande add_bot_to_group"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Échec de l'extraction de l'ID YouTube"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Échec du téléchargement de la miniature ou elle est trop grande"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Choisir la langue audio"
    AA_NO_SUBTITLES_DETECTED_MSG = "Aucun sous-titre détecté"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Choisir la langue des sous-titres"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Erreur d'Authentification"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Compte Introuvable"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Compte Indisponible"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Limite de Taux Dépassée"
    GALLERY_DL_NETWORK_ERROR_MSG = "Erreur Réseau"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Contenu Indisponible"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Restrictions Géographiques"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Vérification Requise"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Violation de Politique"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Erreur Inconnue"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Téléchargement démarré</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Fermer"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Commande de Téléchargement Vidéo</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Utilisation : <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Exemples :</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Voir aussi : /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Limite de flood. Réessayez plus tard."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Utilisation de la Commande Cookie</b>

<code>/cookie</code> - Afficher le menu cookie
<code>/cookie youtube</code> - Télécharger les cookies YouTube
<code>/cookie instagram</code> - Télécharger les cookies Instagram
<code>/cookie tiktok</code> - Télécharger les cookies TikTok
<code>/cookie x</code> ou <code>/cookie twitter</code> - Télécharger les cookies Twitter/X
<code>/cookie facebook</code> - Télécharger les cookies Facebook
<code>/cookie custom</code> - Afficher les instructions de cookie personnalisé

<i>Les services disponibles dépendent de la configuration du bot.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Fichier de cookie supprimé et cache effacé."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Précédent"
    SUBS_BACK_BUTTON_MSG = "🔙Retour"
    SUBS_OFF_BUTTON_MSG = "🚫 DÉSACTIVÉ"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - définir la langue"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - définir la langue avec AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Options valides :"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 LANGUE"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 NETTOYER"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIES"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 MÉDIA"
    SETTINGS_INFO_BUTTON_MSG = "📖 INFO"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ PLUS"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Cookies uniquement"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Logs "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Tags"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Format"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Division"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Sous-titres"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Clavier"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Args"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Proxy"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Flood wait"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Tous les fichiers"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Télécharger mes 5 cookies"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Obtenir le cookie YT du navigateur"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Valider votre fichier de cookie"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Téléverser un cookie personnalisé"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Changer la qualité et le format"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Activer / Désactiver MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Changer la taille de partie vidéo divisée"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Télécharger la vidéo en audio"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Paramètres de langue des sous-titres"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Comment télécharger les listes de lecture"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Télécharger des images via gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Envoyer vos #tags"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Obtenir des instructions"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Envoyer vos logs"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Aide de la liste de lecture"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - comment faire"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Obtenir des liens vidéo directs"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Activer/désactiver le proxy"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Disposition du clavier"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Assistant de recherche en ligne"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - arguments yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - Paramètres de flou NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Options de Nettoyage</b>\n\nChoisissez ce qu'il faut nettoyer :"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile : Activer la recherche @vid"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile : Activer la recherche @vid"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 DÉSACTIVÉ"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 COMPLET"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL Images]({url})"
    IMAGE_ERROR_MSG = "❌ Erreur : {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Retour"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - format personnalisé"
    FORMAT_720P_MSG = "• <code>/format 720</code> - qualité 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - qualité 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - qualité 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - ID de format spécifique"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - toujours afficher le menu"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/meilleure qualité"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Toujours Demander (menu + boutons)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Autres (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (meilleur pour Telegram PC/Mac)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (meilleur pour Telegram mobile)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (qualité MAX)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Personnalisé (entrez le vôtre)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Depuis le Navigateur"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Le Vôtre"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Mode de saisie fermé automatiquement en raison de l'inactivité (5 minutes)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Tout Réinitialiser"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Voir Actuel"
    ARGS_BACK_BUTTON_MSG = "🔙 Retour"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Transmettez ce message à vos favoris pour sauvegarder ces paramètres en tant que modèle.</i> \n\n<i>Transmettez ce message ici pour appliquer ces paramètres.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Arguments yt-dlp Actuels :\n\nAucun paramètre personnalisé configuré.\n\n---\n\n<i>Transmettez ce message à vos favoris pour sauvegarder ces paramètres en tant que modèle.</i> \n\n<i>Transmettez ce message ici pour appliquer ces paramètres.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Arguments yt-dlp Actuels :\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Exporter les Paramètres"
    ARGS_SETTINGS_READY_MSG = "Paramètres prêts pour l'exportation ! Transmettez ce message aux favoris pour sauvegarder."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Arguments yt-dlp Actuels :"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Échec de la reconnaissance des paramètres dans le message. Assurez-vous d'avoir envoyé un modèle de paramètres correct."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Paramètres importés avec succès !\n\nParamètres appliqués : {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Paramètres clés :\n"
    ARGS_ERROR_SAVING_MSG = "❌ Erreur lors de la sauvegarde des paramètres importés."
    ARGS_ERROR_IMPORTING_MSG = "❌ Une erreur s'est produite lors de l'importation des paramètres."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Télécharger les Fichiers Cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Choisissez un service pour télécharger le fichier cookie."
    COOKIE_MENU_SAVE_INFO_MSG = "Les fichiers cookie seront sauvegardés sous cookie.txt dans votre dossier."
    COOKIE_MENU_TIP_HEADER_MSG = "Astuce : Vous pouvez également utiliser la commande directe :"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – télécharger et valider les cookies"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – utiliser une source spécifique par index (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Puis vérifiez avec <code>/check_cookie</code> (tests sur RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Toujours Demander"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Lien"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Regarder"  # TEMPORAIREMENT DÉSACTIVÉ: le service poketube est en panne
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Description"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ COUPER"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Découpage Vidéo</b>\n\nDurée de la vidéo: <b>{start_time} - {end_time}</b>\n\nVeuillez envoyer la plage horaire souhaitée au format:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nExemple: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Format invalide. Veuillez utiliser: <code>HH:MM:SS-HH:MM:SS</code>\n\nExemple: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Plage invalide. L'heure de début doit être inférieure à l'heure de fin."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ La plage horaire est en dehors des limites de la vidéo.\n\nDurée de la vidéo: <b>{start_time} - {end_time}</b>\n\nVotre plage doit être dans ces limites."
    AA_ERROR_VIDEO_DURATION_UNKNOWN_MSG = "❌ Impossible de déterminer la durée de la vidéo. Veuillez réessayer ou utiliser une autre vidéo."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>La vidéo sera coupée:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Partiellement terminé - {successful_uploads}/{total_files} fichiers audio téléversés."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Audio téléchargé et envoyé avec succès - {total_files} fichiers téléversés."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Compte TikTok Privé</b>\n\n"
        "Ce compte TikTok est privé ou toutes les vidéos sont privées.\n\n"
        "<b>💡 Solution :</b>\n"
        "1. Suivez le compte @{username}\n"
        "2. Envoyez vos cookies au bot en utilisant la commande <code>/cookie</code>\n"
        "3. Réessayez\n\n"
        "<b>Après avoir mis à jour les cookies, réessayez !</b>"
    )

    #######################################################
