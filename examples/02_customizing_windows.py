import easykinter as ek
import tkinter as tk

# previously in tkinter, customizing was pretty boring...
# ... you needed to do a whole new line... for most things.
root = ek.CreateRoot("Boring way...")

# one line to change the colors...
root.configure(bg="white")

# ...one line to change their state...
root.focus_force()

# SO! MANY! LINES!
root.wm_attributes("-alpha", 0.5)
root.wm_attributes("-topmost", True)
root.resizable(False, False)

# FORGET THIS!
root.withdraw()

# Here, we have a simple tool to keep it easy.
toplevel = ek.CreateToplevel("The EASY way!", root)
ek.BetterConfigure(toplevel, background="white", WindowTrasparency=0.5, Topmost=True, ResizableHeight=False, ResizableWidth=False)
# Whoo wee! Pretty nice!