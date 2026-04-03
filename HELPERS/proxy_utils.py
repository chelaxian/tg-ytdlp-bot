import re
from urllib.parse import urlsplit, urlunsplit

import requests


def redact_proxy_url_for_logs(proxy_url: str, password_replacement: str = "*****") -> str:
    """
    Return a proxy URL safe for logging (never logs the password).

    Examples:
      - http://user:pass@1.2.3.4:8080 -> http://user:*****@1.2.3.4:8080
      - socks5://1.2.3.4:1080        -> socks5://1.2.3.4:1080
    """
    if not proxy_url:
        return ""
    try:
        parts = urlsplit(str(proxy_url))
        # If we can't parse netloc/host, do not risk returning raw string
        if not parts.netloc or parts.hostname is None:
            return "[REDACTED]"

        user = parts.username
        # IMPORTANT: never use parts.password for logging
        host = parts.hostname
        port = parts.port

        auth = ""
        if user:
            auth = f"{user}:{password_replacement}@"
        elif "@" in parts.netloc:
            # Some malformed URLs may include userinfo without username; still redact
            auth = f"{password_replacement}@"

        hostport = host
        if port is not None:
            hostport = f"{host}:{port}"

        safe_netloc = f"{auth}{hostport}"
        return urlunsplit((parts.scheme, safe_netloc, parts.path, parts.query, parts.fragment))
    except Exception:
        # Fallback: best-effort masking of ":password@" part
        try:
            replacement = ":" + password_replacement + "@"
            return re.sub(r":([^@/]+)@", replacement, str(proxy_url))
        except Exception:
            return "[REDACTED]"


def test_proxy_url(proxy_url: str, timeout: int = 5) -> bool:
    """
    Quick reachability check for a proxy URL.
    """
    try:
        r = requests.get("https://httpbin.org/ip", proxies={"http": proxy_url, "https": proxy_url}, timeout=timeout)
        return r.status_code == 200
    except Exception:
        return False

