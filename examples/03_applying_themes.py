import easykinter as ek
import tkinter as tk

# Previously, we created a few widgets.
# Since i'm sure you already read everything- (I HOPE you did.)
# Why not just- let's rip the code from over there and put it back here!
root = ek.CreateRoot(HideWindow=True)
toplevel = ek.CreateToplevel("Cool widgets!", root, None, 500, 500)

button = ek.CreateButton(toplevel, "New\nButton", ButtonWidth=50, ButtonHeight=50)
button.place(relx=0.5, rely=0.55, anchor="center")

label = ek.CreateLabel(toplevel, "The widget below me is\na super cool Button!", PackType="Place", RelX=0.5, RelY=0.3)

# But of course, no developer reasolably ships their code looking HORRID.
# So let's smart these windows up!
# In order to apply a GOOD LOOKING theme to these widgets... you'd need to MANUALLY PICK COLORS.
button.configure(bg="yellow", fg="white")
toplevel.configure(bg="#B8BB00")

# These look... ABNORMALLY UGLY. (No offense to the yellow lovers though!)
# But NOW, luckily, we have a function to make up for our (yes, OUR, me and you!) lack of styling skills!

# When it comes to listing what we want to change...
# ...we can use a tuple...
widgetTuple = (button, toplevel, label)

# ...or a list...
widgetList = [button, toplevel, label]

# ...or even a dictionary!
widgetDict = {
    "toplevel": toplevel,
    "button": button,
    "label": label
}

# And you can have up to 8 really cool themes!
# You can delete any line you want and change the themes to see everything!
# Here's 3 of them, one for each example:

# Tuples rhyme a lot with 'forest'. (-No they don't, but you get the point, yeah?)
ek.AddColorThemes(widgetTuple, "Forest")

# Lists remind me of sticky notes, and sandstone is yellow, like sticky notes!
ek.AddColorThemes(widgetList, "Sandstone")

# I wanted to make another sly remark... but...
# I don't even know at this point. BUT the nordic theme IS popular! So here it is.
ek.AddColorThemes(widgetDict, "Nordic")
