from glob import escape


print("Ingrese el nombre de sus amigos.\n Para salir escriba exit.\n")
amigos=[]
salir="exit"
ex="o"
cont=1
x=0
while cont!=0:
    amigos.append(str(input()))
    ex=amigos[x]
    x=x+1
    if ex==salir:
        cont=0
        x=x-1
        amigos.pop(x)
x=x-1
print("Sus amigos son:\n")
while x>=0:
    print(amigos[x], end="-")
    x=x-1
print("\n Fin.")