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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of current square

        Returns:
            area of current square (size^2)

        """
        return self.__size ** 2

    def __eq__(self, other):
        """Defines the == comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison"""
        rturn self.area() >= other.area()
