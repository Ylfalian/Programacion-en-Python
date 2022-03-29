<<<<<<< HEAD
#Ejercicio 8-Perez Zavaleta Ramiro
from collections import Counter

datos_user=[]# Datos del usuario
suma=0#verificacion contador result
suma2=0
i=0# contador del primer while
z=0#contador del segundo while
x=0#contador del tercer while
h=0#contador for
simbolos=["!","@","#"]
verif_sim=0
print("Ingrese su nombre, apellido, año de nacimiento y una contraseña\n")

while i<4:
    datos_user.append(input())
    i=i+1

while z<=1:
    Counter=Counter(datos_user[z])
    a=Counter["a"]
    e=Counter["e"]
    i=Counter["i"]
    o=Counter["o"]
    u=Counter["u"]
    suma=a+e+i+o+u
    z=z+1
    if suma>=3:
        break
    elif e>4 and suma<3:
        print("nombre invalido")
        break

<<<<<<< HEAD
if datos_user[2]<1000 or datos_user>9999:
    print("Fecha de nacimiento invalida.")

for h in range(0,4):
    Counter= Counter(datos_user[3])
    verif_sim=Counter[simbolos[h]]
    suma2=suma2+verif_sim
    h=h+1
    if suma2>=1:
        print("goddd")
        break
