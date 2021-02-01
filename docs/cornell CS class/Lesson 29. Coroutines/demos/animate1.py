"""
A module to show off how simple, input driven animation.

This is a simple animation where we move an image every frame
according to the presed keys.

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

# AMOUNT TO CHANGE THE POSITION PER FRAME
ANIMATION_STEP   = 2

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

    # THE THREE MAIN METHODS
    def start(self):
        """
        Initializes the application, creating new attributes.
        """
        # Image files must be stored in a folder called Images
        self.image = GImage(x=WINDOW_WIDTH/2,y=WINDOW_HEIGHT/2,source='Walker.png')

    def update(self,dt):
        """
        Animates the image.

        Parameter dt: The time since the last animation frame.
        Precondition: dt is a float.
        """
        # Use if instead of elif to allow multiple keys at once
        if self.input.is_key_down('up'):
            self.image.y += ANIMATION_STEP
        if self.input.is_key_down('down'):
            self.image.y -= ANIMATION_STEP
        if self.input.is_key_down('right'):
            self.image.x += ANIMATION_STEP
        if self.input.is_key_down('left'):
            self.image.x -= ANIMATION_STEP


    def draw(self):
        """
        Draws the image
        """
        self.image.draw(self.view)


# Application Code
if __name__ == '__main__':
    Animation(left=150,width=WINDOW_WIDTH,height=WINDOW_HEIGHT,fps=60.0).run()
