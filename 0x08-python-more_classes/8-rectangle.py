#!/usr/bin/python3
""" Rectangle Class. """


class Rectangle:
    """ Represent a rectangle.

    Attributes:
       width: width of the rectangle.
       height: hieght of the traingle.
    """

    # Number of instances
    number_of_instances = 0

    # Print symbol
    print_symbol = "#"

    # Initiaisation
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

        Rectangle.number_of_instances += 1

    # width Getter and Setter
    @property
    def width(self):
        """ Retrive the width of rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        self.__width = value

    # height Getter and Setter
    @property
    def height(self):
        """ Retrive the height of rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        self.__height = value

    # Other methods
    def area(self):
        """ Return the area of the rectangle. """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return the perimeter of rectangle.
        if width or height is equal to 0 return 0
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Produce a string representation of the object """
        if self.__width == 0 or self.__height == 0:
            return ("")
        row = str(self.print_symbol) * self.__width
        return ('\n'.join([row] * self.__height))

    def __repr__(self):
        """ Return a reprsentation of the rectangle """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """ Print a messege when deleting a rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
