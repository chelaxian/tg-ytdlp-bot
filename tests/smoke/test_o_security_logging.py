"""Regression guards for credential logging and the list-download address filter.

Run: python tests/smoke/test_o_security_logging.py   (offline, no bot config needed)
"""
import ast
import ipaddress
import sys
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

# names whose full value can carry proxy credentials
SECRET_NAMES = {"proxy_url", "proxy_config"}
SECRET_ATTRS = {"PROXY_PASSWORD", "PROXY_2_PASSWORD", "PROXY_USER", "PROXY_2_USER", "BOT_TOKEN", "API_HASH"}
LOG_METHODS = {"debug", "info", "warning", "error", "exception", "critical"}


def _is_log_call(node):
    f = node.func
    return (isinstance(f, ast.Attribute) and f.attr in LOG_METHODS
            and isinstance(f.value, ast.Name) and f.value.id in {"logger", "logging", "log"}) or \
           (isinstance(f, ast.Name) and f.id == "print")


def _leaks(expr):
    """Names/attributes that reach the log line as a whole value."""
    found = []
    for node in ast.walk(expr):
        if isinstance(node, ast.FormattedValue):
            value = node.value
            if isinstance(value, ast.Name) and value.id in SECRET_NAMES:
                found.append(value.id)
            if isinstance(value, ast.Attribute) and value.attr in SECRET_ATTRS:
                found.append(value.attr)
        if isinstance(node, ast.keyword) and isinstance(node.value, ast.Name) and node.value.id in SECRET_NAMES:
            found.append(node.value.id)
    return found


class CredentialLogging(unittest.TestCase):
    def test_no_log_call_prints_proxy_credentials(self):
        offenders = []
        for path in ROOT.rglob("*.py"):
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith(("venv/", "tests/", ".git/")):
                continue
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"))
            except (SyntaxError, UnicodeDecodeError):
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and _is_log_call(node):
                    for name in _leaks(node):
                        offenders.append(f"{rel}:{node.lineno} {name}")
        self.assertEqual(offenders, [], "\n".join(offenders))

    def test_detector_catches_the_old_patterns(self):
        old = 'logger.info(f"Force using proxy for audio download: {proxy_url}")'
        self.assertEqual(_leaks(ast.parse(old).body[0].value), ["proxy_url"])
        old = 'logger.info(MSG.format(proxy_url=proxy_url))'
        self.assertEqual(_leaks(ast.parse(old).body[0].value), ["proxy_url"])
        safe = 'logger.info(f"proxy: {proxy_config.get(\'ip\')}:{proxy_config.get(\'port\')}")'
        self.assertEqual(_leaks(ast.parse(safe).body[0].value), [])


class AddressFilter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cfg = types.ModuleType("CONFIG.config")
        cfg.Config = type("Config", (), {"PORN_DOMAINS_FILE": "x", "PORN_KEYWORDS_FILE": "y", "SUPPORTED_SITES_FILE": "z"})
        sys.modules.setdefault("CONFIG.config", cfg)
        from services import lists_service
        cls.ls = lists_service

    def test_internal_addresses_blocked(self):
        for a in ["127.0.0.1", "::1", "::ffff:127.0.0.1", "::ffff:10.1.2.3", "10.0.0.5", "192.168.1.1",
                  "169.254.169.254", "100.64.0.1", "fd00::1", "fe80::1", "0.0.0.0", "224.0.0.1"]:
            with self.subTest(a=a):
                self.assertTrue(self.ls._bad_ip(ipaddress.ip_address(a)))

    def test_public_addresses_allowed(self):
        for a in ["8.8.8.8", "1.1.1.1", "2606:4700:4700::1111", "140.82.112.3"]:
            with self.subTest(a=a):
                self.assertFalse(self.ls._bad_ip(ipaddress.ip_address(a)))

    def test_rejected_url_never_connects(self):
        import socket
        from unittest import mock
        with mock.patch.object(socket, "getaddrinfo", return_value=[(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("127.0.0.1", 80))]), \
             mock.patch.object(socket, "socket") as sock:
            with self.assertRaises(self.ls.ListError):
                self.ls._download_text("http://rebind.example/list.txt")
            sock.assert_not_called()

    def test_credentials_in_url_rejected(self):
        with self.assertRaises(self.ls.ListError):
            self.ls._download_text("https://user:pass@example.com/list.txt")

    def test_first_invalid_item(self):
        self.assertEqual(self.ls.first_invalid_item("WHITELIST", ["ok.com", 'bad"x']), 'bad"x')
        self.assertIsNone(self.ls.first_invalid_item("WHITELIST", ["ok.com"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
