# This is where the functions regarding the temple reside. 

import math
import random
import sys


from character import Character, Boss
from functions import d20_roll, stat_block_dex, stat_block_str, strength_check, reflex_check



def main_door():
    # roll checks to detect trap and strength check to open door
    strength_check = random.randrange(1, 21) + stat_block_str(int)
    reflex_check = random.randrange(1, 21) + stat_block_dex(int)
    # main door input and reactions to input
    door = input("Would you like to attempt to open the doors or check the doors for any traps? Door or Trap ")
    if (door.lower() == 'door' or door.lower() == 'd'):
        print(f"You attempt to open the door. You got a {strength_check} on your strength check to open the doors.\n")
        if (strength_check >= 10):
            print("You open the doors and enter the temple.")
        elif (strength_check < 10):
            print("The door didn't open. You try again.")
            main_door()
    if (door.lower() == 'trap' or door.lower() == 't'):
        print(f"You check the door for any traps. You got a {reflex_check} on your reflex check. The door is not trapped\n")
        main_door()
    if (door.lower() == 'q' or door.lower() == 'quit'):
        print("You abandon your attempts to open the door and leave the ruins.")
        sys.exit()


# This is used for the main movement in the dungeon
# While loop added because player could die on paths. Need to account for that
def path():
    while (Character.stats["Health"] > 0):
        intersection = input("After walking for several minutes, you come upon an intersection with paths leading forward, left or right. ")
        if (intersection.lower() == 'forward' or intersection.lower() == 'f'):  # Forward turn path
            door = input("You continue walking down the corridor. After several minutes of walking you reach a door. Would you like to enter the room? Yes or No  ")
            if (door.lower() == 'yes' or door.lower() == 'y'):
                room_1()
            elif(door.lower() == 'no' or door.lower() == 'n'):
                print("You turn and travel back down the corridor.")
        elif (intersection.lower() == 'left' or intersection.lower() == 'l'):  # Left turn path
            print("You turn left and head down the left corridor. You hear a click as you are walking... \n")
            trap()
            if (Character.stats["Health"] <= 0):
                print("You died!\n")
                sys.exit()
            else:
                print("You turn and head back the way you came.")
            path()
        elif (intersection.lower() == 'right' or intersection.lower() == 'r'): # Right turn path
            print("You turn right and head down the right corridor. You notice crypts built into the walls of the passage.")
            print("You eventually come upon another intersection with the corridor continuing to the right or left. Across from you is a door.")
            t_intersection = input("Which way would you like to go? Right, Left, or door? ")
            if (t_intersection.lower() == 'right' or t_intersection.lower() == 'r'):
                print("You walk into a collapsed section of tunnel. There is no way through. You turn and head back and straight through the previous intersection.")
                print("You approach a closed door. You open the door and step in.\n")
                boss_room()
                break
            elif(t_intersection.lower() == 'left' or t_intersection.lower() == 'l'):
                print("You turn left and come upon a closed door. You open the door and step in.\n")
                boss_room()
                break
            elif(t_intersection.lower() == 'door' or t_intersection.lower() == 'd'):
                room_2()
                break
            elif(t_intersection.lower() != 'q'):
                print("That is an invalid response. Please select Right, Left, or Door")
                t_intersection = input("Which way would you like to go? Right, Left, or door? ")
        elif(intersection.lower() == 'quit' or intersection.lower() == 'q'):
            sys.exit()

# There are several traps in the temple. This function is used when the player stumbles into one of them.
def trap():
    reflex_check = random.randrange(1, 21) + stat_block_dex(int)
    print("You have activated a trap. Get out of the way!")
    print(f"You rolled a {reflex_check} to get out of the way!")
    if (reflex_check >= 10):
        print("You managed to get out of the way and didn't get hurt.")
        path()
    if (reflex_check < 10):
        damage = random.randrange(1, 7)
        health = Character.stats["Health"] - damage
        Character.stats.update({"Health": health})
        print(f"You failed to escape the trap. You take {damage} amount of damage. Be careful you only have {health} hitpoints left!")


# Function calls for the two rooms
def room_1():
    print("You enter a room with a stone table with embalming tools and other instruments for the preparation of bodies laying on the table.")
    room_1 = input("Would you like to explore the room or leave? Explore or Leave ")
    if (room_1.lower() == 'explore' or room_1.lower() == 'e'):
        print("You find nothing of value in the room. As you turn to leave a gleam catches your eye. As you touch the gleaming piece of gold you hear a soft click.\n")
        trap()
    elif(room_1.lower() == 'leave' or room_1.lower() == 'l'):
        print("You exit the room and return back down the corridor. You eventually get back to the intersection you started at.\n")


