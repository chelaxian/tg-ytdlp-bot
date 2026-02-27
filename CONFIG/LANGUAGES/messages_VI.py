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
    CREDITS_MSG = "<blockquote><i>Được quản lý bởi</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 Thay đổi ngôn ngữ: /lang</b>"
    TO_USE_MSG = "<i>Để sử dụng bot này, bạn cần đăng ký kênh Telegram @tg_ytdlp.</i>\nSau khi tham gia kênh, <b>gửi lại liên kết video và bot sẽ tải xuống cho bạn</b> ❤️\n\n<blockquote>P.S. Do nội dung 🔞NSFW tiềm ẩn - tải từ ☁️<b>Lưu trữ đám mây</b>, 📁<b>Chia sẻ tệp</b>, 🔗<b>Rút gọn URL</b> và 🔞<b>Trang khiêu dâm</b> là có phí! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ KHÔNG 🗑<b>xóa/hủy đăng ký kênh @tg_ytdlp</b> và KHÔNG 🤖<b>spam URL/lệnh quá nhiều cho bot</b> - bạn sẽ bị cấm sử dụng bot tự động ⛔️</blockquote>"

    ERROR1 = "Không tìm thấy liên kết url. Vui lòng nhập url có <b>https://</b> hoặc <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Danh sách phát (yt-dlp)</b>

Để tải xuống danh sách phát, gửi URL của nó với các phạm vi <code>*start*end</code> ở cuối. Ví dụ: <code>URL*1*5</code> (5 video đầu tiên từ 1 đến 5 bao gồm).<code>URL*-1*-5</code> (5 video cuối cùng từ 1 đến 5 bao gồm).
Hoặc bạn có thể sử dụng <code>/vid TỪ-ĐẾN URL</code>. Ví dụ: <code>/vid 3-7 URL</code> (tải xuống video từ 3 đến 7 bao gồm từ đầu). <code>/vid -3-7 URL</code> (tải xuống video từ 3 đến 7 bao gồm từ cuối). Cũng hoạt động cho lệnh <code>/audio</code>.

<b>Ví dụ:</b>

