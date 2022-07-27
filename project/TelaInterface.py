from tkinter import *
import tkinter.filedialog as fd
import os
from tkinter import messagebox
import code_crup


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
        self.botao_cortar = Button(self.janela, image=photo, command=self.cortar)
        self.botao_cortar.grid(column=1, row=12)
        self.botao_cortar.photo = photo
        self.espacamento.append(put_buttleCuple(self.janela))
        self.botao_abrir_pastaOrigem = put_buttlesFiles_create(self.janela, self.comando_abrir_pasta_cima,
                                                               linha=8, coluna=20,
                                                               arquivo_path=r"IMAGENS Program\buttonImage.png")
        self.espacamento = put_buttlesFiles(self.janela, linha=8, coluna=20)
        self.botao_abrir_pastaDestino = put_buttlesFiles_create(self.janela, self.comando_abrir_pasta_baixo,
                                                                linha=10, coluna=20,
                                                               arquivo_path=r"IMAGENS Program\buttonImage.png")
        self.espacamento = put_buttlesFiles(self.janela, linha=10, coluna=20)
        self.text_btPasta_cima = "PASTA DE IMAGENS PARA CORTAR"
        self.text_btPasta_baixo = "PASTA DE DESTINO DAS IMAGENS CORTADAS"
        self.label_caminho_origem = Label(self.janela, text=self.text_btPasta_cima)
        self.label_caminho_origem.grid(column=1,row=8, columnspan=5)

        self.label_caminho_destino = Label(self.janela, text=self.text_btPasta_baixo)
        self.label_caminho_destino.grid(column=1, row=10, columnspan=5)

        mainloop()


    def comando_abrir_pasta_cima(self):
        folder = fd.askdirectory(parent=self.janela, initialdir="/",
                                 title='PLEASE SELECT THE SOURCE DIRECTORY OF THE IMAGES')
        if (os.path.isdir(folder)):
            self.text_btPasta_cima = folder
            self.label_caminho_origem['text'] = self.get_pathText_formatado(self.text_btPasta_cima)
        else:
            messagebox.showerror("SELECIONE UMA PASTA", "DIRETÓRIO NÃO EXISTE")


    def comando_abrir_pasta_baixo(self):
        folder = fd.askdirectory(parent=self.janela, initialdir="/",
                                 title='PLEASE SELECT THE SOURCE DIRECTORY OF THE IMAGES')
        if (os.path.isdir(folder)):
            self.text_btPasta_baixo = folder
            self.label_caminho_destino['text'] = self.get_pathText_formatado(self.text_btPasta_baixo)
        else:
            messagebox.showerror("SELECIONE UMA PASTA", "DIRETÓRIO NÃO EXISTE")


    def get_pathText_formatado(self, text):
        if len(text)>61:
            text = text[0:53]
            text = text + "..."
        return text


    def cortar(self):
        ok = False
        if os.path.isdir(self.text_btPasta_baixo):
            ok = True
        else:
            messagebox.showerror("ERRO NO CORTE", "DIRETÓRIO DE DESTINO VAZIU OU INCORRETO")

        if ok and os.path.isdir(self.text_btPasta_cima):
            code_crup.save_images_cutted_in_path(self.text_btPasta_cima, self.text_btPasta_baixo)
        elif ok:
            messagebox.showerror("ERRO NO CORTE", "DIRETÓRIO DE ORIGEM VAZIU OU INCORRETO")
            ok = False

        if ok:
            messagebox.showinfo("IMAGENS CORTADAS")





def teste_mygui():
    mg = MyGui()




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

