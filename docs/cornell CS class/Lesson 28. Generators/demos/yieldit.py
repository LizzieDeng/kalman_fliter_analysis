"""
A generator defintion of the range-squared iterable.

Note that generators can only define iterators, not
(general-purpose) iterables. They are one-shot iterables
that cannot be re-used.  To get a more general-purpose
iterable, we still need to use a class.

Author: Walker M. White (wmw2)
Date: October 28, 2020
"""


def range2iter(n):
    """
    Generates the squares of numbers 0 to n-1

    Example: range2iter(5) iterates 0, 1, 4, 9, 16

    Parameter n: The limiter for this generator
    Precondition: n is an int >= 0
    """
    for x in range(n):
        yield x*x


class range2(object):
    """
    An iterable class for iterating squares of a range

    As an iterable class, this is not a one-shot. It will
    regenerate an iterator every single time one is needed.
    However, it can only be used in for-loops (or converted
    to a list/tuple).  You cannot use the next function on
    these objects.
    """

    def __init__(self,n):
        """
        Initializes a squares iterable for the range 0 to n-1

        Paramater n: The limiter for this iterable
        Precondition: n is an int >= 0
        """
        self._limit = n

    def __iter__(self):
        """
        Returns a new iterator for this iterable
        """
        return range2iter(self._limit)
