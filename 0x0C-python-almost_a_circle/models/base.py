#!/usr/bin/python3
""" class Base """
from os import path
import json
import csv


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
        """Writes JSON string representation of list_objs to a file"""
        dict_list = [x.to_dictionary() for x in list_objs]
        my_fjson = cls.__name__ + ".json"  # create name

        with open(my_fjson, "w") as newfile:
            newfile.write(cls.to_json_string(dict_list))
            # json.dump(cls.to_json_string(dict_list), newfile)
            newfile.close()

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the list of
        the JSON string representation
        Args:
            @json_string: string representing a list of dictionaries
        """
        if json_string is None or []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method that returns an instance with all
        attributes already set
        Args:
            @cls
            @dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """ class method that returns a list of instances """
        insta_list = []  # init empty list
        finame = cls.__name__ + ".json"

        if not path.exists(finame):
            return insta_list

        with open(finame) as myfile:  # open in mode "r" default
            data_file = cls.from_json_string(myfile.read())
            for items in data_file:
                insta_list.append(cls.create(**items))
        return insta_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes in CSV
        DictWriter: Create an object which operates like a regular
        writer but maps dictionaries onto output rows

        * fieldnames = ['first_name', 'last_name']
        * writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        """
        dict_list = [x.to_dictionary() for x in list_objs]
        filecsv = cls.__name__ + ".csv"  # create name
        if cls.__name__ == "Rectangle":
            attri_list = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            attri_list = ["id", "size", "x", "y"]

        with open(filecsv, "w") as newfile:
            writer = csv.DictWriter(newfile, fieldnames=attri_list)
            writer.writeheader()
            writer.writerows(dict_list)

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in CSV """
        insta_list = []  # init empty list
        finame = cls.__name__ + ".json"

        if not path.exists(finame):
            return insta_list

        with open(finame) as myfile:  # open in mode "r" default
            reader = csv.DictReader(myfile)

            for row in reader:  # catch row {key:value}
                row = {key: int(row[key]) for key in row.key()}
                insta_list.append(cls.create(**row))  # add to list
        return insta_list

# End base file
