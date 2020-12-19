# This is the main game file that will be run during play.
# Character/Boss info will be imported from character file. 

import random
import math

from character import Character, Boss
from dungeon import main_door, path, boss_room
from functions import roll_dice_dropping_lowest, stat_block_dex, stat_block_str

def game():
    while True:
        start_game = input("""Welcome traveler. Do you seek adventure and the treasure that lies
        at the end? Yes or No (If you wish to quit at anytime type 'Q'.)\n""")
        if (start_game.lower() == "y" or start_game.lower() == "yes"):
            Character.name.update({"Name": input('What is your name traveler? ')})
            #Roll stats for your character
            Character.stats.update({"Dexterity": roll_dice_dropping_lowest(4, 6)})
            Character.stats.update({"Strength": roll_dice_dropping_lowest(4, 6)})

            print(f'\nGreetings {Character.name["Name"]}! Now let us determine your attributes that will help you on your journey.') 
            print(f'You rolled {Character.stats["Dexterity"]} for your Dexterity. You rolled {Character.stats["Strength"]} for you Strength.')
            print(f'From your attribute scores you will be getting a bonus {stat_block_dex(int)} to your Dexterity checks.')  
            print(f'From your attribute scores you will be getting a bonus {stat_block_str(int)} to your strength checks.')
            print(f"You only have {Character.stats['Health']} Hit Points so be careful!")
            Character.stats.update({"Weapon": input("What kind of weapon would you like to have? ")})

            print("\n\nTime to start your journey!\n\nYou arrive at an the ancient ruins of a temple standing alone amongst a field of grass.\n") 
            explore_ruin = input("Would you like to explore the ruins? Y/N  ")
            if (explore_ruin.lower() == 'y' or explore_ruin.lower() == "yes"):
                print("You enter the ruins and find at the bottom of a set of stairs an entrance way with two closed doors.\n")
            else:
                print("You leave the ruins. That was enough adventuring for you.\n")
                break
            
            main_door()
            print("\nYou see a long corridor stretching out before you. You make your way down the dark corridor.")
            path()  
            break          
        else:
            print("Return when you are ready for an adventure.\n\n")
            break


if __name__ == "__main__":
    game()
