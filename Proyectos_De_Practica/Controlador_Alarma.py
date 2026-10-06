class Alarm:
    #Si usamos ="" o =False los parametros se vuelven opcionales, pero aun asi se pueden seguir usando sin problemas
    def __init__(self, horaProgramada="", Etiqueta="", activada=""):
        self.__HoraProgramada = horaProgramada
        self.__Etiqueta = Etiqueta
        self.__activada = activada

    def GetActivada(self):
        return self.__activada

    def SetActivada(self, desactivada):
        self.__activada = desactivada

    def Observar(self):
            print("Hora programada: ", self.__HoraProgramada)
            print("Etiqueta: ", self.__Etiqueta)
            print("Activada: ", self.__activada)




class controlAlarmas:
    def __init__(self):
        self.__ListaDeAlarmas = []

    def AgregarAlarmas(self, Alarma):
        self.__ListaDeAlarmas.append(Alarma)            

    def DesactivarAlarmas(self):
        for ObjetoQueContieneLaInformacion in self.__ListaDeAlarmas:
            if ObjetoQueContieneLaInformacion.GetActivada().lower() == "activada":
                desactivada = "desactivada"
                ObjetoQueContieneLaInformacion.SetActivada(desactivada)

    def ObservarLista(self):
        for ObjetoQueRecorreLaLista in self.__ListaDeAlarmas:
            ObjetoQueRecorreLaLista.Observar()




def crearAlarma(ObjetoControl):

    Hora = input("Hora programada: ")
    Etiqueta = input("Etiqueta: ")
    Activada = input("Activada o desactivada?: ")

    Obj2 = Alarm(Hora, Etiqueta, Activada)
    ObjetoControl.AgregarAlarmas(Obj2)



def desactivarTodas(ObjetoControl):
    ObjetoControl.DesactivarAlarmas()



def VerificarEstado(ObjetoControl):
    ObjetoControl.ObservarLista()



Obj1 = controlAlarmas()



i = 0
while i == 0:
    print("1-) Agregar \n2-) Desactivar alarmas \n3-) Verificar estados")
    Opcion = int(input("Opcion: "))
    if Opcion == 1:
        crearAlarma(Obj1)

    elif Opcion == 2:
        desactivarTodas(Obj1)

    elif Opcion == 3:
        VerificarEstado(Obj1)

    elif Opcion == 4:
        i = 0