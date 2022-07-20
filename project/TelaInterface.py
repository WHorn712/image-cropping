from tkinter import *
import tkinter.filedialog as fd


def open_tela():
    janela = Tk()
    janela.geometry("400x400")
    put_title(janela)


    bt = Button(janela, text="aperte")
    bt.grid(column=2, row=2)

    janela.mainloop()

def put_title(janela):
    janela.title("CORTAR IMAGEM")

    quantidade = 12
    texto = Label(janela, text="CORTAR IMAGEM")
    texto.config(font=("Arial", 15))
    texto.grid(column=quantidade, row=1)

    listaLabels = []
    i = 0
    while i < quantidade:
        listaLabels.append(Label(janela, text=""))
        listaLabels[i].grid(column=i + 1, row=1)
        i += 1