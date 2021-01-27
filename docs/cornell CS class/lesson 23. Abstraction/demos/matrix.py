"""
A module with a simple 2x2 matrix

This module contains a both a 2d point and 2x2
matrix that we can multiply a point.

Author: Walker M. White (wmw2)
Date: October 10, 2020
"""
import math


class Point2(object):
    """
    A class representing a point in 2-dimensional space.

    The point has two attributes: x and y. It represents
    a point of the form (x,y). It is a mutable object,
    so the attributes values can be altered at any time.
    """

    def getX(self):
        """
        Gets x coordinate.

        The value is a float.
        """
        return self._x

    def setX(self,value):
        """
        Sets x coordinate.

        Parameter value: The value to assign x
        Precondition: value is an int or float
        """
        assert type(value) in [int,float], repr(value)+' is not a number'
        self._x = float(value)

    def getY(self):
        """
        Gets x coordinate.

        The value is a float.
        """
        return self._y

    def setY(self,value):
        """
        Sets x coordinate.

        Parameter value: The value to assign x
        Precondition: value is an int or float
        """
        assert type(value) in [int,float], repr(value)+' is not a number'
        self._y = float(value)

    def __init__(self,x=0.0,y=0.0):
        """
        Initializes a new Point (x, y).

        Parameter x: initial x value, default 0
        Precondition: a number (float or int).

        Parameter y: initial y value, default 0
        Precondition: a number (float or int).
        """
        self.setX(x)
        self.setY(y)

    def __add__(self, other):
        """
        Returns a new point that is the sum of this and
        other.

        This method should not alter the contents of
        either self or other.

        Parameter other: the point to add
        Precondition: other is a Point2 object
        """
        assert (type(other) == Point2), "Illegal addition with "+repr(other)
        return Point2(self.x+other.x,self.y+other.y)

    def __eq__(self,other):
        """
        Returns True if other is a Point2 with same
        contents as this one; False otherwise

        Parameter other: the point to compare
        Precondition: other can be anything
        """
        return (type(other) == Point2 and
                self._x == other._x and
                self._y == other._y)

    def __str__(self):
        """
        Returns a string represntation of this point
        """
        return '('+str(self.getX())+', '+str(self.getY())+')'

    def __repr__(self):
        """
        Returns a string represntation of this point
        """
        return self.__str__()


