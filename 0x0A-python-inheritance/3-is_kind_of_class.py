#!/usr/bin/python3

"""
Checks instance
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns true if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """
    return (isinstance(obj, a_class))
