"""Isolated smoke tests for get_video_formats retry behaviour (agent A1).

No network: yt_dlp.YoutubeDL is mocked to raise the errors reported in the
issues; COMMANDS.* (cookies/proxy/args) are stubbed so we control the cookie
and proxy routes and can count every extraction attempt.

Run:  python test_a1_get_video_formats.py <repo_root>
"""
import importlib.abc
import importlib.machinery
import os
import sys
import tempfile
import types
from unittest import mock

REPO = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
sys.path.insert(0, REPO)
os.chdir(tempfile.mkdtemp())  # users/<id>/cookie.txt lookups stay isolated


# ---------------------------------------------------------------- stubbing
class _StubModule(types.ModuleType):
    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)
        value = mock.MagicMock(name=f'{self.__name__}.{name}')
        setattr(self, name, value)
        return value


class _StubFinder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    PREFIXES = ('pyrogram', 'gallery_dl', 'tgcrypto', 'firebase', 'pyrebase')

    def find_spec(self, fullname, path, target=None):
        if fullname.split('.')[0] in self.PREFIXES:
            return importlib.machinery.ModuleSpec(fullname, self, is_package=True)
        return None

    def create_module(self, spec):
        m = _StubModule(spec.name)
        m.__path__ = []
        return m

    def exec_module(self, module):
        pass


sys.meta_path.insert(0, _StubFinder())

# --- fake yt_dlp
yt_dlp = types.ModuleType('yt_dlp')
yt_utils = types.ModuleType('yt_dlp.utils')


class DownloadError(Exception):
    pass


yt_utils.DownloadError = DownloadError
yt_dlp.utils = yt_utils
CALLS = []          # one entry per YoutubeDL.extract_info call (opts snapshot)
BEHAVIOUR = {'fn': None}


class FakeYDL:
    def __init__(self, opts):
        self.opts = dict(opts)

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def extract_info(self, url, download=False):
        CALLS.append(self.opts)
        return BEHAVIOUR['fn'](self.opts, len(CALLS))


yt_dlp.YoutubeDL = FakeYDL
sys.modules['yt_dlp'] = yt_dlp
sys.modules['yt_dlp.utils'] = yt_utils


def _stub(name, **attrs):
    m = _StubModule(name)
    for k, v in attrs.items():
        setattr(m, k, v)
    sys.modules[name] = m
    return m


# Proxy state controlled per test
PROXY = {'enabled': False, 'country': None, 'proxies': []}
proxy_cmd = _stub(
    'COMMANDS.proxy_cmd',
    get_proxy_config=lambda: {},
    is_proxy_enabled=lambda uid: PROXY['enabled'],
    get_user_selected_country=lambda uid: PROXY['country'],
    get_proxies_for_country=lambda c: list(PROXY['proxies']),
    get_proxy_url_for_user_country=lambda uid: ((PROXY['proxies'][0]['proxy_url'], PROXY['country'])
                                                 if PROXY['country'] and PROXY['proxies'] else (None, None)),
)
_stub('COMMANDS.args_cmd', get_user_ytdlp_args=lambda uid, url: {}, log_ytdlp_options=lambda *a, **k: None)
_stub('HELPERS.safe_messeger', safe_send_message=lambda *a, **k: None)
_stub('HELPERS.proxy_utils', test_proxy_url=lambda *a, **k: True, redact_proxy_url_for_logs=lambda u: '[r]')
_stub('HELPERS.pot_helper', add_pot_to_ytdl_opts=lambda opts, url: opts)
_stub('HELPERS.filesystem_hlp', create_directory=lambda *a, **k: None)
_stub('HELPERS.porn', is_porn=lambda *a, **k: False)
import logging
logging.basicConfig(level=logging.WARNING, format='    %(levelname)s %(message)s')
_stub('HELPERS.logger', logger=logging.getLogger('hook'), send_error_to_user=lambda *a, **k: None)


class _MsgStr(str):
    def format(self, *a, **k):
        return str(self)


class _Msgs:
    def __getattr__(self, name):
        return _MsgStr(name)


