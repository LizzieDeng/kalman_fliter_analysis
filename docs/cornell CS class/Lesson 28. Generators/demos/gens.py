"""
A module showing off some simple generators

A classic programming pattern is to to have a generator
that takes an iterator/iterable as parameter and reformats
it somehow. As a general rule, these a functions that we
would have previously written with the accumulator pattern
to make a new list or tuple.

The advantage of the generate is that we can chain these
together to create code that is far faster than the
accumulator versions. That is because Python only needs
to look at one element at a time, and does not need to
keep creating lists/tuples for all of the elements at
once.

Author: Walker M. White (wmw2)
Date: October 28, 2020
"""


def add_one(input):
    """
    Generates 1 added to every element of input

    Example: If data is 1, 2, 3, 1, then this generator
    iterates 2, 3, 4, 2

    Parameter input: The data to process
    Precondition: input an iterable, each element an int
    """
    for x in input:
        yield x+1


def evens(input):
    """
    Generates only the elements of data that are even

    Example: If data is 0, 1, 2, 3, 4, then this generator
    iterates 0, 2, 4

    Parameter input: The data to process
    Precondition: input an iterable, each element an int
    """
    for x in input:
        if x % 2 == 0:
            yield x


def average(input):
    """
    Generates a running average of input

    The running average is an iterator the same size
    as the input.  Each element is the average of all
    of the elements in the input so far

    Example: If data is 1, 3, 5, 7 then this generator
    iterates 1.0, 2.0, 3.0, 4.0

    Parameter input: The data to process
    Precondition: input an iterable, each element a number
    """
    sum = 0
    count = 0
    for x in input:
        sum += x
        count += 1
        yield sum/count
