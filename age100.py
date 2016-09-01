#!/usr/bin/python3

name = input("Hello what is your name?: ")
print("Hello " + name)

age = input("How old are you?: ")
age = int(age)

years_left = 100 - age
date_100 = 2016 + years_left

print(str(name) + " you will turn 100 years old in " + str(date_100))
