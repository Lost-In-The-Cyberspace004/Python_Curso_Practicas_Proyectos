import mysql.connector 
from mysql.connector import Error 

class DAO:

    def __init__(self):
        self.Conexion = None





    #CONEXION
    def Conectar(self):
        try:
            self.Conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'Losty_004',
                db = 'SistemaGestorDeInventarios'
            )
            return self.Conexion
        
        except Error as Ex:
            print("Error presentado: ", Ex)
            return None




    #CERRAR LA CONEXION PARA EVITAR CONSUMIR RECURSOS DE FONDO
    def Cerrar(self):
        if self.Conexion and self.Conexion.is_connected():
            self.Conexion.close()