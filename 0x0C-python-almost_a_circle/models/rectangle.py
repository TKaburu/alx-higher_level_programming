#!/usr/bin/python3

""" Define parent class Base """


class Base:
    """ Private attribute """
    __nb_objects = 0

    """ Define method """

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """
    This is a child class inheriting from
    class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ This is the width getter """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ This is the width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ This is the height getter """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ This is the height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ This is x getter """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ This is x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ This is y getter """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ This is y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ This method gets the area value of the triangle """
        return (self.__height * self.__width)

    def display(self):
        """ prints Rectangle instance with the character # """
        for k in range(self.y):
            print()
        for k in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return (
            f"[Rectangle] ({self.id}) {self.x} / {self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """ This method assigns an argument
        to each attribute based on keywords
        """
        if args:
            super().update(*args)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ This method returns a dictionary representation of a rectangle """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
