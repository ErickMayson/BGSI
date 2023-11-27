from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class wTransformations:
    def __init__(self, master, entityName = "",gerenciador = None, atualizarTreeView = None):
        #Configurações Iniciais
        mainWindow = Toplevel(master)
        mainWindow.title("Transformar Objeto")
        mainWindow.columnconfigure(0, weight=1)
        mainWindow.rowconfigure(0, weight=1)

        self.entityName = entityName

        self.gerenciadorSINGLETON = gerenciador

        #A  cor é uma tupla, o primeiro elemento é o valor em RGB, o segundo é o valor em hexadecimal   
        self.color = ((255, 255, 255), '#FFFFFF')

        # Notebook
        notebook = ttk.Notebook(mainWindow)
        notebook.grid(row=0, column=0, sticky=(N, W, E, S))

            # Frame de Cor
        colorFrame = ttk.Frame(notebook, padding = "2 2 2 2")
        colorFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        colorFrame.columnconfigure(0, weight=1)
        colorFrame.rowconfigure(0, weight=1)

            # Quadrado de cor
        colorSquare = Canvas(colorFrame, width=50, height=50, bg=self.color[1])
        colorSquare.grid(row=0, column=1, pady=10, padx=50, sticky=(E, S))
        
        ttk.Button(colorFrame, text="Escolher cor", command= lambda: self.chooseColor(colorSquare)).grid(row=0, column=0, pady=10, padx=10, sticky=(S, W),)

        ttk.Button(colorFrame, text="Aplicar", command= self.applyColor).grid(row=1, column=1, pady=0, padx=40, sticky=(E, S), )
        
        notebook.add(colorFrame, text='Cor')
        
            # Frame de Translação
        translationFrame = ttk.Frame(notebook, padding = "2 2 2 2")
        translationFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        notebook.add(translationFrame, text='Translação')



        mainWindow.mainloop()


    def applyColor(self):
        entidade = self.gerenciadorSINGLETON.findEntidadeByName(self.entityName)
        print(self.color)
        #A  cor é uma tupla, o primeiro elemento é o valor em RGB, o segundo é o valor em hexadecimal   
        if entidade is not None:
            entidade.corPreenchimento = self.color[0]
            self.gerenciadorSINGLETON.draw()
            
        else:
            messagebox.showerror("Erro", "Isso não devia acontecer, a entidade " + self.entityName + " não foi encontrada.")

    def chooseColor(self, colorSquare):
        self.color = colorchooser.askcolor()
        colorSquare.config(bg=self.color[1])

#wTransformations(Tk())