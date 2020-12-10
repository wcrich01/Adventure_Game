# This is the main game file that will be run during play.
# Character/Boss info will be imported from character file. 

from character import Character
from character import Boss

import random
import math

def roll_dice_dropping_lowest(n_dice, dice_rank):
    results = [  # Generate n_dice numbers between [1, dice_rank]
        random.randint(1, dice_rank)
        for n
        in range(n_dice)
    ]
    lowest = min(results)  # Find the lowest roll among the results
    results.remove(lowest)  # Remove the first instance of that lowest roll
    return sum(results)  # Return the sum of the remaining results.


start_game = print(input("""Welcome traveler. Do you seek adventure and the treasure that lies
at the end? Y/N\n"""))
#if start_game == 'Y':
Character.name.update({"Name": input('What is your name traveler? ')})
# Possible reroll stat function
Character.stats.update({"Dexterity": roll_dice_dropping_lowest(4, 6)})
Character.stats.update({"Strength": roll_dice_dropping_lowest(4, 6)})

print(f'''\nGreetings {Character.name["Name"]} let us now determine your attributes that will help you on your journey.
You rolled {Character.stats["Dexterity"]} for your Dexterity. You rolled {Character.stats["Strength"]} for you Strength.\n
You only have 20 Hit Points so be careful!''')
# elif start_game == 'N':
#     print("Okay. Return when you are ready for an adventure.")