class Matrix(object):
    """
    A class representing a 2x2 matrice.

    The matrix has three attributes: a, b, c, and d.
    It represents a matrix of the form:

        a    b
        c    d

    It is a *immutable* object, so the attributes values
    cannot be altered after the object is constructed.
    """

    def getA(self):
        """
        The top left value of the matrix

        Invariant: the value is a float.  This is
        immutable and may not be altered.
        """
        return self._a00

    def getB(self):
        """
        The top right value of the matrix

        Invariant: the value is a float.  This is
        immutable and may not be altered.
        """
        return self._a01

    def getC(self):
        """
        The bottom left value of the matrix

        Invariant: the value is a float.  This is
        immutable and may not be altered.
        """
        return self._a10

    def getD(self):
        """
        The bottom right value of the matrix

        Invariant: the value is a float.  This is
        immutable and may not be altered.
        """
        return self._a11

    def __init__(self,a=1,b=0,c=0,d=1):
        """
        Initializes a new Matrix [[a, b], [c, d]]

        Parameter a: initial a value, defaults to 1
        Precondition: a is a number (float or int)

        Parameter b: initial b value, defaults to 0
        Precondition: b is a number (float or int)

        Parameter c: initial c value, defaults to 0
        Precondition: c is a number (float or int)

        Parameter d: initial d value, defaults to 1
        Precondition: d is a number (float or int)
        """
        self._a00 = float(a)
        self._a01 = float(b)
        self._a10 = float(c)
        self._a11 = float(d)

    @classmethod
    def createRotation(cls,angle=0):
        """
        Creates a new matrix for rotation

        A rotation matrix will rotate space about
        the origin.

        Parameter angle: The rotation angle in degrees
        Precondition: angle is a number (int or float)
        """
        radians = math.pi*angle/180.0
        c = math.cos(radians)
        s = math.sin(radians)
        return Matrix(c,-s,s,c)
        # Alternatively, we could to this
        #return cls(c,-s,s,c)

    @classmethod
    def createScale(cls,sx=1,sy=1):
        """
        Creates a new matrix for scaling

        A scale matrix is one the causes space to
        grow or shrink.

        Parameter sx: The amount to scale x axis
        Precondition: sx is a number (int or float)

        Parameter sy: The amount to scale y axis
        Precondition: sy is a number (int or float)
        """
        return Matrix(sx,0,0,sy)
        # Alternatively, we could to this
        #return cls(sx,0,0,sy)

    @classmethod
    def createShearX(cls,value=0):
        """
        Creates a new shear matrix paralel the x-axis

        A shear matrix will stretch on parallel to
        the given axis.

        Parameter value: The amount to stretch
        Precondition: value is a number (int or float)
        """
        return Matrix(1,value,0,1)
        # Alternatively, we could to this
        #return cls(1,value,0,1)

    @classmethod
    def createShearY(cls,value=0):
        """
        Creates a new shear matrix paralel the y-axis

        A shear matrix will stretch on parallel to
        the given axis.

        Parameter value: The amount to stretch
        Precondition: value is a number (int or float)
        """
        return Matrix(1,0,value,1)
        # Alternatively, we could to this
        #return cls(1,0,value,1)

    def __eq__(self,other):
        """
        Returns True if other is a Matrix with same
        contents as this one; False otherwise

        Parameter other: The object to compare
        Precondition: other can be anything
        """
        return (type(other) == Matrix and
                self.getA() == other.getA() and
                self.getB() == other.getB() and
                self.getC() == other.getA() and
                self.getD() == other.getD())

    def __mul__(self, other):
        """
        Returns a new value which is the mutliple of this
        Matrix and other

        If other is a Point2, the result is a Point2 using
        standard Matrix * Point2 multiplication.

        It other is a Matrix, the result is a Matrix using
        matrix multiplication. We assume that self is the
        matrix on the left and other is on the right.

        Parameter other: the value to multiply
        Precondition: other is either a Matrix or a Point2.
        """
        assert (type(other) == Matrix or
                type(other) == Point2), "Illegal multiplication with "+repr(other)
        if (type(other) == Matrix):
            return self._multiplyMatrix(other)
        return self._multiplyPoint2(other)

    # Private helper method for matrix multiplication
    def _multiplyMatrix(self, other):
        """
        Returns a new value which is the mutliple of this
        Matrix and other

        Parameter other: the value to multiply
        Precondition: other is a Matrix
        """
        return Matrix(self.getA()*other.getA()+self.getB()*other.getC(),
                      self.getA()*other.getB()+self.getB()*other.getD(),
                      self.getC()*other.getA()+self.getD()*other.getC(),
                      self.getC()*other.getB()+self.getD()*other.getD())

    # Private helper method for matrix*point multiplication
    def _multiplyPoint2(self, other):
        """
        Returns a new value which is the mutliple of this
        Matrix and other

        Parameter other: the value to multiply
        Precondition: other is a Point2
        """
        return Point2(self.getA()*other.getX()+
                        self.getB()*other.getY(),
                      self.getC()*other.getX()+
                        self.getD()*other.getY())

    def __str__(self):
        """
        Returns a string represntation of this point
        """
        row1 = '[ %.3f, %.3f ]' % (self.getA(), self.getB())
        row2 = '[ %.3f, %.3f ]' % (self.getC(), self.getD())
        return '['+row1+', '+row2+']'

    def __repr__(self):
        """
        Returns a string represntation of this point
        """
        return self.__str__()

    def show(self):
        """
        Displays the matrix using a multiline format
        """
        # This will help the table line up nicely
        a = ('%.3f' % self.getA()).rjust(6)
        b = ('%.3f' % self.getB()).rjust(6)
        c = ('%.3f' % self.getC()).rjust(6)
        d = ('%.3f' % self.getD()).rjust(6)
        print('| '+a+' '+b+' |')
        print('| '+c+' '+d+' |')
