#!/usr/bin/python3

"""A module square"""


class square:
    """
    Define a class
    This clas check for the data
    type and has  private attribute
    """
        
    def __init__(self, size=0):
         if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
