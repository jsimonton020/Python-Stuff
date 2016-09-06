#!/usr/bin/python3

def get_numbers():
    with open("numbers.txt") as n:
        numbers = n.read().splitlines()
        lcd = []
        for i in numbers:
            num, den = i.split()
            num = int(num)
            den = int(den)
            small = min(num, den)
            for j in range(small, 1, -1):
                if num % j == 0 and den % j == 0:
                    lcd.append((num // j, den // j))
                    break
    return(lcd)

print (get_numbers())
