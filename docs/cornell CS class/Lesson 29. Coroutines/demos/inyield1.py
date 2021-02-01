"""
A module to show off a yield expression (not a statement)

A yield expression receives data instead of sending it as output. 
You write the word yield in parentheses and assign it to a variable.

Author: Walker M. White
Date:   November 2, 2020
"""


def receive(n):
    """
    Receives n values as input and prints them each out.
    
    This function is a coroutine and the data is sent via a
    send method on the generator object.
    
    Parameter n: The number of messages to receive
    Precondition: n is an int >= 0
    """
    for x in range(n):
        # receive the value sent
        value = (yield)
        print('Coroutine received value '+repr(value))


# Add this if using the Python Tutor
#a = receive(3)
#next(a)
#for x in 'abcde':
#    a.send(x)
