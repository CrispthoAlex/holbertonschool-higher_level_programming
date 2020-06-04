#!/usr/bin/python3
"""
function that inserts a line of text to a file, after each
line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file
    Args:
        @filename: name of file
        @search_string: searched string in file
        @new_string: new string adds after searched string
    """
    with open(filename, mode="r+", encoding="utf-8") as file:
        string_line = ""  # string to generate full file
        for fline in file:  # fline is my line in my file
            string_line += fline
            if search_string in fline:
                string_line += new_string
        file.seek(0)  # position 0 of my file
        file.write(string_line)  # overwrite all my file
