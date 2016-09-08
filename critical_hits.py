#!/usr/bin/python3
import random

dice_numbers = []

def dice_roll():
    dice = random.randint(1,6)
    max_roll = 6
    dice_numbers.append(dice)
    while dice == max_roll:
        dice = random.randint(1,6)
        dice_numbers.append(dice)
    return dice

dice_roll()
print(dice_numbers)

hit = str(sum(dice_numbers))
print('You hit for ' + hit)
