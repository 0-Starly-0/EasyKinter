import os as _os
import sys as _sys
from pathlib import Path as _Path

BIN_DIR = _Path(__file__).parent.joinpath("bin").resolve()
if _sys.platform == "win32" and BIN_DIR.exists():
    _os.add_dll_directory(str(BIN_DIR.resolve()))
    _os.environ["PATH"] = str(BIN_DIR) + _os.pathsep + _os.environ["PATH"]

from .EasyKinter import *

import tkinter
tk = tkinter

from PIL import Image, ImageTk
PILimg = Image
PILimgtk = ImageTk
