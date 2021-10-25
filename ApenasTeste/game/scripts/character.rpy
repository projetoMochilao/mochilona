init python:

    class Player:
        def __init__(self, hp, mp, mdef, level=1):
            self.hp = hp
            self.mp = mp
            self.max_hp = hp
            self.max_mp = mp
            self.mdef = mdef
            self.level = level

        def addHP(self, amount):
            self.hp += amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
    
        def addMP(self, amount):
            self.mp += amount
            if self.mp > self.max_mp:
                self.mp = self.max_mp