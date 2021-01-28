# -*- coding: utf-8 -*-
"""
@Time: 2021/1/28 14:44
@Author: LizzieDeng
@File: GettingAttr.py
@Description:
"""
import random
import introcs
import time

def create_color():
    """
    Returns a randomly constructed color value
    """
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    a = random.randint(0,255)
    return introcs.RGB(r,g,b,a)


def main():
    """
    Runs the script, promping for user input.
    """
    print('Generating random color')
    c = create_color()
    print("c is {}".format(c))
    attr = input('Specify an attribute: ')
    if hasattr(c, attr):
        print('The '+attr+' attribute is '+str(getattr(c,attr)))
    else:
        print('There is no attribute '+attr+'.')


# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit(func):
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('Time Elapsed:', end - start)

        # 将包装后的函数返回

    return wrapper


@timeit
def foo():
    print("this is a test")


def rem3(lst):
    """Remove all 3's from lst"""
    i = 0
    while i < len(lst):
        if lst[i] == 3:
            del lst[i]
        else:
            i = i + 1
    return lst


if __name__ == '__main__':
    # main()
    foo()
    # print(float('1'))
    lst = rem3([3,3,4])
    print(lst)
