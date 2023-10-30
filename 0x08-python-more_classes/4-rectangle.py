#!/usr/bin/python3

""" Defination of class """


class Rectangle:
    """
    Arg:
        width: The width of the rectangle
        height : The height of the rectangle
    Raises:
          TypeError: if width or height are not integers
          ValueError: if height or width are less than 0
    """

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.height = height

    @property
    def width(self):
        """ width property getter """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method calculates area of a square"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ This method returns the rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.width + self.height))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for t in range(self.height):
            rectangle_str += "#" * self.width
            if t < self.height - 1:
                rectangle_str += "\n"
        return (rectangle_str)

    def __repr__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return (f"Rectangle({self.width}, {self.height})")
