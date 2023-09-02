#!/usr/bin/python3
""" Square Class """


class Square:
    # Initialisation
    """ Square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a new Square.

        Args:
             size (int): Size of the new Square.
             position (tuple): The position where to print the square.
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__size = size

        if isinstance(position, tuple) and len(position) == 2:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    # Getter methods
    @property
    def size(self):
        """ Retrive the Size of the Square """
        return (self.__size)

    @property
    def position(self):
        """ retrive the Position of the Square """
        return (position)

    # Setter method
    @size.setter
    def size(self, size):
        """ Set the size of a Square """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__size = size

    @position.setter
    def position(self, position):
        """ Set the position od a Square """
        if isinstance(position, tuple) and len(position) == 2
        and all(isinstance(num, int) and num > 0 for num in position):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    # Methods
    def area(self):
        """ Return The area of the square """
        return (self.__size ** 2)

    def my_print(self):
        """ Print the Squar using the charagter # """
        for y in range(self.__position[1]):
            print("")
        if self.__size == 0:
            for x in range(self.__position[0]):
                print(" ", end="")
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
