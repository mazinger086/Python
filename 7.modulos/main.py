#importamos el paquete con el modulo suma
import operaciones2.suma

# p print nos muesta los directorios de una manera mas amigable
import pprint
import math



def main():
    lista = []
    #Con dir([nombre_objeto]) listamos los modulos y paquetes que contiene una libreria importada
    #pprint.pprint(dir(lista))
    #print('==============')
    #pprint.pprint(dir(math))



    def test():
        print('Hola')

    test()

    pprint.pprint(globals())



if __name__ == '__main__':
    main()