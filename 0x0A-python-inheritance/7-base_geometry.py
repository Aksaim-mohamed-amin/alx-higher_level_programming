#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """ Define a BaseGeometry class """

    def area(self):
        """ Raise an exception with the area not emplimented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate value

        Args:
          name: The name of the parameter.
          value: The value to validate.

        Raises:
          TypeErro: if value is ot integer.
          ValueError: if value is equal or less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value < 1:
            raise ValueError("<name> must be greater than 0")
