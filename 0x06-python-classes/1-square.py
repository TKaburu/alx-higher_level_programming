#!/usr/bin/python3
"""Define class square"""


class Square:
    """
    This square class has a private attribute size
    Arg:
        size : This is the size of a side of a square
    """

    def __init__(self, size):
        """ Initializing the square class """

        self.__size = size
