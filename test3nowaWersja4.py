from random import randrange
import random
status = True
proby = 0

while status == True:
    haslo = []
    for x in range(6):
        haslo = randrange(0,10)
    status = False
    print(haslo)
    
