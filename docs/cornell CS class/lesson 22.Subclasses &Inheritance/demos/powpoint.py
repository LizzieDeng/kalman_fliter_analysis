"""
A module of class stubs to show off subclasses

This module does not do anything. It is simply mean to
accompany the lesson video introducing subclassing.

Author: Walker M. White
Date:   October 6, 2020
"""


class SlideContent(object):
    """Class representing content on a slide"""

    def __init__(self,x,y,w,h):
        """Initialize the slide content"""
        pass

    def draw_frame(self):
        """Draw the frame (handles use to resize)"""
        pass

    def select(self):
        """Show the frame when object clicked"""
        pass

class TextBox(SlideContent):
    """Class representing text on a slide"""

    def __init__(self,x,y,text):
        """Initialize the text box"""
        pass

    def draw(self):
        """Draw the text contents (not the frame)"""
        pass

class Image(SlideContent):
    """Class representing an image on a slide"""

    def __init__(self,x,y,image_file):
        """Initialize the image"""
        pass

    def draw(self):
        """Draw the image (not the frame)"""
        pass
