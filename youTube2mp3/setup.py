# setup.py
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'C:/Users/MHofffmann/AppData/Local/Programs/Python/Python36/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/MHofffmann/AppData/Local/Programs/Python/Python36/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages=["os", "youTube2mp3", "pafy", "threading"],
    excludes=[],
    include_files=['C:/Users/MHofffmann/AppData/Local/Programs/Python/Python36/DLLs/tcl86t.dll',
                   'C:/Users/MHofffmann/AppData/Local/Programs/Python/Python36/DLLs/tk86t.dll'],
    build_exe="..\\build"
)

import sys

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('mainWindow.py', base=None, targetName="Youtube2mp3.exe")
]

setup(name='editor',
      version='1.0',
      description='',
      options=dict(build_exe=buildOptions),
      executables=executables)
