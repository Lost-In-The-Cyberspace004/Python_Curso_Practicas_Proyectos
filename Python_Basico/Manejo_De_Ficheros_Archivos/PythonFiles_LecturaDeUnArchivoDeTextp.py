#Usando open podemos obtener la ruta del archivo
file = open("Archivo.txt", "r")
texto = file.read() #Read se usa para leer el contenido del archivo de texto plano
print(texto)
file.close() #Cerramos el proceso para que asi no consuma mas recursos