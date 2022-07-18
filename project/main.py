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
        lados = [[], [], [], []]
        for c in x:
            cores.append(list(c[1]))
        for cor in cores:
            if cor[0] != 255 and cor[1] != 255 and cor[2] != 255:
                Y, X = np.where(np.all(im == cor, axis=2))
                lados[0].append(np.amin(X))
                lados[1].append(np.amax(X))
                lados[2].append(np.amax(Y))
                lados[3].append(np.amin(Y))

        esquerdo = np.amin(lados[0])
        direito = np.amax(lados[1])
        baixo = np.amin(lados[3])
        cima = np.amax(lados[2])
        print("esquerdo :"+str(esquerdo))
        print("direito :" + str(direito))
        print("baixo :" + str(baixo))
        print("cima :" + str(cima))
        cropimage = p.crop((esquerdo-10, baixo-10, direito+10, cima+10))
        cropimage.show()