_stub('CONFIG.messages', Messages=_Msgs, safe_get_messages=lambda uid=None: _Msgs())


class _Limits:
    ENABLE_LIVE_STREAM_BLOCKING = True
    MAX_PROXIES_PER_COUNTRY = 3
    AUTO_PROXY_MAX_TIME = 300
    AUTO_PROXY_MAX_ATTEMPTS = 100
    AUTO_PROXY_CACHE_TTL = 300


import CONFIG.limits as _real_limits
for _k, _v in vars(_Limits).items():
    if not _k.startswith('__'):
        setattr(_real_limits.LimitsConfig, _k, _v)


class _Domains:
    YTDLP_ONLY_DOMAINS = ['youtube.com', 'youtu.be', 'www.youtube.com', 'm.youtube.com']
    NO_PROXY_DOMAINS = []
    AUTO_PROXY_DOMAINS = []
    PROXY_1_DOMAINS = []
    PROXY_2_DOMAINS = []
    PROXY_ALL_NSFW = False
    NO_FILTER_DOMAINS = []
    NO_COOKIE_DOMAINS = []


import CONFIG.domains as _real_domains
for _k, _v in vars(_Domains).items():
    if not _k.startswith('__'):
        setattr(_real_domains.DomainsConfig, _k, _v)
_stub('URL_PARSERS.nocookie', is_no_cookie_domain=lambda url: False)
_stub('URL_PARSERS.filter_check', is_no_filter_domain=lambda url: True)
_stub('URL_PARSERS.filter_utils', create_smart_match_filter=lambda **k: None, create_legacy_match_filter=lambda **k: None)

COOKIE_LOG = []


def _yt_cookie_retry(user_id, url, func, *args, **kwargs):
    # Mirrors COMMANDS.cookies_cmd: tries 2 cookie sources, swallows errors
    COOKIE_LOG.append('yt')
    for _ in range(2):
        try:
            r = func(*args, **kwargs)
            if r is not None:
                return r
        except Exception:
            pass
    return None


def _non_yt_cookie_fallback(user_id, url, func, *args):
    # Mirrors COMMANDS.cookies_cmd: user, service, global, no-cookie (4 tries)
    COOKIE_LOG.append('non_yt')
    for _ in range(4):
        try:
            r = func(*args)
            if r is not None:
                return r
        except Exception:
            pass
    return None


def _is_youtube_cookie_error(msg):
    low = msg.lower()
    return any(k in low for k in ('sign in', 'cookies', 'unable to extract', 'http error 403', 'forbidden'))


_stub(
    'COMMANDS.cookies_cmd',
    get_youtube_cookie_urls=lambda: [],
    reset_checked_cookie_sources=lambda uid: None,
    _download_content=lambda *a, **k: (False, 0, None, 'x'),
    get_cookie_cache_result=lambda uid, url: None,
    set_cookie_cache_result=lambda *a, **k: None,
    try_non_youtube_cookie_fallback=_non_yt_cookie_fallback,
    get_service_name_from_url=lambda url: 'other',
    is_youtube_cookie_error=_is_youtube_cookie_error,
    is_youtube_geo_error=lambda msg: 'not available in your country' in msg.lower(),
    retry_download_with_different_cookies=_yt_cookie_retry,
    retry_download_with_proxy=lambda *a, **k: None,
)

import DOWN_AND_UP.yt_dlp_hook as hook  # noqa: E402

# ---------------------------------------------------------------- helpers
RESULTS = []


def run(name, url, error_fn, expect_calls, expect, proxy=None, user_id=111, check=None):
    CALLS.clear()
    COOKIE_LOG.clear()
    hook._terminal_results.clear()
    PROXY.update({'enabled': False, 'country': None, 'proxies': []})
    if proxy:
        PROXY.update(proxy)
    BEHAVIOUR['fn'] = error_fn
    try:
        out = hook.get_video_formats(url, user_id)
        outcome = ('dict', out.get('error') if isinstance(out, dict) else None)
    except DownloadError as e:
        out = e
        outcome = ('raise', str(e)[:60])
    ok = len(CALLS) == expect_calls and (expect == outcome[1] if outcome[0] == 'dict' else expect == 'RAISE')
    if check is not None:
        ok = ok and check(out)
    RESULTS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: extractions={len(CALLS)} (expected {expect_calls}), "
          f"outcome={outcome}, cookie_passes={COOKIE_LOG}")
    return out


