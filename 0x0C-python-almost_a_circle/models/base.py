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
        This method tconverts Json string to file
        """
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        file_name = f"{class_name}.json"
        obls = []
        for object in list_objs:
            ob = object.to_dictionary()
            obls.append(ob)
        json_string = cls.to_json_string(obls)
        with open(file_name, mode='w') as file:
            file.write(json_string)
