"""
Script showing off dynamic attribute access.

Our applications in CS 1110 are never advanced enough that
we would need a feature like this.  However, this script
does show off what we can do with dynamic attribute access
(e.g. accessing an attribute with a string, not a direct
expression)

Author: Walker M. White (wmw2)
Date: October 15, 2020
"""
import random
import introcs


def create_color():
    """
    Returns a randomly constructed color value
    """
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    a = random.randint(0,255)
    return introcs.RGB(r,g,b,a)


def main():
    """
    Runs the script, promping for user input.
    """
    print('Generating random color')
    c = create_color()
    attr = input('Specify an attribute: ')
    if hasattr(c,attr):
        print('The '+attr+' attribute is '+str(getattr(c,attr)))
    else:
        print('There is no attribute '+attr+'.')


if __name__ == '__main__':
    main()
