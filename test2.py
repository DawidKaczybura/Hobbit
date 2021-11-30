from random import randrange

losowaLiczba = randrange(1,11)

graAktywna = True

iloscProb = 0

while graAktywna == True:
    print(losowaLiczba)
    iloscProb = iloscProb + 1
    liczbaGracza = int(input("Podaj liczbę: "))

    if (liczbaGracza == losowaLiczba):
        print ("Gratulacje wygrales ! ! !")
        print ("Zgadłeś w "  + str(iloscProb) + " próbach")
        
        jeszczeRaz = int(input("Chcesz zagrać jeszcze raz? YES(1) NO(2): "))
        if (jeszczeRaz == 1):
            losowaLiczba = randrange(1,11)
            iloscProb = 0

        else:
            graAktywna = False
    else:
        print ("Niestety przegrales, sprobuj jeszcze raz..")

print ("Dzięki za gre, do następnego razu :)")