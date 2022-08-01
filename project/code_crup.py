import tkinter
import tkinter.filedialog as fd
import os
from PIL import Image
import numpy as np

#TRATAR CAMINHO NO RECEBIMENTO
def save_images_cutted_in_path(folder_origem, folder_destino):
    for file in os.listdir(folder_origem):
        if file.endswith(".png") or file.endswith(".jpg"):
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
    im_new = []
    im_new = np.array(im_new)
    contador = 0
    index_cima = 0
    index_esquerda = 0
    for i in im:
        is_board = True if len(i[i != [255, 255, 255]]) > 0 else False and is_water(i)
        if is_board:
            index_cima = contador
            break
        contador += 1

    contColuna = 0
    while contColuna < len(im[0]):
        aux = im[:, contColuna]
        if True if len(aux[aux != [255, 255, 255]]) > 0 else False and is_water(aux):
            index_esquerda = contColuna
            break
        contColuna += 1

    im_inverse = im[::-1]
    index_baixo = 0
    contador = 0
    for i in im_inverse:
        is_board = True if len(i[i != [255, 255, 255]]) > 0 else False and is_water(i)
        if is_board:
            index_baixo = contador
            break
        contador += 1
    if contador > 0:
        index_baixo = len(im) - (index_baixo + 1)

    print(index_cima)
    print(index_esquerda)
    print(index_baixo)
    print("dsfdsf")
    x = image.getcolors(image.size[0]*image.size[1])
    return cutting(colors=x, im=im, im_open=image)

def is_water(matriz):
    return np.any(matriz <= 200)

def cutting(colors, im, im_open):
    cores = []
    for c in colors:
        cor_atual = list(c[1])
        if cor_atual[0] != 255 and cor_atual[1] != 255 and cor_atual[2] != 255:
            cores.append(list(c[1]))
    lados = [[], [], [], []]
    q = 0
    for cor in cores:
        q += 1
        X = 0
        Y = 0
        #Y, X = np.where(np.all(im == cor, axis=2))
        lados[0].append(np.amin(X))
        lados[1].append(np.amax(X))
        lados[2].append(np.amax(Y))
        lados[3].append(np.amin(Y))
        print(q)
    print(str(len(im))+" im   /   "+str(len(cores)))
    esquerdo = np.amin(lados[0])
    direito = np.amax(lados[1])
    baixo = np.amin(lados[3])
    cima = np.amax(lados[2])
    esquerdo = 0
    direito = 2000
    baixo = 2000
    cima = 864
    return im_open.crop((esquerdo - 10, baixo - 10, direito + 10, cima + 10))