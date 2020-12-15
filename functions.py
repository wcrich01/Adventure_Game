import random
import math

from character import Character

d20_roll = random.randrange(1, 20)

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

# functions to determine the reflex and strength checks
def reflex_check():
    dex_save = d20_roll + stat_block_dex(int)
    return dex_save
    

def strength_check():
    str_check = d20_roll + stat_block_str(int)
    return str_check
    



# This set of functions is used for directions through the map
def move_all_dir():
    move = print(input("Which way would you like to continue. Right, Forward, Left, or Back? "))
    if (move == 'R' or move == 'r' or move == 'Right' or move == 'right'):
        print("You turn and follow the path to the right.")
    if (move == 'F' or move == 'f' or move == 'Forward' or move == 'forward'):
        print("You continue your way down the corridor.")
    if (move == 'L' or move == 'l' or move == 'Left' or move == 'left'):
        print("You turn and follow the path to the left.")
    if (move == 'B' or move == 'b' or move == 'Back' or move == 'back'):
        print("You turn around and head back the way you can to the previous room.")
    else:
        print("You stand a think about which way you would like to go...")
        move_all_dir()

def no_right_turn():
    move = print(input("Which way would you like to continue. Forward, Left, or Back? "))
    if (move == 'F' or move == 'f' or move == 'Forward' or move == 'forward'):
        print("You continue your way down the corridor.")
    if (move == 'L' or move == 'l' or move == 'Left' or move == 'left'):
        print("You turn and follow the path to the left.")
    if (move == 'B' or move == 'b' or move == 'Back' or move == 'back'):
        print("You turn around and head back the way you can to the previous room.")
    else:
        print("You stand a think about which way you would like to go...")
        no_right_turn

def no_left_turn():
    move = print(input("Which way would you like to continue. Right, Forward, or Back? "))
    if (move == 'R' or move == 'r' or move == 'Right' or move == 'right'):
        print("You turn and follow the path to the right.")
    if (move == 'F' or move == 'f' or move == 'Forward' or move == 'forward'):
        print("You continue your way down the corridor.")
    if (move == 'B' or move == 'b' or move == 'Back' or move == 'back'):
        print("You turn around and head back the way you can to the previous room.")
    else:
        print("You stand a think about which way you would like to go...")
        no_left_turn()

def T_intersection():
    move = print(input("Which way would you like to continue. Right, Left, or Back? "))
    if (move == 'R' or move == 'r' or move == 'Right' or move == 'right'):
        print("You turn and follow the path to the right.")
    if (move == 'L' or move == 'l' or move == 'Left' or move == 'left'):
        print("You turn and follow the path to the left.")
    if (move == 'B' or move == 'b' or move == 'Back' or move == 'back'):
        print("You turn around and head back the way you can to the previous room.")
    else:
        print("You stand a think about which way you would like to go...")
        T_intersection()

def dead_end():
    move = print(input("The bath before you ends in a dead end. Press 'B' to go back. "))
    if (move == 'B' or move == 'b' or move == 'Back' or move == 'back'):
        print("You turn around and head back the way you can to the previous room.")
    else:
        print("You stand a think about which way you would like to go...")
        dead_end()

def left_turn_only():
    move = print(input("You have come to a bend in the corridor. The path continues to the left? Do you continue to follow or turn back? L or B: "))
    if (move == 'L' or move == 'l' or move == 'Left' or move == 'left'):
        print("You turn and follow the path to the left.")
    if (move == 'B' or move == 'b' or move == 'Back' or move == 'back'):
        print("You turn around and head back the way you can to the previous room.")
    else:
        print("You stand a think about which way you would like to go...")
        left_turn_only()

def right_turn_only():
    move = print(input("You have come to a bend in the corridor. The path continues to the right? Do you continue to follow or turn back? R or B: "))
    if (move == 'R' or move == 'r' or move == 'Right' or move == 'right'):
        print("You turn and follow the path to the right.")
    if (move == 'B' or move == 'b' or move == 'Back' or move == 'back'):
        print("You turn around and head back the way you can to the previous room.")
    else:
        print("You stand a think about which way you would like to go...")
        no_left_turn()

def forward_only():
    move = print(input("The path stretches out before you. Do you keep going or go back? Forward or Back: "))
    if (move == 'F' or move == 'f' or move == 'Forward' or move == 'forward'):
        print("You continue down the path")
    if (move == 'B' or move == 'b' or move == 'Back' or move == 'back'):
        print("You turn around and head back the way you can to the previous room.")
    else:
        print("You stand a think about which way you would like to go...")
        forward_only()


