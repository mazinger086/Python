import pprint

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
#print(f"El numero es {numero} y el texto {texto} y tiene {otromas}")


class Juguete:
    nombre = ""
    precio = 0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"El juguete {self.nombre} tiene un precio de: {self.precio}"

j1 = Juguete("Potato", 12.5) #Imprime la representacion de python

#print(j1)

#Metodos strings:

#cadena = "  en un  lugar  de  la  mancha   "
#numero = 'a2'
# Lower
#cadena = cadena.lower()
# Upercase
#cadena = cadena.upper()
# Capitalize (Solo aplica a la primer Letra)
#cadena = cadena.capitalize()
# Title (Uppercase a cada primer palabra)
#cadena = cadena.title()
# Count (Cuenta las letras)
#cadena = cadena.split(' ')
#cadena = cadena.count('a')
#isdigit (Retorna un Booleano si es un digito o no )
#isaplpha (verifica si es alfabetico)
#isanum (verifica si es alfanumerico)
#strip (Elimina los espacios por delante y detras)
#split (Separa por partes)
#cadena = cadena.split()
#cadena = " ".join(cadena)
#endswith('nombre')

# manipulacion de ficheros

#LEYENDO FICHEROS#
f = open('C:\\Users\\v-dlasauskas\\Desktop\\test.txt', 'r')
#datos = f.read() # Lee todos
#datos = f.readline()# lee la primer linea
datos = f.readlines()



f.close()

pprint.pprint(datos)

# r: lectura
# a: append
# w: escritura
# x: create

# t: texto
# b: binary

# +


