#!/usr/bin/python3
""" Base Class """


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
