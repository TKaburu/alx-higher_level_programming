#!/usr/bin/python3

"""define class """


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

    def area(self):
        """Calculates area of rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """returns string of rectangle """
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))


class Square(Rectangle):
    """New class """
    def __init__(self, size):
        """ New method """
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
