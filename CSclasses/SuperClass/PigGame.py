# -*- coding: utf-8 -*-
"""
@Time: 2021/1/28 16:10
@Author: LizzieDeng
@File: PigGame.py
@Description:
"""
#
#
# def range2iter(n):
#     """
#     Generator for the squares
#     of numbers 0 to n-1
#     Precon: n is an int >= 0
#     """
#     for x in range(n):
#         yield x*x
#
# a = range2iter(10)
# print(a)
# ite = [x for x in range2iter(10)]
# print(ite)
# b = next(a)
# print("b is {}".format(b))
# print('a send a value {} back'.format(a.send(1)))
# # print("len(list(a))", len(list(a)))
# c = next(a)
#
# print("c is {}".format(c))
# print('a send a value {} back'.format(a.send(100)))
# print(list(a))
#


def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
               value = (yield value)
            except Exception as e:
               value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")


generator = echo(1)
print(next(generator))
print(next(generator))
print(generator.send(2))
# generator.close()
print(generator)
print(next(generator))
print('list is {}'.format([i for i in generator]))
