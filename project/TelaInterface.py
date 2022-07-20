from tkinter import *
import tkinter.filedialog as fd


def open_tela():
    janela = Tk()
    janela.geometry("400x400")
    put_title(janela)

    put_buttleCuple(janela)

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

def put_buttleCuple(janela):
    photo = PhotoImage(file=r'C:\Users\Micro\OneDrive\Documentos\Git\image-cropping\project\IMAGENS Program\buttonImage.png')
    photo = photo.subsample(5,5)
    bt = Button(janela, image=photo)
    bt.grid(column=2,row=2)
    """photo = PhotoImage(file=r'C:\Gfg\circle.png')
    Button(janela, text='Click Me !', image=photo).pack(side=TOP)
    quantidade = 50
    bt = Button(janela, )"""