"""Regression: real site 403 (Cloudflare-like) must NOT be classified as an
unavailable impersonate target (logaudit 2026-11-10, HELPERS/proxy_helper.py).

With curl_cffi installed, `available_specific_impersonate_targets()` already
returns targets yt-dlp CAN impersonate. Treating a site's HTTP 403 as
"target unavailable" aborted the whole fallback chain after 3 tries and logged
a false "specific browser versions are unavailable / reinstall curl_cffi"
diagnosis. AST-isolated real function body, no app imports, no network.
"""
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import Mock

R = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R))


def functions(path, names, env):
    import ast
    tree = ast.parse((R / path).read_text(encoding="utf-8-sig"))
    selected = [n for n in ast.walk(tree)
                if isinstance(n, ast.FunctionDef) and n.name in names]
    exec(compile(ast.fix_missing_locations(
        ast.Module(body=selected, type_ignores=[])), str(path), "exec"), env)
    return env


def _build_env():
    env = functions("HELPERS/proxy_helper.py", ["try_with_impersonate_fallback"], {})
    env["logger"] = Mock()
    env["available_specific_impersonate_targets"] = lambda limit=24: [
        "chrome-152", "edge-101", "firefox-155", "safari-18.4"]
    # is_cloudflare_error is also extracted so the real pair is tested together
    env2 = functions("HELPERS/proxy_helper.py", ["is_cloudflare_error"], {})
    env["is_cloudflare_error"] = env2["is_cloudflare_error"]
    # Stub curl_cffi so the function takes the "curl_cffi available" branch
    fake = types.ModuleType("curl_cffi")
    fake_dict = types.ModuleType("curl_cffi").__dict__
    fake_dict["__version__"] = "0.17.0-test"

    class FakeCurl:
        def close(self):
            pass

    fake_dict["Curl"] = FakeCurl
    sys.modules.setdefault("curl_cffi", fake)
    return env


class ImpersonateFallback403Tests(unittest.TestCase):
    def test_site_403_not_counted_as_unavailable(self):
        env = _build_env()
        fn = env["try_with_impersonate_fallback"]
        logger = env["logger"]
        calls = []

        def operation_func(opts, url=None, *a, **kw):
            calls.append(opts.get("extractor_args", {}).get("generic", {}).get("impersonate"))
            raise Exception("ERROR: Unable to download webpage: HTTP Error 403: Forbidden")

        result = fn({}, "https://example.test/video", user_id=1,
                    operation_func=operation_func)
        self.assertIsNone(result)
        # every version in the chain was actually tried (no early abort)
        self.assertGreaterEqual(len(calls), 8)
        # no false "STOPPING ... unavailable" abort
        logged = " ".join(str(c.args[0]) for c in logger.error.call_args_list
                          if c.args)
        self.assertNotIn("STOPPING", logged)
        self.assertNotIn("specific browser versions are unavailable", logged)
        # and the final diagnosis must not claim curl_cffi is broken
        self.assertNotIn("needs to be updated or reinstalled", logged)

    def test_explicit_unavailable_still_aborts(self):
        env = _build_env()
        fn = env["try_with_impersonate_fallback"]
        logger = env["logger"]

        def operation_func(opts, url=None, *a, **kw):
            raise Exception("WARNING: none of these impersonate targets are available")

        result = fn({}, "https://example.test/video", user_id=1,
                    operation_func=operation_func, skip_original_attempt=True)
        self.assertIsNone(result)
        logged = " ".join(str(c.args[0]) for c in logger.error.call_args_list
                          if c.args)
        self.assertIn("STOPPING", logged)

    def test_ssl_transport_error_still_counted(self):
        env = _build_env()
        fn = env["try_with_impersonate_fallback"]
        logger = env["logger"]

        def operation_func(opts, url=None, *a, **kw):
            raise Exception("ERROR: Unable to download webpage: curl: (60) SSL certificate problem")

        result = fn({}, "https://example.test/video", user_id=1,
                    operation_func=operation_func, skip_original_attempt=True)
        self.assertIsNone(result)
        logged = " ".join(str(c.args[0]) for c in logger.error.call_args_list
                          if c.args)
        self.assertIn("STOPPING", logged)


if __name__ == "__main__":
    unittest.main()
