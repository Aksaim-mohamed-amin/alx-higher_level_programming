#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """ Define a BaseGeometry class """

    def area(self):
        """ Raise an exception with the area not emplimented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate value """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value < 1:
            raise ValueError("<name> must be greater than 0")

        self.name = name
        self.value = value
