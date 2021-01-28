"""
A class defintion of the range-squared iterable.

In this module we break one of our naming conventions,
namely that class names should all start with capital
letters. That is because we want to compare them with
generators, which following function naming conventions.

Note that we have two classes: an iterator class and an
iterable class. Iterable classes work by returning a
new/fresh iterator each time on demand.

Author: Walker M. White (wmw2)
Date: October 28, 2020
"""

class range2iter(object):
    """
    An iterator class for iterating squares of a range

    Remember that iterators are one-shot. Once you get all
    of the elements from them (either using next or a
    for-loop), then you cannot use them again.
    """

    def getLimit(self):
        """
        The limit defining this range squares iterator.

        If the limit is n, this generator will iterate the
        numbers 0, 1, 4, ... (n-1)*(n-1)
        """
        return self._limit

    def __init__(self,n):
        """
        Initializes a squares iterator for the range 0 to n-1

        Paramater n: The limiter for this iterator
        Precondition: n is an int >= 0
        """
        self._limit = n     # How far we will iterate
        self._pos = 0       # Where we currently are

    def __next__(self):
        """
        Returns the next element in the iteration

        This method raises StopIteration when it reaches the
        end of the iteration.  This will cause the for-loop
        to stop.
        """
        if self._pos >= self._limit:
            raise StopIteration()
        else:
            value = self._pos*self._pos
            self._pos += 1
            return value


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
