from random import randrange

liczba1 = randrange(1,3)
liczba2 = randrange(1,3)
liczba3 = randrange(1,3)
liczba4 = randrange(1,3)
liczba5 = randrange(1,3)
liczba6 = randrange(1,3)

losowanie = liczba1,liczba2,liczba3,liczba4,liczba5,liczba6

liczbaGracza1 = int(input("Wprowadz liczbę pierwszą: "))
liczbaGracza2 = int(input("Wprowadz liczbę druga: "))
liczbaGracza3 = int(input("Wprowadz liczbę trzecia: "))
liczbaGracza4 = int(input("Wprowadz liczbę czwarta: "))
liczbaGracza5 = int(input("Wprowadz liczbę piąta: "))
liczbaGracza6 = int(input("Wprowadz liczbę szósta: "))

liczbyGraczaAll = liczbaGracza1,liczbaGracza2,liczbaGracza3,liczbaGracza4,liczbaGracza5,liczbaGracza6

poprawne = 0

if liczba1 == liczbaGracza1
    poprawne = poprawne + 1
if liczba2 == liczbaGracza2
    poprawne = poprawne + 1
if liczba3 == liczbaGracza3
    poprawne = poprawne + 1
if liczba4 == liczbaGracza4
    poprawne = poprawne + 1
if liczba5 == liczbaGracza5
    poprawne = poprawne + 1
if liczba6 == liczbaGracza6
    poprawne = poprawne + 1

print("Wylosowane liczby: "+losowanie)
print("Twoje liczby: "+liczbyGraczaAll)
print("Zgadłeś "+poprawne+" liczby")