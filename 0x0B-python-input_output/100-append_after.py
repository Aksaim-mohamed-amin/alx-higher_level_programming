#!/usr/bin/python3
""" Python out/in """


def append_after(filename="", search_string="", new_string=""):
    """ Append a new string after each line that contain a specific string.

    Args:
      filename: File name
      search_string: String to append after it line.
      new_string: New string to add.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
