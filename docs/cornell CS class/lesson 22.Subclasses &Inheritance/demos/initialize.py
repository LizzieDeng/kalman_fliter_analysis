"""
A CS1110 lecture example for initialization of subclasses

This is just demonstrating syntax, so there are no specifications.

Authors: Steve Marschner (srm2), Lillian Lee (ljl2), and Walker M. White (wmw2)
Date:    October 28, 2017 (Python 3 Version)
"""

class A(object):

    def __init__(self):
        self.x = 3
        self.y = 5

    def f(self):
        print('A.f: self.x:', self.x)
        print('A.f: self.y:', self.y)

class B(A):

    def __init__(self):
        super().__init__(self)
        self.y = 4
        self.z = 42

    def f(self):
        super().f()
        print('B.f self.y:', self.y)
        print('B.f self.z:', self.z)

# Script code
if __name__ == '__main__':
    a = A()
    b = B()

    a.f()
    b.f()
