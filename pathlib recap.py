# https://docs.python.org/3/library/pathlib.html
# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

import os
from pathlib import Path, WindowsPath

# How to get the Current Working Directory
cwd = Path.cwd()
print(cwd)

# Change the working directory
new_wd = cwd / "Input"
os.chdir(new_wd)
Path.cwd()
os.chdir(cwd)
Path.cwd()

# How to concatenate paths
filepath = cwd / "Input/test_data.txt"
print(filepath)

# How to work with paths
filepath = Path("Input/test_data.txt")
print(filepath)
print(filepath.read_text())
print(filepath.name)
print(filepath.suffix)
print(filepath.stem)
filepath.exists()

# Using Window backslash
filepathWin = WindowsPath("Input\test_data.txt")
print(filepath)
print(filepath.read_text())
print(filepath.name)
print(filepath.suffix)
print(filepath.stem)
filepath.exists()
