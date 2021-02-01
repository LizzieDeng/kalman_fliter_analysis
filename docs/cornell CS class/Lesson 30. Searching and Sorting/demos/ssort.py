"""
A module with selection sort

Author: Walker M. White (wmw2)
Date:   October 20, 2020
"""
import random


def sort(b):
    """
    Selection Sort: Sorts the array b in n^2 time

    Parameter b: The sequence to sort
    Precondition: b is a mutable sequence (e.g. a list).
    """
    assert type(b) == list, repr(b)+' is not a list'
    n = len(b)

    # Start from beginning of list
    i = 0

    # b[0..i-1] sorted and all less than b[i..n-1]
    while i < len(b):
        index = _min_index(b,i);
        _swap(b,i,index)
        i = i+1

    # b[0..n-1] sorted




def _min_index(b, h):
    """
    Returns: The index of the minimum value in b[h..]

    Parameter b: The sequence to search
    Precondition: b is a mutable sequence (e.g. a list).
    """
    # We typically do not enforce preconditions on hidden helpers

    # Start from position h
    i = h
    index = h;

    # index is position of min in b[h..i-1]
    while i < len(b):
        if b[i] < b[index]:
            index = i
        i = i+1

    # index is position of min in b[h..len(b)-1]
    return index



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
