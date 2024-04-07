import math
import random


# statBlock = {"18": 4, "16": 3, "14": 2, "12": 1, "10<=": 0}


class Character:
    def __init__(self, name, stats, damage, attack):
        self.name = name
        self.health = 20
        self.stats = stats
        self.damage = 2 
        self.attack = 1
        

    name = {
        "Name": ""
    }
    stats = {
        "Health": 20,
        "AC": 16,
        "Weapon": "",
    }

    @property
    def player_damage(self):
        return self.damage * random.randrange(1, 7)

    
    initiative = random.randrange(1, 21)

    @property
    def player_attack(self):
        return self.attack * random.randrange(1, 21)


class Boss:
    def __init__(self, name, stats, damage, attack):
        self.name = name
        self.health = 15
        self.stats = stats
        self.damage = 2
        self.attack = 1
    
    name = {
        "Name": ""
    }

    stats = {
    "AC": 16,
    "Health": 15,
    "Weapon": "Sword"
    }

    @property
    def boss_damage(self):
        return self.damage * random.randrange(1, 7)

    
    initiative = random.randrange(1, 21) + 1

    @property
    def boss_attack(self):
        return self.attack * random.randrange(1, 21)


class Dragon:
    def __init__(self, name, stats, damage, attack):
        self.name = name
        self.health = 50
        self.stats = stats
        self.damage = 3
        self.attack = 2
    
    name = {
        "Name": "Vorugal"
    }

    stats = {
    "AC": 20,
    "Health": 50,
    "Weapon": "Claw",
    "Breath": "Fire"
    }

    @property
    def dragon_claw_damage(self):
        return self.damage * random.randrange(1, 11)

    @property
    def dragon_breath_damage(self):
        return self.damage * random.randrange(1, 11)

    
    initiative = random.randrange(1, 21)

    @property
    def dragon_attack(self):
        return self.attack * random.randrange(1, 21)


class Goblin:
    def __init__(self, name, stats, damage, attack):
        self.name = name
        self.health = 15
        self.stats = stats
        self.damage = 1
        self.attack = 1
    
    name = {
        "Name": "Boblin the Goblin"
    }

    stats = {
    "AC": 13,
    "Health": 10,
    "Weapon": "Club"
    }

    @property
    def goblin_damage(self):
        return self.damage * random.randrange(1, 7)

    
    initiative = random.randrange(1, 21)

    @property
    def goblin_attack(self):
        return self.attack * random.randrange(1, 21)