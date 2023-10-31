#!/usr/bin/python3

"""
define  class called LockedClass
"""


class LockedClass:
    """
    Locks the class for only 1 attribute
    """
    __slots__ = ['first_name']
