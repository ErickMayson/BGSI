import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from App.Classes.Entidade import *
from .wCreateObject import wCreateObject
from .wTransformations import wTransformations
from Classes.GerenciadorObjetos import GerenciadorObjetos


#print(sys.path)
#Mantenha o nome das variáveis em inglês.
#Se possível, passar os nomes para CamelCase, comecei fazer com _ pra dar uma variada e achei uma porcaria

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
        self.master.title("BGSI - Computação Gráfica")
        self.master.geometry("400x800")
        self.master.configure(bg=self.backgroundColor)
        
        #Titulo da pagina
        titleLabel = tk.Label(self.master, text="BGSI - Computação Gráfica :]", font=self.boldFont, bg=self.secondaryColor, fg=self.fontColor)
        titleLabel.grid(row=0, column=0, columnspan=4, sticky="ew")
        #titleLabel.pack(fill=tk.X)

        #Lista de Entidades
        entityList = ttk.Treeview(self.master,columns=("nome", "tipo"), show="headings", height=10,)
        entityList.heading("nome", text="Entidade")
        entityList.heading("tipo", text="Tipo")
        
        entityList.grid(row=1, column=1, columnspan=2, rowspan=1, sticky="ew", padx=5, pady=5)
        

        #Isso não basta, nós temos que adicionar as entidades quando a criamos, e não no construtor.
        for entidade in self.gerenciadorSINGLETON.entidadesCriadas:
            # Nó pai, insere na última posição, valores.
            entityList.insert("", tk.END, values=(entidade.nome, entidade.__class__.__name__))
        
        self.entityList = entityList
        
        #Botao para janela de criacao
        #self.createObjectButton = tk.Button(master, text="Criar objeto", command=self.createObjectWindow, bg=self.fontColor, font=self.normalFont, width=10, height=5, bd=4, relief=tk.RAISED, padx=10, pady=5)
        self.createObjectButton = tk.Button(master, text="Novo objeto", command= self.openCreateObject, bg=self.fontColor, font=self.normalFont, width=8, height=1, bd=4, relief=tk.RAISED, padx=10, pady=5)
        self.createObjectButton.grid(row=2, column=1, pady=5, padx=5)
        
        #Botao para janela de transformacao
        self.createObjectButton = tk.Button(master, text="Transformação", command=self.openTransformations, bg=self.fontColor, font=self.normalFont, width=10, height=1, bd=4, relief=tk.RAISED, padx=10, pady=5)
        self.createObjectButton.grid(row=2, column=2, pady=5, padx=5)
        
        #Botao para janela de transformacao
        self.createObjectButton = tk.Button(master, text="Salvar", command=lambda: self.gerenciadorSINGLETON.saveDisplayFile(), bg=self.fontColor, font=self.normalFont, width=10, height=1, bd=4, relief=tk.RAISED, padx=10, pady=5)
        self.createObjectButton.grid(row=3, column=1, columnspan=2, pady=5, padx=5)
        
    
    def updateEntityList(self, entity):
        self.entityList.insert("", tk.END, values=(entity.nome, entity.__class__.__name__))

    def openCreateObject(self):
        wCreateObject(self.master, self.gerenciadorSINGLETON, self.updateEntityList)

    def openTransformations(self):
        #self.entityList.selection() -> Retorna uma tupla com o id do item selecionado
        ident = self.entityList.selection()
        if (ident == ()):
            messagebox.showerror("Erro", "Selecione uma entidade.")
            return
        
        selectedEntityTreeNode = self.entityList.item(self.entityList.selection()[0])
        #SelectEntityTreeNode -> retorna {"text": "", "image": "", "values": ["nome", "tipo"]}
        #SelectEntityTreeNode['values'] -> ["nome", "tipo"]

        entityName = selectedEntityTreeNode['values'][0]
        wTransformations(self.master, entityName, self.gerenciadorSINGLETON, self.updateEntityList)


def main(gerenciadorSINGLETON):
    root = tk.Tk()
    app = Interface(root, gerenciadorSINGLETON)
    root.mainloop()
    
if __name__ == "__main__":
    main()
