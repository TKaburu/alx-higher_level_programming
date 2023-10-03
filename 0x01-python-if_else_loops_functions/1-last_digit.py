#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10 #using modulas to find lst digit 
if number < 0:
    ld = -ld
print(f"Last digit of {number:d} is {ld:d} and is ")
if ld > 5:
    print("greater than 5")
elif ld == 0:
    print("0")
else:
    print("less than 6 and not 0")
