class coordenada:
    def __init__(self, x, y):
        self.X = x 
        self.Y = y

    def coordenadaElement(self):
        print(self.X, " => ", self.Y )

Obj1 = coordenada(2, 2)
Obj2 = coordenada(4, 5)
Obj3 = coordenada(6, 87988)

Obj1.coordenadaElement()
Obj2.coordenadaElement()
Obj3.coordenadaElement()