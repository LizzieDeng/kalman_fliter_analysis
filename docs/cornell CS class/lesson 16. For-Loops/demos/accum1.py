"""
A module with with two list functions.

These functions have been fully implemented.

Author: Walker M. White
Date:   April 15, 2019
"""


def sum(lst):
    """
    Returns: the sum of all elements in the list

    Example: sum([1,2,3]) returns 6
             sum([5]) returns 5

    Parameter lst: the list to sum
    Precondition: lst is a nonempty list of numbers
    (either floats or ints)
    """
    result = 0    # Accumulator

    for x in lst:
        result = result+x

    return result


def num_ints(lst):
    """
    Returns: the number of ints in the list

    Example: num_ints([1,2.0,True]) returns 1

    Parameter lst: the list to count
    Precondition: lst is a list of any mix of types
    """
    result = 0    # Accumulator

    for x in lst:
        if type(x) == int:
            result = result+1

    return result
