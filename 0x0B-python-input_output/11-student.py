#!/usr/bin/python3

""" Define class Student """


class Student:
    def __init__(self, first_name, last_name, age):
        """ Public instance with attributs """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrives a dictionary """
        dictionary = {}
        if attrs is None:
            for key in self.__dict__:
                dictionary[key] = getattr(self, key)
        else:
            for key in attrs:
                if hasattr(self, key):
                    dictionary[key] = getattr(self, key)
        return dictionary
        return (self.__dict__)

    def reload_from_json(self, json):
        """ This is a public method """
        for t in json:
            self.__dict__[t] = json[t]
