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

    def test_show_sheet_without_character_displays_message(self):
        user_input = ["2", "3"]
        output = io.StringIO()

        with patch("builtins.input", side_effect=user_input), patch("sys.stdout", new=output):
            main.run()

        printed = output.getvalue()
        self.assertIn("No character created yet.", printed)

    def test_create_character_and_show_sheet(self):
        user_input = [
            "1",
            "Aragorn",
            "Human",
            "Fighter",
            "2",
            "3"
        ]
        output = io.StringIO()

        with patch("builtins.input", side_effect=user_input), \
             patch("sys.stdout", new=output), \
             patch("character.Character.roll_stats", autospec=True) as mocked_roll:
            mocked_roll.side_effect = self._set_fixed_stats
            main.run()

        printed = output.getvalue()
        self.assertIn("Character created!", printed)
        self.assertIn("Name: Aragorn", printed)
        self.assertIn("Race: Human", printed)
        self.assertIn("Class: Fighter", printed)

    @staticmethod
    def _set_fixed_stats(character_instance):
        character_instance.strength = 15
        character_instance.dexterity = 12
        character_instance.constitution = 14
        character_instance.intelligence = 10
        character_instance.wisdom = 13
        character_instance.charisma = 11


if __name__ == "__main__":
    unittest.main()