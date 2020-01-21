"""
bind tkinter
"""

import tkinter as tk

ROOT = tk.Tk()


def key(event):
    """
    key
    """
    print("pressed", repr(event.char))


def callback(event):
    """
    callback
    """
    FRAME.focus_set()
    print("clicked at", event.x, event.y)


FRAME = tk.Frame(ROOT, width=100, height=100)
FRAME.bind("<Key>", key)
FRAME.bind("<Button-1>", callback)
FRAME.pack()

ROOT.mainloop()
