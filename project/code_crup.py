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
        is_board = True if len(aux[aux != [255, 255, 255]]) > 0 else False
        if is_board and is_water(aux):
            index_esquerda = contColuna
            break
        contColuna += 1

    im_inverse = im[::-1]
    index_baixo = 0
    contador = 0
    for i in im_inverse:
        is_board = True if len(i[i != [255, 255, 255]]) > 0 else False
        if is_board and is_water(i):
            index_baixo = contador
            break
        contador += 1
    if contador > 0:
        index_baixo = len(im) - (index_baixo + 1)

    index_direito = 0
    contColuna = len(im[0]) - 1
    while contColuna >= 0:
        aux = im[:, contColuna]
        is_board = True if len(aux[aux != [255, 255, 255]]) > 0 else False
        if is_board and is_water(aux):
            index_direito = contColuna
            break
        contColuna -= 1

    aux_im = im[index_cima:index_baixo]
    shape = list(np.shape(aux_im))
    shape[1] = len(aux_im[0]) - (index_esquerda + (len(aux_im[0]) - (index_direito+1)))
    new_im = np.zeros(tuple(shape), dtype='u1')
    i = 0

    for a in aux_im:
        new_im[i] = aux_im[i, index_esquerda:(index_direito+1)]
        i += 1


    image = Image.fromarray(new_im, mode="RGB")

    return image

def is_water(matriz):
    return np.any(matriz <= 230)

