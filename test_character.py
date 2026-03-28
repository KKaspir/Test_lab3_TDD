import unittest


class TestCharacter(unittest.TestCase):

    def test_character_creation_with_name(self):
        from character import Character
        char = Character(name="Aragorn")
        self.assertEqual(char.name, "Aragorn")


if __name__ == "__main__":
    unittest.main()