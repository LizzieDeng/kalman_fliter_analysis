"""
A unit test for the Person class.

Author: Walker M. White (wmw2)
Date:   October 10, 2018
"""
import introcs
import person


def build_test_tree():
    """
    Returns the youngest generation Person in a complete family tree

    The purpose of this function is to create a genealogical tree for testing
    """
    # GREAT GRANDPARENTS (some unknown)
    # John Smith Sr.
    ggd1 = person.Person('John', 'Smith')
    ggm1 = person.Person('Pamela', 'Grey')

    ggm2 = person.Person('Eva', 'Brown')

    ggd4 = person.Person('Dan', 'O\'Reilly')
    ggm4 = person.Person('Heather', 'Chase')

    # GRANDPARENTS
    # John Smith Jr.
    gd1 = person.Person('John','Smith',ggm1,ggd1)
    gm1 = person.Person('Jane','Dare',ggm2,None)

    gd2 = person.Person('John','Evans')
    gm2 = person.Person('Ellen','O\'Reilly',ggm4,ggd4)

    # PARENTS
    # John Smith III
    d = person.Person('John','Smith',gm1,gd1)
    m = person.Person('Pamela','Evans',gm2,gd2)

    # FINAL GENERATION
    # John Smith IV
    p = person.Person('John','Smith',m,d)

    return p


def test_num_ancestors(p):
    """
    Tests num_ancestors on tree starting at p

    Parameter p: The input p for the test case
    Precondition: p is a Person
    """
    print('Testing num_ancestors')
    introcs.assert_equals(11, person.num_ancestors(p))
    introcs.assert_equals(4,  person.num_ancestors(p.mom))
    introcs.assert_equals(5,  person.num_ancestors(p.dad))
    introcs.assert_equals(0,  person.num_ancestors(p.mom.dad))


def test_num_with_name(p):
    """
    Tests num_with_name on tree starting at p

    Parameter p: The input p for the test case
    Precondition: p is a Person
    """
    print('Testing num_with_name')
    introcs.assert_equals(5, person.num_with_name(p,'John'))
    introcs.assert_equals(2, person.num_with_name(p,'Pamela'))
    introcs.assert_equals(0, person.num_with_name(p,'Ralph'))


# Script Code
if __name__ == '__main__':
    p = build_test_tree()
    test_num_ancestors(p)
    test_num_with_name(p)
    print('Module person is working properly')
