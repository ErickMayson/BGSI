import tkinter as tk
import pygame
from tkinter import messagebox
from Classes.create import CreateObject, ObjectManager



#Mantenha o nome das variáveis em inglês.
#Se possível, passar os nomes para CamelCase, comecei fazer com _ pra dar uma variada e achei uma porcaria

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("TKinter app")
        self.master.geometry("600x600")
        self.master.configure(bg="gray")
        self.object_manager = ObjectManager()
        self.pygame_screen = None


        self.create_button = tk.Button(master, text="Criar objeto", command=self.create_object_window, width=15, height=10, bd=4, relief=tk.RAISED)
        self.create_button.pack(pady=20, side=tk.LEFT, padx=10)

        self.transform_button = tk.Button(master, text="Transformação", command=self.create_transform_window, width=15, height=10, bd=4, relief=tk.RAISED)
        self.transform_button.pack(pady=20, side=tk.LEFT)
        
        # Inicialize a Listbox apenas, não a mostre inicialmente
        self.object_listbox = tk.Listbox(master, width=30, height=15, bd=4, relief=tk.SUNKEN)

    def create_object_window(self):
        object_window = tk.Toplevel(self.master)
        object_window.title("Criar Objeto")
        object_window.geometry("300x300")
        object_window.configure(bg="gray")

        # Inserir nome do objeto
        name_label = tk.Label(object_window, text="Nome do objeto")
        name_label.grid(row=0, column=0, pady=10)
        self.name_entry = tk.Entry(object_window)
        self.name_entry.grid(row=0, column=1, pady=10)

        # Menu dropdown para tipos de objetos.
        type_label = tk.Label(object_window, text="Tipo de objeto")
        type_label.grid(row=1, column=0, pady=10)
        object_types = ["Reta", "Quadraticos", "Triangulo", "Circulo"]
        self.type_var = tk.StringVar(object_window)
        self.type_var.set(object_types[0])  # Set the default value
        type_dropdown = tk.OptionMenu(object_window, self.type_var, *object_types)
        type_dropdown.grid(row=1, column=1, pady=10)

        # Botão das coordenadas ou parametros sei la
        param_button = tk.Button(object_window, text="Definir coordenadas", command=self.create_parameter_window)
        param_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        

    def create_parameter_window(self):
        param_window = tk.Toplevel(self.master)
        param_window.title("Coordenadas")
        param_window.geometry("300x300")
        param_window.configure(bg="gray")

        object_type = self.type_var.get()

        # Colocar a lógica para outros tipos de objetos
        if object_type == "Reta":
            x1_label = tk.Label(param_window, text="X1")
            x1_label.grid(row=0, column=0, pady=10)
            self.x1_entry = tk.Entry(param_window)
            self.x1_entry.grid(row=0, column=1, pady=10)

            y1_label = tk.Label(param_window, text="Y1")
            y1_label.grid(row=1, column=0, pady=10)
            self.y1_entry = tk.Entry(param_window)
            self.y1_entry.grid(row=1, column=1, pady=10)

            x2_label = tk.Label(param_window, text="X2")
            x2_label.grid(row=2, column=0, pady=10)
            self.x2_entry = tk.Entry(param_window)
            self.x2_entry.grid(row=2, column=1, pady=10)

            y2_label = tk.Label(param_window, text="Y2")
            y2_label.grid(row=3, column=0, pady=10)
            self.y2_entry = tk.Entry(param_window)
            self.y2_entry.grid(row=3, column=1, pady=10)

        # Talvez a gente poderia criar uma lógica dinamica pra objetos quadráticos, sei lá

        # Botão para desenhar
        submit_button = tk.Button(param_window, text="Desenhar", command=self.submit_parameters)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10)
        

    def submit_parameters(self):
        object_type = self.type_var.get()
        object_name = self.name_entry.get()

        if object_type == "Reta":
            x1_coord = int(self.x1_entry.get())
            y1_coord = int(self.y1_entry.get())
            x2_coord = int(self.x2_entry.get())
            y2_coord = int(self.y2_entry.get())

            # Cria objeto
            obj = CreateObject(object_name, object_type, (x1_coord, y1_coord, x2_coord, y2_coord))

            # Adiciona o objeto para a lista.
            self.object_manager.add_object(obj)
            self.update_object_listbox()

            # Debug
            print(f"Object Name: {object_name}, Object Type: {object_type}, Coordinates: {obj.coordinates}")

    def create_transform_window(self):
        object_window = tk.Toplevel(self.master)
        object_window.title("Transformar")
        object_window.geometry("300x300")
        object_window.configure(bg="gray")
        
    def update_object_listbox(self):
        # Isso aqui limpa a Listbox
        self.object_listbox.delete(0, tk.END)

        # Adicione os itens existentes do ObjectManager à Listbox, se houver algum
        for obj in self.object_manager.objects:
            self.object_listbox.insert(tk.END, f"{obj.object_name} - {obj.object_type}")

        # Exiba a Listbox se houver objetos no ObjectManager
        if self.object_manager.objects:
            self.object_listbox.pack(pady=20, padx=10, side=tk.LEFT)
            self.object_listbox.bind("<ButtonRelease-1>", self.on_listbox_click)  # Associe um evento de clique

    def on_listbox_click(self, event):
        selected_item = self.object_listbox.curselection()
        if selected_item:
            item_index = selected_item[0]
            selected_object = self.object_manager.objects[item_index]
            
            #O item clicado tem que ser gerado no PyGame, mas não criei a lógica ainda.
            print(f"Item clicado: {selected_object.object_name} - {selected_object.object_type}, Coordenadas: {selected_object.coordinates}")
        
def main():
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
