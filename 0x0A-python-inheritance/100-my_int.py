#!/usr/bin/python3
"""Defines a MyInt class"""


class MyInt(int):
    """Implements a subclass of int with inverted == and != operators"""

    def __eq__(self, value):
        """Inverts to != operator"""
        return self.real != value

    def __ne__(self, value):
        """Inverts to == operator"""
        return self.real == value
