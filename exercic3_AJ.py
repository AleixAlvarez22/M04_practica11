import random

def endivinaElNumero(): #Donat un numero, el compara amb un numero random.
    numeroAEndevinar = random.randrange(0, 100)
    numeroClient = int(input("Escull un numero del 0 al 100: "))
    trobat = False
    max = 100
    min = 0
    while not False:
        if (numeroAEndevinar == numeroClient):
            print("Molt bé! Has endevinat el número!")
            trobat = True
            break
        elif (numeroAEndevinar < numeroClient):
            max = numeroClient
            print("El número és més petit que {numeroClient}".format(numeroClient=numeroClient))
            numeroClient = int(input("Escull un numero del {min} al {max}: ".format(min=min, max=max)))
        elif (numeroAEndevinar > numeroClient):
            min = numeroClient
            print("El número és més gran que {numeroClient}".format(numeroClient=numeroClient))
            numeroClient = int(input("Escull un numero del {min} al {max}: ".format(min=min, max=max)))

