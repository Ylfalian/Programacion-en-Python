#Ejercicio 10-Perez Zavaleta Ramiro
from random import random


print("Adivine el numero")
numero=random[0,100]
ingreso=0
vidas=5

while vidas!=0:
    ingreso=float(input(f"Ingrese un numero--- tiene {vidas} vidas"))
    if ingreso==numero:
        print("Usted a adivinado el numero")
        break
    else:
        vidas=vidas-1

if vidas==0:
    print("Usted a perdido u.u")
