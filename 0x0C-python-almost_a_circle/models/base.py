#!/usr/bin/python3
""" class Base """
import json


class Base:
    """
    The goal of it is to manage id attribute in all your future
    classes and to avoid duplicating the same code
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Method constructor. Initialize Base Module """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dict):
        """ Returns JSON string representation of list_dictionaries """
        if not list_dict:
            return "[]"
        return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        pass
