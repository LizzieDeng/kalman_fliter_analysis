"""
A module reimagining map and filter as generators

Once again, you may want to run this one in the Python Tutor for full effect.

Author: Walker M. White (wmw2)
Date: October 28, 2020
"""


def map(f,data):
    """
    Generates f applied to each element of data

    Parameter f: The function to apply
    Precondition: f is a function taking exactly one argument

    Parameter data: The data to process
    Precondition: data an iterable, each element satisfying precond of f
    """
    for item in data:
         yield f(item)


def filter(f,data):
    """
    Generates only the elements of data for which f is True

    Parameter f: The function to apply
    Precondition: f is a BOOLEAN function taking exactly one argument

    Parameter data: The data to process
    Precondition: data an iterable, each element satisfying precond of f
    """
    for item in data:
        if f(item):
            yield item


def plus1(x):
    """
    Returns x+1

    Parameter x: The number to add to
    Precondition: x is an int or float
    """
    return x+1


def negate(x):
    """
    Returns -x

    Parameter x: The number to add to
    Precondition: x is an int or float
    """
    return -x


def iseven(x):
    """
    Returns True if x is even

    Parameter x: The number to add to
    Precondition: x is an int
    """
    return x % 2 == 0


def ispos(x):
    """
    Returns True if x > 0

    Parameter x: The number to add to
    Precondition: x is an int or float
    """
    return x > 0


# Add this if using the Python Tutor
#a = [-2,1,4,3]
#b = map(add_one, a)
#b = list(b)
#c = map(negate, a)
#c = list(c)
#d = filter(iseven, a)
#d = list(d)
#e = filter(ispos, a)
#e = list(e)
