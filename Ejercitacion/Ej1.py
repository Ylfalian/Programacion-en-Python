#Numero mayor,menor y suma del todos
from suma import sumar

i=1
z=1
digitos= []
confi="y"
menor=None
mayor=None
while i != 0:
    digitos.append(int(input("\nIngrese un numero----> ")))
    z+1
    if z/2:
        confi=input("\nIngrese una 'Y' para continuar y una 'N' para terminar------> ")
        confi.lower
    if confi=="n":
        i=0
    for numero in digitos:
        if menor==None and mayor==None:
            menor = numero
            mayor = numero
        else:
            if numero<menor:
                menor=numero
            if numero>mayor:
                mayor=numero



print (f"el numero mayor es {mayor}")
print (f"el numero menor es {menor}")
print (f"La suma de todos los numeros es {sumar(digitos)}")







