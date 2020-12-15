import math
import random


# statBlock = {"18": 4, "16": 3, "14": 2, "12": 1, "10<=": 0}


class Character:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.damage = 2 * random.randrange(1, 7)
        self.ability_check = random.randrange(1, 20)
        self.initiative = random.randrange(1,20)

    name = {
        "Name": ""
    }
    stats = {
        "Dexterity": "",
        "Strength": "",
        "Health": 20,
        "AC": 16,
        "Weapon": "",
    }

    def player_attack(self, target):
        print(f'You attacked the creature with your {Character.stats["Weapon"]}')
        target.health -= self.damage
        print(f'{target.name} has {target.health} health remaining.')


class Boss:
    def __init__(self, name, stats, damage, initiative):
        self.name = name
        self.stats = stats
        self.damage = random.randrange(1, 6)
        self.initiative = random.randrange(1,20)
    
    name = {
        "Name": "Gargamel"
    }

    stats = {
    "AC": 16,
    "Health": 15,
    "Weapon": "Sword"
    }

    damage = random.randrange(1, 6)
    initiative = random.randrange(1,20)
