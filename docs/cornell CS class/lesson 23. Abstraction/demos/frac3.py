"""
A module with a simple Fraction class.

This module shows off how to support mixed types for add and multiply.

Author: Walker M. White (wmw2)
Date:   November 2, 2019
"""
from functools import total_ordering  # for implementing comparisons in Python3


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

    This class has an attribute for a number and a denominator.  They
    are only accessible via the getters and setters.
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
    def __mul__(self,other):
        """
        Returns the product of self and other as a new
        Fraction

        This method does not modify the contents of self
        or other

        Parameter other: the value to multiply on the right
        Precondition: other is a Fraction or an int
        """
        assert type(other) == Fraction or type(other) == int, repr(other)+' is not a valid operand'
        if type(other) == int:
            return self._multiplyInt(other)
        return self._multiplyFraction(other)

    # Private helper to multiply fractions
    def _multiplyFraction(self,other):
        """
        Returns the product of self and other as a new
        Fraction

        This method does not modify the contents of self
        or other

        Parameter other: the fraction to multiply on the
        right
        Precondition: other is a Fraction
        """
        # No need to enforce preconditions on a hidden method
        print('Multiplying by fraction')
        top = self.getNumerator()*other.getNumerator()
        bot = self.getDenominator()*other.getDenominator()
        return Fraction(top,bot)

    # Private helper to multiply ints
    def _multiplyInt(self,x):
        """
        Returns the product of self and x as a new
        Fraction

        This method does not modify the contents of self
        or other

        Parameter x: the value to multiply on the right
        Precondition: x is a int
        """
        # No need to enforce preconditions on a hidden method
        print('Multiplying by int')
        top = self.getNumerator()*x
        bot = self.getDenominator()
        return Fraction(top,bot)

    # UNCOMMENT AND WATCH WHAT HAPPENS
    #def __rmul__(self,other):
    #    """
    #    Returns the product of self and other as a new
    #    Fraction
    #
    #    This method does not modify the contents of self
    #    or other
    #
    #    Parameter other: the value to multiply on the left
    #    Precondition: other is a Fraction or an int
    #    """
    #    assert type(other) == Fraction or type(other) == int, repr(other)+' is not a valid operand'
    #    if type(other) == int:
    #        return self._multiplyInt(other)
    #    return self._multiplyFraction(other)

    def __add__(self,other):
        """
        Returns the sum of self and other as a new Fraction

        This method does not modify the contents of self or other

        Parameter other: the value to add on the right
        Precondition: other is a Fraction or an int
        """
        assert type(other) == Fraction or type(other) == int, repr(other)+' is not a valid operand'
        if type(other) == int:
            return self._addInt(other)
        return self._addFraction(other)

    # Private helper to add fractions
    def _addFraction(self,other):
        """
        Returns te sum of self and other as a new Fraction

        This method does not modify the contents of self or other

        Parameter other: the fraction to add on the right
        Precondition: other is a Fraction
        """
        # No need to enforce preconditions on a hidden method
        bot = self.getDenominator()*other.getDenominator()
        top = (self.getNumerator()*other.getDenominator()+
               self.getDenominator()*other.getNumerator())
        return Fraction(top,bot)

    # Private helper to add ints
    def _addInt(self,x):
        """
        Returns the sum of self and other as a new Fraction

        This method does not modify the contents of self or other

        Parameter other: the value to add on the right
        Precondition: other is an int
        """
        # No need to enforce preconditions on a hidden method
        bot = self.getDenominator()
        top = (self.getNumerator()+self.getDenominator()*x)
        return Fraction(top,bot)

    # UNCOMMENT AND WATCH WHAT HAPPENS
    #def __radd__(self,other):
    #    """
    #    Returns the sum of self and other as a new Fraction
    #
    #    This method does not modify the contents of self or other
    #
    #    Parameter other: the value to add on the right
    #    Precondition: other is a Fraction or an int
    #    """
    #    assert type(other) == Fraction or type(other) == int, repr(other)+' is not a valid operand'
    #    if type(other) == int:
    #        return self._addInt(other)
    #    return self._addFraction(other)

    # COMPARISONS
    def __eq__(self,other):
        """
        Returns True if self, other are equal Fractions.

        It returns False if they are not equal, or other is not a Fraction

        Parameter other: value to compare to this fraction
        Precondition: NONE
        """
        if type(other) != Fraction and type(other) != int:
            return False

        if type(other) == int:
            return self.getNumerator() == other*self.getDenominator()

        # Cross multiply
        left = self.getNumerator()*other.getDenominator()
        rght = self.getDenominator()*other.getNumerator()
        return left == rght

    def __lt__(self,other):
        """
        Returns True if self < other, False otherwise

        This method is used to implement all strict comparison operations.
        Both < and > are determined automatically from this method.

        Parameter other: value to compare to this fraction
        Precondition: other is a Fraction
        """
        assert type(other) == Fraction or type(other) == int, repr(other)+' is not a valid operand'

        if type(other) == int:
            return self.getNumerator() < other*self.getDenominator()

        # Cross multiply
        left = self.getNumerator()*other.getDenominator()
        rght = self.getDenominator()*other.getNumerator()
        return left < rght

    def __le__(self,other):
        """
        Returns True if self < other, False otherwise

        This method is used to implement all inclusive comparison operations.
        Both <= and >= are determined automatically from this method.

        Parameter other: value to compare to this fraction
        Precondition: other is a Fraction
        """
        assert type(other) == Fraction or type(other) == int, repr(other)+' is not a valid operand'

        if type(other) == int:
            return self.getNumerator() <= other*self.getDenominator()

        # Cross multiply
        left = self.getNumerator()*other.getDenominator()
        rght = self.getDenominator()*other.getNumerator()
        return left <= rght

    # OTHER METHODS
    def reduce(self):
        """
        Normalizes this fraction into simplest form.

        Normalization ensures that the numerator and denominator have no
        common divisors.
        """
        g = gcd(self.getNumerator(),self.getDenominator())
        self.setNumerator(self.getNumerator()//g)
        self.setDenominator(self.getDenominator()//g)
