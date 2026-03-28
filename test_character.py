import unittest


class TestCharacter(unittest.TestCase):

    def test_character_creation_with_name(self):
        from character import Character
        char = Character(name="Aragorn")
        self.assertEqual(char.name, "Aragorn")

    def test_character_has_race_and_class(self):
        from character import Character
        char = Character(name="Legolas", race="Elf", character_class="Rogue")
        self.assertEqual(char.race, "Elf")
        self.assertEqual(char.character_class, "Rogue")


if __name__ == "__main__":
    unittest.main()