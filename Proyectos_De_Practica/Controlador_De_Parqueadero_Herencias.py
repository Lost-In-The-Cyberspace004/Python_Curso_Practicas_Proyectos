class Vehiculo:
    def __init__(self, tipo = "", placa = ""):
        self.__Tipo = tipo
        self.__Placa = placa

        #Getters y Setters
    def GetTipo(self):
        return self.__Tipo
    def GetPlaca(self):
        return self.__Placa

    def __str__(self):
        return f"Tipo: {self.__Tipo} Placa: {self.__Placa}"  





class Moto(Vehiculo):
    def __init__(self, tipo, placa):
        super().__init__(tipo, placa)




class Auto(Vehiculo):
    def __init__(self, tipo, placa):
        super().__init__(tipo, placa)





class AgregarAlHistorial:
    def __init__(self):
        self.__InventarioDeAutos = []

    def AgregarAutos(self, DatosDeAuto):
        self.__InventarioDeAutos.append(DatosDeAuto)

    def VerAutosEnParqueadero(self):
        for Recorrer in self.__InventarioDeAutos:
            print(Recorrer)

    def CalcularTarifas(self, TipoDeVehiculo, Placa):
            encontrado = False
            for ObjetoContenedorDeValores in self.__InventarioDeAutos:
                if ObjetoContenedorDeValores.GetTipo().lower() == TipoDeVehiculo.lower():
                    if ObjetoContenedorDeValores.GetPlaca().lower() == Placa.lower():
                        if TipoDeVehiculo.lower() == "auto":
                            encontrado = True
                            print("Debes pagar 10.000.000")
                        elif TipoDeVehiculo.lower() == "moto":
                            encontrado = True
                            print("Debes pagar 5.000.000")
                        break
            if not encontrado:
                print("No existe")






Obj1 = AgregarAlHistorial()






i = 0
while i == 0:
    print("1-) Agregar \n2-) Ver Lista \n3-) Pagar tarifa \n4-) Salir")
    opc = int(input("Opcion: "))
    if opc == 1:
        Placa = input("Placa: ")
        Tipo = input("Auto o Moto?: ")

        if Tipo == "Auto":
            AutoObj = Auto(Tipo, Placa)
            Obj1.AgregarAutos(AutoObj)

        elif Tipo == "Moto":
            MotoObj = Moto(Tipo, Placa)
            Obj1.AgregarAutos(MotoObj)

    elif opc == 2:
        Obj1.VerAutosEnParqueadero()

    elif opc == 3:
        Placa = input("Placa: ")
        Tipo = input("Moto o auto?: ")
        Obj1.CalcularTarifas(Tipo, Placa)

    elif opc == 4:
        i = 1
        break

    else:
        print("Opcion ineistente")