# -*- coding: utf-8 -*-
"""
@Time: 2021/1/25 16:12
@Author: LizzieDeng
@File: hilbert.py
@Description:
"""
"""
A module to draw cool shapes with the TkTurtle.

Based on an module write by Dexter Kozen

Author: Walker M. White (wmw2)
Date:   October 10, 2018
"""
import introcs.turtle as turtle
import math


#################### Hilbert Curves ####################


def hilbert(w, side, d, sp=10):
    """
    Draws a Hilbert curve of side-length side and depth d
    on Window w

    This function clears the window and makes a new turtle
    t. This starts at the bottom left corner of the Hilbert
    curve, where the curve is centered at (0,0). It draws
    by calling the function hilbert_helper(t, side, d). The
    turtle is visible during drawing and is hidden at the
    end.

    Parameter w: The window to draw upon.
    Precondition: w is a turtle Window object.

    Parameter side: The width and height of the (square)
    Hilbert curve
    Precondition: side is a number > 0

    Parameter d: The recursive depth of the Hilbert curve
    Precondition: n is a valid depth (int >= 0)

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    assert type(w) == turtle.Window, str(w)+' is not a window object'
    assert type(side) in [int, float] and side > 0, str(side)+' is not a valid length'
    assert type(d) == int and d >= 0, str(d)+' is not a valid depth'
    assert type(sp) == int and 0 <= sp <= 10, str(sp)+' is not a valid Turtle speed'

    # Create the turtle
    w.clear()
    t = turtle.Turtle(w)

    # Set the color and speed of the turtle
    t.color = 'magenta'
    t.speed = sp

    # Get the turtle in position w/o drawing
    t.move(-side/2.0,-side/2.0)
    t.left(90)

    # Draw the Hilbert curve
    hilbert_helper(t, side, d)
    t.visible = False # Hide the turtle at the end
    t.flush()


def hilbert_helper(t, side, d, reverse=False):
    """
    Draws a Hilbert curve of side-length side and depth d
    with Turtle t

    The curve is draw right to left if reverse is True.
    Otherwise, it is drawn left to right.  This feature
    is necessary to smoothly draw the recursive Hilbert
    curves.  If drawing in reverse, the Turtle starts on
    the right side. Otherwise, it start on the left.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter side: The width and height of the (square)
    Hilbert curve
    Precondition: side is a number > 0

    Parameter d: The recursive depth of the Hilbert curve
    Precondition: n is a valid depth (int >= 0)

    Parameter reverse: Whether or not to draw in reverse
    Precondition: reverse is a bool
    """
    # WE WILL NOT WORRY ABOUT ENFORCING PRECONDITIONS IN THE HELPER

    # Turning directions depend on whether or not we are in reverse
    if reverse:
        angle = -90
    else:
        angle = 90

    # BASE CASE: d = 0
    if d == 0:
        t.forward(side)
        t.right(angle)
        t.forward(side)
        t.right(angle)
        t.forward(side)
        return

    # RECURSIVE CASE: d > 0
    # Compute what the grid looks like
    dotsize = (2**(d+1))-1  # Number of dots in grid
    subsize = (2**d)-1      # Number of dots for each sub-hilbert

    # Compute the new edge sizes.
    factor = (subsize)/float(dotsize)
    leng = side*factor
    edge = side-2*leng

    # Recursively draw the curve.
    t.right(angle)
    hilbert_helper(t,leng,d-1,not reverse)
    t.right(angle)
    t.forward(edge)
    hilbert_helper(t,leng,d-1,reverse)
    t.left(angle)
    t.forward(edge)
    t.left(angle)
    hilbert_helper(t,leng,d-1,reverse)
    t.forward(edge)
    t.right(angle)
    hilbert_helper(t,leng,d-1,not reverse)
    t.right(angle)


################ Test Function #################


def main():
    """
    Runs the turtle at multiple depths, pausing for a key
    press at each step
    """
    w = turtle.Window()
    input('Hit <return> ')

    # depth is one less than the power of n
    print('Calling Hilbert n=3')
    hilbert(w, 300, 2)
    input('Hit <return> ')

    print('Calling Hilbert n=4')
    hilbert(w, 300, 3)
    input('Hit <return> ')

    print('Calling Hilbert n=5')
    hilbert(w, 300, 4)
    input('Hit <return> ')

    # Clear the screen to demonstrate speed 0
    w.clear()
    input('Hit <return> ')

    print('Calling Hilbert n=5 (speed 0)')
    hilbert(w, 300, 4, 0)
    input('Hit <return> ')


# Application code
if __name__ == '__main__':
    main()
