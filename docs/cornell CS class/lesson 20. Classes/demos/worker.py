"""
A module with a simple Worker class.

Class demonstrates attributes and an initializer.

Author: Walker M. White (wmw2), Steve Marschner (srm2)
Date:   October 12, 2019
"""


class Worker(object):
    """
    Class to represent a worker at a company

    Not all workers have an immediate boss.

    Attribute lname: The worker's last name
    Invariant: lname is a string

    Attribute ssn: The worker's social security no.
    Invariant: ssn is an int in 0..999999999

    Attribute boss: The worker's boss.
    Invariant: boss is a Worker object, or None if no boss
    """

    def __init__(self, lname, ssn, boss):
        """
        Initialize a new Worker with last name n, soc sec
        number s, and boss b.

        Parameter lname: The worker's last name
        Precondition: lname is a string

        Parameter ssn: The worker's social security number
        Precondition: ssn is an int in 0..999999999

        Parameter boss: The worker's boss
        Precondition: boss is another Worker object or None
        """
        self.lname = lname
        self.ssn   = ssn
        self.boss  = boss

    def __str__(self):
        """
        Returns a text representation of this Worker
        """
        return ('Worker ' + self.lname +
                '. Soc sec XXX-XX-' + str(self.ssn % 10000) +
                ('.' if self.boss is None else '. boss: ' + self.boss.lname))
