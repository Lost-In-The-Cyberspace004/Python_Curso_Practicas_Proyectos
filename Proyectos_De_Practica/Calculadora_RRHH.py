class Calculadora:

    def __init__(self):

        self.__AuxilioTransPorte = 249095
        self.__SalarioMinimo = 1500000
        self.__SalarioBase = self.__SalarioMinimo + self.__AuxilioTransPorte
        self.__diasLaborales = 30





    def CalculoUniversal(self, DiasTrabajados):

        SalarioDevengado = self.__SalarioBase / self.__diasLaborales * DiasTrabajados
        Salud_Empleado = self.__SalarioMinimo * 0.04
        Pension = self.__SalarioMinimo * 0.04
        NetoAPagar = (SalarioDevengado + self.__AuxilioTransPorte) - (Salud_Empleado + Pension)
        Cesantias = (self.__SalarioBase * DiasTrabajados) / 360
        IntCesantias = ((Cesantias * DiasTrabajados) * 0.12) / 360
        PrimaDeServicios = (self.__SalarioBase * DiasTrabajados) / 360
        Vacaciones = ((self.__SalarioMinimo * DiasTrabajados) / 720)

        print("\nSalario devengado: ", SalarioDevengado)
        print("Salud empleado: ", Salud_Empleado)
        print("Pension: ", Pension)
        print("Neto a pagar: ", NetoAPagar)
        print("Cesantias: ", Cesantias)
        print("Intereces a las cesantias: ", IntCesantias)
        print("Prima de servicios: ", PrimaDeServicios)
        print("Vacaciones: ", Vacaciones, "\n")





Obj1 = Calculadora()

i = 0
while i == 0:
    
    Opcion = int(input("--------------------\n1-) Realizar calculos rapidos \n2-) Salir \n-------------------- \nOpcion: "))

    if Opcion == 1:
        diasTrabajados = int(input("Días trabajados: "))
        Obj1.CalculoUniversal(diasTrabajados)

    elif Opcion == 2:
        i = 1
        break
    
    else:
        print("Opcion inexistente")