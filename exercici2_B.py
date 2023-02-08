def parellSenar(): #Et demana  un numero i despres et diu si es parell o senar

    numero = input("Escriu un número: ")
    numero = int(numero)
    if numero % 2 == 0:
        print("El número {numero} és parell.".format(numero=numero))
    else:
        print("El número {numero} és senar.".format(numero=numero))

