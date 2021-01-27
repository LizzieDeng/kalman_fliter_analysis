class Person(object):
    """
    A class representing a person with a birthday.
    """
    ### HIDDEN ATTRIBUTES
    # Attribute _name: the person's name
    # Invariant: string or None if unknown (MUTABLE)
    #
    # Attribute _born: the year the person is born
    # Invariant: int > 1900; -1 if unknown (IMMUTABLE)

    def getName(self):
        """
        Returns the name of this person.

        Name is either a string or None
        """
        return self._name

    def setName(self,value):
        """
        Sets the name of this person.

        Parameter value: The new name of the person
        Precondition: value is either a string or None
        """
        assert value == None or type(value) == str, repr(value)+' is not a valid name'
        self._name = value

    def getBorn(self):
        """
        Returns the year this person is born.

        Born is an int > 1900 or -1
        """
        return self._born

    def __init__(self,name,born):
        """
        Initializes a person with the given name/birth year

        Parameter name: The name of the person
        Precondition: name is either a string or None

        Parameter born: The year this person is born.
        Precondition: born is an int > 1900 or -1
        """
        assert born == None or type(born) == int, repr(born)+' has the wrong type'
        assert born > 1900 or born == -1, repr(born)+' is not a valid birth year'
        self.setName(name)
        self._born = born

    def __str__(self):
        name = 'UNKNOWN' if self._name == None else self._name
        return name+", born "+str(self._born)
