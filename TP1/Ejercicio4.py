#Autor:Perez Zavaleta Ramiro
print("Ingrese los valores a dividir\n")
valores=[]
i=0
for i in range(0,2):
    valores.append(float(input("--")))
    i=i+1
resultado=valores[0]%valores[1]
if resultado==0:
    print(f"El numero {valores[0]} es divisible por {valores[1]}")
else:
    print(f"El numero {valores[0]} no es divisible por {valores[1]}")

print("\n Fin.")
