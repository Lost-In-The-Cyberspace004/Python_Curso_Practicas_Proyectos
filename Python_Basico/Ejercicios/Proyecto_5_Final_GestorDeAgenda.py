class Direccion:
    def __init__(self):
        self.__Calle = ""
        self.__Piso = ""
        self.__Ciudad = ""
        self.__CodigoPostal = ""

    #Getters clase direccion
    def GetCalle(self):
        return self.__Calle

    def GetPiso(self):
        return self.__Piso

    def GetCiudad(self):
        return self.__Ciudad

    def GetCodigoPostal(self):
        return self.__CodigoPostal

    #Setters clase direccion
    def SetCalle(self, Calle):
        self.__Calle = Calle

    def SetPiso(self, piso):
        self.__Piso = piso

    def SetCiudad(self, ciudad):
        self.__Ciudad = ciudad

    def SetCodigoPostal(self, codigoPostal):
        self.__CodigoPostal = codigoPostal





class Persona:
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__FechaDeNacimiento = ""

    #Getters de la clase Pesona
    def GetNombre(self):
        return self.__Nombre

    def GetApellidos(self):
        return self.__Apellidos

    def GetFechaDeNacimiento(self):
        return self.__FechaDeNacimiento

    #Setters de la clase
    def SetNombre(self, nombre):
        self.__Nombre = nombre

    def SetApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def SetFechaDeNacimiento(self, FDN):
        self.__FechaDeNacimiento = FDN





class Telefono:
    def __init__(self):
        self.__TelefonoFijo = ""
        self.__TelefonoMovil = ""
        self.__TelefonoTrabajo = ""

    #Getters de la clase
    def GetTelefonoFijo(self):
        return self.__TelefonoFijo

    def GetTelefonoMovil(self):
        return self.__TelefonoMovil

    def GetTelefonoTrabajo(self):
        return self.__TelefonoTrabajo

    #Setters de la clase
    def SetTelefonoFijo(self, tf):
        self.__TelefonoFijo = tf

    def SetTelefonoMovil(self, tm):
        self.__TelefonoMovil = tm

    def SetTelefonoTrabajo(self, tt):
        self.__TelefonoTrabajo = tt






class Contacto(Direccion, Persona, Telefono):
    def __init__(self):
        super().__init__()
        self.__Email = ""

    def GetEmail(self):
        return self.__Email

    def SetEmail(self, email):
        self.__Email = email

    def MostrarContacto(self):

        print("\n")
        print("Nombre: ", self.GetNombre())
        print("Apellido: ", self.GetApellidos())
        print("Fecha de nacimiento: ", self.GetFechaDeNacimiento())

        print("\n------")

        print("Ciudad: ", self.GetCiudad())
        print("Calle: ", self.GetCalle())
        print("Codigo postal: ", self.GetCodigoPostal())
        print("Piso: ", self.GetPiso())

        print("\n------")
        print("Telefono: ", self.GetTelefonoMovil())
        print("Telefojo fijo:", self.GetTelefonoFijo())
        print("Telefono de trabajo: ", self.GetTelefonoTrabajo())

        print("\n------")
        print("correo: ", self.GetEmail(), "\n")






