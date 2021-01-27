"""
A module with a simple Fraction class.

This module implements a fraction WITHOUT using operator
overloading.  It is an example of the simplest way to use
a class.

Author: Walker M. White (wmw2)
Date:   November 2, 2019
"""


def gcd(a,b):
    """
    Returns the greatest common divisor of x and y.

    Parameter a: The first integer
    Precondition: a is an int

    Parameter b: The second integer
    Precondition: b is an int
    """
    assert type(a) == int,repr(x)+' is not an int'
    assert type(b) == int,repr(y)+' is not an int'
    while b != 0:
       t = b
       b = a % b
       a = t
    return a


class Fraction(object):
    """
    A class to represent a fraction n/d

    This class has an attribute for a number and a
    denominator. They are only accessible via the
    getters and setters.
    """
    # HIDDEN INSTANCE ATTRIBUTES
    # Attribute _numerator: The fraction numerator
    # Invariant: _numerator is an int
    #
    # Attribute _denominator: The fraction denominator
    # Invariant: _denominator is an int > 0

    # GETTER AND SETTERS
    def getNumerator(self):
        """
        Returns the fraction numerator.

        The numerator is an int.
        """
        return self._numerator # returns the attribute

    def setNumerator(self,value):
        """
        Sets the numerator to value.

        Parameter value: the new numerator
        Precondition: value is an int
        """
        # enforce invariant
        assert type(value) == int, repr(value)+' is not an int'
        # assign to attribute
        self._numerator = value

    def getDenominator(self):
        """
        Returns the fraction denominator.

        The denominator is an int > 0.
        """
        return self._denominator # returns the attribute

    def setDenominator(self,value):
        """
        Sets the numerator to value.

        Parameter value: the new denominator
        Precondition: value is an int > 0
        """
        # enforce invariant
        assert type(value) == int, repr(value)+' is not an int'
        assert value > 0, repr(value)+' is not positive'
        # assign to field
        self._denominator = value

    # INITIALIZER
    def __init__(self,n=0,d=1):
        """
        Initializes a new Fraction n/d

        Parameter n: the numerator (default is 0)
        Precondition: n is an int (or optional)

        Parameter d: the denomenator (default is 1)
        Precondition: d is an int > 0 (or optional)
        """
        # No need for asserts; setters handle everything
        self.setNumerator(n)
        self.setDenominator(d)

    def __str__(self):
        """
        Returns this Fraction as a string 'n/d'
        """
        return repr(self._numerator)+'/'+repr(self._denominator)

    def __repr__(self):
        """
        Returns the unambiguous representation of Fraction
        """
        return str(self.__class__)+'['+str(self)+']'

    # MATH METHODS
    def mult(self,other):
        """
        Returns the product of self and other as a new
        Fraction

        This method does not modify the contents of self
        or other

        Parameter other: the fraction to multiply on the right
        Precondition: other is a Fraction
        """
        assert type(other) == Fraction
        top = self.getNumerator()*other.getNumerator()
        bot = self.getDenominator()*other.getDenominator()
        return Fraction(top,bot)

    def add(self,other):
        """
        Returns the sum of self and other as a new Fraction

        This method does not modify the contents of self or
        other

        Parameter other: the fraction to add on the right
        Precondition: other is a Fraction
        """
        assert type(other) == Fraction
        bot = self.getDenominator()*other.getDenominator()
        top = (self.getNumerator()*other.getDenominator()+
               self.getDenominator()*other.getNumerator())
        return Fraction(top,bot)

    def reduce(self):
        """
        Normalizes this fraction into simplest form.

        Normalization ensures that the numerator and
        denominator have no common divisors.
        """
        g = gcd(self.getNumerator(),self.getDenominator())
        self.setNumerator(self.getNumerator()//g)
        self.setDenominator(self.getDenominator()//g)
