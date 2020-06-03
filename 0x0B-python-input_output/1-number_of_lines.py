#!/usr/bin/python3
""" function that returns the number of lines of a text file  """


def number_of_lines(filename=""):
    """
    read_file(filename=""):
    Args: @filename: name of file to open from main
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return len(file.readlines())
