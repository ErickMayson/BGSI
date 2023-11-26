from tkinter import *
from tkinter import ttk

class jAdicionarObjeto:
    
    def __init__(self):
        janelaPrincipal = Tk()
        janelaPrincipal.title("Adicionar Objeto")
        janelaPrincipal.geometry("200x200")

        mainframe = ttk.Frame(janelaPrincipal, padding = "2 2 2 2")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        janelaPrincipal.mainloop()