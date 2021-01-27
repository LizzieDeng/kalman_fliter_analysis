"""
A module providing a class the time of day

This version is a stub that allows us to talk about
implementing a class.

Authors: Walker White (wmw2), Steve Marschner (srm2),
         and Lillian Lee (ljl2)
Date:    October 20, 2019
"""


class Time(object):
    """
    A class to represent the times of day.

    Attribute hour: the hour of the day
    Invariant: hour is an int in 0..23

    Attribute min: the minute of the hour
    Invariant: min is an int in 0..59
    """

    def __init__(self, hour, min):
        """
        Initializes the time hour:min.

        Parameter hour: hour of day
        Precondition: hour is an int in 0.23

        Parameter min: minute of hour
        Precondition: min is an int in 0..59
        """
        pass


    def increment(self, hours, mins):
        """
        Moves this object <hours> hours and <mins> minutes
        into the future.

        Parameter hours: number of hours to move
        Precondition: hours is an int >= 0

        Parameter mins: number of minutes to move
        Precondition: mins an int in 0..59
        """
        pass

    def __str__(self):
        """
        Returns the time as a string in [H]H:MM 24-hour format.
        """
        return str(self.hour) + (':0' if self.min < 10 else ':') + str(self.min)
