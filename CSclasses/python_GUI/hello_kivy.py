# -*- coding: utf-8 -*-
"""
@Time: 2021/1/21 15:02
@Author: LizzieDeng
@File: hello_kivy.py
@Description: A window displaying Hello World.
The purpose of this App is to test that Kivy is installed correctly.
"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle


class Panel(BoxLayout):
    """
       A drawing canvas to display the label.

    This is a simple Kivy panel that contains Hello World.

    """
    def __init__(self, **kw):
        """

        :param kw:
        """
        super(Panel, self).__init__(**kw)

        self.orientation = "vertical"
        # make the background solid white
        color = Color(1.0, 1.0, 1.0, 1.0)
        self.canvas.add(color)
        rect = Rectangle(pos=self.pos, )     # size=rsize
        self.canvas.add(rect)

        # add the label
        label = Label(text='Hello World!')
        label.bold = True
        self.add_widget(label)

        # add the button
        mybutton = Button(text="Click me!")
        mybutton.bind(on_press=lambda a: print(label.text))
        self.add_widget(mybutton)


class HelloApp(App):
    """
    the primary application object
    create and run this to get the panel.
    """
    def build(self):
        """
        Builds the application with a single internal panel
        :return:
        """
        return Panel()
        # Config.set('graphics', 'width', '450')
        # Config.set('graphics', 'height', '250')
        # Config.set('graphics', 'position', 'custom')
        # Config.set('graphics', 'left', 100)
        # Config.set('graphics', 'top', 100)
        # return Panel(size=(450, 250))


# Application Code
if __name__ == "__main__":
    HelloApp().run()

