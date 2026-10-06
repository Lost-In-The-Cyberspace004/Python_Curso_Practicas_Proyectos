#CRUD

from conexion import DAO #LLAMAMOS LA CLASE DEL MODULO CONEXION.PY
from mysql.connector import Error

class ProductoDAO:
    def __init__(self):
        self.dao = DAO()





    #C -> CREATE
    def crear(self, nombre, precio, stock):
        conexion = self.dao.conectar()
        if not conexion:
            return

        #EL CODIGO SQL QUE SE EJECUTARA CORRECTAMENTE EN EL CODIGO PYTHON
        sql = "insert into productos(nombre, precio, stock) values(%s, %s, %s)"
        valores = (nombre, precio, stock)

        try:
            cursor = conexion.cursor()
            cursor.execute(sql, valores)
            conexion.commit()
            print("registrado correctamente")

        except Error as ex:
            print("Error presentado: ", ex)
        finally:
            self.dao.cerrar()





    #R -> READ
    def leer(self):
        conexion = self.dao.conectar()
        if not conexion:
            return []

        sql = "select id, nombre, precio, stock, from productos"
        productos = []

        try:
            cursor = conexion.cursor()
            cursor.execute(sql)
            productos = cursor.fetchall() #USAMOS FETCHALL PARA QUE RETORNE UNA TUPLA CON TODOS LOS VALORES
        except Error as ex:
            print("Error al consultar: ", ex)
        finally:
            self.dao.cerrar()

        return productos #RETORNAMOS LA TUPLA PARA MOSTRARLA EN PANTALLA





    #U -> Update
    def Actualizar(self, id_producto, nombre, precio, stock):
        conexion = self.dao.conectar()
        if not conexion:
            return

        sql = "update productos set nombre = %s, precio = %s, stock = %s, stock = %s where id = %s"
        valores = (nombre, precio, stock, id_producto)

        try:
            cursor = conexion.cursor()
            cursor.execute(sql, valores)
            conexion.commit()

            if cursor.rowcount > 0:
                print("Producto actualizado")
            else:
                print("No existe el producto")
        
        except Error as ex:
            print("Error presentado: ", ex)
        finally:
            self.dao.cerrar()





    #B/F -> Buscar/Filtrar
    def filtrarBuscar(self, id):
        conexion = self.dao.conectar()
        if not conexion: 
            return []

        sql = "select nombre, precio from productos where id = %s"
        busqueda = []

        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id,)) #LE ESPECIFICAMOS QUE EL VALOR ENVIADO POR PARAMETROS SE ASIGNE AL %s
            busqueda = cursor.fetchall()

        except Error as ex:
            print("Error presentado", ex)
        
        finally:
            self.dao.cerrar()

        return busqueda





    #D -> Delete
    def eliminar(self, id_producto):
        conexion = self.dao.conectar()
        if not conexion:
            return

        sql = "delete from productos where id = %s"
        valores = (id_producto,) #LA COMA ES OBLIGATORIA PARA DEFINIR UNA TUPLA DE 1 ELEMENTO

        try:
            cursor = conexion.cursor()
            cursor.execute(sql, valores)
            conexion.commit()

            if cursor.rowncount > 0:
                print("Eliminado correctamente")
            else:
                print("No se encontro el producto")

        except Error as ex:
            print("Error presentado: ", ex)
        
        finally:
            self.dao.cerrar()
