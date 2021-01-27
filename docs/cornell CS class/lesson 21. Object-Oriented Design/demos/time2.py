"""
A module providing a class the time of day

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

    # GETTERS AND SETTERS
    def getHour(self):
        """
        Returns the hour of the day.

        Hour is an int in 0..23
        """
        return self.hour

    def setHour(self,value):
        """
        Sets the hour of the day to be the given value.

        Parameter value: hour of day
        Precondition: value is an int in 0..23
        """
        assert type(value) == int, repr(value)+' is not an int'
        assert 0 <= value and value < 24, repr(value)+' is out of range 0..23'
        self.hour = value

    def getMinute(self):
        """
        Returns the minute of hour.

        Minute is an int in 0..59
        """
        return self.min

    def setMinute(self,value):
        """
        Sets the minute of hour to be the given value.

        Parameter value: minute of hour
        Precondition: value is an int in 0..59
        """
        assert type(value) == int, repr(value)+' is not an int'
        assert 0 <= value and value < 60, repr(value)+' is out of range 0..59'
        self.min = value


    def __init__(self, hour, min):
        """
        Initializes the time hour:min.

        Parameter hour: hour of day
        Precondition: hour is an int in 0.23

        Parameter min: minute of hour
        Precondition: min is an int in 0..59
        """
        assert type(hour) == int, repr(hour)+' is not an int'
        assert 0 <= hour and hour < 24, repr(hour)+' is out of range 0..23'
        assert type(min) == int, repr(min)+' is not an int'
        assert 0 <= min and min < 60, repr(hour)+' is out of range 0..59'

        self.hour = hour
        self.min = min

    def increment(self, hours, mins):
        """
        Moves this object <hours> hours and <mins> minutes
        into the future.

        Parameter hours: number of hours to move
        Precondition: hours is an int >= 0

        Parameter mins: number of minutes to move
        Precondition: mins an int in 0..59
        """
        assert type(hours) == int, repr(hours)+' is not an int'
        assert 0 <= hours, repr(hours)+' is not >= 0'
        assert type(mins) == int, repr(mins)+' is not an int'
        assert 0 <= mins and mins < 60, repr(mins)+' is out of range 0..59'

        self.hour = self.hour + hours
        self.min = self.min + mins
        self.hour = self.hour + self.min // 60
        self.min = self.min % 60
        self.hour = self.hour % 24

    def isPM(self):
        """
        Returns True if this time is noon or later;
        False otherwise.
        """
        return self.hour >= 12

    def __str__(self):
        """
        Returns the time as a string in [H]H:MM 24-hour format.
        """
        return str(self.hour) + (':0' if self.min < 10 else ':') + str(self.min)

    def _iamhidden(self):
        """
        This method does nothing
        """
        return 42



def demo_time():
    """
    Shows off time in action
    """
    t = Time(23,58)
    print(t)
    t.increment(0,3)
    print(t)
    t.increment(11,0)
    print(t, t.isPM())
    t.increment(1, 59)
    print(t, t.isPM())


if __name__ == '__main__':
    demo_time()
