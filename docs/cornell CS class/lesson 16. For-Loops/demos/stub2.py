"""
A module with with three loop-based functions.

These functions show how to design with accumulators.  These
functions are stubs and are not complete.

Author: Walker M. White
Date:   April 15, 2019
"""


def despace(s):
    """
    Returns: s but with its spaces removed

    Examples:
        despace('Hello World!') returns 'HelloWorld!'
        despace(' a b c d e ') returns 'abcde'

    Parameter s: the text to remove spaces
    Precondition: s is a string
    """
    # Create an empty string accumulator
    # For each character x of s
        # Check if x is a space
        # Add it to accumulator if not
    # Return accumulator


def reverse(s):
    """
    Returns: copy with s with characters reversed.

    Example: reverse('hello’) returns 'olleh'

    Parameter s: the text to reverse
    Precondition: s is a (possibly empty string)
    """
    # Create an empty string accumulator
    # For each character x of s
        # Add x to FRONT of accumulator
    # Return accumulator


def copy_add_one(lst):
    """
    Returns: copy of lst with 1 added to every element

    Example: add_one([1,2,3,1]) returns [2,3,4,2]

    Parameter lst: The list to copy
    Precondition: lst is a list of all numbers (either floats
    or ints)
    """
    # Create an empty list accumulator
    # For each element x of list
        # Add 1 to value of x
        # Add x to the accumulator
    # Return accumulator
