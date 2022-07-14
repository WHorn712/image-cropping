import tkinter
import tkinter.filedialog as fd
import os
from PIL import Image

root = tkinter.Tk()
folder = fd.askdirectory(parent=root,initialdir="/",title='please select a directory')
for file in os.listdir(folder):
    if file.endswith(".png"):
        pa = folder+"/"+file
        im = Image.open(pa)
        x = im.getcolors()
        y = im.getbbox()
        print(x)
        print(y)


