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

    # to_json_string
    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries.

        Args:
           list_dictionaries (list of dict): List of dictionary to convert.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ([])

        return (json.dumps(list_dictionaries))
