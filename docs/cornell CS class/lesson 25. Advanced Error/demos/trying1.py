"""
Functions to show how type-specific try-except works

This code works best in the Python Tutor.

Author: Walker M. White (wmw2)
Date:   October 28, 2017 (Python 3 Version)
"""


def first(i):
    """
    Our first function, it passes the argument i to second().
    
    It contains the try-except block for AssertionError.
    
    Raises: ValueError        i == 4
    
    Parameter i: An int to control program flow
    Precondition: i is an int
    """
    print('Starting first')
     
    try:
        second(i)
    except AssertionError:
        print('Caught at first')
    
    print('Ending first')


def second(i):
    """
    Our first function, it passes the argument i to third().  
    
    It contains the try-except block for ArithmeticError.
    
    Raises: AssertionError    i == 3
    Raises: ValueError        i == 4
    
    Parameter i: An int to control program flow
    Precondition: i is an int
    """
    print('Starting second')
     
    try:
        third(i)
    except ArithmeticError as e:
        print('Caught at second')
    
    print('Ending second')


def third(i):
    """
    This function does nothing but throw exceptions.
    
    The Exception thrown depends on i.  Does nothing
    if i is 1.
    
    Raises: ArithmeticError   i == 2
    Raises: AssertionError    i == 3
    Raises: ValueError        i == 4
    
    Parameter i: An int to control program flow
    Precondition: i is an int
    """
    print('Starting third')
    
    if i == 1:
        pass
     
    if i == 2:
        # This exception is for bad arithmetic (i.e. divide by zero)
        y = 5/0
     
    if i == 3:
        # This exception is what assert statements create.
        assert False, 'Intentional Error'
    
    if i == 4:
        # If a calculation uses a value you did not expect.
        y = int('a')
     
    print('Ending third')


# Try this in the Python Tutor
#first(1)
#first(2)
#first(3)
#first(4)