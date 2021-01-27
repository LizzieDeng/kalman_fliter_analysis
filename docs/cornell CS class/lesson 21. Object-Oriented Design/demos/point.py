"""
A module with a simple Point3 class.

This module has a simpler version of the Point class.  The primary purpose
of this module is to show off the built-in methods __str__ and __repr___

Author: Walker White (wmw2)
Date:   October 20, 2019
"""
import math


class Point3(object):
    """
    A class to represent a point in 3D space
    
    Attribute x: The x-coordinate
    Invariant: x is a float
    
    Attribute y: The y-coordinate
    Invariant: y is a float
    
    Attribute z: The y-coordinate
    Invariant: z is a float
    """
    
    # INITIALIZER
    def __init__(self,x=0.0,y=0.0,z=0.0):
        """
        Initializes a new Point3
        
        Parameter x: the x-coordinate (default is 0.0)
        Precondition: x is a float (or optional)
        
        Parameter y: the y-coordinate (default is 0.0)
        Precondition: y is a float (or optional)
        
        Parameter z: the z-coordinate (default is 0.0)
        Precondition: z is a float (or optional)
        """
        self.x = x # x is parameter, self.x is field
        self.y = y # y is parameter, self.y is field
        self.z = z # z is parameter, self.z is field
    
    def __str__(self):
        """
        Returns: this Point as a string '(x, y, z)'
        """
        return '('+str(self.x)+', '+str(self.y)+', '+str(self.z)+')'
    
    def __repr__(self):
        """
        Returns: unambiguous representation of Point3
        """
        return str(self.__class__)+str(self)
    
    def distance(self,other):
        """
        Returns: Distance from self to other
        
        Parameter other: the point to measure to
        Precondition: other is a Point3
        """
        assert type(other) == Point3, repr(other)+' is not a Point3'
        dx = (self.x-other.x)*(self.x-other.x)
        dy = (self.y-other.y)*(self.y-other.y)
        dz = (self.z-other.z)*(self.z-other.z)
        return math.sqrt(dx+dy+dz)
