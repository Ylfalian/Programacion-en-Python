#Numero mayor,menor y suma del todos
from suma import sumar

i=1
z=0
digitos= []
menor=None
mayor=None
while i != 0:
    digitos.append(input("\nIngrese un numero (ingrese exit para salir) ----> "))
    compar = digitos[z]
    z= z + 1
    if compar == "exit":
        z= z - 1
        digitos.pop(z)
        i= 0
    int_digi = [int(c) for c in digitos]
    for numero in int_digi:
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
print (f"La suma de todos los numeros es {sumar(int_digi)}")







