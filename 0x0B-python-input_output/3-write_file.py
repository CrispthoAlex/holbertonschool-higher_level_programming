#!/usr/bin/python3
""" reads n lines of a text file (UTF8) and prints it to stdout """


def write_file(filename="", text=""):
    """
    Args:
        @filename: name of file to open from main
        @nb_lines: number of lines to read of file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
