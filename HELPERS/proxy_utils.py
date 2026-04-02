from __future__ import annotations

from urllib.parse import urlsplit, urlunsplit


def redact_proxy_url_for_logs(proxy_url: str | None) -> str | None:
    """
    Redact credentials in proxy URLs for safe logging.

    Examples:
      - http://user:pass@1.2.3.4:8080 -> http://user:*****@1.2.3.4:8080
      - socks5://user:pass@host:1080 -> socks5://user:*****@host:1080
    """
    if not proxy_url:
        return proxy_url

    s = str(proxy_url)
    if "://" not in s:
        return s

    try:
        parts = urlsplit(s)
        netloc = parts.netloc

        if "@" in netloc:
            userinfo, hostport = netloc.rsplit("@", 1)
            if ":" in userinfo:
                user, _, _pwd = userinfo.partition(":")
                safe_userinfo = f"{user}:*****" if user else "*****"
                netloc = f"{safe_userinfo}@{hostport}"

        return urlunsplit((parts.scheme, netloc, parts.path, parts.query, parts.fragment))
    except Exception:
        return "[REDACTED]"
