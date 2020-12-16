# This is the main game file that will be run during play.
# Character/Boss info will be imported from character file. 

import random
import math

from character import Character
from character import Boss
from functions import *
from dungeon import *

def game():
    while True:
        start_game = input("""Welcome traveler. Do you seek adventure and the treasure that lies
        at the end? Yes or No (If you wish to quit at anytime type 'Q'.)\n""")
        
        if (start_game == "Y" or start_game == "y" or start_game == "yes" or start_game == "Yes"):
            Character.name.update({"Name": input('What is your name traveler? ')})
            #Roll stats for your character
            Character.stats.update({"Dexterity": roll_dice_dropping_lowest(4, 6)})
            Character.stats.update({"Strength": roll_dice_dropping_lowest(4, 6)})


            print(f'\nGreetings {Character.name["Name"]}! Now let us determine your attributes that will help you on your journey.') 
            print(f'You rolled {Character.stats["Dexterity"]} for your Dexterity. You rolled {Character.stats["Strength"]} for you Strength.')
            print("You only have 20 Hit Points so be careful!")
            Character.stats.update({"Weapon": input("What kind of weapon would you like to have? ")})

            print("\n\nTime to start your journey!\n\nYou arrive at an the ancient ruins of a temple standing alone amongst a field of grass.\n") 
            explore_ruin = input("Would you like to explore the ruins? Y/N  ")
            if (explore_ruin == 'Y' or explore_ruin == 'y' or explore_ruin == "yes" or explore_ruin == "Yes"):
                print("You enter the ruins and find at the bottom of a set of stairs an entrance way with two closed doors.\n")
            else:
                print("You leave the ruins. That was enough adventuring for you.\n")
                break
            
            main_door()
            boss_room()
            
            
              

        if (input == 'Q' or input == 'q'):
            break
        else:
            print("Return when you are ready for an adventure.\n\n")
            break

game()

