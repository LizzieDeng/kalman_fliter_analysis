"""
Functions for reordering a string (incomplete)

Author: Walker M. White
Date:   September 6, 2018
"""


def last_name_first(s):
    """
    Returns a copy of s but in the form 'last-name, first-name'
    
    We assume that s is just two names (first and last).  Middle names are
    not supported.
    
    Examples:
        last_name_first('Walker White') returns 'White, Walker'
        last_name_first('Walker      White') returns 'White, Walker'
    
    Parameter s: the person's name
    Precondition: s is a string in the form 'first-name last-name' with one or
    more spaces between the two names. There are no spaces in either first-name
    or last-name
    """
    # Find the first name
    first = first_name(s)
    # Find the last name
    last = last_name(s)
    # Glue them together with comma
    return last+", "+first


def first_name(s):
    """
    Returns the first name in s
    
    Examples:
        last_name_first('Walker White') returns 'Walker'
        last_name_first('Walker      White') returns 'Walker'
    
    Parameter s: a name 'first-name last-name'
    Precondition: s is a string 'first-name last-name' with one or more blanks 
    between the two names.
    """
    end_first = s.find(' ')
    return s[:end_first]


def last_name(s):
    """
    Returns the last name in s
    
    Examples:
        last_name_first('Walker White') returns 'White'
        last_name_first('Walker      White') returns 'White'
    
    Parameter s: a name 'first-name last-name'
    Precondition: s is a string 'first-name last-name' with one or more blanks 
    between the two names.
    """

    start_last = s.rfind(' ')
    return s[start_last+1:]
