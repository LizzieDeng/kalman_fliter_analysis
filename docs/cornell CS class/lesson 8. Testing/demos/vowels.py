"""
A module with a well-specified function

Author: Walker M. White
Date:   February 14, 2019
"""


def number_vowels(w):
    """
    Returns: number of vowels in string w.

    Vowels are defined to be 'a','e','i','o', and 'u'. 'y' is a
    vowel if it is not at the start of the word.

    Repeated vowels are counted separately. Both upper case and
    lower case vowels are counted.

    Examples:
        number_vowels('hat') returns 1
        number_vowels('hate') returns 2
        number_vowels('beet') returns 2
        number_vowels('sky') returns 1
        number_vowels('year') returns 2
        number_vowels('xxx') returns 0

    Parameter w: The text to check for vowels
    Precondition: w string w/ at least one letter and only letters
    """
    a = w.count('a')
    e = w.count('e')
    i = w.count('i')
    o = w.count('o')
    u = w.count('u')
    y = w[1:].count('y')
    return a+e+i+o+u+y
