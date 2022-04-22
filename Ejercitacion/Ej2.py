#orden de palabras alfabeticamente
from textwrap import shorten


c = 1
f = 0
confi = "y"
lista = []

while c!=0:
    lista.append(input("\nIngrese alguna palabra o nombre =====> "))
    f= f + 1
    if f >= 2:
        confi = input("\nIngrese una 'Y' si desea continuar, caso contrario ingrese 'N' para salir ------> ")
        confi.lower
    if confi == "n":
        c=0

orden_lista= sorted(lista)

print(f"Se a ordenado la lista {orden_lista}")