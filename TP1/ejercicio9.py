#Ejercicio 9-Perez Zavaleta Ramiro
#calculadora simple
from typing import no_type_check


operaciones=input("Seleccione 1 para sumar, 2 para restar, 3 para multiplicar y 4 para dividir\n")
i=0
resultado=0
numeros=[]
print("ingrese los numero a operar")
for i in range(0,2):
    numeros.append(float(input()))
    i=i+1


if operaciones==1:
    resultado=numeros[0]+numeros[1]
    print(f"El resultado es {resultado}")
elif operaciones==2:
    resultado= numeros[0]-numeros[1]
    print(f"El resultado es {resultado}")
elif operaciones==3:
    resultado=numeros[0]*numeros[1]
    print(f"El resultado es {resultado}")
elif operaciones==4:
    resultado=numeros[0]/numeros[1]
    print(f"El resultado es {resultado}")
