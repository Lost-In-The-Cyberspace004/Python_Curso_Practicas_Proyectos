file = open("Archivo.txt", "r")
lineas = file.read()
file.close()
print(lineas)

reescritura = open("Archivo.txt", "a")
reescritura.write("Agregado")
reescritura.close()

reobservacion = open("Archivo.txt", "r")
texto = reobservacion.read()
reobservacion.close()

print(texto)