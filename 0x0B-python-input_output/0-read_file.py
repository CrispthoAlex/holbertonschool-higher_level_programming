#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout  """


def read_file(filename=""):
    """
    read_file(filename=""):
    Args: @filename: name of file to open from main
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
