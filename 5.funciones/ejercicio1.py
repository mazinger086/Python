#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros
# y otra función que calcule el área de un círculo recibiendo el radio del mismo

base = float(input('Ingrese la base del triangulo: '))
altura = float(input('Ingrese la altura del triangulo: '))

def areaTriangulo(base, altura):
    area = base * altura / 2
    return area

resultado = areaTriangulo(base, altura)
print('El area del triagulo es: ', resultado)
