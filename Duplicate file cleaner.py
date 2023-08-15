from tkinter import Tk
from tkinter.filedialog import askdirectory

import os

import hashlib

Tk().withdraw()  #don't want a full GUI, so keep the root window from appearing
path = askdirectory(title= "Select a folder")
print(path)

walker = os.walk(path)

uniqueFiles = dict()

for folder, sub_folder, files in walker:
    for file in files:
        filepath = os.path.join(folder, file)
        filehash = hashlib.md5(open(filepath, "rb").read()).hexdigest()

        if filehash in uniqueFiles:
            os.remove(filepath)
            print(f"{filepath} has been deleted")
        else:
            uniqueFiles[filehash] = path    