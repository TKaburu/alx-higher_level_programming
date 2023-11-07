#!/usr/bin/python3

""" Technical question """


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return ([])
    triangle = []
    for t in range(n):
        row = []
        for k in range(t + 1):
            if k == 0 or k == t:
                row.append(1)
            else:
                prev_row = triangle[t - 1]
                row.append(prev_row[k - 1] + prev_row[k])
        triangle.append(row)

    return (triangle)
