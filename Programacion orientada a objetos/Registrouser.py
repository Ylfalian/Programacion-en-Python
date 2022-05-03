from Invitado import *

def Registro ():
    datosregis=[]
    datosregis.append (input("ingrese su mail\n"))
    datosregis.append (input("ingrese su contraseña. Debe contener algun caracter del tipo '!@#$%'\n"))
    while str.isalnum(datosregis[0]) is True or str.isalnum(datosregis[1]) is True :    
        print("A ocurrido un problema...")
        print("Verifique que el mail este bien escrito y que la contraseña contenga caracteres especiales.\n")
        datosregis[0]= input("Ingrese el mail nuevamente-----> ")
        datosregis[1]= input("Vuelva a ingresar la contraseña-----> ")
    datosregis= Invitado
    return(datosregis)