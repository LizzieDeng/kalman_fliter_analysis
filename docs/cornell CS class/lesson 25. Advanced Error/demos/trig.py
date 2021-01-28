"""
Functions to show off the uses of raising

Author: Walker M. White (wmw2)
Date:   October 28, 2017 (Python 3 Version)
"""
import math


def sec(angle):
    """
    Returns: The secant (1/cos) of the given angle
    
    The domain of secant excludes any number of the form PI/2.0+k*PI,
    where k is an integer.  That is because those are the cases where
    cos(angle) is 0.
    
    Parameter angle: The secant angle
    Precondition: angle is an int or float in the domain of secant
    """
    # Raise a type error if not a number
    if not type(angle) in [int, float]:
        raise TypeError(repr(angle)+' is not a number')
    
    val = math.cos(angle)
    if abs(val) < 0.000001:  # Close enough to 0
        raise ValueError(repr(angle)+' is outside of the domain of secant')
    
    return 1/val


def csc(angle):
    """
    Returns: The cosecant (1/sin) of the given angle
    
    The domain of secant excludes any number of the form k*PI, where k is an 
    integer.  That is because those are the cases where sin(angle) is 0.
    
    Parameter angle: The cosecant angle
    Precondition: angle is an int or float in the domain of cosecant
    """
    raise NotImplementedError('This function is not yet completed')

