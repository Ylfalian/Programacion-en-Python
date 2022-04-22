#Piedra, Papel o Tijera
import numpy as np
import time

opciones = {"piedra":"tijera","tijera":"papel","papel":"piedra"}
vic = 0
vic_pc = 0
i = 1

while i != 0 :
    #Condicion de salida
    if vic == 3:
        break
    elif vic_pc == 3:
        break
    
    #Entrada del jugador
    player = input("Selecciona entre piedra, papel o tijera: ")
    while player not in {"piedra", "papel","tijera"}:
        print("Cometiste un erro... ")
        player = input("\nSelecciona entre piedra, papel o tijera: ")
    
    #Seleccion de la PC
    
    pc = np.random.choice(["piedra","papel","tijera"])
    #Mostrar el resultado
    
    time.sleep(.5)
    print("\n Has seleccionado;", player)
    print("La maquina a elejido", pc, "\n")
    time.sleep(.5)
    #Determinar el ganador
    
    if opciones[player] == pc:
        print("Has ganado!!!")
        vic = vic + 1
    elif opciones[pc] == player:
        print("Has Perdido u.u")
        vic_pc = vic_pc + 1
    else:
        print("Empate!!!")
    



if vic == 3:
    print("ERES EL REY DE LOS DUELOS!!!!!!")
elif vic_pc == 3:
    print("FALTO PRACTICA U.U")