from random import randrange
import random
status = True
proby = 0

while status == True:
    haslo = []
    
    for x in range(4):
        haslo.append(randrange(0,10))
    print(haslo)
    hasloPo = (haslo[0]+haslo[1]+haslo[2]+haslo[3])
    print(hasloPo)
    hack = 0
    # while (hack != hasloPo):
    #     hack = random.randint(0,9999)
    #     proby = proby + 1
    #     print(hack)

    znak = 'c'
    znak
    print(ord(znak)+1)

    print("Ustawione hasło: " + str(haslo))
    print("Złamane hasło: " + str(hack))
    print("Złamano po " +str(proby)+ "probach")
    jeszczeRaz = int(input("Czy złamać hasło jeszcze jaz ??? YES(1) NO(2): "))
    if(jeszczeRaz == 1):
        status = True
    else:
        ststus = False

    
 
    
    
    
