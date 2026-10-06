#Las "i" en Python son objetos mas no indices como en Java
#Para usarlas como indices se puede convertir de la siguiente forma

for i in range(len(self.listaContactos)):
    if self.listaContactos[i].GetNombre() == borrarPorNombre:
        del self.listaContactos[i] # O self.listaContactos.pop(i)
        break

#En caso de evitar confusiones, es mejor no llamar la variable iteradora en Python "i"
#Es mejor llamarla de otra forma para evitar confusiones