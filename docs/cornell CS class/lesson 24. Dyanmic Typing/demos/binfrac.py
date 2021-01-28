"""
A module with a simple Fraction class and its subclass.

This module shows off why we want to use isinstance.

Author: Walker M. White (wmw2)
Date:   November 10, 2019
"""
import math


def gcd(a,b):
    """
    Returns: Greatest common divisor of x and y.

    Precondition: x and y are integers.
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
    """
    # INSTANCE ATTRIBUTES
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
        assert isinstance(value, int), repr(value)+' is not an int'
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
        assert isinstance(value, int), repr(value)+' is not an int'
        assert value > 0, repr(value)+' is not positive'
        # assign to attribute
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
        #assert type(other) == Fraction or type(other) == int

        # Check if other an int or SUBCLASS of Fraction
        assert isinstance(other,Fraction) or isinstance(other,int), repr(other)+' is not a valid operand'
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

        Parameter other: the fraction to multiply on the right
        Precondition: other is a Fraction
        """
        # No need to enforce preconditions on a hidden method
        top = self.getNumerator()*other.getNumerator()
        bot = self.getDenominator()*other.getDenominator()
        return Fraction(top,bot)

    # Private helper to multiply ints
    def _multiplyInt(self,x):
        """
        Returns the product of self and other as a new
        Fraction

        This method does not modify the contents of self
        or other

        Parameter other: the value to multiply on the right
        Precondition: other is a int
        """
        # No need to enforce preconditions on a hidden method
        top = self.getNumerator()*x
        bot = self.getDenominator()
        return Fraction(top,bot)

    def __add__(self,other):
        """
        Returns the sum of self and other as a new
        Fraction

        This method does not modify the contents of
        self or other

        Parameter other: the value to add on the right
        Precondition: other is a Fraction or an int
        """
        assert isinstance(other,Fraction) or isinstance(other,int), repr(other)+' is not a valid operand'
        if type(other) == int:
            return self._addInt(other)
        return self._addFraction(other)

    # Private helper to multiply fractions
    def _addFraction(self,other):
        """
        Returns the sum of self and other as a new
        Fraction

        This method does not modify the contents of
        self or other

        Parameter other: the fraction to add on the right
        Precondition: other is a Fraction
        """
        # No need to enforce preconditions on a hidden method
        bot = self.getDenominator()*other.getDenominator()
        top = (self.getNumerator()*other.getDenominator()+
               self.getDenominator()*other.getNumerator())
        return Fraction(top,bot)

    # Private helper to multiply ints
    def _addInt(self,x):
        """
        Returns the sum of self and other as a new
        Fraction

        This method does not modify the contents of
        self or other

        Parameter other: the value to add on the right
        Precondition: other is an int
        """
        # No need to enforce preconditions on a hidden method
        bot = self.getDenominator()
        top = (self.getNumerator()+self.getDenominator()*x)
        return Fraction(top,bot)

    # COMPARISONS
    def __eq__(self,other):
        """
        Returns True if self, other are equal Fractions.

        It returns False if they are not equal, or other
        is not a Fraction

        Parameter other: value to compare to this fraction
        Precondition: NONE
        """
        if not isinstance(other, Fraction) and not isinstance(other, int):
            return False

        if isinstance(other, int):
            return self.getNumerator() == other*self.getDenominator()

        # Cross multiply
        left = self.getNumerator()*other.getDenominator()
        rght = self.getDenominator()*other.getNumerator()
        return left == rght

    def __lt__(self,other):
        """
        Returns True if self < other, False otherwise

        This method is used to implement all strict comparison
        operations.  Both < and > are determined automatically
        from this method.

        Parameter other: value to compare to this fraction
        Precondition: other is a Fraction
        """
        assert isinstance(other, Fraction) or isinstance(other, int), repr(other)+' is not a valid operand'

        if isinstance(other, int):
            return self.getNumerator() < other*self.getDenominator()

        # Cross multiply
        left = self.getNumerator()*other.getDenominator()
        rght = self.getDenominator()*other.getNumerator()
        return left < rght

    def __le__(self,other):
        """
        Returns True if self < other, False otherwise

        This method is used to implement all inclusive comparison
        operations.  Both <= and >= are determined automatically
        from this method.

        Parameter other: value to compare to this fraction
        Precondition: other is a Fraction
        """
        assert isinstance(other, Fraction) or isinstance(other, int), repr(other)+' is not a valid operand'

        if isinstance(other, int):
            return self.getNumerator() <= other*self.getDenominator()

        # Cross multiply
        left = self.getNumerator()*other.getDenominator()
        rght = self.getDenominator()*other.getNumerator()
        return left <= rght

    # OTHER METHODS
    def reduce(self):
        """
        Normalizes this fraction into simplest form.

        Normalization ensures that the numerator and
        denominator have no common divisors.
        """
        g = gcd(self.getNumerator(),self.getDenominator())
        self.setNumerator(self.getNumerator()//g)
        self.setDenominator(self.getDenominator()//g)


class BinaryFraction(Fraction):
    """
    A class to represent fractions that are k/(2**n)
    """
    # INSTANCE ATTRIBUTES are the same, but:
    # Invariant: _denominator is 2 ** n where n >= 0

    def setDenominator(self,value):
        """
        Sets the numerator to 2 ** value.

        Parameter value: the POWER of the new denominator
        Precondition: value is an int >= 0
        """
        # enforce invariant
        assert isinstance(value, int), repr(value)+' is not an int'
        assert value > 0, repr(value)+' is not positive'
        # assign to attribute
        self._denominator = 2 ** value

    def __init__(self,k,n):
         """
         Initializes a fraction k/2n

         Parameter k: The numerator
         Precondition: k is an int

         Parameter n: The exponent for binary fraction 2 ** n
         Precondition: n is an int >= 0
         """
         assert type(n) == int and n >= 0
         # This works because we OVERRIDE setDenominator
         super().__init__(k,n)
