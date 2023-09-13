#!/usr/bin/python3
"""Defines the Student class"""


class Student:
    """Implements the student class

    Properties:
        first_name (str): first name of the student
        last_name (str): last name of the student
        age (int): age of the student
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the student

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """Retrieves a dictionary representatoin of a Student instance

        If attrs is a list of strings, represents only those attributes
        included in the list

        Args:
            attrs (list): (Optional) attributes to be included
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
