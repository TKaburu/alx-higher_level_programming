#!/usr/bin/python3

"""
This method divides all elements matrix
"""

def matrix_divided(matrix, div):
    """
    Args:
        matrix : Lists of lists of integer or floats
        Div : Float or int that is used for the division
        
        Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    
    Returns:
        new matrix from the result of the diviions
    """
    if matrix is None or not matrix or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif type(div) is not  int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

