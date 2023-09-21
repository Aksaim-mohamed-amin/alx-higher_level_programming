#!/usr/bin/python3
""" Base Class """
import json


class Base:
    """ define the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a new instance of the object Base

        Args:
          id: User id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # to json string
    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON serialization of list_dictionaries.

        Args:
           list_dictionaries (list of dict): List of dictionary to convert.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")

        return (json.dumps(list_dictionaries))

    # save to a file
    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file.

        Args:
          list_objs: list of instances who inherits of Base.
        """
        fileName = cls.__name__ + ".json"

        list_dict = []
        if list_objs is not None:
            list_dict = [o.to_dictionary() for o in list_objs]

        with open(fileName, mode='w', encoding="utf-8") as jsonFile:
            jsonFile.write(Base.to_json_string(list_dict))

    # from json string
    def from_json_string(json_string):
        """returns the list of the JSON string representation of json_string"""
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    # Create a new instance
    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10)
        else:
            dummy = cls(10)

        dummy.update(**dictionary)

        return (dummy)
