import easykinter as ek
import tkinter as tk

# settings up the windows we will work with
root = ek.CreateRoot(HideWindow=True)
toplevel = ek.CreateToplevel("Cool widgets!", root, None, 500, 500)

# creating a button
# the button dimension is now measured in pixels! No more annoying MATH.
button = ek.CreateButton(toplevel, "New\nButton", ButtonWidth=50, ButtonHeight=50)

# you can do this to pack your widgets:
button.place(relx=0.5, rely=0.55)

# creating a label
# you can ALSO use the new implemented PackType to automatically pack the widgets!
label = ek.CreateLabel(toplevel, "The widget below me is\na super cool Button!", PackType="Place", RelX=0.5, RelY=0.3)
