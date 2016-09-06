#!/usr/bin/python3

import sys
import random
import os
os.system('clear')

print("Rock: 1")
print("Paper: 2")
print("Scissors: 3")
choice = input("\nMake your selection: ")
rnum = random.randint(1,3)

if choice == "1":
    choice = "Rock"
elif choice == "2":
    choice = "Paper"
elif choice == "3":
    choice = "Scissors"
else:
    sys.exit("Please select from the list")


if rnum == 1:
    rnum = "Rock"
elif rnum == 2:
    rnum = "Paper"
elif rnum == 3:
    rnum = "Scissors"

print("You selected: " + choice)
print("Opponent chooses: " + rnum)

if choice == rnum:
    print("Draw!")
elif choice == "Rock" and rnum == "Scissors":
    print("You win!")
elif choice == "Rock" and rnum == "Paper":
    print("You lose!")
elif choice == "Scissors" and rnum == "Paper":
    print("You win!")
elif choice == "Scissors" and rnum == "Rock":
    print("You lose!")
elif choice == "Paper" and rnum == "Rock":
    print("You win!")
elif choice == "Paper" and rnum == "Scissors":
    print("You lose!")
