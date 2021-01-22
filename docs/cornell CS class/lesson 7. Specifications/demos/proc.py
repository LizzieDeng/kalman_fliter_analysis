"""
A module with a single greeting procedure

This module shows off a user-defined procedure, without using a function
with a return value

Author: Walker M. White
Date:   February 14, 2019
"""


def greet(n):
    """
    Prints a greeting to the name n

    The greeting has format 'Hello <n>!' followed by a conversation starter.

    Parameter n: The name to use in the greeting
    Precondition: n is a nonempty string
    """
    print('Hello '+n+'!')
    print('How are you?')


def greet2(g,n):
    """
    Prints out greeting g to the name n

    The greeting has format '<g> <n>!' followed by a conversation starter.
    For example, greet2('Hola','Walker') prints 'Hola Walker!'

    Parameter g: The greeting to use
    Precondition: g is a nonempty string

    Parameter n: The name to use in the greeting
    Precondition: n is a nonempty string
    """
    phrase = g+','+n+'!'
    print(phrase)
    print('How are you?')
