#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numero_inicial = int(input('Ingresa el numero inicial: '))
numero_final = int(input('Ingresa el numero final: '))

while(numero_inicial <= numero_final):

    if(numero_inicial % 2 != 0):
        print(numero_inicial, 'es Impar')

    numero_inicial += 1