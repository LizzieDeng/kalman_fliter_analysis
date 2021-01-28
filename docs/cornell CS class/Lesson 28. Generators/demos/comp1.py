"""
A module to show off list comprehension.

List comprehension works by putting a generator EXPRESSION
in side of square brackets [].

Author: Walker M. White (wmw2)
Date: October 28, 2020
"""


def add_one(lst):
    """
    Returns a copy of lst with 1 added to every element

    Example: add_one([1,2,3,1]) returns [2,3,4,2]

    Parameter lst: The list to copy
    Precondition: lst is a list of all numbers (either floats
    or ints), or an empty list
    """
    # LIST COMPREHENSION
    #return [ x+1 for x in lst ]

    # ACCUMULATOR PATTERN
    copy = []
    for x in lst:
        x = x+1
        copy.append(x)
    return copy


def evens(lst):
    """
    Returns a copy of lst, containing only the even elements

    Example: evens([1,2,3,4,5]) returns [2,4]
             events([1,3,5]) returns []

    Parameter lst: The list to copy
    Precondition: lst is a list of all numbers (either floats
    or ints), or an empty list
    """
    # LIST COMPREHENSION
    #return [x for x in lst if x % 2 == 0]

    # ACCUMULATOR PATTERN
    copy = []
    for x in lst:
        if x % 2 == 0:
            copy.append(x)
    return copy

    # THIS IS VERY DIFFERENT
    #return [ (x if x % 2 == 0 else -1) for x in lst ]


def transpose(table):
    """
    Returns a copy of table with rows and columns swapped

    Example:
           1  2          1  3  5
           3  4    =>    2  4  6
           5  6

    Parameter table: the table to transpose
    Precondition: table is a rectangular 2d List of numbers
    """
    # LIST COMPREHENSION
    #return [[row[i] for row in table] for i in range(len(table[0]))]

    # ACCUMULATOR PATTERN
    # Find the size of the (non-ragged) table
    numrows = len(table)
    numcols = len(table[0]) # All rows have same no. cols

    # Build the table
    result = [] # Result accumulator
    for m in range(numcols):

        # Make a single row
        row = [] # Single row accumulator
        for n in range(numrows):
            row.append(table[n][m])

        #Add the result to the table
        result.append(row)

    return result
