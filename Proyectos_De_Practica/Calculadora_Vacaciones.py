class calcular:
    def __init__(self, Trabajador, AniosDeTrabajo):
        self.__Trabajador = Trabajador
        self.__AniosDeTrabajo = AniosDeTrabajo

    def Calcular(self, Trabajo, TiempoTrabajado):
        self.__Trabajador = Trabajo.lower().strip()
        self.__AniosDeTrabajo = TiempoTrabajado

        if self.__Trabajador == "bodeguero":
            if self.__AniosDeTrabajo == 1:
                print("Tienes 3 dias de vacaciones\n")
            elif self.__Trabajador == "bodeguero" and self.__AniosDeTrabajo == 2:
                print("Tienes una semana de vacaciones")
            elif self.__Trabajador == "bodeguero" or self.__AniosDeTrabajo >= 3:
                print("Tienes 1 mes de vacaciones")
            else:
                print("Trabajo no existente")

        elif self.__Trabajador == "asistente":
            if self.__AniosDeTrabajo == 1:
                print("Tienes 5 dias de vacaciones\n")
            elif self.__Trabajador == "asistente" and self.__AniosDeTrabajo == 2:
                print("Tienes 2 semanas de vacaciones\n")
            elif self.__Trabajador == "asistente" or self.__AniosDeTrabajo >= 3:
                print("Tienes 1 mes y medio de vacaciones\n") 
            else:
                print("Trabajo no existente")

        elif self.__Trabajador == "jefe gerencial":
            if self.__AniosDeTrabajo == 1:
                print("Tienes 1 mes de vacaciones\n")
            elif self.__Trabajador == "jefe gerencial" and self.__AniosDeTrabajo == 2:
                print("2 meses de vacaciones\n")
            elif self.__Trabajador == "jefe gerencial" and self.__AniosDeTrabajo >= 3:
                print("40.000 meses de vacaciones\n")
            else:
                print("Trabajo no existente")

Obj1 = calcular("Default", 0)

i = 0
while i == 0:
    print("\n")
    Opcion = input("Puesto de trabajo: ")
    AniosDeTrabajo = int(input("Tiempo de trabajo: "))
    
    print("\n")
    Obj1.Calcular(Opcion, AniosDeTrabajo)

    if Opcion == "Salir" or Opcion == "salir" and AniosDeTrabajo == 0:
        i = 1
        break