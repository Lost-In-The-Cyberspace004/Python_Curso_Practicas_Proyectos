#get: metodo que retorna el valor de la clave dentro de una diccionario
#update: actualizar elementos de clave valor
#setdefault: agregar un elemento dentro del diccionario

numeros = {
    "uno": "one",
    "dos": "two",
    "tres": "three"
}

print("diccionario: ", numeros)

print("valor:", numeros.get("tres"))

numeros.update("cuatro": "four", "tres":"Three")
print(numeros)

print("setdefault del Siete: ",numeros.setdefault("Siete","Seven"))
print("Diccionario después del setdefault (nuevo elemento): ",numeros)
print("setdefault del Cinco: ",numeros.setdefault("Cinco","FiveNUEVO"))
print("Diccionario después del setdefault (elemento existente): ",numeros)