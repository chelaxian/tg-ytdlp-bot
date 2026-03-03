# Messages Configuration
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from CONFIG.config import Config

class Messages(object):
    #######################################################
    # Messages and errors
    #######################################################
    CREDITS_MSG = "<blockquote><i>प्रबंधित</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 भाषा बदलें: /lang</b>"
    TO_USE_MSG = "<i>इस बॉट का उपयोग करने के लिए आपको @tg_ytdlp Telegram चैनल की सदस्यता लेनी होगी।</i>\nचैनल में शामिल होने के बाद <b>अपना वीडियो लिंक फिर से भेजें और बॉट इसे आपके लिए डाउनलोड कर देगा</b> ❤️\n\n<blockquote>P.S. संभावित 🔞NSFW सामग्री के कारण - ☁️<b>क्लाउड स्टोरेज</b>, 📁<b>फाइल शेयर</b>, 🔗<b>URL शॉर्टनर</b> और 🔞<b>पोर्न साइट्स</b> से डाउनलोड भुगतान योग्य है! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ @tg_ytdlp चैनल को 🗑<b>मत हटाएं/अनसब्सक्राइब मत करें</b> और बॉट को 🤖<b>बहुत ज्यादा URL/कमांड स्पैम मत भेजें</b> - आपको बॉट उपयोग से स्वचालित रूप से प्रतिबंधित कर दिया जाएगा ⛔️</blockquote>"

    ERROR1 = "URL लिंक नहीं मिला। कृपया <b>https://</b> या <b>http://</b> के साथ एक URL दर्ज करें"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>प्लेलिस्ट (yt-dlp)</b>

प्लेलिस्ट डाउनलोड करने के लिए अंत में <code>*start*end</code> रेंज के साथ इसका URL भेजें। उदाहरण: <code>URL*1*5</code> (पहले 5 वीडियो 1 से 5 तक समावेशी)। <code>URL*-1*-5</code> (अंतिम 5 वीडियो 1 से 5 तक समावेशी)।
या आप <code>/vid FROM-TO URL</code> का उपयोग कर सकते हैं। उदाहरण: <code>/vid 3-7 URL</code> (शुरुआत से 3 से 7 तक समावेशी वीडियो डाउनलोड करता है)। <code>/vid -3-7 URL</code> (अंत से 3 से 7 तक समावेशी वीडियो डाउनलोड करता है)। <code>/audio</code> कमांड के लिए भी काम करता है।

<b>उदाहरण:</b>

🟥 <b>YouTube प्लेलिस्ट से वीडियो रेंज:</b> (🍪 की आवश्यकता)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(1 से 5 तक के वीडियो डाउनलोड करता है)
🟥 <b>YouTube प्लेलिस्ट से एकल वीडियो:</b> (🍪 की आवश्यकता)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(केवल तीसरा वीडियो डाउनलोड करता है)

⬛️ <b>TikTok प्रोफाइल:</b> (आपके 🍪 की आवश्यकता)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(उपयोगकर्ता प्रोफाइल से पहले 10 वीडियो डाउनलोड करता है)

🟪 <b>Instagram कहानियां:</b> (आपके 🍪 की आवश्यकता)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(पहली 3 कहानियां डाउनलोड करता है)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(एल्बम से पहली 10 कहानियां डाउनलोड करता है)

🟦 <b>VK वीडियो:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(उपयोगकर्ता/समूह प्रोफाइल से पहले 3 वीडियो डाउनलोड करता है)

⬛️<b>Rutube चैनल:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(चैनल से 2 से 4 तक के वीडियो डाउनलोड करता है)

🟪 <b>Twitch क्लिप्स:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(चैनल से पहले 3 क्लिप्स डाउनलोड करता है)

🟦 <b>Vimeo समूह:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(समूह से पहले 2 वीडियो डाउनलोड करता है)

🟧 <b>Pornhub मॉडल:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(मॉडल प्रोफाइल से पहले 2 वीडियो डाउनलोड करता है)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(आपके प्रॉम्प्ट द्वारा खोज परिणामों से पहले 3 वीडियो डाउनलोड करता है)

और इसी तरह...
<a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">समर्थित साइटों की सूची</a> देखें
</blockquote>

<blockquote expandable>🖼 <b>छवियां (gallery-dl)</b>

कई प्लेटफॉर्म से छवियां/फोटो/एल्बम डाउनलोड करने के लिए <code>/img URL</code> का उपयोग करें।

<b>उदाहरण:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>रेंज:</b>
<code>/img 11-20 https://example.com/album</code> — आइटम 11..20
<code>/img 11- https://example.com/album</code> — 11 से अंत तक (या बॉट सीमा)

<i>समर्थित प्लेटफॉर्म में vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, आदि शामिल हैं। पूरी सूची:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">gallery-dl समर्थित साइटें</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>वीडियो डाउनलोड बॉट - सहायता</b>

📥 <b>मूल उपयोग:</b>
• कोई भी लिंक भेजें → बॉट इसे डाउनलोड करता है
  <i>बॉट स्वचालित रूप से yt-dlp के माध्यम से वीडियो और gallery-dl के माध्यम से छवियां डाउनलोड करने की कोशिश करता है।</i>
• <b>कई URL:</b> गुणवत्ता चयन मोड में (<code>/format</code>) आप एक संदेश में <b>10 URL</b> तक भेज सकते हैं । प्रत्येक URL एक नई पंक्ति पर या रिक्त स्थान से अलग।
• <code>/audio URL</code> → ऑडियो निकालें
• <code>/link [quality] URL</code> → प्रत्यक्ष लिंक प्राप्त करें
• <code>/proxy</code> → सभी डाउनलोड के लिए प्रॉक्सी सक्षम/अक्षम करें
• वीडियो पर टेक्स्ट के साथ जवाब दें → कैप्शन बदलें

📋 <b>प्लेलिस्ट और रेंज:</b>
• <code>URL*1*5</code> → पहले 5 वीडियो डाउनलोड करें
• <code>URL*-1*-5</code> → अंतिम 5 वीडियो डाउनलोड करें
• <code>/vid 3-7 URL</code> → <code>URL*3*7</code> बन जाता है
• <code>/vid -3-7 URL</code> → <code>URL*-3*-7</code> बन जाता है

🍪 <b>कुकीज़ और निजी:</b>
• निजी वीडियो के लिए *.txt कुकी अपलोड करें
• <code>/cookie [service]</code> → कुकीज़ डाउनलोड करें (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → इंडेक्स द्वारा स्रोत चुनें (1–N)
• <code>/cookies_from_browser</code> → ब्राउज़र से निकालें
• <code>/check_cookie</code> → कुकी सत्यापित करें
• <code>/save_as_cookie</code> → टेक्स्ट को कुकी के रूप में सहेजें

🧹 <b>सफाई:</b>
• <code>/clean</code> → केवल मीडिया फाइलें
• <code>/clean all</code> → सब कुछ
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>सेटिंग्स:</b>
• <code>/settings</code> → सेटिंग्स मेनू
• <code>/format</code> → गुणवत्ता और प्रारूप
• <code>/split</code> → वीडियो को भागों में विभाजित करें
• <code>/mediainfo on/off</code> → मीडिया जानकारी
• <code>/nsfw on/off</code> → NSFW धुंधलापन
• <code>/tags</code> → सहेजे गए टैग देखें
• <code>/sub on/off</code> → उपशीर्षक
• <code>/keyboard</code> → कीबोर्ड (OFF/1x3/2x3)

🏷️ <b>टैग:</b>
• URL के बाद <code>#tag1#tag2</code> जोड़ें
• टैग कैप्शन में दिखाई देते हैं
• <code>/tags</code> → सभी टैग देखें

🔗 <b>प्रत्यक्ष लिंक:</b>
• <code>/link URL</code> → सर्वोत्तम गुणवत्ता
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → विशिष्ट गुणवत्ता

⚙️ <b>त्वरित कमांड:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → गुणवत्ता सेट करें
• <code>/keyboard off/1x3/2x3/full</code> → कीबोर्ड लेआउट
• <code>/split 100mb-2000mb</code> → भाग आकार बदलें
• <code>/subs off/ru/en auto</code> → उपशीर्षक भाषा
• <code>/list URL</code> → उपलब्ध प्रारूपों की सूची
• <code>/mediainfo on/off</code> → मीडिया जानकारी चालू/बंद
• <code>/proxy on/off</code> → सभी डाउनलोड के लिए प्रॉक्सी सक्षम/अक्षम करें

📊 <b>जानकारी:</b>
• <code>/usage</code> → डाउनलोड इतिहास
• <code>/search</code> → @vid के माध्यम से इनलाइन खोज

🖼 <b>छवियां:</b>
• <code>URL</code> → छवि URL डाउनलोड करें
• <code>/img URL</code> → URL से छवियां डाउनलोड करें
• <code>/img 11-20 URL</code> → विशिष्ट रेंज डाउनलोड करें
• <code>/img 11- URL</code> → 11वें से अंत तक डाउनलोड करें

👨‍💻 <i>डेवलपर:</i> @upekshaip
🤝 <i>योगदानकर्ता:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "बस अपनी कुकी को <b><u>cookie.txt</u></b> के रूप में सहेजें और इसे बॉट को दस्तावेज़ के रूप में भेजें।\n\n"
        "आप <b><u>/save_as_cookie</u></b> कमांड के साथ कुकीज़ को सादे टेक्स्ट के रूप में भी भेज सकते हैं।\n"
        "<b><b><u>/save_as_cookie</u></b> का उपयोग:</b>\n\n"
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
        "<b><u>निर्देश:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>वीडियो खोज</b>

@vid के माध्यम से इनलाइन खोज सक्रिय करने के लिए नीचे दिए गए बटन को दबाएं।

<blockquote>PC पर बस किसी भी चैट में <b>"@vid Your_Search_Query"</b> टाइप करें।</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 छवि डाउनलोड कमांड</b>\n\n"
        "उपयोग: <code>/img URL</code>\n\n"
        "<b>उदाहरण:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>समर्थित प्लेटफॉर्म (उदाहरण):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, आदि — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">पूरी सूची</a></blockquote>"
        "यह भी देखें: "
    )
    
    LINK_HINT_MSG = (
        "गुणवत्ता चयन के साथ प्रत्यक्ष वीडियो लिंक प्राप्त करें।\n\n"
        "उपयोग: /link + URL \n\n"
        "(उदा. /link https://youtu.be/abc123)\n"
        "(उदा. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>बॉट को समूह में जोड़ें</b>

उन्नत सुविधाएं और उच्च सीमाएं प्राप्त करने के लिए मेरे बॉट्स को अपने समूहों में जोड़ें!
————————————
📊 <b>वर्तमान मुफ़्त सीमाएँ (बॉट के डीएम में):</b>
<blockquote>•🗑 सभी फाइलों से अव्यवस्थित कबाड़ 👎
• अधिकतम 1 फ़ाइल आकार: <b>8 GB </b>
• अधिकतम 1 फ़ाइल गुणवत्ता: <b>UNLIM</b>
• अधिकतम 1 फ़ाइल अवधि: <b>UNLIM</b>
• अधिकतम डाउनलोड संख्या: <b>UNLIM</b>
• एक संदेश में अधिकतम URL: <b>10</b> (केवल गुणवत्ता चयन मोड में)
• अधिकतम प्लेलिस्ट आइटम प्रति एक बार: <b>50</b>
• अधिकतम TikTok वीडियो प्रति एक बार: <b>500</b>
• अधिकतम छवियाँ प्रति एक बार: <b>1000</b>
• URL दर सीमाएं: <b>5/मिनट, 60/घंटा, 1000/दिन</b>
• कमांड सीमा: <b>20/मिनट</b>
• 1 डाउनलोड अधिकतम समय: <b>2 घंटे</b>
• 🔞 NSFW सामग्री का भुगतान किया जाता है! 1⭐️ = $0.02
• 🆓 सभी अन्य मीडिया पूरी तरह से मुफ़्त हैं
• 📝 सभी सामग्री लॉग और कैशिंग मेरे लॉग चैनल में तुरंत रीपोस्ट करने के लिए</blockquote>

💬<b>ये सीमाएं केवल सबस्क्रिप्ट वाले वीडियो के लिए हैं:</b>
<blockquote>• अधिकतम वीडियो+सबस्क्रिप्ट अवधि: <b>1.5 घंटे</b>
• अधिकतम वीडियो+सबस्क्रिप्ट फ़ाइल आकार: <b>500 MB</b>
• अधिकतम वीडियो+सबस्क्रिप्ट गुणवत्ता: <b>720p</b></blockquote>
————————————
🚀 <b>पेड समूह लाभ (2️⃣x सीमाएं):</b>
<blockquote>•  🗂 संरचित निष्क्रिय मीडिया वाल्ट टोपियों के अनुसार व्यवस्थित है 👍
•  📁 बॉट्स आपके बॉट्स को कॉल करने वाले टोपी में जवाब देते हैं
•  📌 डाउनलोड प्रगति के साथ स्थिति संदेश अपने लॉग चैनल में स्वचालित रूप से डाल दिया जाता है
•  🖼 /img कमांड मीडिया को 10-आइटम अल्बम के रूप में डाउनलोड करता है
• अधिकतम 1 फ़ाइल आकार: <b>16 GB</b> ⬆️
• एक संदेश में अधिकतम URL: <b>20</b> ⬆️ (केवल गुणवत्ता चयन मोड में)
• अधिकतम प्लेलिस्ट आइटम प्रति एक बार: <b>100</b> ⬆️
• अधिकतम TikTok वीडियो प्रति एक बार: 1000 ⬆️
• अधिकतम छवियाँ प्रति एक बार: 2000 ⬆️
• URL दर सीमाएं: <b>10/मिनट, 120/घंटा, 2000/दिन</b> ⬆️
• कमांड सीमा: <b>40/मिनट</b> ⬆️
• 1 डाउनलोड अधिकतम समय: <b>4 घंटे</b> ⬆️
• 🔞 NSFW सामग्री: पूर्ण मेटाडेटा के साथ मुफ़्त 🆓
• 📢 समूह के लिए मेरे चैनल को सदस्यता देने की आवश्यकता नहीं है
• 👥 सभी समूह सदस्य पेड कार्यों तक पहुँच होंगे!
• 🗒 कोई लॉग / कोई कैश मेरे लॉग चैनल में नहीं है! आप समूह सेटिंग्स में कॉपी/रीपोस्ट को अस्वीकार कर सकते हैं</blockquote>

💬 <b>उपशीर्षक वाले वीडियो के लिए 2️⃣x सीमाएँ:</b>
<blockquote>• अधिकतम वीडियो+सबस्क्रिप्ट अवधि: <b>3 घंटे</b> ⬆️
• अधिकतम वीडियो+सबस्क्रिप्ट फ़ाइल आकार: <b>1000 MB</b> ⬆️
• अधिकतम वीडियो+सबस्क्रिप्ट गुणवत्ता: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>मूल्य निर्धारण और सेटअप:</b>
<blockquote>• मूल्य: समूह में प्रति 1 बॉट <b>$5/माह</b>
• सेटअप: Contact @iilililiiillliiliililliilliliiil
• भुगतान: 💎TON या अन्य तरीके💲
• समर्थन: पूर्ण तकनीकी समर्थन समाहित है</blockquote>
————————————
आप मेरे बॉट्स को अपने समूह में जोड़ सकते हैं और मुफ़्त 🔞<b>NSFW</b> को अनलॉक कर सकते हैं और सभी सीमाओं को दोगुना (x2️⃣) कर सकते हैं.
मुझे संपर्क करें अगर आप मेरे बॉट्स का उपयोग करने की अनुमति देना चाहते हैं @iilililiiillliiliililliilliliiil
————————————
💡<b>TIP:</b> <blockquote>आप अपने दोस्तों के साथ किसी भी राशि के साथ पैसे चिपका सकते हैं (उदाहरण के लिए 100 लोग) और समूह के लिए 1 खरीद कर सकते हैं - सभी समूह सदस्य उस समूह में सभी बॉट्स कार्यों तक पूर्ण अनिश्चित पहुँच प्राप्त करेंगे केवल <b>0.05$</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW मोड: चालू✅</b>

• NSFW सामग्री बिना धुंधले प्रदर्शित की जाएगी।
• स्पॉयलर NSFW मीडिया पर लागू नहीं होंगे।
• सामग्री तुरंत दिखाई देगी

<i>धुंधलापन सक्षम करने के लिए /nsfw off का उपयोग करें</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW मोड: बंद</b>

⚠️ <b>धुंधलापन सक्षम</b>
• NSFW सामग्री स्पॉइलर के नीचे छिपा दी जाएगी
• देखने के लिए, आपको मीडिया पर क्लिक करना होगा
• स्पॉइलर NSFW मीडिया पर लागू होंगे।

<i>धुंधलापन बंद करने के लिए /nsfw on का उपयोग करें</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>अमान्य पैरामीटर</b>

उपयोग:
• <code>/nsfw on</code> - धुंधलापन बंद करें
• <code>/nsfw off</code> - धुंधलापन सक्षम करें
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>कैश जांच रहा है...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 प्रसंस्करण..."
    DOWNLOADING_MSG = "📥 <b>मीडिया डाउनलोड हो रहा है...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>छवि डाउनलोड हो रही है...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>डाउनलोड पूरा</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "डाउनलोड किया गया:"
    SENT_STATUS_MSG = "भेजा गया:"
    PENDING_TO_SEND_STATUS_MSG = "भेजने की प्रतीक्षा में:"
    TITLE_LABEL_MSG = "शीर्षक:"
    MEDIA_COUNT_LABEL_MSG = "मीडिया की संख्या:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "डाउनलोड पूरा हुआ, ऑडियो प्रोसेसिंग..."
    VIDEO_PROCESSING_MSG = "📽 वीडियो प्रसंस्करण में है..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>कैश से भेजा गया</b>\n\nभेजे गए एल्बम: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ वीडियो कैश से सफलतापूर्वक भेजा गया।"
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ प्लेलिस्ट वीडियो कैश से भेजे गए ({cached}/{total} फाइलें)।"
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} वीडियो कैश से भेजे गए, लापता वाले डाउनलोड हो रहे हैं..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ कैश से भेजा गया: {cached}\n🔄 डाउनलोड जारी है..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 मीडिया का विश्लेषण नहीं कर सका, अधिकतम अनुमतित रेंज (1-{fallback_limit}) के साथ आगे बढ़ रहे हैं..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 मीडिया की संख्या निर्धारित नहीं कर सका, अधिकतम अनुमतित रेंज (1-{total_limit}) के साथ आगे बढ़ रहे हैं..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 कुल मीडिया संख्या निर्धारित नहीं कर सका, निर्दिष्ट रेंज {start}-{end} के साथ आगे बढ़ रहे हैं..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>अमान्य URL</b>\n\nकृपया http:// या https:// से शुरू होने वाला एक वैध URL प्रदान करें"

    ERROR_OCCURRED_MSG = "❌ <b>त्रुटि हुई</b>\n\n<code>{url}</code>\n\nत्रुटि: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ वीडियो भेजने में त्रुटि: {error}"
    ERROR_UNKNOWN_MSG = "❌ अज्ञात त्रुटि: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ वीडियो डाउनलोड करने के लिए पर्याप्त डिस्क स्थान नहीं है।"
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ फाइल का आकार {limit} GB सीमा से अधिक है। कृपया अनुमतित आकार के भीतर एक छोटी फाइल चुनें।"
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>सभी उपलब्ध प्रॉक्सी के साथ वीडियो डाउनलोड करने में विफल</b>\n\nप्रॉक्सी के माध्यम से सभी डाउनलोड प्रयास विफल रहे।\nकोशिश करें:\n• प्रॉक्सी की कार्यक्षमता की जांच करें\n• सूची से दूसरे प्रॉक्सी को आज़माएं\n• प्रॉक्सी के बिना डाउनलोड करें (यदि संभव हो)"

    ERROR_GETTING_LINK_MSG = "❌ <b>लिंक प्राप्त करने में त्रुटि:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram ने संदेश भेजने को सीमित कर दिया है।\n⏳ कृपया प्रतीक्षा करें: {time}\nटाइमर अपडेट करने के लिए URL को फिर से 2 बार भेजें।"
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram ने संदेश भेजने को सीमित कर दिया है।\n⏳ कृपया प्रतीक्षा करें: \nटाइमर अपडेट करने के लिए URL को फिर से 2 बार भेजें।"
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ उपशीर्षक डाउनलोड करने में विफल"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>प्रत्यक्ष स्ट्रीम लिंक</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>शीर्षक:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>अवधि:</b> {duration} सेकंड\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ त्रुटि: मूल संदेश नहीं मिला।"

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ टैग #{tag} में निषिद्ध वर्ण हैं। केवल अक्षर, अंक और _ की अनुमति है।\nकृपया उपयोग करें: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ प्लेलिस्ट वीडियो भेजे गए: {sent}/{total} फाइलें।"
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>प्लेलिस्ट सुझाव</b>

