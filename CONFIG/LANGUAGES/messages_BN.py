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
    CREDITS_MSG = "<blockquote><i>পরিচালিত</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 ভাষা পরিবর্তন করুন: /lang</b>"
    TO_USE_MSG = "<i>এই বট ব্যবহার করতে আপনাকে @tg_ytdlp Telegram চ্যানেলে সাবস্ক্রাইব করতে হবে।</i>\nচ্যানেলে যোগদানের পর <b>আপনার ভিডিও লিঙ্কটি আবার পাঠান এবং বট এটি আপনার জন্য ডাউনলোড করবে</b> ❤️\n\n<blockquote>P.S. সম্ভাব্য 🔞NSFW কন্টেন্টের কারণে - ☁️<b>ক্লাউড স্টোরেজ</b>, 📁<b>ফাইল শেয়ার</b>, 🔗<b>URL শর্টনার</b> এবং 🔞<b>পর্ন সাইট</b> থেকে ডাউনলোড অর্থপ্রদানযোগ্য! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ @tg_ytdlp চ্যানেল 🗑<b>মুছবেন না/আনসাবস্ক্রাইব করবেন না</b> এবং বটে 🤖<b>অতিরিক্ত URL/কমান্ড স্প্যাম করবেন না</b> - বট ব্যবহার থেকে স্বয়ংক্রিয়ভাবে নিষিদ্ধ হবেন ⛔️</blockquote>"

    ERROR1 = "URL লিঙ্ক পাওয়া যায়নি। অনুগ্রহ করে <b>https://</b> বা <b>http://</b> সহ একটি URL লিখুন"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>প্লেলিস্ট (yt-dlp)</b>

প্লেলিস্ট ডাউনলোড করতে শেষে <code>*start*end</code> রেঞ্জ সহ এর URL পাঠান। উদাহরণ: <code>URL*1*5</code> (1 থেকে 5 পর্যন্ত প্রথম 5টি ভিডিও)।<code>URL*-1*-5</code> (শেষ থেকে 1 থেকে 5 পর্যন্ত শেষ 5টি ভিডিও)।
অথবা আপনি <code>/vid FROM-TO URL</code> ব্যবহার করতে পারেন। উদাহরণ: <code>/vid 3-7 URL</code> (শুরু থেকে 3 থেকে 7 পর্যন্ত ভিডিও ডাউনলোড করে)। <code>/vid -3-7 URL</code> (শেষ থেকে 3 থেকে 7 পর্যন্ত ভিডিও ডাউনলোড করে)। <code>/audio</code> কমান্ডের জন্যও কাজ করে।

<b>উদাহরণ:</b>

🟥 <b>YouTube প্লেলিস্ট থেকে ভিডিও রেঞ্জ:</b> (🍪 প্রয়োজন)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(1 থেকে 5 পর্যন্ত প্রথম 5টি ভিডিও ডাউনলোড করে)
🟥 <b>YouTube প্লেলিস্ট থেকে একক ভিডিও:</b> (🍪 প্রয়োজন)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(শুধুমাত্র 3য় ভিডিও ডাউনলোড করে)

⬛️ <b>TikTok প্রোফাইল:</b> (আপনার 🍪 প্রয়োজন)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(ব্যবহারকারী প্রোফাইল থেকে প্রথম 10টি ভিডিও ডাউনলোড করে)

🟪 <b>Instagram স্টোরিজ:</b> (আপনার 🍪 প্রয়োজন)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(প্রথম 3টি স্টোরি ডাউনলোড করে)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(অ্যালবাম থেকে প্রথম 10টি স্টোরি ডাউনলোড করে)

🟦 <b>VK ভিডিও:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(ব্যবহারকারী/গ্রুপ প্রোফাইল থেকে প্রথম 3টি ভিডিও ডাউনলোড করে)

⬛️<b>Rutube চ্যানেল:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(চ্যানেল থেকে 2 থেকে 4 পর্যন্ত ভিডিও ডাউনলোড করে)

🟪 <b>Twitch ক্লিপ:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(চ্যানেল থেকে প্রথম 3টি ক্লিপ ডাউনলোড করে)

🟦 <b>Vimeo গ্রুপ:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(গ্রুপ থেকে প্রথম 2টি ভিডিও ডাউনলোড করে)

🟧 <b>Pornhub মডেল:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(মডেল প্রোফাইল থেকে প্রথম 2টি ভিডিও ডাউনলোড করে)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(আপনার প্রম্পট দ্বারা অনুসন্ধান ফলাফল থেকে প্রথম 3টি ভিডিও ডাউনলোড করে)

এবং আরও...
দেখুন <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">সমর্থিত সাইটের তালিকা</a>
</blockquote>

<blockquote expandable>🖼 <b>ইমেজ (gallery-dl)</b>

অনেক প্ল্যাটফর্ম থেকে ইমেজ/ফটো/অ্যালবাম ডাউনলোড করতে <code>/img URL</code> ব্যবহার করুন।

<b>উদাহরণ:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>রেঞ্জ:</b>
<code>/img 11-20 https://example.com/album</code> — 11..20 আইটেম
<code>/img 11- https://example.com/album</code> — 11 থেকে শেষ পর্যন্ত (বা বট সীমা)

<i>সমর্থিত প্ল্যাটফর্মগুলির মধ্যে রয়েছে vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, ইত্যাদি। সম্পূর্ণ তালিকা:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">gallery-dl সমর্থিত সাইট</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>ভিডিও ডাউনলোড বট - সাহায্য</b>

📥 <b>মৌলিক ব্যবহার:</b>
• যেকোনো লিঙ্ক পাঠান → বট এটি ডাউনলোড করে
  <i>বট স্বয়ংক্রিয়ভাবে yt-dlp এর মাধ্যমে ভিডিও এবং gallery-dl এর মাধ্যমে ইমেজ ডাউনলোড করার চেষ্টা করে।</i>
• <b>একাধিক URL:</b> গুণমান নির্বাচন মোডে (<code>/format</code>) আপনি একটি বার্তায় <b>10টি URL</b> পর্যন্ত পাঠাতে পারেন। প্রতিটি URL একটি নতুন লাইনে বা স্পেস দ্বারা পৃথক।
• <code>/audio URL</code> → অডিও এক্সট্র্যাক্ট করুন
• <code>/link [quality] URL</code> → সরাসরি লিঙ্ক পান
• <code>/proxy</code> → সমস্ত ডাউনলোডের জন্য প্রক্সি সক্ষম/অক্ষম করুন
• টেক্সট সহ ভিডিওতে উত্তর দিন → ক্যাপশন পরিবর্তন করুন

📋 <b>প্লেলিস্ট এবং রেঞ্জ:</b>
• <code>URL*1*5</code> → প্রথম 5টি ভিডিও ডাউনলোড করুন
• <code>URL*-1*-5</code> → শেষ 5টি ভিডিও ডাউনলোড করুন
• <code>/vid 3-7 URL</code> → হয়ে যায় <code>URL*3*7</code>
• <code>/vid -3-7 URL</code> → হয়ে যায় <code>URL*-3*-7</code>

🍪 <b>কুকিজ এবং প্রাইভেট:</b>
• প্রাইভেট ভিডিওর জন্য *.txt কুকি আপলোড করুন
• <code>/cookie [service]</code> → কুকি ডাউনলোড করুন (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → ইনডেক্স দ্বারা উৎস বেছে নিন (1–N)
• <code>/cookies_from_browser</code> → ব্রাউজার থেকে এক্সট্র্যাক্ট করুন
• <code>/check_cookie</code> → কুকি যাচাই করুন
• <code>/save_as_cookie</code> → টেক্সটকে কুকি হিসাবে সংরক্ষণ করুন

🧹 <b>পরিষ্কার করা:</b>
• <code>/clean</code> → শুধুমাত্র মিডিয়া ফাইল
• <code>/clean all</code> → সবকিছু
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>সেটিংস:</b>
• <code>/settings</code> → সেটিংস মেনু
• <code>/format</code> → গুণমান এবং ফরম্যাট
• <code>/split</code> → ভিডিওকে অংশে বিভক্ত করুন
• <code>/mediainfo on/off</code> → মিডিয়া তথ্য
• <code>/nsfw on/off</code> → NSFW ব্লার
• <code>/tags</code> → সংরক্ষিত ট্যাগ দেখুন
• <code>/sub on/off</code> → সাবটাইটেল
• <code>/keyboard</code> → কীবোর্ড (OFF/1x3/2x3)

🏷️ <b>ট্যাগ:</b>
• URL এর পরে <code>#tag1#tag2</code> যোগ করুন
• ট্যাগ ক্যাপশনে প্রদর্শিত হয়
• <code>/tags</code> → সমস্ত ট্যাগ দেখুন

🔗 <b>সরাসরি লিঙ্ক:</b>
• <code>/link URL</code> → সেরা গুণমান
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → নির্দিষ্ট গুণমান

⚙️ <b>দ্রুত কমান্ড:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → গুণমান সেট করুন
• <code>/keyboard off/1x3/2x3/full</code> → কীবোর্ড লেআউট
• <code>/split 100mb-2000mb</code> → অংশের আকার পরিবর্তন করুন
• <code>/subs off/ru/en auto</code> → সাবটাইটেল ভাষা
• <code>/list URL</code> → উপলব্ধ ফরম্যাটের তালিকা
• <code>/mediainfo on/off</code> → মিডিয়া তথ্য চালু/বন্ধ করুন
• <code>/proxy on/off</code> → সমস্ত ডাউনলোডের জন্য প্রক্সি সক্ষম/অক্ষম করুন

📊 <b>তথ্য:</b>
• <code>/usage</code> → ডাউনলোড ইতিহাস
• <code>/search</code> → @vid এর মাধ্যমে ইনলাইন অনুসন্ধান

🖼 <b>ইমেজ:</b>
• <code>URL</code> → ইমেজ URL ডাউনলোড করুন
• <code>/img URL</code> → URL থেকে ইমেজ ডাউনলোড করুন
• <code>/img 11-20 URL</code> → নির্দিষ্ট রেঞ্জ ডাউনলোড করুন
• <code>/img 11- URL</code> → 11তম থেকে শেষ পর্যন্ত ডাউনলোড করুন

👨‍💻 <i>ডেভেলপার:</i> @upekshaip
🤝 <i>অবদানকারী:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "শুধু আপনার কুকিকে <b><u>cookie.txt</u></b> হিসাবে সংরক্ষণ করুন এবং এটি বটে একটি ডকুমেন্ট হিসাবে পাঠান।\n\n"
        "আপনি <b><u>/save_as_cookie</u></b> কমান্ডের সাথে সাধারণ টেক্সট হিসাবে কুকিও পাঠাতে পারেন।\n"
        "<b><b><u>/save_as_cookie</u></b> এর ব্যবহার:</b>\n\n"
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
        "<b><u>নির্দেশনা:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>ভিডিও অনুসন্ধান</b>

@vid এর মাধ্যমে ইনলাইন অনুসন্ধান সক্রিয় করতে নীচের বোতামটি টিপুন।

<blockquote>PC তে যেকোনো চ্যাটে শুধু <b>"@vid Your_Search_Query"</b> টাইপ করুন।</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 ইমেজ ডাউনলোড কমান্ড</b>\n\n"
        "ব্যবহার: <code>/img URL</code>\n\n"
        "<b>উদাহরণ:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>সমর্থিত প্ল্যাটফর্ম (উদাহরণ):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, ইত্যাদি — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">সম্পূর্ণ তালিকা</a></blockquote>"
        "এছাড়াও দেখুন: "
    )
    
    LINK_HINT_MSG = (
        "গুণমান নির্বাচনের সাথে সরাসরি ভিডিও লিঙ্ক পান।\n\n"
        "ব্যবহার: /link + URL \n\n"
        "(উদাহরণ: /link https://youtu.be/abc123)\n"
        "(উদাহরণ: /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>গ্রুপে বট যোগ করুন</b>

উন্নত বৈশিষ্ট্য এবং উচ্চ সীমা পেতে আপনার গ্রুপে আমার বটগুলি যোগ করুন!
————————————
📊 <b>বর্তমান বিনামূল্যে সীমা (বটের DM এ):</b>
<blockquote>•🗑 সমস্ত ফাইল থেকে অগোছালো আবর্জনা 👎
• সর্বোচ্চ 1 ফাইলের আকার: <b>8 GB </b>
• সর্বোচ্চ 1 ফাইলের গুণমান: <b>সীমাহীন</b>
• সর্বোচ্চ 1 ফাইলের সময়কাল: <b>সীমাহীন</b>
• সর্বোচ্চ ডাউনলোড সংখ্যা: <b>সীমাহীন</b>
• একটি বার্তায় সর্বোচ্চ URL: <b>10</b> (শুধুমাত্র গুণমান নির্বাচন মোডে)
• প্রতি 1 বার সর্বোচ্চ প্লেলিস্ট আইটেম: <b>50</b>
• প্রতি 1 বার সর্বোচ্চ TikTok ভিডিও: <b>500</b>
• প্রতি 1 বার সর্বোচ্চ ইমেজ: <b>1000</b>
• URL রেট সীমা: <b>5/মিনিট, 60/ঘন্টা, 1000/দিন</b>
• কমান্ড সীমা: <b>20/মিনিট</b>
• 1 ডাউনলোড সর্বোচ্চ সময়: <b>2 ঘন্টা</b>
• 🔞 NSFW কন্টেন্ট অর্থপ্রদানযোগ্য! 1⭐️ = $0.02
• 🆓 অন্যান্য সমস্ত মিডিয়া সম্পূর্ণ বিনামূল্যে
• 📝 সমস্ত কন্টেন্ট লগ এবং আমার লগ-চ্যানেলে ক্যাশিং পুনরায় ডাউনলোড করার সময় তাৎক্ষণিক রিপোস্টের জন্য</blockquote>

💬<b>সাবটাইটেল সহ ভিডিওর জন্য এই সীমা:</b>
<blockquote>• সর্বোচ্চ ভিডিও+সাবস সময়কাল: <b>1.5 ঘন্টা</b>
• সর্বোচ্চ ভিডিও+সাবস ফাইল আকার: <b>500 MB</b>
• সর্বোচ্চ ভিডিও+সাবস গুণমান: <b>720p</b></blockquote>
————————————
🚀 <b>পেইড গ্রুপ সুবিধা (2️⃣x সীমা):</b>
<blockquote>•  🗂 বিষয় অনুসারে সাজানো কাঠামোগত পরিষ্কার মিডিয়া ভল্ট 👍
•  📁 আপনি যে বিষয়ে কল করেন সেই বিষয়ে বটগুলি উত্তর দেয়
•  📌 ডাউনলোড অগ্রগতি সহ স্বয়ংক্রিয় পিন স্ট্যাটাস বার্তা
•  🖼 /img কমান্ড 10-আইটেম অ্যালবাম হিসাবে মিডিয়া ডাউনলোড করে
• সর্বোচ্চ 1 ফাইলের আকার: <b>16 GB</b> ⬆️
• একটি বার্তায় সর্বোচ্চ URL: <b>20</b> ⬆️ (শুধুমাত্র গুণমান নির্বাচন মোডে)
• প্রতি 1 বার সর্বোচ্চ প্লেলিস্ট আইটেম: <b>100</b> ⬆️
• প্রতি 1 বার সর্বোচ্চ TikTok ভিডিও: 1000 ⬆️
• প্রতি 1 বার সর্বোচ্চ ইমেজ: 2000 ⬆️
• URL রেট সীমা: <b>10/মিনিট, 120/ঘন্টা, 2000/দিন</b> ⬆️
• কমান্ড সীমা: <b>40/মিনিট</b> ⬆️
• 1 ডাউনলোড সর্বোচ্চ সময়: <b>4 ঘন্টা</b> ⬆️
• 🔞 NSFW কন্টেন্ট: সম্পূর্ণ মেটাডেটা সহ বিনামূল্যে 🆓
• 📢 গ্রুপের জন্য আমার চ্যানেলে সাবস্ক্রাইব করার প্রয়োজন নেই
• 👥 সমস্ত গ্রুপ সদস্যের পেইড ফাংশনে অ্যাক্সেস থাকবে!
• 🗒 আমার লগ-চ্যানেলে কোন লগ/ক্যাশ নেই! আপনি গ্রুপ সেটিংসে কপি/রিপোস্ট প্রত্যাখ্যান করতে পারেন</blockquote>

💬 <b>সাবটাইটেল সহ ভিডিওর জন্য 2️⃣x সীমা:</b>
<blockquote>• সর্বোচ্চ ভিডিও+সাবস সময়কাল: <b>3 ঘন্টা</b> ⬆️
• সর্বোচ্চ ভিডিও+সাবস ফাইল আকার: <b>1000 MB</b> ⬆️
• সর্বোচ্চ ভিডিও+সাবস গুণমান: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>মূল্য এবং সেটআপ:</b>
<blockquote>• মূল্য: গ্রুপে প্রতি 1 বটের জন্য <b>$5/মাস</b>
• সেটআপ: @iilililiiillliiliililliilliliiil এর সাথে যোগাযোগ করুন
• পেমেন্ট: 💎TON বা অন্যান্য পদ্ধতি💲
• সহায়তা: সম্পূর্ণ প্রযুক্তিগত সহায়তা অন্তর্ভুক্ত</blockquote>
————————————
আপনি বিনামূল্যে 🔞<b>NSFW</b> আনব্লক করতে এবং সমস্ত সীমা দ্বিগুণ (x2️⃣) করতে আপনার গ্রুপে আমার বটগুলি যোগ করতে পারেন।
আপনি চান যে আমি আপনার গ্রুপকে আমার বট ব্যবহার করার অনুমতি দিই তাহলে @iilililiiillliiliililliilliliiil এর সাথে যোগাযোগ করুন
————————————
💡<b>টিপ:</b> <blockquote>আপনি আপনার বন্ধুদের যেকোনো সংখ্যার সাথে টাকা যোগ করতে পারেন (উদাহরণস্বরূপ 100 জন) এবং পুরো গ্রুপের জন্য 1টি ক্রয় করতে পারেন - সমস্ত গ্রুপ সদস্যের সেই গ্রুপে সমস্ত বট ফাংশনে সম্পূর্ণ সীমাহীন অ্যাক্সেস থাকবে মাত্র <b>0.05$</b> এর জন্য</blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW মোড: চালু✅</b>

• NSFW কন্টেন্ট ব্লারিং ছাড়াই প্রদর্শিত হবে।
• স্পয়লার NSFW মিডিয়ায় প্রযোজ্য হবে না।
• কন্টেন্ট অবিলম্বে দৃশ্যমান হবে

<i>ব্লার সক্ষম করতে /nsfw off ব্যবহার করুন</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW মোড: বন্ধ</b>

⚠️ <b>ব্লার সক্ষম</b>
• NSFW কন্টেন্ট স্পয়লারের নীচে লুকানো থাকবে   
• দেখার জন্য, আপনাকে মিডিয়ায় ক্লিক করতে হবে
• স্পয়লার NSFW মিডিয়ায় প্রযোজ্য হবে।

<i>ব্লার অক্ষম করতে /nsfw on ব্যবহার করুন</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>অবৈধ প্যারামিটার</b>

ব্যবহার করুন:
• <code>/nsfw on</code> - ব্লার অক্ষম করুন
• <code>/nsfw off</code> - ব্লার সক্ষম করুন
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>ক্যাশ পরীক্ষা করা হচ্ছে...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 প্রক্রিয়াকরণ করা হচ্ছে..."
    DOWNLOADING_MSG = "📥 <b>মিডিয়া ডাউনলোড করা হচ্ছে...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>ইমেজ ডাউনলোড করা হচ্ছে...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>ডাউনলোড সম্পন্ন</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "ডাউনলোড করা হয়েছে:"
    SENT_STATUS_MSG = "পাঠানো হয়েছে:"
    PENDING_TO_SEND_STATUS_MSG = "পাঠানোর জন্য অপেক্ষা করছে:"
    TITLE_LABEL_MSG = "শিরোনাম:"
    MEDIA_COUNT_LABEL_MSG = "মিডিয়া সংখ্যা:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "ডাউনলোড সম্পন্ন, অডিও প্রক্রিয়াকরণ করা হচ্ছে..."
    VIDEO_PROCESSING_MSG = "📽 ভিডিও প্রক্রিয়াকরণ করা হচ্ছে..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>ক্যাশ থেকে পাঠানো হয়েছে</b>\n\nপাঠানো অ্যালবাম: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ ক্যাশ থেকে ভিডিও সফলভাবে পাঠানো হয়েছে।"
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ ক্যাশ থেকে প্লেলিস্ট ভিডিও পাঠানো হয়েছে ({cached}/{total} ফাইল)।"
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} ভিডিও ক্যাশ থেকে পাঠানো হয়েছে, অনুপস্থিতগুলি ডাউনলোড করা হচ্ছে..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ ক্যাশ থেকে পাঠানো হয়েছে: {cached}\n🔄 ডাউনলোড অব্যাহত..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 মিডিয়া বিশ্লেষণ করতে পারেনি, সর্বোচ্চ অনুমোদিত রেঞ্জ (1-{fallback_limit}) দিয়ে এগিয়ে যাচ্ছে..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 মিডিয়া সংখ্যা নির্ধারণ করতে পারেনি, সর্বোচ্চ অনুমোদিত রেঞ্জ (1-{total_limit}) দিয়ে এগিয়ে যাচ্ছে..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 মোট মিডিয়া সংখ্যা নির্ধারণ করতে পারেনি, নির্দিষ্ট রেঞ্জ {start}-{end} দিয়ে এগিয়ে যাচ্ছে..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>অবৈধ URL</b>\n\nঅনুগ্রহ করে http:// বা https:// দিয়ে শুরু একটি বৈধ URL প্রদান করুন"

    ERROR_OCCURRED_MSG = "❌ <b>ত্রুটি ঘটেছে</b>\n\n<code>{url}</code>\n\nত্রুটি: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ ভিডিও পাঠাতে ত্রুটি: {error}"
    ERROR_UNKNOWN_MSG = "❌ অজানা ত্রুটি: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ ভিডিও ডাউনলোড করার জন্য পর্যাপ্ত ডিস্ক স্পেস নেই।"
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ ফাইলের আকার {limit} GB সীমা অতিক্রম করেছে। অনুগ্রহ করে অনুমোদিত আকারের মধ্যে একটি ছোট ফাইল নির্বাচন করুন।"
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>সব উপলব্ধ প্রক্সি দিয়ে ভিডিও ডাউনলোড করতে ব্যর্থ</b>\n\nপ্রক্সির মাধ্যমে সব ডাউনলোড প্রচেষ্টা ব্যর্থ হয়েছে।\nচেষ্টা করুন:\n• প্রক্সির কার্যকারিতা পরীক্ষা করুন\n• তালিকা থেকে অন্য প্রক্সি চেষ্টা করুন\n• প্রক্সি ছাড়া ডাউনলোড করুন (যদি সম্ভব হয়)"

    ERROR_GETTING_LINK_MSG = "❌ <b>লিঙ্ক পাওয়ার ত্রুটি:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram বার্তা পাঠানোর সীমা নির্ধারণ করেছে।\n⏳ অনুগ্রহ করে অপেক্ষা করুন: {time}\nটাইমার আপডেট করতে URL আবার 2 বার পাঠান।"
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram বার্তা পাঠানোর সীমা নির্ধারণ করেছে।\n⏳ অনুগ্রহ করে অপেক্ষা করুন: \nটাইমার আপডেট করতে URL আবার 2 বার পাঠান।"
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ সাবটাইটেল ডাউনলোড করতে ব্যর্থ"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>সরাসরি স্ট্রিম লিঙ্ক</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>শিরোনাম:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>সময়কাল:</b> {duration} সেকেন্ড\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ ত্রুটি: মূল বার্তা পাওয়া যায়নি।"

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ ট্যাগ #{tag} এ নিষিদ্ধ অক্ষর রয়েছে। শুধুমাত্র অক্ষর, সংখ্যা এবং _ অনুমোদিত।\nঅনুগ্রহ করে ব্যবহার করুন: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ প্লেলিস্ট ভিডিও পাঠানো হয়েছে: {sent}/{total} ফাইল।"
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>প্লেলিস্ট টিপ</b>

