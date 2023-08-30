#!/usr/bin/python3
class Square:
    """Defines a square

    Attributes:
        size (int): size of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square

        Args:
            size (int): size of the square
            position (tuple): coordinates of the square

        """
        self.size = size

    @property
    def size(self):
        """int: gets the size of current square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: gets the coordinates of the current square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of current square

        Returns:
            area of current square (size^2)

        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__posiiton[1]):
                print()
            for i in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
