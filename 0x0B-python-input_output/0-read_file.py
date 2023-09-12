#!/usr/bin/python3
""" Read File mudual """


def read_file(filename=""):
    """ Read from a file and print it content

    Args:
       filename (string): File name to read from.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
