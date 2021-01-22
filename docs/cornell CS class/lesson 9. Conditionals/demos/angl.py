"""
Functions to anglicize integers in the range 1..19

This is a simple example for now.  We will see a more complex
version of this later.

Author: Walker M. White
Date:   March 30, 2019
"""


def anglicize(n):
    """
    Returns: English equiv of n.

    Parameter: the integer to anglicize
    Precondition: n in 1..19
    """
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'

    # n = 19
    return 'nineteen'
