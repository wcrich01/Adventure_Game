# This is the main game file that will be run during play.
# Character/Boss info will be imported from character file. 

import random
import math

from character import Character
from character import Boss
from functions import *

def game():
    while True:
        start_game = input("""Welcome traveler. Do you seek adventure and the treasure that lies
        at the end? Y/N\n""")
        if start_game == 'Y' or 'y':
            Character.name.update({"Name": input('What is your name traveler? ')})
            # Possible reroll stat function
            Character.stats.update({"Dexterity": roll_dice_dropping_lowest(4, 6)})
            Character.stats.update({"Strength": roll_dice_dropping_lowest(4, 6)})


            print(f'''\nGreetings {Character.name["Name"]}! Now let us determine your attributes that will help you on your journey.
            You rolled {Character.stats["Dexterity"]} for your Dexterity. You rolled {Character.stats["Strength"]} for you Strength.\n
            You only have 20 Hit Points so be careful!''')

            print("Time to start your journey!\n\n You arrive at an the ancient ruins of a temple standing alone amongst a field of grass.\n") 
            explore_ruin = input("Would you like to explore the ruins? Y/N  ")
            if explore_ruin== 'Y' or 'y':
                print("You enter the ruins and find at the bottom of a set of stairs an entrance way with two closed doors.")
        elif start_game == 'N' or 'n':
            print("Okay. Return when you are ready for an adventure.")
            break
game()