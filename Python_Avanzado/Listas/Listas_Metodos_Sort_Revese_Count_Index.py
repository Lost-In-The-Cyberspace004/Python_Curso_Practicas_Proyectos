#sort: metodo que ordena la lista de manera ascendente, si se necesita de manera descendente se usa "reverse = true"
#reverse: metodo que invierte el orden de la lista
#count: metodo que cuenta cuantas veces se repite un elemento dentro de la lista
#index: metodo que devuelve el primer elemento en la posicion indicada, con 2 parametros opcionales: el primero indica la posicion donde empezar a buscar y el 2do el final de la posicion

lista = [322, 367, 876, 8, 9, 10, 11]
print("Lista original: ", lista)
lista.sort()
print("Lista ordenada: ", lista)
lista.reverse()
print("lista al revés: ", lista.count(9))
print("posicion del elemento a buscar: ", lista.index(10))
