from tkinter import *
from tkinter import ttk
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from App.Classes.Entidade import *

class wCreateObject:
    
    def __init__(self, master, gerenciador = None):

        #Configurações Iniciais
        mainWindow = Toplevel(master)
        mainWindow.title("Adicionar Objeto")
        self.gerenciadorSINGLETON = gerenciador
        #mainWindow.geometry("200x200")

        # Criar frame principal
        mainframe = ttk.Frame(mainWindow, padding = "2 2 2 2")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Cria o frame dos parametros
        parametersFrame = ttk.Frame(mainWindow, padding = "2 2 2 2")
        parametersFrame.grid(column=0, row=1, sticky=(N, W, E, S))
        self.parametersFrame = parametersFrame
        
        # Inserir o nome do objeto
        nameLabel = ttk.Label(mainframe, text="Nome do objeto")
        nameLabel.grid(row=0, column=0, pady=10)
        self.nameEntry = ttk.Entry(mainframe)
        self.nameEntry.grid(row=0, column=1, pady=10)

        # Menu dropdown para types de objetos.
        typeLabel = ttk.Label(mainframe, text="Tipo de objeto")
        typeLabel.grid(row=1, column=0, pady=10)
        types = ["Reta", "Quadrado", "Triangulo", "Circulo"]
        self.selectedType = StringVar(mainframe)
        self.selectedType.set(types[0])  # Set the default value

        self.mainframe = mainframe
        self.mainWindow = mainWindow
        typeDropdown = ttk.OptionMenu(mainframe, self.selectedType, *types, direction="below", command=self.showParameters)
        typeDropdown.grid(row=1, column=1, pady=10)

        mainWindow.mainloop()

    def showParameters(self, *args):
        # Remove o frame de parametros, caso ele exista. Isso é feito para que o frame se adapte ao tipo de objeto selecionado
        self.parametersFrame.grid_forget()

        # Cada if spawnará um frame de parametros diferente, dependendo do tipo de objeto selecionado
        if self.selectedType.get() == "Reta":
            print("Ainda não implementado")
        if self.selectedType.get() == "Quadrado":
            # Define uma lista de strings que serão usadas como rótulos para os campos de entrada
            input = ("Coordenada X Min", "Coordenada Y Min", "Coordenada X Max", "Coordenada Y Max")
            # Cria uma lista de variáveis IntVar, que serão usadas para armazenar os valores dos campos de entrada
            variables = [IntVar() for _ in range(4)]

            # se i = 0 -> i*2 = 0 e i*2+1 = 1
            # se i = 1 -> i*2 = 2 e i*2+1 = 3
            # Assim se economiza linhas de código
            for i in range(2):
                ttk.Label(self.parametersFrame, text = input[i*2]).grid(column = 0, row = i*2, sticky = (W, E))
                ttk.Spinbox(self.parametersFrame, to = 100, width = 5, textvariable= variables[i*2]).grid(column = 1, row =  i*2, sticky = (W, E))
                ttk.Label(self.parametersFrame, text = input[i*2+1]).grid(column = 0, row =  i*2 + 1, sticky = (W, E))
                ttk.Spinbox(self.parametersFrame, to = 100, width = 5, textvariable= variables[i*2+1]).grid(column = 1, row = i*2 + 1, sticky = (W, E))
            
            # Cria um botão que, quando pressionado, chama a função 'submitParameters' com a lista 'variables' como argumento
            ttk.Button(self.parametersFrame,text="Criar", command= lambda: self.submitParameters(variables)).grid(column=1, row=4)
            # Exibe o frame
            self.parametersFrame.grid()
            
        else:
            print("Ainda não implementado")

    # Função que é chamada quando o botão 'Criar' é pressionado
    def submitParameters(self, parameters):
        print("entrei")
        objectType = self.selectedType.get()
        objectName = self.nameEntry.get()

        if objectType == "Quadrado":
            print(parameters[0].get(), parameters[1].get())
            x1Coord = int(parameters[0].get())
            y1Coord = int(parameters[1].get())
            x2Coord = int(parameters[2].get())
            y2Coord = int(parameters[3].get())
            

            coordMin = (x1Coord, y1Coord)
            coordMax = (x2Coord, y2Coord)

            # Cria objeto
            objeto = Linha(coordMin, coordMax, objectName, 1, 1)
            # Adiciona o objeto para a lista.
            self.gerenciadorSINGLETON.addEntidade(objeto)
            self.gerenciadorSINGLETON.draw()

            self.update_object_listbox()



#wCreateObject(Tk())