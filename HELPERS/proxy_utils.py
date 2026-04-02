from __future__ import annotations

from urllib.parse import urlsplit, urlunsplit


def redact_proxy_url_for_logs(proxy_url: str, password_replacement: str = "*****") -> str:
    """
    Return a log-safe proxy URL by masking any embedded password.

    Examples:
      - http://user:pass@1.2.3.4:8080 -> http://user:*****@1.2.3.4:8080
      - socks5h://user:pass@host:1080 -> socks5h://user:*****@host:1080
    """
    if not proxy_url:
        return proxy_url

    try:
        parts = urlsplit(proxy_url)
    except Exception:
        return "[REDACTED]"

    if parts.password is None:
        return proxy_url

    username = parts.username or ""
    host = parts.hostname or ""
    port = parts.port

    if not host:
        return "[REDACTED]"

    if username:
        userinfo = f"{username}:{password_replacement}@"
    else:
        userinfo = f"{password_replacement}@"

    netloc = f"{userinfo}{host}"
    if port is not None:
        netloc = f"{netloc}:{port}"

    return urlunsplit((parts.scheme, netloc, parts.path, parts.query, parts.fragment))

