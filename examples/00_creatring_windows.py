import easykinter as ek
import tkinter as tk

# create the main tk.Tk window, but hide it
# as we will not be working with it
root = ek.CreateRoot(HideWindow=True)

# creating the tk.Toplevel window
toplevel = ek.CreateToplevel("New toplevel!", root, None, 500, 500)

#centering the toplevel window
ek.CenterWindow(toplevel)

# the window can be also interactible with tkinter
toplevel.title("I changed the toplevel's title!")