import tkinter as tk
from tkinter import ttk, colorchooser

def on_color_change():
    rgb = colorchooser.askcolor()[0]
    if rgb:
        r_var.set(int(rgb[0]))
        g_var.set(int(rgb[1]))
        b_var.set(int(rgb[2]))
        update_color()

def update_color():
    r = r_var.get()
    g = g_var.get()
    b = b_var.get()
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    color_label.config(text=hex_color)
    color_frame.config(bg=hex_color)

# Create the main window
root = tk.Tk()
root.title("RGB Color Picker")

# Variables for storing RGB values
r_var = tk.IntVar()
g_var = tk.IntVar()
b_var = tk.IntVar()

# Create widgets
color_frame = tk.Frame(root, width=200, height=100, bg="#000000")
color_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

color_label = tk.Label(root, text="#000000", font=("Helvetica", 14))
color_label.grid(row=1, column=0, columnspan=3)

r_label = tk.Label(root, text="R:")
r_label.grid(row=2, column=0)
r_entry = ttk.Entry(root, textvariable=r_var)
r_entry.grid(row=2, column=1)

g_label = tk.Label(root, text="G:")
g_label.grid(row=2, column=2)
g_entry = ttk.Entry(root, textvariable=g_var)
g_entry.grid(row=2, column=3)

b_label = tk.Label(root, text="B:")
b_label.grid(row=2, column=4)
b_entry = ttk.Entry(root, textvariable=b_var)
b_entry.grid(row=2, column=5)

choose_button = ttk.Button(root, text="Choose Color", command=on_color_change)
choose_button.grid(row=3, column=0, columnspan=6, pady=10)

update_button = ttk.Button(root, text="Update Color", command=update_color)
update_button.grid(row=4, column=0, columnspan=6, pady=10)

# Run the Tkinter event loop
root.mainloop()
