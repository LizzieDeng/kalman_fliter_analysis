"""
Test script for the module anglicize

Author: Walker M. White
Date:   March 30, 2019
"""
import introcs              # testing functions
import angl                 # functions to be tested


def test_anglicize():
    """
    Test procedure for the function anglicize
    """
    print('Testing anglicize')

    result = angl.anglicize(1)
    introcs.assert_equals("one", result)

    result = angl.anglicize(2)
    introcs.assert_equals("two", result)

    result = angl.anglicize(3)
    introcs.assert_equals("three", result)

    result = angl.anglicize(4)
    introcs.assert_equals("four", result)

    result = angl.anglicize(5)
    introcs.assert_equals("five", result)

    result = angl.anglicize(6)
    introcs.assert_equals("six", result)

    result = angl.anglicize(7)
    introcs.assert_equals("seven", result)

    result = angl.anglicize(8)
    introcs.assert_equals("eight", result)

    result = angl.anglicize(9)
    introcs.assert_equals("nine", result)

    result = angl.anglicize(10)
    introcs.assert_equals("ten", result)

    result = angl.anglicize(11)
    introcs.assert_equals("eleven", result)

    result = angl.anglicize(12)
    introcs.assert_equals("twelve", result)

    result = angl.anglicize(13)
    introcs.assert_equals("thirteen", result)

    result = angl.anglicize(14)
    introcs.assert_equals("fourteen", result)

    result = angl.anglicize(15)
    introcs.assert_equals("fifteen", result)

    result = angl.anglicize(16)
    introcs.assert_equals("sixteen", result)

    result = angl.anglicize(17)
    introcs.assert_equals("seventeen", result)

    result = angl.anglicize(18)
    introcs.assert_equals("eighteen", result)

    result = angl.anglicize(19)
    introcs.assert_equals("nineteen", result)


# Script code
test_anglicize()
print('Module angl passed all tests')
