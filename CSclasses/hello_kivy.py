# -*- coding: utf-8 -*-
"""
@Time: 2021/1/21 15:02
@Author: LizzieDeng
@File: hello_kivy.py
@Description:
"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import kivy.graphics
from kivy.config import Config
from kivy.metrics import dp


class TutorialApp(App):
    def build(self):
        # mylayout = BoxLayout(orientation='vertical')
        # mylabel = Label(text='My App')
        # mybutton = Button(text="Click me!")
        # mylayout.add_widget(mylabel)
        # mybutton.bind(on_press=lambda a: print(mylabel.text))
        # mylayout.add_widget(mybutton)
        # return mylayout
        return Mybutton()


class Mybutton(Button):
    text = 'Click me again '
    on_press = lambda a: print('My button')


class Panel(FloatLayout):
    """

    """
    def __init__(self, **kw):
        """

        :param kw:
        """
        super(Panel, self).__init__(**kw)

        rsize = [0, 0]
        rsize[0] = self.size[0] * dp(1)
        rsize[1] = self.size[0] * dp(1)

        color = Color(1.0, 1.0, 1.0, 1.0)

TutorialApp().run()
