"""
A module the quicksort algorithm

Author: Walker M. White (wmw2)
Date:   November 10, 2017 (Python 3 Version)
"""
import random


def partition(b, h, k):
    """
    Returns the new position of pivot in partitioned list
    b[h..k].

    The pivot is the initial value x = b[h].  This function
    rearranges the list so that elements <= x are before
    the pivot and elements >= x are after the pivot.

    Parameter b: The list to rearrange
    Precondition: b is a mutable sequence (e.g. a list).

    Parameter h: The starting point to sort
    Precondition: h is an int and a valid position in b

    Parameter k: The ending poing to sort
    Precondition: k is an int and a valid position in b
    """
    assert type(b) == list, repr(b)+' is not a list'
    assert 0 <= h and h < len(b), repr(h)+' is not a valid position in the list'
    assert 0 <= k and k < len(b), repr(k)+' is not a valid position in the list'

    # position i is end of first paritition range
    i = h
    # position j is beginning of second partition range
    j = k+1

    # Find the first element in the list.
    x = b[h]

    # b[h..i-1] < x, b[i] = x, b[i+1..j-1] unknown,
    # and  b[j..k] >= x
    while i < j-1:
        if b[i+1] >= x:
            # Move this to the end of the block.
            _swap(b,i+1,j-1)
            j = j - 1
        else:   # b[i+1] < x
            _swap(b,i,i+1)
            i = i + 1

    # b[h..i-1] < x, b[i] is x, and b[i+1..k] >= x
    return i


def sort(b):
    """
    Quick Sort: Sorts the array b in n log n average time

    Parameter b: The sequence to sort
    Precondition: b is a mutable sequence (e.g. a list).
    """
    assert type(b) == list, repr(b)+' is not a list'

    # Send everything to the recursive helper
    _qsort_helper(b,0,len(b)-1)


def _qsort_helper(b, h, k):
    """
    Quick Sort: Sorts the array b[h..k] in n log n average
    time

    Parameter b: The sequence to sort
    Precondition: b is a mutable sequence (e.g. a list).

    Parameter h: The starting point to sort
    Precondition: h is an int and a valid position in b

    Parameter k: The ending poing to sort
    Precondition: k is an int and a valid position in b
    """
    # We typically do not enforce preconditions on hidden helpers
    if k-h < 1:            # BASE CASE
        return

    # RECURSIVE CASE
    j = partition(b, h, k)
    # b[h..j-1] <= b[j] <= b[j+1..k]
    # Sort b[h..j-1]  and  b[j+1..k]
    _qsort_helper(b, h, j-1)
    _qsort_helper(b, j+1, k)


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
