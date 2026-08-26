import easykinter as ek
import tkinter as tk

# Previously in tkinter, customizing was pretty boring...
# ... you needed to write a whole new line... for most things.
root = ek.CreateRoot("Boring way...")

# Here, if we want to make out windows pretty-
# We gotta write one line to change the colors...
root.configure(bg="white")

# ...one line to change their state...
root.focus_force()

# SO-
root.wm_attributes("-alpha", 0.5)
# MANY-
root.wm_attributes("-topmost", True)
# LINES OF CODE!
root.resizable(False, False)

# YOU KNOW WHAT, FORGET THIS!
root.withdraw()

# Here, we have a simple tool to keep it easy.
toplevel = ek.CreateToplevel("The EASY way!", root)
ek.BetterConfigure(toplevel, background="white", WindowTrasparency=0.5, Topmost=True, ResizableHeight=False, ResizableWidth=False)
# Whoo wee! Pretty nice! It's looking pretty crisp now, ain't it?