आपने बिना रेंज निर्दिष्ट किए प्लेलिस्ट लिंक भेजा। बॉट ने स्वचालित रूप से पहला वीडियो डाउनलोड किया (<code>*1*1</code>).

<b>प्लेलिस्ट से कई वीडियो डाउनलोड करने के लिए, रेंज निर्दिष्ट करें:</b>
• <code>URL*1*5</code> — पहले 5 वीडियो (1 से 5 तक सम्मिलित)
• <code>URL*3*3</code> — केवल तीसरा वीडियो
• <code>/vid 1-10 URL</code> — वैकल्पिक प्रारूप

अधिक जानें: /playlist"""
    PLAYLIST_CACHE_SENT_MSG = "✅ कैश से भेजा गया: {cached}/{total} फाइलें।"
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ स्ट्रीम लिंक प्राप्त करने में विफल"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "कुकीज़ डाउनलोड करने के लिए एक ब्राउज़र चुनें:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "इस सिस्टम पर कोई ब्राउज़र नहीं मिला। आप रिमोट URL से कुकीज़ डाउनलोड कर सकते हैं या ब्राउज़र स्थिति की निगरानी कर सकते हैं:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>ब्राउज़र खोलें</b> - मिनी-ऐप में ब्राउज़र स्थिति की निगरानी के लिए"
    BROWSER_OPEN_BUTTON_MSG = "🌐 ब्राउज़र खोलें"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 रिमोट URL से डाउनलोड करें"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube कुकी फाइल फॉलबैक के माध्यम से डाउनलोड की गई और cookie.txt के रूप में सहेजी गई"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ कोई समर्थित ब्राउज़र नहीं मिला और कोई COOKIE_URL कॉन्फ़िगर नहीं है। /cookie का उपयोग करें या cookie.txt अपलोड करें।"
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ फॉलबैक COOKIE_URL एक .txt फाइल की ओर इंगित करना चाहिए।"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ फॉलबैक कुकी फाइल बहुत बड़ी है (>100KB)।"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ फॉलबैक कुकी स्रोत उपलब्ध नहीं है (स्थिति {status})। /cookie का उपयोग करें या cookie.txt अपलोड करें।"
    COOKIE_FALLBACK_ERROR_MSG = "❌ फॉलबैक कुकी डाउनलोड करने में त्रुटि। /cookie का उपयोग करें या cookie.txt अपलोड करें।"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ फॉलबैक कुकी डाउनलोड के दौरान अप्रत्याशित त्रुटि।"
    BTN_CLOSE = "🔚बंद करें"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ अमान्य बूलियन मान"
    ARGS_CLOSED_MSG = "बंद"
    ARGS_ALL_RESET_MSG = "✅ सभी तर्क रीसेट"
    ARGS_RESET_ERROR_MSG = "❌ तर्क रीसेट करने में त्रुटि"
    ARGS_INVALID_PARAM_MSG = "❌ अमान्य पैरामीटर"
    ARGS_BOOL_SET_MSG = "{value} पर सेट किया गया"
    ARGS_BOOL_ALREADY_SET_MSG = "पहले से {value} पर सेट है"
    ARGS_INVALID_SELECT_MSG = "❌ अमान्य चयन मान"
    ARGS_VALUE_SET_MSG = "{value} पर सेट किया गया"
    ARGS_VALUE_ALREADY_SET_MSG = "पहले से {value} पर सेट है"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>वर्तमान मान:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>उदाहरण:</b>\n• <code>default</code> - डिफ़ॉल्ट XFF रणनीति का उपयोग करें\n• <code>never</code> - XFF हेडर का कभी उपयोग न करें\n• <code>US</code> - संयुक्त राज्य अमेरिका देश कोड\n• <code>GB</code> - यूनाइटेड किंगडम देश कोड\n• <code>DE</code> - जर्मनी देश कोड\n• <code>FR</code> - फ्रांस देश कोड\n• <code>JP</code> - जापान देश कोड\n• <code>192.168.1.0/24</code> - IP ब्लॉक (CIDR)\n• <code>10.0.0.0/8</code> - निजी IP रेंज\n• <code>203.0.113.0/24</code> - सार्वजनिक IP ब्लॉक\n\n"
    ARGS_XFF_NOTE_MSG = "<b>नोट:</b> यह --geo-bypass विकल्पों को प्रतिस्थापित करता है। CIDR नोटेशन में कोई भी 2-अक्षर देश कोड या IP ब्लॉक का उपयोग करें।\n\n"
    ARGS_EXAMPLE_MSG = "<b>उदाहरण:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "कृपया अपना नया मान भेजें।"
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>रेंज:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "कृपया एक संख्या भेजें।"
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>उदाहरण:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>नोट:</b> ये हेडर मौजूदा Referer और उपयोगकर्ता-एजेंट हेडर में जोड़े जाएंगे।\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 वर्तमान yt-dlp तर्क:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>बूलियन</b> - सही/गलत स्विच\n• 📋 <b>चयन</b> - विकल्पों में से चुनें\n• 🔢 <b>संख्यात्मक</b> - संख्या इनपुट\n• 📝🔧 <b>पाठ</b> - पाठ/JSON इनपुट</blockquote>\n\nये सेटिंग्स आपके सभी डाउनलोड पर लागू होंगी।"
    
    # प्रदर्शन के लिए स्थानीयकृत पैरामीटर नाम
    ARGS_PARAM_NAMES = {
        "force_ipv6": "IPv6 कनेक्शन को मजबूर करें",
        "force_ipv4": "IPv4 कनेक्शन को मजबूर करें", 
        "no_live_from_start": "लाइव स्ट्रीम को शुरुआत से डाउनलोड न करें",
        "live_from_start": "लाइव स्ट्रीम को शुरुआत से डाउनलोड करें",
        "no_check_certificates": "HTTPS सर्टिफिकेट सत्यापन को दबाएं",
        "check_certificate": "SSL सर्टिफिकेट जांचें",
        "no_playlist": "केवल एक वीडियो डाउनलोड करें, प्लेलिस्ट नहीं",
        "embed_metadata": "वीडियो फाइल में मेटाडेटा एम्बेड करें",
        "embed_thumbnail": "वीडियो फाइल में थंबनेल एम्बेड करें",
        "write_thumbnail": "थंबनेल को फाइल में लिखें",
        "ignore_errors": "डाउनलोड त्रुटियों को नजरअंदाज करें और जारी रखें",
        "legacy_server_connect": "पुराने सर्वर कनेक्शन की अनुमति दें",
        "concurrent_fragments": "डाउनलोड के लिए समवर्ती फ्रैगमेंट की संख्या",
        "xff": "X-Forwarded-For हेडर रणनीति",
        "user_agent": "User-Agent हेडर",
        "impersonate": "ब्राउज़र नकली",
        "referer": "Referer हेडर",
        "geo_bypass": "भौगोलिक प्रतिबंधों को बायपास करें",
        "hls_use_mpegts": "HLS के लिए MPEG-TS का उपयोग करें",
        "no_part": ".part फाइलों का उपयोग न करें",
        "no_continue": "आंशिक डाउनलोड को फिर से शुरू न करें",
        "audio_format": "ऑडियो प्रारूप",
        "video_format": "वीडियो प्रारूप",
        "merge_output_format": "मर्ज आउटपुट प्रारूप",
        "send_as_file": "फाइल के रूप में भेजें",
        "username": "उपयोगकर्ता नाम",
        "password": "पासवर्ड",
        "twofactor": "दो-कारक प्रमाणीकरण कोड",
        "min_filesize": "न्यूनतम फाइल आकार (MB)",
        "max_filesize": "अधिकतम फाइल आकार (MB)",
        "playlist_items": "प्लेलिस्ट आइटम",
        "date": "तारीख",
        "datebefore": "तारीख से पहले",
        "dateafter": "तारीख के बाद",
        "http_headers": "HTTP हेडर",
        "sleep_interval": "स्लीप अंतराल",
        "max_sleep_interval": "अधिकतम स्लीप अंतराल",
        "retries": "पुनर्प्रयास की संख्या",
        "http_chunk_size": "HTTP चंक आकार",
        "sleep_subtitles": "सबटाइटल के लिए स्लीप"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp तर्क कॉन्फ़िगरेशन</b>\n\n<blockquote>📋 <b>समूह:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp तर्क कॉन्फ़िगरेशन</b>\n\n"
        "<blockquote>📋 <b>समूह:</b>\n"
        "• ✅/❌ <b>बूलियन</b> - सही/गलत स्विच\n"
        "• 📋 <b>चयन</b> - विकल्पों में से चुनें\n"
        "• 🔢 <b>संख्यात्मक</b> - संख्या इनपुट\n"
        "• 📝🔧 <b>पाठ</b> - पाठ/JSON इनपुट</blockquote>\n\n"
        "ये सेटिंग्स आपके सभी डाउनलोड पर लागू होंगी।"
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ कृपया प्रतीक्षा करें..."
    ERROR_OCCURRED_SHORT_MSG = "❌ त्रुटि हुई"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ निष्क्रियता के कारण इनपुट मोड स्वचालित रूप से बंद हो गया (5 मिनट)।"
    ARGS_INPUT_DANGEROUS_MSG = "❌ इनपुट में संभावित खतरनाक सामग्री है: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ इनपुट बहुत लंबा है (अधिकतम 1000 वर्ण)"
    ARGS_INVALID_URL_MSG = "❌ अमान्य URL प्रारूप। http:// या https:// से शुरू होना चाहिए"
    ARGS_INVALID_JSON_MSG = "❌ अमान्य JSON प्रारूप"
    ARGS_NUMBER_RANGE_MSG = "❌ संख्या {min_val} और {max_val} के बीच होनी चाहिए"
    ARGS_INVALID_NUMBER_MSG = "❌ अमान्य संख्या प्रारूप"
    ARGS_DATE_FORMAT_MSG = "❌ दिनांक YYYYMMDD प्रारूप में होना चाहिए (उदाहरण: 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ वर्ष 1900 और 2100 के बीच होना चाहिए"
    ARGS_MONTH_RANGE_MSG = "❌ महीना 01 और 12 के बीच होना चाहिए"
    ARGS_DAY_RANGE_MSG = "❌ दिन 01 और 31 के बीच होना चाहिए"
    ARGS_INVALID_DATE_MSG = "❌ अमान्य दिनांक प्रारूप"
    ARGS_INVALID_XFF_MSG = "❌ XFF 'default', 'never', देश कोड (उदाहरण: US), या IP ब्लॉक (उदाहरण: 192.168.1.0/24) होना चाहिए"
    ARGS_NO_CUSTOM_MSG = "कोई कस्टम तर्क सेट नहीं है। सभी पैरामीटर डिफ़ॉल्ट मानों का उपयोग करते हैं।"
    ARGS_RESET_SUCCESS_MSG = "✅ सभी तर्क डिफ़ॉल्ट पर रीसेट हो गए।"
    ARGS_TEXT_TOO_LONG_MSG = "❌ पाठ बहुत लंबा है। अधिकतम 500 वर्ण।"
    ARGS_ERROR_PROCESSING_MSG = "❌ इनपुट प्रसंस्करण में त्रुटि। कृपया फिर से कोशिश करें।"
    ARGS_BOOL_INPUT_MSG = "❌ Send As File विकल्प के लिए कृपया 'True' या 'False' दर्ज करें।"
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ कृपया एक वैध संख्या प्रदान करें।"
    ARGS_BOOL_VALUE_REQUEST_MSG = "इस विकल्प को सक्षम/अक्षम करने के लिए कृपया <code>True</code> या <code>False</code> भेजें।"
    ARGS_JSON_VALUE_REQUEST_MSG = "कृपया वैध JSON भेजें।"
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "आपके पास अभी तक कोई टैग नहीं है।"
    TAGS_MESSAGE_CLOSED_MSG = "टैग संदेश बंद।"
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ उपशीर्षक अक्षम और हमेशा पूछें मोड बंद।"
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ सब्स हमेशा पूछें सक्षम।"
    SUBS_LANGUAGE_SET_MSG = "✅ उपशीर्षक भाषा सेट की गई: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️चेतावनी: उच्च CPU प्रभाव के कारण यह फ़ंक्शन बहुत धीमा है (लगभग वास्तविक समय) और सीमित है:\n"
        "- 720p अधिकतम गुणवत्ता\n"
        "- 1.5 घंटे अधिकतम अवधि\n"
        "- 500mb अधिकतम वीडियो आकार</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>त्वरित कमांड:</b>\n"
        "• <code>/subs off</code> - उपशीर्षक अक्षम करें\n"
        "• <code>/subs on</code> - हमेशा पूछें मोड सक्षम करें\n"
        "• <code>/subs ru</code> - भाषा सेट करें\n"
        "• <code>/subs ru auto</code> - AUTO/TRANS के साथ भाषा सेट करें"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 उपशीर्षक अक्षम हैं"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} चयनित भाषा: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 उपशीर्षक डाउनलोड हो रहे हैं..."
    SUBS_DISABLED_ERROR_MSG = "❌ उपशीर्षक अक्षम हैं। कॉन्फ़िगर करने के लिए /subs का उपयोग करें।"
    SUBS_YOUTUBE_ONLY_MSG = "❌ उपशीर्षक डाउनलोड केवल YouTube के लिए समर्थित है।"
    SUBS_CAPTION_MSG = (
        "<b>💬 उपशीर्षक</b>\n\n"
        "<b>वीडियो:</b> {title}\n"
        "<b>भाषा:</b> {lang}\n"
        "<b>प्रकार:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 उपशीर्षक SRT-फाइल उपयोगकर्ता को भेजी गई।"
    SUBS_ERROR_PROCESSING_MSG = "❌ उपशीर्षक फाइल प्रसंस्करण में त्रुटि।"
    SUBS_ERROR_DOWNLOAD_MSG = "❌ उपशीर्षक डाउनलोड करने में विफल।"
    SUBS_ERROR_MSG = "❌ उपशीर्षक डाउनलोड करने में त्रुटि: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ विभाजन भाग आकार सेट किया गया: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **अमान्य आकार!**\n\n"
        "**वैध रेंज:** 100MB से 2GB\n\n"
        "**वैध प्रारूप:**\n"
        "• `100mb` से `2000mb` (मेगाबाइट)\n"
        "• `0.1gb` से `2gb` (गीगाबाइट)\n\n"
        "**उदाहरण:**\n"
        "• `/split 100mb` - 100 मेगाबाइट\n"
        "• `/split 500mb` - 500 मेगाबाइट\n"
        "• `/split 1.5gb` - 1.5 गीगाबाइट\n"
        "• `/split 2gb` - 2 गीगाबाइट\n"
        "• `/split 2000mb` - 2000 मेगाबाइट (2GB)\n\n"
        "**प्रीसेट:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **वीडियो विभाजन के लिए अधिकतम भाग आकार चुनें:**\n\n"
        "**रेंज:** 100MB से 2GB\n\n"
        "**त्वरित कमांड:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**उदाहरण:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "मेनू बंद।"
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>बॉट सेटिंग्स</b>\n\nएक श्रेणी चुनें:"
    SETTINGS_MENU_CLOSED_MSG = "मेनू बंद।"
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 सफाई विकल्प</b>\n\nक्या साफ करना है चुनें:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 कुकीज़</b>\n\nएक क्रिया चुनें:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 मीडिया</b>\n\nएक क्रिया चुनें:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 जानकारी</b>\n\nएक क्रिया चुनें:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ अधिक कमांड</b>\n\nएक क्रिया चुनें:"
    SETTINGS_COMMAND_EXECUTED_MSG = "कमांड निष्पादित।"
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ फ्लड सीमा। बाद में कोशिश करें।"
    SETTINGS_HINT_SENT_MSG = "संकेत भेजा गया।"
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "खोज सहायक खोला गया।"
    SETTINGS_UNKNOWN_COMMAND_MSG = "अज्ञात कमांड।"
    SETTINGS_HINT_CLOSED_MSG = "संकेत बंद।"
    SETTINGS_HELP_SENT_MSG = "उपयोगकर्ता को सहायता txt भेजें"
    SETTINGS_MENU_OPENED_MSG = "/settings मेनू खोला गया"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 खोज सहायक बंद"
    SEARCH_CLOSED_MSG = "बंद"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ प्रॉक्सी {status}।"
    PROXY_ERROR_SAVING_MSG = "❌ प्रॉक्सी सेटिंग्स सहेजने में त्रुटि।"
    PROXY_MENU_TEXT_MSG = "सभी yt-dlp ऑपरेशन के लिए प्रॉक्सी सर्वर का उपयोग सक्षम या अक्षम करें?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "सभी yt-dlp परिचालनों के लिए प्रॉक्सी सर्वर ({config_count} + {file_count} उपलब्ध) का उपयोग सक्षम या अक्षम करें?\n\nसभी (ऑटो) सक्षम होने पर, प्रॉक्सी अनुमत देशों (YouTube त्रुटि में दिए गए) के अनुसार स्वचालित रूप से चुने जाते हैं।"
    PROXY_MENU_CLOSED_MSG = "मेनू बंद।"
    PROXY_ENABLED_CONFIRM_MSG = "✅ प्रॉक्सी सक्षम। सभी yt-dlp ऑपरेशन प्रॉक्सी का उपयोग करेंगे।"
    PROXY_ENABLED_MULTIPLE_MSG = "✅ प्रॉक्सी सक्षम। सभी yt-dlp ऑपरेशन {method} चयन विधि के साथ {count} प्रॉक्सी सर्वर का उपयोग करेंगे।"

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ प्रॉक्सी चालू (YouTube त्रुटि पर ऑटो)।\n\nजब YouTube जियो-ब्लॉक त्रुटि देगा तो बॉट सिर्फ उस त्रुटि में दिए देशों के प्रॉक्सी इस्तेमाल करेगा (सभी प्रॉक्सी क्रम से नहीं आज़माए जाएंगे)।"
    PROXY_DISABLED_MSG = "❌ प्रॉक्सी अक्षम।"
    PROXY_TRYING_COUNTRY_MSG = "🔄 प्रॉक्सी आज़मा रहे हैं: {country} ({current}/{total})"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ प्रॉक्सी सेटिंग्स सहेजने में त्रुटि।"
    PROXY_ENABLED_CALLBACK_MSG = "प्रॉक्सी सक्षम।"
    PROXY_DISABLED_CALLBACK_MSG = "प्रॉक्सी अक्षम।"
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ अपना पिछला डाउनलोड समाप्त होने तक प्रतीक्षा करें"
    AUDIO_HELP_MSG = (
        "<b>🎧 ऑडियो डाउनलोड कमांड</b>\n\n"
        "उपयोग: <code>/audio URL</code>\n\n"
        "<b>उदाहरण:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "यह भी देखें: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "ऑडियो संकेत बंद।"
    PLAYLIST_HELP_CLOSED_MSG = "प्लेलिस्ट सहायता बंद।"
    USERLOGS_CLOSED_MSG = "लॉग संदेश बंद।"
    HELP_CLOSED_MSG = "सहायता बंद।"
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW धुंधलापन सेटिंग्स</b>\n\nNSFW सामग्री <b>{status}</b> है।\n\nNSFW सामग्री को धुंधला करना है या नहीं चुनें:"
    NSFW_MENU_CLOSED_MSG = "मेनू बंद।"
    NSFW_BLUR_DISABLED_MSG = "NSFW धुंधलापन अक्षम।"
    NSFW_BLUR_ENABLED_MSG = "NSFW धुंधलापन सक्षम।"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW धुंधलापन अक्षम।"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW धुंधलापन सक्षम।"
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}।"
    MEDIAINFO_MENU_TITLE_MSG = "डाउनलोड की गई फाइलों के लिए MediaInfo भेजना सक्षम या अक्षम करें?"
    MEDIAINFO_MENU_CLOSED_MSG = "मेनू बंद।"
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo सक्षम। डाउनलोड के बाद, फाइल जानकारी भेजी जाएगी।"
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo अक्षम।"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo सक्षम।"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo अक्षम।"
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 उपलब्ध प्रारूप सूची</b>\n\n"
        "URL के लिए उपलब्ध वीडियो/ऑडियो प्रारूप प्राप्त करें।\n\n"
        "<b>उपयोग:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>उदाहरण:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 प्रारूप ID का उपयोग कैसे करें:</b>\n"
        "सूची प्राप्त करने के बाद, विशिष्ट प्रारूप ID का उपयोग करें:\n"
        "• <code>/format id 401</code> - प्रारूप 401 डाउनलोड करें\n"
        "• <code>/format id401</code> - ऊपर के समान\n"
        "• <code>/format id140 audio</code> - प्रारूप 140 को MP3 ऑडियो के रूप में डाउनलोड करें\n\n"
        "यह कमांड सभी उपलब्ध प्रारूप दिखाएगा जिन्हें डाउनलोड किया जा सकता है।"
    )
    LIST_PROCESSING_MSG = "🔄 उपलब्ध प्रारूप प्राप्त कर रहे हैं..."
    LIST_INVALID_URL_MSG = "❌ कृपया http:// या https:// से शुरू होने वाला एक वैध URL प्रदान करें"
    LIST_CAPTION_MSG = (
        "📃 के लिए उपलब्ध प्रारूप:\n<code>{url}</code>\n\n"
        "💡 <b>प्रारूप कैसे सेट करें:</b>\n"
        "• <code>/format id 134</code> - विशिष्ट प्रारूप ID डाउनलोड करें\n"
        "• <code>/format 720p</code> - गुणवत्ता के अनुसार डाउनलोड करें\n"
        "• <code>/format best</code> - सर्वोत्तम गुणवत्ता डाउनलोड करें\n"
        "• <code>/format ask</code> - हमेशा गुणवत्ता के लिए पूछें\n\n"
        "{audio_note}\n"
        "📋 ऊपर की सूची से प्रारूप ID का उपयोग करें"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>केवल ऑडियो प्रारूप:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - प्रारूप 140 को MP3 ऑडियो के रूप में डाउनलोड करें\n"
        "• <code>/format id140 audio</code> - ऊपर के समान\n"
        "ये MP3 ऑडियो फाइलों के रूप में डाउनलोड होंगे।\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ प्रारूप फाइल भेजने में त्रुटि: {error}"
    LIST_ERROR_GETTING_MSG = "❌ प्रारूप प्राप्त करने में विफल:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ कमांड प्रसंस्करण के दौरान त्रुटि हुई"
    LIST_ERROR_CALLBACK_MSG = "त्रुटि हुई"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 प्रारूप ID का उपयोग कैसे करें:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "सूची प्राप्त करने के बाद, विशिष्ट प्रारूप ID का उपयोग करें:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - प्रारूप 401 डाउनलोड करें\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - ऊपर के समान\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - प्रारूप 140 को MP3 ऑडियो के रूप में डाउनलोड करें\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - ऊपर के समान\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 केवल ऑडियो प्रारूप का पता चला: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "ये प्रारूप MP3 ऑडियो फाइलों के रूप में डाउनलोड होंगे।\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>केवल वीडियो प्रारूप:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 ऊपर की सूची से प्रारूप ID का उपयोग करें"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>उपयोग:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>उदाहरण:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - सर्वोत्तम गुणवत्ता\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p या नीचे\n"
        "• /link 720p https://youtube.com/watch?v=... - ऊपर के समान\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K या नीचे\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K या नीचे"
        "</blockquote>\n\n"
        "<b>गुणवत्ता:</b> 1 से 10000 तक (उदाहरण: 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ कृपया एक वैध URL प्रदान करें"
    LINK_PROCESSING_MSG = "🔗 प्रत्यक्ष लिंक प्राप्त कर रहे हैं..."
    LINK_DURATION_MSG = "⏱ <b>अवधि:</b> {duration} सेकंड\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>वीडियो स्ट्रीम:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>ऑडियो स्ट्रीम:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **कीबोर्ड सेटिंग अपडेट!**\n\nनई सेटिंग: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **अमान्य तर्क!**\n\n"
        "वैध विकल्प: `off`, `1x3`, `2x3`, `full`\n\n"
        "उदाहरण: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **कीबोर्ड सेटिंग्स**\n\n"
        "वर्तमान: **{current}**\n\n"
        "एक विकल्प चुनें:\n\n"
        "या उपयोग करें: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 कीबोर्ड सक्रिय!"
    KEYBOARD_HIDDEN_MSG = "⌨️ कीबोर्ड छुपा"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3 कीबोर्ड सक्रिय!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3 कीबोर्ड सक्रिय!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 इमोजी कीबोर्ड सक्रिय!"
    KEYBOARD_ERROR_APPLYING_MSG = "कीबोर्ड सेटिंग {setting} लागू करने में त्रुटि: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ प्रारूप सेट किया गया: हमेशा पूछें। आपको हर बार URL भेजने पर गुणवत्ता के लिए पूछा जाएगा।"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ प्रारूप सेट किया गया: हमेशा पूछें। अब आपको हर बार URL भेजने पर गुणवत्ता के लिए पूछा जाएगा।"
    FORMAT_BEST_UPDATED_MSG = "✅ प्रारूप सर्वोत्तम गुणवत्ता (AVC+MP4 प्राथमिकता) पर अपडेट किया गया:\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ प्रारूप ID {id} पर अपडेट किया गया:\n{format}\n\n💡 <b>नोट:</b> यदि यह केवल ऑडियो प्रारूप है, तो इसे MP3 ऑडियो फाइल के रूप में डाउनलोड किया जाएगा।"
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ प्रारूप ID {id} (केवल ऑडियो) पर अपडेट किया गया:\n{format}\n\n💡 यह MP3 ऑडियो फाइल के रूप में डाउनलोड होगा।"
    FORMAT_QUALITY_UPDATED_MSG = "✅ प्रारूप गुणवत्ता {quality} पर अपडेट किया गया:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ प्रारूप अपडेट किया गया:\n{format}"
    FORMAT_MENU_MSG = (
        "एक प्रारूप विकल्प चुनें या कस्टम भेजें:\n"
        "• <code>/format &lt;format_string&gt;</code> - कस्टम प्रारूप\n"
        "• <code>/format 720</code> - 720p गुणवत्ता\n"
        "• <code>/format 4k</code> - 4K गुणवत्ता\n"
        "• <code>/format 8k</code> - 8K गुणवत्ता\n"
        "• <code>/format id 401</code> - विशिष्ट प्रारूप ID\n"
        "• <code>/format ask</code> - हमेशा मेनू दिखाएं\n"
        "• <code>/format best</code> - bv+ba/सर्वोत्तम गुणवत्ता"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "कस्टम प्रारूप का उपयोग करने के लिए, कमांड को निम्नलिखित रूप में भेजें:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "<code>bestvideo+bestaudio/best</code> को अपनी वांछित प्रारूप स्ट्रिंग से बदलें।"
    )
    FORMAT_RESOLUTION_MENU_MSG = "अपना वांछित रिज़ॉल्यूशन और कोडेक चुनें:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ प्रारूप सेट किया गया: हमेशा पूछें। अब आपको हर बार URL भेजने पर गुणवत्ता के लिए पूछा जाएगा।"
    FORMAT_UPDATED_MSG = "✅ प्रारूप अपडेट किया गया:\n{format}"
    FORMAT_SAVED_MSG = "✅ प्रारूप सहेजा गया।"
    FORMAT_CHOICE_UPDATED_MSG = "✅ प्रारूप विकल्प अपडेट किया गया।"
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "कस्टम प्रारूप मेनू बंद"
    FORMAT_CODEC_SET_MSG = "✅ कोडेक {codec} पर सेट किया गया"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ ब्राउज़र विकल्प अपडेट किया गया।"
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ पहुंच अस्वीकृत। केवल व्यवस्थापक।"
    ACCESS_DENIED_ADMIN = "❌ पहुंच अस्वीकृत। केवल व्यवस्थापक।"
    WELCOME_MASTER = "स्वागत है मास्टर 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ क्षमा करें... डाउनलोड के दौरान कुछ त्रुटि हुई।"
    SIZE_LIMIT_EXCEEDED = "❌ फाइल का आकार {max_size_gb} GB सीमा से अधिक है। कृपया अनुमतित आकार के भीतर एक छोटी फाइल चुनें।"
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ स्क्रिप्ट नहीं मिली: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ {script_path} का उपयोग करके ताजा Firebase डंप डाउनलोड हो रहा है..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase कैश सफलतापूर्वक रीलोड किया गया!"
    ADMIN_CACHE_FAILED_MSG = "❌ Firebase कैश रीलोड करने में विफल। जांचें कि {cache_file} मौजूद है या नहीं।"
    ADMIN_ERROR_RELOADING_MSG = "❌ कैश रीलोड करने में त्रुटि: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ {script_path} चलाने में त्रुटि:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ प्रोमो संदेश सभी अन्य उपयोगकर्ताओं को भेजा गया</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ प्रोमो संदेश नहीं भेज सकते। किसी संदेश का जवाब देने का प्रयास करें\nया कोई त्रुटि हुई</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ उपयोगकर्ता ने अभी तक कोई सामग्री डाउनलोड नहीं की...</b> लॉग में मौजूद नहीं"
    ADMIN_INVALID_COMMAND_MSG = "❌ अमान्य कमांड"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ कैश में <code>{{path}}</code> के लिए कोई डेटा नहीं मिला"
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ उपयोग: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 व्यवस्थापक व्यवस्थापक को हटा नहीं सकता"
    ADMIN_USER_BLOCKED_MSG = "उपयोगकर्ता ब्लॉक 🔒❌\n \nID: <code>{user_id}</code>\nब्लॉक की तारीख: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> पहले से ब्लॉक है ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 क्षमा करें! आप व्यवस्थापक नहीं हैं"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ उपयोग: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "उपयोगकर्ता अनब्लॉक 🔓✅\n \nID: <code>{user_id}</code>\nअनब्लॉक की तारीख: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> पहले से अनब्लॉक है ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>बॉट चलने का समय -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ कैश साफ करने के लिए कृपया एक URL प्रदान करें।\nउपयोग: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ कृपया एक वैध URL प्रदान करें।\nउपयोग: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ URL के लिए कैश सफलतापूर्वक साफ किया गया:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ इस लिंक के लिए कोई कैश नहीं मिला।"
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ कैश साफ करने में त्रुटि: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ पहुंच अस्वीकृत। केवल व्यवस्थापक।"
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ पोर्न सूची अपडेट स्क्रिप्ट चल रही है: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ स्क्रिप्ट सफलतापूर्वक पूरी हुई!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ स्क्रिप्ट सफलतापूर्वक पूरी हुई!\n\nआउटपुट:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ स्क्रिप्ट रिटर्न कोड {returncode} के साथ विफल:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ स्क्रिप्ट चलाने में त्रुटि: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ पोर्न और डोमेन-संबंधित कैश रीलोड हो रहे हैं..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ पोर्न कैश सफलतापूर्वक रीलोड किए गए!\n\n"
        "📊 वर्तमान कैश स्थिति:\n"
        "• पोर्न डोमेन: {porn_domains}\n"
        "• पोर्न कीवर्ड: {porn_keywords}\n"
        "• समर्थित साइटें: {supported_sites}\n"
        "• WHITELIST: {whitelist}\n"
        "• GREYLIST: {greylist}\n"
        "• BLACK_LIST: {black_list}\n"
        "• WHITE_KEYWORDS: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ पोर्न कैश रीलोड करने में त्रुटि: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ कृपया जांच के लिए URL प्रदान करें।\nउपयोग: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ कृपया एक वैध URL प्रदान करें।\nउपयोग: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 NSFW सामग्री के लिए URL जांच रहा है...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>पोर्न जांच परिणाम</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>स्थिति:</b> <b>{status_text}</b>\n\n"
        "<b>स्पष्टीकरण:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ URL जांचने में त्रुटि: {error}"
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 पिछले {hours} घंटे (2 दिन) के चैनल गतिविधि लॉग."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 पिछले {hours} घंटे (2 दिन) में: शामिल {joined}, निकले {left}."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ पिछले {hours} घंटे (2 दिन) में कोई गतिविधि नहीं।"
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "कुल: 🟢 {joined} ने जॉइन किया, 🔴 {left} ने छोड़ा।"
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ चैनल गतिविधि लॉग तक पहुंच नहीं है। बॉट admin logs नहीं पढ़ सकते। इस सुविधा को सक्षम करने के लिए कॉन्फ़िग में CHANNEL_GUARD_SESSION_STRING के साथ उपयोगकर्ता सत्र प्रदान करें।"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ कतार खाली है — अभी तक कोई चैनल नहीं छोड़ा है।"
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>बैन कतार</b>\nलंबित कुल: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (छोड़ा: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… और {extra} और उपयोगकर्ता।"
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "उपयोग करें /block_user show • all • auto • 10s"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ कतार से उपयोगकर्ताओं को ब्लॉक किया गया: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ ऑटो-ब्लॉकिंग सक्षम: नए छोड़ने वालों को तुरंत बैन कर दिया जाएगा।"
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ ऑटो-ब्लॉकिंग अक्षम।"
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ अनुसूचित ऑटो-ब्लॉक विंडो हर {interval} पर सेट की गई।"
    BAN_TIME_USAGE_MSG = "❌ उपयोग: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ 10s, 6m, 5h, 4d, 3w, 2M या 1y जैसे प्रारूपों का उपयोग करें।"
    BAN_TIME_SET_MSG = "🕒 चैनल लॉग स्कैन अंतराल {interval} पर सेट किया गया।"
    BAN_TIME_REPORT_MSG = (
        "🛡️ चैनल स्कैन रिपोर्ट\n"
        "चलाया गया: {run_ts}\n"
        "अंतराल: {interval}\n"
        "नए छोड़ने वाले: {new_leavers}\n"
        "ऑटो बैन: {auto_banned}\n"
        "लंबित: {pending}\n"
        "अंतिम event_id: {last_event_id}"
    )
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ उपयोगकर्ताओं का ब्लॉक हटाया गया: {count}\n⏱ टाइमस्टैम्प: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ उपयोग: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "उपयोगकर्ता को नजरअंदाज किया गया 👁️❌\n \nआईडी: <code>{user_id}</code>\nनजरअंदाज करने की तारीख: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code> पहले से ही नजरअंदाज किया जा रहा है ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ उपयोग: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "उपयोगकर्ता अब नजरअंदाज नहीं किया जा रहा 👁️✅\n \nआईडी: <code>{user_id}</code>\nनजरअंदाज न करने की तारीख: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code> नजरअंदाज नहीं किया जा रहा ✅😐"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "कुकीज़ साफ की गईं।"
    CLEAN_LOGS_CLEANED_MSG = "लॉग साफ किए गए।"
    CLEAN_TAGS_CLEANED_MSG = "टैग साफ किए गए।"
    CLEAN_FORMAT_CLEANED_MSG = "प्रारूप साफ किया गया।"
    CLEAN_SPLIT_CLEANED_MSG = "स्प्लिट साफ किया गया।"
    CLEAN_MEDIAINFO_CLEANED_MSG = "मीडियाइन्फो साफ किया गया।"
    CLEAN_SUBS_CLEANED_MSG = "उपशीर्षक सेटिंग्स साफ की गईं।"
    CLEAN_KEYBOARD_CLEANED_MSG = "कीबोर्ड सेटिंग्स साफ की गईं।"
    CLEAN_ARGS_CLEANED_MSG = "तर्क सेटिंग्स साफ की गईं।"
    CLEAN_NSFW_CLEANED_MSG = "NSFW सेटिंग्स साफ की गईं।"
    CLEAN_PROXY_CLEANED_MSG = "प्रॉक्सी सेटिंग्स साफ की गईं।"
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "फ्लड प्रतीक्षा सेटिंग्स साफ की गईं।"
    CLEAN_ALL_CLEANED_MSG = "सभी फाइलें साफ की गईं।"
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 कुकीज़</b>\n\nएक क्रिया चुनें:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ कुकी फाइल सहेजी गई"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ गैर-YouTube कुकीज़ के लिए सत्यापन छोड़ दिया गया"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ कुकी फाइल मौजूद है लेकिन गलत प्रारूप है"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ कुकी फाइल नहीं मिली।"
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 YouTube कुकीज़ टेस्ट शुरू हो रहा है...\n\nकृपया प्रतीक्षा करें जबकि मैं आपकी कुकीज़ की जांच और सत्यापन कर रहा हूं।"
    COOKIES_YOUTUBE_WORKING_MSG = "✅ आपकी मौजूदा YouTube कुकीज़ ठीक से काम कर रही हैं!\n\nनई डाउनलोड करने की आवश्यकता नहीं है।"
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ आपकी मौजूदा YouTube कुकीज़ समाप्त हो गई हैं या अमान्य हैं।\n\n🔄 नई कुकीज़ डाउनलोड हो रही हैं..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} कुकी स्रोत कॉन्फ़िगर नहीं है!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} कुकी स्रोत .txt फाइल होनी चाहिए!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ रेंज सीमा पार हो गई: {range_count} फाइलें अनुरोधित (अधिकतम {max_img_files})।\n\nअधिकतम उपलब्ध फाइलें डाउनलोड करने के लिए इनमें से एक कमांड का उपयोग करें:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚बंद करें"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ मीडिया सीमा पार हो गई: {count} फाइलें अनुरोधित (अधिकतम {max_count})।\n\nअधिकतम उपलब्ध फाइलें डाउनलोड करने के लिए इनमें से एक कमांड का उपयोग करें:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 लिंक से <b>{count}</b> मीडिया आइटम मिले"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "डाउनलोड रेंज चुनें:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "ब्राउज़र प्रतिरूपण"
    ARGS_REFERER_DESC_MSG = "रेफरर हेडर"
    ARGS_USER_AGENT_DESC_MSG = "यूजर-एजेंट हेडर"
    ARGS_GEO_BYPASS_DESC_MSG = "भौगोलिक प्रतिबंधों को बायपास करें"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "SSL प्रमाणपत्र जांचें"
    ARGS_LIVE_FROM_START_DESC_MSG = "लाइव स्ट्रीम को शुरुआत से डाउनलोड करें"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "लाइव स्ट्रीम को शुरुआत से डाउनलोड न करें"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "HLS वीडियो के लिए MPEG-TS कंटेनर का उपयोग करें"
    ARGS_NO_PLAYLIST_DESC_MSG = "केवल एकल वीडियो डाउनलोड करें, प्लेलिस्ट नहीं"
    ARGS_NO_PART_DESC_MSG = ".part फाइलों का उपयोग न करें"
    ARGS_NO_CONTINUE_DESC_MSG = "आंशिक डाउनलोड को फिर से शुरू न करें"
    ARGS_AUDIO_FORMAT_DESC_MSG = "निष्कर्षण के लिए ऑडियो प्रारूप"
    ARGS_EMBED_METADATA_DESC_MSG = "वीडियो फाइल में मेटाडेटा एम्बेड करें"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "वीडियो फाइल में थंबनेल एम्बेड करें"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "थंबनेल को फाइल में लिखें"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "डाउनलोड करने के लिए समवर्ती फ्रैगमेंट की संख्या"
    ARGS_FORCE_IPV4_DESC_MSG = "IPv4 कनेक्शन को मजबूर करें"
    ARGS_FORCE_IPV6_DESC_MSG = "IPv6 कनेक्शन को मजबूर करें"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For हेडर रणनीति"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP चंक आकार (बाइट्स)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "उपशीर्षक डाउनलोड से पहले स्लीप (सेकंड)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "लेगेसी सर्वर कनेक्शन की अनुमति दें"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "HTTPS प्रमाणपत्र सत्यापन को दबाएं"
    ARGS_USERNAME_DESC_MSG = "खाता उपयोगकर्ता नाम"
    ARGS_PASSWORD_DESC_MSG = "खाता पासवर्ड"
    ARGS_TWOFACTOR_DESC_MSG = "दो-कारक प्रमाणीकरण कोड"
    ARGS_IGNORE_ERRORS_DESC_MSG = "डाउनलोड त्रुटियों को नजरअंदाज करें और जारी रखें"
    ARGS_MIN_FILESIZE_DESC_MSG = "न्यूनतम फाइल आकार (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "अधिकतम फाइल आकार (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "डाउनलोड करने के लिए प्लेलिस्ट आइटम (उदा., 1,3,5 या 1-5)"
    ARGS_DATE_DESC_MSG = "इस तारीख को अपलोड किए गए वीडियो डाउनलोड करें (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "इस तारीख से पहले अपलोड किए गए वीडियो डाउनलोड करें (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "इस तारीख के बाद अपलोड किए गए वीडियो डाउनलोड करें (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "कस्टम HTTP हेडर (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "अनुरोधों के बीच स्लीप अंतराल (सेकंड)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "अधिकतम स्लीप अंतराल (सेकंड)"
    ARGS_RETRIES_DESC_MSG = "पुनः प्रयासों की संख्या"
    ARGS_VIDEO_FORMAT_DESC_MSG = "वीडियो कंटेनर प्रारूप"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "मर्जिंग के लिए आउटपुट कंटेनर प्रारूप"
    ARGS_SEND_AS_FILE_DESC_MSG = "सभी मीडिया को मीडिया के बजाय दस्तावेज़ के रूप में भेजें"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "प्रतिरूपण"
    ARGS_REFERER_SHORT_MSG = "रेफरर"
    ARGS_GEO_BYPASS_SHORT_MSG = "जियो बायपास"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "प्रमाणपत्र जांचें"
    ARGS_LIVE_FROM_START_SHORT_MSG = "लाइव शुरू"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "लाइव शुरू नहीं"
    ARGS_USER_AGENT_SHORT_MSG = "यूजर एजेंट"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "प्लेलिस्ट नहीं"
    ARGS_NO_PART_SHORT_MSG = "भाग नहीं"
    ARGS_NO_CONTINUE_SHORT_MSG = "जारी नहीं"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "ऑडियो प्रारूप"
    ARGS_EMBED_METADATA_SHORT_MSG = "मेटा एम्बेड करें"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "थंबनेल एम्बेड करें"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "थंबनेल लिखें"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "समवर्ती"
    ARGS_FORCE_IPV4_SHORT_MSG = "IPv4 फोर्स"
    ARGS_FORCE_IPV6_SHORT_MSG = "IPv6 फोर्स"
    ARGS_XFF_SHORT_MSG = "XFF हेडर"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "चंक आकार"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "सब्स स्लीप"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "लेगेसी कनेक्ट"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "प्रमाणपत्र जांच नहीं"
    ARGS_USERNAME_SHORT_MSG = "उपयोगकर्ता नाम"
    ARGS_PASSWORD_SHORT_MSG = "पासवर्ड"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "त्रुटियां नजरअंदाज"
    ARGS_MIN_FILESIZE_SHORT_MSG = "न्यूनतम आकार"
    ARGS_MAX_FILESIZE_SHORT_MSG = "अधिकतम आकार"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "प्लेलिस्ट आइटम"
    ARGS_DATE_SHORT_MSG = "तारीख"
    ARGS_DATEBEFORE_SHORT_MSG = "तारीख से पहले"
    ARGS_DATEAFTER_SHORT_MSG = "तारीख के बाद"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP हेडर"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "स्लीप अंतराल"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "अधिकतम स्लीप"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "वीडियो प्रारूप"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "मर्ज प्रारूप"
    ARGS_SEND_AS_FILE_SHORT_MSG = "फाइल के रूप में भेजें"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ फाइल बहुत बड़ी है। अधिकतम आकार 100 KB है।"
    COOKIES_INVALID_FORMAT_MSG = "❌ केवल निम्नलिखित प्रारूप की फाइलों की अनुमति है .txt।"
    COOKIES_INVALID_COOKIE_MSG = "❌ फाइल cookie.txt जैसी नहीं दिखती ('# Netscape HTTP Cookie File' लाइन नहीं है)।"
    COOKIES_ERROR_READING_MSG = "❌ फाइल पढ़ने में त्रुटि: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ कुकी फाइल मौजूद है और सही प्रारूप है"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} कुकी फाइल बहुत बड़ी है! अधिकतम 100KB, प्राप्त {size}KB।"
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} कुकी फाइल डाउनलोड की गई और आपके फोल्डर में cookie.txt के रूप में सहेजी गई।</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} कुकी स्रोत उपलब्ध नहीं है (स्थिति {status})। कृपया बाद में पुनः प्रयास करें।"
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ {service} कुकी फाइल डाउनलोड करने में त्रुटि। कृपया बाद में पुनः प्रयास करें।"
    COOKIES_USER_PROVIDED_MSG = "<b>✅ उपयोगकर्ता ने एक नई कुकी फाइल प्रदान की।</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ कुकी सफलतापूर्वक अपडेट की गई:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ मान्य कुकी नहीं है।</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube कुकी स्रोत कॉन्फ़िगर नहीं हैं!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 YouTube कुकीज़ डाउनलोड और जांच हो रही है...\n\nप्रयास {attempt} में से {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ पहुंच अस्वीकृत। केवल व्यवस्थापक।"
    ADMIN_USER_LOGS_TOTAL_MSG = "कुल: <b>{total}</b>\n<b>{user_id}</b> - लॉग (अंतिम 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 कीबोर्ड सक्रिय!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ उपशीर्षक भाषा सेट की गई: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ उपशीर्षक भाषा सेट की गई: {flag} {name} AUTO/TRANS सक्षम के साथ।"
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "उपशीर्षक भाषा मेनू बंद।"
    SUBS_DOWNLOADING_MSG = "💬 उपशीर्षक डाउनलोड हो रहे हैं..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Firebase कैश को मेमोरी में रीलोड किया जा रहा है..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ कोई COOKIE_URL कॉन्फ़िगर नहीं है। /cookie का उपयोग करें या cookie.txt अपलोड करें।"
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 रिमोट URL से कुकीज़ डाउनलोड हो रही है..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ फॉलबैक COOKIE_URL .txt फाइल की ओर इंगित करना चाहिए।"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ फॉलबैक कुकी फाइल बहुत बड़ी है (>100KB)।"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube कुकी फाइल फॉलबैक के माध्यम से डाउनलोड की गई और cookie.txt के रूप में सहेजी गई"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ फॉलबैक कुकी स्रोत उपलब्ध नहीं है (स्थिति {status})। /cookie का प्रयास करें या cookie.txt अपलोड करें।"
    COOKIE_FALLBACK_ERROR_MSG = "❌ फॉलबैक कुकी डाउनलोड करने में त्रुटि। /cookie का प्रयास करें या cookie.txt अपलोड करें।"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ फॉलबैक कुकी डाउनलोड के दौरान अप्रत्याशित त्रुटि।"
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} ब्राउज़र इंस्टॉल नहीं है।"
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ ब्राउज़र का उपयोग करके कुकीज़ सहेजी गईं: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ कुकीज़ सहेजने में विफल: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube कुकीज़ ठीक से काम कर रही हैं"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube कुकीज़ समाप्त हो गई हैं या अमान्य हैं\n\nनई कुकीज़ प्राप्त करने के लिए /cookie का उपयोग करें"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - कस्टम प्रारूप\n• <code>/format 720</code> - 720p गुणवत्ता\n• <code>/format 4k</code> - 4K गुणवत्ता"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "संकेत भेजा गया।"
    FORMAT_MKV_TOGGLE_MSG = "MKV अब {status} है"
    COOKIES_NO_REMOTE_URL_MSG = "❌ कोई रिमोट URL कॉन्फ़िगर नहीं है"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ अमान्य फाइल प्रारूप"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ फाइल बहुत बड़ी है"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ कुकीज़ सफलतापूर्वक डाउनलोड की गईं"
    COOKIES_SERVER_ERROR_MSG = "❌ सर्वर त्रुटि {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ डाउनलोड विफल रहा"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ अप्रत्याशित त्रुटि"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ ब्राउज़र इंस्टॉल नहीं है।"
    COOKIES_MENU_CLOSED_MSG = "मेनू बंद।"
    COOKIES_HINT_CLOSED_MSG = "कुकी संकेत बंद।"
    IMG_HELP_CLOSED_MSG = "मदद बंद।"
    SUBS_LANGUAGE_UPDATED_MSG = "उपशीर्षक भाषा सेटिंग्स अपडेट की गईं।"
    SUBS_MENU_CLOSED_MSG = "उपशीर्षक भाषा मेनू बंद।"
    KEYBOARD_SET_TO_MSG = "कीबोर्ड {setting} पर सेट किया गया"
    KEYBOARD_ERROR_PROCESSING_MSG = "सेटिंग प्रोसेस करने में त्रुटि"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo सक्षम।"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo अक्षम।"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW ब्लर अक्षम।"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW ब्लर सक्षम।"
    SETTINGS_MENU_CLOSED_MSG = "मेनू बंद।"
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "फ्लड प्रतीक्षा सक्रिय। बाद में प्रयास करें।"
    OTHER_HELP_CLOSED_MSG = "मदद बंद।"
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "लॉग संदेश बंद।"
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "मेनू बंद।"
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "अमान्य आकार।"
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ MediaInfo भेजने में त्रुटि: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ एक त्रुटि हुई: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - सभी लॉग"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - सभी {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 रिमोट URL से डाउनलोड करें"
    BROWSER_OPEN_BUTTON_MSG = "🌐 ब्राउज़र खोलें"
    SELECT_BROWSER_MSG = "कुकीज़ डाउनलोड करने के लिए एक ब्राउज़र चुनें:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "इस सिस्टम पर कोई ब्राउज़र नहीं मिला। आप रिमोट URL से कुकीज़ डाउनलोड कर सकते हैं या ब्राउज़र स्थिति की निगरानी कर सकते हैं:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>ब्राउज़र खोलें</b> - मिनी-ऐप में ब्राउज़र स्थिति की निगरानी के लिए"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ /check_cookie चलाने में विफल"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ फ्लड सीमा। बाद में प्रयास करें।"
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ ब्राउज़र कुकी मेनू खोलने में विफल"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "कुकी के रूप में सहेजें संकेत बंद।"
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>उपयोग:</b>\n<code>/link [quality] URL</code>\n\n<b>उदाहरण:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - सर्वोत्तम गुणवत्ता\n• /link 720 https://youtube.com/watch?v=... - 720p या कम\n• /link 720p https://youtube.com/watch?v=... - ऊपर के समान\n• /link 4k https://youtube.com/watch?v=... - 4K या कम\n• /link 8k https://youtube.com/watch?v=... - 8K या कम</blockquote>\n\n<b>गुणवत्ता:</b> 1 से 10000 तक (उदा., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K गुणवत्ता"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>प्रत्यक्ष लिंक प्राप्त हुआ</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>ऑडियो स्ट्रीम:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ स्ट्रीम लिंक प्राप्त करने में विफल"
    LINK_ERROR_GETTING_MSG = "❌ <b>लिंक प्राप्त करने में त्रुटि:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ अमान्य YouTube कुकी इंडेक्स: {selected_index}। उपलब्ध रेंज 1-{total_urls} है"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 YouTube कुकीज़ डाउनलोड और जांच हो रही है...\n\nप्रयास {attempt} में से {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 YouTube कुकीज़ डाउनलोड और जांच हो रही है...\n\nप्रयास {attempt} में से {total}\n🔍 कुकीज़ परीक्षण..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube कुकीज़ सफलतापूर्वक डाउनलोड और सत्यापित की गईं!\n\nस्रोत {source} में से {total} का उपयोग किया गया"
    COOKIES_ALL_EXPIRED_MSG = "❌ सभी YouTube कुकीज़ समाप्त हो गई हैं या अनुपलब्ध हैं!\n\nउन्हें बदलने के लिए बॉट व्यवस्थापक से संपर्क करें।"
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube कुकी रिट्राई सीमा पार हो गई!\n\n🔢 अधिकतम: {limit} प्रति घंटे प्रयास\n⏰ कृपया बाद में पुनः प्रयास करें"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ टैग #{wrong} में निषिद्ध वर्ण हैं। केवल अक्षर, अंक और _ की अनुमति है।\nकृपया उपयोग करें: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **अमान्य तर्क!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ उपशीर्षक भाषा सेट की गई: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "उदाहरण: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} चयनित भाषा: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ हमेशा पूछें मोड {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 उपशीर्षक अक्षम हैं"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 उपशीर्षक सेटिंग्स</b>\n\n{status_text}\n\nउपशीर्षक भाषा चुनें:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - उपशीर्षक अक्षम करें\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 उपशीर्षक सेटिंग्स</b>\n\n{status_text}\n\nउपशीर्षक भाषा चुनें:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>शीर्षक:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>अवधि:</b> {duration} सेकंड\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>वीडियो स्ट्रीम:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 720p अधिकतम गुणवत्ता\n- 1.5 घंटे अधिकतम अवधि\n- 500mb अधिकतम वीडियो आकार</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️चेतावनी: उच्च CPU प्रभाव के कारण यह फ़ंक्शन बहुत धीमा है (लगभग रीयल-टाइम) और सीमित है:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>त्वरित कमांड:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - उपशीर्षक अक्षम करें\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - हमेशा पूछें मोड सक्षम करें\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - भाषा सेट करें\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - AUTO/TRANS सक्षम के साथ भाषा सेट करें\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - हमेशा पूछें मोड सक्षम करें\n"
    SUBS_AUTO_SUBS_TEXT = " (ऑटो-सब्स)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Auto-subs mode {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "कमांड के माध्यम से सब्स अक्षम: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "कमांड के माध्यम से सब्स हमेशा पूछें सक्षम: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "कमांड के माध्यम से सब्स भाषा सेट: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "उपशीर्षक भाषा + ऑटो मोड कमांड के माध्यम से सेट: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "उपयोगकर्ता ने /subs मेनू खोला।"
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "उपयोगकर्ता ने उपशीर्षक भाषा सेट की: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "उपयोगकर्ता ने AUTO/TRANS मोड टॉगल किया: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "उपयोगकर्ता ने हमेशा पूछें मोड टॉगल किया: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "उपयोगकर्ता ने ब्राउज़र से कुकीज़ का अनुरोध किया।"
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "केवल इंस्टॉल किए गए ब्राउज़रों के साथ ब्राउज़र चयन कीबोर्ड भेजा गया।"
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "ब्राउज़र चयन बंद।"
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "फॉलबैक COOKIE_URL सफलतापूर्वक उपयोग किया गया (स्रोत छिपा हुआ)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "फॉलबैक COOKIE_URL विफल: स्थिति={status} (छिपा हुआ)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "फॉलबैक COOKIE_URL अप्रत्याशित त्रुटि: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "ब्राउज़र {browser} इंस्टॉल नहीं है।"
    COOKIES_SAVED_BROWSER_LOG_MSG = "ब्राउज़र का उपयोग करके कुकीज़ सहेजी गई: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "उपयोगकर्ता {user_id} के लिए कुकी फ़ाइल सहेजी गई।"
    COOKIES_FILE_WORKING_LOG_MSG = "कुकी फ़ाइल मौजूद है, सही प्रारूप है, और YouTube कुकीज़ काम कर रही हैं।"
    COOKIES_FILE_EXPIRED_LOG_MSG = "कुकी फ़ाइल मौजूद है और सही प्रारूप है, लेकिन YouTube कुकीज़ समाप्त हो गई हैं।"
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "कुकी फ़ाइल मौजूद है और सही प्रारूप है।"
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "कुकी फ़ाइल मौजूद है लेकिन गलत प्रारूप है।"
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "कुकी फ़ाइल नहीं मिली।"
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "उपयोगकर्ता {user_id} के लिए {service} कुकी URL खाली है।"
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} कुकी URL .txt नहीं है (छिपा हुआ)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} कुकी फ़ाइल बहुत बड़ी: {size} बाइट्स (स्रोत छिपा हुआ)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए {service} कुकी फ़ाइल डाउनलोड की गई (स्रोत छिपा हुआ)।"
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "स्क्रिप्ट नहीं मिली: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "प्रारंभिक स्थिति संदेश भेजने में विफल"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "{script_path} चलाने में त्रुटि: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "ऑटो टास्क द्वारा Firebase कैश रीलोड किया गया।"
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "व्यवस्थापक द्वारा Firebase कैश रीलोड किया गया।"
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Firebase कैश रीलोड करने में त्रुटि: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "ब्रॉडकास्ट शुरू किया गया। टेक्स्ट:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "सभी उपयोगकर्ताओं को ब्रॉडकास्ट संदेश भेजा गया।"
    ADMIN_BROADCAST_FAILED_LOG_MSG = "ब्रॉडकास्ट संदेश भेजने में विफल: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "व्यवस्थापक {user_id} ने URL के लिए कैश साफ़ किया: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "व्यवस्थापक {user_id} ने पोर्न सूची अपडेट स्क्रिप्ट शुरू की: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "व्यवस्थापक {user_id} द्वारा पोर्न सूची अपडेट स्क्रिप्ट सफलतापूर्वक पूर्ण"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "व्यवस्थापक {user_id} द्वारा पोर्न सूची अपडेट स्क्रिप्ट विफल: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "व्यवस्थापक {user_id} ने अस्तित्वहीन स्क्रिप्ट चलाने का प्रयास किया: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "व्यवस्थापक {user_id} द्वारा पोर्न अपडेट स्क्रिप्ट चलाने में त्रुटि: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "व्यवस्थापक {user_id} ने पोर्न कैश रीलोड शुरू किया"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "व्यवस्थापक {user_id} द्वारा पोर्न कैश रीलोड करने में त्रुटि: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "व्यवस्थापक {user_id} ने NSFW के लिए URL जांचा: {url} - परिणाम: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "उपयोगकर्ता ने प्रारूप परिवर्तन का अनुरोध किया।"
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "प्रारूप ALWAYS_ASK पर सेट किया गया।"
    FORMAT_UPDATED_BEST_LOG_MSG = "प्रारूप सर्वोत्तम पर अपडेट किया गया: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "प्रारूप ID {format_id} पर अपडेट किया गया: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "प्रारूप ID {format_id} (केवल-ऑडियो) पर अपडेट किया गया: {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "प्रारूप गुणवत्ता {quality} पर अपडेट किया गया: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "प्रारूप अपडेट किया गया: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "प्रारूप मेनू भेजा गया।"
    FORMAT_SELECTION_CLOSED_LOG_MSG = "प्रारूप चयन बंद।"
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "कस्टम प्रारूप संकेत भेजा गया।"
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "प्रारूप रिजॉल्यूशन मेनू भेजा गया।"
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "मुख्य प्रारूप मेनू पर वापस आए।"
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "प्रारूप अपडेट किया गया: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "प्रारूप ALWAYS_ASK पर सेट किया गया।"
    FORMAT_CODEC_SET_LOG_MSG = "कोडेक प्राथमिकता {codec} पर सेट की गई"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "कस्टम प्रारूप मेनू बंद"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए {url} से डायरेक्ट लिंक निकाला गया"
    LINK_EXTRACTION_FAILED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए {url} से डायरेक्ट लिंक निकालने में विफल: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "उपयोगकर्ता {user_id} के लिए लिंक कमांड में त्रुटि: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "उपयोगकर्ता {user_id} ने कीबोर्ड {setting} पर सेट किया"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "उपयोगकर्ता {user_id} ने कीबोर्ड {setting} पर सेट किया"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo कमांड के माध्यम से सेट किया गया: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "उपयोगकर्ता ने /mediainfo मेनू खोला।"
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: बंद।"
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo सक्षम।"
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo अक्षम।"
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "तर्क के माध्यम से विभाजन आकार {size} बाइट्स पर सेट किया गया।"
    SPLIT_MENU_OPENED_LOG_MSG = "उपयोगकर्ता ने /split मेनू खोला।"
    SPLIT_SELECTION_CLOSED_LOG_MSG = "विभाजन चयन बंद।"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "विभाजन आकार {size} बाइट्स पर सेट किया गया।"
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "प्रॉक्सी कमांड के माध्यम से सेट की गई: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "उपयोगकर्ता ने /proxy मेनू खोला।"
    PROXY_MENU_CLOSED_LOG_MSG = "प्रॉक्सी: बंद।"
    PROXY_ENABLED_LOG_MSG = "प्रॉक्सी सक्षम।"
    PROXY_DISABLED_LOG_MSG = "प्रॉक्सी अक्षम।"
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "सहायता संदेश बंद।"
    AUDIO_HELP_SHOWN_LOG_MSG = "/audio मदद दिखाई गई"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "उपयोगकर्ता ने प्लेलिस्ट सहायता का अनुरोध किया।"
    PLAYLIST_HELP_CLOSED_LOG_MSG = "प्लेलिस्ट सहायता बंद।"
    AUDIO_HINT_CLOSED_LOG_MSG = "ऑडियो संकेत बंद।"
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए LINK बटन के माध्यम से {url} से डायरेक्ट लिंक मेनू बनाया गया"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए LINK बटन के माध्यम से {url} से डायरेक्ट लिंक निकालने में विफल: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए LIST कमांड निष्पादित, url: {url}"
    QUICK_EMBED_LOG_MSG = "त्वरित एम्बेड: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "{url} के लिए हमेशा पूछें मेनू भेजा गया"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "त्रुटि के बाद उपयोगकर्ता {user_id} के लिए कैश किए गए गुणवत्ता मेनू बनाया गया: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "{url} के लिए हमेशा पूछें मेनू त्रुटि: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "प्रारूप /args सेटिंग्स के माध्यम से निश्चित है"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "ऑडियो"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "वीडियो"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "वीडियो"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "अगला ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ पिछला"
    SUBTITLES_NEXT_BUTTON_MSG = "अगला ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ सभी टेक्स्ट फील्ड खाली हैं"
    SENDER_VIDEO_DURATION_MSG = "वीडियो अवधि:"
    SENDER_UPLOADING_FILE_MSG = "📤 फाइल अपलोड हो रही है..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 वीडियो अपलोड हो रहा है..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 वीडियो अवधि:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 फाइल अपलोड की गई।"
    DOWN_UP_VIDEO_INFO_MSG = "📋 वीडियो जानकारी"
    DOWN_UP_NUMBER_MSG = "संख्या"
    DOWN_UP_TITLE_MSG = "शीर्षक"
    DOWN_UP_ID_MSG = "आईडी"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ वीडियो डाउनलोड किया गया।"
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 अपलोड के लिए प्रसंस्करण..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 विभाजित भाग {part} फाइल अपलोड की गई"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ अपलोड पूर्ण"
    DOWN_UP_FILES_UPLOADED_MSG = "फाइलें अपलोड की गईं"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 बंद करें"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼कोडेक"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 डब्स"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 सब्स"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 ब्राउज़र"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 डायरेक्ट लिंक प्राप्त कर रहे हैं..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 उपलब्ध प्रारूप प्राप्त कर रहे हैं..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 वीडियो विवरण प्राप्त कर रहे हैं..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ विवरण प्राप्त करने में त्रुटि: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ वीडियो विवरण उपलब्ध नहीं है"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ विवरण भेजने में त्रुटि: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 वीडियो विवरण उपयोगकर्ता {user_id} को {url} ({title}) के लिए भेजा गया"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 गैलरी-डीएल शुरू कर रहे हैं…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>अवधि:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>प्रारूप:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>ब्राउज़र:</b> वेब ब्राउज़र में खोलें"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "के लिए उपलब्ध प्रारूप"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 प्रारूप ID का उपयोग कैसे करें:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "सूची प्राप्त करने के बाद, विशिष्ट प्रारूप ID का उपयोग करें:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - प्रारूप 401 डाउनलोड करें"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - ऊपर के समान"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - प्रारूप 140 को MP3 ऑडियो के रूप में डाउनलोड करें"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 केवल-ऑडियो प्रारूप मिला"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "ये प्रारूप MP3 ऑडियो फ़ाइलों के रूप में डाउनलोड होंगे।"
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>प्रारूप कैसे सेट करें:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - विशिष्ट प्रारूप ID डाउनलोड करें"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - गुणवत्ता के अनुसार डाउनलोड करें"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - सर्वोत्तम गुणवत्ता डाउनलोड करें"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - हमेशा गुणवत्ता के लिए पूछें"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>केवल-ऑडियो प्रारूप:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - प्रारूप 140 को MP3 ऑडियो के रूप में डाउनलोड करें"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "ये MP3 ऑडियो फ़ाइलों के रूप में डाउनलोड होंगे।"
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 ऊपर की सूची से प्रारूप ID का उपयोग करें"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ त्रुटि: मूल संदेश नहीं मिला।"
    ALWAYS_ASK_FORMATS_PAGE_MSG = "प्रारूप पृष्ठ"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ प्रारूप मेनू दिखाने में त्रुटि"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ प्रारूप प्राप्त करने में त्रुटि"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ उपलब्ध प्रारूप प्राप्त करने में त्रुटि।"
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "कृपया बाद में पुनः प्रयास करें।"
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp इस सामग्री को प्रोसेस नहीं कर सकता"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "सिस्टम इसके बजाय gallery-dl का उपयोग करने की सिफारिश करता है।"
    ALWAYS_ASK_OPTIONS_MSG = "**विकल्प:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• छवि गैलरी के लिए: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• एकल छवियों के लिए: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl अक्सर Instagram, Twitter और अन्य सोशल मीडिया सामग्री के लिए बेहतर काम करता है।"
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Gallery-dl कोशिश करें"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 /args के माध्यम से प्रारूप निश्चित"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 उपशीर्षक"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 डब किया गया ऑडियो"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — उपशीर्षक उपलब्ध हैं"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — उपशीर्षक भाषा चुनें"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ उपशीर्षक नहीं मिला और एम्बेड नहीं होगा"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — कैश से तुरंत रीपोस्ट"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — ऑडियो भाषा चुनें"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW पेड है (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — डाउनलोड गुणवत्ता चुनें"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — छवि डाउनलोड करें (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — poketube में वीडियो देखें"  # अस्थायी रूप से अक्षम: poketube सेवा डाउन है
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — वीडियो के लिए प्रत्यक्ष लिंक प्राप्त करें"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — उपलब्ध प्रारूप सूची दिखाएं"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — वीडियो एक्सटेंशन/कोडेक बदलें"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀एम्बेड"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — केवल ऑडियो निकालें"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW भुगतान योग्य है (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — कैश से तत्काल रिपोस्ट"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — poketube में वीडियो देखें"  # अस्थायी रूप से अक्षम: poketube सेवा डाउन है
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — ऑडियो भाषा चुनें"
    ALWAYS_ASK_BEST_BUTTON_MSG = "सर्वोत्तम"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛अन्य"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝केवल उपशीर्षक"
    ALWAYS_ASK_SMART_GROUPING_MSG = "स्मार्ट ग्रुपिंग"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "एक्शन बटन पंक्ति जोड़ी गई (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "एक्शन बटन पंक्तियां जोड़ी गईं (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "मौजूदा पंक्ति में निचले बटन जोड़े गए"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "नई निचली पंक्ति बनाई गई"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "प्लेलिस्ट में कोई वीडियो नहीं मिला"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "असमर्थित URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "कोई वीडियो नहीं मिल सका"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "कोई वीडियो नहीं मिला"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "कोई मीडिया नहीं मिली"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "यह ट्वीट शामिल नहीं है"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>वीडियो जानकारी प्राप्त करने में त्रुटि:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "वीडियो जानकारी प्राप्त करने में त्रुटि"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "<code>/clean</code> कमांड आज़माएं और फिर से कोशिश करें। यदि त्रुटि बनी रहती है, तो YouTube को प्राधिकरण की आवश्यकता है। <code>/cookie</code> या <code>/cookies_from_browser</code> के माध्यम से cookies.txt को अपडेट करें और फिर से कोशिश करें।"
    ALWAYS_ASK_MENU_CLOSED_MSG = "मेनू बंद।"
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 मैनुअल गुणवत्ता चयन"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "स्वचालित पहचान विफल होने के कारण मैनुअल रूप से गुणवत्ता चुनें:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 सभी उपलब्ध प्रारूप"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 उपलब्ध गुणवत्ताएं (कैश से)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ कैश की गई गुणवत्ताओं का उपयोग - नए प्रारूप उपलब्ध नहीं हो सकते"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 प्रारूप डाउनलोड हो रहा है"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 डाउनलोड हो रहा है"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 प्रगति ट्रैकिंग के साथ डाउनलोड हो रहा है..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 प्रारूप का उपयोग करके डाउनलोड हो रहा है:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 प्रारूप का उपयोग करके ऑडियो डाउनलोड हो रहा है:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 सर्वोत्तम गुणवत्ता डाउनलोड हो रही है..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 डेटाबेस डंप डाउनलोड हो रहा है..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 डाउनलोड हो रहा है"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "प्रारूप पृष्ठ"
    ALWAYS_ASK_FROM_CACHE_MSG = "(कैश से)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ त्रुटि: मूल संदेश नहीं मिला। यह हटा दिया गया हो सकता है। कृपया लिंक फिर से भेजें।"
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ त्रुटि: मूल URL नहीं मिला। कृपया लिंक फिर से भेजें।"
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>सीधा लिंक प्राप्त हुआ</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>शीर्षक:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>अवधि:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>प्रारूप:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>वीडियो स्ट्रीम:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>ऑडियो स्ट्रीम:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ स्ट्रीम लिंक प्राप्त करने में विफल"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "उपयोगकर्ता {user_id} के लिए Always Ask मेनू के माध्यम से {url} से डायरेक्ट लिंक निकाला गया"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "उपयोगकर्ता {user_id} के लिए Always Ask मेनू के माध्यम से {url} से डायरेक्ट लिंक निकालने में विफल: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "उपयोगकर्ता {user_id} के लिए down_and_up_with_format के माध्यम से {url} से डायरेक्ट लिंक निकाला गया"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "उपयोगकर्ता {user_id} के लिए down_and_up_with_format के माध्यम से {url} से डायरेक्ट लिंक निकालने में विफल: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "उपयोगकर्ता {user_id} के लिए down_and_audio के माध्यम से {url} से डायरेक्ट लिंक निकाला गया"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "उपयोगकर्ता {user_id} के लिए down_and_audio के माध्यम से {url} से डायरेक्ट लिंक निकालने में विफल: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ ऑडियो कैश से भेजा गया।"
    AUDIO_PROCESSING_MSG = "🎙️ ऑडियो प्रोसेस हो रहा है..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 ऑडियो डाउनलोड हो रहा है:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "ऑडियो डाउनलोड के दौरान त्रुटि हुई।"
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ ऑडियो जानकारी निकालने में विफल"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "इंडेक्स {index} पर प्लेलिस्ट में असमर्थित फ़ाइल प्रकार को छोड़ा जा रहा है"
    AUDIO_FILE_NOT_FOUND_MSG = "डाउनलोड के बाद ऑडियो फ़ाइल नहीं मिली।"

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ ऑडियो भेजने में विफल: फ़ाइल का आकार 0 B के बराबर है (प्लेलिस्ट सूचकांक {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ ऑडियो फ़ाइल अभी भी डाउनलोड हो रही है, कृपया प्रतीक्षा करें..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 ऑडियो फ़ाइल अपलोड हो रही है...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ ऑडियो भेजने में विफल: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "प्लेलिस्ट ऑडियो भेजा गया: {sent}/{total} फ़ाइलें (गुणवत्ता={quality}) उपयोगकर्ता {user_id} को"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ ऑडियो डाउनलोड करने में विफल: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ टाइमआउट के कारण डाउनलोड रद्द किया गया (2 घंटे)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ वीडियो फ़ाइल नहीं मिली: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ वीडियो भेजने में विफल: फ़ाइल का आकार 0 B के बराबर है (प्लेलिस्ट सूचकांक {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ वीडियो फ़ाइल अभी भी डाउनलोड हो रही है, कृपया प्रतीक्षा करें..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ वीडियो प्रोसेस करने में त्रुटि: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ विवरण फ़ाइल भेजने में त्रुटि: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 यदि आप वीडियो कैप्शन बदलना चाहते हैं - नए टेक्स्ट के साथ वीडियो को रिप्लाई करें</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "कोई उपशीर्षक नहीं मिला"
    VIDEO_PROGRESS_MSG = "<b>वीडियो:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>ऑडियो:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL सीमा पार हो गई: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "प्रसंस्करण पूर्ण"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ प्लेलिस्ट रेंज कई URL मोड में अनुमति नहीं है। बिना रेंज के केवल एकल URL भेजें (*1*5, /vid 1-10, आदि)।"
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "यहां <a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>जांचें</a> कि क्या आपकी साइट समर्थित है"
    ERROR_COOKIE_NEEDED_MSG = "इस वीडियो को डाउनलोड करने के लिए आपको <code>cookie</code> की आवश्यकता हो सकती है। पहले <b>/clean</b> कमांड के माध्यम से अपना कार्यक्षेत्र साफ़ करें"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "YouTube के लिए - <b>/cookie</b> कमांड के माध्यम से <code>cookie</code> प्राप्त करें। किसी अन्य समर्थित साइट के लिए - अपना स्वयं का cookie भेजें (<a href='https://t.me/tg_ytdlp/203'>गाइड1</a>) (<a href='https://t.me/tg_ytdlp/214'>गाइड2</a>) और उसके बाद अपना वीडियो लिंक फिर से भेजें।"
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "उपशीर्षक भाषा चुनें"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "कोई वैकल्पिक ऑडियो भाषाएं नहीं"
    CHOOSE_AUDIO_LANGUAGE_MSG = "ऑडियो भाषा चुनें"
    PAGE_NUMBER_MSG = "पृष्ठ {page}"
    TOTAL_PROGRESS_MSG = "कुल प्रगति"
    SUBTITLE_MENU_CLOSED_MSG = "उपशीर्षक मेनू बंद।"
    SUBTITLE_LANGUAGE_SET_MSG = "उपशीर्षक भाषा सेट की गई: {value}"
    AUDIO_SET_MSG = "ऑडियो सेट किया गया: {value}"
    FILTERS_UPDATED_MSG = "फ़िल्टर अपडेट किए गए"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙वापस"
    CLOSE_BUTTON_TEXT = "🔚बंद करें"
    LIST_BUTTON_TEXT = "📃सूची"
    IMAGE_BUTTON_TEXT = "🖼छवि"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ गुणवत्ता स्वचालित रूप से पहचानी नहीं गई\nसभी उपलब्ध प्रारूपों को देखने के लिए 'Other' बटन का उपयोग करें।</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **लाइव स्ट्रीम पहचानी गई**\n\nचल रही या अनंत लाइव स्ट्रीम को डाउनलोड करने की अनुमति नहीं है।\n\nकृपया स्ट्रीम के समाप्त होने का इंतजार करें और फिर से डाउनलोड करने का प्रयास करें जब:\n• स्ट्रीम की अवधि ज्ञात हो\n• स्ट्रीम समाप्त हो गई हो\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>लाइव स्ट्रीम डाउनलोड</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "भाग {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "अधिकतम आकार: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "कुल अवधि: {duration} सेकंड"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>लाइव स्ट्रीम - भाग {chunk}</b>\n⏱ अवधि: {duration} सेकंड\n📦 आकार: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "भाग {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>लाइव स्ट्रीम डाउनलोड पूर्ण</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "{chunks} भाग डाउनलोड किए गए"
    LIVE_STREAM_TOTAL_DURATION_MSG = "कुल अवधि: {duration} सेकंड"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>लाइव स्ट्रीम डाउनलोड रोक दिया गया</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "उपयोगकर्ता निर्देशिका हटा दी गई (शायद /clean कमांड द्वारा)"
    LIVE_STREAM_FILE_DELETED_MSG = "भाग फ़ाइल हटा दी गई (शायद /clean कमांड द्वारा)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ स्ट्रीम समाप्त हो गई"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "कृपया `/format` कमांड का उपयोग करके एक अलग प्रारूप चुनें।"
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>सीधा लिंक प्राप्त हुआ</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>शीर्षक:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>अवधि:</b> {duration} सेकंड\n"
    FORMAT_FIELD_MSG = "🎛 <b>प्रारूप:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>वीडियो स्ट्रीम:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>ऑडियो स्ट्रीम:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **फ़ाइल प्रोसेसिंग त्रुटि**\n\nवीडियो डाउनलोड हो गया लेकिन फ़ाइल नाम में अमान्य वर्णों के कारण प्रोसेस नहीं किया जा सका।\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **फ़ाइल प्रोसेसिंग त्रुटि**\n\nवीडियो डाउनलोड हो गया लेकिन अमान्य तर्क त्रुटि के कारण प्रोसेस नहीं किया जा सका।\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**कारण:**\n"
        "• डाउनलोड की गई फ़ाइल एक वीडियो फ़ाइल नहीं है\n"
        "• यह एक दस्तावेज़ (PDF, DOC, आदि) या संग्रह हो सकता है\n\n"
        "**समाधान:**\n"
        "• लिंक जांचें - यह एक दस्तावेज़ की ओर ले जा सकता है, वीडियो नहीं\n"
        "• एक अलग लिंक या स्रोत आज़माएं\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**कारण:**\n"
        "• फ़ाइल को वीडियो के रूप में प्रसंस्कृत नहीं किया जा सकता\n"
        "• यह वीडियो फ़ाइल नहीं हो सकती या फ़ाइल क्षतिग्रस्त हो सकती है\n\n"
        "**समाधान:**\n"
        "• लिंक जांचें - यह एक दस्तावेज़ की ओर ले जा सकता है, वीडियो नहीं\n"
        "• एक अलग लिंक या स्रोत आज़माएं\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **प्रारूप उपलब्ध नहीं**\n\nअनुरोधित वीडियो प्रारूप इस वीडियो के लिए उपलब्ध नहीं है।\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ प्रारूप ID {format_id} इस वीडियो के लिए नहीं मिला।\n\nउपलब्ध प्रारूप IDs: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **AV1 प्रारूप इस वीडियो के लिए उपलब्ध नहीं है।**\n\n**उपलब्ध प्रारूप:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **फ़ाइल प्रोसेसिंग त्रुटि**\n\nऑडियो डाउनलोड हो गया लेकिन फ़ाइल नाम में अमान्य वर्णों के कारण प्रोसेस नहीं किया जा सका।\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **फ़ाइल प्रोसेसिंग त्रुटि**\n\nऑडियो डाउनलोड हो गया लेकिन अमान्य तर्क त्रुटि के कारण प्रोसेस नहीं किया जा सका।\n\n"
    
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
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "उपयोगकर्ता ने निषिद्ध सामग्री दर्ज की। डाउनलोड नहीं किया जा सकता।"
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "कमांड के माध्यम से NSFW धुंधलापन सेट: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "उपयोगकर्ता ने /nsfw मेनू खोला।"
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: बंद।"
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "{service} कुकी डाउनलोड करने में विफल: स्थिति={status} (url छिपा हुआ)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "{service} कुकी डाउनलोड करने में त्रुटि: {error} (url छिपा हुआ)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "{service} कुकी डाउनलोड करते समय अप्रत्याशित त्रुटि (url छिपा हुआ): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए कुकी फ़ाइल अपडेट की गई।"
    COOKIES_INVALID_CONTENT_LOG_MSG = "उपयोगकर्ता {user_id} द्वारा अमान्य कुकी सामग्री प्रदान की गई।"
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "उपयोगकर्ता {user_id} के लिए YouTube कुकी URL खाली हैं।"
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए स्रोत {source} से YouTube कुकीज़ डाउनलोड और सत्यापित की गईं।"
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए सभी YouTube कुकी स्रोत विफल।"
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "व्यवस्थापक {admin_id} द्वारा check_porn कमांड में त्रुटि: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "विभाजन भाग आकार {size} बाइट्स पर सेट किया गया।"
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "फ़ाइल विभाजन के साथ वीडियो अपलोड पूरा हुआ।"
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "प्लेलिस्ट वीडियो भेजे गए: {sent}/{total} फ़ाइलें (गुणवत्ता={quality}) उपयोगकर्ता {user_id} को"
    UNKNOWN_ERROR_MSG = "❌ अज्ञात त्रुटि: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "इंडेक्स {index} पर प्लेलिस्ट में असमर्थित फ़ाइल प्रकार को छोड़ा जा रहा है"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg नहीं मिला। कृपया FFmpeg इंस्टॉल करें।"
    CONVERSION_TO_MP4_FAILED_MSG = "❌ MP4 में रूपांतरण विफल: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ उपशीर्षक एंबेड करने में लंबा समय लग सकता है (वीडियो के प्रति 1 मिनट 1 मिनट तक)!\n🔥 उपशीर्षक बर्न करना शुरू हो रहा है..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ सीमाओं के कारण उपशीर्षक एंबेड नहीं किए जा सकते (गुणवत्ता/अवधि/आकार)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ चयनित भाषा के लिए उपशीर्षक उपलब्ध नहीं हैं"
    ERROR_SENDING_VIDEO_MSG = "❌ वीडियो भेजने में त्रुटि: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ प्लेलिस्ट वीडियो भेजे गए: {sent}/{total} फ़ाइलें।"
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ टाइमआउट के कारण डाउनलोड रद्द किया गया (2 घंटे)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ वीडियो डाउनलोड करने में विफल: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ त्रुटि: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON एक ऑब्जेक्ट (डिक्शनरी) होना चाहिए।"
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ अमान्य JSON प्रारूप। कृपया वैध JSON प्रदान करें।"
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ मान {min_val} और {max_val} के बीच होना चाहिए।"
    ARGS_PARAM_SET_TO_MSG = "✅ {description} सेट किया गया: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ सही"
    ARGS_FALSE_BUTTON_MSG = "❌ गलत"
    ARGS_BACK_BUTTON_MSG = "🔙 वापस"
    ARGS_CLOSE_BUTTON_MSG = "🔚 बंद करें"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ सही"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ गलत"
    ARGS_NOT_SET_MSG = "सेट नहीं"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["सही", "हाँ", "हां", "True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["गलत", "नहीं", "False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ AV1 प्रारूप इस वीडियो के लिए उपलब्ध नहीं है।\n\nउपलब्ध प्रारूप:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ डाउनलोड करने में त्रुटि: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ इंडेक्स {index} पर प्लेलिस्ट में कोई वीडियो नहीं मिला।"
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **वीडियो रूपांतरण विफल**\n\nअमान्य तर्क त्रुटि के कारण वीडियो को MP4 में रूपांतरित नहीं किया जा सका।\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **वीडियो रूपांतरण विफल**\n\nवीडियो को MP4 में रूपांतरित नहीं किया जा सका।\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ स्ट्रीम लिंक प्राप्त करने में विफल"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>लिंक प्राप्त करने में त्रुटि:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ इंडेक्स {index} पर कोई सामग्री नहीं मिली"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ त्रुटि: मूल संदेश नहीं मिला।"
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ त्रुटि: URL नहीं मिला।"
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ यह URL एंबेड नहीं किया जा सकता।"
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} कोडेक इस वीडियो के लिए उपलब्ध नहीं"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} प्रारूप इस वीडियो के लिए उपलब्ध नहीं"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ फ्लड सीमा। बाद में प्रयास करें।"
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ कुकी जांचें"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ ऑटो (YouTube त्रुटि पर)"
    PROXY_OFF_BUTTON_MSG = "❌ OFF"
    PROXY_CLOSE_BUTTON_MSG = "🔚बंद करें"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 देश चुनें:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ देश चयन साफ़ करें"
    PROXY_COUNTRY_SELECTED_MSG = "✅ देश चयनित: {देश} (कोड: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 उपलब्ध प्रॉक्सी: {proxy_count} (HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 बॉट पहले HTTP का प्रयास करेगा, फिर SOCKS5 का"
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 चयनित देश के लिए प्रॉक्सी स्वचालित रूप से सक्षम हो गई"
    PROXY_COUNTRY_CLEARED_MSG = "✅ देश का चयन साफ़ हो गया"
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ देश का चयन साफ़ हो गया"
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ देश चयनित: {देश}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 फ़ाइल से देश का उपयोग करना: {देश}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 फ़ाइल से उपलब्ध देश: {गिनती}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 चयनित देश: {देश} (कोड: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ इस देश के लिए प्रॉक्सी सक्षम"
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ प्रॉक्सी अक्षम (सक्षम करने के लिए सभी (ऑटो) दबाएँ)"
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ ON"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ OFF"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚बंद करें"
    
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
    NSFW_ON_NO_BLUR_MSG = "✅ ऑन (बिना धुंधलापन)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ ऑन (बिना धुंधलापन)"
    NSFW_OFF_BLUR_MSG = "✅ ऑफ (धुंधलापन)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ ऑफ (धुंधलापन)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "साफ"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "उपयोगकर्ता {user} के लिए उत्तर संदेश प्रोसेस करने में त्रुटि: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "उपयोगकर्ता {user} को ब्रॉडकास्ट भेजने में त्रुटि: {error}"
    ADMIN_LOGS_FORMAT_MSG = "{bot_name} के लॉग\nउपयोगकर्ता: {user_id}\nकुल लॉग: {total}\nवर्तमान समय: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nकुल {path}: {count}\nवर्तमान समय: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>कुल उपयोगकर्ता: {count}</i>\nअंतिम 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "व्यवस्थापक {admin_id} द्वारा पोर्न कैश रीलोड किए गए। डोमेन: {domains}, कीवर्ड: {keywords}, साइटें: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "टाइमआउट संदेश भेजने में त्रुटि: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>भाषा चुनें</b>"
    LANG_CHANGED_MSG = "✅ भाषा {lang_name} में बदली गई"
    LANG_ERROR_MSG = "❌ भाषा बदलने में त्रुटि"
    LANG_CLOSED_MSG = "भाषा चयन बंद"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] कॉलबैक: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "URL के साथ ब्राउज़र मॉनिटरिंग बटन जोड़ रहे हैं: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "ब्राउज़र मॉनिटरिंग URL कॉन्फ़िगर नहीं: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **कीबोर्ड सेटिंग अपडेट की गई!**\n\nनई सेटिंग: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "कीबोर्ड छुपाने में विफल: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "उपयोगकर्ता {user_id} के लिए लिंक निष्कर्षण के लिए काम करने वाली YouTube कुकीज़ का उपयोग कर रहे हैं"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "उपयोगकर्ता {user_id} के लिए लिंक निष्कर्षण के लिए कोई काम करने वाली YouTube कुकीज़ उपलब्ध नहीं हैं"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "उपयोगकर्ता {user_id} के लिए लिंक निष्कर्षण के लिए मौजूदा YouTube कुकीज़ का उपयोग कर रहे हैं"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "उपयोगकर्ता {user_id} के लिए लिंक निष्कर्षण के लिए कोई YouTube कुकीज़ नहीं मिलीं"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "उपयोगकर्ता {user_id} फ़ोल्डर में लिंक निष्कर्षण के लिए वैश्विक कुकी फ़ाइल कॉपी की गई"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] उपयोगकर्ता {user_id} ने mediainfo कमांड का अनुरोध किया"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] उपयोगकर्ता {user_id} व्यवस्थापक है: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] उपयोगकर्ता {user_id} चैनल में है: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] उपयोगकर्ता {user_id} पहुंच अस्वीकृत - व्यवस्थापक नहीं और चैनल में नहीं"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] उपयोगकर्ता {user_id} पहुंच दी गई"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] कॉलबैक: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ यह कमांड केवल व्यवस्थापकों के लिए उपलब्ध है।"
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ PO टोकन सपोर्ट के साथ डाउनलोड पूरा हुआ"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ फ्लड सीमा। बाद में प्रयास करें।"
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST टोकन रिफ्रेश त्रुटि: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Firebase सत्र बंद करने में त्रुटि: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ बेस db संरचना प्रारंभ करने में त्रुटि: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ config.py में सभी पैरामीटर सेट नहीं हैं (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL सेट नहीं है"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey idToken प्राप्त करने के लिए सेट नहीं है"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Firebase डंप डाउनलोड करने में त्रुटि: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ REST के माध्यम से Firebase डंप डाउनलोड करने में विफल"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ _download_and_reload_cache में त्रुटि: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ ऑटो reload_cache चलाने में त्रुटि (प्रयास {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ सभी पुनःप्रयास विफल"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 {datetime} पर Firebase डंप डाउनलोड शुरू हो रहा है"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ निर्भरता उपलब्ध नहीं: requests या Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ डेटाबेस खाली है"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ लॉगर बंद करने में त्रुटि: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ सफाई के दौरान त्रुटि: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ क्लोन त्रुटि: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ क्लोन टाइमआउट"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ क्लोन अपवाद: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ उपयोगकर्ता द्वारा अपडेट रद्द"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ रिपॉजिटरी सफलतापूर्वक क्लोन की गई"
    UPDATE_BACKUPS_MOVED_MSG = "✅ बैकअप _backup/ में स्थानांतरित"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ सभी मॉड्यूल लोड हैं"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ निकास पर सफाई पूरी"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 सिग्नल {signal} प्राप्त हुआ, सहजता से बंद हो रहा है..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "कृपया प्रतीक्षा करें..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 HLS स्ट्रीम डाउनलोड हो रहा है:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "फ्रैगमेंट्स का इंतजार है"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ बैकअप {ts} _backup/ में नहीं मिला"
    RESTORE_FAILED_RESTORE_MSG = "❌ {src} -> {dest_path} रिस्टोर करने में विफल: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ रिस्टोर किया गया: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>विवरण:</b> {error_details}\n\nगंभीर त्रुटि के कारण डाउनलोड बंद हो गया।\n\n💡 <b>सुझाव:</b> यदि आपको 401 Unauthorized त्रुटि मिल रही है, तो <code>/cookie instagram</code> कमांड का उपयोग करने या Instagram के साथ प्रमाणित करने के लिए अपनी कुकीज़ भेजें।"
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ डोमेन पोर्न ब्लैकलिस्ट में है: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ पोर्न कीवर््ड मिले: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ डोमेन व्हाइटलिस्ट में है: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ व्हाइटलिस्ट कीवर््ड मिले: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ कोई पोर्न कीवर््ड नहीं मिले"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ इंडेक्स {index} पर TikTok API त्रुटि, अगले ऑडियो पर जाया जा रहा है..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ इंडेक्स {index} पर TikTok API त्रुटि, अगले वीडियो पर जाया जा रहा है..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "उपयोगकर्ता ने <b>url</b> दर्ज किया\n <b>उपयोगकर्ता का नाम:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>उपयोगकर्ता ने इस प्रकार दर्ज किया:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "चैनल जोड़ें"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 हैंडलर पंजीकृत कर रहे हैं: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - मेरी 5 कुकीज़ डाउनलोड करें"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - ब्राउज़र की YT-कुकी प्राप्त करें"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - अपनी कुकी फ़ाइल सत्यापित करें"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - कस्टम कुकी अपलोड करें"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 बंद करें"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "उपलब्ध प्रारूप: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "प्रारूप_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚बंद करें"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚बंद करें"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚बंद करें"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚बंद करें"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "मदद बंद।"
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "बंद"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "त्रुटि हुई"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "PATH या प्रोजेक्ट डायरेक्टरी में ffmpeg नहीं मिला। कृपया FFmpeg इंस्टॉल करें।"
    YTDLP_NOT_FOUND_MSG = "PATH या प्रोजेक्ट डायरेक्टरी में yt-dlp बाइनरी नहीं मिला। कृपया yt-dlp इंस्टॉल करें।"
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "वीडियो को {rounds} भागों में विभाजित किया जाएगा, जो अत्यधिक हो सकता है"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "वीडियो भाग {current}/{total} विभाजित कर रहे हैं: {start_time:.2f}s से {end_time:.2f}s तक"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "विभाजित भाग {part} बनाने में विफल: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "विभाजित भाग {part} सफलतापूर्वक बनाया गया: {target_name} ({size} बाइट्स)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "वीडियो भाग {part} विभाजित करने में त्रुटि: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "वीडियो सफलतापूर्वक {count} भागों में विभाजित किया गया"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "वीडियो विभाजन प्रक्रिया में त्रुटि: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] वीडियो {video_path} प्रोसेस करते समय त्रुटि: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "वीडियो फ़ाइल मौजूद नहीं है: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "आयाम '{size_result}' पार्स करने में त्रुटि: {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "'{size_result}' से वीडियो आयाम निर्धारित नहीं कर सके, डिफ़ॉल्ट का उपयोग कर रहे हैं: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "थंबनेल बनाने में त्रुटि: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "वीडियो अवधि पार्स करने में त्रुटि: {error}, परिणाम था: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "थंबनेल {thumb_dir} पर नहीं बनाया गया, डिफ़ॉल्ट का उपयोग कर रहे हैं"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "कमांड निष्पादन त्रुटि: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "FFmpeg के साथ थंबनेल बनाने में त्रुटि: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "गैर-डिक्शनरी कॉन्फ़िग सेक्शन छोड़ रहे हैं: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "सेटिंग {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] उपयोगकर्ता कुकीज़ का उपयोग कर रहे हैं: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "उपयोगकर्ता {user_id} के लिए YouTube कुकीज़ का उपयोग कर रहे हैं"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "उपयोगकर्ता {user_id} फ़ोल्डर में वैश्विक कुकी फ़ाइल कॉपी की गई"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] उपयोगकर्ता कुकीज़ के रूप में कॉपी की गई वैश्विक कुकीज़ का उपयोग कर रहे हैं: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "उपयोगकर्ता {user_id} के लिए वैश्विक कुकी फ़ाइल कॉपी करने में विफल: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "डोमेन के लिए --no-cookies का उपयोग कर रहे हैं: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "प्रॉक्सी अनुरोध किया गया लेकिन कॉन्फ़िग आयात/प्राप्त करने में विफल: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "gallery-dl के लिए प्रॉक्सी का उपयोग करने के लिए मजबूर: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "प्रॉक्सी अनुरोध किया गया लेकिन प्रॉक्सी कॉन्फ़िगरेशन अधूरा है"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "प्रॉक्सी हेल्पर विफल: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "एक्सट्रैक्टर आइटम्स पार्स कर रहे हैं..."
    GALLERY_DL_ITEM_COUNT_MSG = "आइटम {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "मेटाडेटा मिला (टैग 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL मिला (टैग 3): {url}, मेटाडेटा: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "मेटाडेटा मिला (लेगेसी): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL मिला (लेगेसी): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "फ़ाइलनाम मिला: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "डायरेक्टरी मिली: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "एक्सटेंशन मिला: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "{count} आइटम्स पार्स किए गए, जानकारी: {info}, फॉलबैक: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "gallery-dl कॉन्फ़िग सेट कर रहे हैं: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "रणनीति A आज़मा रहे हैं: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor मॉड्यूल नहीं मिला"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() इस बिल्ड में उपलब्ध नहीं है"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "extractor.find({url}) को कॉल कर रहे हैं"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "कोई एक्सट्रैक्टर URL से मेल नहीं खाता"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "एक्सट्रैक्टर पर कुकीज़ सेट कर रहे हैं: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "एक्सट्रैक्टर पर कुकीज़ सेट करने में विफल: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "एक्सट्रैक्टर मिला, items() को कॉल कर रहे हैं"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "रणनीति A सफल रही, जानकारी मिली: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "रणनीति A: extractor.items() ने कोई वैध जानकारी नहीं लौटाई"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "रणनीति A (extractor.find) विफल: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "--get-urls से फॉलबैक मेटाडेटा: कुल={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "मेटाडेटा प्राप्त करने के लिए सभी रणनीतियां विफल"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "छवि जानकारी निकालने में विफल: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job मॉड्यूल नहीं मिला (टूटी हुई इंस्टॉलेशन?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob इस बिल्ड में उपलब्ध नहीं है"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "gallery-dl डायरेक्टरी में डाउनलोड की गई फ़ाइलों की खोज कर रहे हैं"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "एक्सट्रैक्टर से नामों के आधार पर फ़ाइलें खोजने का प्रयास कर रहे हैं"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "उपयोगकर्ता {user_id} के लिए तर्क पढ़ने में त्रुटि: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] वीडियो {video_path} को प्रोसेस करते समय त्रुटि: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "उपयोगकर्ता {user_id} के पास send_as_file सक्षम है, दस्तावेज़ के रूप में भेज रहे हैं"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video बार-बार टाइमआउट हो रहा है; send_document पर वापस जा रहे हैं"
    SENDER_CAPTION_TOO_LONG_MSG = "कैप्शन बहुत लंबा है, न्यूनतम कैप्शन के साथ कोशिश कर रहे हैं"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (न्यूनतम कैप्शन) टाइमआउट हो गया; send_document पर वापस जा रहे हैं"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "न्यूनतम कैप्शन के साथ वीडियो भेजने में त्रुटि: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "पूर्ण विवरण फ़ाइल भेजने में त्रुटि: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "अस्थायी विवरण फ़ाइल हटाने में त्रुटि: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "NO_FILTER_DOMAINS में डोमेन के लिए match_filter छोड़ रहे हैं: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए उपयोगकर्ता के URL पर मौजूदा YouTube कुकीज़ की जांच कर रहे हैं"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "मौजूदा YouTube कुकीज़ उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए उपयोगकर्ता के URL पर काम करती हैं - उनका उपयोग कर रहे हैं"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "मौजूदा YouTube कुकीज़ उपयोगकर्ता के URL पर विफल, उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए नई प्राप्त करने का प्रयास कर रहे हैं"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए YouTube कुकी स्रोत {i} की कोशिश कर रहे हैं"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "स्रोत {i} से YouTube कुकीज़ उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए उपयोगकर्ता के URL पर काम करती हैं - उपयोगकर्ता फ़ोल्डर में सहेजी गईं"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "स्रोत {i} से YouTube कुकीज़ उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए उपयोगकर्ता के URL पर काम नहीं करतीं"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए स्रोत {i} से YouTube कुकीज़ डाउनलोड करने में विफल"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए सभी YouTube कुकी स्रोत विफल, कुकीज़ के बिना कोशिश करेंगे"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए कोई YouTube कुकी स्रोत कॉन्फ़िगर नहीं किए गए, कुकीज़ के बिना कोशिश करेंगे"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए कोई YouTube कुकीज़ नहीं मिलीं, नई प्राप्त करने का प्रयास कर रहे हैं"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए YouTube कुकीज़ का उपयोग कर रहे हैं (Always Ask मेनू में पहले से सत्यापित)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "उपयोगकर्ता {user_id} के लिए प्रारूप पहचान के लिए कोई YouTube कुकीज़ नहीं मिलीं, पुनर्स्थापित करने का प्रयास कर रहे हैं..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "प्रारूप पहचान के लिए वैश्विक कुकी फ़ाइल उपयोगकर्ता {user_id} फ़ोल्डर में कॉपी की गई"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "उपयोगकर्ता {user_id} के लिए वैश्विक कुकी फ़ाइल कॉपी करने में विफल: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "get_video_formats में डोमेन के लिए --no-cookies का उपयोग कर रहे हैं: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "ऐप अभी तक प्रारंभ नहीं हुआ। {name} तक पहुंच नहीं सकते"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>कैप्शन:</b> <code>{caption}</code>\n<b>उपयोगकर्ता ID:</b> <code>{user_id}</code>\n<b>उपयोगकर्ता का पहला नाम:</b> <code>{users_name}</code>\n<b>वीडियो फ़ाइल ID:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor में त्रुटि: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor में अप्रत्याशित त्रुटि: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 वीडियो URL</a>{quality_codec}{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "कॉन्फ़िगरेशन में FIREBASE_CONF.databaseURL अनुपस्थित है"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin प्रारंभ किया गया"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken रिफ्रेश किया गया"
    DB_LOG_FOR_USER_ADDED_MSG = "उपयोगकर्ता के लिए लॉग जोड़ा गया"
    DB_DATABASE_CREATED_MSG = "डेटाबेस बनाया गया"
    DB_BOT_STARTED_MSG = "बॉट शुरू किया गया"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY config.py में सहेजा गया: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "प्लेलिस्ट भाग पहले से कैश किया गया: {path_parts}, छोड़ रहे हैं"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: किसी भी URL/गुणवत्ता वेरिएंट के लिए कोई कैश नहीं मिला, खाली dict लौटा रहे हैं"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: बड़ी रेंज के लिए त्वरित गिनती: {cached_count} कैश किए गए वीडियो"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: हैश {url_hash}, गुणवत्ता {quality_key} के लिए कोई कैश नहीं मिला"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: किसी भी URL वेरिएंट के लिए कोई कैश नहीं मिला, None लौटा रहे हैं"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ पहुंच अस्वीकृत। केवल व्यवस्थापक।"
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 ऑटो Firebase कैश रीलोडिंग अपडेट की गई!\n\n📊 स्थिति: {status}\n⏰ शेड्यूल: हर {interval} घंटे 00:00 से\n🕒 अगला रीलोड: {next_exec} ({delta_min} मिनट में)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 ऑटो Firebase कैश रीलोडिंग बंद!\n\n📊 स्थिति: ❌ अक्षम\n💡 पुनः सक्षम करने के लिए /auto_cache on का उपयोग करें"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ अमान्य तर्क। /auto_cache on | off | N (1..168) का उपयोग करें"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ अंतराल 1 और 168 घंटे के बीच होना चाहिए"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ अंतराल सेट करने में विफल"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ ऑटो Firebase कैश अंतराल अपडेट किया गया!\n\n📊 स्थिति: ✅ सक्षम\n⏰ शेड्यूल: हर {interval} घंटे 00:00 से\n🕒 अगला रीलोड: {next_exec} ({delta_min} मिनट में)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 ऑटो Firebase कैश रीलोडिंग शुरू!\n\n📊 स्थिति: ✅ सक्षम\n⏰ शेड्यूल: हर {interval} घंटे 00:00 से\n🕒 अगला रीलोड: {next_exec} ({delta_min} मिनट में)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 ऑटो Firebase कैश रीलोडिंग बंद!\n\n📊 स्थिति: ❌ अक्षम\n💡 पुनः सक्षम करने के लिए /auto_cache on का उपयोग करें"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "ऑटो रीलोड सक्षम; अगला {next_exec} पर"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "व्यवस्थापक द्वारा ऑटो रीलोड अक्षम।"
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "ऑटो रीलोड अंतराल {interval}h पर सेट; अगला {next_exec} पर"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "ऑटो रीलोड शुरू; अगला {next_exec} पर"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "व्यवस्थापक द्वारा ऑटो रीलोड रोका गया।"
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase कैश लोड किया गया: {count} रूट नोड्स"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Firebase कैश फ़ाइल नहीं मिली, खाली कैश के साथ शुरू कर रहे हैं: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Firebase कैश लोड करने में विफल: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase कैश रीलोड किया गया: {count} रूट नोड्स"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Firebase कैश फ़ाइल नहीं मिली: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Firebase कैश रीलोड करने में विफल: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 आपको बॉट से बैन कर दिया गया है! अनबैन के लिए {Config.ADMIN_USERNAME} से संपर्क करें\n<blockquote>P.S. चैनल न छोड़ें - आपको स्वचालित रूप से बैन कर दिया जाएगा ⛔️</blockquote>\n🌍भाषा बदलें /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ कोई वीडियो प्रारूप नहीं मिले। छवि डाउनलोडर का प्रयास किया जा रहा है…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram ने संदेश भेजना सीमित कर दिया है।\n⏳ कृपया प्रतीक्षा करें: {time_str}\nटाइमर अपडेट करने के लिए URL दोबारा 2 बार भेजें।"
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>स्ट्रीम URL कॉपी करने के लिए बटन पर क्लिक करें, फिर इसे VLC ऐप में पेस्ट करें</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>स्ट्रीम URL कॉपी करने के लिए बटन पर क्लिक करें, फिर इसे VLC ऐप में पेस्ट करें</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>लिंक प्राप्त करने में त्रुटि:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ प्रारूप फ़ाइल भेजने में त्रुटि: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ प्रारूप प्राप्त करने में विफल:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 विश्लेषण किया जा रहा है... (6 सेकंड प्रतीक्षा करें)"
    AA_PROCESSING_MSG = "🔎 विश्लेषण किया जा रहा है..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ टैग #{wrong} में निषिद्ध वर्ण हैं। केवल अक्षर, अंक और _ की अनुमति है।\nकृपया उपयोग करें: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ समूह में काम करने के लिए बॉट को व्यवस्थापक अधिकारों की आवश्यकता है। कृपया इस समूह में बॉट को व्यवस्थापक बनाएं।"
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "नमस्ते {first_name},\n \n<i>यह बॉट🤖 किसी भी वीडियो को सीधे टेलीग्राम में डाउनलोड कर सकता है।😊 अधिक जानकारी के लिए <b>/help</b> दबाएं</i> 👈\n\n<blockquote>P.S. संभावित 🔞NSFW सामग्री के कारण - ☁️<b>क्लाउड स्टोरेज</b>, 📁<b>फाइल शेयर</b>, 🔗<b>URL शॉर्टनर</b> और 🔞<b>पोर्न साइट्स</b> से डाउनलोड भुगतान योग्य है! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ @tg_ytdlp चैनल को 🗑<b>मत हटाएं/अनसब्सक्राइब मत करें</b> और बॉट को 🤖<b>बहुत ज्यादा URL/कमांड स्पैम मत भेजें</b> - आपको बॉट उपयोग से स्वचालित रूप से प्रतिबंधित कर दिया जाएगा ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 हटाने के लिए कोई फ़ाइलें नहीं।"
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 सभी फ़ाइलें सफलतापूर्वक हटाई गईं!\n\nहटाई गई फ़ाइलें:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ कृपया प्रतीक्षा करें जब तक आपका पिछला डाउनलोड पूरा नहीं हो जाता"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "check_user में ऐप इंस्टेंस None है"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict None है, डाउनलोड की अनुमति दे रहे हैं"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict None है, उपशीर्षक एम्बेडिंग की अनुमति दे रहे हैं"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: सीमाएं जांच रहे हैं - अधिकतम_गुणवत्ता={max_quality}p, अधिकतम_अवधि={max_duration}s, अधिकतम_आकार={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: info_dict कुंजियां: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "उपशीर्षक एम्बेडिंग छोड़ी गई: अवधि {duration}s सीमा {max_duration}s से अधिक है"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "उपशीर्षक एम्बेडिंग छोड़ी गई: आकार {size_mb:.2f}MB सीमा {max_size}MB से अधिक है"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "उपशीर्षक एम्बेडिंग छोड़ी गई: गुणवत्ता {width}x{height} (न्यूनतम पक्ष {min_side}p) सीमा {max_quality}p से अधिक है"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "टिकटॉक"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "इंस्टाग्राम"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "प्लेलिस्ट"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ {service} के लिए रेंज सीमा पार: {count} (अधिकतम {max_count})।\n\nअधिकतम उपलब्ध फ़ाइलें डाउनलोड करने के लिए इनमें से एक कमांड का उपयोग करें:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ {service} के लिए रेंज सीमा पार: {count} (अधिकतम {max_count})\nउपयोगकर्ता ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "कॉन्फ़िग में PO टोकन प्रदाता अक्षम"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} YouTube डोमेन नहीं है, PO टोकन छोड़ रहे हैं"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO टोकन प्रदाता {base_url} पर उपलब्ध नहीं है, मानक YouTube निष्कर्षण पर वापस जा रहे हैं"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO टोकन प्रदाता कैश साफ़ किया गया, अगले अनुरोध पर उपलब्धता जांचेंगे"
    HELPER_POT_GENERIC_ARGS_MSG = "सामान्य:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "ऐप इंस्टेंस अभी तक उपलब्ध नहीं है"
    HELPER_USER_NAME_MSG = "उपयोगकर्ता"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "फ्लड वेट का पता चला, {wait_seconds} सेकंड के लिए सो रहे हैं"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "फ्लड वेट का पता चला लेकिन समय निकाल नहीं सके, {retry_delay} सेकंड के लिए सो रहे हैं"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno त्रुटि का पता चला, {retry_delay} सेकंड के लिए सो रहे हैं"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "प्रॉक्सी कॉन्फ़िगरेशन अधूरा है, प्रत्यक्ष कनेक्शन का उपयोग कर रहे हैं"
    HELPER_PROXY_COOKIE_PATH_MSG = "उपयोगकर्ता/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚बंद करें"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚बंद करें"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "यूट्यूब"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "टिकटॉक"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "इंस्टाग्राम"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "ट्विटर"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "कस्टम"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚बंद करें"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 लॉग फाइल हटा दी गई।"
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 टैग फाइल हटा दी गई।"
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 प्रारूप फाइल हटा दी गई।"
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 विभाजन फाइल हटा दी गई।"
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Mediainfo फाइल हटा दी गई।"
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 उपशीर्षक सेटिंग्स हटा दी गईं।"
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 कीबोर्ड सेटिंग्स हटा दी गईं।"
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Args सेटिंग्स हटा दी गईं।"
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 NSFW सेटिंग्स हटा दी गईं।"
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 प्रॉक्सी सेटिंग्स हटा दी गईं।"
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 फ्लड प्रतीक्षा सेटिंग्स हटा दी गईं।"
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚बंद करें"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 वीडियो डाउनलोड कमांड"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "उपयोग: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "उदाहरण:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (प्रत्यक्ष क्रम)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (उलटा क्रम)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "यह भी देखें: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "उपयोगकर्ता {user_id} ने add_bot_to_group कमांड बंद की"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "YouTube ID निकालने में विफल"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "थंबनेल डाउनलोड करने में विफल या यह बहुत बड़ा है"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "ऑडियो भाषा चुनें"
    AA_NO_SUBTITLES_DETECTED_MSG = "कोई उपशीर्षक नहीं मिला"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "उपशीर्षक भाषा चुनें"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "प्रमाणीकरण त्रुटि"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "खाता नहीं मिला"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "खाता अनुपलब्ध"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "दर सीमा पार हो गई"
    GALLERY_DL_NETWORK_ERROR_MSG = "नेटवर्क त्रुटि"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "सामग्री अनुपलब्ध"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "भौगोलिक प्रतिबंध"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "सत्यापन आवश्यक"
    GALLERY_DL_POLICY_VIOLATION_MSG = "नीति उल्लंघन"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "अज्ञात त्रुटि"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ डाउनलोड शुरू हुआ</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚बंद करें"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 वीडियो डाउनलोड कमांड</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "उपयोग: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>उदाहरण:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "यह भी देखें: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ फ्लड सीमा। बाद में प्रयास करें।"
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 कुकी कमांड उपयोग</b>

<code>/cookie</code> - कुकी मेनू दिखाएं
<code>/cookie youtube</code> - YouTube कुकीज़ डाउनलोड करें
<code>/cookie instagram</code> - Instagram कुकीज़ डाउनलोड करें
<code>/cookie tiktok</code> - TikTok कुकीज़ डाउनलोड करें
<code>/cookie x</code> या <code>/cookie twitter</code> - Twitter/X कुकीज़ डाउनलोड करें
<code>/cookie facebook</code> - Facebook कुकीज़ डाउनलोड करें
<code>/cookie custom</code> - कस्टम कुकी निर्देश दिखाएं

<i>उपलब्ध सेवाएं बॉट कॉन्फ़िगरेशन पर निर्भर करती हैं।</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 कुकी फाइल हटा दी गई और कैश साफ किया गया।"
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ पिछला"
    SUBS_BACK_BUTTON_MSG = "🔙वापस"
    SUBS_OFF_BUTTON_MSG = "🚫 बंद"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - भाषा सेट करें"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - AUTO/TRANS के साथ भाषा सेट करें"
    SUBS_VALID_OPTIONS_MSG = "मान्य विकल्प:"
    
    # Settings Command Messages
    SETTINGS_LANGUAGE_BUTTON_MSG = "🌍 भाषा"
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 डेव GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 कॉन्ट्र GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 साफ़"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 कुकीज़"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 मीडिया"
    SETTINGS_INFO_BUTTON_MSG = "📖 जानकारी"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ अधिक"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 केवल कुकीज़"
    SETTINGS_LOGS_BUTTON_MSG = "📃 लॉग "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ टैग"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 प्रारूप"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ विभाजन"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 मीडियाइन्फो"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 उपशीर्षक"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 कीबोर्ड"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ तर्क"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 प्रॉक्सी"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 फ्लड प्रतीक्षा"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  सभी फाइलें"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - मेरी 5 कुकीज़ डाउनलोड करें"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - ब्राउज़र की YT-कुकी प्राप्त करें"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - अपनी कुकी फाइल सत्यापित करें"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - कस्टम कुकी अपलोड करें"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /format - गुणवत्ता और प्रारूप बदलें"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - MediaInfo ON / OFF करें"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - विभाजित वीडियो भाग आकार बदलें"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /audio - वीडियो को ऑडियो के रूप में डाउनलोड करें"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - उपशीर्षक भाषा सेटिंग्स"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - प्लेलिस्ट कैसे डाउनलोड करें"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - gallery-dl के माध्यम से छवियां डाउनलोड करें"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - अपने #टैग भेजें"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /help - निर्देश प्राप्त करें"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage - अपने लॉग भेजें"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - प्लेलिस्ट की मदद"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - कैसे करें"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /link - सीधे वीडियो लिंक प्राप्त करें"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - प्रॉक्सी सक्षम/अक्षम करें"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - कीबोर्ड लेआउट"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /search - इनलाइन खोज सहायक"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp तर्क"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - NSFW ब्लर सेटिंग्स"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 सफाई विकल्प</b>\n\nक्या साफ करना है चुनें:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 मोबाइल: @vid खोज सक्रिय करें"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 मोबाइल: @vid खोज सक्रिय करें"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 बंद"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 पूर्ण"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[छवियों का URL]({url})"
    IMAGE_ERROR_MSG = "❌ त्रुटि: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙वापस"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - कस्टम फॉर्मेट"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p गुणवत्ता"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K गुणवत्ता"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K गुणवत्ता"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - विशिष्ट फॉर्मेट ID"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - हमेशा मेनू दिखाएं"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/सर्वोत्तम गुणवत्ता"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ हमेशा पूछें (मेनू + बटन)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 अन्य (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (PC/Mac Telegram के लिए सबसे अच्छा)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (मोबाइल Telegram के लिए सबसे अच्छा)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (अधिकतम गुणवत्ता)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 कस्टम (अपना दर्ज करें)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 ब्राउज़र से"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 अपना खुद का"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ निष्क्रियता के कारण इनपुट मोड स्वचालित रूप से बंद हो गया (5 मिनट)।"
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 सभी रीसेट करें"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 वर्तमान देखें"
    ARGS_BACK_BUTTON_MSG = "🔙 वापस"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>इन सेटिंग्स को टेम्प्लेट के रूप में सहेजने के लिए इस संदेश को अपने पसंदीदा में फॉरवर्ड करें।</i> \n\n<i>इन सेटिंग्स को लागू करने के लिए इस संदेश को वापस यहां फॉरवर्ड करें।</i>"
    ARGS_NO_SETTINGS_MSG = "📋 वर्तमान yt-dlp तर्क:\n\nकोई कस्टम सेटिंग्स कॉन्फ़िगर नहीं की गई।\n\n---\n\n<i>इन सेटिंग्स को टेम्प्लेट के रूप में सहेजने के लिए इस संदेश को अपने पसंदीदा में फॉरवर्ड करें।</i> \n\n<i>इन सेटिंग्स को लागू करने के लिए इस संदेश को वापस यहां फॉरवर्ड करें।</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 वर्तमान yt-dlp तर्क:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 सेटिंग्स निर्यात करें"
    ARGS_SETTINGS_READY_MSG = "सेटिंग्स निर्यात के लिए तैयार! सहेजने के लिए इस संदेश को पसंदीदा में फॉरवर्ड करें।"
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 वर्तमान yt-dlp तर्क:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ संदेश में सेटिंग्स को पहचानने में विफल। सुनिश्चित करें कि आपने सही सेटिंग्स टेम्प्लेट भेजा है।"
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ सेटिंग्स सफलतापूर्वक आयात की गईं!\n\nलागू किए गए पैरामीटर: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "मुख्य सेटिंग्स:\n"
    ARGS_ERROR_SAVING_MSG = "❌ आयातित सेटिंग्स सहेजने में त्रुटि।"
    ARGS_ERROR_IMPORTING_MSG = "❌ सेटिंग्स आयात करते समय एक त्रुटि हुई।"

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>Cookie फाइलें डाउनलोड करें</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "Cookie फाइल डाउनलोड करने के लिए एक सेवा चुनें।"
    COOKIE_MENU_SAVE_INFO_MSG = "Cookie फाइलें आपके फोल्डर में cookie.txt के रूप में सहेजी जाएंगी।"
    COOKIE_MENU_TIP_HEADER_MSG = "टिप: आप सीधी कमांड का भी उपयोग कर सकते हैं:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – cookies डाउनलोड और सत्यापित करें"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – इंडेक्स द्वारा विशिष्ट स्रोत का उपयोग करें (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "फिर <code>/check_cookie</code> के साथ सत्यापित करें (RickRoll पर परीक्षण)।"

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "हमेशा पूछें"
    SUBS_AUTO_TRANS_BUTTON_MSG = "स्वचालित/अनुवाद"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗लिंक"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁देखें"  # अस्थायी रूप से अक्षम: poketube सेवा डाउन है
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝विवरण"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ ट्रिम"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>वीडियो ट्रिम</b>\n\nवीडियो अवधि: <b>{start_time} - {end_time}</b>\n\nकृपया वांछित समय सीमा प्रारूप में भेजें:\n<code>HH:MM:SS-HH:MM:SS</code>\n\nउदाहरण: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ अमान्य प्रारूप। कृपया उपयोग करें: <code>HH:MM:SS-HH:MM:SS</code>\n\nउदाहरण: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ अमान्य सीमा। प्रारंभ समय अंत समय से कम होना चाहिए।"
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ समय सीमा वीडियो की सीमाओं से बाहर है।\n\nवीडियो अवधि: <b>{start_time} - {end_time}</b>\n\nआपकी सीमा इन सीमाओं के भीतर होनी चाहिए।"
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>वीडियो काटा जाएगा:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ आंशिक रूप से पूर्ण - {successful_uploads}/{total_files} ऑडियो फ़ाइलें अपलोड की गईं।"
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ ऑडियो सफलतापूर्वक डाउनलोड और भेजा गया - {total_files} फ़ाइलें अपलोड की गईं।"

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>निजी TikTok खाता</b>\n\n"
        "यह TikTok खाता निजी है या सभी वीडियो निजी हैं।\n\n"
        "<b>💡 समाधान:</b>\n"
        "1. खाते @{username} को फॉलो करें\n"
        "2. <code>/cookie</code> कमांड का उपयोग करके बॉट को अपने cookies भेजें\n"
        "3. फिर से कोशिश करें\n\n"
        "<b>cookies अपडेट करने के बाद, फिर से कोशिश करें!</b>"
    )

    #######################################################
