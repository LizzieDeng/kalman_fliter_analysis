"""
A module with a simple Fraction class.

This version of Fraction has properties, which allow us
to enforce our invariants.  While we will not ask you to
do this on an exam, this is the preferred way to create
getters and setters by commercial Python developers.

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

    Attribute numerator: The fraction numerator
    Invariant: numerator is an int

    Attribute denominator: The fraction denominator
    Invariant: denominator is an int > 0
    """
    # Note that we are pretending properties are attributes
    # The user does not know otherwise

    # PROPERTIES
    @property   # getter
    def numerator(self):
        """
        The fraction numerator.

        Invariant: Must be an int.
        """
        return self._numerator # returns the attribute

    @numerator.setter   # setter
    def numerator(self,value):
        # DO NOT WRITE A SEPARATE SPECIFICATION FOR SETTER
        # enforce invariant
        assert isinstance(value,int), repr(value)+' is not an int'
        # assign to attribute
        self._numerator = value

    @property   # getter
    def denominator(self):
        """
        Fraction denominator.

        Invariant: Must be an int > 0.
        """
        return self._denominator # returns the attribute

    @denominator.setter   # setter
    def denominator(self,value):
        # DO NOT WRITE A SEPARATE SPECIFICATION FOR SETTER
        # enforce invariant
        assert isinstance(value,int), repr(value)+' is not an int'
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
        self.numerator = n
        self.denominator = d

    def __str__(self):
        """
        Returns this Fraction as a string 'n/d'
        """
        return repr(self.numerator)+'/'+repr(self.denominator)

    def __repr__(self):
        """
        Return the unambiguous representation of Fraction
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
        assert isinstance(other,Fraction) or \
               isinstance(other,int), repr(other)+' is not a valid operand'
        if isinstance(other,int):
            return self._multiplyInt(other)
        return self._multiplyFraction(other)

    # Private helper to multiply fractions
    def _multiplyFraction(self,other):
        """
        Return the product of self and other as a new
        Fraction

        This method does not modify the contents of self
        or other

        Parameter other: the fraction to multiply on the right
        Precondition: other is a Fraction
        """
        # No need to enforce preconditions on a hidden method
        top = self.numerator*other.numerator
        bot = self.denominator*other.denominator
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
        top = self.numerator*x
        bot = self.denominator
        return Fraction(top,bot)

    def __add__(self,other):
        """
        Returns the sum of self and other as a new
        Fraction

        This method does not modify the contents of self
        or other

        Parameter other: the value to add on the right
        Precondition: other is a Fraction or an int
        """
        assert isinstance(other,Fraction) or isinstance(other,int), repr(other)+' is not a valid operand'
        if isinstance(other,int):
            return self._addInt(other)
        return self._addFraction(other)

    # Private helper to add fractions
    def _addFraction(self,other):
        """
        Returns: The sum of self and other as a new
         Fraction

        This method does not modify the contents of self
        or other

        Parameter other: the fraction to add on the right
        Precondition: other is a Fraction
        """
        # No need to enforce preconditions on a hidden method
        bot = self.denominator*other.denominator
        top = (self.numerator*other.denominator+
               self.denominator*other.numerator)
        return Fraction(top,bot)

    # Private helper to add ints
    def _addInt(self,x):
        """
        Returns the sum of self and other as a new
        Fraction

        This method does not modify the contents of self
        or other

        Parameter other: the value to add on the right
        Precondition: other is an int
        """
        # No need to enforce preconditions on a hidden method
        bot = self.denominator
        top = (self.numerator+self.denominator*x)
        return Fraction(top,bot)

    # COMPARISONS
    def __eq__(self,other):
        """
        Returns true if self, other are equal Fractions.

        It returns False if they are not equal, or other
        is not a Fraction

        Parameter other: value to compare to this fraction
        Precondition: NONE
        """
        if not isinstance(other,Fraction) and not isinstance(other, int):
            return False

        if isinstance(other,int):
            return self.numerator == other*self.denominator

        # Cross multiply
        left = self.numerator*other.denominator
        rght = self.denominator*other.numerator
        return left == rght

    def __lt__(self,other):
        """
        Returns True if self < other, False otherwise

        This method is used to implement all strict
        comparison operations. Both < and > are determined
        automatically from this method.

        Parameter other: value to compare to this fraction
        Precondition: other is a Fraction
        """
        assert isinstance(other,Fraction) or isinstance(other,int), repr(other)+' is not a valid operand'

        if isinstance(other,int):
            return self.numerator < other*self.denominator

        # Cross multiply
        left = self.numerator*other.denominator
        rght = self.denominator*other.numerator
        return left < rght

    def __le__(self,other):
        """
        Returns True if self < other, False otherwise

        This method is used to implement all inclusive
        comparison operations.  Both <=  and >= are
        determined automatically from this method.

        Parameter other: value to compare to this fraction
        Precondition: other is a Fraction
        """
        assert isinstance(other,Fraction) or isinstance(other,int), repr(other)+' is not a valid operand'

        if isinstance(other,int):
            return self.numerator <= other*self.denominator

        # Cross multiply
        left = self.numerator*other.denominator
        rght = self.denominator*other.numerator
        return left <= rght

    # OTHER METHODS
    def reduce(self):
        """
        Normalizes this fraction into simplest form.

        Normalization ensures that the numerator and
        denominator have no common divisors.
        """
        g = gcd(self.numerator,self.denominator)
        self.numerator(self.numerator//g)
        self.denominator(self.denominator//g)
