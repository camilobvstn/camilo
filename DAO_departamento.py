from Departamento import Departamento
import credenciales
import mysql.connector

class DAO_departamento:
    def __init__(self):
        pass

    def __conectar(self):
        self.__conexion = mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor = self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()

    def registrar_departamento(self,u:Departamento):
        self.__conectar()
        sql = "INSERT INTO departamento (nombre_departamento,id_area) VALUES (%s,%s)"
        values = (u.get_nombre_departamento(),u.get_id_area())
        self.__cursor.execute(sql,values)
        self.__cerrar()

    def modificar_departamento(self,u:Departamento):
        self.__conectar()
        sql = "UPDATE Departamento SET nombre_departamento=%s WHERE id_departamento= %s"
        values = (u.get_nombre_departamento(),u.get_id_departamento())
        self.__cursor.execute(sql,values)
        self.__cerrar()

    def buscar_id(self):
        self.__conectar()
        sql = "SELECT * FROM departamento"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        valor = 0
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Departamento(t[1],t[2],t[0])
                usuario = [t[0]]
            for c in usuario:
                valor = c
            return valor
        else:
            return None

    def mostrar_todo(self):
        self.__conectar()
        sql = "SELECT * FROM departamento"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Departamento(t[1],t[2],t[0])
                usuario.append(u)
            return usuario
        else:
            return None
        