# -*- coding: utf-8 -*-
"""
@Time: 2021/1/27 14:55
@Author: LizzieDeng
@File: DictLearn.py
@Description:
"""


def max_grade(grades):
    """Returns max grade in the grade dictionary
    Precondition: grades has netids as keys, ints as values"""

    maximum_grade = 0
    for key in grades.keys():
        if grades[key] > maximum_grade:
            maximum_grade = grades[key]
    return maximum_grade


def netids_above_cutoff(grades, cutoff):
    """Returns list of netids with grades above or equal cutoff
    Precondition: grades has netids as keys, ints as values.
    cutoff is an int."""
    netid = []
    for key in grades.keys():
        if grades[key] >= cutoff:
            netid.append(key)
    return netid


def give_extra_credit(grades, netids, bonus):
    """Gives bonus points to everyone in sequence netids
    Precondition: grades has netids as keys, ints as values.
    netids is a sequence of strings that are keys in grades
    bonus is an int."""
    for key in grades.keys():
        if key in netids:
            grades[key] += bonus


def add(x, y):
    """Returns x+y """
    return x + y


d = {'x': 1, 'y': 2}
print(add(**d))
grades_dict = {'l': 90, 'p': 33, 'e': 100}
print(max_grade(grades_dict))
print(netids_above_cutoff(grades_dict, 40))
