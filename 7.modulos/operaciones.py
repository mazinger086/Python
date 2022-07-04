
def calificaciones():
    alumno = input('Ingrese nombre de alumno: ')
    nota = input('Ingrese nota de alumno: ')
    resultado = "El Alumno " + alumno + " tiene un " + nota

    def checkCalificacion(nota):
        estado = ""
        if(nota >= 7 and nota <= 10):
            estado = "Promocionado"
        elif(nota >= 4 and nota <= 6):
            estado = "Aprobado"
        elif(nota <= 3):
            estado = "Desaprobado"
        else:
            estado = "Por favor ingrese un valor valido del 1 al 10"

        return estado

    estado = checkCalificacion(int(nota))

    print(resultado, estado)


def como_me_llamo(nombre):
    return "Yo me llamo: "+ nombre

class Calculadora:
    def multipicacion(self, a,b):
        return a * b

    def division(self,a,b):
        return a / b

    def suma(self,a,b):
        return a + b

    def resta(self, a,b):
        return a - b

    def resto(selfa,a, b):
        return a % b
