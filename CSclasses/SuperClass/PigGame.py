# -*- coding: utf-8 -*-
"""
@Time: 2021/1/28 16:10
@Author: LizzieDeng
@File: PigGame.py
@Description:
"""


def range2iter(n):
    """
    Generator for the squares
    of numbers 0 to n-1
    Precon: n is an int >= 0
    """
    for x in range(n):
        yield x*x

print(range2iter(10))
ite = [x for x in range2iter(10)]
print(ite)
