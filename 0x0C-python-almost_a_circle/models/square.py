#!/usr/bin/python3

""" Import from rectangle so as to inherit"""


from models.rectangle import Rectangle

""" Create class Square that inherits from rectangle """


class Square(Rectangle):
    """ Define class method """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ size getter """
        return (self.width)

    @size.setter
    def size(self, data):
        """ Size setter """
        self.width = data
        self.height = data

    def update(self, *args, **kwargs):
        """ public method that sets attributes with
        args and kwargs
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ This method returns a dictionary representation of the square """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
