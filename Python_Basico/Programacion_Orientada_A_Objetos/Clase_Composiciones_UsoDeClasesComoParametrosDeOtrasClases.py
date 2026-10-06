#creamos una clase
class coordenadas:
    def __init__(self, x, y):
        self.X = x 
        self.Y = y

    def Puntos(self):
        print(self.X, " -> ", self.Y )

class vectores:
    def __init__(self, v1, v2, v3):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3

    def mostrarVectores(self):
        self.V1.Puntos() #llamamos al metodo de la clase anterior y lo ejecutamos
        self.V2.Puntos()
        self.V3.Puntos()

punto = coordenadas(12, 3)
punto2 = coordenadas(2, 45)
punto3 = coordenadas(5, 6)

mostrarV = vectores(punto, punto2, punto3) #Usamos los objetos como parametros junto con sus valores. Esto nos permitira tambien acceder a sus metodos
mostrarV.mostrarVectores()    