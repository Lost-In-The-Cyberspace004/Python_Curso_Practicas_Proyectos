class Funciones:
    def __init__(self, Nombre: str, Apellidos: str, Caracter: str, Capacidad: str, Capital: float, Colateral: str, Condiciones: bool, Aprobado: bool):
        self.__Nombre = Nombre
        self.__Apellidos = Apellidos
        self.__Caracter = Caracter
        self.__Capacidad = Capacidad
        self.__Capital = Capital
        self.__Colateral = Colateral
        self.__Condiciones = Condiciones
        self.__Aprobado = Aprobado

        self.__ListaDeAspirantes = []

    def SetNombre(self, nombre):
        self.__Nombre = nombre

    def SetApellidos(self, apellidos):
        self.__Apellidos = apellidos
    
    def SetCaracter(self, caracter):
        self.__Caracter = caracter

    def SetCapacidad(self, capacidad):
        self.__Capacidad = capacidad
    
    def SetCapital(self, capital):
        self.__Capital = capital

    def SetColateral(self, colateral):
        self.__Colateral = colateral
    
    def SetCondiciones(self, condiciones):
        self.__Condiciones = condiciones
    
    def SetAprobado(self, aprobado):
        self.__Aprobado = aprobado

    def GetNombre(self):
        return self.__Nombre

    def GetApellidos(self):
        return self.__Apellidos

    def GetCaracter(self):
        return self.__Caracter

    def GetCapacidad(self):
        return self.__Capacidad

    def GetCapital(self):
        return self.__Capital

    def GetColateral(self):
        return self.__Colateral
    
    def GetCondiciones(self):
        return self.__Condiciones

    def GetAprobado(self):
        return self.__Aprobado

    def __str__(self):
        return f"\nNombre: {self.__Nombre} | Apellidos: {self.__Apellidos} | Caracter: {self.__Caracter} | Capacidad: {self.__Capacidad} | Colateral: {self.__Colateral} | Condiciones: {self.__Condiciones} | Capital: ${self.__Capital} | Aprobado: {self.__Aprobado} \n"




    
    def Agregar(self, Datos: Funciones):
        self.__ListaDeAspirantes.append(Datos)




        
    def Aprobado(self, Nombre, Apellido, ElementoAprobar: Funciones):
        for ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista in ElementoAprobar:
            if ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.GetNombre().lower() == Nombre.lower() and ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.GetApellidos().lower() == Apellido.lower():
                ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.SetAprobado(True)
                print("\n----------\nAprobado correctamente\n----------\n")





    def Rechazar(self, Nombre, Apellido, ElementoRechazar: Funciones):
        for ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista in ElementoRechazar:
                    if ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.GetNombre().lower() == Nombre.lower() and ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.GetApellidos().lower() == Apellido.lower():
                        ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.SetAprobado(False)
                        print("\n----------\nRechazado correctamente\n----------\n")





    def EditarContenido(self, Nombre, Apellido, ElementoBuscar: Funciones):
        for ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista in ElementoBuscar:
                    if ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.GetNombre().lower() == Nombre.lower() and ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.GetApellidos().lower() == Apellido.lower():
                        Nombres = input("Nombre: ")
                        Apellidos = input("Apellidos: ")
                        Caracteres = input("Caracter: ")
                        Capacidad = input("Capacidad: ")
                        Colaterales = input("Colaterales: ")
                        Condiciones = bool(input("Condiciones: "))
                        Capital = float(input("Capital: "))

                        ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.SetNombre(Nombres)
                        ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.SetApellidos(Apellidos)
                        ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.SetCaracter(Caracteres)
                        ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.SetCapacidad(Capacidad)
                        ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.SetColateral(Colaterales)
                        ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.SetCapital(Capital)
                        ObjetoQueRecorreYAlmacenaLaInformacionDeLaLista.SetCondiciones(Condiciones)

                        print("\n----------\nEditado correctamente\n----------\n")





class Seccion_Usuario:

    def verAspirantes(self, Lista: list[Funciones]): #PASAMOS LA LISTA DE LA CLASE ANTERIOR POR PARAMETROS
        for ObjetoQueRecorreYAlmacenaLosValoresEnLista in Lista:
            print(ObjetoQueRecorreYAlmacenaLosValoresEnLista)





Obj1 = Seccion_Usuario()
Obj2 = Funciones("default","default","default","default",0.0,"default", False, False)





Obj2.Agregar(Funciones("Toyota", "Marisa", "Malo", "Malo", 600000, "Casa", True, False))
Obj2.Agregar(Funciones("Adam", "Smith", "Malo", "Malo", 700000, "Casa", True, False))
Obj2.Agregar(Funciones("Daniela", "Campos", "Bueno", "Buena", 3500000, "Casa", True, False))
Obj2.Agregar(Funciones("Danna", "Campos", "Bueno", "Buena", 450000, "Ahorros", True, False))
Obj2.Agregar(Funciones("Karen", "Campos", "Bueno", "Mala", 4500000, "Ahorros", True, False))





i = 0
while i == 0:
    Opcion = int(input("1-) Ver lista \n2-) Aprobar \n3-) Desaprobar \n4-) Modificar datos \nOpcion: "))

    if Opcion == 1:
        Obj1.verAspirantes(Obj2._Funciones__ListaDeAspirantes)

    elif Opcion == 2:
        Nombre = input("Nombre: ")
        Apellidos = input("Apellidos: ")
        Obj2.Aprobado(Nombre, Apellidos, Obj2._Funciones__ListaDeAspirantes) #ENVIAMOS POR PARAMETROS LA LISTA DE LA CLASE, LLAMANDO EL OBJETO, LA CLASE Y LUEGO LA LISTA
    
    elif Opcion == 3:
        Nombre = input("Nombre: ")
        Apellidos = input("Apellidos: ")
        Obj2.Rechazar(Nombre, Apellidos, Obj2._Funciones__ListaDeAspirantes)

    elif Opcion == 4:
        Nombre = input("Nombre: ")
        Apellidos = input("Apellidos: ")
        Obj2.EditarContenido(Nombre, Apellidos, Obj2._Funciones__ListaDeAspirantes)

    elif Opcion == 5:
        i = 1
        break