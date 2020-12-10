import math
import random

statBlock = {"18": 4, "16": 3, "14": 2, "12": 1, "10": 0, "8": -1, "6": -2, "4": -3, "2": -4}

class Character:
    def __init__(self, name):
        self.name = name
    name = {
        "Name": ""
    }
    stats = {
        "Dexterity": "",
        "Strength": "",
        "Health": 20
    }
    attack = 2*random.randrange(1, 7) + ()


class Boss:
    AC = 16
    HP = 15
    attack = random.randrange(1, 7)
