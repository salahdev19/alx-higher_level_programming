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
        return self.__height * self.__width

    def perimeter(self):
        """ find perimeter of rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((2 * self.__height)+(2 * self.__width))

    def __str__(self):
        """ class str """
        if self.__height == 0 or self.__width == 0:
            return ""

        print_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                print_str += "#"
            if i != self.__height - 1:
                print_str += "\n"
        return print_str

    def __repr__(self):
        """ return a string representation of an rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)