আপনি একটি রেঞ্জ নির্দিষ্ট না করে প্লেলিস্ট লিঙ্ক পাঠিয়েছেন। বট স্বয়ংক্রিয়ভাবে প্রথম ভিডিও ডাউনলোড করেছে (<code>*1*1</code>).

<b>প্লেলিস্ট থেকে একাধিক ভিডিও ডাউনলোড করতে, একটি রেঞ্জ নির্দিষ্ট করুন:</b>
• <code>URL*1*5</code> — প্রথম 5টি ভিডিও (1 থেকে 5 পর্যন্ত অন্তর্ভুক্ত)
• <code>URL*3*3</code> — শুধুমাত্র 3য় ভিডিও
• <code>/vid 1-10 URL</code> — বিকল্প ফরম্যাট

আরও জানুন: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ ক্যাশ থেকে পাঠানো হয়েছে: {cached}/{total} ফাইল।"
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ স্ট্রিম লিঙ্ক পাওয়া যায়নি"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "কুকি ডাউনলোড করার জন্য একটি ব্রাউজার নির্বাচন করুন:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "এই সিস্টেমে কোন ব্রাউজার পাওয়া যায়নি। আপনি দূরবর্তী URL থেকে কুকি ডাউনলোড করতে পারেন বা ব্রাউজার স্ট্যাটাস মনিটর করতে পারেন:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>ব্রাউজার খুলুন</b> - মিনি-অ্যাপে ব্রাউজার স্ট্যাটাস মনিটর করতে"
    BROWSER_OPEN_BUTTON_MSG = "🌐 ব্রাউজার খুলুন"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 দূরবর্তী URL থেকে ডাউনলোড করুন"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ ফলব্যাকের মাধ্যমে YouTube কুকি ফাইল ডাউনলোড করা হয়েছে এবং cookie.txt হিসাবে সংরক্ষণ করা হয়েছে"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ কোন সমর্থিত ব্রাউজার পাওয়া যায়নি এবং কোন COOKIE_URL কনফিগার করা নেই। /cookie ব্যবহার করুন বা cookie.txt আপলোড করুন।"
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ ফলব্যাক COOKIE_URL অবশ্যই একটি .txt ফাইলের দিকে নির্দেশ করতে হবে।"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ ফলব্যাক কুকি ফাইল খুব বড় (>100KB)।"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ ফলব্যাক কুকি উৎস অনুপলব্ধ (স্ট্যাটাস {status})। /cookie চেষ্টা করুন বা cookie.txt আপলোড করুন।"
    COOKIE_FALLBACK_ERROR_MSG = "❌ ফলব্যাক কুকি ডাউনলোড করতে ত্রুটি। /cookie চেষ্টা করুন বা cookie.txt আপলোড করুন।"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ ফলব্যাক কুকি ডাউনলোডের সময় অপ্রত্যাশিত ত্রুটি।"
    BTN_CLOSE = "🔚বন্ধ"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ অবৈধ বুলিয়ান মান"
    ARGS_CLOSED_MSG = "বন্ধ"
    ARGS_ALL_RESET_MSG = "✅ সমস্ত আর্গুমেন্ট রিসেট করা হয়েছে"
    ARGS_RESET_ERROR_MSG = "❌ আর্গুমেন্ট রিসেট করতে ত্রুটি"
    ARGS_INVALID_PARAM_MSG = "❌ অবৈধ প্যারামিটার"
    ARGS_BOOL_SET_MSG = "{value} এ সেট করা হয়েছে"
    ARGS_BOOL_ALREADY_SET_MSG = "ইতিমধ্যে {value} এ সেট করা হয়েছে"
    ARGS_INVALID_SELECT_MSG = "❌ অবৈধ নির্বাচন মান"
    ARGS_VALUE_SET_MSG = "{value} এ সেট করা হয়েছে"
    ARGS_VALUE_ALREADY_SET_MSG = "ইতিমধ্যে {value} এ সেট করা হয়েছে"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>বর্তমান মান:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>উদাহরণ:</b>\n• <code>default</code> - ডিফল্ট XFF কৌশল ব্যবহার করুন\n• <code>never</code> - XFF হেডার কখনই ব্যবহার করবেন না\n• <code>US</code> - মার্কিন যুক্তরাষ্ট্র দেশ কোড\n• <code>GB</code> - যুক্তরাজ্য দেশ কোড\n• <code>DE</code> - জার্মানি দেশ কোড\n• <code>FR</code> - ফ্রান্স দেশ কোড\n• <code>JP</code> - জাপান দেশ কোড\n• <code>192.168.1.0/24</code> - IP ব্লক (CIDR)\n• <code>10.0.0.0/8</code> - প্রাইভেট IP রেঞ্জ\n• <code>203.0.113.0/24</code> - পাবলিক IP ব্লক\n\n"
    ARGS_XFF_NOTE_MSG = "<b>নোট:</b> এটি --geo-bypass বিকল্পগুলি প্রতিস্থাপন করে। CIDR নোটেশনে যেকোনো 2-অক্ষরের দেশ কোড বা IP ব্লক ব্যবহার করুন।\n\n"
    ARGS_EXAMPLE_MSG = "<b>উদাহরণ:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "অনুগ্রহ করে আপনার নতুন মান পাঠান।"
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>রেঞ্জ:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "অনুগ্রহ করে একটি সংখ্যা পাঠান।"
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>উদাহরণ:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>নোট:</b> এই হেডারগুলি বিদ্যমান Referer এবং User-Agent হেডারে যোগ করা হবে।\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 বর্তমান yt-dlp আর্গুমেন্ট:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>বুলিয়ান</b> - True/False সুইচ\n• 📋 <b>নির্বাচন</b> - বিকল্প থেকে বেছে নিন\n• 🔢 <b>সংখ্যাসূচক</b> - সংখ্যা ইনপুট\n• 📝🔧 <b>টেক্সট</b> - টেক্সট/JSON ইনপুট</blockquote>\n\nএই সেটিংসগুলি আপনার সমস্ত ডাউনলোডে প্রয়োগ করা হবে।"
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "IPv6 সংযোগ বাধ্য করুন",
        "force_ipv4": "IPv4 সংযোগ বাধ্য করুন", 
        "no_live_from_start": "শুরু থেকে লাইভ স্ট্রিম ডাউনলোড করবেন না",
        "live_from_start": "শুরু থেকে লাইভ স্ট্রিম ডাউনলোড করুন",
        "no_check_certificates": "HTTPS সার্টিফিকেট যাচাইকরণ দমন করুন",
        "check_certificate": "SSL সার্টিফিকেট পরীক্ষা করুন",
        "no_playlist": "শুধুমাত্র একক ভিডিও ডাউনলোড করুন, প্লেলিস্ট নয়",
        "embed_metadata": "ভিডিও ফাইলে মেটাডেটা এমবেড করুন",
        "embed_thumbnail": "ভিডিও ফাইলে থাম্বনেইল এমবেড করুন",
        "write_thumbnail": "থাম্বনেইল ফাইলে লিখুন",
        "ignore_errors": "ডাউনলোড ত্রুটি উপেক্ষা করুন এবং অব্যাহত রাখুন",
        "legacy_server_connect": "লেগাসি সার্ভার সংযোগ অনুমতি দিন",
        "concurrent_fragments": "ডাউনলোড করার জন্য সমবর্তী ফ্র্যাগমেন্টের সংখ্যা",
        "xff": "X-Forwarded-For হেডার কৌশল",
        "user_agent": "User-Agent হেডার",
        "impersonate": "ব্রাউজার অনুকরণ",
        "referer": "Referer হেডার",
        "geo_bypass": "ভৌগোলিক সীমাবদ্ধতা বাইপাস করুন",
        "hls_use_mpegts": "HLS এর জন্য MPEG-TS ব্যবহার করুন",
        "no_part": ".part ফাইল ব্যবহার করবেন না",
        "no_continue": "আংশিক ডাউনলোড পুনরায় শুরু করবেন না",
        "audio_format": "অডিও ফরম্যাট",
        "video_format": "ভিডিও ফরম্যাট",
        "merge_output_format": "আউটপুট ফরম্যাট মার্জ করুন",
        "send_as_file": "ফাইল হিসাবে পাঠান",
        "username": "ব্যবহারকারীর নাম",
        "password": "পাসওয়ার্ড",
        "twofactor": "দুই-ফ্যাক্টর প্রমাণীকরণ কোড",
        "min_filesize": "সর্বনিম্ন ফাইল আকার (MB)",
        "max_filesize": "সর্বোচ্চ ফাইল আকার (MB)",
        "playlist_items": "প্লেলিস্ট আইটেম",
        "date": "তারিখ",
        "datebefore": "তারিখের আগে",
        "dateafter": "তারিখের পরে",
        "http_headers": "HTTP হেডার",
        "sleep_interval": "স্লিপ ইন্টারভাল",
        "max_sleep_interval": "সর্বোচ্চ স্লিপ ইন্টারভাল",
        "retries": "পুনঃপ্রচেষ্টার সংখ্যা",
        "http_chunk_size": "HTTP চাঙ্ক আকার",
        "sleep_subtitles": "সাবটাইটেলের জন্য স্লিপ"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp আর্গুমেন্ট কনফিগারেশন</b>\n\n<blockquote>📋 <b>গ্রুপ:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp আর্গুমেন্ট কনফিগারেশন</b>\n\n"
        "<blockquote>📋 <b>গ্রুপ:</b>\n"
        "• ✅/❌ <b>বুলিয়ান</b> - True/False সুইচ\n"
        "• 📋 <b>নির্বাচন</b> - বিকল্প থেকে বেছে নিন\n"
        "• 🔢 <b>সংখ্যাসূচক</b> - সংখ্যা ইনপুট\n"
        "• 📝🔧 <b>টেক্সট</b> - টেক্সট/JSON ইনপুট</blockquote>\n\n"
        "এই সেটিংসগুলি আপনার সমস্ত ডাউনলোডে প্রয়োগ করা হবে।"
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ অনুগ্রহ করে অপেক্ষা করুন..."
    ERROR_OCCURRED_SHORT_MSG = "❌ ত্রুটি ঘটেছে"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ নিষ্ক্রিয়তার কারণে ইনপুট মোড স্বয়ংক্রিয়ভাবে বন্ধ হয়ে গেছে (5 মিনিট)।"
    ARGS_INPUT_DANGEROUS_MSG = "❌ ইনপুটে সম্ভাব্য বিপজ্জনক কন্টেন্ট রয়েছে: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ ইনপুট খুব দীর্ঘ (সর্বোচ্চ 1000 অক্ষর)"
    ARGS_INVALID_URL_MSG = "❌ অবৈধ URL ফরম্যাট। http:// বা https:// দিয়ে শুরু হতে হবে"
    ARGS_INVALID_JSON_MSG = "❌ অবৈধ JSON ফরম্যাট"
    ARGS_NUMBER_RANGE_MSG = "❌ সংখ্যাটি {min_val} এবং {max_val} এর মধ্যে হতে হবে"
    ARGS_INVALID_NUMBER_MSG = "❌ অবৈধ সংখ্যা ফরম্যাট"
    ARGS_DATE_FORMAT_MSG = "❌ তারিখ YYYYMMDD ফরম্যাটে হতে হবে (উদাহরণ: 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ বছর 1900 এবং 2100 এর মধ্যে হতে হবে"
    ARGS_MONTH_RANGE_MSG = "❌ মাস 01 এবং 12 এর মধ্যে হতে হবে"
    ARGS_DAY_RANGE_MSG = "❌ দিন 01 এবং 31 এর মধ্যে হতে হবে"
    ARGS_INVALID_DATE_MSG = "❌ অবৈধ তারিখ ফরম্যাট"
    ARGS_INVALID_XFF_MSG = "❌ XFF অবশ্যই 'default', 'never', দেশ কোড (উদাহরণ: US), বা IP ব্লক (উদাহরণ: 192.168.1.0/24) হতে হবে"
    ARGS_NO_CUSTOM_MSG = "কোন কাস্টম আর্গুমেন্ট সেট করা নেই। সমস্ত প্যারামিটার ডিফল্ট মান ব্যবহার করে।"
    ARGS_RESET_SUCCESS_MSG = "✅ সমস্ত আর্গুমেন্ট ডিফল্টে রিসেট করা হয়েছে।"
    ARGS_TEXT_TOO_LONG_MSG = "❌ টেক্সট খুব দীর্ঘ। সর্বোচ্চ 500 অক্ষর।"
    ARGS_ERROR_PROCESSING_MSG = "❌ ইনপুট প্রক্রিয়াকরণে ত্রুটি। অনুগ্রহ করে আবার চেষ্টা করুন।"
    ARGS_BOOL_INPUT_MSG = "❌ ফাইল হিসাবে পাঠান বিকল্পের জন্য 'True' বা 'False' লিখুন।"
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ অনুগ্রহ করে একটি বৈধ সংখ্যা প্রদান করুন।"
    ARGS_BOOL_VALUE_REQUEST_MSG = "এই বিকল্পটি সক্ষম/অক্ষম করতে অনুগ্রহ করে <code>True</code> বা <code>False</code> পাঠান।"
    ARGS_JSON_VALUE_REQUEST_MSG = "অনুগ্রহ করে বৈধ JSON পাঠান।"
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "আপনার এখনও কোন ট্যাগ নেই।"
    TAGS_MESSAGE_CLOSED_MSG = "ট্যাগ বার্তা বন্ধ করা হয়েছে।"
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ সাবটাইটেল অক্ষম করা হয়েছে এবং Always Ask মোড বন্ধ করা হয়েছে।"
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Always Ask সক্ষম করা হয়েছে।"
    SUBS_LANGUAGE_SET_MSG = "✅ সাবটাইটেল ভাষা সেট করা হয়েছে: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️সতর্কতা: উচ্চ CPU প্রভাবের কারণে এই ফাংশনটি খুব ধীর (প্রায় রিয়েল-টাইম) এবং সীমাবদ্ধ:\n"
        "- 720p সর্বোচ্চ গুণমান\n"
        "- 1.5 ঘন্টা সর্বোচ্চ সময়কাল\n"
        "- 500mb সর্বোচ্চ ভিডিও আকার</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>দ্রুত কমান্ড:</b>\n"
        "• <code>/subs off</code> - সাবটাইটেল অক্ষম করুন\n"
        "• <code>/subs on</code> - Always Ask মোড সক্ষম করুন\n"
        "• <code>/subs ru</code> - ভাষা সেট করুন\n"
        "• <code>/subs ru auto</code> - AUTO/TRANS সহ ভাষা সেট করুন"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 সাবটাইটেল অক্ষম করা হয়েছে"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} নির্বাচিত ভাষা: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 সাবটাইটেল ডাউনলোড করা হচ্ছে..."
    SUBS_DISABLED_ERROR_MSG = "❌ সাবটাইটেল অক্ষম করা হয়েছে। কনফিগার করতে /subs ব্যবহার করুন।"
    SUBS_YOUTUBE_ONLY_MSG = "❌ সাবটাইটেল ডাউনলোড শুধুমাত্র YouTube এর জন্য সমর্থিত।"
    SUBS_CAPTION_MSG = (
        "<b>💬 সাবটাইটেল</b>\n\n"
        "<b>ভিডিও:</b> {title}\n"
        "<b>ভাষা:</b> {lang}\n"
        "<b>ধরন:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 সাবটাইটেল SRT-ফাইল ব্যবহারকারীকে পাঠানো হয়েছে।"
    SUBS_ERROR_PROCESSING_MSG = "❌ সাবটাইটেল ফাইল প্রক্রিয়াকরণে ত্রুটি।"
    SUBS_ERROR_DOWNLOAD_MSG = "❌ সাবটাইটেল ডাউনলোড করতে ব্যর্থ।"
    SUBS_ERROR_MSG = "❌ সাবটাইটেল ডাউনলোড করতে ত্রুটি: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ বিভাজিত অংশের আকার সেট করা হয়েছে: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **অবৈধ আকার!**\n\n"
        "**বৈধ রেঞ্জ:** 100MB থেকে 2GB\n\n"
        "**বৈধ ফরম্যাট:**\n"
        "• `100mb` থেকে `2000mb` (মেগাবাইট)\n"
        "• `0.1gb` থেকে `2gb` (গিগাবাইট)\n\n"
        "**উদাহরণ:**\n"
        "• `/split 100mb` - 100 মেগাবাইট\n"
        "• `/split 500mb` - 500 মেগাবাইট\n"
        "• `/split 1.5gb` - 1.5 গিগাবাইট\n"
        "• `/split 2gb` - 2 গিগাবাইট\n"
        "• `/split 2000mb` - 2000 মেগাবাইট (2GB)\n\n"
        "**প্রিসেট:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **ভিডিও বিভাজনের জন্য সর্বোচ্চ অংশের আকার বেছে নিন:**\n\n"
        "**রেঞ্জ:** 100MB থেকে 2GB\n\n"
        "**দ্রুত কমান্ড:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**উদাহরণ:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "মেনু বন্ধ করা হয়েছে।"
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>বট সেটিংস</b>\n\nএকটি বিভাগ বেছে নিন:"
    SETTINGS_MENU_CLOSED_MSG = "মেনু বন্ধ করা হয়েছে।"
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 পরিষ্কার করার বিকল্প</b>\n\nকি পরিষ্কার করবেন তা বেছে নিন:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nএকটি ক্রিয়া বেছে নিন:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIA</b>\n\nএকটি ক্রিয়া বেছে নিন:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nএকটি ক্রিয়া বেছে নিন:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ আরও কমান্ড</b>\n\nএকটি ক্রিয়া বেছে নিন:"
    SETTINGS_COMMAND_EXECUTED_MSG = "কমান্ড কার্যকর করা হয়েছে।"
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Flood limit. পরে চেষ্টা করুন।"
    SETTINGS_HINT_SENT_MSG = "ইঙ্গিত পাঠানো হয়েছে।"
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "অনুসন্ধান সহায়ক খোলা হয়েছে।"
    SETTINGS_UNKNOWN_COMMAND_MSG = "অজানা কমান্ড।"
    SETTINGS_HINT_CLOSED_MSG = "ইঙ্গিত বন্ধ করা হয়েছে।"
    SETTINGS_HELP_SENT_MSG = "ব্যবহারকারীকে সাহায্য txt পাঠান"
    SETTINGS_MENU_OPENED_MSG = "/settings মেনু খোলা হয়েছে"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 অনুসন্ধান সহায়ক বন্ধ করা হয়েছে"
    SEARCH_CLOSED_MSG = "বন্ধ"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proxy {status}।"
    PROXY_ERROR_SAVING_MSG = "❌ Proxy সেটিংস সংরক্ষণ করতে ত্রুটি।"
    PROXY_MENU_TEXT_MSG = "সমস্ত yt-dlp অপারেশনের জন্য proxy সার্ভার ব্যবহার সক্ষম বা অক্ষম করবেন?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "সমস্ত yt-dlp অপারেশনের জন্য প্রক্সি সার্ভার ({config_count} + {file_count} উপলব্ধ) ব্যবহার করে সক্ষম বা নিষ্ক্রিয় করবেন?\n\nALL (AUTO) সক্ষম হলে, অনুমোদিত দেশ অনুযায়ী (YouTube ত্রুটিতে উল্লিখিত) প্রক্সি স্বয়ংক্রিয়ভাবে নির্বাচিত হয়।"
    PROXY_MENU_CLOSED_MSG = "মেনু বন্ধ করা হয়েছে।"
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy সক্ষম করা হয়েছে। সমস্ত yt-dlp অপারেশন proxy ব্যবহার করবে।"
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy সক্ষম করা হয়েছে। সমস্ত yt-dlp অপারেশন {method} নির্বাচন পদ্ধতি সহ {count} proxy সার্ভার ব্যবহার করবে।"

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ প্রক্সি চালু (YouTube ত্রুটিতে অটো)।\n\nYouTube যখন জিও-ব্লক ত্রুটি দেবে, বট শুধুমাত্র সেই ত্রুটিতে উল্লিখিত দেশগুলির প্রক্সি ব্যবহার করবে (সমস্ত প্রক্সি ধারাবাহিকভাবে চেষ্টা করা হবে না)।"
    PROXY_DISABLED_MSG = "❌ Proxy অক্ষম করা হয়েছে।"
    PROXY_TRYING_COUNTRY_MSG = "🔄 প্রক্সি চেষ্টা করা হচ্ছে: {country} ({current}/{total})"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Proxy সেটিংস সংরক্ষণ করতে ত্রুটি।"
    PROXY_ENABLED_CALLBACK_MSG = "Proxy সক্ষম করা হয়েছে।"
    PROXY_DISABLED_CALLBACK_MSG = "Proxy অক্ষম করা হয়েছে।"
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ আপনার পূর্ববর্তী ডাউনলোড শেষ না হওয়া পর্যন্ত অপেক্ষা করুন"
    AUDIO_HELP_MSG = (
        "<b>🎧 অডিও ডাউনলোড কমান্ড</b>\n\n"
        "ব্যবহার: <code>/audio URL</code>\n\n"
        "<b>উদাহরণ:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "এছাড়াও দেখুন: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "অডিও ইঙ্গিত বন্ধ করা হয়েছে।"
    PLAYLIST_HELP_CLOSED_MSG = "প্লেলিস্ট সাহায্য বন্ধ করা হয়েছে।"
    USERLOGS_CLOSED_MSG = "লগ বার্তা বন্ধ করা হয়েছে।"
    HELP_CLOSED_MSG = "সাহায্য বন্ধ করা হয়েছে।"
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW ব্লার সেটিংস</b>\n\nNSFW কন্টেন্ট <b>{status}</b>।\n\nNSFW কন্টেন্ট ব্লার করবেন কিনা বেছে নিন:"
    NSFW_MENU_CLOSED_MSG = "মেনু বন্ধ করা হয়েছে।"
    NSFW_BLUR_DISABLED_MSG = "NSFW ব্লার অক্ষম করা হয়েছে।"
    NSFW_BLUR_ENABLED_MSG = "NSFW ব্লার সক্ষম করা হয়েছে।"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW ব্লার অক্ষম করা হয়েছে।"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW ব্লার সক্ষম করা হয়েছে।"
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}।"
    MEDIAINFO_MENU_TITLE_MSG = "ডাউনলোড করা ফাইলের জন্য MediaInfo পাঠানো সক্ষম বা অক্ষম করবেন?"
    MEDIAINFO_MENU_CLOSED_MSG = "মেনু বন্ধ করা হয়েছে।"
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo সক্ষম করা হয়েছে। ডাউনলোডের পর, ফাইল তথ্য পাঠানো হবে।"
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo অক্ষম করা হয়েছে।"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo সক্ষম করা হয়েছে।"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo অক্ষম করা হয়েছে।"
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 উপলব্ধ ফরম্যাটের তালিকা</b>\n\n"
        "একটি URL এর জন্য উপলব্ধ ভিডিও/অডিও ফরম্যাট পান।\n\n"
        "<b>ব্যবহার:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>উদাহরণ:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 ফরম্যাট ID ব্যবহার করার 방법:</b>\n"
        "তালিকা পাওয়ার পর, নির্দিষ্ট ফরম্যাট ID ব্যবহার করুন:\n"
        "• <code>/format id 401</code> - ফরম্যাট 401 ডাউনলোড করুন\n"
        "• <code>/format id401</code> - উপরের মতোই\n"
        "• <code>/format id140 audio</code> - MP3 অডিও হিসাবে ফরম্যাট 140 ডাউনলোড করুন\n\n"
        "এই কমান্ডটি ডাউনলোড করা যায় এমন সমস্ত উপলব্ধ ফরম্যাট দেখাবে।"
    )
    LIST_PROCESSING_MSG = "🔄 উপলব্ধ ফরম্যাট পাওয়া হচ্ছে..."
    LIST_INVALID_URL_MSG = "❌ অনুগ্রহ করে http:// বা https:// দিয়ে শুরু একটি বৈধ URL প্রদান করুন"
    LIST_CAPTION_MSG = (
        "📃 এর জন্য উপলব্ধ ফরম্যাট:\n<code>{url}</code>\n\n"
        "💡 <b>ফরম্যাট সেট করার 방법:</b>\n"
        "• <code>/format id 134</code> - নির্দিষ্ট ফরম্যাট ID ডাউনলোড করুন\n"
        "• <code>/format 720p</code> - গুণমান দ্বারা ডাউনলোড করুন\n"
        "• <code>/format best</code> - সেরা গুণমান ডাউনলোড করুন\n"
        "• <code>/format ask</code> - সর্বদা গুণমানের জন্য জিজ্ঞাসা করুন\n\n"
        "{audio_note}\n"
        "📋 উপরের তালিকা থেকে ফরম্যাট ID ব্যবহার করুন"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>শুধুমাত্র অডিও ফরম্যাট:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - MP3 অডিও হিসাবে ফরম্যাট 140 ডাউনলোড করুন\n"
        "• <code>/format id140 audio</code> - উপরের মতোই\n"
        "এগুলি MP3 অডিও ফাইল হিসাবে ডাউনলোড করা হবে।\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ ফরম্যাট ফাইল পাঠাতে ত্রুটি: {error}"
    LIST_ERROR_GETTING_MSG = "❌ ফরম্যাট পাওয়া যায়নি:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ কমান্ড প্রক্রিয়াকরণের সময় একটি ত্রুটি ঘটেছে"
    LIST_ERROR_CALLBACK_MSG = "ত্রুটি ঘটেছে"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 ফরম্যাট ID ব্যবহার করার 방법:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "তালিকা পাওয়ার পর, নির্দিষ্ট ফরম্যাট ID ব্যবহার করুন:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - ফরম্যাট 401 ডাউনলোড করুন\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - উপরের মতোই\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - MP3 অডিও হিসাবে ফরম্যাট 140 ডাউনলোড করুন\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - উপরের মতোই\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 শুধুমাত্র অডিও ফরম্যাট সনাক্ত করা হয়েছে: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "এগুলি MP3 অডিও ফাইল হিসাবে ডাউনলোড করা হবে।\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>শুধুমাত্র ভিডিও ফরম্যাট:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 উপরের তালিকা থেকে ফরম্যাট ID ব্যবহার করুন"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>ব্যবহার:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>উদাহরণ:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - সেরা গুণমান\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p বা নিম্নতর\n"
        "• /link 720p https://youtube.com/watch?v=... - উপরের মতোই\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K বা নিম্নতর\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K বা নিম্নতর"
        "</blockquote>\n\n"
        "<b>গুণমান:</b> 1 থেকে 10000 (উদাহরণ: 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ অনুগ্রহ করে একটি বৈধ URL প্রদান করুন"
    LINK_PROCESSING_MSG = "🔗 সরাসরি লিঙ্ক পাওয়া হচ্ছে..."
    LINK_DURATION_MSG = "⏱ <b>সময়কাল:</b> {duration} সেকেন্ড\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>ভিডিও স্ট্রিম:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>অডিও স্ট্রিম:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **কীবোর্ড সেটিং আপডেট করা হয়েছে!**\n\nনতুন সেটিং: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **অবৈধ আর্গুমেন্ট!**\n\n"
        "বৈধ বিকল্প: `off`, `1x3`, `2x3`, `full`\n\n"
        "উদাহরণ: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **কীবোর্ড সেটিংস**\n\n"
        "বর্তমান: **{current}**\n\n"
        "একটি বিকল্প বেছে নিন:\n\n"
        "অথবা ব্যবহার করুন: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 কীবোর্ড সক্রিয় করা হয়েছে!"
    KEYBOARD_HIDDEN_MSG = "⌨️ কীবোর্ড লুকানো হয়েছে"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3 কীবোর্ড সক্রিয় করা হয়েছে!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3 কীবোর্ড সক্রিয় করা হয়েছে!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 ইমোজি কীবোর্ড সক্রিয় করা হয়েছে!"
    KEYBOARD_ERROR_APPLYING_MSG = "কীবোর্ড সেটিং {setting} প্রয়োগ করতে ত্রুটি: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ ফরম্যাট সেট করা হয়েছে: Always Ask। আপনি প্রতিবার URL পাঠালে গুণমানের জন্য জিজ্ঞাসা করা হবে।"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ ফরম্যাট সেট করা হয়েছে: Always Ask। এখন আপনি প্রতিবার URL পাঠালে গুণমানের জন্য জিজ্ঞাসা করা হবে।"
    FORMAT_BEST_UPDATED_MSG = "✅ ফরম্যাট সেরা গুণমান (AVC+MP4 অগ্রাধিকার) এ আপডেট করা হয়েছে:\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ ফরম্যাট ID {id} এ আপডেট করা হয়েছে:\n{format}\n\n💡 <b>নোট:</b> এটি যদি শুধুমাত্র অডিও ফরম্যাট হয়, তবে এটি MP3 অডিও ফাইল হিসাবে ডাউনলোড করা হবে।"
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ ফরম্যাট ID {id} (শুধুমাত্র অডিও) এ আপডেট করা হয়েছে:\n{format}\n\n💡 এটি MP3 অডিও ফাইল হিসাবে ডাউনলোড করা হবে।"
    FORMAT_QUALITY_UPDATED_MSG = "✅ ফরম্যাট গুণমান {quality} এ আপডেট করা হয়েছে:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ ফরম্যাট আপডেট করা হয়েছে:\n{format}"
    FORMAT_MENU_MSG = (
        "একটি ফরম্যাট বিকল্প নির্বাচন করুন বা ব্যবহার করে একটি কাস্টম পাঠান:\n"
        "• <code>/format &lt;format_string&gt;</code> - কাস্টম ফরম্যাট\n"
        "• <code>/format 720</code> - 720p গুণমান\n"
        "• <code>/format 4k</code> - 4K গুণমান\n"
        "• <code>/format 8k</code> - 8K গুণমান\n"
        "• <code>/format id 401</code> - নির্দিষ্ট ফরম্যাট ID\n"
        "• <code>/format ask</code> - সর্বদা মেনু দেখান\n"
        "• <code>/format best</code> - bv+ba/সেরা গুণমান"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "কাস্টম ফরম্যাট ব্যবহার করতে, নিম্নলিখিত ফরমে কমান্ড পাঠান:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "<code>bestvideo+bestaudio/best</code> কে আপনার পছন্দের ফরম্যাট স্ট্রিং দিয়ে প্রতিস্থাপন করুন।"
    )
    FORMAT_RESOLUTION_MENU_MSG = "আপনার পছন্দের রেজোলিউশন এবং কোডেক নির্বাচন করুন:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ ফরম্যাট সেট করা হয়েছে: Always Ask। এখন আপনি প্রতিবার URL পাঠালে গুণমানের জন্য জিজ্ঞাসা করা হবে।"
    FORMAT_UPDATED_MSG = "✅ ফরম্যাট আপডেট করা হয়েছে:\n{format}"
    FORMAT_SAVED_MSG = "✅ ফরম্যাট সংরক্ষণ করা হয়েছে।"
    FORMAT_CHOICE_UPDATED_MSG = "✅ ফরম্যাট পছন্দ আপডেট করা হয়েছে।"
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "কাস্টম ফরম্যাট মেনু বন্ধ করা হয়েছে"
    FORMAT_CODEC_SET_MSG = "✅ কোডেক {codec} এ সেট করা হয়েছে"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ ব্রাউজার পছন্দ আপডেট করা হয়েছে।"
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ অ্যাক্সেস অস্বীকার করা হয়েছে। শুধুমাত্র অ্যাডমিন।"
    ACCESS_DENIED_ADMIN = "❌ অ্যাক্সেস অস্বীকার করা হয়েছে। শুধুমাত্র অ্যাডমিন।"
    WELCOME_MASTER = "স্বাগতম মাস্টার 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ দুঃখিত... ডাউনলোডের সময় কিছু ত্রুটি ঘটেছে।"
    SIZE_LIMIT_EXCEEDED = "❌ ফাইলের আকার {max_size_gb} GB সীমা অতিক্রম করেছে। অনুগ্রহ করে অনুমোদিত আকারের মধ্যে একটি ছোট ফাইল নির্বাচন করুন।"
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ স্ক্রিপ্ট পাওয়া যায়নি: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ {script_path} ব্যবহার করে নতুন Firebase dump ডাউনলোড করা হচ্ছে ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase cache সফলভাবে পুনরায় লোড করা হয়েছে!"
    ADMIN_CACHE_FAILED_MSG = "❌ Firebase cache পুনরায় লোড করতে ব্যর্থ। {cache_file} বিদ্যমান কিনা পরীক্ষা করুন।"
    ADMIN_ERROR_RELOADING_MSG = "❌ ক্যাশ পুনরায় লোড করতে ত্রুটি: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ {script_path} চালাতে ত্রুটি:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ প্রমো বার্তা সমস্ত অন্যান্য ব্যবহারকারীকে পাঠানো হয়েছে</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ প্রমো বার্তা পাঠানো যায় না। একটি বার্তায় উত্তর দেওয়ার চেষ্টা করুন\nঅথবা কিছু ত্রুটি ঘটেছে</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ ব্যবহারকারী এখনও কোন কন্টেন্ট ডাউনলোড করেননি...</b> লগে বিদ্যমান নেই"
    ADMIN_INVALID_COMMAND_MSG = "❌ অবৈধ কমান্ড"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ <code>{{path}}</code> এর জন্য ক্যাশে কোন ডেটা পাওয়া যায়নি"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ Queue খালি — এখনও কেউ চ্যানেল ছেড়ে যায়নি।"
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>Ban queue</b>\nমোট অপেক্ষা করছে: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (ছেড়েছে: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… এবং {extra} আরও ব্যবহারকারী।"
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "ব্যবহার করুন /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ Queue থেকে ব্যবহারকারী ব্লক করা হয়েছে: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ Auto-blocking সক্ষম করা হয়েছে: নতুন ছেড়ে যাওয়া ব্যক্তিরা অবিলম্বে নিষিদ্ধ হবে।"
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ Auto-blocking অক্ষম করা হয়েছে।"
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ নির্ধারিত auto-block উইন্ডো প্রতি {interval} এ সেট করা হয়েছে।"
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 শেষ {hours} ঘন্টার (2 দিন) চ্যানেল কার্যকলাপ লগ।"
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 শেষ {hours} ঘন্টা (2 দিন): যোগদান করেছে {joined}, ছেড়েছে {left}।"
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ শেষ {hours} ঘন্টার (2 দিন) জন্য কোন কার্যকলাপ নেই।"
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "মোট: 🟢 {joined} যোগদান করেছে, 🔴 {left} ছেড়েছে।"
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ চ্যানেল কার্যকলাপ লগে অ্যাক্সেস নেই। বটগুলি admin লগ পড়তে পারে না। এই বৈশিষ্ট্যটি সক্ষম করতে config এ CHANNEL_GUARD_SESSION_STRING একটি ব্যবহারকারী সেশনের সাথে প্রদান করুন।"
    BAN_TIME_USAGE_MSG = "❌ ব্যবহার: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ 10s, 6m, 5h, 4d, 3w, 2M বা 1y এর মতো ফরম্যাট ব্যবহার করুন।"
    BAN_TIME_SET_MSG = "🕒 চ্যানেল লগ স্ক্যান ইন্টারভাল {interval} এ সেট করা হয়েছে।"
    BAN_TIME_REPORT_MSG = (
        "🛡️ চ্যানেল স্ক্যান রিপোর্ট\n"
        "চালানো হয়েছে: {run_ts}\n"
        "ইন্টারভাল: {interval}\n"
        "নতুন ছেড়ে যাওয়া: {new_leavers}\n"
        "Auto bans: {auto_banned}\n"
        "অপেক্ষা করছে: {pending}\n"
        "শেষ event_id: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ ব্যবহার: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Admin একজন admin মুছতে পারে না"
    ADMIN_USER_BLOCKED_MSG = "ব্যবহারকারী ব্লক করা হয়েছে 🔒❌\n \nID: <code>{user_id}</code>\nব্লক করা তারিখ: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> ইতিমধ্যে ব্লক করা হয়েছে ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 দুঃখিত! আপনি admin নন"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ ব্যবহার: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "ব্যবহারকারী আনব্লক করা হয়েছে 🔓✅\n \nID: <code>{user_id}</code>\nআনব্লক করা তারিখ: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> ইতিমধ্যে আনব্লক করা হয়েছে ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ আনব্লক করা ব্যবহারকারী: {count}\n⏱ টাইমস্ট্যাম্প: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ ব্যবহার: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "ব্যবহারকারী উপেক্ষা করা হয়েছে 👁️❌\n \nআইডি: <code>{user_id}</code>\nউপেক্ষা করা তারিখ: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> ইতিমধ্যে উপেক্ষা করা হয়েছে ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ ব্যবহার: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "ব্যবহারকারী আর উপেক্ষা করা হচ্ছে না 👁️✅\n \nআইডি: <code>{user_id}</code>\nউপেক্ষা না করার তারিখ: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> উপেক্ষা করা হচ্ছে না ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>বট চলমান সময় -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ অনুগ্রহ করে ক্যাশ পরিষ্কার করার জন্য একটি URL প্রদান করুন।\nব্যবহার: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ অনুগ্রহ করে একটি বৈধ URL প্রদান করুন।\nব্যবহার: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ URL এর জন্য ক্যাশ সফলভাবে পরিষ্কার করা হয়েছে:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ এই লিঙ্কের জন্য কোন ক্যাশ পাওয়া যায়নি।"
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ ক্যাশ পরিষ্কার করতে ত্রুটি: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ অ্যাক্সেস অস্বীকার করা হয়েছে। শুধুমাত্র অ্যাডমিন।"
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Porn list update script চালানো হচ্ছে: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ স্ক্রিপ্ট সফলভাবে সম্পন্ন হয়েছে!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ স্ক্রিপ্ট সফলভাবে সম্পন্ন হয়েছে!\n\nআউটপুট:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ স্ক্রিপ্ট return code {returncode} সহ ব্যর্থ হয়েছে:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ স্ক্রিপ্ট চালাতে ত্রুটি: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Porn এবং domain-সম্পর্কিত caches পুনরায় লোড করা হচ্ছে..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Porn caches সফলভাবে পুনরায় লোড করা হয়েছে!\n\n"
        "📊 বর্তমান ক্যাশ স্ট্যাটাস:\n"
        "• Porn domains: {porn_domains}\n"
        "• Porn keywords: {porn_keywords}\n"
        "• Supported sites: {supported_sites}\n"
        "• WHITELIST: {whitelist}\n"
        "• GREYLIST: {greylist}\n"
        "• BLACK_LIST: {black_list}\n"
        "• WHITE_KEYWORDS: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Porn cache পুনরায় লোড করতে ত্রুটি: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ অনুগ্রহ করে পরীক্ষা করার জন্য একটি URL প্রদান করুন।\nব্যবহার: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ অনুগ্রহ করে একটি বৈধ URL প্রদান করুন।\nব্যবহার: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 NSFW কন্টেন্টের জন্য URL পরীক্ষা করা হচ্ছে...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Porn Check Result</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>স্ট্যাটাস:</b> <b>{status_text}</b>\n\n"
        "<b>ব্যাখ্যা:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ URL পরীক্ষা করতে ত্রুটি: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "কুকি পরিষ্কার করা হয়েছে।"
    CLEAN_LOGS_CLEANED_MSG = "লগ পরিষ্কার করা হয়েছে।"
    CLEAN_TAGS_CLEANED_MSG = "ট্যাগ পরিষ্কার করা হয়েছে।"
    CLEAN_FORMAT_CLEANED_MSG = "ফরম্যাট পরিষ্কার করা হয়েছে।"
    CLEAN_SPLIT_CLEANED_MSG = "বিভাজন পরিষ্কার করা হয়েছে।"
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfo পরিষ্কার করা হয়েছে।"
    CLEAN_SUBS_CLEANED_MSG = "সাবটাইটেল সেটিংস পরিষ্কার করা হয়েছে।"
    CLEAN_KEYBOARD_CLEANED_MSG = "কীবোর্ড সেটিংস পরিষ্কার করা হয়েছে।"
    CLEAN_ARGS_CLEANED_MSG = "Args সেটিংস পরিষ্কার করা হয়েছে।"
    CLEAN_NSFW_CLEANED_MSG = "NSFW সেটিংস পরিষ্কার করা হয়েছে।"
    CLEAN_PROXY_CLEANED_MSG = "Proxy সেটিংস পরিষ্কার করা হয়েছে।"
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Flood wait সেটিংস পরিষ্কার করা হয়েছে।"
    CLEAN_ALL_CLEANED_MSG = "সমস্ত ফাইল পরিষ্কার করা হয়েছে।"
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nএকটি ক্রিয়া বেছে নিন:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Cookie ফাইল সংরক্ষণ করা হয়েছে"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ non-YouTube কুকির জন্য যাচাইকরণ এড়িয়ে যাওয়া হয়েছে"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Cookie ফাইল বিদ্যমান কিন্তু ভুল ফরম্যাট আছে"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Cookie ফাইল পাওয়া যায়নি।"
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 YouTube কুকি পরীক্ষা শুরু করা হচ্ছে...\n\nঅনুগ্রহ করে অপেক্ষা করুন যখন আমি আপনার কুকি পরীক্ষা এবং যাচাই করি।"
    COOKIES_YOUTUBE_WORKING_MSG = "✅ আপনার বিদ্যমান YouTube কুকি সঠিকভাবে কাজ করছে!\n\nনতুনগুলি ডাউনলোড করার প্রয়োজন নেই।"
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ আপনার বিদ্যমান YouTube কুকি মেয়াদ শেষ হয়ে গেছে বা অবৈধ।\n\n🔄 নতুন কুকি ডাউনলোড করা হচ্ছে..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} cookie উৎস কনফিগার করা নেই!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} cookie উৎস অবশ্যই একটি .txt ফাইল হতে হবে!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ রেঞ্জ সীমা অতিক্রম করেছে: {range_count} ফাইল অনুরোধ করা হয়েছে (সর্বোচ্চ {max_img_files})।\n\nসর্বোচ্চ উপলব্ধ ফাইল ডাউনলোড করতে এই কমান্ডগুলির মধ্যে একটি ব্যবহার করুন:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚বন্ধ"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ মিডিয়া সীমা অতিক্রম করেছে: {count} ফাইল অনুরোধ করা হয়েছে (সর্বোচ্চ {max_count})।\n\nসর্বোচ্চ উপলব্ধ ফাইল ডাউনলোড করতে এই কমান্ডগুলির মধ্যে একটি ব্যবহার করুন:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 লিঙ্ক থেকে <b>{count}</b> মিডিয়া আইটেম পাওয়া গেছে"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "ডাউনলোড রেঞ্জ নির্বাচন করুন:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "ব্রাউজার অনুকরণ"
    ARGS_REFERER_DESC_MSG = "Referer হেডার"
    ARGS_USER_AGENT_DESC_MSG = "User-Agent হেডার"
    ARGS_GEO_BYPASS_DESC_MSG = "ভৌগোলিক সীমাবদ্ধতা বাইপাস করুন"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "SSL সার্টিফিকেট পরীক্ষা করুন"
    ARGS_LIVE_FROM_START_DESC_MSG = "শুরু থেকে লাইভ স্ট্রিম ডাউনলোড করুন"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "শুরু থেকে লাইভ স্ট্রিম ডাউনলোড করবেন না"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "HLS ভিডিওর জন্য MPEG-TS কন্টেইনার ব্যবহার করুন"
    ARGS_NO_PLAYLIST_DESC_MSG = "শুধুমাত্র একক ভিডিও ডাউনলোড করুন, প্লেলিস্ট নয়"
    ARGS_NO_PART_DESC_MSG = ".part ফাইল ব্যবহার করবেন না"
    ARGS_NO_CONTINUE_DESC_MSG = "আংশিক ডাউনলোড পুনরায় শুরু করবেন না"
    ARGS_AUDIO_FORMAT_DESC_MSG = "এক্সট্র্যাকশনের জন্য অডিও ফরম্যাট"
    ARGS_EMBED_METADATA_DESC_MSG = "ভিডিও ফাইলে মেটাডেটা এমবেড করুন"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "ভিডিও ফাইলে থাম্বনেইল এমবেড করুন"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "থাম্বনেইল ফাইলে লিখুন"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "ডাউনলোড করার জন্য সমবর্তী ফ্র্যাগমেন্টের সংখ্যা"
    ARGS_FORCE_IPV4_DESC_MSG = "IPv4 সংযোগ বাধ্য করুন"
    ARGS_FORCE_IPV6_DESC_MSG = "IPv6 সংযোগ বাধ্য করুন"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For হেডার কৌশল"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP chunk আকার (বাইট)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "সাবটাইটেল ডাউনলোডের আগে স্লিপ (সেকেন্ড)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "লেগাসি সার্ভার সংযোগ অনুমতি দিন"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "HTTPS সার্টিফিকেট যাচাইকরণ দমন করুন"
    ARGS_USERNAME_DESC_MSG = "অ্যাকাউন্ট ব্যবহারকারীর নাম"
    ARGS_PASSWORD_DESC_MSG = "অ্যাকাউন্ট পাসওয়ার্ড"
    ARGS_TWOFACTOR_DESC_MSG = "দুই-ফ্যাক্টর প্রমাণীকরণ কোড"
    ARGS_IGNORE_ERRORS_DESC_MSG = "ডাউনলোড ত্রুটি উপেক্ষা করুন এবং অব্যাহত রাখুন"
    ARGS_MIN_FILESIZE_DESC_MSG = "সর্বনিম্ন ফাইল আকার (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "সর্বোচ্চ ফাইল আকার (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "ডাউনলোড করার প্লেলিস্ট আইটেম (উদাহরণ: 1,3,5 বা 1-5)"
    ARGS_DATE_DESC_MSG = "এই তারিখে আপলোড করা ভিডিও ডাউনলোড করুন (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "এই তারিখের আগে আপলোড করা ভিডিও ডাউনলোড করুন (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "এই তারিখের পরে আপলোড করা ভিডিও ডাউনলোড করুন (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "কাস্টম HTTP হেডার (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "অনুরোধের মধ্যে স্লিপ ইন্টারভাল (সেকেন্ড)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "সর্বোচ্চ স্লিপ ইন্টারভাল (সেকেন্ড)"
    ARGS_RETRIES_DESC_MSG = "পুনঃপ্রচেষ্টার সংখ্যা"
    ARGS_VIDEO_FORMAT_DESC_MSG = "ভিডিও কন্টেইনার ফরম্যাট"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "মার্জ করার জন্য আউটপুট কন্টেইনার ফরম্যাট"
    ARGS_SEND_AS_FILE_DESC_MSG = "সমস্ত মিডিয়া মিডিয়া হিসাবে নয়, ডকুমেন্ট হিসাবে পাঠান"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "অনুকরণ"
    ARGS_REFERER_SHORT_MSG = "রেফারার"
    ARGS_GEO_BYPASS_SHORT_MSG = "জিও বাইপাস"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "সার্টিফিকেট পরীক্ষা করুন"
    ARGS_LIVE_FROM_START_SHORT_MSG = "লাইভ শুরু"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "লাইভ শুরু নেই"
    ARGS_USER_AGENT_SHORT_MSG = "ইউজার এজেন্ট"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "প্লেলিস্ট নেই"
    ARGS_NO_PART_SHORT_MSG = "Part নেই"
    ARGS_NO_CONTINUE_SHORT_MSG = "Continue নেই"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "অডিও ফরম্যাট"
    ARGS_EMBED_METADATA_SHORT_MSG = "মেটা এমবেড করুন"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "থাম্ব এমবেড করুন"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "থাম্ব লিখুন"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "সমবর্তী"
    ARGS_FORCE_IPV4_SHORT_MSG = "IPv4 বাধ্য করুন"
    ARGS_FORCE_IPV6_SHORT_MSG = "IPv6 বাধ্য করুন"
    ARGS_XFF_SHORT_MSG = "XFF হেডার"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Chunk আকার"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "সাবস স্লিপ"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "লেগাসি সংযোগ"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "সার্টিফিকেট পরীক্ষা করবেন না"
    ARGS_USERNAME_SHORT_MSG = "ব্যবহারকারীর নাম"
    ARGS_PASSWORD_SHORT_MSG = "পাসওয়ার্ড"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "ত্রুটি উপেক্ষা করুন"
    ARGS_MIN_FILESIZE_SHORT_MSG = "সর্বনিম্ন আকার"
    ARGS_MAX_FILESIZE_SHORT_MSG = "সর্বোচ্চ আকার"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "প্লেলিস্ট আইটেম"
    ARGS_DATE_SHORT_MSG = "তারিখ"
    ARGS_DATEBEFORE_SHORT_MSG = "তারিখের আগে"
    ARGS_DATEAFTER_SHORT_MSG = "তারিখের পরে"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP হেডার"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "স্লিপ ইন্টারভাল"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "সর্বোচ্চ স্লিপ"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "ভিডিও ফরম্যাট"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "মার্জ ফরম্যাট"
    ARGS_SEND_AS_FILE_SHORT_MSG = "ফাইল হিসাবে পাঠান"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ ফাইলটি খুব বড়। সর্বোচ্চ আকার 100 KB।"
    COOKIES_INVALID_FORMAT_MSG = "❌ শুধুমাত্র .txt ফরম্যাটের ফাইল অনুমোদিত।"
    COOKIES_INVALID_COOKIE_MSG = "❌ ফাইলটি cookie.txt এর মতো দেখাচ্ছে না (কোন '# Netscape HTTP Cookie File' লাইন নেই)।"
    COOKIES_ERROR_READING_MSG = "❌ ফাইল পড়তে ত্রুটি: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Cookie ফাইল বিদ্যমান এবং সঠিক ফরম্যাট আছে"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} cookie ফাইল খুব বড়! সর্বোচ্চ 100KB, পাওয়া গেছে {size}KB।"
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} cookie ফাইল ডাউনলোড করা হয়েছে এবং আপনার ফোল্ডারে cookie.txt হিসাবে সংরক্ষণ করা হয়েছে।</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} cookie উৎস অনুপলব্ধ (স্ট্যাটাস {status})। অনুগ্রহ করে পরে আবার চেষ্টা করুন।"
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ {service} cookie ফাইল ডাউনলোড করতে ত্রুটি। অনুগ্রহ করে পরে আবার চেষ্টা করুন।"
    COOKIES_USER_PROVIDED_MSG = "<b>✅ ব্যবহারকারী একটি নতুন cookie ফাইল প্রদান করেছেন।</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie সফলভাবে আপডেট করা হয়েছে:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ বৈধ cookie নয়।</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube cookie উৎস কনফিগার করা নেই!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 YouTube কুকি ডাউনলোড এবং পরীক্ষা করা হচ্ছে...\n\nচেষ্টা {attempt} এর {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ অ্যাক্সেস অস্বীকার করা হয়েছে। শুধুমাত্র অ্যাডমিন।"
    ADMIN_USER_LOGS_TOTAL_MSG = "মোট: <b>{total}</b>\n<b>{user_id}</b> - লগ (শেষ 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 কীবোর্ড সক্রিয় করা হয়েছে!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ সাবটাইটেল ভাষা সেট করা হয়েছে: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ সাবটাইটেল ভাষা সেট করা হয়েছে: {flag} {name} AUTO/TRANS সক্ষম সহ।"
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "সাবটাইটেল ভাষা মেনু বন্ধ করা হয়েছে।"
    SUBS_DOWNLOADING_MSG = "💬 সাবটাইটেল ডাউনলোড করা হচ্ছে..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 মেমরিতে Firebase cache পুনরায় লোড করা হচ্ছে..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ কোন COOKIE_URL কনফিগার করা নেই। /cookie ব্যবহার করুন বা cookie.txt আপলোড করুন।"
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 দূরবর্তী URL থেকে কুকি ডাউনলোড করা হচ্ছে..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ ফলব্যাক COOKIE_URL অবশ্যই একটি .txt ফাইলের দিকে নির্দেশ করতে হবে।"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ ফলব্যাক cookie ফাইল খুব বড় (>100KB)।"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie ফাইল ফলব্যাকের মাধ্যমে ডাউনলোড করা হয়েছে এবং cookie.txt হিসাবে সংরক্ষণ করা হয়েছে"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ ফলব্যাক cookie উৎস অনুপলব্ধ (স্ট্যাটাস {status})। /cookie ব্যবহার করুন বা cookie.txt আপলোড করুন।"
    COOKIE_FALLBACK_ERROR_MSG = "❌ ফলব্যাক cookie ডাউনলোড করতে ত্রুটি। /cookie ব্যবহার করুন বা cookie.txt আপলোড করুন।"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ ফলব্যাক cookie ডাউনলোডের সময় অপ্রত্যাশিত ত্রুটি।"
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} ব্রাউজার ইনস্টল করা নেই।"
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ ব্রাউজার ব্যবহার করে কুকি সংরক্ষণ করা হয়েছে: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ কুকি সংরক্ষণ করতে ব্যর্থ: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube কুকি সঠিকভাবে কাজ করছে"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube কুকি মেয়াদ শেষ হয়ে গেছে বা অবৈধ\n\nনতুন কুকি পেতে /cookie ব্যবহার করুন"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - কাস্টম ফরম্যাট\n• <code>/format 720</code> - 720p মান\n• <code>/format 4k</code> - 4K মান"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "ইঙ্গিত পাঠানো হয়েছে।"
    FORMAT_MKV_TOGGLE_MSG = "MKV এখন {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ কোন দূরবর্তী URL কনফিগার করা নেই"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ অবৈধ ফাইল ফরম্যাট"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ ফাইল খুব বড়"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ কুকি সফলভাবে ডাউনলোড করা হয়েছে"
    COOKIES_SERVER_ERROR_MSG = "❌ সার্ভার ত্রুটি {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ ডাউনলোড ব্যর্থ"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ অপ্রত্যাশিত ত্রুটি"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ ব্রাউজার ইনস্টল করা নেই।"
    COOKIES_MENU_CLOSED_MSG = "মেনু বন্ধ করা হয়েছে।"
    COOKIES_HINT_CLOSED_MSG = "Cookie ইঙ্গিত বন্ধ করা হয়েছে।"
    IMG_HELP_CLOSED_MSG = "সাহায্য বন্ধ করা হয়েছে।"
    SUBS_LANGUAGE_UPDATED_MSG = "সাবটাইটেল ভাষা সেটিংস আপডেট করা হয়েছে।"
    SUBS_MENU_CLOSED_MSG = "সাবটাইটেল ভাষা মেনু বন্ধ করা হয়েছে।"
    KEYBOARD_SET_TO_MSG = "কীবোর্ড সেট করা হয়েছে {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "সেটিং প্রক্রিয়াকরণে ত্রুটি"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo সক্ষম করা হয়েছে।"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo অক্ষম করা হয়েছে।"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW blur অক্ষম করা হয়েছে।"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW blur সক্ষম করা হয়েছে।"
    SETTINGS_MENU_CLOSED_MSG = "মেনু বন্ধ করা হয়েছে।"
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Flood wait সক্রিয়। পরে চেষ্টা করুন।"
    OTHER_HELP_CLOSED_MSG = "সাহায্য বন্ধ করা হয়েছে।"
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "লগ বার্তা বন্ধ করা হয়েছে।"
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "মেনু বন্ধ করা হয়েছে।"
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "অবৈধ আকার।"
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ MediaInfo পাঠাতে ত্রুটি: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ একটি ত্রুটি ঘটেছে: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - সমস্ত লগ"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - সমস্ত {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 দূরবর্তী URL থেকে ডাউনলোড করুন"
    BROWSER_OPEN_BUTTON_MSG = "🌐 ব্রাউজার খুলুন"
    SELECT_BROWSER_MSG = "কুকি ডাউনলোড করার জন্য একটি ব্রাউজার নির্বাচন করুন:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "এই সিস্টেমে কোন ব্রাউজার পাওয়া যায়নি। আপনি দূরবর্তী URL থেকে কুকি ডাউনলোড করতে পারেন বা ব্রাউজার স্ট্যাটাস পর্যবেক্ষণ করতে পারেন:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>ব্রাউজার খুলুন</b> - mini-app এ ব্রাউজার স্ট্যাটাস পর্যবেক্ষণ করতে"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ /check_cookie চালাতে ব্যর্থ"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Flood limit। পরে চেষ্টা করুন।"
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ ব্রাউজার cookie মেনু খুলতে ব্যর্থ"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Cookie হিসাবে সংরক্ষণ করুন ইঙ্গিত বন্ধ করা হয়েছে।"
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>ব্যবহার:</b>\n<code>/link [quality] URL</code>\n\n<b>উদাহরণ:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - সেরা মান\n• /link 720 https://youtube.com/watch?v=... - 720p বা নিম্নতর\n• /link 720p https://youtube.com/watch?v=... - উপরের মতো\n• /link 4k https://youtube.com/watch?v=... - 4K বা নিম্নতর\n• /link 8k https://youtube.com/watch?v=... - 8K বা নিম্নতর</blockquote>\n\n<b>মান:</b> 1 থেকে 10000 (উদাহরণ: 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K মান"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>সরাসরি লিঙ্ক পাওয়া গেছে</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>ফরম্যাট:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>অডিও স্ট্রিম:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ স্ট্রিম লিঙ্ক পাওয়া যায়নি"
    LINK_ERROR_GETTING_MSG = "❌ <b>লিঙ্ক পাওয়ার সময় ত্রুটি:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ অবৈধ YouTube cookie সূচক: {selected_index}। উপলব্ধ পরিসীমা হল 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 YouTube কুকি ডাউনলোড এবং পরীক্ষা করা হচ্ছে...\n\nচেষ্টা {attempt} এর {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 YouTube কুকি ডাউনলোড এবং পরীক্ষা করা হচ্ছে...\n\nচেষ্টা {attempt} এর {total}\n🔍 কুকি পরীক্ষা করা হচ্ছে..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube কুকি সফলভাবে ডাউনলোড এবং যাচাই করা হয়েছে!\n\nব্যবহৃত উৎস {source} এর {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ সমস্ত YouTube কুকি মেয়াদ শেষ হয়ে গেছে বা অনুপলব্ধ!\n\nসেগুলি প্রতিস্থাপনের জন্য বট প্রশাসকের সাথে যোগাযোগ করুন।"
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube cookie পুনঃপ্রচেষ্টা সীমা অতিক্রম করেছে!\n\n🔢 সর্বোচ্চ: প্রতি ঘন্টায় {limit} চেষ্টা\n⏰ অনুগ্রহ করে পরে আবার চেষ্টা করুন"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ ট্যাগ #{wrong} এ নিষিদ্ধ অক্ষর রয়েছে। শুধুমাত্র অক্ষর, সংখ্যা এবং _ অনুমোদিত।\nঅনুগ্রহ করে ব্যবহার করুন: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **অবৈধ যুক্তি!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ সাবটাইটেল ভাষা সেট করা হয়েছে: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "উদাহরণ: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} নির্বাচিত ভাষা: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Always Ask মোড {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 সাবটাইটেল অক্ষম করা হয়েছে"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 সাবটাইটেল সেটিংস</b>\n\n{status_text}\n\nসাবটাইটেল ভাষা নির্বাচন করুন:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - সাবটাইটেল অক্ষম করুন\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 সাবটাইটেল সেটিংস</b>\n\n{status_text}\n\nসাবটাইটেল ভাষা নির্বাচন করুন:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>শিরোনাম:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>সময়কাল:</b> {duration} সেকেন্ড\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>ভিডিও স্ট্রিম:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 720p সর্বোচ্চ মান\n- 1.5 ঘন্টা সর্বোচ্চ সময়কাল\n- 500mb সর্বোচ্চ ভিডিও আকার</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️সতর্কতা: উচ্চ CPU প্রভাবের কারণে এই ফাংশনটি খুব ধীর (প্রায় রিয়েল-টাইম) এবং সীমাবদ্ধ:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>দ্রুত কমান্ড:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - সাবটাইটেল অক্ষম করুন\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - Always Ask মোড সক্ষম করুন\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - ভাষা সেট করুন\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - AUTO/TRANS সক্ষম সহ ভাষা সেট করুন\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - Always Ask মোড সক্ষম করুন\n"
    SUBS_AUTO_SUBS_TEXT = " (auto-subs)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Auto-subs মোড {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "কমান্ডের মাধ্যমে SUBS অক্ষম করা হয়েছে: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "কমান্ডের মাধ্যমে SUBS Always Ask সক্ষম করা হয়েছে: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "কমান্ডের মাধ্যমে SUBS ভাষা সেট করা হয়েছে: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "কমান্ডের মাধ্যমে SUBS ভাষা + auto মোড সেট করা হয়েছে: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "ব্যবহারকারী /subs মেনু খুলেছেন।"
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "ব্যবহারকারী সাবটাইটেল ভাষা সেট করেছেন: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "ব্যবহারকারী AUTO/TRANS মোড টগল করেছেন: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "ব্যবহারকারী Always Ask মোড টগল করেছেন: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "ব্যবহারকারী ব্রাউজার থেকে কুকি অনুরোধ করেছেন।"
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "শুধুমাত্র ইনস্টল করা ব্রাউজার সহ ব্রাউজার নির্বাচন কীবোর্ড পাঠানো হয়েছে।"
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "ব্রাউজার নির্বাচন বন্ধ করা হয়েছে।"
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "ফলব্যাক COOKIE_URL সফলভাবে ব্যবহার করা হয়েছে (উৎস লুকানো)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "ফলব্যাক COOKIE_URL ব্যর্থ: status={status} (লুকানো)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "ফলব্যাক COOKIE_URL অপ্রত্যাশিত ত্রুটি: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "ব্রাউজার {browser} ইনস্টল করা নেই।"
    COOKIES_SAVED_BROWSER_LOG_MSG = "ব্রাউজার ব্যবহার করে কুকি সংরক্ষণ করা হয়েছে: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য Cookie ফাইল সংরক্ষণ করা হয়েছে।"
    COOKIES_FILE_WORKING_LOG_MSG = "Cookie ফাইল বিদ্যমান, সঠিক ফরম্যাট আছে, এবং YouTube কুকি কাজ করছে।"
    COOKIES_FILE_EXPIRED_LOG_MSG = "Cookie ফাইল বিদ্যমান এবং সঠিক ফরম্যাট আছে, কিন্তু YouTube কুকি মেয়াদ শেষ হয়ে গেছে।"
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Cookie ফাইল বিদ্যমান এবং সঠিক ফরম্যাট আছে।"
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Cookie ফাইল বিদ্যমান কিন্তু ভুল ফরম্যাট আছে।"
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Cookie ফাইল পাওয়া যায়নি।"
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {service} cookie URL খালি।"
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} cookie URL .txt নয় (লুকানো)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} cookie ফাইল খুব বড়: {size} বাইট (উৎস লুকানো)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {service} cookie ফাইল ডাউনলোড করা হয়েছে (উৎস লুকানো)।"
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "স্ক্রিপ্ট পাওয়া যায়নি: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "প্রাথমিক স্ট্যাটাস বার্তা পাঠাতে ব্যর্থ"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "{script_path} চালাতে ত্রুটি: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "অটো টাস্ক দ্বারা Firebase cache পুনরায় লোড করা হয়েছে।"
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "অ্যাডমিন দ্বারা Firebase cache পুনরায় লোড করা হয়েছে।"
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Firebase cache পুনরায় লোড করতে ত্রুটি: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "ব্রডকাস্ট শুরু করা হয়েছে। পাঠ্য:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "সমস্ত ব্যবহারকারীর কাছে ব্রডকাস্ট বার্তা পাঠানো হয়েছে।"
    ADMIN_BROADCAST_FAILED_LOG_MSG = "ব্রডকাস্ট বার্তা পাঠাতে ব্যর্থ: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "অ্যাডমিন {user_id} URL এর জন্য cache সাফ করেছেন: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "অ্যাডমিন {user_id} পর্ন তালিকা আপডেট স্ক্রিপ্ট শুরু করেছেন: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "অ্যাডমিন {user_id} দ্বারা পর্ন তালিকা আপডেট স্ক্রিপ্ট সফলভাবে সম্পন্ন হয়েছে"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "অ্যাডমিন {user_id} দ্বারা পর্ন তালিকা আপডেট স্ক্রিপ্ট ব্যর্থ হয়েছে: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "অ্যাডমিন {user_id} অস্তিত্বহীন স্ক্রিপ্ট চালানোর চেষ্টা করেছেন: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "অ্যাডমিন {user_id} দ্বারা পর্ন আপডেট স্ক্রিপ্ট চালাতে ত্রুটি: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "অ্যাডমিন {user_id} পর্ন cache পুনরায় লোড শুরু করেছেন"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "অ্যাডমিন {user_id} দ্বারা পর্ন cache পুনরায় লোড করতে ত্রুটি: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "অ্যাডমিন {user_id} NSFW এর জন্য URL পরীক্ষা করেছেন: {url} - ফলাফল: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "ব্যবহারকারী ফরম্যাট পরিবর্তন অনুরোধ করেছেন।"
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "ফরম্যাট ALWAYS_ASK এ সেট করা হয়েছে।"
    FORMAT_UPDATED_BEST_LOG_MSG = "ফরম্যাট সেরা তে আপডেট করা হয়েছে: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "ফরম্যাট ID {format_id} এ আপডেট করা হয়েছে: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "ফরম্যাট ID {format_id} এ আপডেট করা হয়েছে (শুধুমাত্র অডিও): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "ফরম্যাট মান {quality} এ আপডেট করা হয়েছে: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "ফরম্যাট আপডেট করা হয়েছে: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "ফরম্যাট মেনু পাঠানো হয়েছে।"
    FORMAT_SELECTION_CLOSED_LOG_MSG = "ফরম্যাট নির্বাচন বন্ধ করা হয়েছে।"
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "কাস্টম ফরম্যাট ইঙ্গিত পাঠানো হয়েছে।"
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "ফরম্যাট রেজোলিউশন মেনু পাঠানো হয়েছে।"
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "মূল ফরম্যাট মেনুতে ফিরে যাওয়া হয়েছে।"
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "ফরম্যাট আপডেট করা হয়েছে: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "ফরম্যাট ALWAYS_ASK এ সেট করা হয়েছে।"
    FORMAT_CODEC_SET_LOG_MSG = "কোডেক পছন্দ {codec} এ সেট করা হয়েছে"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "কাস্টম ফরম্যাট মেনু বন্ধ করা হয়েছে"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {url} থেকে সরাসরি লিঙ্ক এক্সট্র্যাক্ট করা হয়েছে"
    LINK_EXTRACTION_FAILED_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {url} থেকে সরাসরি লিঙ্ক এক্সট্র্যাক্ট করতে ব্যর্থ: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য link কমান্ডে ত্রুটি: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "ব্যবহারকারী {user_id} কীবোর্ড সেট করেছেন {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "ব্যবহারকারী {user_id} কীবোর্ড সেট করেছেন {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "কমান্ডের মাধ্যমে MediaInfo সেট করা হয়েছে: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "ব্যবহারকারী /mediainfo মেনু খুলেছেন।"
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: বন্ধ করা হয়েছে।"
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo সক্ষম করা হয়েছে।"
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo অক্ষম করা হয়েছে।"
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "যুক্তির মাধ্যমে Split আকার {size} বাইটে সেট করা হয়েছে।"
    SPLIT_MENU_OPENED_LOG_MSG = "ব্যবহারকারী /split মেনু খুলেছেন।"
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Split নির্বাচন বন্ধ করা হয়েছে।"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Split আকার {size} বাইটে সেট করা হয়েছে।"
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "কমান্ডের মাধ্যমে Proxy সেট করা হয়েছে: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "ব্যবহারকারী /proxy মেনু খুলেছেন।"
    PROXY_MENU_CLOSED_LOG_MSG = "Proxy: বন্ধ করা হয়েছে।"
    PROXY_ENABLED_LOG_MSG = "Proxy সক্ষম করা হয়েছে।"
    PROXY_DISABLED_LOG_MSG = "Proxy অক্ষম করা হয়েছে।"
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "সাহায্য বার্তা বন্ধ করা হয়েছে।"
    AUDIO_HELP_SHOWN_LOG_MSG = "/audio সাহায্য দেখানো হয়েছে"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "ব্যবহারকারী প্লেলিস্ট সাহায্য অনুরোধ করেছেন।"
    PLAYLIST_HELP_CLOSED_LOG_MSG = "প্লেলিস্ট সাহায্য বন্ধ করা হয়েছে।"
    AUDIO_HINT_CLOSED_LOG_MSG = "অডিও ইঙ্গিত বন্ধ করা হয়েছে।"
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {url} থেকে LINK বাটনের মাধ্যমে সরাসরি লিঙ্ক মেনু তৈরি করা হয়েছে"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {url} থেকে LINK বাটনের মাধ্যমে সরাসরি লিঙ্ক এক্সট্র্যাক্ট করতে ব্যর্থ: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য LIST কমান্ড চালানো হয়েছে, url: {url}"
    QUICK_EMBED_LOG_MSG = "Quick Embed: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "{url} এর জন্য Always Ask মেনু পাঠানো হয়েছে"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "ত্রুটির পরে ব্যবহারকারী {user_id} এর জন্য ক্যাশ করা মান মেনু তৈরি করা হয়েছে: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "{url} এর জন্য Always Ask মেনু ত্রুটি: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "ফরম্যাট /args সেটিংসের মাধ্যমে স্থির করা হয়েছে"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "অডিও"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "ভিডিও"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "ভিডিও"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "পরবর্তী ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ পূর্ববর্তী"
    SUBTITLES_NEXT_BUTTON_MSG = "পরবর্তী ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ সমস্ত পাঠ্য ক্ষেত্র খালি"
    SENDER_VIDEO_DURATION_MSG = "ভিডিও সময়কাল:"
    SENDER_UPLOADING_FILE_MSG = "📤 ফাইল আপলোড করা হচ্ছে..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 ভিডিও আপলোড করা হচ্ছে..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 ভিডিও সময়কাল:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1টি ফাইল আপলোড করা হয়েছে।"
    DOWN_UP_VIDEO_INFO_MSG = "📋 ভিডিও তথ্য"
    DOWN_UP_NUMBER_MSG = "সংখ্যা"
    DOWN_UP_TITLE_MSG = "শিরোনাম"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ ভিডিও ডাউনলোড করা হয়েছে।"
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 আপলোডের জন্য প্রক্রিয়াকরণ করা হচ্ছে..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 বিভক্ত অংশ {part} ফাইল আপলোড করা হয়েছে"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ আপলোড সম্পন্ন"
    DOWN_UP_FILES_UPLOADED_MSG = "ফাইল আপলোড করা হয়েছে"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 বন্ধ করুন"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼কোডেক"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 ডাব"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 সাবটাইটেল"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 ব্রাউজার"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 সরাসরি লিঙ্ক পাওয়া হচ্ছে..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 উপলব্ধ ফরম্যাট পাওয়া হচ্ছে..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 ভিডিও বিবরণ পাওয়া হচ্ছে..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ বিবরণ পাওয়ার সময় ত্রুটি: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ ভিডিও বিবরণ উপলব্ধ নয়"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ বিবরণ পাঠানোর সময় ত্রুটি: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 ভিডিও বিবরণ ব্যবহারকারী {user_id} কে {url} ({title}) এর জন্য পাঠানো হয়েছে"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 gallery-dl শুরু করা হচ্ছে…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>সময়কাল:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>ফরম্যাট:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Browser:</b> ওয়েব ব্রাউজারে খুলুন"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "এর জন্য উপলব্ধ ফরম্যাট"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 ফরম্যাট ID ব্যবহার করার 방법:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "তালিকা পাওয়ার পরে, নির্দিষ্ট ফরম্যাট ID ব্যবহার করুন:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - ফরম্যাট 401 ডাউনলোড করুন"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - উপরের মতো"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - MP3 অডিও হিসাবে ফরম্যাট 140 ডাউনলোড করুন"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 শুধুমাত্র অডিও ফরম্যাট সনাক্ত করা হয়েছে"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "এই ফরম্যাটগুলি MP3 অডিও ফাইল হিসাবে ডাউনলোড করা হবে।"
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>ফরম্যাট সেট করার 방법:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - নির্দিষ্ট ফরম্যাট ID ডাউনলোড করুন"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - মান অনুযায়ী ডাউনলোড করুন"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - সেরা মান ডাউনলোড করুন"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - সর্বদা মানের জন্য জিজ্ঞাসা করুন"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>শুধুমাত্র অডিও ফরম্যাট:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - MP3 অডিও হিসাবে ফরম্যাট 140 ডাউনলোড করুন"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "এগুলি MP3 অডিও ফাইল হিসাবে ডাউনলোড করা হবে।"
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 উপরের তালিকা থেকে ফরম্যাট ID ব্যবহার করুন"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ ত্রুটি: মূল বার্তা পাওয়া যায়নি।"
    ALWAYS_ASK_FORMATS_PAGE_MSG = "ফরম্যাট পৃষ্ঠা"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ ফরম্যাট মেনু দেখাতে ত্রুটি"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ ফরম্যাট পাওয়ার সময় ত্রুটি"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ উপলব্ধ ফরম্যাট পাওয়ার সময় ত্রুটি।"
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "অনুগ্রহ করে পরে আবার চেষ্টা করুন।"
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp এই কন্টেন্ট প্রক্রিয়া করতে পারে না"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "সিস্টেম পরিবর্তে gallery-dl ব্যবহার করার পরামর্শ দেয়।"
    ALWAYS_ASK_OPTIONS_MSG = "**বিকল্প:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• ছবির গ্যালারির জন্য: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• একক ছবির জন্য: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl প্রায়ই Instagram, Twitter এবং অন্যান্য সোশ্যাল মিডিয়া কন্টেন্টের জন্য ভাল কাজ করে।"
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Gallery-dl চেষ্টা করুন"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 /args এর মাধ্যমে ফরম্যাট স্থির করা হয়েছে"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 সাবটাইটেল"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 ডাব করা অডিও"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — সাবটাইটেল উপলব্ধ"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — সাবটাইটেল ভাষা নির্বাচন করুন"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ সাবস পাওয়া যায়নি এবং এমবেড করা হবে না"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — ক্যাশ থেকে তাত্ক্ষণিক রিপোস্ট"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — অডিও ভাষা নির্বাচন করুন"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW পেইড (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — ডাউনলোড মান নির্বাচন করুন"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — ছবি ডাউনলোড করুন (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — poketube এ ভিডিও দেখুন"  # সাময়িকভাবে নিষ্ক্রিয়: poketube পরিষেবা ডাউন
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — ভিডিওতে সরাসরি লিঙ্ক পান"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — উপলব্ধ ফরম্যাট তালিকা দেখান"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — ভিডিও ext/codec পরিবর্তন করুন"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀এমবেড করুন"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — শুধুমাত্র অডিও এক্সট্র্যাক্ট করুন"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW পেইড (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — ক্যাশ থেকে তাত্ক্ষণিক রিপোস্ট"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — poketube এ ভিডিও দেখুন"  # সাময়িকভাবে নিষ্ক্রিয়: poketube পরিষেবা ডাউন
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — অডিও ভাষা নির্বাচন করুন"
    ALWAYS_ASK_BEST_BUTTON_MSG = "সেরা"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛অন্যান্য"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝শুধুমাত্র সাব"
    ALWAYS_ASK_SMART_GROUPING_MSG = "স্মার্ট গ্রুপিং"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "অ্যাকশন বাটন সারি যোগ করা হয়েছে (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "অ্যাকশন বাটন সারি যোগ করা হয়েছে (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "বিদ্যমান সারিতে নীচের বাটন যোগ করা হয়েছে"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "নতুন নীচের সারি তৈরি করা হয়েছে"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "প্লেলিস্টে কোন ভিডিও পাওয়া যায়নি"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "অসমর্থিত URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "কোন ভিডিও পাওয়া যায়নি"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "কোন ভিডিও পাওয়া যায়নি"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "কোন মিডিয়া পাওয়া যায়নি"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "এই টুইটে নেই"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>ভিডিও তথ্য পাওয়ার সময় ত্রুটি:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "ভিডিও তথ্য পাওয়ার সময় ত্রুটি"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "<code>/clean</code> কমান্ড চেষ্টা করুন এবং আবার চেষ্টা করুন। যদি ত্রুটি অব্যাহত থাকে, YouTube-এর জন্য অনুমোদনের প্রয়োজন। <code>/cookie</code> বা <code>/cookies_from_browser</code> এর মাধ্যমে cookies.txt আপডেট করুন এবং আবার চেষ্টা করুন।"
    ALWAYS_ASK_MENU_CLOSED_MSG = "মেনু বন্ধ করা হয়েছে।"
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 ম্যানুয়াল মান নির্বাচন"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "স্বয়ংক্রিয় সনাক্তকরণ ব্যর্থ হওয়ায় ম্যানুয়ালি মান নির্বাচন করুন:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 সমস্ত উপলব্ধ ফরম্যাট"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 উপলব্ধ মান (ক্যাশ থেকে)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ ক্যাশ করা মান ব্যবহার করা হচ্ছে - নতুন ফরম্যাট উপলব্ধ নাও হতে পারে"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 ফরম্যাট ডাউনলোড করা হচ্ছে"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 ডাউনলোড করা হচ্ছে"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 অগ্রগতি ট্র্যাকিং সহ ডাউনলোড করা হচ্ছে..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 ফরম্যাট ব্যবহার করে ডাউনলোড করা হচ্ছে:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 ফরম্যাট ব্যবহার করে অডিও ডাউনলোড করা হচ্ছে:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 সেরা মান ডাউনলোড করা হচ্ছে..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 ডাটাবেস ডাম্প ডাউনলোড করা হচ্ছে..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 ডাউনলোড করা হচ্ছে"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "ফরম্যাট পৃষ্ঠা"
    ALWAYS_ASK_FROM_CACHE_MSG = "(ক্যাশ থেকে)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ ত্রুটি: মূল বার্তা পাওয়া যায়নি। এটি মুছে ফেলা হতে পারে। অনুগ্রহ করে আবার লিঙ্ক পাঠান।"
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ ত্রুটি: মূল URL পাওয়া যায়নি। অনুগ্রহ করে আবার লিঙ্ক পাঠান।"
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>সরাসরি লিঙ্ক পাওয়া গেছে</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>শিরোনাম:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>সময়কাল:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>ফরম্যাট:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>ভিডিও স্ট্রিম:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>অডিও স্ট্রিম:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ স্ট্রিম লিঙ্ক পাওয়া যায়নি"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {url} থেকে Always Ask মেনুর মাধ্যমে সরাসরি লিঙ্ক এক্সট্র্যাক্ট করা হয়েছে"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {url} থেকে Always Ask মেনুর মাধ্যমে সরাসরি লিঙ্ক এক্সট্র্যাক্ট করতে ব্যর্থ: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {url} থেকে down_and_up_with_format এর মাধ্যমে সরাসরি লিঙ্ক এক্সট্র্যাক্ট করা হয়েছে"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {url} থেকে down_and_up_with_format এর মাধ্যমে সরাসরি লিঙ্ক এক্সট্র্যাক্ট করতে ব্যর্থ: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {url} থেকে down_and_audio এর মাধ্যমে সরাসরি লিঙ্ক এক্সট্র্যাক্ট করা হয়েছে"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য {url} থেকে down_and_audio এর মাধ্যমে সরাসরি লিঙ্ক এক্সট্র্যাক্ট করতে ব্যর্থ: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ ক্যাশ থেকে অডিও পাঠানো হয়েছে।"
    AUDIO_PROCESSING_MSG = "🎙️ অডিও প্রক্রিয়াকরণ করা হচ্ছে..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 অডিও ডাউনলোড করা হচ্ছে:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "অডিও ডাউনলোডের সময় ত্রুটি ঘটেছে।"
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ অডিও তথ্য এক্সট্র্যাক্ট করতে ব্যর্থ"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "প্লেলিস্টে {index} সূচকে অসমর্থিত ফাইল টাইপ এড়িয়ে যাচ্ছি"
    AUDIO_FILE_NOT_FOUND_MSG = "ডাউনলোডের পরে অডিও ফাইল পাওয়া যায়নি।"

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ অডিও পাঠাতে ব্যর্থ: ফাইলের আকার 0 B এর সমান (প্লেলিস্ট সূচক {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ অডিও ফাইল এখনও ডাউনলোড হচ্ছে, অনুগ্রহ করে অপেক্ষা করুন..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 অডিও ফাইল আপলোড করা হচ্ছে...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ অডিও পাঠাতে ব্যর্থ: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "প্লেলিস্ট অডিও পাঠানো হয়েছে: {sent}/{total} ফাইল (মান={quality}) ব্যবহারকারী {user_id} এর কাছে"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ অডিও ডাউনলোড করতে ব্যর্থ: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ টাইমআউটের কারণে ডাউনলোড বাতিল করা হয়েছে (2 ঘন্টা)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ ভিডিও ফাইল পাওয়া যায়নি: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ ভিডিও পাঠাতে ব্যর্থ: ফাইলের আকার 0 B এর সমান (প্লেলিস্ট সূচক {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ ভিডিও ফাইল এখনও ডাউনলোড হচ্ছে, অনুগ্রহ করে অপেক্ষা করুন..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ ভিডিও প্রক্রিয়াকরণে ত্রুটি: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ বিবরণ ফাইল পাঠাতে ত্রুটি: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 যদি আপনি ভিডিও ক্যাপশন পরিবর্তন করতে চান - নতুন পাঠ্য সহ ভিডিওতে উত্তর দিন</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "কোন সাবটাইটেল সনাক্ত করা যায়নি"
    VIDEO_PROGRESS_MSG = "<b>ভিডিও:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>অডিও:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL সীমা অতিক্রম করেছে: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "প্রক্রিয়াকরণ সম্পন্ন হয়েছে"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ একাধিক URL মোডে প্লেলিস্ট রেঞ্জ অনুমোদিত নয়। শুধুমাত্র রেঞ্জ ছাড়া একক URL পাঠান (*1*5, /vid 1-10, ইত্যাদি)।"
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "আপনার সাইট সমর্থিত কিনা <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>এখানে</a> পরীক্ষা করুন"
    ERROR_COOKIE_NEEDED_MSG = "এই ভিডিও ডাউনলোড করার জন্য আপনার <code>cookie</code> প্রয়োজন হতে পারে। প্রথমে, <b>/clean</b> কমান্ডের মাধ্যমে আপনার ওয়ার্কস্পেস পরিষ্কার করুন"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "Youtube এর জন্য - <b>/cookie</b> কমান্ডের মাধ্যমে <code>cookie</code> পান। অন্য কোন সমর্থিত সাইটের জন্য - আপনার নিজের cookie পাঠান (<a href='https://t.me/tg_ytdlp/203'>গাইড1</a>) (<a href='https://t.me/tg_ytdlp/214'>গাইড2</a>) এবং তার পরে আবার আপনার ভিডিও লিঙ্ক পাঠান।"
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "সাবটাইটেল ভাষা নির্বাচন করুন"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "কোন বিকল্প অডিও ভাষা নেই"
    CHOOSE_AUDIO_LANGUAGE_MSG = "অডিও ভাষা নির্বাচন করুন"
    PAGE_NUMBER_MSG = "পৃষ্ঠা {page}"
    TOTAL_PROGRESS_MSG = "মোট অগ্রগতি"
    SUBTITLE_MENU_CLOSED_MSG = "সাবটাইটেল মেনু বন্ধ করা হয়েছে।"
    SUBTITLE_LANGUAGE_SET_MSG = "সাবটাইটেল ভাষা সেট করা হয়েছে: {value}"
    AUDIO_SET_MSG = "অডিও সেট করা হয়েছে: {value}"
    FILTERS_UPDATED_MSG = "ফিল্টার আপডেট করা হয়েছে"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙পিছনে"
    CLOSE_BUTTON_TEXT = "🔚বন্ধ করুন"
    LIST_BUTTON_TEXT = "📃তালিকা"
    IMAGE_BUTTON_TEXT = "🖼ছবি"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ মান স্বয়ংক্রিয়ভাবে সনাক্ত করা হয়নি\nসমস্ত উপলব্ধ ফরম্যাট দেখতে 'অন্যান্য' বাটন ব্যবহার করুন।</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **লাইভ স্ট্রিম সনাক্ত করা হয়েছে**\n\nচলমান বা অসীম লাইভ স্ট্রিম ডাউনলোড করা অনুমোদিত নয়।\n\nঅনুগ্রহ করে স্ট্রিম শেষ হওয়ার জন্য অপেক্ষা করুন এবং আবার ডাউনলোড করার চেষ্টা করুন যখন:\n• স্ট্রিম সময়কাল জানা আছে\n• স্ট্রিম শেষ হয়ে গেছে\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>লাইভ স্ট্রিম ডাউনলোড</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "Chunk {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "সর্বোচ্চ আকার: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "মোট সময়কাল: {duration} সেকেন্ড"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>লাইভ স্ট্রিম - Chunk {chunk}</b>\n⏱ সময়কাল: {duration} সেকেন্ড\n📦 আকার: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "Chunk {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>লাইভ স্ট্রিম ডাউনলোড সম্পন্ন</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "{chunks} chunk(s) ডাউনলোড করা হয়েছে"
    LIVE_STREAM_TOTAL_DURATION_MSG = "মোট সময়কাল: {duration} সেকেন্ড"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>লাইভ স্ট্রিম ডাউনলোড বন্ধ করা হয়েছে</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "ব্যবহারকারী ডিরেক্টরি মুছে ফেলা হয়েছে (সম্ভবত /clean কমান্ড দ্বারা)"
    LIVE_STREAM_FILE_DELETED_MSG = "Chunk ফাইল মুছে ফেলা হয়েছে (সম্ভবত /clean কমান্ড দ্বারা)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ স্ট্রিম শেষ হয়ে গেছে"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "অনুগ্রহ করে `/format` কমান্ড ব্যবহার করে একটি ভিন্ন ফরম্যাট নির্বাচন করুন।"
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>সরাসরি লিঙ্ক পাওয়া গেছে</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>শিরোনাম:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>সময়কাল:</b> {duration} সেকেন্ড\n"
    FORMAT_FIELD_MSG = "🎛 <b>ফরম্যাট:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>ভিডিও স্ট্রিম:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>অডিও স্ট্রিম:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **ফাইল প্রক্রিয়াকরণ ত্রুটি**\n\nভিডিও ডাউনলোড করা হয়েছে কিন্তু ফাইলের নামে অবৈধ অক্ষরের কারণে প্রক্রিয়া করা যায়নি।\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **ফাইল প্রক্রিয়াকরণ ত্রুটি**\n\nভিডিও ডাউনলোড করা হয়েছে কিন্তু অবৈধ যুক্তি ত্রুটির কারণে প্রক্রিয়া করা যায়নি।\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**কারণ:**\n"
        "• ডাউনলোড করা ফাইলটি একটি ভিডিও ফাইল নয়\n"
        "• এটি একটি নথি (PDF, DOC, ইত্যাদি) বা আর্কাইভ হতে পারে\n\n"
        "**সমাধান:**\n"
        "• লিঙ্কটি পরীক্ষা করুন - এটি একটি নথিতে নিয়ে যেতে পারে, ভিডিওতে নয়\n"
        "• একটি ভিন্ন লিঙ্ক বা উৎস চেষ্টা করুন\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**কারণ:**\n"
        "• ফাইলটি ভিডিও হিসাবে প্রক্রিয়া করা যায় না\n"
        "• এটি একটি ভিডিও ফাইল নাও হতে পারে বা ফাইলটি ক্ষতিগ্রস্ত হতে পারে\n\n"
        "**সমাধান:**\n"
        "• লিঙ্কটি পরীক্ষা করুন - এটি একটি নথিতে নিয়ে যেতে পারে, ভিডিওতে নয়\n"
        "• একটি ভিন্ন লিঙ্ক বা উৎস চেষ্টা করুন\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **ফরম্যাট উপলব্ধ নয়**\n\nঅনুরোধ করা ভিডিও ফরম্যাট এই ভিডিওর জন্য উপলব্ধ নয়।\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ এই ভিডিওর জন্য ফরম্যাট ID {format_id} পাওয়া যায়নি।\n\nউপলব্ধ ফরম্যাট ID: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **এই ভিডিওর জন্য AV1 ফরম্যাট উপলব্ধ নয়।**\n\n**উপলব্ধ ফরম্যাট:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **ফাইল প্রক্রিয়াকরণ ত্রুটি**\n\nঅডিও ডাউনলোড করা হয়েছে কিন্তু ফাইলের নামে অবৈধ অক্ষরের কারণে প্রক্রিয়া করা যায়নি।\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **ফাইল প্রক্রিয়াকরণ ত্রুটি**\n\nঅডিও ডাউনলোড করা হয়েছে কিন্তু অবৈধ যুক্তি ত্রুটির কারণে প্রক্রিয়া করা যায়নি।\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "ব্যবহারকারী একটি নিষিদ্ধ কন্টেন্ট প্রবেশ করেছেন। ডাউনলোড করা যাবে না।"
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "কমান্ডের মাধ্যমে NSFW blur সেট করা হয়েছে: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "ব্যবহারকারী /nsfw মেনু খুলেছেন।"
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: বন্ধ করা হয়েছে।"
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "{service} cookie ডাউনলোড করতে ব্যর্থ: status={status} (url লুকানো)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "{service} cookie ডাউনলোড করতে ত্রুটি: {error} (url লুকানো)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "{service} cookie ডাউনলোড করার সময় অপ্রত্যাশিত ত্রুটি (url লুকানো): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য Cookie ফাইল আপডেট করা হয়েছে।"
    COOKIES_INVALID_CONTENT_LOG_MSG = "ব্যবহারকারী {user_id} দ্বারা অবৈধ cookie কন্টেন্ট প্রদান করা হয়েছে।"
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য YouTube cookie URL গুলি খালি।"
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "উৎস {source} থেকে ব্যবহারকারী {user_id} এর জন্য YouTube কুকি ডাউনলোড এবং যাচাই করা হয়েছে।"
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "ব্যবহারকারী {user_id} এর জন্য সমস্ত YouTube cookie উৎস ব্যর্থ হয়েছে।"
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "অ্যাডমিন {admin_id} দ্বারা check_porn কমান্ডে ত্রুটি: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Split অংশের আকার {size} বাইটে সেট করা হয়েছে।"
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "ফাইল বিভাজনের সাথে ভিডিও আপলোড সম্পন্ন হয়েছে।"
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "প্লেলিস্ট ভিডিও পাঠানো হয়েছে: {sent}/{total} ফাইল (মান={quality}) ব্যবহারকারী {user_id} এর কাছে"
    UNKNOWN_ERROR_MSG = "❌ অজানা ত্রুটি: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "প্লেলিস্টে {index} সূচকে অসমর্থিত ফাইল টাইপ এড়িয়ে যাচ্ছি"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg পাওয়া যায়নি। অনুগ্রহ করে FFmpeg ইনস্টল করুন।"
    CONVERSION_TO_MP4_FAILED_MSG = "❌ MP4 এ রূপান্তর ব্যর্থ: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ সাবটাইটেল এমবেড করা অনেক সময় নিতে পারে (প্রতি 1 মিনিট ভিডিওতে 1 মিনিট পর্যন্ত)!\n🔥 সাবটাইটেল বার্ন করা শুরু হচ্ছে..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ সীমাবদ্ধতার কারণে সাবটাইটেল এমবেড করা যায় না (মান/সময়কাল/আকার)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ নির্বাচিত ভাষার জন্য সাবটাইটেল উপলব্ধ নয়"
    ERROR_SENDING_VIDEO_MSG = "❌ ভিডিও পাঠাতে ত্রুটি: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ প্লেলিস্ট ভিডিও পাঠানো হয়েছে: {sent}/{total} ফাইল।"
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ টাইমআউটের কারণে ডাউনলোড বাতিল করা হয়েছে (2 ঘন্টা)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ ভিডিও ডাউনলোড করতে ব্যর্থ: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ ত্রুটি: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON অবশ্যই একটি অবজেক্ট (dictionary) হতে হবে।"
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ অবৈধ JSON ফরম্যাট। অনুগ্রহ করে বৈধ JSON প্রদান করুন।"
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ মান অবশ্যই {min_val} এবং {max_val} এর মধ্যে হতে হবে।"
    ARGS_PARAM_SET_TO_MSG = "✅ {description} সেট করা হয়েছে: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ True"
    ARGS_FALSE_BUTTON_MSG = "❌ False"
    ARGS_BACK_BUTTON_MSG = "🔙 পিছনে"
    ARGS_CLOSE_BUTTON_MSG = "🔚 বন্ধ করুন"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ True"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ False"
    ARGS_NOT_SET_MSG = "সেট করা নেই"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ এই ভিডিওর জন্য AV1 ফরম্যাট উপলব্ধ নয়।\n\nউপলব্ধ ফরম্যাট:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ ডাউনলোড করতে ত্রুটি: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ {index} সূচকে প্লেলিস্টে কোন ভিডিও পাওয়া যায়নি।"
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **ভিডিও রূপান্তর ব্যর্থ**\n\nঅবৈধ যুক্তি ত্রুটির কারণে ভিডিওটি MP4 এ রূপান্তর করা যায়নি।\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **ভিডিও রূপান্তর ব্যর্থ**\n\nভিডিওটি MP4 এ রূপান্তর করা যায়নি।\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ স্ট্রিম লিঙ্ক পাওয়া যায়নি"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>লিঙ্ক পাওয়ার সময় ত্রুটি:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ {index} সূচকে কোন কন্টেন্ট পাওয়া যায়নি"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ ত্রুটি: মূল বার্তা পাওয়া যায়নি।"
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ ত্রুটি: URL পাওয়া যায়নি।"
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ এই URL এমবেড করা যাবে না।"
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ এই ভিডিওর জন্য {codec} কোডেক উপলব্ধ নয়"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ এই ভিডিওর জন্য {format} ফরম্যাট উপলব্ধ নয়"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood limit। পরে চেষ্টা করুন।"
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Cookie পরীক্ষা করুন"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ অটো (YouTube ত্রুটিতে)"
    PROXY_OFF_BUTTON_MSG = "❌ OFF"
    PROXY_CLOSE_BUTTON_MSG = "🔚বন্ধ করুন"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 দেশ নির্বাচন করুন:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ দেশ নির্বাচন পরিষ্কার করুন"
    PROXY_COUNTRY_SELECTED_MSG = "✅ দেশ বেছে নেওয়া হয়েছে: {country} (কোড: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 উপলব্ধ প্রক্সি: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 বট প্রথমে HTTP চেষ্টা করবে, তারপর SOCKS5"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 নির্বাচিত দেশের জন্য প্রক্সি স্বয়ংক্রিয়ভাবে সক্ষম"
    PROXY_COUNTRY_CLEARED_MSG = "✅ দেশ নির্বাচন সাফ করা হয়েছে"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ দেশ নির্বাচন সাফ করা হয়েছে"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ দেশ বেছে নেওয়া হয়েছে: {country}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 ফাইল থেকে দেশ ব্যবহার করা হচ্ছে: {country}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 ফাইল থেকে পাওয়া দেশগুলি: {count}"

    PROXY_COUNTRY_NOT_AVAILABLE_MSG = "❌ এই দেশের জন্য প্রক্সি উপলব্ধ নয়। অন্য দেশ চেষ্টা করুন।"
    PROXY_COUNTRY_SET_BY_COMMAND_MSG = "✅ প্রক্সি সেট করা হয়েছে: দেশ {country} (কোড: {country_code})"
    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 নির্বাচিত দেশ: {country} (কোড: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ এই দেশের জন্য প্রক্সি সক্ষম"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ প্রক্সি নিষ্ক্রিয় (সক্ষম করতে ALL (AUTO) টিপুন)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ ON"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ OFF"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚বন্ধ করুন"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ ON (Blur নেই)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ON (Blur নেই)"
    NSFW_OFF_BLUR_MSG = "✅ OFF (Blur)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ OFF (Blur)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "পরিষ্কার"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "ব্যবহারকারী {user} এর জন্য উত্তর বার্তা প্রক্রিয়াকরণে ত্রুটি: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "ব্যবহারকারী {user} এর কাছে ব্রডকাস্ট পাঠাতে ত্রুটি: {error}"
    ADMIN_LOGS_FORMAT_MSG = "{bot_name} এর লগ\nব্যবহারকারী: {user_id}\nমোট লগ: {total}\nবর্তমান সময়: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nমোট {path}: {count}\nবর্তমান সময়: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>মোট ব্যবহারকারী: {count}</i>\nশেষ 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "অ্যাডমিন {admin_id} দ্বারা পর্ন cache পুনরায় লোড করা হয়েছে। Domains: {domains}, Keywords: {keywords}, Sites: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "টাইমআউট বার্তা পাঠাতে ত্রুটি: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>ভাষা নির্বাচন করুন</b>"
    LANG_CHANGED_MSG = "✅ ভাষা পরিবর্তন করা হয়েছে {lang_name}"
    LANG_ERROR_MSG = "❌ ভাষা পরিবর্তন করতে ত্রুটি"
    LANG_CLOSED_MSG = "ভাষা নির্বাচন বন্ধ করা হয়েছে"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] callback: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "URL সহ ব্রাউজার পর্যবেক্ষণ বাটন যোগ করা হচ্ছে: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "ব্রাউজার পর্যবেক্ষণ URL কনফিগার করা নেই: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **কীবোর্ড সেটিং আপডেট করা হয়েছে!**\n\nনতুন সেটিং: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "কীবোর্ড লুকাতে ব্যর্থ: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "ব্যবহারকারী {user_id} এর জন্য লিঙ্ক এক্সট্র্যাকশনের জন্য কাজ করা YouTube কুকি ব্যবহার করা হচ্ছে"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "ব্যবহারকারী {user_id} এর জন্য লিঙ্ক এক্সট্র্যাকশনের জন্য কাজ করা YouTube কুকি উপলব্ধ নেই"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "ব্যবহারকারী {user_id} এর জন্য লিঙ্ক এক্সট্র্যাকশনের জন্য বিদ্যমান YouTube কুকি ব্যবহার করা হচ্ছে"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "ব্যবহারকারী {user_id} এর জন্য লিঙ্ক এক্সট্র্যাকশনের জন্য কোন YouTube কুকি পাওয়া যায়নি"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "লিঙ্ক এক্সট্র্যাকশনের জন্য ব্যবহারকারী {user_id} ফোল্ডারে গ্লোবাল cookie ফাইল কপি করা হয়েছে"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] ব্যবহারকারী {user_id} mediainfo কমান্ড অনুরোধ করেছেন"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] ব্যবহারকারী {user_id} অ্যাডমিন: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] ব্যবহারকারী {user_id} চ্যানেলে আছেন: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] ব্যবহারকারী {user_id} access denied - অ্যাডমিন নন এবং চ্যানেলে নেই"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] ব্যবহারকারী {user_id} access granted"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ এই কমান্ড শুধুমাত্র প্রশাসকদের জন্য উপলব্ধ।"
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ PO token সমর্থন সহ ডাউনলোড সম্পন্ন হয়েছে"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood limit। পরে চেষ্টা করুন।"
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST token refresh ত্রুটি: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Firebase session বন্ধ করতে ত্রুটি: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ base db structure শুরু করতে ত্রুটি: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ config.py এ সমস্ত প্যারামিটার সেট করা নেই (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL সেট করা নেই"
    DB_API_KEY_NOT_SET_MSG = "❌ idToken পাওয়ার জন্য FIREBASE_CONF.apiKey সেট করা নেই"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Firebase dump ডাউনলোড করতে ত্রুটি: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ REST এর মাধ্যমে Firebase dump ডাউনলোড করতে ব্যর্থ"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ _download_and_reload_cache এ ত্রুটি: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ auto reload_cache চালাতে ত্রুটি (চেষ্টা {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ সমস্ত পুনঃপ্রচেষ্টা ব্যর্থ হয়েছে"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 {datetime} এ Firebase dump ডাউনলোড শুরু করা হচ্ছে"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Dependency উপলব্ধ নেই: requests বা Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ ডাটাবেস খালি"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ logger বন্ধ করতে ত্রুটি: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ cleanup এর সময় ত্রুটি: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Clone ত্রুটি: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Clone timeout"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Clone exception: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ ব্যবহারকারী দ্বারা আপডেট বাতিল করা হয়েছে"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Repository সফলভাবে clone করা হয়েছে"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Backups _backup/ এ সরানো হয়েছে"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ সমস্ত মডিউল লোড করা হয়েছে"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ প্রস্থানের সময় cleanup সম্পন্ন হয়েছে"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Signal {signal} পাওয়া গেছে, gracefully বন্ধ করা হচ্ছে..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "অনুগ্রহ করে অপেক্ষা করুন..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 HLS stream ডাউনলোড করা হচ্ছে:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "fragments এর জন্য অপেক্ষা করা হচ্ছে"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ _backup/ এ Backup {ts} পাওয়া যায়নি"
    RESTORE_FAILED_RESTORE_MSG = "❌ Restore করতে ব্যর্থ {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Restored: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>বিবরণ:</b> {error_details}\n\nক্রিটিক্যাল ত্রুটির কারণে ডাউনলোড বন্ধ করা হয়েছে।\n\n💡 <b>টিপ:</b> যদি আপনি 401 Unauthorized ত্রুটি পাচ্ছেন, <code>/cookie instagram</code> কমান্ড ব্যবহার করুন বা Instagram এর সাথে প্রমাণীকরণের জন্য আপনার নিজের cookies পাঠান।"
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ পর্ন blacklist এ Domain: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ পর্ন keywords পাওয়া গেছে: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ whitelist এ Domain: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ whitelist keywords পাওয়া গেছে: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ কোন পর্ন keywords পাওয়া যায়নি"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ {index} সূচকে TikTok API ত্রুটি, পরবর্তী অডিওতে এড়িয়ে যাচ্ছি..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ {index} সূচকে TikTok API ত্রুটি, পরবর্তী ভিডিওতে এড়িয়ে যাচ্ছি..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "ব্যবহারকারী একটি <b>url</b> প্রবেশ করেছেন\n <b>ব্যবহারকারীর নাম:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>ব্যবহারকারী এভাবে প্রবেশ করেছেন:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "চ্যানেলে যোগ দিন"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Handler নিবন্ধন করা হচ্ছে: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - আমার 5টি cookie ডাউনলোড করুন"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - ব্রাউজারের YT-cookie পান"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - আপনার cookie ফাইল যাচাই করুন"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - কাস্টম cookie আপলোড করুন"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 বন্ধ করুন"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "এর জন্য উপলব্ধ ফরম্যাট: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚বন্ধ করুন"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚বন্ধ করুন"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚বন্ধ করুন"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚বন্ধ করুন"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "সাহায্য বন্ধ করা হয়েছে।"
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "বন্ধ করা হয়েছে"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "ত্রুটি ঘটেছে"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "PATH বা project directory এ ffmpeg পাওয়া যায়নি। অনুগ্রহ করে FFmpeg ইনস্টল করুন।"
    YTDLP_NOT_FOUND_MSG = "PATH বা project directory এ yt-dlp binary পাওয়া যায়নি। অনুগ্রহ করে yt-dlp ইনস্টল করুন।"
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "ভিডিও {rounds} অংশে বিভক্ত করা হবে, যা অত্যধিক হতে পারে"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "ভিডিও অংশ {current}/{total} বিভক্ত করা হচ্ছে: {start_time:.2f}s থেকে {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Split অংশ {part} তৈরি করতে ব্যর্থ: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Split অংশ {part} সফলভাবে তৈরি করা হয়েছে: {target_name} ({size} বাইট)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "ভিডিও অংশ {part} বিভক্ত করতে ত্রুটি: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "ভিডিও {count} অংশে সফলভাবে বিভক্ত করা হয়েছে"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "ভিডিও বিভাজন প্রক্রিয়ায় ত্রুটি: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] ভিডিও {video_path} প্রক্রিয়াকরণের সময় ত্রুটি: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "ভিডিও ফাইল বিদ্যমান নেই: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "dimensions পার্স করতে ত্রুটি '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "'{size_result}' থেকে ভিডিও dimensions নির্ধারণ করা যায়নি, default ব্যবহার করা হচ্ছে: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Thumbnail তৈরি করতে ত্রুটি: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "ভিডিও সময়কাল পার্স করতে ত্রুটি: {error}, ফলাফল ছিল: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "{thumb_dir} এ Thumbnail তৈরি করা হয়নি, default ব্যবহার করা হচ্ছে"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "কমান্ড এক্সিকিউশন ত্রুটি: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "FFmpeg দিয়ে Thumbnail তৈরি করতে ত্রুটি: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "non-dict config section এড়িয়ে যাচ্ছি: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Setting {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] ব্যবহারকারী cookies ব্যবহার করা হচ্ছে: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "ব্যবহারকারী {user_id} এর জন্য YouTube cookies ব্যবহার করা হচ্ছে"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "ব্যবহারকারী {user_id} ফোল্ডারে গ্লোবাল cookie ফাইল কপি করা হয়েছে"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] ব্যবহারকারী cookies হিসাবে কপি করা গ্লোবাল cookies ব্যবহার করা হচ্ছে: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "ব্যবহারকারী {user_id} এর জন্য গ্লোবাল cookie ফাইল কপি করতে ব্যর্থ: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Domain এর জন্য --no-cookies ব্যবহার করা হচ্ছে: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy অনুরোধ করা হয়েছে কিন্তু config import/get করতে ব্যর্থ: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "gallery-dl এর জন্য proxy জোর করে ব্যবহার করা হচ্ছে: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy অনুরোধ করা হয়েছে কিন্তু proxy configuration অসম্পূর্ণ"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Proxy helper ব্যর্থ: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Extractor items পার্স করা হচ্ছে..."
    GALLERY_DL_ITEM_COUNT_MSG = "আইটেম {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Metadata পাওয়া গেছে (tag 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL পাওয়া গেছে (tag 3): {url}, metadata: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Metadata পাওয়া গেছে (legacy): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL পাওয়া গেছে (legacy): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Filename পাওয়া গেছে: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Directory পাওয়া গেছে: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Extension পাওয়া গেছে: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "{count} আইটেম পার্স করা হয়েছে, info: {info}, fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "gallery-dl config সেট করা হচ্ছে: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Strategy A চেষ্টা করা হচ্ছে: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor মডিউল পাওয়া যায়নি"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() এই build এ উপলব্ধ নয়"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "extractor.find({url}) কল করা হচ্ছে"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "কোন extractor URL এর সাথে মিলেছে না"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Extractor এ cookies সেট করা হচ্ছে: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Extractor এ cookies সেট করতে ব্যর্থ: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Extractor পাওয়া গেছে, items() কল করা হচ্ছে"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Strategy A সফল হয়েছে, info পাওয়া গেছে: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Strategy A: extractor.items() কোন বৈধ info ফেরত দেয়নি"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Strategy A (extractor.find) ব্যর্থ হয়েছে: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "--get-urls থেকে Fallback metadata: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "সমস্ত strategy metadata পাওয়ার জন্য ব্যর্থ হয়েছে"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "ছবির তথ্য এক্সট্র্যাক্ট করতে ব্যর্থ: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job মডিউল পাওয়া যায়নি (ভাঙা ইনস্টল?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob এই build এ উপলব্ধ নয়"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "gallery-dl directory এ ডাউনলোড করা ফাইল খুঁজছি"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Extractor থেকে নাম অনুযায়ী ফাইল খুঁজতে চেষ্টা করা হচ্ছে"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "ব্যবহারকারী {user_id} এর জন্য user args পড়তে ত্রুটি: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] ভিডিও প্রক্রিয়াকরণের সময় ত্রুটি {video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "ব্যবহারকারী {user_id} এর send_as_file সক্ষম আছে, document হিসাবে পাঠানো হচ্ছে"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video বারবার timeout হয়েছে; send_document এ fallback করা হচ্ছে"
    SENDER_CAPTION_TOO_LONG_MSG = "Caption খুব দীর্ঘ, minimal caption সহ চেষ্টা করা হচ্ছে"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (minimal caption) timeout হয়েছে; send_document এ fallback করা হচ্ছে"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "minimal caption সহ ভিডিও পাঠাতে ত্রুটি: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "সম্পূর্ণ বিবরণ ফাইল পাঠাতে ত্রুটি: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "অস্থায়ী বিবরণ ফাইল সরাতে ত্রুটি: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "NO_FILTER_DOMAINS এ domain এর জন্য match_filter এড়িয়ে যাচ্ছি: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "ব্যবহারকারী {user_id} এর জন্য format detection এর জন্য ব্যবহারকারীর URL এ বিদ্যমান YouTube cookies পরীক্ষা করা হচ্ছে"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "বিদ্যমান YouTube cookies ব্যবহারকারীর URL এ format detection এর জন্য ব্যবহারকারী {user_id} এর জন্য কাজ করছে - সেগুলি ব্যবহার করা হচ্ছে"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "বিদ্যমান YouTube cookies ব্যবহারকারীর URL এ ব্যর্থ হয়েছে, format detection এর জন্য ব্যবহারকারী {user_id} এর জন্য নতুন ones পাওয়ার চেষ্টা করা হচ্ছে"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Format detection এর জন্য ব্যবহারকারী {user_id} এর জন্য YouTube cookie source {i} চেষ্টা করা হচ্ছে"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "Source {i} থেকে YouTube cookies ব্যবহারকারীর URL এ format detection এর জন্য ব্যবহারকারী {user_id} এর জন্য কাজ করছে - ব্যবহারকারী ফোল্ডারে সংরক্ষণ করা হয়েছে"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "Source {i} থেকে YouTube cookies ব্যবহারকারীর URL এ format detection এর জন্য ব্যবহারকারী {user_id} এর জন্য কাজ করছে না"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Format detection এর জন্য ব্যবহারকারী {user_id} এর জন্য source {i} থেকে YouTube cookies ডাউনলোড করতে ব্যর্থ"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "Format detection এর জন্য ব্যবহারকারী {user_id} এর জন্য সমস্ত YouTube cookie sources ব্যর্থ হয়েছে, cookies ছাড়া চেষ্টা করা হবে"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "Format detection এর জন্য ব্যবহারকারী {user_id} এর জন্য কোন YouTube cookie sources কনফিগার করা নেই, cookies ছাড়া চেষ্টা করা হবে"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "Format detection এর জন্য ব্যবহারকারী {user_id} এর জন্য কোন YouTube cookies পাওয়া যায়নি, নতুন ones পাওয়ার চেষ্টা করা হচ্ছে"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Format detection এর জন্য ব্যবহারকারী {user_id} এর জন্য YouTube cookies ব্যবহার করা হচ্ছে (ইতিমধ্যে Always Ask মেনুতে যাচাই করা হয়েছে)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "Format detection এর জন্য ব্যবহারকারী {user_id} এর জন্য কোন YouTube cookies পাওয়া যায়নি, restore করার চেষ্টা করা হচ্ছে..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Format detection এর জন্য ব্যবহারকারী {user_id} ফোল্ডারে গ্লোবাল cookie ফাইল কপি করা হয়েছে"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "ব্যবহারকারী {user_id} এর জন্য গ্লোবাল cookie ফাইল কপি করতে ব্যর্থ: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "get_video_formats এ domain এর জন্য --no-cookies ব্যবহার করা হচ্ছে: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "App এখনও শুরু করা হয়নি। {name} অ্যাক্সেস করা যাবে না"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Caption:</b> <code>{caption}</code>\n<b>User id:</b> <code>{user_id}</code>\n<b>User first name:</b> <code>{users_name}</code>\n<b>Video file id:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor এ ত্রুটি: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor এ অপ্রত্যাশিত ত্রুটি: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 Video URL</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL কনফিগারেশনে অনুপস্থিত"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin শুরু করা হয়েছে"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken রিফ্রেশ করা হয়েছে"
    DB_LOG_FOR_USER_ADDED_MSG = "ব্যবহারকারীর জন্য Log যোগ করা হয়েছে"
    DB_DATABASE_CREATED_MSG = "db তৈরি করা হয়েছে"
    DB_BOT_STARTED_MSG = "Bot শুরু করা হয়েছে"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY config.py এ সংরক্ষণ করা হয়েছে: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "প্লেলিস্ট অংশ ইতিমধ্যে cache করা হয়েছে: {path_parts}, এড়িয়ে যাচ্ছি"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: কোন URL/quality variant এর জন্য cache পাওয়া যায়নি, empty dict ফেরত দেওয়া হচ্ছে"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: বড় range এর জন্য দ্রুত count: {cached_count} cache করা ভিডিও"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: hash {url_hash}, quality {quality_key} এর জন্য cache পাওয়া যায়নি"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: কোন URL variant এর জন্য cache পাওয়া যায়নি, None ফেরত দেওয়া হচ্ছে"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ অ্যাক্সেস অস্বীকার করা হয়েছে। শুধুমাত্র অ্যাডমিন।"
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Auto Firebase cache reloading আপডেট করা হয়েছে!\n\n📊 Status: {status}\n⏰ Schedule: 00:00 থেকে প্রতি {interval} ঘন্টায়\n🕒 Next reload: {next_exec} ({delta_min} মিনিটে)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Auto Firebase cache reloading বন্ধ করা হয়েছে!\n\n📊 Status: ❌ DISABLED\n💡 পুনরায় সক্ষম করতে /auto_cache on ব্যবহার করুন"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ অবৈধ যুক্তি। /auto_cache on | off | N (1..168) ব্যবহার করুন"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Interval অবশ্যই 1 এবং 168 ঘন্টার মধ্যে হতে হবে"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Interval সেট করতে ব্যর্থ"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Auto Firebase cache interval আপডেট করা হয়েছে!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: 00:00 থেকে প্রতি {interval} ঘন্টায়\n🕒 Next reload: {next_exec} ({delta_min} মিনিটে)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Auto Firebase cache reloading শুরু করা হয়েছে!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: 00:00 থেকে প্রতি {interval} ঘন্টায়\n🕒 Next reload: {next_exec} ({delta_min} মিনিটে)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Auto Firebase cache reloading বন্ধ করা হয়েছে!\n\n📊 Status: ❌ DISABLED\n💡 পুনরায় সক্ষম করতে /auto_cache on ব্যবহার করুন"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Auto reload ENABLED; পরবর্তী {next_exec} এ"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Auto reload DISABLED অ্যাডমিন দ্বারা।"
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Auto reload interval {interval}h এ সেট করা হয়েছে; পরবর্তী {next_exec} এ"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Auto reload শুরু করা হয়েছে; পরবর্তী {next_exec} এ"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Auto reload অ্যাডমিন দ্বারা বন্ধ করা হয়েছে।"
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase cache লোড করা হয়েছে: {count} root nodes"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Firebase cache ফাইল পাওয়া যায়নি, empty cache দিয়ে শুরু করা হচ্ছে: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ firebase cache লোড করতে ব্যর্থ: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase cache পুনরায় লোড করা হয়েছে: {count} root nodes"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Firebase cache ফাইল পাওয়া যায়নি: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ firebase cache পুনরায় লোড করতে ব্যর্থ: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 আপনি বট থেকে নিষিদ্ধ! আনবান করতে {Config.ADMIN_USERNAME} এর সাথে যোগাযোগ করুন\n<blockquote>P.S. চ্যানেল ছেড়ে যাবেন না - আপনি স্বয়ংক্রিয়ভাবে নিষিদ্ধ হবেন ⛔️</blockquote>\n🌍ভাষা পরিবর্তন করুন /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ কোন ভিডিও ফরম্যাট পাওয়া যায়নি। ছবি ডাউনলোডার চেষ্টা করা হচ্ছে…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram বার্তা পাঠানোর সীমাবদ্ধতা রেখেছে।\n⏳ অনুগ্রহ করে অপেক্ষা করুন: {time_str}\nটাইমার আপডেট করতে URL আবার 2 বার পাঠান।"
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>স্ট্রিম URL কপি করতে বাটনে ক্লিক করুন, তারপর VLC app এ paste করুন</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>স্ট্রিম URL কপি করতে বাটনে ক্লিক করুন, তারপর VLC app এ paste করুন</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>লিঙ্ক পাওয়ার সময় ত্রুটি:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ ফরম্যাট ফাইল পাঠাতে ত্রুটি: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ ফরম্যাট পাওয়া যায়নি:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 বিশ্লেষণ করা হচ্ছে... (6 সেকেন্ড অপেক্ষা করুন)"
    AA_PROCESSING_MSG = "🔎 বিশ্লেষণ করা হচ্ছে..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ ট্যাগ #{wrong} এ নিষিদ্ধ অক্ষর রয়েছে। শুধুমাত্র অক্ষর, সংখ্যা এবং _ অনুমোদিত।\nঅনুগ্রহ করে ব্যবহার করুন: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ গ্রুপে কাজ করার জন্য বটের জন্য প্রশাসক অধিকার প্রয়োজন। অনুগ্রহ করে এই গ্রুপে বটকে অ্যাডমিন করুন।"
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "হ্যালো {first_name},\n \n<i>এই বট🤖 সরাসরি telegram এ যেকোনো ভিডিও ডাউনলোড করতে পারে।😊 আরও তথ্যের জন্য <b>/help</b> চাপুন</i> 👈\n\n<blockquote>P.S. সম্ভাব্য 🔞NSFW কন্টেন্টের কারণে - ☁️<b>ক্লাউড স্টোরেজ</b>, 📁<b>ফাইল শেয়ার</b>, 🔗<b>URL শর্টনার</b> এবং 🔞<b>পর্ন সাইট</b> থেকে ডাউনলোড অর্থপ্রদানযোগ্য! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ @tg_ytdlp চ্যানেল 🗑<b>মুছবেন না/আনসাবস্ক্রাইব করবেন না</b> এবং বটে 🤖<b>অতিরিক্ত URL/কমান্ড স্প্যাম করবেন না</b> - বট ব্যবহার থেকে স্বয়ংক্রিয়ভাবে নিষিদ্ধ হবেন ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 সরানোর জন্য কোন ফাইল নেই।"
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 সমস্ত ফাইল সফলভাবে সরানো হয়েছে!\n\nসরানো ফাইল:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ আপনার পূর্ববর্তী ডাউনলোড শেষ না হওয়া পর্যন্ত অপেক্ষা করুন"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "check_user এ App instance None"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict None, ডাউনলোড অনুমোদন করা হচ্ছে"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict None, সাবটাইটেল এমবেডিং অনুমোদন করা হচ্ছে"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: সীমা পরীক্ষা করা হচ্ছে - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: info_dict keys: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "সাবটাইটেল এমবেডিং এড়িয়ে যাওয়া হয়েছে: সময়কাল {duration}s সীমা {max_duration}s অতিক্রম করেছে"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "সাবটাইটেল এমবেডিং এড়িয়ে যাওয়া হয়েছে: আকার {size_mb:.2f}MB সীমা {max_size}MB অতিক্রম করেছে"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "সাবটাইটেল এমবেডিং এড়িয়ে যাওয়া হয়েছে: মান {width}x{height} (min side {min_side}p) সীমা {max_quality}p অতিক্রম করেছে"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "playlist"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ {service} এর জন্য Range limit অতিক্রম করেছে: {count} (সর্বোচ্চ {max_count})।\n\nসর্বোচ্চ উপলব্ধ ফাইল ডাউনলোড করতে এই কমান্ডগুলির মধ্যে একটি ব্যবহার করুন:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ {service} এর জন্য Range limit অতিক্রম করেছে: {count} (সর্বোচ্চ {max_count})\nUser ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "config এ PO token provider অক্ষম করা হয়েছে"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} একটি YouTube domain নয়, PO token এড়িয়ে যাচ্ছি"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO token provider {base_url} এ উপলব্ধ নেই, standard YouTube extraction এ fallback করা হচ্ছে"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO token provider cache সাফ করা হয়েছে, পরবর্তী অনুরোধে availability পরীক্ষা করা হবে"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "App instance এখনও উপলব্ধ নেই"
    HELPER_USER_NAME_MSG = "ব্যবহারকারী"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood wait সনাক্ত করা হয়েছে, {wait_seconds} সেকেন্ডের জন্য sleep করা হচ্ছে"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood wait সনাক্ত করা হয়েছে কিন্তু সময় extract করতে পারেনি, {retry_delay} সেকেন্ডের জন্য sleep করা হচ্ছে"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno ত্রুটি সনাক্ত করা হয়েছে, {retry_delay} সেকেন্ডের জন্য sleep করা হচ্ছে"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy configuration অসম্পূর্ণ, direct connection ব্যবহার করা হচ্ছে"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚বন্ধ করুন"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚বন্ধ করুন"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "custom"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚বন্ধ করুন"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Logs ফাইল সরানো হয়েছে।"
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Tags ফাইল সরানো হয়েছে।"
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Format ফাইল সরানো হয়েছে।"
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Split ফাইল সরানো হয়েছে।"
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Mediainfo ফাইল সরানো হয়েছে।"
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Subtitle সেটিংস সরানো হয়েছে।"
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Keyboard সেটিংস সরানো হয়েছে।"
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Args সেটিংস সরানো হয়েছে।"
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 NSFW সেটিংস সরানো হয়েছে।"
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Proxy সেটিংস সরানো হয়েছে।"
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Flood wait সেটিংস সরানো হয়েছে।"
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚বন্ধ করুন"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Video Download Command"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Usage: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Examples:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (direct order)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (reverse order)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "আরও দেখুন: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "ব্যবহারকারী {user_id} add_bot_to_group কমান্ড বন্ধ করেছেন"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "YouTube ID এক্সট্র্যাক্ট করতে ব্যর্থ"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Thumbnail ডাউনলোড করতে ব্যর্থ বা এটি খুব বড়"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "অডিও ভাষা নির্বাচন করুন"
    AA_NO_SUBTITLES_DETECTED_MSG = "কোন সাবটাইটেল সনাক্ত করা যায়নি"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "সাবটাইটেল ভাষা নির্বাচন করুন"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "প্রমাণীকরণ ত্রুটি"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "অ্যাকাউন্ট পাওয়া যায়নি"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "অ্যাকাউন্ট অনুপলব্ধ"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "হার সীমা অতিক্রম করেছে"
    GALLERY_DL_NETWORK_ERROR_MSG = "নেটওয়ার্ক ত্রুটি"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "কন্টেন্ট অনুপলব্ধ"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "ভৌগোলিক সীমাবদ্ধতা"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "যাচাইকরণ প্রয়োজন"
    GALLERY_DL_POLICY_VIOLATION_MSG = "নীতি লঙ্ঘন"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "অজানা ত্রুটি"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ ডাউনলোড শুরু হয়েছে</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚বন্ধ করুন"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Video Download Command</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "ব্যবহার: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Examples:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "আরও দেখুন: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Flood limit। পরে চেষ্টা করুন।"
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Cookie Command Usage</b>

<code>/cookie</code> - Cookie মেনু দেখান
<code>/cookie youtube</code> - YouTube cookies ডাউনলোড করুন
<code>/cookie instagram</code> - Instagram cookies ডাউনলোড করুন
<code>/cookie tiktok</code> - TikTok cookies ডাউনলোড করুন
<code>/cookie x</code> বা <code>/cookie twitter</code> - Twitter/X cookies ডাউনলোড করুন
<code>/cookie facebook</code> - Facebook cookies ডাউনলোড করুন
<code>/cookie custom</code> - কাস্টম cookie নির্দেশাবলী দেখান

<i>উপলব্ধ পরিষেবাগুলি বট কনফিগারেশনের উপর নির্ভর করে।</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Cookie ফাইল সরানো হয়েছে এবং cache সাফ করা হয়েছে।"
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ পূর্ববর্তী"
    SUBS_BACK_BUTTON_MSG = "🔙পিছনে"
    SUBS_OFF_BUTTON_MSG = "🚫 OFF"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - ভাষা সেট করুন"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - AUTO/TRANS সহ ভাষা সেট করুন"
    SUBS_VALID_OPTIONS_MSG = "বৈধ বিকল্প:"
    
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
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - আমার 5টি cookie ডাউনলোড করুন"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - ব্রাউজারের YT-cookie পান"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - আপনার cookie ফাইল যাচাই করুন"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - কাস্টম cookie আপলোড করুন"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - মান এবং ফরম্যাট পরিবর্তন করুন"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - MediaInfo ON / OFF করুন"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Split ভিডিও অংশের আকার পরিবর্তন করুন"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - ভিডিওকে অডিও হিসাবে ডাউনলোড করুন"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - সাবটাইটেল ভাষা সেটিংস"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - প্লেলিস্ট ডাউনলোড করার 방법"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - gallery-dl এর মাধ্যমে ছবি ডাউনলোড করুন"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - আপনার #tags পাঠান"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - নির্দেশাবলী পান"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - আপনার logs পাঠান"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Playlist এর সাহায্য"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - howto"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - সরাসরি ভিডিও লিঙ্ক পান"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Proxy সক্ষম/অক্ষম করুন"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Keyboard layout"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - Inline search helper"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp arguments"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - NSFW blur সেটিংস"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Clean Options</b>\n\nকি পরিষ্কার করতে হবে তা নির্বাচন করুন:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: @vid search সক্রিয় করুন"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: @vid search সক্রিয় করুন"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 OFF"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 FULL"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[Images URL]({url})"
    IMAGE_ERROR_MSG = "❌ ত্রুটি: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙পিছনে"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - কাস্টম ফরম্যাট"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p মান"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K মান"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K মান"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - নির্দিষ্ট format ID"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - সর্বদা মেনু দেখান"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/sেরা মান"
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
    ARGS_INPUT_TIMEOUT_MSG = "⏰ নিষ্ক্রিয়তার কারণে Input mode স্বয়ংক্রিয়ভাবে বন্ধ করা হয়েছে (5 মিনিট)।"
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Reset All"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 View Current"
    ARGS_BACK_BUTTON_MSG = "🔙 পিছনে"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>এই সেটিংস একটি template হিসাবে সংরক্ষণ করতে এই বার্তাটি আপনার favorites এ forward করুন।</i> \n\n<i>এই সেটিংস প্রয়োগ করতে এই বার্তাটি এখানে আবার forward করুন।</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Current yt-dlp Arguments:\n\nকোন কাস্টম সেটিংস কনফিগার করা নেই।\n\n---\n\n<i>এই সেটিংস একটি template হিসাবে সংরক্ষণ করতে এই বার্তাটি আপনার favorites এ forward করুন।</i> \n\n<i>এই সেটিংস প্রয়োগ করতে এই বার্তাটি এখানে আবার forward করুন।</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Current yt-dlp Arguments:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Export Settings"
    ARGS_SETTINGS_READY_MSG = "Export এর জন্য সেটিংস প্রস্তুত! সংরক্ষণ করতে এই বার্তাটি favorites এ forward করুন।"
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Current yt-dlp Arguments:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ বার্তায় সেটিংস চিনতে ব্যর্থ। নিশ্চিত করুন যে আপনি একটি সঠিক সেটিংস template পাঠিয়েছেন।"
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ সেটিংস সফলভাবে import করা হয়েছে!\n\nপ্রয়োগ করা প্যারামিটার: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "মূল সেটিংস:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Import করা সেটিংস সংরক্ষণ করতে ত্রুটি।"
    ARGS_ERROR_IMPORTING_MSG = "❌ সেটিংস import করার সময় একটি ত্রুটি ঘটেছে।"

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Cookie Files ডাউনলোড করুন</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Cookie ফাইল ডাউনলোড করার জন্য একটি পরিষেবা নির্বাচন করুন।"
    COOKIE_MENU_SAVE_INFO_MSG = "Cookie ফাইলগুলি আপনার ফোল্ডারে cookie.txt হিসাবে সংরক্ষণ করা হবে।"
    COOKIE_MENU_TIP_HEADER_MSG = "টিপ: আপনি সরাসরি কমান্ডও ব্যবহার করতে পারেন:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – cookies ডাউনলোড এবং যাচাই করুন"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – index দ্বারা একটি নির্দিষ্ট উৎস ব্যবহার করুন (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "তারপর <code>/check_cookie</code> দিয়ে যাচাই করুন (RickRoll এ পরীক্ষা করে)।"

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "সবসময় জিজ্ঞাসা করুন"
    SUBS_AUTO_TRANS_BUTTON_MSG = "AUTO/TRANS"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗লিংক"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Watch"  # সাময়িকভাবে নিষ্ক্রিয়: poketube পরিষেবা ডাউন
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝বিবরণ"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ ট্রিম"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>ভিডিও ট্রিম</b>\n\nভিডিওর সময়কাল: <b>{start_time} - {end_time}</b>\n\nঅনুগ্রহ করে পছন্দসই সময় পরিসীমা ফরম্যাটে পাঠান:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nউদাহরণ: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ অবৈধ ফরম্যাট। অনুগ্রহ করে ব্যবহার করুন: <code>HH:MM:SS-HH:MM:SS</code>\n\nউদাহরণ: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ অবৈধ পরিসীমা। শুরুর সময় শেষ সময়ের চেয়ে কম হতে হবে।"
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ সময় পরিসীমা ভিডিওর সীমানার বাইরে।\n\nভিডিওর সময়কাল: <b>{start_time} - {end_time}</b>\n\nআপনার পরিসীমা এই সীমার মধ্যে হতে হবে।"
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>ভিডিও কাটা হবে:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ আংশিক সম্পন্ন - {successful_uploads}/{total_files} অডিও ফাইল আপলোড করা হয়েছে।"
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ অডিও সফলভাবে ডাউনলোড এবং পাঠানো হয়েছে - {total_files} ফাইল আপলোড করা হয়েছে।"

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>Private TikTok Account</b>\n\n"
        "এই TikTok অ্যাকাউন্টটি private বা সমস্ত ভিডিও private।\n\n"
        "<b>💡 সমাধান:</b>\n"
        "1. @{username} অ্যাকাউন্টটি follow করুন\n"
        "2. <code>/cookie</code> কমান্ড ব্যবহার করে আপনার cookies বটে পাঠান\n"
        "3. আবার চেষ্টা করুন\n\n"
        "<b>Cookies আপডেট করার পরে, আবার চেষ্টা করুন!</b>"
    )

    #######################################################
