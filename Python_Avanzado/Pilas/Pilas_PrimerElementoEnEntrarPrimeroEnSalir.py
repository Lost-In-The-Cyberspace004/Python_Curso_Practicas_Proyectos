class pila:
    def __init__(self):
        self.__Items = []

    def estaVacia(self):
        if len(self.__Items)==0: #Si esta vacia entonces retorna verdadero
            return True 
        else:
            return False #Caso contrario, retorna false

    def Apilar(self, item):
        self.__Items.append(item)

    def Retirar(self):
        self.__Items.pop()

    def MostrarPila(self):
        print(self.__Items)

Pila = pila()
for i in range(10):
    Pila.Apilar(i)
Pila.MostrarPila()

PilaReves = pila()
while not pila.estaVacia: #Si la pila no esta vacia
    PilaReves.Apilar(pila.Retirar) #Entonces creamos una nueva pila donde el primer elemento en salir se vuelve el primero en entrar y ultimo en salir

PilaReves.MostrarPila()