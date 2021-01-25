"""
A module to show how global variables work

Author: Walker M. White (wmw2)
Date:   August 25, 2017 (Python 3 Version)
"""

a = 4 # Global variable

def get_a():
    """
    Returns the value of the global variable a
    """
    return a


def change_a():
    """
    Returns the value of the local variable a
    """
    a = 3.5
    return a
