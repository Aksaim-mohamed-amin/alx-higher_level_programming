#!/usr/bin/python3
""" python to Jason string """
import json


def to_json_string(my_obj):
    """ Convert python data to a Json string.

    Args:
      my_obj (object): Object to convert.
    """
    return (json.dumps(my_obj))
