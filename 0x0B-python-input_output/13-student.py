#!/usr/bin/python3
"""
class Student that defines a student by:

Public instance attributes:
first_name
last_name
age
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation
        of a Student instance
        """
        if attrs is None:
            return self.__dict__
        if all(attrs):
            my_dic = {}
            for elements in attrs:
                if elements in self.__dict__ and type(elements) == str:
                    my_dic[elements] = self.__dict__[elements]
            return my_dic

    def reload_from_json(self, json):
        """  replaces all attributes of the Student instance """
        if json is dict:
            for e_key, e_value  in json.items():
                self.__dic__[e_key] = e_value
