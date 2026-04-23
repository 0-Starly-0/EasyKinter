import easykinter as ek
import tkinter as tk

# in tkinter, to bind things, it's so... boring...
root = ek.CreateRoot(PosX=600, PosY=400)

# you need to put event here, and it's so grueling!
def BindingFunction(event):
    root.destroy()

# also, it's so oddly specific and nitpicked how you need to name thhe keybind!
# having to use "<>" is so weird...
root.bind("<Return>", BindingFunction)

# forget it.

# have you ever wished it was like THIS?
toplevel = ek.CreateToplevel()

# no need to place and rely on event anymore!
def AnotherBindingFunction():
    toplevel.destroy()

# you can name anything you want!

# individual keys:
ek.BetterBind(toplevel, KeyToBind="a", FunctionToBind=AnotherBindingFunction)

# specific commands:
ek.BetterBind(toplevel, KeyToBind="return", FunctionToBind=AnotherBindingFunction)

# and no need to use <> anymore. but you also have freedom of choice:
ek.BetterBind(toplevel, KeyToBind="<Return>", FunctionToBind=AnotherBindingFunction)

# test it out! click on a window and press ENTER. (or A if you're in the toplevel.)