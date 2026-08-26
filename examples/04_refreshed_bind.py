import easykinter as ek
import tkinter as tk

# As i'm sure we've all seen in tkinter, to bind things, it's so... boring...
root = ek.CreateRoot(PosX=600, PosY=400)

# You need to put event here, and it's so grueling! It's also really weird.
def BindingFunction(event):
    root.destroy()

# On top of that? It's so oddly specific and nitpicked on how you need to name thhe keybind!
# Having to use "<>" is honestly a pretty bad design flaw in my opinion...
root.bind("<Return>", BindingFunction)

# Just forget it all.

# Have you ever wished it was like THIS?
toplevel = ek.CreateToplevel()

# Look at it: no need to place and rely on events anymore!
def AnotherBindingFunction():
    toplevel.destroy()

# And also something that exsists in tkinter, but was brought back:
# You can name any keybind you want! Literally to your heart's content!

# Here, we have individual keys:
ek.BetterBind(toplevel, KeyToBind="a", FunctionToBind=AnotherBindingFunction)

# You can also do specific commands:
ek.BetterBind(toplevel, KeyToBind="return", FunctionToBind=AnotherBindingFunction)

# Best of all? No need to use <> anymore.
# (But you also have freedom of choice, i'm not a monster.)
ek.BetterBind(toplevel, KeyToBind="<Return>", FunctionToBind=AnotherBindingFunction)

# Test it out yourself! click on a window and press ENTER. (or A if you're focused in the toplevel window.)