def raises(msg):
    def fn(opts, n):
        raise DownloadError(msg)
    return fn


YT = 'https://www.youtube.com/watch?v=abcdefghijk'

# ---------------------------------------------------------------- cases
print('== #479 Video unavailable (YouTube, user without proxy)')
run('#479 video unavailable', YT, raises('ERROR: [youtube] abc: Video unavailable. This video has been removed by the uploader'),
    1, 'PERMANENT_UNAVAILABLE')

print('== #352 members-only (both wordings)')
run('#352 join this channel', YT, raises("ERROR: [youtube] abc: Join this channel to get access to members-only content like this video"),
    1, 'PERMANENT_UNAVAILABLE')
run("#352 available to channel's members", YT, raises("ERROR: [youtube] abc: This video is available to this channel's members on level: Fan"),
    1, 'PERMANENT_UNAVAILABLE')

print('== #360 age verification')
run('#360 sign in to confirm your age', YT, raises("ERROR: [youtube] abc: Sign in to confirm your age. This video may be inappropriate for some users."),
    1, 'PERMANENT_UNAVAILABLE')
run('#360 take a few minutes to verify', YT, raises("ERROR: [youtube] abc: Take a few minutes to verify your age."),
    1, 'PERMANENT_UNAVAILABLE')

print('== #394/#436/#475 bot-check family (fail fast, no cookie/proxy)')
run('#394 not a bot', YT, raises("ERROR: [youtube] abc: Sign in to confirm you're not a bot"), 1, 'PERMANENT_UNAVAILABLE')
run('#436 page needs reload', YT, raises("ERROR: [youtube] abc: The page needs to be reloaded."), 1, 'PERMANENT_UNAVAILABLE')
run('#475 INNERTUBE_CONTEXT', YT, raises("ERROR: [youtube] abc: An extractor error has occurred. (caused by KeyError('INNERTUBE_CONTEXT'))"),
    1, 'PERMANENT_UNAVAILABLE')
run('#475 INNERTUBE_CONTEXT, user with country proxies', YT,
    raises("ERROR: [youtube] abc: An extractor error has occurred. (caused by KeyError('INNERTUBE_CONTEXT'))"),
    1, 'PERMANENT_UNAVAILABLE',
    proxy={'enabled': True, 'country': 'DE', 'proxies': [{'proxy_url': f'http://p{i}:1', 'type': 'http', 'country': 'DE'} for i in range(3)]})

print('== #386 Douyin fresh cookies: exactly one cookie pass, then stop')
run('#386 douyin', 'https://www.douyin.com/video/7300000000000000000',
    raises('ERROR: [Douyin] 7300: Fresh cookies (not necessarily logged in) are needed'),
    1 + 4, 'PERMANENT_UNAVAILABLE', check=lambda out: COOKIE_LOG == ['non_yt'])

print('== #477 generic HTTP 400 / 403')
run('#477 generic 400', 'https://example.org/track', raises('ERROR: [generic] track: Unable to download webpage: HTTP Error 400: Bad Request'),
    1, 'PERMANENT_UNAVAILABLE')
# 403: one cookie pass (4) + impersonate (4 basic targets, no curl_cffi), original NOT repeated; no gallery-dl
# offer (stubbed gallery_dl has no 'find' that returns a specific extractor -> MagicMock); then the error is raised
with mock.patch.object(hook, 'gallery_dl_has_extractor', lambda url: False):
    run('#477 generic 403 (no proxy)', 'https://example.org/track', raises('ERROR: [generic] track: Unable to download webpage: HTTP Error 403: Forbidden'),
        1 + 4 + 4, 'RAISE')

print('== #469/#471 ok.ru json.loads(dict): non-DownloadError TypeError -> EXTRACTION_ERROR, 1 attempt')


