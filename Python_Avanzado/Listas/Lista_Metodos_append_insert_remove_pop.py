#append: metodo que agrega un elemento a la lista pasado por parametros
#insert: metodo que agrega un elemento en la posicion indicada
#remove: metodo que elimina la primera ocurrencia pasada por parametros
#pop: metodo que elimina la primera ocurrencia pasada por parametros y la devuelve
lista = [324,367,876,8,9,9045,777,9,456,34,65]
print("Lista original: ", lista)
lista.append(54)
print("Lista: ", lista)
lista.insert(4, 11)
lista.insert(8, 683)
print("Lista: ", lista)
lista.remove(9)
print("Lista: ", lista)
numeroDevuelto = lista.pop(3)
print("numero: ", numeroDevuelto)
print("Lista: ", lista)