# Easykinter
(Tkinter made **easy**. *It's even in the name!*)
### (Desc.) A simple yet effective Tkinter wrapper that solves most boilerplate issues with tkinter, along with adding additional Quality Of Life features.


## Installation:
```bash
pip install easykinter

```


## Important note:
**Please** *(Please!)* make sure to *check out this command:*
```python
import easykinter as ek

# This function is really important!
ek.Help() # <- This one right here!
```
***This command will give you a full, short guide on how to use Easykinter!***


## Example:
```python
import easykinter as ek

# This one line creates the window
app = ek.CreateRoot()

# One line for a button that actually looks good
button = ek.CreateButton(text="I'm a Pro!", PackType="Pack")

# Stylized theming with 8 color scheme choices
ek.AddColorThemes( (app, button), "Midnight" )

# Root.mainloop()
# running mainloop is now completely optional
# the code can (and will) function nonetheless
```


## Some features brought in with the practicality of EasyKinter:
* ***MASSIVE*** reduction from *most of the boilerplate code from Tkinter!*
* ***An entirely new built-in Class*** for *Tkinter PhotoImages and Pillow!*
* ***Complete Audio support and management*** for Tkinter!
* A *Color Theming function* with up to ***8 profesisonal color themes!***
* A *quick and easy way* of creating and handling `tk.Canvas` and it's shapes!
* *A complete overhaul* to the `.geometry()` and `.bind()` functions!
* *A great overhaul* for *most packing systems!*
* Easier Window and Frame creation.
* Easier GUI, Entry *and* Display elements.
* ***And a bunch more!***


## Why use EasyKinter?
Because it's practical. It doesn't wanna make you pull your hairs out.

**A better explanation would be...**
**EasyKinter** provides you with a facilitated way to finally develop either a small, local and quick tool for those who want a small GUI script or push the limits of Tkinter to produce higher quality apps with much more ease and much less effort than one would normally need to produce the same level app with normal Tkinter!


## Extra Credits:
A **Huge** thanks to:
* The devs of **pygame-ce** for giving a great quality and stable pygame mixer engine!
* The devs of **Pillow** for integrating a huge relief of a headache when it comes to images!
