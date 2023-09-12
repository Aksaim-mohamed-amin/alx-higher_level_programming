#!/usr/bin/python3
""" Write into a file """


def write_file(filename="", text=""):
    """ Write a string into a file
    Create if it doesnt exict and overide the old data
    if the file exict

    Args:
      filename (string): name of the file to write to.
      text (string): Content to write to the file.

    Return: the number of the character writen.
    """
    with open(filename, 'w') as f:
        return (f.write(text))
