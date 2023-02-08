def declaracio(): #Funcio que et demana la edat i els ingresos mensuals. Si tens mes de 18 i cobres mes de 1200 el programa et dirà si as de fer la declaració d'hisenda en cas contrari dira que encara no la pots fer
    edat = input("Introdueix la teva edat: ")
    ingressos = input("Introdueix els teus ingressos mensuals: ")

    edat = int(edat)
    ingressos = int(ingressos)

    if edat >= 18 and ingressos > 1200:
        print("És necessari que facis la declaració d'hisenda, ja que tens {edat} anys i cobres mes de {ingressos}€".format(edat=edat, ingressos=ingressos))
    else:
        print("Encara no pots fer la declaració.")

