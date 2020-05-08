#!/bin/python3
def roman_to_int(roman_string):
    summ = 0
    if roman and type(roman) is str:
        rom = {'I': 1, 'V': 5, 'X': 10,
               'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for idx, value in enumerate(roman):
            if idx < len(roman) - 1 and rom[roman[idx]] < rom[roman[idx+1]]:
                summ -= rom[roman[idx]]
            else:
                summ = summ + rom[roman[idx]]
        return summ
    return 0
