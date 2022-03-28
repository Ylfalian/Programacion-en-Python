#Ejercicio 2 Perez Zavaleta Ramiro
print("Ingre los valores para calcular el area del triangulo\n")
x=0
triangulo=[]
for x in range(0,3):
    triangulo.append(float(input("---")))
    x=x+1
    if x==3:
        area=sum(triangulo)
        print(f"El area del triangulo es de {area} ")
