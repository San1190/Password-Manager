import os
from textos import *
import shutil
import stat
# Función para crear un fichero si no existe y llamarlo con el nombre que le pasemos
def crear_fichero(nombre):
    path_contraseñas = os.getcw
    with open(path_contraseñas, "w"):
        pass  # No necesitas cerrar el archivo manualmente, "with" se encarga de eso
def crear_fichero(nombre, usuario):
    path_contraseñas = os.path.join("Usuarios", usuario, nombre + ".txt")
    with open(path_contraseñas, "w"):
        pass

def crear_fichero_usuario(usuario):
    path_contraseñas = os.path.join("Usuarios", usuario, "contraseña_usuario.txt")
    with open(path_contraseñas, "w"):
        pass

def escribir_contrasena_usuario(nombre, contraseña):
    path_contraseñas = os.path.join("Usuarios", nombre, "contraseña_usuario.txt")
    with open(path_contraseñas, "w") as fichero:
        fichero.write(contraseña)
        fichero.close()

     
# Función para escribir en el fichero que le pasemos
def escribir_fichero(nombre, usuario, contraseña):
    path_contraseñas = os.path.join("Usuarios", usuario, nombre + ".txt")
    with open(path_contraseñas, "w") as fichero:
        fichero.write(contraseña)
        fichero.close()


# Función para leer el fichero y mostrarlo por pantalla
def leer_fichero(nombre):
    path_contraseñas = os.path.join("Usuarios", nombre, nombre + ".txt")
    with open(path_contraseñas, "r") as fichero:
        texto = fichero.read()
        fichero.close()
    return texto

def leer_fichero(numero, usuario):
    path_usuario = os.path.join("Usuarios", usuario)
    ficheros = os.listdir(path_usuario)
    if "contraseña_usuario.txt" in ficheros:
        ficheros.remove("contraseña_usuario.txt")

    with open(os.path.join(path_usuario, ficheros[numero - 1]), "r") as fichero:
        texto = fichero.read()
        fichero.close()
    return texto




def leer_contrasena_usuario(nombre):
    path_usuarios = "Usuarios"
    path_usuario = os.path.join(path_usuarios, nombre)
    path_contraseñas = os.path.join(path_usuario, "contraseña_usuario.txt")

    if os.path.exists(path_contraseñas):
        with open(path_contraseñas, "r") as fichero:
            texto = fichero.read()
        return texto
    else:
        return "El archivo de contraseña no existe para el usuario especificado."
    


# ...

def borrar_fichero(numero, usuario):
  path_usuario = os.path.join("Usuarios", usuario)
  
  # Verificar si el directorio existe
  if not os.path.exists(path_usuario):
      print(f"The directory {path_usuario} does not exist.")
      return

  ficheros = os.listdir(path_usuario)
  if "contraseña_usuario.txt" in ficheros:
      ficheros.remove("contraseña_usuario.txt")
  
  # Verificar si el índice es válido
  if numero - 1 >= len(ficheros):
      print(f"The index {numero} is not valid. There is no file at that position.")
      return

  # Imprimir el archivo a eliminar
  
  # Intentar eliminar el archivo y manejar cualquier error que pueda ocurrir
  try:
      os.remove(os.path.join(path_usuario, ficheros[numero - 1]))
  except OSError as error:
      print(f"Error deleting the file: {error}")

# ...

def borrar_directorio(usuario):
   path_usuario = os.path.join("Usuarios", usuario)
   
   try:
       # Eliminar el directorio y su contenido recursivamente
       shutil.rmtree(path_usuario)
       print(f"Directory '{path_usuario}' successfully deleted.")
   except FileNotFoundError:
       print(f"The directory '{path_usuario}' does not exist.")
   except Exception as e:
       print(f"Error trying to delete the directory '{path_usuario}': {e}")

# ...

def crear_directorio(usuario):
   path_contraseñas = os.path.join("Usuarios", usuario)
   if not os.path.exists(path_contraseñas):
       os.makedirs(path_contraseñas)
       crear_fichero_usuario(usuario)
       print("Password folder successfully created.")
       return True
   
   
       
   else:
       return False
       Error(4)

# ...

def mostrarNombres(usuario):
   path_usuario = os.path.join("Usuarios", usuario)
   ficheros = os.listdir(path_usuario)
   if "contraseña_usuario.txt" in ficheros:
       ficheros.remove("contraseña_usuario.txt")
   for i in range(len(ficheros)):
       ficheros[i] = ficheros[i].replace(".txt", "")
       print(f"{i + 1}." + ficheros[i])
   
   return ficheros 
