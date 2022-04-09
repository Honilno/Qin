import json

from character_factory import CharacterFactory


class CharacterRepository:
    __slots__ = ["characters"]

    def __init__(self):
        with open(
                "characters.json"
        ) as json_file:
            readable_json = json.load(json_file)

        self.characters = []
        character_factory = CharacterFactory()

        for character in readable_json:
            self.characters.append(character_factory.parse(character))

    def print_character_names(self):
        for character in self.characters:
            print(character.name)
