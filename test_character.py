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

    def test_character_has_stats(self):
        from character import Character
        char = Character(
            name="Gimli",
            strength=10,
            dexterity=12,
            constitution=14,
            intelligence=8,
            wisdom=10,
            charisma=9
        )
        self.assertEqual(char.strength, 10)
        self.assertEqual(char.dexterity, 12)
        self.assertEqual(char.constitution, 14)
        self.assertEqual(char.intelligence, 8)
        self.assertEqual(char.wisdom, 10)
        self.assertEqual(char.charisma, 9)

    def test_stats_must_be_in_valid_range(self):
        from character import Character
        with self.assertRaises(ValueError):
            Character(name="BadChar", strength=2)

        with self.assertRaises(ValueError):
            Character(name="BadChar", strength=19)


if __name__ == "__main__":
    unittest.main()