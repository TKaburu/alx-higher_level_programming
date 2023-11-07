#!/usr/bin/python3

""" import json """


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as file_content:
        file_content.write(json.dumps(my_obj))
