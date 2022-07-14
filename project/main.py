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
        x = im.getcolors(im.size[0]*im.size[1])
        y = im.getbbox()
        c = 0
        for i in x:
            if c == 0:
                c = 1
        cores = []
        for cor_rgb in im.getdata():
            if cor_rgb not in cores:
                cores.append(cor_rgb)
        print(cores)



