"""
A simple module showing off files

Author: Walker M. White (wmw2)
Date:   September 28, 2018
"""


def print_file(name):
    """
    Prints out the individual lines of a file.

    Parameter name: the name of the file to print out
    Precondition: name is a string with a valid file name
    """
    thefile = open(name)
    for line in thefile:
        print(line)
    thefile.close()


def file2list(name):
    """
    Returns: a list with the contents of the file.

    Each line of the file will be a separate element in the list.  The list
    size will be the number of lines in the file.

    Parameter name: the name of the file to print out
    Precondition: name is a string with a valid file name
    """
    thefile = open(name)
    result = list(thefile)
    thefile.close()
    return result
