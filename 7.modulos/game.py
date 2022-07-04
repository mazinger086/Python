import random

x = 3
magicNumber = random.randint(1,10)

while x > 0:

    print('oportunidades:', x)
    x -= 1
    numero = int(input('Ingresa un numero: '))
    if x == 0:
        print('Perdiste, intentalo de nuevo')
    if numero == magicNumber:
        print('Felicidades adivininaste el numero')
        break