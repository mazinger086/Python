#Clases Dinamicas
"""
class Juguete:
    encendido = True

    def enciende(self):
        self.estado = True

    def apaga(self):
        self.estado = False

    def isEncendido(self):
        return self.encendido;

class Potato(Juguete): # De esta manera hacemos la  herencia en Python
    def quitarOreja(self):
        print('Quite oreja')

    def quitarNariz(self):
        print('Quite nariz')

class Dino:
    color = None
    nombre = None


    def __init__(self, nombre):
     self.color = nombre
     self.nombre = "Verde"



    def hacerRuido(self):
        print('Roarrrr...')


p1 = Potato()
d1 = Dino('T-Rex')
print(d1.color)
print(d1.nombre)

#Clases Estaticas

class Opciones:
    ServidorSeguro = True
    Reiniciar = False

if Opciones.ServidorSeguro:
    print('El servidor es seguro')
"""

"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

    def diHola(self):
        print("Hola")

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

p = Perro()
g = Gato()

p.sonido()
p.diHola()
g.sonido()
g.diHola()

"""

#COMPOSICION

class Categorias:
    idCategoria = 0
    nombre = "Bazar"

class Proveedores:
    idProveedor = 0
    nombre = ""

class Productos:
    idProducto = 0
    CategoriaProducto = Categorias()
    Precio = 0
    Tamaño = 0
    TipoDeProducto = 0
    CIFProveedor = Proveedores()


producto = Productos()

print("ID:",producto.idProducto)
print("Categoria:", producto.CategoriaProducto.nombre)