class Agenda:
    def __init__(self):
        self.listaContactos = []

    def cargarContactos(self):
        for i in self.listaContactos:
            i.MostrarContacto()
    
    def crearNuevoContacto(self, datosContacto):
        self.listaContactos = self.listaContactos + [datosContacto]

    def BuscarContacto(self, buscarContacto):
        ListaEncontrados = []

        for i in self.listaContactos:
            if i.GetNombre() == buscarContacto:
                ListaEncontrados = ListaEncontrados + [i]
        return ListaEncontrados

    def BuscarPorTelefono(self, buscarPorTelefono):
        ListaNumeros = []
        for i in self.listaContactos:
            if i.GetTelefonoMovil() == buscarPorTelefono:
                ListaNumeros = ListaNumeros + [i]
        return ListaNumeros

    def BorrarPorNombre(self, borrarPorNombre):
        contacto_Encontrado = False
        for i in self.listaContactos[:]:
            if i.GetNombre() == borrarPorNombre:
                self.listaContactos.remove(i)
                contacto_Encontrado = True
                print("Eliminado")
            else:
                print("No encontrado o inexistente")

    def BorrarPorTelefono(self, borrarPorTelefono):
        Numero_Encontrado = False
        for i in self.listaContactos[:]:
            if i.GetTelefonoFijo() == borrarPorTelefono or i.GetTelefonoMovil() == borrarPorTelefono or i.GetTelefonoTrabajo() == borrarPorTelefono:
                self.listaContactos.remove(i)
                contacto_Encontrado = True
                print("Eliminado")
            else:
                print("No encontrado o inexistente")





def IngresarValores(Mi_Agenda):
    Nombre = input("Nombre: ")
    Apellidos = input("Apellidos: ")
    FechaDeNacimiento = input("Fecha de nacimiento: ")

    ciudad = input("Ciudad: ")
    calle = input("Calle: ")
    codigoPostal = input("Codigo postal: ")
    piso = input("Piso: ")

    telefono = input("Telefono: ")
    telefonoJ = input("Telefojo fijo: ")
    telefonoT = input("Telefojo de trabajo: ")

    correo = input("Correo: ")

    DatosUsuario = Contacto() #como contacto hereda de direccion, persona y telefono el objeto puede trabajar tambien como un objeto de esas clases de las que se hereda 

    DatosUsuario.SetNombre(Nombre)
    DatosUsuario.SetApellidos(Apellidos)
    DatosUsuario.SetFechaDeNacimiento(FechaDeNacimiento)

    DatosUsuario.SetCalle(calle)
    DatosUsuario.SetCiudad(ciudad)
    DatosUsuario.SetCodigoPostal(codigoPostal)
    DatosUsuario.SetPiso(piso)

    DatosUsuario.SetTelefonoFijo(telefonoJ)
    DatosUsuario.SetTelefonoMovil(telefono)
    DatosUsuario.SetTelefonoTrabajo(telefonoT)

    DatosUsuario.SetEmail(correo)
    DatosUsuario.MostrarContacto()
    Mi_Agenda.crearNuevoContacto(DatosUsuario)






def BuscarPorNombre(Mi_Agenda):
    Nombre = input("Ingresa el nombre: ")
    NombreBuscar = Mi_Agenda.BuscarContacto(Nombre)

    for i in NombreBuscar:
        i.MostrarContacto()






def BuscarPorTelefono(Mi_Agenda):
    Numero = input("Ingresar el telefono: ")
    BuscarNumero = Mi_Agenda.BuscarPorTelefono(Numero)

    for i in BuscarNumero:
        i.MostrarContacto()






def BorrarPorNombre(Mi_Agenda):
    Nombre = input("Ingresar nombre: ")
    Mi_Agenda.BorrarPorNombre(Nombre)






def BorrarPorNumero(Mi_Agenda):
    Numero = input("Ingresar numero: ")
    Mi_Agenda.BorrarPorTelefono(Numero)






def EntrUs():
    print("1-) Ingresar valores \n2-) Buscar por nombre \n3-) Buscar por telefono \n4-) Eliminar por nombre \n5-) Eliminar por numero")

    Opcion = int(input("Opcion: "))
    return Opcion





mis_Contactos = Agenda()
i = 0
while i == 0:
    Opcion = EntrUs()

    if Opcion == 1:
        IngresarValores(mis_Contactos)

    elif Opcion == 2:
        BuscarPorNombre(mis_Contactos)

    elif Opcion == 3:
        BuscarPorTelefono(mis_Contactos)

    elif Opcion == 4:
        BorrarPorNombre(mis_Contactos)

    elif Opcion == 5:
        BorrarPorNumero(mis_Contactos)