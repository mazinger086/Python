"""
temperatura = 7.0

def miFuncion(nombre="cliente"):
    #global temperatura //Cambiamos el valor de la variable local
    temperatura = 20.0
    print("Hola,", nombre, "la temperatura interior es de:", temperatura)

miFuncion()
print("La temperatura exterior es de:",temperatura)

a = int(input('Ingrese el primer numero: '))
b = int(input('Ingrese el segundo numero: '))

def suma(a,b):
     resultado = a + b
     print(resultado)


suma(a,b)"""
#Args nos permite definir un argumento global sin tener que poner cierta cantidad
"""def miFuncion(*args):
    print(args)
miFuncion(1,2,3,4,5)"""

#kwargs nos permite utlizar un diccionario como argumento principal

"""def miFuncion2(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

miFuncion2(vivienda = 'depto', piso='2', habitantes='4', adultos=True)

def operaciones(a,b):
    return a + b, a - b, a * b, a / b

resultado = operaciones(10, 5)

for res in resultado:
    print(type(res))

def sumador(inicial, final):
    resultado = 0

    for x in range(inicial, final + 1): #tener en cuenta que si no le agregas el 1 llega hasta el 4
        resultado += x

    return resultado

print(sumador(1,5))"""

#Funciones anonimas (lambda) son las que se asignan a una variable

anonima = lambda nombre, edad: \
    print("Hola", nombre, "tienes:",edad, 'años')
anonima('Gisela', 38)


