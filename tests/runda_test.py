import unittest

from character_factory import CharacterFactory
from runda import Runda


class RundaTest(unittest.TestCase):

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
            "Name": "peasant_defender",
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

    def test_initiative(self):
        runda = Runda()
        runda.set_fighters(self.character_1, self.character_2)
        runda.declaration_phase()
        runda.determine_initiative()
        self.assertEqual(runda.character_with_initiative, 0)

    def test_round_resolve(self):
        runda = Runda()
        runda.set_fighters(self.character_1, self.character_2)
        runda.resolve_round()
        self.assertEqual(runda.character_with_initiative, 0)
        self.assertEqual(runda.round_count, 1)
