import random
import math
import sys
import time


from character import Character, Dragon, Goblin



def roll_dice_dropping_lowest(n_dice, dice_rank):
    results = [  # Generate n_dice numbers between [1, dice_rank]
        random.randint(1, dice_rank)
        for n
        in range(n_dice)
    ]
    lowest = min(results)  # Find the lowest roll among the results
    results.remove(lowest)  # Remove the first instance of that lowest roll
    return sum(results)  # Return the sum of the remaining results.

# Function to determine bonus added to Dex save and to find traps
def stat_block_dex(int):
    char_stat_roll = int(Character.stats["Dexterity"])
    #print(char_stat_roll)
    if char_stat_roll >= 18:
        return 4
    elif 18 > char_stat_roll >= 16:
        return 3
    elif 16 > char_stat_roll >= 14:
        return 2
    elif 14 > char_stat_roll >= 12:
        return 1
    elif 12 > char_stat_roll:
        return 0

# # Function to determine bonus that will be added to attack
def stat_block_str(int):
    char_stat_roll = int(Character.stats["Strength"])
    #print(char_stat_roll)
    if char_stat_roll >= 18:
        return 4
    elif 18 > char_stat_roll >= 16:
        return 3
    elif 16 > char_stat_roll >= 14:
        return 2
    elif 14 > char_stat_roll >= 12:
        return 1
    elif 12 > char_stat_roll:
        return 0


# Function for adding to health
def stat_block_con(int):
    char_stat_roll = int(Character.stats["Constitution"])
    #print(char_stat_roll)
    if char_stat_roll >= 18:
        return 4
    elif 18 > char_stat_roll >= 16:
        return 3
    elif 16 > char_stat_roll >= 14:
        return 2
    elif 14 > char_stat_roll >= 12:
        return 1
    elif 12 > char_stat_roll:
        return 0

# functions to determine the reflex and strength checks
d20_roll = random.randrange(1, 21) # Rolls a d20 

def reflex_check():
    dex_save = d20_roll + stat_block_dex(int)
    return dex_save
    

def strength_check():
    str_check = d20_roll + stat_block_str(int)
    return str_check
    


# function for possible random encounter
def random_encounter():
    d100_roll = random.randrange(1, 101) # Rolls a d100
    if d100_roll  <= 50:
        sys.exit() 
    elif 51 > d100_roll <= 99:
        return goblin_encounter()
    elif d100_roll >= 100:
        return dragon_encounter()


# Function for goblin encounter
def goblin_encounter():
 # Created instances for both classes 
    character = Character('name', 'stats', 'damage', 'attack')
    goblin = Goblin('name', 'stats', 'damage', 'attack')
    # So player can see the initiatives
    print(f"Goblin initiative: {Goblin.initiative}, Character initiative: {Character.initiative}")
    time.sleep(2)
    # Loop for the boss encouter. Will continue till either boss or player is dead. 
    while Goblin.stats["Health"] > 0 or Character.stats["Health"] > 0:
        if (Goblin.initiative > Character.initiative):
            goblin_damage = goblin.goblin_damage
            goblin_attack = goblin.goblin_attack
            current_player_health = Character.stats["Health"]
            if(goblin_attack >= Character.stats["AC"]):
                current_player_health = current_player_health - goblin_damage # The players current health after damage. 
                Character.stats.update({"Health": current_player_health})
                print(f"The goblin did {goblin_damage} damage. You now have {current_player_health} hitpoints left.\n")
                time.sleep(2)
                if (Character.stats["Health"] <= 0):
                    print('\nYou died!\n')
                    break
            else:
                print("The goblin missed its attack.\n")
                time.sleep(2)
            player_damage = character.player_damage
            player_attack = character.player_attack
            if (player_attack >= Goblin.stats["AC"]):
                current_goblin_health = Goblin.stats["Health"] - player_damage
                Goblin.stats.update({"Health": current_goblin_health}) # The Boss's current health after damage
                print(f"You attacked the goblin with your {Character.stats['Weapon'].lower()} and dealt {player_damage} damage.\n")
                time.sleep(2)
                if (Goblin.stats["Health"] <= 0):
                    print(f'\nCongratulations {Character.name["Name"]}! You have beaten the goblin!\n')
                        
            else:
                print(f"You rolled a {player_attack} on your attack and missed.\n")
                time.sleep(2)
          
        elif (Character.initiative > Goblin.initiative):
            player_damage = character.player_damage
            player_attack = character.player_attack
            if (player_attack >= Goblin.stats["AC"]):
                current_goblin_health = Goblin.stats["Health"] - player_damage
                Goblin.stats.update({"Health": current_goblin_health})
                print(f"You attacked the goblin with your {Character.stats['Weapon'].lower()} and dealt {player_damage} damage.\n")
                if (Goblin.stats["Health"] <= 0):
                    print(f'\nCongratulations {Character.name["Name"]}! You have beaten the goblin!\n')
                    
            else:
                print(f"You rolled a {player_attack} on your attack and missed.\n")
                time.sleep(2)
            goblin_damage = goblin.goblin_damage
            goblin_attack = goblin.goblin_attack
            if(goblin_attack >= Character.stats["AC"]):
                current_player_health = Character.stats["Health"] - goblin_damage
                Character.stats.update({"Health": current_player_health})
                print(f"The goblin did {goblin_damage} damage. You now have {Character.stats['Health']} hitpoints left.")
                time.sleep(2)
                if (Character.stats["Health"] <= 0):
                    print('\nYou died!\n')
                    break
            else:
                print("The goblin missed its attack.")

