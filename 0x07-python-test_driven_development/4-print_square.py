#!/usr/bin/python3
"""
a function that prints a square with the character #
"""


def print_square(size):
    """ Define the function """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for row in range(size):
            print("#" * size)
