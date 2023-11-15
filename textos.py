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
   print("What do you want to do?")
   print(bcolors.ENDC)
   print(bcolors.SKYBLUE)
   print("1. Register")
   print("2. Login")
   print("3. Exit")
   opcion = int(input("Choose an option: " + bcolors.ORANGE))
   print(bcolors.SKYBLUE)
   return opcion
   

def Inicio():
   os.system("cls")
   print(bcolors.RED + bcolors.BOLD)
   tprint("Session started", font="small")
   print(bcolors.ENDC)
   print(bcolors.BOLD + bcolors.SKYBLUE)
   print("What do you want to do? \n")
   print(bcolors.ENDC)
   print(bcolors.SKYBLUE)
   print("1. Create password")
   print("2. Read password")
   print("3. Logout")
   print("4. Delete user")
   print("5. Delete password")
   print("6. Exit")
   opcion = int(input("Choose an option: " + bcolors.ORANGE))
   print(bcolors.SKYBLUE)
   return opcion


def Error(num_Error):
   os.system("cls")
   print(bcolors.RED)
   if num_Error == 1:
       print("You have not entered a number\n")
       input("Press enter to continue...")
       os.system("cls")
       
   elif num_Error == 2:
       print("Could not create the file\n")
       input("Press enter to continue...")
       os.system("cls")
   elif num_Error == 3:
       print("Could not write to the file\n")
       input("Press enter to continue...")
       os.system("cls")
   elif num_Error == 4:
       print("The user already exists\n")
       input("Press enter to continue...")
       os.system("cls")
   elif num_Error == 5:
       print("The password or the user is incorrect\n")
       input("Press enter to continue...")
       os.system("cls")
   elif num_Error == 6:
       print("Could not register the user\n")
       input("Press enter to continue...")
       os.system("cls")
   elif num_Error == 7:
       print("Could not delete the file\n")
       input("Press enter to continue...")
       os.system("cls")

   print(bcolors.ENDC)
       

def Despedida():
   os.system("cls")
   print(bcolors.ORANGE + bcolors.BOLD)
   print("Thank you for using the application")
   exit()

def CerrarSesion():
   os.system("cls")
   print("Session closed successfully")
   input("Press enter to continue...")
   os.system("cls")

def RegistroCorrecto(usuario, contraseña):
   os.system("cls")
   print(bcolors.SKYBLUE)
   print("User registered successfully")
   print("Your username is: " + usuario)
   print("Your password is: " + contraseña)
   print("Keep these data in a safe place")
   input("Press enter to continue...")
   os.system("cls")
