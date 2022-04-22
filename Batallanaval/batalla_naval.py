import numpy as np

filas = 10
columnas = 10

arreglo_vacio = np.zeros([filas,columnas])
barcos = np.array([ [1,0,0,0,0,0,0,0,1,0],
                    [1,0,0,0,0,0,0,0,1,0],
                    [1,0,0,0,0,0,0,0,1,0],
                    [1,0,0,0,0,0,0,0,0,0]
                    [0,0,0,1,1,1,1,0,0,0]
                    [0,0,0,0,0,0,0,0,0,0]
                    [0,0,0,0,0,0,0,0,1,0]
                    [0,0,0,0,0,0,0,0,1,0]
                    [0,0,0,0,0,0,0,0,1,0]
                    [0,0,0,0,0,0,0,0,1,0]])
vidas = 5
arreglo_vacio = barcos
x=0
print("Derriba los buques enemigos en un mapa de 10x10")

while vidas > 0:
    fila = int(input("Ingresa n° de fila: "))
    columna = int(input("Ingresa n° de columa: "))

    if barcos[fila-1,columna-1] and arreglo_vacio [fila-1,columna-1] == 1:
        print("Me diste!!!")
        arreglo_vacio[fila-1,columna-1]=0
        x +=1
    else:
        print("Ya disparaste en lugar o no hay nada!")
        vidas -=1
        print("te quedan...♥",vidas,"vidas")
    if x == 15:
        vidas = 0

if vidas == 0 and x == 15:
    print("GANASTE")
