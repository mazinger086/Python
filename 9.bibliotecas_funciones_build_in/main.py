# Bibliotecas y funciones Build-In
"""
import _thread
import time

def horaActual(nombre_thread, tiempo_de_espera):

    count = 0

    while count < 5:
        time.sleep(tiempo_de_espera)
        count += 1
        print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')


_thread.start_new_thread(horaActual, ("thread_uno", 1))
_thread.start_new_thread(horaActual, ("thread_dos", 2))

while True:
    time.sleep(0.1)



import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Quitando bichos")
logging.info(("Arrancando el programa"))
logging.warning("Hace calor")
logging.error("test")
logging.critical("adios")

"""
# FILTER

"""
numeros = [1,2,3,4,5,6,7,8,9,10]

def miFuncion(x):
    if x % 2 != 0:
        return True
    return False

#resultado = filter(miFuncion, numeros)
resultado = filter(lambda x: x % 2 == 0 , numeros)

print(list(resultado))
"""

#MAP

"""
numeros = [1,2,3,4,5,6,7,8,9]

def cuadrado(x):
    return x * x

#resultado = map(cuadrado, numeros)
resultado = map(lambda x: x * x, numeros)

print(list(resultado))
"""

from functools import reduce

#REDUCE (nos da un unico resultado a traves de una lista)

"""
def suma(a, b):
    print(f'a={a}, b={b}')
    return a + b

res = reduce(suma, [1,2,3,4,5])
print(res)

"""

#ZIP (Iterables en una tupla y los devuelve)

"""
cursos = ['Java', 'Python', 'Git']
asistentes = [15, 20, 4]
demo = zip(cursos, asistentes)
print(list(demo))
"""

# All and Any (Sirven para verificar que todas las condiciones de las listas se cumplan)

"""
listaA = [1 == 1, 2 == 2, 3 == 4]
res = all(listaA)
#res = any(listaA)
print(res)
"""

# Round (Redondea dependiendo del decimal)
"""
a = 5.5
b = 5.4
c = 5.6

print(round(a))
print(round(b))
print(round(c))
"""


#MIN (Obtiene el minimo de una lista)
#print(min(2,3,4,5,6,7,8,9,3,1))

#Pow (Potencia de numeros)
#print(pow(2,4))
#print(2**4)

#Ordenar Listas
"""
lista = ['z','c','d','a', 'f']
ordenada = sorted(lista, reverse=True)
print(ordenada)
"""

#Input (Valores por pantalla)
"""
a = input("¿Como te llamas?: ")
print(f'Hola, {a}')
"""
"""
from getpass import getpass

user = input('Ingrese usuario: ')
password = getpass("password: ")

print(user, password)
"""

secreto = 50

valor = 0
while valor != secreto:
    valor = int(input("Introduce un numero: "))

    if valor > secreto:
        print("Muy alto")
        continue

    if valor < secreto:
        print("Muy bajo")
        continue

print("Acertaste")











