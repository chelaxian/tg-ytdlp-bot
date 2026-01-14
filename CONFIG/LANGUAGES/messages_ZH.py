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
    CREDITS_MSG = "<blockquote><i>由</i> @iilililiiillliiliililliilliliiil <i>管理</i>\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 更改语言: /lang</b>"
    TO_USE_MSG = "<i>要使用此机器人，您需要订阅 @tg_ytdlp Telegram 频道。</i>\n加入频道后，<b>重新发送您的视频链接，机器人将为您下载</b> ❤️\n\n<blockquote>P.S. 下载 🔞NSFW 内容和 ☁️云存储文件需要付费！1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ 不要离开频道 - 否则将被禁止使用机器人 ⛔️</blockquote>"

    ERROR1 = "未找到URL链接。请输入带有 <b>https://</b> 或 <b>http://</b> 的URL"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>播放列表 (yt-dlp)</b>

要下载播放列表，请在URL末尾发送带有 <code>*start*end</code> 范围的URL。例如：<code>URL*1*5</code>（从1到5包含的前5个视频）。<code>URL*-1*-5</code>（从1到5包含的最后5个视频）。
或者您可以使用 <code>/vid FROM-TO URL</code>。例如：<code>/vid 3-7 URL</code>（从开头下载3到7包含的视频）。<code>/vid -3-7 URL</code>（从末尾下载3到7包含的视频）。也适用于 <code>/audio</code> 命令。

<b>示例：</b>

🟥 <b>YouTube播放列表的视频范围：</b>（需要 🍪）
<code>https://youtu.be/playlist?list=PL...*1*5</code>
（下载从1到5包含的前5个视频）
🟥 <b>YouTube播放列表中的单个视频：</b>（需要 🍪）
<code>https://youtu.be/playlist?list=PL...*3*3</code>
（仅下载第3个视频）

⬛️ <b>TikTok个人资料：</b>（需要您的 🍪）
<code>https://www.tiktok.com/@USERNAME*1*10</code>
（从用户个人资料下载前10个视频）

🟪 <b>Instagram故事：</b>（需要您的 🍪）
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
（下载前3个故事）
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
（从相册下载前10个故事）

🟦 <b>VK视频：</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
（从用户/群组个人资料下载前3个视频）

⬛️<b>Rutube频道：</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
（从频道下载2到4包含的视频）

🟪 <b>Twitch剪辑：</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
（从频道下载前3个剪辑）

🟦 <b>Vimeo群组：</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
（从群组下载前2个视频）

🟧 <b>Pornhub模型：</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
（从模型个人资料下载前2个视频）
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
（根据您的提示从搜索结果下载前3个视频）

等等...
查看 <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">支持的网站列表</a>
</blockquote>

<blockquote expandable>🖼 <b>图片 (gallery-dl)</b>

使用 <code>/img URL</code> 从许多平台下载图片/照片/相册。

<b>示例：</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>范围：</b>
<code>/img 11-20 https://example.com/album</code> — 项目11..20
<code>/img 11- https://example.com/album</code> — 从11到末尾（或机器人限制）

<i>支持的平台包括 vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor 等。完整列表：</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">gallery-dl 支持的网站</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>视频下载机器人 - 帮助</b>

📥 <b>基本用法：</b>
• 发送任何链接 → 机器人下载它
  <i>机器人自动尝试通过 yt-dlp 下载视频，通过 gallery-dl 下载图片。</i>
• <b>多个URL：</b> 在质量选择模式（<code>/format</code>）下，您可以在一条消息中发送最多 <b>10个URL</b>。每个URL在新行上或由空格分隔。
• <code>/audio URL</code> → 提取音频
• <code>/link [quality] URL</code> → 获取直接链接
• <code>/proxy</code> → 启用/禁用所有下载的代理
• 回复视频并输入文本 → 更改标题

📋 <b>播放列表和范围：</b>
• <code>URL*1*5</code> → 下载前5个视频
• <code>URL*-1*-5</code> → 下载最后5个视频
• <code>/vid 3-7 URL</code> → 变为 <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → 变为 <code>URL*-3*-7</code>

🍪 <b>Cookies和私有：</b>
• 上传 *.txt cookie 用于私有视频
• <code>/cookie [service]</code> → 下载cookies（youtube/tiktok/x/custom）
• <code>/cookie youtube 1</code> → 按索引选择源（1–N）
• <code>/cookies_from_browser</code> → 从浏览器提取
• <code>/check_cookie</code> → 验证cookie
• <code>/save_as_cookie</code> → 将文本保存为cookie

🧹 <b>清理：</b>
• <code>/clean</code> → 仅媒体文件
• <code>/clean all</code> → 所有内容
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>设置：</b>
• <code>/settings</code> → 设置菜单
• <code>/format</code> → 质量和格式
• <code>/split</code> → 将视频分割成部分
• <code>/mediainfo on/off</code> → 媒体信息
• <code>/nsfw on/off</code> → NSFW模糊
• <code>/tags</code> → 查看保存的标签
• <code>/sub on/off</code> → 字幕
• <code>/keyboard</code> → 键盘（OFF/1x3/2x3）

🏷️ <b>标签：</b>
• 在URL后添加 <code>#tag1#tag2</code>
• 标签出现在标题中
• <code>/tags</code> → 查看所有标签

🔗 <b>直接链接：</b>
• <code>/link URL</code> → 最佳质量
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → 特定质量

⚙️ <b>快速命令：</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → 设置质量
• <code>/keyboard off/1x3/2x3/full</code> → 键盘布局
• <code>/split 100mb-2000mb</code> → 更改部分大小
• <code>/subs off/ru/en auto</code> → 字幕语言
• <code>/list URL</code> → 查看可用格式列表
• <code>/mediainfo on/off</code> → 开启/关闭媒体信息
• <code>/proxy on/off</code> → 启用/禁用所有下载的代理

📊 <b>信息：</b>
• <code>/usage</code> → 下载历史
• <code>/search</code> → 通过 @vid 进行内联搜索

🖼 <b>图片：</b>
• <code>URL</code> → 下载图片URL
• <code>/img URL</code> → 从URL下载图片
• <code>/img 11-20 URL</code> → 下载特定范围
• <code>/img 11- URL</code> → 从第11个下载到末尾

👨‍💻 <i>开发者：</i> @upekshaip
🤝 <i>贡献者：</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "只需将您的cookie保存为 <b><u>cookie.txt</u></b> 并将其作为文档发送给机器人。\n\n"
        "您也可以使用 <b><u>/save_as_cookie</u></b> 命令以纯文本形式发送cookies。\n"
        "<b><b><u>/save_as_cookie</u></b> 的用法：</b>\n\n"
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
        "<b><u>说明：</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>视频搜索</b>

按下下面的按钮以通过 @vid 激活内联搜索。

