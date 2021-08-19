import random
import math

from character import Character



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
    if 18 > char_stat_roll >= 16:
        return 3
    if 16 > char_stat_roll >= 14:
        return 2
    if 14 > char_stat_roll >= 12:
        return 1
    if 12 > char_stat_roll:
        return 0

# # Function to determine bonus that will be added to attack
def stat_block_str(int):
    char_stat_roll = int(Character.stats["Strength"])
    #print(char_stat_roll)
    if char_stat_roll >= 18:
        return 4
    if 18 > char_stat_roll >= 16:
        return 3
    if 16 > char_stat_roll >= 14:
        return 2
    if 14 > char_stat_roll >= 12:
        return 1
    if 12 > char_stat_roll:
        return 0


# Function for adding to health
def stat_block_con(int):
    char_stat_roll = int(Character.stats["Constitution"])
    #print(char_stat_roll)
    if char_stat_roll >= 18:
        return 4
    if 18 > char_stat_roll >= 16:
        return 3
    if 16 > char_stat_roll >= 14:
        return 2
    if 14 > char_stat_roll >= 12:
        return 1
    if 12 > char_stat_roll:
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
        return 
    if 51 > d100_roll <= 99:
        return 
    if d100_roll >= 100:
        return 
