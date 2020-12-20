# This is the main game file that will be run during play.
# Character/Boss info will be imported from character file. 

import random
import math
import sys


from character import Character, Boss
from dungeon import main_door, path, boss_room
from functions import roll_dice_dropping_lowest, stat_block_dex, stat_block_str, stat_block_con

def game():
    while True:
        start_game = input("""Welcome traveler. Do you seek adventure and the treasure that lies
        at the end? Yes or No (If you wish to quit at anytime type 'Q'.)\n""")
        if (start_game.lower() == "y" or start_game.lower() == "yes"):
            Character.name.update({"Name": input('What is your name traveler? ').capitalize()})
            #Roll stats for your character
            Character.stats.update({"Dexterity": roll_dice_dropping_lowest(4, 6)})
            Character.stats.update({"Strength": roll_dice_dropping_lowest(4, 6)})
            Character.stats.update({"Constitution": roll_dice_dropping_lowest(4, 6)})
            Health = Character.stats['Health'] + stat_block_con(int)
            Character.stats.update({"Health": Health})

            print(f'\nGreetings {Character.name["Name"]}! Now let us determine your attributes that will help you on your journey.') 
            print(f'You rolled {Character.stats["Dexterity"]} for your Dexterity, which gave you a bonus {stat_block_dex(int)} to your Dexterity checks.')
            print(f'You rolled {Character.stats["Strength"]} for your Strength, which gave you a bonus {stat_block_str(int)} to your Strength checks.')
            print(f'You rolled {Character.stats["Constitution"]} for your Constitution, which gave you a bonus {stat_block_con(int)} to your health.')
            print(f"You only have {Character.stats['Health']} Hit Points so be careful!")
            Character.stats.update({"Weapon": input("What kind of weapon would you like to have? ")})

            print("\n\nTime to start your journey!\nYou arrive at an the ancient ruins of a temple standing alone amongst a field of grass.\n") 
            def ruins():
                explore_ruin = input("Would you like to explore the ruins? Y/N  ")
                if (explore_ruin.lower() == 'y' or explore_ruin.lower() == "yes"):
                    print("You enter the ruins. At the bottom of a wide staircase sits an entrance way with two closed doors.\n")
                    main_door()
                elif (explore_ruin.lower() == 'n' or explore_ruin.lower() == "n" or explore_ruin.lower() == 'q'):
                    print("You leave the ruins. That was enough adventuring for you.\n")
                    sys.exit()
                
                else:
                    print("The wheel of time turns as you decide what to do...")
                    ruins()
            ruins()
            print("\nYou see a long corridor stretching out before you. You make your way down the dark corridor.")
            path()  
            break
        if (input == 'Q' or input == 'q'):
            sys.exit()
        else:
            print("Return when you are ready for an adventure.\n\n")
            break


if __name__ == "__main__":
    game()
