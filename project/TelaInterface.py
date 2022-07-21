from tkinter import *
import tkinter.filedialog as fd


def open_tela():
    janela = Tk()
    janela.geometry("400x400")
    put_title(janela)

    put_buttleCuple(janela)

    put_buttlesFiles(janela, linha=8, coluna=20, arquivo_path=r"IMAGENS Program\buttonImage.png")

    put_buttlesFiles(janela, linha=10, coluna=20, arquivo_path=r"IMAGENS Program\buttonImage.png")

    """photo = PhotoImage(
        file=r'IMAGENS Program\labelcomparar.png')
    photo = photo.subsample(3, 3)"""
    tv = r"C:\Users\Micro\OneDrive\Área de Trabalho\Nova pasta          abc"
    t = ""
    if len(tv)>61:
        sobra = len(tv) - 61
        c = 1
        while c<=sobra:
            print(c)
            c += 1
        #tv = tv.replace(, '...')
    else:
        t = tv

    print(tv)
    imagem_caminho_text = Label(janela, text=t)
    imagem_caminho_text.grid(column=1,row=8, columnspan=5)
    print(len(t))

    imagem_caminho_text = Label(janela, text=r"C:\Users\Micro\OneDrive\Área de Trabalho\Nova pasta")
    imagem_caminho_text.grid(column=1, row=10, columnspan=5)


    janela.mainloop()

def put_title(janela):
    janela.title("CORTAR IMAGEM")

    quantidade = 5
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
    quantidade = 12

    photo = PhotoImage(
        file=r'IMAGENS Program\tizoura.png')
    photo = photo.subsample(3,3)
    bt = Button(janela, image=photo)
    bt.grid(column=1,row=quantidade)
    bt.photo = photo

    listaLabels = []
    i = 0
    while i < quantidade:
        listaLabels.append(Label(janela, text=""))
        listaLabels[i].grid(column=1, row=i+1)
        i += 1

def put_buttlesFiles(janela, linha = 10, coluna=10, arquivo_path=r"IMAGENS Program\tizoura.png"):
    photo = PhotoImage(
        file=arquivo_path)
    photo = photo.subsample(6, 6)
    bt = Button(janela, image=photo)
    bt.grid(column=coluna, row=linha)
    bt.photo = photo

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