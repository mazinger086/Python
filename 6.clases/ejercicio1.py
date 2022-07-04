class Vehiculo:
    color = "blanco"
    ruedas = 4
    puertas= 4


class Coche(Vehiculo):
    velocidad = 140
    cilindrada = 1600

miCoche = Coche()


print("Color:", miCoche.color)
print("Cant ruedas:", miCoche.ruedas)
print("Cant puertas:", miCoche.puertas)
print("Max vel:", miCoche.velocidad)
print("Cilindrada:", miCoche.velocidad)