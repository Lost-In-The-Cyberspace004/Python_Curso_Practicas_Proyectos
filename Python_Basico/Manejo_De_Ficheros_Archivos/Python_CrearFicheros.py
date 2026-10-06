fileCrear = open("Archivo2.txt", "x")
fileCrear.write("Archivo creado por codigo \n")
fileCrear.write("Ejemplo simplementes \n")
fileCrear.close()

lectura = open("Archivo2.txt", "r")
contenido = lectura.read()
lectura.close()
print(contenido)