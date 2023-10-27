#!/usr/bin/python3

class Square:
    """Definition of a class called Square"""

    def __init__(self, size=0):
        """
        Initialization of the square class.
        Args:
            size : size of a side of the square
        """
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ This method sets size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This method calculates the area of the square"""
        return (self.__size * self.__size)
