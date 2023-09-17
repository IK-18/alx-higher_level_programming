#!/usr/bin/python3
"""Defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Implements the Square class

    Properties:
        size (int): size of the square
        x (int): x-axis position of the square
        y (int): y-axis position of the square
        id (int): id of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square

        Args:
            size (int): size of the square
            x (int): x-axis position of the square
            y (int): y-axis position of the square
            id (int): id of teh square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets/Sets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square

        Args:
            *args (ints): new attribute values
                - id (int): id of the square
                - size (int): size of the square
                - x (int): x-axis position of the square
                - y (int): y-axis position of the square
            **kwargs (dict): New key: value pairs of attributes
        """
        if args and len(args) != 0:
            attr = 0
            for arg in args:
                if attr == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif attr == 1:
                    self.size = arg
                elif attr == 2:
                    self.x = arg
                elif attr == 3:
                    self.y = arg
                attr += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns the print() and str() representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
