from tkinter import *
import tkinter.filedialog as fd
import os
from tkinter import messagebox


class MyGui:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("400x400")
        self.janela.title("CORTAR IMAGEM")
        self.texto_titulo_janela = Label(self.janela, text="CORTAR IMAGEM", font=("Arial", 15))
        self.texto_titulo_janela.grid(column=5, row=1)
        ##Descrição da variavel espacamento abaixo
        ##lista de tupla do espaçamento em cada objeto da tela
        ##1ºelemento-descrição(string) / 2ºelemento-coluna(lista de labels) / 3ºelemento-linha(lista de labels)
        self.espacamento = []
        self.espacamento.append(put_title(self.janela))
        photo = PhotoImage(
            file=r'IMAGENS Program\tizoura.png')
        photo = photo.subsample(3, 3)
        self.botao_cortar = Button(self.janela, image=photo)
        self.botao_cortar.grid(column=1, row=12)
        self.botao_cortar.photo = photo
        self.espacamento.append(put_buttleCuple(self.janela))
        self.botao_abrir_pastaOrigem = put_buttlesFiles_create(self.janela, comando_bt1, linha=8, coluna=20,
                                                               arquivo_path=r"IMAGENS Program\buttonImage.png")
        self.espacamento = put_buttlesFiles(self.janela, linha=8, coluna=20)
        self.botao_abrir_pastaDestino = put_buttlesFiles_create(self.janela, self.comando_abrir_pasta, linha=10, coluna=20,
                                                               arquivo_path=r"IMAGENS Program\buttonImage.png")
        self.espacamento = put_buttlesFiles(self.janela, linha=10, coluna=20)
        self.text_btPasta_cima = "PASTA DE IMAGENS PARA CORTAR"
        self.text_btPasta_baixo = "PASTA DE DESTINO DAS IMAGENS CORTADAS"
        self.text_caminho_origem = Label(self.janela, text=self.text_btPasta_cima)
        self.text_caminho_origem.grid(column=1,row=8, columnspan=5)

        self.text_caminho_destino = Label(self.janela, text=self.text_btPasta_baixo)
        self.text_caminho_destino.grid(column=1, row=10, columnspan=5)

        mainloop()

    def comando_abrir_pasta(self):
        folder = fd.askdirectory(parent=self.janela, initialdir="/",
                                 title='PLEASE SELECT THE SOURCE DIRECTORY OF THE IMAGES')
        if (os.path.isdir(folder)):
            print("")
        else:
            messagebox("DIRETÓRIO NÃO EXISTE")

def teste_mygui():
    mg = MyGui()

def open_tela():
    janela = Tk()
    janela.geometry("400x400")
    put_title(janela)

    put_buttleCuple(janela)

    put_buttlesFiles(janela, comando_bt1, linha=8, coluna=20, arquivo_path=r"IMAGENS Program\buttonImage.png")

    put_buttlesFiles(janela, comando_bt1, linha=10, coluna=20, arquivo_path=r"IMAGENS Program\buttonImage.png")

    tv = ""
    if len(tv)>61:
        tv = tv[0:58]
        tv = tv + "..."

    imagem_caminho_text = Label(janela, text="PASTA DE IMAGENS PARA CORTAR")
    imagem_caminho_text.grid(column=1,row=8, columnspan=5)

    imagem_caminho_text = Label(janela, text="PASTA DE DESTINO")
    imagem_caminho_text.grid(column=1, row=10, columnspan=5)


    janela.mainloop()

def put_title(janela):
    quantidade = 5

    listaLabels = []
    i = 0
    while i < quantidade:
        listaLabels.append(Label(janela, text=""))
        listaLabels[i].grid(column=i + 1, row=1)
        i += 1
    linhas = []
    return ("titulo", listaLabels, linhas)

def put_buttleCuple(janela):
    quantidade = 12

    listaLabels = []
    i = 0
    while i < quantidade:
        listaLabels.append(Label(janela, text=""))
        listaLabels[i].grid(column=1, row=i+1)
        i += 1
    colunas = []
    return ("botão_cortar", colunas, listaLabels)



def put_buttlesFiles_create(janela, comando, linha = 10, coluna=10, arquivo_path=r"IMAGENS Program\tizoura.png"):
    photo = PhotoImage(
        file=arquivo_path)
    photo = photo.subsample(6, 6)
    bt = Button(janela, image=photo, command=comando)
    bt.grid(column=coluna, row=linha)
    bt.photo = photo

    return bt


def put_buttlesFiles(janela, linha = 10, coluna=10):

    listaLabels2 = []
    i = 0
    while i < coluna:
        listaLabels2.append(Label(janela, text=""))
        listaLabels2[i].grid(column=coluna+1, row=1)
        i += 1

    listaLabels = []
    i = 0
    while i < linha:
        listaLabels.append(Label(janela, text=""))
        listaLabels[i].grid(column=1, row=i + 1)
        i += 1

    return ("botões de definir caminho das pastas", listaLabels2, listaLabels)

def comando_bt1():
    print("teste comando")