# function for dragon encounter
def dragon_encounter():
     # Created instances for both classes 
    character = Character('name', 'stats', 'damage', 'attack')
    dragon = Dragon('name', 'stats', 'damage', 'attack')
    # So player can see the initiatives
    print(f"Boss initiative: {Dragon.initiative}, Character initiative: {Character.initiative}")
    time.sleep(2)
    # Loop for the boss encouter. Will continue till either boss or player is dead. 
    while Dragon.stats["Health"] > 0 or Character.stats["Health"] > 0:
        if (Dragon.initiative > Character.initiative):
            dragon_damage = dragon.dragon_claw_damage
            dragon_attack = dragon.dragon_attack
            current_player_health = Character.stats["Health"]
            if(dragon_attack >= Character.stats["AC"]):
                current_player_health = current_player_health - dragon_damage # The players current health after damage. 
                Character.stats.update({"Health": current_player_health})
                print(f"The dragon did {dragon_damage} damage. You now have {current_player_health} hitpoints left.\n")
                time.sleep(2)
                if (Character.stats["Health"] <= 0):
                    print('\nYou died!\n')
                    break
            else:
                print("The boss missed its attack.\n")
                time.sleep(2)
            player_damage = character.player_damage
            player_attack = character.player_attack
            if (player_attack >= Dragon.stats["AC"]):
                current_dragon_health = Dragon.stats["Health"] - player_damage
                Dragon.stats.update({"Health": current_dragon_health}) # The Boss's current health after damage
                print(f"You attacked the dragon with your {Character.stats['Weapon'].lower()} and dealt {player_damage} damage.\n")
                time.sleep(2)
                if (Dragon.stats["Health"] <= 0):
                    print(f'\nCongratulations {Character.name["Name"]}! You have beaten the dragon!\n')
                    break    
            else:
                print(f"You rolled a {player_attack} on your attack and missed.\n")
                time.sleep(2)
          
        elif (Character.initiative > Dragon.initiative):
            player_damage = character.player_damage
            player_attack = character.player_attack
            if (player_attack >= Dragon.stats["AC"]):
                current_boss_health = Dragon.stats["Health"] - player_damage
                Dragon.stats.update({"Health": current_boss_health})
                print(f"You attacked the creature with your {Character.stats['Weapon'].lower()} and dealt {player_damage} damage.\n")
                if (Dragon.stats["Health"] <= 0):
                    print(f'\nCongratulations {Character.name["Name"]}! You have beaten the dragon!\n')
                    break
            else:
                print(f"You rolled a {player_attack} on your attack and missed.\n")
                time.sleep(2)
            boss_damage = dragon.dragon_claw_damage
            boss_attack = dragon.dragon_attack
            if(boss_attack >= Character.stats["AC"]):
                current_player_health = Character.stats["Health"] - boss_damage
                Character.stats.update({"Health": current_player_health})
                print(f"The boss did {boss_damage} damage. You now have {Character.stats['Health']} hitpoints left.")
                time.sleep(2)
                if (Character.stats["Health"] <= 0):
                    print('\nYou died!\n')
                    break
            else:
                print("The boss missed its attack.")