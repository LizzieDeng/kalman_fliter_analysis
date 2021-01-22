"""
Test script for the module anglicize

Author: Walker M. White
Date:   September 10, 2019
"""
import introcs              # introcs assert functions
import anglicize            # function to be tested


def test_anglicize():
    """
    Test procedure for the primary anglicize function
    """
    print('Testing anglicize')
    result = anglicize.anglicize(1)
    introcs.assert_equals("one", result)
    
    result = anglicize.anglicize(19)
    introcs.assert_equals("nineteen", result)
    
    result = anglicize.anglicize(20)
    introcs.assert_equals("twenty", result)
    
    result = anglicize.anglicize(35)
    introcs.assert_equals("thirty five", result)
    
    result = anglicize.anglicize(50)
    introcs.assert_equals("fifty", result)
    
    result = anglicize.anglicize(99)
    introcs.assert_equals("ninety nine", result)
    
    result = anglicize.anglicize(100)
    introcs.assert_equals("one hundred", result)
    
    result = anglicize.anglicize(301)
    introcs.assert_equals("three hundred one", result)
    
    result = anglicize.anglicize(999)
    introcs.assert_equals("nine hundred ninety nine", result)
    
    result = anglicize.anglicize(1000)
    introcs.assert_equals("one thousand", result)
    
    result = anglicize.anglicize(1009)
    introcs.assert_equals("one thousand nine", result)
    
    result = anglicize.anglicize(900000)
    introcs.assert_equals("nine hundred thousand", result)
    
    result = anglicize.anglicize(789436)
    introcs.assert_equals("seven hundred eighty nine thousand four hundred thirty six",
                              result)


def test_anglicize1000():
    """
    Test procedure for the helper function anglicize1000
    """
    print('Testing anglicize1000')
    
    result = anglicize.anglicize1000(1)
    introcs.assert_equals("one", result)
    
    result = anglicize.anglicize1000(19)
    introcs.assert_equals("nineteen", result)
    
    result = anglicize.anglicize1000(20)
    introcs.assert_equals("twenty", result)
    
    result = anglicize.anglicize1000(35)
    introcs.assert_equals("thirty five", result)
    
    result = anglicize.anglicize1000(50)
    introcs.assert_equals("fifty", result)
    
    result = anglicize.anglicize1000(99)
    introcs.assert_equals("ninety nine", result)
    
    result = anglicize.anglicize1000(100)
    introcs.assert_equals("one hundred", result)
    
    result = anglicize.anglicize1000(301)
    introcs.assert_equals("three hundred one", result)
    
    result = anglicize.anglicize1000(999)
    introcs.assert_equals("nine hundred ninety nine", result)


def test_anglicize100to999():
    """
    Test procedure for the helper function anglicize100to999
    """
    print('Testing anglicize100to999')

    result = anglicize.anglicize100to999(100)
    introcs.assert_equals("one hundred", result)
    
    result = anglicize.anglicize100to999(301)
    introcs.assert_equals("three hundred one", result)
    
    result = anglicize.anglicize100to999(999)
    introcs.assert_equals("nine hundred ninety nine", result)


def test_anglicize20to99():
    """
    Test procedure for the helper function anglicize20to99
    """
    print('Testing anglicize20to99')

    result = anglicize.anglicize20to99(35)
    introcs.assert_equals("thirty five", result)
    
    result = anglicize.anglicize20to99(50)
    introcs.assert_equals("fifty", result)
    
    result = anglicize.anglicize20to99(99)
    introcs.assert_equals("ninety nine", result)


def test_anglicize1to19():
    """
    Test procedure for the helper function anglicize1to19
    """
    print('Testing anglicize1to19')
    
    result = anglicize.anglicize1to19(1)
    introcs.assert_equals("one", result)
    
    result = anglicize.anglicize1to19(2)
    introcs.assert_equals("two", result)
    
    result = anglicize.anglicize1to19(3)
    introcs.assert_equals("three", result)
    
    result = anglicize.anglicize1to19(4)
    introcs.assert_equals("four", result)
    
    result = anglicize.anglicize1to19(5)
    introcs.assert_equals("five", result)
    
    result = anglicize.anglicize1to19(6)
    introcs.assert_equals("six", result)
    
    result = anglicize.anglicize1to19(7)
    introcs.assert_equals("seven", result)
    
    result = anglicize.anglicize1to19(8)
    introcs.assert_equals("eight", result)
    
    result = anglicize.anglicize1to19(9)
    introcs.assert_equals("nine", result)
    
    result = anglicize.anglicize1to19(10)
    introcs.assert_equals("ten", result)
    
    result = anglicize.anglicize1to19(11)
    introcs.assert_equals("eleven", result)
    
    result = anglicize.anglicize1to19(12)
    introcs.assert_equals("twelve", result)
    
    result = anglicize.anglicize1to19(13)
    introcs.assert_equals("thirteen", result)
    
    result = anglicize.anglicize1to19(14)
    introcs.assert_equals("fourteen", result)
    
    result = anglicize.anglicize1to19(15)
    introcs.assert_equals("fifteen", result)
    
    result = anglicize.anglicize1to19(16)
    introcs.assert_equals("sixteen", result)
    
    result = anglicize.anglicize1to19(17)
    introcs.assert_equals("seventeen", result)
    
    result = anglicize.anglicize1to19(18)
    introcs.assert_equals("eighteen", result)
    
    result = anglicize.anglicize1to19(19)
    introcs.assert_equals("nineteen", result)


def test_tens():
    """
    Test procedure for the helper function tens
    """
    print('Testing tens')
    result = anglicize.tens(2)
    introcs.assert_equals("twenty", result)
    
    result = anglicize.tens(3)
    introcs.assert_equals("thirty", result)
    
    result = anglicize.tens(4)
    introcs.assert_equals("forty", result)
    
    result = anglicize.tens(5)
    introcs.assert_equals("fifty", result)
    
    result = anglicize.tens(6)
    introcs.assert_equals("sixty", result)
    
    result = anglicize.tens(7)
    introcs.assert_equals("seventy", result)
    
    result = anglicize.tens(8)
    introcs.assert_equals("eighty", result)
    
    result = anglicize.tens(9)
    introcs.assert_equals("ninety", result)


# Script code
if __name__ == '__main__':      # Execute code below only if run as a script
    test_tens()
    test_anglicize1to19()
    test_anglicize20to99()
    test_anglicize100to999()
    test_anglicize1000()
    test_anglicize()
    print('Module anglicize passed all tests.')
