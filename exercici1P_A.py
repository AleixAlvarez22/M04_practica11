def dosNumeros():
    numero1 = input("Escriu un numero")
    numero2 = input("Escriu un altre numero")
    if numero1 > numero2:
        print('El {numero1} és el més gran i el {numero2} el més petit'.format(numero1=numero1, numero2=numero2))
    elif numero1 < numero2:
        print('El {numero2} és el més gran i el {numero1} el més petit'.format(numero1=numero1, numero2=numero2))
    else:
        print('Els numeros son iguals')



