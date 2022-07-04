"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación
para calcular el tiempo que queda de trabajo.
"""

import time

total = time.time()
tiempo = time.localtime(total)


hora = tiempo.tm_hour
minutos = tiempo.tm_min

def formatoReloj(h, m):

    # Ceros to hora y minutos

    if(h < 10):
        h = "0" + str(h)
    else:
        h = str(h)

    if(m < 10):
        m = "0" + str(m)
    else:
        m = str(m)

    tiempoFormateado = h+":"+m

    return tiempoFormateado





def cuantoFalta(h, m):
    totalFaltante = ""
    faltanMinutos = 60 - m
    faltanHoras = 19 - h
    totalFaltante = "Faltan: " + str(faltanHoras) + " horas y " + str(faltanMinutos) + " minutos para ir a casa"

    print(formatoReloj(h, m))
    print(totalFaltante)


cuantoFalta(hora, minutos)




#print("Faltan:", faltanMinutos, "minutos")
#print("Faltan Horas:", faltanHoras)

