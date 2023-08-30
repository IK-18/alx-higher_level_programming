#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """Defines a square

    Attributes:
        size (int): size of the square

    """

    def __init__(self, size=0):
        """Initializes a new square

        Args:
            size (int): size of the square

        """
        self.size = size

    @property
    def size(self):
        """int: gets the size of current square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(calue, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of current square

        Returns:
            area of current square (size^2)

        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
