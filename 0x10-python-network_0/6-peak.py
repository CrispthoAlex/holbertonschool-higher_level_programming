#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers.
Authors: Cirspthofer Ricnon - Maria Crespo
"""


def find_peak(list_of_integers):
    """
    Write a function that finds a peak in a list of unsorted integers.
    """

    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[1] <= list_of_integers[0]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    middle = len(list_of_integers) // 2
    if list_of_integers[middle] >= list_of_integers[middle - 1] and \
       list_of_integers[middle] >= list_of_integers[middle + 1]:
        return list_of_integers[middle]

    if list_of_integers[middle + 1] > list_of_integers[middle]:
        return(find_peak(list_of_integers[middle + 1:len(list_of_integers)]))

    if list_of_integers[middle - 1] > list_of_integers[middle]:
        return(find_peak(list_of_integers[0:middle]))
