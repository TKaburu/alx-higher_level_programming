#!/usr/bin/python3

""" import os and Json module """


import json
import os

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

        file_name = cls.__name__ + ".json"
        if list_objs is None:
            string = "[]"
        else:
            to_dict_list = []
            for object in list_objs:
                to_dict_list.append(i.to_dictionary())
            string = cls.to_json_string(to_dict_list)

        with open(file_name, 'w', encoding="utf-8") as file:
            written_string = file.write(string)

        return written_string

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

    @classmethod
    def load_from_file(cls):
        """
            files to instance
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in list_dicts]
                return instances
        except FileNotFoundError:
            return []
