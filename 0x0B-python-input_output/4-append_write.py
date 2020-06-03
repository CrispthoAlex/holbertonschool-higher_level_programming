#!/usr/bin/python3
""" Appends a string at the end of a text file """


def append_write(filename="", text=""):
    """
    Returns the number of characters added
    Args:
        @filename: name of file to open from main
        @nb_lines: number of lines to read of file
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
