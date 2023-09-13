#!/usr/bin/python3
""" Json representation """
import json


def save_to_json_file(my_obj, filename):
    """ Write an object to a text file usinf json representation

    Args:
      my_obj: Object to serialized and safe.
      filename: Name of the file where to store the data.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
