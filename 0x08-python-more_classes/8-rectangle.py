#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """A rectangle class

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
        number_of_instances (int): number of instances of rectangle
        print_symbol (any): symbol used for string representation

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle

        Raises:
            TypeError: If either arg is not a Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Returns the informal printable string representation"""

        if self.__width == 0 or self.__height == 0:
            return ""
        tmp = []
        for i in range(self.__height):
            for j in range(self.__width):
                tmp.append(str(self.print_symbol))
            if i != self.__height - 1:
                tmp.append("\n")
        return ("".join(tmp))

    def __repr__(self):
        """Returns the official printable string representation"""

        string = "Rectangle(" + str(self.__width)
        string += ", " + str(self.__height) + ")"
        return string

    def __del__(self):
        """Prints a message when deleted"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
