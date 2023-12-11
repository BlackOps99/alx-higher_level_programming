#!/usr/bin/python3
"""Defines a base class."""
from models.base import Base


class Rectangle(Base):
    """Base Parent.

    This is the Parent for all other classes*.

    Private Class Attributes:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        x (int): The x coordinate of the new Rectangle.
        y (int): The y coordinate of the new Rectangle.
        id (int): The identity of the Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the Rectangle.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the Rectangle."""
        self.__width = value

    @property
    def height(self):
        """get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the Rectangle."""
        self.__height = value

    @property
    def x(self):
        """get the coordinate x of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """set the coordinate x of the Rectangle."""
        self.__x = value

    @property
    def y(self):
        """get the coordinate y of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """set the coordinate y of the Rectangle."""
        self.__y = value
