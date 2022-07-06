from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

def miFuncion(x):
    if x % 2 != 0:
        return True
    return False

impares = filter(miFuncion, numeros) # [1,3,5,7,9]
impares = list(impares)


def sumarImpares(a, b):
    return a + b

resultado = reduce(sumarImpares, impares)

print(f"El resultado de sumar la lista {impares} da como resultado {resultado}")