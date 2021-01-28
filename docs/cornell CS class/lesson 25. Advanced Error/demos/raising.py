"""
Functions to show off the uses of raising

Author: Walker M. White (wmw2)
Date:   October 28, 2017 (Python 3 Version)
"""


def foo1(x):
    """
    Returns x+1
    
    Parameter x: The number to add to
    Precondition: x is a number (int or float)
    """
    assert type(x) in [int,float], repr(x)+' is not a number'
    
    return x+1


def foo2(x):
    """
    Returns x+1
    
    Parameter x: The number to add to
    Precondition: x is a number (int or float)
    """
    if not type(x) in [int,float]:
        err = AssertionError(repr(x)+' is not a number')
        raise err
    
    return x+1

