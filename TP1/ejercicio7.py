#input de datos 
datos_user=[]
i=0#las letras sueltas son utilizadas como variables contadoras para el for o while
print("ingrese su Nombre, edad, el dinero que hay en su billetera y el habre que tiene (del 0 al 10)\n")
for i in range(0,4):
    if i==0:
        datos_user.append(input())
    elif i==2:
        datos_user.append(float(input()))
    else:
        datos_user.append(int(input()))
    i=i+1

if datos_user[1]>34 and datos_user[2]>500 and datos_user[3]>5:
    print(f"Hola {datos_user[0]}, ¿Hoy hay asado?")
elif datos_user[3]<7 or datos_user[2]<100 and datos_user[1]<18:
    print(f"Hola {datos_user[0]} ¿Vas a comer a lo de tus padres?")
elif datos_user[1]<=35:
    print(f"Hola {datos_user[0]}. Eres una persona joven ya que tu edad es {datos_user[1]}.")