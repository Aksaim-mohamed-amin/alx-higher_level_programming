#!/usr/bin/python3
""" Rectangle Class. """


class Rectangle:
    """ Represent a rectangle.

    Attributes:
       width: width of the rectangle.
       height: hieght of the traingle.
    """

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle.

        Args:
             widht (int): width of the new rectangle.
             height (int): height of the new rectangle.
        """
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        self.__width = width

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        self.__height = height

    # width Getter and Setter
    @property
    def width(self):
        return (self.__size)

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        self.__width = value

    # height Getter and Setter
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        self.__height = value
