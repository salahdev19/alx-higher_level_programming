#!/usr/bin/python3

""" Class Rectangel """


class Rectangle:

    """
    initialize rectangle:
    private instance property: width (int)
    private instance property: height (int)
    """
    def __init__(self, width=0, height=0):
        """ constructor method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width retrieve """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        self.__width = value
        if value < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        self.__height = value
        if value < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    def area(self):
        """ find rectangle area """

