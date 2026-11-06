"""Offline: media cache (DATABASE/cache_db) and cached repost (HELPERS/cache_repost).

Each DB engine runs in its own subprocess (the DB modules initialise at import).
No Telegram: forward_messages is a fake. Needs CONFIG/config.py (run on the bot host).
Run: python tests/smoke/test_t_media_cache.py [repo_root]
"""
import os
import subprocess
import sys
import tempfile
import types

REPO = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else \
    str(__import__("pathlib").Path(__file__).resolve().parents[2])


def check(name, cond, detail=""):
    if not cond:
        raise AssertionError(f"FAIL {name}: {detail}")
    print(f"ok  {name}")


def child(engine, workdir):
    sys.path.insert(0, REPO)
    os.chdir(workdir)
    from CONFIG.config import Config
    Config.USE_FIREBASE = False
    Config.DB_ENGINE = engine
    Config.SQLITE_DB_PATH = os.path.join(workdir, "bot.sqlite3")
    Config.FIREBASE_CACHE_FILE = os.path.join(workdir, "dump.json")
    Config.BOT_NAME_FOR_USERS = "testbot"
    t = lambda n, c, d="": check(f"{engine}:{n}", c, d)

    import DATABASE.firebase_init as fi
    import DATABASE.cache_db as cdb

    # count backend round trips
    stats = {"get": 0, "update": 0, "sync": 0}
    if engine != "json":
        store = fi.get_sql_store()
        orig_get, orig_update = store.get, store.update

        def get(path=""):
            stats["get"] += 1
            return orig_get(path)

        def update(path, values):
            stats["update"] += 1
            return orig_update(path, values)
        store.get, store.update = get, update
    else:
        orig_sync = cdb._sync_local_cache_to_file

        def sync():
            stats["sync"] += 1
            return orig_sync()
        cdb._sync_local_cache_to_file = sync

    def reset():
        for k in stats:
            stats[k] = 0

    yt = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    yt_short = "https://youtu.be/dQw4w9WgXcQ"

    reset()
    cdb.save_to_video_cache(yt, "720p", [4242])
    if engine == "json":
        t("video_save_one_dump_rewrite", stats["sync"] == 1, stats)
    else:
        t("video_save_one_transaction", stats["update"] == 1, stats)
    t("video_hit", cdb.get_cached_message_ids(yt, "720p") == [4242], cdb.get_cached_message_ids(yt, "720p"))
    t("video_hit_other_youtube_form", cdb.get_cached_message_ids(yt_short, "720p") == [4242])
    cdb.save_to_video_cache(yt, "1080p", [1, 2, 3])
    t("split_video_ids", cdb.get_cached_message_ids(yt, "1080p") == [1, 2, 3])
    t("qualities", cdb.get_cached_qualities(yt) == {"720p", "1080p"}, cdb.get_cached_qualities(yt))
    t("miss_is_none", cdb.get_cached_message_ids(yt, "360p") is None)

    # a quality menu looks up many qualities: the URL nodes are read once
    if engine != "json":
        cdb.invalidate_media_cache_memo()
        reset()
        for q in ("144p", "240p", "360p", "480p", "720p", "1080p", "best", "mp3"):
            cdb.get_cached_message_ids(yt, q)
        cdb.get_cached_qualities(yt)
        t("menu_reads_memoized", stats["get"] <= 3, stats)

    cdb.save_to_video_cache(yt, "720p", [], clear=True)
    t("clear_visible_at_once", cdb.get_cached_message_ids(yt, "720p") is None)
    t("clear_keeps_other_quality", cdb.get_cached_message_ids(yt, "1080p") == [1, 2, 3])
    t("empty_ids_not_saved", cdb.save_to_video_cache(yt, "480p", []) is None and cdb.get_cached_message_ids(yt, "480p") is None)

    pl = "https://www.youtube.com/playlist?list=PL1234567890abcdef"
    reset()
    cdb.save_to_playlist_cache(pl, "720p", [1, 2, 3], [11, 12, 13],
                               video_urls_dict={2: "https://www.youtube.com/watch?v=aaaaaaaaaaa"})
    if engine == "json":
        t("playlist_save_one_dump_rewrite", stats["sync"] == 1, stats)
    else:
        t("playlist_save_one_transaction", stats["update"] == 1, stats)
    t("playlist_items", cdb.get_cached_playlist_videos(pl, "720p", [1, 2, 3, 4]) == {1: 11, 2: 12, 3: 13},
      cdb.get_cached_playlist_videos(pl, "720p", [1, 2, 3, 4]))
    t("playlist_item_as_video", cdb.get_cached_message_ids("https://youtu.be/aaaaaaaaaaa", "720p") == [12])
    cdb.save_to_playlist_cache(pl, "720p", [4], [21, 22])
    t("split_playlist_item_keeps_all_parts",
      cdb.get_cached_playlist_message_ids(pl, "720p", [4]) == {4: [21, 22]},
      cdb.get_cached_playlist_message_ids(pl, "720p", [4]))
    t("playlist_count", cdb.get_cached_playlist_count(pl, "720p", [1, 2, 3, 4, 5]) == 4)
    t("playlist_count_all", cdb.get_cached_playlist_count(pl, "720p") == 4)
    rounded = cdb._expand_quality_keys("721p")[-1]
    cdb.save_to_playlist_cache(pl, rounded, [9], [90])
    t("playlist_rounded_quality", rounded != "721p" and cdb.get_cached_playlist_videos(pl, "721p", [9]) == {9: 90},
      (rounded, cdb.get_cached_playlist_videos(pl, "721p", [9])))
    t("playlist_qualities", cdb.get_cached_playlist_qualities(pl) == {"720p", rounded}, cdb.get_cached_playlist_qualities(pl))
    cdb.remove_playlist_cache_entries(pl, "720p", [2])
    t("stale_item_removed", cdb.get_cached_playlist_videos(pl, "720p", [1, 2, 3]) == {1: 11, 3: 13})
    cdb.save_to_playlist_cache(pl, "720p", [], [], clear=True)
    t("playlist_clear", cdb.get_cached_playlist_count(pl, "720p", [1, 3, 4]) == 0)

    # ---- DUBS: a dubbed audio track is cached apart from the default audio
    t("dub_key", cdb.dub_cache_key("720p", "en-US") == "720p@en-US" and cdb.dub_cache_key("best", "de") == "best@de")
    t("dub_key_default_audio", cdb.dub_cache_key("720p", None) == "720p" and cdb.dub_cache_key("720p", "ALL") == "720p"
      and cdb.dub_cache_key("720p", "OFF") == "720p")
    t("dub_key_not_for_mp3_or_format_ids", cdb.dub_cache_key("mp3", "en") == "mp3"
      and cdb.dub_cache_key("other_id|399", "en") == "other_id|399")
    t("dub_key_sanitized", cdb.dub_cache_key("720p", "en.US/x") == "720p@enUSx")
    t("dub_split", cdb.split_dub_cache_key("720p@en-US") == ("720p", "en-US") and cdb.split_dub_cache_key("mp3") == ("mp3", None))
    fmt = ("bv*[vcodec*=avc1][height<=720][height>480]+ba[language^=en-US]/bv*[vcodec*=avc1][height<=720]+ba[language^=en-US]"
           "/bv*[vcodec*=avc1]+ba[language^=en-US]/bv+ba/best")
    t("dub_from_format", cdb.audio_lang_from_format(fmt) == "en-US" and cdb.audio_lang_from_format("bv*+ba/best") is None
      and cdb.audio_lang_from_format(None) is None)
    t("dub_expand_keeps_suffix", cdb._expand_quality_keys("721p@de")[0] == "721p@de"
      and cdb._expand_quality_keys("721p@de")[-1] == cdb._expand_quality_keys("721p")[-1] + "@de")

    dv = "https://www.youtube.com/watch?v=bbbbbbbbbbb"
    cdb.save_to_video_cache(dv, "720p", [500])                                    # original audio
    cdb.save_to_video_cache(dv, cdb.dub_cache_key("720p", "en-US"), [501])        # English dub
    cdb.save_to_video_cache(dv, "mp3", [502])
    t("dub_original_kept", cdb.get_cached_message_ids(dv, "720p") == [500])
    t("dub_separate_entry", cdb.get_cached_message_ids(dv, cdb.dub_cache_key("720p", "en-US")) == [501])
    t("dub_other_lang_misses", cdb.get_cached_message_ids(dv, cdb.dub_cache_key("720p", "de-DE")) is None)
    allq = cdb.get_cached_qualities(dv)
    t("menu_original_audio", cdb.qualities_for_audio(allq, None) == {"720p", "mp3"}, cdb.qualities_for_audio(allq, None))
    t("menu_dub_en", cdb.qualities_for_audio(allq, "en-US") == {"720p", "mp3"}, cdb.qualities_for_audio(allq, "en-US"))
    t("menu_dub_de_no_rocket_for_720p", cdb.qualities_for_audio(allq, "de-DE") == {"mp3"}, cdb.qualities_for_audio(allq, "de-DE"))
    pl2 = "https://www.youtube.com/playlist?list=PLdubdubdubdub0001"
    cdb.save_to_playlist_cache(pl2, cdb.dub_cache_key("720p", "en-US"), [1], [601])
    cdb.save_to_playlist_cache(pl2, "720p", [1], [600])
    t("dub_playlist_separate", cdb.get_cached_playlist_videos(pl2, "720p", [1]) == {1: 600}
      and cdb.get_cached_playlist_videos(pl2, "720p@en-US", [1]) == {1: 601})
    t("dub_playlist_menu", cdb.qualities_for_audio(cdb.get_cached_playlist_qualities(pl2), "en-US") == {"720p"}
      and cdb.qualities_for_audio(cdb.get_cached_playlist_qualities(pl2), None) == {"720p"})

    # menu helpers of always_ask_menu (module too heavy to import: run their source)
    import ast
    src = open(os.path.join(REPO, "DOWN_AND_UP", "always_ask_menu.py"), encoding="utf-8").read()
    want = {"_cache_audio_lang", "_user_cache_key", "_user_cached_qualities"}
    code = "\n\n".join(ast.get_source_segment(src, n) for n in ast.parse(src).body
                       if isinstance(n, ast.FunctionDef) and n.name in want)
    filters = {}
    dubs_mod = types.ModuleType("COMMANDS.dubs_cmd")
    dubs_pref = {"lang": None}

    def apply_dubs_preference(uid, fstate):
        if dubs_pref["lang"] and not fstate.get("audio_lang"):
            fstate["audio_lang"] = dubs_pref["lang"]
        return fstate
    dubs_mod.apply_dubs_preference = apply_dubs_preference
    saved_dubs = sys.modules.get("COMMANDS.dubs_cmd")
    sys.modules["COMMANDS.dubs_cmd"] = dubs_mod
    ns = {"get_filters": lambda uid: filters, "dub_cache_key": cdb.dub_cache_key,
          "qualities_for_audio": cdb.qualities_for_audio, "get_cached_qualities": cdb.get_cached_qualities}
    exec(code, ns)
    t("menu_helper_default", ns["_user_cache_key"](1, "720p") == "720p" and ns["_user_cached_qualities"](dv, 1) == {"720p", "mp3"})
    filters["audio_lang"] = "de-DE"
    t("menu_helper_dub_de", ns["_user_cache_key"](1, "720p") == "720p@de-DE" and ns["_user_cached_qualities"](dv, 1) == {"mp3"})
    filters["audio_lang"] = "ALL"
    t("menu_helper_all_is_default", ns["_user_cache_key"](1, "720p") == "720p")
    filters["audio_lang"] = None
    dubs_pref["lang"] = "en-US"
    t("menu_helper_dubs_preference", ns["_user_cache_key"](1, "best") == "best@en-US" and filters.get("audio_lang") is None,
      filters)
    if saved_dubs is not None:
        sys.modules["COMMANDS.dubs_cmd"] = saved_dubs
    else:
        sys.modules.pop("COMMANDS.dubs_cmd", None)

    img = "https://example.com/gallery/1"
    cdb.save_to_image_cache(img, 1, [5, 6])
    cdb.save_to_image_cache(img, 2, [7])
    t("image_posts", cdb.get_cached_image_posts(img) == {1: [5, 6], 2: [7]}, cdb.get_cached_image_posts(img))
    t("image_indices", cdb.get_cached_image_post_indices(img) == {1, 2})
    cdb.save_to_image_cache(img, 1, [99])
    t("image_entry_kept", cdb.get_cached_image_posts(img, [1]) == {1: [5, 6]})

    if engine == "json":
        import json
        with open(Config.FIREBASE_CACHE_FILE, encoding="utf-8") as f:
            disk = json.load(f)
        h = cdb.get_url_hash(__import__("URL_PARSERS.normalizer", fromlist=["x"]).normalize_url_for_cache(yt))
        t("json_persisted", disk["bot"]["video_cache"][h]["1080p"] == "1,2,3", disk["bot"]["video_cache"].get(h))
    print("CHILD OK")


