import os
from time import sleep
from crearComb import crearComb as cC
from textos import *
from cifrado import *
from ficheros import *
import pyperclip
from art import *
check = False 
usuario = ""  

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


def Registrarse():
   tick = False
  
   usuario = str(input("Enter your username: " + bcolors.ORANGE)).strip().lower()
   print(bcolors.SKYBLUE)
   contraseña = getpass().strip()
   if crear_directorio(usuario):

       escribir_contrasena_usuario(usuario, contraseña)
       tick = True
   else:
       Error(4)

   return usuario, contraseña, tick


def IniciarSesion():
   global usuario
   usuario = input("Enter your username: " + bcolors.ORANGE).strip().lower()
   print(bcolors.SKYBLUE)
   contraseña = getpass().strip()
   return contraseña == leer_contrasena_usuario(usuario)
       

def CrearContraseña():
   global usuario
   while True:
       try:
           longitud = int(input("Enter the length of the password: " + bcolors.ORANGE))
           print(bcolors.SKYBLUE)
           break
       except:
           Error(1)
   contraseña = cC(longitud)
   while True:
       try:
           nombre = input("Enter the indicator with which you want to save the password: " + bcolors.ORANGE)
           print(bcolors.SKYBLUE)
           try:
               crear_fichero(nombre, usuario)
               escribir_fichero(nombre,usuario, contraseña)
               break
           except:
               Error(2)
       except:
           Error(1)
   return contraseña


def LeerContraseña():
   num = int(input("Enter the indicator of the password you want to read: " + bcolors.ORANGE))
   print(bcolors.SKYBLUE)
   try:
       contraseña = leer_fichero(num, usuario)
       return contraseña
   except:
       Error(2)


def main():
   if "Usuarios" not in os.listdir():
       os.mkdir("Usuarios")
   global usuario
   global check
   while True:
      
       try:
           if usuario != "":
               
               check = True
               break
   
           opcion = Registro()
           break
       except:
           Error(1)
   if check == False:
       if opcion == 1:
           try:
               usuario, contraseña, tick = Registrarse()
               if tick:
                  RegistroCorrecto(usuario, contraseña)
           except:
               Error(6)
       elif opcion == 2:
           try:
               
               check = IniciarSesion()
               if check:
                  print(bcolors.SKYBLUE)
                  input("Press enter to continue...")
                  os.system("cls")
               elif not check:
                  Error(5)
               print(check)
           except:
               Error(5)
       elif opcion == 3:
           Despedida()
   
   if check:
       while True:
           try:
                  opcion = Inicio()
                  break
           
           except:
               Error(1)
       
       if opcion == 1:
           try:
               contraseña = CrearContraseña()
           except:
               Error(1)
       elif opcion == 2:
           try:
               print("The passwords you have saved are: \n")
               mostrarNombres(usuario)
               contraseña = LeerContraseña()
               os.system("cls")
               print("The password is: " + bcolors.GREEN + contraseña)
               print(bcolors.SKYBLUE)
               sleep(2)
               os.system("cls")
               pyperclip.copy(contraseña)
               print("The password has been copied to the clipboard")
               input("Press enter to continue...")
               
           except:
               Error(3)

       elif opcion == 3:
           CerrarSesion()
           usuario = ""
           check = False
         

       elif opcion == 4:
           try:
               borrar_directorio(usuario)
               usuario = ""
               check = False
               input("Press enter to continue...")
           except:
               Error(2)

       elif opcion == 5:
           try:
               print("The passwords you have saved are: \n")
               mostrarNombres(usuario)
               nombre = int(input("Enter the indicator of the password you want to delete: " + bcolors.ORANGE))
               print(bcolors.SKYBLUE)
               borrar_fichero(nombre, usuario)
               
               print("The password has been deleted correctly")
               input("Press enter to continue...")
           except:
               Error(7)


       elif opcion == 6:
           Despedida()
   
   else:
       usuario = ""
   
   os.system("cls")
   main()

main()
