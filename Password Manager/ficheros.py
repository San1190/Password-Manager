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
    




def borrar_fichero(numero, usuario):
   path_usuario = os.path.join("Usuarios", usuario)
   
   # Verificar si el directorio existe
   if not os.path.exists(path_usuario):
       print(f"El directorio {path_usuario} no existe.")
       return

   ficheros = os.listdir(path_usuario)
   if "contraseña_usuario.txt" in ficheros:
       ficheros.remove("contraseña_usuario.txt")
   
   # Verificar si el índice es válido
   if numero - 1 >= len(ficheros):
       print(f"El índice {numero} no es válido. No hay un archivo en esa posición.")
       return

   # Imprimir el archivo a eliminar
   print(os.path.join(path_usuario, ficheros[numero - 1]))
   
   # Intentar eliminar el archivo y manejar cualquier error que pueda ocurrir
   try:
       os.remove(os.path.join(path_usuario, ficheros[numero - 1]))
   except OSError as error:
       print(f"Error al eliminar el archivo: {error}")


# Función para crear un directorio de usuario
def crear_directorio(usuario):
    path_contraseñas = os.path.join("Usuarios", usuario)
    if not os.path.exists(path_contraseñas):
        os.makedirs(path_contraseñas)
        crear_fichero_usuario(usuario)
        print("Se ha creado la carpeta contraseñas")
        return True
    
    
        
    else:
        return False
        Error(4)





def borrar_directorio(usuario):
    path_usuario = os.path.join("Usuarios", usuario)
    
    try:
        # Eliminar el directorio y su contenido recursivamente
        shutil.rmtree(path_usuario)
        print(f"Directorio '{path_usuario}' eliminado con éxito.")
    except FileNotFoundError:
        print(f"El directorio '{path_usuario}' no existe.")
    except Exception as e:
        print(f"Error al intentar eliminar el directorio '{path_usuario}': {e}")



def mostrarNombres(usuario):
    path_usuario = os.path.join("Usuarios", usuario)
    ficheros = os.listdir(path_usuario)
    if "contraseña_usuario.txt" in ficheros:
        ficheros.remove("contraseña_usuario.txt")
    for i in range(len(ficheros)):
        ficheros[i] = ficheros[i].replace(".txt", "")
        print(f"{i + 1}." + ficheros[i])
    
    return ficheros