# ---------------------------------------------------------------- repost (no DB)
class MessageIdInvalid(Exception):
    pass


class UserIsBlocked(Exception):
    pass


class FakeApp:
    def __init__(self, existing, blocked=False):
        self.existing = set(existing)
        self.calls = []
        self.blocked = blocked

    def forward_messages(self, chat_id, from_chat_id, message_ids, message_thread_id=None):
        self.calls.append(list(message_ids))
        if self.blocked:
            raise UserIsBlocked("USER_IS_BLOCKED")
        alive = [m for m in message_ids if m in self.existing]
        if not alive:
            raise MessageIdInvalid("[400 MESSAGE_ID_INVALID]")
        return [types.SimpleNamespace(id=1000 + m, forward_origin=types.SimpleNamespace(message_id=m))
                for m in sorted(alive)]


def repost_tests():
    sys.path.insert(0, REPO)
    try:
        from HELPERS import cache_repost as cr
    except Exception as e:  # HELPERS.logger needs the bot config
        print(f"skip repost tests: {type(e).__name__}: {e}")
        return
    t = lambda n, c, d="": check(f"repost:{n}", c, d)

    app = FakeApp(range(1, 300))
    d, dead, failed = cr.forward_cached(app, 1, -100, list(range(1, 251)))
    t("batches_of_100", [len(c) for c in app.calls] == [100, 100, 50], [len(c) for c in app.calls])
    t("all_delivered", d == list(range(1, 251)) and not dead and not failed)

    app = FakeApp(range(1, 10))
    cr.forward_cached(app, 1, -100, [5, 4, 3])
    t("reverse_order_one_by_one", app.calls == [[5], [4], [3]], app.calls)

    app = FakeApp([1, 3])
    d, dead, failed = cr.forward_cached(app, 1, -100, [1, 2, 3])
    t("deleted_id_in_batch_detected", d == [1, 3] and dead == [2] and not failed, (d, dead, failed))
    t("deleted_id_single_request", len(app.calls) == 1, app.calls)

    app = FakeApp([])
    d, dead, failed = cr.forward_cached(app, 1, -100, [7, 8])
    t("all_deleted", d == [] and dead == [7, 8], (d, dead, failed))

    app = FakeApp([1, 2], blocked=True)
    ok, stale = cr.repost_single(app, 1, -100, [1, 2])
    t("blocked_user_keeps_cache", ok is False and stale is False and len(app.calls) == 1, (ok, stale, app.calls))

    app = FakeApp([11, 13, 21, 22])
    stale, undelivered = cr.repost_playlist_items(app, 1, -100, [1, 2, 3, 4], {1: 11, 2: 12, 3: 13, 4: [21, 22]})
    t("playlist_stale_index", stale == [2] and undelivered == [2], (stale, undelivered))
    t("playlist_one_request", app.calls == [[11, 12, 13, 21, 22]], app.calls)

    app = FakeApp([1, 2])
    ok, stale = cr.repost_single(app, 1, -100, [1, 2, 3])
    t("missing_part_is_stale", ok is False and stale is True)
    ok, stale = cr.repost_single(FakeApp([1, 2]), 1, -100, [1, 2])
    t("full_repost_ok", ok is True and stale is False)


if __name__ == "__main__":
    if len(sys.argv) > 3 and sys.argv[2] == "--child":
        child(sys.argv[3], sys.argv[4])
        sys.exit(0)
    failed = 0
    for engine in ("sqlite", "json"):
        with tempfile.TemporaryDirectory() as wd:
            r = subprocess.run([sys.executable, __file__, REPO, "--child", engine, wd],
                               capture_output=True, text=True, timeout=300)
            out = "\n".join(l for l in r.stdout.splitlines() if l.startswith(("ok ", "CHILD", "FAIL")))
            print(out)
            if r.returncode or "CHILD OK" not in r.stdout:
                failed += 1
                print(r.stdout[-3000:], r.stderr[-3000:])
    repost_tests()
    print("ALL OK" if not failed else f"{failed} engine(s) FAILED")
    sys.exit(1 if failed else 0)
