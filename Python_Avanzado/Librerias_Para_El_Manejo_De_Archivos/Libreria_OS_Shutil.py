#getcwd = RETORNA LA UBICACION ACTUAL DEL SISTEMA 
#chdir = CAMBIAR DE DIRECTORIOS
#getpid = DEVUELVE EL IDENTIFICADOR DEL PROCESO APLICATIVO
#getuid = DEVUELVE EL IDENTIFICADOR DEL USUARIO DEL PROCESO APLICATIVO

import os
import shutil

print("Directorio actual: ", os.getcwd())
os.chdir("/users/downloads/")
print("Nuevo directorio: ", os.getcwd())
print("ID proceso: ", os.getpid())
print("ID usuario:", os.getuid())

#listdir = LISTA EL CONTENIDO DEL DIRECTORIO ACTUAL
#mkdir = CREA UN NUEVO DIRECTORIO
#rename = RENOMBRA UN FICHERO
#copy = copia un fichero y lo ubica en el nuevo fichero especificado por parametros
#move = mueve un fichero a una nueva ubicacion especificada por parametros

print("Directorio de trabajo: ",os.getcwd())
print("Contenido: ", os.listdir())

print("¡Copiando el fichero ejemplo.txt!")
shutil.copy("ejemplo.txt","nuevoejemplo.txt")

print("Contenido: ", os.listdir())

print("¡Renombrar nuevoejemplo.txt!")
os.rename("nuevoejemplo.txt","nuevonombre.txt")

print("Contenido: ", os.listdir())
print("¡Creando el nuevo directorio!")

os.mkdir("NuevoDirectorio")
print("Contenido del directorio: ", os.listdir())

print("¡Moviendo el fichero al nuevo directorio!")
shutil.move("nuevonombre.txt","NuevoDirectorio")

print("Contenido del directorio: ", os.listdir())
print("¡Cambiando directorio de trabajo!")

os.chdir("/Users/alfre/Desktop/Ejercicios 6-5/NuevoDirectorio")
print("Nuevo directorio de trabajo: ",os.getcwd())

#rmtree = elimina el directorio con todo su contenido
#remove = elimina el fichero especificado por parametros
print("Directorio de trabajo: ",os.getcwd())
print("Contenido del directorio: ", os.listdir())

print("¡Eliminar el directorio NuevoDirectorio!")
shutil.rmtree("NuevoDirectorio")

print("Contenido del directorio: ", os.listdir())
print("¡Borrando el fichero ejemplo.txt!")

os.remove("ejemplo.txt")
print("Contenido del directorio: ", os.listdir())
