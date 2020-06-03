#!/usr/bin/python3
""" reads n lines of a text file (UTF8) and prints it to stdout """


def read_lines(filename="", nb_lines=0):
    """
    Args:
        @filename: name of file to open from main
        @nb_lines: number of lines to read of file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        list_lines = list(file)  # list of lines of file
        lines_cont = len(list_lines)  # lenght of list of lines

        if nb_lines <= 0 or nb_lines > lines_cont:
            for line in list_lines:
                print(line, end="")
        else:
            count = 1
            for line in list_lines:
                print(line, end="")
                count += 1
                if count > nb_lines:
                    break
