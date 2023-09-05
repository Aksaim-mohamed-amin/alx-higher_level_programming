#!/usr/bin/python3
def print_square(size):
    """ Print a square using the character "#"

    Args:
      size: Size of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
