import tkinter
import tkinter.filedialog as fd
import os
from PIL import Image
import numpy as np

#TRATAR CAMINHO NO RECEBIMENTO
def save_images_cutted_in_path(folder_origem, folder_destino):
    for file in os.listdir(folder_origem):
        if file.endswith(".png"):
            pa = folder_origem + "/" + file
            p = Image.open(pa)
            imagem_cortada = get_image_cuted(p)
            text_path = folder_destino+"/imagem"+str(get_quantidade_arquivos_in_path(folder_destino))+".png"
            imagem_cortada.save(text_path)


def get_quantidade_arquivos_in_path(folder):
    quantidade = 0
    for file in os.listdir(folder):
        if file.endswith(".png") or file.endswith(".jpg"):
            quantidade += 1
    return quantidade


def get_image_cuted(image):
    pim = image.convert('RGB')
    im = np.array(pim)
    x = image.getcolors()
    return cutting(colors=x, im=im, im_open=image)


def cutting(colors, im, im_open):
    cores = []
    for c in colors:
        cores.append(list(c[1]))
    lados = [[], [], [], []]
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
    return im_open.crop((esquerdo - 10, baixo - 10, direito + 10, cima + 10))