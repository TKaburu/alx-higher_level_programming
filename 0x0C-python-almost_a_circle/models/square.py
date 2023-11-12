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

