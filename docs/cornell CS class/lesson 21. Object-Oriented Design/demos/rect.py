"""
A module providing a class to represent 2D rectangles.

Authors: Walker White (wmw2), Steve Marschner (srm2), and Lillian Lee (ljl2)
Date:    October 20, 2019
"""


class Rectangle(object):
    """
    A class to represent rectangular regions of the plane.

    Attribute l: The x-coordinate of the left edge
    Invariant: l is a float, l <= r

    Attribute r: The x-coordinate of the right edge
    Invariant: r is a float, l <= r

    Attribute b: The y-coordinate of the bottom edge
    Invariant: b is a float, b <= t

    Attribute t: The y-coordinate of the top edge
    Invariant: t is a float, b <= t
    """

    def __init__(self, l, r, b, t):
        """
        Initializes the rectangle [l, r] x [b, t]

        Parameter l: left edge
        Precondition: l is a float

        Parameter r: right edge
        Precondition: r is a float, l <= r

        Parameter b: bottom edge
        Precondition: b is a float

        Parameter t: top edge
        Precondition: t is a float, b <= t
        """
        self.l = l
        self.r = r
        self.b = b
        self.t = t

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return (self.r - self.l) * (self.t - self.b)

    def intersection(self, other):
        """
        Returns a new Rectangle which is intersection of self with other.

        The result may be an "empty" rectangle

        Parameter other: the rectangle to intersect
        Precondition: other is a rectangle
        """
        l = max(self.l, other.l)
        r = min(self.r, other.r)
        b = max(self.b, other.b)
        t = min(self.t, other.t)
        if (r < l):
            r = l
        if (t < b):
            t = b
        return Rectangle(l, r, b, t)

    def __str__(self):
        """
        Returns: String representation of this rectangle.
        """
        return "(%g, %g) x (%g, %g)" % (self.l, self.r, self.b, self.t)


def demo_rect():
    """
    Shows off rectangle in action
    """
    r1 = Rectangle(0., 1., 2., 3.)
    print(r1.area())
    r2 = Rectangle(.5, 2., 2.5, 9.)
    print(r2.area())
    r3 = r1.intersection(r2)
    r4 = r2.intersection(r1)
    print(r3)
    print(r4)


if __name__ == '__main__':
    demo_rect()
