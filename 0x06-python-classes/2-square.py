#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """Defines a square

    Attributes:
        __size (int): size of the square

    """

    def __init__(self, size=0):
        """Initializes a new square

        Args:
            size (int): size of the square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
