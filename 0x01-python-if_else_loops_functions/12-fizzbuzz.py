#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        getout = ""
        if i % 3 == 0:
            getout += "Fizz"
        if i % 5 == 0:
            getout += "Buzz"
        if getout == "":
            getout = i
        print(getout, end=" ")
