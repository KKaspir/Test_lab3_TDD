import random

class Character:
    def __init__(
        self,
        name,
        race=None,
        character_class=None,
        strength=None,
        dexterity=None,
        constitution=None,
        intelligence=None,
        wisdom=None,
        charisma=None
    ):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.strength = self._validate_stat(strength)
        self.dexterity = self._validate_stat(dexterity)
        self.constitution = self._validate_stat(constitution)
        self.intelligence = self._validate_stat(intelligence)
        self.wisdom = self._validate_stat(wisdom)
        self.charisma = self._validate_stat(charisma)
        self._apply_race_bonus()

    def _validate_stat(self, value):
        if value is None:
            return value
        if value < 3 or value > 18:
            raise ValueError("Stat must be between 3 and 18")
        return value

    def _apply_race_bonus(self):
        race_bonuses = {
            "Human": {
                "strength": 1,
                "dexterity": 1,
                "constitution": 1,
                "intelligence": 1,
                "wisdom": 1,
                "charisma": 1,
            },
            "Elf": {
                "dexterity": 2,
            },
            "Dwarf": {
                "constitution": 2,
            }
        }

        bonuses = race_bonuses.get(self.race, {})
        for stat_name, bonus in bonuses.items():
            current_value = getattr(self, stat_name)
            if current_value is not None:
                setattr(self, stat_name, current_value + bonus)

    def get_modifier(self, stat):
        return (stat - 10) // 2

    def roll_stats(self):
        def roll_4d6_drop_lowest():
            rolls = [random.randint(1, 6) for _ in range(4)]
            return sum(rolls) - min(rolls)

        self.strength = roll_4d6_drop_lowest()
        self.dexterity = roll_4d6_drop_lowest()
        self.constitution = roll_4d6_drop_lowest()
        self.intelligence = roll_4d6_drop_lowest()
        self.wisdom = roll_4d6_drop_lowest()
        self.charisma = roll_4d6_drop_lowest()