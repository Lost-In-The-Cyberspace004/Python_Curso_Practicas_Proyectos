files = open("Archivo.txt")
lineas = list(files)
files.close()

for i in lineas:
    print(i)