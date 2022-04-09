from character import Character
from kostka import Kostka


class Runda:
    __slots__ = ["character_with_initiative", "fighters", "round_count"]

    @staticmethod
    def resolve_attack(attacker: Character, defender: Character):
        if attacker.get_offensive_pa() > 0:
            attack_result = attacker.get_offensive_pa() - defender.get_defence() + Kostka.k6PRO()
            damage = 0
            if attack_result >= 0:
                damage = attack_result*attacker.weapon_size
                defender.receive_blow(damage)
            print(attacker.name, " attacks, result: ", attack_result, " damage: ", damage)

    def __init__(self):
        self.character_with_initiative = None
        self.fighters = []
        self.round_count = 0

    def resolve_round(self):
        self.round_count += 1
        self.declaration_phase()
        self.determine_initiative()
        self.resolve_attacks()

    def set_fighters(self, fighter1: Character, fighter2: Character):
        self.fighters.append(fighter1)
        self.fighters.append(fighter2)

    def declaration_phase(self):
        for fighter in self.fighters:
            fighter.define_tactics()

    def determine_initiative(self):
        aggressiveness = []
        ob = []
        for fighter in self.fighters:
            aggressiveness.append(fighter.get_aggressiveness())
            ob.append(fighter.get_ob())

        if aggressiveness[0] > aggressiveness[1]:
            self.character_with_initiative = 0
        elif aggressiveness[0] < aggressiveness[1]:
            self.character_with_initiative = 1
        else:
            if ob[0] > ob[1]:
                self.character_with_initiative = 0
            elif ob[0] < ob[1]:
                self.character_with_initiative = 1
            else:
                if Kostka.k6() > 3:
                    self.character_with_initiative = 1

    def resolve_attacks(self):
        if self.character_with_initiative == 0:
            Runda.resolve_attack(self.fighters[0], self.fighters[1])
            Runda.resolve_attack(self.fighters[1], self.fighters[0])
            print("initiative 0")
        else:
            Runda.resolve_attack(self.fighters[1], self.fighters[0])
            Runda.resolve_attack(self.fighters[0], self.fighters[1])
            print("initiative 1")

