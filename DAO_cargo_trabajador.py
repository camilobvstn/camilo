from Cargo_trabajador import Cargo_trabajador
import credenciales
import mysql.connector

class DAO_cargo_trabajador:
    def __init__(self):
        pass

    def __conectar(self):
        self.__conexion=mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor=self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit() #cambios
        self.__conexion.close()

    def registrar_Cargo_trabajador(self,u:Cargo_trabajador):
        self.__conectar()
        sql = "INSERT INTO Cargo_trabajador (cargo_trabajador,fecha_ingreso) VALUES (%s,%s)"
        values = (u.get_cargo_trabajador(),u.get_fecha_ingreso())
        self.__cursor.execute(sql,values)
        self.__cerrar()

    def modificar_Cargo_trabajador(self,u:Cargo_trabajador):
        self.__conectar()
        sql = "UPDATE Cargo_trabajador SET cargo_trabajador=%s WHERE id_Cargo= %s"
        values = (u.get_cargo_trabajador(),u.get_id_cargo())
        self.__cursor.execute(sql,values)
        self.__cerrar()

    def buscar_cargo(self,rut):
        self.__conectar()
        sql = "SELECT ct.cargo_trabajador FROM cargo_trabajador ct JOIN usuario u ON ct.id_cargo_trabajador = u.id_cargo_trabajador WHERE u.rut = %s;"
        values = (rut,)
        self.__cursor.execute(sql,values)
        tupla = self.__cursor.fetchone()
        cargo = ""
        for r in tupla:
            cargo = r
        return r

    def buscar_id(self):
        self.__conectar()
        sql = "SELECT * FROM cargo_trabajador"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        valor = 0
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Cargo_trabajador(t[1],t[2],t[0])
                usuario = [t[0]]
            for c in usuario:
                valor = c
            return valor
        else:
            return None

    def mostrar_todo(self):
        self.__conectar()
        sql = "SELECT * FROM cargo_trabajador"
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchall()
        self.__cerrar()
        usuario = []
        if tupla != []:
            for t in tupla:
                u = Cargo_trabajador(t[1],t[2],t[0])
                usuario.append(u)
            return usuario
        else:
            return None
