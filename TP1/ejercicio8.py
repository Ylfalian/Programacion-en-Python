from collections import Counter

vocales=["a","e","i","o","u"]
letra="a"
sig_eps=["~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}",";",":",",","<",".",">","/","?","|"]
dato_use=[]
voca=vocales[0]
suma=0#variable usada para contar en el while secundario
suma2=0#usado en contraseña
compa=0#usado en la seccion de la contraseña
f=0#contador en seccion contraseña
i=0
t=0
x=0
z=0
vocal_cont=0
print("Ingrese su nombre, luego su apellido, fecha de nacimiento y una contraseña\n")

for i in range(0,5):
    dato_use.append(input())
    while x<=2:
        Counter=Counter(dato_use[x])
        while vocal_cont<=3:
            Counter[letra]=suma
            vocal_cont=vocal_cont+suma
            t=t+1
            if t>5 and vocal_cont<3:
                break
        if t>5 and vocal_cont<3:
            break
    if t>5 and vocal_cont<3:
        print("El nombre y el apellido deben contener un minimo de 3 vocales")
        break
    if i==2:#año de nacimiento
        dato_use.append(int(input()))
        if dato_use<1900 or dato_use>2022:
            print("La fecha de nacimiento tiene que tene que ser valida")
            break
    if i==3:#contraseña
        dato_use.append(input())
        Counter=Counter(dato_use[3])
        while compa<1:
            Counter[sig_eps[f]]=suma2
            compa=compa+suma2
            f=f+1
            if f>30 and compa<1:
                break
        if f>30 and compa<1:
            break
    if f>30 and compa<1:
        print("Tiene que incluir un caracter especial en la contraseña")
        break

print(f"Hola {dato_use[0]} {dato_use[1]}")