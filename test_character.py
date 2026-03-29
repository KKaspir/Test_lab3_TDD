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

    def test_get_modifier(self):
        from character import Character
        char = Character(name="Test", strength=14)
        self.assertEqual(char.get_modifier(char.strength), 2)

        char = Character(name="Test", strength=9)
        self.assertEqual(char.get_modifier(char.strength), -1)

    def test_roll_stats_fills_all_attributes_in_range(self):
        from character import Character
        char = Character(name="RandomHero")
        char.roll_stats()
        stats = [
            char.strength, char.dexterity, char.constitution,
            char.intelligence, char.wisdom, char.charisma
        ]
        for stat in stats:
            self.assertTrue(3 <= stat <= 18)

    def test_human_gets_plus_one_to_all_stats(self):
        from character import Character
        char = Character(
            name="HumanHero",
            race="Human",
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10
        )
        self.assertEqual(char.strength, 11)
        self.assertEqual(char.dexterity, 11)
        self.assertEqual(char.constitution, 11)
        self.assertEqual(char.intelligence, 11)
        self.assertEqual(char.wisdom, 11)
        self.assertEqual(char.charisma, 11)

    def test_elf_gets_plus_two_to_dexterity(self):
        from character import Character
        char = Character(
            name="Legolas",
            race="Elf",
            dexterity=10
        )
        self.assertEqual(char.dexterity, 12)

    def test_dwarf_gets_plus_two_to_constitution(self):
        from character import Character
        char = Character(
            name="Gimli",
            race="Dwarf",
            constitution=10
        )
        self.assertEqual(char.constitution, 12)


if __name__ == "__main__":
    unittest.main()