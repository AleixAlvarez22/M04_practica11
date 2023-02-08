import random
def num0100():
    numeroCorrecte = random.randrange(0,100)
    numeroClient = input("Escriu un numero entre 0 i 100 : ")
    numeroClient = int(numeroClient)
    superior = 100
    inferior = 0
    while numeroClient != numeroCorrecte:
        if numeroClient < numeroCorrecte:
            print("El número és més gran")
            inferior = numeroClient
            int(input("Escriu un numero entre {inferior} i {superior} : ".format(inferior=inferior, superior=superior)))
        elif numeroClient > numeroCorrecte:
            print("El número és més petit")
            superior = numeroClient
            int(input("Escriu un numero entre {inferior} i {superior} : ".format(inferior=inferior, superior=superior)))

    if numeroClient == numeroCorrecte:
     print("Molt bé! Has endevinat el número!")
