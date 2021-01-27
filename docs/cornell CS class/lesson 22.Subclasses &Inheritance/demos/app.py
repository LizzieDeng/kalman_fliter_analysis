"""
A module to show off inheritance in Kivy

Author: Walker M. White (wmw2)
Date:   October 31, 2019
"""

import kivy
import kivy.app
import kivy.uix.label
import kivy.uix.button
from kivy.config import *
from kivy.metrics import dp

# ALL applications inherit from kivy.app.App
class MyApp(kivy.app.App):
    """
    A class is a window with 'Hello World!' inside
    """
    # HIDDEN INSTANCE ATTRIBUTES
    # Attribute _button: text display in window
    # Invariant: _button is a kivy.uix.button.Button object

    # Override the build method (not __init__) to add buttons, etc.
    def build(self):
        """
        Builds the application with a single internal panel
        """
        Config.set('graphics', 'position', 'custom')
        Config.set('graphics', 'left', 100)
        Config.set('graphics', 'top',  100)
        Config.set('graphics', 'width', '400')
        Config.set('graphics', 'height', '400')
        self._button = kivy.uix.button.Button(size=(400,400),
                                            text='Hello World!',
                                            font_size=dp(36),
                                            bold=True)
        return self._button


# Script Code.
if __name__ == '__main__':
    MyApp().run()
