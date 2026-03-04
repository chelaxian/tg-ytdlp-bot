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
    CREDITS_MSG = "<blockquote><i>จัดการโดย</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 เปลี่ยนภาษา: /lang</b>"
    TO_USE_MSG = "<i>เพื่อใช้บอทนี้คุณต้องสมัครสมาชิกช่อง Telegram @tg_ytdlp</i>\nหลังจากเข้าร่วมช่องแล้ว <b>ส่งลิงก์วิดีโอของคุณอีกครั้งและบอทจะดาวน์โหลดให้คุณ</b> ❤️\n\n<blockquote>P.S. เนื่องจากเนื้อหา 🔞NSFW ที่อาจเกิดขึ้น - การดาวน์โหลดจาก ☁️<b>คลาวด์สตอเรจ</b> 📁<b>แชร์ไฟล์</b> 🔗<b>ตัวย่อ URL</b> และ 🔞<b>เว็บโป๊</b> เป็นแบบเสียเงิน! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ อย่า 🗑<b>ลบ/ยกเลิกสมัครช่อง @tg_ytdlp</b> และอย่า 🤖<b>สแปม URL/คำสั่งกับบอทมากเกินไป</b> - คุณจะถูกแบนจากการใช้บอทโดยอัตโนมัติ ⛔️</blockquote>"

    ERROR1 = "ไม่พบลิงก์ URL กรุณาใส่ URL ที่มี <b>https://</b> หรือ <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>เพลย์ลิสต์ (yt-dlp)</b>

ในการดาวน์โหลดเพลย์ลิสต์ ส่ง URL พร้อมช่วง <code>*start*end</code> ที่ท้าย ตัวอย่าง: <code>URL*1*5</code> (วิดีโอ 5 รายการแรกตั้งแต่ 1 ถึง 5 รวม).<code>URL*-1*-5</code> (วิดีโอ 5 รายการสุดท้ายตั้งแต่ 1 ถึง 5 รวม).
หรือคุณสามารถใช้ <code>/vid จาก-ถึง URL</code> ตัวอย่าง: <code>/vid 3-7 URL</code> (ดาวน์โหลดวิดีโอตั้งแต่ 3 ถึง 7 รวมตั้งแต่ต้น). <code>/vid -3-7 URL</code> (ดาวน์โหลดวิดีโอตั้งแต่ 3 ถึง 7 รวมตั้งแต่ท้าย). ใช้งานได้กับคำสั่ง <code>/audio</code> ด้วย

<b>ตัวอย่าง:</b>

