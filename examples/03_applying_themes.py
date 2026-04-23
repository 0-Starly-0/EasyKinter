import easykinter as ek
import tkinter as tk

# previously, we created a few widgets.
# let's rip the code from over there and put it back here!
root = ek.CreateRoot(HideWindow=True)
toplevel = ek.CreateToplevel("Cool widgets!", root, None, 500, 500)

button = ek.CreateButton(toplevel, "New\nButton", ButtonWidth=50, ButtonHeight=50)
button.place(relx=0.5, rely=0.55, anchor="center")

label = ek.CreateLabel(toplevel, "The widget below me is\na super cool Button!", PackType="Place", RelX=0.5, RelY=0.3)

# in order to apply a GOOD LOOKING theme to these widgets... you'd need to MANUALLY PICK COLORS.
button.configure(bg="yellow", fg="white")
toplevel.configure(bg="#B8BB00")

# these look... ABNORMALLY UGLY. no offense to yellow lovers.
# luckily, we have a function to make up for our (yes, OUR) lack of styling skills!

# we can use a tuple...
widgetTuple = (button, toplevel, label)

# ...also a list...
widgetList = [button, toplevel, label]

# ...and even a dictionary!
widgetDict = {
    "toplevel": toplevel,
    "button": button,
    "label": label
}

# and you can have up to 8 really cool themes!
# you can delete any line you want and change the themes to see everything!
# here's 3 of them, one for each example:

# tuples rhyme a lot with forest (no they don't...)
ek.AddColorThemes(widgetTuple, "Forest")

# lists remind me of sticky notes, and sandstone is yellow, like sticky notes!
ek.AddColorThemes(widgetList, "Sandstone")

# i don't even know at this point. BUT the nordic theme IS popular! that means i'm gonna use it.
ek.AddColorThemes(widgetDict, "Nordic")