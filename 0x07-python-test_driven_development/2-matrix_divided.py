#!/usr/bin/python3
""" Define a function that devide a matrix. """

def matrix_divided(matrix, div):
    """ Divide all element of a matrix by a number

    Args:
      matrix (matrix): The matrix to devide.
      div (int): Divider to divid by.

    Return: new matrix.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [list(map(lambda num: round(num / div, 2), row)) for row in matrix]
