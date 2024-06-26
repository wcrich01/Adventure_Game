# This file is for the various locations in the game
# Town is currently in the works
# A road location will be added eventually


import random
import math
import sys


from character import Character
from dungeon import main_door, path, boss_room
from functions import roll_dice_dropping_lowest, stat_block_dex, stat_block_str, stat_block_con


def town():
    print("\nYour adventure starts in the town for Forsburg. there are several sites to visit. Where shall you start your adventure?")
    town_poi = input("Would you like to visit the tavern, town hall, chapel, or leave town? ")
    if (town_poi.lower() == 'tavern'):
        print("""You make your way over to the town tavern. As you approach, you see the name of the tavern is, 'The Magestic Hen,' from within you hear
        the sounds of people eating and talking.""")
    elif(town_poi.lower() == 'town hall'):
        print("""You make your way over to the town hall. It is a two story stone building. It is the only building in the town made entirely of stone. 
        You pass a sentry standing guard at the door and head in. Off the main hall is a door labeled 'Mayor', you approach and open the door.
        The mayor's office is a modest room with a in the middle and shelves of scrolls lining the walls.""")
    elif(town_poi.lower() == 'chapel'):
        print("""On the Western edge of the town you can see a small church. Making your way over to that side of town you find a church and graveyard
        situated on a field of green grass. The building appears to be in good repair and the grounds well maintained. As you approach the church you can 
        make out a sunburst on each door. This is a temple to Pelor. As you push open the door you are greeted by the smell of incense. Walking in you 
        approach you are greeted by a priest. 
        'Greeting traveller. How may I be of assistance?' """)

def ruins():
    print("\n\nYou arrive at an the ancient ruins of a temple standing alone amongst a field of grass.\n")
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
