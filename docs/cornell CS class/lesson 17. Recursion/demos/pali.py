"""
Functions showing how helpers interact with recursion

The first version of palindrome is simple.  All we have to
do is to implement the recursion as described in the
specification.  However, when we want to mix it up a bit,
then we have think about integrating helpers.

Author: Walker M. White (wmw2)
Date:   October 10, 2018
"""


def ispalindrome(s):
    """
    Returns true if s is a palindrome

    There are two ways to define a palindrome:
      1. s is a palindrome if it reads the same backward
         and forward.
      2. s is a palindrome if either
         (1) its length is <= 1   OR
         (2) its first and last chars are the same and the
             string between them is a palindrome.
      Letters must match exactly.

    Parameter s: the candidate palindrome
    Precondition s is a string
    """
    assert type(s) == str, repr(s) + ' is not a string'     # get in the habit

    # Base palindrome
    if len(s) < 2:
        return True

    # s has at least 2 characters
    ends = s[0] == s[-1]
    middle = ispalindrome(s[1:-1])

    # Both must be true to be a palindrome
    return ends and middle


def ispalindrome2(s):
    """
    Returns true if s is a palindrome

    There are two ways to define a palindrome:
      1. s is a palindrome if it reads the same backward
         and forward.
      2. s is a palindrome if either
         (1) its length is <= 1   OR
         (2) its first and last chars are the same and the
             string between them is a palindrome.
      Letters that differ only in case are considered to
      match.

    Parameter s: the candidate palindrome
    Precondition s is a string
    """
    # get in the habit
    assert type(s) == str, repr(s) + ' is not a string'

    # Base palindrome
    if len(s) < 2:
        return True

    # s has at least 2 characters
    ends = equals_ignore_case(s[0], s[-1])
    middle = ispalindrome2(s[1:-1])

    # Both must be true to be a palindrome
    return ends and middle

    # This also works by the way
    #return equals_ignore_case(s,reverse(s))


def ispalindrome_loosely(s):
    """
    Returns true if s is a palindrome paying attention
    only to the letters

    Case and any non-letter characters are ignored.

    Parameter s: the candidate palindrome
    Precondition s is a string
    """
    assert type(s) == str, repr(s) + ' is not a string'     # get in the habit
    return ispalindrome2(depunct(s))


def equals_ignore_case(c, d):
    """
    Returns true if strings c and d differ only in case,
    if at all

    Parameter c: first string to compare
    Preconditon: c is a string

    Parameter d: second string to compare
    Preconditon: d is a string
    """
    assert type(c) == str, repr(c) + ' is not a string'     # get in the habit
    assert type(d) == str, repr(d) + ' is not a string'     # get in the habit

    return c.upper() == d.upper()


# HELPER FUNCTIONS
def depunct(s):
    """
    Returns s but with everything that is not a letter
    removed

    Parameter: s the string to edit
    Precondition s is a string
    """
    assert type(s) == str, repr(s) + ' is not a string'     # get in the habit


    # Work on small data  (BASE CASE)
    if s == '':
        return s

    # Break up the data   (RECUSIVE CASE)
    left = s[0]
    if not s[0].isalpha():
        left = ''
    right = depunct(s[1:])

    # Combine the results
    return left+right


def reverse(s):
    """
    Returns s with its characters in reverse order

    Parameter: s the string to reverse
    Precondition s is a string
    """
    assert type(s) == str, repr(s) + ' is not a string'     # get in the habit

    # Work on small data  (BASE CASE)
    if s == '':
        return s

    # Break up the data   (RECUSIVE CASE)
    left  = s[0]  # Reverse of one letter is itself
    right = reverse(s[1:])

    # Combine the results
    return right+left
