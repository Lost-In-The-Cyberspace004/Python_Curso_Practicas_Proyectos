class coordenada: #Creamos la clase
    def __init__(self, x, y): #Incializamos el constructor con sus parametros
        self.X = x #Asignamos los parametros del constructor a los atributos (self.X y self.Y)
        self.Y = y

    def mostrarCoordenadas(self): #Creamos un metodo que obtiene los valores del constructor
        print(self.X , " => ", self.Y)

Obj1 = coordenada(2, 3)  #El valor por parametros se asigna al constructor
Obj1.mostrarCoordenadas()