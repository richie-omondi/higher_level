#!/usr/bin/python3
"""
This is a module that defines a class Square
by: (2-square.py)
"""


class Square:
    """
    This is a module that defines a class Square

    Attributes:
        size (int): Length of one side of the square.
    """
    def __init__(self, size=0):
        """
        The __init__ method initializes the attributes whenever an object is instantiated

        Args:
            size (int): Length of one side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        Private instance attribute: size
        """
    def area(self):
        """
        Calculates the area of a square

        Returns:
            Area
        """
        return self.__size * self.__size
