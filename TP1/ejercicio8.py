#Ejercicio 8-Perez Zavaleta Ramiro
from collections import Counter

datos_user=[]# Datos del usuario
suma=0#verificacion contador result
i=0# contador del primer while
z=0#contador del segundo while
chek=0

print("Ingrese su nombre, apellido, año de nacimiento y una contraseña\n")

while i<4:
    if i!=2:
        datos_user.append(input())
    else:
        datos_user.append(int(input()))
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
        chek=chek+1
        break
    elif suma<3:
        print("nombre invalido")
        break

if datos_user[2]<1000 or datos_user[2]>9999:
    print("Fecha de nacimiento invalida.")
else:
    chek=chek+1

if str.isalnum(datos_user[3]) is True:
    print("la contraseña tiene que tener caracteres especiales")
else:
    chek=chek+1

if chek==3:
        print(f"\nbienvenido {datos_user[0]} {datos_user[1]} ")
