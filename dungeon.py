# This is where the functions regarding the temple reside. 

import math
import random


from character import Character, Boss
from functions import d20_roll, stat_block_dex, stat_block_str, strength_check, reflex_check



def main_door():
    strength_check = random.randrange(1, 21) + stat_block_str(int)
    reflex_check = random.randrange(1, 21) + stat_block_dex(int)
    door = input("Would you like to attempt to open the doors or check the doors for any traps? Door or Trap ")
    if (door == 'Door' or door == 'door'):
        print(f"You attempt to open the door. You rolled a {strength_check} on your attempt to open the doors.\n")
        if (strength_check >= 10):
            print("You open the doors and enter the temple.")
        elif (strength_check < 10):
            print("The door didn't open. You try again.")
            main_door()
    if (door == 'Trap' or door == 'trap'):
        print(f"You check the door for any traps. You rolled a {reflex_check} on your check. The door is not trapped\n")
        main_door()

# There are several traps in the temple. This function is used when the player stumbles into one of them.
def trap():
    print("You have activated a trap. Get out of the way!")
    print(f"You rolled a {reflex_check} to get out of the way!")
    if (reflex_check >= 10):
        print("You managed to get out of the way and didn't get hurt.")
    if (reflex_check < 10):
        damage = random.randrange(1, 7)
        health = Character.stats["Health"] - damage
        Character.stats.update({"Health": health})
        print(f"You failed to escape the trap. You take {damage} amount of damage. Be careful you only have {health} hitpoints left!")

# Final room of the temple where a boss encounter and treasure reside.
def boss_room():
    boss_room_entrence = input("""You notice as you enter the room a the walls glimmer with light reflecting off gold and silver. In the center of the room sits a tomb 
with the effegy of a king on the lid. As you enter the room a voice calls out. 'Who dares enters my chamber?' do you answer or run?  \n""")
    if(boss_room_entrence.lower() == 'answer' or boss_room_entrence.lower() == 'a'):
        print(f"You respond to the voice. My name is {Character.name['Name']}, and I come seeking the treasure of this forgotten temple. Will you let me have it or must we fight?\n")
        print(f"'I cannot let you have my treasure {Character.name['Name']}.' says the voice as the lid slides open. A skeletal figure rises out of the tomb. and starts making for you. ")
        print("The skeletal creature grabs a sword from the wall and takes a swing at you...\n")
        boss_battle()
    if (boss_room_entrence.lower() == 'run' or boss_room_entrence.lower == 'r'):
        print("You flee the room, sprinting back the way you came and out of the temple.")
        main_door()

# Function for the boss battle
def boss_battle():
    character = Character('name', 'stats', 'damage')
    boss = Boss('name', 'stats', 'damage')
    # So player can see the initiatives
    print(f"Boss initiative: {Boss.initiative}, Character initiative: {Character.initiative}")
    # Loop for the boss encouter. Will continue till either boss or player is dead. 
    while Boss.stats["Health"] > 0 or Character.stats["Health"] > 0:
        if (Boss.initiative > Character.initiative):
            boss_damage = boss.boss_damage
            current_player_health = Character.stats["Health"] - boss.boss_damage
            Character.stats.update({"Health": current_player_health})
            print(f"The boss did {boss_damage} damage. You now have {current_player_health} hitpoints left.\n")
            if (Character.stats["Health"] <= 0):
                print('You died!')
                break
            player_damage = character.player_damage
            current_boss_health = Boss.stats["Health"] - character.player_damage
            Boss.stats.update({"Health": current_boss_health})
            print(f"You attacked the creature with your {Character.stats['Weapon']} and dealt {player_damage} damage.\n")
            if (Boss.stats["Health"] <= 0):
                print(f'Congratulations {Character.name["Name"]}! You have beaten the boss and claimed the treasure!')
                break
          
        elif (Character.initiative > Boss.initiative):
            player_damage = character.player_damage
            current_boss_health = Boss.stats["Health"] - character.player_damage
            Boss.stats.update({"Health": current_boss_health})
            print(f"You attacked the creature with your {Character.stats['Weapon']} and dealt {player_damage} damage.")
            if (Boss.stats["Health"] <= 0):
                print(f'Congratulations {current_player_health}! You have beaten the boss and claimed the treasure!')
                break
            boss_damage = boss.boss_damage
            current_player_health = Character.stats["Health"] - boss.boss_damage
            Character.stats.update({"Health": current_player_health})
            print(f"The boss did {boss.boss_damage} damage. You now have {Character.stats['Health']} hitpoints left.\n")
            if (Character.stats["Health"] <= 0):
                print('You died!')
                break
        
