import tkinter as tk
import warnings as _warn
from PIL import Image as img, ImageTk as imgtk
import atexit as _atexit
from typing import Literal as _literal

# to hide the pygame-ce message (sorry devs but a console message is just a bit of a bummer)
import os as _os
_os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# yeah i really am sorry but i had to keep it tidy
from pygame import mixer as _mixer, mixer_music as _mixermusic

# adding this because apparently it's really useful
__all__ = [
    "Help"
    "CreateRoot",
    "CreateToplevel",
    "BetterConfigure",
    "CreateLabel",
    "CreateEntry",
    "CreateButton",
    "CreateMiscInputs",
    "CreateBoolInputs"
    "BetterBind",
    "BetterGeometry",
    "CenterWindow",
    "AddColorThemes"
    "CreateCanvas",
    "CreateCanvasShapes",
    "CreateCanvasMisc",
    "EasyMixer",
    "BetterAudio",
    "PlayAudio",
    "StreamAudio",
    "BetterPhotoImage",
    "BetterImage"
]

# also this for my sake:
__version__ = "0.1.1"

############################################
# tkinter (yay) this is where it all started
############################################9
#region all the nice and dandy EasyKinter functions 
#region Code that Automatically Runs mainloop() DO NOT TOUCH
#verifying if mainloop was called
_MainloopCalled = False
_OriginalMainloop = tk.Tk.mainloop

def _newmainloop(self, n=0):
    global _MainloopCalled
    _MainloopCalled = True
    return _OriginalMainloop(self, n)

tk.Tk.mainloop = _newmainloop

#now call the function if mainloop wasn't written, and we're good to go.
def _auto_run():
    global _MainloopCalled
    if not _MainloopCalled and hasattr(tk, "_default_root") and tk._default_root:
        try:
            tk._default_root.mainloop()
        except Exception:
            pass
_atexit.register(_auto_run)
#hell yeah.
#endregion

#region Create Root Window Function
_HideWindowChoices = _literal[True, False]
def CreateRoot(Title="Root Tkinter Window", SizeX=250, SizeY=250, PosX=None, PosY = None, HideWindow:_HideWindowChoices = False):
    """
    # This function creates a new Root window and returns the value of the fully created window when done.

    **Title** = What the Tk window's name will be upon creation.

    **Geometry Configs**:
        SizeX = Dictates the width of your window.
        SizeY = Dictates the height of your window.

        PosX = Position in your screen where the window is created, cannot be higher than the size of your monitor. (Width)
        PosY = Position in your screen where the window is created, cannot be higher than the size of your monitor. (Height)

    **Extra**:
        HideWindow = Tells the program if your window will be hidden upon creation.
    """
    
    if tk._default_root is not None:
        raise RuntimeError(f"Root window could not be created as a root instance already exists.") from None

    else:
        newRoot = tk.Tk()
        newRoot.title(Title)
        newRoot.geometry(f"{SizeX}x{SizeY}{f'+{PosX}' if PosX is not None else ''}{f'+{PosY}' if PosY is not None else ''}")

        if HideWindow:
            newRoot.withdraw()
    newRoot.update_idletasks()
    
    return newRoot
# endregion

#region Create Toplevel Window Function
def CreateToplevel(Title="Toplevel Tkinter Window", Parent=None, Child=None, SizeX=250, SizeY=250, PosX=None, PosY=None):
    """
    # This function creates a new Toplevel window and returns the value of the fully created window when done.

    **Title** = What the TopLevel window's name will be upon creation.
    
    **Geometry Configs**:
        SizeX = Dictates the width of your window.
        SizeY = Dictates the height of your window.

        PosX = Position in your screen where the window is created, cannot be higher than the size of your monitor. (Width)
        PosY = Position in your screen where the window is created, cannot be higher than the size of your monitor. (Height)

    **Extra**:
        Parent = Tells the program what parent this toplevel window will have. This can greatly affect the window's behavior.
    """

    WindowName = tk.Toplevel(Parent)
    WindowName.title(Title)
    WindowName.geometry(f"{SizeX}x{SizeY}{f'+{PosX}' if PosX is not None else ''}{f'+{PosY}' if PosY is not None else ''}")

    if Child is not None:
        if not isinstance(Child (tk.Toplevel, tk.Tk)):
            raise ValueError(f"Could not link {WindowName} with {Child} as {Child} is not a Toplevel or Tk window. Did you try checking the 'Child=' value?") from None

        else:
            Child.transient(WindowName)
    WindowName.update_idletasks()

    return WindowName
#endregion

#region Customization Function
_BoolChoices = _literal[True, False]
def BetterConfigure(TargetWindow, background=None, HideTitleBar:_BoolChoices=False, ResizableWidth:_BoolChoices=None, ResizableHeight:_BoolChoices=None, ClosingFunction=None, WindowTrasparency=None, Topmost:_BoolChoices=False, FocusForce:_BoolChoices=False):
    """
    # This function allows you to fully customize and color any window you want.

    **TargetWindow** = The name of the window or widget that will be targetted.    

    **Configs:**
        background = What the color of the widget's background will be set to.
        HideTitleBar = Will apply overridedirect(True) to window and remove its TitleBar.
        ResizableWidth = Dictates wether your window can be resized horizontally.
        ResizableHeight = Dictates if your window can be resized vertically.
        ClosingFunction = Adds a custom function that runs when said window is closed.
        WindowTransparency = Defines the Aplha of the selected window, where 0 is invisible and 1 is opaque.
            (Value ranges from 0 to 1. Do note that 0 aplha has a chance to be highly unstable, and is untraceable.)
        Topmost = Wether the window will constantly be always on top of other windows.
        FocusForce = Will force the window to be focused on.
    """

    if TargetWindow is None:
        raise ValueError(f"Expected a Tkinter window/frame, but got None instead.") from None
     
    elif not isinstance(TargetWindow, (tk.Tk, tk.Toplevel)):
        raise TypeError(f"Expected a Tkinter window, but got {type(TargetWindow).__name__} instead.") from None
    
    else:
        if background is not None:
            TargetWindow.configure(bg=background)

        if FocusForce:
            TargetWindow.focus_force()

        TargetWindow.attributes("-topmost", Topmost)

        if WindowTrasparency is not None:
            if isinstance(WindowTrasparency, (int, float)) and WindowTrasparency <= 1 and WindowTrasparency >=0:
                TargetWindow.attributes("-alpha", WindowTrasparency)
            
            else:
                raise ValueError("Could not set window's transparency as the value given was not an integer, float, or was not between 0 and 1. Did you try checking 'WindowTransparency'?") from None

        if HideTitleBar:
            TargetWindow.overrideredirect(True)
    
        if ResizableHeight is not None or ResizableWidth is not None:
            if isinstance(TargetWindow, (tk.Tk, tk.Toplevel)):
                TargetWindow.resizable(ResizableWidth, ResizableHeight)
            
            else:
                _warn.warn(f"Resize attributes were skipped as the target was a '{type(TargetWindow).__name__}' and it cannot have a Resizeable attrbute. Have you tried using tk.Toplevel or tk.Tk?", category=RuntimeWarning)

        if ClosingFunction is not None:
            if not isinstance(ClosingFunction, function):
                raise TypeError("Could not add a customized function to linked window as the value given wasn't a function.") from None
            
            else:
                TargetWindow.protocol("WM_DELETE_WINDOW", ClosingFunction)
#endregion

#region Creating Customizeable Labels and Auto-Pack Function
_PackTypeChoices = _literal["Pack", "Grid", "Place"]
_AnchorChoices = _literal["n", "s", "e", "w", "se", "sw", "ne", "nw", "center"]
_ImgCompundChoices = _literal["Top", "Left", "Right", "Bottom", "Center"]
_ExtraTextCustomChoices = _literal["Bold", "Italic", "Underline", "Overstrike"]
def CreateLabel(ForWindow, Text="New Label", font="Arial", FontSize=12, OptionalFontCustom:_ExtraTextCustomChoices="", LabelImage=None, ImageCompound:_ImgCompundChoices="Center", BgColor="#f0f0f0", FgColor="#000000", PackType:_PackTypeChoices=None, Anchor:_AnchorChoices="center", PadX=0, PadY=0, Side=tk.TOP, Row=0, Column=0, Sticky=None, X=None, Y=None, RelX=None, RelY=None):
    """
    # This function creates and returns a custom label that can be also packed within the same function.

    **ForWindow** = This dictates that target where the label will be created for.

    **Formatting:**
        text = What text the label will contain.
        font = What custom font the label will use.
        FontSize = The size of the font used.
        OptionalFontCustom = Dictates special font formatting such as bold, italic, or underline.
            (Options: 'bold', 'italic', 'underline', 'overstrike')
        LabelImage = What custom image the label will have. (Must be a tk.PhotoImage object.)
        ImageCompound = What direction the image will be placed on top of the text.
            (Options: 'top', 'left', 'center',  'right', 'bottom', 'none')

    **Extra Customization:**
        BgColor = What the background of the label will be colored as.
        FgColor = The color of the text within the label.
        Anchor = Where the text will be anchored, affects where it will be packed.
            (Options: 'e', 's', 'w', 'n', 'se', 'sw', 'ne', 'nw', 'center')
    
    # Packing Types and their parameters:

    **Pack (The default type, packs label and contains borders.):**
        PadX = Width for the padding of the label.
        PadY = Height for the padding of the label.
        Side = Side where the label will go to in the widget, is relative.
        Sticky = Position where the label will stick to in the widget, is not relative.
    
    **Grid (for mounting grids and organized sheets):**
        Row = The row where your element will be placed. (Horizontal)
        Column = the column where your element will be placed. (Vertical)
        PadX = the padding width your element will have, affects elements in and outside of the grid.
        PadY = the padding height your element will have, affects elements in and outside of the grid.
    
    **Place (for accurately placing elements in absolute or relative positions):**
        X = The absolute position of the element in your window, cannot be moved. (Width)
        Y = The absolute position of the element in your window, cannot be moved. (Height)
        RelX = The relative position of the element in your window, can be moved. (Width)
        RelY = The relative position of the element in your window, can be moved. (Height)
    """

    if not isinstance(ForWindow, (tk.Tk, tk.Frame, tk.Toplevel)):
        raise TypeError(f"Expected a Tkinter window/frame, but got {type(ForWindow).__name__} instead.") from None

    if ImageCompound is not None:
        ImageCompound = ImageCompound.lower()

        if ImageCompound == "top":
            ImageCompound = tk.TOP
        
        elif ImageCompound == "left":
            ImageCompound = tk.LEFT
        
        elif ImageCompound == "center":
            ImageCompound = tk.CENTER
        
        elif ImageCompound == "right":
            ImageCompound = tk.RIGHT
        
        elif ImageCompound == "bottom":
            ImageCompound = tk.BOTTOM

    newLabel = tk.Label(ForWindow, image=LabelImage, compound=ImageCompound, text=Text, font=(font, FontSize, OptionalFontCustom.lower()), bg=BgColor, fg=FgColor)

    if PackType is not None:
        PackType = PackType.lower()

    if PackType is not None and PackType not in ["place", "grid", "pack"]:
        raise ValueError(f"Expected a proper packing style, but got {PackType} instead. Current packing types are 'Pack', 'Grid', or 'Place'") from None

    elif PackType == "pack":
        newLabel.pack(anchor=Anchor, padx=PadX, pady=PadY, side=Side, sticky=Sticky)
    
    elif PackType == "place":
        newLabel.place(x=X, y=Y, relx=RelX, rely=RelY, anchor=Anchor)

    elif PackType == "grid":
        newLabel.grid(row=Row, column=Column, padx=PadX, pady=PadY)
    
    return newLabel
