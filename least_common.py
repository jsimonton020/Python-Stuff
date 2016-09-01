#!/usr/bin/python3

def get_numbers():
    with open("numbers.txt") as n:
      numbers = n.readline()
    return(numbers)

print(numbers)
