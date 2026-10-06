valor = int(input("valor: "))
if valor <= 10: #si se cumple la condicion entonces ejecuta la instruccion
    print("Se cumple la condicion") 
else: #Si no se cumple la condicion pasa a la excepcion
    print("No se cumple la condicion")

Palabra = "Lolazos bacrrums"
if Palabra.startswith("L"):
    print("Empieza con L")
elif Palabra.endswith("s"): #si el condicional anterior no se cumple, entonces puede haber un 2do condicional
    print("Termina en s")
else:
    print("No empieza con L")
