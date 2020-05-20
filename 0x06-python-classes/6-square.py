#!/usr/bin/python3
"""
Size validation mandatory: Write a class Square that defines a square by:
(based on 1-square.py)

* Private instance attribute: size
  - property def size(self): to retrieve it
  - property setter def size(self, value): to set it:
    + size must be an integer, otherwise raise a TypeError exception with the
 message size must be an integer
    + if size is less than 0, raise a ValueError exception with the message
 size must be >= 0
* Private instance attribute: position:
  - property def position(self): to retrieve it
  - property setter def position(self, value): to set it:
    + position must be a tuple of 2 positive integers, otherwise raise a
      TypeError exception with the message position must be a tuple of 2
      positive integers

* Instantiation with optional size: def __init__(self, size=0):
* Instantiation with optional size and optional position:
   def __init__(self, size=0, position=(0, 0)):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square
 with the character #:
  - if size is equal to 0, print an empty line
  - position should be use by using space - Dont fill lines by spaces when
    position[1] > 0
* You are not allowed to import any module
"""


class Square:
    """ init __size constructor and area() method """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is tuple and len(position) == 2\
            and type(position[0]) is int and type(position[1]) is int\
                and position[0] >= 0 and position[1] >= 0:
                    self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ area method """
        squasize = self.__size
        return (squasize ** 2)

    @property
    def size(self):
        """ getter size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter position"""
        if type(value) is tuple and len(value) == 2\
            and type(value[0]) is int and type(value[1]) is int\
                and value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """ prints square with character # """
        squapri = self.__size
        if squapri > 0:
            print("\n" * self.__position[1], end="")
            for i in range(squapri):
                print(" " * self.__position[0], end="")
                print("#" * squapri)
        else:
            print()
