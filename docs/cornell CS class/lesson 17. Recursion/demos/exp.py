"""
Functions for raising a number to an exponent

These functions show the why the choice of division at the
recursive step matters. In this case, it greatly affects
the performance of the algorithm.

Author: Walker M. White (wmw2)
Date:   October 10, 2018
"""
import sys


# Allow us to go really deep
#sys.setrecursionlimit(999999999)


# Number of frames used in exp recursive calls
count_frames = 0


def exp_slow(b, c):
    """
    Returns the value  b^c.

    Property: b^c =  b * b^(c-1)

    Parameter b: the number to raise to a power
    Precondition: b is a number

    Parameter c: the exponent
    Precondition: c is an int >= 0
    """
    # get in the habit of checking what you can
    assert type(b) in [float, int], repr(b)+' is not a number'
    assert type(c) == int, repr(c)+' is not an int'
    assert c >= 0, repr(c)+' is negative'

    # Allows us to write to global variable. EVIL! Do not use!
    global count_frames

    # Work on small data   (BASE CASE)
    if c == 0:
        return 1

    # Break up into halves (RECURSIVE CASE)
    left  = b
    right = exp_slow(b, c-1)

    # Used to count the number of frames
    count_frames = count_frames+1

    # Combine the answer
    return left * right


def exp_alt(b, c):
    """
    Returns the value  b^c.

    Property: b^c =  b^(c/2) * b^(c-c/2)

    Parameter b: the number to raise to a power
    Precondition: b is a number

    Parameter c: the exponent
    Precondition: c is an int >= 0
    """
    assert type(b) in [float, int], repr(b)+' is not a number'
    assert type(c) == int, repr(c)+' is not an int'
    assert c >= 0, repr(c)+' is negative'

    # Allows us to write to global variable. EVIL! Do not use!
    global count_frames

    # Work on small data   (BASE CASE)
    if c == 0:
        return 1
    elif c == 1:
        return b

    # Break up into halves (RECURSIVE CASE)
    left  = exp_alt(b, c//2)
    right = exp_alt(b,c-c//2)

    # Used to count the number of frames
    count_frames = count_frames+1;

    # Combine the answer
    return left * right


def exp_fast(b, c):
    """
    Returns the value  b^c.

    Property. b^c =  b * b^(c-1)
    Property. b^c = (b*b)^(c/2) for even c

    Parameter b: the number to raise to a power
    Precondition: b is a number

    Parameter c: the exponent
    Precondition: c is an int >= 0
    """
    assert type(b) in [float, int], repr(b)+' is not a number'
    assert type(c) == int, repr(c)+' is not an int'
    assert c >= 0, repr(c)+' is negative'

    # Allows us to write to global variable. EVIL! Do not use!
    global count_frames

    # Work on small data   (BASE CASE)
    if c == 0:
        return 1

    # Used to count the number of frames
    count_frames = count_frames+1;

    # Break up into halves (RECURSIVE CASE)
    if c % 2 == 0:
        left  = b
        right = b
        return exp_fast(left*right, c//2)

    # If not even
    left  = b
    right = exp_fast(b, c-1)
    return left * right
