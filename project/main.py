import tkinter
import tkinter.filedialog as fd
import os
from PIL import Image
import numpy as np

root = tkinter.Tk()
folder = fd.askdirectory(parent=root,initialdir="/",title='please select a directory')
for file in os.listdir(folder):
    if file.endswith(".png"):
        pa = folder+"/"+file
        im = Image.open(pa)
        x = im.getcolors(im.size[0]*im.size[1])
        y = im.getbbox()
        c = 0
        cor = ()
        print(type(cor))
        for i in x:
            if c == 0:
                c = 1
            elif c == 1:
                c = 2






