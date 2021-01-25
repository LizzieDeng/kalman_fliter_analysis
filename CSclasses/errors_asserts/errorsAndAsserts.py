# -*- coding: utf-8 -*-
"""
@Time: 2021/1/25 10:16
@Author: LizzieDeng
@File: errorsAndAsserts.py
@Description:
"""

"""
python asserts 断言用于判断一个表达式，在表达式为False时触发异常
语法：
assert expression [, arguments]
"""


def is_two_words(w):
    """
    Returns: True if w is 2 words sep by 1 or more spaces.

    A word is a string with no spaces. So this means that
        1. The first characters is not a space (or empty)
        2. The last character is not a space (or empty)
        3. There is at least one space in the middle
        4. If there is more than one space, the spaces are adjacent

    Parameter w: the string to test
    Precondition: w is a string
    """
    if not ' ' in w:
        return False

    # Find the first space
    first = w.find(' ')
    # Find the Last space
    last = w.rfind(' ')

    # Break the string into three parts
    w0 = w[:first]
    w1 = w[first:last + 1]
    w2 = w[last + 1:]

    # Make sure middle is only spaces
    cond1 = w1.count(' ') == len(w1)
    # Make sure other strings not empty
    cond0 = w0 != ''
    cond2 = w2 != ''

    return cond0 and cond1 and cond2


def last_name_first(n):
    """Returns: copy of n in form 'last-name, first-name'
    Precondition: n string in form 'first-name last-name
    n has only space, separating first and last."""

    assert type(n) == str, str(n) + " is not a string"
    assert is_two_words(n), n+' has the wrong form'

    # Compute the value
    end_first = n.find(' ')
    first = n[:end_first]
    last = n[end_first + 1:]
    return last + ', ' + first


def to_centigrade(x):
    """
    Returns: x converted to centigrade

    The value returned has type float.

    Parameter x: the temperature in fahrenheit
    Precondition: x is a float
    """
    assert type(x) == float, repr(x)+' is not a float'
    return 5*(x-32)/9.0


def is_float(s):
    """

    :param s: s is a string
    :return: True if string s can be cast to a float
    """
    try:
        x = float(s)
        return True
    except:
        return False


def error_handling():
    # 1. use conditional
    # results = input("number:")
    # if is_float(results):
    #     x = float(results)
    #     print('The next number is '+str(x+1))
    # else:
    #     print("That is not a number")
    # 2. use Try except
    try:
        results = input("number:")
        x = float(results)
        print('The next number is ' + str(x + 1))
    except:
        print('That is not a number!')

# a = '1 '
# print(last_name_first(a))
# print(to_centigrade(a))
# error_handling()


#   ############ tracking control flow ########################
def third(x):
    print("Starting third")
    assert x < 1
    print("ending third")


def second(x):
    print("starting second")
    try:
        third(x)
    except:
        print("caught at second")
    print("ending second")


def first(x):
    print("staring first.")
    try:
        second(x)
    except:
        print("caught at first")
    print("Ending first")

first(2)
