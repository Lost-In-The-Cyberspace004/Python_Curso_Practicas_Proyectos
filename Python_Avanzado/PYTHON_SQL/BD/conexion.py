import mysql.connector
from mysql.connector import Error

#CREAMOS UNA CLASE DONDE CONECTARNOS A LA BASE DE DATOS
class DAO:



    #EN EL CONSTRUCTOR ESTABLECEMOS LA CONEXION
    def __init__(self):
        self.conexion = None





    #METODO DONDE NOS CONECTAREMOS
    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                passwordd = 'Losty_004',
                db = 'SistemaInventario'
            )
            return self.conexion
        except Error as ex:
            print("Error al intentar la conexion", ex)
            return None



    #CERRAR LA CONEXION PARA EVITAR CONSUMIR RECURSOS DE FONDO
    def cerrar(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()