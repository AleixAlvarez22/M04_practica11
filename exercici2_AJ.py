def escullUnNom(): #Donat un nom, es comproba si esta en la llista o no
    noms = ['Joan', 'Aleix', 'Pablo', 'Edgar', 'Carlos']
    nomEscollit = input("Escriu el teu nom: ")

    if nomEscollit not in noms:
        print("{nomEscollit} no esta en la llista d'aprobats".format(nomEscollit=nomEscollit))
    else:
        print("{nomEscollit} esta en la llista d'aprobats".format(nomEscollit=nomEscollit))

