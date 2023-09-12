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
