from random import randrange

wylosowanaLiczba = randrange(1,11)

graAktywna = True

licznikProb = 0

while graAktywna == True:
    
    print(wylosowanaLiczba)
    licznikProb = licznikProb + 1
    liczbaGracza = int(input("Podaj liczbe:"))
    
    if(liczbaGracza == wylosowanaLiczba):
        
        print("WYGRAŁEŚ GRATULACJĘ")
        
        print ("Zgadles w " + str(licznikProb) + " probach") #czymu str a nie np. int??
        jeszczeRaz = int(input("Czy chcesz zagrać jeszcze raz YES(1) or NO(2) ???"))
        if(jeszczeRaz == 1):
            #graAktywna = True #dlaczego to tu musi być?? jak było tylko to..
            licznikProb = 0
            wylosowanaLiczba = randrange(1,11)
        else:
            graAktywna = False
    else: 
        print("Przegrales, spróbuj ponownie.")

print("Dzięki za grę, mam nadzieję że znów kiedyś pogramy :)")