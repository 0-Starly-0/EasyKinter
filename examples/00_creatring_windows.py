import easykinter as ek
import tkinter as tk

# Firstly, all tkinter scripts need the main tk.Tk window,
# But who works with the root window anyways? Let's hide it.
root = ek.CreateRoot(HideWindow=True)

# Let's start by creating the tk.Toplevel window:
toplevel = ek.CreateToplevel("New toplevel!", root, None, 500, 500)
# Yeah, it's all come down to just ONE LINE of code... ain't that neat?

# The window can be also interacted with normally in tkinter!
toplevel.title("I changed the toplevel's title!")

# Almost as if... this was just tkinter all along, but better. Crazy concept, right?
# Wink wink, nudge nudge, EasyKinter.
