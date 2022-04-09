from character import Character


class CharacterFactory:

    def parse(self, input_dictionary):
        character = Character()
        character.name = input_dictionary.get("Name")
        character.agility = input_dictionary.get("Agility")
        character.body = input_dictionary.get("Body")
        character.willpower = input_dictionary.get("Willpower")
        character.melee = input_dictionary.get("Melee")
        character.weapon_skill = input_dictionary.get("Weapon_skill")
        character.constitution = input_dictionary.get("Constitution")
        character.weapon_size = input_dictionary.get("Weapon_size")
        character.armor_resistance = input_dictionary.get("Armor_resistance")
        character.tactics = input_dictionary.get("Tactics")
        character.initialize_abilities()
        return character
