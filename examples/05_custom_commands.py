import easykinter as ek, tkinter as tk
# You know, this little import line sounds so rhythmic...
# It's almost fun to write, and even better to read, so smooth.
# Especially when you write this like 20 times...

# Easykinter also gives you a few extra functions you can use.
root = ek.CreateRoot(HideWindow=True)
TopLevel1 = ek.CreateToplevel()


# Here's some examples:

# We covered this before,
# It's basically a MUST-HAVE if you've never seen this library before.
# Chances are-- you didn't. So yeah, use it.
ek.Help()

# This one was covered on a previous example:
ek.AddColorThemes(TopLevel1, "Snow")

# This one was too:
ek.BetterBind(TopLevel1, "Enter", lambda:None)

# But here's one you didn't see before:
# You ever wanted to move a window SMOOTHLY...
# ...but tkinter is just too CLUNKY? Here's the solution!
ek.BetterGeometry(TopLevel1, 250, 250, 600, 400, 1, 1, 1)

# You can also center the window... with one easy line.
# Yeah... you're not really saving 20+ lines of code here, but...
# ...I find this one a bit disappointing, personally, but it's there!
ek.CenterWindow(TopLevel1)

# Allow me to clean this one up:
TopLevel1.destroy()

# This one will blow your mind, i swear.
# So, originally, tkinter used to have something
# in the tkinter window attributes called: "-transparentcolor".
# It was really neat!.. in the 1980's... when it worked.
# But now?
SacrificedWindow = ek.CreateToplevel("I don't want to die :(")
SacrificedWindow.attributes("-transparentcolor", "#171717")

# As you can see... it's gone. R.I.P.
# Let me just clean up the mess:
root.after(7500, lambda: SacrificedWindow.destroy())

# But now, i brought back the function,
# And it even works properly now!

# But okay, let me place a few things on the window first.
# Or else it'll be an invisible cube. We can't even see it otherwise!
TopLevel2 = ek.CreateToplevel()
TopLevel2.config(bg="#202020")
Label1 = ek.CreateLabel(TopLevel2, "This text is...\nFLOATING MIDAIR!", "Monaco", 20, BgColor="#202020", FgColor="black", PackType="Place", RelX=0.5, RelY=0.5)

# Let me center it for you,
# for better viewing of the magic trick, of course.
ek.CenterWindow(TopLevel2)

# And now, for the final trick:
ek.BetterChromaKey(TopLevel2, "#202020")
# Poof, gone!