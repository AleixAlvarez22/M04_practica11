def comparacio():
    numero1 = input("Digues el numero 1: ")
    numero2 = input("Digues el numero 2: ")

    if (numero1 == numero2):
        print("El numero {numero1} i el numero {numero2}, son iguals".format(numero1=numero1, numero2=numero2))
    elif (numero1 < numero2):
        print("El numero {numero2} es més gran que el numero {numero1}".format(numero1=numero1, numero2=numero2))
    else:
        print("El numero {numero1} es més gran que el numero {numero2}".format(numero1=numero1, numero2=numero2))

comparacio()