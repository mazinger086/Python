#Escribe una función que pueda decirte si un número (número entero) es primo o no.
#El numero es primo si y solo si tiene 2 divisiores, el mismo y la unidad

#NOTA: Un número es primo si se divide entre sí mismo y el 1.



def numeroPrimo(numero):
    if numero == 0 or numero == 1 or numero == 4: #si no, el ciclo fallará por su naturaleza de dividir entre 2 al número.
        return False
    for x in range(2, int(numero / 2)):
        if numero % x == 0:
            print(x)
            return False
    return True

numero = int(input('Ingresa un numero entero: '))
es_primo = numeroPrimo(numero)
if es_primo:
    print("es primo")
else:
    print('No es primo')


