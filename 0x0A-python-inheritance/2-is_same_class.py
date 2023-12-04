#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise, returns False.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class; False otherwise.
    """
    return type(obj) is a_class
