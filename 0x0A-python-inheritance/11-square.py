#!/usr/bin/python3
"""Defines a Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Implements the Square class

    Properties:
        size (int): size of the square
    """

    def __init__(self, size):
        """Initializes a new Square

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Return the print() and str() representation of a Square"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
