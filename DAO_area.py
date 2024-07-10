from Area import Area
import credenciales
import mysql.connector

class DAO_area:
    def __init__(self):
        pass

    def __conectar(self):
        self.__conexion = mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor = self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit() #cambios
        self.__conexion.close()

    def registrar_area(self,u:Area):
        self.__conectar()
        sql = "INSERT INTO area (nombre_area) VALUES (%s)"
        values = (u.get_nombre_area(),)
        self.__cursor.execute(sql,values)
        self.__cerrar()

    def modificar_area(self,u:Area):
        self.__conectar()
        sql = "UPDATE area SET nombre_area=%s WHERE id_area= %s"
        values = (u.get_nombre_area(),u.get_id_area())
        self.__cursor.execute(sql,values)
        self.__cerrar()

    def buscar_id(self):
        self.__conectar()
        sql = "SELECT * FROM area"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        valor = 0
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Area(t[1],t[0])
                usuario = [t[0]]
            for c in usuario:
                valor = c
            return valor
        else:
            return None

    def mostrar_todo(self):
        self.__conectar()
        sql = "SELECT * FROM area"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Area(t[1],t[0])
                usuario.append(u)
            return usuario
        else:
            return None