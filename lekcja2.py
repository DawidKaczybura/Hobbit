from random import randrange

wylosowanaLiczba = randrange(1,11)

graAktywna = True

licznikProb = 0

while graAktywna == True:
    
    print(wylosowanaLiczba)
    licznikProb = licznikProb + 1
    liczbaGracza = int(input("Podaj liczbe:"))
    
    if(liczbaGracza == wylosowanaLiczba):
        
        print("Wygrales")
        
        print ("GRATULACJE KONIEC GRY")
        print ("Zgadles w " + str(licznikProb) + " probach")
        jeszczeRaz = int(input("Czy chcesz zagrać jeszcze raz YES(1) or NO(2) ???"))
        if(jeszczeRaz == 1):
            #graAktywna = True #dlaczego to tu musi być?? jak było tylko to..
            licznikProb = 0
            wylosowanaLiczba = randrange(1,11)
        else:
            print("Dzięki za grę, mam nadzieję że znów kiedyś pogramy")
            graAktywna = False
    else: 
        print("Przegrales, spróbuj ponownie.")
