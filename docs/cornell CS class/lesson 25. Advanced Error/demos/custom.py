"""
A module with two custom error types

Author: Walker M. White (wmw2)
Date:   October 28, 2017 (Python 3 Version)
"""


class CustomError(Exception):
    """
    A class for the simplest error possible
    """
    pass



















class ComplexError(ValueError):
    """
    An error class with extra attributes
    """
    # Mutable Attribute
    # Attribute value: The value that caused the error
    # Invariant: value is a string

    def getValue(self):
        """
        Returns the value causing this error
        """
        return self._value

    def setValue(self,value):
        """
        Sets the value for this error type

        Parameter value: An associated value
        Precondition: value is a string
        """
        assert isinstance(value,str), repr(value)+' is not a string'
        self._value = value

    def __init__(self,msg,value):
        """
        Initializes a new ComplexError

        Parameter msg: The error message
        Precondition: msg is a string

        Parameter value: An associated value
        Precondition: value is a string
        """
        super().__init__(msg)
        self.setValue(value)
