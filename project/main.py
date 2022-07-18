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
        x = p.getcolors()
        cores = []
        vertical = []
        horizontal = []
        for c in x:
            cores.append(list(c[1]))
        for cor in cores:
            if cor[0] != 255 and cor[1] != 255 and cor[2] != 255:
                Y, X = np.where(np.all(im == cor, axis=2))
                vertical.append(np.amin(Y))
                horizontal.append(np.amin(X))

        esquerdo = np.amin(horizontal)
        direito = np.amax(horizontal)
        baixo = np.amin(vertical)
        cima = np.amax(vertical)
        print("esquerdo :"+str(esquerdo))
        print("direito :" + str(direito))
        print("baixo :" + str(baixo))
        print("cima :" + str(cima))

        """pim = Image.open(pa)
        x = pim.getcolors()
        cores = []
        for c in x:
            cores.append(list(c[1]))
        cor = cores[0]
        Y, X = np.where(np.all(pim==cor, axis=2))
        print(X, Y)"""