def _typeerror(opts, n):
    raise TypeError('the JSON object must be str, bytes or bytearray, not dict')


run('#469 ok.ru TypeError', 'https://ok.ru/videoembed/123', _typeerror, 1, 'EXTRACTION_ERROR')
run('#471 wrapped as DownloadError', 'https://ok.ru/videoembed/123',
    raises('ERROR: the JSON object must be str, bytes or bytearray, not dict'), 1, 'PERMANENT_UNAVAILABLE')

print('== #480 Pinterest image-only pin -> gallery-dl, 1 attempt')
with mock.patch.object(hook, 'gallery_dl_has_extractor', lambda url: True):
    run('#480 pinterest', 'https://www.pinterest.com/pin/123/', raises('ERROR: [Pinterest] 123: No video formats found!'),
        1, 'FALLBACK_TO_GALLERY_DL')

print('== #362 Requested format not available (YouTube, no proxy): no identical re-runs, error re-raised')
run('#362 format n/a', YT, raises('ERROR: [youtube] abc: Requested format is not available. Use --list-formats'), 1, 'RAISE')

print('== #484/#328 Facebook cannot parse data')
run('#484 facebook', 'https://www.facebook.com/watch/?v=1', raises('ERROR: [facebook] 1: Cannot parse data; please report this issue'),
    1, 'PERMANENT_UNAVAILABLE')

print('== #464 read timeout: exactly one retry with longer socket_timeout (no recursion)')
run('#464 timeout twice', YT, raises("ERROR: HTTPSConnectionPool(host='www.youtube.com', port=443): Read timed out. (read timeout=60.0)"),
    2, 'RAISE', check=lambda out: CALLS[1].get('socket_timeout') == 120)


def _timeout_then_ok(opts, n):
    if n == 1:
        raise DownloadError("ERROR: Read timed out. (read timeout=60.0)")
    return {'id': 'abc', 'title': 't', 'formats': []}


run('#464 timeout then success', YT, _timeout_then_ok, 2, None, check=lambda out: isinstance(out, dict) and out.get('id') == 'abc')

print('== country proxy route: rotates only for non-terminal errors')
_px = {'enabled': True, 'country': 'DE', 'proxies': [{'proxy_url': f'http://p{i}:1', 'type': 'http', 'country': 'DE'} for i in range(3)]}
run('geo-ish unknown error w/ 3 proxies', YT, raises('ERROR: [youtube] abc: something odd'), 1 + 3 + 1, 'RAISE', proxy=_px)

print('== negative cache: repeated calls for a dead video do not re-extract')
CALLS.clear(); hook._terminal_results.clear(); PROXY.update({'enabled': False, 'country': None, 'proxies': []})
BEHAVIOUR['fn'] = raises('ERROR: [youtube] abc: Video unavailable')
outs = [hook.get_video_formats(YT, 222) for _ in range(9)]
ok = len(CALLS) == 1 and all(o.get('error') == 'PERMANENT_UNAVAILABLE' for o in outs)
RESULTS.append(ok)
print(f"[{'PASS' if ok else 'FAIL'}] 9 calls (download format cascade) -> extractions={len(CALLS)} (expected 1)")
# new cookie.txt invalidates the entry
os.makedirs(os.path.join('users', '222'), exist_ok=True)
with open(os.path.join('users', '222', 'cookie.txt'), 'w') as f:
    f.write('# Netscape HTTP Cookie File\n')
hook.get_video_formats(YT, 222)
ok = len(CALLS) == 2
RESULTS.append(ok)
print(f"[{'PASS' if ok else 'FAIL'}] new cookie.txt invalidates cache -> extractions={len(CALLS)} (expected 2)")

print('== success path unchanged')
run('success', YT, lambda o, n: {'id': 'x', 'title': 'T', 'formats': [{'format_id': '18'}]}, 1, None,
    check=lambda out: out.get('id') == 'x')

print()
print(f"{sum(RESULTS)}/{len(RESULTS)} passed")
sys.exit(0 if all(RESULTS) else 1)
