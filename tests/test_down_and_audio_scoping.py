import os
import sys
import unittest


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)


class TestDownAndAudioScoping(unittest.TestCase):
    def test_send_error_to_user_is_not_local_in_down_and_audio(self) -> None:
        """
        Regression test:
        If `down_and_audio()` contains an in-function import/assignment of
        `send_error_to_user`, Python will treat it as a local, and nested helpers
        can crash with: "free variable 'send_error_to_user' referenced before assignment".
        """
        from DOWN_AND_UP import down_and_audio as mod

        locals_ = set(mod.down_and_audio.__code__.co_varnames)
        self.assertNotIn("send_error_to_user", locals_)


if __name__ == "__main__":
    unittest.main()

