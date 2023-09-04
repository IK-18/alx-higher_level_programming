#!/usr/bin/python3
"""Defines a function that adds 2 integers."""


def add_integer(a, b=98):
    """Returns the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Args:
        a (int): First integer value.
        b (int): Second integer value that defaults to 98.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.

    Returns:
        The value of the int addition of a and b.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