#endregion

#region Creating Text Entry Widget and Custom Keybinding Function
def CreateEntry(ForWindow, CustomFunc=None, CustomFuncKeybind=None, PlaceHolderEnabled:_BoolChoices=True, PlaceHolderText="Insert text here...", PlaceHolderTextColor="Gray", Width=None, Font="Arial", FontSize=12, FontProperties="", borderwidth=None, bg=None, fg="#000000", PackType:_PackTypeChoices=None, Anchor:_AnchorChoices="center", PadX=0, PadY=0, Side=tk.TOP, Row=0, Column=0, Sticky=None, X=None, Y=None, RelX=None, RelY=None):
    """
    # This function automatically creates and customizes an Entry widget in tkinter. Can also additionally trigger a funtion or be automatically packed.

    **Logic parameters:**
        ForWindow = Defines the target window where the entry will be created.
        CustomFunc = Sets a function to automatically trigger when the set keybind is activated. Must be added alongside **CustomFuncKeybind.**
        CustomFuncKeybind = Sets a keybind for a function to trigger when entering said keybind in the entry widget. Must be added alongside **CustomFunc.**
        PlaceHolderEnabled = Dictates wether the Entry widget will have a pre-built placeholder.
        
    **UX and Customization:**
        PlaceHolderText = Defines what text will appear in the placeholder UI.
        PlaceHolderTextColor = Defines what color of the placeholder text will be.
        Width = Defines the width of the input box.
        Font = Defines the custom font the text will have in the input.
        FontSize: = Defines the size of the text in the Entry box. Also affects Entry box height.
        FontPorperties = Wether a custom font property will be applied.
            (Current properties availiable = 'Bold', 'Italic', 'Underline', 'Overstrike')
        bg = What the background of the label will be colored as.
        fg = The color of the text within the label.
    
    # Packing Types and their parameters:

    **Pack (The default type, packs label and contains borders.):**
        PadX = Width for the padding of the label.
        PadY = Height for the padding of the label.
        Side = Side where the label will go to in the widget, is relative.
        Sticky = Position where the label will stick to in the widget, is not relative.
    
    **Grid (for mounting grids and organized sheets):**
        Row = The row where your element will be placed. (Horizontal)
        Column = the column where your element will be placed. (Vertical)
        PadX = the padding width your element will have, affects elements in and outside of the grid.
        PadY = the padding height your element will have, affects elements in and outside of the grid.
    
    **Place (for accurately placing elements in absolute or relative positions):**
        X = The absolute position of the element in your window, cannot be moved. (Width)
        Y = The absolute position of the element in your window, cannot be moved. (Height)
        RelX = The relative position of the element in your window, can be moved. (Width)
        RelY = The relative position of the element in your window, can be moved. (Height)    
    """

    def on_entry_click(event=None):
        if NewEntry.get() == PlaceHolderText:
            NewEntry.delete(0, tk.END)
            NewEntry.config(fg=fg.lower())

    def on_focus_out(event=None):
        if not NewEntry.get():
            NewEntry.insert(0, PlaceHolderText)
            NewEntry.config(fg=PlaceHolderTextColor.lower())


    NewEntry = tk.Entry(ForWindow, width=Width if Width is not None else 20, font=(Font.capitalize(), FontSize, FontProperties.lower() if FontProperties else "normal"), bg=bg, fg=fg, borderwidth=borderwidth if borderwidth is not None else 1)

    if CustomFuncKeybind is not None and CustomFunc is not None:
        #this is for a single key
        if len(CustomFuncKeybind) == 1:
            FinalKey = CustomFuncKeybind

        #this is for the war veterans whose died plenty for not using <>
        elif CustomFuncKeybind.startswith("<") and CustomFuncKeybind.endswith(">"):
            CustomFuncKeybind = CustomFuncKeybind.title()

            FinalKey = f"{CustomFuncKeybind}"

        #and for the people with dementia
        else:
            CustomFuncKeybind = CustomFuncKeybind.title()

            FinalKey = f"<{CustomFuncKeybind}>"
        def eventNeedlessFunction(event):
            CustomFunc()

        NewEntry.bind(FinalKey, eventNeedlessFunction)
    
    elif CustomFuncKeybind is not None or CustomFunc is not None:
        raise ValueError("The function could not be called as the Function Keybind values have not been filled properly. Did you try checking both 'CustomFunc__' values?") from None

    if PlaceHolderEnabled:
        NewEntry.bind("<FocusIn>", on_entry_click)
        NewEntry.bind("<FocusOut>", on_focus_out)
        on_focus_out()


    if PackType is not None:
        PackType = PackType.lower()

    if PackType is not None and PackType not in ["place", "grid", "pack"]:
        raise ValueError(f"Expected a proper packing style, but got {PackType} instead. Current packing types are 'Pack', 'Grid', or 'Place'") from None

    elif PackType == "pack":
        NewEntry.pack(anchor=Anchor, padx=PadX, pady=PadY, side=Side, sticky=Sticky)
    
    elif PackType == "place":
        NewEntry.place(x=X, y=Y, relx=RelX, rely=RelY, anchor=Anchor)

    elif PackType == "grid":
        NewEntry.grid(row=Row if Row is not None else 0, column=Column if Column is not None else 0, padx=PadX, pady=PadY)

    return NewEntry
#endregion

#region Creating Button Widget and Custom Keybinding Function
def CreateButton(ForWindow, Text="New Button", Image=None, Compound:_ImgCompundChoices="center", font="Arial", FontSize=12, optionalCustomization:_ExtraTextCustomChoices="", CommandFunc=None, ButtonWidth=100, ButtonHeight=30, BgColor="#f0f0f0", FgColor="#000000", PackType:_PackTypeChoices=None, Anchor:_AnchorChoices="center", PadX=0, PadY=0, Side=tk.TOP, Row=0, Column=0, Sticky=None, X=None, Y=None, RelX=None, RelY=None):
    """
    # This function creates and returns a custom button that can be also packed within the same function.

    **ForWindow** = This dictates that target where the button will be created for.

    **Button Contents:**
        Text = What custom text will the button have.
        Image = What custom image the button will have.

    **Formatting:**
        Compound = What direction the image will be placed on top of the text.
            (Options: 'top', 'left', 'center',  'right', 'bottom', 'none')
        font = What custom font the button will use.
        FontSize = The size of the font used.
        OptionalCustomization = Dictates special font formatting such as bold, italic, or underline.
            (Options: 'bold', 'italic', 'underline', 'overstrike')

    **Extra Customization:**
        BgColor = What the background of the button will be colored as.
        FgColor = The color of the text within the button.
        Anchor = Where the text will be anchored, affects where it will be packed.
    
    # Packing Types and their parameters:

    **Pack (The default type, packs label and contains borders.):**
        PadX = Width for the padding of the label.
        PadY = Height for the padding of the label.
        Side = Side where the label will go to in the widget, is relative.
        Sticky = Position where the label will stick to in the widget, is not relative.
    
    **Grid (for mounting grids and organized sheets):**
        Row = The row where your element will be placed. (Horizontal)
        Column = the column where your element will be placed. (Vertical)
        PadX = the padding width your element will have, affects elements in and outside of the grid.
        PadY = the padding height your element will have, affects elements in and outside of the grid.
    
    **Place (for accurately placing elements in absolute or relative positions):**
        X = The absolute position of the element in your window, cannot be moved. (Width)
        Y = The absolute position of the element in your window, cannot be moved. (Height)
        RelX = The relative position of the element in your window, can be moved. (Width)
        RelY = The relative position of the element in your window, can be moved. (Height)
    """
    
    if not isinstance(ForWindow, (tk.Tk, tk.Frame, tk.Toplevel)):
        raise TypeError(f"Expected a Tkinter window/frame, but got {type(ForWindow).__name__} instead.") from None

    TransparentPixel = "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
    TrasnparentImage = tk.PhotoImage(data=TransparentPixel)

    Compound = Compound.lower()

    if Image is None:
        newButton = tk.Button(ForWindow, command=CommandFunc, image=TrasnparentImage, text=Text, compound=Compound, font=(font, FontSize, optionalCustomization.lower()), width=ButtonWidth, height=ButtonHeight, bg=BgColor, fg=FgColor)
        newButton.image = TrasnparentImage

    else:
        newButton = tk.Button(ForWindow, command=CommandFunc, image=Image, text=Text, compound=Compound,  font=(font, FontSize, optionalCustomization.lower()), width=ButtonWidth, height=ButtonHeight, bg=BgColor, fg=FgColor)
        newButton.image = Image

    if PackType is not None:
        PackType = PackType.lower()

    if PackType is not None and PackType not in ["place", "grid", "pack"]:
        raise ValueError(f"Expected a proper packing style, but got {PackType} instead. Current packing types are 'Pack', 'Grid', or 'Place'") from None

    elif PackType == "pack":
        newButton.pack(anchor=Anchor, padx=PadX, pady=PadY, side=Side, sticky=Sticky)
    
    elif PackType == "place":
        newButton.place(x=X, y=Y, relx=RelX, rely=RelY, anchor=Anchor)

    elif PackType == "grid":
        newButton.grid(row=Row, column=Column, padx=PadX, pady=PadY)
    
    return newButton
