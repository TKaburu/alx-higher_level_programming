#!/usr/bin/python3

""" import Json module """


import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This method returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
