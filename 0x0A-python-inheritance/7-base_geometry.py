#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry:
    """Defines an instance of BaseGeometry

    Raises:
        Exception: area() is not implemented
    """

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name (string): name
            value (int): value to be validated

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
