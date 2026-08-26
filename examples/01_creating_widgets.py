import easykinter as ek
import tkinter as tk

# Let's start this example by doing what we did beforehand:
root = ek.CreateRoot(HideWindow=True)
toplevel = ek.CreateToplevel("Cool widgets!", root, None, 500, 500)

# Remember how creating windows was as easy as a single line? You guessed it.
button = ek.CreateButton(toplevel, "New\nButton", ButtonWidth=50, ButtonHeight=50)
# The button dimension is now measured in pixels! No more annoying MATH.

# In normal (and unneficient) Tkinter, you usually wasted a line of code doing this:
button.place(relx=0.5, rely=0.65)

# Let me create a label to demonstrate the NEW WAY of doing it.
# Because now- you can ALSO use the new implemented PackType to automatically pack the widgets!
label = ek.CreateLabel(toplevel, "The widget below me is\na super cool Button!", PackType="Place", RelX=0.5, RelY=0.3)
