#!/usr/bin/python3
"""Defines an Class Named MyList"""


class MyList(list):
    """Sub Class for Build in List."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
