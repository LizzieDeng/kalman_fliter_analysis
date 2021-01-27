"""
A CS1110 lecture example for overriding of methods and class variables

This is just demonstrating syntax, so there are no specifications.

Authors: Steve Marschner (srm2), Lillian Lee (ljl2), and Walker M. White (wmw2)
Date:    October 28, 2017 (Python 3 Version)
"""


class A(object):
    x = 3
    y = 5
    
    def f(self):
        self.g()
    
    def g(self):
        print('  this is A.g')

class B(A):
    y = 4
    z = 42
    
    def g(self):
        print('  this is B.g')
    
    def h(self):
        print('  this is B.h')

# Script code
if __name__ == '__main__':
    a = A()
    b = B()   
    
    print('a.f():')
    a.f()
    print('b.f():')
    b.f()
    print('b.y:', b.y)
    print('b.x:', b.x)
    print('A.y:', A.y)
    print('B.x:', B.x)
