"""
A module showing off some classic for-loops

This module is for comparison with gens.py.  This
module shows the old way of doing things.

Author: Walker M. White (wmw2)
Date: October 28, 2020
"""


def add_one(input):
    """
    Returns the list with 1 added to every element of input

    Example: add_one([1,2,3,1]) returns [2,3,4,2]

    Parameter input: The data to process
    Precondition: input an iterable, each element an int
    """
    result = []
    for x in input:
        x = x+1
        result.append(x)
    return result


def evens(input):
    """
    Returns a list with only the even elements of data

    Example: evens([0, 1, 2, 3, 4]) returns [0,2,4]

    Parameter input: The data to process
    Precondition: input an iterable, each element an int
    """
    result = []
    for x in input:
        if x % 2 == 0:
            result.append(x)
    return result


def average(input):
    """
    Returns a list with a running average of input

    The running average is a list with the same size
    as the input.  Each element at position n is the
    average of all of the elements in input[:n+1]

    Example: average([1, 3, 5, 7]) returns
    [1.0, 2.0, 3.0, 4.0]

    Parameter input: The data to process
    Precondition: input an iterable, each element a number
    """
    result = [] # Accumulator
    sum = 0     # Accumulator helper
    count = 0   # Accumulator helper
    for x in input:
        sum += x
        count += 1
        result.append(sum/count)
    return result
