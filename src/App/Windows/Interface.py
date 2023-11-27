import tkinter as tk
from tkinter import ttk
import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from App.Classes.Entidade import *
from .wCreateObject import wCreateObject

#print(sys.path)

class Interface:
    
    def __init__(self, master, gerenciadorSINGLETON):
        
        self.gerenciadorSINGLETON = gerenciadorSINGLETON

        with open("palette.json", "r") as json_file:
            stylingData = json.load(json_file)
            
        self.backgroundColor =  stylingData["palette"]["Main"]
        self.secondaryColor = stylingData["palette"]["Secondary"]
        self.tertiaryColor = stylingData["palette"]["Tertiary"]
        self.boldFont = stylingData["palette"]["boldFont"]
        self.normalFont = stylingData["palette"]["normalFont"]
        self.fontColor = stylingData["palette"]["fontColor"]
            
        self.master = master
        self.master.title("Object Generator")
        self.master.geometry("800x800")
        self.master.configure(bg=self.backgroundColor)
        
        #Titulo da pagina
        titleLabel = tk.Label(self.master, text="Object Generator", font=self.boldFont, bg=self.secondaryColor, fg=self.fontColor)
        titleLabel.pack(fill=tk.X)
        
        #Botao para janela de criacao
        #self.createObjectButton = tk.Button(master, text="Criar objeto", command=self.createObjectWindow, bg=self.fontColor, font=self.normalFont, width=10, height=5, bd=4, relief=tk.RAISED, padx=10, pady=5)
        self.createObjectButton = tk.Button(master, text="Criar objeto", command=wCreateObject.__init__, bg=self.fontColor, font=self.normalFont, width=10, height=5, bd=4, relief=tk.RAISED, padx=10, pady=5)
        self.createObjectButton.pack(pady=10, side=tk.LEFT, padx=10)
        
        #Botao para janela de transformacao
        self.createObjectButton = tk.Button(master, text="Transformação", command=self.createTransformWindow, bg=self.fontColor, font=self.normalFont, width=10, height=5, bd=4, relief=tk.RAISED, padx=10, pady=5)
        self.createObjectButton.pack(pady=10, side=tk.LEFT, padx=10)
        
    def createObjectWindow(self):
        objectWindow = tk.Toplevel(self.master)
        objectWindow.title("Create Object")
        objectWindow.geometry("300x300")
        objectWindow.configure(bg=self.backgroundColor)
        
        #Titulo da pagina
        titleLabel = tk.Label(objectWindow, text="Object Creator", font=self.boldFont, bg=self.secondaryColor, fg=self.fontColor)
        titleLabel.grid(row=0, column=0, columnspan=3, sticky="ew")
        objectWindow.columnconfigure(0, weight=1) # Faz o title label ocupar toda linha 0

        
        #Nomear o objeto
        nameLabel = tk.Label(objectWindow, text="Object Name", bg=self.backgroundColor, fg= self.fontColor, font=self.normalFont)
        nameLabel.grid(row=2, column=0, pady=5, padx=5)
        self.nameEntry = tk.Entry(objectWindow)
        self.nameEntry.grid(row=3, column=0, pady=5, padx=5)
        
        # Menu dropdown para types de objetos.
        typeLabel = tk.Label(objectWindow, text="Tipo de objeto", bg=self.backgroundColor, fg= self.fontColor, font=self.normalFont)
        typeLabel.grid(row=2, column=1, pady=5)
        objectTypes = ["Reta", "Quadratico", "Triangulo", "Circulo"]
        self.types = tk.StringVar(objectWindow)
        self.types.set(objectTypes[0])  # Define o valor default
        typeDropdown = tk.OptionMenu(objectWindow, self.types, *objectTypes) #Depois fazer a estilização
        typeDropdown.grid(row=3, column=1, pady=5)
        
        # Botao de parametros
        self.paramsButton = tk.Button(objectWindow, text="Definir coordenadas", command=self.createParamsWindow, bg=self.fontColor, font=self.normalFont, relief=tk.RAISED, padx=10, pady=5)
        self.paramsButton.grid(row=4, column=0, columnspan=2, pady=5)


        
    # def createParamsWindow(self):
    #     paramsWindow = tk.Toplevel(self.master)
    #     paramsWindow.title("Set Parameters")
    #     paramsWindow.geometry("300x300")
    #     paramsWindow.configure(bg=self.backgroundColor)
        
    #     objectType = self.types.get()
    #     objectName = self.nameEntry.get()
        
    #     #Essa logica vai meio de placeholder aqui, depois a gente revisa
        
    #     if objectType == "Reta":
            
    #         #Titulo da pagina
    #         titleLabel = tk.Label(paramsWindow, text=f"Set Parameters for {objectName} ", font=self.boldFont, bg=self.secondaryColor, fg=self.fontColor)
    #         titleLabel.grid(row=0, column=0, columnspan=4, sticky="ew")
    #         paramsWindow.columnconfigure(0, weight=1) # Faz o title label ocupar toda linha 0
            
    #         #Coordenadas minimas
    #         minLabel = tk.Label(paramsWindow, text="Minimos", font=self.normalFont, bg=self.secondaryColor, fg=self.fontColor)
    #         minLabel.grid(row=1, column=1,  pady=5, padx=5)
    #         maxLabel = tk.Label(paramsWindow, text="Maximos", font=self.normalFont, bg=self.secondaryColor, fg=self.fontColor)
    #         maxLabel.grid(row=1, column=3, pady=5, padx=5)
            
    #         x1Label = tk.Label(paramsWindow, text="X1", font=self.normalFont)
    #         x1Label.grid(row=2, column=0, padx=3, pady=5, sticky="e")
    #         self.x1Entry = tk.Entry(paramsWindow)
    #         self.x1Entry.grid(row=2, column=1, pady=5, sticky="w")
            
    #         x2Label = tk.Label(paramsWindow, text="X2", font=self.normalFont)
    #         x2Label.grid(row=2, column=2, padx=3, pady=5, sticky="e")
    #         self.x2Entry = tk.Entry(paramsWindow)
    #         self.x2Entry.grid(row=2, column=3, pady=5, sticky="w")
            
    #         y1Label = tk.Label(paramsWindow, text="Y1", font=self.normalFont)
    #         y1Label.grid(row=3, column=0, padx=3, pady=5, sticky="e")
    #         self.y1Entry = tk.Entry(paramsWindow)
    #         self.y1Entry.grid(row=3, column=1, pady=5, sticky="w")
            
    #         y2Label = tk.Label(paramsWindow, text="Y2", font=self.normalFont)
    #         y2Label.grid(row=3, column=2, padx=3, pady=5, sticky="e")
    #         self.y2Entry = tk.Entry(paramsWindow)
    #         self.y2Entry.grid(row=3, column=3, pady=5, sticky="w")
            
    #         # Botão para desenhar
    #         submitButton = tk.Button(paramsWindow, text="Draw", command=self.submitParameters, bg=self.fontColor, font=self.normalFont, relief=tk.RAISED, padx=10, pady=5)
    #         submitButton.grid(row=4, column=0, columnspan=2, pady=5)
        
    
    # def submitParameters(self):
    #     objectType = self.types.get()
    #     object_name = self.nameEntry.get()
    #     if objectType == "Reta":
    #         x1_coord = int(self.x1Entry.get())
    #         y1_coord = int(self.y1Entry.get())
    #         x2_coord = int(self.x2Entry.get())
    #         y2_coord = int(self.y2Entry.get())
            

    #         coordMin = (x1_coord, y1_coord)
    #         coordMax = (x2_coord, y2_coord)

    #         # Cria objeto
    #         objeto = Linha(coordMin, coordMax, object_name, 1, 1)
    #         # Adiciona o objeto para a lista.
    #         self.gerenciadorSINGLETON.addEntidade(objeto)
    #         self.gerenciadorSINGLETON.draw()


    #         #obj = CreateObject(object_name, objectType, (coordMin, coordMax))
    #         # Adiciona o objeto para a lista.
    #         #self.object_manager.add_object(obj)
    #         self.update_object_listbox()
    #         # Debug
    #         #print(f"Object Name: {object_name}, Object Type: {objectType}, Coordinates: {obj.coordinates}")
            
    def createTransformWindow(self):
        transformWindow = tk.Toplevel(self.master)
        transformWindow.title("Transform Object")
        transformWindow.geometry("300x300")
        transformWindow.configure(bg=self.backgroundColor)
        
        #Titulo da pagina
        titleLabel = tk.Label(transformWindow, text="Transform Object", font=self.boldFont, bg=self.secondaryColor, fg=self.fontColor)
        titleLabel.pack(fill=tk.X)


def main(gerenciadorSINGLETON):
    root = tk.Tk()
    app = Interface(root, gerenciadorSINGLETON)
    root.mainloop()
    
if __name__ == "__main__":
    main()
