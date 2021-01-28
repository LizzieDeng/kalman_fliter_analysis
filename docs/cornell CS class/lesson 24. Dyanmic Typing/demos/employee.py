"""
A module with two classes to show off inheritance

Note the use of super() to handle inheritance.

Author: Walker M. White (wmw2)
Date:   October 31, 2019
"""


class Employee(object):
    """
    A class representing an employee with a salary.

    This class has attributes for name, start date, and
    salary. However, they are only accessible via the
    getters and setters of the same name.
    """
    # HIDDEN INSTANCE ATTRIBUTES:
    # Attribute _name: The employee's name
    # Invariant: _name is a non-empty string
    #
    # Attribute _start: The year hired
    # Invariant: _start is an int > 1970; -1 if undefined
    #
    # Attribute _salary: The employee salary
    # Invariant: _salary is an int or float >= 0

    # GETTERS/SETTERS
    def getName(self):
        """
        Returns the employee's name.

        The name is a non-empty string.
        """
        return self._name

    def setName(self,value):
        """
        Sets the employee's name to to the given value

        Parameter value: the new name
        Precondition: value is a nonempty string
        """
        assert type(value) == str and value != '', repr(value)+' is an invalid name'
        self._name = value

    def getStart(self):
        """
        Returns the year hired.

        The year is an int > 1970 or -1.  If it is -1 that
        means the year is undefined
        """
        return self._start

    def setStart(self,value):
        """
        Sets the year hired to the given value.

        Parameter value: the new year
        Precondition: valus is an int > 1970, or -1 if
        undefined.
        """
        assert type(value) == int, repr(value)+' is not an int'
        assert value > 1970 or value == -1, repr(value)+' is an invalid start date'
        self._start = value

    def getSalary(self):
        """
        Returns the annual salary

        The salary is a number >= 0.
        """
        return self._salary

    def setSalary(self,value):
        """
        Sets the annual salary to the given value.

        Parameter value: the new salary
        Precondition: value is a number (int or float) >= 0.
        """
        assert type(value) == int or type(value) == float, repr(value)+' is not a number'
        assert value >= 0, repr(value)+' is negative'
        self._salary = value

    def getCompensation(self):
        """
        Returns the annual compensation (will be overridden).

        For base employees, this is the same as the salary.
        """
        return self._salary

    # INITIALIZER
    def __init__(self, n, d=-1, s=50000.0):
        """
        Initializes an Employee with name n, year hired d, salary s

        Parameter n: the employee name
        Precondition: n is a nonempty string

        Parameter d: the employee start date (optional)
        Precondition: d is an int > 1970 or -1 if undefined
        (default)

        Parameter s: the employee salary (optional)
        Precondition: s is an int or float >= 0
        (50000.0 default)
        """
        # LET THE SETTERS ENFORCE THE PRECONDITIONS
        self.setName(n)
        self.setStart(d)
        self.setSalary(s)

    # OPERATIONS
    def __str__(self):
        """
        Returns the string representation of this Employee
        """
        return self._name + ', year ' + str(self._start) + ', salary ' + str(self._salary)


# SUBCLASS
class Executive(Employee):
    """
    A class representing an Employee with a bonus.

    This class has an additional attribute for an annual
    bonus. This attribute is only accessible via setters
    and getters.
    """
    # HIDDEN INSTANCE ATTRIBUTES:
    # Attribute _bonus: The annual bonus
    # Invariant: _bonus is an int or float >= 0

    # GETTERS/SETTERS
    def getBonus(self):
        """
        Returns the annual bonus.

        The bonus is a number >= 0.
        """
        return self._bonus

    def setBonus(self,value):
        """
        Sets the annual bonus salary to the give value

        Parameter value: the new bonus
        Precondition: value is a number (int or float) >= 0.
        """
        assert type(value) == int or type(value) == float, repr(value)+' is not a number'
        assert value >= 0, repr(value)+' is negative'
        self._bonus = value

    def getCompensation(self):
        """
        Returns the annual compensation (will be overridden).

        For executives, this is the salary plus the annual
        bonus.
        """
        return self._salary+self._bonus

    # INITIALIZER
    def __init__(self, n, d, b=0.0):
        """
        Initializes an Executive w/ name n, year hired d,
        and bonus b

        The default salary of an executive is 50k

        Parameter n: the executive name
        Precondition: n is a nonempty string

        Parameter d: the executive start date (optional)
        Precondition: d is an int > 1970 or -1 if undefined (default)

        Parameter b: the executive bonus (optional)
        Precondition: b is an int or float >= 0
        (0.0 default)
        """
        # Asserts precondition for n and d
        super().__init__(n,d,50000)
        self.setBonus(b)

    # OPERATIONS
    def __str__(self):
        """
        Returns a string representation of this Executive
        """
        # Add on to the string representation of the base class.
        return super().__str__() + ', bonus ' + str(self._bonus)