🟥 <b>Phạm vi video từ danh sách phát YouTube:</b> (cần 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(tải xuống 5 video đầu tiên từ 1 đến 5 bao gồm)
🟥 <b>Video đơn từ danh sách phát YouTube:</b> (cần 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(chỉ tải xuống video thứ 3)

⬛️ <b>Hồ sơ TikTok:</b> (cần 🍪 của bạn)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(tải xuống 10 video đầu tiên từ hồ sơ người dùng)

🟪 <b>Stories Instagram:</b> (cần 🍪 của bạn)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(tải xuống 3 stories đầu tiên)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(tải xuống 10 stories đầu tiên từ album)

🟦 <b>Video VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(tải xuống 3 video đầu tiên từ hồ sơ người dùng/nhóm)

⬛️<b>Kênh Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(tải xuống video từ 2 đến 4 bao gồm từ kênh)

🟪 <b>Clip Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(tải xuống 3 clip đầu tiên từ kênh)

🟦 <b>Nhóm Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(tải xuống 2 video đầu tiên từ nhóm)

🟧 <b>Model Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(tải xuống 2 video đầu tiên từ hồ sơ model)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(tải xuống 3 video đầu tiên từ kết quả tìm kiếm theo prompt của bạn)

và vân vân...
xem <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">danh sách trang web được hỗ trợ</a>
</blockquote>

<blockquote expandable>🖼 <b>Hình ảnh (gallery-dl)</b>

Sử dụng <code>/img URL</code> để tải xuống hình ảnh/ảnh/album từ nhiều nền tảng.

<b>Ví dụ:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Phạm vi:</b>
<code>/img 11-20 https://example.com/album</code> — các mục 11..20
<code>/img 11- https://example.com/album</code> — từ 11 đến cuối (hoặc giới hạn bot)

<i>Các nền tảng được hỗ trợ bao gồm vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, v.v. Danh sách đầy đủ:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">các trang web được gallery-dl hỗ trợ</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>Bot Tải Video - Trợ giúp</b>

📥 <b>Cách sử dụng cơ bản:</b>
• Gửi bất kỳ liên kết nào → bot sẽ tải xuống
  <i>bot tự động cố gắng tải video qua yt-dlp và hình ảnh qua gallery-dl.</i>
• <b>Nhiều URL:</b> Ở chế độ chọn chất lượng (<code>/format</code>) bạn có thể gửi tối đa <b>10 URL</b> trong một tin nhắn. Mỗi URL trên một dòng mới hoặc cách nhau bằng khoảng trắng.
• <code>/audio URL</code> → trích xuất âm thanh
• <code>/link [quality] URL</code> → lấy liên kết trực tiếp
• <code>/proxy</code> → bật/tắt proxy cho tất cả lượt tải
• Trả lời video bằng văn bản → thay đổi chú thích

📋 <b>Danh sách phát & Phạm vi:</b>
• <code>URL*1*5</code> → tải 5 video đầu tiên
• <code>URL*-1*-5</code> → tải 5 video cuối cùng
• <code>/vid 3-7 URL</code> → trở thành <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → trở thành <code>URL*-3*-7</code>

🍪 <b>Cookie & Riêng tư:</b>
• Tải lên *.txt cookie cho video riêng tư
• <code>/cookie [service]</code> → tải cookie (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → chọn nguồn theo chỉ mục (1–N)
• <code>/cookies_from_browser</code> → trích xuất từ trình duyệt
• <code>/check_cookie</code> → xác minh cookie
• <code>/save_as_cookie</code> → lưu văn bản dưới dạng cookie

🧹 <b>Dọn dẹp:</b>
• <code>/clean</code> → chỉ tệp phương tiện
• <code>/clean all</code> → tất cả
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Cài đặt:</b>
• <code>/settings</code> → menu cài đặt
• <code>/format</code> → chất lượng & định dạng
• <code>/split</code> → chia video thành các phần
• <code>/mediainfo on/off</code> → thông tin phương tiện
• <code>/nsfw on/off</code> → làm mờ NSFW
• <code>/tags</code> → xem thẻ đã lưu
• <code>/sub on/off</code> → phụ đề
• <code>/keyboard</code> → bàn phím (OFF/1x3/2x3)

🏷️ <b>Thẻ:</b>
• Thêm <code>#tag1#tag2</code> sau URL
• Thẻ xuất hiện trong chú thích
• <code>/tags</code> → xem tất cả thẻ

🔗 <b>Liên kết trực tiếp:</b>
• <code>/link URL</code> → chất lượng tốt nhất
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → chất lượng cụ thể

⚙️ <b>Lệnh nhanh:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → đặt chất lượng
• <code>/keyboard off/1x3/2x3/full</code> → bố cục bàn phím
• <code>/split 100mb-2000mb</code> → thay đổi kích thước phần
• <code>/subs off/ru/en auto</code> → ngôn ngữ phụ đề
• <code>/list URL</code> → danh sách định dạng có sẵn
• <code>/mediainfo on/off</code> → bật/tắt thông tin phương tiện
• <code>/proxy on/off</code> → bật/tắt proxy cho tất cả lượt tải

📊 <b>Thông tin:</b>
• <code>/usage</code> → lịch sử tải xuống
• <code>/search</code> → tìm kiếm nội tuyến qua @vid

🖼 <b>Hình ảnh:</b>
• <code>URL</code> → tải URL hình ảnh
• <code>/img URL</code> → tải hình ảnh từ URL
• <code>/img 11-20 URL</code> → tải phạm vi cụ thể
• <code>/img 11- URL</code> → tải từ thứ 11 đến cuối

👨‍💻 <i>Nhà phát triển:</i> @upekshaip
🤝 <i>Người đóng góp:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Just save your cookie as <b><u>cookie.txt</u></b> and send it to bot as a document.\n\n"
        "You can also send cookies as plain text with <b><u>/save_as_cookie</u></b> command.\n"
        "<b>Usage of <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>Instructions:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>Video search</b>

Press the button below to activate inline search via @vid.

<blockquote>On PC just type <b>"@vid Your_Search_Query"</b> in any chat.</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 Image Download Command</b>\n\n"
        "Usage: <code>/img URL</code>\n\n"
        "<b>Examples:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Supported platforms (examples):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, etc. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">full list</a></blockquote>"
        "Also see: "
    )
    
    LINK_HINT_MSG = (
        "Get direct video links with quality selection.\n\n"
        "Usage: /link + URL \n\n"
        "(ex. /link https://youtu.be/abc123)\n"
        "(ex. /link 720 https://youtu.be/abc123)"
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
🔞 <b>NSFW Mode: ON✅</b>

• NSFW content will be displayed without blurring.
• Spoilers will not apply to NSFW media.
• The content will be visible immediately

<i>Use /nsfw off to enable blur</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW Mode: OFF</b>

⚠️ <b>Blur enabled</b>
• NSFW content will be hidden under spoiler   
• To view, you will need to click on the media
• Spoilers will apply to NSFW media.

<i>Use /nsfw on to disable blur</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Invalid parameter</b>

Use:
• <code>/nsfw on</code> - disable blur
• <code>/nsfw off</code> - enable blur
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Checking cache...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Đang xử lý..."
    DOWNLOADING_MSG = "📥 <b>Đang tải xuống phương tiện...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Đang tải xuống hình ảnh...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Tải xuống hoàn tất</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "Đã tải xuống:"
    SENT_STATUS_MSG = "Đã gửi:"
    PENDING_TO_SEND_STATUS_MSG = "Đang chờ gửi:"
    TITLE_LABEL_MSG = "Tiêu đề:"
    MEDIA_COUNT_LABEL_MSG = "Số lượng phương tiện:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "Tải xuống hoàn tất, đang xử lý âm thanh..."
    VIDEO_PROCESSING_MSG = "📽 Video đang được xử lý..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Đã gửi từ bộ nhớ cache</b>\n\nĐã gửi album: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Video đã được gửi thành công từ bộ nhớ cache."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Video danh sách phát đã được gửi từ bộ nhớ cache ({cached}/{total} tệp)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} video đã được gửi từ bộ nhớ cache, đang tải xuống các video còn thiếu..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ Đã gửi từ bộ nhớ cache: {cached}\n🔄 Đang tiếp tục tải xuống..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 Không thể phân tích phương tiện, tiếp tục với phạm vi tối đa được phép (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 Không thể xác định số lượng phương tiện, tiếp tục với phạm vi tối đa được phép (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 Không thể xác định tổng số lượng phương tiện, tiếp tục với phạm vi được chỉ định {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>URL không hợp lệ</b>\n\nVui lòng cung cấp URL hợp lệ bắt đầu bằng http:// hoặc https://"

    ERROR_OCCURRED_MSG = "❌ <b>Đã xảy ra lỗi</b>\n\n<code>{url}</code>\n\nLỗi: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Lỗi khi gửi video: {error}"
    ERROR_UNKNOWN_MSG = "❌ Lỗi không xác định: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Không đủ dung lượng ổ đĩa để tải xuống video."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Kích thước tệp vượt quá giới hạn {limit} GB. Vui lòng chọn tệp nhỏ hơn trong phạm vi kích thước được phép."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>Không thể tải xuống video với tất cả proxy có sẵn</b>\n\nTất cả các lần thử tải xuống qua proxy đều thất bại.\nHãy thử:\n• Kiểm tra chức năng của proxy\n• Thử proxy khác từ danh sách\n• Tải xuống không dùng proxy (nếu có thể)"

    ERROR_GETTING_LINK_MSG = "❌ <b>Lỗi khi lấy liên kết:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram đã giới hạn việc gửi tin nhắn.\n⏳ Vui lòng đợi: {time}\nĐể cập nhật bộ đếm thời gian, gửi lại URL 2 lần."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram đã giới hạn việc gửi tin nhắn.\n⏳ Vui lòng đợi: \nĐể cập nhật bộ đếm thời gian, gửi lại URL 2 lần."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Không thể tải xuống phụ đề"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Liên kết Stream Trực tiếp</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Tiêu đề:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Thời lượng:</b> {duration} giây\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Lỗi: Không tìm thấy tin nhắn gốc."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Thẻ #{tag} chứa các ký tự bị cấm. Chỉ cho phép chữ cái, chữ số và _.\nVui lòng sử dụng: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Video danh sách phát đã được gửi: {sent}/{total} tệp."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>Mẹo về danh sách phát</b>

Bạn đã gửi liên kết danh sách phát mà không chỉ định phạm vi. Bot đã tự động tải xuống video đầu tiên (<code>*1*1</code>).

<b>Để tải xuống nhiều video từ danh sách phát, hãy chỉ định phạm vi:</b>
• <code>URL*1*5</code> — 5 video đầu tiên (từ 1 đến 5 bao gồm)
• <code>URL*3*3</code> — chỉ video thứ 3
• <code>/vid 1-10 URL</code> — định dạng thay thế

Tìm hiểu thêm: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ Đã gửi từ bộ nhớ cache: {cached}/{total} tệp."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Không thể lấy liên kết stream"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Chọn trình duyệt để tải cookie từ:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Không tìm thấy trình duyệt nào trên hệ thống này. Bạn có thể tải cookie từ URL từ xa hoặc theo dõi trạng thái trình duyệt:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Mở Trình duyệt</b> - để theo dõi trạng thái trình duyệt trong mini-app"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Mở Trình duyệt"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Tải từ URL Từ xa"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Tệp cookie YouTube đã được tải xuống qua fallback và lưu dưới dạng cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Không tìm thấy trình duyệt được hỗ trợ và không có COOKIE_URL được cấu hình. Sử dụng /cookie hoặc tải lên cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ COOKIE_URL fallback phải trỏ đến tệp .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Tệp cookie fallback quá lớn (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Nguồn cookie fallback không khả dụng (trạng thái {status}). Thử /cookie hoặc tải lên cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Lỗi khi tải xuống cookie fallback. Thử /cookie hoặc tải lên cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Lỗi không mong đợi trong quá trình tải xuống cookie fallback."
    BTN_CLOSE = "🔚Đóng"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Giá trị boolean không hợp lệ"
    ARGS_CLOSED_MSG = "Đã đóng"
    ARGS_ALL_RESET_MSG = "✅ Đã đặt lại tất cả các đối số"
    ARGS_RESET_ERROR_MSG = "❌ Lỗi khi đặt lại đối số"
    ARGS_INVALID_PARAM_MSG = "❌ Tham số không hợp lệ"
    ARGS_BOOL_SET_MSG = "Đặt thành {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "Đã đặt thành {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Giá trị lựa chọn không hợp lệ"
    ARGS_VALUE_SET_MSG = "Đặt thành {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "Đã đặt thành {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Giá trị hiện tại:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Ví dụ:</b>\n• <code>default</code> - Sử dụng chiến lược XFF mặc định\n• <code>never</code> - Không bao giờ sử dụng tiêu đề XFF\n• <code>US</code> - Mã quốc gia Hoa Kỳ\n• <code>GB</code> - Mã quốc gia Vương quốc Anh\n• <code>DE</code> - Mã quốc gia Đức\n• <code>FR</code> - Mã quốc gia Pháp\n• <code>JP</code> - Mã quốc gia Nhật Bản\n• <code>192.168.1.0/24</code> - Khối IP (CIDR)\n• <code>10.0.0.0/8</code> - Phạm vi IP riêng\n• <code>203.0.113.0/24</code> - Khối IP công cộng\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Lưu ý:</b> Điều này thay thế các tùy chọn --geo-bypass. Sử dụng bất kỳ mã quốc gia 2 chữ cái hoặc khối IP trong ký hiệu CIDR.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Ví dụ:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Vui lòng gửi giá trị mới của bạn."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Phạm vi:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Vui lòng gửi một số."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Ví dụ:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Lưu ý:</b> Các tiêu đề này sẽ được thêm vào các tiêu đề Referer và User-Agent hiện có.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Đối số yt-dlp Hiện tại:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - Công tắc True/False\n• 📋 <b>Select</b> - Chọn từ các tùy chọn\n• 🔢 <b>Numeric</b> - Nhập số\n• 📝🔧 <b>Text</b> - Nhập văn bản/JSON</blockquote>\n\nCác cài đặt này sẽ được áp dụng cho tất cả lượt tải xuống của bạn."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "Bắt buộc kết nối IPv6",
        "force_ipv4": "Bắt buộc kết nối IPv4", 
        "no_live_from_start": "Không tải stream trực tiếp từ đầu",
        "live_from_start": "Tải stream trực tiếp từ đầu",
        "no_check_certificates": "Bỏ qua xác thực chứng chỉ HTTPS",
        "check_certificate": "Kiểm tra chứng chỉ SSL",
        "no_playlist": "Chỉ tải video đơn, không phải danh sách phát",
        "embed_metadata": "Nhúng metadata vào tệp video",
        "embed_thumbnail": "Nhúng thumbnail vào tệp video",
        "write_thumbnail": "Ghi thumbnail ra tệp",
        "ignore_errors": "Bỏ qua lỗi tải xuống và tiếp tục",
        "legacy_server_connect": "Cho phép kết nối máy chủ cũ",
        "concurrent_fragments": "Số lượng fragment đồng thời để tải xuống",
        "xff": "Chiến lược tiêu đề X-Forwarded-For",
        "user_agent": "Tiêu đề User-Agent",
        "impersonate": "Giả mạo trình duyệt",
        "referer": "Tiêu đề Referer",
        "geo_bypass": "Bỏ qua hạn chế địa lý",
        "hls_use_mpegts": "Sử dụng MPEG-TS cho HLS",
        "no_part": "Không sử dụng tệp .part",
        "no_continue": "Không tiếp tục tải xuống một phần",
        "audio_format": "Định dạng âm thanh",
        "video_format": "Định dạng video",
        "merge_output_format": "Định dạng đầu ra hợp nhất",
        "send_as_file": "Gửi dưới dạng tệp",
        "username": "Tên người dùng",
        "password": "Mật khẩu",
        "twofactor": "Mã xác thực hai yếu tố",
        "min_filesize": "Kích thước tệp tối thiểu (MB)",
        "max_filesize": "Kích thước tệp tối đa (MB)",
        "playlist_items": "Mục danh sách phát",
        "date": "Ngày",
        "datebefore": "Ngày trước",
        "dateafter": "Ngày sau",
        "http_headers": "Tiêu đề HTTP",
        "sleep_interval": "Khoảng thời gian chờ",
        "max_sleep_interval": "Khoảng thời gian chờ tối đa",
        "retries": "Số lần thử lại",
        "http_chunk_size": "Kích thước chunk HTTP",
        "sleep_subtitles": "Chờ cho phụ đề"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ Cấu hình Đối số yt-dlp</b>\n\n<blockquote>📋 <b>Nhóm:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ Cấu hình Đối số yt-dlp</b>\n\n"
        "<blockquote>📋 <b>Nhóm:</b>\n"
        "• ✅/❌ <b>Boolean</b> - Công tắc True/False\n"
        "• 📋 <b>Select</b> - Chọn từ các tùy chọn\n"
        "• 🔢 <b>Numeric</b> - Nhập số\n"
        "• 📝🔧 <b>Text</b> - Nhập văn bản/JSON</blockquote>\n\n"
        "Các cài đặt này sẽ được áp dụng cho tất cả lượt tải xuống của bạn."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Vui lòng đợi..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Đã xảy ra lỗi"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Chế độ nhập tự động đóng do không hoạt động (5 phút)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Đầu vào chứa nội dung có khả năng nguy hiểm: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Đầu vào quá dài (tối đa 1000 ký tự)"
    ARGS_INVALID_URL_MSG = "❌ Định dạng URL không hợp lệ. Phải bắt đầu bằng http:// hoặc https://"
    ARGS_INVALID_JSON_MSG = "❌ Định dạng JSON không hợp lệ"
    ARGS_NUMBER_RANGE_MSG = "❌ Số phải nằm giữa {min_val} và {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Định dạng số không hợp lệ"
    ARGS_DATE_FORMAT_MSG = "❌ Ngày phải ở định dạng YYYYMMDD (ví dụ: 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Năm phải nằm giữa 1900 và 2100"
    ARGS_MONTH_RANGE_MSG = "❌ Tháng phải nằm giữa 01 và 12"
    ARGS_DAY_RANGE_MSG = "❌ Ngày phải nằm giữa 01 và 31"
    ARGS_INVALID_DATE_MSG = "❌ Định dạng ngày không hợp lệ"
    ARGS_INVALID_XFF_MSG = "❌ XFF phải là 'default', 'never', mã quốc gia (ví dụ: US), hoặc khối IP (ví dụ: 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "Không có đối số tùy chỉnh nào được đặt. Tất cả các tham số sử dụng giá trị mặc định."
    ARGS_RESET_SUCCESS_MSG = "✅ Tất cả đối số đã được đặt lại về mặc định."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Văn bản quá dài. Tối đa 500 ký tự."
    ARGS_ERROR_PROCESSING_MSG = "❌ Lỗi xử lý đầu vào. Vui lòng thử lại."
    ARGS_BOOL_INPUT_MSG = "❌ Vui lòng nhập 'True' hoặc 'False' cho tùy chọn Gửi Dưới dạng Tệp."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Vui lòng cung cấp một số hợp lệ."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Vui lòng gửi <code>True</code> hoặc <code>False</code> để bật/tắt tùy chọn này."
    ARGS_JSON_VALUE_REQUEST_MSG = "Vui lòng gửi JSON hợp lệ."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "Bạn chưa có thẻ nào."
    TAGS_MESSAGE_CLOSED_MSG = "Tin nhắn thẻ đã đóng."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Phụ đề đã tắt và chế độ Luôn Hỏi đã tắt."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Luôn Hỏi đã bật."
    SUBS_LANGUAGE_SET_MSG = "✅ Ngôn ngữ phụ đề đã đặt thành: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️CẢNH BÁO: do tác động CPU cao, chức năng này rất chậm (gần thời gian thực) và bị giới hạn:\n"
        "- Chất lượng tối đa 720p\n"
        "- Thời lượng tối đa 1.5 giờ\n"
        "- Kích thước video tối đa 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Lệnh nhanh:</b>\n"
        "• <code>/subs off</code> - tắt phụ đề\n"
        "• <code>/subs on</code> - bật chế độ Luôn Hỏi\n"
        "• <code>/subs ru</code> - đặt ngôn ngữ\n"
        "• <code>/subs ru auto</code> - đặt ngôn ngữ với AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Phụ đề đã tắt"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Ngôn ngữ đã chọn: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Đang tải xuống phụ đề..."
    SUBS_DISABLED_ERROR_MSG = "❌ Phụ đề đã tắt. Sử dụng /subs để cấu hình."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Tải xuống phụ đề chỉ được hỗ trợ cho YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Phụ đề</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Ngôn ngữ:</b> {lang}\n"
        "<b>Loại:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Tệp phụ đề SRT đã được gửi cho người dùng."
    SUBS_ERROR_PROCESSING_MSG = "❌ Lỗi xử lý tệp phụ đề."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Không thể tải xuống phụ đề."
    SUBS_ERROR_MSG = "❌ Lỗi tải xuống phụ đề: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Kích thước phần chia đã đặt thành: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **Kích thước không hợp lệ!**\n\n"
        "**Phạm vi hợp lệ:** 100MB đến 2GB\n\n"
        "**Định dạng hợp lệ:**\n"
        "• `100mb` đến `2000mb` (megabyte)\n"
        "• `0.1gb` đến `2gb` (gigabyte)\n\n"
        "**Ví dụ:**\n"
        "• `/split 100mb` - 100 megabyte\n"
        "• `/split 500mb` - 500 megabyte\n"
        "• `/split 1.5gb` - 1.5 gigabyte\n"
        "• `/split 2gb` - 2 gigabyte\n"
        "• `/split 2000mb` - 2000 megabyte (2GB)\n\n"
        "**Cài đặt sẵn:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Chọn kích thước phần tối đa để chia video:**\n\n"
        "**Phạm vi:** 100MB đến 2GB\n\n"
        "**Lệnh nhanh:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Ví dụ:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Menu đã đóng."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Cài đặt Bot</b>\n\nChọn một danh mục:"
    SETTINGS_MENU_CLOSED_MSG = "Menu đã đóng."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Tùy chọn Dọn dẹp</b>\n\nChọn những gì cần dọn dẹp:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIE</b>\n\nChọn một hành động:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 PHƯƠNG TIỆN</b>\n\nChọn một hành động:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 THÔNG TIN</b>\n\nChọn một hành động:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ LỆNH KHÁC</b>\n\nChọn một hành động:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Lệnh đã được thực thi."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Giới hạn flood. Thử lại sau."
    SETTINGS_HINT_SENT_MSG = "Gợi ý đã được gửi."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Trợ lý tìm kiếm đã mở."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Lệnh không xác định."
    SETTINGS_HINT_CLOSED_MSG = "Gợi ý đã đóng."
    SETTINGS_HELP_SENT_MSG = "Gửi tệp trợ giúp cho người dùng"
    SETTINGS_MENU_OPENED_MSG = "Đã mở menu /settings"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Trợ lý tìm kiếm đã đóng"
    SEARCH_CLOSED_MSG = "Đã đóng"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proxy {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Lỗi khi lưu cài đặt proxy."
    PROXY_MENU_TEXT_MSG = "Bật hoặc tắt sử dụng máy chủ proxy cho tất cả các thao tác yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Bật hoặc tắt việc sử dụng máy chủ proxy (có sẵn {config_count} + {file_count}) cho tất cả hoạt động yt-dlp?\n\nKhi được bật TẤT CẢ (TỰ ĐỘNG), proxy sẽ được chọn bằng phương pháp ngẫu nhiên."
    PROXY_MENU_CLOSED_MSG = "Menu đã đóng."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy đã bật. Tất cả các thao tác yt-dlp sẽ sử dụng proxy."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy đã bật. Tất cả các thao tác yt-dlp sẽ sử dụng {count} máy chủ proxy với phương pháp chọn {method}."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ Đã bật proxy (TẤT CẢ chế độ TỰ ĐỘNG).\n\n📊 Bot sẽ thử proxy theo thứ tự sau:\n1️⃣ {config_count} proxy từ Config.py\n2️⃣ {file_count} proxy từ tệp TXT/proxy.txt\n\n🔄 Tất cả các proxy sẽ được thử tuần tự cho đến khi kết nối thành công."
    PROXY_DISABLED_MSG = "❌ Proxy đã tắt."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Lỗi khi lưu cài đặt proxy."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy đã bật."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy đã tắt."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ ĐỢI CHO ĐẾN KHI LƯỢT TẢI XUỐNG TRƯỚC CỦA BẠN HOÀN TẤT"
    AUDIO_HELP_MSG = (
        "<b>🎧 Lệnh Tải Xuống Âm thanh</b>\n\n"
        "Sử dụng: <code>/audio URL</code>\n\n"
        "<b>Ví dụ:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Xem thêm: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Gợi ý âm thanh đã đóng."
    PLAYLIST_HELP_CLOSED_MSG = "Trợ giúp danh sách phát đã đóng."
    USERLOGS_CLOSED_MSG = "Tin nhắn log đã đóng."
    HELP_CLOSED_MSG = "Trợ giúp đã đóng."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>Cài đặt Làm mờ NSFW</b>\n\nNội dung NSFW là <b>{status}</b>.\n\nChọn có làm mờ nội dung NSFW hay không:"
    NSFW_MENU_CLOSED_MSG = "Menu đã đóng."
    NSFW_BLUR_DISABLED_MSG = "Làm mờ NSFW đã tắt."
    NSFW_BLUR_ENABLED_MSG = "Làm mờ NSFW đã bật."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Làm mờ NSFW đã tắt."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Làm mờ NSFW đã bật."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Bật hoặc tắt gửi MediaInfo cho các tệp đã tải xuống?"
    MEDIAINFO_MENU_CLOSED_MSG = "Menu đã đóng."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo đã bật. Sau khi tải xuống, thông tin tệp sẽ được gửi."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo đã tắt."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo đã bật."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo đã tắt."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 Liệt kê Định dạng Có sẵn</b>\n\n"
        "Lấy định dạng video/âm thanh có sẵn cho một URL.\n\n"
        "<b>Sử dụng:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Ví dụ:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 Cách sử dụng ID định dạng:</b>\n"
        "Sau khi lấy danh sách, sử dụng ID định dạng cụ thể:\n"
        "• <code>/format id 401</code> - tải định dạng 401\n"
        "• <code>/format id401</code> - giống như trên\n"
        "• <code>/format id140 audio</code> - tải định dạng 140 dưới dạng âm thanh MP3\n\n"
        "Lệnh này sẽ hiển thị tất cả các định dạng có sẵn có thể được tải xuống."
    )
    LIST_PROCESSING_MSG = "🔄 Đang lấy định dạng có sẵn..."
    LIST_INVALID_URL_MSG = "❌ Vui lòng cung cấp URL hợp lệ bắt đầu bằng http:// hoặc https://"
    LIST_CAPTION_MSG = (
        "📃 Định dạng có sẵn cho:\n<code>{url}</code>\n\n"
        "💡 <b>Cách đặt định dạng:</b>\n"
        "• <code>/format id 134</code> - Tải ID định dạng cụ thể\n"
        "• <code>/format 720p</code> - Tải theo chất lượng\n"
        "• <code>/format best</code> - Tải chất lượng tốt nhất\n"
        "• <code>/format ask</code> - Luôn hỏi chất lượng\n\n"
        "{audio_note}\n"
        "📋 Sử dụng ID định dạng từ danh sách trên"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Định dạng chỉ âm thanh:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Tải định dạng 140 dưới dạng âm thanh MP3\n"
        "• <code>/format id140 audio</code> - giống như trên\n"
        "Những định dạng này sẽ được tải xuống dưới dạng tệp âm thanh MP3.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Lỗi khi gửi tệp định dạng: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Không thể lấy định dạng:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ Đã xảy ra lỗi khi xử lý lệnh"
    LIST_ERROR_CALLBACK_MSG = "Đã xảy ra lỗi"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 Cách sử dụng ID định dạng:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "Sau khi lấy danh sách, sử dụng ID định dạng cụ thể:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - tải định dạng 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - giống như trên\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - tải định dạng 140 dưới dạng âm thanh MP3\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - giống như trên\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Đã phát hiện định dạng chỉ âm thanh: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "Những định dạng này sẽ được tải xuống dưới dạng tệp âm thanh MP3.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Định dạng chỉ video:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 Sử dụng ID định dạng từ danh sách trên"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Sử dụng:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>Ví dụ:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - chất lượng tốt nhất\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p hoặc thấp hơn\n"
        "• /link 720p https://youtube.com/watch?v=... - giống như trên\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K hoặc thấp hơn\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K hoặc thấp hơn"
        "</blockquote>\n\n"
        "<b>Chất lượng:</b> từ 1 đến 10000 (ví dụ: 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Vui lòng cung cấp URL hợp lệ"
    LINK_PROCESSING_MSG = "🔗 Đang lấy liên kết trực tiếp..."
    LINK_DURATION_MSG = "⏱ <b>Thời lượng:</b> {duration} giây\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Stream video:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Stream âm thanh:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Cài đặt bàn phím đã được cập nhật!**\n\nCài đặt mới: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Đối số không hợp lệ!**\n\n"
        "Tùy chọn hợp lệ: `off`, `1x3`, `2x3`, `full`\n\n"
        "Ví dụ: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Cài đặt Bàn phím**\n\n"
        "Hiện tại: **{current}**\n\n"
        "Chọn một tùy chọn:\n\n"
        "Hoặc sử dụng: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 bàn phím đã được kích hoạt!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Bàn phím đã ẩn"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 Bàn phím 1x3 đã được kích hoạt!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 Bàn phím 2x3 đã được kích hoạt!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Bàn phím emoji đã được kích hoạt!"
    KEYBOARD_ERROR_APPLYING_MSG = "Lỗi khi áp dụng cài đặt bàn phím {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Định dạng đã đặt thành: Luôn Hỏi. Bạn sẽ được nhắc về chất lượng mỗi khi gửi URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Định dạng đã đặt thành: Luôn Hỏi. Bây giờ bạn sẽ được nhắc về chất lượng mỗi khi gửi URL."
    FORMAT_BEST_UPDATED_MSG = "✅ Định dạng đã được cập nhật thành chất lượng tốt nhất (ưu tiên AVC+MP4):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Định dạng đã được cập nhật thành ID {id}:\n{format}\n\n💡 <b>Lưu ý:</b> Nếu đây là định dạng chỉ âm thanh, nó sẽ được tải xuống dưới dạng tệp âm thanh MP3."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Định dạng đã được cập nhật thành ID {id} (chỉ âm thanh):\n{format}\n\n💡 Điều này sẽ được tải xuống dưới dạng tệp âm thanh MP3."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Định dạng đã được cập nhật thành chất lượng {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Định dạng đã được cập nhật thành:\n{format}"
    FORMAT_MENU_MSG = (
        "Chọn một tùy chọn định dạng hoặc gửi một tùy chọn tùy chỉnh bằng cách sử dụng:\n"
        "• <code>/format &lt;format_string&gt;</code> - định dạng tùy chỉnh\n"
        "• <code>/format 720</code> - chất lượng 720p\n"
        "• <code>/format 4k</code> - chất lượng 4K\n"
        "• <code>/format 8k</code> - chất lượng 8K\n"
        "• <code>/format id 401</code> - ID định dạng cụ thể\n"
        "• <code>/format ask</code> - luôn hiển thị menu\n"
        "• <code>/format best</code> - bv+ba/chất lượng tốt nhất"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "Để sử dụng định dạng tùy chỉnh, gửi lệnh theo dạng sau:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Thay thế <code>bestvideo+bestaudio/best</code> bằng chuỗi định dạng mong muốn của bạn."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Chọn độ phân giải và codec mong muốn của bạn:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Định dạng đã đặt thành: Luôn Hỏi. Bây giờ bạn sẽ được nhắc về chất lượng mỗi khi gửi URL."
    FORMAT_UPDATED_MSG = "✅ Định dạng đã được cập nhật thành:\n{format}"
    FORMAT_SAVED_MSG = "✅ Định dạng đã được lưu."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Lựa chọn định dạng đã được cập nhật."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Menu định dạng tùy chỉnh đã đóng"
    FORMAT_CODEC_SET_MSG = "✅ Codec đã đặt thành {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Lựa chọn trình duyệt đã được cập nhật."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Truy cập bị từ chối. Chỉ dành cho admin."
    ACCESS_DENIED_ADMIN = "❌ Truy cập bị từ chối. Chỉ dành cho admin."
    WELCOME_MASTER = "Chào mừng Thầy 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Xin lỗi... Đã xảy ra lỗi trong quá trình tải xuống."
    SIZE_LIMIT_EXCEEDED = "❌ Kích thước tệp vượt quá giới hạn {max_size_gb} GB. Vui lòng chọn tệp nhỏ hơn trong phạm vi kích thước được phép."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Không tìm thấy script: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Đang tải xuống Firebase dump mới bằng {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase cache đã được tải lại thành công!"
    ADMIN_CACHE_FAILED_MSG = "❌ Không thể tải lại Firebase cache. Kiểm tra xem {cache_file} có tồn tại không."
    ADMIN_ERROR_RELOADING_MSG = "❌ Lỗi khi tải lại cache: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Lỗi khi chạy {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Tin nhắn quảng cáo đã được gửi đến tất cả người dùng khác</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Không thể gửi tin nhắn quảng cáo. Thử trả lời một tin nhắn\nHoặc đã xảy ra lỗi</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ Người dùng chưa tải xuống nội dung nào...</b> Không tồn tại trong log"
    ADMIN_INVALID_COMMAND_MSG = "❌ Lệnh không hợp lệ"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ Không tìm thấy dữ liệu trong cache cho <code>{{path}}</code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Hàng đợi trống — chưa có ai rời khỏi kênh."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Hàng đợi cấm</b>\nTổng đang chờ: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (rời: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… và {extra} người dùng khác."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "Sử dụng /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Đã chặn người dùng từ hàng đợi: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Tự động chặn đã bật: những người rời mới sẽ bị cấm ngay lập tức."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Tự động chặn đã tắt."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ Cửa sổ tự động chặn theo lịch đã đặt thành mỗi {interval}."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 Nhật ký hoạt động kênh trong {hours} giờ qua (2 ngày)."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 {hours} giờ qua (2 ngày): đã tham gia {joined}, đã rời {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ Không có hoạt động nào trong {hours} giờ qua (2 ngày)."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "Tổng: 🟢 {joined} đã tham gia, 🔴 {left} đã rời."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ Không có quyền truy cập vào nhật ký hoạt động kênh. Bot không thể đọc log admin. Cung cấp CHANNEL_GUARD_SESSION_STRING trong config với session người dùng để bật tính năng này."
    BAN_TIME_USAGE_MSG = "❌ Sử dụng: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ Sử dụng định dạng như 10s, 6m, 5h, 4d, 3w, 2M hoặc 1y."
    BAN_TIME_SET_MSG = "🕒 Khoảng thời gian quét log kênh đã đặt thành {interval}."
    BAN_TIME_REPORT_MSG = (
        "🛡️ Báo cáo quét kênh\n"
        "Chạy lúc: {run_ts}\n"
        "Khoảng thời gian: {interval}\n"
        "Người rời mới: {new_leavers}\n"
        "Tự động cấm: {auto_banned}\n"
        "Đang chờ: {pending}\n"
        "event_id cuối: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Sử dụng: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Admin không thể xóa admin"
    ADMIN_USER_BLOCKED_MSG = "Người dùng đã bị chặn 🔒❌\n \nID: <code>{user_id}</code>\nNgày chặn: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> đã bị chặn ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Xin lỗi! Bạn không phải là admin"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Sử dụng: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "Người dùng đã được bỏ chặn 🔓✅\n \nID: <code>{user_id}</code>\nNgày bỏ chặn: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> đã được bỏ chặn ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ Đã bỏ chặn người dùng: {count}\n⏱ Dấu thời gian: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ Sử dụng: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "Người dùng bị bỏ qua 👁️❌\n \nID: <code>{user_id}</code>\nNgày bỏ qua: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> đã bị bỏ qua ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ Sử dụng: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "Người dùng không còn bị bỏ qua 👁️✅\n \nID: <code>{user_id}</code>\nNgày không bỏ qua: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> không bị bỏ qua ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Thời gian chạy bot -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Vui lòng cung cấp URL để xóa cache.\nSử dụng: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Vui lòng cung cấp URL hợp lệ.\nSử dụng: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Cache đã được xóa thành công cho URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ Không tìm thấy cache cho liên kết này."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Lỗi khi xóa cache: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Truy cập bị từ chối. Chỉ dành cho admin."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Đang chạy script cập nhật danh sách porn: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Script đã hoàn thành thành công!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Script đã hoàn thành thành công!\n\nĐầu ra:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Script thất bại với mã trả về {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Lỗi khi chạy script: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Đang tải lại cache porn và liên quan đến domain..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Cache porn đã được tải lại thành công!\n\n"
        "📊 Trạng thái cache hiện tại:\n"
        "• Domain porn: {porn_domains}\n"
        "• Từ khóa porn: {porn_keywords}\n"
        "• Trang web được hỗ trợ: {supported_sites}\n"
        "• WHITELIST: {whitelist}\n"
        "• GREYLIST: {greylist}\n"
        "• BLACK_LIST: {black_list}\n"
        "• WHITE_KEYWORDS: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Lỗi khi tải lại cache porn: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Vui lòng cung cấp URL để kiểm tra.\nSử dụng: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Vui lòng cung cấp URL hợp lệ.\nSử dụng: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Đang kiểm tra URL cho nội dung NSFW...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Kết quả Kiểm tra Porn</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Trạng thái:</b> <b>{status_text}</b>\n\n"
        "<b>Giải thích:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Lỗi khi kiểm tra URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Cookie đã được dọn dẹp."
    CLEAN_LOGS_CLEANED_MSG = "log đã được dọn dẹp."
    CLEAN_TAGS_CLEANED_MSG = "thẻ đã được dọn dẹp."
    CLEAN_FORMAT_CLEANED_MSG = "định dạng đã được dọn dẹp."
    CLEAN_SPLIT_CLEANED_MSG = "split đã được dọn dẹp."
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfo đã được dọn dẹp."
    CLEAN_SUBS_CLEANED_MSG = "Cài đặt phụ đề đã được dọn dẹp."
    CLEAN_KEYBOARD_CLEANED_MSG = "Cài đặt bàn phím đã được dọn dẹp."
    CLEAN_ARGS_CLEANED_MSG = "Cài đặt args đã được dọn dẹp."
    CLEAN_NSFW_CLEANED_MSG = "Cài đặt NSFW đã được dọn dẹp."
    CLEAN_PROXY_CLEANED_MSG = "Cài đặt proxy đã được dọn dẹp."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Cài đặt flood wait đã được dọn dẹp."
    CLEAN_ALL_CLEANED_MSG = "Tất cả tệp đã được dọn dẹp."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIE</b>\n\nChọn một hành động:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Tệp cookie đã được lưu"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Đã bỏ qua xác thực cho cookie không phải YouTube"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Tệp cookie tồn tại nhưng có định dạng không đúng"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Không tìm thấy tệp cookie."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Đang bắt đầu kiểm tra cookie YouTube...\n\nVui lòng đợi trong khi tôi kiểm tra và xác thực cookie của bạn."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Cookie YouTube hiện có của bạn đang hoạt động tốt!\n\nKhông cần tải xuống cookie mới."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Cookie YouTube hiện có của bạn đã hết hạn hoặc không hợp lệ.\n\n🔄 Đang tải xuống cookie mới..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ Nguồn cookie {service} chưa được cấu hình!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ Nguồn cookie {service} phải là tệp .txt!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Giới hạn phạm vi vượt quá: {range_count} tệp được yêu cầu (tối đa {max_img_files}).\n\nSử dụng một trong các lệnh sau để tải xuống tối đa các tệp có sẵn:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Đóng"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Giới hạn phương tiện vượt quá: {count} tệp được yêu cầu (tối đa {max_count}).\n\nSử dụng một trong các lệnh sau để tải xuống tối đa các tệp có sẵn:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 Đã tìm thấy <b>{count}</b> mục phương tiện từ liên kết"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "Chọn phạm vi tải xuống:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Giả mạo trình duyệt"
    ARGS_REFERER_DESC_MSG = "Tiêu đề Referer"
    ARGS_USER_AGENT_DESC_MSG = "Tiêu đề User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "Bỏ qua hạn chế địa lý"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Kiểm tra chứng chỉ SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "Tải stream trực tiếp từ đầu"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Không tải stream trực tiếp từ đầu"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Sử dụng container MPEG-TS cho video HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "Chỉ tải video đơn, không phải danh sách phát"
    ARGS_NO_PART_DESC_MSG = "Không sử dụng tệp .part"
    ARGS_NO_CONTINUE_DESC_MSG = "Không tiếp tục tải xuống một phần"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Định dạng âm thanh để trích xuất"
    ARGS_EMBED_METADATA_DESC_MSG = "Nhúng metadata vào tệp video"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Nhúng thumbnail vào tệp video"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Ghi thumbnail ra tệp"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Số lượng fragment đồng thời để tải xuống"
    ARGS_FORCE_IPV4_DESC_MSG = "Bắt buộc kết nối IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "Bắt buộc kết nối IPv6"
    ARGS_XFF_DESC_MSG = "Chiến lược tiêu đề X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "Kích thước chunk HTTP (byte)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Chờ trước khi tải phụ đề (giây)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Cho phép kết nối máy chủ cũ"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Bỏ qua xác thực chứng chỉ HTTPS"
    ARGS_USERNAME_DESC_MSG = "Tên người dùng tài khoản"
    ARGS_PASSWORD_DESC_MSG = "Mật khẩu tài khoản"
    ARGS_TWOFACTOR_DESC_MSG = "Mã xác thực hai yếu tố"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Bỏ qua lỗi tải xuống và tiếp tục"
    ARGS_MIN_FILESIZE_DESC_MSG = "Kích thước tệp tối thiểu (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Kích thước tệp tối đa (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Mục danh sách phát để tải xuống (ví dụ: 1,3,5 hoặc 1-5)"
    ARGS_DATE_DESC_MSG = "Tải video đã tải lên vào ngày này (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Tải video đã tải lên trước ngày này (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Tải video đã tải lên sau ngày này (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Tiêu đề HTTP tùy chỉnh (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Khoảng thời gian chờ giữa các yêu cầu (giây)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Khoảng thời gian chờ tối đa (giây)"
    ARGS_RETRIES_DESC_MSG = "Số lần thử lại"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Định dạng container video"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Định dạng container đầu ra để hợp nhất"
    ARGS_SEND_AS_FILE_DESC_MSG = "Gửi tất cả phương tiện dưới dạng tài liệu thay vì phương tiện"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Giả mạo"
    ARGS_REFERER_SHORT_MSG = "Referer"
    ARGS_GEO_BYPASS_SHORT_MSG = "Bỏ qua Địa lý"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Kiểm tra Chứng chỉ"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Trực tiếp Từ đầu"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Không Trực tiếp Từ đầu"
    ARGS_USER_AGENT_SHORT_MSG = "User Agent"  # User-Agent is a technical term, can remain
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Không Danh sách phát"
    ARGS_NO_PART_SHORT_MSG = "Không Phần"
    ARGS_NO_CONTINUE_SHORT_MSG = "Không Tiếp tục"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Định dạng Âm thanh"
    ARGS_EMBED_METADATA_SHORT_MSG = "Nhúng Meta"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Nhúng Thumb"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Ghi Thumb"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Đồng thời"
    ARGS_FORCE_IPV4_SHORT_MSG = "Bắt buộc IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Bắt buộc IPv6"
    ARGS_XFF_SHORT_MSG = "Tiêu đề XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Kích thước Chunk"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Chờ Phụ đề"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Kết nối Cũ"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Không Kiểm tra Chứng chỉ"
    ARGS_USERNAME_SHORT_MSG = "Tên người dùng"
    ARGS_PASSWORD_SHORT_MSG = "Mật khẩu"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Bỏ qua Lỗi"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Kích thước Tối thiểu"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Kích thước Tối đa"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Mục Danh sách phát"
    ARGS_DATE_SHORT_MSG = "Ngày"
    ARGS_DATEBEFORE_SHORT_MSG = "Ngày Trước"
    ARGS_DATEAFTER_SHORT_MSG = "Ngày Sau"
    ARGS_HTTP_HEADERS_SHORT_MSG = "Tiêu đề HTTP"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Khoảng thời gian Chờ"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Chờ Tối đa"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Định dạng Video"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Định dạng Hợp nhất"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Gửi Dưới dạng Tệp"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ Tệp quá lớn. Kích thước tối đa là 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Chỉ cho phép tệp có định dạng .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ Tệp không giống cookie.txt (không có dòng '# Netscape HTTP Cookie File')."
    COOKIES_ERROR_READING_MSG = "❌ Lỗi khi đọc tệp: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Tệp cookie tồn tại và có định dạng đúng"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ Tệp cookie {service} quá lớn! Tối đa 100KB, nhận được {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ Tệp cookie {service} đã được tải xuống và lưu dưới dạng cookie.txt trong thư mục của bạn.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ Nguồn cookie {service} không khả dụng (trạng thái {status}). Vui lòng thử lại sau."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Lỗi khi tải xuống tệp cookie {service}. Vui lòng thử lại sau."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ Người dùng đã cung cấp tệp cookie mới.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie đã được cập nhật thành công:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Không phải cookie hợp lệ.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ Nguồn cookie YouTube chưa được cấu hình!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Đang tải xuống và kiểm tra cookie YouTube...\n\nLần thử {attempt} trong tổng {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Truy cập bị từ chối. Chỉ dành cho admin."
    ADMIN_USER_LOGS_TOTAL_MSG = "Tổng: <b>{total}</b>\n<b>{user_id}</b> - log (10 mục cuối):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 bàn phím đã được kích hoạt!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Ngôn ngữ phụ đề đã đặt thành: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Ngôn ngữ phụ đề đã đặt thành: {flag} {name} với AUTO/TRANS đã bật."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Menu ngôn ngữ phụ đề đã đóng."
    SUBS_DOWNLOADING_MSG = "💬 Đang tải xuống phụ đề..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Đang tải lại Firebase cache vào bộ nhớ..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ Không có COOKIE_URL được cấu hình. Sử dụng /cookie hoặc tải lên cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Đang tải cookie từ URL từ xa..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ COOKIE_URL fallback phải trỏ đến tệp .txt."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Tệp cookie fallback quá lớn (>100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Tệp cookie YouTube đã được tải xuống qua fallback và lưu dưới dạng cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Nguồn cookie fallback không khả dụng (trạng thái {status}). Thử /cookie hoặc tải lên cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Lỗi khi tải xuống cookie fallback. Thử /cookie hoặc tải lên cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Lỗi không mong đợi trong quá trình tải xuống cookie fallback."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ Trình duyệt {browser} chưa được cài đặt."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookie đã được lưu bằng trình duyệt: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Không thể lưu cookie: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ Cookie YouTube đang hoạt động tốt"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ Cookie YouTube đã hết hạn hoặc không hợp lệ\n\nSử dụng /cookie để lấy cookie mới"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - định dạng tùy chỉnh\n• <code>/format 720</code> - chất lượng 720p\n• <code>/format 4k</code> - chất lượng 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Gợi ý đã được gửi."
    FORMAT_MKV_TOGGLE_MSG = "MKV hiện là {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Không có URL từ xa được cấu hình"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Định dạng tệp không hợp lệ"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Tệp quá lớn"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookie đã được tải xuống thành công"
    COOKIES_SERVER_ERROR_MSG = "❌ Lỗi máy chủ {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Tải xuống thất bại"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Lỗi không mong đợi"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Trình duyệt chưa được cài đặt."
    COOKIES_MENU_CLOSED_MSG = "Menu đã đóng."
    COOKIES_HINT_CLOSED_MSG = "Gợi ý cookie đã đóng."
    IMG_HELP_CLOSED_MSG = "Trợ giúp đã đóng."
    SUBS_LANGUAGE_UPDATED_MSG = "Cài đặt ngôn ngữ phụ đề đã được cập nhật."
    SUBS_MENU_CLOSED_MSG = "Menu ngôn ngữ phụ đề đã đóng."
    KEYBOARD_SET_TO_MSG = "Bàn phím đã đặt thành {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Lỗi xử lý cài đặt"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo đã bật."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo đã tắt."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "Làm mờ NSFW đã tắt."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "Làm mờ NSFW đã bật."
    SETTINGS_MENU_CLOSED_MSG = "Menu đã đóng."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Flood wait đang hoạt động. Thử lại sau."
    OTHER_HELP_CLOSED_MSG = "Trợ giúp đã đóng."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Tin nhắn log đã đóng."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Menu đã đóng."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Kích thước không hợp lệ."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Lỗi khi gửi MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ Đã xảy ra lỗi: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - tất cả log"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - tất cả {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Tải từ URL Từ xa"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Mở Trình duyệt"
    SELECT_BROWSER_MSG = "Chọn trình duyệt để tải cookie từ:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Không tìm thấy trình duyệt nào trên hệ thống này. Bạn có thể tải cookie từ URL từ xa hoặc theo dõi trạng thái trình duyệt:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Mở Trình duyệt</b> - để theo dõi trạng thái trình duyệt trong mini-app"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Không thể chạy /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Giới hạn flood. Thử lại sau."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Không thể mở menu cookie trình duyệt"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Gợi ý lưu dưới dạng cookie đã đóng."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Sử dụng:</b>\n<code>/link [quality] URL</code>\n\n<b>Ví dụ:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - chất lượng tốt nhất\n• /link 720 https://youtube.com/watch?v=... - 720p hoặc thấp hơn\n• /link 720p https://youtube.com/watch?v=... - giống như trên\n• /link 4k https://youtube.com/watch?v=... - 4K hoặc thấp hơn\n• /link 8k https://youtube.com/watch?v=... - 8K hoặc thấp hơn</blockquote>\n\n<b>Chất lượng:</b> từ 1 đến 10000 (ví dụ: 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - chất lượng 8K"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Liên kết trực tiếp đã được lấy</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Định dạng:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Stream âm thanh:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Không thể lấy liên kết stream"
    LINK_ERROR_GETTING_MSG = "❌ <b>Lỗi khi lấy liên kết:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Chỉ mục cookie YouTube không hợp lệ: {selected_index}. Phạm vi có sẵn là 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Đang tải xuống và kiểm tra cookie YouTube...\n\nLần thử {attempt} trong tổng {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Đang tải xuống và kiểm tra cookie YouTube...\n\nLần thử {attempt} trong tổng {total}\n🔍 Đang kiểm tra cookie..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ Cookie YouTube đã được tải xuống và xác thực thành công!\n\nĐã sử dụng nguồn {source} trong tổng {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Tất cả cookie YouTube đã hết hạn hoặc không khả dụng!\n\nLiên hệ quản trị viên bot để thay thế chúng."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ Giới hạn thử lại cookie YouTube đã vượt quá!\n\n🔢 Tối đa: {limit} lần thử mỗi giờ\n⏰ Vui lòng thử lại sau"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Thẻ #{wrong} chứa các ký tự bị cấm. Chỉ cho phép chữ cái, chữ số và _.\nVui lòng sử dụng: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Đối số không hợp lệ!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Ngôn ngữ phụ đề đã đặt: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Ví dụ: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Ngôn ngữ đã chọn: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Chế độ Luôn Hỏi {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Phụ đề đã tắt"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Cài đặt phụ đề</b>\n\n{status_text}\n\nChọn ngôn ngữ phụ đề:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - tắt phụ đề\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Cài đặt phụ đề</b>\n\n{status_text}\n\nChọn ngôn ngữ phụ đề:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Tiêu đề:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Thời lượng:</b> {duration} giây\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Stream video:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- Chất lượng tối đa 720p\n- Thời lượng tối đa 1.5 giờ\n- Kích thước video tối đa 500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️CẢNH BÁO: do tác động CPU cao, chức năng này rất chậm (gần thời gian thực) và bị giới hạn:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Lệnh nhanh:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - tắt phụ đề\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - bật chế độ Luôn Hỏi\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - đặt ngôn ngữ\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - đặt ngôn ngữ với AUTO/TRANS đã bật\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - bật chế độ Luôn Hỏi\n"
    SUBS_AUTO_SUBS_TEXT = " (phụ đề tự động)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Chế độ phụ đề tự động {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS đã tắt qua lệnh: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Luôn Hỏi đã bật qua lệnh: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "Ngôn ngữ SUBS đã đặt qua lệnh: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "Ngôn ngữ SUBS + chế độ tự động đã đặt qua lệnh: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Người dùng đã mở menu /subs."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "Người dùng đã đặt ngôn ngữ phụ đề thành: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "Người dùng đã chuyển chế độ AUTO/TRANS thành: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "Người dùng đã chuyển chế độ Luôn Hỏi thành: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Người dùng đã yêu cầu cookie từ trình duyệt."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Bàn phím chọn trình duyệt đã được gửi chỉ với các trình duyệt đã cài đặt."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Lựa chọn trình duyệt đã đóng."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "COOKIE_URL fallback đã được sử dụng thành công (nguồn ẩn)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "COOKIE_URL fallback thất bại: status={status} (ẩn)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "COOKIE_URL fallback lỗi không mong đợi: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Trình duyệt {browser} chưa được cài đặt."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Cookie đã được lưu bằng trình duyệt: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "Tệp cookie đã được lưu cho người dùng {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "Tệp cookie tồn tại, có định dạng đúng và cookie YouTube đang hoạt động."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Tệp cookie tồn tại và có định dạng đúng, nhưng cookie YouTube đã hết hạn."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Tệp cookie tồn tại và có định dạng đúng."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Tệp cookie tồn tại nhưng có định dạng không đúng."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Không tìm thấy tệp cookie."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "URL cookie {service} trống cho người dùng {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "URL cookie {service} không phải .txt (ẩn)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "Tệp cookie {service} quá lớn: {size} byte (nguồn ẩn)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "Tệp cookie {service} đã được tải xuống cho người dùng {user_id} (nguồn ẩn)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Không tìm thấy script: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Không thể gửi tin nhắn trạng thái ban đầu"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Lỗi khi chạy {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Firebase cache đã được tải lại bởi tác vụ tự động."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Firebase cache đã được tải lại bởi admin."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Lỗi khi tải lại Firebase cache: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Broadcast đã được khởi tạo. Văn bản:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Tin nhắn broadcast đã được gửi đến tất cả người dùng."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Không thể broadcast tin nhắn: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Admin {user_id} đã xóa cache cho URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Admin {user_id} đã bắt đầu script cập nhật danh sách porn: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Script cập nhật danh sách porn đã hoàn thành thành công bởi admin {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Script cập nhật danh sách porn thất bại bởi admin {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Admin {user_id} đã cố chạy script không tồn tại: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Lỗi khi chạy script cập nhật porn bởi admin {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Admin {user_id} đã bắt đầu tải lại cache porn"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Lỗi khi tải lại cache porn bởi admin {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Admin {user_id} đã kiểm tra URL cho NSFW: {url} - Kết quả: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "Người dùng đã yêu cầu thay đổi định dạng."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "Định dạng đã đặt thành ALWAYS_ASK."
    FORMAT_UPDATED_BEST_LOG_MSG = "Định dạng đã được cập nhật thành tốt nhất: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "Định dạng đã được cập nhật thành ID {format_id}: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "Định dạng đã được cập nhật thành ID {format_id} (chỉ âm thanh): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "Định dạng đã được cập nhật thành chất lượng {quality}: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "Định dạng đã được cập nhật thành: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "Menu định dạng đã được gửi."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "Lựa chọn định dạng đã đóng."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "Gợi ý định dạng tùy chỉnh đã được gửi."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "Menu độ phân giải định dạng đã được gửi."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "Đã quay lại menu định dạng chính."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "Định dạng đã được cập nhật thành: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "Định dạng đã đặt thành ALWAYS_ASK."
    FORMAT_CODEC_SET_LOG_MSG = "Tùy chọn codec đã đặt thành {codec}"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Menu định dạng tùy chỉnh đã đóng"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "Liên kết trực tiếp đã được trích xuất cho người dùng {user_id} từ {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Không thể trích xuất liên kết trực tiếp cho người dùng {user_id} từ {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Lỗi trong lệnh link cho người dùng {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "Người dùng {user_id} đã đặt bàn phím thành {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "Người dùng {user_id} đã đặt bàn phím thành {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo đã đặt qua lệnh: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Người dùng đã mở menu /mediainfo."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: đã đóng."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo đã bật."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo đã tắt."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Kích thước chia đã đặt thành {size} byte qua đối số."
    SPLIT_MENU_OPENED_LOG_MSG = "Người dùng đã mở menu /split."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Lựa chọn chia đã đóng."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Kích thước chia đã đặt thành {size} byte."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Proxy đã đặt qua lệnh: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Người dùng đã mở menu /proxy."
    PROXY_MENU_CLOSED_LOG_MSG = "Proxy: đã đóng."
    PROXY_ENABLED_LOG_MSG = "Proxy đã bật."
    PROXY_DISABLED_LOG_MSG = "Proxy đã tắt."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Tin nhắn trợ giúp đã đóng."
    AUDIO_HELP_SHOWN_LOG_MSG = "Đã hiển thị trợ giúp /audio"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Người dùng đã yêu cầu trợ giúp danh sách phát."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Trợ giúp danh sách phát đã đóng."
    AUDIO_HINT_CLOSED_LOG_MSG = "Gợi ý âm thanh đã đóng."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Menu liên kết trực tiếp đã được tạo qua nút LINK cho người dùng {user_id} từ {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Không thể trích xuất liên kết trực tiếp qua nút LINK cho người dùng {user_id} từ {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "Lệnh LIST đã được thực thi cho người dùng {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Nhúng Nhanh: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Menu Luôn Hỏi đã được gửi cho {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Đã tạo menu chất lượng cache cho người dùng {user_id} sau lỗi: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Lỗi menu Luôn Hỏi cho {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Định dạng được cố định qua cài đặt /args"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Âm thanh"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Video"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Video"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Tiếp theo ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ Trước"
    SUBTITLES_NEXT_BUTTON_MSG = "Tiếp theo ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Tất cả các trường văn bản đều trống"
    SENDER_VIDEO_DURATION_MSG = "Thời lượng video:"
    SENDER_UPLOADING_FILE_MSG = "📤 Đang tải tệp lên..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 Đang tải Video lên..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 Thời lượng video:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 tệp đã được tải lên."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Thông tin Video"
    DOWN_UP_NUMBER_MSG = "Số"
    DOWN_UP_TITLE_MSG = "Tiêu đề"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Video đã được tải xuống."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Đang xử lý để tải lên..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Phần {part} đã được chia và tải lên"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Tải lên hoàn tất"
    DOWN_UP_FILES_UPLOADED_MSG = "tệp đã được tải lên"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Đóng"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBS"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 SUBS"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Trình duyệt"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Đang lấy liên kết trực tiếp..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Đang lấy định dạng có sẵn..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 Đang lấy mô tả video..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ Lỗi khi lấy mô tả: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ Mô tả video không khả dụng"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ Lỗi khi gửi mô tả: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 Mô tả video đã được gửi cho người dùng {user_id} cho {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Đang bắt đầu gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Thời lượng:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Định dạng:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Trình duyệt:</b> Mở trong trình duyệt web"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Định dạng có sẵn cho"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 Cách sử dụng ID định dạng:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "Sau khi lấy danh sách, sử dụng ID định dạng cụ thể:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - tải định dạng 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - giống như trên"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - tải định dạng 140 dưới dạng âm thanh MP3"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Đã phát hiện định dạng chỉ âm thanh"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "Những định dạng này sẽ được tải xuống dưới dạng tệp âm thanh MP3."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>Cách đặt định dạng:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Tải ID định dạng cụ thể"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Tải theo chất lượng"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Tải chất lượng tốt nhất"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Luôn hỏi chất lượng"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Định dạng chỉ âm thanh:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Tải định dạng 140 dưới dạng âm thanh MP3"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "Những định dạng này sẽ được tải xuống dưới dạng tệp âm thanh MP3."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Sử dụng ID định dạng từ danh sách trên"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Lỗi: Không tìm thấy tin nhắn gốc."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Trang định dạng"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Lỗi khi hiển thị menu định dạng"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Lỗi khi lấy định dạng"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Lỗi khi lấy định dạng có sẵn."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Vui lòng thử lại sau."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp không thể xử lý nội dung này"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "Hệ thống khuyến nghị sử dụng gallery-dl thay thế."
    ALWAYS_ASK_OPTIONS_MSG = "**Tùy chọn:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• Đối với thư viện hình ảnh: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• Đối với hình ảnh đơn: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl thường hoạt động tốt hơn cho Instagram, Twitter và nội dung mạng xã hội khác."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Thử Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Định dạng được cố định qua /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Phụ đề"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Âm thanh lồng tiếng"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Phụ đề có sẵn"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Chọn ngôn ngữ phụ đề"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Không tìm thấy phụ đề và sẽ không nhúng"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Đăng lại ngay từ cache"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Chọn ngôn ngữ âm thanh"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW là có phí (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Chọn chất lượng tải xuống"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Tải hình ảnh (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Lấy liên kết trực tiếp đến video"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Hiển thị danh sách định dạng có sẵn"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Thay đổi phần mở rộng/codec video"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀Nhúng"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — Chỉ trích xuất âm thanh"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW là có phí (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Đăng lại ngay từ cache"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Chọn ngôn ngữ âm thanh"
    ALWAYS_ASK_BEST_BUTTON_MSG = "Tốt nhất"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Khác"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝chỉ phụ đề"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Nhóm thông minh"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Đã thêm hàng nút hành động (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Đã thêm hàng nút hành động (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Đã thêm nút dưới cùng vào hàng hiện có"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Đã tạo hàng dưới cùng mới"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Không tìm thấy video trong danh sách phát"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "URL không được hỗ trợ"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Không thể tìm thấy video"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Không tìm thấy video"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Không tìm thấy phương tiện"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "Tweet này không chứa"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Lỗi khi lấy thông tin video:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "Lỗi khi lấy thông tin video"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Thử lệnh <code>/clean</code> và thử lại. Nếu lỗi vẫn tiếp tục, YouTube yêu cầu xác thực. Cập nhật cookies.txt qua <code>/cookie</code> hoặc <code>/cookies_from_browser</code> và thử lại."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Menu đã đóng."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Lựa Chọn Chất Lượng Thủ Công"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Chọn chất lượng thủ công vì phát hiện tự động thất bại:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Tất Cả Định Dạng Có Sẵn"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Chất Lượng Có Sẵn (từ cache)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Sử dụng chất lượng cache - định dạng mới có thể không khả dụng"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Đang tải định dạng"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Đang tải xuống"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 Đang tải xuống với theo dõi tiến trình..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 Đang tải xuống bằng định dạng:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 Đang tải âm thanh bằng định dạng:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 Đang tải chất lượng tốt nhất..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 Đang tải xuống database dump..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 Đang tải xuống"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Trang định dạng"
    ALWAYS_ASK_FROM_CACHE_MSG = "(từ cache)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Lỗi: Không tìm thấy tin nhắn gốc. Có thể đã bị xóa. Vui lòng gửi lại liên kết."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Lỗi: Không tìm thấy URL gốc. Vui lòng gửi lại liên kết."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Liên kết trực tiếp đã được lấy</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Tiêu đề:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Thời lượng:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Định dạng:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Stream video:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Stream âm thanh:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Không thể lấy liên kết stream"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Liên kết trực tiếp đã được trích xuất qua menu Luôn Hỏi cho người dùng {user_id} từ {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Không thể trích xuất liên kết trực tiếp qua menu Luôn Hỏi cho người dùng {user_id} từ {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Liên kết trực tiếp đã được trích xuất qua down_and_up_with_format cho người dùng {user_id} từ {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Không thể trích xuất liên kết trực tiếp qua down_and_up_with_format cho người dùng {user_id} từ {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Liên kết trực tiếp đã được trích xuất qua down_and_audio cho người dùng {user_id} từ {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Không thể trích xuất liên kết trực tiếp qua down_and_audio cho người dùng {user_id} từ {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Âm thanh đã được gửi từ cache."
    AUDIO_PROCESSING_MSG = "🎙️ Âm thanh đang được xử lý..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Đang tải âm thanh:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Đã xảy ra lỗi trong quá trình tải âm thanh."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Không thể trích xuất thông tin âm thanh"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Bỏ qua loại tệp không được hỗ trợ trong danh sách phát tại chỉ mục {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "Không tìm thấy tệp âm thanh sau khi tải xuống."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ Không thể gửi âm thanh: Kích thước tệp bằng 0 B (chỉ mục danh sách phát {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ Tệp âm thanh vẫn đang được tải xuống, vui lòng đợi..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Đang tải tệp âm thanh lên...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Không thể gửi âm thanh: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Âm thanh danh sách phát đã được gửi: {sent}/{total} tệp (chất lượng={quality}) cho người dùng{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Không thể tải âm thanh: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Tải xuống đã bị hủy do hết thời gian chờ (2 giờ)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Không tìm thấy tệp video: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ Không thể gửi video: Kích thước tệp bằng 0 B (chỉ mục danh sách phát {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ Tệp video vẫn đang được tải xuống, vui lòng đợi..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ Lỗi khi xử lý video: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Lỗi khi gửi tệp mô tả: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 nếu bạn muốn thay đổi chú thích video - trả lời video bằng văn bản mới</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Không phát hiện phụ đề"
    VIDEO_PROGRESS_MSG = "<b>Video:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>Âm thanh:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ Giới hạn URL vượt quá: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "Xử lý hoàn tất"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ Phạm vi danh sách phát không được phép trong chế độ nhiều URL. Chỉ gửi URL đơn không có phạm vi (*1*5, /vid 1-10, v.v.)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "Kiểm tra <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>tại đây</a> nếu trang web của bạn được hỗ trợ"
    ERROR_COOKIE_NEEDED_MSG = "Bạn có thể cần <code>cookie</code> để tải video này. Trước tiên, dọn dẹp không gian làm việc của bạn qua lệnh <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Đối với Youtube - lấy <code>cookie</code> qua lệnh <b>/cookie</b>. Đối với bất kỳ trang web được hỗ trợ nào khác - gửi cookie của riêng bạn (<a href='https://t.me/tg_ytdlp/203'>hướng dẫn1</a>) (<a href='https://t.me/tg_ytdlp/214'>hướng dẫn2</a>) và sau đó gửi lại liên kết video của bạn."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Chọn ngôn ngữ phụ đề"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Không có ngôn ngữ âm thanh thay thế"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Chọn ngôn ngữ âm thanh"
    PAGE_NUMBER_MSG = "Trang {page}"
    TOTAL_PROGRESS_MSG = "Tiến Trình Tổng"
    SUBTITLE_MENU_CLOSED_MSG = "Menu phụ đề đã đóng."
    SUBTITLE_LANGUAGE_SET_MSG = "Ngôn ngữ phụ đề đã đặt: {value}"
    AUDIO_SET_MSG = "Âm thanh đã đặt: {value}"
    FILTERS_UPDATED_MSG = "Bộ lọc đã được cập nhật"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Quay lại"
    CLOSE_BUTTON_TEXT = "🔚Đóng"
    LIST_BUTTON_TEXT = "📃Danh sách"
    IMAGE_BUTTON_TEXT = "🖼Hình ảnh"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Chất lượng không được phát hiện tự động\nSử dụng nút 'Khác' để xem tất cả định dạng có sẵn.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Đã Phát Hiện Stream Trực Tiếp**\n\nTải xuống stream trực tiếp đang diễn ra hoặc vô hạn không được phép.\n\nVui lòng đợi stream kết thúc và thử tải lại khi:\n• Thời lượng stream đã được biết\n• Stream đã kết thúc\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>Tải Stream Trực Tiếp</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Chunk {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "Kích thước tối đa: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "Tổng thời lượng: {duration} giây"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>Stream Trực Tiếp - Chunk {chunk}</b>\n⏱ Thời lượng: {duration} giây\n📦 Kích thước: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Chunk {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>Tải Stream Trực Tiếp Hoàn Tất</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "Đã tải {chunks} chunk"
    LIVE_STREAM_TOTAL_DURATION_MSG = "Tổng thời lượng: {duration} giây"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>Tải Stream Trực Tiếp Đã Dừng</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "Thư mục người dùng đã bị xóa (có thể do lệnh /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "Tệp chunk đã bị xóa (có thể do lệnh /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ Stream đã kết thúc"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Vui lòng chọn định dạng khác bằng lệnh `/format`."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Liên kết trực tiếp đã được lấy</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Tiêu đề:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Thời lượng:</b> {duration} giây\n"
    FORMAT_FIELD_MSG = "🎛 <b>Định dạng:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Stream video:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Stream âm thanh:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Lỗi Xử Lý Tệp**\n\nVideo đã được tải xuống nhưng không thể xử lý do ký tự không hợp lệ trong tên tệp.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Lỗi Xử Lý Tệp**\n\nVideo đã được tải xuống nhưng không thể xử lý do lỗi đối số không hợp lệ.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**Lý do:**\n"
        "• Tệp đã tải xuống không phải là tệp video\n"
        "• Có thể là tài liệu (PDF, DOC, v.v.) hoặc kho lưu trữ\n\n"
        "**Giải pháp:**\n"
        "• Kiểm tra liên kết - nó có thể dẫn đến tài liệu, không phải video\n"
        "• Thử một liên kết hoặc nguồn khác\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**Lý do:**\n"
        "• Tệp không thể được xử lý dưới dạng video\n"
        "• Có thể không phải là tệp video hoặc tệp bị hỏng\n\n"
        "**Giải pháp:**\n"
        "• Kiểm tra liên kết - nó có thể dẫn đến tài liệu, không phải video\n"
        "• Thử một liên kết hoặc nguồn khác\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Định Dạng Không Khả Dụng**\n\nĐịnh dạng video được yêu cầu không khả dụng cho video này.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Không tìm thấy ID định dạng {format_id} cho video này.\n\nID định dạng có sẵn: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **Định dạng AV1 không khả dụng cho video này.**\n\n**Định dạng có sẵn:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Lỗi Xử Lý Tệp**\n\nÂm thanh đã được tải xuống nhưng không thể xử lý do ký tự không hợp lệ trong tên tệp.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Lỗi Xử Lý Tệp**\n\nÂm thanh đã được tải xuống nhưng không thể xử lý do lỗi đối số không hợp lệ.\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Người dùng đã nhập nội dung bị cấm. Không thể tải xuống."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "Làm mờ NSFW đã đặt qua lệnh: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Người dùng đã mở menu /nsfw."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: đã đóng."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Không thể tải cookie {service}: status={status} (url ẩn)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Lỗi khi tải cookie {service}: {error} (url ẩn)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Lỗi không mong đợi khi tải cookie {service} (url ẩn): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Tệp cookie đã được cập nhật cho người dùng {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Nội dung cookie không hợp lệ được cung cấp bởi người dùng {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "URL cookie YouTube trống cho người dùng {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "Cookie YouTube đã được tải xuống và xác thực cho người dùng {user_id} từ nguồn {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "Tất cả nguồn cookie YouTube thất bại cho người dùng {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Lỗi trong lệnh check_porn bởi admin {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Kích thước phần chia đã đặt thành {size} byte."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Tải video lên hoàn tất với chia tệp."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Video danh sách phát đã được gửi: {sent}/{total} tệp (chất lượng={quality}) cho người dùng {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Lỗi không xác định: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Bỏ qua loại tệp không được hỗ trợ trong danh sách phát tại chỉ mục {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ Không tìm thấy FFmpeg. Vui lòng cài đặt FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Chuyển đổi sang MP4 thất bại: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Nhúng phụ đề có thể mất nhiều thời gian (lên đến 1 phút cho mỗi 1 phút video)!\n🔥 Bắt đầu đốt phụ đề..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Phụ đề không thể nhúng do giới hạn (chất lượng/thời lượng/kích thước)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Phụ đề không khả dụng cho ngôn ngữ đã chọn"
    ERROR_SENDING_VIDEO_MSG = "❌ Lỗi khi gửi video: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Video danh sách phát đã được gửi: {sent}/{total} tệp."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Tải xuống đã bị hủy do hết thời gian chờ (2 giờ)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Không thể tải video: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Lỗi: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON phải là một đối tượng (từ điển)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Định dạng JSON không hợp lệ. Vui lòng cung cấp JSON hợp lệ."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Giá trị phải nằm giữa {min_val} và {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} đã đặt thành: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Đúng"
    ARGS_FALSE_BUTTON_MSG = "❌ Sai"
    ARGS_BACK_BUTTON_MSG = "🔙 Quay lại"
    ARGS_CLOSE_BUTTON_MSG = "🔚 Đóng"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Đúng"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Sai"
    ARGS_NOT_SET_MSG = "Chưa đặt"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ Định dạng AV1 không khả dụng cho video này.\n\nĐịnh dạng có sẵn:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Lỗi khi tải xuống: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ Không tìm thấy video trong danh sách phát tại chỉ mục {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Chuyển Đổi Video Thất Bại**\n\nVideo không thể chuyển đổi sang MP4 do lỗi đối số không hợp lệ.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Chuyển Đổi Video Thất Bại**\n\nVideo không thể chuyển đổi sang MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Không thể lấy liên kết stream"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Lỗi khi lấy liên kết:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ Không tìm thấy nội dung tại chỉ mục {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Lỗi: Không tìm thấy tin nhắn gốc."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Lỗi: Không tìm thấy URL."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ URL này không thể nhúng."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ Codec {codec} không khả dụng cho video này"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ Định dạng {format} không khả dụng cho video này"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Giới hạn flood. Thử lại sau."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Kiểm Tra Cookie"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ TẤT CẢ (TỰ ĐỘNG)"
    PROXY_OFF_BUTTON_MSG = "❌ TẮT"
    PROXY_CLOSE_BUTTON_MSG = "🔚Đóng"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 Chọn quốc gia:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ Lựa chọn quốc gia rõ ràng"
    PROXY_COUNTRY_SELECTED_MSG = "✅ Quốc gia được chọn: {country} (code: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 Proxy hiện có: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 Bot sẽ thử HTTP trước, sau đó là SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 Proxy được bật tự động cho quốc gia đã chọn"
    PROXY_COUNTRY_CLEARED_MSG = "✅ Đã xóa lựa chọn quốc gia"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ Đã xóa lựa chọn quốc gia"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ Quốc gia được chọn: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 Sử dụng quốc gia từ tệp: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 Các quốc gia có sẵn trong tệp: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 Quốc gia được chọn: {country} (code: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ Đã bật proxy cho quốc gia này"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ Proxy bị vô hiệu hóa (nhấn TẤT CẢ (AUTO) để bật)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ BẬT"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ TẮT"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Đóng"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV: BẬT"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV: TẮT"
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ BẬT (Không Làm Mờ)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ BẬT (Không Làm Mờ)"
    NSFW_OFF_BLUR_MSG = "✅ TẮT (Làm Mờ)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ TẮT (Làm Mờ)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Sạch"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Lỗi khi xử lý tin nhắn trả lời cho người dùng {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Lỗi khi gửi broadcast cho người dùng {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Log của {bot_name}\nNgười dùng: {user_id}\nTổng log: {total}\nThời gian hiện tại: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nTổng {path}: {count}\nThời gian hiện tại: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Tổng Người Dùng: {count}</i>\n20 {path} cuối:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Cache porn đã được tải lại bởi admin {admin_id}. Domain: {domains}, Từ khóa: {keywords}, Trang web: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Lỗi khi gửi tin nhắn hết thời gian chờ: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Chọn ngôn ngữ</b>"
    LANG_CHANGED_MSG = "✅ Đã thay đổi ngôn ngữ sang {lang_name}"
    LANG_ERROR_MSG = "❌ Lỗi khi thay đổi ngôn ngữ"
    LANG_CLOSED_MSG = "Đã đóng lựa chọn ngôn ngữ"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] callback: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Đang thêm nút theo dõi trình duyệt với URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "URL theo dõi trình duyệt chưa được cấu hình: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Cài đặt bàn phím đã được cập nhật!**\n\nCài đặt mới: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Không thể ẩn bàn phím: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Sử dụng cookie YouTube đang hoạt động để trích xuất liên kết cho người dùng {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "Không có cookie YouTube đang hoạt động để trích xuất liên kết cho người dùng {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Sử dụng cookie YouTube hiện có để trích xuất liên kết cho người dùng {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "Không tìm thấy cookie YouTube để trích xuất liên kết cho người dùng {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Đã sao chép tệp cookie toàn cục vào thư mục người dùng {user_id} để trích xuất liên kết"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] Người dùng {user_id} đã yêu cầu lệnh mediainfo"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] Người dùng {user_id} là admin: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] Người dùng {user_id} đang ở trong kênh: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] Người dùng {user_id} bị từ chối truy cập - không phải admin và không ở trong kênh"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] Người dùng {user_id} được cấp quyền truy cập"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ Lệnh này chỉ dành cho quản trị viên."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Tải xuống hoàn tất với hỗ trợ token PO"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Giới hạn flood. Thử lại sau."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ Lỗi làm mới token REST: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Lỗi khi đóng session Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Lỗi khi khởi tạo cấu trúc db cơ sở: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Không phải tất cả tham số đều được đặt trong config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL chưa được đặt"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey chưa được đặt để lấy idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Lỗi khi tải xuống Firebase dump: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Không thể tải xuống Firebase dump qua REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Lỗi trong _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Lỗi khi chạy tự động reload_cache (lần thử {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ Tất cả các lần thử lại đều thất bại"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Đang bắt đầu tải xuống Firebase dump lúc {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Phụ thuộc không khả dụng: requests hoặc Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ Database trống"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Lỗi khi đóng logger: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Lỗi trong quá trình dọn dẹp: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Lỗi clone: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Clone hết thời gian chờ"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Ngoại lệ clone: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Cập nhật đã bị hủy bởi người dùng"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Repository đã được clone thành công"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Backup đã được di chuyển đến _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ Tất cả module đã được tải"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Dọn dẹp hoàn tất khi thoát"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Đã nhận tín hiệu {signal}, đang tắt một cách nhẹ nhàng..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Vui lòng đợi..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Đang tải stream HLS:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "đang chờ fragment"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Không tìm thấy backup {ts} trong _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Không thể khôi phục {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Đã khôi phục: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Chi tiết:</b> {error_details}\n\nTải xuống đã dừng do lỗi nghiêm trọng.\n\n💡 <b>Mẹo:</b> Nếu bạn gặp lỗi 401 Unauthorized, thử sử dụng lệnh <code>/cookie instagram</code> hoặc gửi cookie của riêng bạn để xác thực với Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domain trong danh sách đen porn: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Đã tìm thấy từ khóa porn: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domain trong danh sách trắng: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Đã tìm thấy từ khóa danh sách trắng: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Không tìm thấy từ khóa porn"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Lỗi API TikTok tại chỉ mục {index}, bỏ qua đến âm thanh tiếp theo..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ Lỗi API TikTok tại chỉ mục {index}, bỏ qua đến video tiếp theo..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "Người dùng đã nhập <b>url</b>\n <b>tên người dùng:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>Người dùng đã nhập như sau:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Tham Gia Kênh"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Đang đăng ký handler: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Tải 5 cookie của tôi"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Lấy cookie YT từ trình duyệt"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Xác thực tệp cookie của bạn"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Tải lên cookie tùy chỉnh"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Đóng"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Định dạng có sẵn cho: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Đóng"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Đóng"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Đóng"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Đóng"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Trợ giúp đã đóng."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Đã đóng"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Đã xảy ra lỗi"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "Không tìm thấy ffmpeg trong PATH hoặc thư mục dự án. Vui lòng cài đặt FFmpeg."
    YTDLP_NOT_FOUND_MSG = "Không tìm thấy binary yt-dlp trong PATH hoặc thư mục dự án. Vui lòng cài đặt yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Video sẽ được chia thành {rounds} phần, có thể quá nhiều"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Đang chia phần video {current}/{total}: {start_time:.2f}s đến {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Không thể tạo phần chia {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Đã tạo thành công phần chia {part}: {target_name} ({size} byte)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Lỗi khi chia phần video {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Video đã được chia thành {count} phần thành công"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Lỗi trong quá trình chia video: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Lỗi khi xử lý video {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Tệp video không tồn tại: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Lỗi khi phân tích kích thước '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Không thể xác định kích thước video từ '{size_result}', sử dụng mặc định: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Lỗi khi tạo thumbnail: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Lỗi khi phân tích thời lượng video: {error}, kết quả là: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Thumbnail không được tạo tại {thumb_dir}, sử dụng mặc định"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Lỗi thực thi lệnh: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Lỗi khi tạo thumbnail với FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Bỏ qua phần cấu hình không phải dict: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Đang đặt {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Đang sử dụng cookie người dùng: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Đang sử dụng cookie YouTube cho người dùng {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Đã sao chép tệp cookie toàn cục vào thư mục người dùng {user_id}"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Đang sử dụng cookie toàn cục đã sao chép làm cookie người dùng: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Không thể sao chép tệp cookie toàn cục cho người dùng {user_id}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Đang sử dụng --no-cookies cho domain: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy được yêu cầu nhưng không thể import/lấy config: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Bắt buộc sử dụng proxy cho gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy được yêu cầu nhưng cấu hình proxy không đầy đủ"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Proxy helper thất bại: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Đang phân tích mục extractor..."
    GALLERY_DL_ITEM_COUNT_MSG = "Mục {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Đã tìm thấy metadata (tag 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "Đã tìm thấy URL (tag 3): {url}, metadata: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Đã tìm thấy metadata (legacy): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "Đã tìm thấy URL (legacy): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Đã tìm thấy tên tệp: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Đã tìm thấy thư mục: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Đã tìm thấy phần mở rộng: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Đã phân tích {count} mục, info: {info}, fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Đang đặt cấu hình gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Đang thử Chiến lược A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "Không tìm thấy module gallery_dl.extractor"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() không khả dụng trong bản build này"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Đang gọi extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Không có extractor khớp với URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Đang đặt cookie trên extractor: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Không thể đặt cookie trên extractor: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Đã tìm thấy extractor, đang gọi items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Chiến lược A thành công, đã lấy info: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Chiến lược A: extractor.items() không trả về info hợp lệ"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Chiến lược A (extractor.find) thất bại: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Metadata fallback từ --get-urls: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Tất cả chiến lược đều thất bại khi lấy metadata"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Không thể trích xuất thông tin hình ảnh: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "Không tìm thấy module gallery_dl.job (cài đặt bị hỏng?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob không khả dụng trong bản build này"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Đang tìm tệp đã tải xuống trong thư mục gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Đang thử tìm tệp theo tên từ extractor"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Lỗi khi đọc args người dùng cho {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Lỗi khi xử lý video{video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "Người dùng {user_id} đã bật send_as_file, đang gửi dưới dạng tài liệu"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video hết thời gian chờ nhiều lần; chuyển sang send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Chú thích quá dài, đang thử với chú thích tối thiểu"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (chú thích tối thiểu) hết thời gian chờ; chuyển sang send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Lỗi khi gửi video với chú thích tối thiểu: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Lỗi khi gửi tệp mô tả đầy đủ: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Lỗi khi xóa tệp mô tả tạm thời: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Bỏ qua match_filter cho domain trong NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Đang kiểm tra cookie YouTube hiện có trên URL người dùng để phát hiện định dạng cho người dùng {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Cookie YouTube hiện có hoạt động trên URL người dùng để phát hiện định dạng cho người dùng {user_id} - đang sử dụng chúng"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Cookie YouTube hiện có thất bại trên URL người dùng, đang thử lấy cookie mới để phát hiện định dạng cho người dùng {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Đang thử nguồn cookie YouTube {i} để phát hiện định dạng cho người dùng {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "Cookie YouTube từ nguồn {i} hoạt động trên URL người dùng để phát hiện định dạng cho người dùng {user_id} - đã lưu vào thư mục người dùng"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "Cookie YouTube từ nguồn {i} không hoạt động trên URL người dùng để phát hiện định dạng cho người dùng {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Không thể tải cookie YouTube từ nguồn {i} để phát hiện định dạng cho người dùng {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Tất cả nguồn cookie YouTube thất bại để phát hiện định dạng cho người dùng {user_id}, sẽ thử không có cookie"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Không có nguồn cookie YouTube được cấu hình để phát hiện định dạng cho người dùng {user_id}, sẽ thử không có cookie"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Không tìm thấy cookie YouTube để phát hiện định dạng cho người dùng {user_id}, đang cố lấy cookie mới"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Đang sử dụng cookie YouTube để phát hiện định dạng cho người dùng {user_id} (đã được xác thực trong menu Luôn Hỏi)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Không tìm thấy cookie YouTube để phát hiện định dạng cho người dùng {user_id}, đang cố khôi phục..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Đã sao chép tệp cookie toàn cục vào thư mục người dùng {user_id} để phát hiện định dạng"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Không thể sao chép tệp cookie toàn cục cho người dùng {user_id}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Đang sử dụng --no-cookies cho domain trong get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "Ứng dụng chưa được khởi tạo. Không thể truy cập {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Chú thích:</b> <code>{caption}</code>\n<b>ID người dùng:</b> <code>{user_id}</code>\n<b>Tên người dùng:</b> <code>{users_name}</code>\n<b>ID tệp video:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Lỗi trong caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Lỗi không mong đợi trong caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL Video</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL thiếu trong cấu hình"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin đã được khởi tạo"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken đã được làm mới"
    DB_LOG_FOR_USER_ADDED_MSG = "Log cho người dùng đã được thêm"
    DB_DATABASE_CREATED_MSG = "db đã được tạo"
    DB_BOT_STARTED_MSG = "Bot đã được khởi động"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY đã được lưu vào config.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Phần danh sách phát đã được cache: {path_parts}, bỏ qua"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: không tìm thấy cache cho bất kỳ biến thể URL/chất lượng nào, trả về dict trống"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: đếm nhanh cho phạm vi lớn: {cached_count} video đã cache"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: không tìm thấy cache cho hash {url_hash}, chất lượng {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: không tìm thấy cache cho bất kỳ biến thể URL nào, trả về None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Truy cập bị từ chối. Chỉ dành cho admin."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Tự động tải lại Firebase cache đã được cập nhật!\n\n📊 Trạng thái: {status}\n⏰ Lịch trình: mỗi {interval} giờ từ 00:00\n🕒 Lần tải lại tiếp theo: {next_exec} (trong {delta_min} phút)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Tự động tải lại Firebase cache đã dừng!\n\n📊 Trạng thái: ❌ TẮT\n💡 Sử dụng /auto_cache on để bật lại"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Đối số không hợp lệ. Sử dụng /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Khoảng thời gian phải nằm giữa 1 và 168 giờ"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Không thể đặt khoảng thời gian"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Khoảng thời gian tự động Firebase cache đã được cập nhật!\n\n📊 Trạng thái: ✅ BẬT\n⏰ Lịch trình: mỗi {interval} giờ từ 00:00\n🕒 Lần tải lại tiếp theo: {next_exec} (trong {delta_min} phút)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Tự động tải lại Firebase cache đã bắt đầu!\n\n📊 Trạng thái: ✅ BẬT\n⏰ Lịch trình: mỗi {interval} giờ từ 00:00\n🕒 Lần tải lại tiếp theo: {next_exec} (trong {delta_min} phút)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Tự động tải lại Firebase cache đã dừng!\n\n📊 Trạng thái: ❌ TẮT\n💡 Sử dụng /auto_cache on để bật lại"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Tự động tải lại ĐÃ BẬT; lần tiếp theo lúc {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Tự động tải lại ĐÃ TẮT bởi admin."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Khoảng thời gian tự động tải lại đã đặt thành {interval}h; lần tiếp theo lúc {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Tự động tải lại đã bắt đầu; lần tiếp theo lúc {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Tự động tải lại đã dừng bởi admin."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase cache đã được tải: {count} nút gốc"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Không tìm thấy tệp cache Firebase, bắt đầu với cache trống: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Không thể tải cache Firebase: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase cache đã được tải lại: {count} nút gốc"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Không tìm thấy tệp cache Firebase: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Không thể tải lại cache Firebase: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 Bạn đã bị cấm sử dụng bot! Để được gỡ cấm, liên hệ với {Config.ADMIN_USERNAME}\n<blockquote>P.S. Đừng rời khỏi kênh - bạn sẽ bị cấm tự động ⛔️</blockquote>\n🌍Thay đổi ngôn ngữ /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Không tìm thấy định dạng video. Đang thử trình tải hình ảnh…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram đã giới hạn gửi tin nhắn.\n⏳ Vui lòng đợi: {time_str}\nĐể cập nhật bộ đếm thời gian, gửi lại URL 2 lần."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Nhấn nút để sao chép URL stream, sau đó dán vào ứng dụng VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Nhấn nút để sao chép URL stream, sau đó dán vào ứng dụng VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Lỗi khi lấy liên kết:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Lỗi khi gửi tệp định dạng: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Không thể lấy định dạng:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 Đang phân tích... (đợi 6 giây)"
    AA_PROCESSING_MSG = "🔎 Đang phân tích..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Thẻ #{wrong} chứa các ký tự bị cấm. Chỉ cho phép chữ cái, chữ số và _.\nVui lòng sử dụng: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Để bot hoạt động trong nhóm, bot cần quyền quản trị viên. Vui lòng đặt bot làm quản trị viên của nhóm này."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "Xin chào {first_name},\n \n<i>Bot này🤖 có thể tải bất kỳ video nào vào telegram trực tiếp.😊 Để biết thêm thông tin, nhấn <b>/help</b></i> 👈\n\n<blockquote>P.S. Tải xuống nội dung 🔞NSFW và tệp từ ☁️Cloud Storage là có phí! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ Đừng rời khỏi kênh - bạn sẽ bị cấm sử dụng bot ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Không có tệp để xóa."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 Tất cả tệp đã được xóa thành công!\n\nTệp đã xóa:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ ĐỢI CHO ĐẾN KHI TẢI XUỐNG TRƯỚC ĐÓ CỦA BẠN HOÀN TẤT"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "App instance là None trong check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict là None, cho phép tải xuống"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict là None, cho phép nhúng phụ đề"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: đang kiểm tra giới hạn - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: khóa info_dict: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Nhúng phụ đề đã bỏ qua: thời lượng {duration}s vượt quá giới hạn {max_duration}s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Nhúng phụ đề đã bỏ qua: kích thước {size_mb:.2f}MB vượt quá giới hạn {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Nhúng phụ đề đã bỏ qua: chất lượng {width}x{height} (cạnh tối thiểu {min_side}p) vượt quá giới hạn {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "danh sách phát"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Giới hạn phạm vi vượt quá cho {service}: {count} (tối đa {max_count}).\n\nSử dụng một trong các lệnh sau để tải xuống tối đa các tệp có sẵn:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Giới hạn phạm vi vượt quá cho {service}: {count} (tối đa {max_count})\nID Người dùng: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "Nhà cung cấp token PO đã tắt trong config"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} không phải domain YouTube, bỏ qua token PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "Nhà cung cấp token PO không khả dụng tại {base_url}, chuyển sang trích xuất YouTube tiêu chuẩn"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "Cache nhà cung cấp token PO đã được xóa, sẽ kiểm tra khả dụng vào lần yêu cầu tiếp theo"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "App instance chưa khả dụng"
    HELPER_USER_NAME_MSG = "Người dùng"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Đã phát hiện flood wait, đang chờ {wait_seconds} giây"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Đã phát hiện flood wait nhưng không thể trích xuất thời gian, đang chờ {retry_delay} giây"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "Đã phát hiện lỗi msg_seqno, đang chờ {retry_delay} giây"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Cấu hình proxy không đầy đủ, sử dụng kết nối trực tiếp"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Đóng"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Đóng"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Đóng"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Tệp log đã được xóa."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Tệp thẻ đã được xóa."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Tệp định dạng đã được xóa."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Tệp chia đã được xóa."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Tệp mediainfo đã được xóa."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Cài đặt phụ đề đã được xóa."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Cài đặt bàn phím đã được xóa."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Cài đặt args đã được xóa."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 Cài đặt NSFW đã được xóa."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Cài đặt proxy đã được xóa."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Cài đặt flood wait đã được xóa."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Đóng"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Lệnh Tải Video"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Sử dụng: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Ví dụ:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (thứ tự trực tiếp)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (thứ tự ngược)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Xem thêm: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "Người dùng {user_id} đã đóng lệnh add_bot_to_group"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Không thể trích xuất ID YouTube"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Không thể tải thumbnail hoặc nó quá lớn"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Chọn ngôn ngữ âm thanh"
    AA_NO_SUBTITLES_DETECTED_MSG = "Không phát hiện phụ đề"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Chọn ngôn ngữ phụ đề"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Lỗi Xác Thực"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Không Tìm Thấy Tài Khoản"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Tài Khoản Không Khả Dụng"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Vượt Quá Giới Hạn Tỷ Lệ"
    GALLERY_DL_NETWORK_ERROR_MSG = "Lỗi Mạng"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Nội Dung Không Khả Dụng"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Hạn Chế Địa Lý"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Yêu Cầu Xác Minh"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Vi Phạm Chính Sách"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Lỗi Không Xác Định"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Tải xuống đã bắt đầu</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Đóng"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Lệnh Tải Video</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Sử dụng: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Ví dụ:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Xem thêm: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Giới hạn flood. Thử lại sau."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Cách Sử Dụng Lệnh Cookie</b>

<code>/cookie</code> - Hiển thị menu cookie
<code>/cookie youtube</code> - Tải cookie YouTube
<code>/cookie instagram</code> - Tải cookie Instagram
<code>/cookie tiktok</code> - Tải cookie TikTok
<code>/cookie x</code> hoặc <code>/cookie twitter</code> - Tải cookie Twitter/X
<code>/cookie facebook</code> - Tải cookie Facebook
<code>/cookie custom</code> - Hiển thị hướng dẫn cookie tùy chỉnh

<i>Các dịch vụ có sẵn phụ thuộc vào cấu hình bot.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Tệp cookie đã được xóa và cache đã được xóa."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Trước"
    SUBS_BACK_BUTTON_MSG = "🔙Quay lại"
    SUBS_OFF_BUTTON_MSG = "🚫 TẮT"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - đặt ngôn ngữ"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - đặt ngôn ngữ với AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Tùy chọn hợp lệ:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 NGÔN NGỮ"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 DỌN DẸP"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIE"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 PHƯƠNG TIỆN"
    SETTINGS_INFO_BUTTON_MSG = "📖 THÔNG TIN"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ THÊM"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Chỉ Cookie"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Log "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Thẻ"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Định Dạng"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Chia"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Phụ Đề"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Bàn Phím"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Args"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Proxy"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Flood wait"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Tất cả tệp"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Tải 5 cookie của tôi"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Lấy cookie YT từ trình duyệt"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Xác thực tệp cookie của bạn"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Tải lên cookie tùy chỉnh"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - Thay đổi chất lượng & định dạng"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Bật / Tắt MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Thay đổi kích thước phần video chia"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - Tải video dưới dạng âm thanh"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Cài đặt ngôn ngữ phụ đề"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - Cách tải danh sách phát"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Tải hình ảnh qua gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Gửi #thẻ của bạn"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - Lấy hướng dẫn"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - Gửi log của bạn"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Trợ giúp danh sách phát"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - hướng dẫn"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - Lấy liên kết video trực tiếp"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Bật/tắt proxy"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Bố cục bàn phím"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Trợ giúp tìm kiếm nội tuyến"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - đối số yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - Cài đặt làm mờ NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Tùy Chọn Dọn Dẹp</b>\n\nChọn những gì cần dọn dẹp:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Di động: Kích hoạt tìm kiếm @vid"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Di động: Kích hoạt tìm kiếm @vid"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 TẮT"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 ĐẦY ĐỦ"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL Hình ảnh]({url})"
    IMAGE_ERROR_MSG = "❌ Lỗi: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Quay lại"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - định dạng tùy chỉnh"
    FORMAT_720P_MSG = "• <code>/format 720</code> - chất lượng 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - chất lượng 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - chất lượng 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - ID định dạng cụ thể"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - luôn hiển thị menu"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/chất lượng tốt nhất"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Luôn Hỏi (menu + nút)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Khác (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (tốt nhất cho PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (tốt nhất cho Telegram di động)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (chất lượng TỐI ĐA)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Tùy chỉnh (nhập của riêng bạn)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 Từ Trình Duyệt"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Của Riêng Bạn"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Chế độ nhập tự động đóng do không hoạt động (5 phút)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Đặt Lại Tất Cả"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Xem Hiện Tại"
    ARGS_BACK_BUTTON_MSG = "🔙 Quay lại"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Chuyển tiếp tin nhắn này đến mục yêu thích của bạn để lưu các cài đặt này dưới dạng mẫu.</i> \n\n<i>Chuyển tiếp tin nhắn này trở lại đây để áp dụng các cài đặt này.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Đối Số yt-dlp Hiện Tại:\n\nKhông có cài đặt tùy chỉnh được cấu hình.\n\n---\n\n<i>Chuyển tiếp tin nhắn này đến mục yêu thích của bạn để lưu các cài đặt này dưới dạng mẫu.</i> \n\n<i>Chuyển tiếp tin nhắn này trở lại đây để áp dụng các cài đặt này.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Đối Số yt-dlp Hiện Tại:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Xuất Cài Đặt"
    ARGS_SETTINGS_READY_MSG = "Cài đặt sẵn sàng để xuất! Chuyển tiếp tin nhắn này đến mục yêu thích để lưu."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Đối Số yt-dlp Hiện Tại:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Không thể nhận dạng cài đặt trong tin nhắn. Đảm bảo bạn đã gửi mẫu cài đặt đúng."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Cài đặt đã được nhập thành công!\n\nTham số đã áp dụng: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Cài đặt chính:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Lỗi khi lưu cài đặt đã nhập."
    ARGS_ERROR_IMPORTING_MSG = "❌ Đã xảy ra lỗi khi nhập cài đặt."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Tải Tệp Cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Chọn một dịch vụ để tải tệp cookie."
    COOKIE_MENU_SAVE_INFO_MSG = "Tệp cookie sẽ được lưu dưới dạng cookie.txt trong thư mục của bạn."
    COOKIE_MENU_TIP_HEADER_MSG = "Mẹo: Bạn cũng có thể sử dụng lệnh trực tiếp:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – tải và xác thực cookie"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – sử dụng nguồn cụ thể theo chỉ mục (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "Sau đó xác minh bằng <code>/check_cookie</code> (kiểm tra trên RickRoll)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "Luôn Hỏi"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗Liên kết"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Watch"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝Chú thích"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ CẮT"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>Cắt Video</b>\n\nThời lượng video: <b>{start_time} - {end_time}</b>\n\nVui lòng gửi phạm vi thời gian mong muốn theo định dạng:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nVí dụ: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ Định dạng không hợp lệ. Vui lòng sử dụng: <code>HH:MM:SS-HH:MM:SS</code>\n\nVí dụ: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ Phạm vi không hợp lệ. Thời gian bắt đầu phải nhỏ hơn thời gian kết thúc."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ Phạm vi thời gian nằm ngoài giới hạn của video.\n\nThời lượng video: <b>{start_time} - {end_time}</b>\n\nPhạm vi của bạn phải nằm trong các giới hạn này."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>Video sẽ được cắt:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ Hoàn thành một phần - {successful_uploads}/{total_files} tệp âm thanh đã được tải lên."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ Âm thanh đã được tải xuống và gửi thành công - {total_files} tệp đã được tải lên."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Tài Khoản TikTok Riêng Tư</b>\n\n"
        "Tài khoản TikTok này là riêng tư hoặc tất cả video đều riêng tư.\n\n"
        "<b>💡 Giải Pháp:</b>\n"
        "1. Theo dõi tài khoản @{username}\n"
        "2. Gửi cookie của bạn cho bot bằng lệnh <code>/cookie</code>\n"
        "3. Thử lại\n\n"
        "<b>Sau khi cập nhật cookie, thử lại!</b>"
    )

    #######################################################
