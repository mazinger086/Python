#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos
# su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje
# con el resultado de la nota y si ha aprobado o no.

class Alumno:
    nombre = None
    nota = None

    def check(self, nota):
        resultado = None
        if (nota >= 4 and nota <= 7):
            resultado = "Aprobado"
        elif (nota > 7):
            resultado = "Promocionado"
        else:
            resultado = "Reprobado"

        return resultado

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        mensaje = self.check(nota)
        print("El Alumno", nombre, "tiene una nota", nota, "y ha", mensaje)



a1 = Alumno('Gisela', 7)
a2 = Alumno('Daniel', 4)
a3 = Alumno('Julio', 2)
a4 = Alumno('Emilia', 10)







