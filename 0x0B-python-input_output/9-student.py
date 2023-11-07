#!/usr/bin/python3

""" Define class Student """


class Student:
    def __init__(self, first_name, last_name, age):
        """ Public instance with attributs """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives a dictionary """
        return (self.__dict__)
