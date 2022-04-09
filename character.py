import random


class Character:
    __slots__ = ("name", "agility", "melee", "weapon_skill", "body", "constitution", "willpower", "pa", "wound_limit",
                 "light_wounds", "medium_wounds", "heavy_wounds", "critical_wounds", "offensive", "defensive",
                 "weapon_size", "armor_resistance", "tactics", "crippled_locations", "target", "round_done")

    def __init__(self):
        self.pa = None
        self.wound_limit = None
        self.target = None
        self.light_wounds = 0
        self.medium_wounds = 0
        self.heavy_wounds = 0
        self.critical_wounds = 0
        self.offensive = []
        self.defensive = []
        self.crippled_locations = []
        self.round_done = False

    def initialize_abilities(self):
        self.pa = self.agility + self.melee + self.weapon_skill
        self.wound_limit = self.body + self.constitution

    def select_target(self, target):
        self.target = target

    def get_offensive_pa(self, i=0):
        if i < len(self.offensive):
            return self.offensive[i]
        else:
            return 0

    def get_defensive_pa(self, i=0):
        if i < len(self.defensive):
            return self.defensive[i]
        else:
            return 0

    def get_defence(self, i=0):
        return self.get_defensive_pa(i)

    def get_aggressiveness(self):
        ob = sum(self.offensive)
        if ob == 0:
            return 0
        db = sum(self.defensive)
        if db == 0:
            return 3
        ratio = ob/db
        if ratio > 2:
            return 3
        elif ratio >= 0.5:
            return 2
        else:
            return 1

    def get_ob(self):
        return sum(self.offensive)

    def define_tactics(self):
        if self.tactics == "defend":
            self.tactics_defender()
        elif self.tactics == "berserk":
            self.tactics_berserk()
        elif self.tactics == "random":
            self.tactics_random()

    def receive_blow(self, hits):
        hits_passed_armor = hits - self.armor_resistance
        if hits_passed_armor <= 0:
            pass
        elif hits_passed_armor <= self.body:
            self.light_wounds += 1
            self.reduce_offence(1)
        elif hits_passed_armor <= self.body * 2:
            self.medium_wounds += 1
            self.reduce_offence(3)
        elif hits_passed_armor <= self.body * 4:
            self.heavy_wounds += 1
            self.reduce_offence(5)
        else:
            self.critical_wounds += 1
            self.offensive = []

    def reduce_offence(self, i):
        reduction = i
        if not self.round_done:
            j = len(self.offensive) - 1
            while j >= 0:
                if self.offensive[j] >= reduction:
                    self.offensive[j] -= reduction
                    reduction = 0
                    j -= 1
                else:
                    reduction -= self.offensive[j]
                    self.offensive.pop(j)
                    j -= 1

    def tactics_defender(self):
        self.defensive = []
        self.offensive = []
        if self.pa > 1:
            self.offensive.append(1)
            self.defensive.append(self.pa - 1)
        else:
            self.offensive.append(0)
            self.defensive.append(self.pa)

    def tactics_berserk(self):
        self.defensive = []
        self.offensive = []
        self.defensive.append(0)
        self.offensive.append(self.pa)

    def tactics_random(self):
        self.defensive = []
        self.offensive = []
        if self.pa > 1:
            random_offence = random.randint(1, self.pa)
            self.defensive.append(self.pa - random_offence)
            self.offensive.append(random_offence)
        else:
            self.defensive.append(0)
            self.offensive.append(self.pa)

