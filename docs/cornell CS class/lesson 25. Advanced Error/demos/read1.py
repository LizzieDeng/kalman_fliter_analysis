"""
A simple application to show off try-except

This time we recover on value, but not out of range

Author: Walker M. White (wmw2)
Date:   October 28, 2017 (Python 3 Version)
"""


def main():
    """
    Get some input from the user
    """
    try:
        value = input('Number: ')   # get number from user
        x = float(value)            # convert string to float
        print('The next number is '+repr(x+1))
        if x > 10:
            assert 1 == 2, 'Out of range'
    except ValueError:
        print('Hey! That is not a number!')

    print('Program is done')


# Script Code
if __name__ == '__main__':
    main()
