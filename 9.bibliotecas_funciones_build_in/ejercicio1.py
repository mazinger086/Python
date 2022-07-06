# Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

lista = []


while len(lista) != 5:
    ingreso = input('Ingrese un pais: ')
    lista.append(ingreso.lower())



norepeated = set(lista)
norepeated = list(norepeated)
norepeated = sorted(norepeated)

print(norepeated)