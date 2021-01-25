"""
Script to show off test cases on functions with for-loops

This test script shows you how to test both immutable AND
mutable functions.  The latter are interesting because they
typically do not have a return-value. But they do modify
a parameter, and we check that instead of the return value.

Author: Walker M. White
Date:   August 15, 2020
"""
import introcs          # introcs assert functions
import accum2           # functions to be tested
import mut              # functions to be tested


def test_despace():
    """
    Test procedure for despace(s)
    """
    print('Testing despace')
    # One space
    result = accum2.despace('a b')
    introcs.assert_equals('ab',result)

    # Adjacent spaces
    result = accum2.despace('a  b')
    introcs.assert_equals('ab',result)

    # Non-adjacent spaces
    result = accum2.despace(' a b ')
    introcs.assert_equals('ab',result)

    # No spaces
    result = accum2.despace('ab')
    introcs.assert_equals('ab',result)

    # All spaces
    result = accum2.despace('    ')
    introcs.assert_equals('',result)


def test_reverse():
    """
    Test procedure for reverse(s)
    """
    print('Testing reverse')
    # One character
    result = accum2.reverse('a')
    introcs.assert_equals('a',result)

    # More than one charater
    result = accum2.reverse('abc')
    introcs.assert_equals('cba',result)

    # Empty string
    result = accum2.reverse('')
    introcs.assert_equals('',result)


def test_copy_add_one():
    """
    Test procedure for copy_add_one(x)
    """
    print('Testing copy_add_one')
    # List of one element
    x = [1]
    result = accum2.copy_add_one(x)
    introcs.assert_equals([2],result)
    # Make sure x is NOT modified
    introcs.assert_equals([1],x)

    # More than one element
    x = [2,5,-1]
    result = accum2.copy_add_one(x)
    introcs.assert_equals([3,6,0],result)
    # Make sure x is NOT modified
    introcs.assert_equals([2,5,-1],x)

    # Empty List
    x = []
    result = accum2.copy_add_one(x)
    introcs.assert_equals([],result)
    # Make sure x is NOT modified
    introcs.assert_equals([],x)


def test_add_one():
    """
    Test procedure for add_one(x)
    """
    print('Testing add_one')
    # List of one element
    x = [1]
    result = mut.add_one(x)
    # Make sure x was modified
    introcs.assert_equals([2],x)
    # Make sure NO value is returned
    introcs.assert_equals(None,result)

    # More than one element
    x = [2,5,-1]
    result = mut.add_one(x)
    # Make sure x was modified
    introcs.assert_equals([3,6,0],x)
    # Make sure NO value is returned
    introcs.assert_equals(None,result)

    # Empty List
    x = []
    result = mut.add_one(x)
    # Make sure x was modified
    introcs.assert_equals([],x)
    # Make sure NO value is returned
    introcs.assert_equals(None,result)


if __name__ == '__main__':
    test_despace()
    test_reverse()
    test_copy_add_one()
    test_add_one()
    print('Modules accum2 and mut passed all tests.')
