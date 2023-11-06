#!/usr/bin/python3

""" Define the class """


class BaseGeometry:
    """ Define the method """
    def area(self):
        """This is a public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A public instance that validate value
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """ Define a child class Rectangle"""
    def __init__(self, width, height):
        """
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
