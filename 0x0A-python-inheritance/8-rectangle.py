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
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
