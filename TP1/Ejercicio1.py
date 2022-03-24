#Ejercicio 1 - Perez Zavaleta Ramiro
materias=["lengua","matematica","fisica","quimica"]
cont=4
while cont>0:
    momentaneo=str(input("\nSeleccione una materia para cargar las notas\nLengua\nMatematica\nFisica\nQuimica\n\n-"))
    mate_selecc=momentaneo.lower()
    if mate_selecc in materias:
        nota1=float(input("\nIngrese la Primer Nota:"))
        nota2=float(input("\nIngrese la Segunda Nota:"))
        nota3=float(input("\nIngrese la Tercera Nota:"))
        promedio=(nota1+nota2+nota3)/3
        if promedio>=8:
            print(f"\nEl Alumno a promocionado con {promedio}\n")
        elif promedio>=6 and promedio<8:
            print(f"\nEl Alumno a aprobado con {promedio} y debe rendir un final\n")
        else:
            print(f"\nEl Alumno a desaprobado\n")
        cont=cont-1
print("Fin")