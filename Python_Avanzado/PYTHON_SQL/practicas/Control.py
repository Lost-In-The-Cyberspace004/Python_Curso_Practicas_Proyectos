from Conexion import DAO
from mysql.connector import Error

class ControlDeSistemas:
    def __init__(self):
        self.dao = DAO()




    #METODO PARA VER EL CONTENIDO DE LA BASE DE DATOS
    def VerContenido(self):
        Conectar = self.dao.Conectar()
        if not Conectar:
            return []

        sql = "select personID, Producto, Precio, Cantidad from Inventario"
        ProductosLista = []

        try:
            cursor = Conectar.cursor()
            cursor.execute(sql)
            ProductosLista = cursor.fetchall()

        except Error as Ex:
            print("Error presentado: ", Ex)

        finally:
            self.dao.Cerrar()

        return ProductosLista





    #METODO PARA INSERTAR LOS VALORES
    def InsertarContenido(self, Producto, precio, cantidad):
        Conectar = self.dao.Conectar()
        
        if not Conectar:
            return

        #INSERTAMOS LOS VALORES
        sql = "insert into Inventario(Producto, Precio, Cantidad) values(%s, %s, %s)"
        valores = (Producto, precio, cantidad)

        try:
            Cursor = Conectar.cursor()
            Cursor.execute(sql, valores)
            Conectar.commit()
            print("Registrado correctamente")

        except Error as Ex:
            print("Error presentado", Ex)

        finally:
            self.dao.Cerrar()





    #METODO DONDE ELIMINAREMOS EL CONTENIDO
    def EliminarContenido(self, ID):
        Conectar = self.dao.Conectar()
        
        if not Conectar:
            return

        sql = "delete from Inventario where personID = %s"
        valores = (ID,) #RECUERDA: PONEMOS LA COMA PARA QUE SEA IDENTIFICADO COMO UNA TUPLA Y PODAMOS ACCEDER A ESE DATO PARA ELIMINARLO O CAMBIARLO

        try:
            Cursor = Conectar.cursor()
            Cursor.execute(sql, valores)
            Conectar.commit()

            if Cursor.rowcount > 0:
                print("Eliminado correctamente")
            else:
                print("No se ha encontrado")
        
        except Error as Ex:
            print("Error presentado: ", Ex)

        finally:
            self.dao.Cerrar()





    #METODO DONDE BUSCAREMOS LOS VALORES O FILTRARLOS
    def BuscarValores(self):

        Conectar = self.dao.Conectar()
        if not Conectar:
            return []

        #OPCIONES PARA BUSCAR
        print("\n1-) Buscar por ID \n2-) Buscar por nombre del producto\n")
        Opcion = int(input("Opcion: "))

        if Opcion == 1:

            ID = int(input("ID a buscar: "))

            sql = "select personID, Producto, Precio, Cantidad from Inventario where personID = %s"
            busqueda = []

            #BUSCAR POR ID
            try:
                Cursor = Conectar.cursor()
                Cursor.execute(sql, (ID,)) #ESPECIFICAMOS QUE EL ELEMENTO SE ASIGNE AL %s YA QUE AHI ESTA EL VALOR A BUSCAR
                busqueda = Cursor.fetchall()

            except Error as Ex:
                print("Error presentado", Ex)

            finally:
                self.dao.Cerrar()

            return busqueda

        elif Opcion == 2:

            Producto = input("Nombre del producto: ")

            sql = "select personID, Producto, Precio, Cantidad from Inventario where Producto = %s"
            busquedaNombre = []

            #BUSCAR POR NOMBRE
            try:
                Cursor = Conectar.cursor()
                Cursor.execute(sql, (Producto,))
                busquedaNombre = Cursor.fetchall()

            except Error as Ex:
                print("Error presentado: ", Ex)

            finally:
                self.dao.Cerrar()

            return busquedaNombre

        else:
            print("Opcion inexistente")




    #METODO PARA ACTUALIZAR VALORES DENTRO DE LA BASE DE DATOS
    def EditarValores(self, id,  Producto, Precio, Cantidad):
        Conectar = self.dao.Conectar()
        if not Conectar:
            return
            
        sql = "update Inventario set Producto = %s, Precio = %s, Cantidad = %s where personID = %s"
        valores = (Producto, Precio, Cantidad, id)

        try:
            Cursor = Conectar.cursor()
            Cursor.execute(sql, valores)
            Conectar.commit()

            if Cursor.rowcount > 0:
                print("Producto actualizado con exito")
            else:
                print("No existe el producto")

        except Error as Ex:
            print("Error presentado: ", Ex)

        finally:
            self.dao.Cerrar()