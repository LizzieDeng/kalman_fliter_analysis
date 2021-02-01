"""
A module to show off a timed animation

A timed animation starts when we press a key, and continues for
a given length of time (ANIMATION_SPEED). It will ignore any
input until the animation is complete. This is actually how most
professional animation works in games.

Author: Walker M. White (wmw2)
Date:   November 20, 2019
"""
import introcs
import random
import math
from game2d import *
import time
import random


############# CONSTANTS #############
# Window Size
WINDOW_WIDTH  = 512
WINDOW_HEIGHT = 512

# THE ANIMATION SPEED IN SECONDS
ANIMATION_SPEED = 1

############# CONTROLLER CLASS #############
class Animation(GameApp):
    """
    This class is an application to animate an image with the arrow keys

    At each step, the update() method checks for key input
    and moves the image accordingly.

    Attribute view : the view (inherited from GameApp)
    Invariant: view is an instance of GView

    Attribute image: the image to animate
    Invariant: image is a GImage made from a PNG file
    """
    # Attribute _animating: Whether we are in the process of animating
    # Invariant: _animating is a boolean
    #
    # Attribute _rotation: Whether the animation is rotation or vertical
    # Invariant: _rotation is a boolean
    #
    # Attribute _sangle: The start angle for animaton (in degrees)
    # Invariant: _sangle is a float
    #
    # Attribute _fangle: The final angle for animaton (in degrees)
    # Invariant: _fangle is a float
    #
    # Attribute _svert: The start y-coordinate position for animaton
    # Invariant: _svert is a float
    #
    # Attribute _fvert: The final y-coordinate position for animaton
    # Invariant: _fvert is a float


    # THE THREE MAIN METHODS
    def start(self):
        """
        Initializes the application, creating new attributes.
        """
        self.image = GImage(x=WINDOW_WIDTH/2,y=WINDOW_HEIGHT/2,source='Walker.png')
        self.image.angle = 0    # This force loads the image, preventing a later delay
        self._animating = False
        self._rotation = False
        self._sangle = 0
        self._fangle = 0
        self._svert = 0
        self._fvert = 0

    def update(self,dt):
        """
        Animates the image.

        Parameter dt: The time since the last animation frame.
        Precondition: dt is a float.
        """
        if self._animating:
            if self._rotation:
                self._animate_turn(dt)
            else:
                self._animate_slide(dt)
        elif self.input.is_key_down('left'):
            self._animating = True
            self._rotation = True
            self._sangle = self.image.angle
            self._fangle = self._sangle+90
        elif self.input.is_key_down('right'):
            self._animating = True
            self._rotation = True
            self._sangle = self.image.angle
            self._fangle = self._sangle-90
        elif self.input.is_key_down('up'):
            self._animating = True
            self._rotation = False
            self._svert = self.image.y
            self._fvert = self._svert+self.image.height
        elif self.input.is_key_down('down'):
            self._animating = True
            self._rotation = False
            self._svert = self.image.y
            self._fvert = self._svert-self.image.height

    def draw(self):
        """
        Draws the image
        """
        self.image.draw(self.view)

    def _animate_turn(self,dt):
        """
        Animates a rotation of the image over ANIMATION_SPEED seconds

        This method rotates the image from self._sangle to self._fangle.
        It uses dt to do a little bit of work at a time until it gets
        the correct answer.

        Parameter dt: The time since the last animation frame.
        Precondition: dt is a float.
        """
        # Degrees per second
        steps = (self._fangle-self._sangle)/ANIMATION_SPEED
        amount = steps*dt

        # Update the angle
        self.image.angle = self.image.angle+amount

        # If we go to far, clamp and stop animating
        if abs(self.image.angle-self._sangle) >= 90:
            self.image.angle = self._fangle
            self._animating = False

    def _animate_slide(self,dt):
        """
        Animates a vertical up or down of the image over ANIMATION_SPEED seconds

        This method moves the image form self._svert to self._fvert.
        It uses dt to do a little bit of work at a time until it gets
        the correct answer.

        Parameter dt: The time since the last animation frame.
        Precondition: dt is a float.
        """
        # Degrees per second
        steps = (self._fvert-self._svert)/ANIMATION_SPEED
        amount = steps*dt

        # Update the position
        self.image.y = self.image.y+amount

        # If we go to far, clamp and stop animating
        if abs(self.image.y-self._svert) >= self.image.height:
            self.image.y = self._fvert
            self._animating = False


# Application Code
if __name__ == '__main__':
    Animation(left=150,width=WINDOW_WIDTH,height=WINDOW_HEIGHT,fps=60.0).run()
