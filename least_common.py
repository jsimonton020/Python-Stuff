#!/usr/bin/python3

def get_numbers():
    with open("numbers.txt") as n:
        numbers = n.read().splitlines()
        lcd = []
        for i in numbers:
            x, y = i.split()
            x = int(x)
            y = int(y)
            small = min(x, y)
            for j in range(small, 1, -1):
                if x % j == 0 and y % j == 0:
                    lcd.append((x // j, y // j))
                    break
    return(lcd)

print (get_numbers())
