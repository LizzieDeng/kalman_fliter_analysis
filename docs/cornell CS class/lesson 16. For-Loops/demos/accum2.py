"""
A module with with three loop-based functions.

These functions show how to design with accumulators.  These
functions have been fully implemented.

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
    # Accumulator
    result = ''

    for x in s:
        if x != ' ':
            result = result+x

    return result


def reverse(s):
    """
    Returns: copy with s with characters reversed.

    Example: reverse('hello’) returns 'olleh'

    Parameter s: the text to reverse
    Precondition: s is a (possibly empty string)
    """
    # Accumulator
    result = ''

    for x in s:
        result = x+result

    return result


def copy_add_one(lst):
    """
    Returns: copy of lst with 1 added to every element

    Example: add_one([1,2,3,1]) returns [2,3,4,2]

    Parameter lst: The list to copy
    Precondition: lst is a list of all numbers (either floats
    or ints), or an empty list
    """
    copy = []  # accumulator
    for x in lst:
        x = x+1
        copy = copy+[x]       # add to end of copy
    return copy
