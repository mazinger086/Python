#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis
# y escribáis dentro del archivo.
# Para ello, tendréis que acceder dos veces al archivo creado.

f = open('mifichero.txt', 'w')
f.write("Datos\n")
f.write("Datos2\n")
f.close()



f = open('mifichero.txt', 'r')
datos = f.read()
f.close()

print(datos)



