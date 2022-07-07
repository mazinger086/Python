"""
En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables,
también debe de tener un label con el texto que queráis.
"""

import tkinter

from tkinter import ttk, END

window = tkinter.Tk()

label = ttk.Label(text="Lista de Estudiantes: ")
label.grid(column=0, row=0, padx=10, pady=10, sticky=tkinter.W)

elemento = tkinter.StringVar()

listaContenedor = tkinter.Listbox(window)

estudiantes = ['Juan', 'Jose', 'Pedro', 'Maria', 'Eduardo', 'Cristina', 'Sebastian', 'Ernesto', 'Julia', 'Belen']

for e in estudiantes:
   listaContenedor.insert(END, e)

listaContenedor.grid(column=0, row=1, pady=10, padx=10)

window.mainloop()
