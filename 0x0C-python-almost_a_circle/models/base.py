#!/usr/bin/python3
"""Defines a base class."""


class Base:
    """Base Parent.

    This is the Parent for all other classes*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class Base.

        Args:
            id (int): The identity of the child.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
