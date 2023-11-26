from tkinter import *
from tkinter import ttk

class jAdicionarObjeto:
    
    def __init__(self, master):
        janelaPrincipal = Toplevel(master)
        janelaPrincipal.title("Adicionar Objeto")
        #janelaPrincipal.geometry("200x200")

        mainframe = ttk.Frame(janelaPrincipal, padding = "2 2 2 2")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Inserir nome do objeto
        name_label = ttk.Label(mainframe, text="Nome do objeto")
        name_label.grid(row=0, column=0, pady=10)
        self.name_entry = ttk.Entry(mainframe)
        self.name_entry.grid(row=0, column=1, pady=10)

        # Menu dropdown para tipos de objetos.
        type_label = ttk.Label(mainframe, text="Tipo de objeto")
        type_label.grid(row=1, column=0, pady=10)
        tipos = ["Reta", "Quadrado", "Triangulo", "Circulo"]
        self.tipo_selecionado = StringVar(mainframe)
        self.tipo_selecionado.set(tipos[0])  # Set the default value

        self.mainframe = mainframe
        type_dropdown = ttk.OptionMenu(mainframe, self.tipo_selecionado, *tipos, direction="below", command=self.mostrarParametros)
        type_dropdown.grid(row=1, column=1, pady=10)

        janelaPrincipal.mainloop()

    def mostrarParametros(self, *args):
        if self.tipo_selecionado.get() == "Reta":
            print("Ainda não implementado")
        if self.tipo_selecionado.get() == "Quadrado":
            input = ("Coordenada X Min", "Coordenada Y Min", "Coordenada X Max", "Coordenada Y Max")
            for i in range(0,3,2):
                ttk.Label(self.mainframe, text = input[i]).grid(column = 0, row = i + 2, sticky = (W, E))
                ttk.Spinbox(self.mainframe, to = 100, width = 5).grid(column = 1, row = i + 2, sticky = (W, E))
                ttk.Label(self.mainframe, text = input[i+1]).grid(column = 0, row = i + 3, sticky = (W, E))
                ttk.Spinbox(self.mainframe, to = 100, width = 5).grid(column = 1, row = i + 4, sticky = (W, E))
            ttk.Button(text="Criar").grid(column=2, row=2)
        else:
            print("Ainda não implementado")

