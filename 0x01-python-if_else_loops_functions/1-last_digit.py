#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lastNum = 0

if number < 0:
    lastNum = number % -10
else:
    lastNum = number % 10

if lastNum > 5:
    print(f"Last digit of {number} is {lastNum} and is greater than 5")
elif lastNum < 6 and lastNum != 0:
    print(f"Last digit of {number} is {lastNum} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is 0 and is 0")