#endregion

#region Creating AplhaNumerical Input Widgets and Miscellaneous
_InputTypeChoices = _literal["Text", "Spinbox", "Scale"]
def CreateMiscInputs(ForWindow, InputType:_InputTypeChoices, Border=2, CustomFont="Arial", CustomFontSize=12, CustomFontExtra:_ExtraTextCustomChoices="", BgColor="#f0f0f0", FgColor="#000000", CommandKeybind=None, CommandFunction=None, TextHeight=40, TextWidth=70, SpinboxFrom=-100, SpinboxTo=100, ScaleLength=100, ScaleRepeatDelay=1, ScaleResolution=1, PackType:_PackTypeChoices=None, PadX=None, PadY=None, Anchor:_AnchorChoices="center", Side=tk.TOP, Row=0, Column=0, Sticky=None, X=None, Y=None, RelX=None, RelY=None):
    """
    # This function can create, pack, and set a command for other, miscellaneous Aplhanumerical input widgets and returns the widget.

    **Essential Parameters:**
        ForWindow = This parameter dictates what window the custom widget will be created for.
        InputType = This parameter dictates what custom widget will be created.
            (Options: Text, Spinbox, Scale)

    **Customization Parameters:** 
        Border = This parameter defines the border of the created widget.
        CustomFont = This parameter defines the Font that will be used in the created widget.
        CustomFontSize = This parameter defines the custom Font Size that the widget will have.
        CustomFontExtra = This parameter defines any extra properties the font can have, such as Bold.
            (Options: 'Bold', 'Italic', 'Underline', 'Overstrike'.)
        BgColor = Defines the background color of the widget.
        FgColor = Defines the foreground color of the widget.

    **Custom Keybind Parameters:**
        CommandKeybind = What the custom keybind of said widget will be. Must have CommandFunction to work.
        CommandFunction = The command that will be executed when pressing the respective keybind. Must have CommandKeybind to work.

    **Text Specific Parameters:**
        TextHeight = The height, in pixels, of the text element.
        TextWidth = The width, in pixels, of the text element.

    **SpinBox Specific Parameters:**
        SpinboxFrom = The minimum value that the SpinBox can have.
        SpinboxTo = The maximum value that the spinbox can have.
    
    **Scale Specific Parameters:**
        ScaleLength = The length of the scale in pixels. (Width, X value.)
        ScaleRepeatDelay = The frequency that the scale will show numbers based on their position.
            (For example, a ScaleRepeatDelay of 0.5 would show numbers every 0.5.)
        ScaleResolution = The rounding that the scale will have upon selecting a value, where it snaps your cursor to said value.
            (For example, setting to 1 snaps your selector to every integer, skipping decimals. Setting to -1 disables rounding.)
    
    # Packing Types and their parameters:

    **Pack (The default type, packs label and contains borders.):**
        PadX = Width for the padding of the label.
        PadY = Height for the padding of the label.
        Side = Side where the label will go to in the widget, is relative.
        Sticky = Position where the label will stick to in the widget, is not relative.
    
    **Grid (for mounting grids and organized sheets):**
        Row = The row where your element will be placed. (Horizontal)
        Column = the column where your element will be placed. (Vertical)
        PadX = the padding width your element will have, affects elements in and outside of the grid.
        PadY = the padding height your element will have, affects elements in and outside of the grid.
    
    **Place (for accurately placing elements in absolute or relative positions):**
        X = The absolute position of the element in your window, cannot be moved. (Width)
        Y = The absolute position of the element in your window, cannot be moved. (Height)
        RelX = The relative position of the element in your window, can be moved. (Width)
        RelY = The relative position of the element in your window, can be moved. (Height)
    """
    
    if not ForWindow or not InputType:
        raise ValueError("Could not create miscellaneous input types as one of the necessary values wew not given. Did you try filling the primary essential values?") from None

    else:
        InputType = InputType.lower()

        if InputType == "text":
            NewInput = tk.Text(ForWindow, height=TextHeight, width=TextWidth, bg=BgColor, fg=FgColor, bd=Border, font=(CustomFont.capitalize(), CustomFontSize, CustomFontExtra.lower()))
        
        elif InputType == "spinbox":
            NewInput = tk.Spinbox(ForWindow, bg=BgColor, fg=FgColor, bd=Border, font=(CustomFont.capitalize(), CustomFontSize, CustomFontExtra.lower()), from_=SpinboxFrom, to=SpinboxTo)

        elif InputType == "scale":
            NewInput = NewInput = tk.Scale(ForWindow, bg=BgColor, fg=FgColor, bd=Border, font=(CustomFont.capitalize(), CustomFontSize, CustomFontExtra.lower()), repeatdelay=ScaleRepeatDelay, resolution=ScaleResolution, length=ScaleLength)
    
    if CommandKeybind is not None and CommandFunction is not None:
        #this is for a single key
        if len(CommandKeybind) == 1:
            FinalKey = CommandKeybind

        #this is for the war veterans whose died plenty for not using <>
        elif CommandKeybind.startswith("<") and CommandKeybind.endswith(">"):
            CommandKeybind = CommandKeybind.title()

            FinalKey = f"{CommandKeybind}"

        #and for the people with dementia
        else:
            CommandKeybind = CommandKeybind.title()

            FinalKey = f"<{CommandKeybind}>"
        def eventNeedlessFunction(event):
            CommandFunction()

        NewInput.bind(FinalKey, eventNeedlessFunction)

    elif CommandKeybind is not None or CommandFunction is not None:
        raise ValueError("Could not bind a command to this widget as one of the proper 'Command__' were not filled. Did you try checking both the 'Command__' parameters?") from None

    if PackType is not None:
        PackType = PackType.lower()

    if PackType is not None and PackType not in ["place", "grid", "pack"]:
        raise ValueError(f"Expected a proper packing style, but got {PackType} instead. Current packing types are 'Pack', 'Grid', or 'Place'") from None

    elif PackType == "pack":
        NewInput.pack(anchor=Anchor, padx=PadX, pady=PadY, side=Side, sticky=Sticky)
    
    elif PackType == "place":
        NewInput.place(x=X, y=Y, relx=RelX, rely=RelY, anchor=Anchor)

    elif PackType == "grid":
        NewInput.grid(row=Row if Row is not None else 0, column=Column if Column is not None else 0, padx=PadX, pady=PadY)

    return NewInput
#endregion

