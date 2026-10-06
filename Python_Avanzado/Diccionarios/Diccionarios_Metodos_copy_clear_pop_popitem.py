#copy metodo que realida una copia del diccionario y lo retorna
#clear: limpia todos los elementos del diccionario
#pop(): elimina un elemento pasado por parametros dentro del diccionario
#pop()item: lo mismo que el anterior pero de manera aleatoria

numeros = {
    "uno": "one",
    "dos": "two",
    "tres": "three"
}

print("diccionario: ", numeros)
copia = numeros.copy()
print("diccionario copia: ", copia)

numeros.pop("dos") #usamos la clave
print("diccionario: ", numeros)

numeros.clear()
print("diccionario: ", numeros)