🟥 <b>ช่วงวิดีโอจากเพลย์ลิสต์ YouTube:</b> (ต้องใช้ 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(ดาวน์โหลดวิดีโอ 5 รายการแรกตั้งแต่ 1 ถึง 5 รวม)
🟥 <b>วิดีโอเดียวจากเพลย์ลิสต์ YouTube:</b> (ต้องใช้ 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(ดาวน์โหลดเฉพาะวิดีโอที่ 3)

⬛️ <b>โปรไฟล์ TikTok:</b> (ต้องใช้ 🍪 ของคุณ)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(ดาวน์โหลดวิดีโอ 10 รายการแรกจากโปรไฟล์ผู้ใช้)

🟪 <b>สตอรี่ Instagram:</b> (ต้องใช้ 🍪 ของคุณ)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(ดาวน์โหลดสตอรี่ 3 รายการแรก)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(ดาวน์โหลดสตอรี่ 10 รายการแรกจากอัลบั้ม)

🟦 <b>วิดีโอ VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(ดาวน์โหลดวิดีโอ 3 รายการแรกจากโปรไฟล์ผู้ใช้/กลุ่ม)

⬛️<b>ช่อง Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(ดาวน์โหลดวิดีโอตั้งแต่ 2 ถึง 4 รวมจากช่อง)

🟪 <b>คลิป Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(ดาวน์โหลดคลิป 3 รายการแรกจากช่อง)

🟦 <b>กลุ่ม Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(ดาวน์โหลดวิดีโอ 2 รายการแรกจากกลุ่ม)

🟧 <b>โมเดล Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(ดาวน์โหลดวิดีโอ 2 รายการแรกจากโปรไฟล์โมเดล)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(ดาวน์โหลดวิดีโอ 3 รายการแรกจากผลการค้นหาตามคำขอของคุณ)

และอื่นๆ...
ดู <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">รายชื่อเว็บไซต์ที่รองรับ</a>
</blockquote>

<blockquote expandable>🖼 <b>รูปภาพ (gallery-dl)</b>

ใช้ <code>/img URL</code> เพื่อดาวน์โหลดรูปภาพ/ภาพถ่าย/อัลบั้มจากหลายแพลตฟอร์ม

<b>ตัวอย่าง:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>ช่วง:</b>
<code>/img 11-20 https://example.com/album</code> — รายการ 11..20
<code>/img 11- https://example.com/album</code> — จาก 11 ถึงท้าย (หรือขีดจำกัดของบอท)

<i>แพลตฟอร์มที่รองรับรวมถึง vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor ฯลฯ รายการเต็ม:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">เว็บไซต์ที่ gallery-dl รองรับ</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>บอทดาวน์โหลดวิดีโอ - คำแนะนำ</b>

📥 <b>การใช้งานพื้นฐาน:</b>
• ส่งลิงก์ใดๆ → บอทจะดาวน์โหลด
  <i>บอทจะพยายามดาวน์โหลดวิดีโอผ่าน yt-dlp และรูปภาพผ่าน gallery-dl โดยอัตโนมัติ</i>
• <b>หลาย URL:</b> ในโหมดเลือกคุณภาพ (<code>/format</code>) คุณสามารถส่งได้ถึง <b>10 URL</b> ในข้อความเดียว แต่ละ URL ในบรรทัดใหม่หรือคั่นด้วยช่องว่าง
• <code>/audio URL</code> → แยกเสียง
• <code>/link [quality] URL</code> → รับลิงก์โดยตรง
• <code>/proxy</code> → เปิด/ปิดพร็อกซี่สำหรับการดาวน์โหลดทั้งหมด
• ตอบกลับวิดีโอด้วยข้อความ → เปลี่ยนคำบรรยาย

📋 <b>เพลย์ลิสต์และช่วง:</b>
• <code>URL*1*5</code> → ดาวน์โหลดวิดีโอ 5 รายการแรก
• <code>URL*-1*-5</code> → ดาวน์โหลดวิดีโอ 5 รายการสุดท้าย
• <code>/vid 3-7 URL</code> → กลายเป็น <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → กลายเป็น <code>URL*-3*-7</code>

🍪 <b>คุกกี้และส่วนตัว:</b>
• อัปโหลด *.txt cookie สำหรับวิดีโอส่วนตัว
• <code>/cookie [service]</code> → ดาวน์โหลดคุกกี้ (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → เลือกแหล่งที่มาตามดัชนี (1–N)
• <code>/cookies_from_browser</code> → แยกจากเบราว์เซอร์
• <code>/check_cookie</code> → ตรวจสอบคุกกี้
• <code>/save_as_cookie</code> → บันทึกข้อความเป็นคุกกี้

🧹 <b>การทำความสะอาด:</b>
• <code>/clean</code> → เฉพาะไฟล์สื่อ
• <code>/clean all</code> → ทุกอย่าง
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>การตั้งค่า:</b>
• <code>/settings</code> → เมนูการตั้งค่า
• <code>/format</code> → คุณภาพและรูปแบบ
• <code>/split</code> → แบ่งวิดีโอเป็นส่วนๆ
• <code>/mediainfo on/off</code> → ข้อมูลสื่อ
• <code>/nsfw on/off</code> → เบลอ NSFW
• <code>/tags</code> → ดูแท็กที่บันทึกไว้
• <code>/sub on/off</code> → คำบรรยาย
• <code>/keyboard</code> → คีย์บอร์ด (OFF/1x3/2x3)

🏷️ <b>แท็ก:</b>
• เพิ่ม <code>#tag1#tag2</code> หลัง URL
• แท็กจะปรากฏในคำบรรยาย
• <code>/tags</code> → ดูแท็กทั้งหมด

🔗 <b>ลิงก์โดยตรง:</b>
• <code>/link URL</code> → คุณภาพที่ดีที่สุด
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → คุณภาพเฉพาะ

⚙️ <b>คำสั่งด่วน:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → ตั้งคุณภาพ
• <code>/keyboard off/1x3/2x3/full</code> → เลย์เอาต์คีย์บอร์ด
• <code>/split 100mb-2000mb</code> → เปลี่ยนขนาดส่วน
• <code>/subs off/ru/en auto</code> → ภาษาคำบรรยาย
• <code>/list URL</code> → รายการรูปแบบที่มี
• <code>/mediainfo on/off</code> → เปิด/ปิดข้อมูลสื่อ
• <code>/proxy on/off</code> → เปิด/ปิดพร็อกซี่สำหรับการดาวน์โหลดทั้งหมด

📊 <b>ข้อมูล:</b>
• <code>/usage</code> → ประวัติการดาวน์โหลด
• <code>/search</code> → การค้นหาแบบอินไลน์ผ่าน @vid

🖼 <b>รูปภาพ:</b>
• <code>URL</code> → ดาวน์โหลด URL รูปภาพ
• <code>/img URL</code> → ดาวน์โหลดรูปภาพจาก URL
• <code>/img 11-20 URL</code> → ดาวน์โหลดช่วงเฉพาะ
• <code>/img 11- URL</code> → ดาวน์โหลดจากที่ 11 ถึงท้าย

👨‍💻 <i>นักพัฒนา:</i> @upekshaip
🤝 <i>ผู้มีส่วนร่วม:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "เพียงบันทึกคุกกี้ของคุณเป็น <b><u>cookie.txt</u></b> และส่งให้บอทเป็นเอกสาร\n\n"
        "คุณยังสามารถส่งคุกกี้เป็นข้อความธรรมดาด้วยคำสั่ง <b><u>/save_as_cookie</u></b>\n"
        "<b>การใช้งาน <b><u>/save_as_cookie</u></b>:</b>\n\n"
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
        "<b><u>คำแนะนำ:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message
    SEARCH_MSG = """
🔍 <b>ค้นหาวิดีโอ</b>

กดปุ่มด้านล่างเพื่อเปิดใช้งานการค้นหาแบบอินไลน์ผ่าน @vid

<blockquote>บน PC เพียงพิมพ์ <b>"@vid Your_Search_Query"</b> ในแชทใดก็ได้</blockquote>
    """
    
    # Settings and Hints
    
    
    IMG_HELP_MSG = (
        "<b>🖼 คำสั่งดาวน์โหลดรูปภาพ</b>\n\n"
        "การใช้งาน: <code>/img URL</code>\n\n"
        "<b>ตัวอย่าง:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>แพลตฟอร์มที่รองรับ (ตัวอย่าง):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor ฯลฯ — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">รายการเต็ม</a></blockquote>"
        "ดูเพิ่มเติม: "
    )
    
    LINK_HINT_MSG = (
        "รับลิงก์วิดีโอโดยตรงพร้อมการเลือกคุณภาพ\n\n"
        "การใช้งาน: /link + URL \n\n"
        "(เช่น /link https://youtu.be/abc123)\n"
        "(เช่น /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>เพิ่มบอทเข้ากลุ่ม</b>

เพิ่มบอทของฉันเข้ากลุ่มของคุณเพื่อรับฟีเจอร์ที่เพิ่มขึ้นและขีดจำกัดที่สูงขึ้น!
————————————
📊 <b>ขีดจำกัดฟรีปัจจุบัน (ใน DM ของบอท):</b>
<blockquote>•🗑 ไฟล์ที่ไม่ได้เรียงลำดับทั้งหมด 👎
• ขนาดไฟล์สูงสุด 1 ไฟล์: <b>8 GB </b>
• คุณภาพไฟล์สูงสุด 1 ไฟล์: <b>ไม่จำกัด</b>
• ระยะเวลาของไฟล์สูงสุด 1 ไฟล์: <b>ไม่จำกัด</b>
• จำนวนการดาวน์โหลดสูงสุด: <b>ไม่จำกัด</b>
• URL สูงสุดในข้อความเดียว: <b>10</b> (เฉพาะในโหมดเลือกคุณภาพ)
• รายการเพลย์ลิสต์สูงสุดต่อ 1 ครั้ง: <b>50</b>
• วิดีโอ TikTok สูงสุดต่อ 1 ครั้ง: <b>500</b>
• รูปภาพสูงสุดต่อ 1 ครั้ง: <b>1000</b>
• ขีดจำกัดอัตรา URL: <b>5/นาที, 60/ชั่วโมง, 1000/วัน</b>
• ขีดจำกัดคำสั่ง: <b>20/นาที</b>
• เวลาสูงสุด 1 การดาวน์โหลด: <b>2 ชั่วโมง</b>
• 🔞 เนื้อหา NSFW เป็นแบบเสียเงิน! 1⭐️ = $0.02
• 🆓 สื่ออื่นๆ ทั้งหมดฟรีทั้งหมด
• 📝 บันทึกเนื้อหาทั้งหมดและการแคชไปยังช่องบันทึกของฉันสำหรับการโพสต์ซ้ำทันทีเมื่อดาวน์โหลดซ้ำ</blockquote>

💬<b>ขีดจำกัดเหล่านี้สำหรับวิดีโอพร้อมคำบรรยายเท่านั้น:</b>
<blockquote>• ระยะเวลาวิดีโอ+คำบรรยายสูงสุด: <b>1.5 ชั่วโมง</b>
• ขนาดไฟล์วิดีโอ+คำบรรยายสูงสุด: <b>500 MB</b>
• คุณภาพวิดีโอ+คำบรรยายสูงสุด: <b>720p</b></blockquote>
————————————
🚀 <b>ประโยชน์ของกลุ่มแบบเสียเงิน (2️⃣x ขีดจำกัด):</b>
<blockquote>•  🗂 คลังสื่อที่เป็นระเบียบจัดเรียงตามหัวข้อ 👍
•  📁 บอทตอบกลับในหัวข้อที่คุณเรียกใช้
•  📌 ข้อความสถานะปักหมุดอัตโนมัติพร้อมความคืบหน้าการดาวน์โหลด
•  🖼 คำสั่ง /img ดาวน์โหลดสื่อเป็นอัลบั้ม 10 รายการ
• ขนาดไฟล์สูงสุด 1 ไฟล์: <b>16 GB</b> ⬆️
• URL สูงสุดในข้อความเดียว: <b>20</b> ⬆️ (เฉพาะในโหมดเลือกคุณภาพ)
• รายการเพลย์ลิสต์สูงสุดต่อ 1 ครั้ง: <b>100</b> ⬆️
• วิดีโอ TikTok สูงสุดต่อ 1 ครั้ง: 1000 ⬆️
• รูปภาพสูงสุดต่อ 1 ครั้ง: 2000 ⬆️
• ขีดจำกัดอัตรา URL: <b>10/นาที, 120/ชั่วโมง, 2000/วัน</b> ⬆️
• ขีดจำกัดคำสั่ง: <b>40/นาที</b> ⬆️
• เวลาสูงสุด 1 การดาวน์โหลด: <b>4 ชั่วโมง</b> ⬆️
• 🔞 เนื้อหา NSFW: ฟรีพร้อมเมตาดาต้าเต็ม 🆓
• 📢 ไม่ต้องสมัครสมาชิกช่องของฉันสำหรับกลุ่ม
• 👥 สมาชิกกลุ่มทั้งหมดจะเข้าถึงฟังก์ชันแบบเสียเงินได้!
• 🗒 ไม่มีบันทึก / ไม่มีแคชไปยังช่องบันทึกของฉัน! คุณสามารถปฏิเสธการคัดลอก/โพสต์ซ้ำในการตั้งค่ากลุ่ม</blockquote>

💬 <b>2️⃣x ขีดจำกัดสำหรับวิดีโอพร้อมคำบรรยาย:</b>
<blockquote>• ระยะเวลาวิดีโอ+คำบรรยายสูงสุด: <b>3 ชั่วโมง</b> ⬆️
• ขนาดไฟล์วิดีโอ+คำบรรยายสูงสุด: <b>1000 MB</b> ⬆️
• คุณภาพวิดีโอ+คำบรรยายสูงสุด: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>ราคาและการตั้งค่า:</b>
<blockquote>• ราคา: <b>$5/เดือน</b> ต่อ 1 บอทในกลุ่ม
• การตั้งค่า: ติดต่อ @iilililiiillliiliililliilliliiil
• การชำระเงิน: 💎TON หรือวิธีอื่น💲
• การสนับสนุน: การสนับสนุนทางเทคนิคเต็มรูปแบบรวมอยู่ด้วย</blockquote>
————————————
คุณสามารถเพิ่มบอทของฉันเข้ากลุ่มของคุณเพื่อปลดล็อก 🔞<b>NSFW</b> ฟรีและเพิ่มขีดจำกัดทั้งหมดเป็นสองเท่า (x2️⃣)
ติดต่อฉันหากคุณต้องการให้ฉันอนุญาตให้กลุ่มของคุณใช้บอทของฉัน @iilililiiillliiliililliilliliiil
————————————
💡<b>เคล็ดลับ:</b> <blockquote>คุณสามารถร่วมกันจ่ายเงินกับเพื่อนของคุณจำนวนเท่าใดก็ได้ (เช่น 100 คน) และทำการซื้อ 1 ครั้งสำหรับทั้งกลุ่ม - สมาชิกกลุ่มทั้งหมดจะมีการเข้าถึงแบบไม่จำกัดเต็มรูปแบบสำหรับฟังก์ชันบอททั้งหมดในกลุ่มนั้นเพียง <b>0.05$</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>โหมด NSFW: เปิด✅</b>

• เนื้อหา NSFW จะแสดงโดยไม่เบลอ
• สปอยเลอร์จะไม่ใช้กับสื่อ NSFW
• เนื้อหาจะมองเห็นได้ทันที

<i>ใช้ /nsfw off เพื่อเปิดใช้งานเบลอ</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>โหมด NSFW: ปิด</b>

⚠️ <b>เบลอเปิดใช้งาน</b>
• เนื้อหา NSFW จะถูกซ่อนไว้ใต้สปอยเลอร์   
• ในการดู คุณจะต้องคลิกที่สื่อ
• สปอยเลอร์จะใช้กับสื่อ NSFW

<i>ใช้ /nsfw on เพื่อปิดใช้งานเบลอ</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>พารามิเตอร์ไม่ถูกต้อง</b>

ใช้:
• <code>/nsfw on</code> - ปิดใช้งานเบลอ
• <code>/nsfw off</code> - เปิดใช้งานเบลอ
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>กำลังตรวจสอบแคช...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 กำลังประมวลผล..."
    DOWNLOADING_MSG = "📥 <b>กำลังดาวน์โหลดสื่อ...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>กำลังดาวน์โหลดรูปภาพ...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>ดาวน์โหลดเสร็จสมบูรณ์</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "ดาวน์โหลดแล้ว:"
    SENT_STATUS_MSG = "ส่งแล้ว:"
    PENDING_TO_SEND_STATUS_MSG = "รอการส่ง:"
    TITLE_LABEL_MSG = "ชื่อเรื่อง:"
    MEDIA_COUNT_LABEL_MSG = "จำนวนสื่อ:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "ดาวน์โหลดเสร็จแล้ว กำลังประมวลผลเสียง..."
    VIDEO_PROCESSING_MSG = "📽 วิดีโอกำลังประมวลผล..."
    WAITING_HOURGLASS_MSG = ""
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>ส่งจากแคช</b>\n\nอัลบั้มที่ส่ง: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ วิดีโอส่งจากแคชสำเร็จแล้ว"
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ วิดีโอเพลย์ลิสต์ส่งจากแคชแล้ว ({cached}/{total} ไฟล์)"
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} วิดีโอส่งจากแคชแล้ว กำลังดาวน์โหลดที่ขาดหายไป..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ ส่งจากแคช: {cached}\n🔄 ดาวน์โหลดต่อ..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 ไม่สามารถวิเคราะห์สื่อได้ ดำเนินการต่อด้วยช่วงสูงสุดที่อนุญาต (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 ไม่สามารถกำหนดจำนวนสื่อได้ ดำเนินการต่อด้วยช่วงสูงสุดที่อนุญาต (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 ไม่สามารถกำหนดจำนวนสื่อทั้งหมดได้ ดำเนินการต่อด้วยช่วงที่ระบุ {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>URL ไม่ถูกต้อง</b>\n\nกรุณาใส่ URL ที่ถูกต้องที่ขึ้นต้นด้วย http:// หรือ https://"

    ERROR_OCCURRED_MSG = "❌ <b>เกิดข้อผิดพลาด</b>\n\n<code>{url}</code>\n\nข้อผิดพลาด: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ สายการบินในการส่งวิดีโอ: {error}"
    ERROR_UNKNOWN_MSG = "❌ ข้อผิดพลาดที่ไม่ทราบสาเหตุ: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ พื้นที่ดิสก์ไม่เพียงพอสำหรับการดาวน์โหลดวิดีโอ"
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ ขนาดไฟล์เกินขีดจำกัด {limit} GB กรุณาเลือกไฟล์ที่เล็กกว่าในขนาดที่อนุญาต"
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>ไม่สามารถดาวน์โหลดวิดีโอด้วยพร็อกซี่ที่มีอยู่ทั้งหมดได้</b>\n\nความพยายามในการดาวน์โหลดผ่านพร็อกซี่ทั้งหมดล้มเหลว\nลอง:\n• ตรวจสอบการทำงานของพร็อกซี่\n• ลองพร็อกซี่อื่นจากรายการ\n• ดาวน์โหลดโดยไม่ใช้พร็อกซี่ (ถ้าเป็นไปได้)"

    ERROR_GETTING_LINK_MSG = "❌ <b>ข้อผิดพลาดในการรับลิงก์:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram จำกัดการส่งข้อความ\n⏳ กรุณารอ: {time}\nเพื่ออัปเดตตัวจับเวลา ส่ง URL อีกครั้ง 2 ครั้ง"
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram จำกัดการส่งข้อความ\n⏳ กรุณารอ: \nเพื่ออัปเดตตัวจับเวลา ส่ง URL อีกครั้ง 2 ครั้ง"
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ ดาวน์โหลดคำบรรยายล้มเหลว"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>ลิงก์สตรีมโดยตรง</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>ชื่อเรื่อง:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>ระยะเวลา:</b> {duration} วินาที\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ ข้อผิดพลาด: ไม่พบข้อความต้นฉบับ"

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ แท็ก #{tag} มีอักขระที่ไม่อนุญาต อนุญาตเฉพาะตัวอักษร ตัวเลข และ _ เท่านั้น\nกรุณาใช้: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ วิดีโอเพลย์ลิสต์ส่งแล้ว: {sent}/{total} ไฟล์"
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>เคล็ดลับเกี่ยวกับเพลย์ลิสต์</b>

คุณส่งลิงก์เพลย์ลิสต์โดยไม่ระบุช่วง บอทดาวน์โหลดวิดีโอแรกโดยอัตโนมัติ (<code>*1*1</code>)

<b>ในการดาวน์โหลดวิดีโอหลายรายการจากเพลย์ลิสต์ ให้ระบุช่วง:</b>
• <code>URL*1*5</code> — วิดีโอ 5 รายการแรก (ตั้งแต่ 1 ถึง 5 รวม)
• <code>URL*3*3</code> — เฉพาะวิดีโอที่ 3
• <code>/vid 1-10 URL</code> — รูปแบบทางเลือก

เรียนรู้เพิ่มเติม: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ ส่งจากแคช: {cached}/{total} ไฟล์"
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ รับลิงก์สตรีมล้มเหลว"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "เลือกดาวน์โหลดเพื่อดาวน์โหลดคุกกี้:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "ค้นพบเรื่องราวนี้ในเรื่องราวการดาวน์โหลดคุกกี้จาก URL ที่ยาวนานหรือตรวจสอบสถานะต่อเนื่อง:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>เปิดเครื่อง</b> - โทนเนอร์ในแอปมินิ"
    BROWSER_OPEN_BUTTON_MSG = "🌐 ออดิโออิน"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 ดาวน์โหลดจาก URL ที่มา"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ คุกกี้ YouTube ดาวน์โหลดผ่านทางเลือกและบันทึกเป็น cookie.txt ต่อไป"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ไม่พบความแตกต่างที่เข้ากันได้กับและไม่ได้หมายความว่า COOKIE_URL ใช้ /cookie หรือคุกกี้หรือคุกกี้.txt"
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ COOKIE_URL ทางเลือกมุ่งไปที่ไฟล์ .txt"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌นั่นหมายความว่าคุกกี้ทางเลือกขนาดใหญ่เกินไป (>100KB)"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ แหล่งคุกกี้ fallback ไม่พร้อมใช้งาน (สถานะ {status}) ลอง /cookie หรืออัปโหลด cookie.txt"
    COOKIE_FALLBACK_ERROR_MSG = "❌ ที่นั่นในนั้นคุกกี้ fallback ลอง /cookie หรือคุกกี้ cookie.txt"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ ที่จะไปถึงระหว่างนั้นคุกกี้ทางเลือก"
    BTN_CLOSE = "🔚ปิด"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ ค่าบูลีนไม่ถูกต้อง"
    ARGS_CLOSED_MSG = "ปิดแล้ว"
    ARGS_ALL_RESET_MSG = "✅ รีเซ็ตอาร์กิวเมนต์ทั้งหมดแล้ว"
    ARGS_RESET_ERROR_MSG = "❌ เกิดข้อผิดพลาดในการรีเซ็ตอาร์กิวเมนต์"
    ARGS_INVALID_PARAM_MSG = "❌ พารามิเตอร์ไม่ถูกต้อง"
    ARGS_BOOL_SET_MSG = "ตั้งค่าเป็น {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "ตั้งค่าเป็น {value} แล้ว"
    ARGS_INVALID_SELECT_MSG = "❌ ค่าที่เลือกไม่ถูกต้อง"
    ARGS_VALUE_SET_MSG = "ตั้งค่าเป็น {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "ตั้งค่าเป็น {value} แล้ว"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>ค่าปัจจุบัน:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>ตัวอย่าง:</b>\n• <code>default</code> - ใช้กลยุทธ์ XFF เริ่มต้น\n• <code>never</code> - ไม่ใช้หัวข้อ XFF\n• <code>US</code> - รหัสประเทศสหรัฐอเมริกา\n• <code>GB</code> - รหัสประเทศสหราชอาณาจักร\n• <code>DE</code> - รหัสประเทศเยอรมนี\n• <code>FR</code> - รหัสประเทศฝรั่งเศส\n• <code>JP</code> - รหัสประเทศญี่ปุ่น\n• <code>192.168.1.0/24</code> - บล็อก IP (CIDR)\n• <code>10.0.0.0/8</code> - ช่วง IP ส่วนตัว\n• <code>203.0.113.0/24</code> - บล็อก IP สาธารณะ\n\n"
    ARGS_XFF_NOTE_MSG = "<b>หมายเหตุ:</b> สิ่งนี้แทนที่ตัวเลือก --geo-bypass ใช้รหัสประเทศ 2 ตัวอักษรหรือบล็อก IP ในสัญกรณ์ CIDR\n\n"
    ARGS_EXAMPLE_MSG = "<b>ตัวอย่าง:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "กรุณาส่งค่าของคุณใหม่"
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>ช่วง:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "กรุณาส่งตัวเลข"
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>ตัวอย่าง:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>หมายเหตุ:</b> หัวข้อเหล่านี้จะถูกเพิ่มเข้าไปในหัวข้อ Referer และ User-Agent ที่มีอยู่\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 อาร์กิวเมนต์ yt-dlp ปัจจุบัน:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - สวิตช์ True/False\n• 📋 <b>Select</b> - เลือกจากตัวเลือก\n• 🔢 <b>Numeric</b> - การป้อนตัวเลข\n• 📝🔧 <b>Text</b> - การป้อนข้อความ/JSON</blockquote>\n\nการตั้งค่าเหล่านี้จะถูกนำไปใช้กับการดาวน์โหลดทั้งหมดของคุณ"
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "บังคับการเชื่อมต่อ IPv6",
        "force_ipv4": "บังคับการเชื่อมต่อ IPv4", 
        "no_live_from_start": "ไม่ดาวน์โหลดสตรีมสดตั้งแต่เริ่มต้น",
        "live_from_start": "ดาวน์โหลดสตรีมสดตั้งแต่เริ่มต้น",
        "no_check_certificates": "ระงับการตรวจสอบใบรับรอง HTTPS",
        "check_certificate": "ตรวจสอบใบรับรอง SSL",
        "no_playlist": "ดาวน์โหลดเฉพาะวิดีโอเดียว ไม่ใช่เพลย์ลิสต์",
        "embed_metadata": "ฝังเมตาดาต้าในไฟล์วิดีโอ",
        "embed_thumbnail": "ฝังภาพย่อในไฟล์วิดีโอ",
        "write_thumbnail": "เขียนภาพย่อไปยังไฟล์",
        "ignore_errors": "ละเว้นข้อผิดพลาดในการดาวน์โหลดและดำเนินการต่อ",
        "legacy_server_connect": "อนุญาตการเชื่อมต่อเซิร์ฟเวอร์แบบเก่า",
        "concurrent_fragments": "จำนวนส่วนที่ดาวน์โหลดพร้อมกัน",
        "xff": "กลยุทธ์หัวข้อ X-Forwarded-For",
        "user_agent": "หัวข้อ User-Agent",
        "impersonate": "การเลียนแบบเบราว์เซอร์",
        "referer": "หัวข้อ Referer",
        "geo_bypass": "ข้ามข้อจำกัดทางภูมิศาสตร์",
        "hls_use_mpegts": "ใช้ MPEG-TS สำหรับ HLS",
        "no_part": "ไม่ใช้ไฟล์ .part",
        "no_continue": "ไม่ดำเนินการดาวน์โหลดบางส่วนต่อ",
        "audio_format": "รูปแบบเสียง",
        "video_format": "รูปแบบวิดีโอ",
        "merge_output_format": "รูปแบบผลลัพธ์การรวม",
        "send_as_file": "ส่งเป็นไฟล์",
        "username": "ชื่อผู้ใช้",
        "password": "รหัสผ่าน",
        "twofactor": "รหัสยืนยันตัวตนสองขั้นตอน",
        "min_filesize": "ขนาดไฟล์ขั้นต่ำ (MB)",
        "max_filesize": "ขนาดไฟล์สูงสุด (MB)",
        "playlist_items": "รายการเพลย์ลิสต์",
        "date": "วันที่",
        "datebefore": "วันที่ก่อน",
        "dateafter": "วันที่หลัง",
        "http_headers": "หัวข้อ HTTP",
        "sleep_interval": "ช่วงเวลาพัก",
        "max_sleep_interval": "ช่วงเวลาพักสูงสุด",
        "retries": "จำนวนครั้งที่ลองใหม่",
        "http_chunk_size": "ขนาดส่วน HTTP",
        "sleep_subtitles": "พักสำหรับคำบรรยาย"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ การกำหนดค่าอาร์กิวเมนต์ yt-dlp</b>\n\n<blockquote>📋 <b>กลุ่ม:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ การกำหนดค่าอาร์กิวเมนต์ yt-dlp</b>\n\n"
        "<blockquote>📋 <b>กลุ่ม:</b>\n"
        "• ✅/❌ <b>Boolean</b> - สวิตช์ True/False\n"
        "• 📋 <b>Select</b> - เลือกจากตัวเลือก\n"
        "• 🔢 <b>Numeric</b> - การป้อนตัวเลข\n"
        "• 📝🔧 <b>Text</b> - การป้อนข้อความ/JSON</blockquote>\n\n"
        "การตั้งค่าเหล่านี้จะถูกนำไปใช้กับการดาวน์โหลดทั้งหมดของคุณ"
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ กรุณารอ..."
    ERROR_OCCURRED_SHORT_MSG = "❌ เกิดข้อผิดพลาด"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ โหมดการป้อนถูกปิดโดยอัตโนมัติเนื่องจากไม่มีการใช้งาน (5 นาที)"
    ARGS_INPUT_DANGEROUS_MSG = "❌ การป้อนมีเนื้อหาที่อาจเป็นอันตราย: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ การป้อนยาวเกินไป (สูงสุด 1000 ตัวอักษร)"
    ARGS_INVALID_URL_MSG = "❌ รูปแบบ URL ไม่ถูกต้อง ต้องขึ้นต้นด้วย http:// หรือ https://"
    ARGS_INVALID_JSON_MSG = "❌ รูปแบบ JSON ไม่ถูกต้อง"
    ARGS_NUMBER_RANGE_MSG = "❌ ตัวเลขต้องอยู่ระหว่าง {min_val} และ {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ รูปแบบตัวเลขไม่ถูกต้อง"
    ARGS_DATE_FORMAT_MSG = "❌ วันที่ต้องอยู่ในรูปแบบ YYYYMMDD (เช่น 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ ปีต้องอยู่ระหว่าง 1900 และ 2100"
    ARGS_MONTH_RANGE_MSG = "❌ เดือนต้องอยู่ระหว่าง 01 และ 12"
    ARGS_DAY_RANGE_MSG = "❌ วันต้องอยู่ระหว่าง 01 และ 31"
    ARGS_INVALID_DATE_MSG = "❌ รูปแบบวันที่ไม่ถูกต้อง"
    ARGS_INVALID_XFF_MSG = "❌ XFF ต้องเป็น 'default', 'never', รหัสประเทศ (เช่น US) หรือบล็อก IP (เช่น 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "ไม่ได้ตั้งค่าอาร์กิวเมนต์แบบกำหนดเอง พารามิเตอร์ทั้งหมดใช้ค่าเริ่มต้น"
    ARGS_RESET_SUCCESS_MSG = "✅ รีเซ็ตอาร์กิวเมนต์ทั้งหมดเป็นค่าเริ่มต้นแล้ว"
    ARGS_TEXT_TOO_LONG_MSG = "❌ ข้อความยาวเกินไป สูงสุด 500 ตัวอักษร"
    ARGS_ERROR_PROCESSING_MSG = "❌ เกิดข้อผิดพลาดในการประมวลผลข้อมูล กรุณาลองอีกครั้ง"
    ARGS_BOOL_INPUT_MSG = "❌ กรุณาใส่ 'True' หรือ 'False' สำหรับตัวเลือกส่งเป็นไฟล์"
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ กรุณาใส่ตัวเลขที่ถูกต้อง"
    ARGS_BOOL_VALUE_REQUEST_MSG = "กรุณาส่ง <code>True</code> หรือ <code>False</code> เพื่อเปิด/ปิดตัวเลือกนี้"
    ARGS_JSON_VALUE_REQUEST_MSG = "กรุณาส่ง JSON ที่ถูกต้อง"
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "คุณยังไม่มีแท็ก"
    TAGS_MESSAGE_CLOSED_MSG = "ปิดข้อความแท็กแล้ว"
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ ปิดคำบรรยายและปิดโหมด Always Ask แล้ว"
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ เปิด SUBS Always Ask แล้ว"
    SUBS_LANGUAGE_SET_MSG = "✅ การปรับแต่งภาษาเป็น: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️คำเตือน: เนื่องจากผลกระทบต่อ CPU สูง ฟังก์ชันนี้ทำงานช้ามาก (ใกล้เคียงเวลาจริง) และจำกัดไว้ที่:\n"
        "- คุณภาพสูงสุด 720p\n"
        "- ระยะเวลาสูงสุด 1.5 ชั่วโมง\n"
        "- ขนาดวิดีโอสูงสุด 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>คำสั่งด่วน:</b>\n"
        "• <code>/subs off</code> - ปิดคำบรรยาย\n"
        "• <code>/subs on</code> - เปิดโหมด Always Ask\n"
        "• <code>/subs ru</code> - ตั้งค่าภาษา\n"
        "• <code>/subs ru auto</code> - ตั้งค่าภาษาพร้อม AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 นักร้องถูกปิด"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} ภาษาที่เลือก: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "😢 ดาวน์โหลดเพลงดาวน์โหลด..."
    SUBS_DISABLED_ERROR_MSG = "❌ คำบรรยายถูกปิด ใช้ /subs เพื่อตั้งค่า"
    SUBS_YOUTUBE_ONLY_MSG = "❌ การดาวน์โหลดคำบรรยายรองรับเฉพาะ YouTube"
    SUBS_CAPTION_MSG = (
        "<b>💬 Subtitles</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Language:</b> {lang}\n"
        "<b>Type:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 ส่งไฟล์คำบรรยาย SRT ให้ผู้ใช้แล้ว"
    SUBS_ERROR_PROCESSING_MSG = "❌ เกิดข้อผิดพลาดในการประมวลผลไฟล์คำบรรยาย"
    SUBS_ERROR_DOWNLOAD_MSG = "❌ ดาวน์โหลดคำบรรยายไม่สำเร็จ"
    SUBS_ERROR_MSG = "❌ เกิดข้อผิดพลาดในการดาวน์โหลดคำบรรยาย: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ ตั้งค่าขนาดชิ้นส่วนแยกเป็น: {size}"
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
    SPLIT_MENU_CLOSED_MSG = "ปิดเมนูแล้ว"
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>การตั้งค่า Bot</b>\n\nเลือกหมวดหมู่:"
    SETTINGS_MENU_CLOSED_MSG = "ปิดเมนูแล้ว"
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Clean Options</b>\n\nChoose what to clean:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nChoose an action:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIA</b>\n\nChoose an action:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nChoose an action:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ MORE COMMANDS</b>\n\nChoose an action:"
    SETTINGS_COMMAND_EXECUTED_MSG = "ดำเนินการคำสั่งแล้ว"
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ จำกัด Flood ลองอีกครั้งในภายหลัง"
    SETTINGS_HINT_SENT_MSG = "ส่งคำใบ้แล้ว"
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "เปิดตัวช่วยค้นหาแล้ว"
    SETTINGS_UNKNOWN_COMMAND_MSG = "คำสั่งไม่รู้จัก"
    SETTINGS_HINT_CLOSED_MSG = "ปิดคำใบ้แล้ว"
    SETTINGS_HELP_SENT_MSG = "ส่งไฟล์ช่วยเหลือ txt ให้ผู้ใช้แล้ว"
    SETTINGS_MENU_OPENED_MSG = "เปิดเมนู /settings แล้ว"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 ปิดตัวช่วยค้นหาแล้ว"
    SEARCH_CLOSED_MSG = "ปิดแล้ว"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ พร็อกซี {status}."
    PROXY_ERROR_SAVING_MSG = "❌ เกิดข้อผิดพลาดในการบันทึกการตั้งค่าพร็อกซี"
    PROXY_MENU_TEXT_MSG = "เปิดหรือปิดการใช้เซิร์ฟเวอร์พร็อกซี่สำหรับการทำงานทั้งหมดของ yt-dlp?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "เปิดหรือปิดใช้งานโดยใช้พร็อกซีเซิร์ฟเวอร์ (มี {config_count} + {file_count}) สำหรับการดำเนินการ yt-dlp ทั้งหมด\n\nเมื่อเปิดใช้งาน ALL (AUTO) พร็อกซีจะถูกเลือกอัตโนมัติตามประเทศที่อนุญาต (จากข้อผิดพลาดของ YouTube)"
    PROXY_MENU_CLOSED_MSG = "ปิดเมนูแล้ว"
    PROXY_ENABLED_CONFIRM_MSG = "✅เปิดใช้งานพรอกซี การดำเนินการ yt-dlp ทั้งหมดจะใช้พร็อกซี"
    PROXY_ENABLED_MULTIPLE_MSG = "✅เปิดใช้งานพรอกซี การดำเนินการ yt-dlp ทั้งหมดจะใช้ {count} พร็อกซีเซิร์ฟเวอร์พร้อมวิธีเลือก {method}"

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ เปิดใช้งานพร็อกซี (อัตโนมัติเมื่อ YouTube เกิดข้อผิดพลาด)\n\nเมื่อ YouTube แจ้งข้อผิดพลาดการบล็อกตามภูมิภาค บอทจะใช้เฉพาะพร็อกซีจากประเทศที่ระบุในข้อผิดพลาดนั้น (ไม่ลองพร็อกซีทั้งหมดตามลำดับ)"
    PROXY_DISABLED_MSG = "❌ ปิดพร็อกซีแล้ว"
    PROXY_TRYING_COUNTRY_MSG = "🔄 กำลังลองพร็อกซี: {country} ({current}/{total})"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ เกิดข้อผิดพลาดในการบันทึกการตั้งค่าพร็อกซี"
    PROXY_ENABLED_CALLBACK_MSG = "เปิดใช้งานพร็อกซี่แล้ว"
    PROXY_DISABLED_CALLBACK_MSG = "ปิดใช้งานพร็อกซี่แล้ว"
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ รอจนกว่าการดาวน์โหลดก่อนหน้าจะเสร็จสิ้น"
    AUDIO_HELP_MSG = (
        "<b>🎧 Audio Download Command</b>\n\n"
        "Usage: <code>/audio URL</code>\n\n"
        "<b>Examples:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Also see: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "ปิดคำแนะนำเสียงแล้ว"
    PLAYLIST_HELP_CLOSED_MSG = "ปิดความช่วยเหลือเพลย์ลิสต์แล้ว"
    USERLOGS_CLOSED_MSG = "ปิดข้อความบันทึกแล้ว"
    HELP_CLOSED_MSG = "ปิดความช่วยเหลือแล้ว"
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW Blur Settings</b>\n\nNSFW content is <b>{status}</b>.\n\nChoose whether to blur NSFW content:"
    NSFW_MENU_CLOSED_MSG = "ปิดเมนูแล้ว"
    NSFW_BLUR_DISABLED_MSG = "ปิดการใช้งานการเบลอ NSFW"
    NSFW_BLUR_ENABLED_MSG = "เปิดใช้งานการเบลอ NSFW"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "ปิดการใช้งานการเบลอ NSFW"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "เปิดใช้งานการเบลอ NSFW"
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ มีเดียอินโฟ {status}."
    MEDIAINFO_MENU_TITLE_MSG = "เปิดหรือปิดการส่ง MediaInfo สำหรับไฟล์ที่ดาวน์โหลด?"
    MEDIAINFO_MENU_CLOSED_MSG = "ปิดเมนูแล้ว"
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ เปิด MediaInfo แล้ว หลังจากดาวน์โหลด ข้อมูลไฟล์จะถูกส่ง"
    MEDIAINFO_DISABLED_MSG = "❌ ปิด MediaInfo แล้ว"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "เปิด MediaInfo ต่อไป"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "ปิด MediaInfo ต่อไป"
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 รายการรูปแบบที่มีอยู่</b>\n\n"
        "รับรูปแบบวิดีโอ/เสียงที่มีอยู่สำหรับ URL\n\n"
        "<b>การใช้งาน:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>ตัวอย่าง:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 วิธีใช้รูปแบบ ID:</b>\n"
        "หลังจากได้รับรายการแล้ว ใช้รูปแบบ ID เฉพาะ:\n"
        "• <code>/format id 401</code> - ดาวน์โหลดรูปแบบ 401\n"
        "• <code>/format id401</code> - เหมือนด้านบน\n"
        "• <code>/format id140 audio</code> - ดาวน์โหลดรูปแบบ 140 เป็นเสียง MP3\n\n"
        "คำสั่งนี้จะแสดงรูปแบบทั้งหมดที่มีอยู่ที่สามารถดาวน์โหลดได้"
    )
    LIST_PROCESSING_MSG = "🔄 กำลังรับรูปแบบที่ใช้ได้..."
    LIST_INVALID_URL_MSG = "❌ โปรดระบุ URL ที่ถูกต้องโดยขึ้นต้นด้วย http:// หรือ https://"
    LIST_CAPTION_MSG = (
        "📃 Available formats for:\n<code>{url}</code>\n\n"
        "💡 <b>How to set format:</b>\n"
        "• <code>/format id 134</code> - Download specific format ID\n"
        "• <code>/format 720p</code> - Download by quality\n"
        "• <code>/format best</code> - Download best quality\n"
        "• <code>/format ask</code> - Always ask for quality\n\n"
        "{audio_note}\n"
        "📋 Use format ID from the list above"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Audio-only formats:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Download format 140 as MP3 audio\n"
        "• <code>/format id140 audio</code> - same as above\n"
        "These will be downloaded as MP3 audio files.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ เกิดข้อผิดพลาดในการส่งไฟล์รูปแบบ: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Failed to get formats:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ เกิดข้อผิดพลาดขณะประมวลผลคำสั่ง"
    LIST_ERROR_CALLBACK_MSG = "เกิดข้อผิดพลาด"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 วิธีใช้รูปแบบ ID:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "หลังจากได้รับรายการแล้ว ใช้รูปแบบ ID เฉพาะ:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - ดาวน์โหลดรูปแบบ 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - same as above\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - download format 140 as MP3 audio\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - same as above\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Audio-only formats detected: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "รูปแบบเหล่านี้จะถูกดาวน์โหลดเป็นไฟล์เสียง MP3\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>Video-only formats:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 ใช้รหัสรูปแบบจากรายการด้านบน"
    
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
    LINK_INVALID_URL_MSG = "❌ โปรดระบุ URL ที่ถูกต้อง"
    LINK_PROCESSING_MSG = "🔗 รับลิงค์ตรง..."
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
    KEYBOARD_ACTIVATED_MSG = "🎹 เปิดใช้งานคีย์บอร์ดแล้ว!"
    KEYBOARD_HIDDEN_MSG = "⌨️ คีย์บอร์ดซ่อนอยู่"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 เปิดใช้งานคีย์บอร์ด 1x3 แล้ว!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 เปิดใช้งานแป้นพิมพ์ 2x3 แล้ว!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 เปิดใช้งานคีย์บอร์ดอิโมจิแล้ว!"
    KEYBOARD_ERROR_APPLYING_MSG = "เกิดข้อผิดพลาดในการใช้การตั้งค่าแป้นพิมพ์ {setting}: {error}"
    
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
    FORMAT_RESOLUTION_MENU_MSG = "เลือกความละเอียดและ codec ที่ต้องการ:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ ตั้งค่ารูปแบบเป็น: Always Ask ตอนนี้จะถามคุณเกี่ยวกับคุณภาพทุกครั้งที่ส่ง URL"
    FORMAT_UPDATED_MSG = "✅ อัปเดตรูปแบบเป็น:\n{format}"
    FORMAT_SAVED_MSG = "✅ บันทึกรูปแบบแล้ว"
    FORMAT_CHOICE_UPDATED_MSG = "✅ อัปเดตตัวเลือกรูปแบบแล้ว"
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "ปิดเมนูรูปแบบที่กำหนดเองแล้ว"
    FORMAT_CODEC_SET_MSG = "✅ ตั้งค่า codec เป็น {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ อัปเดตตัวเลือกเบราว์เซอร์แล้ว"
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ การเข้าถึงถูกปฏิเสธ ผู้ดูแลระบบเท่านั้น"
    ACCESS_DENIED_ADMIN = "❌ การเข้าถึงถูกปฏิเสธ ผู้ดูแลระบบเท่านั้น"
    WELCOME_MASTER = "ยินดีต้อนรับท่านอาจารย์ 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ ขออภัย... มีข้อผิดพลาดเกิดขึ้นระหว่างการดาวน์โหลด"
    SIZE_LIMIT_EXCEEDED = "❌ ขนาดไฟล์เกินขีดจำกัด {max_size_gb} GB โปรดเลือกไฟล์ที่มีขนาดเล็กกว่าในขนาดที่อนุญาต"
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ ไม่พบสคริปต์: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ กำลังดาวน์โหลด Firebase dump ใหม่โดยใช้ {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ โหลดแคช Firebase สำเร็จแล้ว!"
    ADMIN_CACHE_FAILED_MSG = "❌ ไม่สามารถโหลดแคช Firebase ใหม่ได้ ตรวจสอบว่า {cache_file} มีอยู่หรือไม่"
    ADMIN_ERROR_RELOADING_MSG = "❌ เกิดข้อผิดพลาดในการโหลดแคชซ้ำ: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ เกิดข้อผิดพลาดในการรัน {script_path}:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ ข้อความส่งเสริมการขายส่งถึงผู้ใช้รายอื่นทั้งหมด</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ ไม่สามารถส่งข้อความส่งเสริมการขายได้ ลองตอบกลับข้อความ\nหรือเกิดข้อผิดพลาดบางอย่าง</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ ผู้ใช้ยังไม่ได้ดาวน์โหลดเนื้อหาใดๆ...</b> ไม่มีอยู่ในบันทึก"
    ADMIN_INVALID_COMMAND_MSG = "❌คำสั่งไม่ถูกต้อง"
    ADMIN_NO_DATA_FOUND_MSG = "❌ ไม่พบข้อมูลในแคชสำหรับ <code>{{path}code>"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️คิวว่าง — ยังไม่มีใครออกจากช่องเลย"
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Ban queue</b>\nPending total: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (ซ้าย: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… และ {extra} ผู้ใช้เพิ่มขึ้น"
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "ใช้ /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ บล็อกผู้ใช้จากคิว: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ เปิดใช้งานการบล็อกอัตโนมัติ: ผู้ออกใหม่จะถูกแบนทันที"
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ ปิดการใช้งานการบล็อกอัตโนมัติ"
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ หน้าต่างบล็อกอัตโนมัติตามกำหนดเวลาตั้งค่าเป็นทุก ๆ {interval}"
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 บันทึกกิจกรรมของช่องสำหรับ {hours} ชั่วโมงที่ผ่านมา (2 วัน)"
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "dict {left} ชั่วโมงล่าสุด (2 วัน): เข้าร่วม {joined}กไป {left}"
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ ไม่มีกิจกรรมในช่วง {hours} ชั่วโมงที่ผ่านมา (2 วัน)"
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "ทั้งหมด: 🟢 {joined} เข้าร่วม, 🔴 {left} ออก"
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ ไม่สามารถเข้าถึงบันทึกกิจกรรมของช่อง บอทไม่สามารถอ่านบันทึกของผู้ดูแลระบบได้ ระบุ CHANNEL_GUARD_SESSION_STRING ในการกำหนดค่าด้วยเซสชันผู้ใช้เพื่อเปิดใช้งานคุณลักษณะนี้"
    BAN_TIME_USAGE_MSG = "❌ การใช้งาน: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ ใช้รูปแบบเช่น 10s, 6m, 5h, 4d, 3w, 2M หรือ 1y"
    BAN_TIME_SET_MSG = "🕒 ตั้งค่าช่วงเวลาการสแกนบันทึกช่องเป็น {interval}"
    BAN_TIME_REPORT_MSG = (
        "🛡️ Channel scan report\n"
        "Run at: {run_ts}\n"
        "Interval: {interval}\n"
        "New leavers: {new_leavers}\n"
        "Auto bans: {auto_banned}\n"
        "Pending: {pending}\n"
        "Last event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ การใช้งาน: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 แอดมินไม่สามารถลบแอดมินได้"
    ADMIN_USER_BLOCKED_MSG = "ผู้ใช้ถูกบล็อก 🔒❌\n \nID: <code>{user_id}</code>\nวันที่บล็อก: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> ถูกบล็อกแล้ว ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 ขออภัย! คุณไม่ใช่ผู้ดูแลระบบ"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ การใช้งาน: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "ผู้ใช้ถูกยกเลิกการบล็อก 🔓✅\n \nID: <code>{user_id}</code>\nวันที่ยกเลิกการบล็อก: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> ปลดล็อคแล้ว ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ ผู้ใช้ที่ปลดบล็อก: {count}\n⏱ วันที่: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ การใช้งาน: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "ผู้ใช้ถูกละเว้น 👁️❌\n \nID: <code>{user_id}</code>\nวันที่ละเว้น: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> ถูกละเว้นอยู่แล้ว ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ การใช้งาน: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "ผู้ใช้ไม่ถูกละเว้นอีกต่อไป 👁️✅\n \nID: <code>{user_id}</code>\nวันที่ไม่ละเว้น: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> ไม่ถูกละเว้น ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>เวลาทำงานของบอท -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ โปรดระบุ URL เพื่อล้างแคช\nการใช้งาน: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ โปรดระบุ URL ที่ถูกต้อง\nการใช้งาน: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ ล้างแคชสำเร็จสำหรับ URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ ไม่พบแคชสำหรับลิงก์นี้"
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ เกิดข้อผิดพลาดในการล้างแคช: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ การเข้าถึงถูกปฏิเสธ ผู้ดูแลระบบเท่านั้น"
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ เรียกใช้สคริปต์อัปเดตรายการสื่อลามก: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ สคริปต์สำเร็จแล้ว!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ สคริปต์เสร็จสมบูรณ์!\n\nผลลัพธ์:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ สคริปต์ล้มเหลวด้วยรหัสส่งคืน {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ เกิดข้อผิดพลาดในการรันสคริปต์: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ กำลังโหลดสื่อลามกและแคชที่เกี่ยวข้องกับโดเมน..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ โหลดแคชสื่อลามกสำเร็จ!\n\n"
        "📊 สถานะแคชปัจจุบัน:\n"
        "• โดเมนสื่อลามก: {porn_domains}\n"
        "• คำหลักสื่อลามก: {porn_keywords}\n"
        "• เว็บไซต์ที่รองรับ: {supported_sites}\n"
        "• รายชื่อขาว: {whitelist}\n"
        "• รายชื่อเทา: {greylist}\n"
        "• รายชื่อดำ: {black_list}\n"
        "• คำหลักขาว: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ เกิดข้อผิดพลาดในการโหลดแคชสื่อลามกซ้ำ: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ โปรดระบุ URL เพื่อตรวจสอบ\nการใช้งาน: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ โปรดระบุ URL ที่ถูกต้อง\nการใช้งาน: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 กำลังตรวจสอบ URL สำหรับเนื้อหา NSFW...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>ผลการตรวจสอบเนื้อหาลามก</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>สถานะ:</b> <b>{status_text}</b>\n\n"
        "<b>Explanation:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ เกิดข้อผิดพลาดในการตรวจสอบ URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "ทำความสะอาด cookies แล้ว"
    CLEAN_LOGS_CLEANED_MSG = "ทำความสะอาดบันทึกแล้ว"
    CLEAN_TAGS_CLEANED_MSG = "ทำความสะอาดแท็กแล้ว"
    CLEAN_FORMAT_CLEANED_MSG = "ทำความสะอาดรูปแบบแล้ว"
    CLEAN_SPLIT_CLEANED_MSG = "ทำความสะอาดการแบ่งแล้ว"
    CLEAN_MEDIAINFO_CLEANED_MSG = "ทำความสะอาด MediaInfo แล้ว"
    CLEAN_SUBS_CLEANED_MSG = "ทำความสะอาดการตั้งค่าคำบรรยายแล้ว"
    CLEAN_KEYBOARD_CLEANED_MSG = "ทำความสะอาดการตั้งค่าแป้นพิมพ์แล้ว"
    CLEAN_ARGS_CLEANED_MSG = "ทำความสะอาดการตั้งค่าอาร์กิวเมนต์แล้ว"
    CLEAN_NSFW_CLEANED_MSG = "ทำความสะอาดการตั้งค่า NSFW แล้ว"
    CLEAN_PROXY_CLEANED_MSG = "ทำความสะอาดการตั้งค่าพร็อกซี่แล้ว"
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "ทำความสะอาดการตั้งค่า Flood wait แล้ว"
    CLEAN_ALL_CLEANED_MSG = "ทำความสะอาดไฟล์ทั้งหมดแล้ว"
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nChoose an action:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ บันทึกไฟล์คุกกี้แล้ว"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ ข้ามการตรวจสอบคุกกี้ที่ไม่ใช่ของ YouTube"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ มีไฟล์คุกกี้อยู่แต่มีรูปแบบไม่ถูกต้อง"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ ไม่พบไฟล์คุกกี้"
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Starting YouTube cookies test...\n\nPlease wait while I check and validate your cookies."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Your existing YouTube cookies are working properly!\n\nNo need to download new ones."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Your existing YouTube cookies are expired or invalid.\n\n🔄 Downloading new cookies..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} แหล่งที่มาของคุกกี้ไม่ได้กำหนดค่า!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} แหล่งที่มาของคุกกี้ต้องเป็นไฟล์ .txt!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Range limit exceeded: {range_count} files requested (maximum {max_img_files}).\n\nUse one of these commands to download maximum available files:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚ปิด"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Media limit exceeded: {count} files requested (maximum {max_count}).\n\nUse one of these commands to download maximum available files:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 พบ <b>{count}</b> รายการสื่อจากลิงก์"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "เลือกช่วงการดาวน์โหลด:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "การเลียนแบบเบราว์เซอร์"
    ARGS_REFERER_DESC_MSG = "ส่วนหัว Referer"
    ARGS_USER_AGENT_DESC_MSG = "ส่วนหัว User-Agent"
    ARGS_GEO_BYPASS_DESC_MSG = "ข้ามข้อจำกัดทางภูมิศาสตร์"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "ตรวจสอบใบรับรอง SSL"
    ARGS_LIVE_FROM_START_DESC_MSG = "ดาวน์โหลดสตรีมสดตั้งแต่เริ่มต้น"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "ไม่ดาวน์โหลดสตรีมสดตั้งแต่เริ่มต้น"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "ใช้คอนเทนเนอร์ MPEG-TS สำหรับวิดีโอ HLS"
    ARGS_NO_PLAYLIST_DESC_MSG = "ดาวน์โหลดเฉพาะวิดีโอเดียว ไม่ใช่เพลย์ลิสต์"
    ARGS_NO_PART_DESC_MSG = "ไม่ใช้ไฟล์ .part"
    ARGS_NO_CONTINUE_DESC_MSG = "ไม่ดำเนินการดาวน์โหลดบางส่วนต่อ"
    ARGS_AUDIO_FORMAT_DESC_MSG = "รูปแบบเสียงสำหรับการสกัด"
    ARGS_EMBED_METADATA_DESC_MSG = "ฝังข้อมูลเมตาในไฟล์วิดีโอ"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "ฝังภาพย่อในไฟล์วิดีโอ"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "เขียนภาพย่อไปยังไฟล์"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "จำนวนส่วนที่ดาวน์โหลดพร้อมกัน"
    ARGS_FORCE_IPV4_DESC_MSG = "บังคับการเชื่อมต่อ IPv4"
    ARGS_FORCE_IPV6_DESC_MSG = "บังคับการเชื่อมต่อ IPv6"
    ARGS_XFF_DESC_MSG = "กลยุทธ์ส่วนหัว X-Forwarded-For"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "ขนาด chunk HTTP (ไบต์)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "รอก่อนดาวน์โหลดคำบรรยาย (วินาที)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "อนุญาตการเชื่อมต่อเซิร์ฟเวอร์แบบเดิม"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "ยับยั้งการตรวจสอบใบรับรอง HTTPS"
    ARGS_USERNAME_DESC_MSG = "ชื่อผู้ใช้บัญชี"
    ARGS_PASSWORD_DESC_MSG = "รหัสผ่านบัญชี"
    ARGS_TWOFACTOR_DESC_MSG = "รหัสยืนยันตัวตนสองขั้นตอน"
    ARGS_IGNORE_ERRORS_DESC_MSG = "ละเว้นข้อผิดพลาดในการดาวน์โหลดและดำเนินการต่อ"
    ARGS_MIN_FILESIZE_DESC_MSG = "ขนาดไฟล์ขั้นต่ำ (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "ขนาดไฟล์สูงสุด (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "รายการเพลย์ลิสต์ที่จะดาวน์โหลด (เช่น 1,3,5 หรือ 1-5)"
    ARGS_DATE_DESC_MSG = "ดาวน์โหลดวิดีโอที่อัปโหลดในวันที่นี้ (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "ดาวน์โหลดวิดีโอที่อัปโหลดก่อนวันที่นี้ (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "ดาวน์โหลดวิดีโอที่อัปโหลดหลังวันที่นี้ (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "ส่วนหัว HTTP ที่กำหนดเอง (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "ช่วงเวลารอระหว่างคำขอ (วินาที)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "ช่วงเวลารอสูงสุด (วินาที)"
    ARGS_RETRIES_DESC_MSG = "จำนวนครั้งที่ลองใหม่"
    ARGS_VIDEO_FORMAT_DESC_MSG = "รูปแบบคอนเทนเนอร์วิดีโอ"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "รูปแบบคอนเทนเนอร์ผลลัพธ์สำหรับการรวม"
    ARGS_SEND_AS_FILE_DESC_MSG = "ส่งสื่อทั้งหมดเป็นเอกสารแทนสื่อ"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "เลียนแบบ"
    ARGS_REFERER_SHORT_MSG = "ผู้อ้างอิง"
    ARGS_GEO_BYPASS_SHORT_MSG = "ข้าม Geo"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "ตรวจสอบใบรับรอง"
    ARGS_LIVE_FROM_START_SHORT_MSG = "สตรีมสดเริ่มต้น"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "ไม่สตรีมสดเริ่มต้น"
    ARGS_USER_AGENT_SHORT_MSG = "ตัวแทนผู้ใช้"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "ไม่มีเพลย์ลิสต์"
    ARGS_NO_PART_SHORT_MSG = "ไม่ใช้ Part"
    ARGS_NO_CONTINUE_SHORT_MSG = "ไม่ดำเนินการต่อ"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "รูปแบบเสียง"
    ARGS_EMBED_METADATA_SHORT_MSG = "ฝังเมตา"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "ฝังภาพย่อ"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "เขียนภาพย่อ"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "พร้อมกัน"
    ARGS_FORCE_IPV4_SHORT_MSG = "บังคับ IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "บังคับ IPv6"
    ARGS_XFF_SHORT_MSG = "ส่วนหัว XFF"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "ขนาด Chunk"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "รอคำบรรยาย"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Legacy Connect"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "ไม่ตรวจสอบใบรับรอง"
    ARGS_USERNAME_SHORT_MSG = "ชื่อผู้ใช้"
    ARGS_PASSWORD_SHORT_MSG = "รหัสผ่าน"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "ละเว้นข้อผิดพลาด"
    ARGS_MIN_FILESIZE_SHORT_MSG = "ขนาดขั้นต่ำ"
    ARGS_MAX_FILESIZE_SHORT_MSG = "ขนาดสูงสุด"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "รายการเพลย์ลิสต์"
    ARGS_DATE_SHORT_MSG = "วันที่"
    ARGS_DATEBEFORE_SHORT_MSG = "ก่อนวันที่"
    ARGS_DATEAFTER_SHORT_MSG = "หลังวันที่"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP Headers"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "ช่วงเวลารอ"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "รอสูงสุด"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "รูปแบบวิดีโอ"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "รูปแบบการรวม"
    ARGS_SEND_AS_FILE_SHORT_MSG = "ส่งเป็นไฟล์"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ ไฟล์มีขนาดใหญ่เกินไป ขนาดสูงสุดคือ 100 KB"
    COOKIES_INVALID_FORMAT_MSG = "❌ อนุญาตให้ใช้เฉพาะไฟล์ในรูปแบบต่อไปนี้ .txt"
    COOKIES_INVALID_COOKIE_MSG = "❌ ไฟล์ดูไม่เหมือน cookie.txt (ไม่มีบรรทัด '# ไฟล์คุกกี้ Netscape HTTP')"
    COOKIES_ERROR_READING_MSG = "❌ เกิดข้อผิดพลาดในการอ่านไฟล์: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ มีไฟล์คุกกี้และมีรูปแบบที่ถูกต้อง"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} ไฟล์คุกกี้ใหญ่เกินไป! สูงสุด 100KB ได้รับ {size}KB"
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} ไฟล์คุกกี้ที่ดาวน์โหลดและบันทึกเป็น cookie.txt ในโฟลเดอร์ของคุณ</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ แหล่งคุกกี้ {service} ไม่พร้อมใช้งาน (สถานะ {status}) กรุณาลองอีกครั้งในภายหลัง"
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ เกิดข้อผิดพลาดในการดาวน์โหลดไฟล์คุกกี้ {service} โปรดลองอีกครั้งในภายหลัง"
    COOKIES_USER_PROVIDED_MSG = "<b>✅ผู้ใช้ให้ไฟล์คุกกี้ใหม่</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ อัปเดตคุกกี้สำเร็จ:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ ไม่ใช่คุกกี้ที่ถูกต้อง</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ แหล่งที่มาของคุกกี้ YouTube ไม่ได้ถูกกำหนดค่า!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ การเข้าถึงถูกปฏิเสธ ผู้ดูแลระบบเท่านั้น"
    ADMIN_USER_LOGS_TOTAL_MSG = "ทั้งหมด: <b>{total}</b>\n<b>{user_id}</b> - บันทึก (10 รายการล่าสุด):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 เปิดใช้งานคีย์บอร์ดแล้ว!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ ตั้งค่าภาษาคำบรรยายเป็น: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ ตั้งค่าภาษาคำบรรยายเป็น: {flag} {name} โดยเปิดใช้งาน AUTO/TRANS"
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "ปิดเมนูภาษาคำบรรยายแล้ว"
    SUBS_DOWNLOADING_MSG = "💌 กำลังดาวน์โหลดคำบรรยาย..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 กำลังโหลดแคช Firebase ใหม่ในหน่วยความจำ..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ ไม่ได้กำหนดค่า COOKIE_URL ใช้ /cookie หรืออัพโหลด cookie.txt"
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 กำลังดาวน์โหลดคุกกี้จาก URL ระยะไกล..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ COOKIE_URL สำรองจะต้องชี้ไปที่ไฟล์ .txt"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ ไฟล์คุกกี้สำรองมีขนาดใหญ่เกินไป (>100KB)"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ ไฟล์คุกกี้ YouTube ที่ดาวน์โหลดผ่านทางเลือกและบันทึกเป็น cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ แหล่งคุกกี้สำรองไม่พร้อมใช้งาน (สถานะ {status}) ลอง /cookie หรืออัปโหลด cookie.txt"
    COOKIE_FALLBACK_ERROR_MSG = "❌ เกิดข้อผิดพลาดในการดาวน์โหลดคุกกี้สำรอง ลอง /cookie หรืออัพโหลด cookie.txt"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ เกิดข้อผิดพลาดที่ไม่คาดคิดระหว่างการดาวน์โหลดคุกกี้สำรอง"
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} ไม่ได้ติดตั้งเบราว์เซอร์"
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ คุกกี้ที่บันทึกโดยใช้เบราว์เซอร์: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ ไม่สามารถบันทึกคุกกี้: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ คุกกี้ YouTube ทำงานอย่างถูกต้อง"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube cookies are expired or invalid\n\nUse /cookie to get new cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - รูปแบบที่กำหนดเอง\n• <code>/format 720</code> - คุณภาพ 720p\n• <code>/format 4k</code> - คุณภาพ 4K"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "ส่งคำใบ้แล้ว"
    FORMAT_MKV_TOGGLE_MSG = "MKV ตอนนี้ {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ ไม่มีการกำหนดค่า URL ระยะไกล"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ รูปแบบไฟล์ไม่ถูกต้อง"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ ไฟล์ใหญ่เกินไป"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ ดาวน์โหลดคุกกี้สำเร็จ"
    COOKIES_SERVER_ERROR_MSG = "❌ ข้อผิดพลาดของเซิร์ฟเวอร์ {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ ดาวน์โหลดล้มเหลว"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ข้อผิดพลาดที่ไม่คาดคิด"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ไม่ได้ติดตั้งเบราว์เซอร์"
    COOKIES_MENU_CLOSED_MSG = "ปิดเมนูแล้ว."
    COOKIES_HINT_CLOSED_MSG = "ปิดคำใบ้คุกกี้แล้ว"
    IMG_HELP_CLOSED_MSG = "ปิดความช่วยเหลือแล้ว"
    SUBS_LANGUAGE_UPDATED_MSG = "อัปเดตการตั้งค่าภาษาคำบรรยายแล้ว"
    SUBS_MENU_CLOSED_MSG = "ปิดเมนูภาษาคำบรรยายแล้ว"
    KEYBOARD_SET_TO_MSG = "ตั้งค่าแป้นพิมพ์เป็น {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "เกิดข้อผิดพลาดในการประมวลผลการตั้งค่า"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "เปิดใช้งาน MediaInfo แล้ว"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo ปิดการใช้งาน"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "ปิดการใช้งานการเบลอ NSFW"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "เปิดใช้งานการเบลอ NSFW"
    SETTINGS_MENU_CLOSED_MSG = "ปิดเมนูแล้ว."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "น้ำท่วมรออยู่ ลองใหม่ภายหลัง"
    OTHER_HELP_CLOSED_MSG = "ปิดความช่วยเหลือแล้ว"
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "ปิดข้อความบันทึกแล้ว"
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "ปิดเมนูแล้ว."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "ขนาดไม่ถูกต้อง"
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ เกิดข้อผิดพลาดในการส่ง MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ เกิดข้อผิดพลาด: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - บันทึกทั้งหมด"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - ทั้งหมด {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 ดาวน์โหลดจาก URL ระยะไกล"
    BROWSER_OPEN_BUTTON_MSG = "🌐 เปิดเบราว์เซอร์"
    SELECT_BROWSER_MSG = "เลือกเบราว์เซอร์เพื่อดาวน์โหลดคุกกี้จาก:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "ไม่พบเบราว์เซอร์ในระบบนี้ คุณสามารถดาวน์โหลดคุกกี้จาก URL ระยะไกลหรือตรวจสอบสถานะเบราว์เซอร์:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>เปิดเบราว์เซอร์</b> - เพื่อตรวจสอบสถานะเบราว์เซอร์ในแอปขนาดเล็ก"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ ไม่สามารถรัน /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ ขีดจำกัดน้ำท่วม ลองใหม่ภายหลัง"
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ ไม่สามารถเปิดเมนูคุกกี้ของเบราว์เซอร์ได้"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "บันทึกเป็นคำแนะนำคุกกี้ปิดแล้ว"
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Usage:</b>\n<code>/link [quality] URL</code>\n\n<b>Examples:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - best quality\n• /link 720 https://youtube.com/watch?v=... - 720p or lower\n• /link 720p https://youtube.com/watch?v=... - same as above\n• /link 4k https://youtube.com/watch?v=... - 4K or lower\n• /link 8k https://youtube.com/watch?v=... - 8K or lower</blockquote>\n\n<b>Quality:</b> from 1 to 10000 (e.g., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K quality"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ ไม่สามารถรับลิงก์สตรีมได้"
    LINK_ERROR_GETTING_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ ดัชนีคุกกี้ YouTube ไม่ถูกต้อง: {selected_index} ช่วงที่ใช้ได้คือ 1-{selected_index}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 กำลังดาวน์โหลดและตรวจสอบคุกกี้ YouTube...\n\nความพยายาม {attempt} จาก {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 กำลังดาวน์โหลดและตรวจสอบคุกกี้ YouTube...\n\nความพยายาม {attempt} จาก {total}\n🔍 กำลังทดสอบคุกกี้..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ ดาวน์โหลดและตรวจสอบคุกกี้ YouTube สำเร็จ!\n\nใช้แหล่ง {source} จาก {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ คุกกี้ YouTube ทั้งหมดหมดอายุหรือไม่พร้อมใช้งาน!\n\nติดต่อผู้ดูแลบอทเพื่อแทนที่"
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ เกินขีดจำกัดการลองใหม่ของคุกกี้ YouTube!\n\n🔢 สูงสุด: {limit} ครั้งต่อชั่วโมง\n⏰ กรุณาลองอีกครั้งในภายหลัง"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ แท็ก #{wrong} มีอักขระที่ไม่อนุญาต อนุญาตเฉพาะตัวอักษร ตัวเลข และ _ เท่านั้น\nกรุณาใช้: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **อาร์กิวเมนต์ไม่ถูกต้อง!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ ชุดภาษาคำบรรยาย: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "ตัวอย่าง: `/subs และอัตโนมัติ`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} ภาษาที่เลือก: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ โหมด Always Ask {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 คำบรรยายถูกปิดใช้งาน"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 การตั้งค่าคำบรรยาย</b>\n\n{status_text}\n\nเลือกภาษาคำบรรยาย:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - ปิดการใช้งานคำบรรยาย\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 การตั้งค่าคำบรรยาย</b>\n\n{status_text}\n\nเลือกภาษาคำบรรยาย:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Title:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- คุณภาพสูงสุด 720p\n- ระยะเวลาสูงสุด 1.5 ชั่วโมง\n- ขนาดวิดีโอสูงสุด 500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️คำเตือน: เนื่องจากผลกระทบต่อ CPU สูง ฟังก์ชันนี้ช้ามาก (เกือบเรียลไทม์) และจำกัดที่:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>คำสั่งด่วน:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - ปิดการใช้งานคำบรรยาย\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - เปิดใช้งานโหมดถามเสมอ\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - set language\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - set language with AUTO/TRANS enabled\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - enable Always Ask mode\n"
    SUBS_AUTO_SUBS_TEXT = "(ออโต้ซับ)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ โหมดย่อยอัตโนมัติ {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS ถูกปิดใช้งานผ่านคำสั่ง: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "เปิดใช้งาน SUBS Always Ask ผ่านคำสั่ง: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "ภาษา SUBS ตั้งค่าผ่านคำสั่ง: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "ภาษา SUBS + โหมดอัตโนมัติที่ตั้งค่าผ่านคำสั่ง: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "ผู้ใช้เปิดเมนู /subs"
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "ผู้ใช้ตั้งค่าภาษาคำบรรยายเป็น: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "ผู้ใช้สลับโหมด AUTO/TRANS เป็น: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "ผู้ใช้สลับโหมดถามเสมอเป็น: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "ผู้ใช้ร้องขอคุกกี้จากเบราว์เซอร์"
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "แป้นพิมพ์การเลือกเบราว์เซอร์ที่ส่งมาพร้อมกับเบราว์เซอร์ที่ติดตั้งไว้เท่านั้น"
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "ปิดการเลือกเบราว์เซอร์แล้ว"
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "ใช้ COOKIE_URL สำรองสำเร็จแล้ว (ซ่อนแหล่งที่มา)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "COOKIE_URL สำรองล้มเหลว: status={status} (ซ่อนอยู่)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "ข้อผิดพลาดสำรอง COOKIE_URL ที่ไม่คาดคิด: {error}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "ไม่ได้ติดตั้งเบราว์เซอร์ {browser}"
    COOKIES_SAVED_BROWSER_LOG_MSG = "คุกกี้ที่บันทึกโดยใช้เบราว์เซอร์: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "ไฟล์คุกกี้ที่บันทึกไว้สำหรับผู้ใช้ {user_id}"
    COOKIES_FILE_WORKING_LOG_MSG = "มีไฟล์คุกกี้อยู่ มีรูปแบบที่ถูกต้อง และคุกกี้ของ YouTube กำลังทำงาน"
    COOKIES_FILE_EXPIRED_LOG_MSG = "มีไฟล์คุกกี้อยู่และมีรูปแบบที่ถูกต้อง แต่คุกกี้ของ YouTube หมดอายุ"
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "มีไฟล์คุกกี้อยู่และมีรูปแบบที่ถูกต้อง"
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "มีไฟล์คุกกี้อยู่แต่มีรูปแบบไม่ถูกต้อง"
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "ไม่พบไฟล์คุกกี้"
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{service} URL คุกกี้ว่างเปล่าสำหรับผู้ใช้ {user_id}"
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} URL คุกกี้ไม่ใช่ .txt (ซ่อนอยู่)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} ไฟล์คุกกี้ใหญ่เกินไป: {size} ไบต์ (ซ่อนแหล่งที่มา)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{service} ไฟล์คุกกี้ที่ดาวน์โหลดสำหรับผู้ใช้ {user_id} (ซ่อนแหล่งที่มา)"
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "ไม่พบสคริปต์: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "ไม่สามารถส่งข้อความสถานะเริ่มต้นได้"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "ข้อผิดพลาดในการรัน {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "แคช Firebase โหลดใหม่โดยงานอัตโนมัติ"
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "แคช Firebase โหลดซ้ำโดยผู้ดูแลระบบ"
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "เกิดข้อผิดพลาดในการโหลดแคช Firebase ใหม่: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "เริ่มการออกอากาศ ข้อความ:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "ข้อความออกอากาศที่ส่งถึงผู้ใช้ทุกคน"
    ADMIN_BROADCAST_FAILED_LOG_MSG = "ไม่สามารถออกอากาศข้อความ: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "ผู้ดูแลระบบ {url} ล้างแคชสำหรับ URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "ผู้ดูแลระบบ {script_path} เริ่มต้นสคริปต์อัปเดตรายการสื่อลามก: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "สคริปต์อัปเดตรายการโป๊เสร็จสมบูรณ์โดยผู้ดูแลระบบ {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "สคริปต์อัปเดตรายการอนาจารล้มเหลวโดยผู้ดูแลระบบ {error}: {user_id}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "ผู้ดูแลระบบ {script_path} พยายามเรียกใช้สคริปต์ที่ไม่มีอยู่จริง: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "เกิดข้อผิดพลาดในการเรียกใช้สคริปต์อัปเดตสื่อลามกโดยผู้ดูแลระบบ {error}: {user_id}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "ผู้ดูแลระบบ {user_id} เริ่มโหลดแคชเนื้อหาลามกใหม่"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "เกิดข้อผิดพลาดในการโหลดแคชสื่อลามกซ้ำโดยผู้ดูแลระบบ {error}: {user_id}"
    ADMIN_PORN_CHECK_LOG_MSG = "ผู้ดูแลระบบ {status} ตรวจสอบ URL สำหรับ NSFW: {url} - ผลลัพธ์: {status}"
    
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
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "ปิดเมนูรูปแบบที่กำหนดเองแล้ว"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "แยกลิงก์โดยตรงสำหรับผู้ใช้ {user_id} จาก {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "ไม่สามารถแยกลิงก์โดยตรงสำหรับผู้ใช้ {user_id} จาก {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "เกิดข้อผิดพลาดในคำสั่งลิงก์สำหรับผู้ใช้ {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "ผู้ใช้ {setting} ตั้งค่าแป้นพิมพ์เป็น {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "ผู้ใช้ {setting} ตั้งค่าแป้นพิมพ์เป็น {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo ตั้งค่าผ่านคำสั่ง: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "ผู้ใช้เปิดเมนู /mediainfo"
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "มีเดียอินโฟ: ปิดแล้ว"
    MEDIAINFO_ENABLED_LOG_MSG = "เปิดใช้งาน MediaInfo แล้ว"
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo ปิดการใช้งาน"
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "ขนาดแยกตั้งค่าเป็น {size} ไบต์ผ่านอาร์กิวเมนต์"
    SPLIT_MENU_OPENED_LOG_MSG = "ผู้ใช้เปิด /แยกเมนู"
    SPLIT_SELECTION_CLOSED_LOG_MSG = "ปิดการเลือกแยกแล้ว"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "ตั้งค่าขนาดแยกเป็น {size} ไบต์"
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "พร็อกซีที่ตั้งค่าผ่านคำสั่ง: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "ผู้ใช้เปิดเมนู /proxy"
    PROXY_MENU_CLOSED_LOG_MSG = "หนังสือมอบฉันทะ: ปิดแล้ว"
    PROXY_ENABLED_LOG_MSG = "เปิดใช้งานพรอกซีแล้ว"
    PROXY_DISABLED_LOG_MSG = "พร็อกซีถูกปิดใช้งาน"
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "ปิดข้อความช่วยเหลือแล้ว"
    AUDIO_HELP_SHOWN_LOG_MSG = "แสดงความช่วยเหลือ /audio แล้ว"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "ผู้ใช้ขอความช่วยเหลือเกี่ยวกับเพลย์ลิสต์"
    PLAYLIST_HELP_CLOSED_LOG_MSG = "ความช่วยเหลือเกี่ยวกับเพลย์ลิสต์ปิดแล้ว"
    AUDIO_HINT_CLOSED_LOG_MSG = "ปิดคำแนะนำเสียงแล้ว"
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "เมนูลิงก์โดยตรงที่สร้างผ่านปุ่ม LINK สำหรับผู้ใช้ {user_id} จาก {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "ไม่สามารถแยกลิงก์โดยตรงผ่านปุ่ม LINK สำหรับผู้ใช้ {user_id} จาก {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "คำสั่ง LIST ดำเนินการสำหรับผู้ใช้ {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "ฝังด่วน: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "ส่งเมนูถามเสมอสำหรับ {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "สร้างเมนูคุณสมบัติแคชสำหรับผู้ใช้ {error} หลังจากข้อผิดพลาด: {user_id}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "ถามข้อผิดพลาดเมนูเสมอสำหรับ {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "รูปแบบถูกกำหนดผ่านการตั้งค่า /args"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "เสียง"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "วิดีโอ"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "วิดีโอ"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "ถัดไป ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ ก่อนหน้า"
    SUBTITLES_NEXT_BUTTON_MSG = "ต่อไป➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ ช่องข้อความทั้งหมดว่างเปล่า"
    SENDER_VIDEO_DURATION_MSG = "ระยะเวลาวิดีโอ:"
    SENDER_UPLOADING_FILE_MSG = "📤 กำลังอัพโหลดไฟล์..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 กำลังอัปโหลดวิดีโอ..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 ระยะเวลาวิดีโอ:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "อัปโหลดแล้ว 1 ไฟล์"
    DOWN_UP_VIDEO_INFO_MSG = "📋 ข้อมูลวิดีโอ"
    DOWN_UP_NUMBER_MSG = "หมายเลข"
    DOWN_UP_TITLE_MSG = "ชื่อเรื่อง"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ดาวน์โหลดวิดีโอแล้ว"
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 กำลังประมวลผลสำหรับการอัปโหลด..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 อัปโหลดไฟล์ส่วนที่แยก {part} แล้ว"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ อัพโหลดเรียบร้อยแล้ว"
    DOWN_UP_FILES_UPLOADED_MSG = "อัพโหลดไฟล์แล้ว"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (แอนดรอยด์)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 ปิด"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "ดุ๊บส์"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💌 สมัครสมาชิก"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 เบราว์เซอร์"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 รับลิงค์ตรง..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 กำลังรับรูปแบบที่ใช้ได้..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 รับคำอธิบายวิดีโอ..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ เกิดข้อผิดพลาดในการรับคำอธิบาย: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ ไม่มีคำอธิบายวิดีโอ"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ เกิดข้อผิดพลาดในการส่งคำอธิบาย: {error_msg}"
    CAPTION_SENT_LOG_MSG = "🤔 คำอธิบายวิดีโอส่งถึงผู้ใช้ {user_id} สำหรับ {url} ({title})"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 กำลังเริ่ม gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>ระยะเวลา:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>รูปแบบ:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>เบราว์เซอร์:</b> เปิดในเว็บเบราว์เซอร์"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "รูปแบบที่มีให้สำหรับ"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 วิธีใช้รหัสรูปแบบ:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "หลังจากได้รับรายการแล้ว ให้ใช้ ID รูปแบบเฉพาะ:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - ดาวน์โหลดฟอร์แมต 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - เหมือนข้างบน"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 เสียง - ดาวน์โหลดรูปแบบ 140 เป็นเสียง MP3"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 ตรวจพบรูปแบบเสียงเท่านั้น"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "รูปแบบเหล่านี้จะถูกดาวน์โหลดเป็นไฟล์เสียง MP3"
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>วิธีกำหนดรูปแบบ:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - ดาวน์โหลด ID รูปแบบเฉพาะ"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - ดาวน์โหลดตามคุณภาพ"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - ดาวน์โหลดคุณภาพดีที่สุด"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - ถามคุณภาพเสมอ"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>รูปแบบเสียงเท่านั้น:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - ดาวน์โหลดรูปแบบ 140 เป็นเสียง MP3"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "ไฟล์เหล่านี้จะถูกดาวน์โหลดเป็นไฟล์เสียง MP3"
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 ใช้รหัสรูปแบบจากรายการด้านบน"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ ข้อผิดพลาด: ไม่พบข้อความต้นฉบับ"
    ALWAYS_ASK_FORMATS_PAGE_MSG = "หน้ารูปแบบ"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ เกิดข้อผิดพลาดในการแสดงเมนูรูปแบบ"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ เกิดข้อผิดพลาดในการรับรูปแบบ"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ เกิดข้อผิดพลาดในการรับรูปแบบที่ใช้ได้"
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "โปรดลองอีกครั้งในภายหลัง"
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp ไม่สามารถประมวลผลเนื้อหานี้ได้"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "ระบบแนะนำให้ใช้ gallery-dl แทน"
    ALWAYS_ASK_OPTIONS_MSG = "**ตัวเลือก:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• สำหรับแกลเลอรี่ภาพ: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• สำหรับภาพเดี่ยว: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl มักจะทำงานได้ดีกว่าสำหรับ Instagram, Twitter และเนื้อหาโซเชียลมีเดียอื่นๆ"
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 ลองใช้ Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 รูปแบบถูกกำหนดผ่าน /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 คำบรรยาย"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎶 พากย์เสียง"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💌 — มีคำบรรยาย"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💌 — เลือกภาษาคำบรรยาย"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ ไม่พบหมวดย่อยและจะไม่ฝัง"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — โพสต์ใหม่ทันทีจากแคช"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "😢 — เลือกภาษาของเสียง"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW จ่ายแล้ว (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — เลือกคุณภาพการดาวน์โหลด"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — ดาวน์โหลดภาพ (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — รับลิงก์โดยตรงไปยังวิดีโอ"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — แสดงรายการรูปแบบที่ใช้ได้"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — เปลี่ยนวิดีโอต่อ/โคเดก"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀ฝัง"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎶 — แยกเฉพาะเสียง"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW จ่ายแล้ว (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — โพสต์ใหม่ทันทีจากแคช"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "😢 — เลือกภาษาของเสียง"
    ALWAYS_ASK_BEST_BUTTON_MSG = "ดีที่สุด"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛อื่นๆ"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝เฉพาะคำบรรยาย"
    ALWAYS_ASK_SMART_GROUPING_MSG = "การจัดกลุ่มอัจฉริยะ"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "เพิ่มแถวปุ่มการทำงาน (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "เพิ่มแถวปุ่มการทำงาน (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "เพิ่มปุ่มด้านล่างไปยังแถวที่มีอยู่"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "สร้างแถวล่างใหม่"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "ไม่พบวิดีโอในเพลย์ลิสต์"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "URL ไม่รองรับ"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "ไม่พบวิดีโอ"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "ไม่พบวิดีโอ"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "ไม่พบสื่อ"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "ทวีตนี้ไม่มี"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>เกิดข้อผิดพลาดในการดึงข้อมูลวิดีโอ:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "เกิดข้อผิดพลาดในการดึงข้อมูลวิดีโอ"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "ลองใช้คำสั่ง <code>/clean</code> แล้วลองอีกครั้ง หากข้อผิดพลาดยังคงอยู่ YouTube จำเป็นต้องได้รับอนุญาต อัปเดต Cookies.txt ผ่าน <code>/cookie</code> หรือ <code>/cookies_from_browser</code> แล้วลองอีกครั้ง"
    ALWAYS_ASK_MENU_CLOSED_MSG = "ปิดเมนูแล้ว."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 การเลือกคุณภาพด้วยตนเอง"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "เลือกคุณภาพด้วยตนเองเนื่องจากการตรวจหาอัตโนมัติล้มเหลว:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 มีทุกรูปแบบ"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 คุณภาพที่มีอยู่ (จากแคช)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ การใช้คุณสมบัติแคช - อาจไม่มีรูปแบบใหม่"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 รูปแบบการดาวน์โหลด"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 กำลังดาวน์โหลด"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 กำลังดาวน์โหลดพร้อมการติดตามความคืบหน้า..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 การดาวน์โหลดโดยใช้รูปแบบ:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 การดาวน์โหลดเสียงโดยใช้รูปแบบ:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 กำลังดาวน์โหลดคุณภาพดีที่สุด..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 กำลังดาวน์โหลดดัมพ์ฐานข้อมูล..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 กำลังดาวน์โหลด"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "หน้ารูปแบบ"
    ALWAYS_ASK_FROM_CACHE_MSG = "(จากแคช)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ ข้อผิดพลาด: ไม่พบข้อความต้นฉบับ มันอาจจะถูกลบไปแล้ว กรุณาส่งลิงค์อีกครั้ง"
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ ข้อผิดพลาด: ไม่พบ URL ดั้งเดิม กรุณาส่งลิงค์อีกครั้ง"
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>ได้รับลิงก์โดยตรง</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>ชื่อเรื่อง:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>ระยะเวลา:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>รูปแบบ:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>สตรีมวิดีโอ:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>สตรีมเสียง:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ ไม่สามารถรับลิงก์สตรีมได้"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "แยกลิงก์โดยตรงผ่านเมนูถามเสมอสำหรับผู้ใช้ {user_id} จาก {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "ไม่สามารถแยกลิงก์โดยตรงผ่านเมนูถามเสมอสำหรับผู้ใช้ {error} จาก {url}{error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "ลิงก์โดยตรงที่แยกออกมาผ่าน down_and_up_with_format สำหรับผู้ใช้ {url} จาก {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "ไม่สามารถแยกลิงก์โดยตรงผ่าน down_and_up_with_format สำหรับผู้ใช้ {error} จาก {url}{error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "ลิงก์โดยตรงที่แยกออกมาผ่าน down_and_audio สำหรับผู้ใช้ {user_id} จาก {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "ไม่สามารถแยกลิงก์โดยตรงผ่าน down_and_audio สำหรับผู้ใช้ {error} จาก {url}{error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅เสียงที่ส่งจากแคช"
    AUDIO_PROCESSING_MSG = "🎙️ กำลังประมวลผลเสียง..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 กำลังดาวน์โหลดเสียง:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "เกิดข้อผิดพลาดระหว่างการดาวน์โหลดเสียง"
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ ไม่สามารถแยกข้อมูลเสียงได้"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "ข้ามประเภทไฟล์ที่ไม่รองรับในเพลย์ลิสต์ที่ดัชนี {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "ไม่พบไฟล์เสียงหลังจากดาวน์โหลด"

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ ส่งเสียงล้มเหลว: ขนาดไฟล์เท่ากับ 0 B (ดัชนีเพลย์ลิสต์ {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ ไฟล์เสียงยังกำลังดาวน์โหลดอยู่ โปรดรอสักครู่..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 กำลังอัปโหลดไฟล์เสียง...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ ไม่สามารถส่งเสียง: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "เสียงเพลย์ลิสต์ที่ส่ง: {sent}/{total} ไฟล์ (คุณภาพ={quality}) ถึงผู้ใช้{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ ไม่สามารถดาวน์โหลดเสียง: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ การดาวน์โหลดถูกยกเลิกเนื่องจากหมดเวลา (2 ชั่วโมง)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ ไม่พบไฟล์วิดีโอ: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ ส่งวิดีโอล้มเหลว: ขนาดไฟล์เท่ากับ 0 B (ดัชนีเพลย์ลิสต์ {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ ไฟล์วิดีโอยังกำลังดาวน์โหลดอยู่ โปรดรอสักครู่..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ เกิดข้อผิดพลาดในการประมวลผลวิดีโอ: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ เกิดข้อผิดพลาดในการส่งไฟล์คำอธิบาย: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 หากคุณต้องการเปลี่ยนคำบรรยายวิดีโอ - ตอบกลับวิดีโอด้วยข้อความใหม่</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "ไม่พบคำบรรยาย"
    VIDEO_PROGRESS_MSG = "<b>วิดีโอ:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>เสียง:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ เกินขีดจำกัด URL: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "ประมวลผลเสร็จสิ้น"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ ไม่อนุญาตให้ใช้ช่วงเพลย์ลิสต์ในโหมด URL หลายโหมด ส่ง URL เดียวเท่านั้นโดยไม่มีช่วง (*1*5, /vid 1-10 ฯลฯ)"
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "ตรวจสอบ <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>ที่นี่</a> หากไซต์ของคุณได้รับการรองรับ"
    ERROR_COOKIE_NEEDED_MSG = "คุณอาจต้องใช้ <code>cookie</code> เพื่อดาวน์โหลดวิดีโอนี้ ขั้นแรก ทำความสะอาดพื้นที่ทำงานของคุณผ่านคำสั่ง <b>/clean</b>"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "สำหรับ Youtube - รับ <code>cookie</code> ผ่านคำสั่ง <b>/cookie</b> สำหรับไซต์อื่นๆ ที่สนับสนุน - ส่งคุกกี้ของคุณเอง (<a href='https://t.me/tg_ytdlp/203'>guide1</a>) (<a href='https://t.me/tg_ytdlp/214'>guide2</a>) แล้วส่งลิงก์วิดีโอของคุณอีกครั้ง"
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "เลือกภาษาคำบรรยาย"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "ไม่มีภาษาอื่นทางเลือก"
    CHOOSE_AUDIO_LANGUAGE_MSG = "เลือกภาษาเสียง"
    PAGE_NUMBER_MSG = "หน้า {page}"
    TOTAL_PROGRESS_MSG = "ความคืบหน้าทั้งหมด"
    SUBTITLE_MENU_CLOSED_MSG = "ปิดเมนูคำบรรยายแล้ว"
    SUBTITLE_LANGUAGE_SET_MSG = "ชุดภาษาคำบรรยาย: {value}"
    AUDIO_SET_MSG = "ชุดเสียง: {value}"
    FILTERS_UPDATED_MSG = "อัปเดตตัวกรองแล้ว"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙กลับ"
    CLOSE_BUTTON_TEXT = "🔚ปิด"
    LIST_BUTTON_TEXT = "📃รายการ"
    IMAGE_BUTTON_TEXT = "🖼รูปภาพ"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ ไม่ได้ตรวจจับคุณภาพอัตโนมัติ\nใช้ปุ่ม 'อื่นๆ' เพื่อดูรูปแบบทั้งหมดที่พร้อมใช้งาน</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **ตรวจพบสตรีมสด**\n\nไม่อนุญาตให้ดาวน์โหลดสตรีมสดที่กำลังดำเนินอยู่หรือไม่มีที่สิ้นสุด\n\nกรุณารอให้สตรีมสิ้นสุดและลองดาวน์โหลดอีกครั้งเมื่อ:\n• รู้ระยะเวลาของสตรีม\n• สตรีมสิ้นสุดแล้ว\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>ดาวน์โหลดสตรีมสด</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "ก้อน {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "ขนาดสูงสุด: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "ระยะเวลาทั้งหมด: {duration} วินาที"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>สตรีมสด - ส่วน {chunk}</b>\n⏱ ระยะเวลา: {duration} วินาที\n📦 ขนาด: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "ก้อน {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>การดาวน์โหลดสตรีมสดเสร็จสมบูรณ์</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "ดาวน์โหลดแล้ว {chunks} ชิ้น"
    LIVE_STREAM_TOTAL_DURATION_MSG = "ระยะเวลาทั้งหมด: {duration} วินาที"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>การดาวน์โหลดสตรีมสดหยุด</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "ไดเร็กทอรีผู้ใช้ถูกลบแล้ว (อาจเป็นโดยคำสั่ง /clean)"
    LIVE_STREAM_FILE_DELETED_MSG = "ไฟล์ Chunk ถูกลบแล้ว (อาจเป็นโดยคำสั่ง /clean)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ สตรีมสิ้นสุดแล้ว"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "โปรดเลือกรูปแบบอื่นโดยใช้คำสั่ง `/format`"
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>ได้รับลิงก์โดยตรง</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Title:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **ข้อผิดพลาดในการประมวลผลไฟล์**\n\nวิดีโอถูกดาวน์โหลดแล้ว แต่ไม่สามารถประมวลผลได้เนื่องจากอักขระไม่ถูกต้องในชื่อไฟล์\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **ข้อผิดพลาดในการประมวลผลไฟล์**\n\nวิดีโอถูกดาวน์โหลดแล้ว แต่ไม่สามารถประมวลผลได้เนื่องจากข้อผิดพลาดของอาร์กิวเมนต์ที่ไม่ถูกต้อง\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**สาเหตุ:**\n"
        "• ไฟล์ที่ดาวน์โหลดไม่ใช่ไฟล์วิดีโอ\n"
        "• อาจเป็นเอกสาร (PDF, DOC ฯลฯ) หรือไฟล์เก็บถาวร\n\n"
        "**วิธีแก้ไข:**\n"
        "• ตรวจสอบลิงก์ - อาจนำไปสู่เอกสาร ไม่ใช่วิดีโอ\n"
        "• ลองใช้ลิงก์หรือแหล่งที่มาอื่น\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**สาเหตุ:**\n"
        "• ไม่สามารถประมวลผลไฟล์เป็นวิดีโอได้\n"
        "• อาจไม่ใช่ไฟล์วิดีโอหรือไฟล์เสียหาย\n\n"
        "**วิธีแก้ไข:**\n"
        "• ตรวจสอบลิงก์ - อาจนำไปสู่เอกสาร ไม่ใช่วิดีโอ\n"
        "• ลองใช้ลิงก์หรือแหล่งที่มาอื่น\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **รูปแบบไม่พร้อมใช้งาน**\n\nรูปแบบวิดีโอที่ร้องขอไม่พร้อมใช้งานสำหรับวิดีโอนี้\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ ไม่พบ Format ID {format_id} สำหรับวิดีโอนี้\n\nFormat ID ที่พร้อมใช้งาน: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **รูปแบบ AV1 ไม่พร้อมใช้งานสำหรับวิดีโอนี้**\n\n**รูปแบบที่พร้อมใช้งาน:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **ข้อผิดพลาดในการประมวลผลไฟล์**\n\nเสียงถูกดาวน์โหลดแล้ว แต่ไม่สามารถประมวลผลได้เนื่องจากอักขระไม่ถูกต้องในชื่อไฟล์\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **ข้อผิดพลาดในการประมวลผลไฟล์**\n\nเสียงถูกดาวน์โหลดแล้ว แต่ไม่สามารถประมวลผลได้เนื่องจากข้อผิดพลาดของอาร์กิวเมนต์ที่ไม่ถูกต้อง\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "ผู้ใช้ป้อนเนื้อหาต้องห้าม ไม่สามารถดาวน์โหลดได้"
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "ตั้งค่าการเบลอ NSFW ผ่านคำสั่ง: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "ผู้ใช้เปิดเมนู /nsfw"
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: ปิดแล้ว"
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "ไม่สามารถดาวน์โหลด {service} คุกกี้: status={status} (ซ่อน URL)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "เกิดข้อผิดพลาดในการดาวน์โหลด {service} คุกกี้: {error} (ซ่อน URL)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "เกิดข้อผิดพลาดที่ไม่คาดคิดขณะดาวน์โหลด {service} คุกกี้ (ซ่อน URL): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "อัปเดตไฟล์คุกกี้สำหรับผู้ใช้ {user_id}"
    COOKIES_INVALID_CONTENT_LOG_MSG = "เนื้อหาคุกกี้ที่จัดทำโดยผู้ใช้ {user_id} ไม่ถูกต้อง"
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "URL คุกกี้ของ YouTube ว่างเปล่าสำหรับผู้ใช้ {user_id}"
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "คุกกี้ YouTube ดาวน์โหลดและตรวจสอบความถูกต้องสำหรับผู้ใช้ {user_id} จากแหล่งที่มา {user_id}"
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "แหล่งที่มาของคุกกี้ YouTube ทั้งหมดล้มเหลวสำหรับผู้ใช้ {user_id}"
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "เกิดข้อผิดพลาดในคำสั่ง check_porn โดยผู้ดูแลระบบ {error}: {admin_id}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "กำหนดขนาดการแบ่งส่วนเป็น {size} ไบต์"
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "การอัปโหลดวิดีโอเสร็จสิ้นโดยมีการแยกไฟล์"
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "วิดีโอเพลย์ลิสต์ที่ส่ง: {sent}/{total} ไฟล์ (คุณภาพ={quality}) ถึงผู้ใช้ {user_id}"
    UNKNOWN_ERROR_MSG = "❌ ข้อผิดพลาดที่ไม่รู้จัก: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "ข้ามประเภทไฟล์ที่ไม่รองรับในเพลย์ลิสต์ที่ดัชนี {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg not found. Please install FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ การแปลงเป็น MP4 ล้มเหลว: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ การฝังคำบรรยายอาจใช้เวลานาน (สูงสุด 1 นาทีต่อวิดีโอ 1 นาที)!\n🔥 กำลังเริ่มเผาคำบรรยาย..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ ไม่สามารถฝังคำบรรยายได้เนื่องจากมีข้อจำกัด (คุณภาพ/ระยะเวลา/ขนาด)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ คำบรรยายไม่พร้อมใช้งานสำหรับภาษาที่เลือก"
    ERROR_SENDING_VIDEO_MSG = "❌ เกิดข้อผิดพลาดในการส่งวิดีโอ: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ วิดีโอเพลย์ลิสต์ที่ส่ง: {sent}/{total} ไฟล์"
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ การดาวน์โหลดถูกยกเลิกเนื่องจากหมดเวลา (2 ชั่วโมง)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ ไม่สามารถดาวน์โหลดวิดีโอได้: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ ข้อผิดพลาด: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON ต้องเป็นวัตถุ (พจนานุกรม)"
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ รูปแบบ JSON ไม่ถูกต้อง โปรดระบุ JSON ที่ถูกต้อง"
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ ค่าจะต้องอยู่ระหว่าง {min_val} ถึง {max_val}"
    ARGS_PARAM_SET_TO_MSG = "✅ {description} ตั้งค่าเป็น: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅จริง."
    ARGS_FALSE_BUTTON_MSG = "❌เท็จ"
    ARGS_BACK_BUTTON_MSG = "🔙 Back"
    ARGS_CLOSE_BUTTON_MSG = "🔚 ปิด"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅จริง."
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌เท็จ"
    ARGS_NOT_SET_MSG = "ไม่ได้ตั้งค่า"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ รูปแบบ AV1 ไม่พร้อมใช้งานสำหรับวิดีโอนี้\n\nรูปแบบที่พร้อมใช้งาน:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ เกิดข้อผิดพลาดในการดาวน์โหลด: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ ไม่พบวิดีโอในเพลย์ลิสต์ที่ดัชนี {index}"
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **การแปลงวิดีโอล้มเหลว**\n\nไม่สามารถแปลงวิดีโอเป็น MP4 ได้เนื่องจากข้อผิดพลาดของอาร์กิวเมนต์ที่ไม่ถูกต้อง\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **การแปลงวิดีโอล้มเหลว**\n\nไม่สามารถแปลงวิดีโอเป็น MP4 ได้\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ ไม่สามารถรับลิงก์สตรีมได้"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ ไม่พบเนื้อหาที่ดัชนี {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ ข้อผิดพลาด: ไม่พบข้อความต้นฉบับ"
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ ข้อผิดพลาด: ไม่พบ URL"
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ URL นี้ไม่สามารถฝังได้"
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} ตัวแปลงสัญญาณไม่พร้อมใช้งานสำหรับวิดีโอนี้"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} รูปแบบไม่พร้อมใช้งานสำหรับวิดีโอนี้"
    
    # Always Ask Menu button texts
    AA_AVC_BUTTON_MSG = "✅เอวีซี"
    AA_AVC_BUTTON_INACTIVE_MSG = "☑️ AVC"
    AA_AVC_BUTTON_UNAVAILABLE_MSG = "❌ AVC"
    AA_AV1_BUTTON_MSG = "✅AV1"
    AA_AV1_BUTTON_INACTIVE_MSG = "☑️ AV1"
    AA_AV1_BUTTON_UNAVAILABLE_MSG = "❌ AV1"
    AA_VP9_BUTTON_MSG = "✅VP9"
    AA_VP9_BUTTON_INACTIVE_MSG = "☑️ VP9"
    AA_VP9_BUTTON_UNAVAILABLE_MSG = "❌ VP9"
    AA_MP4_BUTTON_MSG = "✅ MP4"
    AA_MP4_BUTTON_INACTIVE_MSG = "☑️ MP4"
    AA_MP4_BUTTON_UNAVAILABLE_MSG = "❌ MP4"
    AA_MKV_BUTTON_MSG = "✅เอ็มเควี"
    AA_MKV_BUTTON_INACTIVE_MSG = "☑️ MKV"
    AA_MKV_BUTTON_UNAVAILABLE_MSG = "❌ MKV"

    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood limit. Try later."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ ตรวจสอบคุกกี้"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ อัตโนมัติ (เมื่อ YouTube เกิดข้อผิดพลาด)"
    PROXY_OFF_BUTTON_MSG = "❌ ปิด"
    PROXY_CLOSE_BUTTON_MSG = "🔚ปิด"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 เลือกประเทศ:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ ล้างการเลือกประเทศ"
    PROXY_COUNTRY_SELECTED_MSG = "✅ ประเทศที่เลือก: {country} (รหัส: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 พรอกซีที่ใช้ได้: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 บอทจะลองใช้ HTTP ก่อน จากนั้นจึงใช้ SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 เปิดใช้งานพรอกซีโดยอัตโนมัติสำหรับประเทศที่เลือก"
    PROXY_COUNTRY_CLEARED_MSG = "✅ เคลียร์การเลือกประเทศแล้ว"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ เคลียร์การเลือกประเทศแล้ว"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ ประเทศที่เลือก: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 ใช้ประเทศจากไฟล์: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 ประเทศที่มีจากไฟล์: {count}"
    PROXY_COUNTRY_NOT_AVAILABLE_MSG = "❌ พร็อกซีไม่พร้อมใช้งานสำหรับประเทศนี้ ลองประเทศอื่น"
    PROXY_COUNTRY_SET_BY_COMMAND_MSG = "✅ ตั้งค่าพร็อกซี: ประเทศ {country} (รหัส: {country_code})"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 ประเทศที่เลือก: {country} (รหัส: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ เปิดใช้งานพรอกซีสำหรับประเทศนี้"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ ปิดใช้งานพรอกซี (กดทั้งหมด (อัตโนมัติ) เพื่อเปิดใช้งาน)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅เปิด"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ ปิด"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚ปิด"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ เปิด (ไม่เบลอ)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ เปิด (ไม่เบลอ)"
    NSFW_OFF_BLUR_MSG = "✅ ปิด (เบลอ)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ ปิด (เบลอ)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "ทำความสะอาด"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "เกิดข้อผิดพลาดในการประมวลผลข้อความตอบกลับสำหรับผู้ใช้ {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "เกิดข้อผิดพลาดในการส่งการออกอากาศไปยังผู้ใช้ {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "บันทึกของ {bot_name}\nผู้ใช้: {user_id}\nบันทึกทั้งหมด: {total}\nเวลาปัจจุบัน: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nทั้งหมด {path}: {count}\nเวลาปัจจุบัน: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>ผู้ใช้ทั้งหมด: {count}</i>\n20 รายการล่าสุด {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "แคชสื่อลามกโหลดซ้ำโดยผู้ดูแลระบบ {no_cookie_domains} โดเมน: {domains}, คำสำคัญ: {keywords}, ไซต์: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "เกิดข้อผิดพลาดในการส่งข้อความหมดเวลา: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>เลือกภาษา</b>"
    LANG_CHANGED_MSG = "✅ เปลี่ยนภาษาเป็น {lang_name}"
    LANG_ERROR_MSG = "❌ เกิดข้อผิดพลาดในการเปลี่ยนภาษา"
    LANG_CLOSED_MSG = "ปิดการเลือกภาษา"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[เบราว์เซอร์] โทรกลับ: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "การเพิ่มปุ่มตรวจสอบเบราว์เซอร์ด้วย URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "URL การตรวจสอบเบราว์เซอร์ไม่ได้กำหนดค่า: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Keyboard setting updated!**\n\nNew setting: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "ไม่สามารถซ่อนแป้นพิมพ์: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "การใช้คุกกี้ YouTube ที่ใช้งานได้เพื่อแยกลิงก์สำหรับผู้ใช้ {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "ไม่มีคุกกี้ YouTube ที่ใช้งานได้สำหรับการดึงลิงก์สำหรับผู้ใช้ {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "การใช้คุกกี้ YouTube ที่มีอยู่เพื่อแยกลิงก์สำหรับผู้ใช้ {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "ไม่พบคุกกี้ YouTube สำหรับการดึงลิงก์สำหรับผู้ใช้ {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "คัดลอกไฟล์ cookie ส่วนกลางไปยังโฟลเดอร์ผู้ใช้ {user_id} สำหรับการสกัดลิงก์"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] ผู้ใช้ {user_id} ขอคำสั่ง mediainfo"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] ผู้ใช้ {is_admin} คือผู้ดูแลระบบ: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] ผู้ใช้ {user_id} อยู่ในช่อง: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] การเข้าถึงของผู้ใช้ {user_id} ถูกปฏิเสธ - ไม่ใช่ผู้ดูแลระบบและไม่ได้อยู่ในช่อง"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] ผู้ใช้ {user_id} ให้สิทธิ์การเข้าถึงแล้ว"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] โทรกลับ: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ คำสั่งนี้ใช้ได้สำหรับผู้ดูแลระบบเท่านั้น"
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ ดาวน์โหลดเสร็จสิ้นด้วยการสนับสนุนโทเค็น PO"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ ขีดจำกัดน้ำท่วม ลองใหม่ภายหลัง"
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ ข้อผิดพลาดในการรีเฟรชโทเค็น REST: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ เกิดข้อผิดพลาดในการปิดเซสชัน Firebase: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ เกิดข้อผิดพลาดในการเริ่มต้นโครงสร้าง db ฐาน: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ พารามิเตอร์บางตัวไม่ได้ตั้งค่าไว้ใน config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL ไม่ได้ถูกตั้งค่า"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey ไม่ได้ถูกตั้งค่าให้รับ idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ เกิดข้อผิดพลาดในการดาวน์โหลดดัมพ์ของ Firebase: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ ดาวน์โหลด Firebase dump ผ่าน REST ไม่สำเร็จ"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ ข้อผิดพลาดใน _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ เกิดข้อผิดพลาดในการเรียกใช้ auto reload_cache (พยายาม {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ การลองใหม่ทั้งหมดล้มเหลว"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 เริ่มดาวน์โหลด Firebase dump ที่ {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ ไม่สามารถพึ่งพาได้: คำขอหรือเซสชัน"
    DB_DATABASE_EMPTY_MSG = "⚠️ฐานข้อมูลว่างเปล่า"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ เกิดข้อผิดพลาดในการปิดตัวบันทึก: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ ข้อผิดพลาดระหว่างการล้างข้อมูล: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ ข้อผิดพลาดในการโคลน: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ หมดเวลาการโคลน"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ ข้อยกเว้นการโคลน: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ การอัปเดตถูกยกเลิกโดยผู้ใช้"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ โคลนพื้นที่เก็บข้อมูลสำเร็จ"
    UPDATE_BACKUPS_MOVED_MSG = "✅ ข้อมูลสำรองย้ายไปที่ _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ โหลดครบทุกโมดูลแล้ว"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ การล้างข้อมูลเสร็จสิ้นเมื่อออก"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 รับสัญญาณ {signal} กำลังปิดระบบอย่างเหมาะสม..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "โปรดรอ..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 กำลังดาวน์โหลดสตรีม HLS:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "รอชิ้นส่วน"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ ไม่พบข้อมูลสำรอง {ts} ใน _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ ไม่สามารถกู้คืน {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ กู้คืนแล้ว: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>รายละเอียด:</b> {error_details}\n\nหยุดการดาวน์โหลดเนื่องจากข้อผิดพลาดร้ายแรง\n\n💡 <b>เคล็ดลับ:</b> หากคุณได้รับข้อผิดพลาด 401 Unauthorized ลองใช้คำสั่ง <code>/cookie instagram</code> หรือส่งคุกกี้ของคุณเองเพื่อยืนยันตัวตนกับ Instagram"
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ โดเมนในบัญชีดำสื่อลามก: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ พบคำสำคัญอนาจาร: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ โดเมนในรายการไวท์ลิสต์: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ พบคำหลักที่อนุญาตพิเศษ: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ ไม่พบคำสำคัญภาพอนาจาร"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ ข้อผิดพลาด TikTok API ที่ดัชนี {index} กำลังข้ามไปยังเสียงถัดไป..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ ข้อผิดพลาด TikTok API ที่ดัชนี {index} กำลังข้ามไปยังวิดีโอถัดไป..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "ผู้ใช้ป้อน <b>url</b>\n <b>ชื่อผู้ใช้:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>ผู้ใช้ป้อนแบบนี้:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "เข้าร่วมช่อง"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 ตัวจัดการการลงทะเบียน: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - ดาวน์โหลดคุกกี้ 5 อันของฉัน"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - รับคุกกี้ YT ของเบราว์เซอร์"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - ตรวจสอบไฟล์คุกกี้ของคุณ"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - อัปโหลดคุกกี้ที่กำหนดเอง"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 ปิด"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "รูปแบบที่ใช้ได้สำหรับ: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚ปิด"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚ปิด"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚ปิด"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚ปิด"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "ปิดความช่วยเหลือแล้ว"
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "ปิดแล้ว"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "เกิดข้อผิดพลาด"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ไม่พบ ffmpeg ใน PATH หรือไดเรกทอรีโปรเจ็กต์ กรุณาติดตั้ง FFmpeg"
    YTDLP_NOT_FOUND_MSG = "ไม่พบไบนารี yt-dlp ใน PATH หรือไดเรกทอรีโครงการ กรุณาติดตั้ง yt-dlp"
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "วิดีโอจะถูกแบ่งเป็น {rounds} ส่วน ซึ่งอาจมากเกินไป"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "กำลังแบ่งส่วนวิดีโอ {current}/{total}: {start_time:.2f}วินาที ถึง {end_time:.2f}วินาที"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "ไม่สามารถสร้างส่วนที่แบ่ง {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "สร้างส่วนที่แบ่ง {part} สำเร็จ: {target_name} ({size} ไบต์)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "ข้อผิดพลาดในการแบ่งส่วนวิดีโอ {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "แบ่งวิดีโอเป็น {count} ส่วนสำเร็จ"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "ข้อผิดพลาดในกระบวนการแบ่งวิดีโอ: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] ข้อผิดพลาดขณะประมวลผลวิดีโอ {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "ไฟล์วิดีโอไม่มีอยู่: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "ข้อผิดพลาดในการแยกวิเคราะห์ขนาด '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "ไม่สามารถกำหนดขนาดวิดีโอจาก '{size_result}' ได้ ใช้ค่าเริ่มต้น: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "ข้อผิดพลาดในการสร้างภาพย่อ: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "ข้อผิดพลาดในการแยกวิเคราะห์ระยะเวลาวิดีโอ: {error} ผลลัพธ์คือ: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "ไม่ได้สร้างภาพย่อที่ {thumb_dir} ใช้ค่าเริ่มต้น"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "ข้อผิดพลาดในการดำเนินการคำสั่ง: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "ข้อผิดพลาดในการสร้างภาพย่อด้วย FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "ข้ามส่วนการกำหนดค่าที่ไม่ใช่ dict: {opts}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "การตั้งค่า {value}.{key} {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] การใช้คุกกี้ของผู้ใช้: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "การใช้คุกกี้ YouTube สำหรับผู้ใช้ {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "คัดลอกไฟล์ cookie ส่วนกลางไปยังโฟลเดอร์ผู้ใช้ {user_id}"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] การใช้คุกกี้ส่วนกลางที่คัดลอกมาเป็นคุกกี้ของผู้ใช้: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "ไม่สามารถคัดลอกไฟล์คุกกี้ส่วนกลางสำหรับผู้ใช้ {error}: {user_id}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "การใช้ --no-cookies สำหรับโดเมน: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "พร็อกซีร้องขอแต่ล้มเหลวในการนำเข้า/รับการกำหนดค่า: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "บังคับให้ใช้พร็อกซีสำหรับ gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "ร้องขอพร็อกซี่แต่การกำหนดค่าพร็อกซี่ไม่สมบูรณ์"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "ตัวช่วยพร็อกซีล้มเหลว: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "กำลังแยกวิเคราะห์รายการแยกวิเคราะห์..."
    GALLERY_DL_ITEM_COUNT_MSG = "รายการ {item}: {count}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "พบข้อมูลเมตา (แท็ก 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "พบ URL (แท็ก 3): {url} ข้อมูลเมตา: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "พบข้อมูลเมตา (ดั้งเดิม): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "พบ URL (เดิม): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "พบชื่อไฟล์: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "พบไดเรกทอรี: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "พบส่วนขยาย: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "แยกวิเคราะห์ {count} รายการ ข้อมูล: {info} ทางเลือก: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "การตั้งค่าการกำหนดค่า gallery-dl: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "ลองใช้กลยุทธ์ A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "ไม่พบโมดูล gallery_dl.extractor"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() ไม่พร้อมใช้งานในบิลด์นี้"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "กำลังเรียก extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "ไม่มีตัวแยกข้อมูลที่ตรงกับ URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "การตั้งค่าคุกกี้บนตัวแยก: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "ไม่สามารถตั้งค่าคุกกี้บนตัวแยก: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "พบตัวแยกข้อมูล เรียก item()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "กลยุทธ์ A สำเร็จ ได้รับข้อมูล: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "กลยุทธ์ A: extractor.items() ส่งคืนข้อมูลที่ถูกต้อง"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "กลยุทธ์ A (extractor.find) ล้มเหลว: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "ข้อมูลเมตาสำรองจาก --get-urls: Total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "กลยุทธ์ทั้งหมดล้มเหลวในการรับข้อมูลเมตา"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "ไม่สามารถแยกข้อมูลรูปภาพ: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "ไม่พบโมดูล gallery_dl.job (ติดตั้งเสียหายหรือไม่)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob ไม่พร้อมใช้งานในรุ่นนี้"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "กำลังค้นหาไฟล์ที่ดาวน์โหลดในไดเรกทอรี gallery-dl"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "กำลังพยายามค้นหาไฟล์ตามชื่อจาก extractor"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "เกิดข้อผิดพลาดในการอ่านคำโต้แย้งของผู้ใช้สำหรับ {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] เกิดข้อผิดพลาดขณะประมวลผลวิดีโอ{error}: {video_path}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "ผู้ใช้ {user_id} เปิดใช้งาน send_as_file กำลังส่งเป็นเอกสาร"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video หมดเวลาซ้ำแล้วซ้ำอีก ถอยกลับไปที่ send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "คำอธิบายยาวเกินไป กำลังลองใช้คำอธิบายแบบย่อ"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (คำบรรยายภาพขั้นต่ำ) หมดเวลา; ทางเลือกกลับไปที่ send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "เกิดข้อผิดพลาดในการส่งวิดีโอที่มีคำบรรยายน้อยที่สุด: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "เกิดข้อผิดพลาดในการส่งไฟล์คำอธิบายแบบเต็ม: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "เกิดข้อผิดพลาดในการลบไฟล์คำอธิบายชั่วคราว: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "ข้าม match_filter สำหรับโดเมนใน NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "ตรวจสอบคุกกี้ YouTube ที่มีอยู่ใน URL ของผู้ใช้เพื่อตรวจหารูปแบบสำหรับผู้ใช้ {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "YouTube cookies ที่มีอยู่ทำงานบน URL ของผู้ใช้สำหรับการตรวจจับรูปแบบสำหรับผู้ใช้ {user_id} - กำลังใช้"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "คุกกี้ YouTube ที่มีอยู่ล้มเหลวใน URL ของผู้ใช้ พยายามรับคุกกี้ใหม่สำหรับการตรวจจับรูปแบบสำหรับผู้ใช้ {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "ลองใช้แหล่งที่มาของคุกกี้ YouTube {i} เพื่อการตรวจจับรูปแบบสำหรับผู้ใช้ {i}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "YouTube cookies จากแหล่งที่มา {i} ทำงานบน URL ของผู้ใช้สำหรับการตรวจจับรูปแบบสำหรับผู้ใช้ {user_id} - บันทึกไปยังโฟลเดอร์ผู้ใช้"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "คุกกี้ YouTube จากแหล่งที่มา {user_id} ใช้ไม่ได้กับ URL ของผู้ใช้สำหรับการตรวจจับรูปแบบสำหรับผู้ใช้ {i}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "ไม่สามารถดาวน์โหลดคุกกี้ YouTube จากแหล่งที่มา {user_id} เพื่อการตรวจจับรูปแบบสำหรับผู้ใช้ {i}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "แหล่งที่มาของ YouTube cookies ทั้งหมดล้มเหลวสำหรับการตรวจจับรูปแบบสำหรับผู้ใช้ {user_id} จะลองโดยไม่มี cookies"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "ไม่ได้กำหนดค่าแหล่งที่มาของ YouTube cookies สำหรับการตรวจจับรูปแบบสำหรับผู้ใช้ {user_id} จะลองโดยไม่มี cookies"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "ไม่พบ YouTube cookies สำหรับการตรวจจับรูปแบบสำหรับผู้ใช้ {user_id} กำลังพยายามรับใหม่"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "การใช้คุกกี้ YouTube เพื่อตรวจจับรูปแบบสำหรับผู้ใช้ {user_id} (ตรวจสอบแล้วในเมนูถามเสมอ)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "ไม่พบคุกกี้ YouTube สำหรับการตรวจจับรูปแบบสำหรับผู้ใช้ {user_id} กำลังพยายามกู้คืน..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "คัดลอกไฟล์ cookie ส่วนกลางไปยังโฟลเดอร์ผู้ใช้ {user_id} สำหรับการตรวจจับรูปแบบ"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "ไม่สามารถคัดลอกไฟล์คุกกี้ส่วนกลางสำหรับผู้ใช้ {error}: {user_id}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "การใช้ --no-cookies สำหรับโดเมนใน get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "แอปยังไม่ได้เริ่มต้น ไม่สามารถเข้าถึง {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Caption:</b> <code>{caption}</code>\n<b>User id:</b> <code>{user_id}</code>\n<b>User first name:</b> <code>{users_name}</code>\n<b>Video file id:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "ข้อผิดพลาดใน Caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "ข้อผิดพลาดที่ไม่คาดคิดใน Caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 URL ของวิดีโอ</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL ขาดหายไปในการกำหนดค่า"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin เริ่มต้นได้แล้ว"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken รีเฟรชแล้ว"
    DB_LOG_FOR_USER_ADDED_MSG = "เพิ่มบันทึกสำหรับผู้ใช้แล้ว"
    DB_DATABASE_CREATED_MSG = "สร้างฐานข้อมูลแล้ว"
    DB_BOT_STARTED_MSG = "เริ่มบอทแล้ว"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY ยืนยันเป็น config.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "ส่วนเพลย์ลิสต์ถูกแคชแล้ว: {path_parts} ข้าม"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: ไม่พบแคชสำหรับ URL/ตัวแปรคุณภาพใด ๆ โดยส่งคืน dict ว่างเปล่า"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: นับอย่างรวดเร็วสำหรับช่วงขนาดใหญ่: {cached_count} วิดีโอที่แคชไว้"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: ไม่พบแคชสำหรับแฮช {quality_key} คุณ{url_hash}_0__"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: ไม่พบแคชสำหรับตัวแปร URL ใด ๆ ส่งคืนไม่มี"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ การเข้าถึงถูกปฏิเสธ ผู้ดูแลระบบเท่านั้น"
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Auto Firebase cache reloading updated!\n\n📊 Status: {status}\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ อาร์กิวเมนต์ไม่ถูกต้อง ใช้ /auto_cache บน | ปิด | ยังไม่มีข้อความ (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ ช่วงเวลาต้องอยู่ระหว่าง 1 ถึง 168 ชั่วโมง"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ ไม่สามารถกำหนดช่วงเวลาได้"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Auto Firebase cache interval updated!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Auto Firebase cache reloading started!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "เปิดใช้งานการโหลดซ้ำอัตโนมัติ; ถัดไปที่ {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "โหลดอัตโนมัติปิดการใช้งานโดยผู้ดูแลระบบ"
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "ตั้งค่าช่วงการรีโหลดอัตโนมัติเป็น {next_exec}h; ถัดไปที{interval}__"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "เริ่มโหลดอัตโนมัติแล้ว ถัดไปที่ {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "โหลดอัตโนมัติหยุดโดยผู้ดูแลระบบ"
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ โหลดแคช Firebase แล้ว: {count} โหนดรูท"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ ไม่พบไฟล์แคช Firebase โดยเริ่มต้นด้วยแคชว่าง: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ ไม่สามารถโหลดแคช firebase: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ โหลดแคช Firebase แล้ว: {count} โหนดรูท"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ ไม่พบไฟล์แคช Firebase: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ ไม่สามารถโหลดแคช firebase ใหม่ได้: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 คุณถูกแบนจากบอท! หากต้องการยกเลิกการแบน กรุณาติดต่อ {Config.ADMIN_USERNAME}\n<blockquote>P.S. อย่าออกจากช่อง - คุณจะถูกแบนโดยอัตโนมัติ ⛔️</blockquote>\n🌍เปลี่ยนภาษา /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ ไม่พบรูปแบบวิดีโอ กำลังลองใช้โปรแกรมดาวน์โหลดรูปภาพ..."
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram จำกัดการส่งข้อความ\n⏳ กรุณารอ: {time_str}\nเพื่ออัปเดตตัวจับเวลา ส่ง URL อีก 2 ครั้ง"
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>คลิกปุ่มเพื่อคัดลอก URL สตรีม จากนั้นวางในแอป VLC</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>คลิกปุ่มเพื่อคัดลอก URL สตรีม จากนั้นวางในแอป VLC</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>ข้อผิดพลาดในการรับลิงก์:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ เกิดข้อผิดพลาดในการส่งไฟล์รูปแบบ: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ ไม่สามารถรับรูปแบบได้:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 กำลังวิเคราะห์... (รอ 6 วินาที)"
    AA_PROCESSING_MSG = "🔎 กำลังวิเคราะห์..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ แท็ก #{wrong} มีอักขระที่ไม่อนุญาต อนุญาตเฉพาะตัวอักษร ตัวเลข และ _ เท่านั้น\nกรุณาใช้: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Для работы в группе боту нужны права администратора. Пожалуйста, сделайте бота дмином этой группы."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "สวัสดี {first_name},\n \n<i>บอทนี้🤖 สามารถดาวน์โหลดวิดีโอใดๆ เข้า telegram โดยตรง😊 สำหรับข้อมูลเพิ่มเติม กด <b>/help</b></i> 👈\n\n<blockquote>P.S. เนื่องจากเนื้อหา 🔞NSFW ที่อาจเกิดขึ้น - การดาวน์โหลดจาก ☁️<b>คลาวด์สตอเรจ</b> 📁<b>แชร์ไฟล์</b> 🔗<b>ตัวย่อ URL</b> และ 🔞<b>เว็บโป๊</b> เป็นแบบเสียเงิน! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ อย่า 🗑<b>ลบ/ยกเลิกสมัครช่อง @tg_ytdlp</b> และอย่า 🤖<b>สแปม URL/คำสั่งกับบอทมากเกินไป</b> - คุณจะถูกแบนจากการใช้บอทโดยอัตโนมัติ ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 ไม่มีไฟล์ที่จะลบ"
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 All files removed successfully!\n\nRemoved files:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ รอจนกว่าการดาวน์โหลดก่อนหน้าจะเสร็จสิ้น"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "อินสแตนซ์แอปเป็น None ใน check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict คือ None อนุญาตให้ดาวน์โหลด"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict คือ None อนุญาตให้ฝังคำบรรยายได้"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: การตรวจสอบขีดจำกัด - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: คีย์ info_dict: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "ข้ามการฝังคำบรรยาย: ระยะเวลา {duration}วินาที เกินขีดจำกัด {max_duration}วินาที"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "การฝังคำบรรยายถูกข้าม: ขนาด {size_mb:.2f}MB เกินขีดจำกัด {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "ข้ามการฝังคำบรรยาย: คุณภาพ {width}x{height} (ด้านที่เล็กที่สุด {min_side}p) เกินขีดจำกัด {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "ติ๊กต๊อก"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "อินสตาแกรม"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "เพลย์ลิสต์"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ เกินขีดจำกัดช่วงสำหรับ {service}: {count} (สูงสุด {max_count})\n\nใช้คำสั่งใดคำสั่งหนึ่งเหล่านี้เพื่อดาวน์โหลดไฟล์ที่มีให้มากที่สุด:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ เกินขีดจำกัดช่วงสำหรับ {service}: {count} (สูงสุด {max_count})\nID ผู้ใช้: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "ผู้ให้บริการโทเค็น PO ถูกปิดใช้งานในการกำหนดค่า"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} ไม่ใช่โดเมน YouTube กำลังข้ามโทเค็น PO"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "ผู้ให้บริการโทเค็น PO ไม่พร้อมให้บริการที่ {base_url} โดยจะกลับไปใช้การแยก YouTube แบบมาตรฐาน"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "ล้างแคชของผู้ให้บริการโทเค็น PO แล้ว จะตรวจสอบความพร้อมในคำขอถัดไป"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "อินสแตนซ์แอปยังไม่พร้อมใช้งาน"
    HELPER_USER_NAME_MSG = "ผู้ใช้"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "ตรวจพบ Flood wait กำลังรอ {wait_seconds} วินาที"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "ตรวจพบ Flood wait แต่ไม่สามารถดึงเวลาได้ กำลังรอ {retry_delay} วินาที"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "ตรวจพบข้อผิดพลาด msg_seqno เข้าสู่โหมดสลีปเป็นเวลา {retry_delay} วินาที"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "การกำหนดค่าพร็อกซี่ไม่สมบูรณ์ ใช้การเชื่อมต่อโดยตรง"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚ปิด"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚ปิด"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚ปิด"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 ลบไฟล์บันทึกแล้ว"
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 ลบไฟล์แท็กแล้ว"
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 ลบไฟล์ฟอร์แมตแล้ว"
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 ลบไฟล์แยกแล้ว"
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 ลบไฟล์ Mediainfo แล้ว"
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 ลบการตั้งค่าคำบรรยายแล้ว"
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 ลบการตั้งค่าคีย์บอร์ดแล้ว"
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 ลบการตั้งค่า Args แล้ว"
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 ลบการตั้งค่า NSFW แล้ว"
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 ลบการตั้งค่าพร็อกซีแล้ว"
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 ลบการตั้งค่าการรอน้ำท่วมแล้ว"
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚ปิด"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 คำสั่งดาวน์โหลดวิดีโอ"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "การใช้งาน: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "ตัวอย่าง:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (ลำดับตรง)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (ลำดับย้อนกลับ)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "ดูเพิ่มเติม: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "ผู้ใช้ {user_id} ปิดคำสั่ง add_bot_to_group"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "ไม่สามารถแยกรหัส YouTube"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "ไม่สามารถดาวน์โหลดภาพย่อหรือภาพใหญ่เกินไป"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "เลือกภาษาเสียง"
    AA_NO_SUBTITLES_DETECTED_MSG = "ไม่พบคำบรรยาย"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "เลือกภาษาคำบรรยาย"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "ข้อผิดพลาดในการยืนยันตัวตน"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "ไม่พบบัญชี"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "บัญชีไม่พร้อมใช้งาน"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "เกินขีดจำกัดอัตรา"
    GALLERY_DL_NETWORK_ERROR_MSG = "ข้อผิดพลาดเครือข่าย"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "เนื้อหาไม่พร้อมใช้งาน"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "ข้อจำกัดทางภูมิศาสตร์"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "ต้องยืนยันตัวตน"
    GALLERY_DL_POLICY_VIOLATION_MSG = "ละเมิดนโยบาย"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "ข้อผิดพลาดที่ไม่ทราบสาเหตุ"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ เริ่มการดาวน์โหลด</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚ปิด"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 คำสั่งดาวน์โหลดวิดีโอ</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "การใช้งาน: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>ตัวอย่าง:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "ดูเพิ่มเติม: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Flood limit. Try later."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 การใช้งานคำสั่ง Cookie</b>

<code>/cookie</code> - แสดงเมนู cookie
<code>/cookie youtube</code> - ดาวน์โหลด YouTube cookies
<code>/cookie instagram</code> - ดาวน์โหลด Instagram cookies
<code>/cookie tiktok</code> - ดาวน์โหลด TikTok cookies
<code>/cookie x</code> หรือ <code>/cookie twitter</code> - ดาวน์โหลด Twitter/X cookies
<code>/cookie facebook</code> - ดาวน์โหลด Facebook cookies
<code>/cookie custom</code> - แสดงคำแนะนำ cookie ที่กำหนดเอง

<i>บริการที่มีอยู่ขึ้นอยู่กับการกำหนดค่าบอท</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 ลบไฟล์ cookie และล้างแคชแล้ว"
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ ก่อนหน้า"
    SUBS_BACK_BUTTON_MSG = "🔙กลับ"
    SUBS_OFF_BUTTON_MSG = "🚫 ปิด"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - ตั้งค่าภาษา"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - ตั้งค่าภาษาพร้อม AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "ตัวเลือกที่ถูกต้อง:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 ภาษา"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 ควบคุม GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 สะอาด"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 คุกกี้"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 สื่อ"
    SETTINGS_INFO_BUTTON_MSG = "📖 ข้อมูล"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ เพิ่มเติม"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 เฉพาะ cookies"
    SETTINGS_LOGS_BUTTON_MSG = "📃 บันทึก "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ แท็ก"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 รูปแบบ"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ แบ่ง"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 MediaInfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 คำบรรยาย"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 แป้นพิมพ์"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ อาร์กิวเมนต์"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 พร็อกซี่"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 รอน้ำท่วม"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  ไฟล์ทั้งหมด"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - ดาวน์โหลด cookies 5 ไฟล์ของฉัน"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - รับ YT-cookie ของเบราว์เซอร์"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - ตรวจสอบไฟล์ cookie ของคุณ"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - อัปโหลด cookie ที่กำหนดเอง"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - เปลี่ยนคุณภาพและรูปแบบ"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - เปิด / ปิด MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - เปลี่ยนขนาดส่วนวิดีโอที่แบ่ง"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - ดาวน์โหลดวิดีโอเป็นเสียง"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - การตั้งค่าภาษาคำบรรยาย"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - วิธีดาวน์โหลดเพลย์ลิสต์"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - ดาวน์โหลดรูปภาพผ่าน gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - ส่ง #แท็กของคุณ"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - รับคำแนะนำ"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - ส่งบันทึกของคุณ"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - ความช่วยเหลือเพลย์ลิสต์"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - วิธีทำ"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - รับลิงก์วิดีโอโดยตรง"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - เปิด/ปิดพร็อกซี่"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - เค้าโครงแป้นพิมพ์"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - ตัวช่วยค้นหาแบบอินไลน์"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - อาร์กิวเมนต์ yt-dlp"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - การตั้งค่าการเบลอ NSFW"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 ตัวเลือกการทำความสะอาด</b>\n\nเลือกสิ่งที่ต้องการทำความสะอาด:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 มือถือ: เปิดใช้งาน @vid search"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 มือถือ: เปิดใช้งานการค้นหา @vid"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 ปิด"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 เต็ม"
    KEYBOARD_1X3_BUTTON_MSG = "📱1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[URL รูปภาพ]({url})"
    IMAGE_ERROR_MSG = "❌ ข้อผิดพลาด: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙กลับ"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - รูปแบบที่กำหนดเอง"
    FORMAT_720P_MSG = "• <code>/format 720</code> - คุณภาพ 720p"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - คุณภาพ 4K"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - คุณภาพ 8K"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - ID รูปแบบเฉพาะ"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - แสดงเมนูเสมอ"
    FORMAT_BEST_MSG = "• <code>/format best</code> - คุณภาพ bv+ba/ดีที่สุด"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ ถามเสมอ (เมนู + ปุ่ม)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 อื่นๆ (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (ดีที่สุดสำหรับ PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (ดีที่สุดสำหรับ Telegram บนมือถือ)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (คุณภาพสูงสุด)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 กำหนดเอง (ป้อนของคุณเอง)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 ยูทูป (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 จากเบราว์เซอร์"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 ทวิตเตอร์/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 ติ๊กต๊อก"
    COOKIES_VK_BUTTON_MSG = "📘 วีคอนแทคเต้"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 อินสตาแกรม"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 ของคุณเอง"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ โหมดการป้อนข้อมูลปิดโดยอัตโนมัติเนื่องจากไม่มีการใช้งาน (5 นาที)"
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 รีเซ็ตทั้งหมด"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 ดูปัจจุบัน"
    ARGS_BACK_BUTTON_MSG = "🔙 กลับ"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>ส่งต่อข้อความนี้ไปยังรายการโปรดของคุณเพื่อบันทึกการตั้งค่าเหล่านี้เป็นเทมเพลต</i> \n\n<i>ส่งต่อข้อความนี้กลับมาที่นี่เพื่อใช้การตั้งค่าเหล่านี้</i>"
    ARGS_NO_SETTINGS_MSG = "📋 อาร์กิวเมนต์ yt-dlp ปัจจุบัน:\n\nไม่มีการกำหนดค่าการตั้งค่าแบบกำหนดเอง\n\n---\n\n<i>ส่งต่อข้อความนี้ไปยังรายการโปรดของคุณเพื่อบันทึกการตั้งค่าเหล่านี้เป็นเทมเพลต</i> \n\n<i>ส่งต่อข้อความนี้กลับมาที่นี่เพื่อใช้การตั้งค่าเหล่านี้</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 อาร์กิวเมนต์ yt-dlp ปัจจุบัน:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 ส่งออกการตั้งค่า"
    ARGS_SETTINGS_READY_MSG = "การตั้งค่าพร้อมส่งออก! ส่งต่อข้อความนี้ไปยังรายการโปรดเพื่อบันทึก"
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 อาร์กิวเมนต์ yt-dlp ปัจจุบัน:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ ไม่สามารถจดจำการตั้งค่าในข้อความได้ ตรวจสอบให้แน่ใจว่าคุณส่งเทมเพลตการตั้งค่าที่ถูกต้อง"
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ นำเข้าการตั้งค่าสำเร็จ!\n\nพารามิเตอร์ที่ใช้: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "การตั้งค่าหลัก:\n"
    ARGS_ERROR_SAVING_MSG = "❌ เกิดข้อผิดพลาดในการบันทึกการตั้งค่าที่นำเข้า"
    ARGS_ERROR_IMPORTING_MSG = "❌ เกิดข้อผิดพลาดขณะนำเข้าการตั้งค่า"

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>ดาวน์โหลดไฟล์ Cookie</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "เลือกบริการเพื่อดาวน์โหลดไฟล์ cookie"
    COOKIE_MENU_SAVE_INFO_MSG = "ไฟล์ cookie จะถูกบันทึกเป็น cookie.txt ในโฟลเดอร์ของคุณ"
    COOKIE_MENU_TIP_HEADER_MSG = "เคล็ดลับ: คุณยังสามารถใช้คำสั่งโดยตรงได้:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – ดาวน์โหลดและตรวจสอบ cookies"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – ใช้แหล่งที่มาเฉพาะตามดัชนี (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "จากนั้นตรวจสอบด้วย <code>/check_cookie</code> (ทดสอบบน RickRoll)"

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "ถามเสมอ"
    SUBS_AUTO_TRANS_BUTTON_MSG = "อัตโนมัติ/แปล"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗ลิงก์"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁ดู"  # ปิดใช้งานชั่วคราว: บริการ poketube ไม่ทำงาน
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝คำอธิบาย"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ ตัด"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>ตัดวิดีโอ</b>\n\nระยะเวลาวิดีโอ: <b>{start_time} - {end_time}</b>\n\nกรุณาส่งช่วงเวลาที่ต้องการในรูปแบบ:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nตัวอย่าง: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ รูปแบบไม่ถูกต้อง กรุณาใช้: <code>HH:MM:SS-HH:MM:SS</code>\n\nตัวอย่าง: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ ช่วงเวลาไม่ถูกต้อง เวลาเริ่มต้นต้องน้อยกว่าเวลาสิ้นสุด"
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ ช่วงเวลาอยู่นอกขอบเขตของวิดีโอ\n\nระยะเวลาวิดีโอ: <b>{start_time} - {end_time}</b>\n\nช่วงเวลาของคุณต้องอยู่ภายในขีดจำกัดเหล่านี้"
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>วิดีโอจะถูกตัด:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ เสร็จสมบูรณ์บางส่วน - อัปโหลดไฟล์เสียง {successful_uploads}/{total_files} ไฟล์"
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ ดาวน์โหลดและส่งเสียงสำเร็จ - อัปโหลด {total_files} ไฟล์"

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>บัญชี TikTok ส่วนตัว</b>\n\n"
        "บัญชี TikTok นี้เป็นส่วนตัวหรือวิดีโอทั้งหมดเป็นส่วนตัว\n\n"
        "<b>💡 วิธีแก้ไข:</b>\n"
        "1. ติดตามบัญชี @{username}\n"
        "2. ส่ง cookies ของคุณไปยังบอทโดยใช้คำสั่ง <code>/cookie</code>\n"
        "3. ลองอีกครั้ง\n\n"
        "<b>หลังจากอัปเดต cookies แล้ว ลองอีกครั้ง!</b>"
    )

    #######################################################
