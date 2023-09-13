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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representatoin of a Student instance"""
        return self.__dict__
