class coordenada:
    def __init__(self, x, y):
        self.X = x 
        self.Y = y

    def coordenadaElement(self):
        print(self.X, " => ", self.Y )

Obj1 = coordenada(2, 2)
Obj1.coordenadaElement()
Obj2 = coordenada(3, 5)
Obj2.coordenadaElement()

Obj1 = Obj2 #Asignamos el valor por objeto
Obj1.coordenadaElement()