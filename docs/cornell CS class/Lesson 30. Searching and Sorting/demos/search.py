"""
A module with the basic searching algorithms

Author: Walker M. White (wmw2)
Date:   October 20, 2020
"""
import random

def linear_search(c,b):
    """
    Returns index of first occurrence of c in b; -1 if not
    found.

    Parameter c: The value to search for
    Precondition: NONE (c can be any value)

    Parameter b: The sequence to search
    Precondition: b is a sequence
    """
    # Quick way to check if a sequence
    assert len(b) >= 0, repr(b)+' is a not a sequence (list, string, or tuple)'

    # Store in i the index of the first c in b[0..]
    i = len(b)-1
    while i >= 0 and b[i] != c:
        i = i - 1;

    if i >= 0:
        return i

    # NOT FOUND
    return -1


def binary_search(c,b):
    """
    Returns index of first occurrence of c in b; -1 if not
    found.

    Parameter b: The sequence to search
    Precondition: b is a SORTED sequence

    Parameter c: The value to search for
    Precondition: NONE (c can be any value)
    """
    # Quick way to check if a sequence; CANNOT easily check sorted
    assert len(b) >= 0, repr(b)+' is a not a sequence (list, string, or tuple)'

    # Store in i the value BEFORE beginning of range to search
    i = 0
    # Store in j the end of the range to search (element after)
    j = len(b)
    # The middle position of the range
    mid = (i+j)//2

    while j > i:
        if b[mid] < c:
            i = mid+1
        else:     # b[mid] >= c
            j = mid

        # Compute a new middle.
        mid = (i+j)//2

    if i < len(b) and b[i] == c:
        return i

    # NOT FOUND
    return -1


def scramble(b):
    """
    Scrambles the list to resort again

    Parameter b: The list to scramble
    Precondition: b is a mutable sequence (e.g. a list).
    """
    assert type(b) == list, repr(b)+' is not a list'

    # Start from the beginning
    i = 0
    while i < len(b):
        size = len(b)-i
        pos  = int(random.random()*size)
        _swap(b,i,i+pos)
        i = i+1


# HELPER FUNCTIONS
def _swap(b, h, k):
    """
    Procedure swaps b[h] and b[k]

    Parameter b: The list to rearrange
    Precondition: b is a mutable sequence (e.g. a list).

    Parameter h: The first position to swap
    Precondition: h is an int and a valid position in b

    Parameter k: The second position to swap
    Precondition: k is an int and a valid position in b
    """
    # We typically do not enforce preconditions on hidden helpers
    temp = b[h]
    b[h] = b[k]
    b[k] = temp
