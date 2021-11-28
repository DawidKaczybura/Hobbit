from random import randrange

wylosowanaLiczba = randrange(1,11)
#print(wylosowanaLiczba)
graAktywna = True

licznikProb = 0


while graAktywna == True:
    
    licznikProb = licznikProb + 1
    liczbaGracza = int(input("Podaj liczbe:"))
    
    if(liczbaGracza == wylosowanaLiczba):
        
        print("Wygrales")
        graAktywna = False
    else: 
        print("Przegrales, spróbuj ponownie.")
   




print ("GRATULACJE KONIEC GRY")
print ("Zgadles w " + str(licznikProb) + " probach")
jeszczeRaz = int(input("Czy chcesz zagrać jeszcze raz Y or N ???"))
if(jeszczeRaz == 1):
    graAktywna = True
else:
    print("Dzięki za grę, mam nadzieję że znów kiedyś pogramy")
