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
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>利用可能なすべてのプロキシでビデオのダウンロードに失敗しました</b>\n\nプロキシ経由のすべてのダウンロード試行が失敗しました。\n試してください：\n• プロキシの機能を確認する\n• リストから別のプロキシを試す\n• プロキシなしでダウンロードする（可能な場合）"

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
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>プレイリストのヒント</b>

範囲を指定せずにプレイリストのリンクを送信しました。ボットは自動的に最初の動画をダウンロードしました (<code>*1*1</code>)。

<b>プレイリストから複数の動画をダウンロードするには、範囲を指定してください：</b>
• <code>URL*1*5</code> — 最初の5本の動画（1から5まで含む）
• <code>URL*3*3</code> — 3番目の動画のみ
• <code>/vid 1-10 URL</code> — 代替形式

詳細: <code>/playlist</code>"""
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
    PROXY_MENU_TEXT_MULTIPLE_MSG = "すべての yt-dlp 操作でプロキシ サーバー ({config_count} + {file_count} が利用可能) の使用を有効または無効にしますか?\n\nALL (AUTO) を有効にすると、プロキシはランダムな方法で選択されます。"
    PROXY_MENU_CLOSED_MSG = "メニューを閉じました。"
    PROXY_ENABLED_CONFIRM_MSG = "✅ プロキシが有効になりました。すべてのyt-dlp操作でプロキシが使用されます。"
    PROXY_ENABLED_MULTIPLE_MSG = "✅ プロキシが有効になりました。すべてのyt-dlp操作で{count}個のプロキシサーバーが{method}選択メソッドで使用されます。"

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ プロキシが有効になっています (ALL AUTO モード)。\n\n📊 ボットは次の順序でプロキシを試行します。\n1️⃣ Config.py からの {config_count} プロキシ\n2️⃣ TXT/proxy.txt ファイルからの {file_count} プロキシ\n\n🔄 接続が成功するまで、すべてのプロキシが順番に試行されます。"
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
    KEYBOARD_ACTIVATED_MSG = "🎹キーボードが有効になりました！"
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
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ ブラウザの選択が更新されました。"
    
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
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ 使用方法：/ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "ユーザーを無視しました 👁️❌\n \nID：<code>{user_id}</code>\n無視した日付：{date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> は既に無視されています ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ 使用方法：/unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "ユーザーはもう無視されていません 👁️✅\n \nID：<code>{user_id}</code>\n無視を解除した日付：{date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> は無視されていません ✅😐"
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
    ARGS_REFERER_SHORT_MSG = "リファラー"
    ARGS_GEO_BYPASS_SHORT_MSG = "Geoバイパス"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "証明書確認"
    ARGS_LIVE_FROM_START_SHORT_MSG = "ライブ開始"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "ライブ開始なし"
    ARGS_USER_AGENT_SHORT_MSG = "User Agent"  # User-Agent is a technical term, can remain
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
    ARGS_TWOFACTOR_SHORT_MSG = "2要素認証"
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
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ アクセスが拒否されました。管理者のみ。"
    ADMIN_USER_LOGS_TOTAL_MSG = "合計: <b>{total}</b>\n<b>{user_id}</b> - ログ (最後の10件):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 キーボードが有効になりました!"
    
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
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 メディア情報</blockquote>"
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
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ ブラウザの Cookie メニューを開けませんでした"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Cookie ヒントを閉じて保存します。"
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>使用方法：</b>\n<code>/link [quality] URL</code>\n\n<b>例：</b>\n<blockquote>• /link https://youtube.com/watch?v=... - 最高品質\n• /link 720 https://youtube.com/watch?v=... - 720p以下\n• /link 720p https://youtube.com/watch?v=... - 上記と同じ\n• /link 4k https://youtube.com/watch?v=... - 4K以下\n• /link 8k https://youtube.com/watch?v=... - 8K以下</blockquote>\n\n<b>品質：</b> 1から10000まで（例：144、240、720、1080）"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K quality"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ ストリームリンクの取得に失敗しました"
    LINK_ERROR_GETTING_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ YouTube Cookie インデックスが無効です: {total_urls} 。使用可能な範囲は{selected_index}0__ です"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 YouTubeクッキーをダウンロードして確認中...\n\n試行 {attempt}/{total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 YouTubeクッキーをダウンロードして確認中...\n\n試行 {attempt}/{total}\n🔍 クッキーをテスト中..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTubeクッキーが正常にダウンロードされ、検証されました!\n\n使用したソース {source}/{total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ すべてのYouTubeクッキーが期限切れまたは利用できません!\n\nボット管理者に連絡して交換してください。"
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
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "ユーザーがブラウザから Cookie をリクエストしました。"
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "ブラウザ選択キーボードは、インストールされているブラウザでのみ送信されます。"
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "ブラウザの選択は終了しました。"
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "フォールバック COOKIE_URL が正常に使用されました (ソースは非表示)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "フォールバック COOKIE_URL が失敗しました: status= {status} (非表示)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "フォールバック COOKIE_URL の予期しないエラー: {error}: {error_type}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "ブラウザ {browser} がインストールされていません。"
    COOKIES_SAVED_BROWSER_LOG_MSG = "ブラウザを使用して保存された Cookie: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "ユーザー {user_id} 用に保存された Cookie ファイル。"
    COOKIES_FILE_WORKING_LOG_MSG = "Cookie ファイルが存在し、形式が正しく、YouTube Cookie が機能しています。"
    COOKIES_FILE_EXPIRED_LOG_MSG = "Cookie ファイルは存在し、正しい形式ですが、YouTube Cookie の有効期限が切れています。"
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Cookie ファイルが存在し、正しい形式になっています。"
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Cookie ファイルは存在しますが、形式が正しくありません。"
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Cookie ファイルが見つかりません。"
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "ユーザー {service} の {user_id} クッキー URL が空です。"
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} Cookie URL は .txt ではありません (非表示)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{size} Cookie ファイルが大きすぎます: {service}ト (ソースは非表示)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{user_id} Cookie ファイルがユーザー {service} 用にダウンロードされました (ソースは非表示)。"
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "スクリプトが見つかりません: {user_id}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "初期ステータスメッセージの送信に失敗しました"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "{script_path}の実行エラー: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Firebase キャッシュは自動タスクによってリロードされます。"
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Firebase キャッシュは管理者によってリロードされました。"
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Firebase キャッシュのリロード中にエラーが発生しました: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "ブロードキャスト開始。テキスト:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "すべてのユーザーに送信されるブロードキャスト メッセージ。"
    ADMIN_BROADCAST_FAILED_LOG_MSG = "メッセージのブロードキャストに失敗しました: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "管理者 {user_id} が URL: {url} のキャッシュをクリアしました"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "管理者 {script_path} がポルノ リスト更新スクリプトを開始しま{user_id}_0__"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "ポルノリスト更新スクリプトが管理者によって正常に完了しました {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "ポルノ リストの更新スクリプトが管理者によって失敗しました {error} : {user_id}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "管理者 {script_path} が存在しないスクリプトを実行しようとしま{user_id}_0__"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "管理者によるポルノ更新スクリプトの実行中にエラーが発生しました {error} : {user_id}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "管理者 {user_id} がポルノ キャッシュのリロードを開始しました"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "管理者によるポルノ キャッシュのリロード中にエラーが発生しました {error} : {user_id}"
    ADMIN_PORN_CHECK_LOG_MSG = "管理者 {status} が NSFW の URL をチェックしました: _{url}- 結果: __VAR{user_id}"
    
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
    LINK_EXTRACTED_LOG_MSG = "ユーザー {user_id} から {url} から抽出された直接リンク"
    LINK_EXTRACTION_FAILED_LOG_MSG = "ユーザー {user_id} の {url} からの直接リンクを抽出できませんでした: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "ユーザー {error} のリンク コマンドでエラーが発生しました: {user_id}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "ユーザー {setting} がキーボードを {user_id} に設定しました"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "ユーザー {setting} がキーボードを {user_id} に設定しました"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "コマンドで設定された MediaInfo: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "ユーザーが /mediainfo メニューを開きました。"
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "メディア情報: 閉鎖されました。"
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfoを有効にしました。"
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfoを無効にしました。"
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "引数を介して分割サイズを {size} バイトに設定します。"
    SPLIT_MENU_OPENED_LOG_MSG = "ユーザーが /split メニューを開きました。"
    SPLIT_SELECTION_CLOSED_LOG_MSG = "分割選択が閉じられました。"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "分割サイズは {size} バイトに設定されます。"
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "コマンドで設定されたプロキシ: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "ユーザーが /proxy メニューを開きました。"
    PROXY_MENU_CLOSED_LOG_MSG = "プロキシ: 閉鎖されました。"
    PROXY_ENABLED_LOG_MSG = "プロキシが有効になりました。"
    PROXY_DISABLED_LOG_MSG = "プロキシが無効になりました。"
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "ヘルプ メッセージは閉じられました。"
    AUDIO_HELP_SHOWN_LOG_MSG = "/音声ヘルプを表示しました"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "ユーザーがプレイリストのヘルプをリクエストしました。"
    PLAYLIST_HELP_CLOSED_LOG_MSG = "プレイリストヘルプを閉じました。"
    AUDIO_HINT_CLOSED_LOG_MSG = "オーディオヒントを閉じました。"
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "{user_id} からユーザー {url} の [リンク] ボタンを介して直接リンク メニューが作成されました"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "ユーザー {error} の {url}らのリンク ボタンを介した直接リンクの抽出に失敗しました: {user_id}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "ユーザー {user_id} に対して LIST コマンドが実行されました、URL: {url}"
    QUICK_EMBED_LOG_MSG = "クイック埋め込み: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "{url} の「Always Ask」メニューが送信されました"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "エラーの後、ユーザー {error} のキャッシュされた品質メニューが作成されました: {user_id}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "{error} の常に尋ねるメニュー エラー: {url}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Format is fixed via /args settings"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "オーディオ"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "ビデオ"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "ビデオ"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "次へ ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️前へ"
    SUBTITLES_NEXT_BUTTON_MSG = "次へ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ すべてのテキストフィールドが空です"
    SENDER_VIDEO_DURATION_MSG = "動画の長さ:"
    SENDER_UPLOADING_FILE_MSG = "📤 ファイルをアップロードしています..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 ビデオをアップロード中..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 動画の長さ:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 ファイルがアップロードされました。"
    DOWN_UP_VIDEO_INFO_MSG = "📋 ビデオ情報"
    DOWN_UP_NUMBER_MSG = "番号"
    DOWN_UP_TITLE_MSG = "タイトル"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ ダウンロードしたビデオ。"
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 アップロードを処理中..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 分割部分 {part} ファイルがアップロードされました"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅アップロード完了"
    DOWN_UP_FILES_UPLOADED_MSG = "アップロードされたファイル"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚閉じる"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼コーデック"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣ダブス"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬サブスク"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 ブラウザ"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 直接リンクを取得しています..."
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
    ALWAYS_ASK_FROM_CACHE_MSG = "(キャッシュから)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ エラー: 元のメッセージが見つかりません。削除された可能性があります。再度リンクを送信してください。"
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ エラー: 元の URL が見つかりません。再度リンクを送信してください。"
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>直接リンクを取得しました</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>タイトル:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>期間:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>形式:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>ビデオ ストリーム:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>オーディオ ストリーム:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ ストリームリンクの取得に失敗しました"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "ユーザー {user_id} の {url} から Always Ask メニューを介して抽出された直接リンク"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "ユーザー {error} の {url}らの Always Ask メニューによる直接リンクの抽出に失敗しました: {user_id}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "ユーザー {user_id} から {url} から down_and_up_with_format 経由で抽出された直接リンク"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "ユーザー {error} の {url}らの down_and_up_with_format による直接リンクの抽出に失敗しました: {user_id}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "ユーザー {user_id} から {url} から down_and_audio 経由で抽出された直接リンク"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "ユーザー {error} の down_and_audio 経由の直接リンクを {url}ら抽出できませんでした: {user_id}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ 音声はキャッシュから送信されます。"
    AUDIO_PROCESSING_MSG = "🎙️ 音声を処理しています..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 オーディオをダウンロード中:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "音声のダウンロード中にエラーが発生しました。"
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ 音声情報の抽出に失敗しました"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "プレイリストのインデックス {index} でサポートされていないファイル タイプをスキップします"
    AUDIO_FILE_NOT_FOUND_MSG = "ダウンロード後に音声ファイルが見つかりません。"

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ 音声の送信に失敗しました: ファイルサイズが 0 B です (プレイリストインデックス {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ 音声ファイルはまだダウンロード中です。お待ちください..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 オーディオファイルをアップロード中...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ 音声の送信に失敗しました: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "プレイリスト オーディオがユーザー {sent} に送信されました: {user_id}/{quality} ファイル (品質= {total})"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ オーディオのダウンロードに失敗しました: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ タイムアウトのためダウンロードがキャンセルされました (2 時間)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ ビデオ ファイルが見つかりません: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ 動画の送信に失敗しました: ファイルサイズが 0 B です (プレイリストインデックス {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ 動画ファイルはまだダウンロード中です。お待ちください..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ ビデオ処理エラー: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ 説明ファイルの送信中にエラーが発生しました: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 動画のキャプションを変更したい場合 - 新しいテキストで動画に返信</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "字幕が検出されませんでした"
    VIDEO_PROGRESS_MSG = "<b>ビデオ:</b> {total} / {current}"
    AUDIO_PROGRESS_MSG = "<b>音声:</b> {total} / {current}"
    URL_PROGRESS_MSG = "<b>URL:</b> {total} / {current}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL 制限を超えました: {limit} / {count}"
    MULTI_URL_COMPLETED_MSG = "処理が完了しました"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ マルチ URL モードでは、プレイリスト範囲は許可されません。範囲のない単一の URL のみを送信します (*1*5、/vid 1-10 など)。"
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "サイトがサポートされているかどうかは、<a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>ここ</a>で確認してください。"
    ERROR_COOKIE_NEEDED_MSG = "このビデオをダウンロードするには、<code>Cookie</code> が必要な場合があります。まず、<b>/clean</b> コマンドでワークスペースをクリーンアップします。"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "YouTube の場合 - <b>/cookie</b> コマンドで <code>cookie</code> を取得します。その他のサポートされているサイトの場合 - 独自の Cookie (<a href='https://t.me/tg_ytdlp/203'>guide1</a>) (<a href='https://t.me/tg_ytdlp/214'>guide2</a>) を送信し、その後ビデオ リンクを再度送信します。"
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "字幕言語を選択してください"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "代替の音声言語はありません"
    CHOOSE_AUDIO_LANGUAGE_MSG = "音声言語を選択してください"
    PAGE_NUMBER_MSG = "ページ {page}"
    TOTAL_PROGRESS_MSG = "総進捗状況"
    SUBTITLE_MENU_CLOSED_MSG = "字幕メニューを閉じました。"
    SUBTITLE_LANGUAGE_SET_MSG = "字幕言語を設定しました：{value}"
    AUDIO_SET_MSG = "オーディオを設定しました：{value}"
    FILTERS_UPDATED_MSG = "フィルターを更新しました"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙戻る"
    CLOSE_BUTTON_TEXT = "🔚閉じる"
    LIST_BUTTON_TEXT = "📃リスト"
    IMAGE_BUTTON_TEXT = "🖼画像"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Qualities not auto-detected\nUse 'Other' button to see all available formats.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Live Stream Detected**\n\nDownloading of ongoing or infinite live streams is not allowed.\n\nPlease wait for the stream to end and try downloading again when:\n• The stream duration is known\n• The stream has finished\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>ライブ ストリームのダウンロード</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "チャンク {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "最大サイズ: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "合計継続時間: {duration} 秒"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Live Stream - Chunk {chunk}</b>\n⏱ Duration: {duration} sec\n📦 Size: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "チャンク {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>ライブ ストリームのダウンロードが完了しました</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "ダウンロードされた {chunks} チャンク"
    LIVE_STREAM_TOTAL_DURATION_MSG = "合計継続時間: {duration} 秒"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>ライブ ストリームのダウンロードが停止しました</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "ユーザー ディレクトリが削除されました (おそらく /clean コマンドによって)"
    LIVE_STREAM_FILE_DELETED_MSG = "チャンクファイルが削除されました (おそらく /clean コマンドによって)"
    LIVE_STREAM_ENDED_MSG = "ℹ️配信は終了しました"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "`/format` コマンドを使用して別の形式を選択してください。"
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>ダイレクトリンクを取得しました</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Title:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>オーディオストリーム:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **File Processing Error**\n\nThe video was downloaded but couldn't be processed due to invalid characters in the filename.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **File Processing Error**\n\nThe video was downloaded but couldn't be processed due to an invalid argument error.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**理由:**\n"
        "• ダウンロードしたファイルは動画ファイルではありません\n"
        "• ドキュメント（PDF、DOCなど）またはアーカイブの可能性があります\n\n"
        "**解決策:**\n"
        "• リンクを確認してください - 動画ではなくドキュメントにリンクしている可能性があります\n"
        "• 別のリンクまたはソースを試してください\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**理由:**\n"
        "• ファイルを動画として処理できません\n"
        "• 動画ファイルではないか、ファイルが破損している可能性があります\n\n"
        "**解決策:**\n"
        "• リンクを確認してください - 動画ではなくドキュメントにリンクしている可能性があります\n"
        "• 別のリンクまたはソースを試してください\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Format Not Available**\n\nThe requested video format is not available for this video.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Format ID {format_id} not found for this video.\n\nAvailable format IDs: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **この動画ではAV1形式は利用できません。**\n\n**利用可能な形式:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **ファイル処理エラー**\n\nオーディオはダウンロードされましたが、ファイル名に無効な文字が含まれているため処理できませんでした。\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **ファイル処理エラー**\n\nオーディオはダウンロードされましたが、無効な引数エラーのため処理できませんでした。\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "ユーザーが禁止されたコンテンツを入力しました。ダウンロードできません。"
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "コマンドで設定された NSFW ブラー: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "ユーザーが /nsfw メニューを開きました。"
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: 閉鎖されました。"
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "{status} Cookie のダウンロードに失敗しました: status= _{service}(URL は非表示)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "{error} Cookie のダウンロード中にエラーが発生しました: {service}URL は非表示)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "{service} Cookie (URL 非表示) のダウンロード中に予期しないエラーが発生しました: {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "ユーザー {user_id} の Cookie ファイルが更新されました。"
    COOKIES_INVALID_CONTENT_LOG_MSG = "ユーザー {user_id} によって提供された Cookie コンテンツが無効です。"
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "ユーザー {user_id} の YouTube Cookie URL は空です。"
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "YouTube Cookie がソース {user_id} からダウンロードされ、ユーザー {source} に対して検証されました。"
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "ユーザー {user_id} のすべての YouTube Cookie ソースが失敗しました。"
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "管理者による check_porn コマンドのエラー {error} : {admin_id}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "分割部分のサイズは {size} バイトに設定されます。"
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "ファイル分割によりビデオのアップロードが完了しました。"
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "プレイリストビデオがユーザー {sent} に送信されました: {user_id}/{quality} ファイル (品質= {total})"
    UNKNOWN_ERROR_MSG = "❌ 不明なエラー: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "プレイリストのインデックス {index} でサポートされていないファイル タイプをスキップします"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg not found. Please install FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ MP4 への変換に失敗しました: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Embedding subtitles may take a long time (up to 1 min per 1 min of video)!\n🔥 Starting to burn subtitles..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ 字幕は（画質・長さ・サイズ）の制限により埋め込むことができません。"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ 選択された言語の字幕は利用できません"
    ERROR_SENDING_VIDEO_MSG = "❌ ビデオの送信エラー：{error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ プレイリストのビデオを送信しました：{sent}/{total}ファイル。"
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ タイムアウトによりダウンロードがキャンセルされました（2時間）"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ ビデオのダウンロードに失敗しました：{error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ エラー: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON はオブジェクト (辞書) である必要があります。"
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ 無効なJSON形式です。有効なJSONを提供してください。"
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ 値は {max_val} と {min_val} の間である必要があります。"
    ARGS_PARAM_SET_TO_MSG = "✅ {value} を次のように設定します: <code> {description}/code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ 本当です"
    ARGS_FALSE_BUTTON_MSG = "❌ 誤り"
    ARGS_BACK_BUTTON_MSG = "🔙戻る"
    ARGS_CLOSE_BUTTON_MSG = "🔚閉じる"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ 本当です"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ 誤り"
    ARGS_NOT_SET_MSG = "未設定"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ この動画ではAV1形式は利用できません。\n\n利用可能な形式:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ ダウンロードエラー: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ プレイリストのインデックス {index} にビデオが見つかりません。"
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **動画変換失敗**\n\n無効な引数エラーのため、動画をMP4に変換できませんでした。\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **動画変換失敗**\n\n動画をMP4に変換できませんでした。\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ ストリームリンクの取得に失敗しました"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ インデックス {index} にコンテンツが見つかりません"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ エラー: 元のメッセージが見つかりません。"
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ エラー: URL が見つかりません。"
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ このURLは埋め込みできません。"
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} コーデックはこのビデオでは使用できません"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} 形式はこのビデオでは使用できません"
    
    # Always Ask Menu button texts
    AA_AVC_BUTTON_MSG = "✅ AVC"
    AA_AVC_BUTTON_INACTIVE_MSG = "☑️ AVC"
    AA_AVC_BUTTON_UNAVAILABLE_MSG = "❌ AVC"
    AA_AV1_BUTTON_MSG = "✅ AV1"
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
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ クッキーを確認する"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ オール（オート）"
    PROXY_OFF_BUTTON_MSG = "❌ オフ"
    PROXY_CLOSE_BUTTON_MSG = "🔚閉じる"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 国を選択:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ 国の選択をクリア"
    PROXY_COUNTRY_SELECTED_MSG = "✅ 選択した国: {country} (コード: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 利用可能なプロキシ: {proxy_count} (HTTP: {http_count}、SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 ボットは最初に HTTP を試行し、次に SOCKS5 を試行します"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 選択した国に対してプロキシが自動的に有効になります"
    PROXY_COUNTRY_CLEARED_MSG = "✅ 国の選択がクリアされました"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ 国の選択がクリアされました"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ 選択した国: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 ファイルからの国を使用: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 ファイルから利用可能な国: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 選択した国: {country} (コード: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ この国ではプロキシが有効になっています"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ プロキシが無効になっています (有効にするには [ALL (AUTO)] を押します)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ オン"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ オフ"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚閉じる"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ オン (ぼかしなし)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ON (No Blur)"
    NSFW_OFF_BLUR_MSG = "✅ オフ（ぼかし）"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ OFF (Blur)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "クリーン"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "ユーザー {error} の応答メッセージの処理中にエラーが発生しました: {user}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "ユーザー {error} へのブロードキャスト送信エラー: {user}"
    ADMIN_LOGS_FORMAT_MSG = "{bot_name}のログ\nユーザー: {user_id}\n合計ログ: {total}\n現在時刻: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\n合計 {path}: {count}\n現在時刻: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>合計ユーザー: {count}</i>\n最後の20件 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "ポルノキャッシュは管理者 {admin_id} によってリロードされました。ドメイン: {domains}, キーワード: {keywords}, サイト: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "タイムアウト メッセージの送信エラー: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>言語を選択</b>"
    LANG_CHANGED_MSG = "✅ 言語が{lang_name}に変更されました"
    LANG_ERROR_MSG = "❌ 言語の変更中にエラーが発生しました"
    LANG_CLOSED_MSG = "言語選択が閉じられました"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[ブラウザ] コールバック: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "URL を使用してブラウザ監視ボタンを追加: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "ブラウザ監視 URL が構成されていません: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Keyboard setting updated!**\n\nNew setting: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "キーボードを非表示にできませんでした: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "ユーザー {user_id} のリンク抽出に動作する YouTube Cookie を使用する"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "ユーザー {user_id} のリンク抽出に使用できる有効な YouTube Cookie がありません"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "ユーザー {user_id} のリンク抽出に既存の YouTube Cookie を使用する"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "ユーザー {user_id} のリンク抽出用の YouTube Cookie が見つかりませんでした"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "リンク抽出のためにグローバルcookieファイルをユーザー{user_id}のフォルダにコピーしました"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] ユーザー {user_id} が mediainfo コマンドを要求しました"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] ユーザー {is_admin} は管理者です:{user_id}_"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] ユーザー {is_in_channel} は{user_id}AR_0__ にいます"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] ユーザー {user_id} のアクセスが拒否されました - 管理者でもチャンネルでもありません"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] ユーザー {user_id} のアクセスが許可されました"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] コールバック: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ このコマンドは管理者のみが使用できます。"
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ PO トークンのサポートによりダウンロードが完了しました"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ 洪水制限。後で試してください。"
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST トークン更新エラー: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Firebase セッションを閉じるときにエラーが発生しました: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ 基本データベース構造の初期化中にエラーが発生しました: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ すべてのパラメータが config.py に設定されているわけではありません (FIREBASE_CONF、FIREBASE_USER、FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL が設定されていません"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey が idToken を取得するように設定されていません"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Firebase ダンプのダウンロード中にエラーが発生しました: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ REST 経由で Firebase ダンプをダウンロードできませんでした"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ _download_and_reload_cache のエラー: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ auto reload_cache の実行中にエラーが発生しました ({error}/{max_retries}試行){attempt}__"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ 再試行はすべて失敗しました"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Firebase ダンプのダウンロードを {datetime} で開始します"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ 依存関係は使用できません: リクエストまたはセッション"
    DB_DATABASE_EMPTY_MSG = "⚠️ データベースが空です"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ ロガーを閉じるときにエラーが発生しました: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ クリーンアップ中のエラー: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ クローン エラー: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ クローンのタイムアウト"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ クローン例外: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ ユーザーによってアップデートがキャンセルされました"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ リポジトリのクローンが正常に作成されました"
    UPDATE_BACKUPS_MOVED_MSG = "✅ バックアップは _backup/ に移動されました"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ すべてのモジュールがロードされています"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ 終了時にクリーンアップが完了しました"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Received signal {signal}, shutting down gracefully..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "お待ちください..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 HLS ストリームをダウンロードしています:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "断片を待っています"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ バックアップ {ts} が _backup/ に見つかりません"
    RESTORE_FAILED_RESTORE_MSG = "❌ Failed to restore {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ 復元されました: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Details:</b> {error_details}\n\nDownload stopped due to critical error.\n\n💡 <b>Tip:</b> If you're getting 401 Unauthorized error, try using <code>/cookie instagram</code> command or send your own cookies to authenticate with Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ ポルノ ブラックリストのドメイン: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ 見つかったポルノキーワード: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ ホワイトリスト内のドメイン: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ ホワイトリストのキーワードが見つかりました: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ ポルノキーワードが見つかりませんでした"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ インデックス {index} で TikTok API エラーが発生し、次の音声にスキップしています..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ インデックス {index} で TikTok API エラーが発生し、次の動画にスキップします..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "User entered a <b>url</b>\n <b>user's name:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>User entered like this:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "チャンネルに参加"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 ハンドラーの登録: {func_name} {handler_type}__"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - 私の 5 つのクッキーをダウンロード"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - ブラウザの YT Cookie を取得します"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Cookie ファイルを検証します"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - カスタム Cookie をアップロードします"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚閉じる"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "利用可能な形式: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚閉じる"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚閉じる"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚閉じる"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚閉じる"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "ヘルプは終了しました。"
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "閉じる"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "エラーが発生しました"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg not found in PATH or project directory. Please install FFmpeg."
    YTDLP_NOT_FOUND_MSG = "yt-dlp バイナリが PATH またはプロジェクト ディレクトリに見つかりません。 yt-dlpをインストールしてください。"
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
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "辞書以外の構成セクションをスキップ: {opts}= {section}"
    GALLERY_DL_SETTING_CONFIG_MSG = "{value}.{key} {section}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] ユーザー Cookie の使用: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "ユーザー {user_id} に YouTube Cookie を使用する"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "グローバルcookieファイルをユーザー{user_id}のフォルダにコピーしました"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] コピーしたグローバルcookieをユーザーcookieとして使用: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "ユーザー{user_id}のグローバルcookieファイルのコピーに失敗しました: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "ドメイン{url}に--no-cookiesを使用"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "プロキシが要求されましたが、設定のインポート/取得に失敗しました: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "gallery-dlにプロキシを強制使用: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "プロキシが要求されましたが、プロキシ設定が不完全です"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "プロキシ ヘルパーが失敗しました: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "抽出アイテムを解析しています..."
    GALLERY_DL_ITEM_COUNT_MSG = "アイテム {item}: {count}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "見つかったメタデータ (タグ 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "見つかった URL (タグ 3): {metadata}、メタデータ:{url}_"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "見つかったメタデータ (レガシー): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "見つかった URL (レガシー): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "見つかったファイル名: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "見つかったディレクトリ: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "見つかった拡張子: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "解析された {fallback} アイテム、情報:{info}_、フォールバック: {count}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "gallery-dl config の設定: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "戦略 A を試す: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor モジュールが見つかりません"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() はこのビルドでは使用できません"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "extractor.find( {url} ) の呼び出し"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "URL に一致するエクストラクターはありませんでした"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "エクストラクターに Cookie を設定: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "エクストラクターに Cookie を設定できませんでした: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "エクストラクタが見つかり、items() を呼び出しています"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "戦略 A が成功し、情報を取得しました: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "戦略 A: extractor.items() は有効な情報を返しませんでした"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "戦略 A (extractor.find) が失敗しました: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "--get-urls からのフォールバック メタデータ: total= {total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "すべての戦略がメタデータの取得に失敗しました"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "画像情報の抽出に失敗しました: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job モジュールが見つかりません (インストールが壊れていますか?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob はこのビルドでは使用できません"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "gallery-dl ディレクトリでダウンロードしたファイルを検索しています"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "エクストラクターから名前でファイルを検索しようとしています"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "ユーザー{user_id}の引数の読み取り中にエラーが発生しました: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] 動画{video_path}の処理中にエラーが発生しました: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "ユーザー {user_id} は send_as_file を有効にし、ドキュメントとして送信しています"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video が繰り返しタイムアウトになりました。 send_document にフォールバックする"
    SENDER_CAPTION_TOO_LONG_MSG = "キャプションが長すぎます。最小限のキャプションで試してください"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (最小限のキャプション) がタイムアウトしました。 send_document へのフォールバック"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "最小限のキャプションを含むビデオの送信エラー: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "完全な説明ファイルの送信中にエラーが発生しました: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "一時的な説明ファイルの削除中にエラーが発生しました: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "NO_FILTER_DOMAINS内のドメイン{url}のmatch_filterをスキップしています"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "ユーザー{user_id}のフォーマット検出のためにユーザーのURLで既存のYouTube cookieを確認中"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "既存の YouTube Cookie は、ユーザー {user_id} の形式検出のためにユーザーの URL に作用します - それらを使用します"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "ユーザーの URL で既存の YouTube Cookie が失敗しました。ユーザー {user_id} の形式検出のために新しい Cookie を取得しようとしました"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "ユーザー {i} の形式検出のために YouTube Cookie ソース {user_id} を試しています"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "ソース {user_id} からの YouTube Cookie は、ユーザー {i} の形式を検出するためにユーザーの URL に作用します - ユーザー フォルダーに保存されます"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "ソース {user_id} からの YouTube Cookie は、ユーザー {i} の形式検出のためにユーザーの URL では機能しません"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "ユーザー {i} の形式検出のため、ソース {user_id} から YouTube Cookie をダウンロードできませんでした"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "すべての YouTube Cookie ソースがユーザー {user_id} の形式検出に失敗しました。Cookie なしで試行します"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "ユーザー {user_id} の形式検出用に設定された YouTube Cookie ソースがありません。Cookie なしで試行します。"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "ユーザー {user_id} のフォーマット検出用の YouTube Cookie が見つかりませんでした。新しいクッキーを取得しようとしています"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "ユーザー {user_id} のフォーマット検出に YouTube Cookie を使用する (常に確認するメニューで検証済み)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "ユーザー {user_id} のフォーマット検出用の YouTube Cookie が見つかりませんでした。復元を試みています..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "フォーマット検出のためにグローバル Cookie ファイルをユーザー {user_id} フォルダーにコピーしました"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "ユーザー {error} のグローバル Cookie ファイルのコピーに失敗しました: {user_id}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "get_video_formats のドメインに --no-cookies を使用する: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "アプリはまだ初期化されていません。 {name} にアクセスできません"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>キャプション:</b> <code>{caption}</code>\n<b>ユーザーID:</b> <code>{user_id}</code>\n<b>ユーザー名:</b> <code>{users_name}</code>\n<b>動画ファイルID:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor のエラー: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor で予期しないエラーが発生しました: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 動画 URL</a>{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL によるアクセス"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin が初期化されました"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken が更新されました"
    DB_LOG_FOR_USER_ADDED_MSG = "追加されたユーザーのログ"
    DB_DATABASE_CREATED_MSG = "データベースが作成されました"
    DB_BOT_STARTED_MSG = "ボットが開始されました"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY が config.py に永続化されました: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "プレイリスト部分はすでにキャッシュされています: {path_parts} 、スキップしています"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: URL/品質バリアントのキャッシュが見つからず、空の辞書を返します"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: 広い範囲の高速カウント: {cached_count} キャッシュされたビデオ"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: ハッシュ {quality_key} {url_hash}_0__ のキャッシュが見つかりませんでした"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: どの URL バリアントでもキャッシュが見つからず、None を返します"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ アクセスが拒否されました。管理者のみ。"
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Firebaseキャッシュの自動再読み込みが更新されました!\n\n📊 ステータス: {status}\n⏰ スケジュール: 00:00から{interval}時間ごと\n🕒 次回再読み込み: {next_exec} ({delta_min}分後)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Firebaseキャッシュの自動再読み込みが停止されました!\n\n📊 ステータス: ❌ 無効\n💡 再有効化するには /auto_cache on を使用してください"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ 引数が無効です。 | で /auto_cache を使用します。オフ | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ 間隔は 1 ～ 168 時間にする必要があります"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ 間隔の設定に失敗しました"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Firebaseキャッシュの自動間隔が更新されました!\n\n📊 ステータス: ✅ 有効\n⏰ スケジュール: 00:00から{interval}時間ごと\n🕒 次回再読み込み: {next_exec} ({delta_min}分後)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Firebaseキャッシュの自動再読み込みが開始されました!\n\n📊 ステータス: ✅ 有効\n⏰ スケジュール: 00:00から{interval}時間ごと\n🕒 次回再読み込み: {next_exec} ({delta_min}分後)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Firebaseキャッシュの自動再読み込みが停止されました!\n\n📊 ステータス: ❌ 無効\n💡 再有効化するには /auto_cache on を使用してください"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "自動リロードが有効です。次は {next_exec} で"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "自動リロードは管理者によって無効にされています。"
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "自動リロード間隔は {next_exec}h に設定されます。次{interval}__ で"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "自動リロードが開始されました。次は {next_exec} で"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "自動リロードは管理者によって停止されました。"
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase キャッシュがロードされました: {count} ルート ノード"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Firebase キャッシュ ファイルが見つかりません。空のキャッシュから始まります: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Firebase キャッシュのロードに失敗しました: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase キャッシュがリロードされました: {count} ルート ノード"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Firebase キャッシュ ファイルが見つかりません: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Firebase キャッシュのリロードに失敗しました: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 あなたはボットへのアクセスを禁止されています! 解除するには {Config.ADMIN_USERNAME} に連絡してください\n<blockquote>P.S. チャンネルを離れないでください - 自動的に禁止されます ⛔️</blockquote>\n🌍言語を変更 /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ ビデオ形式が見つかりません。画像ダウンローダーを試しています…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegramがメッセージ送信を制限しています。\n⏳ お待ちください: {time_str}\nタイマーを更新するには、URLを再度2回送信してください。"
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>ボタンをクリックしてストリームURLをコピーし、VLCアプリに貼り付けてください</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>ボタンをクリックしてストリームURLをコピーし、VLCアプリに貼り付けてください</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>リンク取得エラー:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ フォーマットファイルの送信エラー：{error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ フォーマットの取得に失敗しました：\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 分析中... (6 秒待ち)"
    AA_PROCESSING_MSG = "🔎 分析中..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ タグ #{wrong} に禁止文字が含まれています。文字、数字、_のみ使用可能です。\n使用例: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ 問題は解決しました。 Пожалуйста、сделайте бота админом этой группы。"
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Hello {first_name},\n \n<i>This bot🤖 can download any videos into telegram directly.😊 For more information press <b>/help</b></i> 👈\n\n<blockquote>P.S. Downloading 🔞NSFW content and files from ☁️Cloud Storage is paid! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Do not leave the channel - you will be banned from using the bot ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 削除するファイルはありません。"
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 All files removed successfully!\n\nRemoved files:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ 前回のダウンロードが完了するまで待ちます"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "check_user でアプリ インスタンスが None になっています"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict が None なので、ダウンロードが許可されます"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict は None で、字幕の埋め込みが許可されます"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: 制限のチェック - max_quality= {max_size} p、max_duration={max_duration}_ s、max_{max_quality}AR_0__ MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: info_dict キー: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "字幕の埋め込みをスキップしました: 長さ{duration}秒が制限{max_duration}秒を超えています"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "字幕の埋め込みをスキップしました: サイズ{size_mb:.2f}MBが制限{max_size}MBを超えています"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "字幕の埋め込みをスキップしました: 品質{width}x{height}（最小辺{min_side}p）が制限{max_quality}pを超えています"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "インスタグラム"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "プレイリスト"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ {service}の範囲制限を超えました: {count}（最大{max_count}）。\n\n利用可能な最大数のファイルをダウンロードするには、次のコマンドのいずれかを使用してください:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ {service}の範囲制限を超えました: {count}（最大{max_count}）\nユーザーID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "PO トークンプロバイダーが構成で無効になっています"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} は YouTube ドメインではないため、PO トークンをスキップします"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO トークン プロバイダーは {base_url} では利用できず、標準の YouTube 抽出にフォールバックします"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO トークン プロバイダーのキャッシュがクリアされました。次のリクエストで利用可能かどうかを確認します"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "Appインスタンスはまだ利用できません"
    HELPER_USER_NAME_MSG = "ユーザー"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood waitが検出されました。{wait_seconds}秒待機中"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood waitが検出されましたが、時間を抽出できませんでした。{retry_delay}秒待機中"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno エラーが検出されました。{retry_delay} 秒間スリープ状態になります"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "プロキシ設定が不完全です。直接接続を使用します"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚閉じる"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚閉じる"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚閉じる"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 ログファイルが削除されました。"
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 タグファイルが削除されました。"
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 フォーマットファイルが削除されました。"
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 分割ファイルが削除されました。"
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Mediainfo ファイルが削除されました。"
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 字幕設定が削除されました。"
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 キーボード設定が削除されました。"
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Args 設定が削除されました。"
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 NSFW設定が削除されました。"
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 プロキシ設定が削除されました。"
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 フラッド待機設定が削除されました。"
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚閉じる"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬ビデオダウンロードコマンド"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "使用法: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "例："
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (direct order)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (reverse order)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "参照：/audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "ユーザー {user_id} が add_bot_to_group コマンドを閉じました"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "YouTube ID を抽出できませんでした"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "サムネイルのダウンロードに失敗したか、サムネイルが大きすぎます"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "音声言語を選択してください"
    AA_NO_SUBTITLES_DETECTED_MSG = "字幕が検出されませんでした"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "字幕言語を選択してください"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "認証エラー"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "アカウントが見つかりません"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Account Unavailable"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "レート制限を超えました"
    GALLERY_DL_NETWORK_ERROR_MSG = "ネットワークエラー"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Content Unavailable"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "地理的制限"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "検証が必要です"
    GALLERY_DL_POLICY_VIOLATION_MSG = "ポリシー違反"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "不明なエラー"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ ダウンロードが開始されました</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚閉じる"
    
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
    MAGIC_VID_HELP_ALSO_SEE_MSG = "関連項目: /audio、/img、/help、/playlist、/settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Flood limit. Try later."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Cookieコマンドの使用方法</b>

<code>/cookie</code> - Cookieメニューを表示
<code>/cookie youtube</code> - YouTubeのCookieをダウンロード
<code>/cookie instagram</code> - InstagramのCookieをダウンロード
<code>/cookie tiktok</code> - TikTokのCookieをダウンロード
<code>/cookie x</code> または <code>/cookie twitter</code> - Twitter/XのCookieをダウンロード
<code>/cookie facebook</code> - FacebookのCookieをダウンロード
<code>/cookie custom</code> - カスタムCookieの手順を表示

<i>利用可能なサービスはボットの設定によって異なります。</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Cookie ファイルが削除され、キャッシュがクリアされました。"
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️前へ"
    SUBS_BACK_BUTTON_MSG = "🔙戻る"
    SUBS_OFF_BUTTON_MSG = "🚫オフ"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - 言語を設定"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - AUTO/TRANSで言語を設定"
    SUBS_VALID_OPTIONS_MSG = "有効なオプション："
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 言語"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠開発GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 GitHub を参照"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 クリーン"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪クッキー"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞メディア"
    SETTINGS_INFO_BUTTON_MSG = "📖 情報"
    SETTINGS_MORE_BUTTON_MSG = "⚙️もっと見る"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 クッキーのみ"
    SETTINGS_LOGS_BUTTON_MSG = "📃 ログ"
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ タグ"
    SETTINGS_FORMAT_BUTTON_MSG = "📼フォーマット"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ スプリット"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 メディア情報"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 字幕"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹キーボード"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ 引数"
    SETTINGS_NSFW_BUTTON_MSG = "🔞NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎プロキシ"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 洪水待ち"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑 すべてのファイル"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - 私の 5 つのクッキーをダウンロード"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - ブラウザの YT Cookie を取得します"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Cookie ファイルを検証します"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - カスタム Cookie をアップロードします"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - 品質と形式を変更する"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - メディア情報をオン/オフにします"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - 分割ビデオ部分のサイズを変更します"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - ビデオをオーディオとしてダウンロード"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - 字幕言語設定"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - プレイリストのダウンロード方法"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - gallery-dl 経由で画像をダウンロード"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - #tags を送信します"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - 手順を確認する"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - ログを送信します"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - プレイリストのヘルプ"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - ハウツー"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - 直接ビデオリンクを取得します"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - プロキシを有効/無効にします"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - キーボードレイアウト"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - インライン検索ヘルパー"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp 引数"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - NSFW ぼかし設定"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Clean Options</b>\n\nChoose what to clean:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 モバイル: @vid 検索を有効にする"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 モバイル: @vid 検索を有効にする"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴オフ"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 満席"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[画像URL]( {url} )"
    IMAGE_ERROR_MSG = "❌ エラー: {str(e)}"
    
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
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1- {max} )"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 ブラウザから"
    COOKIES_TWITTER_BUTTON_MSG = "🐦ツイッター/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 フコンタクテ"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷インスタグラム"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 あなた自身の"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ 非アクティブ (5 分間) のため、入力モードは自動的に終了します。"
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 すべてリセット"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 現在を表示"
    ARGS_BACK_BUTTON_MSG = "🔙戻る"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>このメッセージをお気に入りに転送して、これらの設定をテンプレートとして保存します。</i> \n\n<i>このメッセージをここに転送して、これらの設定を適用します。</i>"
    ARGS_NO_SETTINGS_MSG = "📋 現在のyt-dlp引数:\n\nカスタム設定が構成されていません。\n\n---\n\n<i>このメッセージをお気に入りに転送して、これらの設定をテンプレートとして保存します。</i> \n\n<i>このメッセージをここに転送して、これらの設定を適用します。</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 現在のyt-dlp引数:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 設定のエクスポート"
    ARGS_SETTINGS_READY_MSG = "設定をエクスポートする準備ができました。このメッセージをお気に入りに転送して保存します。"
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 現在の yt-dlp 引数:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ メッセージ内の設定を認識できませんでした。正しい設定テンプレートを送信したことを確認してください。"
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ 設定が正常にインポートされました!\n\n適用されたパラメータ: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "主要設定:\n"
    ARGS_ERROR_SAVING_MSG = "❌ インポートされた設定の保存中にエラーが発生しました。"
    ARGS_ERROR_IMPORTING_MSG = "❌ 設定のインポート中にエラーが発生しました。"

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Cookie ファイルをダウンロード</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Cookie ファイルをダウンロードするサービスを選択します。"
    COOKIE_MENU_SAVE_INFO_MSG = "Cookie ファイルは cookie.txt としてフォルダーに保存されます。"
    COOKIE_MENU_TIP_HEADER_MSG = "ヒント: 直接コマンドを使用することもできます。"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – Cookie をダウンロードして検証します。"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – インデックスによる特定のソースを使用します (1– {max_index} )"
    COOKIE_MENU_TIP_VERIFY_MSG = "次に、<code>/check_cookie</code> で検証します (RickRoll でテスト)。"

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "常に確認"
    SUBS_AUTO_TRANS_BUTTON_MSG = "オート/トランス"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗リンク"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Watch"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝キャプション"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ トリム"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>動画トリム</b>\n\n動画の長さ: <b>{start_time} - {end_time}</b>\n\n希望の時間範囲を次の形式で送信してください:\n<code>HH:MM:SS-HH:MM:SS</code>\n\n例: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ 無効な形式。次を使用してください: <code>HH:MM:SS-HH:MM:SS</code>\n\n例: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ 無効な範囲。開始時間は終了時間より小さくする必要があります。"
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ 時間範囲が動画の境界を超えています。\n\n動画の長さ: <b>{start_time} - {end_time}</b>\n\n範囲はこれらの制限内である必要があります。"
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>動画はトリミングされます:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ 部分的に完了 - {total_files{successful_uploads}_0__ 音声ファイルがアップロードされました。"
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ 音声が正常にダウンロードされ、送信されました - {total_files} ファイルがアップロードされました。"

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
