"""
A module with a simple Point class.

This module has a simpler version of the Point class than
what we saw in previous labs.  It shows off the minimum
that we need to get started with a class.

Author: Walker M. White (wmw2)
Date:   October 1, 2017 (Python 3 Version)
"""
import math


class Point(object):
    """
    A class to represent a point in 3D space

    Attribute x: The x-coordinate
    Invariant: x is a float

    Attribute y: The y-coordinate
    Invariant: y is a float

    Attribute z: The z-coordinate
    Invariant: z is a float
    """

    def __init__(self,x=0.0,y=0.0,z=4.0):
        """
        Initializers a new Point3

        Parameter x: The x-coordinate
        Precondition: x is a float

        Parameter y: The y-coordinate
        Precondition: y is a float

        Parameter z: The z-coordinate
        Precondition: z is a float
        """
        self.x = x # x is parameter, self.x is attribute
        self.y = y # y is parameter, self.y is attribute
        self.z = z # z is parameter, self.z is attribute

    def __str__(self):
        """
        Returns this Point as a string '(x, y, z)'
        """
        return '('+str(self.x)+', '+str(self.y)+', '+str(self.z)+')'

    def __repr__(self):
        """
        Returns an unambiguous representation of this point
        """
        return str(self.__class__)+str(self)

    def __eq__(self,other):
        """
        Returns True if other is a point equal to this one.

        Parameter other: The point to compare
        Precondition: other is a Point
        """
        assert type(other) == Point, repr(other)+' is not a Point'
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self,other):
        """
        Returns a new point that is the pointwise sum of self and other

        Parameter other: The point to add
        Precondition: other is a Point
        """
        assert type(other) == Point, repr(other)+' is not a Point'
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def distance(self,other):
        """
        Returns the distance from self to other

        Parameter other: The point to compare
        Precondition: other is a Point
        """
        assert type(other) == Point, repr(other)+' is not a Point'
        dx = (self.x-other.x)*(self.x-other.x)
        dy = (self.y-other.y)*(self.y-other.y)
        dz = (self.z-other.z)*(self.z-other.z)
        return math.sqrt(dx+dy+dz)
