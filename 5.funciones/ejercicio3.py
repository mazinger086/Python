#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

#Para calcular si un año determinado es bisiesto, compruebe que el año es divisible por 4 pero no por 100.
# Si no se cumple esta condición, compruebe que el año es divisible por 400. El año es bisiesto si el resultado es un entero

year = int(input('Ingrese un año: '))

def bisiesto(year):
    resultado = year % 4
    not100 = year % 100 != 0
    if resultado == 0 and not100:
        print('Es bisiesto')
    elif year % 400 == 0:
        print('Es bisiesto')
    else:
        print('No es bisiesto')



bisiesto(year)