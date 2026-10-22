"""classify_yt_dlp_error categories + has_alternative_proxy_route (agent A1). No network."""
import sys, os
sys.argv.append('.')
REPO = os.path.abspath(sys.argv[1])
sys.path.insert(0, REPO)
# reuse the stubbing harness of the main test without running its cases
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_a1_get_video_formats.py'), encoding='utf-8').read()
exec(src.split('# ---------------------------------------------------------------- helpers')[0])

from CONFIG.errors import classify_yt_dlp_error
from HELPERS import proxy_helper

cases = [
    ("Join this channel to get access to members-only content", 'MEMBERS_ONLY'),
    ("This video is available to this channel's members on level: Fan", 'MEMBERS_ONLY'),
    ("Sign in to confirm your age. This video may be inappropriate for some users.", 'AGE_RESTRICTED'),
    ("Take a few minutes to verify your age", 'AGE_RESTRICTED'),
    ("Sign in to confirm you're not a bot", 'SIGN_IN_REQUIRED'),
    ("[Douyin] 1: Fresh cookies (not necessarily logged in) are needed", 'COOKIES_REQUIRED'),
    ("[generic] track: Unable to download webpage: HTTP Error 400: Bad Request", 'HTTP_CLIENT_ERROR'),
    ("[generic] track: Unable to download webpage: HTTP Error 404: Not Found", 'HTTP_CLIENT_ERROR'),
    ("[generic] track: Unable to download webpage: HTTP Error 403: Forbidden", None),
    ("[facebook] 1: Cannot parse data; please report this issue", 'EXTRACTOR_ERROR'),
    ("An extractor error has occurred. (caused by KeyError('INNERTUBE_CONTEXT'))", 'EXTRACTOR_ERROR'),
    ("the JSON object must be str, bytes or bytearray, not dict", 'EXTRACTOR_ERROR'),
    ("The page needs to be reloaded.", 'EXTRACTOR_ERROR'),
    ("Video unavailable", None),
]
ok_all = True
for text, exp in cases:
    got = classify_yt_dlp_error(text)
    ok = got == exp
    ok_all &= ok
    print(f"[{'PASS' if ok else 'FAIL'}] {text[:60]!r} -> {got} (expected {exp})")

route_cases = [
    ({'enabled': False, 'country': None, 'proxies': []}, False),
    ({'enabled': True, 'country': None, 'proxies': []}, False),        # AUTO mode
    ({'enabled': True, 'country': 'DE', 'proxies': []}, False),        # country without proxies
    ({'enabled': True, 'country': 'DE', 'proxies': [{'proxy_url': 'http://p:1'}]}, True),
]
for state, exp in route_cases:
    PROXY.update(state)
    got = proxy_helper.has_alternative_proxy_route('https://www.youtube.com/watch?v=x', 1)
    ok = got == exp
    ok_all &= ok
    print(f"[{'PASS' if ok else 'FAIL'}] has_alternative_proxy_route({state}) -> {got} (expected {exp})")
print(f"no user_id -> {proxy_helper.has_alternative_proxy_route('https://x.org/', None)} (expected False)")
ok_all &= proxy_helper.has_alternative_proxy_route('https://x.org/', None) is False
print('ALL PASS' if ok_all else 'SOME FAILED')
sys.exit(0 if ok_all else 1)
