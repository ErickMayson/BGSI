import tkinter as tk
from tkinter import messagebox

#Mantenha o nome das variáveis em inglês.

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("TKinter app")
        self.master.geometry("600x600")
        self.master.configure(bg="gray")

        self.create_button = tk.Button(master, text="Criar objeto", command=self.create_object_window, width=15, height=10, bd=4, relief=tk.RAISED)
        self.create_button.pack(pady=20, side=tk.LEFT, padx=10)

        self.transform_button = tk.Button(master, text="Transformação", command=self.create_transform_window, width=15, height=10, bd=4, relief=tk.RAISED)
        self.transform_button.pack(pady=20, side=tk.LEFT)

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
            x1_coord = self.x1_entry.get()
            y1_coord = self.y1_entry.get()
            x2_coord = self.x2_entry.get()
            y2_coord = self.y2_entry.get()


            # Não tem função então só printa os inputs.
            print(f"Object Name: {object_name}, Object Type: {object_type}, X1: {x1_coord}, Y1: {y1_coord}, X2: {x2_coord}, Y2: {y2_coord}")

        # Adicionar lógica para os outros objetos.

    def create_transform_window(self):
        object_window = tk.Toplevel(self.master)
        object_window.title("Transformar")
        object_window.geometry("300x300")
        object_window.configure(bg="gray")

def main():
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
