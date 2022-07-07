import random
import sys
import tkinter
from tkinter import ttk

#widget && componentes: Son Controles (Botons, imput, radio buttons, checkboxes)
# Se pueden poner en componenetes como Frames o Ventanas

"""
import pprint

pprint.pprint(dir(window))
"""

# Creando una Ventana

window = tkinter.Tk()

# Geometrias: Pack, Grid, Place

#Etiqueta
"""
label1 = tkinter.Label(window, text="label 1", bg="purple", fg="white")
label2 = tkinter.Label(window, text="label 2", bg="red", fg="white")
label3 = tkinter.Label(window, text="label 3", bg="blue", fg="white")
label4 = tkinter.Label(window, text="label 4", bg="brown", fg="white")
label5 = tkinter.Label(window, text="label 5", bg="yellow", fg="black")
label6 = tkinter.Label(window, text="label 6", bg="green", fg="white")
"""


# GEOMETRIA PACK: Se utiliza para situar elementos de arriba a abajo o cara a cara
"""
label1.pack(ipadx=45, ipady=15, fill='x')
label2.pack(ipadx=45,ipady=15, fill='x')
label3.pack(ipadx=45, ipady=15, fill='x')
label4.pack(ipadx=15,ipady=15, side='left')
label5.pack(ipadx=15, ipady=15, side='left')
label6.pack(ipadx=15,ipady=15, side='right')
"""

# GEOMETRIA GRID:

# (0,0) (1,0) (2,0)
# Label Entry

# (0,1) (1,1) (2,1)

"""
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Etiqueta Usuario
username_label = ttk.Label(window, text="Username:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

# Input Usuario
username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, pady=5, padx=5)

# Etiqueta Password
password_label = ttk.Label(window, text="Password:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

# Input Password
password_entry = ttk.Entry(window, show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.E, pady=5, padx=5)

# Boton
login_button = ttk.Button(window, text="Entrar")
login_button.grid(column=1, row=3, sticky=tkinter.E, pady=5, padx=5)
"""

# GEOMETRIA PLACE

"""
import random

colors = ['blue', 'red', 'yellow', 'pink', 'purple', 'black']

for x in range(0,10):
    color = random.randint(0, len(colors) -1)
    color2 = random.randint(0, len(colors) -1)
    ancho = random.randint(0,50)
    alto = random.randint(0,100)
    label = tkinter.Label(window, text="etiqueta", bg=colors[color], fg=colors[color2])
    label.place(x=random.randint(0,100), y=random.randint(0,100))

label1 = tkinter.Label(window, text="Posiscionamiento Absoluto", bg='blue', fg='white')
label1.place(x=10, y=50)

label2 = tkinter.Label(window, text="Otro mas", bg='red', fg='yellow')
label2.place(x=10, y=30)
"""

# WIDGETS

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

#Frame sirven para agrupar elementos
"""
frame = ttk.Frame(window)
frame.grid(column=0, row=0, sticky=tkinter.W)

label = ttk.Label(frame, text="Hola")
label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)
"""

# Radio Buttons
"""
r1 = ttk.Radiobutton(window, text='Si', value='1', variable=seleccionado)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=seleccionado)
r3 = ttk.Radiobutton(window, text='Quizas', value='3', variable=seleccionado)

r1.grid(column=0, row=1, pady=5, padx=10, sticky=tkinter.W)
r2.grid(column=0, row=2, pady=5, padx=10, sticky=tkinter.W)
r3.grid(column=0, row=3, pady=5, padx=10, sticky=tkinter.W)
"""

# Checkbox buttons
"""
var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
checkbox = ttk.Checkbutton(window, variable=var1, text='Acepto condiciones', onvalue=1, offvalue=0)
checkbox1 = ttk.Checkbutton(window, variable=var2,text='No', onvalue=1, offvalue=0)

checkbox.grid(column=0, row=1, pady=5, padx=10, sticky=tkinter.W)
checkbox1.grid(column=0, row=2, pady=5, padx=10, sticky=tkinter.W)
"""

#Boton

def salir(e):
    print('Adios')
    window.quit()

def saludar(e):
    print('Han hecho click en saludar')

def saludarDobleClick(e):
    print('Has hecho doble click...')


boton = tkinter.Button(window, text='Haz click')
boton.pack()
boton.bind('<Button-1>', saludar)
boton.bind('<Double-1>', saludarDobleClick)

botonSalir = tkinter.Button(window, text='Salir')
botonSalir.pack()
botonSalir.bind('<Button-1>', salir)


# llamando al loop
window.mainloop()
sys.exit(0)





