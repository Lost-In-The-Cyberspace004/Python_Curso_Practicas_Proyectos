files = open("Archivo.txt", "r")
lineas = files.readlines()
files.close()
print(lineas[0])