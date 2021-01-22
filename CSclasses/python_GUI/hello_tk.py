# -*- coding: utf-8 -*-
"""
@Time: 2021/1/22 10:20
@Author: LizzieDeng
@File: hello_tk.py
@Description: A Hello World GUI.

The purpose of this App is to test that tkinter is working correctly.
"""

from tkinter import *


def create_app():
    """
    returns a Tkinter app not yet executing.
    call mainloop on the app to have it execute.
    :return:
    """
    root = Tk()
    root.title('Hello APP')
    root.protocol("WM_DELETE_WINDOW", root.quit)

    mssg = Label(root, text="hello World!", font=('Times', 14))
    mssg.pack()
    return root


if __name__ == "__main__":
    create_app().mainloop()




