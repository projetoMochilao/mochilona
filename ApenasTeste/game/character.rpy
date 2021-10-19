init python:

    class Player:
        def __init__(self, hp, mp, atk, defense, mdef, Lavel=1):
            self.hp = hp
            self.mp = mp
            self.max_hp = hp
            self.max_mp = mp
            self.atk = atk
            self.defense = defense
            self.mdef = mdef
            self.level = level
            self.weapon = None
            self.armor = {"head": None, "chest": None, "acc": None, "shield": None}

    def addHP(amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    
    def addMp(amount):
        self.mp += amount
        if self.mp > self.max_mp:
            self.mp = self.max_mp
    
    def equip_weapon(weapon):
        if self.weapon != None:
            self.unequip_weapon()
        
        self.weapon = weapon
        self.atk += weapon.atk

    def unequip_weapon():
        if self.weapon != None:
            self.atk -= self.weapon.atk
            self.weapon = None

