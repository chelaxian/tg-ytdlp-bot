"""Smoke test: HELPERS/porn keyword matchers (compiled once, trie) == the former per-call regexes.

Needs the bot environment (CONFIG/config.py, tldextract, TXT/porn_*.txt) — run on a bot host:
    venv/bin/python tests/smoke/test_u_porn_matchers.py
"""
import os
import random
import re
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from HELPERS import porn  # noqa: E402

ok = fail = 0


def check(name, cond, extra=""):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name} {extra}")
    else:
        fail += 1
        print(f"FAIL {name} {extra}")


# ---- legacy reference implementations (verbatim logic of the previous porn.py) ----
def legacy_text_pattern(keywords):
    kws = [re.escape(kw.lower()) for kw in keywords if kw.strip()]
    return re.compile(r"\b(" + "|".join(kws) + r")\b", flags=re.IGNORECASE)


def legacy_url_regex(raw_keyword):
    words = [re.escape(w) for w in raw_keyword.split() if w]
    if not words:
        return re.compile(r"a^")
    core = r"[^A-Za-z0-9]+".join(words)
    return re.compile(rf"(?<![A-Za-z0-9])(?:{core})(?![A-Za-z0-9])", flags=re.IGNORECASE)


kws = sorted(porn.PORN_KEYWORDS)
check("keywords loaded", len(kws) > 100, f"({len(kws)})")

t0 = time.perf_counter()
m = porn._get_keyword_matchers()
build_ms = (time.perf_counter() - t0) * 1000
check("matchers built", m.text_re is not None and m.url_re is not None, f"({build_ms:.0f} ms)")
check("matchers reused (no rebuild)", porn._get_keyword_matchers() is m)

old_text = legacy_text_pattern(kws)
old_url = [legacy_url_regex(k) for k in kws]

rnd = random.Random(1234)
sample = rnd.sample(kws, min(4000, len(kws))) + [k for k in kws if re.search(r"[^\w\s]", k)]
benign = ["funny cats compilation", "how to cook pasta at home", "official music video 4k",
          "my vacation in thailand vlog", "teen titans go full episode", "big bang theory s01e01",
          "minecraft speedrun world record", "лучшие моменты матча", "新闻 直播", "قناة الأخبار",
          "", "a", "🔞 video", "18+ only", "rated 18+", "s&m", "#nsfw #porn", "🥵🥵 hot day"]
texts = list(benign)
for k in sample:
    texts += [k, k.upper(), f"watch {k} now", f"x{k}y", f"{k}s", f"pre {k}_suffix", f"({k})"]

mismatch = [t for t in texts if bool(old_text.search(t)) != bool(m.text_re.search(t))]
check("text: same verdict as legacy regex", not mismatch, f"({len(texts)} texts)")
if mismatch:
    print("  e.g.", mismatch[:5])

urls = ["https://example.org/watch?v=abc123", "https://vk.com/video-123_456", "https://site.net/"]
for k in sample[:1500]:
    slug = re.sub(r"\s+", rnd.choice(["-", "_", "%20", "/", "+"]), k)
    urls += [f"https://host.net/v/{slug}", f"https://host.net/v/x{slug}", f"https://host.net/{slug}123",
             f"https://{slug}.host.net/"]
url_mismatch = []
for u in urls:
    ul = u.lower()
    if any(r.search(ul) for r in old_url) != bool(m.url_re.search(ul)):
        url_mismatch.append(u)
check("url: same verdict as legacy per-keyword regexes", not url_mismatch, f"({len(urls)} urls)")
if url_mismatch:
    print("  e.g.", url_mismatch[:5])

# ---- is_porn: speed + memoisation ----
porn._is_porn_cached.cache_clear()
long_desc = " ".join(rnd.choice(["video", "travel", "family", "cooking", "review", "music"]) for _ in range(800))
t0 = time.perf_counter()
r1 = porn.is_porn("https://vk.com/video-123_456", "Family trip", long_desc, None, tags="#travel", uploader="TripChannel")
first_ms = (time.perf_counter() - t0) * 1000
check("non-whitelisted clean url is fast (was ~5.5 s)", first_ms < 300 and r1 is False, f"({first_ms:.1f} ms)")
t0 = time.perf_counter()
r2 = porn.is_porn("https://vk.com/video-123_456", "Family trip", long_desc, None, tags="#travel", uploader="TripChannel")
check("repeat call is a cache hit", r2 is r1 and porn._is_porn_cached.cache_info().hits >= 1,
      f"({(time.perf_counter() - t0) * 1e6:.0f} us)")
check("list args (tags as list) work and are cached", porn.is_porn("https://vk.com/x", "t", "", None, tags=["#a", "#b"]) is False and porn.is_porn("https://vk.com/x", "t", "", None, tags="#a #b") is False and porn._is_porn_cached.cache_info().hits >= 2)

kw = next(k for k in kws if re.fullmatch(r"[a-z]{5,}", k))
check("keyword in title -> True", porn.is_porn("https://vk.com/video1", f"some {kw} clip", "") is True)
check("keyword in url -> True", porn.is_porn(f"https://vk.com/{kw}-clip", "", "") is True)
check("whitelisted domain -> False", porn.is_porn("https://www.youtube.com/watch?v=x", f"{kw}", "") is False)
pd = sorted(porn.PORN_DOMAINS)[0]
check("porn domain -> True", porn.is_porn(f"https://{pd}/video/1", "", "") is True)

# reload drops memoised verdicts and rebuilds matchers when the list object changes
porn.load_domain_lists()
check("load_domain_lists clears verdict cache", porn._is_porn_cached.cache_info().currsize == 0)
check("matchers rebuilt after reload", porn._get_keyword_matchers() is not m)

ok_d, expl = porn.check_porn_detailed(f"https://vk.com/{kw}", f"{kw}", "", None)
check("check_porn_detailed still explains", ok_d is True and kw in expl, f"({expl[:80]!r})")
ok_u, expl_u = porn.check_porn_detailed(f"https://vk.com/{kw}-x", "", "", None)
check("check_porn_detailed url hit", ok_u is True and "URL" in expl_u)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
