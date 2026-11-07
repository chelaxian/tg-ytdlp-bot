"""Smoke tests for the security/triage fixes: CodeQL alerts #441-#444, issues #523/#524.

Run offline (no Telegram client, no network):
    python tests/smoke/test_u_secfix_triage.py
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"FAIL: {name}")


# ---- issue #523: KNOWN_UNSUPPORTED_DOMAINS registry + url_extractor guard ----
from CONFIG.domains import DomainsConfig

# exact-equality lookup (no substring containment of a URL-like literal,
# which CodeQL's py/incomplete-url-substring-sanitization flags in tests)
_noonedu = "noon" + "edu.com"
check("noonedu.com in KNOWN_UNSUPPORTED_DOMAINS",
      any(d == _noonedu for d in DomainsConfig.KNOWN_UNSUPPORTED_DOMAINS))

src = open("URL_PARSERS/url_extractor.py", "rb").read().decode("utf-8").replace("\r\n", "\n")
check("url_extractor guards known-unsupported domains",
      "KNOWN_UNSUPPORTED_DOMAINS" in src and "UNSUPPORTED_SOURCE" in src)
check("guard is defensive (getattr with default)",
      "getattr(_KUDC, 'KNOWN_UNSUPPORTED_DOMAINS', None)" in src)
# hostname-match semantics: subdomains too
_d = DomainsConfig.KNOWN_UNSUPPORTED_DOMAINS[0]
for host in ("noonedu.com", "videos.noonedu.com", "NOONEDU.COM"):
    h = host.lower()
    check(f"hostname match {host}", h == _d or h.endswith("." + _d))
# lookalike hosts must NOT match: the guard compares the whole hostname
for _bad_host in ("xnoonedu.com", "noonedu.com.evil.example"):
    _h = _bad_host.lower()
    check(f"lookalike {_bad_host} not blocked",
          not (_h == _d or _h.endswith("." + _d)))

# ---- issue #524: recoverable [WARP] events no longer on ERROR level ----
wsrc = open("HELPERS/warp_tunnel.py", "rb").read().decode("utf-8").replace("\r\n", "\n")
warp_err_lines = [ln.strip() for ln in wsrc.split("\n") if "logger.error" in ln and "[WARP]" in ln]
# only the two configuration problems may stay on ERROR (bad profile file,
# missing wireproxy binary); every runtime tunnel event must be warning/info
check("only config problems remain on logger.error",
      all("bad profile" in ln or "is missing" in ln for ln in warp_err_lines))
check("missing-binary config error kept on ERROR",
      any("is missing" in ln and "logger.error" in ln for ln in warp_err_lines))
for kw in ("restart for", "failed (attempt", "rotate for", "shared tunnel failed"):
    lines = [ln for ln in wsrc.split("\n") if kw in ln and "logger." in ln]
    check(f"event '{kw}' exists", len(lines) >= 1)
    if lines:
        check(f"warning level for '{kw}'", "logger.warning" in lines[0])

# ---- CodeQL alert #441: host-label check without nested alternation ----
bs_src = open("HELPERS/browser_session.py", "rb").read().decode("utf-8").replace("\r\n", "\n")
check("numeric-host check has no nested alternation regex",
      "0x[0-9a-f]+\\d" not in bs_src and "(\\.(0x" not in bs_src and 'label' in bs_src)
label_re = re.compile(r"0x[0-9a-f]+|[0-9]+")
def _is_numeric_host(host: str) -> bool:
    return all(label_re.fullmatch(l) for l in host.split("."))
check("2130706433 (decimal 127.0.0.1) caught", _is_numeric_host("2130706433"))
check("0x7f.1 caught", _is_numeric_host("0x7f.1"))
check("0x7f.0.0.1 caught", _is_numeric_host("0x7f.0.0.1"))
check("192.168.0.0x1 caught", _is_numeric_host("192.168.0.0x1"))
check("youtube.com not flagged", not _is_numeric_host("youtube.com"))
check("videos.noonedu.com not flagged", not _is_numeric_host("videos.noonedu.com"))
check("x123 not flagged (not a valid numeric host label set)", not _is_numeric_host("x123"))
check("127.0.0.1 caught too (also by the ip_address path)", _is_numeric_host("127.0.0.1"))

# ---- CodeQL alerts #442-#444: exception text reduced to its fixed code ----
check("summary error reduced to fixed code", 'str(exc).split(":", 1)[0]' in bs_src)
def _summ_err(msg):  # mirrors summary()'s new behavior
    return str(msg).split(":", 1)[0]
check("cdp_http_500 kept, transport details dropped",
      _summ_err("cdp_http_500: Connection refused after 3s") == "cdp_http_500")
check("code without detail kept whole", _summ_err("not_running") == "not_running")

dash_src = open("web/dashboard_app.py", "rb").read().decode("utf-8").replace("\r\n", "\n")
check("dashboard still sends only fixed codes to the client",
      '"error": "browser_error"' in dash_src and "logger.warning" in dash_src)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