#region Creating Boolean Input Widgets and Miscellaneous
_BoolInputChoices = _literal["Checkbutton", "Radiobutton", "Listbox"]
_CheckboxStateChoices = _literal["NORMAL", "DISABLED"]
def CreateBoolInputs(ForWindow, WidgetType:_BoolInputChoices, Border=2, CustomText="", CustomFont="Arial", CustomFontSize=12, CustomFontExtra:_ExtraTextCustomChoices="", BgColor="#f0f0f0", FgColor="#000000", CommandKeybind=None, CommandFunction=None, CheckBoxState:_CheckboxStateChoices="NORMAL", CheckBoxOnValue=1, CheckBoxOffValue=0, PackType:_PackTypeChoices=None, PadX=None, PadY=None, Anchor:_AnchorChoices="center", Side=tk.TOP, Row=0, Column=0, Sticky=None, X=None, Y=None, RelX=None, RelY=None):
    """
    # Creates a miscellaneous input from the Bool type.

    **Essential Parameters:**
        ForWindow = This parameter dictates what window the custom widget will be created for.
        WidgetType = This parameter dictates what custom widget will be created.
            (Options: Checkbutton, Radiobutton, Listbox)

    **Customization Parameters:** 
        Border = This parameter defines the border of the created widget.
        CustomFont = This parameter defines the Font that will be used in the created widget.
        CustomFontSize = This parameter defines the custom Font Size that the widget will have.
        CustomFontExtra = This parameter defines any extra properties the font can have, such as Bold.
            (Options: 'Bold', 'Italic', 'Underline', 'Overstrike'.)
        BgColor = Defines the background color of the widget.
        FgColor = Defines the foreground color of the widget.

    **Custom Keybind Parameters:**
        CommandKeybind = What the custom keybind of said widget will be. Must have CommandFunction to work.
        CommandFunction = The command that will be executed when pressing the respective keybind. Must have CommandKeybind to work.
    
    **CheckBox Specific Parameters:**
        CheckBoxState = 'NORMAL' for the checkbox to function normally. 'DISABLED' for the checkbox to not work.
        CheckBoxOnValue = The value that the checkbox will return when on.
        CheckBoxOffValue = The value that the checkbox will return when off.

    # Packing Types and their parameters:

    **Pack (The default type, packs label and contains borders.):**
        PadX = Width for the padding of the label.
        PadY = Height for the padding of the label.
        Side = Side where the label will go to in the widget, is relative.
        Sticky = Position where the label will stick to in the widget, is not relative.
    
    **Grid (for mounting grids and organized sheets):**
        Row = The row where your element will be placed. (Horizontal)
        Column = the column where your element will be placed. (Vertical)
        PadX = the padding width your element will have, affects elements in and outside of the grid.
        PadY = the padding height your element will have, affects elements in and outside of the grid.
    
    **Place (for accurately placing elements in absolute or relative positions):**
        X = The absolute position of the element in your window, cannot be moved. (Width)
        Y = The absolute position of the element in your window, cannot be moved. (Height)
        RelX = The relative position of the element in your window, can be moved. (Width)
        RelY = The relative position of the element in your window, can be moved. (Height)
    """
    
    if not ForWindow or not WidgetType:
        raise ValueError("Could not create a bool input widget as the essential parameters were not filled. Did you try checking 'ForWindow' and 'WidgetType'?") from None
    
    else:
        WidgetType = WidgetType.lower()

        if WidgetType == "checkbutton":
            NewBool = tk.Checkbutton(ForWindow, bd=Border, text=CustomText, anchor=Anchor, font=(CustomFont.capitalize(), CustomFontSize, CustomFontExtra.lower()), bg=BgColor, fg=FgColor, state=CheckBoxState, onvalue=CheckBoxOnValue, offvalue=CheckBoxOffValue)

        elif WidgetType == "radiobutton":
            NewBool = tk.Radiobutton(ForWindow, bd=Border, anchor=Anchor, text=CustomText, font=(CustomFont.capitalize(), CustomFontSize, CustomFontExtra.lower()), bg=BgColor, fg=FgColor)

        elif WidgetType == "listbox":
            NewBool = tk.Listbox(ForWindow, bd=Border, text=CustomText, font=(CustomFont.capitalize(), CustomFontSize, CustomFontExtra.lower()), bg=BgColor, fg=FgColor)

    if CommandKeybind is not None and CommandFunction is not None:
        #this is for a single key
        if len(CommandKeybind) == 1:
            FinalKey = CommandKeybind

        #this is for the war veterans whose died plenty for not using <>
        elif CommandKeybind.startswith("<") and CommandKeybind.endswith(">"):
            CommandKeybind = CommandKeybind.title()

            FinalKey = f"{CommandKeybind}"

        #and for the people with dementia
        else:
            CommandKeybind = CommandKeybind.title()

            FinalKey = f"<{CommandKeybind}>"
        def eventNeedlessFunction(event):
            CommandFunction()

        NewBool.bind(FinalKey, eventNeedlessFunction)

    elif CommandKeybind is not None or CommandFunction is not None:
        raise ValueError("Could not bind a command to this widget as one of the proper 'Command__' were not filled. Did you try checking both the 'Command__' parameters?") from None

    if PackType is not None:
        PackType = PackType.lower()

    if PackType is not None and PackType not in ["place", "grid", "pack"]:
        raise ValueError(f"Expected a proper packing style, but got {PackType} instead. Current packing types are 'Pack', 'Grid', or 'Place'") from None

    elif PackType == "pack":
        NewBool.pack(anchor=Anchor, padx=PadX, pady=PadY, side=Side, sticky=Sticky)
    
    elif PackType == "place":
        NewBool.place(x=X, y=Y, relx=RelX, rely=RelY, anchor=Anchor)

    elif PackType == "grid":
        NewBool.grid(row=Row if Row is not None else 0, column=Column if Column is not None else 0, padx=PadX, pady=PadY)

    return NewBool
#endregion

#region Better Bind With Additional Improved Features
def BetterBind(TargetWindow, KeyToBind, FunctionToBind, After=1, RepeatTimes=0, RepeatDelay=1):
    """
    # A function that improves Tkinter's .bind() feature, improving it with a new nit-picked quality of life add-ons.

    **Necessary parameters:**
        TargetWindow = The Tkinter element you want to bind your function and keybind to.
        FunctionToBind = The function you wish to bind to a key, that runs within the element.
        KeyToBind = The Keybind you want to set to your element to run your script.
            (Luckily, here's a couple references!)
                https://web.archive.org/web/20190512164300id_/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-types.html
                https://web.archive.org/web/20190515021108id_/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html
                https://www.tcl-lang.org/man/tcl8.4/TkCmd/keysyms.htm

    **Additional parameters:**
        After = Dictates the time in **milliseconds** the function will take to run.
        RepeatTimes = The amount of times the function will repeat after running once.
            (Note: You can repeat infinitely by typing 'inf' or -1.)
        RepeatDelay = The delay in **milliseconds** that a function will take to repeat.
    """

    if TargetWindow and KeyToBind and FunctionToBind:
        #this is for a single key
        if len(KeyToBind) == 1:
            FinalKey = KeyToBind

        #this is for the war veterans whose died plenty for not using <>
        elif KeyToBind.startswith("<") and KeyToBind.endswith(">"):
            KeyToBind = KeyToBind.title()

            FinalKey = f"{KeyToBind}"

        #and for the people with dementia
        else:
            KeyToBind = KeyToBind.title()

            FinalKey = f"<{KeyToBind}>"

        def EventlessBind(event):
            def StartFunctions():
                FunctionRunCount = 0

                def repeatingFunction():
                    nonlocal FunctionRunCount, RepeatTimes
                    FunctionToBind()

                    if isinstance(RepeatTimes, str) and RepeatTimes.lower() == "inf":
                        RepeatTimes = -1

                    elif isinstance(RepeatTimes, str) and RepeatTimes != "inf":
                        raise TypeError("The function oculd not be repeated as the value typed for RepeatTimes is invalid. Did you try checking the RepeatTimes value type?") from None

                    FunctionRunCount += 1
                            
                    if FunctionRunCount <= RepeatTimes or RepeatTimes == -1:
                        TargetWindow.after(RepeatDelay, repeatingFunction)

                repeatingFunction()

            TargetWindow.after(After, StartFunctions)
        
        TargetWindow.bind(FinalKey, EventlessBind)
    
    else:
        raise ValueError("Could not bind function to an element as one of the necessary parameters were not filled. Have you tried filling all '__ToBind' parameters?") from None
#endregion

#region Moving Windows and Changing Their Geometry Smoothly Function
def BetterGeometry(TargetWindow, SizeX=0, SizeY=0, PosX=None, PosY=None, SizeSmooth=0, PosSmooth=0, Delay=1):
    """
    # This function is a better way to set a window's geometry, both in size and position on screen, smoothing included.

    **TargetWindow** = The window in which position or size will be altered.

    **Geometry Positions:**
        SizeX = The final width that the window will have.
        SizeY = The final height that the window will have.
        PosX = The final width position that the window will have.
        PosY = The final height position that the window will have.
    
    **Additional Parameters:**
        SizeSmooth = How much the change from the current size to the final size will be smoothed. **The lesser the number, the smoother.**
        PosSmooth = How much the movement from the current position to the final position will be smoothed. **The lesser the number, the smoother.**
        Delay = The delay in time that will take for the window to go to it's next position. **The lesser the number, the smoother.**
    """
    TargetWindow.update_idletasks()

    TargetWindowX = TargetWindow.winfo_width()
    TargetWindowY = TargetWindow.winfo_height()

    if SizeSmooth == 0 and PosSmooth == 0:
        TargetWindow.geometry(f"{SizeX if SizeX != 0 else TargetWindowX}x{SizeY if SizeY != 0 else TargetWindowY}{f'+{PosX}' if PosX is not None else ''}{f'+{PosY}' if PosY is not None else ''}")
    
    else:
        s_smooth = max(1, int(SizeSmooth)) if SizeSmooth and SizeSmooth > 0 else 0
        p_smooth = max(1, int(PosSmooth)) if PosSmooth and PosSmooth > 0 else 0

        curX, curY = TargetWindow.winfo_x(), TargetWindow.winfo_y()
        curW, curH = TargetWindow.winfo_width(), TargetWindow.winfo_height()

        tX = int(PosX) if PosX is not None else curX
        tY = int(PosY) if PosY is not None else curY
        tW = int(SizeX) if (SizeX is not None and SizeX != 0) else curW
        tH = int(SizeY) if (SizeY is not None and SizeY != 0) else curH

        def TheTrueSmooth():
            nonlocal curX, curY, curW, curH

            if p_smooth > 0:
                if curX != tX:
                    diffX = tX - curX
                    if abs(diffX) <= p_smooth: curX = tX
                    else: curX += p_smooth if diffX > 0 else -p_smooth
                if curY != tY:
                    diffY = tY - curY
                    if abs(diffY) <= p_smooth: curY = tY
                    else: curY += p_smooth if diffY > 0 else -p_smooth

            if s_smooth > 0:
                if curW != tW:
                    diffW = tW - curW
                    if abs(diffW) <= s_smooth: curW = tW
                    else: curW += s_smooth if diffW > 0 else -s_smooth
                if curH != tH:
                    diffH = tH - curH
                    if abs(diffH) <= s_smooth: curH = tH
                    else: curH += s_smooth if diffH > 0 else -s_smooth

            TargetWindow.geometry(f"{curW}x{curH}+{curX}+{curY}")

            if curX != tX or curY != tY or curW != tW or curH != tH:
                TargetWindow.after(Delay, TheTrueSmooth)

        TheTrueSmooth()        
