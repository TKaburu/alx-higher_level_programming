#!/usr/bin/python3

"""
This function returnshe dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """Define the function """
    return (obj.__dict__)
