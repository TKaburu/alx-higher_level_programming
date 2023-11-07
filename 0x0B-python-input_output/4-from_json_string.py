#!/usr/bin/python3

""" Import json module"""

import json


def from_json_string(my_str):
    """ converts KSON string to python object"""
    return (json.loads(my_str))
