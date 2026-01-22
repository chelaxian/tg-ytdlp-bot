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
    CREDITS_MSG = "<blockquote><i>관리자</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>\n<b>🌍 언어 변경: /lang</b>"
    TO_USE_MSG = "<i>이 봇을 사용하려면 @tg_ytdlp Telegram 채널에 구독해야 합니다.</i>\n채널에 가입한 후, <b>비디오 링크를 다시 보내시면 봇이 다운로드해 드립니다</b> ❤️\n\n<blockquote>P.S. 🔞NSFW 콘텐츠 및 ☁️클라우드 스토리지에서 파일 다운로드는 유료입니다! 1⭐️ = $0.02</blockquote>\n<blockquote>P.P.S. ‼️ 채널을 떠나지 마세요 - 봇 사용이 금지됩니다 ⛔️</blockquote>"

    ERROR1 = "URL 링크를 찾을 수 없습니다. <b>https://</b> 또는 <b>http://</b>가 포함된 URL을 입력하세요"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>재생 목록 (yt-dlp)</b>

재생 목록을 다운로드하려면 URL 끝에 <code>*start*end</code> 범위를 붙여 보내세요. 예: <code>URL*1*5</code> (1부터 5까지 처음 5개 동영상 포함).<code>URL*-1*-5</code> (1부터 5까지 마지막 5개 동영상 포함).
또는 <code>/vid 시작-끝 URL</code>을 사용할 수 있습니다. 예: <code>/vid 3-7 URL</code> (처음부터 3부터 7까지 동영상 다운로드). <code>/vid -3-7 URL</code> (끝부터 3부터 7까지 동영상 다운로드). <code>/audio</code> 명령에도 작동합니다.

<b>예제:</b>

🟥 <b>YouTube 재생 목록의 동영상 범위:</b> (🍪 필요)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(1부터 5까지 처음 5개 동영상 다운로드)
🟥 <b>YouTube 재생 목록의 단일 동영상:</b> (🍪 필요)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(3번째 동영상만 다운로드)

⬛️ <b>TikTok 프로필:</b> (🍪 필요)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(사용자 프로필에서 처음 10개 동영상 다운로드)

🟪 <b>Instagram 스토리:</b> (🍪 필요)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(처음 3개 스토리 다운로드)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(앨범에서 처음 10개 스토리 다운로드)

🟦 <b>VK 동영상:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(사용자/그룹 프로필에서 처음 3개 동영상 다운로드)

⬛️<b>Rutube 채널:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(채널에서 2부터 4까지 동영상 다운로드)

🟪 <b>Twitch 클립:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(채널에서 처음 3개 클립 다운로드)

🟦 <b>Vimeo 그룹:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(그룹에서 처음 2개 동영상 다운로드)

🟧 <b>Pornhub 모델:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(모델 프로필에서 처음 2개 동영상 다운로드)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(프롬프트에 따른 검색 결과에서 처음 3개 동영상 다운로드)

등등...
<a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">지원 사이트 목록</a> 참조
</blockquote>

<blockquote expandable>🖼 <b>이미지 (gallery-dl)</b>

여러 플랫폼에서 이미지/사진/앨범을 다운로드하려면 <code>/img URL</code>을 사용하세요.

<b>예제:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>범위:</b>
<code>/img 11-20 https://example.com/album</code> — 항목 11..20
<code>/img 11- https://example.com/album</code> — 11부터 끝까지 (또는 봇 제한)

<i>지원 플랫폼에는 vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor 등이 포함됩니다. 전체 목록:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">gallery-dl 지원 사이트</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>동영상 다운로드 봇 - 도움말</b>

📥 <b>기본 사용법:</b>
• 링크 보내기 → 봇이 다운로드
  <i>봇은 자동으로 yt-dlp를 통해 동영상을, gallery-dl을 통해 이미지를 다운로드하려고 시도합니다.</i>
• <b>여러 URL:</b> 품질 선택 모드(<code>/format</code>)에서 한 메시지에 최대 <b>10개의 URL</b>을 보낼 수 있습니다. 각 URL은 새 줄에 있거나 공백으로 구분됩니다.
• <code>/audio URL</code> → 오디오 추출
• <code>/link [quality] URL</code> → 직접 링크 가져오기
• <code>/proxy</code> → 모든 다운로드에 대한 프록시 활성화/비활성화
• 동영상에 텍스트로 답장 → 캡션 변경

📋 <b>재생 목록 및 범위:</b>
• <code>URL*1*5</code> → 처음 5개 동영상 다운로드
• <code>URL*-1*-5</code> → 마지막 5개 동영상 다운로드
• <code>/vid 3-7 URL</code> → <code>URL*3*7</code>이 됨
• <code>/vid -3-7 URL</code> → <code>URL*-3*-7</code>이 됨

