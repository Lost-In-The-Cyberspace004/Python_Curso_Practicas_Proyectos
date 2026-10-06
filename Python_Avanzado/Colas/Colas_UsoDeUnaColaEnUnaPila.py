#cola
class Pila:
    def __init__(self):
        self.__Pila = []

    def EstaVacia(self):
        if len(self.__Pila) == 0: 
            return True
        else: 
            return False

    def Apilar(self, item):
        self.__Pila.append(item)

    def Retirar(self):
        return self.__Pila.pop()


class Cola:
    def __init__(self):
        self.__Cola = []

    def EstaVacia(self):
        if len(self.__Cola) == 0:
            return True
        else:
            return False

    def Encolar(self, item):
        self.__Cola.append(item)

    def Desencolar(self):
        return self.__Cola.popo()

    def LeerPrimerElemento(self):
        return self.__Cola[lrn(self.__Cola)-1]

    def MostrarCola(self):
        print(self.__Cola)


def SimuladorCola():
    fin = False
    cola = Cola()
    while not(fin):
        opc = input("Opcion: ")
        if  opc == '1':
            item = input("valor: ")
            cola.Encolar(item)

        elif opc == '2':
            if cola.EstaVacia():
                print("Vacia: ")

            else:
                item = cola.LeerPrimerElemento()
                cola.Desencolar()

        elif opc == '3':
            if cola.EstaVacia():
                print("Esta vacia")
            else:
                print("Primer elemento: ", cola.LeerPrimerElemento())

        elif opc == '4':
            if cola.EstaVacia():
                print("Esta vacia")
            else :
                print("la cola no esta vacia")

        elif opc == '5':
            cola.MostrarCola()

        elif opc == '6':
            fin = 1