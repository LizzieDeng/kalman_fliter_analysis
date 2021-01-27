"""
A class to rerpresent a genealogical tree

Author: Walker M. White (wmw2)
Date:   October 10, 2018
"""
import sys

# Allow us to go really deep
sys.setrecursionlimit(999999999)


# We will cover this NEXT lecture
class Person(object):
    """
    A class to represent a person in a genealogical tree.
    
    Attribute fname: The first name
    Invariant: fname is a string
    
    Attribute lname: The last name
    Invariant: lname is a string
    
    Attribute mom: The person's mother
    Invariant: mom is a Person object, or None if not known
    
    Attribute dad: The person's father
    Invariant: dad is a Person object, or None if not known
    """
    
    def __init__(self,fname,lname,mom=None,dad=None):
        """
        Initializes a new instance of person
        
        Parameter fname: The first name
        Precondition: fname is a string
        
        Parameter lname: The last name
        Precondition: lname is a string
        
        Parameter mom: The mother of this person (optional)
        Precondition: mom is a Person or None
        
        Parameter dad: The father of this person (optional)
        Precondition: dad is a Person or None
        """
        self.fname = fname
        self.lname = lname
        self.mom = mom
        self.dad = dad
    
    def __str__(self):
        """
        Returns a string representation of this person
        """
        result = '(Person: '+self.name()
        
        if not self.mom is None:
            result += '; mom: '+self.mom.name()
            
        if not self.dad is None:
            result += '; dad: '+self.dad.name()
        
        return result+')'
    
    def __repr__(self):
        """
        Returns an unambigious string representation of this person
        """
        return str(self)
    
    def name(self):
        """
        Returns the full name of this person
        """
        return self.fname+' '+self.lname


# Recursive functions
def num_ancestors(p):
    """
    Returns the number of known ancestors of p
    
    Does not include p, so the answer might be 0.
    
    Parameter p: The initial family member
    Precondition: p is a Person (and not None)
    """
    # Work on small data    (BASE CASE)
    if p.mom == None and p.dad == None:
        return 0
    
    # Break up into halves  (RECURSIVE CASE)
    moms = 0
    if not p.mom == None:
        # Do not forget to include mom as well.
        moms = 1+num_ancestors(p.mom)

    dads = 0
    if not p.dad == None:
        # Do not forget to include dad as well.
        dads = 1+num_ancestors(p.dad)
    
    # Combine the answer
    return moms+dads


def num_with_name(p,name):
    """
    Returns the number of people with name as a first name.
    
    This function does not just check ancestors; it checks
    p as well.
    
    Parameter p: The initial family member
    Precondition: p is a Person (and not None).
    
    Parameter name: The name to match
    Precondition: name is a string
    """
    # Check we match
    match = 1 if p.fname == name else 0
    
    # Work on small data    (BASE CASE)
    if p.mom == None and p.dad == None:
        # Conditional expression
        return match
        
    # Break up into halves  (RECURSIVE CASE)
    moms = 0
    if not p.mom == None:
        # No need to check mom; handled in recursive call.
        moms = num_with_name(p.mom,name)

    dads = 0
    if not p.dad == None:
        # No need to check dad; handled in recursive call.
        dads = num_with_name(p.dad,name)
    
    # Combine the answer
    return moms+dads+match
