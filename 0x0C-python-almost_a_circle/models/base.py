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
        """
        This method returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This class method writes the JSON string representation
        of list_objs to a file
        """
        filename = cls.__name__ + ".json"

        with open(filename, mode='w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        This method lists the JSON string representation
        """
        if json_string is None:
            return []
        if json_string == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ This method sets all attributes """
       if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)

        instance.update(**dictionary)
        return (instance)
