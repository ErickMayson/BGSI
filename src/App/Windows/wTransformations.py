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
        mainWindow.title(entityName)
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
        mainWindow.focus_set()
        ttk.Button(colorFrame, text="Aplicar", command= self.applyColor).grid(row=1, column=1, pady=0, padx=40, sticky=(E, S), )
        
        notebook.add(colorFrame, text='Cor')
        
            # Frame de Translação
        translationFrame = ttk.Frame(notebook, padding = "2 2 2 2")
        translationFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        notebook.add(translationFrame, text='Translação')
        
        inputLabelX = ttk.Label(translationFrame, text="Delta X")
        inputLabelX.grid(row=0, column=0, pady=5, padx=5)
        inputLabelY = ttk.Label(translationFrame, text="Delta Y")
        inputLabelY.grid(row=1, column=0, pady=5, padx=5)

        self.xEntry = ttk.Entry(translationFrame)
        self.xEntry.grid(row=0, column=1, pady=5, padx=5)
        self.yEntry = ttk.Entry(translationFrame)
        self.yEntry.grid(row=1, column=1, pady=5, padx=5)
        
        ttk.Button(translationFrame, text="Mover objeto", command=self.moveObject).grid(row=3, column=1, pady=10, padx=10, sticky=(S, W),)
        mainWindow.focus_set()
        
        # Frame de escalonamento
        scalingFrame = ttk.Frame(notebook, padding = "2 2 2 2")
        scalingFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        notebook.add(scalingFrame, text='Escalonamento')
        
        scalingLabel = ttk.Label(scalingFrame, text="X")
        scalingLabel.grid(row=0, column=0, pady=5, padx=5)
        
        self.scalingInputX = ttk.Entry(scalingFrame)
        self.scalingInputX.grid(row=0, column=1, pady=5, padx=5)
        
        scalingLabel = ttk.Label(scalingFrame, text="Y")
        scalingLabel.grid(row=1, column=0, pady=5, padx=5)

        self.scalingInputY = ttk.Entry(scalingFrame)
        self.scalingInputY.grid(row=1, column=1, pady=5, padx=5)
        
        ttk.Button(scalingFrame, text="Escalonar objeto", command=self.scaleObject).grid(row=3, column=1, pady=10, padx=10, sticky=(S, W),)
        mainWindow.focus_set()

        mainWindow.mainloop()


    def applyColor(self):
        entidade = self.gerenciadorSINGLETON.findEntidadeByName(self.entityName)
        #print(self.color)
        #A  cor é uma tupla, o primeiro elemento é o valor em RGB, o segundo é o valor em hexadecimal   
        if entidade is not None:
            entidade.corPreenchimento = self.color[0]
            self.gerenciadorSINGLETON.draw()
            
        else:
            messagebox.showerror("Erro", "Isso não devia acontecer, a entidade " + self.entityName + " não foi encontrada.")

    def chooseColor(self, colorSquare):
        self.color = colorchooser.askcolor()
        colorSquare.config(bg=self.color[1])

    def moveObject(self):
        translationX = self.xEntry.get()
        translationY = self.yEntry.get()
        
        translationInput = (int(translationX), int(translationY))

        entidade = self.gerenciadorSINGLETON.findEntidadeByName(self.entityName)
        if entidade is not None:
            entidade.translacao = translationInput
            #print(entidade.translacao)
            # Not redrawing?
            self.gerenciadorSINGLETON.draw()
            # Reseta a translação do objeto para 0, para não continuar somando.
            entidade.translacao = (0,0)
            
            
    def scaleObject(self):
        scalingFactorX = float(self.scalingInputX.get())
        scalingFactorY = float(self.scalingInputY.get())
        

        entidade = self.gerenciadorSINGLETON.findEntidadeByName(self.entityName)
        if entidade is not None:
            entidade.escala = (scalingFactorX, scalingFactorY)
            #print(entidade.escala)
            # Not redrawing?
            self.gerenciadorSINGLETON.draw()
            # Reseta a escala do objeto para 1, para não continuar escalando.
            entidade.escala = (1, 1)
            
        else:
            messagebox.showerror("Erro", "Isso não devia acontecer, a entidade " + self.entityName + " não foi encontrada.")
            
    def rotateObject(self):
        return print("Placeholder for Rotate function")
        
#wTransformations(Tk())