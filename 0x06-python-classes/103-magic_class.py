#!/usr/bin/python3

import math


class MagicClass:
    """Defines a circle

    Attributes:
        radius (int or float): radius of the circle

    """

    def __init__(self, radius=0):
        """Initializes the MagicClass

        Args:
            radius (int or float): rudius of the new MagicClass

        """

        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the MagicClass"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the MagicClass"""
        return 2 * math.pi * self.__radius
