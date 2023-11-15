import os
from art import *
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    SKYBLUE = '\033[36m'
    ORANGE = '\033[33m'

def Registro(): #debe tener registrado un usuario con una contraseña para poder acceder
    os.system("cls")
    print(bcolors.RED + bcolors.BOLD)
    tprint("Password Manager", font="small")
    print(bcolors.GREEN + bcolors.BOLD)
    tprint("By: San1190", font="small")
    print(bcolors.ENDC)
    print(bcolors.BOLD + bcolors.SKYBLUE)
    print("¿Qué desea hacer?")
    print(bcolors.ENDC)
    print(bcolors.SKYBLUE)
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = int(input("Elija una opción: " + bcolors.ORANGE))
    print(bcolors.SKYBLUE)
    return opcion
    

def Inicio():
    os.system("cls")
    print(bcolors.RED + bcolors.BOLD)
    tprint("Sesion iniciada", font="small")
    print(bcolors.ENDC)
    print(bcolors.BOLD + bcolors.SKYBLUE)
    print("¿Qué desea hacer? \n")
    print(bcolors.ENDC)
    print(bcolors.SKYBLUE)
    print("1. Crear contraseña")
    print("2. Leer contraseña")
    print("3. Cerrar sesión")
    print("4. Borrar usuario")
    print("5. Borra contraseña")
    print("6. Salir")
    opcion = int(input("Elija una opción: " + bcolors.ORANGE))
    print(bcolors.SKYBLUE)
    return opcion


def Error(num_Error):
    os.system("cls")
    print(bcolors.RED)
    if num_Error == 1:
        print("No ha introducido un número\n")
        input("Pulse enter para continuar...")
        os.system("cls")
        
    elif num_Error == 2:
        print("No se ha podido crear el fichero\n")
        input("Pulse enter para continuar...")
        os.system("cls")
    elif num_Error == 3:
        print("No se ha podido escribir en el fichero\n")
        input("Pulse enter para continuar...")
        os.system("cls")
    elif num_Error == 4:
        print("El usuario ya existe\n")
        input("Pulse enter para continuar...")
        os.system("cls")
    elif num_Error == 5:
        print("La contraseña o el usuario son incorrectos\n")
        input("Pulse enter para continuar...")
        os.system("cls")
    elif num_Error == 6:
        
        print("No se ha podido registrar el usuario\n")
        input("Pulse enter para continuar...")
        os.system("cls")
    elif num_Error == 7:
        print("No se ha podido borrar el fichero\n")
        input("Pulse enter para continuar...")
        os.system("cls")

    print(bcolors.ENDC)
        

def Despedida():
    os.system("cls")
    print(bcolors.ORANGE + bcolors.BOLD)
    print("Gracias por usar la aplicación")
    exit()

def CerrarSesion():
    os.system("cls")
    print("Sesión cerrada con éxito")
    input("Pulse enter para continuar...")
    os.system("cls")

def RegistroCorrecto(usuario, contraseña):
    os.system("cls")
    print(bcolors.SKYBLUE)
    print("Usuario registrado con éxito")
    print("Su usuario es: " + usuario)
    print("Su contraseña es: " + contraseña)
    print("Guarde estos datos en un lugar seguro")
    input("Pulse enter para continuar...")
    os.system("cls")