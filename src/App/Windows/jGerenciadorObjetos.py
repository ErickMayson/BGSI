from tkinter import *
from tkinter import ttk


class jGerenciadorObjetos:

    
    def __init__(self):
        janela = Tk()
        janela.title("Gerenciador de Objetos")

        # A coluna 0 vai ter peso 1;
        # Uma coluna 1 com peso 2 ocuparia o dobro do espaço horizontal que a coluna 0;
        janela.columnconfigure(0, weight=1, minsize=1)
        janela.rowconfigure(0, weight=1, minsize=1)


        mainframe = ttk.Frame(janela, padding = "2 2 2 2")
        # column = 0 faz com que o widget seja posicionado na primeira coluna da janela. columnspan = 3 faz com que o widget ocupe 3 colunas.
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # Posicionamos o mainframe na janela e definimos que ele se expandirá em todas as direções.
        # O TK gerencia o número de colunas e linhas a medida da necessidade.

        input = ("Coordenada X Min", "Coordenada Y Min", "Coordenada X Max", "Coordenada Y Max")
        for i in range(0,3,2):
            ttk.Label(mainframe, text = input[i]).grid(column = 0, row = i, sticky = (W, E))
            ttk.Spinbox(mainframe, to = 100, width = 5).grid(column = 1, row = i, sticky = (W, E))
            ttk.Label(mainframe, text = input[i+1]).grid(column = 0, row = i+1, sticky = (W, E))
            ttk.Spinbox(mainframe, to = 100, width = 5).grid(column = 1, row = i + 1, sticky = (W, E))
        ttk.Button(text="Criar").grid(column=2, row=2)
            
        janela.mainloop()

    def executar():
        print("Executando...")
    #class jGerenciadorObjetos: