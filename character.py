class Character:
    __slots__ = ("agility", "melee", "weapon_skill", "body", "constitution", "willpower", "pa", "wound_limit",
                 "light_wounds", "heavy_wounds", "critical_wounds", "offensive", "defensive", "weapon_size",
                 "armor_resistance")

    def __init__(self):
        self.light_wounds = 0
        self.heavy_wounds = 0
        self.critical_wounds = 0
        self.offensive = []
        self.defensive = []

    def initialize_abilities(self):
        self.pa = self.agility+self.melee+self.weapon_skill
        self.wound_limit = self.body+self.constitution

    def get_offensive(self, i):
        if i < len(self.offensive[i]):
            return self.offensive[i]
        else:
            return 0

    def get_defensive(self, i):
        if i < len(self.defensive):
            return self.defensive[i]
        else:
            return 0

    def define_tactics(self):
        pass

    def receive_blow(self, hits):
        if hits == 0:
            pass
        elif hits <= self.body:
            self.light_wounds += 1
        pass

