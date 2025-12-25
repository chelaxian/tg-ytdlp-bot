# Messages Configuration
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# Removed circular import

class Messages(object):
    #######################################################
    # Messages and errors
    #######################################################
    CREDITS_MSG = "<blockquote><i>管理：</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 言語を変更: /lang</b>"
    TO_USE_MSG = "<i>このボットを使用するには、@tg_ytdlp Telegramチャンネルに登録する必要があります。</i>\nチャンネルに参加した後、<b>動画リンクを再度送信すると、ボットがダウンロードします</b> ❤️\n\n<blockquote>P.S. 🔞NSFWコンテンツと☁️クラウドストレージからのファイルのダウンロードは有料です！1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ チャンネルを離れないでください - ボットの使用が禁止されます ⛔️</blockquote>"

    ERROR1 = "URLリンクが見つかりませんでした。<b>https://</b>または<b>http://</b>を含むURLを入力してください"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>プレイリスト (yt-dlp)</b>

プレイリストをダウンロードするには、URLの末尾に<code>*start*end</code>の範囲を付けて送信してください。例：<code>URL*1*5</code>（1から5まで最初の5本の動画）。<code>URL*-1*-5</code>（1から5まで最後の5本の動画）。
または<code>/vid FROM-TO URL</code>を使用できます。例：<code>/vid 3-7 URL</code>（最初から3から7まで動画をダウンロード）。<code>/vid -3-7 URL</code>（最後から3から7まで動画をダウンロード）。<code>/audio</code>コマンドでも動作します。

<b>例：</b>

🟥 <b>YouTubeプレイリストからの動画範囲：</b>（🍪が必要）
<code>https://youtu.be/playlist?list=PL...*1*5</code>
（1から5まで最初の5本の動画をダウンロード）
🟥 <b>YouTubeプレイリストからの単一動画：</b>（🍪が必要）
<code>https://youtu.be/playlist?list=PL...*3*3</code>
（3番目の動画のみダウンロード）

⬛️ <b>TikTokプロフィール：</b>（あなたの🍪が必要）
<code>https://www.tiktok.com/@USERNAME*1*10</code>
（ユーザープロフィールから最初の10本の動画をダウンロード）

🟪 <b>Instagramストーリー：</b>（あなたの🍪が必要）
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
（最初の3つのストーリーをダウンロード）
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
（アルバムから最初の10つのストーリーをダウンロード）

🟦 <b>VK動画：</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
（ユーザー/グループプロフィールから最初の3本の動画をダウンロード）

⬛️<b>Rutubeチャンネル：</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
（チャンネルから2から4まで動画をダウンロード）

🟪 <b>Twitchクリップ：</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
（チャンネルから最初の3つのクリップをダウンロード）

🟦 <b>Vimeoグループ：</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
（グループから最初の2本の動画をダウンロード）

🟧 <b>Pornhubモデル：</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
（モデルプロフィールから最初の2本の動画をダウンロード）
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
（あなたのプロンプトによる検索結果から最初の3本の動画をダウンロード）

など...
<a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">対応サイト一覧</a>を参照
</blockquote>

<blockquote expandable>🖼 <b>画像 (gallery-dl)</b>

<code>/img URL</code>を使用して、多くのプラットフォームから画像/写真/アルバムをダウンロードします。

<b>例：</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>範囲：</b>
<code>/img 11-20 https://example.com/album</code> — アイテム11..20
<code>/img 11- https://example.com/album</code> — 11から最後まで（またはボットの制限まで）

<i>対応プラットフォームには、vk、2ch、35photo、4chan、500px、ArtStation、Boosty、Civitai、Cyberdrop、DeviantArt、Discord、Facebook、Fansly、Instagram、Pinterest、Reddit、TikTok、Tumblr、Twitter/X、JoyReactorなどが含まれます。完全なリスト：</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">gallery-dl対応サイト</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>動画ダウンロードボット - ヘルプ</b>

📥 <b>基本的な使用方法：</b>
• 任意のリンクを送信 → ボットがダウンロードします
  <i>ボットは自動的にyt-dlpで動画を、gallery-dlで画像をダウンロードしようとします。</i>
• <b>複数のURL：</b> 品質選択モード（<code>/format</code>）では、1つのメッセージで最大<b>10個のURL</b>を送信できます。各URLは新しい行またはスペースで区切ります。
• <code>/audio URL</code> → 音声を抽出
• <code>/link [quality] URL</code> → 直接リンクを取得
• <code>/proxy</code> → すべてのダウンロードでプロキシを有効/無効化
• 動画にテキストで返信 → キャプションを変更

📋 <b>プレイリストと範囲：</b>
• <code>URL*1*5</code> → 最初の5本の動画をダウンロード
• <code>URL*-1*-5</code> → 最後の5本の動画をダウンロード
• <code>/vid 3-7 URL</code> → <code>URL*3*7</code>になります
• <code>/vid -3-7 URL</code> → <code>URL*-3*-7</code>になります

🍪 <b>クッキーとプライベート：</b>
• プライベート動画用に*.txtクッキーをアップロード
• <code>/cookie [service]</code> → クッキーをダウンロード（youtube/tiktok/x/custom）
• <code>/cookie youtube 1</code> → インデックスでソースを選択（1–N）
• <code>/cookies_from_browser</code> → ブラウザから抽出
• <code>/check_cookie</code> → クッキーを検証
• <code>/save_as_cookie</code> → テキストをクッキーとして保存

🧹 <b>クリーンアップ：</b>
• <code>/clean</code> → メディアファイルのみ
• <code>/clean all</code> → すべて
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>設定：</b>
• <code>/settings</code> → 設定メニュー
• <code>/format</code> → 品質とフォーマット
• <code>/split</code> → 動画をパーツに分割
• <code>/mediainfo on/off</code> → メディア情報
• <code>/nsfw on/off</code> → NSFWぼかし
• <code>/tags</code> → 保存されたタグを表示
• <code>/sub on/off</code> → 字幕
• <code>/keyboard</code> → キーボード（OFF/1x3/2x3）

🏷️ <b>タグ：</b>
• URLの後に<code>#tag1#tag2</code>を追加
• タグはキャプションに表示されます
• <code>/tags</code> → すべてのタグを表示

🔗 <b>直接リンク：</b>
• <code>/link URL</code> → 最高品質
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → 特定の品質

⚙️ <b>クイックコマンド：</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → 品質を設定
• <code>/keyboard off/1x3/2x3/full</code> → キーボードレイアウト
• <code>/split 100mb-2000mb</code> → パーツサイズを変更
• <code>/subs off/ru/en auto</code> → 字幕言語
• <code>/list URL</code> → 利用可能なフォーマットのリスト
• <code>/mediainfo on/off</code> → メディア情報のオン/オフ
• <code>/proxy on/off</code> → すべてのダウンロードでプロキシを有効/無効化

📊 <b>情報：</b>
• <code>/usage</code> → ダウンロード履歴
• <code>/search</code> → @vid経由のインライン検索

🖼 <b>画像：</b>
• <code>URL</code> → 画像URLをダウンロード
• <code>/img URL</code> → URLから画像をダウンロード
• <code>/img 11-20 URL</code> → 特定の範囲をダウンロード
• <code>/img 11- URL</code> → 11番目から最後までダウンロード

👨‍💻 <i>開発者：</i> @upekshaip
🤝 <i>貢献者：</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "クッキーを<b><u>cookie.txt</u></b>として保存し、ドキュメントとしてボットに送信してください。\n\n"
        "<b><u>/save_as_cookie</u></b>コマンドでプレーンテキストとしてクッキーを送信することもできます。\n"
        "<b><u>/save_as_cookie</u></b>の使用方法：</b>\n\n"
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
        "<b><u>説明：</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>動画検索</b>

下のボタンを押して、@vid経由でインライン検索を有効にします。

