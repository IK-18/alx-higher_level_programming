#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """Defines a square

    Attributes:
        size (int): size of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square

        Args:
            size (int): size of the square
            position (tuple): coordinates of the square

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: gets the size of current square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: gets the coordinates of the current square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return

        for i in range(0, self.__posiiton[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
