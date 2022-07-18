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
        p = Image.open(pa)
        pim = p.convert('RGB')
        im = np.array(pim)
        print(len(im))
        x = p.getcolors()
        cores = []
        for c in x:
            cores.append(list(c[1]))
        cor = cores[0]
        Y, X = np.where(np.all(im == cor, axis=2))

        print(type(X))

        """pim = Image.open(pa)
        x = pim.getcolors()
        cores = []
        for c in x:
            cores.append(list(c[1]))
        cor = cores[0]
        Y, X = np.where(np.all(pim==cor, axis=2))
        print(X, Y)"""







