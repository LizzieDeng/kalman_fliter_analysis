"""
A module with a slightly more interesting class

Author: Steve Marschner (srm2), Walker M. White (wmw2)
Date:   October 10, 2019
"""


class Example2(object):
    """
    A class that defines some things.
    """
    
    # This is a class variable.
    a = 29
    
    def set_b(self, x):
        """
        Assigns x to instance variable b
        """
        print(type(self))
        self.b = x
    
    def f(self):
        """
        Returns multiple of class variable a and instance variable b
        """
        return self.a * self.b
