#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj: The object to look up.

    Returns:
    - A list of strings representing attributes and methods.
    """
    return [attribute for attribute in dir(obj)]
