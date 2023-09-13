#!/usr/bin/python3
""" Pars a Json data """
import json


def from_json_string(my_str):
    """ Pars data from json string

    Args:
      my_str (str): String that contain the data.
    """
    return (json.loads(my_str))