#endregion

#region Centering Windows to the Screen Function
def CenterWindow(TargetWindow):
    """
    # This script automatically moves the target window towards the cetner of the monitor.

    **TargetWindow** = The target window that will be centered. 
    """
    TargetWindow.attributes('-alpha', 0)
    
    def CenteringFunc():
        width = TargetWindow.winfo_width()
        height = TargetWindow.winfo_height()
        
        ScreenWidth = TargetWindow.winfo_screenwidth()
        ScreenHeight = TargetWindow.winfo_screenheight()
        

        x = (ScreenWidth // 2) - (width // 2)
        y = (ScreenHeight // 2) - (height // 2)
        
        TargetWindow.geometry(f'{width}x{height}+{x}+{y}')
        TargetWindow.attributes("-alpha", 1)
    TargetWindow.after(125, CenteringFunc)
#endregion

#endregion


############################################
# time to move on to tk.Canvas, my nightmare
############################################
#region ahhh... tk.Canvas, where hell sets loose

#region Function that Automatically Creates and Packs Canvas
def CreateCanvas(TargetWindow, SizeX=250, SizeY=250, BgColor="#f0f0f0", PackType:_PackTypeChoices=None, Anchor:_AnchorChoices="center", PadX=0, PadY=0, Side=tk.TOP, Row=0, Column=0, Sticky=None, X=None, Y=None, RelX=None, RelY=None):
    """
    # Creates a tk.Canvas element and automatically packs it.

    **Necessary parameters:**
        TargetWindow = The window that will be receiving the Canvas.

    **Geometry Parameters:**
        SizeX = The width in pixels of the Canvas Widget.
        SizeY = The height in pixels of the Canvas Widget.
    
    **Extra Customization:**
        BgColor = What the background of the label will be colored as.

    # Packing Types and their parameters:

    **Pack (The default type, packs label and contains borders.):**
        PadX = Width for the padding of the label.
        PadY = Height for the padding of the label.
        Side = Side where the label will go to in the widget, is relative.
        Sticky = Position where the label will stick to in the widget, is not relative.
    
    **Grid (for mounting grids and organized sheets):**
        Row = The row where your element will be placed. (Horizontal)
        Column = the column where your element will be placed. (Vertical)
        PadX = the padding width your element will have, affects elements in and outside of the grid.
        PadY = the padding height your element will have, affects elements in and outside of the grid.
    
    **Place (for accurately placing elements in absolute or relative positions):**
        X = The absolute position of the element in your window, cannot be moved. (Width)
        Y = The absolute position of the element in your window, cannot be moved. (Height)
        RelX = The relative position of the element in your window, can be moved. (Width)
        RelY = The relative position of the element in your window, can be moved. (Height)
    """

    if not isinstance(TargetWindow, (tk.Tk, tk.Toplevel)):
        raise TypeError(f"Expected a Tkinter window, but got {type(TargetWindow).__name__} instead.") from None

    NewCanvas = tk.Canvas(TargetWindow, width=SizeX, height=SizeY, bg=BgColor)

    if PackType is not None:
        PackType = PackType.lower()

    if PackType is not None and PackType not in ["place", "grid", "pack"]:
        raise ValueError(f"Expected a proper packing style, but got {PackType} instead. Current packing types are 'Pack', 'Grid', or 'Place'") from None

    elif PackType == "pack":
        NewCanvas.pack(anchor=Anchor, padx=PadX, pady=PadY, side=Side, sticky=Sticky)
    
    elif PackType == "place":
        NewCanvas.place(x=X, y=Y, relx=RelX, rely=RelY, anchor=Anchor)

    elif PackType == "grid":
        NewCanvas.grid(row=Row, column=Column, padx=PadX, pady=PadY)

    return NewCanvas
#endregion

#region Creating Various Shapes in Canvas
_ShapeChoices = _literal["Square", "Rectangle", "Circle", "Oval"]
def CreateCanvasShapes(ForCanvas, Shape:_ShapeChoices, PosX, PosY, SquareSize=25, RectangleX=20, RectangleY=40, CircleSize=25, OvalX=20, OvalY=40, color="blue", OutlineColor="black", ActiveColor=None):
    """
    # Creates a custom shape for a tk.Canvas and automatically centers it in the give ncoordinates and size.

    **Necessary parameters:**
        ForCanvas = Dictates the used tk.Canvas that the shape will be placed in.
        Shape = What shape will be placed in the tk.Canvas.
            (Options: Square, Rectangle, Circle, Oval)
        
    **Geometry parameters:**
        PosX = The horizontal position in pixels where the shape will be placed.
        PosY = The vertical position in pixels where the shape will be placed.
    
    **Customization parameters:**
        Color = The color that the shape will be filled with.
        OutlineColor = The color of the shape's border.
        ActiveColor = The color that the shappe will have when it's hovered on, changes back to normal when hovering off.

    # Shape specific parameters
    
    **Square parameters:**
        SquareSize = The size in pixels that the square will have.
    
    **Circle parameters:**
        CircleSize = The size in pixels that the circle will have.
    
    **Rectangle parameters:**
        RectangleX = The width of the rectangle in pixels.
        RectangleY = The height of the rectangle in pixels.
    
    **Oval parameters:**
        OvalX = The width of the oval in pixels.
        OvalY = The height of the oval in pixels.
    """

    if not isinstance(ForCanvas, tk.Canvas):
        raise ValueError(f"Could not create custom canvas shape as {ForCanvas} is not a valid canvas. Did you try checking the tk.Canvas given?") from None

    Shape = Shape.lower()
    color = color.lower()
    OutlineColor = OutlineColor.lower()
    ActiveColor = color if ActiveColor is None else ActiveColor.lower()

    if Shape == "square":
        offset = SquareSize // 2
        NewShape = ForCanvas.create_rectangle(PosX - offset, PosY - offset, PosX + offset, PosY + offset, fill=color, outline=OutlineColor, activefill=ActiveColor)

    elif Shape == "rectangle":
        Xoffset = RectangleX // 2
        Yoffset = RectangleY // 2

        x1 = PosX - Yoffset
        y1 = PosY - Xoffset
        x2 = PosX + Yoffset
        y2 = PosY + Xoffset
        
        NewShape = ForCanvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=OutlineColor, activefill=ActiveColor)

    elif Shape == "circle":
        offset = CircleSize // 2
        NewShape = ForCanvas.create_oval(PosX - offset, PosY - offset, PosX + offset, PosY + offset, fill=color, outline=OutlineColor, activefill=ActiveColor)

    elif Shape == "oval":
        Xoffset = OvalX // 2
        Yoffset = OvalY // 2

        x1 = PosX - Xoffset
        y1 = PosY - Yoffset
        x2 = PosX + Yoffset
        y2 = PosY + Xoffset
        
        NewShape = ForCanvas.create_oval(x1, y1, x2, y2, fill=color, outline=OutlineColor, activefill=ActiveColor)

    else:
        raise ValueError(f"Could not create custom canvas shape as {Shape} is not a valid option. Did you try checking the allowed shapes (specified in the doctype)?") from None
    
    return NewShape
#endregion

#region Creating Miscellaneous Things in Canvas Function
_CanvasMiscChoices = _literal["Image", "Text", "Window"]
def CreateCanvasMisc(ForCanvas, Type:_CanvasMiscChoices, PosX, PosY, Anchor:_AnchorChoices="center", ImageFile=None, Text="New Canvas Text", font="Arial", FontSize=12, OptionalFontCustom:_ExtraTextCustomChoices="", TextBG=None, TextFG="#000000", WindowObject=None):
    """
    # Creates and returns a miscellaneous element inside a Tkinter Canvas.

    **Necessary parameters:**
        ForCanvas = The tk.Canvas element in which the element will be created on.
        Type = The type of miscellaneous widget that will be created.
            (Options: Image, Text, Window)
        PosX = The horizontal position, in pixels, where the element will be placed.
        PosY = The vertical position, in pixels, where the element will be placed.
    
    **Anchor** = The position of the element that will be anchored.
        (Options: 'e', 's', 'w', 'n', 'se', 'sw', 'ne', 'nw', 'center')

    **Image specific parameters:**
        ImageFile = The linked object/file of the image that will be used. Must be a properly handled tkinter image format or a PhotoImage object.
    
    **Text specific parameters:**
        Text = What text the label will contain.
        font = What custom font the label will use.
        FontSize = The size of the font used.
        OptionalFontCustom = Dictates special font formatting such as bold, italic, or underline.
            (Options: 'bold', 'italic', 'underline', 'overstrike')
        TextBG = The color of the text element's background.
        TextFG = The color of the text element's foreground.

    **Window specific parameters:**
        WindowObject = The object that will be packed within the canvas, it must be a unique element for the Canvas.        
    """
    
    if not isinstance(ForCanvas, tk.Canvas):
        raise ValueError(f"Could not create custom canvas shape as {ForCanvas} is not a valid canvas. Did you try checking the tk.Canvas given?") from None

    Type = Type.lower()
    Anchor = Anchor.lower()

    if Type == "image":
        if ImageFile is not None and isinstance(ImageFile, tk.PhotoImage):
            NewElement = ForCanvas.create_image(PosX, PosY, image=ImageFile, anchor=Anchor)
        
        else:
            raise TypeError("Could not create a custom Canvas image as the value given was not a proper PhotoImage or was empty. Did you try checking the 'ImageFile' parameter?") from None

    elif Type == "text":
        NewElement = ForCanvas.create_text(PosX, PosY, text=Text, font=(font, FontSize, OptionalFontCustom), bg=TextBG if TextBG is not None else "#f0f0f0", fg=TextFG, anchor=Anchor)

    elif Type == "window":
        UsageCheck = WindowObject.winfo_manager()

        if WindowObject is not None and (UsageCheck == "" or UsageCheck == "canvas"):
            NewElement = ForCanvas.create_window(PosX, PosY, window=WindowObject, anchor=Anchor)
        
        elif WindowObject is None:
            raise TypeError("Could not create a customized Canvas Window Object as there wasn't an object provided. Did you try checking 'WindowObject'?") from None

        else:
            raise TypeError("Could not create a customized Canvas Window Object as the provided object is already in use. Did you try checking 'WindowObject'?") from None

    return NewElement
#endregion

#endregion


########################################
# time to mess a bit with PIL and images
########################################
#region (SINGLE USE) Messing with Pillow and Image Rendering
_MirrorImageChoice = _literal["Vertical", "Horizontal"]
def BetterPhotoImage(Image, RotateDegrees=None, RotateChangeSize:_BoolChoices=False, ResizeImageX=None, ResizeImageY=None, MirrorImage:_MirrorImageChoice=None):
    """
    # (SINGLE USE) Renders and modifies a custom image using PIL and returns the modified Tkinter ready image.

    **Required parameters:**
        Image = The file name of the image being used.

    **Image customization parameters:**
        RotateDegrees = The angle, in degrees, where the image will be rotated. **Must be an integer.**
        RotateChangeSize = Wether when rotating an image, the size will maintain for be affected. **Does not work without RotateDegrees.**
        MirrorImage = If the image will be mirrored vertically or horizontally.
            (Options: 'None', 'Vertical', 'Horizontal')

    **Resizing parameters:**
        ResizeImageX = Value, in pixels, what the window's width will be resized to.
        ResizeImageY = Valye, in pixels, what the window's height will be resized to.
    """
    #function to tell wether the image is actually valid
    def is_valid_image_pillow(imgg):
        try:
            with img.open(imgg) as immg:
                immg.verify()
                return True
        except (IOError, SyntaxError):
            return False
    #liar liar pants on fire i guess

    #back to the actual code
    if is_valid_image_pillow(Image):
        NewImage = img.open(Image)

        if NewImage.mode != 'RGBA':
            NewImage = NewImage.convert('RGBA')

        IMGwidth, IMGheight = NewImage.size
        
        if RotateDegrees is not None:
            if not isinstance(RotateDegrees, bool):
                _warn.warn(f"'RotateChangeSize' value was {RotateChangeSize} and as it is not True or False, was defaulted to false.")
                RotateChangeSize = False
            
            if not isinstance(RotateDegrees, int):
                raise TypeError("Could not properly rotate image as the value given was not a proper integer. Did you try ") from None

            NewImage = NewImage.rotate(RotateDegrees, expand=RotateChangeSize, fillcolor=(0, 0, 0, 0))
            IMGwidth, IMGheight = NewImage.size

        if ResizeImageX is not None or ResizeImageY is not None:
            NewImage = NewImage.resize((ResizeImageX if ResizeImageX is not None else IMGwidth, ResizeImageY if ResizeImageY is not None else IMGheight))

        if MirrorImage is not None:
            MirrorImage = MirrorImage.lower()

            if MirrorImage == "vertical":
                NewImage = NewImage.transpose(img.FLIP_TOP_BOTTOM)
            
            elif MirrorImage == "horizontal":
                NewImage = NewImage.transpose(img.FLIP_LEFT_RIGHT)
            
            else:
                raise ValueError("Could not flip image as the given value was not 'vertical' or 'horizontal'. Did you try checking the 'MirrorImage' value?") from None

        NewImage = imgtk.PhotoImage(NewImage)

        return NewImage

    else:
        raise ValueError("Could not create a ImageTk image as the file given was not a proper image file/format. Did you try checking the 'Image' parameter given?") from None
#endregion

#region Class to create PIL images
class BetterImage:
    def __init__(self, FilePath, RotateDegrees=None, RotateChangeSize:_BoolChoices=False, ResizeImageX=None, ResizeImageY=None, MirrorImage:_MirrorImageChoice=None, ConvertPhotoImage:_BoolChoices=False):
        """
        # Renders and modifies a custom image using PIL and creates a BetterImage object.

        **Image customization parameters:**
            RotateDegrees = The angle, in degrees, where the image will be rotated. **Must be an integer.**
            RotateChangeSize = Wether when rotating an image, the size will maintain for be affected. **Does not work without RotateDegrees.**
            MirrorImage = If the image will be mirrored vertically or horizontally.
                (Options: 'None', 'Vertical', 'Horizontal')

        **Resizing parameters:**
            ResizeImageX = Value, in pixels, what the window's width will be resized to.
            ResizeImageY = Valye, in pixels, what the window's height will be resized to.
        """
        # function to tell wether the image is actually valid
        def is_valid_image_pillow(imgg):
            try:
                with img.open(imgg) as immg:
                    immg.verify()
                    return True
            except (IOError, SyntaxError):
                return False
            # liar liar pants on fire i guess

        # back to the actual code
        if is_valid_image_pillow(FilePath):
            self.NewImg = img.open(FilePath)
            self.converted = False
            self.filepath = FilePath

            if self.NewImg.mode != 'RGBA':
                self.NewImg = self.NewImg.convert('RGBA')

            IMGwidth, IMGheight = self.NewImg.size
            
            if RotateDegrees is not None:
                if not isinstance(RotateDegrees, bool):
                    _warn.warn(f"'RotateChangeSize' value was {RotateChangeSize} and as it is not True or False, was defaulted to false.")
                    RotateChangeSize = False
                
                if not isinstance(RotateDegrees, int):
                    raise TypeError("Could not properly rotate image as the value given was not a proper integer. Did you try ") from None

                self.NewImg = self.NewImg.rotate(RotateDegrees, expand=RotateChangeSize, fillcolor=(0, 0, 0, 0))
                IMGwidth, IMGheight = self.NewImg.size

            if ResizeImageX is not None or ResizeImageY is not None:
                self.NewImg = self.NewImg.resize((ResizeImageX if ResizeImageX is not None else IMGwidth, ResizeImageY if ResizeImageY is not None else IMGheight))

            if MirrorImage is not None:
                MirrorImage = MirrorImage.lower()

                if MirrorImage == "vertical":
                    self.NewImg = self.NewImg.transpose(img.FLIP_TOP_BOTTOM)
                
                elif MirrorImage == "horizontal":
                    self.NewImg = self.NewImg.transpose(img.FLIP_LEFT_RIGHT)
                
                else:
                    raise ValueError("Could not flip image as the given value was not 'vertical' or 'horizontal'. Did you try checking the 'MirrorImage' value?") from None
            
            if ConvertPhotoImage and not isinstance(self.NewImg, tk.PhotoImage):
                self.converted = True
                self.NewImg = imgtk.PhotoImage(self.NewImg)
            
            elif ConvertPhotoImage and isinstance(self.NewImg, tk.PhotoImage):
                _warn.warn(f"Did not convert {self.NewImg} to PhotoImage as {self.NewImg} is already a tk.PhotoImage object.")
        else:
            raise ValueError("Could not create a ImageTk image as the file given was not a proper image file/format. Did you try checking the 'Image' parameter given?") from None

    def __repr__(self):
        return f"<BetterImage: File Path: {self.filepath}, Size: {self.NewImg.size if not isinstance(self.NewImg, tk.PhotoImage) else f"{self.NewImg.width()}, {self.NewImg.height()}"}>"

    # now to edit the created EkImage class
    def Configure(self, RotateDegrees=None, RotateChangeSize:_BoolChoices=False, ResizeImageX=None, ResizeImageY=None, MirrorImage:_MirrorImageChoice=None, ConvertPhotoImage:_BoolChoices=False):
        """
        # Configures the already existing ek.BetterImage object.

        **Image customization parameters:**
            RotateDegrees = The angle, in degrees, where the image will be rotated. **Must be an integer.**
            RotateChangeSize = Wether when rotating an image, the size will maintain for be affected. **Does not work without RotateDegrees.**
            MirrorImage = If the image will be mirrored vertically or horizontally.
                (Options: 'None', 'Vertical', 'Horizontal')

        **Resizing parameters:**
            ResizeImageX = Value, in pixels, what the window's width will be resized to.
            ResizeImageY = Valye, in pixels, what the window's height will be resized to.
        """
        if self.converted:
            raise TypeError(f"Could not modify {self} as the image was already converted to a PhotoImage. Did you try checking 'ConvertPhotoImage'?") from None

        if self.NewImg.mode != 'RGBA':
            self.NewImg = self.NewImg.convert('RGBA')

        IMGwidth, IMGheight = self.NewImg.size
        
        if RotateDegrees is not None:
            if not isinstance(RotateDegrees, bool):
                _warn.warn(f"'RotateChangeSize' value was {RotateChangeSize} and as it is not True or False, was defaulted to false.")
                RotateChangeSize = False
            
            if not isinstance(RotateDegrees, int):
                raise TypeError("Could not properly rotate image as the value given was not a proper integer. Did you try ") from None

            self.NewImg = self.NewImg.rotate(RotateDegrees, expand=RotateChangeSize, fillcolor=(0, 0, 0, 0))
            IMGwidth, IMGheight = self.NewImg.size

        if ResizeImageX is not None or ResizeImageY is not None:
            self.NewImg = self.NewImg.resize((ResizeImageX if ResizeImageX is not None else IMGwidth, ResizeImageY if ResizeImageY is not None else IMGheight))

        if MirrorImage is not None:
            MirrorImage = MirrorImage.lower()

            if MirrorImage == "vertical":
                self.NewImg = self.NewImg.transpose(img.FLIP_TOP_BOTTOM)
            
            elif MirrorImage == "horizontal":
                self.NewImg = self.NewImg.transpose(img.FLIP_LEFT_RIGHT)
            
            else:
                raise ValueError("Could not flip image as the given value was not 'vertical' or 'horizontal'. Did you try checking the 'MirrorImage' value?") from None

        if ConvertPhotoImage and not isinstance(self.NewImg, tk.PhotoImage):
                self.NewImg = imgtk.PhotoImage(self.NewImg)
            
        elif ConvertPhotoImage and isinstance(self.NewImg, tk.PhotoImage):
            _warn.warn(f"Did not convert {self.NewImg} to PhotoImage as {self.NewImg} is already a tk.PhotoImage object.")
    
    # gotta add this just incase someone misses the damn "ConvertPhotoImage" parameter in BOTH funcs... 
    def ConvertPhotoImg(self):
        """
        # Turns the ek.BetterImage object into a Tkinter ready image (tk.PhotoImage)
        """

        if not isinstance(self.NewImg, tk.PhotoImage):
                self.NewImg = imgtk.PhotoImage(self.NewImg)
                self.converted = True

        elif isinstance(self.NewImg, tk.PhotoImage):
            _warn.warn(f"Did not convert {self} to a Tkinter ready format is already a Tkinter ready format image.")
    
    Config = Configure
#endregion


##########################################################
# time to work with sounds and pygame (yuck tkinter rival)
##########################################################
#region Class to Create the Main Mixer
class _EasyMixer:
    def __init__(self):
        # aint no bum supposed to see this i'm not gonna make a doctype
        self._mix = _mixer
        self._mixM = _mixermusic

    def InitMixer(self):
        """
        # Initiates the EasySound mixer. Required for audio to play correctly.
            **(Note: Highly recommended to close the mixer before ending your script to prevent memory leaks.)**
            **(Note: Highly recommended to configure the mixer before playing or using any audio.)**
        """
        self._mix.init()
        self.mixerRunning = True

    def PauseMixer(self, Paused:_BoolChoices):
        """
        # Pauses or unpauses the mixer for a better temporary performance increase.
            **Paused** = Wether the mixer will be paused or not. Set to False to unpause mixer.
        """
        if Paused:
            self._mix.pause()
            self.mixerRunning = False
        
        else:
            self._mix.unpause()
            self.mixerRunning = True

    def CloseMixer(self):
        """
        # Exits the EasySound mixer.
            **(Note: Highly recommended to close the mixer before ending your script to prevent memory leaks.)**
        """
        self._mix.quit()
        self.mixerRunning = False
    
    def Configure(self, SamplingRate=44100, BitQuality=16, SurroundChannels=2, OpenChannels=32, Buffer=512, ReservedChannels=8, Volume=1):
        """
        # Restarts the mixer with the new applied settings.

        **Configuration parameters:**
            SamplingRate = The quality (also known as sampling rate) of the audios played.
            BitQuality = The quality, in bit types, of the audio. (Hence why some audios are called '8-bit' and have lower quality.)
            SurroundChannels = The amount of channels that will be used to play the audios. (1 - Mono, 2 - Stereo, 3+ - Surround Sound)
            OpenChannels = The amount of channels open to play different audios at once.
                (Note: Playing more audios than the amount of channel will cause an audio to be overwritten.)
            Buffer = The chunks of an audio that will be buffered to play at once. (Higher numbers use up mr eram but deliver higher quality.)
            ReservedChannels = The amount of channels of the OpenChannels that will be reserved for specialized audios.
            Volume = The volume multiplier of the played audios. (Ranges from 0 - 1.)
        """
        
        # in case the average human puts 16 bits and not -16 because who the hell designed the numbers to be negative
        # no wonder i'm a tkinter fan at heart aint no pygame gonna rot my soul
        if BitQuality > 0:
            BitQuality = -BitQuality

        self._mix.init(frequency=SamplingRate, size=BitQuality, channels=SurroundChannels, buffer=Buffer)

        self._mix.set_num_channels(OpenChannels)
        self._mix.set_reserved(ReservedChannels)
        self.volume = Volume
        self.mixerRunning = True
    Config = Configure

EasyMixer = _EasyMixer()
del _EasyMixer
del _mixer
del _mixermusic
#endregion

#region Class for New Audios
_soundMethodChoices = _literal["Stream", "Play"]
class BetterAudio:
    def __init__(self, FilePath, Method:_soundMethodChoices, FadeIn=0, FadeOut=0, Loops=0, StartFrom=0, IgnoreMP3Warning:_BoolChoices=False):
        """
        # Creates a BetterAudio object that handles and plays audio files.
            **(Note: You must initialize the mixer first before playing an audio)**

        **Required parameters:**
            FilePath = The path leading to the file that will be converted into the object.
            Method = The method that will be used to play that audio file.
                ('Stream' will load the audio from the DISK, saving RAM, 'Play' will store the audio in the RAM for quick playback.)
                (Note: There can only be one audio with the 'Stream' method at once, assigning a new audio with the 'Stream' method will override the previus one.)
        
        **Play parameters:**
            FadeIn = The amount, in milliseconds, where the audio will fade in gradually.
            Loops = The amount of times the audio will loop.
                (To loop infinitely, the value can be 'inf' or -1.)

        **Stream parameters:**
            FadeIn = The amount, in milliseconds, where the audio will fade in gradually.
            FadeOut = The amount, in milliseconds, where the audio will fade out gradually before stopping.
            Loops = The amount of times the audio will loop.
                (To loop infinitely, the value can be 'inf' or -1.)
            StartFrom = The timestamp, in seconds, where the audio will begin streaming.
        """
        
        def _check_mp3(FilePath):
            if not FilePath.lower().endswith(".mp3"):
                return False
            
            try:
                with open(FilePath, "rb") as f:
                    header = f.read(4)
                    if header.startswith(b"ID3") or (header[0:2] == b'\xff\xfb' or header[0:2] == b'\xff\xf3'):
                        return True
            except Exception:
                pass
            return False
        # liar liar pants on fire i guess (audio version)

        self.filepath = FilePath
        Method = Method.title()
        self.method = Method

        if Loops == "inf":
            Loops = -1

        if self.method == "Play":
            try:
                self.NewAudio = EasyMixer._mix.Sound(FilePath)
            except _mixer.error as e:
                raise TypeError(f"Could not load '{FilePath}' as the file might be corrupted, or the format is unsupported. Did you try checking 'FilePath'?\n(Original Error: {e})") from None
            
            self.fadein = FadeIn
            self.loops = Loops
        
        elif self.method == "Stream":
            self.NewAudio = FilePath
            if _check_mp3(self.NewAudio) and IgnoreMP3Warning == False:
                _warn.warn("BetterAudio warning: MP3 files can become unstable when providing an MP3 file and bring unexpected side effects such as uneven playback and seeking.\nTo disable this warning, enable 'IgnoreMP3Warning'.")

            self.fadein = FadeIn
            self.fadeout = FadeOut
            self.loops = Loops
            self.startfrom = StartFrom
        
        else:
            raise ValueError("Could not create a BetterAudio object as method given was not a correct value. Did you try checking 'Method'?") from None
    
    def __repr__(self):
        return f"<BetterAudio: Method (Stream/Play): {self.method}, File Path: {self.filepath}>"
    
    def Inspect(self):
        """
        # Prints the complete details of the BetterAudio object in the console.
        """
        
        print(f"<BetterSound Object>\n\n")
        print(f"File: {self.filepath}\n")
        print(f"Method: {self.method}\n")
        
        _LoopInspect = "Infinite" if self.loops == -1 else self.loops
        print(f"Loops: {_LoopInspect}\n")
        print(f"FadeIn: {self.fadein}ms\n")

        if self.method == "Stream":
            print(f"Start: {self.startfrom}s\n")
            print(f"FadeOut: {self.fadeout}ms\n")

    def Configure(self, FadeIn=0, FadeOut=0, Loops=0, StartFrom=0):
        """
        # Configures an already existing BetterSound object.

        **Play parameters:**
            FadeIn = The amount, in milliseconds, where the audio will fade in gradually.
            Loops = The amount of times the audio will loop.
                (To loop infinitely, the value can be 'inf' or -1.)

        **Stream parameters:**
            FadeIn = The amount, in milliseconds, where the audio will fade in gradually.
            FadeOut = The amount, in milliseconds, where the audio will fade out gradually before stopping.
            Loops = The amount of times the audio will loop.
                (To loop infinitely, the value can be 'inf' or -1.)
            StartFrom = The timestamp, in seconds, where the audio will begin streaming.
        """

        if Loops == "inf":
            Loops = -1

        if self.method == "Play":
            self.fadein = FadeIn
            self.loops = Loops
        
        elif self.method == "Stream":
            self.fadein = FadeIn
            self.fadeout = FadeOut
            self.loops = Loops
            self.startfrom = StartFrom
    Config = Configure

    def PlayAudio(self):
        """
        # Plays the BetterAudio object with it's configurations.
        """
        if self.method == "Play":
            self.NewAudio.play(loops=self.loops, fade_ms=self.fadein)
        
        else:
            EasyMixer._mixM.load(self.filepath)
            EasyMixer._mixM.play(loops=self.loops, start=self.startfrom, fade_ms=self.fadein)

    def Paused(self, Paused:_BoolChoices):
        """
        # Pauses or Unpauses the BetterAudio object.
            **(Note: Only works with audios containing the 'Stream' method.)**
        """
        if Paused:
            EasyMixer._mixM.pause()
        else:
            EasyMixer._mixM.unpause()

    def StopAudio(self):
        """
        # Stops the BetterAudio object with it's confiurations.
        """

        if self.fadeout != 0:
            if self.method == "Play":
                self.NewAudio.fadeout(self.fadeout)
            else:
                EasyMixer._mixM.fadeout(self.fadeout)

        else:
            if self.method == "Play":
                self.NewAudio.stop()
            else:
                EasyMixer._mixM.stop()
#endregion

#region (SINGLE USE) Creating and Playing Pygame (yucky) Audio
def PlayAudio(FilePath, FadeIn=0, Loops=0):
    """
    # A quick function that loads an audio file into the RAM and plays it.
        **(Returns a BetterAudio object with the 'Play' method.)**

    **Parameters:**
        FadeIn = The fade, in milliseconds, the audio will have at the beggining.
        Loops = The amount of times the audio will loop.
            (Note: Type 'inf' or -1 for an unlimited amont of loops.)
    """
    NewAudio = BetterAudio(FilePath, "Play") 
    NewAudio.Configure(FadeIn=FadeIn, Loops=Loops)
    NewAudio.PlayAudio()

    return NewAudio
#endregion

#region (SINGLE USE) Creating and Streaming pygame(yucky) Audio
def StreamAudio(FilePath, StartFrom=0, Loops=0, FadeIn=0, IgnoreMP3Warning:_BoolChoices=False):
    """
    # A quick function that loads an audio file from the DISK and plays it.
        **(Returns a BetterAudio object with the 'Stream' method.)**

    **Parameters:**
        FadeIn = The fade, in milliseconds, the audio will have at the beggining.
        Loops = The amount of times the audio will loop.
            (Note: Type 'inf' or -1 for an unlimited amont of loops.)
    """
    if Loops == "inf":
        Loops = -1
    
    def _check_mp3(FilePath):
            if not FilePath.lower().endswith(".mp3"):
                return False
            
            try:
                with open(FilePath, "rb") as f:
                    header = f.read(4)
                    if header.startswith(b"ID3") or (header[0:2] == b'\xff\xfb' or header[0:2] == b'\xff\xf3'):
                        return True
            except Exception:
                pass
            return False
        # liar liar pants on fire i guess (audio version)

    if _check_mp3(FilePath) and IgnoreMP3Warning == False:
        _warn.warn("BetterAudio warning: MP3 files can become unstable when providing an MP3 file and bring unexpected side effects such as uneven playback and seeking.\nTo disable this warning, enable 'IgnoreMP3Warning'.")

    EasyMixer._mixM.load(FilePath)
    EasyMixer._mixM.play(fade_ms=FadeIn, loops=Loops, start=StartFrom)
    
    return BetterAudio(FilePath, "Stream", FadeIn, Loops=Loops, StartFrom=StartFrom)
#endregion


#############################################
# time to do some extra stuff that's cool too
#############################################
#region Changing Color Theme and Scheme Function
_ColorSchemeChoices = _literal["Nordic", "Moonlight", "Snow", "Slate", "Midnight", "Sandstone", "ModernLight", "Forest"]
def AddColorThemes(TargetElement, ColorTheme:_ColorSchemeChoices):
    """
    # Adds a completely and entirely customized color theme to a given element.

    **TargetElement** = The element(s) that will be applied the customized theme.
        (Can be an individual object, a list, tuple, or dictionary.)

    **ColorTheme** = The custom theme that will be applied to the element.
        (Options: 'Nordic', 'Moonlight', 'Snow', 'Slate', 'Midnight', 'Sandstone', 'ModernLight', 'Graphite')
    """

    ColorSchemes = {
        "Nordic": {
            "bg" : "#2E3440",
            "fg" : "#ECEFF4",
            "surface" : "#3B4252",
            "accent" : "#88C0D0"
        },

        "Moonlight": {
            "bg" : "#191B28",
            "fg" : "#C5CDE4",
            "surface" : "#24283B",
            "accent" : "#7AA2F7"
        },

        "Snow": {
            "bg" : "#F3F3F3",   
            "fg" : "#1A1A1A",  
            "surface" : "#F2F2F2", 
            "accent" : "#005FB8"
        },

        "Slate": {
            "bg" : "#1C1C1D",
            "fg" : "#D1D1D1",
            "surface" : "#373737",
            "accent" : "#78858D"
        },

        "Midnight": {
            "bg" : "#0B0E14",
            "fg" : "#F0F6FC",
            "surface" : "#151B23",
            "accent" : "#376DD8"
        },

        "Sandstone": {
            "bg" : "#FFC569",
            "fg" : "#3C3C3C",
            "surface" : "#FFF891",
            "accent" : "#B18F29"
        },

        "Modernlight": {
            "bg" : "#F9FAFB",
            "fg" : "#111827",
            "surface" : "#E5E7EB",
            "accent" : "#6366F1"
        },

        "Forest" : {
            "bg" : "#032C1C",
            "fg" : "#E6F2ED",
            "surface" : "#025E36",
            "accent" : "#00D18F"
        }
    }

    availiableTargets = [tk.Tk, tk.Toplevel, tk.Frame, tk.LabelFrame, tk.Button, tk.Entry, tk.Text, tk.Checkbutton, tk.Radiobutton, tk.Scale, tk.Label, tk.Listbox, tk.Canvas, tk.Scrollbar, tk.Message]

    WindowElements = [tk.Tk, tk.Toplevel, tk.Frame, tk.LabelFrame]
    TextElements = [tk.Entry, tk.Text]
    ActionElements = [tk.Button, tk.Checkbutton, tk.Radiobutton, tk.Scale]
    DisplayElements = [tk.Label, tk.Listbox, tk.Canvas, tk.Scrollbar, tk.Message]

    availiableSchemes = ["Slate", "Midnight", "Sandstone", "Modernlight", "Forest", "Nordic", "Snow", "Moonlight"]

    ColorTheme = ColorTheme.title()
    if ColorTheme not in availiableSchemes:
        raise TypeError("Could not change element's color theme as the color theme given was not an availiable option. did you try checking 'ColorTheme'?") from None

    usedELements = []
    if isinstance(TargetElement, (list, tuple)):
        usedELements.extend(TargetElement)
    elif isinstance(TargetElement, dict):
        usedELements.extend(TargetElement.values())
    else:
        usedELements.append(TargetElement)

    for i in usedELements:
        ElementType = type(i)

        if ElementType in availiableTargets:
            if ElementType in WindowElements:
                i.configure(bg=ColorSchemes[ColorTheme]["bg"])
            
            elif ElementType in TextElements:
                    i.configure(bg=ColorSchemes[ColorTheme]["surface"], fg=ColorSchemes[ColorTheme]["fg"], insertbackground=ColorSchemes[ColorTheme]["bg"], highlightthickness=1)

            elif ElementType in ActionElements:
                i.configure(bg=ColorSchemes[ColorTheme]["surface"], fg=ColorSchemes[ColorTheme]["fg"], activebackground=ColorSchemes[ColorTheme]["accent"], activeforeground=ColorSchemes[ColorTheme]["surface"])

            elif ElementType in DisplayElements:
                i.configure(bg=ColorSchemes[ColorTheme]["bg"], fg=ColorSchemes[ColorTheme]["fg"])

        else:
            raise TypeError(f"Could not apply a custom color scheme as {TargetElement} was not an availiable element. Did you try checking the 'TargetElement' parameter?") from None
#endregion

#region Adding Helper Function to List all Funcs
def Help():
    """
    # Prints a complete list of all functions and clases and their respective short descriptions.
    """
    __menu_ = f"""
{"-="*40}
<--EasyKinter v{__version__}-->
{"-="*40}
Objects, Classes and Class Specific Functions:
{"-"*5}
BetterImage (CLASS)-> Create a BetterImage object with full support to Tkinter's PhotoImage.
BetterPhotoImage   -> Render an image and return a tk.PhotoImage object.
{"-"*5}
ek.EasyMixer (OBJ) -> Necessary mixer to initiate for mixer settings and audio playback.)
BetterAudio (CLASS)-> Create a BetterAudio object which allow for easy audio control and playback.
PlayAudio          -> Create and return a BetterAudio object and automatically play it.
StreamAudio        -> Create and return a BetterAudio object and automatically stream it.
{"-="*40}
Tkinter (tk) Specific Functions:
{"-"*5}
CreateRoot       -> Create and return a fully created tk.Tk window.
CreateToplevel   -> Create and return a fully created tk.Toplevel window.
BetterConfigure  -> Customize a window (tk.Tk or tk.Toplevel) with added features.
CreateLabel      -> Create, return and pack a fully customizeable tk.Label.
CreateEntry      -> Create, return and pack a fully customizeable tk.Entry.
CreateButton     -> Create, return and pack a fully customizeable tk.Button
CreateMiscInputs -> Create, return and pack one of three miscellaneous inputs. (Text, Spinbox, Scale)
CreateBoolInputs -> Create, return and pack one of three miscellaneous bool inputs. (Checkbutton, Radiobutton, Listbox)
BetterBind       -> A better, and improved .bind() function from Tkinter with added features.
BetterGeometry   -> A better, and improved .geometry() function from Tkinter with added features.
CenterWindow     -> A function to automatically and dynamically center a window in the screen.
{"-="*40}
Canvas (tk.Canvas) Specific Funtions:
{"-"*5}
CreateCanvas       -> Create, return, and pack a tk.Canvas in a window/frame.
CreateCanvasShapes -> Automatically create a shape (Square, Rectangle, Circle, Oval) and place it centered to the coordinates given.
CreateCanvasMisc   -> Automatically create a miscellaneous widget (Image, Text, Window) in the tk.Canvas.
{"-="*40}
Miscellaneous Functions:
AddColorThemes -> Configure any widget given (Handles: List, Tuple, or Dict) to apply one of 8 color themes.
Help           -> Prints this menu message in the console.
"""
    print(__menu_)

#endregion
