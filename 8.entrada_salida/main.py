#ENTRADA Y SALIDA


numero = 511
texto = "quijote"
otromas = 1.2

# Formateando datos

#old
#print("El numero es %d y el texto %s y tiene %.1f" % (numero, texto, otromas))

# 2.7 to 3.6
#print("El numero es {} y el texto {} y tiene {}".format(numero, texto, otromas))

# 3.10 => son como los template strings
print(f"El numero es {numero} y el texto {texto} y tiene {otromas}")