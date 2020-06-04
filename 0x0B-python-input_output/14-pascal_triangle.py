#!/usr/bin/python3
"""
function that returns a list of lists of integers
representing the Pascals triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascals triangle
    Args: @n:
    """
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    pascal = [[1], [1, 1]]
    n_list = []

    for row in range(2, n):
        n_list = [1]
        for line in range(1, row):
            element = pascal[row - 1][line - 1] + pascal[row - 1][line]
            n_list.append(element)
        n_list.append(1)
        pascal.append(n_list)

    return pascal
