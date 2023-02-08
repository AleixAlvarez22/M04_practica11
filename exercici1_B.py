def petitOGran(): #Demana 2 numeros i despres els compara i et diu quin es mes gran i quien es mes petit, si son iguals no diu res
    num1 = input("Escriu el primer número: ")
    num2 = input("Escriu el segon número: ")

    if num1 > num2:
        print("El número {num1} és més gran que {num2}".format(num1=num1, num2=num2))
    elif num2 > num1:
        print("El número {num2} és més gran que {num1}".format(num1=num1, num2=num2))

