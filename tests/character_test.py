import unittest

from character_factory import CharacterFactory


class CharacterTest(unittest.TestCase):

    def setUp(self) -> None:
        character_dictionary_input_1 = {
                                        "Name": "peasant_berserker",
                                        "Agility": 4,
                                        "Body": 4,
                                        "Willpower": 4,
                                        "Melee": 2,
                                        "Weapon_skill": 1,
                                        "Constitution": 1,
                                        "Weapon_size": 2,
                                        "Armor_resistance": 0,
                                        "Tactics": "berserk"
                                        }
        character_factory = CharacterFactory()
        self.character_1 = character_factory.parse(character_dictionary_input_1)
        character_dictionary_input_2 = {
                                        "Name": "peasant_berserker",
                                        "Agility": 4,
                                        "Body": 4,
                                        "Willpower": 4,
                                        "Melee": 2,
                                        "Weapon_skill": 1,
                                        "Constitution": 1,
                                        "Weapon_size": 2,
                                        "Armor_resistance": 0,
                                        "Tactics": "defend"
                                        }
        self.character_2 = character_factory.parse(character_dictionary_input_2)

    def test_tactics(self):
        self.character_1.define_tactics()
        self.assertEqual(self.character_1.get_offensive_pa(0), self.character_1.pa)
        self.assertEqual(self.character_1.get_offensive_pa(1), 0)
        self.assertEqual(self.character_1.get_defence(0), 0)
        self.assertEqual(self.character_1.get_defence(1), 0)
        self.assertEqual(self.character_1.get_aggressiveness(), 3)
        self.character_2.define_tactics()
        self.assertEqual(self.character_2.get_offensive_pa(0), 1)
        self.assertEqual(self.character_2.get_offensive_pa(1), 0)
        self.assertEqual(self.character_2.get_defensive_pa(0), self.character_1.pa-1)
        self.assertEqual(self.character_2.get_defence(0), self.character_1.pa-1)
        self.assertEqual(self.character_2.get_defence(1), 0)
        self.assertEqual(self.character_2.get_aggressiveness(), 1)
        self.character_1.receive_blow(self.character_1.body+self.character_1.armor_resistance+1)
        self.assertEqual(self.character_1.get_offensive_pa(0), self.character_1.pa-3)
        self.assertEqual(self.character_1.medium_wounds, 1)
        self.character_2.receive_blow(self.character_2.body+self.character_2.armor_resistance+1)
        self.assertEqual(self.character_2.get_offensive_pa(0), 0)
        self.assertEqual(self.character_2.medium_wounds, 1)



