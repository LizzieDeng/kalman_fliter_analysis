"""
A module to illustrate difference between for-loops and while-loops

Author: Walker M. White (wmw2)
Date:   November 1, 2019
"""
import math


def increment_for(seq):
    """
    Increments each element of seq
    
    Parameter seq: list to increment
    Precondition: seq is a list of integers
    """
    for k in range(len(seq)):
       seq[k] = seq[k]+1


def increment_while(seq):
    """
    Increments each element of seq
    
    Parameter seq: list to increment
    Precondition: seq is a list of integers
    """
    k = 0
    while k < len(seq):
       seq[k] = seq[k]+1
       k = k + 1


def remove_all_for(seq,v):
    """
    Removes all occurences of v from seq
    
    Parameter seq: list to modify
    Precondition: seq is a list
    
    Parameter v: Value to remove
    Precondition: None (v can be anything)
    """
    # Find the number of occurrences of v
    amt = seq.count(v)
    
    # Remove v that many times
    for k in range(amt):
        seq.remove(v)


def remove_all_while(seq,v):
    """
    Removes all occurences of v from seq
    
    Parameter seq: list to modify
    Precondition: seq is a list
    
    Parameter v: Value to remove
    Precondition: None (v can be anything)
    """
    while v in seq:
        seq.remove(v)


def square_table_for(n):
    """
    Returns: list of squares less than (or equal to) N 
    
    This function creates a list of integer squares 1*1, 2*2, ...
    It only adds those squares that are less than or equal to N.
    
    Parameter n: the bound on the squares
    Precondition: n >= 0 is a number
    """
    seq = []
    stop = int(math.floor(math.sqrt(n))) + 1
    for k in range(stop):
        seq.append(k*k)
    
    return seq


def square_table_while(n):
    """
    Returns: list of squares less than (or equal to) N 
    
    This function creates a list of integer squares 1*1, 2*2, ...
    It only adds those squares that are less than or equal to N.
    
    Parameter n: the bound on the squares
    Precondition: n >= 0 is a number
    """
    seq = []
    k = 0
    while k*k < n:
        seq.append(k*k)
        k = k+1
    
    return seq


def fib_table_for(n):
    """
    Returns: fibonacci list [a0, a1, ..., an]
    
    Parameter n: the position in the fibonacci sequence
    Precondition: n >= 0 is an int
    """
    if n == 0:
        return [1]
    
    # if for n==1 is unnecessary
    fib = [1,1]
    for k in range(2,n):
        fib.append(fib[-1] + fib[-2])
    
    return fib


def fib_table_while(n):
    """
    Returns: fibonacci list [a0, a1, ..., an]
    
    Parameter n: the position in the fibonacci sequence
    Precondition: n >= 0 is an int
    """
    if n == 0:
        return [1]
    
    # if for n==1 is unnecessary
    fib = [1,1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    return fib