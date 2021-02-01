"""
A module to show off a yield expression (not a statement)

A yield expression can output data, just like yield statement.  To
do that, put the output inside of the parentheses with the yield.
The coroutine will output that data, and then assign the new input
to the variable when it resumes.

Author: Walker M. White
Date:   November 2, 2020
"""


def give_receive(n):
    """
    Receives n values as input and prints them each out.

    This function is a coroutine and the data is sent via a
    send method on the generator object.

    Parameter n: The number of messages to receive
    Precondition: n is an int >= 0
    """
    for x in range(n):
        # Give x to the parent function, receive the value sent
        value = (yield x)
        print('Coroutine received value '+repr(value))


# Add this if using the Python Tutor
#a = give_receive(3)
#next(a)
#for x in 'abcde':
#    value a.send(x)
#    print('Current value is '+repr(value))
