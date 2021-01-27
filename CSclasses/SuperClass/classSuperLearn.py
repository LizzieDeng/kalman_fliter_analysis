# -*- coding: utf-8 -*-
"""
@Time: 2021/1/27 16:37
@Author: LizzieDeng
@File: classSuperLearn.py
@Description:
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
        super().__init__()
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
