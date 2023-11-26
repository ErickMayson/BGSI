from tkinter import *
from tkinter import ttk
from .jAdicionarObjeto import jAdicionarObjeto

class jPrincipal:

    def __init__(self):
        janelaPrincipal = Tk()
        janelaPrincipal.title("Sistema Gráfico Interativo Básico")
        janelaPrincipal.geometry("320x800")
        janelaPrincipal.columnconfigure(0, weight=1, minsize=1)
        janelaPrincipal.rowconfigure(0, weight=1, minsize=1)

        mainframe = ttk.Frame(janelaPrincipal, padding = "2 2 2 2")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Button(mainframe, text="+", width=2, command= lambda: self.abrirJanela("jAdicionarObjeto")).grid(column=10, row=3, sticky=(N, E))


        janelaPrincipal.mainloop()

    def abrirJanela(self, janela):
        if janela == "jAdicionarObjeto":
            print("barata")
            jAdicionarObjeto()
            
