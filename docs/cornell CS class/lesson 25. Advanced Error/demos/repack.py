"""
Module showing how to repackage an error type

This looks best in the Python Tutor

Author: Walker M. White (wmw2)
Date:   October 28, 2017 (Python 3 Version)
"""
from custom import ComplexError

def extract_value(error):
    """
    Returns the value in the error message (as a string)

    If error is a ValueError, then the error is guaranteed
    to be after the final colon.

    Parameter error: The error object
    Precondition: error is a ValueError
    """
    assert isinstance(error,ValueError), repr(error)+' is not a ValueError'
    msg = error.args[0]
    pos = msg.rfind(':')
    result = msg[pos+1:]
    return result.strip()


def get_value(message):
    """
    Returns the number that the user typed after message

    Parameter message: The message to display
    Precondition: message is a non-empty string
    """
    try:
        value = input(message)
        result = float(value)
        return result
    except ValueError as e:
        value = extract_value(e)
        raise ComplexError('Bad Value',value)


def main():
    """
    Prompt the user for a number
    """
    try:
        answer = get_value('Enter a number: ')
        print(answer)
    except ComplexError as e:
        print(e.getValue()+' is not a number')


if __name__ == '__main__':
    main()
