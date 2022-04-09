

from character_repository import CharacterRepository

character_repository = CharacterRepository()

character_repository.print_character_names()

for character in character_repository.characters:
    character.define_tactics()
    print("name: ", character.name,
          " ob: ", character.get_offensive_pa(),
          " db: ", character.get_defence(),
          " in: ", character.get_aggressiveness(),
          "/", character.get_ob())
