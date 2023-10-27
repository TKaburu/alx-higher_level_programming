#!/usr/bin/python3

"""A module square"""


class Square:
    """ Defination of a class called square """

    def __init__(self, size=0):
        """
        Initialization of the square class.
        Args:
            size : size of a side of the square
        Raises:
            TypeError: if the size is not an int
            ValueError: if the size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This method calculates area of a square"""
        return (self.__size * self.__size)
