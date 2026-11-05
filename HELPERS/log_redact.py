"""Mask credentials in every log record before any handler formats it.

Users pass their own credentials to the bot: /args http_headers with
"Authorization: Bearer <JWT>" or cookies, proxy URLs with user:password. The
bot logs args, yt-dlp options and message texts, so on 2026-11-05 a user's
bearer token sat in the journal in clear text (~50 lines in 12 h).

install() wraps the logging record factory: the final message of each record
(for every logger, at every handler) has these values replaced by "***".
Dependency-free on purpose; installed first thing in magic.py.
"""
import logging
import re

_HINTS = ("bearer", "basic ", "authoriz", "cookie", "token", "api-key", "api_key", "eyj", "@")

_PATTERNS = (
    # Authorization: Bearer xxx / Basic xxx (any quoting, also inside escaped JSON)
    (re.compile(r"\b(Bearer|Basic)(\s+)[A-Za-z0-9._~+/=-]{6,}", re.IGNORECASE), r"\1\2***"),
    # header-like keys followed by a value: "Cookie": "a=b; c=d" / x-api-key=... / X-Auth-Token: ...
    (re.compile(
        r"""((?:proxy-)?authorization|cookie|set-cookie|x-api-key|api[_-]key|x-auth-token|access[_-]token|refresh[_-]token)"""
        r"""(\\?["']?\s*[:=]\s*\\?["']?)(?!\s*(?:Bearer|Basic)\b)([^"'\\\n,}{]{3,})""",
        re.IGNORECASE),
     r"\1\2***"),
    # bare JWTs
    (re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{4,}"), "***jwt***"),
    # proxy/URL credentials scheme://user:pass@host
    (re.compile(r"((?:https?|socks4a?|socks5h?)://)[^:@\s/'\"]+:[^@\s'\"]+@", re.IGNORECASE), r"\1***:***@"),
)


def redact(text: str) -> str:
    """Return text with credentials masked (cheap no-op for ordinary lines)."""
    if not text:
        return text
    lowered = text.lower()
    if not any(h in lowered for h in _HINTS):
        return text
    for pattern, repl in _PATTERNS:
        text = pattern.sub(repl, text)
    return text


_installed = False


def install() -> bool:
    """Wrap the record factory once. Returns True if installed now."""
    global _installed
    if _installed:
        return False
    previous = logging.getLogRecordFactory()

    def factory(*args, **kwargs):
        record = previous(*args, **kwargs)
        try:
            message = record.getMessage()
        except Exception:
            return record  # let the handler report the broken format as usual
        cleaned = redact(message)
        if cleaned is not message and cleaned != message:
            record.msg = cleaned
            record.args = None
        return record

    logging.setLogRecordFactory(factory)
    _installed = True
    return True
