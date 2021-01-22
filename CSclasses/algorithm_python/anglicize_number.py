# -*- coding: utf-8 -*-
"""
@Time: 2021/1/22 15:15
@Author: LizzieDeng
@File: anglicize_number.py
@Description: Functions to anglicize integers in the range 1..999,999, The primary function in this module is anglicize(). This is a
great module to help you understand preconditions.
"""


def anglicize1to19(n):
    """
    :return: English equivalent of n
    precondition: 0 < n < 20
    """
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'

    # n = 19
    return 'nineteen'


def tens(n):
    """
    :param n: n in 2..9
    :return: tens-word for n
    """
    if n == 2:
        return 'twenty'
    elif n == 3:
        return 'thirty'
    elif n == 4:
        return 'forty'
    elif n == 5:
        return 'fifty'
    elif n == 6:
        return 'sixty'
    elif n == 7:
        return 'seventy'
    elif n == 8:
        return 'eighty'

    return 'ninety'


def anglicize1to99(n):
    """
    precondition: 0 < n < 99
    :param n:
    :return: English equivalent of n
    """
    if n < 20:
        return anglicize1to19(n)
    else:
        twen = n % 10
        if 0 < twen < 20:
            return tens(n // 10) + ' ' + anglicize1to19(twen)
        else:
            return tens(n // 10)


def anglicize99to999(n):
    """
    99<n<1000
    :return:
    """
    hundred = n % 100
    if 0 < hundred < 100:
        st = anglicize1to99(hundred)
    else:
        st = ''

    return anglicize1to19(n // 100) + ' hundred ' + st


def anglicize1000plus(n):
    """

    :param n:
    :return:
    """
    thousand = n // 1000
    if 0 < thousand < 100:
        ths = anglicize1to99(thousand)
    elif 99 < thousand < 1000:
        ths = anglicize99to999(thousand)
    else:
        ths = ""
    thousand_plus = n % 1000
    if 0 < thousand_plus < 100:
        ths_plus = anglicize1to99(thousand_plus)
    elif 100 < thousand_plus < 1000:
        ths_plus = anglicize99to999(thousand_plus)
    else:
        ths_plus = ""
    return ths + ' thousand ' + ths_plus


def anglicize(n):
    """
    Example:
    3:  "three"
    45: "forty five"
    100: "one hundred"
    127: "one hundred twenty seven"
    1001: "one thousand one"
    990,099: "nine hundred ninety thousand ninety nine"

    :param n: integer, number
    precondition: 0 < n < 1,000, 000
    :return: English equivalent of n
    """
    if n < 0 or n >= 1000000:
        print("the input {} is not in the scope".format(n))
    elif n < 100:
        return anglicize1to99(n)
    elif n < 1000:
        return anglicize99to999(n)
    elif n >= 1000:
        return anglicize1000plus(n)


n = 1001
print(anglicize(n))
