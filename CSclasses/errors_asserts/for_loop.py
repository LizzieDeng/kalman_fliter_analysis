# -*- coding: utf-8 -*-
"""
@Time: 2021/1/25 12:52
@Author: LizzieDeng
@File: for_loop.py
@Description:
"""


def partition(s):
    """Returns: a list splitting s in two parts
    Precondition: s is a string."""
    first = ""
    second = ""
    # for x in s:
    #     pos = s.find(x)
    #     print(pos)
    #     if pos % 2 == 0:
    #         first += x
    #     else:
    #         second += x
    for pos in range(len(s)):
        if pos % 2 == 0:
            first = first + s[pos]
        else:
            second = second + s[pos]
    return [first, second]


a = partition("aabb")
print(a)
