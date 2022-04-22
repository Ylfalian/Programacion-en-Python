#bicicletas,motos,autos,camionetas,colectivos,camiones y acomplados.


class Autos:
    def __init__(self):
        Autos.marca= "Toyota"
        Autos.registro="1A8Q46"
        Autos.color="Azul"

class Camiones:
    def __init__(self):
        Camiones.marca="Mercedez"
        Camiones.registro="24A5E9"
        Camiones.color="verde"

class Motos:
    def __init__(self):
        Autos.marca= "Yamaha"
        Autos.registro="T48U86"
        Autos.color="Negro"

class Acoplados:
    def __init__(self):
        Acoplados.marca="Acoplado?"
        Acoplados.registro="24A5E9"
        Acoplados.color="rojo"

class Colectivo:
    def __init__(self):
        Colectivo.marca="Ford"
        Colectivo.registro="U8T6Y4"
        Colectivo.color="Verde"

class Camionetas: 
    def __init__(self):
        pass

class Bicicletas:
    def __init__(self):
        pass

taxi=Autos()
camion_trasporte=Camiones()
acople_trasporte=Acoplados()
linea56=Colectivo()
moto_deliveri=Motos()
bicicleta_deport=Bicicletas()
camioneta_policia=Camionetas()

camioneta_policia.marca=input("Ingrese la marca del vehiculo: ")
camioneta_policia.registro=input("\nIngrese la Patente del vehiculo: ")
camioneta_policia.color=input("\nIndique el color del vehiculo:")

print(f"\n\n La marca de su Vehiculo es {taxi.marca}, Patente {taxi.registro} y color {taxi.color}")

print(f"\n\n La marca de su Vehiculo es {camion_trasporte.marca}, Patente {camion_trasporte.registro} y color {camion_trasporte.color}")

print(f"\n\n La marca de su Vehiculo es {acople_trasporte.marca}, Patente {acople_trasporte.registro} y color {acople_trasporte.color}")

print(f"\n\n La marca de su Vehiculo es {linea56.marca}, Patente {linea56.registro} y color {linea56.color}")

print(f"\n\n La marca de su Vehiculo es {moto_deliveri.marca}, Patente {moto_deliveri.registro} y color {moto_deliveri.color}")

print(f"\n\n La marca de su Vehiculo es {bicicleta_deport.marca}, Patente {bicicleta_deport.registro} y color {bicicleta_deport.color}")

print(f"\n\n La marca de su Vehiculo es {camioneta_policia.marca}, Patente {camioneta_policia.registro} y color {camioneta_policia.color}")