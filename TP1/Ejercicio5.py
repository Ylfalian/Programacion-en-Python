#Ejercicio 5-Perez Zavaleta Ramiro
from itertools import count

print("Ingrese los numeros a comaparar:\n")
numeros=[]
x=0

while x<=2:
    numeros.append(float(input("--")))
    x=x+1

if numeros[0]>=numeros[1] and numeros[0]>=numeros[2]:
    print(f"\nEl numero {numeros[0]} es mayor")
elif numeros[1]>=numeros[0] and numeros[1]>=numeros[2]:
    print(f"\nEl numero {numeros[1]} es mayor")
elif numeros[2]>=numeros[0] and numeros[2]>=numeros[1]:
    print(f"\nEl numero {numeros[2]} es mayor")

print("\nFin.")
