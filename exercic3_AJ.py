import random


def endivinaElNumero():
    numeroAEndevinar = random.randrange(0, 100)
    numeroClient = int(input("Escull un numero del 0 al 100: "))

    while numeroAEndevinar is not numeroClient:
        if (numeroAEndevinar == numeroClient):
            print("Molt bé! Has endevinat el número!")
            break
        elif (numeroAEndevinar < numeroClient):
            print("El número és més petit")
            numeroClient = int(input("Escull un numero del 0 al 100: "))
        elif (numeroAEndevinar > numeroClient):
            print("El número és més gran")
            numeroClient = int(input("Escull un numero del 0 al 100: "))

endivinaElNumero()