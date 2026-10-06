class Hotel:
    def __init__(self):
        self.__NumeroHabitaciones = 0
        self.__Estrellas = 0

    def SetNumeroHabitaciones(self, N):
        self.__NumeroHabitaciones = N

    def  SetEstrellas(self, estrellas):
        self.__Estrellas = estrellas

    def MostrarHotel(self):
        print("------")
        print("Hotel")
        print("Estrellas: ", self.__Estrellas)
        print("Numero de habitaciones: ", self.__NumeroHabitaciones)
        print("------")

class Restaurante:
    def __init__(self):
        self.__Tenedores = 0
        self.__HoraApertura = 0

    def SetTenedores(self, tenedores):
        self.__Tenedores = tenedores

    def SetHoraApertura(self, Hora):
        self.__HoraApertura = Hora

    def MostrarRestaurante(self):
        print("------")
        print("Restaurante: ")
        print("Tenedores: ", self.__Tenedores)
        print("Hora de apertura: ", self.__HoraApertura)
        print("------")

class Negocio(Hotel, Restaurante): #Heredamos de ambas clases
    def __init__(self): #Inicializamos la herencia
        super().__init__()
        self.__Nombre = ""
        self.__Direccion = ""
        self.__Telefono = 0

    def SetNombre(self, nombre):
        self.__Nombre = nombre

    def SetDireccion(self, direccion):
        self.__Direccion = direccion

    def SetTelefono(self, telefono):
        self.__Telefono = telefono

    def MostrarNegocio(self):
        print("------")
        print("Negocio")
        print("Nombre", self.__Nombre)
        print("Direccion: ", self.__Direccion)
        print("Telefono: ", self.__Telefono)
        print("------")

        self.MostrarHotel()
        self.MostrarRestaurante()

negocio = Negocio() #Como en una herencia normal: Podemos acceder a los metodos y atributos de cada clase de la que se hereda
negocio.SetEstrellas(4)
negocio.SetNumeroHabitaciones(255)
negocio.SetTenedores(3)
negocio.SetHoraApertura(6)
negocio.SetNombre("Time of chamba!")
negocio.SetDireccion("Calle random")
negocio.SetTelefono("12345")
negocio.MostrarNegocio()