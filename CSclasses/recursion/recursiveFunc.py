# -*- coding: utf-8 -*-
"""
@Time: 2021/1/25 13:08
@Author: LizzieDeng
@File: recursiveFunc.py
@Description:
"""
import introcs

def fibonacci(n):
    """Returns: Fibonacci an
    Precondition: n ≥ 0 an int"""
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    """Returns: factorial of n.
    Pre: n ≥ 0 an int"""
    if n == 0:
        return 1
    return n * factorial(n-1)


def commafy(s):
    """
    Returns a copy of s, with commas every 3 digits.

    Example:
        commafy('5341267') = '5,341,267'

    Parameter s: string representing an integer
    Precondition: s a string with only digits, not starting with 0
    """
    if len(s) <= 3:
        return s
    left = commafy(s[0:-3])
    right = s[-3:]
    return left + ',' + right


def deblank(s):
    """
      Returns: s but with blanks removed

      Parameter: s the string to edit
      Precondition s is a string
      for example: deblank(' 1 23  4') returns '1234'
      """
    if s == '':
        return s
    elif len(s) == 1:
        if s != ' ':
            return s
        else:
            return ''
    left = deblank(s[0])

    right = deblank(s[1:])
    return left + right


def depunct(s):
    """
    Returns: s but with everything that is not a letter removed

    Parameter: s the string to edit
    Precondition s is a string
    """
    assert type(s) == str, repr(s) + ' is not a string'
    if s == '':
        return s
    elif len(s) == 1:
        if not introcs.isalpha(s):
            return ""
        else:
            return s
    left = depunct(s[0])
    right = depunct(s[1:])

    return left + right


def exp(b, c):
    """Returns: b**c
    Precondition: b a float, c ≥ 0 an int"""
    assert type(b) == float, repr(b) + " is not a float "
    assert c >= 0 and type(c) == int, repr(c) + 'is the wrong format'
    if c == 0:
        return 1
    left = b
    right = exp(b, c-1)

    return left * right


def exp_1(b, c):
    """Returns: b**c
       Precondition: b a float, c ≥ 0 an int"""
    if c == 0:
        return 1
    if c % 2 == 0:
        return exp(b, c//2) * exp(b, c//2)
    return b * exp_1(b, c-1)


def ispalindrome(s):
    """
    Returns: True if s is a palindrome 回文判断
    :param s:
    :return:
    """
    if len(s) < 2:
        return True
    start = s[0]
    end = s[-1]
    start_end = start.upper() == end.upper()
    middle = ispalindrome(s[1:-1])
    return start_end and middle


y = factorial(4)
fub = fibonacci(5)
print(y)
print(fub)
print(commafy('5341267'))
de_blank = deblank(' 113 4')
print(de_blank)
print((depunct(' 1a33vv ')))
print(exp(6.0, 4))
print(exp_1(6.0, 4))
print(ispalindrome('111222111'))




