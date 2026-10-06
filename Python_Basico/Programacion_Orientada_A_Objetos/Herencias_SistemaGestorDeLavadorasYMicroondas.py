class Electrodomestico:
    def __init__(self, tension, encendido): #Debes inicializar siempre la clase que va a heredar
        self.__Tension = tension
        self.__Encendido = encendido

    def encender(self):
        self.__Encendido = True

    def apagar(self):
        self.__Encendido = False

    def EstaEncendido(self):
        return self.__Encendido

    def SetTencion(self, tensionAct):
        self.__Tension = tensionAct

    def GetTencion(self):
        return self.__Tension



class Lavadora(Electrodomestico): #Heredamos de la clase anterior
    #Inicializamos la clase padre
    def __init__(self, tension = 0, encendido = False):
        super().__init__(tension, encendido)
        self.__RPM = 0
        self.__Kilos = 0

    def SetRPM(self, rpm):
        self.__RPM = rpm

    def SetKilos(self, kilos):
        self.__Kilos = kilos

    def MostrarLavadora(self):
        print("----Lavadora----")
        print("rpm: ", self.__RPM)
        print("kilos: ", self.__Kilos)
        print("tension: ", self.GetTencion())

        if self.EstaEncendido():
            print("Encendida")
        else:
            print("Apagada")



class Microondas(Electrodomestico):
    def __init__(self, tension = 0, encendido = False):
        super().__init__(tension, encendido)
        self.__PotenciaMaxima = 0
        self.__Grill = False

    def SetPotenciaMaxima(self, Potencia):
        self.__PotenciaMaxima = Potencia

    def SetGrill(self, grill):
        self.__Grill = grill

    def MostrarMicroondas(self):
        print("----Microondas----")
        print("Potencia Maxima: ", self.__PotenciaMaxima)
        if self.__Grill == True:
            print("Grill: si")
        else:
            print("Grill: No")
        print("Tension: ",  self.GetTencion())
        if self.EstaEncendido():
            print("Microondas Encendido")
        else:
            print("Microondas Apagado")



#Creamos el objeto de tipo lavadora
lavadora = Lavadora()

#Llamamos el setter de los rpm que se encuentra en esa clase
#Al igual que las demás
lavadora.SetRPM(1200)
lavadora.SetKilos(200)

#Como heredamos de la clase electrodomestico, podemos acceder al setter de la clase de la que se hereda
#Desde el objeto creado 
lavadora.SetTencion(220)
#Al igual que los metodos genericos
lavadora.encender()
lavadora.EstaEncendido()

lavadora.MostrarLavadora()

#Lo mismo pero tambien aplicado a la clase Microondas
microondas = Microondas()
microondas.SetPotenciaMaxima(800)
microondas.SetGrill(True)

#Observa como volvemos a usar los metodos que heredamos de la clase electrodomestico 
microondas.SetTencion(220)
microondas.apagar()

microondas.MostrarMicroondas()