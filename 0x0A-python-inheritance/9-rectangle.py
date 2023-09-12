#!/usr/bin/python3
"""Defines a Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implements a Rectangle subclass of BaseGeometry

    Properties:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, width, height):
        """Initializes a new Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("heigth", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Returns:
            Area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
