import random

caracteres = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
caracteresEspeciales = "!#$%&/()=?¿¡*+"

combinacion = ""

def crearComb(longitud):
    global combinacion
    combinacion = ""
    for i in range(0, longitud):
        comb = random.choice(caracteres + caracteres.upper() + numeros + caracteresEspeciales)
        combinacion += comb
        
    return combinacion

       
    

