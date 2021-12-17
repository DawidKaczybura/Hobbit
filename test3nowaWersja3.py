from random import randrange
import random
poprawne = 0
status = True
tablica = [1,2,3,4,5,6,7,8,9]

while status == True:
    losowanie = []
    losowanie.append(random.choice(tablica))
    tablica.remove(losowanie[0]) #pozycja 0 w liście 
    losowanie.append(random.choice(tablica))
    tablica.remove(losowanie[1])
    losowanie.append(random.choice(tablica))
    tablica.remove(losowanie[2])
    losowanie.append(random.choice(tablica))
    tablica.remove(losowanie[3])
    losowanie.append(random.choice(tablica))
    tablica.remove(losowanie[4])
    losowanie.append(random.choice(tablica))
    tablica.remove(losowanie[5])

    #losowanie = liczba1,liczba2,liczba3,liczba4,liczba5,liczba6

    liczbaGracza1 = int(input("Wprowadz liczbę pierwszą: "))
    liczbaGracza2 = int(input("Wprowadz liczbę druga: "))
    liczbaGracza3 = int(input("Wprowadz liczbę trzecia: "))
    liczbaGracza4 = int(input("Wprowadz liczbę czwarta: "))
    liczbaGracza5 = int(input("Wprowadz liczbę piąta: "))
    liczbaGracza6 = int(input("Wprowadz liczbę szósta: "))

    liczbyGraczaAll = liczbaGracza1,liczbaGracza2,liczbaGracza3,liczbaGracza4,liczbaGracza5,liczbaGracza6




    if (losowanie[0] in liczbyGraczaAll):
        poprawne = poprawne + 1
    if (losowanie[1] in liczbyGraczaAll):
        poprawne = poprawne + 1
    if (losowanie[2] in liczbyGraczaAll):
        poprawne = poprawne + 1
    if (losowanie[3] in liczbyGraczaAll):
        poprawne = poprawne + 1
    if (losowanie[4] in liczbyGraczaAll):
        poprawne = poprawne + 1
    if (losowanie[5] in liczbyGraczaAll):
        poprawne = poprawne + 1
    
    print("Wylosowane liczby: " + str(losowanie))
    print("Twoje liczby:      " + str(liczbyGraczaAll))
    print("Zgadłeś " + str(poprawne) + " liczby")

    jeszczeRaz = int(input("Chcesz zagrać jeszcze raz? YES(1) NO(2): "))
    if(jeszczeRaz == 1):
        poprawne = 0
        status = True
    else:
        status = False

print("KONIEC GRY")