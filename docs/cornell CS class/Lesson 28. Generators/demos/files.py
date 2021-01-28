"""
A module to show that files are also iterables

Author: Walker M. White (wmw2)
Date: October 28, 2020
"""


def print_file(filename):
    """
    Prints the contents of the file filename

    When we read from a file, it will always include
    a '\n' at the end of each line.  We want to remove
    this from the line before we print it, or we will
    always get an extra unnecessary line

    Parameter filename: The file to read
    Precondition: filename is a string and refers to
    a valid text file
    """
    file = open(filename)
    for line in file:
        # Watch what happens if you remove this line
        line = line[:-1] # Remove stray '\n' at end
        print(line)

    # You should always close a file when done
    file.close()
