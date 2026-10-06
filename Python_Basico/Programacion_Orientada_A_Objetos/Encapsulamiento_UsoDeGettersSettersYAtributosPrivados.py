#Convertiremos atributos y metodos de manera privada o publica
#Dependiendo eso, asi se permiten o no sus accesos a otras partes del codigo

class puntoPublico:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class puntoPrivado:
    def __init__(self, x, y):
        self.__X = x #Usamos __ para declararlos como privados
        self.__Y = y

    #usamos getters para obtener / retornar su contenido ya que son atributos privados
    #No podemos acceder a ellos de manera normal
    #Para modificarlos usaremos setters
    def GetX(self):
        return self.__X
    def GetY(self):
        return self.__Y
    def SetX(self, x):
        self.__X = x 
    def SetY(self, y):
        self.__Y = y

publico = puntoPublico(4, 6)
privado = puntoPrivado(6, 7)
print("Valores punto publico:", publico.X,",",publico.Y)
print("Valores punto privado:", privado.GetX(),",",privado.GetY())

publico.X = 2 #Al ser publicos solo se llama el atributo y se modifica su valor
privado.SetX(9) #Al ser privados se debe llamar el setter y se le asigna el valor

print("Valores punto publico:", publico.X,",",publico.Y)
print("Valores punto privado:", privado.GetX(),",",privado.GetY()) #recuerda: get retorna el valor