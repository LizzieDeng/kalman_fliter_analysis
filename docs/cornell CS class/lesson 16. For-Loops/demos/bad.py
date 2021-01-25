"""
Module to demonstrate how to modify a list in a for-loop.

This version of the function does not work.  Put it in the
Python Tutor to see why.

Author: Walker M. White (wmw2)
Date:   May 24, 2019
"""


def add_one(lst):
    """
    (Procedure) Adds 1 to every element in the list

    Example: If a = [1,2,3], add_one(a) changes a to [2,3,4]

    Parameter lst: The list to modify
    Precondition: lst is a list of all numbers (either floats
    or ints), or an empty list
    """
    for x in lst:
        x = x+1
    # procedure; no return


# Add this if using the Python Tutor
#a = [3,2,1]
#add_one(a)
