"""
Test script for simple divide-and-conquer functions.

Author: Walker M. White (wmw2)
Date:   October 10, 2017 (Python 3 Version)
"""
import introcs
import simple
import de2
import com

def test_length():
    """
    Test the function length
    """
    print('Testing length')
    introcs.assert_equals(0,  simple.length(''))
    introcs.assert_equals(1,  simple.length('e'))
    introcs.assert_equals(7,  simple.length('ceceddd'))
    introcs.assert_equals(15, simple.length('*0;jh=52y;jh=`5'))


def test_num_e():
    """
    Test the function num_e
    """
    print('Testing num_e')
    introcs.assert_equals(0,  simple.num_e(''))
    introcs.assert_equals(1,  simple.num_e('e'))
    introcs.assert_equals(0,  simple.num_e('c'))
    introcs.assert_equals(2,  simple.num_e('ceceddd'))
    introcs.assert_equals(0,  simple.num_e('asdfasdfadsf'))


def test_deblank():
    """
    Test the function deblank
    """
    print('Testing deblank')
    introcs.assert_equals('',   de2.deblank(''));
    introcs.assert_equals('',   de2.deblank(' '));
    introcs.assert_equals('B',  de2.deblank('B'));
    introcs.assert_equals('BG', de2.deblank('B G'));
    introcs.assert_equals('',   de2.deblank('         '));


def test_depunct():
    """
    Test the function depunct
    """
    print('Testing depunct')
    introcs.assert_equals('',    de2.depunct('(@$*&@'));
    introcs.assert_equals('foo', de2.depunct('  f,o**o!!!'));
    introcs.assert_equals('foo', de2.depunct('f  (!*@&,.<>:\'  oo'));


def test_commafy():
    """
    Tests the (string-based) commafy function
    """
    print('Testing commafy')
    introcs.assert_equals('5',           com.commafy(5))
    introcs.assert_equals('12',          com.commafy(12))
    introcs.assert_equals('952',         com.commafy(952))
    introcs.assert_equals('999',         com.commafy(999))
    introcs.assert_equals('1,000',       com.commafy(1000))
    introcs.assert_equals('23,456',      com.commafy(23456))
    introcs.assert_equals('12,345,678',  com.commafy(12345678))
    introcs.assert_equals('912,345,678', com.commafy(912345678))


# Application Code
if __name__ == '__main__':
    test_length()
    test_num_e()
    test_deblank()
    test_depunct()
    test_commafy()
    print('Modules simple, de2, and com passed all tests.')
