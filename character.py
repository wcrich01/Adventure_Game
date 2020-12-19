import math
import random


# statBlock = {"18": 4, "16": 3, "14": 2, "12": 1, "10<=": 0}


class Character:
    def __init__(self, name, stats, damage):
        self.name = name
        self.health = 20
        self.stats = stats
        self.damage = 2 
        

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


class Boss:
    def __init__(self, name, stats, damage):
        self.name = name
        self.health = 15
        self.stats = stats
        self.damage = 2
    
    name = {
        "Name": "Gargamel"
    }

    stats = {
    "AC": 16,
    "Health": 15,
    "Weapon": "Sword"
    }

    @property
    def boss_damage(self):
        return self.damage * random.randrange(1, 7)

    
    initiative = random.randrange(1, 21)
