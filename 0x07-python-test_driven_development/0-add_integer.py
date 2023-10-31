#!/usr/bin/python3

""" define the method """


def add_integer(a, b=98):
    """
    This method add two integers
    Args:
        a: The first integerr
        b: The second integer
    Returns:
        The sum of a and b
    Raises:
        TypeError: if any of the two arguments is not an integer
    """
    
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    """
    if both arguments are floats then they have
    to be casted
    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (a + b)
