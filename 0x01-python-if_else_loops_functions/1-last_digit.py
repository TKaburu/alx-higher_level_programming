#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if number < 0:
    print(f"Last digit of {number:d} is {ld:d} and is ")
if ld > 5:
    print("greater than 5")
if ld == 0:
    print("0")
else:
    print("less than 6 and not 0")