<blockquote>PCでは、任意のチャットで<b>"@vid Your_Search_Query"</b>と入力するだけです。</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 画像ダウンロードコマンド</b>\n\n"
        "使用方法：<code>/img URL</code>\n\n"
        "<b>例：</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>対応プラットフォーム（例）：</b>\n"
        "<blockquote>vk、2ch、35photo、4chan、500px、ArtStation、Boosty、Civitai、Cyberdrop、DeviantArt、Discord、Facebook、Fansly、Instagram、Patreon、Pinterest、Reddit、TikTok、Tumblr、Twitter/X、JoyReactorなど — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">完全なリスト</a></blockquote>"
        "参照："
    )
    
    LINK_HINT_MSG = (
        "品質選択付きで直接動画リンクを取得します。\n\n"
        "使用方法：/link + URL \n\n"
        "（例：/link https://youtu.be/abc123）\n"
        "（例：/link 720 https://youtu.be/abc123）"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>グループにボットを追加</b>

強化された機能とより高い制限を取得するために、私のボットをグループに追加してください！
————————————
📊 <b>現在の無料制限（ボットのDM内）：</b>
<blockquote>•🗑 すべてのファイルが未整理の乱雑なジャンク 👎
• 最大1ファイルサイズ：<b>8 GB</b>
• 最大1ファイル品質：<b>無制限</b>
• 最大1ファイル時間：<b>無制限</b>
• 最大ダウンロード数：<b>無制限</b>
• 1メッセージあたりの最大URL：<b>10</b>（品質選択モードのみ）
• 1回あたりの最大プレイリスト項目：<b>50</b>
• 1回あたりの最大TikTok動画：<b>500</b>
• 1回あたりの最大画像：<b>1000</b>
• URLレート制限：<b>5/分、60/時間、1000/日</b>
• コマンド制限：<b>20/分</b>
• 1ダウンロード最大時間：<b>2時間</b>
• 🔞 NSFWコンテンツは有料です！1⭐️ = $0.02
• 🆓 その他すべてのメディアは完全に無料
• 📝 すべてのコンテンツログとキャッシュをログチャンネルに保存し、再ダウンロード時に即座に再投稿</blockquote>

💬<b>この制限は字幕付き動画のみ：</b>
<blockquote>• 最大動画+字幕時間：<b>1.5時間</b>
• 最大動画+字幕ファイルサイズ：<b>500 MB</b>
• 最大動画+字幕品質：<b>720p</b></blockquote>
————————————
🚀 <b>有料グループ特典（2️⃣倍の制限）：</b>
<blockquote>•  🗂 トピック別に整理された整然としたメディア保管庫 👍
•  📁 ボットは呼び出したトピックで返信
•  📌 ダウンロード進捗を含むステータスメッセージを自動ピン留め
•  🖼 /imgコマンドはメディアを10項目のアルバムとしてダウンロード
• 最大1ファイルサイズ：<b>16 GB</b> ⬆️
• 1メッセージあたりの最大URL：<b>20</b> ⬆️（品質選択モードのみ）
• 1回あたりの最大プレイリスト項目：<b>100</b> ⬆️
• 1回あたりの最大TikTok動画：1000 ⬆️
• 1回あたりの最大画像：2000 ⬆️
• URLレート制限：<b>10/分、120/時間、2000/日</b> ⬆️
• コマンド制限：<b>40/分</b> ⬆️
• 1ダウンロード最大時間：<b>4時間</b> ⬆️
• 🔞 NSFWコンテンツ：完全なメタデータ付きで無料 🆓
• 📢 グループでは私のチャンネルに登録する必要はありません
• 👥 すべてのグループメンバーが有料機能にアクセスできます！
• 🗒 ログチャンネルへのログ/キャッシュなし！グループ設定でコピー/再投稿を拒否できます</blockquote>

💬 <b>字幕付き動画の2️⃣倍の制限：</b>
<blockquote>• 最大動画+字幕時間：<b>3時間</b> ⬆️
• 最大動画+字幕ファイルサイズ：<b>1000 MB</b> ⬆️
• 最大動画+字幕品質：<b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>価格とセットアップ：</b>
<blockquote>• 価格：グループ内の1ボットあたり<b>$5/月</b>
• セットアップ：@iilililiiillliiliililliilliliiilに連絡
• 支払い：💎TONまたはその他の方法💲
• サポート：完全な技術サポートを含む</blockquote>
————————————
私のボットをグループに追加して、無料の🔞<b>NSFW</b>のブロックを解除し、すべての制限を2倍（x2️⃣）にできます。
グループで私のボットを使用できるようにしたい場合は、@iilililiiillliiliililliilliliiilに連絡してください
————————————
💡<b>ヒント：</b> <blockquote>友達と任意の金額（例えば100人）でお金を出し合い、グループ全体で1回購入すると、そのグループ内のすべてのボット機能に<b>0.05$</b>だけで全グループメンバーが完全な無制限アクセスを持ちます</blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFWモード：ON✅</b>

• NSFWコンテンツはぼかしなしで表示されます。
• ネタバレはNSFWメディアに適用されません。
• コンテンツはすぐに表示されます

<i>ぼかしを有効にするには /nsfw off を使用</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFWモード：OFF</b>

⚠️ <b>ぼかしが有効</b>
• NSFWコンテンツはネタバレの下に隠されます
• 表示するには、メディアをクリックする必要があります
• ネタバレがNSFWメディアに適用されます。

<i>ぼかしを無効にするには /nsfw on を使用</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>無効なパラメータ</b>

使用：
• <code>/nsfw on</code> - ぼかしを無効化
• <code>/nsfw off</code> - ぼかしを有効化
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>キャッシュを確認中...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 処理中..."
    DOWNLOADING_MSG = "📥 <b>メディアをダウンロード中...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>画像をダウンロード中...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>ダウンロード完了</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "ダウンロード済み："
    SENT_STATUS_MSG = "送信済み："
    PENDING_TO_SEND_STATUS_MSG = "送信待ち："
    TITLE_LABEL_MSG = "タイトル："
    MEDIA_COUNT_LABEL_MSG = "メディア数："
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "ダウンロード完了、音声を処理中..."
    VIDEO_PROCESSING_MSG = "📽 動画を処理中..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>キャッシュから送信</b>\n\n送信されたアルバム：<b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ 動画をキャッシュから正常に送信しました。"
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ プレイリストの動画をキャッシュから送信しました（{cached}/{total}ファイル）。"
    CACHE_PARTIAL_MSG = "📥 {cached}/{total}本の動画をキャッシュから送信、不足分をダウンロード中..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ キャッシュから送信：{cached}\n🔄 ダウンロードを続行中..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 メディアを分析できませんでした。最大許可範囲（1-{fallback_limit}）で続行します..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 メディア数を決定できませんでした。最大許可範囲（1-{total_limit}）で続行します..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 メディアの総数を決定できませんでした。指定された範囲{start}-{end}で続行します..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>無効なURL</b>\n\nhttp://またはhttps://で始まる有効なURLを入力してください"

    ERROR_OCCURRED_MSG = "❌ <b>エラーが発生しました</b>\n\n<code>{url}</code>\n\nエラー：{error}"

    ERROR_SENDING_VIDEO_MSG = "❌ 動画の送信エラー：{error}"
    ERROR_UNKNOWN_MSG = "❌ 不明なエラー：{error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ 動画をダウンロードするためのディスク容量が不足しています。"
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ ファイルサイズが{limit}GBの制限を超えています。許可されたサイズ内でより小さなファイルを選択してください。"

    ERROR_GETTING_LINK_MSG = "❌ <b>リンク取得エラー：</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegramがメッセージ送信を制限しています。\n⏳ お待ちください：{time}\nタイマーを更新するには、URLを再度2回送信してください。"
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegramがメッセージ送信を制限しています。\n⏳ お待ちください：\nタイマーを更新するには、URLを再度2回送信してください。"
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ 字幕のダウンロードに失敗しました"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>直接ストリームリンク</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>タイトル：</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>時間：</b> {duration}秒\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ エラー：元のメッセージが見つかりませんでした。"

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ タグ #{tag} に禁止文字が含まれています。文字、数字、_のみ使用できます。\n使用例：{example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ プレイリストの動画を送信しました：{sent}/{total}ファイル。"
    PLAYLIST_CACHE_SENT_MSG = "✅ キャッシュから送信しました：{cached}/{total}ファイル。"
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ ストリームリンクの取得に失敗しました"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "クッキーをダウンロードするブラウザを選択："
    SELECT_BROWSER_NO_BROWSERS_MSG = "このシステムでブラウザが見つかりませんでした。リモートURLからクッキーをダウンロードするか、ブラウザのステータスを監視できます："
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>ブラウザを開く</b> - ミニアプリでブラウザのステータスを監視"
    BROWSER_OPEN_BUTTON_MSG = "🌐 ブラウザを開く"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 リモートURLからダウンロード"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTubeクッキーファイルをフォールバック経由でダウンロードし、cookie.txtとして保存しました"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ サポートされているブラウザが見つからず、COOKIE_URLが設定されていません。/cookieを使用するか、cookie.txtをアップロードしてください。"
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ フォールバックCOOKIE_URLは.txtファイルを指す必要があります。"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ フォールバッククッキーファイルが大きすぎます（>100KB）。"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ フォールバッククッキーソースが利用できません（ステータス{status}）。/cookieを試すか、cookie.txtをアップロードしてください。"
    COOKIE_FALLBACK_ERROR_MSG = "❌ フォールバッククッキーのダウンロードエラー。/cookieを試すか、cookie.txtをアップロードしてください。"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ フォールバッククッキーのダウンロード中に予期しないエラーが発生しました。"
    BTN_CLOSE = "🔚閉じる"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ 無効なブール値"
    ARGS_CLOSED_MSG = "閉じました"
    ARGS_ALL_RESET_MSG = "✅ すべての引数がリセットされました"
    ARGS_RESET_ERROR_MSG = "❌ 引数のリセット中にエラーが発生しました"
    ARGS_INVALID_PARAM_MSG = "❌ 無効なパラメータ"
    ARGS_BOOL_SET_MSG = "{value}に設定"
    ARGS_BOOL_ALREADY_SET_MSG = "既に{value}に設定されています"
    ARGS_INVALID_SELECT_MSG = "❌ 無効な選択値"
    ARGS_VALUE_SET_MSG = "{value}に設定"
    ARGS_VALUE_ALREADY_SET_MSG = "既に{value}に設定されています"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>現在の値：</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>例：</b>\n• <code>default</code> - デフォルトのXFF戦略を使用\n• <code>never</code> - XFFヘッダーを使用しない\n• <code>US</code> - 米国の国コード\n• <code>GB</code> - 英国の国コード\n• <code>DE</code> - ドイツの国コード\n• <code>FR</code> - フランスの国コード\n• <code>JP</code> - 日本の国コード\n• <code>192.168.1.0/24</code> - IPブロック（CIDR）\n• <code>10.0.0.0/8</code> - プライベートIP範囲\n• <code>203.0.113.0/24</code> - パブリックIPブロック\n\n"
    ARGS_XFF_NOTE_MSG = "<b>注意：</b> これは--geo-bypassオプションを置き換えます。2文字の国コードまたはCIDR表記のIPブロックを使用してください。\n\n"
    ARGS_EXAMPLE_MSG = "<b>例：</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "新しい値を送信してください。"
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>範囲：</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "数値を送信してください。"
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>例：</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>注意：</b> これらのヘッダーは既存のRefererおよびUser-Agentヘッダーに追加されます。\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 現在のyt-dlp引数：</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>ブール</b> - True/Falseスイッチ\n• 📋 <b>選択</b> - オプションから選択\n• 🔢 <b>数値</b> - 数値入力\n• 📝🔧 <b>テキスト</b> - テキスト/JSON入力</blockquote>\n\nこれらの設定はすべてのダウンロードに適用されます。"
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "IPv6接続を強制",
        "force_ipv4": "IPv4接続を強制", 
        "no_live_from_start": "開始からライブストリームをダウンロードしない",
        "live_from_start": "開始からライブストリームをダウンロード",
        "no_check_certificates": "HTTPS証明書の検証を抑制",
        "check_certificate": "SSL証明書を確認",
        "no_playlist": "単一の動画のみダウンロード、プレイリストではない",
        "embed_metadata": "動画ファイルにメタデータを埋め込む",
        "embed_thumbnail": "動画ファイルにサムネイルを埋め込む",
        "write_thumbnail": "サムネイルをファイルに書き込む",
        "ignore_errors": "ダウンロードエラーを無視して続行",
        "legacy_server_connect": "レガシーサーバー接続を許可",
        "concurrent_fragments": "同時にダウンロードするフラグメント数",
        "xff": "X-Forwarded-Forヘッダー戦略",
        "user_agent": "User-Agentヘッダー",
        "impersonate": "ブラウザの偽装",
        "referer": "Refererヘッダー",
        "geo_bypass": "地理的制限をバイパス",
        "hls_use_mpegts": "HLSにMPEG-TSを使用",
        "no_part": ".partファイルを使用しない",
        "no_continue": "部分的なダウンロードを再開しない",
        "audio_format": "音声フォーマット",
        "video_format": "動画フォーマット",
        "merge_output_format": "マージ出力フォーマット",
        "send_as_file": "ファイルとして送信",
        "username": "ユーザー名",
        "password": "パスワード",
        "twofactor": "二要素認証コード",
        "min_filesize": "最小ファイルサイズ（MB）",
        "max_filesize": "最大ファイルサイズ（MB）",
        "playlist_items": "プレイリスト項目",
        "date": "日付",
        "datebefore": "日付より前",
        "dateafter": "日付より後",
        "http_headers": "HTTPヘッダー",
        "sleep_interval": "スリープ間隔",
        "max_sleep_interval": "最大スリープ間隔",
        "retries": "再試行回数",
        "http_chunk_size": "HTTPチャンクサイズ",
        "sleep_subtitles": "字幕のスリープ"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp引数設定</b>\n\n<blockquote>📋 <b>グループ：</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp引数設定</b>\n\n"
        "<blockquote>📋 <b>グループ：</b>\n"
        "• ✅/❌ <b>ブール</b> - True/Falseスイッチ\n"
        "• 📋 <b>選択</b> - オプションから選択\n"
        "• 🔢 <b>数値</b> - 数値入力\n"
        "• 📝🔧 <b>テキスト</b> - テキスト/JSON入力</blockquote>\n\n"
        "これらの設定はすべてのダウンロードに適用されます。"
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ お待ちください..."
    ERROR_OCCURRED_SHORT_MSG = "❌ エラーが発生しました"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ 非アクティブのため入力モードが自動的に閉じられました（5分）。"
    ARGS_INPUT_DANGEROUS_MSG = "❌ 入力に潜在的に危険なコンテンツが含まれています：{pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ 入力が長すぎます（最大1000文字）"
    ARGS_INVALID_URL_MSG = "❌ 無効なURL形式。http://またはhttps://で始まる必要があります"
    ARGS_INVALID_JSON_MSG = "❌ 無効なJSON形式"
    ARGS_NUMBER_RANGE_MSG = "❌ 数値は{min_val}から{max_val}の間である必要があります"
    ARGS_INVALID_NUMBER_MSG = "❌ 無効な数値形式"
    ARGS_DATE_FORMAT_MSG = "❌ 日付はYYYYMMDD形式である必要があります（例：20230930）"
    ARGS_YEAR_RANGE_MSG = "❌ 年は1900から2100の間である必要があります"
    ARGS_MONTH_RANGE_MSG = "❌ 月は01から12の間である必要があります"
    ARGS_DAY_RANGE_MSG = "❌ 日は01から31の間である必要があります"
    ARGS_INVALID_DATE_MSG = "❌ 無効な日付形式"
    ARGS_INVALID_XFF_MSG = "❌ XFFは'default'、'never'、国コード（例：US）、またはIPブロック（例：192.168.1.0/24）である必要があります"
    ARGS_NO_CUSTOM_MSG = "カスタム引数が設定されていません。すべてのパラメータはデフォルト値を使用します。"
    ARGS_RESET_SUCCESS_MSG = "✅ すべての引数がデフォルトにリセットされました。"
    ARGS_TEXT_TOO_LONG_MSG = "❌ テキストが長すぎます。最大500文字。"
    ARGS_ERROR_PROCESSING_MSG = "❌ 入力の処理中にエラーが発生しました。もう一度お試しください。"
    ARGS_BOOL_INPUT_MSG = "❌ ファイルとして送信オプションには'True'または'False'を入力してください。"
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ 有効な数値を入力してください。"
    ARGS_BOOL_VALUE_REQUEST_MSG = "このオプションを有効/無効にするには、<code>True</code>または<code>False</code>を送信してください。"
    ARGS_JSON_VALUE_REQUEST_MSG = "有効なJSONを送信してください。"
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "まだタグがありません。"
    TAGS_MESSAGE_CLOSED_MSG = "タグメッセージを閉じました。"
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ 字幕が無効になり、常に尋ねるモードがオフになりました。"
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ 字幕の常に尋ねるモードが有効になりました。"
    SUBS_LANGUAGE_SET_MSG = "✅ 字幕言語が設定されました：{flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️警告：高いCPU負荷により、この機能は非常に遅く（ほぼリアルタイム）、以下の制限があります：\n"
        "- 最大品質720p\n"
        "- 最大時間1.5時間\n"
        "- 最大動画サイズ500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>クイックコマンド：</b>\n"
        "• <code>/subs off</code> - 字幕を無効化\n"
        "• <code>/subs on</code> - 常に尋ねるモードを有効化\n"
        "• <code>/subs ru</code> - 言語を設定\n"
        "• <code>/subs ru auto</code> - AUTO/TRANS付きで言語を設定"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 字幕は無効です"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} 選択された言語：{name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 字幕をダウンロード中..."
    SUBS_DISABLED_ERROR_MSG = "❌ 字幕は無効です。/subsを使用して設定してください。"
    SUBS_YOUTUBE_ONLY_MSG = "❌ 字幕のダウンロードはYouTubeのみサポートされています。"
    SUBS_CAPTION_MSG = (
        "<b>💬 字幕</b>\n\n"
        "<b>動画：</b> {title}\n"
        "<b>言語：</b> {lang}\n"
        "<b>タイプ：</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 字幕SRTファイルをユーザーに送信しました。"
    SUBS_ERROR_PROCESSING_MSG = "❌ 字幕ファイルの処理エラー。"
    SUBS_ERROR_DOWNLOAD_MSG = "❌ 字幕のダウンロードに失敗しました。"
    SUBS_ERROR_MSG = "❌ 字幕のダウンロードエラー：{error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ 分割パートサイズが設定されました：{size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **無効なサイズ！**\n\n"
        "**有効な範囲：** 100MBから2GB\n\n"
        "**有効な形式：**\n"
        "• `100mb`から`2000mb`（メガバイト）\n"
        "• `0.1gb`から`2gb`（ギガバイト）\n\n"
        "**例：**\n"
        "• `/split 100mb` - 100メガバイト\n"
        "• `/split 500mb` - 500メガバイト\n"
        "• `/split 1.5gb` - 1.5ギガバイト\n"
        "• `/split 2gb` - 2ギガバイト\n"
        "• `/split 2000mb` - 2000メガバイト（2GB）\n\n"
        "**プリセット：**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **動画分割の最大パートサイズを選択：**\n\n"
        "**範囲：** 100MBから2GB\n\n"
        "**クイックコマンド：**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**例：** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "メニューを閉じました。"
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>ボット設定</b>\n\nカテゴリを選択："
    SETTINGS_MENU_CLOSED_MSG = "メニューを閉じました。"
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 クリーンオプション</b>\n\nクリーンするものを選択："
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 クッキー</b>\n\nアクションを選択："
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 メディア</b>\n\nアクションを選択："
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 情報</b>\n\nアクションを選択："
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ その他のコマンド</b>\n\nアクションを選択："
    SETTINGS_COMMAND_EXECUTED_MSG = "コマンドが実行されました。"
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ フラッド制限。後でもう一度お試しください。"
    SETTINGS_HINT_SENT_MSG = "ヒントを送信しました。"
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "検索ヘルパーを開きました。"
    SETTINGS_UNKNOWN_COMMAND_MSG = "不明なコマンド。"
    SETTINGS_HINT_CLOSED_MSG = "ヒントを閉じました。"
    SETTINGS_HELP_SENT_MSG = "ユーザーにヘルプテキストを送信"
    SETTINGS_MENU_OPENED_MSG = "/settingsメニューを開きました"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 検索ヘルパーを閉じました"
    SEARCH_CLOSED_MSG = "閉じる"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ プロキシ{status}。"
    PROXY_ERROR_SAVING_MSG = "❌ プロキシ設定の保存エラー。"
    PROXY_MENU_TEXT_MSG = "すべてのyt-dlp操作にプロキシサーバーを使用することを有効または無効にしますか？"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "すべてのyt-dlp操作にプロキシサーバー（{count}個利用可能）を使用することを有効または無効にしますか？\n\n有効にすると、プロキシは{method}メソッドを使用して選択されます。"
    PROXY_MENU_CLOSED_MSG = "メニューを閉じました。"
    PROXY_ENABLED_CONFIRM_MSG = "✅ プロキシが有効になりました。すべてのyt-dlp操作でプロキシが使用されます。"
    PROXY_ENABLED_MULTIPLE_MSG = "✅ プロキシが有効になりました。すべてのyt-dlp操作で{count}個のプロキシサーバーが{method}選択メソッドで使用されます。"
    PROXY_DISABLED_MSG = "❌ プロキシが無効になりました。"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ プロキシ設定の保存エラー。"
    PROXY_ENABLED_CALLBACK_MSG = "プロキシが有効になりました。"
    PROXY_DISABLED_CALLBACK_MSG = "プロキシが無効になりました。"
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ 前のダウンロードが完了するまでお待ちください"
    AUDIO_HELP_MSG = (
        "<b>🎧 音声ダウンロードコマンド</b>\n\n"
        "使用方法：<code>/audio URL</code>\n\n"
        "<b>例：</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "参照：/vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "音声ヒントを閉じました。"
    PLAYLIST_HELP_CLOSED_MSG = "プレイリストヘルプを閉じました。"
    USERLOGS_CLOSED_MSG = "ログメッセージを閉じました。"
    HELP_CLOSED_MSG = "ヘルプを閉じました。"
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFWぼかし設定</b>\n\nNSFWコンテンツは<b>{status}</b>です。\n\nNSFWコンテンツをぼかすかどうかを選択："
    NSFW_MENU_CLOSED_MSG = "メニューを閉じました。"
    NSFW_BLUR_DISABLED_MSG = "NSFWぼかしが無効になりました。"
    NSFW_BLUR_ENABLED_MSG = "NSFWぼかしが有効になりました。"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFWぼかしが無効になりました。"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFWぼかしが有効になりました。"
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}。"
    MEDIAINFO_MENU_TITLE_MSG = "ダウンロードしたファイルのMediaInfo送信を有効または無効にしますか？"
    MEDIAINFO_MENU_CLOSED_MSG = "メニューを閉じました。"
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfoが有効になりました。ダウンロード後、ファイル情報が送信されます。"
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfoが無効になりました。"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfoが有効になりました。"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfoが無効になりました。"
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 利用可能なフォーマット一覧</b>\n\n"
        "URLの利用可能な動画/音声フォーマットを取得します。\n\n"
        "<b>使用方法：</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>例：</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 フォーマットIDの使用方法：</b>\n"
        "リストを取得した後、特定のフォーマットIDを使用：\n"
        "• <code>/format id 401</code> - フォーマット401をダウンロード\n"
        "• <code>/format id401</code> - 上記と同じ\n"
        "• <code>/format id140 audio</code> - フォーマット140をMP3音声としてダウンロード\n\n"
        "このコマンドはダウンロード可能なすべての利用可能なフォーマットを表示します。"
    )
    LIST_PROCESSING_MSG = "🔄 利用可能なフォーマットを取得中..."
    LIST_INVALID_URL_MSG = "❌ http://またはhttps://で始まる有効なURLを入力してください"
    LIST_CAPTION_MSG = (
        "📃 利用可能なフォーマット：\n<code>{url}</code>\n\n"
        "💡 <b>フォーマットの設定方法：</b>\n"
        "• <code>/format id 134</code> - 特定のフォーマットIDをダウンロード\n"
        "• <code>/format 720p</code> - 品質でダウンロード\n"
        "• <code>/format best</code> - 最高品質をダウンロード\n"
        "• <code>/format ask</code> - 常に品質を尋ねる\n\n"
        "{audio_note}\n"
        "📋 上記のリストからフォーマットIDを使用"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>音声のみのフォーマット：</b> {formats}\n"
        "• <code>/format id 140 audio</code> - フォーマット140をMP3音声としてダウンロード\n"
        "• <code>/format id140 audio</code> - 上記と同じ\n"
        "これらはMP3音声ファイルとしてダウンロードされます。\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ フォーマットファイルの送信エラー：{error}"
    LIST_ERROR_GETTING_MSG = "❌ フォーマットの取得に失敗しました：\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ コマンドの処理中にエラーが発生しました"
    LIST_ERROR_CALLBACK_MSG = "エラーが発生しました"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 フォーマットIDの使用方法：\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "リストを取得した後、特定のフォーマットIDを使用してください：\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - フォーマット401をダウンロード\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - 上記と同じ\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - フォーマット140をMP3オーディオとしてダウンロード\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - 上記と同じ\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 オーディオのみのフォーマットが検出されました：{formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "これらのフォーマットはMP3オーディオファイルとしてダウンロードされます。\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>ビデオのみのフォーマット：</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 上記のリストからフォーマットIDを使用してください"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>使用方法：</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>例：</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - 最高品質\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p以下\n"
        "• /link 720p https://youtube.com/watch?v=... - 上記と同じ\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K以下\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K以下"
        "</blockquote>\n\n"
        "<b>品質：</b> 1から10000まで（例：144、240、720、1080）"
    )
    LINK_INVALID_URL_MSG = "❌ 有効なURLを入力してください"
    LINK_PROCESSING_MSG = "🔗 直接リンクを取得中..."
    LINK_DURATION_MSG = "⏱ <b>時間：</b> {duration}秒\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>動画ストリーム：</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>音声ストリーム：</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **キーボード設定が更新されました！**\n\n新しい設定：**{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **無効な引数！**\n\n"
        "有効なオプション：`off`、`1x3`、`2x3`、`full`\n\n"
        "例：`/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **キーボード設定**\n\n"
        "現在：**{current}**\n\n"
        "オプションを選択：\n\n"
        "または使用：`/keyboard off`、`/keyboard 1x3`、`/keyboard 2x3`、`/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 キーボードが有効になりました！"
    KEYBOARD_HIDDEN_MSG = "⌨️ キーボードが非表示になりました"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3キーボードが有効になりました！"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3キーボードが有効になりました！"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 絵文字キーボードが有効になりました！"
    KEYBOARD_ERROR_APPLYING_MSG = "キーボード設定{setting}の適用エラー：{error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ フォーマットが設定されました：常に尋ねる。URLを送信するたびに品質を尋ねられます。"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ フォーマットが設定されました：常に尋ねる。URLを送信するたびに品質を尋ねられます。"
    FORMAT_BEST_UPDATED_MSG = "✅ フォーマットが最高品質（AVC+MP4優先）に更新されました：\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ フォーマットがID {id}に更新されました：\n{format}\n\n💡 <b>注意：</b> これが音声のみのフォーマットの場合、MP3音声ファイルとしてダウンロードされます。"
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ フォーマットがID {id}（音声のみ）に更新されました：\n{format}\n\n💡 これはMP3音声ファイルとしてダウンロードされます。"
    FORMAT_QUALITY_UPDATED_MSG = "✅ フォーマットが品質{quality}に更新されました：\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ フォーマットが更新されました：\n{format}"
    FORMAT_MENU_MSG = (
        "フォーマットオプションを選択するか、カスタムを送信：\n"
        "• <code>/format &lt;format_string&gt;</code> - カスタムフォーマット\n"
        "• <code>/format 720</code> - 720p品質\n"
        "• <code>/format 4k</code> - 4K品質\n"
        "• <code>/format 8k</code> - 8K品質\n"
        "• <code>/format id 401</code> - 特定のフォーマットID\n"
        "• <code>/format ask</code> - 常にメニューを表示\n"
        "• <code>/format best</code> - bv+ba/最高品質"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "カスタムフォーマットを使用するには、次の形式でコマンドを送信：\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "<code>bestvideo+bestaudio/best</code>を希望のフォーマット文字列に置き換えてください。"
    )
    FORMAT_RESOLUTION_MENU_MSG = "希望の解像度とコーデックを選択："
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ フォーマットが設定されました：常に尋ねる。URLを送信するたびに品質を尋ねられます。"
    FORMAT_UPDATED_MSG = "✅ フォーマットが更新されました：\n{format}"
    FORMAT_SAVED_MSG = "✅ フォーマットが保存されました。"
    FORMAT_CHOICE_UPDATED_MSG = "✅ フォーマット選択が更新されました。"
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "カスタムフォーマットメニューを閉じました"
    FORMAT_CODEC_SET_MSG = "✅ コーデックが{codec}に設定されました"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Browser choice updated."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ アクセスが拒否されました。管理者のみ。"
    ACCESS_DENIED_ADMIN = "❌ アクセスが拒否されました。管理者のみ。"
    WELCOME_MASTER = "マスター、ようこそ 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ 申し訳ございません... ダウンロード中にエラーが発生しました。"
    SIZE_LIMIT_EXCEEDED = "❌ ファイルサイズが{max_size_gb}GBの制限を超えています。許可されたサイズ内でより小さなファイルを選択してください。"
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ スクリプトが見つかりません：{script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ {script_path}を使用して新しいFirebaseダンプをダウンロード中..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebaseキャッシュが正常に再読み込みされました！"
    ADMIN_CACHE_FAILED_MSG = "❌ Firebaseキャッシュの再読み込みに失敗しました。{cache_file}が存在するか確認してください。"
    ADMIN_ERROR_RELOADING_MSG = "❌ キャッシュの再読み込みエラー：{error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ {script_path}の実行エラー：\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ プロモメッセージが他のすべてのユーザーに送信されました</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ プロモメッセージを送信できません。メッセージに返信してみてください\nまたはエラーが発生しました</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ ユーザーはまだコンテンツをダウンロードしていません...</b> ログに存在しません"
    ADMIN_INVALID_COMMAND_MSG = "❌ 無効なコマンド"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ <code>{{path}}</code>のキャッシュにデータが見つかりません"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ キューは空です — まだ誰もチャンネルを離れていません。"
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>禁止キュー</b>\n保留中：{total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username}（離脱：{last_left}）"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… および{extra}人の追加ユーザー。"
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "/block_user show • all • auto • 10s を使用"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ キューからユーザーをブロック：{count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ 自動ブロックが有効になりました：新しい離脱者は即座に禁止されます。"
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ 自動ブロックが無効になりました。"
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ スケジュールされた自動ブロックウィンドウが{interval}ごとに設定されました。"
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 過去{hours}時間（2日間）のチャンネル活動ログ。"
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 過去{hours}時間（2日間）：参加{joined}、離脱{left}。"
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ 過去{hours}時間（2日間）の活動はありません。"
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "合計：🟢 {joined}参加、🔴 {left}離脱。"
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ チャンネル活動ログにアクセスできません。ボットは管理者ログを読み取れません。この機能を有効にするには、設定でCHANNEL_GUARD_SESSION_STRINGにユーザーセッションを提供してください。"
    BAN_TIME_USAGE_MSG = "❌ 使用方法：{command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ 10s、6m、5h、4d、3w、2M、1yなどの形式を使用してください。"
    BAN_TIME_SET_MSG = "🕒 チャンネルログスキャン間隔が{interval}に設定されました。"
    BAN_TIME_REPORT_MSG = (
        "🛡️ チャンネルスキャンレポート\n"
        "実行時刻：{run_ts}\n"
        "間隔：{interval}\n"
        "新しい離脱者：{new_leavers}\n"
        "自動禁止：{auto_banned}\n"
        "保留中：{pending}\n"
        "最後のevent_id：{last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ 使用方法：/block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 管理者は管理者を削除できません"
    ADMIN_USER_BLOCKED_MSG = "ユーザーがブロックされました 🔒❌\n \nID：<code>{user_id}</code>\nブロック日：{date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code>は既にブロックされています ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 申し訳ございません！あなたは管理者ではありません"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ 使用方法：/unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "ユーザーのブロックが解除されました 🔓✅\n \nID：<code>{user_id}</code>\nブロック解除日：{date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code>は既にブロック解除されています ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ ブロック解除されたユーザー：{count}\n⏱ タイムスタンプ：{date}"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>ボット稼働時間 -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ キャッシュをクリアするURLを入力してください。\n使用方法：<code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ 有効なURLを入力してください。\n使用方法：<code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ URLのキャッシュが正常にクリアされました：\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ このリンクのキャッシュが見つかりません。"
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ キャッシュのクリアエラー：{error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ アクセスが拒否されました。管理者のみ。"
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ ポルノリスト更新スクリプトを実行中：{script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ スクリプトが正常に完了しました！"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ スクリプトが正常に完了しました！\n\n出力：\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ スクリプトがリターンコード{returncode}で失敗しました：\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ スクリプトの実行エラー：{error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ ポルノおよびドメイン関連のキャッシュを再読み込み中..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ ポルノキャッシュが正常に再読み込みされました！\n\n"
        "📊 現在のキャッシュステータス：\n"
        "• ポルノドメイン：{porn_domains}\n"
        "• ポルノキーワード：{porn_keywords}\n"
        "• サポートされているサイト：{supported_sites}\n"
        "• ホワイトリスト：{whitelist}\n"
        "• グレーリスト：{greylist}\n"
        "• ブラックリスト：{black_list}\n"
        "• ホワイトキーワード：{white_keywords}\n"
        "• プロキシドメイン：{proxy_domains}\n"
        "• プロキシ2ドメイン：{proxy_2_domains}\n"
        "• クリーンクエリ：{clean_query}\n"
        "• クッキーなしドメイン：{no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ ポルノキャッシュの再読み込みエラー：{error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ チェックするURLを入力してください。\n使用方法：<code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ 有効なURLを入力してください。\n使用方法：<code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 NSFWコンテンツのURLをチェック中...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>ポルノチェック結果</b>\n\n"
        "<b>URL：</b> <code>{url}</code>\n"
        "<b>ステータス：</b> <b>{status_text}</b>\n\n"
        "<b>説明：</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ URLのチェックエラー：{error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "クッキーがクリーンされました。"
    CLEAN_LOGS_CLEANED_MSG = "ログがクリーンされました。"
    CLEAN_TAGS_CLEANED_MSG = "タグがクリーンされました。"
    CLEAN_FORMAT_CLEANED_MSG = "フォーマットがクリーンされました。"
    CLEAN_SPLIT_CLEANED_MSG = "分割がクリーンされました。"
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfoがクリーンされました。"
    CLEAN_SUBS_CLEANED_MSG = "字幕設定がクリーンされました。"
    CLEAN_KEYBOARD_CLEANED_MSG = "キーボード設定がクリーンされました。"
    CLEAN_ARGS_CLEANED_MSG = "引数設定がクリーンされました。"
    CLEAN_NSFW_CLEANED_MSG = "NSFW設定がクリーンされました。"
    CLEAN_PROXY_CLEANED_MSG = "プロキシ設定がクリーンされました。"
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "フラッド待機設定がクリーンされました。"
    CLEAN_ALL_CLEANED_MSG = "すべてのファイルがクリーンされました。"
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 クッキー</b>\n\nアクションを選択："
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ クッキーファイルが保存されました"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ 非YouTubeクッキーの検証をスキップしました"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ クッキーファイルは存在しますが、形式が正しくありません"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ クッキーファイルが見つかりません。"
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 YouTubeクッキーテストを開始しています...\n\nクッキーをチェックして検証する間、お待ちください。"
    COOKIES_YOUTUBE_WORKING_MSG = "✅ 既存のYouTubeクッキーが正常に機能しています！\n\n新しいものをダウンロードする必要はありません。"
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ 既存のYouTubeクッキーが期限切れまたは無効です。\n\n🔄 新しいクッキーをダウンロード中..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service}クッキーソースが設定されていません！"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service}クッキーソースは.txtファイルである必要があります！"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ 範囲制限を超えました：{range_count}ファイルがリクエストされました（最大{max_img_files}）。\n\n利用可能な最大ファイルをダウンロードするには、次のコマンドのいずれかを使用：\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚閉じる"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ メディア制限を超えました：{count}ファイルがリクエストされました（最大{max_count}）。\n\n利用可能な最大ファイルをダウンロードするには、次のコマンドのいずれかを使用：\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 リンクから<b>{count}</b>個のメディア項目が見つかりました"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "ダウンロード範囲を選択："
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "ブラウザの偽装"
    ARGS_REFERER_DESC_MSG = "Refererヘッダー"
    ARGS_USER_AGENT_DESC_MSG = "User-Agentヘッダー"
    ARGS_GEO_BYPASS_DESC_MSG = "地理的制限をバイパス"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "SSL証明書を確認"
    ARGS_LIVE_FROM_START_DESC_MSG = "ライブストリームを最初からダウンロード"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "ライブストリームを最初からダウンロードしない"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "HLS動画にMPEG-TSコンテナを使用"
    ARGS_NO_PLAYLIST_DESC_MSG = "プレイリストではなく単一の動画のみダウンロード"
    ARGS_NO_PART_DESC_MSG = ".partファイルを使用しない"
    ARGS_NO_CONTINUE_DESC_MSG = "部分的なダウンロードを再開しない"
    ARGS_AUDIO_FORMAT_DESC_MSG = "抽出用のオーディオフォーマット"
    ARGS_EMBED_METADATA_DESC_MSG = "動画ファイルにメタデータを埋め込む"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "動画ファイルにサムネイルを埋め込む"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "サムネイルをファイルに書き込む"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "同時にダウンロードするフラグメント数"
    ARGS_FORCE_IPV4_DESC_MSG = "IPv4接続を強制"
    ARGS_FORCE_IPV6_DESC_MSG = "IPv6接続を強制"
    ARGS_XFF_DESC_MSG = "X-Forwarded-Forヘッダー戦略"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTPチャンクサイズ（バイト）"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "字幕ダウンロード前の待機（秒）"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "レガシーサーバー接続を許可"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "HTTPS証明書の検証を抑制"
    ARGS_USERNAME_DESC_MSG = "アカウントのユーザー名"
    ARGS_PASSWORD_DESC_MSG = "アカウントのパスワード"
    ARGS_TWOFACTOR_DESC_MSG = "二要素認証コード"
    ARGS_IGNORE_ERRORS_DESC_MSG = "ダウンロードエラーを無視して続行"
    ARGS_MIN_FILESIZE_DESC_MSG = "最小ファイルサイズ（MB）"
    ARGS_MAX_FILESIZE_DESC_MSG = "最大ファイルサイズ（MB）"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "ダウンロードするプレイリスト項目（例：1,3,5 または 1-5）"
    ARGS_DATE_DESC_MSG = "この日付にアップロードされた動画をダウンロード（YYYYMMDD）"
    ARGS_DATEBEFORE_DESC_MSG = "この日付より前にアップロードされた動画をダウンロード（YYYYMMDD）"
    ARGS_DATEAFTER_DESC_MSG = "この日付より後にアップロードされた動画をダウンロード（YYYYMMDD）"
    ARGS_HTTP_HEADERS_DESC_MSG = "カスタムHTTPヘッダー（JSON）"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "リクエスト間の待機間隔（秒）"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "最大待機間隔（秒）"
    ARGS_RETRIES_DESC_MSG = "再試行回数"
    ARGS_VIDEO_FORMAT_DESC_MSG = "動画コンテナフォーマット"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "マージ用の出力コンテナフォーマット"
    ARGS_SEND_AS_FILE_DESC_MSG = "すべてのメディアをメディアではなくドキュメントとして送信"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "偽装"
    ARGS_REFERER_SHORT_MSG = "Referer"
    ARGS_GEO_BYPASS_SHORT_MSG = "Geoバイパス"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "証明書確認"
    ARGS_LIVE_FROM_START_SHORT_MSG = "ライブ開始"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "ライブ開始なし"
    ARGS_USER_AGENT_SHORT_MSG = "User Agent"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "プレイリストなし"
    ARGS_NO_PART_SHORT_MSG = "パートなし"
    ARGS_NO_CONTINUE_SHORT_MSG = "続行なし"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "オーディオフォーマット"
    ARGS_EMBED_METADATA_SHORT_MSG = "メタ埋め込み"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "サムネ埋め込み"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "サムネ書き込み"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "同時"
    ARGS_FORCE_IPV4_SHORT_MSG = "IPv4強制"
    ARGS_FORCE_IPV6_SHORT_MSG = "IPv6強制"
    ARGS_XFF_SHORT_MSG = "XFFヘッダー"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "チャンクサイズ"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "サブ待機"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "レガシー接続"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "証明書確認なし"
    ARGS_USERNAME_SHORT_MSG = "ユーザー名"
    ARGS_PASSWORD_SHORT_MSG = "パスワード"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "エラー無視"
    ARGS_MIN_FILESIZE_SHORT_MSG = "最小サイズ"
    ARGS_MAX_FILESIZE_SHORT_MSG = "最大サイズ"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "プレイリスト項目"
    ARGS_DATE_SHORT_MSG = "日付"
    ARGS_DATEBEFORE_SHORT_MSG = "日付以前"
    ARGS_DATEAFTER_SHORT_MSG = "日付以降"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTPヘッダー"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "待機間隔"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "最大待機"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "動画フォーマット"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "マージフォーマット"
    ARGS_SEND_AS_FILE_SHORT_MSG = "ファイルとして送信"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ ファイルが大きすぎます。最大サイズは100KBです。"
    COOKIES_INVALID_FORMAT_MSG = "❌ 許可されている形式は.txtファイルのみです。"
    COOKIES_INVALID_COOKIE_MSG = "❌ ファイルがcookie.txtのようには見えません（'# Netscape HTTP Cookie File'という行がありません）。"
    COOKIES_ERROR_READING_MSG = "❌ ファイルの読み取りエラー：{error}"
    COOKIES_FILE_EXISTS_MSG = "✅ クッキーファイルが存在し、正しい形式です"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service}クッキーファイルが大きすぎます！最大100KB、取得したサイズ{size}KB。"
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service}クッキーファイルがダウンロードされ、フォルダにcookie.txtとして保存されました。</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service}クッキーソースが利用できません（ステータス{status}）。後でもう一度お試しください。"
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ {service}クッキーファイルのダウンロードエラー。後でもう一度お試しください。"
    COOKIES_USER_PROVIDED_MSG = "<b>✅ ユーザーが新しいクッキーファイルを提供しました。</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ クッキーが正常に更新されました：</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ 有効なクッキーではありません。</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTubeクッキーソースが設定されていません！"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 YouTubeクッキーをダウンロードしてチェック中...\n\n試行{attempt}/{total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Access denied. Admin only."
    ADMIN_USER_LOGS_TOTAL_MSG = "Total: <b>{total}</b>\n<b>{user_id}</b> - logs (Last 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 keyboard activated!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ 字幕言語が設定されました：{flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ 字幕言語が設定されました：{flag} {name}（AUTO/TRANS有効）。"
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "字幕言語メニューを閉じました。"
    SUBS_DOWNLOADING_MSG = "💬 字幕をダウンロード中..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Firebaseキャッシュをメモリに再読み込み中..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ COOKIE_URLが設定されていません。/cookieを使用するか、cookie.txtをアップロードしてください。"
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 リモートURLからクッキーをダウンロード中..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ フォールバックCOOKIE_URLは.txtファイルを指す必要があります。"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ フォールバッククッキーファイルが大きすぎます（>100KB）。"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTubeクッキーファイルがフォールバック経由でダウンロードされ、cookie.txtとして保存されました"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ フォールバッククッキーソースが利用できません（ステータス{status}）。/cookieを試すか、cookie.txtをアップロードしてください。"
    COOKIE_FALLBACK_ERROR_MSG = "❌ フォールバッククッキーのダウンロードエラー。/cookieを試すか、cookie.txtをアップロードしてください。"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ フォールバッククッキーのダウンロード中に予期しないエラーが発生しました。"
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser}ブラウザがインストールされていません。"
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ ブラウザを使用してクッキーが保存されました：{browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ クッキーの保存に失敗しました：{error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTubeクッキーが正常に機能しています"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTubeクッキーが期限切れまたは無効です\n\n新しいクッキーを取得するには/cookieを使用してください"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - custom format\n• <code>/format 720</code> - 720p quality\n• <code>/format 4k</code> - 4K quality"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "ヒントを送信しました。"
    FORMAT_MKV_TOGGLE_MSG = "MKVは現在{status}です"
    COOKIES_NO_REMOTE_URL_MSG = "❌ リモートURLが設定されていません"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ 無効なファイル形式"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ ファイルが大きすぎます"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ クッキーが正常にダウンロードされました"
    COOKIES_SERVER_ERROR_MSG = "❌ サーバーエラー{status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ ダウンロードに失敗しました"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ 予期しないエラー"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ ブラウザがインストールされていません。"
    COOKIES_MENU_CLOSED_MSG = "メニューを閉じました。"
    COOKIES_HINT_CLOSED_MSG = "クッキーヒントを閉じました。"
    IMG_HELP_CLOSED_MSG = "ヘルプを閉じました。"
    SUBS_LANGUAGE_UPDATED_MSG = "字幕言語設定が更新されました。"
    SUBS_MENU_CLOSED_MSG = "字幕言語メニューを閉じました。"
    KEYBOARD_SET_TO_MSG = "キーボードが{setting}に設定されました"
    KEYBOARD_ERROR_PROCESSING_MSG = "設定の処理中にエラーが発生しました"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfoが有効になりました。"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfoが無効になりました。"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFWぼかしが無効になりました。"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFWぼかしが有効になりました。"
    SETTINGS_MENU_CLOSED_MSG = "メニューを閉じました。"
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "フラッド待機がアクティブです。後でもう一度お試しください。"
    OTHER_HELP_CLOSED_MSG = "ヘルプを閉じました。"
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "ログメッセージを閉じました。"
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "メニューを閉じました。"
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "無効なサイズ。"
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ MediaInfoの送信エラー：{error}"
    LINK_ERROR_OCCURRED_MSG = "❌ エラーが発生しました：{error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - すべてのログ"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - すべての{path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 リモートURLからダウンロード"
    BROWSER_OPEN_BUTTON_MSG = "🌐 ブラウザを開く"
    SELECT_BROWSER_MSG = "クッキーをダウンロードするブラウザを選択："
    SELECT_BROWSER_NO_BROWSERS_MSG = "このシステムでブラウザが見つかりませんでした。リモートURLからクッキーをダウンロードするか、ブラウザのステータスを監視できます："
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>ブラウザを開く</b> - ミニアプリでブラウザのステータスを監視"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ /check_cookieの実行に失敗しました"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ フラッド制限。後でもう一度お試しください。"
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Failed to open browser cookie menu"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Save as cookie hint closed."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>使用方法：</b>\n<code>/link [quality] URL</code>\n\n<b>例：</b>\n<blockquote>• /link https://youtube.com/watch?v=... - 最高品質\n• /link 720 https://youtube.com/watch?v=... - 720p以下\n• /link 720p https://youtube.com/watch?v=... - 上記と同じ\n• /link 4k https://youtube.com/watch?v=... - 4K以下\n• /link 8k https://youtube.com/watch?v=... - 8K以下</blockquote>\n\n<b>品質：</b> 1から10000まで（例：144、240、720、1080）"
    
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
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube cookieの再試行制限を超えました！\n\n🔢 最大：1時間あたり{limit}回の試行\n⏰ 後でもう一度お試しください"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Tag #{wrong} contains forbidden characters. Only letters, digits and _ are allowed.\nPlease use: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Invalid argument!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ 字幕言語を設定しました：{flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "例：`/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} 選択された言語：{name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Always Askモード {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 字幕は無効です"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 字幕設定</b>\n\n{status_text}\n\n字幕言語を選択：\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - 字幕を無効にする\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 字幕設定</b>\n\n{status_text}\n\n字幕言語を選択："
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>タイトル：</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>時間：</b> {duration} 秒\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>ビデオストリーム：</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 最大品質720p\n- 最大時間1.5時間\n- 最大ビデオサイズ500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️警告：高いCPU負荷により、この機能は非常に遅く（ほぼリアルタイム）、以下に制限されます：\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>クイックコマンド：</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - 字幕を無効にする\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - Always Askモードを有効にする\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - 言語を設定\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - AUTO/TRANSを有効にして言語を設定\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - Always Askモードを有効にする\n"
    SUBS_AUTO_SUBS_TEXT = "（自動字幕）"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ 自動字幕モード {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "コマンド経由でSUBSを無効化：{arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "コマンド経由でSUBS Always Askを有効化：{arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "コマンド経由でSUBS言語を設定：{arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "コマンド経由でSUBS言語+自動モードを設定：{arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "ユーザーが/subsメニューを開きました。"
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "ユーザーが字幕言語を設定：{lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "ユーザーがAUTO/TRANSモードを切り替え：{new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "ユーザーがAlways Askモードを切り替え：{new_always_ask}"
    
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
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "カスタムフォーマットメニューを閉じました"
    
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
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfoを有効にしました。"
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfoを無効にしました。"
    
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
    PLAYLIST_HELP_CLOSED_LOG_MSG = "プレイリストヘルプを閉じました。"
    AUDIO_HINT_CLOSED_LOG_MSG = "オーディオヒントを閉じました。"
    
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
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 利用可能なフォーマットを取得中..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 ビデオの説明を取得中..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ 説明の取得エラー：{error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ ビデオの説明は利用できません"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ 説明の送信エラー：{error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 ビデオの説明をユーザー{user_id}に送信しました {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 gallery-dlを開始中…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>時間：</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>フォーマット：</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>ブラウザ：</b> ウェブブラウザで開く"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "利用可能なフォーマット"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 フォーマットIDの使用方法："
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "リストを取得した後、特定のフォーマットIDを使用してください："
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - フォーマット401をダウンロード"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - 上記と同じ"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - フォーマット140をMP3オーディオとしてダウンロード"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 オーディオのみのフォーマットが検出されました"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "これらのフォーマットはMP3オーディオファイルとしてダウンロードされます。"
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>フォーマットの設定方法：</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - 特定のフォーマットIDをダウンロード"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - 品質でダウンロード"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - 最高品質をダウンロード"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - 常に品質を尋ねる"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>オーディオのみのフォーマット：</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - フォーマット140をMP3オーディオとしてダウンロード"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "これらはMP3オーディオファイルとしてダウンロードされます。"
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 上記のリストからフォーマットIDを使用してください"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ エラー：元のメッセージが見つかりませんでした。"
    ALWAYS_ASK_FORMATS_PAGE_MSG = "フォーマットページ"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ フォーマットメニューの表示エラー"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ フォーマットの取得エラー"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ 利用可能なフォーマットの取得エラー。"
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "後でもう一度お試しください。"
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlpはこのコンテンツを処理できません"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "システムは代わりにgallery-dlの使用を推奨します。"
    ALWAYS_ASK_OPTIONS_MSG = "**オプション：**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• 画像ギャラリーの場合：<code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• 単一画像の場合：<code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dlは、Instagram、Twitter、その他のソーシャルメディアコンテンツでより良く機能することがよくあります。"
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Gallery-dlを試す"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 /args経由でフォーマットが固定されました"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 字幕"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 吹き替えオーディオ"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — 字幕が利用可能です"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — 字幕言語を選択"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ 字幕が見つからず、埋め込まれません"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — キャッシュから即座に再投稿"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — オーディオ言語を選択"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFWは有料です（⭐️$0.02）"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — ダウンロード品質を選択"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — 画像をダウンロード（gallery-dl）"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — poketubeでビデオを視聴"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — ビデオへの直接リンクを取得"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — 利用可能なフォーマットリストを表示"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — ビデオ拡張子/コーデックを変更"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀埋め込み"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — オーディオのみ抽出"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFWは有料です（⭐️$0.02）"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — キャッシュから即座に再投稿"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — poketubeでビデオを視聴"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — オーディオ言語を選択"
    ALWAYS_ASK_BEST_BUTTON_MSG = "最高"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛その他"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝字幕のみ"
    ALWAYS_ASK_SMART_GROUPING_MSG = "スマートグループ化"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "アクションボタン行を追加しました（3）"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "アクションボタン行を追加しました（2+2）"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "既存の行に下部ボタンを追加しました"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "新しい下部行を作成しました"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "プレイリストにビデオが見つかりません"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "サポートされていないURL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "ビデオが見つかりませんでした"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "ビデオが見つかりません"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "メディアが見つかりません"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "このツイートには含まれていません"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>ビデオ情報の取得エラー：</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "ビデオ情報の取得エラー"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "<code>/clean</code>コマンドを試して、もう一度お試しください。エラーが続く場合、YouTubeは認証が必要です。<code>/cookie</code>または<code>/cookies_from_browser</code>経由でcookies.txtを更新して、もう一度お試しください。"
    ALWAYS_ASK_MENU_CLOSED_MSG = "メニューを閉じました。"
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 手動品質選択"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "自動検出が失敗したため、手動で品質を選択してください："
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 すべての利用可能なフォーマット"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 利用可能な品質（キャッシュから）"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ キャッシュされた品質を使用中 - 新しいフォーマットは利用できない場合があります"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 フォーマットをダウンロード中"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 ダウンロード中"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 進捗追跡付きでダウンロード中..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 フォーマットを使用してダウンロード中："
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 フォーマットを使用してオーディオをダウンロード中："
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 最高品質をダウンロード中..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 データベースダンプをダウンロード中..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 ダウンロード中"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "フォーマットページ"
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
    SUBTITLE_MENU_CLOSED_MSG = "字幕メニューを閉じました。"
    SUBTITLE_LANGUAGE_SET_MSG = "字幕言語を設定しました：{value}"
    AUDIO_SET_MSG = "オーディオを設定しました：{value}"
    FILTERS_UPDATED_MSG = "フィルターを更新しました"
    
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
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ 選択された言語の字幕は利用できません"
    ERROR_SENDING_VIDEO_MSG = "❌ ビデオの送信エラー：{error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ プレイリストのビデオを送信しました：{sent}/{total}ファイル。"
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ タイムアウトによりダウンロードがキャンセルされました（2時間）"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ ビデオのダウンロードに失敗しました：{error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Error: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON must be an object (dictionary)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ 無効なJSON形式です。有効なJSONを提供してください。"
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
    ARGS_NOT_SET_MSG = "未設定"
    
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
    ADMIN_STATUS_CLEAN_TEXT_MSG = "クリーン"
    
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
    LANG_SELECTION_MSG = "🌍 <b>言語を選択</b>"
    LANG_CHANGED_MSG = "✅ 言語が{lang_name}に変更されました"
    LANG_ERROR_MSG = "❌ 言語の変更中にエラーが発生しました"
    LANG_CLOSED_MSG = "言語選択が閉じられました"
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
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "リンク抽出のためにグローバルcookieファイルをユーザー{user_id}のフォルダにコピーしました"
    
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
    CHANNEL_JOIN_BUTTON_MSG = "チャンネルに参加"
    
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
    URL_EXTRACTOR_CLOSED_MSG = "閉じる"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "エラーが発生しました"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg not found in PATH or project directory. Please install FFmpeg."
    YTDLP_NOT_FOUND_MSG = "yt-dlp binary not found in PATH or project directory. Please install yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "動画は{rounds}個のパートに分割されます。これは過剰かもしれません"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "動画パート{current}/{total}を分割中: {start_time:.2f}秒から{end_time:.2f}秒まで"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "分割パート{part}の作成に失敗しました: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "分割パート{part}を正常に作成しました: {target_name} ({size}バイト)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "動画パート{part}の分割中にエラーが発生しました: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "動画を{count}個のパートに正常に分割しました"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "動画分割プロセスでエラーが発生しました: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] 動画{video_path}の処理中にエラーが発生しました: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "動画ファイルが存在しません: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "サイズ'{size_result}'の解析中にエラーが発生しました: {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "'{size_result}'から動画のサイズを決定できませんでした。デフォルトを使用: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "サムネイルの作成中にエラーが発生しました: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "動画の長さの解析中にエラーが発生しました: {error}、結果は: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "{thumb_dir}でサムネイルが作成されませんでした。デフォルトを使用"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Command execution error: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Error creating thumbnail with FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Skipping non-dict config section: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Setting {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Using user cookies: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Using YouTube cookies for user {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "グローバルcookieファイルをユーザー{user_id}のフォルダにコピーしました"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] コピーしたグローバルcookieをユーザーcookieとして使用: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "ユーザー{user_id}のグローバルcookieファイルのコピーに失敗しました: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "ドメイン{url}に--no-cookiesを使用"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "プロキシが要求されましたが、設定のインポート/取得に失敗しました: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "gallery-dlにプロキシを強制使用: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "プロキシが要求されましたが、プロキシ設定が不完全です"
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
    SENDER_ERROR_READING_USER_ARGS_MSG = "ユーザー{user_id}の引数の読み取り中にエラーが発生しました: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] 動画{video_path}の処理中にエラーが発生しました: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "User {user_id} has send_as_file enabled, sending as document"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video timed out repeatedly; falling back to send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Caption too long, trying with minimal caption"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (minimal caption) timed out; fallback to send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Error sending video with minimal caption: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Error sending full description file: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Error removing temporary description file: {error}"
    
    # YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "NO_FILTER_DOMAINS内のドメイン{url}のmatch_filterをスキップしています"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "ユーザー{user_id}のフォーマット検出のためにユーザーのURLで既存のYouTube cookieを確認中"
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
    AA_ERROR_SENDING_FORMATS_MSG = "❌ フォーマットファイルの送信エラー：{error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ フォーマットの取得に失敗しました：\n<code>{output}</code>"
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
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "字幕の埋め込みをスキップしました: 長さ{duration}秒が制限{max_duration}秒を超えています"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "字幕の埋め込みをスキップしました: サイズ{size_mb:.2f}MBが制限{max_size}MBを超えています"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "字幕の埋め込みをスキップしました: 品質{width}x{height}（最小辺{min_side}p）が制限{max_quality}pを超えています"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "プレイリスト"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ {service}の範囲制限を超えました: {count}（最大{max_count}）。\n\n利用可能な最大数のファイルをダウンロードするには、次のコマンドのいずれかを使用してください:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ {service}の範囲制限を超えました: {count}（最大{max_count}）\nユーザーID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "PO token provider disabled in config"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} is not a YouTube domain, skipping PO token"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO token provider is not available at {base_url}, falling back to standard YouTube extraction"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO token provider cache cleared, will check availability on next request"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Appインスタンスはまだ利用できません"
    HELPER_USER_NAME_MSG = "ユーザー"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood waitが検出されました。{wait_seconds}秒待機中"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood waitが検出されましたが、時間を抽出できませんでした。{retry_delay}秒待機中"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno error detected, sleeping for {retry_delay} seconds"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "プロキシ設定が不完全です。直接接続を使用します"
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
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "例："
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (direct order)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (reverse order)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "参照：/audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "ユーザー {user_id} が add_bot_to_group コマンドを閉じました"

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
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - 言語を設定"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - AUTO/TRANSで言語を設定"
    SUBS_VALID_OPTIONS_MSG = "有効なオプション："
    
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
    ARGS_KEY_SETTINGS_MSG = "主要設定:\n"
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
    SUBS_ALWAYS_ASK_BUTTON_MSG = "常に確認"
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
