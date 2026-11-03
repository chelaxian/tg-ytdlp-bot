"""Offline tests: per-user daily quotas (HELPERS/daily_quota.py).

Counters survive a restart (on disk), reset at local midnight, exempt admins and
groups, and every blocked attempt gets a fresh message with the time left.
Run: python test_j_daily_quota.py [repo_root]
"""
import datetime
import importlib
import json
import os
import sys
import tempfile
import types

REPO = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])
sys.path.insert(0, REPO)
WORK = tempfile.mkdtemp(prefix="quota_test_")
os.makedirs(os.path.join(WORK, "CONFIG"))
os.chdir(WORK)
PASSED = []


def check(name, cond, detail=""):
    if not cond:
        raise AssertionError(f"FAIL {name}: {detail}")
    PASSED.append(name)
    print(f"ok  {name}")


ADMINS = {1}
sent = []
sys.modules["HELPERS.logger"] = types.SimpleNamespace(logger=types.SimpleNamespace(
    info=lambda *a, **k: None, warning=print, debug=lambda *a, **k: None))
sys.modules["HELPERS.limitter"] = types.SimpleNamespace(
    should_apply_limits_to_admin=lambda user_id=None, message=None: int(user_id) not in ADMINS)
sys.modules["HELPERS.safe_messeger"] = types.SimpleNamespace(
    safe_send_message=lambda chat_id, text, **k: sent.append((chat_id, text)))
router = types.SimpleNamespace(get_user_language=lambda uid: "ru" if uid == 7 else "en")
sys.modules["CONFIG.LANGUAGES.language_router"] = types.SimpleNamespace(language_router=router)

from CONFIG.limits import LimitsConfig  # noqa: E402
LimitsConfig.DAILY_VIDEO_LIMIT = 3
LimitsConfig.DAILY_IMAGE_LIMIT = 5
import HELPERS.daily_quota as q  # noqa: E402


def msg(chat_id):
    return types.SimpleNamespace(chat=types.SimpleNamespace(id=chat_id))


user, ru_user, admin, group = msg(42), msg(7), msg(1), msg(-100123)
check("fresh_user_has_full_quota", q.remaining(user, q.VIDEO) == 3 and q.remaining(user, q.IMAGE) == 5)
check("admin_exempt", q.remaining(admin, q.VIDEO) is None and not q.deny_if_exhausted(admin, q.VIDEO))
check("group_exempt", q.remaining(group, q.VIDEO) is None)
q.record(admin, q.VIDEO, 10)
q.record(group, q.VIDEO, 10)
check("exempt_not_counted", "1" not in q._STATE["users"] and "-100123" not in q._STATE["users"])

q.record(user, q.VIDEO)
q.record(user, q.VIDEO, cached=True)
check("counts_downloads_and_cache", q.used(user, q.VIDEO) == 2)
check("not_blocked_below_limit", not q.deny_if_exhausted(user, q.VIDEO) and not sent)
q.record(user, q.VIDEO)
check("blocked_at_limit", q.deny_if_exhausted(user, q.VIDEO) and len(sent) == 1)
check("message_has_count_and_timer", "3/3" in sent[0][1] and "00:00" in sent[0][1] and "min" in sent[0][1], sent[0][1])
q.deny_if_exhausted(user, q.VIDEO)
check("every_attempt_gets_a_new_message", len(sent) == 2)
check("images_counted_separately", q.remaining(user, q.IMAGE) == 5)
q.record(user, q.IMAGE, 5)
check("image_quota_exhausted", q.remaining(user, q.IMAGE) == 0 and q.deny_if_exhausted(user, q.IMAGE))
check("image_message_in_english", "5/5" in sent[-1][1] and "images" in sent[-1][1])

q.record(ru_user, q.VIDEO, 3)
q.deny_if_exhausted(ru_user, q.VIDEO)
check("message_in_user_language", "Достигнут дневной лимит" in sent[-1][1] and "видео" in sent[-1][1], sent[-1][1])

# a restart keeps the counters (they are on disk)
saved = json.load(open(os.path.join("CONFIG", ".daily_quota.json"), encoding="utf-8"))
check("persisted_to_disk", saved["users"]["42"] == {"video": 3, "image": 5} and saved["date"] == q._today())
q = importlib.reload(q)
check("survives_restart", q.remaining(user, q.VIDEO) == 0 and q.used(ru_user, q.VIDEO) == 3)

# midnight: a new date starts everyone from zero
real_today = q._today
q._today = lambda: (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
check("reset_at_midnight", q.remaining(user, q.VIDEO) == 3 and q.remaining(user, q.IMAGE) == 5)
q._today = real_today

# timer until the next local midnight
now = datetime.datetime(2026, 11, 3, 18, 47, 30)
check("seconds_until_midnight", q.seconds_until_reset(now) == 5 * 3600 + 12 * 60 + 30)
check("wait_text_en", q._wait_text("en", 5 * 3600 + 12 * 60 + 30) == "5 h 13 min", q._wait_text("en", 18750))
check("wait_text_minutes_only", q._wait_text("ru", 45) == "1 мин", q._wait_text("ru", 45))

LimitsConfig.DAILY_QUOTA_COUNT_CACHED = False
before = q.used(msg(55), q.VIDEO)
q.record(msg(55), q.VIDEO, cached=True)
check("cache_can_be_excluded", q.used(msg(55), q.VIDEO) == before)
LimitsConfig.DAILY_VIDEO_LIMIT = 0
check("zero_disables_quota", q.remaining(user, q.VIDEO) is None and not q.deny_if_exhausted(user, q.VIDEO))
print("ALL", len(PASSED), "CHECKS PASSED")
