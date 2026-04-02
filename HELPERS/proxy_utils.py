import re
from urllib.parse import urlsplit, urlunsplit


def redact_proxy_url_for_logs(proxy_url: str, password_replacement: str = "*****") -> str:
    """
    Return a log-safe proxy URL with any embedded password redacted.

    Supports URLs like:
      - http://user:pass@host:port
      - socks5://user:pass@host:port
    """
    if not proxy_url:
        return proxy_url
    try:
        parts = urlsplit(proxy_url)
        netloc = parts.netloc
        if "@" not in netloc:
            return proxy_url
        creds, hostport = netloc.rsplit("@", 1)
        if ":" not in creds:
            # username@host:port (no password present)
            return proxy_url
        user, _pwd = creds.split(":", 1)
        safe_netloc = f"{user}:{password_replacement}@{hostport}"
        return urlunsplit((parts.scheme, safe_netloc, parts.path, parts.query, parts.fragment))
    except Exception:
        # Fallback: best-effort masking of ":password@" part
        return re.sub(r":([^@/]+)@", f":{password_replacement}@", str(proxy_url))


def test_proxy_url(proxy_url: str, timeout: int = 5) -> bool:
    """
    Test if proxy is reachable (one quick request). Used before download to skip dead proxies.
    Returns True if proxy responds, False otherwise.
    """
    if not proxy_url:
        return False
    try:
        import requests
        proxies = {"http": proxy_url, "https": proxy_url}
        r = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=timeout)
        return r.status_code == 200
    except Exception:
        return False
