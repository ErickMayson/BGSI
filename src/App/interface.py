import tkinter as tk
from tkinter import messagebox

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Tkinter App")
        self.master.geometry("600x600")
        self.master.configure(bg="gray")

        self.create_button = tk.Button(master, text="Create Object", command=self.create_object, width=15, height=10, bd=4, relief=tk.RAISED)
        self.create_button.pack(pady=20, side=tk.LEFT, padx=10)

        self.transform_button = tk.Button(master, text="Transformacao", command=self.transform_text, width=15, height=10, bd=4, relief=tk.RAISED)
        self.transform_button.pack(pady=20, side=tk.LEFT)

    def create_object(self):
        object_window = tk.Toplevel(self.master)
        object_window.title("Object Window")
        object_window.geometry("300x300")
        object_window.configure(bg="gray")

        self.placeholder_label = tk.Label(object_window, text="Placeholder")
        self.placeholder_label.pack(pady=20)

        transform_button = tk.Button(object_window, text="Transformacao", command=self.transform_text, width=15, height=10, bd=4, relief=tk.RAISED)
        transform_button.pack(pady=10)

    def transform_text(self):
        if hasattr(self, 'placeholder_label'):
            self.placeholder_label.config(text="Text Transformed")

def main():
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
