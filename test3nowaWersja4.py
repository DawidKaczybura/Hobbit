from random import randrange
import random
status = True
proby = 0

while status == True:
    haslo = []
    
    for x in range(4):
        haslo.append(randrange(0,10)) # jak daje samo 10 to też działa, dlaczego??
    
    hack = 0
    while (hack != haslo):
        hack = random.randint(0,9999)
        print(hack)

    print("Ustawione hasło: " + str(haslo))
    print("Złamane hasło: " + str(hack))

    jeszczeRaz = int(input("Czy złamać hasło jeszcze jaz ??? YES(1) NO(2): "))
    if(jeszczeRaz == 1):
        status = True
    else:
        ststus = False

    
    
    
    
    
