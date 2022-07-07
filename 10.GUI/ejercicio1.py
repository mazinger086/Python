"""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado
y que contenga un botón de reinicio para que deje todo como al principio. Al principio no tiene que haber una opción seleccionada.
"""

import sys
import tkinter
from tkinter import ttk
import  pprint

window = tkinter.Tk()

label = ttk.Label(window,text="Lista de lenguajes de programación:")
label.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady=10)

def obtenerValor():
    print(seleccionado.get())


def limpiar():
    seleccionado.set(None)

seleccionado = tkinter.StringVar()

r1 = ttk.Radiobutton(window, text="Javascript", value="Javascript", variable=seleccionado, command=obtenerValor)
r2 = ttk.Radiobutton(window, text="Python", value="Python", variable=seleccionado,  command=obtenerValor)
r3 = ttk.Radiobutton(window, text="C#", value="C#", variable=seleccionado,  command=obtenerValor)
r4 = ttk.Radiobutton(window, text="Fortran", value="Fortran", variable=seleccionado,  command=obtenerValor)

r1.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=5)
r2.grid(column=0, row=3, sticky=tkinter.W, padx=10, pady=5)
r3.grid(column=0, row=4, sticky=tkinter.W, padx=10, pady=5)
r4.grid(column=0, row=5, sticky=tkinter.W, padx=10, pady=5)

clearButton = ttk.Button(text="Clear", command=limpiar)
clearButton.grid(column=0, row=6, sticky=tkinter.E, padx=10, pady=10)

window.mainloop()
sys.exit(0)