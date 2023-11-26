import tkinter as tk
from tkinter import ttk
import json

class Interface:
    
    def __init__(self, master):
        
        with open("palette.json", "r") as json_file:
            stylingData = json.load(json_file)
            
        self.backgroundColor =  stylingData["palette"]["Main"]
        self.secondaryColor = stylingData["palette"]["Secondary"]
        self.tertiaryColor = stylingData["palette"]["Tertiary"]
        self.font = stylingData["palette"]["Font"]
        self.fontColor = stylingData["palette"]["FontColor"]
            
        self.master = master
        self.master.title("Object Generator")
        self.master.geometry("800x800")
        self.master.configure(bg=self.backgroundColor)
        
        #Titulo da pagina
        titleLabel = tk.Label(self.master, text="Object Generator", font=("Helvetica", 18, "bold"), bg=self.secondaryColor, fg=self.fontColor)
        titleLabel.pack(fill=tk.X)
        
        #Botao para janela de criacao
        self.createObjectButton = tk.Button(master, text="Criar objeto", command=self.createObjectWindow, bg=self.fontColor, font=("Helvetica", 12, "bold"), width=10, height=5, bd=4, relief=tk.RAISED, padx=10, pady=5)
        self.createObjectButton.pack(pady=10, side=tk.LEFT, padx=10)
        
        #Botao para janela de transformacao
        self.createObjectButton = tk.Button(master, text="Transformação", command=self.createTransformWindow, bg=self.fontColor, font=("Helvetica", 12, "bold"), width=10, height=5, bd=4, relief=tk.RAISED, padx=10, pady=5)
        self.createObjectButton.pack(pady=10, side=tk.LEFT, padx=10)
        
    def createObjectWindow(self):
        objectWindow = tk.Toplevel(self.master)
        objectWindow.title("Create Object")
        objectWindow.geometry("300x300")
        objectWindow.configure(bg=self.backgroundColor)
        
        #Titulo da pagina
        titleLabel = tk.Label(objectWindow, text="Object Creator", font=("Helvetica", 18, "bold"), bg=self.secondaryColor, fg=self.fontColor)
        titleLabel.pack(fill=tk.X)
        
        
        
    def createTransformWindow(self):
        transformWindow = tk.Toplevel(self.master)
        transformWindow.title("Transform Object")
        transformWindow.geometry("300x300")
        transformWindow.configure(bg=self.backgroundColor)
        
        #Titulo da pagina
        titleLabel = tk.Label(transformWindow, text="Transform Object", font=("Helvetica", 18, "bold"), bg=self.secondaryColor, fg=self.fontColor)
        titleLabel.pack(fill=tk.X)


def main():
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()