#!/usr/bin/python3
"""Defines a function that prints 'My name is <first name> <last name>'."""


def say_my_name(first_name, last_name=""):
    """Prints a name.

    Args:
        first_name (str): First name.
        last_name (str): Last name defaults to an empty string.

    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
