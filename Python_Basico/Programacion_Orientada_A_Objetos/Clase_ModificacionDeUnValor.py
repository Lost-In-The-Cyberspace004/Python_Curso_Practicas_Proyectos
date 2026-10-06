class coordenada:
    def __init__(self, x, y):
        self.X = x 
        self.Y = y

    def coordenadaElement(self):
        print(self.X, " => ", self.Y )

Obj1 = coordenada(2, 2)
Obj1.coordenadaElement()
Obj1.X = 2 #Llamando el parametro del constructor podemos cambiar el valor
Obj1.Y = 3
Obj1.coordenadaElement()