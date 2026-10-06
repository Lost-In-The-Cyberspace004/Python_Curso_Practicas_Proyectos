class Producto:
    def __init__(self):
        self.__Codigo = ""
        self.__Nombre = ""
        self.__Precio = ""
        self.__Cantidad = ""

    def InsertarCodigo(self, codigo):
        self.__Codigo = codigo

    def InsertarNombre(self, nombre):
        self.__Nombre = nombre

    def InsertarPrecio(self, precio):
        self.__Precio = precio

    def InsertarCantidades(self, cantidad):
        self.__Cantidad = cantidad

    #Setters y getters
    def SetInsertarCodigo(self, codigo):
        self.__Codigo = codigo
    def GetInsertarCodigo(self):
        return self.__Codigo

    def SetInsertarNombre(self, nombre):
        self.__Nombre = nombre
    def GetInsertarNombre(self):
        return self.__Nombre

    def SetInsertarPrecio(self, precio):
        self.__Precio = precio
    def GetInsertarPrecio(self):
        return self.__Precio

    def SetInsertarCantidades(self, cantidades):
        self.__Cantidad = cantidades
    def GetInsertarCantidades(self):
        return self.__Cantidad





    #Para ver putisimas listas, convertimos a string su contenido
    def __str__(self):
        return f"Nombre: {self.__Nombre} | Código: {self.__Codigo} | Precio: {self.__Precio} | Cantidad: {self.__Cantidad}"






class Inventario:
    def __init__(self):
        super().__init__()
        self.__Inventario = []

    def AgregarAlInventario(self, items):
        self.__Inventario.append(items)

    def GetContenido(self):
        return self.__Inventario






    def Buscar(self, ItemValorInventario): 
        encontrado = False

        #LA LOGICA ES QUE DADO QUE RECIBIMOS UN OBJETO DE LA CLASE ANTERIOR, PODEMOS USAR LOS METODOS DE LA CLASE ANTERIOR
        for ObjetoContenedorDeInformacion in self.__Inventario:
            #DONDE PODEMOS USAR LOS METODOS GETTERS Y SETTERS PARA ASI OBTENER SUS VALORES, USARLOS, COMPARARLOS, OPERARLOS ETC...
            if ObjetoContenedorDeInformacion.GetInsertarNombre().lower() == ItemValorInventario.lower():
                print(ObjetoContenedorDeInformacion)
                encontrado = True
            else:
                print("Inexistente o no agregado")






    def VerLista(self):
        for Producto in self.__Inventario: #CUANDO CONVERTIMOS LA LISTA AL STRING PODEMOS RECORRERLA Y MOSTRARLA
            print(Producto)





    def Eliminar(self, ItemValorInventarioEliminar):
        encontrado = False
        for ObjetoContenedorDeInformacion in self.__Inventario:
            if ObjetoContenedorDeInformacion.GetInsertarNombre().lower() == ItemValorInventarioEliminar.lower():
                self.__Inventario.remove(ObjetoContenedorDeInformacion)
                encontrado = True
            else:
                print("Inexistente o no es posible eliminar")



    def ActualizarDatos(self, ActualizarDatos):
        encontrado = False
        for ObjetoContenedorDeInformacionDeLaLista in self.__Inventario:
            if ObjetoContenedorDeInformacionDeLaLista.GetInsertarNombre().lower() == ActualizarDatos.lower():
                encontrado = True

                Nombre = input("Nombre: ")
                Codigo = input("Codigo: ")
                Precio = input("Precio: ")
                Cantidad = input("Cantidad: ")

                ObjetoContenedorDeInformacionDeLaLista.SetInsertarCodigo(Codigo)
                ObjetoContenedorDeInformacionDeLaLista.SetInsertarNombre(Nombre)
                ObjetoContenedorDeInformacionDeLaLista.SetInsertarPrecio(Precio)
                ObjetoContenedorDeInformacionDeLaLista.SetInsertarCantidades(Cantidad)

            else:
                print("No encontrado o no existe, no se puede actualizar")

    
def agregar_Productos(Mi_Inventario_):
    DatosAAgregar = Producto()

    Nombre = input("Nombre: ")
    DatosAAgregar.SetInsertarNombre(Nombre)

    Cantidades = input("Cantidades: ")
    DatosAAgregar.SetInsertarCantidades(Cantidades)

    Codigo = input("Codigo: ")
    DatosAAgregar.SetInsertarCodigo(Codigo)

    Precio = input("Precio: ")
    DatosAAgregar.SetInsertarPrecio(Precio)





    Mi_Inventario_.AgregarAlInventario(DatosAAgregar) #RECUERDA: ESTAMOS PASANDO POR PARAMETROS EL OBJETO QUE SE CONECTA A LA CLASE QUE CONTIENE LOS METODOS DE ESA CLASE!
    #LO QUE SIGNIFICA QUE SE PUEDEN MANIPULAR DESDE LA OTRA CLASE





def Actualizar_Stock(Mi_Inventario_):
    ActualizacionDeDatos = input("Ingresa el nombre del elemento a actualizar: ")
    Mi_Inventario_.ActualizarDatos(ActualizacionDeDatos)

def Obtener_Total_Inventario(Mi_Inventario_):
    Mi_Inventario_.VerLista()

Mi_Inventario = Inventario()

i = 0
while i == 0:
    print("1-) Agregar productos \n2-) Actualizar Productos \n3-) Ver inventario \n4-) Buscar elemento \n5-) Eliminar elemento")
    Opc = input("opcion: ")
    if Opc == "1":
        agregar_Productos(Mi_Inventario)

    elif Opc == "2":
        Actualizar_Stock(Mi_Inventario)

    elif Opc == "3":
        Obtener_Total_Inventario(Mi_Inventario)

    elif Opc == "4":
        BuscarElemento = input("Nombre del elemento a buscar: ")
        Mi_Inventario.Buscar(BuscarElemento)

    elif Opc == '5':
        EliminarElemento = input("Eliminar elemento: ")
        Mi_Inventario.Eliminar(EliminarElemento)