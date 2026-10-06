class Buscador:
    
    def __init__(self, Nombres: str, Apellidos: str, Edad: int, CC: int):
        self.Nombres = Nombres
        self.Apellidos = Apellidos
        self.Edad = Edad
        self.CC = CC





    def GetNombres(self):
        return self.Nombres
    def GetApellidos(self):
        return self.Apellidos
    def GetEdad(self):
        return self.Edad
    def GetCC(self):
        return self.CC





    def __str__(self):
        return f"Nombres: {self.Nombres} | Apellidos: {self.Apellidos} | Edad: {self.Edad} | CC: {self.CC}"





    def BuscarDatos(self, Nombre: str, Apellidos: str, lista: list): #LE PASAMOS UN ARRAY Y COMO PUEDES OBSERVAR ESPECIFICAMOS QUE ES UN ARRAY
        for ObjetoQueRecorreLaListaYObtieneElContenido in lista:
            if ObjetoQueRecorreLaListaYObtieneElContenido.GetNombres() == Nombre and ObjetoQueRecorreLaListaYObtieneElContenido.GetApellidos() == Apellidos:
                print("\nEncontrado")
                print(ObjetoQueRecorreLaListaYObtieneElContenido, "\n")





#OTRA FORMA DE CREAR ARRAYS DE OBJETOS, INSTANCIANDO LA CLASE Y ASIGNANDOLE VALORES!
Lista = [
    Buscador("Jorge", "Campos", 18, 1117815220),
    Buscador("Danna", "Campos", 24, 1234567890),
    Buscador("Daniela", "Campos", 21, 1234567890),
    Buscador("Karen", "Campos", 35, 1234567890),
    Buscador("Simon", "Campos", 15, 1234567890) 
]

Obj1 = Buscador("default", "default", 0, 0)





i = 0
while i == 0:
    Opcion = int(input("1-) Buscar \n2-) Salir \nOpcion: "))
    if Opcion == 1:
        Nombre = input("\nNombre: ")
        Apellidos = input("Apellidos: ")
        Obj1.BuscarDatos(Nombre, Apellidos, Lista) #ENVIAMOS EL ARRAY DE OBJETOS

    elif Opcion == 2:
        i = 1
        break

    else:
        print("Opcion inexistente")