def room_2():
    print("You enter a room with walls covered in scroll shelves. There is a lone desk sitting in the middle of the room.")
    room_1 = input("Would you like to explore the room or leave? Explore or Leave ")
    if (room_1.lower() == 'explore' or room_1.lower() == 'e'):
        print("\nThere are plenty off ancient scrolls stacked on the shelves. You pull several out to look at but they are in a language you don't speak.")
        print("On the desk you find quills and dried inkwells. You guess this room is a records room for the temple.")
        print("You decide to leave the room and exit to right. You approach a closed door. You open the door and step in.\n")
        boss_room()
    elif(room_1.lower() == 'leave' or room_1.lower() == 'l'):
        print("You exit the room and turn right down the corridor. You approach a closed door. You open the door and step in.\n")
        boss_room()
        

# Final room of the temple where a boss encounter and treasure reside.
def boss_room():
    boss_room_entrence = input("""You notice as you enter the room a the walls glimmer with light reflecting off gold and silver. In the center of the room sits a tomb 
with the effegy of a king on the lid. As you enter the room a voice calls out. 'Who dares enters my chamber?' do you answer or run?  """)
    if(boss_room_entrence.lower() == 'answer' or boss_room_entrence.lower() == 'a'):
        print(f"\nYou respond to the voice. My name is {Character.name['Name']}, and I come seeking the treasure of this forgotten temple. Will you let me have it or must we fight?\n")
        print(f"'I am {Boss.name['Name']}, I cannot let you have my treasure {Character.name['Name']}.' says the voice as the lid slides open. A skeletal figure rises out of the tomb. and starts making for you. ")
        print("The skeletal creature grabs a sword from the wall and takes a swing at you...")
        print('Time to roll initiative!\n')
        boss_battle()
    elif (boss_room_entrence.lower() == 'run' or boss_room_entrence.lower() == 'r'):
        print(f"\n{Character.name['Name']} flees the room, sprinting back the way you came and out of the temple.")
    elif(boss_room_entrence.lower() == 'quit' or boss_room_entrence.lower() == 'q'):
        return


# Function for the boss battle
def boss_battle():
    # Created instances for both classes 
    character = Character('name', 'stats', 'damage')
    boss = Boss('name', 'stats', 'damage')
    # So player can see the initiatives
    print(f"Boss initiative: {Boss.initiative}, Character initiative: {Character.initiative}")
    # Loop for the boss encouter. Will continue till either boss or player is dead. 
    while Boss.stats["Health"] > 0 or Character.stats["Health"] > 0:
        if (Boss.initiative > Character.initiative):
            boss_damage = boss.boss_damage
            current_player_health = Character.stats["Health"]
            current_player_health = current_player_health - boss_damage # The players current health after damage. 
            Character.stats.update({"Health": current_player_health})
            print(f"The boss did {boss_damage} damage. You now have {current_player_health} hitpoints left.")
            if (Character.stats["Health"] <= 0):
                print('\nYou died!\n')
                break
            player_damage = character.player_damage
            current_boss_health = Boss.stats["Health"] - player_damage
            Boss.stats.update({"Health": current_boss_health}) # The Boss's current health after damage
            print(f"You attacked the creature with your {Character.stats['Weapon'].lower()} and dealt {player_damage} damage.")
            if (Boss.stats["Health"] <= 0):
                print(f'\nCongratulations {Character.name["Name"]}! You have beaten the boss and claimed the treasure!\n')
                break
          
        elif (Character.initiative > Boss.initiative):
            player_damage = character.player_damage
            current_boss_health = Boss.stats["Health"] - player_damage
            Boss.stats.update({"Health": current_boss_health})
            print(f"You attacked the creature with your {Character.stats['Weapon'].lower()} and dealt {player_damage} damage.")
            if (Boss.stats["Health"] <= 0):
                print(f'\nCongratulations {Character.name["Name"]}! You have beaten the boss and claimed the treasure!\n')
                break
            boss_damage = boss.boss_damage
            current_player_health = Character.stats["Health"] - boss_damage
            Character.stats.update({"Health": current_player_health})
            print(f"The boss did {boss_damage} damage. You now have {Character.stats['Health']} hitpoints left.")
            if (Character.stats["Health"] <= 0):
                print('\nYou died!\n')
                break
        
