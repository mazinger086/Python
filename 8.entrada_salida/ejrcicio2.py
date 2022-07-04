# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle

class Vehiculo:
    motor = 0
    combustible = ""

    def __init__(self, motor, combustible):
        self.motor = motor
        self.combustible = combustible

"""
#Creamos el archivo bin con pickle
coche = Vehiculo(1.9, "Diesel")
f = open('datos.bin', 'wb')
pickle.dump(coche, f)
f.close()"""

# Leemos el archivo bin con pickle
f = open('datos.bin', 'rb')
coche = pickle.load(f)
f.close()

print(type(coche))
print(coche.motor, coche.combustible)




