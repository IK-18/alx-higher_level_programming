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
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
