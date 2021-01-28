"""
A module to show off dictionary comprehension.

Dictionary comprehension is similar to list comprehension
except that you put the generator expression inside of {}
instead of [].

Author: Walker M. White (wmw2)
Date: October 28, 2020
"""


GRADES = {'jrs1':80,'jrs2':92,'wmw2':50,'abc1':95}


def histogram(s):
    """
    Returns a histogram (dictionary) of the # of letters
    in string s.

    The letters in s are keys, and the count of each letter
    is the value. If the letter is not in s, then there is
    NO KEY for it in the histogram.

    Example: histogram('') returns {},
             histogram('all') returns {'a':1,'l':2}
             histogram('abracadabra') returns
                {'a':5,'b':2,'c':1,'d':1,'r':2}

    Parameter s: The string to analyze
    Precondition: s is a string (possibly empty).
    """
    # DICTIONARY COMPREHENSION
    #return { x:s.count(x) for x in s }

    # ACCUMULATOR PATTERN
    result = {}
    for x in s:
        result[x] = s.count(x)
    return result


def halve_grades(grades):
    """
    Returns a copy of grades, cutting all of the exam grades in half.

    Parameter grades: The dictionary of student grades
    Precondition: grades has netids as keys, ints as values.
    """
    # DICTIONARY COMPREHENSION
    #return { k:grades[k]//2 for k in grades }

    # ACCUMULATOR PATTERN
    result = {}
    for k in grades:
        result[k] = grades[k]//2
    return result


def extra_credit(grades,students,bonus):
    """
    Returns a copy of grades with extra credit assigned

    The dictionary returned adds a bonus to the grade of
    every student whose netid is in the list students.

    Parameter grades: The dictionary of student grades
    Precondition: grades has netids as keys, ints as values.

    Parameter netids: The list of students to give extra credit
    Precondition: netids is a list of valid (string) netids

    Parameter bonus: The extra credit bonus to award
    Precondition: bonus is an int
    """
    # DICTIONARY COMPREHENSION
    #return { k:(grades[k]+bonus if k in students else grades[k]) for k in grades }

    # ACCUMULATOR PATTERN
    result = {}
    for k in  grades:
        if k in students:
            result[k] = grades[k]+bonus
        else:
            result[k] = grades[k]
    return result
