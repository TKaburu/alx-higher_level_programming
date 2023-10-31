#!/usr/bin/python3
"""
This function prints a full name
"""


def say_my_name(first_name, last_name=""):
    """ full name function"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
