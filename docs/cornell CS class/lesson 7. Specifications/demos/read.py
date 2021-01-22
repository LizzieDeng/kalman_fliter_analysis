"""
A module with a function to read text

This module shows off a more complicated type of precondition

Author: Walker M. White
Date:   February 14, 2019
"""
import introcs


def get_number(filename):
    """
    Returns the number stored in the file <filename>
    
    When we read a file, we get a string.  This function changes the result to
    an int before returning it.
    
    Parameter filename: The file to get the number from
    Precondition: filename is a string and a reference to a valid file.
    In addition, this file only has a single integer in it.
    """
    contents = introcs.read_txt(filename)
    
    # Change string to int before returning
    result = int(contents)
    return result
