#!/usr/bin/python3
"""Defines an Class Named MyList"""


class MyList(list):
    """a subclass of list"""

    def __init__(self):
        """initializes the object MyList"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
