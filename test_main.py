import io
import unittest
from unittest.mock import patch

import main


class TestMain(unittest.TestCase):

    def test_menu_exit_option_finishes_program(self):
        user_input = ["3"]
        output = io.StringIO()

        with patch("builtins.input", side_effect=user_input), patch("sys.stdout", new=output):
            main.run()

        printed = output.getvalue()
        self.assertIn("1. Create character", printed)
        self.assertIn("3. Exit", printed)
        self.assertIn("Goodbye!", printed)


if __name__ == "__main__":
    unittest.main()