#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: ., ? and :
>>> text_indentation()

"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :
    Text identation module
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char_spe = [':', '.', '?']
    init_line = True

    for char in text:
        if char == " " and init_line is True:
            continue
        if char in char_spe:
            print(char, end="")
            print('\n')
            init_line = True
        else:
            print(char, end="")
            init_line = False
