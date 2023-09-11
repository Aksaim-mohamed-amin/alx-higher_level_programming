#!/usr/bin/python3
""" Lookup modual """


def lookup(obj):
    """ returns the list of available attributes and methods of an object

    Args:
      obj (object): The object to return it attributes and methodes
    """
    return (dir(obj))
