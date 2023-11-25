# Importa toda a biblioteca do tk para o programa.   
from tkinter import *
# Importa o submódulo ttk para o programa, contem funcionalidades mais atualizadas.
from tkinter import ttk

class janelaControladorCor:
    # Método construtor da classe. É obrigatório passar self como argumento
    def __init__(self):
        #self.mudarCor
        
        # Cria uma jenela que representa a classe.
        self.janela = Tk()
        self.janela.title("Controlador de cor")

        # A coluna 0 vai ter peso 1;
        # Uma coluna 1 com peso 2 ocuparia o dobro do espaço horizontal que a coluna 0;
        self.janela.columnconfigure(0, weight=1, minsize=1)
        self.janela.rowconfigure(0, weight=1, minsize=1)

        # Widget que conterá o conteúdo da interface
        mainframe = ttk.Frame(self.janela, padding = "2 2 2 2")
        # column = 0 faz com que o widget seja posicionado na primeira coluna da janela. columnspan = 3 faz com que o widget ocupe 3 colunas.
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # Posicionamos o mainframe na janela e definimos que ele se expandirá em todas as direções.

        inputs = ("Red", "Green", "Blue")
        i = 0
        for cor in inputs:
            ttk.Label(master= mainframe, text = cor).grid(column=0, row=i)
            ttk.Scale(master= mainframe, orient="horizontal", to= 255).grid(column=1, row=i)
            i += 1
        
        ttk.Button(text="Alterar").grid(column=2, row=2)
        # Inicia o loop principal do Tkinter, que mantém a janela aberta e escuta eventos
        

    def spawn(self):
        self.janela.update()
        self.janela.update_idletasks()
        self.janela.mainloop()


    #def setFunc(self, func):
    #    self.mudarCor=func
         