<blockquote>在PC上，只需在任何聊天中输入 <b>"@vid Your_Search_Query"</b>。</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 图片下载命令</b>\n\n"
        "用法：<code>/img URL</code>\n\n"
        "<b>示例：</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>支持的平台（示例）：</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor 等 — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">完整列表</a></blockquote>"
        "另请参阅："
    )
    
    LINK_HINT_MSG = (
        "获取带质量选择的直接视频链接。\n\n"
        "用法：/link + URL \n\n"
        "（例如：/link https://youtu.be/abc123）\n"
        "（例如：/link 720 https://youtu.be/abc123）"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>将机器人添加到群组</b>

将我的机器人添加到您的群组以获得增强功能和更高的限制！
————————————
📊 <b>当前免费限制（在机器人私信中）：</b>
<blockquote>•🗑 所有文件未排序的混乱垃圾 👎
• 最大1个文件大小：<b>8 GB</b>
• 最大1个文件质量：<b>无限制</b>
• 最大1个文件时长：<b>无限制</b>
• 最大下载数量：<b>无限制</b>
• 一条消息中最大URL数：<b>10</b>（仅在质量选择模式下）
• 每次最大播放列表项目：<b>50</b>
• 每次最大TikTok视频：<b>500</b>
• 每次最大图片：<b>1000</b>
• URL速率限制：<b>5/分钟，60/小时，1000/天</b>
• 命令限制：<b>20/分钟</b>
• 1次下载最大时间：<b>2小时</b>
• 🔞 NSFW内容是付费的！1⭐️ = $0.02
• 🆓 所有其他媒体完全免费
• 📝 所有内容日志和缓存到我的日志频道，以便在重新下载时即时重新发布</blockquote>

💬<b>此限制仅适用于带字幕的视频：</b>
<blockquote>• 最大视频+字幕时长：<b>1.5小时</b>
• 最大视频+字幕文件大小：<b>500 MB</b>
• 最大视频+字幕质量：<b>720p</b></blockquote>
————————————
🚀 <b>付费群组福利（2️⃣倍限制）：</b>
<blockquote>•  🗂 按主题分类的结构化整洁媒体库 👍
•  📁 机器人在您调用它们的主题中回复
•  📌 自动固定带有下载进度的状态消息
•  🖼 /img 命令将媒体下载为10项相册
• 最大1个文件大小：<b>16 GB</b> ⬆️
• 一条消息中最大URL数：<b>20</b> ⬆️（仅在质量选择模式下）
• 每次最大播放列表项目：<b>100</b> ⬆️
• 每次最大TikTok视频：1000 ⬆️
• 每次最大图片：2000 ⬆️
• URL速率限制：<b>10/分钟，120/小时，2000/天</b> ⬆️
• 命令限制：<b>40/分钟</b> ⬆️
• 1次下载最大时间：<b>4小时</b> ⬆️
• 🔞 NSFW内容：免费，包含完整元数据 🆓
• 📢 群组无需订阅我的频道
• 👥 所有群组成员都可以访问付费功能！
• 🗒 无日志/无缓存到我的日志频道！您可以在群组设置中拒绝复制/重新发布</blockquote>

💬 <b>带字幕视频的2️⃣倍限制：</b>
<blockquote>• 最大视频+字幕时长：<b>3小时</b> ⬆️
• 最大视频+字幕文件大小：<b>1000 MB</b> ⬆️
• 最大视频+字幕质量：<b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>定价和设置：</b>
<blockquote>• 价格：<b>$5/月</b> 每个群组中的1个机器人
• 设置：联系 @iilililiiillliiliililliilliliiil
• 付款：💎TON 或其他方式💲
• 支持：包含完整技术支持</blockquote>
————————————
您可以将我的机器人添加到您的群组以解锁免费 🔞<b>NSFW</b> 并将所有限制加倍（x2️⃣）。
如果您希望我允许您的群组使用我的机器人，请联系我 @iilililiiillliiliililliilliliiil
————————————
💡<b>提示：</b> <blockquote>您可以与任意数量的朋友（例如100人）一起凑钱，为整个群组进行1次购买 - 所有群组成员只需 <b>0.05$</b> 即可在该群组中完全无限制地访问所有机器人功能</blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW模式：开启✅</b>

• NSFW内容将不进行模糊处理显示。
• 剧透将不适用于NSFW媒体。
• 内容将立即可见

<i>使用 /nsfw off 启用模糊</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW模式：关闭</b>

⚠️ <b>已启用模糊</b>
• NSFW内容将被隐藏在剧透下
• 要查看，您需要点击媒体
• 剧透将适用于NSFW媒体。

<i>使用 /nsfw on 禁用模糊</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>无效参数</b>

使用：
• <code>/nsfw on</code> - 禁用模糊
• <code>/nsfw off</code> - 启用模糊
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>正在检查缓存...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 处理中..."
    DOWNLOADING_MSG = "📥 <b>正在下载媒体...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>正在下载图片...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>下载完成</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "已下载："
    SENT_STATUS_MSG = "已发送："
    PENDING_TO_SEND_STATUS_MSG = "待发送："
    TITLE_LABEL_MSG = "标题："
    MEDIA_COUNT_LABEL_MSG = "媒体数量："
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "下载完成，正在处理音频..."
    VIDEO_PROCESSING_MSG = "📽 视频正在处理..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>从缓存发送</b>\n\n已发送相册：<b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ 视频已成功从缓存发送。"
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ 播放列表视频已从缓存发送（{cached}/{total} 个文件）。"
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} 个视频已从缓存发送，正在下载缺失的..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ 从缓存发送：{cached}\n🔄 继续下载..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 无法分析媒体，继续使用最大允许范围（1-{fallback_limit}）..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 无法确定媒体数量，继续使用最大允许范围（1-{total_limit}）..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 无法确定总媒体数量，继续使用指定范围 {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>无效的URL</b>\n\n请提供以 http:// 或 https:// 开头的有效URL"

    ERROR_OCCURRED_MSG = "❌ <b>发生错误</b>\n\n<code>{url}</code>\n\n错误：{error}"

    ERROR_SENDING_VIDEO_MSG = "❌ 发送视频时出错：{error}"
    ERROR_UNKNOWN_MSG = "❌ 未知错误：{error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ 磁盘空间不足，无法下载视频。"
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ 文件大小超过 {limit} GB 限制。请在允许的大小范围内选择较小的文件。"

    ERROR_GETTING_LINK_MSG = "❌ <b>获取链接时出错：</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram已限制消息发送。\n⏳ 请等待：{time}\n要更新计时器，请再次发送URL 2次。"
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram已限制消息发送。\n⏳ 请等待：\n要更新计时器，请再次发送URL 2次。"
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ 下载字幕失败"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>直接流链接</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>标题：</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>时长：</b> {duration} 秒\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ 错误：找不到原始消息。"

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ 标签 #{tag} 包含禁止的字符。只允许字母、数字和 _。\n请使用：{example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ 播放列表视频已发送：{sent}/{total} 个文件。"
    PLAYLIST_CACHE_SENT_MSG = "✅ 从缓存发送：{cached}/{total} 个文件。"
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ 获取流链接失败"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "选择要从中下载cookies的浏览器："
    SELECT_BROWSER_NO_BROWSERS_MSG = "在此系统上未找到浏览器。您可以从远程URL下载cookies或监控浏览器状态："
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>打开浏览器</b> - 在迷你应用中监控浏览器状态"
    BROWSER_OPEN_BUTTON_MSG = "🌐 打开浏览器"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 从远程URL下载"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie文件已通过备用方式下载并保存为cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ 未找到支持的浏览器且未配置COOKIE_URL。使用 /cookie 或上传 cookie.txt。"
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ 备用COOKIE_URL必须指向.txt文件。"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ 备用cookie文件太大（>100KB）。"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ 备用cookie源不可用（状态 {status}）。尝试 /cookie 或上传 cookie.txt。"
    COOKIE_FALLBACK_ERROR_MSG = "❌ 下载备用cookie时出错。尝试 /cookie 或上传 cookie.txt。"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ 下载备用cookie时发生意外错误。"
    BTN_CLOSE = "🔚关闭"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ 无效的布尔值"
    ARGS_CLOSED_MSG = "已关闭"
    ARGS_ALL_RESET_MSG = "✅ 所有参数已重置"
    ARGS_RESET_ERROR_MSG = "❌ 重置参数时出错"
    ARGS_INVALID_PARAM_MSG = "❌ 无效参数"
    ARGS_BOOL_SET_MSG = "设置为 {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "已设置为 {value}"
    ARGS_INVALID_SELECT_MSG = "❌ 无效的选择值"
    ARGS_VALUE_SET_MSG = "设置为 {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "已设置为 {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>当前值：</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>示例：</b>\n• <code>default</code> - 使用默认XFF策略\n• <code>never</code> - 从不使用XFF标头\n• <code>US</code> - 美国国家代码\n• <code>GB</code> - 英国国家代码\n• <code>DE</code> - 德国国家代码\n• <code>FR</code> - 法国国家代码\n• <code>JP</code> - 日本国家代码\n• <code>192.168.1.0/24</code> - IP块（CIDR）\n• <code>10.0.0.0/8</code> - 私有IP范围\n• <code>203.0.113.0/24</code> - 公共IP块\n\n"
    ARGS_XFF_NOTE_MSG = "<b>注意：</b> 这将替换 --geo-bypass 选项。使用任何2字母国家代码或CIDR表示法的IP块。\n\n"
    ARGS_EXAMPLE_MSG = "<b>示例：</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "请发送您的新值。"
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>范围：</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "请发送一个数字。"
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>示例：</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>注意：</b> 这些标头将添加到现有的Referer和User-Agent标头中。\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 当前yt-dlp参数：</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>布尔值</b> - 真/假开关\n• 📋 <b>选择</b> - 从选项中选择\n• 🔢 <b>数字</b> - 数字输入\n• 📝🔧 <b>文本</b> - 文本/JSON输入</blockquote>\n\n这些设置将应用于您的所有下载。"
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "强制IPv6连接",
        "force_ipv4": "强制IPv4连接", 
        "no_live_from_start": "不从开始下载直播流",
        "live_from_start": "从开始下载直播流",
        "no_check_certificates": "抑制HTTPS证书验证",
        "check_certificate": "检查SSL证书",
        "no_playlist": "仅下载单个视频，不下载播放列表",
        "embed_metadata": "在视频文件中嵌入元数据",
        "embed_thumbnail": "在视频文件中嵌入缩略图",
        "write_thumbnail": "将缩略图写入文件",
        "ignore_errors": "忽略下载错误并继续",
        "legacy_server_connect": "允许旧版服务器连接",
        "concurrent_fragments": "并发下载的片段数量",
        "xff": "X-Forwarded-For标头策略",
        "user_agent": "User-Agent标头",
        "impersonate": "浏览器模拟",
        "referer": "Referer标头",
        "geo_bypass": "绕过地理限制",
        "hls_use_mpegts": "对HLS使用MPEG-TS",
        "no_part": "不使用.part文件",
        "no_continue": "不恢复部分下载",
        "audio_format": "音频格式",
        "video_format": "视频格式",
        "merge_output_format": "合并输出格式",
        "send_as_file": "作为文件发送",
        "username": "用户名",
        "password": "密码",
        "twofactor": "双因素认证代码",
        "min_filesize": "最小文件大小（MB）",
        "max_filesize": "最大文件大小（MB）",
        "playlist_items": "播放列表项目",
        "date": "日期",
        "datebefore": "日期之前",
        "dateafter": "日期之后",
        "http_headers": "HTTP标头",
        "sleep_interval": "睡眠间隔",
        "max_sleep_interval": "最大睡眠间隔",
        "retries": "重试次数",
        "http_chunk_size": "HTTP块大小",
        "sleep_subtitles": "字幕睡眠"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp参数配置</b>\n\n<blockquote>📋 <b>组：</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp参数配置</b>\n\n"
        "<blockquote>📋 <b>组：</b>\n"
        "• ✅/❌ <b>布尔值</b> - 真/假开关\n"
        "• 📋 <b>选择</b> - 从选项中选择\n"
        "• 🔢 <b>数字</b> - 数字输入\n"
        "• 📝🔧 <b>文本</b> - 文本/JSON输入</blockquote>\n\n"
        "这些设置将应用于您的所有下载。"
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ 请稍候..."
    ERROR_OCCURRED_SHORT_MSG = "❌ 发生错误"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ 由于不活动，输入模式自动关闭（5分钟）。"
    ARGS_INPUT_DANGEROUS_MSG = "❌ 输入包含潜在危险内容：{pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ 输入太长（最多1000个字符）"
    ARGS_INVALID_URL_MSG = "❌ 无效的URL格式。必须以 http:// 或 https:// 开头"
    ARGS_INVALID_JSON_MSG = "❌ 无效的JSON格式"
    ARGS_NUMBER_RANGE_MSG = "❌ 数字必须在 {min_val} 和 {max_val} 之间"
    ARGS_INVALID_NUMBER_MSG = "❌ 无效的数字格式"
    ARGS_DATE_FORMAT_MSG = "❌ 日期必须为YYYYMMDD格式（例如：20230930）"
    ARGS_YEAR_RANGE_MSG = "❌ 年份必须在1900和2100之间"
    ARGS_MONTH_RANGE_MSG = "❌ 月份必须在01和12之间"
    ARGS_DAY_RANGE_MSG = "❌ 日期必须在01和31之间"
    ARGS_INVALID_DATE_MSG = "❌ 无效的日期格式"
    ARGS_INVALID_XFF_MSG = "❌ XFF必须是'default'、'never'、国家代码（例如：US）或IP块（例如：192.168.1.0/24）"
    ARGS_NO_CUSTOM_MSG = "未设置自定义参数。所有参数使用默认值。"
    ARGS_RESET_SUCCESS_MSG = "✅ 所有参数已重置为默认值。"
    ARGS_TEXT_TOO_LONG_MSG = "❌ 文本太长。最多500个字符。"
    ARGS_ERROR_PROCESSING_MSG = "❌ 处理输入时出错。请重试。"
    ARGS_BOOL_INPUT_MSG = "❌ 请输入'True'或'False'用于'作为文件发送'选项。"
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ 请提供有效的数字。"
    ARGS_BOOL_VALUE_REQUEST_MSG = "请发送 <code>True</code> 或 <code>False</code> 以启用/禁用此选项。"
    ARGS_JSON_VALUE_REQUEST_MSG = "请发送有效的JSON。"
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "您还没有标签。"
    TAGS_MESSAGE_CLOSED_MSG = "标签消息已关闭。"
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ 字幕已禁用，始终询问模式已关闭。"
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ 字幕始终询问已启用。"
    SUBS_LANGUAGE_SET_MSG = "✅ 字幕语言设置为：{flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️警告：由于CPU影响高，此功能非常慢（接近实时）并限制为：\n"
        "- 最大质量720p\n"
        "- 最大时长1.5小时\n"
        "- 最大视频大小500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>快速命令：</b>\n"
        "• <code>/subs off</code> - 禁用字幕\n"
        "• <code>/subs on</code> - 启用始终询问模式\n"
        "• <code>/subs ru</code> - 设置语言\n"
        "• <code>/subs ru auto</code> - 使用AUTO/TRANS设置语言"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 字幕已禁用"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} 所选语言：{name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 正在下载字幕..."
    SUBS_DISABLED_ERROR_MSG = "❌ 字幕已禁用。使用 /subs 进行配置。"
    SUBS_YOUTUBE_ONLY_MSG = "❌ 字幕下载仅支持YouTube。"
    SUBS_CAPTION_MSG = (
        "<b>💬 字幕</b>\n\n"
        "<b>视频：</b> {title}\n"
        "<b>语言：</b> {lang}\n"
        "<b>类型：</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 字幕SRT文件已发送给用户。"
    SUBS_ERROR_PROCESSING_MSG = "❌ 处理字幕文件时出错。"
    SUBS_ERROR_DOWNLOAD_MSG = "❌ 下载字幕失败。"
    SUBS_ERROR_MSG = "❌ 下载字幕时出错：{error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ 分割部分大小设置为：{size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **无效的大小！**\n\n"
        "**有效范围：** 100MB到2GB\n\n"
        "**有效格式：**\n"
        "• `100mb` 到 `2000mb`（兆字节）\n"
        "• `0.1gb` 到 `2gb`（千兆字节）\n\n"
        "**示例：**\n"
        "• `/split 100mb` - 100兆字节\n"
        "• `/split 500mb` - 500兆字节\n"
        "• `/split 1.5gb` - 1.5千兆字节\n"
        "• `/split 2gb` - 2千兆字节\n"
        "• `/split 2000mb` - 2000兆字节（2GB）\n\n"
        "**预设：**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **选择视频分割的最大部分大小：**\n\n"
        "**范围：** 100MB到2GB\n\n"
        "**快速命令：**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**示例：** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "菜单已关闭。"
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>机器人设置</b>\n\n选择一个类别："
    SETTINGS_MENU_CLOSED_MSG = "菜单已关闭。"
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 清理选项</b>\n\n选择要清理的内容："
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\n选择一个操作："
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 媒体</b>\n\n选择一个操作："
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 信息</b>\n\n选择一个操作："
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ 更多命令</b>\n\n选择一个操作："
    SETTINGS_COMMAND_EXECUTED_MSG = "命令已执行。"
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ 洪水限制。请稍后再试。"
    SETTINGS_HINT_SENT_MSG = "提示已发送。"
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "搜索助手已打开。"
    SETTINGS_UNKNOWN_COMMAND_MSG = "未知命令。"
    SETTINGS_HINT_CLOSED_MSG = "提示已关闭。"
    SETTINGS_HELP_SENT_MSG = "向用户发送帮助文本"
    SETTINGS_MENU_OPENED_MSG = "已打开 /settings 菜单"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 搜索助手已关闭"
    SEARCH_CLOSED_MSG = "已关闭"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ 代理 {status}。"
    PROXY_ERROR_SAVING_MSG = "❌ 保存代理设置时出错。"
    PROXY_MENU_TEXT_MSG = "启用或禁用代理服务器用于所有yt-dlp操作？"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "启用或禁用代理服务器（{count} 个可用）用于所有yt-dlp操作？\n\n启用后，将使用 {method} 方法选择代理。"
    PROXY_MENU_CLOSED_MSG = "菜单已关闭。"
    PROXY_ENABLED_CONFIRM_MSG = "✅ 代理已启用。所有yt-dlp操作将使用代理。"
    PROXY_ENABLED_MULTIPLE_MSG = "✅ 代理已启用。所有yt-dlp操作将使用 {count} 个代理服务器，采用 {method} 选择方法。"
    PROXY_DISABLED_MSG = "❌ 代理已禁用。"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ 保存代理设置时出错。"
    PROXY_ENABLED_CALLBACK_MSG = "代理已启用。"
    PROXY_DISABLED_CALLBACK_MSG = "代理已禁用。"
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ 请等待您之前的下载完成"
    AUDIO_HELP_MSG = (
        "<b>🎧 音频下载命令</b>\n\n"
        "用法：<code>/audio URL</code>\n\n"
        "<b>示例：</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "另请参阅：/vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "音频提示已关闭。"
    PLAYLIST_HELP_CLOSED_MSG = "播放列表帮助已关闭。"
    USERLOGS_CLOSED_MSG = "日志消息已关闭。"
    HELP_CLOSED_MSG = "帮助已关闭。"
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW模糊设置</b>\n\nNSFW内容为 <b>{status}</b>。\n\n选择是否模糊NSFW内容："
    NSFW_MENU_CLOSED_MSG = "菜单已关闭。"
    NSFW_BLUR_DISABLED_MSG = "NSFW模糊已禁用。"
    NSFW_BLUR_ENABLED_MSG = "NSFW模糊已启用。"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW模糊已禁用。"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW模糊已启用。"
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}。"
    MEDIAINFO_MENU_TITLE_MSG = "启用或禁用为下载的文件发送MediaInfo？"
    MEDIAINFO_MENU_CLOSED_MSG = "菜单已关闭。"
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo已启用。下载后，将发送文件信息。"
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo已禁用。"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo已启用。"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo已禁用。"
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 列出可用格式</b>\n\n"
        "获取URL的可用视频/音频格式。\n\n"
        "<b>用法：</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>示例：</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 如何使用格式ID：</b>\n"
        "获取列表后，使用特定的格式ID：\n"
        "• <code>/format id 401</code> - 下载格式401\n"
        "• <code>/format id401</code> - 同上\n"
        "• <code>/format id140 audio</code> - 将格式140下载为MP3音频\n\n"
        "此命令将显示所有可以下载的可用格式。"
    )
    LIST_PROCESSING_MSG = "🔄 正在获取可用格式..."
    LIST_INVALID_URL_MSG = "❌ 请提供以 http:// 或 https:// 开头的有效URL"
    LIST_CAPTION_MSG = (
        "📃 可用格式：\n<code>{url}</code>\n\n"
        "💡 <b>如何设置格式：</b>\n"
        "• <code>/format id 134</code> - 下载特定格式ID\n"
        "• <code>/format 720p</code> - 按质量下载\n"
        "• <code>/format best</code> - 下载最佳质量\n"
        "• <code>/format ask</code> - 始终询问质量\n\n"
        "{audio_note}\n"
        "📋 使用上面列表中的格式ID"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>仅音频格式：</b> {formats}\n"
        "• <code>/format id 140 audio</code> - 将格式140下载为MP3音频\n"
        "• <code>/format id140 audio</code> - 同上\n"
        "这些将作为MP3音频文件下载。\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ 发送格式文件时出错：{error}"
    LIST_ERROR_GETTING_MSG = "❌ 获取格式失败：\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ 处理命令时发生错误"
    LIST_ERROR_CALLBACK_MSG = "发生错误"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 如何使用格式ID：\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "获取列表后，使用特定的格式ID：\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - 下载格式401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - 同上\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - 将格式140下载为MP3音频\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - 同上\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 检测到仅音频格式：{formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "这些格式将作为MP3音频文件下载。\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>仅视频格式：</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 使用上面列表中的格式ID"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>用法：</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>示例：</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - 最佳质量\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p或更低\n"
        "• /link 720p https://youtube.com/watch?v=... - 同上\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K或更低\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K或更低"
        "</blockquote>\n\n"
        "<b>质量：</b> 从1到10000（例如：144, 240, 720, 1080）"
    )
    LINK_INVALID_URL_MSG = "❌ 请提供有效的URL"
    LINK_PROCESSING_MSG = "🔗 正在获取直接链接..."
    LINK_DURATION_MSG = "⏱ <b>时长：</b> {duration} 秒\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>视频流：</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>音频流：</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **键盘设置已更新！**\n\n新设置：**{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **无效参数！**\n\n"
        "有效选项：`off`, `1x3`, `2x3`, `full`\n\n"
        "示例：`/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **键盘设置**\n\n"
        "当前：**{current}**\n\n"
        "选择一个选项：\n\n"
        "或使用：`/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 键盘已激活！"
    KEYBOARD_HIDDEN_MSG = "⌨️ 键盘已隐藏"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3键盘已激活！"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3键盘已激活！"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 表情符号键盘已激活！"
    KEYBOARD_ERROR_APPLYING_MSG = "应用键盘设置 {setting} 时出错：{error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ 格式设置为：始终询问。每次发送URL时都会提示您选择质量。"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ 格式设置为：始终询问。现在每次发送URL时都会提示您选择质量。"
    FORMAT_BEST_UPDATED_MSG = "✅ 格式已更新为最佳质量（AVC+MP4优先级）：\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ 格式已更新为ID {id}：\n{format}\n\n💡 <b>注意：</b> 如果这是仅音频格式，它将作为MP3音频文件下载。"
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ 格式已更新为ID {id}（仅音频）：\n{format}\n\n💡 这将作为MP3音频文件下载。"
    FORMAT_QUALITY_UPDATED_MSG = "✅ 格式已更新为质量 {quality}：\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ 格式已更新为：\n{format}"
    FORMAT_MENU_MSG = (
        "选择一个格式选项或使用以下方式发送自定义格式：\n"
        "• <code>/format &lt;format_string&gt;</code> - 自定义格式\n"
        "• <code>/format 720</code> - 720p质量\n"
        "• <code>/format 4k</code> - 4K质量\n"
        "• <code>/format 8k</code> - 8K质量\n"
        "• <code>/format id 401</code> - 特定格式ID\n"
        "• <code>/format ask</code> - 始终显示菜单\n"
        "• <code>/format best</code> - bv+ba/最佳质量"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "要使用自定义格式，请以以下形式发送命令：\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "将 <code>bestvideo+bestaudio/best</code> 替换为您想要的格式字符串。"
    )
    FORMAT_RESOLUTION_MENU_MSG = "选择您想要的分辨率和编解码器："
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ 格式设置为：始终询问。现在每次发送URL时都会提示您选择质量。"
    FORMAT_UPDATED_MSG = "✅ 格式已更新为：\n{format}"
    FORMAT_SAVED_MSG = "✅ 格式已保存。"
    FORMAT_CHOICE_UPDATED_MSG = "✅ 格式选择已更新。"
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "自定义格式菜单已关闭"
    FORMAT_CODEC_SET_MSG = "✅ 编解码器设置为 {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ 浏览器选择已更新。"
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ 访问被拒绝。仅限管理员。"
    ACCESS_DENIED_ADMIN = "❌ 访问被拒绝。仅限管理员。"
    WELCOME_MASTER = "欢迎主人 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ 抱歉...下载过程中发生了一些错误。"
    SIZE_LIMIT_EXCEEDED = "❌ 文件大小超过 {max_size_gb} GB 限制。请在允许的大小范围内选择较小的文件。"
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ 未找到脚本：{script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ 正在使用 {script_path} 下载新的Firebase转储..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase缓存已成功重新加载！"
    ADMIN_CACHE_FAILED_MSG = "❌ 重新加载Firebase缓存失败。请检查 {cache_file} 是否存在。"
    ADMIN_ERROR_RELOADING_MSG = "❌ 重新加载缓存时出错：{error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ 运行 {script_path} 时出错：\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ 促销消息已发送给所有其他用户</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ 无法发送促销消息。请尝试回复消息\n或发生了某些错误</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ 用户尚未下载任何内容...</b> 日志中不存在"
    ADMIN_INVALID_COMMAND_MSG = "❌ 无效命令"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ 在缓存中未找到 <code>{{path}}</code> 的数据"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ 队列为空 — 还没有人离开频道。"
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>封禁队列</b>\n待处理总数：{total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username}（离开时间：{last_left}）"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… 还有 {extra} 个用户。"
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "使用 /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ 从队列中封禁用户：{count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ 自动封禁已启用：新的离开者将立即被封禁。"
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ 自动封禁已禁用。"
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ 计划的自动封禁窗口设置为每 {interval}。"
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 过去 {hours} 小时（2天）的频道活动日志。"
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 过去 {hours} 小时（2天）：加入 {joined}，离开 {left}。"
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ 过去 {hours} 小时（2天）没有活动。"
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "总计：🟢 {joined} 加入，🔴 {left} 离开。"
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ 无法访问频道活动日志。机器人无法读取管理员日志。在配置中提供带有用户会话的 CHANNEL_GUARD_SESSION_STRING 以启用此功能。"
    BAN_TIME_USAGE_MSG = "❌ 用法：{command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ 使用格式如 10s, 6m, 5h, 4d, 3w, 2M 或 1y。"
    BAN_TIME_SET_MSG = "🕒 频道日志扫描间隔设置为 {interval}。"
    BAN_TIME_REPORT_MSG = (
        "🛡️ 频道扫描报告\n"
        "运行时间：{run_ts}\n"
        "间隔：{interval}\n"
        "新离开者：{new_leavers}\n"
        "自动封禁：{auto_banned}\n"
        "待处理：{pending}\n"
        "最后事件ID：{last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ 用法：/block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 管理员不能删除管理员"
    ADMIN_USER_BLOCKED_MSG = "用户已封禁 🔒❌\n \nID：<code>{user_id}</code>\n封禁日期：{date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> 已被封禁 ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 抱歉！您不是管理员"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ 用法：/unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "用户已解封 🔓✅\n \nID：<code>{user_id}</code>\n解封日期：{date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> 已解封 ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ 已解封用户：{count}\n⏱ 时间戳：{date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ 用法：/ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "用户已忽略 👁️❌\n \nID：<code>{user_id}</code>\n忽略日期：{date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> 已被忽略 ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ 用法：/unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "用户不再被忽略 👁️✅\n \nID：<code>{user_id}</code>\n取消忽略日期：{date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> 未被忽略 ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>机器人运行时间 -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ 请提供要清除缓存的URL。\n用法：<code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ 请提供有效的URL。\n用法：<code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ URL的缓存已成功清除：\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ 未找到此链接的缓存。"
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ 清除缓存时出错：{error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ 访问被拒绝。仅限管理员。"
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ 正在运行色情列表更新脚本：{script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ 脚本已成功完成！"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ 脚本已成功完成！\n\n输出：\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ 脚本失败，返回代码 {returncode}：\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ 运行脚本时出错：{error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ 正在重新加载色情和域名相关缓存..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ 色情缓存已成功重新加载！\n\n"
        "📊 当前缓存状态：\n"
        "• 色情域名：{porn_domains}\n"
        "• 色情关键词：{porn_keywords}\n"
        "• 支持的网站：{supported_sites}\n"
        "• 白名单：{whitelist}\n"
        "• 灰名单：{greylist}\n"
        "• 黑名单：{black_list}\n"
        "• 白关键词：{white_keywords}\n"
        "• 代理域名：{proxy_domains}\n"
        "• 代理2域名：{proxy_2_domains}\n"
        "• 清理查询：{clean_query}\n"
        "• 无Cookie域名：{no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ 重新加载色情缓存时出错：{error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ 请提供要检查的URL。\n用法：<code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ 请提供有效的URL。\n用法：<code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 正在检查URL的NSFW内容...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>色情检查结果</b>\n\n"
        "<b>URL：</b> <code>{url}</code>\n"
        "<b>状态：</b> <b>{status_text}</b>\n\n"
        "<b>说明：</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ 检查URL时出错：{error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Cookies已清理。"
    CLEAN_LOGS_CLEANED_MSG = "日志已清理。"
    CLEAN_TAGS_CLEANED_MSG = "标签已清理。"
    CLEAN_FORMAT_CLEANED_MSG = "格式已清理。"
    CLEAN_SPLIT_CLEANED_MSG = "分割已清理。"
    CLEAN_MEDIAINFO_CLEANED_MSG = "媒体信息已清理。"
    CLEAN_SUBS_CLEANED_MSG = "字幕设置已清理。"
    CLEAN_KEYBOARD_CLEANED_MSG = "键盘设置已清理。"
    CLEAN_ARGS_CLEANED_MSG = "参数设置已清理。"
    CLEAN_NSFW_CLEANED_MSG = "NSFW设置已清理。"
    CLEAN_PROXY_CLEANED_MSG = "代理设置已清理。"
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "洪水等待设置已清理。"
    CLEAN_ALL_CLEANED_MSG = "所有文件已清理。"
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\n选择一个操作："
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Cookie文件已保存"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ 跳过非YouTube cookies的验证"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Cookie文件存在但格式不正确"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ 未找到Cookie文件。"
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 正在启动YouTube cookies测试...\n\n请稍候，我正在检查和验证您的cookies。"
    COOKIES_YOUTUBE_WORKING_MSG = "✅ 您现有的YouTube cookies工作正常！\n\n无需下载新的。"
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ 您现有的YouTube cookies已过期或无效。\n\n🔄 正在下载新的cookies..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} cookie源未配置！"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} cookie源必须是.txt文件！"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ 范围限制超出：请求了 {range_count} 个文件（最大 {max_img_files}）。\n\n使用以下命令之一下载最大可用文件：\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚关闭"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ 媒体限制超出：请求了 {count} 个文件（最大 {max_count}）。\n\n使用以下命令之一下载最大可用文件：\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 从链接中找到 <b>{count}</b> 个媒体项目"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "选择下载范围："
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "浏览器模拟"
    ARGS_REFERER_DESC_MSG = "Referer标头"
    ARGS_USER_AGENT_DESC_MSG = "User-Agent标头"
    ARGS_GEO_BYPASS_DESC_MSG = "绕过地理限制"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "检查SSL证书"
    ARGS_LIVE_FROM_START_DESC_MSG = "从开始下载直播流"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "不从开始下载直播流"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "对HLS视频使用MPEG-TS容器"
    ARGS_NO_PLAYLIST_DESC_MSG = "仅下载单个视频，不下载播放列表"
    ARGS_NO_PART_DESC_MSG = "不使用.part文件"
    ARGS_NO_CONTINUE_DESC_MSG = "不恢复部分下载"
    ARGS_AUDIO_FORMAT_DESC_MSG = "提取的音频格式"
    ARGS_EMBED_METADATA_DESC_MSG = "在视频文件中嵌入元数据"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "在视频文件中嵌入缩略图"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "将缩略图写入文件"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "并发下载的片段数量"
    ARGS_FORCE_IPV4_DESC_MSG = "强制IPv4连接"
    ARGS_FORCE_IPV6_DESC_MSG = "强制IPv6连接"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For标头策略"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP块大小（字节）"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "字幕下载前睡眠（秒）"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "允许旧版服务器连接"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "抑制HTTPS证书验证"
    ARGS_USERNAME_DESC_MSG = "账户用户名"
    ARGS_PASSWORD_DESC_MSG = "账户密码"
    ARGS_TWOFACTOR_DESC_MSG = "双因素认证代码"
    ARGS_IGNORE_ERRORS_DESC_MSG = "忽略下载错误并继续"
    ARGS_MIN_FILESIZE_DESC_MSG = "最小文件大小（MB）"
    ARGS_MAX_FILESIZE_DESC_MSG = "最大文件大小（MB）"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "要下载的播放列表项目（例如：1,3,5 或 1-5）"
    ARGS_DATE_DESC_MSG = "下载在此日期上传的视频（YYYYMMDD）"
    ARGS_DATEBEFORE_DESC_MSG = "下载在此日期之前上传的视频（YYYYMMDD）"
    ARGS_DATEAFTER_DESC_MSG = "下载在此日期之后上传的视频（YYYYMMDD）"
    ARGS_HTTP_HEADERS_DESC_MSG = "自定义HTTP标头（JSON）"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "请求之间的睡眠间隔（秒）"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "最大睡眠间隔（秒）"
    ARGS_RETRIES_DESC_MSG = "重试次数"
    ARGS_VIDEO_FORMAT_DESC_MSG = "视频容器格式"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "合并的输出容器格式"
    ARGS_SEND_AS_FILE_DESC_MSG = "将所有媒体作为文档而不是媒体发送"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "模拟"
    ARGS_REFERER_SHORT_MSG = "引用来源"
    ARGS_GEO_BYPASS_SHORT_MSG = "地理绕过"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "检查证书"
    ARGS_LIVE_FROM_START_SHORT_MSG = "直播开始"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "不直播开始"
    ARGS_USER_AGENT_SHORT_MSG = "用户代理"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "无播放列表"
    ARGS_NO_PART_SHORT_MSG = "无Part"
    ARGS_NO_CONTINUE_SHORT_MSG = "不继续"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "音频格式"
    ARGS_EMBED_METADATA_SHORT_MSG = "嵌入元数据"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "嵌入缩略图"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "写入缩略图"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "并发"
    ARGS_FORCE_IPV4_SHORT_MSG = "强制IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "强制IPv6"
    ARGS_XFF_SHORT_MSG = "XFF标头"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "块大小"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "字幕睡眠"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "旧版连接"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "不检查证书"
    ARGS_USERNAME_SHORT_MSG = "用户名"
    ARGS_PASSWORD_SHORT_MSG = "密码"
    ARGS_TWOFACTOR_SHORT_MSG = "双因素认证"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "忽略错误"
    ARGS_MIN_FILESIZE_SHORT_MSG = "最小大小"
    ARGS_MAX_FILESIZE_SHORT_MSG = "最大大小"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "播放列表项目"
    ARGS_DATE_SHORT_MSG = "日期"
    ARGS_DATEBEFORE_SHORT_MSG = "日期之前"
    ARGS_DATEAFTER_SHORT_MSG = "日期之后"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP标头"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "睡眠间隔"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "最大睡眠"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "视频格式"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "合并格式"
    ARGS_SEND_AS_FILE_SHORT_MSG = "作为文件发送"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ 文件太大。最大大小为100 KB。"
    COOKIES_INVALID_FORMAT_MSG = "❌ 只允许以下格式的文件.txt。"
    COOKIES_INVALID_COOKIE_MSG = "❌ 该文件看起来不像cookie.txt（没有'# Netscape HTTP Cookie File'行）。"
    COOKIES_ERROR_READING_MSG = "❌ 读取文件时出错：{error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Cookie文件存在且格式正确"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} cookie文件太大！最大100KB，得到{size}KB。"
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} cookie文件已下载并保存为您文件夹中的cookie.txt。</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} cookie源不可用（状态 {status}）。请稍后再试。"
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ 下载{service} cookie文件时出错。请稍后再试。"
    COOKIES_USER_PROVIDED_MSG = "<b>✅ 用户提供了新的cookie文件。</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie已成功更新：</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ 不是有效的cookie。</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube cookie源未配置！"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 正在下载并检查YouTube cookies...\n\n尝试 {attempt} / {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ 访问被拒绝。仅限管理员。"
    ADMIN_USER_LOGS_TOTAL_MSG = "总计：<b>{total}</b>\n<b>{user_id}</b> - 日志（最近10条）：\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 键盘已激活！"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ 字幕语言设置为：{flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ 字幕语言设置为：{flag} {name}，已启用AUTO/TRANS。"
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "字幕语言菜单已关闭。"
    SUBS_DOWNLOADING_MSG = "💬 正在下载字幕..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 正在将Firebase缓存重新加载到内存中..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ 未配置COOKIE_URL。使用 /cookie 或上传 cookie.txt。"
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 正在从远程URL下载cookies..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ 备用COOKIE_URL必须指向.txt文件。"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ 备用cookie文件太大（>100KB）。"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie文件已通过备用方式下载并保存为cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ 备用cookie源不可用（状态 {status}）。尝试 /cookie 或上传 cookie.txt。"
    COOKIE_FALLBACK_ERROR_MSG = "❌ 下载备用cookie时出错。尝试 /cookie 或上传 cookie.txt。"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ 下载备用cookie时发生意外错误。"
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} 浏览器未安装。"
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ 使用浏览器保存的cookies：{browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ 保存cookies失败：{error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube cookies工作正常"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube cookies已过期或无效\n\n使用 /cookie 获取新的cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - 自定义格式\n• <code>/format 720</code> - 720p质量\n• <code>/format 4k</code> - 4K质量"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "提示已发送。"
    FORMAT_MKV_TOGGLE_MSG = "MKV现在为 {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ 未配置远程URL"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ 无效的文件格式"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ 文件太大"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookies已成功下载"
    COOKIES_SERVER_ERROR_MSG = "❌ 服务器错误 {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ 下载失败"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ 意外错误"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ 浏览器未安装。"
    COOKIES_MENU_CLOSED_MSG = "菜单已关闭。"
    COOKIES_HINT_CLOSED_MSG = "Cookie提示已关闭。"
    IMG_HELP_CLOSED_MSG = "帮助已关闭。"
    SUBS_LANGUAGE_UPDATED_MSG = "字幕语言设置已更新。"
    SUBS_MENU_CLOSED_MSG = "字幕语言菜单已关闭。"
    KEYBOARD_SET_TO_MSG = "键盘设置为 {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "处理设置时出错"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo已启用。"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo已禁用。"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW模糊已禁用。"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW模糊已启用。"
    SETTINGS_MENU_CLOSED_MSG = "菜单已关闭。"
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "洪水等待激活。请稍后再试。"
    OTHER_HELP_CLOSED_MSG = "帮助已关闭。"
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "日志消息已关闭。"
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "菜单已关闭。"
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "无效的大小。"
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ 发送MediaInfo时出错：{error}"
    LINK_ERROR_OCCURRED_MSG = "❌ 发生错误：{error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - 所有日志"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - 所有 {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 从远程URL下载"
    BROWSER_OPEN_BUTTON_MSG = "🌐 打开浏览器"
    SELECT_BROWSER_MSG = "选择要从中下载cookies的浏览器："
    SELECT_BROWSER_NO_BROWSERS_MSG = "在此系统上未找到浏览器。您可以从远程URL下载cookies或监控浏览器状态："
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>打开浏览器</b> - 在迷你应用中监控浏览器状态"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ 运行 /check_cookie 失败"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ 洪水限制。请稍后再试。"
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ 打开浏览器cookie菜单失败"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "保存为cookie提示已关闭。"
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>用法：</b>\n<code>/link [quality] URL</code>\n\n<b>示例：</b>\n<blockquote>• /link https://youtube.com/watch?v=... - 最佳质量\n• /link 720 https://youtube.com/watch?v=... - 720p或更低\n• /link 720p https://youtube.com/watch?v=... - 同上\n• /link 4k https://youtube.com/watch?v=... - 4K或更低\n• /link 8k https://youtube.com/watch?v=... - 8K或更低</blockquote>\n\n<b>质量：</b> 从1到10000（例如：144, 240, 720, 1080）"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K质量"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>已获得直接链接</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>格式：</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>音频流：</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ 获取流链接失败"
    LINK_ERROR_GETTING_MSG = "❌ <b>获取链接时出错：</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ 无效的YouTube cookie索引：{selected_index}。可用范围是1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 正在下载并检查YouTube cookies...\n\n尝试 {attempt} / {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 正在下载并检查YouTube cookies...\n\n尝试 {attempt} / {total}\n🔍 正在测试cookies..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube cookies已成功下载并验证！\n\n使用源 {source} / {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ 所有YouTube cookies已过期或不可用！\n\n请联系机器人管理员替换它们。"
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube cookie重试限制已超出！\n\n🔢 最大：每小时 {limit} 次尝试\n⏰ 请稍后再试"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ 标签 #{wrong} 包含禁止的字符。只允许字母、数字和 _。\n请使用：{example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **无效参数！**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ 字幕语言设置：{flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "示例：`/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} 所选语言：{name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ 始终询问模式 {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 字幕已禁用"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 字幕设置</b>\n\n{status_text}\n\n选择字幕语言：\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - 禁用字幕\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 字幕设置</b>\n\n{status_text}\n\n选择字幕语言："
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>标题：</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>时长：</b> {duration} 秒\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>视频流：</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 最大质量720p\n- 最大时长1.5小时\n- 最大视频大小500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️警告：由于CPU影响高，此功能非常慢（接近实时）并限制为：\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>快速命令：</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - 禁用字幕\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - 启用始终询问模式\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - 设置语言\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - 设置语言并启用AUTO/TRANS\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - 启用始终询问模式\n"
    SUBS_AUTO_SUBS_TEXT = "（自动字幕）"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ 自动字幕模式 {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "字幕通过命令禁用：{arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "字幕始终询问通过命令启用：{arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "字幕语言通过命令设置：{arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "字幕语言+自动模式通过命令设置：{arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "用户打开了 /subs 菜单。"
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "用户将字幕语言设置为：{lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "用户将AUTO/TRANS模式切换为：{new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "用户将始终询问模式切换为：{new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "用户请求从浏览器获取cookies。"
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "浏览器选择键盘已发送，仅包含已安装的浏览器。"
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "浏览器选择已关闭。"
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "备用COOKIE_URL使用成功（源已隐藏）"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "备用COOKIE_URL失败：status={status}（已隐藏）"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "备用COOKIE_URL意外错误：{error_type}：{error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "浏览器 {browser} 未安装。"
    COOKIES_SAVED_BROWSER_LOG_MSG = "使用浏览器保存的cookies：{browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "为用户 {user_id} 保存了cookie文件。"
    COOKIES_FILE_WORKING_LOG_MSG = "Cookie文件存在，格式正确，YouTube cookies工作正常。"
    COOKIES_FILE_EXPIRED_LOG_MSG = "Cookie文件存在且格式正确，但YouTube cookies已过期。"
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Cookie文件存在且格式正确。"
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Cookie文件存在但格式不正确。"
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "未找到cookie文件。"
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{service} cookie URL 对于用户 {user_id} 为空。"
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} cookie URL 不是.txt（已隐藏）"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} cookie文件太大：{size} 字节（源已隐藏）"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{service} cookie文件已为用户 {user_id} 下载（源已隐藏）。"
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "未找到脚本：{script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "发送初始状态消息失败"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "运行 {script_path} 时出错：{stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Firebase缓存已由自动任务重新加载。"
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Firebase缓存已由管理员重新加载。"
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "重新加载Firebase缓存时出错：{error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "广播已启动。文本：\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "广播消息已发送给所有用户。"
    ADMIN_BROADCAST_FAILED_LOG_MSG = "广播消息失败：{error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "管理员 {user_id} 清除了URL的缓存：{url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "管理员 {user_id} 启动了色情列表更新脚本：{script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "色情列表更新脚本已由管理员 {user_id} 成功完成"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "色情列表更新脚本由管理员 {user_id} 失败：{error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "管理员 {user_id} 尝试运行不存在的脚本：{script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "管理员 {user_id} 运行色情更新脚本时出错：{error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "管理员 {user_id} 启动了色情缓存重新加载"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "管理员 {user_id} 重新加载色情缓存时出错：{error}"
    ADMIN_PORN_CHECK_LOG_MSG = "管理员 {user_id} 检查URL的NSFW：{url} - 结果：{status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "用户请求更改格式。"
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "格式设置为ALWAYS_ASK。"
    FORMAT_UPDATED_BEST_LOG_MSG = "格式已更新为最佳：{format}"
    FORMAT_UPDATED_ID_LOG_MSG = "格式已更新为ID {format_id}：{format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "格式已更新为ID {format_id}（仅音频）：{format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "格式已更新为质量 {quality}：{format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "格式已更新为：{format}"
    FORMAT_MENU_SENT_LOG_MSG = "格式菜单已发送。"
    FORMAT_SELECTION_CLOSED_LOG_MSG = "格式选择已关闭。"
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "自定义格式提示已发送。"
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "格式分辨率菜单已发送。"
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "返回到主格式菜单。"
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "格式已更新为：{format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "格式设置为ALWAYS_ASK。"
    FORMAT_CODEC_SET_LOG_MSG = "编解码器首选项设置为 {codec}"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "自定义格式菜单已关闭"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "为用户 {user_id} 从 {url} 提取了直接链接"
    LINK_EXTRACTION_FAILED_LOG_MSG = "为用户 {user_id} 从 {url} 提取直接链接失败：{error}"
    LINK_COMMAND_ERROR_LOG_MSG = "用户 {user_id} 的link命令出错：{error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "用户 {user_id} 将键盘设置为 {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "用户 {user_id} 将键盘设置为 {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo通过命令设置：{arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "用户打开了 /mediainfo 菜单。"
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo：已关闭。"
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo已启用。"
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo已禁用。"
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "通过参数将分割大小设置为 {size} 字节。"
    SPLIT_MENU_OPENED_LOG_MSG = "用户打开了 /split 菜单。"
    SPLIT_SELECTION_CLOSED_LOG_MSG = "分割选择已关闭。"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "分割大小设置为 {size} 字节。"
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "代理通过命令设置：{arg}"
    PROXY_MENU_OPENED_LOG_MSG = "用户打开了 /proxy 菜单。"
    PROXY_MENU_CLOSED_LOG_MSG = "代理：已关闭。"
    PROXY_ENABLED_LOG_MSG = "代理已启用。"
    PROXY_DISABLED_LOG_MSG = "代理已禁用。"
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "帮助消息已关闭。"
    AUDIO_HELP_SHOWN_LOG_MSG = "显示了 /audio 帮助"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "用户请求播放列表帮助。"
    PLAYLIST_HELP_CLOSED_LOG_MSG = "播放列表帮助已关闭。"
    AUDIO_HINT_CLOSED_LOG_MSG = "音频提示已关闭。"
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "通过LINK按钮为用户 {user_id} 从 {url} 创建了直接链接菜单"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "通过LINK按钮为用户 {user_id} 从 {url} 提取直接链接失败：{error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "为用户 {user_id} 执行了LIST命令，url：{url}"
    QUICK_EMBED_LOG_MSG = "快速嵌入：{embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "为 {url} 发送了始终询问菜单"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "在错误后为用户 {user_id} 创建了缓存质量菜单：{error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "为 {url} 的始终询问菜单出错：{error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "格式通过 /args 设置固定"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "音频"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "视频"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "视频"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "下一个 ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ 上一个"
    SUBTITLES_NEXT_BUTTON_MSG = "下一个 ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ 所有文本字段为空"
    SENDER_VIDEO_DURATION_MSG = "视频时长："
    SENDER_UPLOADING_FILE_MSG = "📤 正在上传文件..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 正在上传视频..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 视频时长："
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "已上传1个文件。"
    DOWN_UP_VIDEO_INFO_MSG = "📋 视频信息"
    DOWN_UP_NUMBER_MSG = "编号"
    DOWN_UP_TITLE_MSG = "标题"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ 已下载视频。"
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 正在处理以上传..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 已上传分割部分 {part} 文件"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ 上传完成"
    DOWN_UP_FILES_UPLOADED_MSG = "已上传文件"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC（Android）"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 关闭"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼编解码器"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 配音"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 字幕"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 浏览器"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC（iOS）"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 正在获取直接链接..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 正在获取可用格式..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 正在获取视频描述..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ 获取描述时出错: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ 视频描述不可用"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ 发送描述时出错: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 视频描述已发送给用户 {user_id}，URL: {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 正在启动gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>时长：</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>格式：</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>浏览器：</b> 在网页浏览器中打开"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "可用格式"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 如何使用格式ID："
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "获取列表后，使用特定的格式ID："
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - 下载格式401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - 同上"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - 将格式140下载为MP3音频"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 检测到仅音频格式"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "这些格式将作为MP3音频文件下载。"
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>如何设置格式：</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - 下载特定格式ID"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - 按质量下载"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - 下载最佳质量"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - 始终询问质量"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>仅音频格式：</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - 将格式140下载为MP3音频"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "这些将作为MP3音频文件下载。"
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 使用上面列表中的格式ID"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ 错误：找不到原始消息。"
    ALWAYS_ASK_FORMATS_PAGE_MSG = "格式页面"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ 显示格式菜单时出错"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ 获取格式时出错"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ 获取可用格式时出错。"
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "请稍后再试。"
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp无法处理此内容"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "系统建议改用gallery-dl。"
    ALWAYS_ASK_OPTIONS_MSG = "**选项：**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• 对于图片库：<code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• 对于单个图片：<code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl通常对Instagram、Twitter和其他社交媒体内容效果更好。"
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 尝试Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 格式通过 /args 固定"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 字幕"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 配音音频"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — 字幕可用"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — 选择字幕语言"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ 未找到字幕且不会嵌入"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — 从缓存即时重新发布"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — 选择音频语言"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW是付费的（⭐️$0.02）"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — 选择下载质量"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — 下载图片（gallery-dl）"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — 在poketube中观看视频"  # 暂时禁用：poketube服务已关闭
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — 获取视频的直接链接"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — 显示可用格式列表"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — 更改视频扩展名/编解码器"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀嵌入"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — 仅提取音频"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW是付费的（⭐️$0.02）"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — 从缓存即时重新发布"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — 在poketube中观看视频"  # 暂时禁用：poketube服务已关闭
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — 选择音频语言"
    ALWAYS_ASK_BEST_BUTTON_MSG = "最佳"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛其他"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝仅字幕"
    ALWAYS_ASK_SMART_GROUPING_MSG = "智能分组"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "添加了操作按钮行（3）"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "添加了操作按钮行（2+2）"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "向现有行添加了底部按钮"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "创建了新的底部行"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "播放列表中未找到视频"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "不支持的URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "找不到视频"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "未找到视频"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "未找到媒体"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "此推文不包含"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>检索视频信息时出错：</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "检索视频信息时出错"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "尝试 <code>/clean</code> 命令并重试。如果错误仍然存在，YouTube需要授权。通过 <code>/cookie</code> 或 <code>/cookies_from_browser</code> 更新cookies.txt，然后重试。"
    ALWAYS_ASK_MENU_CLOSED_MSG = "菜单已关闭。"
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 手动质量选择"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "由于自动检测失败，请手动选择质量："
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 所有可用格式"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 可用质量（来自缓存）"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ 使用缓存的质量 - 新格式可能不可用"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 正在下载格式"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 正在下载"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 正在下载并跟踪进度..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 正在使用格式下载："
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 正在使用格式下载音频："
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 正在下载最佳质量..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 正在下载数据库转储..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 正在下载"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "格式页面"
    ALWAYS_ASK_FROM_CACHE_MSG = "（来自缓存）"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ 错误：找不到原始消息。它可能已被删除。请再次发送链接。"
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ 错误：找不到原始URL。请再次发送链接。"
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>已获得直接链接</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>标题：</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>时长：</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>格式：</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>视频流：</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>音频流：</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ 获取流链接失败"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "通过始终询问菜单为用户 {user_id} 从 {url} 提取了直接链接"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "通过始终询问菜单为用户 {user_id} 从 {url} 提取直接链接失败：{error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "通过down_and_up_with_format为用户 {user_id} 从 {url} 提取了直接链接"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "通过down_and_up_with_format为用户 {user_id} 从 {url} 提取直接链接失败：{error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "通过down_and_audio为用户 {user_id} 从 {url} 提取了直接链接"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "通过down_and_audio为用户 {user_id} 从 {url} 提取直接链接失败：{error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ 音频已从缓存发送。"
    AUDIO_PROCESSING_MSG = "🎙️ 音频正在处理..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 正在下载音频：\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "下载音频时发生错误。"
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ 提取音频信息失败"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "跳过播放列表中索引 {index} 处不支持的文件类型"
    AUDIO_FILE_NOT_FOUND_MSG = "下载后未找到音频文件。"
    AUDIO_UPLOADING_MSG = "{process}\n📤 正在上传音频文件...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ 发送音频失败：{error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "播放列表音频已发送：{sent}/{total} 个文件（质量={quality}）给用户{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ 下载音频失败：{error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ 由于超时（2小时）取消下载"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ 未找到视频文件：{filename}"
    VIDEO_PROCESSING_ERROR_MSG = "❌ 处理视频时出错：{error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ 发送描述文件时出错：{error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 如果您想更改视频标题 - 回复视频并输入新文本</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "未检测到字幕"
    VIDEO_PROGRESS_MSG = "<b>视频：</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>音频：</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL：</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL限制超出：{count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "处理完成"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ 多URL模式下不允许播放列表范围。仅发送不带范围的单个URL（*1*5, /vid 1-10 等）。"
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "如果您的网站受支持，请查看<a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>这里</a>"
    ERROR_COOKIE_NEEDED_MSG = "您可能需要 <code>cookie</code> 来下载此视频。首先，通过 <b>/clean</b> 命令清理您的工作区"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "对于Youtube - 通过 <b>/cookie</b> 命令获取 <code>cookie</code>。对于任何其他支持的网站 - 发送您自己的cookie（<a href='https://t.me/tg_ytdlp/203'>指南1</a>）（<a href='https://t.me/tg_ytdlp/214'>指南2</a>），然后再次发送您的视频链接。"
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "选择字幕语言"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "没有替代音频语言"
    CHOOSE_AUDIO_LANGUAGE_MSG = "选择音频语言"
    PAGE_NUMBER_MSG = "第 {page} 页"
    TOTAL_PROGRESS_MSG = "总进度"
    SUBTITLE_MENU_CLOSED_MSG = "字幕菜单已关闭。"
    SUBTITLE_LANGUAGE_SET_MSG = "字幕语言设置：{value}"
    AUDIO_SET_MSG = "音频设置：{value}"
    FILTERS_UPDATED_MSG = "过滤器已更新"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙返回"
    CLOSE_BUTTON_TEXT = "🔚关闭"
    LIST_BUTTON_TEXT = "📃列表"
    IMAGE_BUTTON_TEXT = "🖼图片"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ 质量未自动检测\n使用'其他'按钮查看所有可用格式。</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **检测到直播流**\n\n不允许下载正在进行的或无限的直播流。\n\n请等待流结束，然后在以下情况下再次尝试下载：\n• 流时长已知\n• 流已结束\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>直播流下载</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "块 {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "最大大小：{size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "总时长：{duration} 秒"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>直播流 - 块 {chunk}</b>\n⏱ 时长：{duration} 秒\n📦 大小：{size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "块 {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>直播流下载完成</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "已下载 {chunks} 个块"
    LIVE_STREAM_TOTAL_DURATION_MSG = "总时长：{duration} 秒"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>直播流下载已停止</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "用户目录已删除（可能通过 /clean 命令）"
    LIVE_STREAM_FILE_DELETED_MSG = "块文件已删除（可能通过 /clean 命令）"
    LIVE_STREAM_ENDED_MSG = "ℹ️ 流已结束"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "请使用 `/format` 命令选择不同的格式。"
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>已获得直接链接</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>标题：</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>时长：</b> {duration} 秒\n"
    FORMAT_FIELD_MSG = "🎛 <b>格式：</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>视频流：</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>音频流：</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **文件处理错误**\n\n视频已下载，但由于文件名中的无效字符而无法处理。\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **文件处理错误**\n\n视频已下载，但由于无效参数错误而无法处理。\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
    FORMAT_NOT_AVAILABLE_MSG = "❌ **格式不可用**\n\n请求的视频格式对此视频不可用。\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ 此视频未找到格式ID {format_id}。\n\n可用格式ID：{available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **此视频的AV1格式不可用。**\n\n**可用格式：**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **文件处理错误**\n\n音频已下载，但由于文件名中的无效字符而无法处理。\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **文件处理错误**\n\n音频已下载，但由于无效参数错误而无法处理。\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "用户输入了禁止内容。无法下载。"
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "NSFW模糊通过命令设置：{arg}"
    NSFW_MENU_OPENED_LOG_MSG = "用户打开了 /nsfw 菜单。"
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW：已关闭。"
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "下载{service} cookie失败：status={status}（URL已隐藏）"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "下载{service} cookie时出错：{error}（URL已隐藏）"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "下载{service} cookie时发生意外错误（URL已隐藏）：{error_type}：{error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "为用户 {user_id} 更新了cookie文件。"
    COOKIES_INVALID_CONTENT_LOG_MSG = "用户 {user_id} 提供了无效的cookie内容。"
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "用户 {user_id} 的YouTube cookie URL为空。"
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "为用户 {user_id} 从源 {source} 下载并验证了YouTube cookies。"
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "用户 {user_id} 的所有YouTube cookie源都失败了。"
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "管理员 {admin_id} 的check_porn命令出错：{error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "分割部分大小设置为 {size} 字节。"
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "视频上传完成，已分割文件。"
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "播放列表视频已发送：{sent}/{total} 个文件（质量={quality}）给用户 {user_id}"
    UNKNOWN_ERROR_MSG = "❌ 未知错误：{error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "跳过播放列表中索引 {index} 处不支持的文件类型"
    FFMPEG_NOT_FOUND_MSG = "❌ 未找到FFmpeg。请安装FFmpeg。"
    CONVERSION_TO_MP4_FAILED_MSG = "❌ 转换为MP4失败：{error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ 嵌入字幕可能需要很长时间（每1分钟视频最多1分钟）！\n🔥 开始烧录字幕..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ 由于限制（质量/时长/大小），无法嵌入字幕"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ 所选语言的字幕不可用"
    ERROR_SENDING_VIDEO_MSG = "❌ 发送视频时出错：{error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ 播放列表视频已发送：{sent}/{total} 个文件。"
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ 由于超时（2小时）取消下载"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ 下载视频失败：{error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ 错误：{error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON必须是一个对象（字典）。"
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ 无效的JSON格式。请提供有效的JSON。"
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ 值必须在 {min_val} 和 {max_val} 之间。"
    ARGS_PARAM_SET_TO_MSG = "✅ {description} 设置为：<code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ 真"
    ARGS_FALSE_BUTTON_MSG = "❌ 假"
    ARGS_BACK_BUTTON_MSG = "🔙 返回"
    ARGS_CLOSE_BUTTON_MSG = "🔚 关闭"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ 真"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ 假"
    ARGS_NOT_SET_MSG = "未设置"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ 此视频的AV1格式不可用。\n\n可用格式：\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ 下载时出错：{error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ 在播放列表索引 {index} 处未找到视频。"
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **视频转换失败**\n\n由于无效参数错误，视频无法转换为MP4。\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **视频转换失败**\n\n视频无法转换为MP4。\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ 获取流链接失败"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>获取链接时出错：</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ 在索引 {index} 处未找到内容"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ 错误：找不到原始消息。"
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ 错误：找不到URL。"
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ 此URL无法嵌入。"
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ 此视频的{codec}编解码器不可用"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ 此视频的{format}格式不可用"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ 洪水限制。请稍后再试。"
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ 检查Cookie"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ 开启"
    PROXY_OFF_BUTTON_MSG = "❌ 关闭"
    PROXY_CLOSE_BUTTON_MSG = "🔚关闭"
    
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ 开启"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ 关闭"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚关闭"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV：开启"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV：关闭"
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ 开启（无模糊）"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ 开启（无模糊）"
    NSFW_OFF_BLUR_MSG = "✅ 关闭（模糊）"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ 关闭（模糊）"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "干净"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "处理用户 {user} 的回复消息时出错：{error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "向用户 {user} 发送广播时出错：{error}"
    ADMIN_LOGS_FORMAT_MSG = "{bot_name}的日志\n用户：{user_id}\n总日志：{total}\n当前时间：{now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\n总计 {path}：{count}\n当前时间：{now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>总用户数：{count}</i>\n最近20个 {path}：\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "管理员 {admin_id} 重新加载了色情缓存。域名：{domains}，关键词：{keywords}，网站：{sites}，白名单：{whitelist}，灰名单：{greylist}，黑名单：{black_list}，白关键词：{white_keywords}，代理域名：{proxy_domains}，代理2域名：{proxy_2_domains}，清理查询：{clean_query}，无Cookie域名：{no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "发送超时消息时出错：{error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>选择语言</b>"
    LANG_CHANGED_MSG = "✅ 语言已更改为 {lang_name}"
    LANG_ERROR_MSG = "❌ 更改语言时出错"
    LANG_CLOSED_MSG = "语言选择已关闭"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] 回调：{callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "添加浏览器监控按钮，URL：{miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "浏览器监控URL未配置：{miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **键盘设置已更新！**\n\n新设置：**{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "隐藏键盘失败：{error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "使用工作的YouTube cookies为用户 {user_id} 提取链接"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "用户 {user_id} 没有可用的工作YouTube cookies用于链接提取"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "使用现有的YouTube cookies为用户 {user_id} 提取链接"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "用户 {user_id} 未找到YouTube cookies用于链接提取"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "已将全局cookie文件复制到用户 {user_id} 文件夹用于链接提取"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] 用户 {user_id} 请求mediainfo命令"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] 用户 {user_id} 是管理员：{is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] 用户 {user_id} 在频道中：{is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] 用户 {user_id} 访问被拒绝 - 不是管理员且不在频道中"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] 用户 {user_id} 访问已授予"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] 回调：{callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ 此命令仅适用于管理员。"
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ 下载完成，支持PO令牌"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ 洪水限制。请稍后再试。"
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST令牌刷新错误：{error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ 关闭Firebase会话时出错：{error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ 初始化基础数据库结构时出错：{error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ config.py中未设置所有参数（FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD）"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ 未设置FIREBASE_CONF.databaseURL"
    DB_API_KEY_NOT_SET_MSG = "❌ 未设置FIREBASE_CONF.apiKey用于获取idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ 下载Firebase转储时出错：{error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ 通过REST下载Firebase转储失败"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ _download_and_reload_cache中出错：{error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ 运行自动reload_cache时出错（尝试 {attempt}/{max_retries}）：{error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ 所有重试尝试都失败了"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 在 {datetime} 开始下载Firebase转储"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ 依赖项不可用：requests 或 Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ 数据库为空"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ 关闭记录器时出错：{error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ 清理过程中出错：{error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ 克隆错误：{error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ 克隆超时"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ 克隆异常：{error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ 用户取消了更新"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ 存储库已成功克隆"
    UPDATE_BACKUPS_MOVED_MSG = "✅ 备份已移动到 _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ 所有模块已加载"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ 退出时清理完成"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 收到信号 {signal}，正在优雅关闭..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "请稍候..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 正在下载HLS流："
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "等待片段"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ 在 _backup/ 中未找到备份 {ts}"
    RESTORE_FAILED_RESTORE_MSG = "❌ 恢复失败 {src} -> {dest_path}：{e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ 已恢复：{dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL：</b> <code>{url}</code>\n\n<b>详细信息：</b> {error_details}\n\n由于严重错误，下载已停止。\n\n💡 <b>提示：</b> 如果您收到401未授权错误，请尝试使用 <code>/cookie instagram</code> 命令或发送您自己的cookies以通过Instagram认证。"
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ 域名在色情黑名单中：{domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ 找到色情关键词：{keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ 域名在白名单中：{domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ 找到白名单关键词：{keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ 未找到色情关键词"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API在索引 {index} 处出错，跳过到下一个音频..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API在索引 {index} 处出错，跳过到下一个视频..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "用户输入了 <b>url</b>\n <b>用户名：</b> {user_name}\nURL：{url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>用户输入如下：</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "加入频道"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 正在注册处理器：{handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - 下载我的5个cookies"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - 获取浏览器的YT-cookie"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - 验证您的cookie文件"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - 上传自定义cookie"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 关闭"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "可用格式：{url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Close"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Close"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Close"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Close"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "帮助已关闭。"
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "已关闭"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "发生错误"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "在PATH或项目目录中未找到ffmpeg。请安装FFmpeg。"
    YTDLP_NOT_FOUND_MSG = "在PATH或项目目录中未找到yt-dlp二进制文件。请安装yt-dlp。"
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "视频将被分割为 {rounds} 个部分，这可能过多"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "正在分割视频部分 {current}/{total}：{start_time:.2f}秒 到 {end_time:.2f}秒"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "创建分割部分 {part} 失败：{target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "成功创建分割部分 {part}：{target_name}（{size} 字节）"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "分割视频部分 {part} 时出错：{error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "视频已成功分割为 {count} 个部分"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "视频分割过程中出错：{error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] 处理视频 {video_path} 时出错：{error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "视频文件不存在：{video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "解析尺寸 '{size_result}' 时出错：{error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "无法从 '{size_result}' 确定视频尺寸，使用默认值：{width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "创建缩略图时出错：{stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "解析视频时长时出错：{error}，结果为：{result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "未在 {thumb_dir} 创建缩略图，使用默认值"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "命令执行错误：{error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "使用FFmpeg创建缩略图时出错：{error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "跳过非字典配置部分：{section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "设置 {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] 使用用户cookies：{cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "为用户 {user_id} 使用YouTube cookies"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "已将全局cookie文件复制到用户 {user_id} 文件夹"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] 使用复制的全局cookies作为用户cookies：{cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "为用户 {user_id} 复制全局cookie文件失败：{error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "对域名使用 --no-cookies：{url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "请求代理但导入/获取配置失败：{error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "强制为gallery-dl使用代理：{proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "请求代理但代理配置不完整"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "代理助手失败：{error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "正在解析提取器项目..."
    GALLERY_DL_ITEM_COUNT_MSG = "项目 {count}：{item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "找到元数据（标签2）：{info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "找到URL（标签3）：{url}，元数据：{metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "找到元数据（旧版）：{info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "找到URL（旧版）：{url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "找到文件名：{filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "找到目录：{directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "找到扩展名：{extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "已解析 {count} 个项目，信息：{info}，回退：{fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "设置gallery-dl配置：{config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "尝试策略A：extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "未找到gallery_dl.extractor模块"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "此构建中不可用gallery_dl.extractor.find()"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "调用extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "没有提取器匹配URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "在提取器上设置cookies：{cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "在提取器上设置cookies失败：{error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "找到提取器，调用items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "策略A成功，获得信息：{info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "策略A：extractor.items()未返回有效信息"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "策略A（extractor.find）失败：{error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "来自--get-urls的回退元数据：总计={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "所有策略都未能获取元数据"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "提取图像信息失败：{error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "未找到gallery_dl.job模块（安装损坏？）"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "此构建中不可用gallery_dl.job.DownloadJob"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "在gallery-dl目录中搜索已下载的文件"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "尝试通过提取器的名称查找文件"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "读取用户 {user_id} 的参数时出错：{error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] 处理视频{video_path}时出错：{error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "用户 {user_id} 已启用send_as_file，作为文档发送"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video多次超时；回退到send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "标题太长，尝试使用最小标题"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video（最小标题）超时；回退到send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "发送带最小标题的视频时出错：{error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "发送完整描述文件时出错：{error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "删除临时描述文件时出错：{error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts
File size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "跳过NO_FILTER_DOMAINS中域名的match_filter：{url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "检查用户 {user_id} 的URL上现有YouTube cookies以进行格式检测"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "现有YouTube cookies在用户 {user_id} 的URL上工作正常，用于格式检测 - 使用它们"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "现有YouTube cookies在用户 {user_id} 的URL上失败，尝试获取新的用于格式检测"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "尝试YouTube cookie源 {i} 用于用户 {user_id} 的格式检测"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "来自源 {i} 的YouTube cookies在用户 {user_id} 的URL上工作正常，用于格式检测 - 已保存到用户文件夹"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "来自源 {i} 的YouTube cookies在用户 {user_id} 的URL上不工作，用于格式检测"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "从源 {i} 下载YouTube cookies失败，用于用户 {user_id} 的格式检测"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "所有YouTube cookie源都失败，用于用户 {user_id} 的格式检测，将尝试不使用cookies"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "未配置YouTube cookie源，用于用户 {user_id} 的格式检测，将尝试不使用cookies"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "未找到YouTube cookies，用于用户 {user_id} 的格式检测，尝试获取新的"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "使用YouTube cookies用于用户 {user_id} 的格式检测（已在Always Ask菜单中验证）"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "未找到YouTube cookies，用于用户 {user_id} 的格式检测，尝试恢复..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "已将全局cookie文件复制到用户 {user_id} 文件夹用于格式检测"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "为用户 {user_id} 复制全局cookie文件失败：{error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "在get_video_formats中对域名使用 --no-cookies：{url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "应用尚未初始化。无法访问 {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>标题：</b> <code>{caption}</code>\n<b>用户ID：</b> <code>{user_id}</code>\n<b>用户名字：</b> <code>{users_name}</code>\n<b>视频文件ID：</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor中出错：{error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor中发生意外错误：{error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 视频URL</a>{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "配置中缺少FIREBASE_CONF.databaseURL"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin已初始化"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken已刷新"
    DB_LOG_FOR_USER_ADDED_MSG = "已添加用户日志"
    DB_DATABASE_CREATED_MSG = "数据库已创建"
    DB_BOT_STARTED_MSG = "机器人已启动"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY已持久化到config.py：{hours}小时"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "播放列表部分已缓存：{path_parts}，跳过"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos：未找到任何URL/质量变体的缓存，返回空字典"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count：大范围的快速计数：{cached_count} 个缓存的视频"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids：未找到哈希 {url_hash}、质量 {quality_key} 的缓存"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids：未找到任何URL变体的缓存，返回None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ 访问被拒绝。仅限管理员。"
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 自动Firebase缓存重新加载已更新！\n\n📊 状态：{status}\n⏰ 计划：从00:00开始每 {interval} 小时\n🕒 下次重新加载：{next_exec}（{delta_min} 分钟后）"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 自动Firebase缓存重新加载已停止！\n\n📊 状态：❌ 已禁用\n💡 使用 /auto_cache on 重新启用"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ 无效参数。使用 /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ 间隔必须在1到168小时之间"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ 设置间隔失败"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ 自动Firebase缓存间隔已更新！\n\n📊 状态：✅ 已启用\n⏰ 计划：从00:00开始每 {interval} 小时\n🕒 下次重新加载：{next_exec}（{delta_min} 分钟后）"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 自动Firebase缓存重新加载已启动！\n\n📊 状态：✅ 已启用\n⏰ 计划：从00:00开始每 {interval} 小时\n🕒 下次重新加载：{next_exec}（{delta_min} 分钟后）"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 自动Firebase缓存重新加载已停止！\n\n📊 状态：❌ 已禁用\n💡 使用 /auto_cache on 重新启用"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "自动重新加载已启用；下次在 {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "自动重新加载已被管理员禁用。"
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "自动重新加载间隔设置为 {interval}小时；下次在 {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "自动重新加载已启动；下次在 {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "自动重新加载已被管理员停止。"
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase缓存已加载：{count} 个根节点"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ 未找到Firebase缓存文件，从空缓存开始：{cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ 加载firebase缓存失败：{error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase缓存已重新加载：{count} 个根节点"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ 未找到Firebase缓存文件：{cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ 重新加载firebase缓存失败：{error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 您已被机器人封禁！要解除封禁，请联系 {Config.ADMIN_USERNAME}\n<blockquote>P.S. 不要离开频道 - 您将被自动封禁 ⛔️</blockquote>\n🌍更改语言 /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ 未找到视频格式。尝试图像下载器…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram限制了消息发送。\n⏳ 请等待：{time_str}\n要更新计时器，请再次发送URL 2次。"
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC播放器（iOS）</a></b>\n\n<i>点击按钮复制流URL，然后粘贴到VLC应用中</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC播放器（Android）</a></b>\n\n<i>点击按钮复制流URL，然后粘贴到VLC应用中</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>获取链接时出错：</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ 发送格式文件时出错：{error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ 获取格式失败：\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 正在分析...（等待6秒）"
    AA_PROCESSING_MSG = "🔎 正在分析..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ 标签 #{wrong} 包含禁止的字符。只允许字母、数字和 _。\n请使用：{example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ 机器人在群组中工作需要管理员权限。请将机器人设为该群组的管理员。"
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "你好 {first_name}，\n \n<i>这个机器人🤖可以直接将任何视频下载到telegram。😊 更多信息请按 <b>/help</b></i> 👈\n\n<blockquote>附注：下载🔞NSFW内容和☁️云存储文件是付费的！1⭐️ = $0.02</blockquote>\n<blockquote>再附注：‼️ 不要离开频道 - 您将被禁止使用机器人 ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 没有要删除的文件。"
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 所有文件已成功删除！\n\n已删除的文件：\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ 请等待您之前的下载完成"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "check_user中App instance为None"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit：info_dict为None，允许下载"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits：info_dict为None，允许嵌入字幕"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits：检查限制 - 最大质量={max_quality}p，最大时长={max_duration}秒，最大大小={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits：info_dict键：{keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "跳过字幕嵌入：时长 {duration}秒超过限制 {max_duration}秒"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "跳过字幕嵌入：大小 {size_mb:.2f}MB超过限制 {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "跳过字幕嵌入：质量 {width}x{height}（最小边 {min_side}p）超过限制 {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "播放列表"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ {service}的范围限制超出：{count}（最大 {max_count}）。\n\n使用以下命令之一下载最大可用文件：\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ {service}的范围限制超出：{count}（最大 {max_count}）\n用户ID：{user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "配置中PO令牌提供程序已禁用"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} 不是YouTube域名，跳过PO令牌"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO令牌提供程序在 {base_url} 不可用，回退到标准YouTube提取"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO令牌提供程序缓存已清除，将在下次请求时检查可用性"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "应用实例尚不可用"
    HELPER_USER_NAME_MSG = "用户"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "检测到洪水等待，休眠 {wait_seconds} 秒"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "检测到洪水等待但无法提取时间，休眠 {retry_delay} 秒"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "检测到msg_seqno错误，休眠 {retry_delay} 秒"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "代理配置不完整，使用直接连接"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚关闭"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚关闭"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚关闭"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 日志文件已删除。"
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 标签文件已删除。"
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 格式文件已删除。"
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 分割文件已删除。"
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 媒体信息文件已删除。"
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 字幕设置已删除。"
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 键盘设置已删除。"
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 参数设置已删除。"
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 NSFW设置已删除。"
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 代理设置已删除。"
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 洪水等待设置已删除。"
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚关闭"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 视频下载命令"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "用法：<code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "示例："
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>（正序）\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code>（倒序）"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "另请参阅：/audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "用户 {user_id} 关闭了add_bot_to_group命令"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "提取YouTube ID失败"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "下载缩略图失败或太大"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "选择音频语言"
    AA_NO_SUBTITLES_DETECTED_MSG = "未检测到字幕"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "选择字幕语言"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "认证错误"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "未找到账户"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "账户不可用"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "超出速率限制"
    GALLERY_DL_NETWORK_ERROR_MSG = "网络错误"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "内容不可用"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "地理限制"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "需要验证"
    GALLERY_DL_POLICY_VIOLATION_MSG = "违反政策"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "未知错误"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ 下载已开始</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚关闭"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 视频下载命令</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "用法：<code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>示例：</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "另请参阅：/audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ 洪水限制。请稍后再试。"
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Cookie命令用法</b>

<code>/cookie</code> - 显示cookie菜单
<code>/cookie youtube</code> - 下载YouTube cookies
<code>/cookie instagram</code> - 下载Instagram cookies
<code>/cookie tiktok</code> - 下载TikTok cookies
<code>/cookie x</code> 或 <code>/cookie twitter</code> - 下载Twitter/X cookies
<code>/cookie facebook</code> - 下载Facebook cookies
<code>/cookie custom</code> - 显示自定义cookie说明

<i>可用服务取决于机器人配置。</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Cookie文件已删除，缓存已清除。"
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ 上一页"
    SUBS_BACK_BUTTON_MSG = "🔙返回"
    SUBS_OFF_BUTTON_MSG = "🚫 关闭"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - 设置语言"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - 设置语言并启用AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "有效选项："
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 语言"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 开发GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 贡献GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 清理"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIES"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 媒体"
    SETTINGS_INFO_BUTTON_MSG = "📖 信息"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ 更多"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 仅Cookies"
    SETTINGS_LOGS_BUTTON_MSG = "📃 日志 "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ 标签"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 格式"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ 分割"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 媒体信息"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 字幕"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 键盘"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ 参数"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 代理"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 洪水等待"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  所有文件"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - 下载我的5个cookies"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - 获取浏览器的YT-cookie"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - 验证您的cookie文件"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - 上传自定义cookie"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - 更改质量和格式"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - 开启/关闭MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - 更改分割视频部分大小"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - 将视频下载为音频"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - 字幕语言设置"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - 如何下载播放列表"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - 通过gallery-dl下载图像"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - 发送您的#标签"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - 获取说明"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - 发送您的日志"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - 播放列表帮助"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - 如何操作"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - 获取直接视频链接"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - 启用/禁用代理"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - 键盘布局"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - 内联搜索助手"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp参数"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - NSFW模糊设置"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 清理选项</b>\n\n选择要清理的内容："
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 移动端：激活@vid搜索"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 移动端：激活@vid搜索"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 关闭"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 完整"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[图像URL]({url})"
    IMAGE_ERROR_MSG = "❌ 错误：{str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙返回"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - 自定义格式"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p质量"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K质量"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K质量"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - 特定格式ID"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - 始终显示菜单"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/最佳质量"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ 始终询问（菜单+按钮）"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 其他（144p - 4320p）"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k（最适合PC/Mac Telegram）"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD（最适合移动端Telegram）"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈最佳视频+最佳音频（最大质量）"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 自定义（输入您自己的）"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 从浏览器"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 您自己的"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ 由于不活动，输入模式已自动关闭（5分钟）。"
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 重置全部"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 查看当前"
    ARGS_BACK_BUTTON_MSG = "🔙 返回"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>将此消息转发到您的收藏夹以将这些设置保存为模板。</i> \n\n<i>将此消息转发回此处以应用这些设置。</i>"
    ARGS_NO_SETTINGS_MSG = "📋 当前yt-dlp参数：\n\n未配置自定义设置。\n\n---\n\n<i>将此消息转发到您的收藏夹以将这些设置保存为模板。</i> \n\n<i>将此消息转发回此处以应用这些设置。</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 当前yt-dlp参数：\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 导出设置"
    ARGS_SETTINGS_READY_MSG = "设置已准备好导出！将此消息转发到收藏夹以保存。"
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 当前yt-dlp参数："
    ARGS_FAILED_RECOGNIZE_MSG = "❌ 无法识别消息中的设置。请确保您发送了正确的设置模板。"
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ 设置已成功导入！\n\n应用的参数：{applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "关键设置：\n"
    ARGS_ERROR_SAVING_MSG = "❌ 保存导入的设置时出错。"
    ARGS_ERROR_IMPORTING_MSG = "❌ 导入设置时发生错误。"

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>下载Cookie文件</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "选择要下载cookie文件的服务。"
    COOKIE_MENU_SAVE_INFO_MSG = "Cookie文件将保存为您文件夹中的cookie.txt。"
    COOKIE_MENU_TIP_HEADER_MSG = "提示：您也可以使用直接命令："
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – 下载并验证cookies"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – 按索引使用特定源（1–{max_index}）"
    COOKIE_MENU_TIP_VERIFY_MSG = "然后使用 <code>/check_cookie</code> 验证（在RickRoll上测试）。"

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "始终询问"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗链接"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁观看"  # 暂时禁用：poketube服务已关闭
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝描述"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ 修剪"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>视频修剪</b>\n\n视频时长: <b>{start_time} - {end_time}</b>\n\n请以以下格式发送所需的时间范围:\n<code>HH:MM:SS-HH:MM:SS</code>\n\n示例: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ 格式无效。请使用: <code>HH:MM:SS-HH:MM:SS</code>\n\n示例: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ 范围无效。开始时间必须小于结束时间。"
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ 时间范围超出视频边界。\n\n视频时长: <b>{start_time} - {end_time}</b>\n\n您的范围必须在此限制内。"
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>视频将被裁剪:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ 部分完成 - 已上传 {successful_uploads}/{total_files} 个音频文件。"
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ 音频已成功下载并发送 - 已上传 {total_files} 个文件。"

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>私有TikTok账户</b>\n\n"
        "此TikTok账户是私有的或所有视频都是私有的。\n\n"
        "<b>💡 解决方案：</b>\n"
        "1. 关注账户 @{username}\n"
        "2. 使用 <code>/cookie</code> 命令将您的cookies发送给机器人\n"
        "3. 重试\n\n"
        "<b>更新cookies后，请重试！</b>"
    )

    #######################################################
