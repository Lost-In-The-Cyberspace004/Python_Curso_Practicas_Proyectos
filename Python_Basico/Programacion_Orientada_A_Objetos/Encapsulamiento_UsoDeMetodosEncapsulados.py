class mostrarValores:
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    def __Sumar(self):
        return self.__X + self.__Y

    def __Restar(self):
        return self.__X - self.__Y

    #Al ser metodos privados, se deben llamar desde un metodo publico dentro de la clase
    def Operar(self):
        print(self.__Sumar())
        print(self.__Restar())
    

Operaciones = mostrarValores(23, 45)
Operaciones.Operar() #Llamamos el metodo publico para acceder a los metodos privados