def noms():
    nom = input("Escolleix un nom dels seguents: Wenceslao, Di Maria, Julián, Mariano, Aleix : ")
    if nom == "Wenceslao":
        print("Senyor {nom} la seva solicitud per saltar en paracaigudes sense paracaigudes ha sigut rebutjada".format(nom=nom))
    elif nom == "Di Maria":
        print('{nom} va participar en un els gols de la selecció Argentina en la victoria als francesos'.format(nom=nom))
    elif nom == "Julián":
        print('{nom} va ser un dels jugadors que mes gols van fer a la copa del món 2022'.format(nom=nom))
    elif nom == "Mariano":
        print("Haré todo lo que pueda y un poco más de lo que pueda si es que eso es posible, "
              "y haré todo lo posible e incluso lo imposible si también lo imposible es posible")
    elif nom == "Aleix":
        print('{nom} va rebre el premi al millor alumne del dia 30 de febrer'.format(nom=nom))
    else:
        print('{nom} no esta en la llista'.format(nom=nom))



