#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number < 0:
    lastDigit = - lastDigit
print(f"Last digit of {number:d} is {lastDigit:d} ", end="")
if lastDigit > 5:
    print(f"and is greater than 5")
elif lastDigit == 0:
    print(f"and is 0")
elif lastDigit < 6 and lastDigit != 0:
    print(f"and is less than 6 and not 0")
