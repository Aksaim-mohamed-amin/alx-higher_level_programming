#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """ Print the full name

    Args:
      first_name (str): Frist name.
      last_name (str) (optionall): last name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
