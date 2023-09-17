#!/usr/bin/python3
"""Defines the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Implements the Rectangle class

    Properties:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x-axis position
        y (int): y-axis position
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectanlge
            x (int): x-axis position
            y (int): y axis position
            id (int): id of the class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets/Sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets/Sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets/Sets the x-axis position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets/Sets the y-axis position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle to stdout using the '#' character"""
        if self.width == 0 or self.height == 0:
            print()
            return
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Update the properties of the rectangle

        Args:
            *args (ints): New attribute values
                - id (int): id of the rectangle
                - width (int): width of the rectangle
                - height (int): height of the rectangle
                - x (int): x-axis position of the rectangle
                - y (int): y-axis position of the rectangle
            **kwargs (dict): New key: value pairs of attributes
        """
        if args and len(args) != 0:
            attr = 0
            for arg in args:
                if attr == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif attr == 1:
                    self.width = arg
                elif attr == 2:
                    self.height = arg
                elif attr == 3:
                    self.x = arg
                elif attr == 4:
                    self.y = arg
                attr += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() epresentation of the rectangle"""
        return "[Rectangle ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                     self.y, self.width,
                                                     self.height)
