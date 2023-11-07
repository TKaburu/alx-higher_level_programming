#!/usr/bin/python3

""" Import Json module """


import json


def load_from_json_file(filename):
    """ This function  creates an Object from a “JSON file” """
    with open(filename, encoding="utf-8") as file_content:
        print(json.load(file_content))
