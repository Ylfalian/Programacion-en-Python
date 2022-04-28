#orden de palabras alfabeticamente
from textwrap import shorten


c = 1
f = 0
confi = "y"
lista = []

while c!=0:
    lista.append(input("\nIngrese alguna palabra o nombre (Ingrese 'EXIT' para terminar) =====> "))
    if lista[f] == "EXIT":
        lista.pop(f)
        c = 0
    f = f + 1

orden_lista= sorted(lista)

print(f"Se a ordenado la lista {orden_lista}")