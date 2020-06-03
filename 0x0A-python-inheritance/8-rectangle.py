#!/usr/bin/python3
"""
import Class BaseGeometry

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class BaseGeometry
    """

    def __init__(self, width, height):
        """
        * Instantiation with width and height:
            Validated by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
