#!/usr/bin/python3
""" Define a MagicClass """

import math


class MagicClass:
    """ Magic Class """

    def __init__(self, radius=0):
        """ Initialize a MagicClass

        Args:
          radius (float or int): The raduis of the new cyrcle.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """ return thearea of the cyrcle """
        return (2 ** self.__radius * math.pi)

    def circumference(self):
        """ return the circumference of the cycle """
        return (2 * math.pi * self.__radius)
