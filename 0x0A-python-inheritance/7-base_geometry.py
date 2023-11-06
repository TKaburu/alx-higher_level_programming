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
