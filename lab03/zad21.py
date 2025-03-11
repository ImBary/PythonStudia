import random
import os

y = random.randint(1,100)
while(True):
    x = input("zgadnij liczbe: ")
    if(eval(x)==eval(y)):
        print("fajno zgadłes")
        break
    else:
        print("no nie fajno, nie zgadles")
    
