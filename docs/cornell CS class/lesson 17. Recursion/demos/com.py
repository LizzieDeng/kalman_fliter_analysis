"""
A recursive function adding commas to integers.

These functions show the why the choice of division at the recursive step matters.

Author: Walker M. White (wmw2)
Date:   October 10, 2018
"""
import sys


# Allow us to go really deep
#sys.setrecursionlimit(999999999)


# COMMAFY FUNCTIONS
def commafy(s):
    """
    Returns a copy of s, with commas every 3 digits.

    Example:
        commafy('5341267') = '5,341,267'

    Parameter s: string representing an integer
    Precondition: s a string with only digits, not starting with 0
    """
    # You can't always check everything with an assert
    # However, check what you can
    assert type(s) == str, repr(s) + ' is not a string'

    # Work on small data   (BASE CASE)
    if len(s) <= 3:
        return s

    # Break up into halves (RECURSIVE CASE)
    left = commafy(s[0:-3])
    right = s[-3:]

    # Combine the answer
    return left + ',' + right


def commafy_int(n):
    """
    Returns n as a string, with commas every 3 digits.

    Example:
        commafy('5341267') = '5,341,267'

    Parameter n: number to convert
    Precondition: n is an int with n >= 0
    """
    assert type(n) == int, repr(n)+' is not an int'     # get in the habit
    assert n >= 0, repr(n)+' is negative'               # get in the habit

    # Use helpers
    return commafy(str(n))


    # Work on small data   (BASE CASE)
    #if n < 1000:
    #    return str(n)

    # Break up into halves (RECURSIVE CASE)
    #left  = commafy(n//1000)
    #right = to3(n % 1000)

    # Combine the answer
    #return left + ',' + right


def to3(p):
    """
    Returns a string representation of p with at least 3 chars

    Adds leading 0's if necessary

    Parameter n: number to pad
    Precondition: p is an int
    """
    assert type(p) == int, repr(p)+' is not an int'     # get in the habit

    if p < 10:
        return '00' + str(p)
    elif p < 100:
        return '0' + str(p)

    return str(p)
