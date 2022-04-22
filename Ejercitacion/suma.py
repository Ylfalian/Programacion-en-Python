def sumar(digitos) :
    if digitos == []:
        return 0
    else:
        return digitos[0] + sumar(digitos[1:])