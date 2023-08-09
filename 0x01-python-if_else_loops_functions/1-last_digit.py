#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastDigit = abs(number) % 10
elif number < 0:
    lastDigit = - (abs(number) % 10)
print(f"Last digit of {number:d} is {lastDigit:d} ", end="")
if abs(lastDigit) > 5:
    print(f"and is greater than 5")
elif abs(lastDigit) == 0:
    print(f"and is zero")
elif abs(lastDigit) < 6 and lastDigit != 0:
    print(f"and is less than 6 and not 0")