🍪 <b>쿠키 및 비공개:</b>
• 비공개 동영상용 *.txt 쿠키 업로드
• <code>/cookie [service]</code> → 쿠키 다운로드 (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → 인덱스로 소스 선택 (1–N)
• <code>/cookies_from_browser</code> → 브라우저에서 추출
• <code>/check_cookie</code> → 쿠키 확인
• <code>/save_as_cookie</code> → 텍스트를 쿠키로 저장

🧹 <b>정리:</b>
• <code>/clean</code> → 미디어 파일만
• <code>/clean all</code> → 모든 것
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>설정:</b>
• <code>/settings</code> → 설정 메뉴
• <code>/format</code> → 품질 및 형식
• <code>/split</code> → 동영상을 여러 부분으로 분할
• <code>/mediainfo on/off</code> → 미디어 정보
• <code>/nsfw on/off</code> → NSFW 흐림
• <code>/tags</code> → 저장된 태그 보기
• <code>/sub on/off</code> → 자막
• <code>/keyboard</code> → 키보드 (OFF/1x3/2x3)

🏷️ <b>태그:</b>
• URL 뒤에 <code>#tag1#tag2</code> 추가
• 태그는 캡션에 표시됨
• <code>/tags</code> → 모든 태그 보기

🔗 <b>직접 링크:</b>
• <code>/link URL</code> → 최고 품질
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → 특정 품질

⚙️ <b>빠른 명령:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → 품질 설정
• <code>/keyboard off/1x3/2x3/full</code> → 키보드 레이아웃
• <code>/split 100mb-2000mb</code> → 부분 크기 변경
• <code>/subs off/ru/en auto</code> → 자막 언어
• <code>/list URL</code> → 사용 가능한 형식 목록
• <code>/mediainfo on/off</code> → 미디어 정보 켜기/끄기
• <code>/proxy on/off</code> → 모든 다운로드에 대한 프록시 활성화/비활성화

📊 <b>정보:</b>
• <code>/usage</code> → 다운로드 기록
• <code>/search</code> → @vid를 통한 인라인 검색

🖼 <b>이미지:</b>
• <code>URL</code> → 이미지 URL 다운로드
• <code>/img URL</code> → URL에서 이미지 다운로드
• <code>/img 11-20 URL</code> → 특정 범위 다운로드
• <code>/img 11- URL</code> → 11번째부터 끝까지 다운로드

👨‍💻 <i>개발자:</i> @upekshaip
🤝 <i>기여자:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "쿠키를 <b><u>cookie.txt</u></b>로 저장하고 봇에 문서로 보내세요.\n\n"
        "<b><u>/save_as_cookie</u></b> 명령으로 일반 텍스트로 쿠키를 보낼 수도 있습니다.\n"
        "<b><b><u>/save_as_cookie</u></b> 사용법:</b>\n\n"
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
        "<b><u>지침:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message
    SEARCH_MSG = """
🔍 <b>동영상 검색</b>

아래 버튼을 눌러 @vid를 통해 인라인 검색을 활성화하세요.

<blockquote>PC에서는 채팅에서 <b>"@vid Your_Search_Query"</b>를 입력하세요.</blockquote>
    """
    
    # Settings and Hints
    
    
    IMG_HELP_MSG = (
        "<b>🖼 이미지 다운로드 명령</b>\n\n"
        "사용법: <code>/img URL</code>\n\n"
        "<b>예제:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>지원 플랫폼 (예제):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor 등 — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">전체 목록</a></blockquote>"
        "참고: "
    )
    
    LINK_HINT_MSG = (
        "품질 선택과 함께 직접 동영상 링크를 가져오세요.\n\n"
        "사용법: /link + URL \n\n"
        "(예: /link https://youtu.be/abc123)\n"
        "(예: /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>그룹에 봇 추가</b>

향상된 기능과 더 높은 제한을 위해 그룹에 내 봇을 추가하세요!
————————————
📊 <b>현재 무료 제한 (봇 DM):</b>
<blockquote>•🗑 정렬되지 않은 모든 파일의 지저분한 정크 👎
• 최대 1개 파일 크기: <b>8 GB </b>
• 최대 1개 파일 품질: <b>무제한</b>
• 최대 1개 파일 지속 시간: <b>무제한</b>
• 최대 다운로드 수: <b>무제한</b>
• 한 메시지의 최대 URL: <b>10</b> (품질 선택 모드에서만)
• 1회당 최대 재생 목록 항목: <b>50</b>
• 1회당 최대 TikTok 동영상: <b>500</b>
• 1회당 최대 이미지: <b>1000</b>
• URL 속도 제한: <b>5/분, 60/시간, 1000/일</b>
• 명령 제한: <b>20/분</b>
• 1회 다운로드 최대 시간: <b>2시간</b>
• 🔞 NSFW 콘텐츠는 유료입니다! 1⭐️ = $0.02
• 🆓 다른 모든 미디어는 완전 무료입니다
• 📝 모든 콘텐츠 로그 및 캐싱은 재다운로드 시 즉시 재게시를 위해 내 로그 채널로</blockquote>

💬<b>이 제한은 자막이 있는 동영상에만 해당:</b>
<blockquote>• 최대 동영상+자막 지속 시간: <b>1.5시간</b>
• 최대 동영상+자막 파일 크기: <b>500 MB</b>
• 최대 동영상+자막 품질: <b>720p</b></blockquote>
————————————
🚀 <b>유료 그룹 혜택 (2️⃣x 제한):</b>
<blockquote>•  🗂 주제별로 정렬된 구조화된 깔끔한 미디어 저장소 👍
•  📁 봇이 호출한 주제에서 응답
•  📌 다운로드 진행 상황이 있는 자동 고정 상태 메시지
•  🖼 /img 명령이 미디어를 10개 항목 앨범으로 다운로드
• 최대 1개 파일 크기: <b>16 GB</b> ⬆️
• 한 메시지의 최대 URL: <b>20</b> ⬆️ (품질 선택 모드에서만)
• 1회당 최대 재생 목록 항목: <b>100</b> ⬆️
• 1회당 최대 TikTok 동영상: 1000 ⬆️
• 1회당 최대 이미지: 2000 ⬆️
• URL 속도 제한: <b>10/분, 120/시간, 2000/일</b> ⬆️
• 명령 제한: <b>40/분</b> ⬆️
• 1회 다운로드 최대 시간: <b>4시간</b> ⬆️
• 🔞 NSFW 콘텐츠: 전체 메타데이터와 함께 무료 🆓
• 📢 그룹의 경우 내 채널 구독 불필요
• 👥 모든 그룹 구성원이 유료 기능에 액세스할 수 있습니다!
• 🗒 내 로그 채널에 로그 없음 / 캐시 없음! 그룹 설정에서 복사/재게시를 거부할 수 있습니다</blockquote>

💬 <b>자막이 있는 동영상의 2️⃣x 제한:</b>
<blockquote>• 최대 동영상+자막 지속 시간: <b>3시간</b> ⬆️
• 최대 동영상+자막 파일 크기: <b>1000 MB</b> ⬆️
• 최대 동영상+자막 품질: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>가격 및 설정:</b>
<blockquote>• 가격: <b>$5/월</b> 그룹당 1개 봇
• 설정: @iilililiiillliiliililliilliliiil 연락
• 결제: 💎TON 또는 기타 방법💲
• 지원: 전체 기술 지원 포함</blockquote>
————————————
그룹에 내 봇을 추가하여 무료 🔞<b>NSFW</b>를 차단 해제하고 모든 제한을 두 배로 늘릴 수 있습니다.
그룹이 내 봇을 사용하도록 허용하려면 @iilililiiillliiliililliilliliiil로 연락하세요
————————————
💡<b>팁:</b> <blockquote>친구들과 함께 어떤 금액이든 모금할 수 있습니다(예: 100명) 그리고 전체 그룹을 위해 1회 구매를 하면 - 모든 그룹 구성원이 해당 그룹의 모든 봇 기능에 완전 무제한 액세스를 갖게 됩니다 단 <b>$0.05</b>만으로</blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW 모드: 켜짐✅</b>

• NSFW 콘텐츠가 흐림 없이 표시됩니다.
• 스포일러가 NSFW 미디어에 적용되지 않습니다.
• 콘텐츠가 즉시 표시됩니다

<i>흐림을 활성화하려면 /nsfw off를 사용하세요</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW 모드: 꺼짐</b>

⚠️ <b>흐림 활성화됨</b>
• NSFW 콘텐츠가 스포일러 아래에 숨겨집니다   
• 보려면 미디어를 클릭해야 합니다
• 스포일러가 NSFW 미디어에 적용됩니다.

<i>흐림을 비활성화하려면 /nsfw on을 사용하세요</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>잘못된 매개변수</b>

사용:
• <code>/nsfw on</code> - 흐림 비활성화
• <code>/nsfw off</code> - 흐림 활성화
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>캐시 확인 중...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 처리 중..."
    DOWNLOADING_MSG = "📥 <b>미디어 다운로드 중...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>이미지 다운로드 중...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>다운로드 완료</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "다운로드됨:"
    SENT_STATUS_MSG = "전송됨:"
    PENDING_TO_SEND_STATUS_MSG = "전송 대기 중:"
    TITLE_LABEL_MSG = "제목:"
    MEDIA_COUNT_LABEL_MSG = "미디어 수:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "다운로드 완료, 오디오 처리 중..."
    VIDEO_PROCESSING_MSG = "📽 동영상 처리 중..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>캐시에서 전송됨</b>\n\n전송된 앨범: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ 동영상이 캐시에서 성공적으로 전송되었습니다."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ 재생 목록 동영상이 캐시에서 전송되었습니다 ({cached}/{total} 파일)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} 동영상이 캐시에서 전송되었으며, 누락된 항목 다운로드 중..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ 캐시에서 전송됨: {cached}\n🔄 다운로드 계속 중..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 미디어를 분석할 수 없어 허용된 최대 범위로 진행 중 (1-{fallback_limit})..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 미디어 수를 확인할 수 없어 허용된 최대 범위로 진행 중 (1-{total_limit})..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 총 미디어 수를 확인할 수 없어 지정된 범위로 진행 중 {start}-{end}..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>잘못된 URL</b>\n\nhttp:// 또는 https://로 시작하는 유효한 URL을 제공하세요"

    ERROR_OCCURRED_MSG = "❌ <b>오류 발생</b>\n\n<code>{url}</code>\n\n오류: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ 동영상 전송 오류: {error}"
    ERROR_UNKNOWN_MSG = "❌ 알 수 없는 오류: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ 동영상을 다운로드할 디스크 공간이 부족합니다."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ 파일 크기가 {limit} GB 제한을 초과했습니다. 허용된 크기 내에서 더 작은 파일을 선택하세요."
    ERROR_ALL_PROXIES_FAILED_MSG = "❌ <b>사용 가능한 모든 프록시로 비디오 다운로드 실패</b>\n\n프록시를 통한 모든 다운로드 시도가 실패했습니다.\n시도해 보세요:\n• 프록시 기능 확인\n• 목록에서 다른 프록시 시도\n• 프록시 없이 다운로드 (가능한 경우)"

    ERROR_GETTING_LINK_MSG = "❌ <b>링크 가져오기 오류:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram이 메시지 전송을 제한했습니다.\n⏳ 대기하세요: {time}\n타이머를 업데이트하려면 URL을 다시 2번 보내세요."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram이 메시지 전송을 제한했습니다.\n⏳ 대기하세요: \n타이머를 업데이트하려면 URL을 다시 2번 보내세요."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ 자막 다운로드 실패"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>직접 스트림 링크</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>제목:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>지속 시간:</b> {duration}초\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ 오류: 원본 메시지를 찾을 수 없습니다."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ 태그 #{tag}에 금지된 문자가 포함되어 있습니다. 문자, 숫자 및 _만 허용됩니다.\n사용: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ 재생 목록 동영상 전송됨: {sent}/{total} 파일."
    
    PLAYLIST_AUTO_RANGE_HINT_MSG = """💡 <b>재생 목록 팁</b>

범위를 지정하지 않고 재생 목록 링크를 보냈습니다. 봇이 자동으로 첫 번째 동영상을 다운로드했습니다 (<code>*1*1</code>).

<b>재생 목록에서 여러 동영상을 다운로드하려면 범위를 지정하세요:</b>
• <code>URL*1*5</code> — 처음 5개 동영상 (1~5 포함)
• <code>URL*3*3</code> — 3번째 동영상만
• <code>/vid 1-10 URL</code> — 대체 형식

자세히 알아보기: <code>/playlist</code>"""
    PLAYLIST_CACHE_SENT_MSG = "✅ 캐시에서 전송됨: {cached}/{total} 파일."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ 스트림 링크 가져오기 실패"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "쿠키를 다운로드할 브라우저 선택:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "이 시스템에서 브라우저를 찾을 수 없습니다. 원격 URL에서 쿠키를 다운로드하거나 브라우저 상태를 모니터링할 수 있습니다:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>브라우저 열기</b> - 미니 앱에서 브라우저 상태 모니터링"
    BROWSER_OPEN_BUTTON_MSG = "🌐 브라우저 열기"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 원격 URL에서 다운로드"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube 쿠키 파일이 fallback을 통해 다운로드되어 cookie.txt로 저장되었습니다"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ 지원되는 브라우저를 찾을 수 없고 COOKIE_URL이 구성되지 않았습니다. /cookie를 사용하거나 cookie.txt를 업로드하세요."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL은 .txt 파일을 가리켜야 합니다."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fallback 쿠키 파일이 너무 큽니다 (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fallback 쿠키 소스를 사용할 수 없습니다 (상태 {status}). /cookie를 시도하거나 cookie.txt를 업로드하세요."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Fallback 쿠키 다운로드 오류. /cookie를 시도하거나 cookie.txt를 업로드하세요."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Fallback 쿠키 다운로드 중 예기치 않은 오류."
    BTN_CLOSE = "🔚닫기"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ 잘못된 불리언 값"
    ARGS_CLOSED_MSG = "닫기"
    ARGS_ALL_RESET_MSG = "✅ 모든 인수가 재설정되었습니다"
    ARGS_RESET_ERROR_MSG = "❌ 인수 재설정 중 오류 발생"
    ARGS_INVALID_PARAM_MSG = "❌ 잘못된 매개변수"
    ARGS_BOOL_SET_MSG = "{value}로 설정"
    ARGS_BOOL_ALREADY_SET_MSG = "이미 {value}로 설정됨"
    ARGS_INVALID_SELECT_MSG = "❌ 잘못된 선택 값"
    ARGS_VALUE_SET_MSG = "{value}로 설정"
    ARGS_VALUE_ALREADY_SET_MSG = "이미 {value}로 설정됨"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>현재 값:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>예제:</b>\n• <code>default</code> - 기본 XFF 전략 사용\n• <code>never</code> - XFF 헤더를 사용하지 않음\n• <code>US</code> - 미국 국가 코드\n• <code>GB</code> - 영국 국가 코드\n• <code>DE</code> - 독일 국가 코드\n• <code>FR</code> - 프랑스 국가 코드\n• <code>JP</code> - 일본 국가 코드\n• <code>192.168.1.0/24</code> - IP 블록 (CIDR)\n• <code>10.0.0.0/8</code> - 사설 IP 범위\n• <code>203.0.113.0/24</code> - 공용 IP 블록\n\n"
    ARGS_XFF_NOTE_MSG = "<b>참고:</b> 이것은 --geo-bypass 옵션을 대체합니다. CIDR 표기법의 2자 국가 코드 또는 IP 블록을 사용하세요.\n\n"
    ARGS_EXAMPLE_MSG = "<b>예제:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "새 값을 보내주세요."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>범위:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "숫자를 보내주세요."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>예제:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>참고:</b> 이러한 헤더는 기존 Referer 및 User-Agent 헤더에 추가됩니다.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 현재 yt-dlp 인수:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - True/False 스위치\n• 📋 <b>Select</b> - 옵션에서 선택\n• 🔢 <b>Numeric</b> - 숫자 입력\n• 📝🔧 <b>Text</b> - 텍스트/JSON 입력</blockquote>\n\n이 설정은 모든 다운로드에 적용됩니다."
    
    # Localized parameter names for display
    ARGS_PARAM_NAMES = {
        "force_ipv6": "IPv6 연결 강제",
        "force_ipv4": "IPv4 연결 강제", 
        "no_live_from_start": "처음부터 라이브 스트림 다운로드 안 함",
        "live_from_start": "처음부터 라이브 스트림 다운로드",
        "no_check_certificates": "HTTPS 인증서 검증 억제",
        "check_certificate": "SSL 인증서 확인",
        "no_playlist": "단일 동영상만 다운로드, 재생 목록 아님",
        "embed_metadata": "동영상 파일에 메타데이터 포함",
        "embed_thumbnail": "동영상 파일에 썸네일 포함",
        "write_thumbnail": "썸네일을 파일로 쓰기",
        "ignore_errors": "다운로드 오류 무시하고 계속",
        "legacy_server_connect": "레거시 서버 연결 허용",
        "concurrent_fragments": "다운로드할 동시 조각 수",
        "xff": "X-Forwarded-For 헤더 전략",
        "user_agent": "User-Agent 헤더",
        "impersonate": "브라우저 가장",
        "referer": "Referer 헤더",
        "geo_bypass": "지리적 제한 우회",
        "hls_use_mpegts": "HLS에 MPEG-TS 사용",
        "no_part": ".part 파일 사용 안 함",
        "no_continue": "부분 다운로드 재개 안 함",
        "audio_format": "오디오 형식",
        "video_format": "동영상 형식",
        "merge_output_format": "병합 출력 형식",
        "send_as_file": "파일로 보내기",
        "username": "사용자 이름",
        "password": "비밀번호",
        "twofactor": "2단계 인증 코드",
        "min_filesize": "최소 파일 크기 (MB)",
        "max_filesize": "최대 파일 크기 (MB)",
        "playlist_items": "재생 목록 항목",
        "date": "날짜",
        "datebefore": "이전 날짜",
        "dateafter": "이후 날짜",
        "http_headers": "HTTP 헤더",
        "sleep_interval": "대기 간격",
        "max_sleep_interval": "최대 대기 간격",
        "retries": "재시도 횟수",
        "http_chunk_size": "HTTP 청크 크기",
        "sleep_subtitles": "자막 대기"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp 인수 구성</b>\n\n<blockquote>📋 <b>그룹:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp 인수 구성</b>\n\n"
        "<blockquote>📋 <b>그룹:</b>\n"
        "• ✅/❌ <b>Boolean</b> - True/False 스위치\n"
        "• 📋 <b>Select</b> - 옵션에서 선택\n"
        "• 🔢 <b>Numeric</b> - 숫자 입력\n"
        "• 📝🔧 <b>Text</b> - 텍스트/JSON 입력</blockquote>\n\n"
        "이 설정은 모든 다운로드에 적용됩니다."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ 기다려주세요..."
    ERROR_OCCURRED_SHORT_MSG = "❌ 오류 발생"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ 비활성으로 인해 입력 모드가 자동으로 닫혔습니다 (5분)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ 입력에 잠재적으로 위험한 내용이 포함되어 있습니다: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ 입력이 너무 깁니다 (최대 1000자)"
    ARGS_INVALID_URL_MSG = "❌ 잘못된 URL 형식. http:// 또는 https://로 시작해야 합니다"
    ARGS_INVALID_JSON_MSG = "❌ 잘못된 JSON 형식"
    ARGS_NUMBER_RANGE_MSG = "❌ 숫자는 {min_val}과 {max_val} 사이여야 합니다"
    ARGS_INVALID_NUMBER_MSG = "❌ 잘못된 숫자 형식"
    ARGS_DATE_FORMAT_MSG = "❌ 날짜는 YYYYMMDD 형식이어야 합니다 (예: 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ 연도는 1900과 2100 사이여야 합니다"
    ARGS_MONTH_RANGE_MSG = "❌ 월은 01과 12 사이여야 합니다"
    ARGS_DAY_RANGE_MSG = "❌ 일은 01과 31 사이여야 합니다"
    ARGS_INVALID_DATE_MSG = "❌ 잘못된 날짜 형식"
    ARGS_INVALID_XFF_MSG = "❌ XFF는 'default', 'never', 국가 코드 (예: US) 또는 IP 블록 (예: 192.168.1.0/24)이어야 합니다"
    ARGS_NO_CUSTOM_MSG = "사용자 지정 인수가 설정되지 않았습니다. 모든 매개변수는 기본값을 사용합니다."
    ARGS_RESET_SUCCESS_MSG = "✅ 모든 인수가 기본값으로 재설정되었습니다."
    ARGS_TEXT_TOO_LONG_MSG = "❌ 텍스트가 너무 깁니다. 최대 500자."
    ARGS_ERROR_PROCESSING_MSG = "❌ 입력 처리 중 오류가 발생했습니다. 다시 시도해주세요."
    ARGS_BOOL_INPUT_MSG = "❌ 파일로 보내기 옵션에 대해 'True' 또는 'False'를 입력해주세요."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ 유효한 숫자를 입력해주세요."
    ARGS_BOOL_VALUE_REQUEST_MSG = "이 옵션을 활성화/비활성화하려면 <code>True</code> 또는 <code>False</code>를 보내주세요."
    ARGS_JSON_VALUE_REQUEST_MSG = "유효한 JSON을 보내주세요."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "아직 태그가 없습니다."
    TAGS_MESSAGE_CLOSED_MSG = "태그 메시지가 닫혔습니다."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ 자막이 비활성화되었고 Always Ask 모드가 꺼졌습니다."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Always Ask가 활성화되었습니다."
    SUBS_LANGUAGE_SET_MSG = "✅ 자막 언어가 다음으로 설정되었습니다: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️경고: 높은 CPU 영향으로 인해 이 기능은 매우 느립니다 (거의 실시간) 그리고 다음으로 제한됩니다:\n"
        "- 최대 품질 720p\n"
        "- 최대 지속 시간 1.5시간\n"
        "- 최대 비디오 크기 500mb</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>빠른 명령:</b>\n"
        "• <code>/subs off</code> - 자막 비활성화\n"
        "• <code>/subs on</code> - Always Ask 모드 활성화\n"
        "• <code>/subs ru</code> - 언어 설정\n"
        "• <code>/subs ru auto</code> - AUTO/TRANS로 언어 설정"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 자막이 비활성화되어 있습니다"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} 선택된 언어: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 자막 다운로드 중..."
    SUBS_DISABLED_ERROR_MSG = "❌ 자막이 비활성화되어 있습니다. /subs를 사용하여 구성하세요."
    SUBS_YOUTUBE_ONLY_MSG = "❌ 자막 다운로드는 YouTube에서만 지원됩니다."
    SUBS_CAPTION_MSG = (
        "<b>💬 Subtitles</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Language:</b> {lang}\n"
        "<b>Type:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 자막 SRT 파일이 사용자에게 전송되었습니다."
    SUBS_ERROR_PROCESSING_MSG = "❌ 자막 파일 처리 중 오류가 발생했습니다."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ 자막 다운로드에 실패했습니다."
    SUBS_ERROR_MSG = "❌ 자막 다운로드 중 오류가 발생했습니다: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ 분할 부분 크기가 다음으로 설정되었습니다: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **잘못된 크기!**\n\n"
        "**유효한 범위:** 100MB ~ 2GB\n\n"
        "**유효한 형식:**\n"
        "• `100mb` ~ `2000mb` (메가바이트)\n"
        "• `0.1gb` ~ `2gb` (기가바이트)\n\n"
        "**예제:**\n"
        "• `/split 100mb` - 100 메가바이트\n"
        "• `/split 500mb` - 500 메가바이트\n"
        "• `/split 1.5gb` - 1.5 기가바이트\n"
        "• `/split 2gb` - 2 기가바이트\n"
        "• `/split 2000mb` - 2000 메가바이트 (2GB)\n\n"
        "**프리셋:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **비디오 분할을 위한 최대 부분 크기 선택:**\n\n"
        "**범위:** 100MB ~ 2GB\n\n"
        "**빠른 명령:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**예제:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "메뉴가 닫혔습니다."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>봇 설정</b>\n\n카테고리를 선택하세요:"
    SETTINGS_MENU_CLOSED_MSG = "메뉴가 닫혔습니다."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 정리 옵션</b>\n\n정리할 항목을 선택하세요:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 쿠키</b>\n\n작업을 선택하세요:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 미디어</b>\n\n작업을 선택하세요:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 정보</b>\n\n작업을 선택하세요:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ 추가 명령</b>\n\n작업을 선택하세요:"
    SETTINGS_COMMAND_EXECUTED_MSG = "명령이 실행되었습니다."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ 플러드 제한. 나중에 다시 시도하세요."
    SETTINGS_HINT_SENT_MSG = "힌트가 전송되었습니다."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "검색 도우미가 열렸습니다."
    SETTINGS_UNKNOWN_COMMAND_MSG = "알 수 없는 명령입니다."
    SETTINGS_HINT_CLOSED_MSG = "힌트가 닫혔습니다."
    SETTINGS_HELP_SENT_MSG = "사용자에게 도움말 txt 파일 전송"
    SETTINGS_MENU_OPENED_MSG = "/settings 메뉴가 열렸습니다"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 검색 도우미가 닫혔습니다"
    SEARCH_CLOSED_MSG = "닫기"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ 프록시 {status}."
    PROXY_ERROR_SAVING_MSG = "❌ 프록시 설정 저장 중 오류가 발생했습니다."
    PROXY_MENU_TEXT_MSG = "모든 yt-dlp 작업에 대해 프록시 서버 사용을 활성화하거나 비활성화하시겠습니까?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "모든 yt-dlp 작업에 프록시 서버({config_count} + {file_count} 사용 가능) 사용을 활성화 또는 비활성화하시겠습니까?\n\nALL(AUTO)을 활성화하면 무작위 방법을 사용하여 프록시가 선택됩니다."
    PROXY_MENU_CLOSED_MSG = "메뉴가 닫혔습니다."
    PROXY_ENABLED_CONFIRM_MSG = "✅ 프록시가 활성화되었습니다. 모든 yt-dlp 작업이 프록시를 사용합니다."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ 프록시가 활성화되었습니다. 모든 yt-dlp 작업이 {method} 선택 방법으로 {count}개의 프록시 서버를 사용합니다."

    PROXY_ENABLED_ALL_AUTO_MSG = "✅ 프록시가 활성화되었습니다(ALL AUTO 모드).\n\n📊 봇은 다음 순서로 프록시를 시도합니다.\n1️⃣ Config.py의 {config_count} 프록시\n2️⃣ TXT/proxy.txt 파일의 {file_count} 프록시\n\n🔄 모든 프록시는 성공적으로 연결될 때까지 순차적으로 시도됩니다."
    PROXY_DISABLED_MSG = "❌ 프록시가 비활성화되었습니다."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ 프록시 설정 저장 중 오류가 발생했습니다."
    PROXY_ENABLED_CALLBACK_MSG = "프록시가 활성화되었습니다."
    PROXY_DISABLED_CALLBACK_MSG = "프록시가 비활성화되었습니다."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ 이전 다운로드가 완료될 때까지 기다려주세요"
    AUDIO_HELP_MSG = (
        "<b>🎧 오디오 다운로드 명령</b>\n\n"
        "사용법: <code>/audio URL</code>\n\n"
        "<b>예제:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "참고: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "오디오 힌트가 닫혔습니다."
    PLAYLIST_HELP_CLOSED_MSG = "재생 목록 도움말이 닫혔습니다."
    USERLOGS_CLOSED_MSG = "로그 메시지가 닫혔습니다."
    HELP_CLOSED_MSG = "도움말이 닫혔습니다."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW 블러 설정</b>\n\nNSFW 콘텐츠는 <b>{status}</b>입니다.\n\nNSFW 콘텐츠를 블러 처리할지 선택하세요:"
    NSFW_MENU_CLOSED_MSG = "메뉴가 닫혔습니다."
    NSFW_BLUR_DISABLED_MSG = "NSFW 블러가 비활성화되었습니다."
    NSFW_BLUR_ENABLED_MSG = "NSFW 블러가 활성화되었습니다."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW 블러가 비활성화되었습니다."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW 블러가 활성화되었습니다."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "다운로드된 파일에 대해 MediaInfo 전송을 활성화하거나 비활성화하시겠습니까?"
    MEDIAINFO_MENU_CLOSED_MSG = "메뉴가 닫혔습니다."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo가 활성화되었습니다. 다운로드 후 파일 정보가 전송됩니다."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo가 비활성화되었습니다."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo가 활성화되었습니다."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo가 비활성화되었습니다."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 사용 가능한 형식 목록</b>\n\n"
        "URL에 대한 사용 가능한 비디오/오디오 형식을 가져옵니다.\n\n"
        "<b>사용법:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>예제:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 형식 ID 사용 방법:</b>\n"
        "목록을 받은 후 특정 형식 ID를 사용하세요:\n"
        "• <code>/format id 401</code> - 형식 401 다운로드\n"
        "• <code>/format id401</code> - 위와 동일\n"
        "• <code>/format id140 audio</code> - 형식 140을 MP3 오디오로 다운로드\n\n"
        "이 명령은 다운로드할 수 있는 모든 사용 가능한 형식을 표시합니다."
    )
    LIST_PROCESSING_MSG = "🔄 사용 가능한 형식 가져오는 중..."
    LIST_INVALID_URL_MSG = "❌ http:// 또는 https://로 시작하는 유효한 URL을 입력해주세요"
    LIST_CAPTION_MSG = (
        "📃 사용 가능한 형식:\n<code>{url}</code>\n\n"
        "💡 <b>형식 설정 방법:</b>\n"
        "• <code>/format id 134</code> - 특정 형식 ID 다운로드\n"
        "• <code>/format 720p</code> - 품질별 다운로드\n"
        "• <code>/format best</code> - 최고 품질 다운로드\n"
        "• <code>/format ask</code> - 항상 품질 묻기\n\n"
        "{audio_note}\n"
        "📋 위 목록에서 형식 ID를 사용하세요"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>오디오 전용 형식:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - 형식 140을 MP3 오디오로 다운로드\n"
        "• <code>/format id140 audio</code> - 위와 동일\n"
        "이것들은 MP3 오디오 파일로 다운로드됩니다.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ 형식 파일 전송 중 오류가 발생했습니다: {error}"
    LIST_ERROR_GETTING_MSG = "❌ 형식 가져오기에 실패했습니다:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ 명령 처리 중 오류가 발생했습니다"
    LIST_ERROR_CALLBACK_MSG = "오류 발생"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 형식 ID 사용 방법:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "목록을 받은 후 특정 형식 ID를 사용하세요:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - 형식 401 다운로드\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - 위와 동일\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - 형식 140을 MP3 오디오로 다운로드\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - 위와 동일\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 오디오 전용 형식 감지됨: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "이 형식들은 MP3 오디오 파일로 다운로드됩니다.\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>비디오 전용 형식:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 위 목록에서 형식 ID를 사용하세요"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>사용법:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>예제:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - 최고 품질\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p 또는 이하\n"
        "• /link 720p https://youtube.com/watch?v=... - 위와 동일\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K 또는 이하\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K 또는 이하"
        "</blockquote>\n\n"
        "<b>품질:</b> 1부터 10000까지 (예: 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ 유효한 URL을 입력해주세요"
    LINK_PROCESSING_MSG = "🔗 직접 링크 가져오는 중..."
    LINK_DURATION_MSG = "⏱ <b>지속 시간:</b> {duration} 초\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>비디오 스트림:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>오디오 스트림:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **키보드 설정이 업데이트되었습니다!**\n\n새 설정: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **잘못된 인수!**\n\n"
        "유효한 옵션: `off`, `1x3`, `2x3`, `full`\n\n"
        "예제: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **키보드 설정**\n\n"
        "현재: **{current}**\n\n"
        "옵션을 선택하세요:\n\n"
        "또는 사용: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 키보드가 활성화되었습니다!"
    KEYBOARD_HIDDEN_MSG = "⌨️ 키보드가 숨겨졌습니다"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3 키보드가 활성화되었습니다!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3 키보드가 활성화되었습니다!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 이모지 키보드가 활성화되었습니다!"
    KEYBOARD_ERROR_APPLYING_MSG = "키보드 설정 {setting} 적용 중 오류가 발생했습니다: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ 형식이 다음으로 설정되었습니다: Always Ask. URL을 보낼 때마다 품질을 묻습니다."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ 형식이 다음으로 설정되었습니다: Always Ask. 이제 URL을 보낼 때마다 품질을 묻습니다."
    FORMAT_BEST_UPDATED_MSG = "✅ 형식이 최고 품질로 업데이트되었습니다 (AVC+MP4 우선순위):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ 형식이 ID {id}로 업데이트되었습니다:\n{format}\n\n💡 <b>참고:</b> 이것이 오디오 전용 형식인 경우 MP3 오디오 파일로 다운로드됩니다."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ 형식이 ID {id}로 업데이트되었습니다 (오디오 전용):\n{format}\n\n💡 이것은 MP3 오디오 파일로 다운로드됩니다."
    FORMAT_QUALITY_UPDATED_MSG = "✅ 형식이 품질 {quality}로 업데이트되었습니다:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ 형식이 다음으로 업데이트되었습니다:\n{format}"
    FORMAT_MENU_MSG = (
        "형식 옵션을 선택하거나 다음을 사용하여 사용자 지정 형식을 보내세요:\n"
        "• <code>/format &lt;format_string&gt;</code> - 사용자 지정 형식\n"
        "• <code>/format 720</code> - 720p 품질\n"
        "• <code>/format 4k</code> - 4K 품질\n"
        "• <code>/format 8k</code> - 8K 품질\n"
        "• <code>/format id 401</code> - 특정 형식 ID\n"
        "• <code>/format ask</code> - 항상 메뉴 표시\n"
        "• <code>/format best</code> - bv+ba/최고 품질"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "사용자 지정 형식을 사용하려면 다음 형식으로 명령을 보내세요:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "<code>bestvideo+bestaudio/best</code>를 원하는 형식 문자열로 교체하세요."
    )
    FORMAT_RESOLUTION_MENU_MSG = "원하는 해상도와 코덱을 선택하세요:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ 형식이 다음으로 설정되었습니다: Always Ask. 이제 URL을 보낼 때마다 품질을 묻습니다."
    FORMAT_UPDATED_MSG = "✅ 형식이 다음으로 업데이트되었습니다:\n{format}"
    FORMAT_SAVED_MSG = "✅ 형식이 저장되었습니다."
    FORMAT_CHOICE_UPDATED_MSG = "✅ 형식 선택이 업데이트되었습니다."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "사용자 지정 형식 메뉴가 닫혔습니다"
    FORMAT_CODEC_SET_MSG = "✅ 코덱이 {codec}으로 설정되었습니다"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ 브라우저 선택이 업데이트되었습니다."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ 접근이 거부되었습니다. 관리자만 가능합니다."
    ACCESS_DENIED_ADMIN = "❌ 접근이 거부되었습니다. 관리자만 가능합니다."
    WELCOME_MASTER = "환영합니다 관리자님 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ 죄송합니다... 다운로드 중 오류가 발생했습니다."
    SIZE_LIMIT_EXCEEDED = "❌ 파일 크기가 {max_size_gb} GB 제한을 초과했습니다. 허용된 크기 내에서 더 작은 파일을 선택해주세요."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ 스크립트를 찾을 수 없습니다: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ {script_path}를 사용하여 최신 Firebase 덤프 다운로드 중..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase 캐시가 성공적으로 다시 로드되었습니다!"
    ADMIN_CACHE_FAILED_MSG = "❌ Firebase 캐시를 다시 로드하는 데 실패했습니다. {cache_file}이(가) 존재하는지 확인하세요."
    ADMIN_ERROR_RELOADING_MSG = "❌ 캐시 다시 로드 중 오류가 발생했습니다: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ {script_path} 실행 중 오류가 발생했습니다:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ 프로모션 메시지가 모든 다른 사용자에게 전송되었습니다</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ 프로모션 메시지를 전송할 수 없습니다. 메시지에 답장을 시도하거나\n일부 오류가 발생했습니다</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ 사용자가 아직 콘텐츠를 다운로드하지 않았습니다...</b> 로그에 존재하지 않습니다"
    ADMIN_INVALID_COMMAND_MSG = "❌ 잘못된 명령입니다"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ <code>{{path}}</code>에 대한 캐시에서 데이터를 찾을 수 없습니다"
    CHANNEL_GUARD_PENDING_EMPTY_MSG = "🛡️ 대기열이 비어 있습니다 — 아직 채널을 떠난 사람이 없습니다."
    CHANNEL_GUARD_PENDING_HEADER_MSG = "🛡️ <b>차단 대기열</b>\n대기 중인 총: {total}"
    CHANNEL_GUARD_PENDING_ROW_MSG = "• <code>{user_id}</code> — {name} @{username} (떠남: {last_left})"
    CHANNEL_GUARD_PENDING_MORE_MSG = "… 및 {extra}명의 추가 사용자."
    CHANNEL_GUARD_PENDING_FOOTER_MSG = "/block_user show • all • auto • 10s 사용"
    CHANNEL_GUARD_BLOCKED_ALL_MSG = "✅ 대기열에서 사용자 차단됨: {count}"
    CHANNEL_GUARD_AUTO_ENABLED_MSG = "⚙️ 자동 차단이 활성화되었습니다: 새로 떠난 사람은 즉시 차단됩니다."
    CHANNEL_GUARD_AUTO_DISABLED_MSG = "⏸ 자동 차단이 비활성화되었습니다."
    CHANNEL_GUARD_AUTO_INTERVAL_SET_MSG = "⏱ 자동 차단 창이 매 {interval}마다 설정되었습니다."
    CHANNEL_GUARD_ACTIVITY_FILE_CAPTION_MSG = "🗂 지난 {hours}시간(2일) 동안의 채널 활동 로그."
    CHANNEL_GUARD_ACTIVITY_SUMMARY_MSG = "📝 지난 {hours}시간(2일): {joined}명 가입, {left}명 떠남."
    CHANNEL_GUARD_ACTIVITY_EMPTY_MSG = "ℹ️ 지난 {hours}시간(2일) 동안 활동이 없습니다."
    CHANNEL_GUARD_ACTIVITY_TOTALS_LINE_MSG = "총: 🟢 {joined}명 가입, 🔴 {left}명 떠남."
    CHANNEL_GUARD_NO_ACCESS_MSG = "❌ 채널 활동 로그에 대한 접근 권한이 없습니다. 봇은 관리자 로그를 읽을 수 없습니다. 이 기능을 활성화하려면 config에서 사용자 세션과 함께 CHANNEL_GUARD_SESSION_STRING을 제공하세요."
    BAN_TIME_USAGE_MSG = "❌ 사용법: {command} <10s|6m|5h|4d|3w|2M|1y>"
    BAN_TIME_INTERVAL_INVALID_MSG = "❌ 10s, 6m, 5h, 4d, 3w, 2M 또는 1y 형식을 사용하세요."
    BAN_TIME_SET_MSG = "🕒 채널 로그 스캔 간격이 {interval}로 설정되었습니다."
    BAN_TIME_REPORT_MSG = (
        "🛡️ 채널 스캔 보고서\n"
        "실행 시간: {run_ts}\n"
        "간격: {interval}\n"
        "새로 떠난 사람: {new_leavers}\n"
        "자동 차단: {auto_banned}\n"
        "대기 중: {pending}\n"
        "마지막 이벤트 ID: {last_event_id}"
    )
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ 사용법: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 관리자는 관리자를 삭제할 수 없습니다"
    ADMIN_USER_BLOCKED_MSG = "사용자가 차단되었습니다 🔒❌\n \nID: <code>{user_id}</code>\n차단 날짜: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code>는 이미 차단되었습니다 ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 죄송합니다! 관리자가 아닙니다"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ 사용법: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "사용자 차단이 해제되었습니다 🔓✅\n \nID: <code>{user_id}</code>\n차단 해제 날짜: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code>는 이미 차단 해제되었습니다 ✅😐"
    ADMIN_UNBLOCK_ALL_DONE_MSG = "✅ 차단 해제된 사용자: {count}\n⏱ 타임스탬프: {date}"
    ADMIN_IGNORE_USER_USAGE_MSG = "❌ 사용법: /ignore_user <user_id>"
    ADMIN_USER_IGNORED_MSG = "사용자 무시됨 👁️❌\n \nID: <code>{user_id}</code>\n무시된 날짜: {date}"
    ADMIN_USER_ALREADY_IGNORED_MSG = "<code>{user_id}</code>는 이미 무시되고 있습니다 ❌😐"
    ADMIN_UNIGNORE_USER_USAGE_MSG = "❌ 사용법: /unignore_user <user_id>"
    ADMIN_USER_UNIGNORED_MSG = "사용자가 더 이상 무시되지 않음 👁️✅\n \nID: <code>{user_id}</code>\n무시 해제 날짜: {date}"
    ADMIN_USER_ALREADY_UNIGNORED_MSG = "<code>{user_id}</code>는 무시되지 않습니다 ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>봇 실행 시간 -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ 캐시를 지울 URL을 입력해주세요.\n사용법: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ 유효한 URL을 입력해주세요.\n사용법: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ URL에 대한 캐시가 성공적으로 지워졌습니다:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ 이 링크에 대한 캐시를 찾을 수 없습니다."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ 캐시 지우는 중 오류가 발생했습니다: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ 접근이 거부되었습니다. 관리자만 가능합니다."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ 성인 목록 업데이트 스크립트 실행 중: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ 스크립트가 성공적으로 완료되었습니다!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ 스크립트가 성공적으로 완료되었습니다!\n\n출력:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ 스크립트가 반환 코드 {returncode}로 실패했습니다:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ 스크립트 실행 중 오류가 발생했습니다: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ 성인 및 도메인 관련 캐시 다시 로드 중..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ 성인 캐시가 성공적으로 다시 로드되었습니다!\n\n"
        "📊 현재 캐시 상태:\n"
        "• 성인 도메인: {porn_domains}\n"
        "• 성인 키워드: {porn_keywords}\n"
        "• 지원되는 사이트: {supported_sites}\n"
        "• 화이트리스트: {whitelist}\n"
        "• 그레이리스트: {greylist}\n"
        "• 블랙리스트: {black_list}\n"
        "• 화이트 키워드: {white_keywords}\n"
        "• 프록시 도메인: {proxy_domains}\n"
        "• 프록시 2 도메인: {proxy_2_domains}\n"
        "• 정리 쿼리: {clean_query}\n"
        "• 쿠키 없음 도메인: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ 성인 캐시 다시 로드 중 오류가 발생했습니다: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ 확인할 URL을 입력해주세요.\n사용법: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ 유효한 URL을 입력해주세요.\n사용법: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 NSFW 콘텐츠에 대한 URL 확인 중...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>성인 콘텐츠 확인 결과</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>상태:</b> <b>{status_text}</b>\n\n"
        "<b>설명:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ URL 확인 중 오류가 발생했습니다: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "쿠키가 정리되었습니다."
    CLEAN_LOGS_CLEANED_MSG = "로그가 정리되었습니다."
    CLEAN_TAGS_CLEANED_MSG = "태그가 정리되었습니다."
    CLEAN_FORMAT_CLEANED_MSG = "형식이 정리되었습니다."
    CLEAN_SPLIT_CLEANED_MSG = "분할이 정리되었습니다."
    CLEAN_MEDIAINFO_CLEANED_MSG = "미디어 정보가 정리되었습니다."
    CLEAN_SUBS_CLEANED_MSG = "자막 설정이 정리되었습니다."
    CLEAN_KEYBOARD_CLEANED_MSG = "키보드 설정이 정리되었습니다."
    CLEAN_ARGS_CLEANED_MSG = "인수 설정이 정리되었습니다."
    CLEAN_NSFW_CLEANED_MSG = "NSFW 설정이 정리되었습니다."
    CLEAN_PROXY_CLEANED_MSG = "프록시 설정이 정리되었습니다."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "플러드 대기 설정이 정리되었습니다."
    CLEAN_ALL_CLEANED_MSG = "모든 파일이 정리되었습니다."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 쿠키</b>\n\n작업을 선택하세요:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ 쿠키 파일이 저장되었습니다"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ YouTube가 아닌 쿠키에 대한 검증을 건너뛰었습니다"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ 쿠키 파일이 존재하지만 형식이 잘못되었습니다"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ 쿠키 파일을 찾을 수 없습니다."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 YouTube 쿠키 테스트 시작 중...\n\n쿠키를 확인하고 검증하는 동안 기다려주세요."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ 기존 YouTube 쿠키가 제대로 작동하고 있습니다!\n\n새 것을 다운로드할 필요가 없습니다."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ 기존 YouTube 쿠키가 만료되었거나 유효하지 않습니다.\n\n🔄 새 쿠키 다운로드 중..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} 쿠키 소스가 구성되지 않았습니다!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} 쿠키 소스는 .txt 파일이어야 합니다!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ 범위 제한 초과: {range_count}개 파일 요청됨 (최대 {max_img_files}).\n\n사용 가능한 최대 파일을 다운로드하려면 다음 명령 중 하나를 사용하세요:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚 닫기"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ 미디어 제한 초과: {count}개 파일 요청됨 (최대 {max_count}).\n\n사용 가능한 최대 파일을 다운로드하려면 다음 명령 중 하나를 사용하세요:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 링크에서 <b>{count}</b>개의 미디어 항목 발견"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "다운로드 범위 선택:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "브라우저 가장"
    ARGS_REFERER_DESC_MSG = "Referer 헤더"
    ARGS_USER_AGENT_DESC_MSG = "User-Agent 헤더"
    ARGS_GEO_BYPASS_DESC_MSG = "지리적 제한 우회"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "SSL 인증서 확인"
    ARGS_LIVE_FROM_START_DESC_MSG = "처음부터 라이브 스트림 다운로드"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "처음부터 라이브 스트림 다운로드 안 함"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "HLS 비디오에 MPEG-TS 컨테이너 사용"
    ARGS_NO_PLAYLIST_DESC_MSG = "단일 비디오만 다운로드, 재생 목록 아님"
    ARGS_NO_PART_DESC_MSG = ".part 파일 사용 안 함"
    ARGS_NO_CONTINUE_DESC_MSG = "부분 다운로드 재개 안 함"
    ARGS_AUDIO_FORMAT_DESC_MSG = "추출할 오디오 형식"
    ARGS_EMBED_METADATA_DESC_MSG = "비디오 파일에 메타데이터 포함"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "비디오 파일에 썸네일 포함"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "썸네일을 파일로 쓰기"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "다운로드할 동시 조각 수"
    ARGS_FORCE_IPV4_DESC_MSG = "IPv4 연결 강제"
    ARGS_FORCE_IPV6_DESC_MSG = "IPv6 연결 강제"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For 헤더 전략"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP 청크 크기 (바이트)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "자막 다운로드 전 대기 (초)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "레거시 서버 연결 허용"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "HTTPS 인증서 검증 억제"
    ARGS_USERNAME_DESC_MSG = "계정 사용자 이름"
    ARGS_PASSWORD_DESC_MSG = "계정 비밀번호"
    ARGS_TWOFACTOR_DESC_MSG = "2단계 인증 코드"
    ARGS_IGNORE_ERRORS_DESC_MSG = "다운로드 오류 무시하고 계속"
    ARGS_MIN_FILESIZE_DESC_MSG = "최소 파일 크기 (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "최대 파일 크기 (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "다운로드할 재생 목록 항목 (예: 1,3,5 또는 1-5)"
    ARGS_DATE_DESC_MSG = "이 날짜에 업로드된 비디오 다운로드 (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "이 날짜 이전에 업로드된 비디오 다운로드 (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "이 날짜 이후에 업로드된 비디오 다운로드 (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "사용자 지정 HTTP 헤더 (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "요청 간 대기 간격 (초)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "최대 대기 간격 (초)"
    ARGS_RETRIES_DESC_MSG = "재시도 횟수"
    ARGS_VIDEO_FORMAT_DESC_MSG = "비디오 컨테이너 형식"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "병합용 출력 컨테이너 형식"
    ARGS_SEND_AS_FILE_DESC_MSG = "미디어 대신 문서로 모든 미디어 전송"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "가장"
    ARGS_REFERER_SHORT_MSG = "리퍼러"
    ARGS_GEO_BYPASS_SHORT_MSG = "지리 우회"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "인증서 확인"
    ARGS_LIVE_FROM_START_SHORT_MSG = "라이브 시작"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "라이브 시작 안 함"
    ARGS_USER_AGENT_SHORT_MSG = "User-Agent"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "재생 목록 없음"
    ARGS_NO_PART_SHORT_MSG = "Part 없음"
    ARGS_NO_CONTINUE_SHORT_MSG = "재개 안 함"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "오디오 형식"
    ARGS_EMBED_METADATA_SHORT_MSG = "메타 포함"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "썸네일 포함"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "썸네일 쓰기"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "동시"
    ARGS_FORCE_IPV4_SHORT_MSG = "IPv4 강제"
    ARGS_FORCE_IPV6_SHORT_MSG = "IPv6 강제"
    ARGS_XFF_SHORT_MSG = "XFF 헤더"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "청크 크기"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "자막 대기"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "레거시 연결"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "인증서 확인 안 함"
    ARGS_USERNAME_SHORT_MSG = "사용자 이름"
    ARGS_PASSWORD_SHORT_MSG = "비밀번호"
    ARGS_TWOFACTOR_SHORT_MSG = "2단계 인증"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "오류 무시"
    ARGS_MIN_FILESIZE_SHORT_MSG = "최소 크기"
    ARGS_MAX_FILESIZE_SHORT_MSG = "최대 크기"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "재생 목록 항목"
    ARGS_DATE_SHORT_MSG = "날짜"
    ARGS_DATEBEFORE_SHORT_MSG = "이전 날짜"
    ARGS_DATEAFTER_SHORT_MSG = "이후 날짜"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP 헤더"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "대기 간격"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "최대 대기"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "비디오 형식"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "병합 형식"
    ARGS_SEND_AS_FILE_SHORT_MSG = "파일로 보내기"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ 파일이 너무 큽니다. 최대 크기는 100 KB입니다."
    COOKIES_INVALID_FORMAT_MSG = "❌ 다음 형식의 파일만 허용됩니다: .txt"
    COOKIES_INVALID_COOKIE_MSG = "❌ 파일이 cookie.txt처럼 보이지 않습니다 ('# Netscape HTTP Cookie File' 줄이 없습니다)."
    COOKIES_ERROR_READING_MSG = "❌ 파일 읽기 중 오류가 발생했습니다: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ 쿠키 파일이 존재하며 올바른 형식입니다"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} 쿠키 파일이 너무 큽니다! 최대 100KB, 받은 크기 {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} 쿠키 파일이 다운로드되어 폴더에 cookie.txt로 저장되었습니다.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} 쿠키 소스를 사용할 수 없습니다 (상태 {status}). 나중에 다시 시도해주세요."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ {service} 쿠키 파일 다운로드 중 오류가 발생했습니다. 나중에 다시 시도해주세요."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ 사용자가 새 쿠키 파일을 제공했습니다.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ 쿠키가 성공적으로 업데이트되었습니다:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ 유효한 쿠키가 아닙니다.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube 쿠키 소스가 구성되지 않았습니다!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 YouTube 쿠키 다운로드 및 확인 중...\n\n시도 {attempt}/{total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ 접근이 거부되었습니다. 관리자만 가능합니다."
    ADMIN_USER_LOGS_TOTAL_MSG = "총: <b>{total}</b>\n<b>{user_id}</b> - 로그 (마지막 10개):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 키보드가 활성화되었습니다!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ 자막 언어가 다음으로 설정되었습니다: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ 자막 언어가 AUTO/TRANS 활성화와 함께 다음으로 설정되었습니다: {flag} {name}"
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "자막 언어 메뉴가 닫혔습니다."
    SUBS_DOWNLOADING_MSG = "💬 자막 다운로드 중..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Firebase 캐시를 메모리로 다시 로드 중..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ COOKIE_URL이 구성되지 않았습니다. /cookie를 사용하거나 cookie.txt를 업로드하세요."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 원격 URL에서 쿠키 다운로드 중..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL은 .txt 파일을 가리켜야 합니다."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fallback 쿠키 파일이 너무 큽니다 (>100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ Fallback을 통해 YouTube 쿠키 파일이 다운로드되어 cookie.txt로 저장되었습니다"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fallback 쿠키 소스를 사용할 수 없습니다 (상태 {status}). /cookie를 사용하거나 cookie.txt를 업로드하세요."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Fallback 쿠키 다운로드 중 오류가 발생했습니다. /cookie를 사용하거나 cookie.txt를 업로드하세요."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Fallback 쿠키 다운로드 중 예기치 않은 오류가 발생했습니다."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} 브라우저가 설치되지 않았습니다."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ 브라우저를 사용하여 쿠키가 저장되었습니다: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ 쿠키 저장 실패: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube 쿠키가 제대로 작동하고 있습니다"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube 쿠키가 만료되었거나 유효하지 않습니다\n\n새 쿠키를 얻으려면 /cookie를 사용하세요"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - 사용자 정의 형식\n• <code>/format 720</code> - 720p 화질\n• <code>/format 4k</code> - 4K 화질"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "힌트가 전송되었습니다."
    FORMAT_MKV_TOGGLE_MSG = "MKV가 이제 {status}입니다"
    COOKIES_NO_REMOTE_URL_MSG = "❌ 원격 URL이 구성되지 않았습니다"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ 잘못된 파일 형식입니다"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ 파일이 너무 큽니다"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ 쿠키가 성공적으로 다운로드되었습니다"
    COOKIES_SERVER_ERROR_MSG = "❌ 서버 오류 {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ 다운로드 실패"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ 예기치 않은 오류"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ 브라우저가 설치되지 않았습니다."
    COOKIES_MENU_CLOSED_MSG = "메뉴가 닫혔습니다."
    COOKIES_HINT_CLOSED_MSG = "쿠키 힌트가 닫혔습니다."
    IMG_HELP_CLOSED_MSG = "도움말이 닫혔습니다."
    SUBS_LANGUAGE_UPDATED_MSG = "자막 언어 설정이 업데이트되었습니다."
    SUBS_MENU_CLOSED_MSG = "자막 언어 메뉴가 닫혔습니다."
    KEYBOARD_SET_TO_MSG = "키보드가 {setting}로 설정되었습니다"
    KEYBOARD_ERROR_PROCESSING_MSG = "설정 처리 중 오류가 발생했습니다"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo가 활성화되었습니다."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo가 비활성화되었습니다."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW 블러가 비활성화되었습니다."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW 블러가 활성화되었습니다."
    SETTINGS_MENU_CLOSED_MSG = "메뉴가 닫혔습니다."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "플러드 대기가 활성화되었습니다. 나중에 다시 시도하세요."
    OTHER_HELP_CLOSED_MSG = "도움말이 닫혔습니다."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "로그 메시지가 닫혔습니다."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "메뉴가 닫혔습니다."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "잘못된 크기입니다."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ MediaInfo 전송 중 오류가 발생했습니다: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ 오류가 발생했습니다: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - 모든 로그"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - 모든 {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 원격 URL에서 다운로드"
    BROWSER_OPEN_BUTTON_MSG = "🌐 브라우저 열기"
    SELECT_BROWSER_MSG = "쿠키를 다운로드할 브라우저를 선택하세요:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "이 시스템에서 브라우저를 찾을 수 없습니다. 원격 URL에서 쿠키를 다운로드하거나 브라우저 상태를 모니터링할 수 있습니다:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>브라우저 열기</b> - 미니 앱에서 브라우저 상태 모니터링"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ /check_cookie 실행 실패"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ 플러드 제한. 나중에 다시 시도하세요."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ 브라우저 쿠키 메뉴 열기 실패"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "쿠키로 저장 힌트가 닫혔습니다."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>사용법:</b>\n<code>/link [quality] URL</code>\n\n<b>예제:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - 최고 품질\n• /link 720 https://youtube.com/watch?v=... - 720p 또는 이하\n• /link 720p https://youtube.com/watch?v=... - 위와 동일\n• /link 4k https://youtube.com/watch?v=... - 4K 또는 이하\n• /link 8k https://youtube.com/watch?v=... - 8K 또는 이하</blockquote>\n\n<b>품질:</b> 1부터 10000까지 (예: 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K 품질"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>직접 링크 획득</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>형식:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>오디오 스트림:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ 스트림 링크 가져오기 실패"
    LINK_ERROR_GETTING_MSG = "❌ <b>링크 가져오기 오류:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ 잘못된 YouTube 쿠키 인덱스: {selected_index}. 사용 가능한 범위는 1-{total_urls}입니다"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 YouTube 쿠키 다운로드 및 확인 중...\n\n시도 {attempt}/{total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 YouTube 쿠키 다운로드 및 확인 중...\n\n시도 {attempt}/{total}\n🔍 쿠키 테스트 중..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube 쿠키가 성공적으로 다운로드되고 검증되었습니다!\n\n사용된 소스 {source}/{total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ 모든 YouTube 쿠키가 만료되었거나 사용할 수 없습니다!\n\n교체하려면 봇 관리자에게 문의하세요."
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube 쿠키 재시도 제한을 초과했습니다!\n\n🔢 최대: 시간당 {limit}회 시도\n⏰ 나중에 다시 시도해주세요"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ 태그 #{wrong}에 금지된 문자가 포함되어 있습니다. 문자, 숫자 및 _만 허용됩니다.\n다음을 사용하세요: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **잘못된 인수!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ 자막 언어 설정: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "예제: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} 선택된 언어: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Always Ask 모드 {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 자막이 비활성화되어 있습니다"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 자막 설정</b>\n\n{status_text}\n\n자막 언어 선택:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - 자막 비활성화\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 자막 설정</b>\n\n{status_text}\n\n자막 언어 선택:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>제목:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>지속 시간:</b> {duration} 초\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>비디오 스트림:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 최대 품질 720p\n- 최대 지속 시간 1.5시간\n- 최대 비디오 크기 500mb</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️경고: 높은 CPU 영향으로 인해 이 기능은 매우 느립니다 (거의 실시간) 그리고 다음으로 제한됩니다:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>빠른 명령:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - 자막 비활성화\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - Always Ask 모드 활성화\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - 언어 설정\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - AUTO/TRANS 활성화와 함께 언어 설정\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - Always Ask 모드 활성화\n"
    SUBS_AUTO_SUBS_TEXT = " (자동 자막)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ 자동 자막 모드 {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "명령을 통해 SUBS 비활성화됨: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Always Ask가 명령을 통해 활성화되었습니다: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "명령을 통해 SUBS 언어 설정됨: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "명령을 통해 SUBS 언어 + 자동 모드 설정됨: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "사용자가 /subs 메뉴를 열었습니다."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "사용자가 자막 언어를 다음으로 설정했습니다: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "사용자가 AUTO/TRANS 모드를 다음으로 전환했습니다: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "사용자가 Always Ask 모드를 다음으로 전환했습니다: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "사용자가 브라우저에서 쿠키를 요청했습니다."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "설치된 브라우저만 포함하여 브라우저 선택 키보드가 전송되었습니다."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "브라우저 선택이 닫혔습니다."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "Fallback COOKIE_URL이 성공적으로 사용됨 (소스 숨김)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "Fallback COOKIE_URL 실패: status={status} (숨김)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Fallback COOKIE_URL 예기치 않은 오류: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "브라우저 {browser}가 설치되지 않았습니다."
    COOKIES_SAVED_BROWSER_LOG_MSG = "브라우저를 사용하여 쿠키 저장됨: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "사용자 {user_id}에 대한 쿠키 파일이 저장되었습니다."
    COOKIES_FILE_WORKING_LOG_MSG = "쿠키 파일이 존재하며 올바른 형식이며 YouTube 쿠키가 작동 중입니다."
    COOKIES_FILE_EXPIRED_LOG_MSG = "쿠키 파일이 존재하고 올바른 형식이지만 YouTube 쿠키가 만료되었습니다."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "쿠키 파일이 존재하며 올바른 형식입니다."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "쿠키 파일이 존재하지만 형식이 잘못되었습니다."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "쿠키 파일을 찾을 수 없습니다."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "사용자 {user_id}에 대한 {service} 쿠키 URL이 비어 있습니다."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} 쿠키 URL이 .txt가 아닙니다 (숨김)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} 쿠키 파일이 너무 큼: {size} 바이트 (소스 숨김)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "사용자 {user_id}에 대한 {service} 쿠키 파일이 다운로드되었습니다 (소스 숨김)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "스크립트를 찾을 수 없습니다: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "초기 상태 메시지 전송 실패"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "{script_path} 실행 중 오류: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "자동 작업으로 Firebase 캐시가 다시 로드되었습니다."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "관리자에 의해 Firebase 캐시가 다시 로드되었습니다."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Firebase 캐시 다시 로드 중 오류: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "브로드캐스트가 시작되었습니다. 텍스트:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "모든 사용자에게 브로드캐스트 메시지가 전송되었습니다."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "브로드캐스트 메시지 전송 실패: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "관리자 {user_id}가 URL에 대한 캐시를 지웠습니다: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "관리자 {user_id}가 성인 목록 업데이트 스크립트를 시작했습니다: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "관리자 {user_id}에 의해 성인 목록 업데이트 스크립트가 성공적으로 완료되었습니다"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "관리자 {user_id}에 의해 성인 목록 업데이트 스크립트가 실패했습니다: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "관리자 {user_id}가 존재하지 않는 스크립트를 실행하려고 했습니다: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "관리자 {user_id}에 의해 성인 업데이트 스크립트 실행 중 오류: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "관리자 {user_id}가 성인 캐시 다시 로드를 시작했습니다"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "관리자 {user_id}에 의해 성인 캐시 다시 로드 중 오류: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "관리자 {user_id}가 NSFW에 대한 URL을 확인했습니다: {url} - 결과: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "사용자가 형식 변경을 요청했습니다."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "형식이 ALWAYS_ASK로 설정되었습니다."
    FORMAT_UPDATED_BEST_LOG_MSG = "형식이 최고로 업데이트되었습니다: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "형식이 ID {format_id}로 업데이트되었습니다: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "형식이 ID {format_id}로 업데이트되었습니다 (오디오 전용): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "형식이 품질 {quality}로 업데이트되었습니다: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "형식이 다음으로 업데이트되었습니다: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "형식 메뉴가 전송되었습니다."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "형식 선택이 닫혔습니다."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "사용자 지정 형식 힌트가 전송되었습니다."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "형식 해상도 메뉴가 전송되었습니다."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "메인 형식 메뉴로 돌아갔습니다."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "형식이 다음으로 업데이트되었습니다: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "형식이 ALWAYS_ASK로 설정되었습니다."
    FORMAT_CODEC_SET_LOG_MSG = "코덱 기본 설정이 {codec}으로 설정되었습니다"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "사용자 지정 형식 메뉴가 닫혔습니다"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "사용자 {user_id}에 대한 {url}에서 직접 링크 추출됨"
    LINK_EXTRACTION_FAILED_LOG_MSG = "사용자 {user_id}에 대한 {url}에서 직접 링크 추출 실패: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "사용자 {user_id}에 대한 링크 명령 오류: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "사용자 {user_id}가 키보드를 {setting}로 설정했습니다"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "사용자 {user_id}가 키보드를 {setting}로 설정했습니다"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "명령을 통해 MediaInfo 설정됨: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "사용자가 /mediainfo 메뉴를 열었습니다."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: 닫혔습니다."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo가 활성화되었습니다."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo가 비활성화되었습니다."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "인수를 통해 분할 크기가 {size} 바이트로 설정되었습니다."
    SPLIT_MENU_OPENED_LOG_MSG = "사용자가 /split 메뉴를 열었습니다."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "분할 선택이 닫혔습니다."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "분할 크기가 {size} 바이트로 설정되었습니다."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "명령을 통해 프록시 설정됨: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "사용자가 /proxy 메뉴를 열었습니다."
    PROXY_MENU_CLOSED_LOG_MSG = "프록시: 닫혔습니다."
    PROXY_ENABLED_LOG_MSG = "프록시가 활성화되었습니다."
    PROXY_DISABLED_LOG_MSG = "프록시가 비활성화되었습니다."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "도움말 메시지가 닫혔습니다."
    AUDIO_HELP_SHOWN_LOG_MSG = "/audio 도움말 표시됨"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "사용자가 재생 목록 도움말을 요청했습니다."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "재생 목록 도움말이 닫혔습니다."
    AUDIO_HINT_CLOSED_LOG_MSG = "오디오 힌트가 닫혔습니다."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "사용자 {user_id}에 대한 {url}에서 LINK 버튼을 통해 직접 링크 메뉴 생성됨"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "사용자 {user_id}에 대한 {url}에서 LINK 버튼을 통해 직접 링크 추출 실패: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "사용자 {user_id}에 대한 LIST 명령 실행됨, url: {url}"
    QUICK_EMBED_LOG_MSG = "빠른 임베드: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "{url}에 대한 Always Ask 메뉴 전송됨"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "오류 후 사용자 {user_id}에 대한 캐시된 품질 메뉴 생성됨: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "{url}에 대한 Always Ask 메뉴 오류: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "형식이 /args 설정을 통해 고정되었습니다"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "오디오"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "비디오"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "비디오"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "다음 ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ 이전"
    SUBTITLES_NEXT_BUTTON_MSG = "다음 ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ 모든 텍스트 필드가 비어 있습니다"
    SENDER_VIDEO_DURATION_MSG = "비디오 지속 시간:"
    SENDER_UPLOADING_FILE_MSG = "📤 파일 업로드 중..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 비디오 업로드 중..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 비디오 지속 시간:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1개 파일 업로드됨."
    DOWN_UP_VIDEO_INFO_MSG = "📋 비디오 정보"
    DOWN_UP_NUMBER_MSG = "번호"
    DOWN_UP_TITLE_MSG = "제목"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ 다운로드된 비디오."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 업로드 처리 중..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 분할된 부분 {part} 파일 업로드됨"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ 업로드 완료"
    DOWN_UP_FILES_UPLOADED_MSG = "파일 업로드됨"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (안드로이드)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 닫기"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼코덱"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 더빙"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 자막"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 브라우저"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 직접 링크 가져오는 중..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 사용 가능한 형식 가져오는 중..."
    ALWAYS_ASK_GETTING_CAPTION_MSG = "📝 비디오 설명 가져오는 중..."
    AA_ERROR_GETTING_CAPTION_MSG = "❌ 설명 가져오기 오류: {error_msg}"
    AA_NO_DESCRIPTION_AVAILABLE_MSG = "⚠️ 비디오 설명을 사용할 수 없습니다"
    AA_ERROR_SENDING_CAPTION_MSG = "❌ 설명 전송 오류: {error_msg}"
    CAPTION_SENT_LOG_MSG = "📝 사용자 {user_id}에게 {url} ({title})의 비디오 설명 전송됨"
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 gallery-dl 시작 중…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>재생 시간:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>형식:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>브라우저:</b> 웹 브라우저에서 열기"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "사용 가능한 형식:"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 형식 ID 사용 방법:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "목록을 얻은 후 특정 형식 ID 사용:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - 형식 401 다운로드"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - 위와 동일"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - 형식 140을 MP3 오디오로 다운로드"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 오디오 전용 형식 감지됨"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "이 형식들은 MP3 오디오 파일로 다운로드됩니다."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>형식 설정 방법:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - 특정 형식 ID 다운로드"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - 화질별 다운로드"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - 최고 화질 다운로드"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - 항상 화질 선택"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>오디오 전용 형식:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - 형식 140을 MP3 오디오로 다운로드"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "이것들은 MP3 오디오 파일로 다운로드됩니다."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 위 목록에서 형식 ID 사용"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ 오류: 원본 메시지를 찾을 수 없습니다."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "형식 페이지"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ 형식 메뉴 표시 오류"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ 형식 가져오기 오류"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ 사용 가능한 형식을 가져오는 중 오류가 발생했습니다."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "나중에 다시 시도하세요."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp가 이 콘텐츠를 처리할 수 없습니다"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "시스템은 대신 gallery-dl 사용을 권장합니다."
    ALWAYS_ASK_OPTIONS_MSG = "**옵션:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• 이미지 갤러리의 경우: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• 단일 이미지의 경우: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl은 Instagram, Twitter 및 기타 소셜 미디어 콘텐츠에 더 잘 작동합니다."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Gallery-dl 시도"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 /args를 통해 형식 고정됨"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 자막"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 더빙 오디오"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — 자막 사용 가능"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — 자막 언어 선택"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ 자막을 찾을 수 없으며 삽입되지 않습니다"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — 캐시에서 즉시 재게시"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — 오디오 언어 선택"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW는 유료입니다 (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — 다운로드 화질 선택"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — 이미지 다운로드 (gallery-dl)"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — 비디오 직접 링크 가져오기"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — 사용 가능한 형식 목록 표시"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — 비디오 확장자/코덱 변경"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀임베드"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — 오디오만 추출"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW는 유료입니다 (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — 캐시에서 즉시 재게시"
    # ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch video in poketube"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — 오디오 언어 선택"
    ALWAYS_ASK_BEST_BUTTON_MSG = "최고"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛기타"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝자막만"
    ALWAYS_ASK_SMART_GROUPING_MSG = "스마트 그룹화"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "작업 버튼 행 추가됨 (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "작업 버튼 행 추가됨 (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "기존 행에 하단 버튼 추가됨"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "새 하단 행 생성됨"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "재생목록에서 비디오를 찾을 수 없습니다"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "지원되지 않는 URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "비디오를 찾을 수 없습니다"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "비디오를 찾을 수 없음"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "미디어를 찾을 수 없음"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "이 트윗에는 포함되지 않음"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>비디오 정보 검색 오류:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "비디오 정보 검색 오류"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "<code>/clean</code> 명령을 시도하고 다시 시도하세요. 오류가 지속되면 YouTube에 인증이 필요합니다. <code>/cookie</code> 또는 <code>/cookies_from_browser</code>를 통해 cookies.txt를 업데이트하고 다시 시도하세요."
    ALWAYS_ASK_MENU_CLOSED_MSG = "메뉴 닫힘."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 수동 화질 선택"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "자동 감지 실패로 수동으로 화질을 선택하세요:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 사용 가능한 모든 형식"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 사용 가능한 화질 (캐시에서)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ 캐시된 화질 사용 중 - 새 형식을 사용할 수 없을 수 있습니다"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 형식 다운로드 중"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 다운로드 중"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 진행 상황 추적과 함께 다운로드 중..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 다음 형식을 사용하여 다운로드 중:"
    ALWAYS_ASK_DOWNLOADING_AUDIO_FORMAT_USING_MSG = "📥 다음 형식을 사용하여 오디오 다운로드 중:"
    ALWAYS_ASK_DOWNLOADING_BEST_QUALITY_MSG = "📥 최고 화질 다운로드 중..."
    ALWAYS_ASK_DOWNLOADING_DATABASE_MSG = "📥 데이터베이스 덤프 다운로드 중..."
    ALWAYS_ASK_DOWNLOADING_IMAGES_MSG = "📥 다운로드 중"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "형식 페이지"
    ALWAYS_ASK_FROM_CACHE_MSG = "(캐시에서)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ 오류: 원본 메시지를 찾을 수 없습니다. 삭제되었을 수 있습니다. 링크를 다시 보내주세요."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ 오류: 원본 URL을 찾을 수 없습니다. 링크를 다시 보내주세요."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>직접 링크 획득됨</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>제목:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>재생 시간:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>형식:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>비디오 스트림:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>오디오 스트림:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ 스트림 링크를 가져오지 못했습니다"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "사용자 {user_id}의 {url}에서 Always Ask 메뉴를 통해 직접 링크 추출됨"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "사용자 {user_id}의 {url}에서 Always Ask 메뉴를 통한 직접 링크 추출 실패: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "사용자 {user_id}의 {url}에서 down_and_up_with_format을 통해 직접 링크 추출됨"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "사용자 {user_id}의 {url}에서 down_and_up_with_format을 통한 직접 링크 추출 실패: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "사용자 {user_id}의 {url}에서 down_and_audio를 통해 직접 링크 추출됨"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "사용자 {user_id}의 {url}에서 down_and_audio를 통한 직접 링크 추출 실패: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ 캐시에서 오디오 전송됨."
    AUDIO_PROCESSING_MSG = "🎙️ 오디오 처리 중..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 오디오 다운로드 중:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "오디오 다운로드 중 오류가 발생했습니다."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ 오디오 정보 추출 실패"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "재생목록 인덱스 {index}에서 지원되지 않는 파일 형식 건너뛰기"
    AUDIO_FILE_NOT_FOUND_MSG = "다운로드 후 오디오 파일을 찾을 수 없습니다."

    AUDIO_FILE_SIZE_ZERO_MSG = "❌ 오디오 전송 실패: 파일 크기가 0 B입니다 (재생 목록 인덱스 {index})"
    AUDIO_FILE_STILL_DOWNLOADING_MSG = "❌ 오디오 파일이 아직 다운로드 중입니다. 잠시 기다려 주세요..."
    AUDIO_UPLOADING_MSG = "{process}\n📤 오디오 파일 업로드 중...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ 오디오 전송 실패: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "재생목록 오디오 전송됨: {sent}/{total} 파일 (quality={quality}) 사용자{user_id}에게"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ 오디오 다운로드 실패: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ 시간 초과로 인해 다운로드 취소됨 (2시간)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ 비디오 파일을 찾을 수 없습니다: {filename}"

    VIDEO_FILE_SIZE_ZERO_MSG = "❌ 비디오 전송 실패: 파일 크기가 0 B입니다 (재생 목록 인덱스 {index})"
    VIDEO_FILE_STILL_DOWNLOADING_MSG = "❌ 비디오 파일이 아직 다운로드 중입니다. 잠시 기다려 주세요..."
    VIDEO_PROCESSING_ERROR_MSG = "❌ 비디오 처리 오류: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ 설명 파일 전송 오류: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 비디오 캡션을 변경하려면 - 새 텍스트로 비디오에 답장하세요</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "자막 감지되지 않음"
    VIDEO_PROGRESS_MSG = "<b>비디오:</b> {current} / {total}"
    AUDIO_PROGRESS_MSG = "<b>오디오:</b> {current} / {total}"
    URL_PROGRESS_MSG = "<b>URL:</b> {current} / {total}"
    MULTI_URL_LIMIT_EXCEEDED_MSG = "❌ URL 한도 초과: {count}/{limit}"
    MULTI_URL_COMPLETED_MSG = "처리 완료"
    MULTI_URL_RANGE_NOT_ALLOWED_MSG = "❌ 여러 URL 모드에서는 재생목록 범위가 허용되지 않습니다. 범위 없이 단일 URL만 보내세요 (*1*5, /vid 1-10 등)."
    
    # Error messages
    ERROR_CHECK_SUPPORTED_SITES_MSG = "<a href='https://github.com/chelaxian/tg-ytdlp-bot/wiki/YT_DLP#supported-sites'>여기</a>에서 사이트가 지원되는지 확인하세요"
    ERROR_COOKIE_NEEDED_MSG = "이 비디오를 다운로드하려면 <code>cookie</code>가 필요할 수 있습니다. 먼저 <b>/clean</b> 명령으로 작업 공간을 정리하세요"
    ERROR_COOKIE_INSTRUCTIONS_MSG = "YouTube의 경우 - <b>/cookie</b> 명령으로 <code>cookie</code>를 받으세요. 기타 지원 사이트의 경우 - 자신의 쿠키를 보내세요 (<a href='https://t.me/tg_ytdlp/203'>가이드1</a>) (<a href='https://t.me/tg_ytdlp/214'>가이드2</a>) 그런 다음 비디오 링크를 다시 보내세요."
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "자막 언어 선택"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "대체 오디오 언어 없음"
    CHOOSE_AUDIO_LANGUAGE_MSG = "오디오 언어 선택"
    PAGE_NUMBER_MSG = "페이지 {page}"
    TOTAL_PROGRESS_MSG = "전체 진행 상황"
    SUBTITLE_MENU_CLOSED_MSG = "자막 메뉴 닫힘."
    SUBTITLE_LANGUAGE_SET_MSG = "자막 언어 설정: {value}"
    AUDIO_SET_MSG = "오디오 설정: {value}"
    FILTERS_UPDATED_MSG = "필터 업데이트됨"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙뒤로"
    CLOSE_BUTTON_TEXT = "🔚닫기"
    LIST_BUTTON_TEXT = "📃목록"
    IMAGE_BUTTON_TEXT = "🖼이미지"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ 화질이 자동 감지되지 않음\n'기타' 버튼을 사용하여 사용 가능한 모든 형식을 확인하세요.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **라이브 스트림 감지됨**\n\n진행 중이거나 무한한 라이브 스트림의 다운로드는 허용되지 않습니다.\n\n다음 조건이 충족되면 스트림이 종료될 때까지 기다렸다가 다시 다운로드를 시도하세요:\n• 스트림 재생 시간을 알 수 있음\n• 스트림이 종료됨\n"
    LIVE_STREAM_DOWNLOAD_PROGRESS_MSG = "📡 <b>라이브 스트림 다운로드</b>"
    LIVE_STREAM_CHUNK_NUMBER_MSG = "청크 {chunk}"
    LIVE_STREAM_CHUNK_SIZE_MSG = "최대 크기: {size}"
    LIVE_STREAM_ACCUMULATED_DURATION_MSG = "총 재생 시간: {duration}초"
    LIVE_STREAM_CHUNK_CAPTION_MSG = "📡 <b>라이브 스트림 - 청크 {chunk}</b>\n⏱ 재생 시간: {duration}초\n📦 크기: {size}"
    LIVE_STREAM_CHUNK_TITLE_MSG = "청크 {chunk}"
    LIVE_STREAM_DOWNLOAD_COMPLETE_MSG = "✅ <b>라이브 스트림 다운로드 완료</b>"
    LIVE_STREAM_CHUNKS_DOWNLOADED_MSG = "{chunks}개 청크 다운로드됨"
    LIVE_STREAM_TOTAL_DURATION_MSG = "총 재생 시간: {duration}초"
    LIVE_STREAM_DOWNLOAD_STOPPED_MSG = "⏹ <b>라이브 스트림 다운로드 중지됨</b>"
    LIVE_STREAM_USER_DIRECTORY_DELETED_MSG = "사용자 디렉토리가 삭제되었습니다 (아마도 /clean 명령으로)"
    LIVE_STREAM_FILE_DELETED_MSG = "청크 파일이 삭제되었습니다 (아마도 /clean 명령으로)"
    LIVE_STREAM_ENDED_MSG = "ℹ️ 스트림이 종료되었습니다"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "`/format` 명령을 사용하여 다른 형식을 선택하세요."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>직접 링크 획득됨</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>제목:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>재생 시간:</b> {duration}초\n"
    FORMAT_FIELD_MSG = "🎛 <b>형식:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>비디오 스트림:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>오디오 스트림:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **파일 처리 오류**\n\n비디오가 다운로드되었지만 파일 이름의 잘못된 문자로 인해 처리할 수 없습니다.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **파일 처리 오류**\n\n비디오가 다운로드되었지만 잘못된 인수 오류로 인해 처리할 수 없습니다.\n\n"
    FILE_PROCESSING_ERROR_NON_VIDEO_FILE_MSG = (
        "**이유:**\n"
        "• 다운로드한 파일이 비디오 파일이 아닙니다\n"
        "• 문서(PDF, DOC 등) 또는 아카이브일 수 있습니다\n\n"
        "**해결 방법:**\n"
        "• 링크를 확인하세요 - 비디오가 아닌 문서로 연결될 수 있습니다\n"
        "• 다른 링크 또는 소스를 시도하세요\n"
    )
    FILE_PROCESSING_ERROR_INVALID_DATA_MSG = (
        "**이유:**\n"
        "• 파일을 비디오로 처리할 수 없습니다\n"
        "• 비디오 파일이 아니거나 파일이 손상되었을 수 있습니다\n\n"
        "**해결 방법:**\n"
        "• 링크를 확인하세요 - 비디오가 아닌 문서로 연결될 수 있습니다\n"
        "• 다른 링크 또는 소스를 시도하세요\n"
    )
    FORMAT_NOT_AVAILABLE_MSG = "❌ **형식을 사용할 수 없음**\n\n요청한 비디오 형식을 이 비디오에 사용할 수 없습니다.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ 형식 ID {format_id}을(를) 이 비디오에서 찾을 수 없습니다.\n\n사용 가능한 형식 ID: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **AV1 형식을 이 비디오에 사용할 수 없습니다.**\n\n**사용 가능한 형식:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **파일 처리 오류**\n\n오디오가 다운로드되었지만 파일 이름의 잘못된 문자로 인해 처리할 수 없습니다.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **파일 처리 오류**\n\n오디오가 다운로드되었지만 잘못된 인수 오류로 인해 처리할 수 없습니다.\n\n"
    
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
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "{service} cookie 다운로드 실패: status={status} (url 숨김)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "{service} cookie 다운로드 오류: {error} (url 숨김)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "{service} cookie 다운로드 중 예상치 못한 오류 (url 숨김): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "사용자 {user_id}의 cookie 파일 업데이트됨."
    COOKIES_INVALID_CONTENT_LOG_MSG = "사용자 {user_id}가 제공한 잘못된 cookie 내용."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "사용자 {user_id}의 YouTube cookie URL이 비어 있습니다."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "사용자 {user_id}의 YouTube cookie가 소스 {source}에서 다운로드되고 검증됨."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "사용자 {user_id}의 모든 YouTube cookie 소스 실패."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "관리자 {admin_id}의 check_porn 명령 오류: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "분할 부분 크기를 {size} 바이트로 설정."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "파일 분할과 함께 비디오 업로드 완료."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "재생목록 비디오 전송됨: {sent}/{total} 파일 (quality={quality}) 사용자 {user_id}에게"
    UNKNOWN_ERROR_MSG = "❌ 알 수 없는 오류: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "재생목록 인덱스 {index}에서 지원되지 않는 파일 형식 건너뛰기"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg를 찾을 수 없습니다. FFmpeg를 설치하세요."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ MP4 변환 실패: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ 자막 삽입은 시간이 오래 걸릴 수 있습니다 (비디오 1분당 최대 1분)!\n🔥 자막 삽입 시작..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ 제한(화질/재생 시간/크기)으로 인해 자막을 삽입할 수 없습니다"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ 선택한 언어에 대한 자막을 사용할 수 없습니다"
    ERROR_SENDING_VIDEO_MSG = "❌ 비디오 전송 오류: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ 재생목록 비디오 전송됨: {sent}/{total} 파일."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ 시간 초과로 인해 다운로드 취소됨 (2시간)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ 비디오 다운로드 실패: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ 오류: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON은 객체(딕셔너리)여야 합니다."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ 잘못된 JSON 형식입니다. 유효한 JSON을 제공하세요."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ 값은 {min_val}과 {max_val} 사이여야 합니다."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} 설정됨: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ 참"
    ARGS_FALSE_BUTTON_MSG = "❌ 거짓"
    ARGS_BACK_BUTTON_MSG = "🔙 뒤로"
    ARGS_CLOSE_BUTTON_MSG = "🔚 닫기"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ 참"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ 거짓"
    ARGS_NOT_SET_MSG = "설정되지 않음"
    
    # Boolean values for import/export (all possible variations)
    ARGS_BOOLEAN_TRUE_VALUES = ["True", "true", "1", "yes", "on", "✅"]
    ARGS_BOOLEAN_FALSE_VALUES = ["False", "false", "0", "no", "off", "❌"]
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ AV1 형식을 이 비디오에 사용할 수 없습니다.\n\n사용 가능한 형식:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ 다운로드 오류: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ 재생목록 인덱스 {index}에서 비디오를 찾을 수 없습니다."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **비디오 변환 실패**\n\n잘못된 인수 오류로 인해 비디오를 MP4로 변환할 수 없습니다.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **비디오 변환 실패**\n\n비디오를 MP4로 변환할 수 없습니다.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ 스트림 링크를 가져오지 못했습니다"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>링크 가져오기 오류:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ 인덱스 {index}에서 콘텐츠를 찾을 수 없습니다"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ 오류: 원본 메시지를 찾을 수 없습니다."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ 오류: URL을 찾을 수 없습니다."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ 이 URL은 삽입할 수 없습니다."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} 코덱을 이 비디오에 사용할 수 없습니다"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} 형식을 이 비디오에 사용할 수 없습니다"
    
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
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood 제한. 나중에 시도하세요."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ 쿠키 확인"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ 모두(자동)"
    PROXY_OFF_BUTTON_MSG = "❌ OFF"
    PROXY_CLOSE_BUTTON_MSG = "🔚Close"
    

    PROXY_COUNTRY_SELECT_HEADER_MSG = "🌍 국가 선택:"
    PROXY_COUNTRY_CLEAR_BUTTON_MSG = "❌ 국가 선택 지우기"
    PROXY_COUNTRY_SELECTED_MSG = "✅ 선택한 국가: {country}(코드: {country_code})"
    PROXY_COUNTRY_PROXIES_AVAILABLE_MSG = "📊 사용 가능한 프록시: {proxy_count}(HTTP: {http_count}, SOCKS5: {socks5_count})"
    PROXY_COUNTRY_TRY_ORDER_MSG = "🔄 봇은 HTTP를 먼저 시도한 다음 SOCKS5를 시도합니다."
    PROXY_COUNTRY_AUTO_ENABLED_MSG = "💡 선택한 국가에 대해 프록시가 자동으로 활성화됩니다."
    PROXY_COUNTRY_CLEARED_MSG = "✅ 국가 선택이 삭제되었습니다."
    PROXY_COUNTRY_CLEARED_CALLBACK_MSG = "✅ 국가 선택이 삭제되었습니다."
    PROXY_COUNTRY_SELECTED_CALLBACK_MSG = "✅ 선택한 국가: {국가}"
    PROXY_COUNTRY_FROM_FILE_MSG = "🌍 파일의 국가 사용: {국가}"

    PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG = "🌍 파일에서 사용 가능한 국가: {count}"

    PROXY_COUNTRY_SELECTED_IN_MENU_MSG = "🌍 선택한 국가: {country}(코드: {country_code})"
    PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG = "✅ 이 국가에 프록시가 활성화되었습니다."
    PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG = "⚠️ 프록시 비활성화됨(활성화하려면 모두(AUTO)를 누르세요)"
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
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV: 켜짐"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV: 꺼짐"
    
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
    ADMIN_STATUS_CLEAN_TEXT_MSG = "청소됨"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "사용자 {user}의 답장 메시지 처리 오류: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "사용자 {user}에게 브로드캐스트 전송 오류: {error}"
    ADMIN_LOGS_FORMAT_MSG = "{bot_name}의 로그\n사용자: {user_id}\n총 로그: {total}\n현재 시간: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\n총 {path}: {count}\n현재 시간: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>총 사용자: {count}</i>\n최근 20개 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "관리자 {admin_id}가 포르노 캐시를 다시 로드했습니다. 도메인: {domains}, 키워드: {keywords}, 사이트: {sites}, 화이트리스트: {whitelist}, 그레이리스트: {greylist}, 블랙리스트: {black_list}, 화이트 키워드: {white_keywords}, 프록시 도메인: {proxy_domains}, 프록시 2 도메인: {proxy_2_domains}, 클린 쿼리: {clean_query}, 쿠키 없는 도메인: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "타임아웃 메시지 전송 오류: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>언어 선택</b>"
    LANG_CHANGED_MSG = "✅ 언어가 {lang_name}로 변경되었습니다"
    LANG_ERROR_MSG = "❌ 언어 변경 중 오류가 발생했습니다"
    LANG_CLOSED_MSG = "언어 선택이 닫혔습니다"
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] 콜백: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "URL로 브라우저 모니터링 버튼 추가 중: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "브라우저 모니터링 URL이 구성되지 않음: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **키보드 설정이 업데이트되었습니다!**\n\n새 설정: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "키보드 숨기기 실패: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "사용자 {user_id}의 링크 추출을 위해 작동하는 YouTube 쿠키 사용 중"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "사용자 {user_id}의 링크 추출을 위해 사용 가능한 작동하는 YouTube 쿠키가 없음"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "사용자 {user_id}의 링크 추출을 위해 기존 YouTube 쿠키 사용 중"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "사용자 {user_id}의 링크 추출을 위해 YouTube 쿠키를 찾을 수 없음"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "링크 추출을 위해 전역 쿠키 파일을 사용자 {user_id} 폴더로 복사함"
    
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
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ PO 토큰 지원으로 다운로드 완료"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood 제한. 나중에 시도하세요."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST 토큰 새로고침 오류: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Firebase 세션 종료 오류: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ 기본 데이터베이스 구조 초기화 오류: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ config.py에 모든 매개변수가 설정되지 않았습니다 (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL이 설정되지 않았습니다"
    DB_API_KEY_NOT_SET_MSG = "❌ idToken을 가져오기 위해 FIREBASE_CONF.apiKey가 설정되지 않았습니다"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Firebase 덤프 다운로드 오류: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ REST를 통해 Firebase 덤프 다운로드 실패"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ _download_and_reload_cache 오류: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ 자동 reload_cache 실행 오류 (시도 {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ 모든 재시도 실패"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 {datetime}에 Firebase 덤프 다운로드 시작"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ 종속성을 사용할 수 없음: requests 또는 Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ 데이터베이스가 비어 있습니다"
    
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
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "기다려주세요..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 HLS 스트림 다운로드 중:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "프래그먼트 대기 중"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Backup {ts} not found in _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Failed to restore {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ 복원됨: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>세부사항:</b> {error_details}\n\n중대한 오류로 인해 다운로드가 중지되었습니다.\n\n💡 <b>팁:</b> 401 Unauthorized 오류가 발생하는 경우 <code>/cookie instagram</code> 명령을 사용하거나 자체 쿠키를 보내서 Instagram으로 인증하세요."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domain in porn blacklist: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Found porn keywords: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domain in whitelist: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Found whitelist keywords: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ 포르노 키워드를 찾을 수 없습니다"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ 인덱스 {index}에서 TikTok API 오류, 다음 오디오로 건너뜀..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API error at index {index}, skipping to next video..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "User entered a <b>url</b>\n <b>user's name:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>사용자가 다음과 같이 입력했습니다:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "채널 가입"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 핸들러 등록 중: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - 내 5개 쿠키 다운로드"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - 브라우저의 YT 쿠키 가져오기"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - 쿠키 파일 검증"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - 사용자 정의 쿠키 업로드"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 닫기"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "사용 가능한 형식: {url}"
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
    URL_EXTRACTOR_CLOSED_MSG = "닫기"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "오류 발생"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "PATH 또는 프로젝트 디렉토리에서 ffmpeg를 찾을 수 없습니다. FFmpeg를 설치하세요."
    YTDLP_NOT_FOUND_MSG = "PATH 또는 프로젝트 디렉토리에서 yt-dlp 바이너리를 찾을 수 없습니다. yt-dlp를 설치하세요."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "비디오가 {rounds}개 부분으로 분할됩니다. 과도할 수 있습니다"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "비디오 부분 {current}/{total} 분할 중: {start_time:.2f}초부터 {end_time:.2f}초까지"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "분할 부분 {part} 생성 실패: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "분할 부분 {part} 성공적으로 생성됨: {target_name} ({size} 바이트)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "비디오 부분 {part} 분할 오류: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "비디오가 {count}개 부분으로 성공적으로 분할됨"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "비디오 분할 프로세스 오류: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] 비디오 {video_path} 처리 중 오류: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "비디오 파일이 존재하지 않습니다: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "크기 '{size_result}' 파싱 오류: {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "'{size_result}'에서 비디오 크기를 확인할 수 없습니다. 기본값 사용: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "썸네일 생성 오류: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "비디오 재생 시간 파싱 오류: {error}, 결과: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "{thumb_dir}에 썸네일이 생성되지 않았습니다. 기본값 사용"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "명령 실행 오류: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "FFmpeg로 썸네일 생성 오류: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "딕셔너리가 아닌 구성 섹션 건너뜀: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "{section}.{key} = {value} 설정"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] 사용자 쿠키 사용: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "사용자 {user_id}에 대한 YouTube 쿠키 사용"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "전역 쿠키 파일을 사용자 {user_id} 폴더로 복사함"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] 복사된 전역 쿠키를 사용자 쿠키로 사용: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "사용자 {user_id}에 대한 전역 쿠키 파일 복사 실패: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "도메인에 대해 --no-cookies 사용: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "프록시 요청되었지만 구성 가져오기/가져오기 실패: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "gallery-dl에 대해 프록시 강제 사용: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "프록시 요청되었지만 프록시 구성이 불완전함"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "프록시 도우미 실패: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "추출기 항목 파싱 중..."
    GALLERY_DL_ITEM_COUNT_MSG = "항목 {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "메타데이터 발견 (태그 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "URL 발견 (태그 3): {url}, 메타데이터: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "메타데이터 발견 (레거시): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "URL 발견 (레거시): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "파일명 발견: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "디렉토리 발견: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "확장자 발견: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "{count}개 항목 파싱됨, 정보: {info}, 대체: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "gallery-dl 구성 설정: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "전략 A 시도: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor 모듈을 찾을 수 없음"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "이 빌드에서 gallery_dl.extractor.find()를 사용할 수 없음"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "extractor.find({url}) 호출"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "URL과 일치하는 추출기가 없음"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "추출기에 쿠키 설정: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "추출기에 쿠키 설정 실패: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "추출기 발견, items() 호출"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "전략 A 성공, 정보 획득: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "전략 A: extractor.items()가 유효한 정보를 반환하지 않음"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "전략 A (extractor.find) 실패: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "--get-urls의 대체 메타데이터: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "모든 전략이 메타데이터를 얻지 못함"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "이미지 정보 추출 실패: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job 모듈을 찾을 수 없음 (설치가 손상되었나요?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "이 빌드에서 gallery_dl.job.DownloadJob을 사용할 수 없음"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "gallery-dl 디렉토리에서 다운로드된 파일 검색 중"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "추출기에서 이름으로 파일 찾기 시도"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "사용자 {user_id}의 인수 읽기 오류: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] 비디오 {video_path} 처리 중 오류: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "사용자 {user_id}가 send_as_file을 활성화했으며, 문서로 전송 중"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video가 반복적으로 시간 초과됨; send_document로 대체"
    SENDER_CAPTION_TOO_LONG_MSG = "캡션이 너무 깁니다. 최소 캡션으로 시도 중"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (최소 캡션) 시간 초과됨; send_document로 대체"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "최소 캡션으로 비디오 전송 오류: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "전체 설명 파일 전송 오류: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "임시 설명 파일 제거 오류: {error}"
    SENDER_FILE_SPLIT_FAILED_MSG = "❌ Error: Failed to split file into parts\nFile size: {size_mib:.2f} MiB"
    SENDER_VIDEO_PART_MSG = "Part {part_num}"
    SENDER_VIDEO_PART_OF_MSG = "Part {part_num}/{total_parts}"
    SENDER_VIDEO_SUBPART_MSG = "Part {part_num}.{subpart_num}"
# YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "NO_FILTER_DOMAINS의 도메인에 대해 match_filter 건너뜀: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "사용자 {user_id}의 형식 감지를 위해 사용자 URL에서 기존 YouTube 쿠키 확인 중"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "기존 YouTube 쿠키가 사용자 {user_id}의 형식 감지를 위해 사용자 URL에서 작동함 - 사용 중"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "기존 YouTube 쿠키가 사용자 URL에서 실패함, 사용자 {user_id}의 형식 감지를 위해 새 쿠키 가져오기 시도 중"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "사용자 {user_id}의 형식 감지를 위해 YouTube 쿠키 소스 {i} 시도 중"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "소스 {i}의 YouTube 쿠키가 사용자 {user_id}의 형식 감지를 위해 사용자 URL에서 작동함 - 사용자 폴더에 저장됨"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "소스 {i}의 YouTube 쿠키가 사용자 {user_id}의 형식 감지를 위해 사용자 URL에서 작동하지 않음"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "사용자 {user_id}의 형식 감지를 위해 소스 {i}에서 YouTube 쿠키 다운로드 실패"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "사용자 {user_id}의 형식 감지를 위해 모든 YouTube 쿠키 소스 실패, 쿠키 없이 시도함"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "사용자 {user_id}의 형식 감지를 위해 YouTube 쿠키 소스가 구성되지 않음, 쿠키 없이 시도함"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "사용자 {user_id}의 형식 감지를 위해 YouTube 쿠키를 찾을 수 없음, 새 쿠키 가져오기 시도 중"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "사용자 {user_id}의 형식 감지를 위해 YouTube 쿠키 사용 중 (Always Ask 메뉴에서 이미 검증됨)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "사용자 {user_id}의 형식 감지를 위해 YouTube 쿠키를 찾을 수 없음, 복원 시도 중..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "사용자 {user_id}의 형식 감지를 위해 전역 쿠키 파일을 사용자 {user_id} 폴더로 복사함"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "사용자 {user_id}의 전역 쿠키 파일 복사 실패: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "get_video_formats에서 도메인에 대해 --no-cookies 사용: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "앱이 아직 초기화되지 않았습니다. {name}에 액세스할 수 없습니다"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>캡션:</b> <code>{caption}</code>\n<b>사용자 ID:</b> <code>{user_id}</code>\n<b>사용자 이름:</b> <code>{users_name}</code>\n<b>비디오 파일 ID:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor 오류: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "caption_editor 예상치 못한 오류: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 비디오 URL</a>{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL이 구성에 없습니다"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin 초기화됨"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken 새로고침됨"
    DB_LOG_FOR_USER_ADDED_MSG = "사용자 로그 추가됨"
    DB_DATABASE_CREATED_MSG = "데이터베이스 생성됨"
    DB_BOT_STARTED_MSG = "봇 시작됨"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY가 config.py에 저장됨: {hours}시간"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "재생목록 부분이 이미 캐시됨: {path_parts}, 건너뜀"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: URL/화질 변형에 대한 캐시를 찾을 수 없음, 빈 딕셔너리 반환"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: 큰 범위에 대한 빠른 카운트: {cached_count}개의 캐시된 비디오"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: 해시 {url_hash}, 화질 {quality_key}에 대한 캐시를 찾을 수 없음"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: URL 변형에 대한 캐시를 찾을 수 없음, None 반환"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ 접근 거부됨. 관리자만 가능합니다."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 자동 Firebase 캐시 다시 로드 업데이트됨!\n\n📊 상태: {status}\n⏰ 일정: 00:00부터 매 {interval}시간마다\n🕒 다음 다시 로드: {next_exec} ({delta_min}분 후)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 자동 Firebase 캐시 다시 로드 중지됨!\n\n📊 상태: ❌ 비활성화됨\n💡 다시 활성화하려면 /auto_cache on 사용"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ 잘못된 인수입니다. /auto_cache on | off | N (1..168) 사용"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ 간격은 1시간에서 168시간 사이여야 합니다"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ 간격 설정 실패"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ 자동 Firebase 캐시 간격 업데이트됨!\n\n📊 상태: ✅ 활성화됨\n⏰ 일정: 00:00부터 매 {interval}시간마다\n🕒 다음 다시 로드: {next_exec} ({delta_min}분 후)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 자동 Firebase 캐시 다시 로드 시작됨!\n\n📊 상태: ✅ 활성화됨\n⏰ 일정: 00:00부터 매 {interval}시간마다\n🕒 다음 다시 로드: {next_exec} ({delta_min}분 후)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 자동 Firebase 캐시 다시 로드 중지됨!\n\n📊 상태: ❌ 비활성화됨\n💡 다시 활성화하려면 /auto_cache on 사용"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "자동 다시 로드 활성화됨; 다음: {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "관리자에 의해 자동 다시 로드 비활성화됨."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "자동 다시 로드 간격을 {interval}시간으로 설정; 다음: {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "자동 다시 로드 시작됨; 다음: {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "관리자에 의해 자동 다시 로드 중지됨."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase 캐시 로드됨: {count}개 루트 노드"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Firebase 캐시 파일을 찾을 수 없음, 빈 캐시로 시작: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Firebase 캐시 로드 실패: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase 캐시 다시 로드됨: {count}개 루트 노드"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Firebase 캐시 파일을 찾을 수 없음: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Firebase 캐시 다시 로드 실패: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = f"🚫 봇에서 차단되었습니다! 차단 해제를 원하시면 {Config.ADMIN_USERNAME}에게 문의하세요\n<blockquote>P.S. 채널을 떠나지 마세요 - 자동으로 차단됩니다 ⛔️</blockquote>\n🌍언어 변경 /lang"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ 비디오 형식을 찾을 수 없습니다. 이미지 다운로더 시도 중…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram이 메시지 전송을 제한했습니다.\n⏳ 기다려주세요: {time_str}\n타이머를 업데이트하려면 URL을 다시 2번 보내세요."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>버튼을 클릭하여 스트림 URL을 복사한 다음 VLC 앱에 붙여넣으세요</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>버튼을 클릭하여 스트림 URL을 복사한 다음 VLC 앱에 붙여넣으세요</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>링크 가져오기 오류:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ 형식 파일 전송 오류: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ 형식을 가져오지 못했습니다:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔎 분석 중... (6초 대기)"
    AA_PROCESSING_MSG = "🔎 분석 중..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ 태그 #{wrong}에 금지된 문자가 포함되어 있습니다. 문자, 숫자 및 _만 허용됩니다.\n사용: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ 그룹에서 작동하려면 봇에 관리자 권한이 필요합니다. 이 그룹의 관리자로 봇을 설정하세요."
    
    # URL extractor messages
    URL_EXTRACTOR_WELCOME_MSG = "안녕하세요 {first_name},\n \n<i>이 봇🤖은 모든 비디오를 Telegram으로 직접 다운로드할 수 있습니다.😊 자세한 내용은 <b>/help</b>를 누르세요</i> 👈\n\n<blockquote>참고: 🔞NSFW 콘텐츠 및 ☁️클라우드 스토리지의 파일 다운로드는 유료입니다! 1⭐️ = $0.02</blockquote>\n<blockquote>주의: ‼️ 채널을 떠나지 마세요 - 봇 사용이 차단됩니다 ⛔️</blockquote>\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 제거할 파일이 없습니다."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 모든 파일이 성공적으로 제거되었습니다!\n\n제거된 파일:\n{files_list}"
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ 이전 다운로드가 완료될 때까지 기다리세요"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "check_user에서 앱 인스턴스가 None입니다"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict가 None입니다, 다운로드 허용"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict가 None입니다, 자막 삽입 허용"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: 제한 확인 중 - max_quality={max_quality}p, max_duration={max_duration}초, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: info_dict 키: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "자막 삽입 건너뜀: 재생 시간 {duration}초가 제한 {max_duration}초를 초과함"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "자막 삽입 건너뜀: 크기 {size_mb:.2f}MB가 제한 {max_size}MB를 초과함"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "자막 삽입 건너뜀: 화질 {width}x{height} (최소 변 {min_side}p)가 제한 {max_quality}p를 초과함"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "TikTok"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Instagram"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "재생목록"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ {service}에 대한 범위 제한 초과: {count} (최대 {max_count}).\n\n사용 가능한 최대 파일을 다운로드하려면 다음 명령 중 하나를 사용하세요:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ {service}에 대한 범위 제한 초과: {count} (최대 {max_count})\n사용자 ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "구성에서 PO 토큰 제공자가 비활성화됨"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url}이 YouTube 도메인이 아니므로 PO 토큰 건너뜀"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO 토큰 제공자가 {base_url}에서 사용할 수 없음, 표준 YouTube 추출로 대체"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO 토큰 제공자 캐시가 지워졌습니다. 다음 요청에서 가용성을 확인합니다"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "앱 인스턴스를 아직 사용할 수 없음"
    HELPER_USER_NAME_MSG = "사용자"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood 대기 감지됨, {wait_seconds}초 대기 중"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood 대기가 감지되었지만 시간을 추출할 수 없음, {retry_delay}초 대기 중"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno 오류 감지됨, {retry_delay}초 대기 중"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "프록시 구성이 불완전함, 직접 연결 사용"
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
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "예:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code> (direct order)\n• <code>/vid -3-7 https://youtube.com/playlist?list=123abc</code> (reverse order)"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "참고: /audio, /img, /help, /playlist, /settings"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "사용자 {user_id}가 add_bot_to_group 명령을 닫았습니다"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "YouTube ID 추출 실패"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "썸네일 다운로드 실패 또는 너무 큼"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "오디오 언어 선택"
    AA_NO_SUBTITLES_DETECTED_MSG = "자막 감지되지 않음"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "자막 언어 선택"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "인증 오류"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "계정을 찾을 수 없음"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "계정을 사용할 수 없음"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "속도 제한 초과"
    GALLERY_DL_NETWORK_ERROR_MSG = "네트워크 오류"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "콘텐츠를 사용할 수 없음"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "지리적 제한"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "인증 필요"
    GALLERY_DL_POLICY_VIOLATION_MSG = "정책 위반"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "알 수 없는 오류"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ 다운로드 시작됨</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Close"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 비디오 다운로드 명령</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "사용법: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>예제:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "참고: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Flood 제한. 나중에 시도하세요."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 쿠키 명령 사용법</b>

<code>/cookie</code> - 쿠키 메뉴 표시
<code>/cookie youtube</code> - YouTube 쿠키 다운로드
<code>/cookie instagram</code> - Instagram 쿠키 다운로드
<code>/cookie tiktok</code> - TikTok 쿠키 다운로드
<code>/cookie x</code> 또는 <code>/cookie twitter</code> - Twitter/X 쿠키 다운로드
<code>/cookie facebook</code> - Facebook 쿠키 다운로드
<code>/cookie custom</code> - 사용자 정의 쿠키 지침 표시

<i>사용 가능한 서비스는 봇 구성에 따라 다릅니다.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 쿠키 파일이 제거되고 캐시가 지워졌습니다."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Prev"
    SUBS_BACK_BUTTON_MSG = "🔙Back"
    SUBS_OFF_BUTTON_MSG = "🚫 OFF"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - set language"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - set language with AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Valid options:"
    
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
    KEYBOARD_OFF_BUTTON_MSG = "🔴 꺼짐"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 전체"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[이미지 URL]({url})"
    IMAGE_ERROR_MSG = "❌ 오류: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙 뒤로"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - 사용자 정의 형식"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p 화질"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K 화질"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K 화질"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - 특정 형식 ID"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - 항상 메뉴 표시"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/최고 화질"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ 항상 묻기 (메뉴 + 버튼)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 기타 (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (PC/Mac Telegram에 최적)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (모바일 Telegram에 최적)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (최대 화질)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 사용자 정의 (직접 입력)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 브라우저에서"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 직접 입력"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ 비활성으로 인해 입력 모드가 자동으로 닫혔습니다 (5분)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 모두 재설정"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 현재 보기"
    ARGS_BACK_BUTTON_MSG = "🔙 뒤로"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>이 메시지를 즐겨찾기로 전달하여 이러한 설정을 템플릿으로 저장하세요.</i> \n\n<i>이 메시지를 여기로 다시 전달하여 이러한 설정을 적용하세요.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 현재 yt-dlp 인수:\n\n사용자 정의 설정이 구성되지 않았습니다.\n\n---\n\n<i>이 메시지를 즐겨찾기로 전달하여 이러한 설정을 템플릿으로 저장하세요.</i> \n\n<i>이 메시지를 여기로 다시 전달하여 이러한 설정을 적용하세요.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 현재 yt-dlp 인수:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 설정 내보내기"
    ARGS_SETTINGS_READY_MSG = "설정이 내보내기 준비되었습니다! 이 메시지를 즐겨찾기로 전달하여 저장하세요."
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 현재 yt-dlp 인수:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ 메시지에서 설정을 인식하지 못했습니다. 올바른 설정 템플릿을 보냈는지 확인하세요."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ 설정이 성공적으로 가져왔습니다!\n\n적용된 매개변수: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "주요 설정:\n"
    ARGS_ERROR_SAVING_MSG = "❌ 가져온 설정 저장 중 오류가 발생했습니다."
    ARGS_ERROR_IMPORTING_MSG = "❌ 설정 가져오기 중 오류가 발생했습니다."

    # Cookie command menu messages
    COOKIE_MENU_TITLE_MSG = "🍪 <b>쿠키 파일 다운로드</b>"
    COOKIE_MENU_DESCRIPTION_MSG = "쿠키 파일을 다운로드할 서비스를 선택하세요."
    COOKIE_MENU_SAVE_INFO_MSG = "쿠키 파일은 폴더에 cookie.txt로 저장됩니다."
    COOKIE_MENU_TIP_HEADER_MSG = "팁: 직접 명령을 사용할 수도 있습니다:"
    COOKIE_MENU_TIP_YOUTUBE_MSG = "• <code>/cookie youtube</code> – 쿠키 다운로드 및 검증"
    COOKIE_MENU_TIP_YOUTUBE_INDEX_MSG = "• <code>/cookie youtube 1</code> – 인덱스로 특정 소스 사용 (1–{max_index})"
    COOKIE_MENU_TIP_VERIFY_MSG = "그런 다음 <code>/check_cookie</code>로 확인하세요 (RickRoll에서 테스트)."

    # Subs command button messages
    SUBS_ALWAYS_ASK_BUTTON_MSG = "항상 묻기"
    SUBS_AUTO_TRANS_BUTTON_MSG = "자동/번역"

    # Always Ask menu button messages
    ALWAYS_ASK_LINK_BUTTON_MSG = "🔗링크"
    # ALWAYS_ASK_WATCH_BUTTON_MSG = "👁Watch"  # TEMPORARILY DISABLED: poketube service is down
    ALWAYS_ASK_CAPTION_BUTTON_MSG = "📝캡션"
    ALWAYS_ASK_TRIM_BUTTON_MSG = "✂️ 자르기"
    ALWAYS_ASK_TRIM_PROMPT_MSG = "✂️ <b>비디오 자르기</b>\n\n비디오 길이: <b>{start_time} - {end_time}</b>\n\n원하는 시간 범위를 형식으로 보내주세요:\n<code>HH:MM:SS-HH:MM:SS</code>\n\n예: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_FORMAT_MSG = "❌ 잘못된 형식입니다. 다음을 사용하세요: <code>HH:MM:SS-HH:MM:SS</code>\n\n예: <code>01:13:20-10:01:01</code>"
    ALWAYS_ASK_TRIM_INVALID_RANGE_MSG = "❌ 잘못된 범위입니다. 시작 시간은 종료 시간보다 작아야 합니다."
    ALWAYS_ASK_TRIM_OUT_OF_BOUNDS_MSG = "❌ 시간 범위가 비디오 경계를 벗어났습니다.\n\n비디오 길이: <b>{start_time} - {end_time}</b>\n\n범위는 이러한 제한 내에 있어야 합니다."
    ALWAYS_ASK_TRIM_INFO_MSG = "✂️ <b>비디오가 잘립니다:</b> {start_time} - {end_time}"

    # Audio upload completion messages
    AUDIO_PARTIALLY_COMPLETED_MSG = "⚠️ 부분 완료 - {successful_uploads}/{total_files} 오디오 파일이 업로드되었습니다."
    AUDIO_SUCCESSFULLY_COMPLETED_MSG = "✅ 오디오가 성공적으로 다운로드되고 전송되었습니다 - {total_files} 파일이 업로드되었습니다."

    # TikTok private account messages
    TIKTOK_PRIVATE_ACCOUNT_MSG = (
        "🔒 <b>비공개 TikTok 계정</b>\n\n"
        "이 TikTok 계정은 비공개이거나 모든 비디오가 비공개입니다.\n\n"
        "<b>💡 해결 방법:</b>\n"
        "1. 계정 @{username}을(를) 팔로우하세요\n"
        "2. <code>/cookie</code> 명령을 사용하여 봇에 쿠키를 보내세요\n"
        "3. 다시 시도하세요\n\n"
        "<b>쿠키를 업데이트한 후 다시 시도하세요!</b>"
    )

    #######################################################
