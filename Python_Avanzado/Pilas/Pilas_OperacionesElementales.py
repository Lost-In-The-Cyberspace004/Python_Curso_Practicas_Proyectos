class Pila:
    def __init__(self):
        self.__Items = []

    def EstaVacia(self):
        if len(self.__Items) == 0:
            return True
        else:
            return False

    def Apilar(self, Item):
        self.__Items.append(Item)

    def Retirar(self):
        return self.__Items.pop()

    def LeerCima(self):
        return self.__Items[len(self.__Items)-1]

    def MostrarPila(self):
        print(self.__Items)

    def SimuladorPila():
        fin = False
        pila = Pila()
        while not(fin):
            opc = input("Opcion: ")
            if opc == '1':
                item = input("Introduzca elemento al pilar: ")
                pila.Apilar(item)
                print("Elemento apilado: ", item)

            elif opc == '2':
                if pila.EstaVacia():
                    print("Esta vacia")
                else:
                    item = pila.LeerCima()
                    pila.Retirar()
                    print("Contiene valores y el elemento fue retirado")

            elif opc == '3':
                if pila.EstaVacia():
                    print("La pila está vacía, no puede leerse la cima")
                else:
                    print("La cima es: ", pila.LeerCima())
            elif opc=='4':
                if pila.EstaVacia():
                    print("La pila está vacía")
                else:
                    print("La pila no está vacía")
            elif opc== 5:
                pila.MostrarPila()
            elif(opc=='6'):
                fin = 1

