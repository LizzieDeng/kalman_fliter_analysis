"""
A test script for palindrome functions.

Author: Walker M. White (wmw2)
Date:   October 10, 2018
"""
import introcs
import pali


def test_ispalindrome():
    """
    Tests the basic palindrome function
    """
    print('Testing ispalindrome')
    introcs.assert_equals(True,  pali.ispalindrome(''))
    introcs.assert_equals(True,  pali.ispalindrome('B'))
    introcs.assert_equals(True,  pali.ispalindrome('BB'))
    introcs.assert_equals(False, pali.ispalindrome('BA'))
    introcs.assert_equals(True,  pali.ispalindrome('BOB'))
    introcs.assert_equals(False, pali.ispalindrome('BOA'))
    introcs.assert_equals(True,
                              pali.ispalindrome('ablewasiereisawelba'))
    introcs.assert_equals(True,
                              pali.ispalindrome('amanaplanacanalpanama'))
    introcs.assert_equals(False,
                              pali.ispalindrome('Amanaplanacanalpanama'))
    introcs.assert_equals(False,
                              pali.ispalindrome('amanaplana canalpanama'))


def test_ispalindrome2():
    """
    Tests the palindrome function without case
    """
    print('Testing ispalindrome2')
    introcs.assert_equals(True,  pali.ispalindrome2(''))
    introcs.assert_equals(True,  pali.ispalindrome2('B'))
    introcs.assert_equals(True,  pali.ispalindrome2('BB'))
    introcs.assert_equals(False, pali.ispalindrome2('BA'))
    introcs.assert_equals(True,  pali.ispalindrome2('BOB'))
    introcs.assert_equals(False, pali.ispalindrome2('BOA'))
    introcs.assert_equals(True,
                              pali.ispalindrome2('ablewasiereisawelba'))
    introcs.assert_equals(True,
                              pali.ispalindrome2('amanaplanacanalpanama'))
    introcs.assert_equals(True,
                              pali.ispalindrome2('Amanaplanacanalpanama'))
    introcs.assert_equals(False,
                              pali.ispalindrome2('amanaplana canalpanama'))


def test_ispalindrome_loosely():
    """
    Tests the palindrome without case, non-letters
    """
    print('Testing ispalindrome_loosely')
    introcs.assert_equals(True,
        pali.ispalindrome_loosely('a**68(&!#7! a'))
    introcs.assert_equals(True,
        pali.ispalindrome_loosely('A man, a plan, a canal --Panama!'))
    introcs.assert_equals(False,
        pali.ispalindrome_loosely('A man, a plan, a cabal --Panama!'))


# Script Code
if __name__ == '__main__':
    test_ispalindrome()
    test_ispalindrome2()
    test_ispalindrome_loosely()
    print('Module palindrome passed all tests')
