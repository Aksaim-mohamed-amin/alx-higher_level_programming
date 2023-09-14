#!/usr/bin/python3
""" serialize a class """


def class_to_json(obj):
    """ Save a class to a json file

    Args:
      obj (class): Class to serialize.
    """
    return (obj.__dict__)
